"""Check portable skill resources, not private runtime artifacts."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ppt-local-workflow"


class PackageTests(unittest.TestCase):
    def test_required_frontmatter_and_ui_metadata(self):
        content = (SKILL / "SKILL.md").read_text(encoding="utf-8-sig")
        self.assertTrue(content.startswith("---\nname: ppt-local-workflow\n"))
        self.assertIn("description: Use when", content.split("---", 2)[1])
        metadata = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8-sig")
        self.assertIn("$ppt-local-workflow", metadata)

    def test_all_local_markdown_links_resolve(self):
        for document in ROOT.rglob("*.md"):
            if any(part in (".git", "work", "outputs", "dist") for part in document.relative_to(ROOT).parts):
                continue
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8-sig")):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((document.parent / target.split("#", 1)[0]).exists(), f"Broken link in {document.name}: {target}")

    def test_skill_has_no_machine_specific_absolute_paths(self):
        for document in SKILL.rglob("*"):
            if document.is_file() and document.suffix in (".md", ".yaml", ".py"):
                text = document.read_text(encoding="utf-8-sig")
                self.assertIsNone(re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]", text), document.name)
                self.assertNotIn("/Users/", text)
                self.assertNotIn("/home/", text)


if __name__ == "__main__":
    unittest.main()
