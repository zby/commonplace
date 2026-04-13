"""Best-effort review decision parsing and footer rewriting."""

from __future__ import annotations

import re


_METADATA_BLOCK_RE = re.compile(
    r"\A<!-- REVIEW-METADATA\n(?P<body>.*?)\n-->\n?",
    re.DOTALL,
)
_BOLD_DECISION_RE = re.compile(r"^\*\*(pass|fail|warn|error)\*\*", re.IGNORECASE)
_RESULT_RE = re.compile(
    r"^(?:##\s*(?:Result|Verdict):|Verdict:|(?:[-*]\s*)?Outcome:)\s*"
    r"(pass|fail|error|warn|info|ok|unknown)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_SPLIT_RESULT_RE = re.compile(
    r"^##\s*(?:Result|Verdict|Outcome)\s*$\s*^(pass|fail|error|warn|info|ok|unknown)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_REVISED_RESULT_RE = re.compile(
    r"^(?:\*\*)?Revised\s+(?:result|verdict|outcome)(?:\*\*)?\s*:\s*"
    r"(pass|fail|error|warn|info|ok|unknown)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_FLAGGING_DECISION_RE = re.compile(
    r"\bflagging\s+as\s+(pass|fail|error|warn|info|ok|unknown)\b",
    re.IGNORECASE,
)
_LEGACY_RESULT_HEADING_RE = re.compile(
    r"^##\s+(pass|fail|error|warn|info|ok|unknown)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_RELAXED_RESULT_LINE_RE = re.compile(
    r"^(?:\*\*)?(?:##\s*)?(?:Result|Verdict|Outcome)\s*:\s*"
    r"(pass|fail|error|warn|info|ok|unknown)"
    r"(?:\s*\([^)]*\))?(?:\*\*)?\s*$",
    re.IGNORECASE,
)
_FINDING_SEVERITY_RE = re.compile(
    r"^(?:[-*]\s+)?(?:\*\*Severity:\*\*\s*)?(pass|ok|info|warn|fail|error)\s*(?:[:\u2014-]|$)|"
    r"^(?:[-*]\s+)?\*\*(pass|ok|info|warn|fail|error)\b",
    re.IGNORECASE | re.MULTILINE,
)
_LEGACY_BOLD_DECISION_RE = re.compile(r"^\*\*(pass|fail|error|warn|info|ok|unknown)\b", re.IGNORECASE)
_LEGACY_BOLD_INLINE_DECISION_RE = re.compile(
    r"^\*\*(pass|fail|error|warn|info|ok|unknown)(?:[.!:]?)\*\*(?:\s+.*)?$",
    re.IGNORECASE,
)
_LEGACY_INLINE_DECISION_RE = re.compile(
    r"^(pass|fail|error|warn|info|ok|unknown)\b(?:[.!:]|\s+[\u2014-])?(?:\s+.*)?$",
    re.IGNORECASE,
)
_LEGACY_HEADING_SUFFIX_DECISION_RE = re.compile(
    r"^#+\s+.*?[\u2014-]\s*(pass|fail|error|warn|info|ok|unknown)\s*$",
    re.IGNORECASE,
)
_LEGACY_STATUS_LINE_RE = re.compile(
    r"^\*\*status:\s*(pass|fail|error|warn|info|ok|unknown)(?:\s*\([^)]*\))?\*\*$",
    re.IGNORECASE,
)
_NO_VIOLATIONS_RE = re.compile(r"\bno violations found\b", re.IGNORECASE)
_MANUAL_IMPORT_PASS_PHRASE_RE = re.compile(
    r"\b(?:"
    r"no actionable instances|"
    r"no findings|"
    r"no [a-z0-9-]+ failure detected|"
    r"no [a-z0-9-]+ found|"
    r"no link text sets an expectation|"
    r"pairwise contradiction:\s*none found|"
    r"definition drift:\s*none observed"
    r")\b",
    re.IGNORECASE,
)
_QUALITATIVE_FINDING_RE = re.compile(r"^(?:[-*]\s+)?\*\*(minor|moderate|major)\b", re.IGNORECASE | re.MULTILINE)
_SINGLE_LINE_RESULT_RE = re.compile(
    r"^(?:##\s*(?:Result|Verdict):|Verdict:|(?:[-*]\s*)?Outcome:)\s*"
    r"(pass|fail|error|warn|info|ok|unknown)\s*$",
    re.IGNORECASE,
)
_SPLIT_RESULT_HEADING_RE = re.compile(r"^##\s*(?:Result|Verdict|Outcome)\s*$", re.IGNORECASE)
_DECISION_LINE_RE = re.compile(r"^(pass|fail|error|warn|info|ok|unknown)\s*$", re.IGNORECASE)
_LEGACY_RESULT_LINE_RE = re.compile(r"^##\s+(pass|fail|error|warn|info|ok|unknown)\s*$", re.IGNORECASE)

