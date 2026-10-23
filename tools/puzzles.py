"""Validate, search, scaffold and build the Algorithmic Puzzles knowledge system."""
import argparse
import datetime
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

if __package__:
    from .common import (CONFIG_FILE, PUZZLE_FILES, ROOT, edition_rows, load_config, load_system, output_pdfs,
                         project_path, puzzle_dirs, read_json, sha256, solution_for, stars, validate, write_json)
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from common import (CONFIG_FILE, PUZZLE_FILES, ROOT, edition_rows, load_config, load_system, output_pdfs,
                        project_path, puzzle_dirs, read_json, sha256, solution_for, stars, validate, write_json)

KINDS = ("student", "instructor")


def folded(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text.lower().replace("đ", "d")) if not unicodedata.combining(c))


# ----------------------------------------------------------------- rendering
def input_hashes(system):
    root, config = system["root"], system["config"]
    files = {root / CONFIG_FILE, system["edition_dir"] / "edition.json",
             system["edition_dir"] / system["edition"]["renderer"]}
    files.update(project_path(root, config[key]) for key in ("sources", "taxonomy"))
    files.update(folder / name for folder in puzzle_dirs(root, config) for name in PUZZLE_FILES)
    files.update(project_path(root, s["path"]) for s in system["sources"])
    files.update(project_path(root, config["cards"]).glob("*.json"))
    files.update(p for p in project_path(root, config["assets"]).rglob("*") if p.is_file())
    files.update(project_path(root, path) for path in system["edition"].get("renderer_dependencies", []))
    return {p.relative_to(root).as_posix(): sha256(p) for p in sorted(files)}


def check_rendered(system, tex_dir):
    rows = edition_rows(system)
    student = (tex_dir / "student.tex").read_text(encoding="utf-8")
    if student.count(r"\puzzhead{") != len(rows):
        raise ValueError("Rendered student puzzle count mismatch")
    visible = re.sub(r"\\(?:input\{[^}]+\}|includegraphics(?:\[[^\]]*\])?\{[^}]+\})", "", student)
    if "{{DATA}}" in student:
        raise ValueError("Instance data placeholder was not rendered")
    if re.search(r"PZ-\d{4}", visible):
        raise ValueError("Bank IDs leaked into student text")
    for name in KINDS:
        text = (tex_dir / (name + ".tex")).read_text(encoding="utf-8")
        if name == "instructor" and re.search(r"PZ-\d{4}|bài bổ sung|Ấn bản", text):
            raise ValueError("Editorial metadata leaked into instructor document")
        for include in re.findall(r"\\input\{([^}]+)\}", text):
            target = (tex_dir / include).resolve()
            if not target.is_relative_to(system["root"]) or not target.is_file():
                raise ValueError(f"Unresolved rendered input: {include}")
    return len(rows)


def render_edition(system):
    """Write build/<edition>/tex/*.tex. Never touches knowledge, sources or assets."""
    validate(system)
    root, edition, config = system["root"], system["edition"], system["config"]
    before = input_hashes(system)
    output = project_path(root, config["build"]) / edition["id"]
    tex_dir = output / "tex"
    spec = importlib.util.spec_from_file_location("edition_renderer", system["edition_dir"] / edition["renderer"])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = edition_rows(system)
    module.render(rows, edition, tex_dir, project_path(root, config["assets"]))
    check_rendered(system, tex_dir)
    if input_hashes(system) != before:
        raise ValueError("Rendering changed an editorial input")
    write_json(output / "data" / "edition-rows.json", rows)
    write_json(output / "manifest.json", {
        "schema_version": 1, "edition_id": edition["id"], "status": "rendered", "inputs": before,
        "selection": [{"number": i, "puzzle_id": row["id"], "section": row["section"]} for i, row in enumerate(rows, 1)],
        "outputs": {f"tex/{name}.tex": sha256(tex_dir / (name + ".tex")) for name in KINDS}})
    return output


