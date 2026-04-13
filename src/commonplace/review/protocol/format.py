"""Shared sentinel and result-line grammar for review protocol text."""

from __future__ import annotations

import re


BUNDLE_START_RE = re.compile(r"^=== GATE REVIEW START: (?P<gate_id>.+?) ===$")
BUNDLE_END_RE = re.compile(r"^=== GATE REVIEW END: (?P<gate_id>.+?) ===$")
NOTE_START_RE = re.compile(r"^=== NOTE START: (?P<note_path>.+?) ===$")
NOTE_END_RE = re.compile(r"^=== NOTE END: (?P<note_path>.+?) ===$")
RESERVED_SENTINEL_RE = re.compile(r"^===\s.+\s===$")

GATE_REVIEW_START_TEMPLATE = "=== GATE REVIEW START: {gate_id} ==="
GATE_REVIEW_END_TEMPLATE = "=== GATE REVIEW END: {gate_id} ==="
NOTE_START_TEMPLATE = "=== NOTE START: {note_path} ==="
NOTE_END_TEMPLATE = "=== NOTE END: {note_path} ==="
RESULT_LINE_TEMPLATE = "## Result: PASS|WARN|FAIL|ERROR"

DECISION_LINE_INSTRUCTION = (
    "- Inside each block, include a decision line in a parseable form such as "
    "`## Result: PASS` or `## Result: WARN`."
)
GATE_SWEEP_DECISION_LINE_INSTRUCTION = (
    "- Inside each gate block, include a decision line in a parseable form such as "
    "`## Result: PASS` or `## Result: WARN`."
)
