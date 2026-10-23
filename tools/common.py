"""Load and validate the knowledge system. No generated file is a content source.

Layout (paths come from project.json):
  knowledge/puzzles/<PZ-xxxx>/puzzle.json      statement, difficulty, analysis
  knowledge/puzzles/<PZ-xxxx>/solution.json    answer, outline, teaching notes
  knowledge/puzzles/<PZ-xxxx>/review.json      review status
  knowledge/puzzles/<PZ-xxxx>/provenance.json  sources and authorship
  editions/<edition>/edition.json              selection, sections, layout
  publications/<output_name>-{student,instructor}.pdf   released PDFs
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = "project.json"
PUZZLE_ID = re.compile(r"PZ-\d{4}")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
PUZZLE_FILES = ("puzzle.json", "solution.json", "review.json", "provenance.json")
SOLUTION_SCOPES = {"answer-only", "answer-and-outline", "full-proof"}
SOLUTION_STATUSES = {"draft", "reviewed"}
ANALYSIS_STATUSES = {"not-assessed", "suggested", "reviewed"}


def project_path(root, relative):
    root = Path(root).resolve()
    target = (root / relative).resolve()
    if not target.is_relative_to(root):
        raise ValueError(f"Path leaves project: {relative}")
    return target


def read_json(file):
    return json.loads(Path(file).read_text(encoding="utf-8"))


def sha256(file):
    return hashlib.sha256(Path(file).read_bytes()).hexdigest()


def text_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_json(file, value):
    file = Path(file)
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def unique_index(records, field, label):
    result = {}
    for record in records:
        key = record[field]
        if key in result:
            raise ValueError(f"Duplicate {label}: {key}")
        result[key] = record
    return result


def document(file, version=1):
    value = read_json(file)
    if value.get("schema_version") != version:
        raise ValueError(f"Unsupported schema version: {file}")
    return value


def body(file):
    return {k: v for k, v in document(file).items() if k != "schema_version"}


def stars(puzzle):
    return puzzle["difficulty"]["stars"]


def puzzle_dirs(root, config):
    base = project_path(root, config["puzzles"])
    folders = sorted(p for p in base.iterdir() if p.is_dir())
    for folder in folders:
        if not PUZZLE_ID.fullmatch(folder.name):
            raise ValueError(f"Unexpected folder in puzzle bank: {folder.name}")
        missing = [name for name in PUZZLE_FILES if not (folder / name).is_file()]
        if missing:
            raise ValueError(f"{folder.name}: missing {', '.join(missing)}")
    return folders


def load_config(root=ROOT):
    return document(Path(root).resolve() / CONFIG_FILE, version=2)


def load_system(root=ROOT, edition_id=None):
    root = Path(root).resolve()
    config = load_config(root)
    edition_id = edition_id or config["default_edition"]
    if not SLUG.fullmatch(edition_id):
        raise ValueError("Invalid edition ID")
    edition_dir = project_path(root, config["editions"]) / edition_id
    puzzles, reviews, provenance = [], [], []
    for folder in puzzle_dirs(root, config):
        puzzle = body(folder / "puzzle.json")
        if puzzle.get("id") != folder.name:
            raise ValueError(f"Puzzle ID does not match its folder: {folder.name}")
        # Derived, never stored: the folder is the single source of location.
        puzzle["solution_path"] = (folder / "solution.json").relative_to(root).as_posix()
        puzzles.append(puzzle)
        reviews.append(body(folder / "review.json"))
        provenance.append(body(folder / "provenance.json"))
    return {
        "root": root, "config": config,
        "puzzles": puzzles, "reviews": reviews, "provenance": provenance,
        "sources": document(project_path(root, config["sources"]))["sources"],
        "taxonomy": document(project_path(root, config["taxonomy"])),
        "cards": [document(p) for p in sorted(project_path(root, config["cards"]).glob("*.json"))],
        "edition": document(edition_dir / "edition.json"),
        "edition_dir": edition_dir,
    }


def solution_for(system, puzzle):
    value = read_json(project_path(system["root"], puzzle["solution_path"]))
    if value.get("schema_version") != 1:
        raise ValueError(f"Unsupported solution schema: {puzzle['id']}")
    return value


def output_pdfs(system):
    """Released PDF paths for the loaded edition."""
    folder = project_path(system["root"], system["config"]["publications"])
    name = system["edition"]["output_name"]
    return {kind: folder / f"{name}-{kind}.pdf" for kind in ("student", "instructor")}


def check_figure(system, figure_id):
    root, config = system["root"], system["config"]
    if not re.fullmatch(r"[A-Za-z0-9-]+", figure_id):
        raise ValueError(f"Invalid figure ID: {figure_id}")
    figure = project_path(root, f"{config['assets']}/figures/{figure_id}_tikz.tex")
    text = figure.read_text(encoding="utf-8")
    for image in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", text):
        if not project_path(root, f"{config['assets']}/figures/{image}").is_file():
            raise ValueError(f"Missing raster asset: {image}")


def edition_rows(system):
    """Adapter for edition layouts; order/section belongs only to the edition."""
    bank = unique_index(system["puzzles"], "id", "puzzle ID")
    rows = []
    for section in system["edition"]["sections"]:
        for pid in section["puzzle_ids"]:
            puzzle = bank[pid]
            solution = solution_for(system, puzzle)
            rows.append({"id": pid, "section": section["id"], "title": puzzle["title"],
                         "difficulty": stars(puzzle), "body": puzzle["statement"],
                         "fig": puzzle["figure_id"], "instance": puzzle.get("instance"),
                         "figure_model": puzzle.get("figure_model"),
                         "key": solution["answer"], "route": solution["outline"],
                         "note": solution["teaching_notes"],
                         "pedagogy": solution.get("pedagogical_notes", ""),
                         "complexity": solution.get("complexity")})
    return rows


def reviewed_by_someone(review):
    return bool(review["reviewer"] and review["reviewed_on"])


def validate_puzzle(system, puzzle, review, provenance, sources, concepts, techniques, cognitive, roles):
    pid = puzzle["id"]
    if not puzzle["title"].strip() or not puzzle["statement"].strip():
        raise ValueError(f"Empty puzzle: {pid}")
    if type(stars(puzzle)) is not int or not 1 <= stars(puzzle) <= 5:
        raise ValueError(f"Invalid stars: {pid}")
    if "{{DATA}}" in puzzle["statement"] and not puzzle.get("instance"):
        raise ValueError(f"Missing instance data: {pid}")
    instance = puzzle.get("instance") or {}
    if instance.get("columns"):
        records = instance.get("records", [])
        if not records or any(column["field"] not in row for column in instance["columns"] for row in records):
            raise ValueError(f"Incomplete instance table: {pid}")
    if review["puzzle_id"] != pid or provenance["puzzle_id"] != pid:
        raise ValueError(f"Review/provenance link mismatch: {pid}")

    solution = solution_for(system, puzzle)
    if solution["puzzle_id"] != pid:
        raise ValueError(f"Wrong solution link: {pid}")
    if solution["scope"] not in SOLUTION_SCOPES:
        raise ValueError(f"Unknown solution scope: {pid}")
    if solution["scope"] == "full-proof" and not solution["proof"]:
        raise ValueError(f"Full proof is missing: {pid}")
    if solution["status"] not in SOLUTION_STATUSES:
        raise ValueError(f"Unknown solution review status: {pid}")
    if solution["status"] == "reviewed" and not reviewed_by_someone(review):
        raise ValueError(f"Reviewed solution has no reviewer/date: {pid}")
    evidence = solution.get("evidence")
    if evidence is not None:
        source = sources.get(evidence.get("source_id"))
        if source is None:
            raise ValueError(f"Unknown evidence source: {pid}")
        data = read_json(project_path(system["root"], source["path"]))
        if type(evidence.get("record_index")) is not int or not 0 <= evidence["record_index"] < len(data):
            raise ValueError(f"Invalid source record locator: {pid}")

    analysis = puzzle["analysis"]
    if analysis["status"] not in ANALYSIS_STATUSES:
        raise ValueError(f"Unknown analysis status: {pid}")
    for field, allowed in (("concept_ids", concepts), ("prerequisite_ids", concepts), ("technique_ids", techniques)):
        if len(analysis[field]) != len(set(analysis[field])) or not set(analysis[field]).issubset(allowed):
            raise ValueError(f"Unknown/duplicate {field}: {pid}")
    for role_field, label_field in (("concept_roles", "concept_ids"), ("technique_roles", "technique_ids")):
        assigned = analysis.get(role_field, {})
        if (not isinstance(assigned, dict) or not set(assigned).issubset(analysis[label_field])
                or not set(assigned.values()).issubset(roles)):
            raise ValueError(f"Invalid {role_field} assignment: {pid}")
    if analysis["cognitive_level"] is not None and analysis["cognitive_level"] not in cognitive:
        raise ValueError(f"Unknown cognitive level: {pid}")
    if analysis["status"] != "not-assessed" and not analysis["rationale"]:
        raise ValueError(f"Missing analysis rationale: {pid}")
    if analysis["status"] == "reviewed" and not reviewed_by_someone(review):
        raise ValueError(f"Reviewed analysis has no reviewer/date: {pid}")
    if puzzle["figure_id"]:
        check_figure(system, puzzle["figure_id"])


def validate_edition(system, bank):
    root, config, edition = system["root"], system["config"], system["edition"]
    if edition["id"] != system["edition_dir"].name:
        raise ValueError("Edition ID does not match directory")
    if not SLUG.fullmatch(edition.get("output_name", "")):
        raise ValueError("Edition output_name must be kebab-case")
    unique_index(edition["sections"], "id", "section ID")
    selection = [pid for section in edition["sections"] for pid in section["puzzle_ids"]]
    if len(selection) != len(set(selection)) or not set(selection).issubset(bank):
        raise ValueError("Edition has duplicate or unknown puzzle IDs")
    if len(selection) != edition["expected_count"]:
        raise ValueError("Edition count mismatch")
    if edition.get("pedagogy", {}).get("difficulty_order") == "nondecreasing-within-section":
        for section in edition["sections"]:
            values = [stars(bank[pid]) for pid in section["puzzle_ids"]]
            if values != sorted(values):
                raise ValueError(f"Section difficulty order is not nondecreasing: {section['id']}")
    if not (system["edition_dir"] / edition["renderer"]).is_file():
        raise ValueError("Missing edition renderer")
    layout = edition["layout"]
    for fid in set(layout["side_figure_ids"] + layout["student_hidden_figure_ids"] + [layout["cover_figure_id"]]):
        check_figure(system, fid)
    for font in layout["font_files"]:
        if not project_path(root, f"{config['assets']}/fonts/{font}").is_file():
            raise ValueError(f"Missing font asset: {font}")
    if __package__:
        from .artwork import validate_layout
    else:
        from artwork import validate_layout
    validate_layout(root, config["assets"], edition, system["puzzles"])
    return selection


def validate_cards(system, bank, concepts, techniques):
    root = system["root"]
    for card in system["cards"]:
        if card["status"] not in {"draft", "reviewed"}:
            raise ValueError(f"Unknown knowledge card status: {card['id']}")
        for field, allowed in (("concept_ids", concepts), ("technique_ids", techniques)):
            if not set(card[field]).issubset(allowed):
                raise ValueError(f"Unknown card {field}: {card['id']}")
        if not all(card[field] for field in ("claim", "conditions", "when_to_use", "reasoning", "pitfalls", "evidence")):
            raise ValueError(f"Incomplete knowledge card: {card['id']}")
        for evidence in card["evidence"]:
            puzzle = bank[evidence["puzzle_id"]]
            if (evidence["statement_sha256"] != text_hash(puzzle["statement"])
                    or evidence["solution_sha256"] != sha256(project_path(root, puzzle["solution_path"]))):
                raise ValueError(f"Stale knowledge evidence: {card['id']} / {puzzle['id']}")
        if card["status"] == "reviewed" and not (card.get("reviewer") and card.get("reviewed_on")):
            raise ValueError(f"Reviewed card has no reviewer/date: {card['id']}")


def validate(system):
    """Integrity only: unreviewed mathematics is never promoted by this check."""
    root = system["root"]
    bank = unique_index(system["puzzles"], "id", "puzzle ID")
    sources = unique_index(system["sources"], "id", "source ID")
    reviews = unique_index(system["reviews"], "puzzle_id", "review")
    provenance = unique_index(system["provenance"], "puzzle_id", "provenance")
    unique_index(system["cards"], "id", "knowledge card ID")
    for source in sources.values():
        if sha256(project_path(root, source["path"])) != source["sha256"]:
            raise ValueError(f"Source checksum changed: {source['id']}")
    taxonomy = system["taxonomy"]
    concepts = unique_index(taxonomy["concepts"], "id", "concept ID")
    techniques = unique_index(taxonomy["techniques"], "id", "technique ID")
    cognitive = unique_index(taxonomy["cognitive_levels"], "id", "cognitive level")
    roles = {role["id"] for role in taxonomy.get("assignment_roles", [])}
    for pid, puzzle in bank.items():
        validate_puzzle(system, puzzle, reviews[pid], provenance[pid], sources, concepts, techniques, cognitive, roles)
    selection = validate_edition(system, bank)
    validate_cards(system, bank, concepts, techniques)
    return {"puzzles": len(bank), "selected": len(selection), "cards": len(system["cards"]),
            "figures": len({bank[pid]["figure_id"] for pid in selection if bank[pid]["figure_id"]}),
            "reviewed_solutions": sum(solution_for(system, p)["status"] == "reviewed" for p in bank.values())}