DECISION_VALUES = ("pass", "warn", "fail", "error", "unknown")


def normalize_review_decision(raw: str) -> str | None:
    decision = raw.strip().lower()
    if decision in {"pass", "ok", "info"}:
        return "pass"
    if decision == "warn":
        return "warn"
    if decision in {"fail", "error", "unknown"}:
        return decision
    return None


def _decision_rank(decision: str) -> int:
    return {
        "pass": 0,
        "warn": 1,
        "fail": 2,
        "error": 3,
        "unknown": 4,
    }[decision]


def _collect_explicit_review_decisions(review_text: str) -> list[tuple[str, str]]:
    explicit: list[tuple[str, str]] = []
    for pattern, source in (
        (_RESULT_RE, "result"),
        (_SPLIT_RESULT_RE, "split-result"),
        (_LEGACY_RESULT_HEADING_RE, "legacy-heading"),
        (_REVISED_RESULT_RE, "revised-result"),
    ):
        for match in pattern.finditer(review_text):
            decision = normalize_review_decision(match.group(1))
            if decision is not None:
                explicit.append((source, decision))

    stripped = review_text.lstrip()
    match = _LEGACY_BOLD_DECISION_RE.match(stripped)
    if match is not None:
        decision = normalize_review_decision(match.group(1))
        if decision is not None:
            explicit.append(("bold-heading", decision))
    return explicit


def _derive_review_decision_from_findings(review_text: str) -> str | None:
    severities = {
        normalized
        for match in _FINDING_SEVERITY_RE.finditer(review_text)
        for group in match.groups()
        if group
        for normalized in [normalize_review_decision(group)]
        if normalized is not None
    }
    if not severities:
        return None
    return max(severities, key=_decision_rank)


def _collect_flagged_review_decisions(review_text: str) -> list[str]:
    decisions: list[str] = []
    for match in _FLAGGING_DECISION_RE.finditer(review_text):
        decision = normalize_review_decision(match.group(1))
        if decision is not None:
            decisions.append(decision)
    return decisions


def _collect_qualitative_findings(review_text: str) -> set[str]:
    return {match.group(1).lower() for match in _QUALITATIVE_FINDING_RE.finditer(review_text)}


def _extract_declared_review_decision(review_text: str) -> str | None:
    flagged = _collect_flagged_review_decisions(review_text)
    if flagged and len(set(flagged)) == 1:
        return flagged[-1]

    explicit = _collect_explicit_review_decisions(review_text)
    revised = [decision for source, decision in explicit if source == "revised-result"]
    if revised and len(set(revised)) == 1:
        return revised[-1]

    unrevised = [decision for source, decision in explicit if source != "revised-result"]
    if unrevised and len(set(unrevised)) == 1:
        return unrevised[-1]

    stripped = review_text.lstrip()
    match = _LEGACY_BOLD_DECISION_RE.match(stripped)
    if match is not None:
        decision = normalize_review_decision(match.group(1))
        if decision is not None:
            return decision
    return None


def strip_review_metadata_block(review_text: str) -> str:
    match = _METADATA_BLOCK_RE.match(review_text)
    if match is None:
        return review_text
    return review_text[match.end() :].lstrip("\n")


def strip_legacy_frontmatter_block(review_text: str) -> str:
    lines = review_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return review_text
    for index in range(1, min(len(lines), 12)):
        if lines[index].strip() == "---":
            return "\n".join(lines[index + 1 :]).lstrip("\n")
    return review_text


