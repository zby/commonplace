"""Artifact snapshot persistence."""

from __future__ import annotations

import sqlite3

from commonplace.freshness.versioning import ResolvedVersion
from commonplace.review.clock import iso_now
from commonplace.freshness.models import ArtifactSnapshot


def insert_or_get_snapshot(
    conn: sqlite3.Connection,
    *,
    resolved: ResolvedVersion,
    captured_at: str | None = None,
) -> ArtifactSnapshot:
    captured = captured_at or iso_now()
    conn.execute(
        """
        INSERT OR IGNORE INTO artifact_snapshots (
            artifact_path,
            version_kind,
            content_sha256,
            content_text,
            captured_at
        ) VALUES (?, ?, ?, ?, ?)
        """,
        (
            resolved.artifact_path,
            resolved.version_kind,
            resolved.content_sha256,
            resolved.content_text,
            captured,
        ),
    )
    row = conn.execute(
        """
        SELECT snapshot_id, artifact_path, content_sha256, content_text
        FROM artifact_snapshots
        WHERE artifact_path = ?
          AND version_kind = ?
          AND content_sha256 = ?
        """,
        (resolved.artifact_path, resolved.version_kind, resolved.content_sha256),
    ).fetchone()
    if row is None:
        raise RuntimeError(f"failed to load artifact snapshot: {resolved.artifact_path}")
    return ArtifactSnapshot(
        snapshot_id=int(row["snapshot_id"]),
        artifact_path=row["artifact_path"],
        content_sha256=row["content_sha256"],
        content_text=row["content_text"],
    )


def load_snapshot_by_id(conn: sqlite3.Connection, snapshot_id: int) -> ArtifactSnapshot | None:
    row = conn.execute(
        """
        SELECT snapshot_id, artifact_path, content_sha256, content_text
        FROM artifact_snapshots
        WHERE snapshot_id = ?
        """,
        (snapshot_id,),
    ).fetchone()
    if row is None:
        return None
    return ArtifactSnapshot(
        snapshot_id=int(row["snapshot_id"]),
        artifact_path=row["artifact_path"],
        content_sha256=row["content_sha256"],
        content_text=row["content_text"],
    )