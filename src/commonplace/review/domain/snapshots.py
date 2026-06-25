"""Value objects for review freshness decisions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NoteSnapshot:
    path: str
    content_hash: str


@dataclass(frozen=True)
class GateSnapshot:
    id: str
    content_hash: str


@dataclass(frozen=True)
class AcceptanceSnapshot:
    accepted_note_hash: str
    accepted_gate_hash: str