def strip_relaxed_review_result_lines(review_text: str) -> str:
    lines = review_text.splitlines()
    kept: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if _SPLIT_RESULT_HEADING_RE.match(stripped) and index + 1 < len(lines):
            next_stripped = lines[index + 1].strip()
            if _DECISION_LINE_RE.match(next_stripped):
                index += 2
                continue
        if (
            _SINGLE_LINE_RESULT_RE.match(stripped)
            or _LEGACY_RESULT_LINE_RE.match(stripped)
            or _RELAXED_RESULT_LINE_RE.match(stripped)
        ):
            index += 1
            continue
        kept.append(line)
        index += 1

    stripped_text = "\n".join(kept).strip()
    return re.sub(r"\n{3,}", "\n\n", stripped_text)


def _extract_manual_import_leading_decision(review_text: str) -> str | None:
    lines = [line.strip() for line in review_text.splitlines() if line.strip()]
    for line in lines[:8]:
        for pattern in (
            _RELAXED_RESULT_LINE_RE,
            _LEGACY_STATUS_LINE_RE,
            _LEGACY_HEADING_SUFFIX_DECISION_RE,
            _LEGACY_BOLD_INLINE_DECISION_RE,
            _LEGACY_INLINE_DECISION_RE,
            _LEGACY_RESULT_HEADING_RE,
        ):
            match = pattern.match(line)
            if match is None:
                continue
            decision = normalize_review_decision(match.group(1))
            if decision is not None:
                return decision
        if line.startswith("#") or line == "---" or line.lower().startswith(("gate:", "note:")):
            continue
        break
    return None


def infer_manual_import_review_decision(review_text: str) -> str:
    stripped = strip_review_metadata_block(review_text)
    stripped = strip_legacy_frontmatter_block(stripped)

    leading_decision = _extract_manual_import_leading_decision(stripped)
    if leading_decision is not None:
        return leading_decision

    stripped_without_results = strip_relaxed_review_result_lines(stripped)
    parsed_decision = parse_review_decision(stripped_without_results)
    if parsed_decision != "unknown":
        return parsed_decision

    if _MANUAL_IMPORT_PASS_PHRASE_RE.search(stripped_without_results):
        return "pass"

    return "unknown"


def strip_explicit_review_result_lines(review_text: str) -> str:
    return strip_relaxed_review_result_lines(review_text)


def rewrite_review_result_footer(review_text: str, *, decision: str | None = None) -> str:
    normalized_decision = normalize_review_decision(decision) if decision else None
    declared_decision = _extract_declared_review_decision(review_text)
    parsed_decision = parse_review_decision(review_text)

    footer_decision = normalized_decision if normalized_decision in {"pass", "warn", "fail", "error", "unknown"} else None
    if footer_decision is None and declared_decision is not None:
        footer_decision = declared_decision
    if footer_decision is None and parsed_decision in {"pass", "warn", "fail", "error"}:
        footer_decision = parsed_decision

    if footer_decision is None:
        normalized_text = review_text.strip()
        return f"{normalized_text}\n" if normalized_text else ""

    body = strip_explicit_review_result_lines(review_text)
    footer = f"## Result: {footer_decision.upper()}"
    if body:
        return f"{body}\n\n{footer}\n"
    return f"{footer}\n"


def parse_review_decision(review_text: str) -> str:
    explicit = _collect_explicit_review_decisions(review_text)
    findings_decision = _derive_review_decision_from_findings(review_text)
    flagged = _collect_flagged_review_decisions(review_text)
    qualitative_findings = _collect_qualitative_findings(review_text)

    if flagged:
        if len(set(flagged)) > 1:
            return "unknown"
        return flagged[-1]

    revised = [decision for source, decision in explicit if source == "revised-result"]
    if revised:
        if len(set(revised)) > 1:
            return "unknown"
        return revised[-1]

    explicit_decisions = [decision for _, decision in explicit]
    if explicit_decisions:
        unique_explicit = set(explicit_decisions)
        if len(unique_explicit) > 1:
            return "unknown"
        candidate = explicit_decisions[-1]
        if candidate == "warn" and findings_decision == "pass" and _NO_VIOLATIONS_RE.search(review_text):
            return "pass"
        if candidate == "warn" and qualitative_findings & {"minor", "moderate"}:
            return "warn"
        if candidate == "fail" and "major" in qualitative_findings:
            return "fail"
        if findings_decision is not None and candidate != findings_decision:
            return "unknown"
        return candidate

    if findings_decision is not None:
        return findings_decision

    stripped = review_text.lstrip()
    match = _BOLD_DECISION_RE.match(stripped)
    if match is not None:
        decision = normalize_review_decision(match.group(1))
        if decision is not None:
            return decision
    return "unknown"
