"""Review freshness classification."""

from __future__ import annotations

from dataclasses import dataclass

from commonplace.review.domain.snapshots import AcceptanceSnapshot, GateSnapshot, NoteSnapshot


@dataclass(frozen=True)
class Staleness:
    reason: str


def classify_staleness(
    note: NoteSnapshot,
    gate: GateSnapshot,
    acceptance: AcceptanceSnapshot | None,
) -> Staleness | None:
    if acceptance is None:
        return Staleness("missing-review")
    if acceptance.accepted_gate_sha != gate.blob_sha:
        return Staleness("gate-changed")
    if acceptance.accepted_note_sha != note.blob_sha:
        return Staleness("note-changed")
    return None