def find_program(program):
    """Also read the updated user PATH when the IDE predates installation."""
    executable = shutil.which(program)
    if executable is None and os.name == "nt":
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
                user_path = winreg.QueryValueEx(key, "Path")[0]
            executable = shutil.which(program, path=os.path.expandvars(user_path))
        except (FileNotFoundError, OSError):
            pass
    return executable


def compile_edition(output, release=None, compiler="xelatex"):
    """Compile build/<edition>/tex into PDFs; on full success copy them to `release` paths."""
    executable = find_program(compiler)
    if executable is None:
        raise ValueError("XeLaTeX is unavailable. Run python tools/setup_tex.py, or use build --render-only.")
    output = Path(output).resolve()
    logs = output / "logs"
    logs.mkdir(exist_ok=True)
    version = subprocess.run([executable, "--version"], check=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, encoding="utf-8", errors="replace").stdout
    (logs / "xelatex-version.txt").write_text(version, encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix=".latex-", dir=output) as scratch:
        scratch = Path(scratch).resolve()
        for name in KINDS:
            print(f"Compiling {name}.pdf with XeLaTeX...", flush=True)
            for _ in range(2):
                try:
                    subprocess.run([executable, "-interaction=nonstopmode", "-halt-on-error", "-recorder",
                                    f"-output-directory={scratch.as_posix()}", name + ".tex"], cwd=output / "tex",
                                   check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   encoding="utf-8", errors="replace")
                finally:
                    for extension in (".log", ".fls"):
                        diagnostic = scratch / (name + extension)
                        if diagnostic.exists():
                            shutil.copy2(diagnostic, logs / diagnostic.name)
            if not (scratch / (name + ".pdf")).is_file():
                raise ValueError(f"Compiler produced no fresh PDF: {name}")
            final_log = (scratch / (name + ".log")).read_text(encoding="utf-8", errors="replace")
            defects = re.findall(r"(?m)^.*(?:Overfull \\[hv]box|Missing character:|Package wrapfig Warning:).*$", final_log)
            if defects:
                raise ValueError(f"{name}: layout check failed; see logs/{name}.log: " + "; ".join(defects[:3]))
        pdf_dir = output / "pdf"
        pdf_dir.mkdir(exist_ok=True)
        for name in KINDS:
            shutil.copy2(scratch / (name + ".pdf"), pdf_dir / (name + ".pdf"))
    manifest = read_json(output / "manifest.json")
    manifest["status"] = "compiled"
    manifest["compiler"] = {"engine": "XeLaTeX", "version_output": version.strip()}
    manifest["outputs"].update({f"pdf/{name}.pdf": sha256(pdf_dir / (name + ".pdf")) for name in KINDS})
    if release:
        for name, target in release.items():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(pdf_dir / (name + ".pdf"), target)
        manifest["released"] = {name: target.name for name, target in release.items()}
    write_json(output / "manifest.json", manifest)


# ----------------------------------------------------------------- retrieval
def search(system, args):
    labels = {item["id"]: item["label"] for key in ("concepts", "techniques") for item in system["taxonomy"][key]}
    results = []
    for puzzle in system["puzzles"]:
        analysis, solution = puzzle["analysis"], solution_for(system, puzzle)
        if args.concept and args.concept not in analysis["concept_ids"]:
            continue
        if args.technique and args.technique not in analysis["technique_ids"]:
            continue
        if args.difficulty and args.difficulty != stars(puzzle):
            continue
        if args.analysis_status and args.analysis_status != analysis["status"]:
            continue
        if args.solution_status and args.solution_status != solution["status"]:
            continue
        haystack = folded(" ".join([puzzle["id"], puzzle["title"], puzzle["statement"], *puzzle.get("aliases", []),
                                    solution["outline"], *(labels[t] for t in analysis["concept_ids"] + analysis["technique_ids"])]))
        if folded(args.query).strip() in haystack:
            results.append({"id": puzzle["id"], "title": puzzle["title"], "stars": stars(puzzle),
                            "analysis_status": analysis["status"], "solution_status": solution["status"],
                            "concept_ids": analysis["concept_ids"], "technique_ids": analysis["technique_ids"]})
    return results[:args.limit]


