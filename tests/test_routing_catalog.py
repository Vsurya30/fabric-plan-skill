"""Nothing in the routing catalog may name a private or native endpoint.

test_discovery.py already proves the catalog resolves to shipped guides,
registered commands and existing callables. This guards the other direction:
routing text must never invite an agent toward a route this skill cannot use.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Endpoint shapes and private runtime modules only. Prose may still disclaim a
# route in words, and tests/test_discovery.py requires POWERTABLE to do exactly
# that; naming one as a usable path is what this forbids.
ROUTE = re.compile(
    r"/v1/workload|/v1/rules|/v1/access/|/webapi/|planningproxy|generatemwctokenv2|"
    r"\bruntime\.(native|session|home_api|builder_api|intelligence_api|activation|"
    r"assets_api|dashboard_readback|navigation_publish|planning_rule_state|"
    r"powertable_readiness)\b"
)


GUIDE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*\.md\b")
# Restating why a document is absent is not an invitation to read it.
GAPS_EXEMPT = {"documentationNotBundled"}


class RoutingCatalogBoundaries(unittest.TestCase):
    def test_catalog_names_no_private_route(self):
        text = (ROOT / "catalog" / "module-routing.json").read_text(encoding="utf-8")
        self.assertIsNone(ROUTE.search(text.lower()))

    def test_guides_name_no_private_route(self):
        for path in sorted((ROOT / "references").glob("*.md")):
            with self.subTest(guide=path.name):
                self.assertIsNone(ROUTE.search(path.read_text(encoding="utf-8").lower()))

    def test_shipped_text_points_only_at_bundled_guides(self):
        bundled = {path.name for path in (ROOT / "references").glob("*.md")}
        sources = {
            "catalog/module-routing.json": (ROOT / "catalog" / "module-routing.json").read_text(
                encoding="utf-8"
            ),
            "SKILL.md": (ROOT / "SKILL.md").read_text(encoding="utf-8"),
            "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
        }
        gaps = json.loads((ROOT / "catalog" / "api-contract-gaps.json").read_text(encoding="utf-8"))
        sources["catalog/api-contract-gaps.json"] = json.dumps(
            {key: value for key, value in gaps.items() if key not in GAPS_EXEMPT}
        )
        for name, text in sources.items():
            with self.subTest(source=name):
                self.assertEqual(set(GUIDE_NAME.findall(text)) - bundled - {"SKILL.md"}, set())


if __name__ == "__main__":
    unittest.main()
