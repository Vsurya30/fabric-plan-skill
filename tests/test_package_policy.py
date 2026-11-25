import hashlib
import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SYNTHETIC_GUID = re.compile(r"[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}")
LARGE_NUMBER = re.compile(r"(?<![A-Za-z0-9])\d{16,20}(?![A-Za-z0-9])")


class PackagePolicyTests(unittest.TestCase):
    def test_manifest_covers_public_package_roots(self):
        manifest = json.loads((ROOT / "package-manifest.json").read_text())
        required = {"runtime/", "references/", "fixtures/", "schemas/", "tools/", "vendor/"}
        self.assertTrue(required <= set(manifest["classification"]["runtime-required"]))
        for path in manifest["retained-unreferenced-assets"]:
            if "*" in path:
                self.assertTrue(list(ROOT.glob(path)), path)
            else:
                self.assertTrue((ROOT / path).is_file(), path)

    def test_no_tracked_bytecode_or_private_workspace_content(self):
        tracked = subprocess.check_output(
            ["git", "ls-files", "-z"], cwd=ROOT, text=False
        ).decode().split("\0")
        forbidden = tuple(
            path for path in tracked
            if path.endswith((".pyc", ".pyo"))
            or any(marker in path for marker in ("__pycache__", "_brief/", "_build/", "_samples/"))
        )
        self.assertEqual(forbidden, ())

    def test_reference_markdown_is_bounded_and_machine_data_is_elsewhere(self):
        limit = json.loads((ROOT / "package-manifest.json").read_text())[
            "limits"]["references_markdown_max_bytes"]
        oversized = [
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "references").glob("*.md")
            if path.stat().st_size > limit
        ]
        self.assertEqual(oversized, [])
        self.assertEqual(
            {path.name for path in (ROOT / "references").glob("*.json")},
            {"preservation-manifest.json"},
        )

    def test_request_examples_use_deterministic_synthetic_id_ranges(self):
        examples = [
            ROOT / "examples/planning-presentation.request.json",
            ROOT / "examples/measure-display.request.json",
            ROOT / "examples/five-usecases/destination.example.json",
        ]
        for path in examples:
            relative = path.relative_to(ROOT)
            text = path.read_text()
            for identifier in SYNTHETIC_GUID.findall(text):
                self.assertTrue(
                    identifier.lower().startswith(
                        ("f0000000-0000-4000-8000-", "10000000-0000-4000-8000-")
                    ),
                                f"{relative}: non-synthetic UUID {identifier}")
            for identifier in LARGE_NUMBER.findall(text):
                self.assertTrue(
                    identifier.startswith(("100000000000000", "200000000000000")),
                                f"{relative}: non-synthetic numeric identity")


if __name__ == "__main__":
    unittest.main()