def render_index(system):
    """Markdown catalogue of the whole bank, for browsing on GitHub."""
    labels = {item["id"]: item["label"] for item in system["taxonomy"]["concepts"]}
    placed = {row["id"]: (i, row["section"]) for i, row in enumerate(edition_rows(system), 1)}
    edition = system["edition"]
    lines = ["# Mục lục ngân hàng câu đố", "",
             "> File sinh tự động bởi `python tools/puzzles.py index`. Không sửa tay.", "",
             f"Tổng số: **{len(system['puzzles'])}** bài. Cột *Sách* là vị trí trong ấn phẩm mặc định "
             f"`{edition['id']}` ({edition['title']}); để trống nghĩa là bài chưa được chọn.", "",
             "| ID | Tên | ★ | Khái niệm | Lời giải | Sách |", "|---|---|:-:|---|---|---|"]
    for puzzle in sorted(system["puzzles"], key=lambda p: p["id"]):
        pid = puzzle["id"]
        concepts = ", ".join(labels[c] for c in puzzle["analysis"]["concept_ids"])
        where = f"{placed[pid][0]} (P{placed[pid][1]})" if pid in placed else ""
        title = puzzle["title"].replace("|", "\\|")
        lines.append(f"| [{pid}]({pid}/puzzle.json) | {title} | {stars(puzzle)} | {concepts} | "
                     f"{solution_for(system, puzzle)['status']} | {where} |")
    return "\n".join(lines) + "\n"


def index_path(system):
    return project_path(system["root"], system["config"]["puzzles"]) / "INDEX.md"


# ------------------------------------------------------------------ authoring
def next_puzzle_id(root=ROOT):
    used = [int(folder.name[3:]) for folder in puzzle_dirs(Path(root).resolve(), load_config(root))]
    return f"PZ-{max(used, default=0) + 1:04d}"


def scaffold_puzzle(title, author=None, root=ROOT):
    """Create knowledge/puzzles/<next ID>/ with the four records in draft state."""
    root = Path(root).resolve()
    if not title.strip():
        raise ValueError("Title must not be empty")
    pid = next_puzzle_id(root)
    folder = project_path(root, load_config(root)["puzzles"]) / pid
    folder.mkdir()
    today = datetime.date.today().isoformat()
    write_json(folder / "puzzle.json", {
        "schema_version": 1, "id": pid, "title": title.strip(),
        "statement": "TODO: bối cảnh, dữ kiện, luật và mục tiêu (không gợi ý phương pháp, xem docs/editorial-style.md).",
        "aliases": [], "figure_id": None,
        "difficulty": {"stars": 3, "status": "proposed", "basis": "knowledge/difficulty-rubric.md",
                       "target_population": "", "rationale": "", "assessed_on": today},
        "analysis": {"status": "not-assessed", "concept_ids": [], "technique_ids": [], "prerequisite_ids": [],
                     "cognitive_level": None, "rationale": ""},
    })
    write_json(folder / "solution.json", {
        "schema_version": 1, "puzzle_id": pid, "status": "draft", "scope": "answer-and-outline",
        "answer": "TODO", "outline": "TODO", "teaching_notes": "", "pedagogical_notes": "",
        "proof": None, "complexity": None, "optimality": None, "evidence": None,
    })
    write_json(folder / "review.json", {
        "schema_version": 1, "puzzle_id": pid, "statement": "draft", "solution": "draft", "taxonomy": "not-assessed",
        "figure": "none", "reviewer": None, "reviewed_on": None, "notes": [],
    })
    write_json(folder / "provenance.json", {
        "schema_version": 1, "puzzle_id": pid, "author": author, "created_on": today,
        "catalog_headings": [], "external_source_status": "not-recorded", "external_sources": [],
    })
    return folder


