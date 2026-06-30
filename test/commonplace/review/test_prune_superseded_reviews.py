from __future__ import annotations

from pathlib import Path

from commonplace.review.artifacts import encode_stage_filename
from commonplace.review import executor, review_db
from test.commonplace.review.pair_helpers import accept_pair, source_gate_path

from ._run_cli import run_cli


MODEL_PARTITION = "test-model"


def _prepare_db(repo: Path) -> Path:
    db_path = repo / "kb" / "reports" / "review-store.sqlite"
    review_db.ensure_db(db_path)
    return db_path


def _insert_completed_job(
    conn,
    *,
    note_path: str,
    gate_ids: tuple[str, ...],
    started_at: str,
) -> tuple[int, dict[str, int]]:
    job_id = review_db.create_job_with_pairs(
        conn,
        model_partition=MODEL_PARTITION,
        runner="test-runner",
        created_at=started_at,
        started_at=started_at,
        status="running",
        packing="note",
        pairs=[
            review_db.ReviewPairRequest(
                note_path=note_path,
                gate_path=source_gate_path(gate_id),
                pair_ordinal=ordinal,
            )
            for ordinal, gate_id in enumerate(gate_ids)
        ],
    )
    review_db.complete_review_pairs(
        conn,
        review_job_id=job_id,
        review_pairs=[
            review_db.ReviewPairCompletion(
                note_path=note_path,
                gate_path=source_gate_path(gate_id),
                decision="pass",
                reviewed_at=started_at,
            )
            for gate_id in gate_ids
        ],
        reviewed_at=started_at,
    )
    review_db.complete_review_job(conn, review_job_id=job_id, completed_at=started_at)
    pair_ids_by_path = {
        pair.gate_path: pair.review_pair_id
        for pair in review_db.load_review_pairs_for_job(conn, review_job_id=job_id)
    }
    pair_ids = {gate_id: pair_ids_by_path[source_gate_path(gate_id)] for gate_id in gate_ids}
    return job_id, pair_ids


def _write_job_artifacts(repo: Path, review_job_id: int, gate_ids: tuple[str, ...]) -> Path:
    artifact_dir = executor.bundle_artifact_dir(repo, review_job_id)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "bundle-output.md").write_text("raw bundle output\n", encoding="utf-8")
    (artifact_dir / "prompt.md").write_text("prompt\n", encoding="utf-8")
    for gate_id in gate_ids:
        (artifact_dir / encode_stage_filename(gate_id)).write_text(
            f"{gate_id} review\n",
            encoding="utf-8",
        )
    return artifact_dir


def test_prune_superseded_reviews_deletes_rows_and_whole_obsolete_job_artifacts(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    db_path = _prepare_db(repo)

    with review_db.connect(db_path) as conn:
        mixed_job, mixed_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/mixed.md",
            gate_ids=("prose/source-residue", "semantic/grounding-alignment"),
            started_at="2026-01-01T00:00:00Z",
        )
        current_source_job, current_source_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/mixed.md",
            gate_ids=("prose/source-residue",),
            started_at="2026-01-02T00:00:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=mixed_pairs["prose/source-residue"],
            note_path="kb/notes/mixed.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-01T00:02:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=current_source_pairs["prose/source-residue"],
            note_path="kb/notes/mixed.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-02T00:01:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=mixed_pairs["semantic/grounding-alignment"],
            note_path="kb/notes/mixed.md",
            gate_id="semantic/grounding-alignment",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-01T00:03:00Z",
        )

        old_full_job, old_full_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/full.md",
            gate_ids=("prose/source-residue",),
            started_at="2026-01-03T00:00:00Z",
        )
        current_full_job, current_full_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/full.md",
            gate_ids=("prose/source-residue",),
            started_at="2026-01-04T00:00:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=old_full_pairs["prose/source-residue"],
            note_path="kb/notes/full.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-03T00:01:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=current_full_pairs["prose/source-residue"],
            note_path="kb/notes/full.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-04T00:01:00Z",
        )

        ack_old_job, ack_old_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/ack.md",
            gate_ids=("prose/source-residue",),
            started_at="2026-01-05T00:00:00Z",
        )
        ack_latest_job, ack_latest_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/ack.md",
            gate_ids=("prose/source-residue",),
            started_at="2026-01-06T00:00:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=ack_old_pairs["prose/source-residue"],
            note_path="kb/notes/ack.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-05T00:01:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=None,
            note_path="kb/notes/ack.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-06T00:01:00Z",
        )
        conn.commit()

    mixed_artifacts = _write_job_artifacts(
        repo,
        mixed_job,
        ("prose/source-residue", "semantic/grounding-alignment"),
    )
    old_full_artifacts = _write_job_artifacts(repo, old_full_job, ("prose/source-residue",))
    _write_job_artifacts(repo, ack_old_job, ("prose/source-residue",))
    _write_job_artifacts(repo, ack_latest_job, ("prose/source-residue",))

    dry_run = run_cli("prune_superseded_reviews", "--dry-run", cwd=repo, db_path=db_path)

    assert "obsolete_acceptance_events: 3" in dry_run.stdout
    assert "obsolete_review_pairs: 3" in dry_run.stdout
    assert "obsolete_review_jobs: 2" in dry_run.stdout
    assert "obsolete_job_artifact_dirs: 2" in dry_run.stdout
    assert "mode: dry-run" in dry_run.stdout
    assert old_full_artifacts.exists()
    assert mixed_artifacts.exists()

    applied = run_cli("prune_superseded_reviews", "--apply", cwd=repo, db_path=db_path)

    assert "mode: apply" in applied.stdout
    assert not old_full_artifacts.exists()
    assert mixed_artifacts.exists()
    assert (mixed_artifacts / encode_stage_filename("prose/source-residue")).exists()
    assert (mixed_artifacts / encode_stage_filename("semantic/grounding-alignment")).exists()

    with review_db.connect(db_path) as conn:
        review_pair_ids = {
            int(row["review_pair_id"])
            for row in conn.execute("SELECT review_pair_id FROM review_pairs ORDER BY review_pair_id").fetchall()
        }
        assert review_pair_ids == {
            mixed_pairs["semantic/grounding-alignment"],
            current_source_pairs["prose/source-residue"],
            current_full_pairs["prose/source-residue"],
            ack_latest_pairs["prose/source-residue"],
        }
        review_job_ids = {
            int(row["review_job_id"])
            for row in conn.execute("SELECT review_job_id FROM review_jobs ORDER BY review_job_id").fetchall()
        }
        assert review_job_ids == {mixed_job, current_source_job, current_full_job, ack_latest_job}
        acceptance_count = int(conn.execute("SELECT COUNT(*) FROM acceptance_events").fetchone()[0])
        assert acceptance_count == 4
