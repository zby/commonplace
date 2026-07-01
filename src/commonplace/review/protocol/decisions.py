"""Strict review decision parsing and footer rewriting."""

from __future__ import annotations

import re


DECISION_VALUES = ("pass", "warn", "fail", "error")

_STRICT_RESULT_LINE_RE = re.compile(r"^## Result: (?P<decision>PASS|WARN|FAIL|ERROR)$")
_RESULTISH_LINE_RE = re.compile(
    r"^(?:##\s*(?:Result|Verdict|Outcome)\b|Verdict:|(?:[-*]\s*)?Outcome:|"
    r"(?:\*\*)?Revised\s+(?:result|verdict|outcome)|"
    r"(?:\*\*)?(?:PASS|WARN|FAIL|ERROR|[A-Z]{2,})(?:\*\*)?\s*$)",
    re.IGNORECASE,
)
_FLAGGING_DECISION_RE = re.compile(r"\bflagging\s+as\s+[A-Za-z]+\b", re.IGNORECASE)


def normalize_review_decision(raw: str) -> str | None:
    decision = raw.strip().lower()
    if decision in DECISION_VALUES:
        return decision
    return None


def _strict_result_lines(review_text: str) -> list[tuple[int, str, str]]:
    result_lines: list[tuple[int, str, str]] = []
    for index, line in enumerate(review_text.splitlines()):
        stripped = line.strip()
        match = _STRICT_RESULT_LINE_RE.match(stripped)
        if match is not None:
            result_lines.append((index, stripped, match.group("decision").lower()))
    return result_lines


def _invalid_resultish_lines(review_text: str, strict_line: str | None) -> list[str]:
    invalid: list[str] = []
    for line in review_text.splitlines():
        stripped = line.strip()
        if not stripped or stripped == strict_line:
            continue
        if _RESULTISH_LINE_RE.match(stripped) or _FLAGGING_DECISION_RE.search(stripped):
            invalid.append(stripped)
    return invalid


def parse_review_decision(review_text: str) -> str:
    """Return the single strict result decision or raise on non-live output."""
    result_lines = _strict_result_lines(review_text)
    if not result_lines:
        invalid = _invalid_resultish_lines(review_text, strict_line=None)
        if invalid:
            raise ValueError(f"invalid result signal: {invalid[0]}")
        raise ValueError("missing result line")
    if len(result_lines) > 1:
        raise ValueError("duplicate result lines")

    index, strict_line, decision = result_lines[0]
    non_empty_line_indexes = [
        line_index
        for line_index, line in enumerate(review_text.splitlines())
        if line.strip()
    ]
    if non_empty_line_indexes and index != non_empty_line_indexes[-1]:
        raise ValueError("result line must be the last non-empty line")

    invalid = _invalid_resultish_lines(review_text, strict_line=strict_line)
    if invalid:
        raise ValueError(f"invalid result signal: {invalid[0]}")
    return decision


def strip_explicit_review_result_lines(review_text: str) -> str:
    kept = [
        line
        for line in review_text.splitlines()
        if _STRICT_RESULT_LINE_RE.match(line.strip()) is None
    ]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept).strip())


def rewrite_review_result_footer(review_text: str, *, decision: str | None = None) -> str:
    normalized_decision = normalize_review_decision(decision) if decision else parse_review_decision(review_text)
    if normalized_decision is None:
        raise ValueError(f"invalid review decision: {decision}")
    body = strip_explicit_review_result_lines(review_text)
    footer = f"## Result: {normalized_decision.upper()}"
    if body:
        return f"{body}\n\n{footer}\n"
    return f"{footer}\n"
