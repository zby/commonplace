"""The strict result line decides each stored outcome; an ambiguous review must be rejected, not read."""

from __future__ import annotations

import pytest

from commonplace.lib.review_workflows.outcomes import parse_report, parse_verdict


@pytest.mark.parametrize(
    ("text", "message"),
    [
        ("### Summary\nNo explicit outcome.\n", "missing result line"),
        ("### Summary\nDone.\n\n## Result: OK\n", "invalid result signal"),
        ("### Summary\nDone.\n\nVerdict: PASS\n", "invalid result signal"),
        ("### Summary\nDone.\n\n## Result: PASS\n\n## Result: WARN\n", "duplicate result lines"),
        ("## Result: PASS\n\n### Summary\nDone.\n", "result line must be the last non-empty line"),
        ("### Summary\nFlagging as WARN.\n\n## Result: PASS\n", "invalid result signal"),
        ("### Summary\nDone.\n\nverdict: pass\n\n## Result: PASS\n", "invalid result signal"),
        ("### Summary\nCannot judge.\n\n## Result: ERROR\n", "invalid result signal"),
    ],
)
def test_verdict_rejects_non_strict_output(text: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        parse_verdict(text)


def test_verdict_tolerates_a_single_word_body_line() -> None:
    assert parse_verdict("### Summary\nApproved\n\n## Result: WARN\n") == "warn"


def test_report_requires_the_report_line_and_rejects_a_verdict() -> None:
    parse_report("The critique.\n\n## Result: REPORT\n")
    with pytest.raises(ValueError, match="verdict result is invalid"):
        parse_report("The critique.\n\n## Result: PASS\n")
    with pytest.raises(ValueError, match="missing report result line"):
        parse_report("The critique.\n")
