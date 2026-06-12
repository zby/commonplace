"""Shared sentinel and result-line grammar for review protocol text.

The unit of review output is one (note, gate) pair. Every block is keyed by
the full pair regardless of how pairs were packed into the surrounding LLM
call (one note with many gates, one gate over many notes, or any mix).
"""

from __future__ import annotations

import re


PAIR_KEY_SEPARATOR = " :: "

PAIR_START_RE = re.compile(r"^=== PAIR REVIEW START: (?P<note_path>.+?) :: (?P<gate_id>.+?) ===$")
PAIR_END_RE = re.compile(r"^=== PAIR REVIEW END: (?P<note_path>.+?) :: (?P<gate_id>.+?) ===$")
RESERVED_SENTINEL_RE = re.compile(r"^===\s.+\s===$")

PAIR_START_TEMPLATE = "=== PAIR REVIEW START: {note_path} :: {gate_id} ==="
PAIR_END_TEMPLATE = "=== PAIR REVIEW END: {note_path} :: {gate_id} ==="
RESULT_LINE_TEMPLATE = "## Result: PASS|WARN|FAIL|ERROR"

DECISION_LINE_INSTRUCTION = (
    "- Inside each block, include a decision line in a parseable form such as "
    "`## Result: PASS` or `## Result: WARN`."
)
