from __future__ import annotations

import importlib.util
import sqlite3
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
        ("semantic-completeness-run6-warn.md", "warn"),
        ("semantic-grounding-run9-warn.md", "warn"),
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


def test_parse_review_decision_supports_legacy_heading() -> None:
    review_text = """<!-- REVIEW-METADATA -->
## PASS

Looks good.
"""

    assert review_db.parse_review_decision(review_text) == "pass"


def test_parse_review_decision_supports_revised_result_override() -> None:
    review_text = """## Result: WARN

### Findings
- WARN: Something looked wrong at first.

Revised result: PASS
"""

    assert review_db.parse_review_decision(review_text) == "pass"


def test_parse_review_decision_supports_flagging_phrase_override() -> None:
    review_text = """## Result: WARN

### Findings
- INFO: Borderline issue.

Flagging as INFO rather than WARN because the case is defensible.
"""

    assert review_db.parse_review_decision(review_text) == "pass"


def test_parse_review_decision_supports_minor_severity() -> None:
    review_text = """## Result: WARN

### Findings
- **minor**: The title is mildly awkward as inline prose.
- **info**: No rewrite required.
"""

    assert review_db.parse_review_decision(review_text) == "warn"


def test_parse_review_decision_keeps_pass_when_minor_note_is_non_blocking() -> None:
    review_text = """## Result: PASS

### Findings
- Minor: The summary could be tighter.
"""

    assert review_db.parse_review_decision(review_text) == "pass"


def test_parse_review_decision_treats_no_violations_with_pass_findings_as_pass() -> None:
    review_text = """## Result: WARN

### Summary
No violations found.

### Findings
- PASS: All bullet items begin with a capitalized lead-in.
"""

    assert review_db.parse_review_decision(review_text) == "pass"


def test_parse_review_decision_returns_unknown_on_conflicting_signals() -> None:
    review_text = """## Result: WARN

### Findings
- PASS: The title is clear and aligned.
"""

    assert review_db.parse_review_decision(review_text) == "unknown"


def test_parse_review_decision_returns_unknown_when_no_signal_exists() -> None:
    review_text = """### Summary
No explicit outcome and no severity labels.
"""

    assert review_db.parse_review_decision(review_text) == "unknown"


def test_rewrite_review_result_footer_moves_result_to_end() -> None:
    review_text = """## Result: PASS

Grounding is aligned.
"""

    assert review_db.rewrite_review_result_footer(review_text) == "Grounding is aligned.\n\n## Result: PASS\n"


def test_rewrite_review_result_footer_preserves_declared_result_when_parse_is_unknown() -> None:
    review_text = """## Result: FAIL

### Findings
- PASS: The title is clear and aligned.
"""

    assert review_db.rewrite_review_result_footer(review_text) == (
        "### Findings\n- PASS: The title is clear and aligned.\n\n## Result: FAIL\n"
    )


def test_rewrite_review_result_footer_allows_unknown_when_explicitly_requested() -> None:
    review_text = """Pass

No findings.
"""

    assert review_db.rewrite_review_result_footer(review_text, decision="unknown") == (
        "Pass\n\nNo findings.\n\n## Result: UNKNOWN\n"
    )


def test_infer_manual_import_review_decision_prefers_legacy_body_over_stale_warn_footer() -> None:
    review_text = """<!-- REVIEW-METADATA
note-path: kb/notes/sample.md
-->
pass

No findings.

## Result: WARN
"""

    assert review_db.infer_manual_import_review_decision(review_text) == "pass"


def test_infer_manual_import_review_decision_handles_yaml_style_legacy_header() -> None:
    review_text = """---
gate: prose/bridge-paragraph-duplication
---

No instances found.

## Result: WARN
"""

    assert review_db.infer_manual_import_review_decision(review_text) == "pass"


def test_infer_manual_import_review_decision_supports_relaxed_result_line() -> None:
    review_text = """## Result: PASS (1 INFO)

The alignment is plausible but not exact.
"""

    assert review_db.infer_manual_import_review_decision(review_text) == "pass"


def test_infer_manual_import_review_decision_supports_bold_result_line() -> None:
    review_text = """## prose/anthropomorphic-framing

**Result: WARN**

One instance to fix.
"""

    assert review_db.infer_manual_import_review_decision(review_text) == "warn"


def test_ensure_db_migrates_gate_review_schema_to_support_unknown_and_warn(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    old_schema = (REPO_ROOT / "scripts" / "review-schema.sql").read_text(encoding="utf-8").replace(
        "decision IN ('pass', 'warn', 'fail', 'error', 'unknown')",
        "decision IN ('pass', 'warn', 'fail', 'error')",
    )
    with sqlite3.connect(db_path) as conn:
        conn.executescript(old_schema)
        conn.commit()

    review_db.ensure_db(REPO_ROOT, db_path)

    with sqlite3.connect(db_path) as conn:
        row = conn.execute(
            """
            SELECT sql
            FROM sqlite_master
            WHERE type = 'table' AND name = 'gate_reviews'
            """
        ).fetchone()
        assert row is not None
        assert "'unknown'" in row[0].lower()
        assert "'warn'" in row[0].lower()
