"""Value objects for review freshness decisions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NoteSnapshot:
    path: str
    blob_sha: str
    commit: str | None = None
    text: str | None = None


@dataclass(frozen=True)
class GateSnapshot:
    id: str
    blob_sha: str
    commit: str | None = None
    watches: frozenset[str] = frozenset()
    requires_trait: str | None = None
    requires_type: str | None = None
    body: str | None = None


@dataclass(frozen=True)
class AcceptanceSnapshot:
    note_path: str
    gate_id: str
    model_id: str
    accepted_note_sha: str
    accepted_gate_sha: str
    accepted_note_commit: str | None = None
    accepted_at: str | None = None
    acceptance_kind: str | None = None
