from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures" / "review-decision"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


review_db = load_module("review_db_decision_parser_test", SCRIPTS_DIR / "review_db.py")


def read_fixture(name: str) -> str:
    return (FIXTURES_DIR / name).read_text(encoding="utf-8")


def test_parse_review_decision_concrete_fixtures() -> None:
    cases = [
        ("result-pass.md", "pass"),
        ("semantic-completeness-run6-warn.md", "concern"),
        ("semantic-grounding-run9-warn.md", "concern"),
        ("semantic-internal-consistency-run9-info.md", "pass"),
    ]

    for fixture_name, expected in cases:
        actual = review_db.parse_review_decision(read_fixture(fixture_name))
        assert actual == expected, fixture_name


def test_parse_review_decision_uses_highest_finding_severity_without_explicit_outcome() -> None:
    review_text = """## Findings

- INFO: Minor note.
- WARN: Meaningful issue.
- FAIL: Blocking problem.
"""

    assert review_db.parse_review_decision(review_text) == "fail"
