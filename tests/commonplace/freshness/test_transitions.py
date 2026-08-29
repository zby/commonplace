from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.freshness.transitions import (
    InputObservation,
    ack_target_inputs,
    retire_target,
)
from commonplace.lib.hashing import content_sha256_for_text
from commonplace.review.review_db import (
    connect,
    ensure_db,
    load_current_freshness_baselines,
    snapshot_file,
)
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair

NOTE_PATH = "kb/notes/example.md"
CRITERION_PATH = "kb/instructions/review-gates/prose/source-residue.md"
CRITERION_ID = "prose/source-residue"
MODEL_PARTITION = "codex"
INITIAL_REVIEWED_AT = "2026-07-13T00:00:00+00:00"


def _target_key() -> dict[str, str]:
    return {
        "note_path": NOTE_PATH,
        "criterion_path": CRITERION_PATH,
        "model_partition": MODEL_PARTITION,
    }


def _init_store(tmp_path: Path) -> Path:
    repo_root = tmp_path
    (repo_root / "kb" / "notes").mkdir(parents=True)
    (repo_root / "kb" / "instructions" / "review-gates" / "prose").mkdir(parents=True)
    note = repo_root / NOTE_PATH
    gate = repo_root / CRITERION_PATH
    note.write_text("# Example\n", encoding="utf-8")
    gate.write_text("# Gate\n", encoding="utf-8")
    db_path = repo_root / "kb/reports/state/commonplace-store.sqlite"
    ensure_db(db_path)
    return db_path


def _seed_accepted_baseline(
    conn,
    repo_root: Path,
    *,
    reviewed_at: str = INITIAL_REVIEWED_AT,
) -> tuple[int, int, int]:
    note_snapshot = snapshot_file(conn, repo_root=repo_root, path=NOTE_PATH)
    criterion_snapshot = snapshot_file(
        conn,
        repo_root=repo_root,
        path=CRITERION_PATH,
    )
    pair_id = insert_completed_pair(
        conn,
        note_path=NOTE_PATH,
        criterion_id=CRITERION_ID,
        model_partition=MODEL_PARTITION,
        outcome="pass",
        completed_at=reviewed_at,
        reviewed_note_snapshot_id=note_snapshot.snapshot_id,
        reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
    )
    accept_pair(
        conn,
        review_pair_id=pair_id,
        note_path=NOTE_PATH,
        criterion_id=CRITERION_ID,
        model_partition=MODEL_PARTITION,
        baseline_updated_at=reviewed_at,
        baseline_note_snapshot_id=note_snapshot.snapshot_id,
        baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
    )
    return pair_id, note_snapshot.snapshot_id, criterion_snapshot.snapshot_id


