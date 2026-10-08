"""Collect the pinned criterion bytes analysis validators apply."""
from __future__ import annotations

from commonplace.lib.agentic_analysis.sets import SET_TYPE
from commonplace.workflow import CodeAttempt


def criterion_bytes(attempt: CodeAttempt) -> dict[str, bytes]:
    """The job's pinned library files plus the set type fixed at start.

    Missing dependencies stay absent; the closed validator rejects them.
    """
    return {**attempt.read_files(), SET_TYPE: attempt.type_text.encode("utf-8")}
