from __future__ import annotations

import pytest

from commonplace.review.protocol import outcomes


@pytest.mark.parametrize(
    ("review_text", "message"),
    [
        ("### Summary\nNo explicit outcome.\n", "missing result line"),
        ("### Summary\nDone.\n\n## Result: OK\n", "invalid result signal"),
        ("### Summary\nDone.\n\nVerdict: PASS\n", "invalid result signal"),
        ("### Summary\nDone.\n\n## Result: PASS\n\n## Result: WARN\n", "duplicate result lines"),
        ("## Result: PASS\n\n### Summary\nDone.\n", "result line must be the last non-empty line"),
        ("### Summary\nFlagging as WARN.\n\n## Result: PASS\n", "invalid result signal"),
    ],
)
def test_parse_review_outcome_rejects_non_strict_live_output(review_text: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        outcomes.parse_review_outcome(review_text)


def test_parse_review_outcome_tolerates_single_word_body_line() -> None:
    review_text = """### Summary
Approved

## Result: WARN
"""

    assert outcomes.parse_review_outcome(review_text) == "warn"


def test_parse_review_outcome_rejects_result_aliases_case_insensitively() -> None:
    review_text = """### Summary
Done.

verdict: pass

## Result: PASS
"""

    with pytest.raises(ValueError, match="invalid result signal"):
        outcomes.parse_review_outcome(review_text)
