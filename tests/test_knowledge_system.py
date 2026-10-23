"""Regression checks for the knowledge system and its build workflow."""
import argparse
import copy
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.common import edition_rows, load_system, output_pdfs, project_path, read_json, validate, write_json
from tools.puzzles import compile_edition, index_path, input_hashes, render_edition, render_index, scaffold_puzzle, search

COPIED_DIRS = ("knowledge", "sources", "assets", "editions", "tools")


def copy_project(target):
    for directory in COPIED_DIRS:
        shutil.copytree(ROOT / directory, target / directory, ignore=shutil.ignore_patterns("__pycache__", "*.pdf"))
    shutil.copy2(ROOT / "project.json", target / "project.json")


class KnowledgeSystemTests(unittest.TestCase):
    def setUp(self):
        self.system = load_system()

    def test_sources_live_under_sources(self):
        self.assertTrue(all(s["path"].startswith("sources/") for s in self.system["sources"]))

    def test_index_is_up_to_date(self):
        target = index_path(self.system)
        self.assertTrue(target.is_file(), "run: python tools/puzzles.py index")
        self.assertEqual(target.read_text(encoding="utf-8"), render_index(self.system),
                         "knowledge/puzzles/INDEX.md is stale; run: python tools/puzzles.py index")

    def test_release_paths_follow_output_name(self):
        pdfs = output_pdfs(self.system)
        name = self.system["edition"]["output_name"]
        self.assertEqual({p.name for p in pdfs.values()}, {f"{name}-student.pdf", f"{name}-instructor.pdf"})
        self.assertTrue(all(p.parent == ROOT / "publications" for p in pdfs.values()))

    def test_folder_name_must_match_puzzle_id(self):
        with tempfile.TemporaryDirectory(prefix="algorithmic-puzzles-tests-") as folder:
            root = Path(folder).resolve()
            copy_project(root)
            puzzles = root / "knowledge/puzzles"
            (puzzles / "PZ-0001").rename(puzzles / "PZ-0999")
            with self.assertRaisesRegex(ValueError, "does not match its folder"):
                load_system(root)

    def test_new_puzzle_scaffold_gets_next_id_and_validates(self):
        with tempfile.TemporaryDirectory(prefix="algorithmic-puzzles-tests-") as folder:
            root = Path(folder).resolve()
            copy_project(root)
            before = max(p["id"] for p in load_system(root)["puzzles"])
            created = scaffold_puzzle("Bài thử nghiệm", author="GV A", root=root)
            self.assertEqual(created.name, f"PZ-{int(before[3:]) + 1:04d}")
            counts = validate(load_system(root))
            self.assertEqual(counts["puzzles"], len(self.system["puzzles"]) + 1)
            self.assertEqual(counts["selected"], len(edition_rows(self.system)))

    def test_bank_order_is_independent_of_edition_order(self):
        expected = edition_rows(self.system)
        self.system["puzzles"].reverse()
        self.assertEqual(edition_rows(self.system), expected)
        selection = self.system["edition"]["sections"][0]["puzzle_ids"]
        selection[0], selection[1] = selection[1], selection[0]
        self.assertEqual(edition_rows(self.system)[0]["id"], expected[1]["id"])
        self.assertEqual(edition_rows(self.system)[1]["body"], expected[0]["body"])

    def test_validation_does_not_promote_mathematical_review(self):
        before = copy.deepcopy(self.system)
        counts = validate(self.system)
        self.assertEqual(self.system, before)
        self.assertEqual(counts["reviewed_solutions"], 0)
        self.assertTrue(all(p["analysis"]["cognitive_level"] is None for p in self.system["puzzles"]))

    def test_unknown_taxonomy_is_rejected(self):
        self.system["puzzles"][0]["analysis"]["technique_ids"].append("T-does-not-exist")
        with self.assertRaisesRegex(ValueError, "technique_ids"):
            validate(self.system)

    def test_duplicate_id_is_rejected(self):
        self.system["puzzles"][1]["id"] = self.system["puzzles"][0]["id"]
        with self.assertRaisesRegex(ValueError, "Duplicate puzzle ID"):
            validate(self.system)

    def test_method_roles_require_assigned_labels_and_known_roles(self):
        analysis = self.system["puzzles"][0]["analysis"]
        analysis["technique_roles"] = {"T-induction": "primary"}
        with self.assertRaisesRegex(ValueError, "technique_roles"):
            validate(self.system)
        analysis["technique_roles"] = {"T-backward": "unknown-role"}
        with self.assertRaisesRegex(ValueError, "technique_roles"):
            validate(self.system)

    def test_wrong_solution_link_is_rejected(self):
        self.system["puzzles"][0]["solution_path"] = self.system["puzzles"][1]["solution_path"]
        with self.assertRaisesRegex(ValueError, "Wrong solution link"):
            validate(self.system)

    def test_unknown_and_duplicate_edition_ids_are_rejected(self):
        section = self.system["edition"]["sections"][0]["puzzle_ids"]
        section[1] = section[0]
        with self.assertRaisesRegex(ValueError, "duplicate or unknown"):
            validate(self.system)
        section[1] = "PZ-9999"
        with self.assertRaisesRegex(ValueError, "duplicate or unknown"):
            validate(self.system)

    def test_stale_knowledge_evidence_is_rejected(self):
        self.system["cards"][0]["evidence"][0]["statement_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "Stale knowledge evidence"):
            validate(self.system)

    def test_review_requires_attribution(self):
        self.system["puzzles"][0]["analysis"]["status"] = "reviewed"
        with self.assertRaisesRegex(ValueError, "reviewer/date"):
            validate(self.system)

    def test_paths_cannot_escape_project(self):
        with self.assertRaisesRegex(ValueError, "leaves project"):
            project_path(ROOT, "../outside.json")
        with self.assertRaisesRegex(ValueError, "edition ID"):
            load_system(edition_id="../../outside")

    def test_search_distinguishes_adjacent_merge_from_greedy_merge(self):
        args = argparse.Namespace(query="", concept=None, technique="T-interval-dp", difficulty=None,
                                  analysis_status="suggested", solution_status=None, limit=50)
        ids = {row["id"] for row in search(self.system, args)}
        self.assertIn("PZ-0040", ids)
        self.assertNotIn("PZ-0035", ids)
        args.query, args.technique = "sap nhap", None
        self.assertIn("PZ-0040", {row["id"] for row in search(self.system, args)})
        args.query = "ma hoa"
        encoded = {row["id"] for row in search(self.system, args)}
        self.assertIn("PZ-0009", encoded)
        self.assertNotIn("PZ-0002", encoded)

    def test_author_edits_survive_repeated_render_and_compiler_failure(self):
        with tempfile.TemporaryDirectory(prefix="algorithmic-puzzles-tests-") as folder:
            root = Path(folder).resolve()
            copy_project(root)
            puzzle_file = root / "knowledge/puzzles/PZ-0001/puzzle.json"
            puzzle = read_json(puzzle_file)
            puzzle["statement"] += "\n\nDữ kiện biên tập mới được giữ lại."
            write_json(puzzle_file, puzzle)
            solution_path = root / "knowledge/puzzles/PZ-0001/solution.json"
            solution = read_json(solution_path)
            solution["outline"] += " TEACHERONLYSENTINEL"
            write_json(solution_path, solution)
            system = load_system(root)
            before = input_hashes(system)
            output = render_edition(system)
            first = (output / "tex/student.tex").read_bytes()
            render_edition(load_system(root))
            # Exercise the documented direct script entry, whose import path
            # differs from importing tools.puzzles through build.py.
            subprocess.run([sys.executable, str(root / "tools/puzzles.py"), "render"],
                           cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(input_hashes(load_system(root)), before)
            self.assertEqual((output / "tex/student.tex").read_bytes(), first)
            student = first.decode("utf-8")
            self.assertIn("Dữ kiện biên tập mới được giữ lại.", student)
            self.assertNotIn("TEACHERONLYSENTINEL", student)
            self.assertIn("TEACHERONLYSENTINEL", (output / "tex/instructor.tex").read_text(encoding="utf-8"))
            self.assertNotIn("{{DATA}}", student)
            (output / "pdf").mkdir()
            old_pdf = output / "pdf/student.pdf"
            old_pdf.write_bytes(b"previous PDF")
            release = output_pdfs(load_system(root))
            with patch("tools.puzzles.shutil.which", return_value="fake-xelatex"), patch(
                    "tools.puzzles.subprocess.run", side_effect=subprocess.CalledProcessError(1, ["fake-xelatex"], output="bad TeX")):
                with self.assertRaises(subprocess.CalledProcessError):
                    compile_edition(output, release)
            self.assertEqual(old_pdf.read_bytes(), b"previous PDF")
            self.assertFalse(any(p.exists() for p in release.values()), "failed build must not release PDFs")
            self.assertEqual(read_json(output / "manifest.json")["status"], "rendered")


if __name__ == "__main__":
    unittest.main()
