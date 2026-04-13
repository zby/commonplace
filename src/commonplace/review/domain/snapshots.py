"""Value objects for review freshness decisions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NoteSnapshot:
    path: str
    blob_sha: str


@dataclass(frozen=True)
class GateSnapshot:
    id: str
    blob_sha: str


@dataclass(frozen=True)
class AcceptanceSnapshot:
    accepted_note_sha: str
    accepted_gate_sha: str