def test_retire_target_is_idempotent(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    with connect(db_path) as conn:
        _seed_accepted_baseline(conn, tmp_path)
        target_key = _target_key()
        first_retirement = retire_target(
            conn,
            target_kind="review-pair",
            target_key=target_key,
        )
        repeated_retirement = retire_target(
            conn,
            target_kind="review-pair",
            target_key=target_key,
        )
        remaining = load_current_freshness_baselines(conn)

    assert (first_retirement, repeated_retirement, remaining) == (True, False, {})


def test_ack_advances_baseline_revision(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    note = tmp_path / "kb/notes/example.md"
    gate = tmp_path / "kb/instructions/review-gates/prose/source-residue.md"
    with connect(db_path) as conn:
        pair_id, _, _ = _seed_accepted_baseline(conn, tmp_path)
        note.write_text("# Example changed\n", encoding="utf-8")
        ack_target_inputs(
            conn,
            repo_root=tmp_path,
            target_kind="review-pair",
            target_key=_target_key(),
            expected_baseline_revision=1,
            selected_inputs=(
                InputObservation(
                    input_role="note",
                    artifact_path=NOTE_PATH,
                    version_kind="file-text",
                    content_sha256=content_sha256_for_text(note.read_text(encoding="utf-8")),
                ),
            ),
            accepted_at="2026-07-13T01:00:00+00:00",
        )
        baselines = load_current_freshness_baselines(conn)
        baseline = baselines[(NOTE_PATH, CRITERION_PATH, MODEL_PARTITION)]
        assert baseline.evidence_review_pair_id == pair_id
        assert baseline.baseline_note_text == "# Example changed\n"
        assert baseline.baseline_criterion_text == gate.read_text(encoding="utf-8")


def test_ack_rejects_decoy_artifact_path(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    decoy = tmp_path / "kb/notes/decoy.md"
    decoy.write_text("unchanged\n", encoding="utf-8")
    note = tmp_path / "kb/notes/example.md"
    with connect(db_path) as conn:
        _seed_accepted_baseline(conn, tmp_path)
        note.write_text("# changed\n", encoding="utf-8")
        with pytest.raises(ValueError, match="artifact_path for note must be"):
            ack_target_inputs(
                conn,
                repo_root=tmp_path,
                target_kind="review-pair",
                target_key=_target_key(),
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


def test_upsert_observation_rejects_mismatched_expected_revision(tmp_path: Path) -> None:
    from commonplace.review import review_db

    db_path = _init_store(tmp_path)
    with connect(db_path) as conn:
        pair_id, note_snapshot_id, criterion_snapshot_id = _seed_accepted_baseline(
            conn,
            tmp_path,
        )
        with pytest.raises(ValueError, match="stale-baseline-revision"):
            review_db.upsert_freshness_baseline(
                conn,
                note_path=NOTE_PATH,
                criterion_path=CRITERION_PATH,
                model_partition=MODEL_PARTITION,
                evidence_review_pair_id=pair_id,
                baseline_note_snapshot_id=note_snapshot_id,
                baseline_criterion_snapshot_id=criterion_snapshot_id,
                baseline_updated_at="2026-07-13T01:00:00+00:00",
                expected_baseline_revision=99,
                capture_refresh=False,
            )


def test_finalize_rejects_missing_baseline_after_retire_aba(tmp_path: Path) -> None:
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
    note_path = NOTE_PATH
    criterion_path = CRITERION_PATH
    target_key = _target_key()

    with connect(db_path) as conn:
        note_snapshot = snapshot_file(conn, repo_root=tmp_path, path=note_path)
        criterion_snapshot = snapshot_file(conn, repo_root=tmp_path, path=criterion_path)

        job_id = create_job_with_pairs(
            conn,
            model_partition=MODEL_PARTITION,
            runner=None,
            created_at="2026-07-13T00:00:00+00:00",
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

        _seed_accepted_baseline(
            conn,
            tmp_path,
            reviewed_at="2026-07-13T01:00:00+00:00",
        )
        retire_target(conn, target_kind="review-pair", target_key=target_key)

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
            completed_at="2026-07-13T02:00:00+00:00",
        )
        complete_review_job(conn, review_job_id=job_id, completed_at="2026-07-13T02:00:00+00:00")

        with pytest.raises(ValueError, match="baseline generation advanced since queue"):
            upsert_freshness_baseline(
                conn,
                note_path=note_path,
                criterion_path=criterion_path,
                model_partition=MODEL_PARTITION,
                evidence_review_pair_id=queued.review_pair_id,
                baseline_note_snapshot_id=queued.reviewed_note_snapshot_id,
                baseline_criterion_snapshot_id=queued.reviewed_criterion_snapshot_id,
                baseline_updated_at="2026-07-13T02:00:00+00:00",
                expected_baseline_revision=queued.expected_baseline_revision,
                expected_generation_next_revision=queued.expected_generation_next_revision,
                capture_refresh=True,
            )


def test_ack_rejects_empty_selected_inputs(tmp_path: Path) -> None:
    db_path = _init_store(tmp_path)
    with connect(db_path) as conn:
        _seed_accepted_baseline(conn, tmp_path)
        with pytest.raises(ValueError, match="selected_inputs must not be empty"):
            ack_target_inputs(
                conn,
                repo_root=tmp_path,
                target_kind="review-pair",
                target_key=_target_key(),
                expected_baseline_revision=1,
                selected_inputs=(),
            )


def test_ack_uses_caller_revision_at_finalize(tmp_path: Path) -> None:
    from commonplace.freshness import baselines as freshness_baselines

    db_path = _init_store(tmp_path)
    note = tmp_path / "kb/notes/example.md"
    with connect(db_path) as conn:
        pair_id, note_snapshot_id, criterion_snapshot_id = _seed_accepted_baseline(
            conn,
            tmp_path,
        )
        note.write_text("# changed once\n", encoding="utf-8")
        ack_target_inputs(
            conn,
            repo_root=tmp_path,
            target_kind="review-pair",
            target_key=_target_key(),
            expected_baseline_revision=1,
            selected_inputs=(
                InputObservation(
                    input_role="note",
                    artifact_path=NOTE_PATH,
                    version_kind="file-text",
                    content_sha256=content_sha256_for_text(note.read_text(encoding="utf-8")),
                ),
            ),
            accepted_at="2026-07-13T00:30:00+00:00",
        )
        with pytest.raises(ValueError, match="stale-baseline-revision"):
            freshness_baselines.refresh_review_baseline_from_observation(
                conn,
                note_path=NOTE_PATH,
                criterion_path=CRITERION_PATH,
                model_partition=MODEL_PARTITION,
                evidence_review_pair_id=pair_id,
                baseline_note_snapshot_id=note_snapshot_id,
                baseline_criterion_snapshot_id=criterion_snapshot_id,
                expected_baseline_revision=1,
                accepted_at="2026-07-13T01:00:00+00:00",
            )


def test_retire_recreate_advances_revision_and_rejects_stale_finalize(tmp_path: Path) -> None:
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
    note_path = NOTE_PATH
    criterion_path = CRITERION_PATH
    target_key = _target_key()

    with connect(db_path) as conn:
        _, note_snapshot_id, criterion_snapshot_id = _seed_accepted_baseline(
            conn,
            tmp_path,
        )

        job_id = create_job_with_pairs(
            conn,
            model_partition=MODEL_PARTITION,
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
                    reviewed_note_snapshot_id=note_snapshot_id,
                    reviewed_criterion_snapshot_id=criterion_snapshot_id,
                )
            ],
        )
        queued = load_review_pairs_for_job(conn, review_job_id=job_id)[0]

        retire_target(conn, target_kind="review-pair", target_key=target_key)

        _seed_accepted_baseline(
            conn,
            tmp_path,
            reviewed_at="2026-07-13T02:00:00+00:00",
        )

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
                model_partition=MODEL_PARTITION,
                evidence_review_pair_id=queued.review_pair_id,
                baseline_note_snapshot_id=queued.reviewed_note_snapshot_id,
                baseline_criterion_snapshot_id=queued.reviewed_criterion_snapshot_id,
                baseline_updated_at="2026-07-13T03:00:00+00:00",
                expected_baseline_revision=queued.expected_baseline_revision,
                expected_generation_next_revision=queued.expected_generation_next_revision,
                capture_refresh=True,
            )
