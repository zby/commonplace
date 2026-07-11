"""Shared sentinel and result-line grammar for review protocol text.

The unit of assay output is one persisted (note_path, criterion_path) pair. Every block is keyed by
the full pair regardless of how pairs were grouped into the surrounding LLM
call (one note with many criteria, one criterion over many notes, or any mix).
"""

from __future__ import annotations

import re


PAIR_KEY_SEPARATOR = " :: "

PAIR_START_RE = re.compile(r"^=== PAIR REVIEW START: (?P<note_path>.+?) :: (?P<criterion_path>.+?) ===$")
PAIR_END_RE = re.compile(r"^=== PAIR REVIEW END: (?P<note_path>.+?) :: (?P<criterion_path>.+?) ===$")
RESERVED_SENTINEL_RE = re.compile(r"^===\s.+\s===$")

PAIR_START_TEMPLATE = "=== PAIR REVIEW START: {note_path} :: {criterion_path} ==="
PAIR_END_TEMPLATE = "=== PAIR REVIEW END: {note_path} :: {criterion_path} ==="
RESULT_LINE_TEMPLATE = "## Result: PASS|WARN|FAIL|ERROR"
REPORT_LINE_TEMPLATE = "## Result: REPORT"

OUTCOME_LINE_INSTRUCTION = (
    "- Inside each block, include exactly one final result line: "
    "`## Result: PASS`, `## Result: WARN`, `## Result: FAIL`, or `## Result: ERROR`. "
    "Use ERROR only when you cannot produce the contracted verdict; it fails the whole job and is not an outcome. "
    "Do not use aliases such as Verdict, Outcome, INFO, OK, or UNKNOWN."
)
