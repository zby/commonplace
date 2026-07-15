from __future__ import annotations

import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.review.review_db import connect, ensure_db


REPO_ROOT = Path(__file__).resolve().parents[3]
LIVE_SOURCE = REPO_ROOT / "kb/reports/review-store.sqlite"


@pytest.mark.skipif(not LIVE_SOURCE.is_file(), reason="live review-store.sqlite not present")
def test_live_migration_fixture_counts(tmp_path: Path) -> None:
    source = tmp_path / "review-store.sqlite"
    destination = tmp_path / "commonplace-store.sqlite"
    shutil.copy2(LIVE_SOURCE, source)
    with sqlite3.connect(source) as source_conn:
        source_version = int(source_conn.execute("PRAGMA user_version").fetchone()[0])
        if source_version != 7:
            pytest.skip(f"live review-store.sqlite is schema v{source_version}, not v7")
        source_counts = {
            "review_jobs": source_conn.execute("SELECT count(*) FROM review_jobs").fetchone()[0],
            "review_pairs": source_conn.execute("SELECT count(*) FROM review_pairs").fetchone()[0],
            "review_file_snapshots": source_conn.execute(
                "SELECT count(*) FROM review_file_snapshots"
            ).fetchone()[0],
            "freshness_baselines": source_conn.execute(
                "SELECT count(*) FROM freshness_baselines"
            ).fetchone()[0],
        }
        migratable_baselines = sum(
            1
            for note_path, criterion_path in source_conn.execute(
                "SELECT note_path, criterion_path FROM freshness_baselines"
            ).fetchall()
            if (REPO_ROOT / note_path).is_file() and (REPO_ROOT / criterion_path).is_file()
        )
        skipped_baselines = source_counts["freshness_baselines"] - migratable_baselines

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts/migrate-review-db-v7-to-commonplace-store.py"),
            "--repo-root",
            str(REPO_ROOT),
            "--source",
            str(source),
            "--destination",
            str(destination),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert f"{migratable_baselines} baselines" in result.stdout
    assert f"{skipped_baselines} skipped" in result.stdout

    ensure_db(destination)
    with connect(destination) as conn:
        assert (
            conn.execute("SELECT count(*) FROM artifact_snapshots").fetchone()[0]
            == source_counts["review_file_snapshots"]
        )
        assert (
            conn.execute("SELECT count(*) FROM review_jobs").fetchone()[0]
            == source_counts["review_jobs"]
        )
        assert (
            conn.execute("SELECT count(*) FROM review_pairs").fetchone()[0]
            == source_counts["review_pairs"]
        )
        assert (
            conn.execute("SELECT count(*) FROM freshness_baselines").fetchone()[0]
            == migratable_baselines
        )
        assert (
            conn.execute("SELECT count(*) FROM freshness_inputs").fetchone()[0]
            == migratable_baselines * 2
        )
        assert (
            conn.execute("SELECT count(*) FROM review_freshness_evidence").fetchone()[0]
            == migratable_baselines
        )
