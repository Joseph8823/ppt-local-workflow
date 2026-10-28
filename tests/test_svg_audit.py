"""Synthetic structural checks; these do not test PowerPoint rendering."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ppt-local-workflow" / "scripts" / "audit_svg.py"
PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aN1kAAAAASUVORK5CYII="


def sample(extra="", image=None):
    picture = image or f"data:image/png;base64,{PNG}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
      <rect x="0" y="0" width="1280" height="720" fill="#ffffff"/>
      <text x="64" y="90" font-family="Arial" font-size="32" font-weight="700" fill="#17324d" text-anchor="start">Project update</text>
      <text x="64" y="160" font-family="Arial" font-size="24" font-weight="400" fill="#17324d" text-anchor="start">A complete editable visual line.</text>
      <image x="800" y="140" width="200" height="200" href="{picture}"/>{extra}
    </svg>'''


class AuditTests(unittest.TestCase):
    def setUp(self):
        if not SCRIPT.is_file():
            self.fail("The SVG audit helper has not been implemented.")
        spec = importlib.util.spec_from_file_location("audit_svg", SCRIPT)
        self.audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.audit)

    def inspect(self, source):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sample.svg"
            path.write_text(source, encoding="utf-8")
            return self.audit.audit_file(path)

    def test_complete_lines_and_embedded_picture(self):
        result = self.inspect(sample())
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["counts"]["text"], 2)
        self.assertEqual(result["counts"]["image"], 1)
        self.assertEqual(result["view_box"], [0.0, 0.0, 1280.0, 720.0])

    def test_rejects_external_picture(self):
        result = self.inspect(sample(image="https://example.invalid/figure.png"))
        self.assertTrue(any("embedded" in error for error in result["errors"]))

    def test_rejects_invalid_embedded_picture(self):
        result = self.inspect(sample(image="data:image/png;base64,broken!"))
        self.assertTrue(any("base64" in error for error in result["errors"]))

    def test_rejects_character_position_lists(self):
        result = self.inspect(sample().replace('x="64" y="90"', 'x="64 84 104" y="90"'))
        self.assertTrue(any("coordinate list" in error for error in result["errors"]))

    def test_rejects_missing_explicit_font(self):
        result = self.inspect(sample().replace(' font-family="Arial"', "", 1))
        self.assertTrue(any("font-family" in error for error in result["errors"]))

    def test_rejects_relative_or_nonfinite_root_dimensions(self):
        for value in ("100%", "20em", "1e999", "0", "-4"):
            with self.subTest(value=value):
                result = self.inspect(sample().replace('width="1280"', f'width="{value}"', 1))
                self.assertTrue(any("Root width" in error for error in result["errors"]))

    def test_rejects_foreign_text_and_scripts(self):
        for element in ("<foreignObject/>", "<script/>", "<textPath/>"):
            with self.subTest(element=element):
                self.assertTrue(self.inspect(sample(extra=element))["errors"])

    def test_rejects_external_stylesheet_and_entities(self):
        for prefix in ('<?xml-stylesheet href="https://example.invalid/x.css"?>', '<!DOCTYPE svg [<!ENTITY name "text">]>'):
            with self.subTest(prefix=prefix):
                self.assertTrue(self.inspect(prefix + sample())["errors"])

    def test_allows_internal_gradient_reference(self):
        source = sample(extra='<defs><linearGradient id="paint"/></defs><rect width="12" height="12" fill="url(#paint)"/>')
        self.assertEqual(self.inspect(source)["errors"], [])

    def test_rejects_external_css_url(self):
        source = sample(extra='<rect width="12" height="12" fill="url(https://example.invalid/paint.svg)"/>')
        self.assertTrue(self.inspect(source)["errors"])

    def test_structural_success_does_not_claim_native_acceptance(self):
        result = self.inspect(sample())
        self.assertEqual(result["powerpoint_validation"], "not_performed")
        self.assertFalse(result["visually_verified"])

    def test_flags_suspected_character_objects_without_rejecting_a_label(self):
        tiny = '<text x="10" y="20" font-family="Arial" font-size="20" font-weight="400" fill="#111111" text-anchor="start">A</text>'
        result = self.inspect(sample(extra=tiny * 12))
        self.assertTrue(any("character" in warning for warning in result["warnings"]))
        self.assertEqual(self.inspect(sample(extra=tiny))["errors"], [])

    def test_cli_reports_all_files_and_fails_for_invalid_structure(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "01.svg").write_text(sample(), encoding="utf-8")
            (root / "02.svg").write_text(sample(image="missing.png"), encoding="utf-8")
            report = root / "report.json"
            process = subprocess.run([sys.executable, str(SCRIPT), str(root), "--output", str(report)], capture_output=True, text=True)
            self.assertEqual(process.returncode, 1)
            result = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(len(result["files"]), 2)
            self.assertFalse(result["structure_ok"])


if __name__ == "__main__":
    unittest.main()
