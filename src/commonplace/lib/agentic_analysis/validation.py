"""Collect only declared criterion bytes for analysis validators."""
from __future__ import annotations

from commonplace.workflow import CodeAttempt

ROOT = "agentic-system-analyses/"
TYPES = {
    "set": "agentic-system-analysis-set", "boundary": "agentic-system-boundary",
    "runtime": "agentic-system-runtime-report", "memory": "agent-memory-analysis-report",
    "epistemic": "agentic-system-epistemic-report", "reconciliation": "agentic-system-reconciliation-report",
    "memory-profile": "agent-memory-profile", "overview": "agentic-system-analysis-overview",
    "record-verification": "agentic-system-verification", "profile-verification": "agentic-system-verification",
    "synthesis-verification": "agentic-system-verification", "synthesis": "agentic-system-synthesis",
}
CRITERIA = {
    "collection": ROOT + "COLLECTION.md", "validation-contract": "reference/validation-contract.md",
    "boundary-contract": ROOT + "instructions/agentic-analysis-boundary.md",
    "sources-contract": ROOT + "instructions/agentic-analysis-sources.md",
    "records-contract": ROOT + "instructions/agentic-analysis-records.md",
    "note-type": "types/note.md", "type-spec": "types/type-spec.md",
    "type-spec-schema": "types/type-spec.schema.yaml", "note-schema": "types/note.schema.yaml",
    "note-base-schema": "types/note-base.schema.yaml",
    **{role + "-type": ROOT + "types/" + name + ".md" for role, name in TYPES.items()},
    **{name + "-schema": ROOT + "types/" + name + ".schema.yaml" for name in set(TYPES.values())},
}


def criterion_bytes(attempt: CodeAttempt) -> dict[str, bytes]:
    """Missing declared dependencies stay absent; the closed validator rejects them."""
    result = {}
    for alias, path in CRITERIA.items():
        if alias == "set-type":
            # The set type is fixed for the run, never a live file input.
            result[path] = attempt.type_text.encode("utf-8")
            continue
        try:
            data = attempt.read(alias)
        except KeyError:
            continue
        if data is not None:
            if path in result and result[path] != data:
                raise ValueError(f"conflicting pinned criterion aliases: {path}")
            result[path] = data
    return result