# ------------------------------------------------------------------------ CLI
def main(argv=None):
    # PowerShell pipes may default to a legacy Windows code page.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "stats", "render", "build", "search", "show", "index", "new"):
        child = sub.add_parser(command)
        child.add_argument("--edition", default=None, help="edition ID under editions/ (default from project.json)")
        if command == "build":
            child.add_argument("--render-only", action="store_true")
            child.add_argument("--no-release", action="store_true", help="keep PDFs in build/ only")
        if command == "index":
            child.add_argument("--check", action="store_true", help="fail if INDEX.md is stale instead of writing it")
        if command == "new":
            child.add_argument("title")
            child.add_argument("--author", default=None)
        if command == "search":
            child.add_argument("query", nargs="?", default="")
            child.add_argument("--concept")
            child.add_argument("--technique")
            child.add_argument("--difficulty", type=int, choices=range(1, 6))
            child.add_argument("--analysis-status", choices=("not-assessed", "suggested", "reviewed"))
            child.add_argument("--solution-status", choices=("draft", "reviewed"))
            child.add_argument("--limit", type=int, default=20)
            child.add_argument("--json", action="store_true")
        if command == "show":
            child.add_argument("id")
    args = parser.parse_args(argv)
    try:
        if args.command == "new":
            folder = scaffold_puzzle(args.title, args.author)
            validate(load_system(edition_id=args.edition))
            print(f"Created {folder.relative_to(ROOT).as_posix()}/: edit puzzle.json and solution.json, "
                  "then run: python tools/puzzles.py index")
            return 0
        system = load_system(edition_id=args.edition)
        counts = validate(system)
        if args.command == "validate":
            print(f"PASS: {counts}")
        elif args.command == "stats":
            print(json.dumps(counts, ensure_ascii=False, indent=2))
        elif args.command == "index":
            target, text = index_path(system), render_index(system)
            current = target.read_text(encoding="utf-8") if target.is_file() else None
            if args.check:
                if current != text:
                    raise ValueError("INDEX.md is stale; run: python tools/puzzles.py index")
                print("INDEX.md is up to date")
            else:
                target.write_text(text, encoding="utf-8", newline="\n")
                print(f"Wrote {target.relative_to(system['root']).as_posix()}")
        elif args.command in {"render", "build"}:
            output = render_edition(system)
            if args.command == "build" and not args.render_only:
                release = None if args.no_release else output_pdfs(system)
                compile_edition(output, release)
                if release:
                    for path in release.values():
                        print(f"released: {path.relative_to(system['root']).as_posix()}")
            print(f"{read_json(output / 'manifest.json')['status']}: {output}")
        elif args.command == "search":
            if args.limit < 1:
                raise ValueError("Search limit must be positive")
            for field, key in ((args.concept, "concepts"), (args.technique, "techniques")):
                if field and field not in {item["id"] for item in system["taxonomy"][key]}:
                    raise ValueError(f"Unknown taxonomy ID: {field}")
            result = search(system, args)
            if args.json:
                print(json.dumps(result, ensure_ascii=False, indent=2))
            else:
                for row in result:
                    print(f"{row['id']} | {row['stars']} stars | {row['analysis_status']} | {row['title']}")
                print(f"{len(result)} result(s); tags are suggestions unless reviewed.")
        elif args.command == "show":
            matches = [p for p in system["puzzles"] if args.id == p["id"] or args.id in p.get("aliases", [])]
            if len(matches) != 1:
                raise ValueError(f"ID/alias resolves to {len(matches)} puzzles; use a PZ ID")
            puzzle = matches[0]
            print(json.dumps({"puzzle": puzzle, "solution": solution_for(system, puzzle),
                              "review": next(r for r in system["reviews"] if r["puzzle_id"] == puzzle["id"]),
                              "provenance": next(r for r in system["provenance"] if r["puzzle_id"] == puzzle["id"])},
                             ensure_ascii=False, indent=2))
        return 0
    except subprocess.CalledProcessError as exc:
        print(exc.stdout or str(exc), file=sys.stderr)
        return 1
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
