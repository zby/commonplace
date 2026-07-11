"""Strict review outcome parsing and footer rewriting."""

from __future__ import annotations

import re


OUTCOME_VALUES = ("pass", "warn", "fail")

_STRICT_RESULT_LINE_RE = re.compile(r"^## Result: (?P<outcome>PASS|WARN|FAIL)$")
_ERROR_RESULT_LINE_RE = re.compile(r"^## Result: ERROR$")
_STRICT_REPORT_LINE_RE = re.compile(r"^## Result: REPORT$")
# Alias branches are case-insensitive via the scoped (?i:...) group; the bare
# caps-word branch must stay case-sensitive or any single-word prose line
# ("none", "Approved") would read as a result signal and fail the job.
_RESULTISH_LINE_RE = re.compile(
    r"^(?:(?i:##\s*(?:Result|Verdict|Outcome)\b|Verdict:|(?:[-*]\s*)?Outcome:|"
    r"(?:\*\*)?Revised\s+(?:result|verdict|outcome))|"
    r"(?:\*\*)?[A-Z]{2,}(?:\*\*)?\s*$)"
)
_FLAGGING_OUTCOME_RE = re.compile(r"\bflagging\s+as\s+[A-Za-z]+\b", re.IGNORECASE)


def normalize_review_outcome(raw: str) -> str | None:
    outcome = raw.strip().lower()
    if outcome in OUTCOME_VALUES:
        return outcome
    return None


def _invalid_resultish_lines(review_text: str, strict_line: str | None) -> list[str]:
    invalid: list[str] = []
    for line in review_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped == strict_line:
            continue
        if _RESULTISH_LINE_RE.match(stripped) or _FLAGGING_OUTCOME_RE.search(stripped):
            invalid.append(stripped)
    return invalid


def _parse_result_line(
    review_text: str,
    pattern: re.Pattern[str],
    *,
    missing_message: str,
    wrong_kind_pattern: re.Pattern[str] | None = None,
) -> re.Match[str]:
    lines = review_text.splitlines()
    if any(_ERROR_RESULT_LINE_RE.match(line.strip()) for line in lines):
        raise ValueError("worker reported ERROR")
    matches = [
        (index, line.strip(), match)
        for index, line in enumerate(lines)
        if (match := pattern.match(line.strip())) is not None
    ]
    if not matches:
        if wrong_kind_pattern is not None and any(wrong_kind_pattern.match(line.strip()) for line in lines):
            raise ValueError("verdict result is invalid for report pair")
        invalid = _invalid_resultish_lines(review_text, strict_line=None)
        if invalid:
            raise ValueError(f"invalid result signal: {invalid[0]}")
        raise ValueError(missing_message)
    if len(matches) > 1:
        raise ValueError("duplicate result lines")
    index, strict_line, match = matches[0]
    non_empty = [line_index for line_index, line in enumerate(lines) if line.strip()]
    if index != non_empty[-1]:
        raise ValueError("result line must be the last non-empty line")
    invalid = _invalid_resultish_lines(review_text, strict_line=strict_line)
    if invalid:
        raise ValueError(f"invalid result signal: {invalid[0]}")
    return match


def parse_review_outcome(review_text: str) -> str:
    """Return the single strict result outcome or raise on non-live output."""
    match = _parse_result_line(review_text, _STRICT_RESULT_LINE_RE, missing_message="missing result line")
    return match.group("outcome").lower()


def parse_report_completion(review_text: str) -> None:
    """Require REPORT as the sole final result signal."""
    _parse_result_line(
        review_text,
        _STRICT_REPORT_LINE_RE,
        missing_message="missing report result line",
        wrong_kind_pattern=_STRICT_RESULT_LINE_RE,
    )


def canonicalize_report_completion(review_text: str) -> str:
    parse_report_completion(review_text)
    body = "\n".join(
        line for line in review_text.splitlines() if not _STRICT_REPORT_LINE_RE.match(line.strip())
    ).strip()
    return f"{body}\n\n## Result: REPORT\n" if body else "## Result: REPORT\n"


def strip_explicit_review_result_lines(review_text: str) -> str:
    kept = [
        line
        for line in review_text.splitlines()
        if _STRICT_RESULT_LINE_RE.match(line.strip()) is None
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept).strip())


def rewrite_review_result_footer(review_text: str, *, outcome: str) -> str:
    normalized_outcome = normalize_review_outcome(outcome)
    if normalized_outcome is None:
        raise ValueError(f"invalid review outcome: {outcome}")
    body = strip_explicit_review_result_lines(review_text)
    footer = f"## Result: {normalized_outcome.upper()}"
    if body:
        return f"{body}\n\n{footer}\n"
    return f"{footer}\n"
