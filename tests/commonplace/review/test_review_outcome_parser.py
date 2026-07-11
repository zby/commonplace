from __future__ import annotations

import pytest

from commonplace.review.protocol import outcomes


def test_parse_review_outcome_accepts_single_final_result_line() -> None:
    review_text = """### Summary
Grounding is aligned.

## Result: PASS
"""

    assert outcomes.parse_review_outcome(review_text) == "pass"


def test_parse_review_outcome_treats_error_as_execution_failure() -> None:
    with pytest.raises(ValueError, match="worker reported ERROR"):
        outcomes.parse_review_outcome("Unable to judge.\n\n## Result: ERROR\n")


def test_rewrite_review_result_footer_moves_result_to_end() -> None:
    review_text = """## Result: WARN

Grounding needs one citation.
"""

    assert outcomes.rewrite_review_result_footer(review_text, outcome="warn") == (
        "Grounding needs one citation.\n\n## Result: WARN\n"
    )


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


def test_parse_review_outcome_tolerates_bare_prose_word_lines() -> None:
    review_text = """### Summary
Fine note.

### Findings
- info: minor thing

### Suggested Revision
none

## Result: PASS
"""

    assert outcomes.parse_review_outcome(review_text) == "pass"


@pytest.mark.parametrize("word", ["none", "Approved", "Summary", "ok"])
def test_parse_review_outcome_tolerates_single_word_body_line(word: str) -> None:
    review_text = f"""### Summary
{word}

## Result: WARN
"""

    assert outcomes.parse_review_outcome(review_text) == "warn"


@pytest.mark.parametrize(
    "line",
    ["## result: PASS", "verdict: pass", "- outcome: warn", "**revised verdict**", "UNKNOWN"],
)
def test_parse_review_outcome_rejects_result_aliases_case_insensitively(line: str) -> None:
    review_text = f"""### Summary
Done.

{line}

## Result: PASS
"""

    with pytest.raises(ValueError, match="invalid result signal"):
        outcomes.parse_review_outcome(review_text)
