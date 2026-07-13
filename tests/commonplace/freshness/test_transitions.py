from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.hashing import content_sha256_for_text
from commonplace.freshness.transitions import (
    InputObservation,
    accept_target_observations,
    ack_target_inputs,
    retire_target,
)
from commonplace.review.review_db import connect, ensure_db, load_current_freshness_baselines, snapshot_file
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair


def _init_store(tmp_path: Path) -> Path:
    repo_root = tmp_path
    (repo_root / "kb" / "notes").mkdir(parents=True)
    (repo_root / "kb" / "instructions" / "review-gates" / "prose").mkdir(parents=True)
    note = repo_root / "kb/notes/example.md"
    gate = repo_root / "kb/instructions/review-gates/prose/source-residue.md"
    note.write_text("# Example\n", encoding="utf-8")
    gate.write_text("# Gate\n", encoding="utf-8")
    db_path = repo_root / "kb/reports/commonplace-store.sqlite"
    ensure_db(db_path)
    return db_path


def test_accept_rejects_unsupported_target_kind(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    with connect(db_path) as conn:
        with pytest.raises(ValueError, match="not supported for generic accept"):
            accept_target_observations(
                conn,
                repo_root=tmp_path,
                target_kind="collection-maintenance",
                target_key={"collection_path": "kb/notes"},
                inputs={
                    "contract": InputObservation(
                        input_role="contract",
                        artifact_path="kb/notes/example.md",
                        version_kind="file-text",
                        content_sha256=content_sha256_for_text(
                            (tmp_path / "kb/notes/example.md").read_text(encoding="utf-8")
                        ),
                    )
                },
                expected_baseline_revision=None,
            )


def test_accept_rejects_review_pair(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    with connect(db_path) as conn:
        with pytest.raises(ValueError, match="review-pair"):
            accept_target_observations(
                conn,
                repo_root=tmp_path,
                target_kind="review-pair",
                target_key={
                    "note_path": "kb/notes/example.md",
                    "criterion_path": "kb/instructions/review-gates/prose/source-residue.md",
                    "model_partition": "codex",
                },
                inputs={},
                expected_baseline_revision=None,
            )


def test_retire_target_is_idempotent(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    with connect(db_path) as conn:
        pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            outcome="pass",
            completed_at="2026-07-13T00:00:00+00:00",
        )
        accept_pair(
            conn,
            review_pair_id=pair_id,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            baseline_updated_at="2026-07-13T00:00:00+00:00",
        )
        target_key = {
            "note_path": "kb/notes/example.md",
            "criterion_path": "kb/instructions/review-gates/prose/source-residue.md",
            "model_partition": "codex",
        }
        assert retire_target(conn, target_kind="review-pair", target_key=target_key) is True
        assert retire_target(conn, target_kind="review-pair", target_key=target_key) is False
        assert load_current_freshness_baselines(conn) == {}


def test_ack_advances_baseline_revision(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    note = tmp_path / "kb/notes/example.md"
    gate = tmp_path / "kb/instructions/review-gates/prose/source-residue.md"
    with connect(db_path) as conn:
        note_snapshot = snapshot_file(conn, repo_root=tmp_path, path="kb/notes/example.md")
        criterion_snapshot = snapshot_file(
            conn,
            repo_root=tmp_path,
            path="kb/instructions/review-gates/prose/source-residue.md",
        )
        pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            outcome="pass",
            completed_at="2026-07-13T00:00:00+00:00",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=pair_id,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            baseline_updated_at="2026-07-13T00:00:00+00:00",
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        note.write_text("# Example changed\n", encoding="utf-8")
        ack_target_inputs(
            conn,
            repo_root=tmp_path,
            target_kind="review-pair",
            target_key={
                "note_path": "kb/notes/example.md",
                "criterion_path": "kb/instructions/review-gates/prose/source-residue.md",
                "model_partition": "codex",
            },
            expected_baseline_revision=1,
            selected_inputs=(
                InputObservation(
                    input_role="note",
                    artifact_path="kb/notes/example.md",
                    version_kind="file-text",
                    content_sha256=content_sha256_for_text(note.read_text(encoding="utf-8")),
                ),
            ),
            accepted_at="2026-07-13T01:00:00+00:00",
        )
        baselines = load_current_freshness_baselines(conn)
        baseline = baselines[("kb/notes/example.md", "kb/instructions/review-gates/prose/source-residue.md", "codex")]
        assert baseline.evidence_review_pair_id == pair_id
        assert baseline.baseline_note_text == "# Example changed\n"
        assert baseline.baseline_criterion_text == gate.read_text(encoding="utf-8")


def test_ack_rejects_decoy_artifact_path(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    decoy = tmp_path / "kb/notes/decoy.md"
    decoy.write_text("unchanged\n", encoding="utf-8")
    note = tmp_path / "kb/notes/example.md"
    with connect(db_path) as conn:
        note_snapshot = snapshot_file(conn, repo_root=tmp_path, path="kb/notes/example.md")
        criterion_snapshot = snapshot_file(
            conn,
            repo_root=tmp_path,
            path="kb/instructions/review-gates/prose/source-residue.md",
        )
        pair_id = insert_completed_pair(
            conn,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            outcome="pass",
            completed_at="2026-07-13T00:00:00+00:00",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=pair_id,
            note_path="kb/notes/example.md",
            criterion_id="prose/source-residue",
            model_partition="codex",
            baseline_updated_at="2026-07-13T00:00:00+00:00",
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        note.write_text("# changed\n", encoding="utf-8")
        with pytest.raises(ValueError, match="artifact_path for note must be"):
            ack_target_inputs(
                conn,
                repo_root=tmp_path,
                target_kind="review-pair",
                target_key={
                    "note_path": "kb/notes/example.md",
                    "criterion_path": "kb/instructions/review-gates/prose/source-residue.md",
                    "model_partition": "codex",
                },
                expected_baseline_revision=1,
                selected_inputs=(
                    InputObservation(
                        input_role="note",
                        artifact_path="kb/notes/decoy.md",
                        version_kind="file-text",
                        content_sha256=content_sha256_for_text(decoy.read_text(encoding="utf-8")),
                    ),
                ),
            )


def test_retire_recreate_advances_revision_and_rejects_stale_finalize(tmp_path: Path) -> None:
    from commonplace.freshness.keys import review_pair_target_key
    from commonplace.review.review_db import (
        ReviewPairCompletion,
        ReviewPairRequest,
        complete_review_job,
        complete_review_pairs,
        create_job_with_pairs,
        load_review_pairs_for_job,
        upsert_freshness_baseline,
    )

    db_path = _init_store(tmp_path)
    note_path = "kb/notes/example.md"
    criterion_path = "kb/instructions/review-gates/prose/source-residue.md"
    target_key = {
        "note_path": note_path,
        "criterion_path": criterion_path,
        "model_partition": "codex",
    }

    with connect(db_path) as conn:
        note_snapshot = snapshot_file(conn, repo_root=tmp_path, path=note_path)
        criterion_snapshot = snapshot_file(conn, repo_root=tmp_path, path=criterion_path)
        pair1 = insert_completed_pair(
            conn,
            note_path=note_path,
            criterion_id="prose/source-residue",
            model_partition="codex",
            outcome="pass",
            completed_at="2026-07-13T00:00:00+00:00",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=pair1,
            note_path=note_path,
            criterion_id="prose/source-residue",
            model_partition="codex",
            baseline_updated_at="2026-07-13T00:00:00+00:00",
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )

        job_id = create_job_with_pairs(
            conn,
            model_partition="codex",
            runner=None,
            created_at="2026-07-13T01:00:00+00:00",
            status="queued",
            grouping="note",
            pairs=[
                ReviewPairRequest(
                    note_path=note_path,
                    criterion_path=criterion_path,
                    pair_ordinal=1,
                    result_kind="verdict",
                    reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                    reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
                )
            ],
        )
        queued = load_review_pairs_for_job(conn, review_job_id=job_id)[0]
        assert queued.expected_baseline_revision == 1

        retire_target(conn, target_kind="review-pair", target_key=target_key)

        pair2 = insert_completed_pair(
            conn,
            note_path=note_path,
            criterion_id="prose/source-residue",
            model_partition="codex",
            outcome="pass",
            completed_at="2026-07-13T02:00:00+00:00",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )
        accept_pair(
            conn,
            review_pair_id=pair2,
            note_path=note_path,
            criterion_id="prose/source-residue",
            model_partition="codex",
            baseline_updated_at="2026-07-13T02:00:00+00:00",
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
        )

        key_json = review_pair_target_key(
            note_path=note_path,
            criterion_path=criterion_path,
            model_partition="codex",
        )
        row = conn.execute(
            """
            SELECT revision
            FROM freshness_baselines
            WHERE target_kind = 'review-pair' AND target_key_json = ?
            """,
            (key_json,),
        ).fetchone()
        assert row is not None
        assert int(row["revision"]) == 2

        complete_review_pairs(
            conn,
            review_job_id=job_id,
            review_pairs=[
                ReviewPairCompletion(
                    note_path=note_path,
                    criterion_path=criterion_path,
                    outcome="pass",
                )
            ],
            completed_at="2026-07-13T03:00:00+00:00",
        )
        complete_review_job(conn, review_job_id=job_id, completed_at="2026-07-13T03:00:00+00:00")

        with pytest.raises(ValueError, match="stale-baseline-revision"):
            upsert_freshness_baseline(
                conn,
                note_path=note_path,
                criterion_path=criterion_path,
                model_partition="codex",
                evidence_review_pair_id=queued.review_pair_id,
                baseline_note_snapshot_id=queued.reviewed_note_snapshot_id,
                baseline_criterion_snapshot_id=queued.reviewed_criterion_snapshot_id,
                baseline_updated_at="2026-07-13T03:00:00+00:00",
                expected_baseline_revision=queued.expected_baseline_revision,
                capture_refresh=True,
            )