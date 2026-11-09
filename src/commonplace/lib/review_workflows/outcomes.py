"""The strict result line a review ends with.

A verdict review ends with exactly one `## Result: PASS`, `## Result: WARN`
or `## Result: FAIL` as its last non-empty line; a report ends with
`## Result: REPORT`. Any other result-like line (an alias such as
`Verdict:`, a second result line, a bare capitalised word on its own line,
`flagging as WARN`) makes the review invalid, so an ambiguous review is
rejected instead of read one way.
"""

from __future__ import annotations

import re

_VERDICT_LINE = re.compile(r"^## Result: (?P<outcome>PASS|WARN|FAIL)$")
_REPORT_LINE = re.compile(r"^## Result: REPORT$")
# Alias branches are case-insensitive via the scoped (?i:...) group; the bare
# caps-word branch stays case-sensitive, or any single-word prose line
# ("none", "Approved") would read as a result signal.
_RESULTISH_LINE = re.compile(
    r"^(?:(?i:##\s*(?:Result|Verdict|Outcome)\b|Verdict:|(?:[-*]\s*)?Outcome:|"
    r"(?:\*\*)?Revised\s+(?:result|verdict|outcome))|"
    r"(?:\*\*)?[A-Z]{2,}(?:\*\*)?\s*$)"
)
_FLAGGING = re.compile(r"\bflagging\s+as\s+[A-Za-z]+\b", re.IGNORECASE)


def _invalid_signals(lines: list[str], strict_line: str | None) -> list[str]:
    return [line.strip() for line in lines
            if line.strip() and line.strip() != strict_line
            and (_RESULTISH_LINE.match(line.strip()) or _FLAGGING.search(line.strip()))]


def _result_line(text: str, pattern: re.Pattern[str], *, missing: str,
                 wrong_kind: re.Pattern[str] | None = None) -> re.Match[str]:
    lines = text.splitlines()
    matches = [(index, line.strip(), match) for index, line in enumerate(lines)
               if (match := pattern.match(line.strip())) is not None]
    if not matches:
        if wrong_kind is not None and any(wrong_kind.match(line.strip()) for line in lines):
            raise ValueError("verdict result is invalid for a report criterion")
        invalid = _invalid_signals(lines, None)
        raise ValueError(f"invalid result signal: {invalid[0]}" if invalid else missing)
    if len(matches) > 1:
        raise ValueError("duplicate result lines")
    index, strict_line, match = matches[0]
    if index != max(number for number, line in enumerate(lines) if line.strip()):
        raise ValueError("result line must be the last non-empty line")
    invalid = _invalid_signals(lines, strict_line)
    if invalid:
        raise ValueError(f"invalid result signal: {invalid[0]}")
    return match


def parse_verdict(text: str) -> str:
    """`pass`, `warn` or `fail` from the review's single strict result line; ValueError otherwise."""
    return _result_line(text, _VERDICT_LINE, missing="missing result line").group("outcome").lower()


def parse_report(text: str) -> None:
    """Require `## Result: REPORT` as the review's single final result signal; ValueError otherwise."""
    _result_line(text, _REPORT_LINE, missing="missing report result line", wrong_kind=_VERDICT_LINE)
