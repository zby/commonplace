from __future__ import annotations

import shutil
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
    assert "48 baselines" in result.stdout
    assert "4 skipped" in result.stdout
    assert "1 failed queued jobs" in result.stdout

    ensure_db(destination)
    with connect(destination) as conn:
        assert conn.execute("SELECT count(*) FROM artifact_snapshots").fetchone()[0] == 19
        assert conn.execute("SELECT count(*) FROM freshness_baselines").fetchone()[0] == 48
        assert conn.execute("SELECT count(*) FROM freshness_inputs").fetchone()[0] == 96
        failed = conn.execute(
            "SELECT failure_reason FROM review_jobs WHERE review_job_id = 49"
        ).fetchone()
        assert failed is not None
        assert failed[0] == "stale-queued-capture"