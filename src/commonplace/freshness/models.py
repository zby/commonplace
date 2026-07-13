"""Freshness data types."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArtifactSnapshot:
    snapshot_id: int
    artifact_path: str
    content_sha256: str
    content_text: str

    @property
    def path(self) -> str:
        return self.artifact_path