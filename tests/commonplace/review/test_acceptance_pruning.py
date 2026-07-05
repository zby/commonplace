from __future__ import annotations

from pathlib import Path

from commonplace.review import review_db
from tests.commonplace.review.pair_helpers import accept_pair, source_gate_path


MODEL_PARTITION = "test-model"


def _insert_completed_job(
    conn,
    *,
    note_path: str,
    gate_ids: tuple[str, ...],
    reviewed_at: str,
) -> tuple[int, dict[str, int]]:
    job_id = review_db.create_job_with_pairs(
        conn,
        model_partition=MODEL_PARTITION,
        runner="test-runner",
        created_at=reviewed_at,
        status="queued",
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
                reviewed_at=reviewed_at,
            )
            for gate_id in gate_ids
        ],
        reviewed_at=reviewed_at,
    )
    review_db.complete_review_job(conn, review_job_id=job_id, completed_at=reviewed_at)
    pair_ids_by_path = {
        pair.gate_path: pair.review_pair_id
        for pair in review_db.load_review_pairs_for_job(conn, review_job_id=job_id)
    }
    return job_id, {gate_id: pair_ids_by_path[source_gate_path(gate_id)] for gate_id in gate_ids}


def test_inline_prune_keeps_bundled_job_until_all_pairs_are_superseded(tmp_path: Path) -> None:
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        bundled_job_id, bundled_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/mixed.md",
            gate_ids=("prose/source-residue", "semantic/grounding-alignment"),
            reviewed_at="2026-01-01T00:00:00Z",
        )
        source_job_id, source_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/mixed.md",
            gate_ids=("prose/source-residue",),
            reviewed_at="2026-01-02T00:00:00Z",
        )
        grounding_job_id, grounding_pairs = _insert_completed_job(
            conn,
            note_path="kb/notes/mixed.md",
            gate_ids=("semantic/grounding-alignment",),
            reviewed_at="2026-01-03T00:00:00Z",
        )

        accept_pair(
            conn,
            review_pair_id=bundled_pairs["prose/source-residue"],
            note_path="kb/notes/mixed.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-01T00:01:00Z",
        )
        accept_pair(
            conn,
            review_pair_id=bundled_pairs["semantic/grounding-alignment"],
            note_path="kb/notes/mixed.md",
            gate_id="semantic/grounding-alignment",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-01T00:02:00Z",
        )
        superseded_source = accept_pair(
            conn,
            review_pair_id=source_pairs["prose/source-residue"],
            note_path="kb/notes/mixed.md",
            gate_id="prose/source-residue",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-02T00:01:00Z",
        )

        first_deleted_jobs = review_db.prune_superseded_acceptances(conn, [superseded_source])
        bundled_job_after_first = conn.execute(
            "SELECT review_job_id FROM review_jobs WHERE review_job_id = ?",
            (bundled_job_id,),
        ).fetchone()
        retained_grounding_pair = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_pair_id = ?",
            (bundled_pairs["semantic/grounding-alignment"],),
        ).fetchone()
        deleted_source_pair = conn.execute(
            "SELECT review_pair_id FROM review_pairs WHERE review_pair_id = ?",
            (bundled_pairs["prose/source-residue"],),
        ).fetchone()

        superseded_grounding = accept_pair(
            conn,
            review_pair_id=grounding_pairs["semantic/grounding-alignment"],
            note_path="kb/notes/mixed.md",
            gate_id="semantic/grounding-alignment",
            model_partition=MODEL_PARTITION,
            accepted_at="2026-01-03T00:01:00Z",
        )
        second_deleted_jobs = review_db.prune_superseded_acceptances(conn, [superseded_grounding])
        review_job_ids = {
            int(row["review_job_id"])
            for row in conn.execute("SELECT review_job_id FROM review_jobs").fetchall()
        }
        acceptance_count = conn.execute("SELECT COUNT(*) FROM acceptance").fetchone()[0]

    assert first_deleted_jobs == set()
    assert bundled_job_after_first is not None
    assert retained_grounding_pair is not None
    assert deleted_source_pair is None
    assert second_deleted_jobs == {bundled_job_id}
    assert review_job_ids == {source_job_id, grounding_job_id}
    assert acceptance_count == 2


def _insert_completed_gate_packed_job(
    conn,
    *,
    note_paths: tuple[str, ...],
    gate_id: str,
    reviewed_at: str,
) -> int:
    gate_path = source_gate_path(gate_id)
    job_id = review_db.create_job_with_pairs(
        conn,
        model_partition=MODEL_PARTITION,
        runner="test-runner",
        created_at=reviewed_at,
        status="queued",
        packing="gate",
        pairs=[
            review_db.ReviewPairRequest(
                note_path=note_path,
                gate_path=gate_path,
                pair_ordinal=ordinal,
            )
            for ordinal, note_path in enumerate(note_paths, start=1)
        ],
    )
    review_db.complete_review_pairs(
        conn,
        review_job_id=job_id,
        review_pairs=[
            review_db.ReviewPairCompletion(
                note_path=note_path,
                gate_path=gate_path,
                decision="pass",
                reviewed_at=reviewed_at,
            )
            for note_path in note_paths
        ],
        reviewed_at=reviewed_at,
    )
    review_db.complete_review_job(conn, review_job_id=job_id, completed_at=reviewed_at)
    return job_id


def test_result_paths_stay_stable_when_a_sibling_pair_is_pruned(tmp_path: Path) -> None:
    """Derived result paths are a pure function of the pair row: pruning a
    superseded sibling (here, a basename-colliding note in a gate-packed job)
    must not change the surviving pair's result path."""
    db_path = tmp_path / "review-store.sqlite"
    review_db.ensure_db(db_path)

    with review_db.connect(db_path) as conn:
        bundled_job_id = _insert_completed_gate_packed_job(
            conn,
            note_paths=("kb/notes/x/sample.md", "kb/notes/y/sample.md"),
            gate_id="prose/source-residue",
            reviewed_at="2026-01-01T00:00:00Z",
        )
        pairs = review_db.load_review_pairs_for_job(conn, review_job_id=bundled_job_id)
        pair_by_note = {pair.note_path: pair for pair in pairs}
        for pair in pairs:
            review_db.upsert_acceptance(
                conn,
                note_path=pair.note_path,
                gate_path=pair.gate_path,
                model_partition=MODEL_PARTITION,
                accepted_review_pair_id=pair.review_pair_id,
                accepted_at="2026-01-01T00:00:00Z",
            )
        surviving_result_path_before = pair_by_note["kb/notes/y/sample.md"].result_path

        rereview_job_id = _insert_completed_gate_packed_job(
            conn,
            note_paths=("kb/notes/x/sample.md",),
            gate_id="prose/source-residue",
            reviewed_at="2026-01-02T00:00:00Z",
        )
        new_pair = review_db.load_review_pairs_for_job(conn, review_job_id=rereview_job_id)[0]
        superseded = review_db.upsert_acceptance(
            conn,
            note_path=new_pair.note_path,
            gate_path=new_pair.gate_path,
            model_partition=MODEL_PARTITION,
            accepted_review_pair_id=new_pair.review_pair_id,
            accepted_at="2026-01-02T00:00:00Z",
        )
        review_db.prune_superseded_acceptances(conn, [superseded])
        conn.commit()

        surviving_pairs = review_db.load_review_pairs_for_job(conn, review_job_id=bundled_job_id)
        assert [pair.note_path for pair in surviving_pairs] == ["kb/notes/y/sample.md"]
        assert surviving_pairs[0].result_path == surviving_result_path_before
