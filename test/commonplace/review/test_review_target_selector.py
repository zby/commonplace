from __future__ import annotations

import json
import sqlite3
import subprocess
from pathlib import Path

import pytest

from commonplace.review import resolve_gates, review_db, review_target_selector
from test.commonplace.review.pair_helpers import accept_pair, insert_completed_pair

from ._run_cli import run_cli

TEST_MODEL = "test-model"
PLACEHOLDER_COMMIT = "0" * 40
REVIEWED_AT = "2026-03-31T00:00:00+00:00"


def db_path_for(repo_root: Path) -> Path:
    return repo_root / "kb" / "reports" / "review-store.sqlite"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(
    path: Path,
    title: str,
    body: str,
    *,
    status: str = "current",
    traits: str = "[]",
    note_type: str = "kb/types/note.md",
) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: {note_type}
traits: {traits}
status: {status}
---

# {title}
{body}
""",
    )


def make_gate(
    path: Path,
    gate_id: str,
    lens: str,
    *,
    requires_trait: str | None = None,
    requires_type: str | None = None,
) -> Path:
    requires_trait_line = f"requires_trait: {requires_trait}\n" if requires_trait else ""
    requires_type_line = f"requires-type: {requires_type}\n" if requires_type else ""
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
watches: [body]
staleness: changed
{requires_trait_line}{requires_type_line}---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
    )


def seed_acceptance(
    repo_root: Path,
    *,
    note_path: str,
    note_abs: Path,
    gate_abs: Path,
    gate_id: str,
    commit: str = PLACEHOLDER_COMMIT,
) -> None:
    """Insert a completed review pair + acceptance as if a full review passed."""
    review_db.ensure_db(db_path_for(repo_root))
    gate_path = gate_abs.relative_to(repo_root).as_posix()
    with review_db.connect(db_path_for(repo_root)) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=note_path)
        gate_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=gate_path)
        review_pair_id = insert_completed_pair(
            conn,
            note_path=note_path,
            gate_id=gate_id,
            model_partition=TEST_MODEL,
            decision="pass",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
            reviewed_at=REVIEWED_AT,
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path=note_path,
            gate_id=gate_id,
            model_partition=TEST_MODEL,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at=REVIEWED_AT,
        )
        conn.commit()


def seed_snapshot_acceptance(
    repo_root: Path,
    *,
    note_path: str,
    gate_path: str,
) -> None:
    review_db.ensure_db(db_path_for(repo_root))
    with review_db.connect(db_path_for(repo_root)) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=note_path)
        gate_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=gate_path)
        review_run_id = review_db.create_run_with_pairs(
            conn,
            model_partition=TEST_MODEL,
            runner="test-runner",
            started_at=REVIEWED_AT,
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path=note_path,
                    gate_path=gate_path,
                    pair_ordinal=0,
                    reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                    reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
                )
            ],
        )
        review_db.complete_review_pairs(
            conn,
            review_run_id=review_run_id,
            review_pairs=[
                review_db.ReviewPairCompletion(
                    note_path=note_path,
                    gate_path=gate_path,
                    decision="pass",
                    reviewed_at=REVIEWED_AT,
                )
            ],
            reviewed_at=REVIEWED_AT,
        )
        review_pair = review_db.load_review_pairs_for_run(conn, review_run_id=review_run_id)[0]
        review_db.append_acceptance_event(
            conn,
            note_path=note_path,
            gate_path=gate_path,
            model_partition=TEST_MODEL,
            accepted_review_pair_id=review_pair.review_pair_id,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at=REVIEWED_AT,
        )
        conn.commit()


def build_fixture(tmp_path: Path) -> dict[str, Path]:
    """2 notes + 3 gates; `stable` has 3 accepted reviews, `unreviewed` has none."""
    notes_dir = tmp_path / "kb" / "notes"
    gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

    stable = make_note(notes_dir / "stable.md", "Stable title", "\nLine 1.\nLine 2.\n")
    unreviewed = make_note(notes_dir / "unreviewed.md", "Unreviewed title", "\nBody.\n")

    g1 = make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")
    g2 = make_gate(
        gates_dir / "prose" / "confidence-miscalibration.md",
        "prose/confidence-miscalibration",
        "prose",
    )
    g3 = make_gate(
        gates_dir / "semantic" / "grounding-alignment.md",
        "semantic/grounding-alignment",
        "semantic",
    )

    for gate_id, gate_abs in [
        ("prose/source-residue", g1),
        ("prose/confidence-miscalibration", g2),
        ("semantic/grounding-alignment", g3),
    ]:
        seed_acceptance(
            tmp_path,
            note_path="kb/notes/stable.md",
            note_abs=stable,
            gate_abs=gate_abs,
            gate_id=gate_id,
        )

    return {
        "stable": stable,
        "unreviewed": unreviewed,
        "gate_prose_sr": g1,
        "gate_prose_cm": g2,
        "gate_semantic_ga": g3,
    }


class TestMissingReview:
    def test_missing_review_marks_stale(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/confidence-miscalibration", "missing-review"),
            ("prose/source-residue", "missing-review"),
        ]

    def test_missing_review_without_model_partition_uses_any_partition_coverage(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)

        stable = review_target_selector.select_stale_gates(
            tmp_path,
            model=None,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        unreviewed = review_target_selector.select_stale_gates(
            tmp_path,
            model=None,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )

        assert stable == []
        assert [(s.gate_id, s.reason) for s in unreviewed] == [
            ("prose/confidence-miscalibration", "missing-review"),
            ("prose/source-residue", "missing-review"),
        ]

    def test_claude_opus_alias_queries_canonical_partition(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        with review_db.connect(db_path_for(tmp_path)) as conn:
            review_db.rekey_model_partition(conn, old_model_partition=TEST_MODEL, new_model_partition="claude-opus")
            conn.commit()

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model="opus-4-6",
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )

        assert stale == []

    def test_all_gates_finds_missing_across_bundles(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue", "semantic/grounding-alignment"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        gate_ids = [s.gate_id for s in stale]
        assert "prose/source-residue" in gate_ids
        assert "semantic/grounding-alignment" in gate_ids

    def test_current_filter_limits_selection_to_current_notes(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "current-top.md", "Current top", "\nBody.\n", status="current")
        make_note(notes_dir / "archived.md", "Archived", "\nBody.\n", status="archived")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/source-residue"],
            current_only=True,
        )

        assert [record.note_path for record in stale] == [
            "kb/notes/current-top.md",
        ]

    def test_automatic_discovery_ignores_nested_notes(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "definitions" / "term.md", "Current term", "\nBody.\n", status="current")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/source-residue"],
            current_only=True,
        )

        assert stale == []

    def test_current_filter_includes_reference_top_level_notes(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        reference_dir = tmp_path / "kb" / "reference"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "note-current.md", "Note", "\nBody.\n", status="current")
        make_note(reference_dir / "architecture.md", "Architecture", "\nBody.\n", status="current")
        make_note(reference_dir / "adr" / "001-nested.md", "Nested ADR", "\nBody.\n", status="current")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/source-residue"],
            current_only=True,
        )

        assert [record.note_path for record in stale] == [
            "kb/notes/note-current.md",
            "kb/reference/architecture.md",
        ]

    def test_directory_filter_expands_direct_reviewable_children_only(self, tmp_path: Path) -> None:
        definitions_dir = tmp_path / "kb" / "notes" / "definitions"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(definitions_dir / "term.md", "Current term", "\nBody.\n", status="current")
        make_note(definitions_dir / "index.md", "Definitions index", "\nBody.\n", status="current")
        write(definitions_dir / "plain.txt", "not markdown\n")
        write(definitions_dir / "no-frontmatter.md", "# No frontmatter\n")
        make_note(definitions_dir / "nested" / "too-deep.md", "Nested", "\nBody.\n", status="current")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/source-residue"],
            note_filter=["kb/notes/definitions"],
        )

        assert [record.note_path for record in stale] == [
            "kb/notes/definitions/term.md",
        ]

    def test_directory_filter_skips_type_definition_content(self, tmp_path: Path) -> None:
        types_dir = tmp_path / "kb" / "notes" / "types"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(types_dir / "definition.template.md", "Definition template", "\nBody.\n", status="current")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        with pytest.raises(ValueError, match="No reviewable notes found in directory: kb/notes/types"):
            review_target_selector.select_stale_gates(
                tmp_path,
                model=TEST_MODEL,
                gate_ids=["prose/source-residue"],
                note_filter=["kb/notes/types"],
            )

    def test_directory_filter_deduplicates_overlapping_operands(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "one.md", "One", "\nBody.\n", status="current")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/source-residue"],
            note_filter=["kb/notes", "kb/notes/one.md"],
        )

        assert [record.note_path for record in stale] == [
            "kb/notes/one.md",
        ]

    def test_selector_requires_explicit_scope_without_current(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "current-top.md", "Current top", "\nBody.\n", status="current")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        with pytest.raises(ValueError, match="provide note paths/directories or --current"):
            review_target_selector.select_stale_gates(
                tmp_path,
                model=TEST_MODEL,
                gate_ids=["prose/source-residue"],
            )

    def test_trait_gated_gates_are_skipped_for_notes_without_trait(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "plain.md", "Plain note", "\nBody.\n")
        make_gate(
            gates_dir / "frontmatter" / "claim-strength.md",
            "frontmatter/claim-strength",
            "frontmatter",
            requires_trait="title-as-claim",
        )

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["frontmatter/claim-strength"],
            note_filter=["kb/notes/plain.md"],
        )

        assert stale == []

    def test_trait_gated_gates_apply_when_note_has_trait(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "claim.md", "Claim note", "\nBody.\n", traits="[title-as-claim]")
        make_gate(
            gates_dir / "frontmatter" / "claim-strength.md",
            "frontmatter/claim-strength",
            "frontmatter",
            requires_trait="title-as-claim",
        )

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["frontmatter/claim-strength"],
            note_filter=["kb/notes/claim.md"],
        )

        assert [(record.note_path, record.gate_id) for record in stale] == [
            ("kb/notes/claim.md", "frontmatter/claim-strength"),
        ]

    def test_type_gated_gates_apply_only_to_matching_note_type(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "definition.md", "Definition", "\nBody.\n", note_type="kb/types/definition.md")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")
        make_gate(
            gates_dir / "frontmatter" / "definition-precision.md",
            "frontmatter/definition-precision",
            "frontmatter",
            requires_type="kb/types/definition.md",
        )
        make_gate(
            gates_dir / "frontmatter" / "related-system-fit.md",
            "frontmatter/related-system-fit",
            "frontmatter",
            requires_type="kb/types/note.md",
        )

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=[
                "frontmatter/definition-precision",
                "frontmatter/related-system-fit",
                "prose/source-residue",
            ],
            note_filter=["kb/notes/definition.md"],
        )

        assert [(record.note_path, record.gate_id) for record in stale] == [
            ("kb/notes/definition.md", "frontmatter/definition-precision"),
            ("kb/notes/definition.md", "prose/source-residue"),
        ]


class TestFreshReview:
    def test_review_with_matching_metadata_is_fresh(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert stale == []

    def test_snapshot_acceptance_selects_without_git(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_note(notes_dir / "stable.md", "Stable title", "\nLine 1.\n")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")
        seed_snapshot_acceptance(
            tmp_path,
            note_path="kb/notes/stable.md",
            gate_path="kb/instructions/review-gates/prose/source-residue.md",
        )

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )

        assert stale == []


class TestGateChanged:
    def test_gate_fingerprint_change_marks_stale(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        fixture["gate_prose_sr"].write_text(
            fixture["gate_prose_sr"].read_text(encoding="utf-8") + "\nExtra line.\n",
            encoding="utf-8",
        )

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/source-residue", "gate-changed"),
        ]


class TestNoteChanged:
    def test_note_sha_change_marks_stale(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        make_note(fixture["stable"], "Stable title", "\nUpdated line.\n")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/confidence-miscalibration", "note-changed"),
            ("prose/source-residue", "note-changed"),
        ]

    def test_snapshot_acceptance_diff_does_not_need_git(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        note = make_note(notes_dir / "stable.md", "Stable title", "\nOriginal line.\n")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")
        seed_snapshot_acceptance(
            tmp_path,
            note_path="kb/notes/stable.md",
            gate_path="kb/instructions/review-gates/prose/source-residue.md",
        )
        make_note(note, "Stable title", "\nUpdated line.\n")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
            include_diff=True,
        )

        assert len(stale) == 1
        assert stale[0].reason == "note-changed"
        assert stale[0].diff is not None
        assert "Original line" in stale[0].diff
        assert "Updated line" in stale[0].diff


class TestAckMetadata:
    def test_ack_appends_acceptance_event_without_creating_new_review_pairs(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        make_note(fixture["stable"], "Stable title", "\nUpdated line.\n")

        with sqlite3.connect(db_path_for(tmp_path)) as conn:
            review_pair_count_before = conn.execute("SELECT count(*) FROM review_pairs").fetchone()[0]

        stale_before = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert len(stale_before) == 2

        acked = review_target_selector.ack_pairs(
            tmp_path,
            [
                "kb/notes/stable.md:prose/source-residue",
                "kb/notes/stable.md:prose/confidence-miscalibration",
            ],
            TEST_MODEL,
        )
        assert acked == [
            ("kb/notes/stable.md", "prose/source-residue"),
            ("kb/notes/stable.md", "prose/confidence-miscalibration"),
        ]

        stale_after = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert stale_after == []

        with sqlite3.connect(db_path_for(tmp_path)) as conn:
            conn.row_factory = sqlite3.Row
            review_pair_count_after = conn.execute("SELECT count(*) FROM review_pairs").fetchone()[0]
            row = conn.execute(
                """
                SELECT accepted_review_pair_id, accepted_note_hash
                FROM current_gate_acceptances
                WHERE note_path = ? AND gate_path = ? AND model_partition = ?
                """,
                ("kb/notes/stable.md", "kb/instructions/review-gates/prose/source-residue.md", TEST_MODEL),
            ).fetchone()
        assert row is not None
        assert review_pair_count_after == review_pair_count_before
        assert row["accepted_review_pair_id"] is None
        assert row["accepted_note_hash"] is not None

    def test_ack_allows_dirty_note_and_records_snapshot_baseline(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        make_note(fixture["stable"], "Stable title", "\nDirty update.\n")
        review_target_selector.ack_pairs(
            tmp_path,
            ["kb/notes/stable.md:prose/source-residue"],
            TEST_MODEL,
        )
        with sqlite3.connect(db_path_for(tmp_path)) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                """
                SELECT accepted_note_snapshot_id, accepted_note_hash
                FROM current_gate_acceptances
                WHERE note_path = ? AND gate_path = ? AND model_partition = ?
                """,
                ("kb/notes/stable.md", "kb/instructions/review-gates/prose/source-residue.md", TEST_MODEL),
            ).fetchone()
        assert row is not None
        assert row["accepted_note_snapshot_id"] is not None
        assert row["accepted_note_hash"] is not None

    def test_ack_rejects_invalid_pair_without_exiting(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)

        with pytest.raises(ValueError, match="invalid pair"):
            review_target_selector.ack_pairs(
                tmp_path,
                ["kb/notes/stable.md"],
                TEST_MODEL,
            )

    def test_ack_does_not_create_review_file_when_missing(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale_before = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert len(stale_before) == 2

        review_target_selector.ack_pairs(
            tmp_path,
            [
                "kb/notes/unreviewed.md:prose/confidence-miscalibration",
                "kb/notes/unreviewed.md:prose/source-residue",
            ],
            TEST_MODEL,
        )

        stale_after = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert stale_after == []

        with sqlite3.connect(db_path_for(tmp_path)) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                """
                SELECT accepted_review_pair_id
                FROM current_gate_acceptances
                WHERE note_path = ? AND gate_path = ? AND model_partition = ?
                """,
                ("kb/notes/unreviewed.md", "kb/instructions/review-gates/prose/source-residue.md", TEST_MODEL),
            ).fetchone()
        assert row is not None
        assert row["accepted_review_pair_id"] is None


class TestDiffGeneration:
    def test_note_changed_includes_diff_in_json_mode(self, tmp_path: Path) -> None:
        """Diff reconstruction reads previous note text from the git object store,
        so this test needs a real commit (unlike the others)."""
        subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "T"], cwd=tmp_path, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "t@e"], cwd=tmp_path, check=True, capture_output=True)

        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        note_path = make_note(notes_dir / "target.md", "Target", "\nOriginal line.\n")
        gate_path = make_gate(gates_dir / "prose" / "test-gate.md", "prose/test-gate", "prose")
        subprocess.run(["git", "add", "."], cwd=tmp_path, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "init"], cwd=tmp_path, check=True, capture_output=True)
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=tmp_path, check=True, capture_output=True, text=True
        ).stdout.strip()

        seed_acceptance(
            tmp_path,
            note_path="kb/notes/target.md",
            note_abs=note_path,
            gate_abs=gate_path,
            gate_id="prose/test-gate",
            commit=commit,
        )

        make_note(note_path, "Target", "\nUpdated line.\n")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/test-gate"],
            note_filter=["kb/notes/target.md"],
            include_diff=True,
        )
        assert len(stale) == 1
        assert stale[0].reason == "note-changed"
        assert stale[0].diff is not None
        assert "Updated line" in stale[0].diff


class TestJsonOutput:
    def test_json_output_omits_review_path(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            model=TEST_MODEL,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        json_str = review_target_selector.render_json(stale)
        items = json.loads(json_str)
        assert len(items) == 2
        for item in items:
            assert "review_path" not in item


class TestModelOptional:
    def test_cli_allows_missing_review_without_model(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)

        result = run_cli(
            "review_target_selector",
            "prose",
            "--note",
            "kb/notes/unreviewed.md",
            cwd=tmp_path,
        )

        assert "kb/notes/unreviewed.md" in result.stdout
        assert "missing-review" in result.stdout

    def test_cli_requires_model_for_non_missing_reason(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)

        result = run_cli(
            "review_target_selector",
            "prose",
            "--note",
            "kb/notes/unreviewed.md",
            "--reason",
            "note-changed",
            cwd=tmp_path,
            check=False,
        )

        assert result.returncode == 2
        assert "--model is required unless selecting missing-review coverage" in result.stderr

    def test_cli_requires_model_for_ack(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)

        result = run_cli(
            "review_target_selector",
            "--ack",
            "kb/notes/stable.md:prose/source-residue",
            cwd=tmp_path,
            check=False,
        )

        assert result.returncode == 2
        assert "--model is required with --ack" in result.stderr


class TestResolveGates:
    def test_individual_gate_resolves(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        ids = resolve_gates.resolve_to_gate_ids(["prose/source-residue"], gates_dir)
        assert ids == ["prose/source-residue"]

    def test_bundle_expands_to_all_gates(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "a-gate.md", "prose/a-gate", "prose")
        make_gate(gates_dir / "prose" / "b-gate.md", "prose/b-gate", "prose")

        ids = resolve_gates.resolve_to_gate_ids(["prose"], gates_dir)
        assert ids == ["prose/a-gate", "prose/b-gate"]

    def test_mixed_bundles_and_ids(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "a-gate.md", "prose/a-gate", "prose")
        make_gate(gates_dir / "semantic" / "b-gate.md", "semantic/b-gate", "semantic")

        ids = resolve_gates.resolve_to_gate_ids(["semantic/b-gate", "prose"], gates_dir)
        assert ids == ["semantic/b-gate", "prose/a-gate"]

    def test_cli_output_includes_gate_header_without_path(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        result = run_cli("resolve_gates", "prose/source-residue", cwd=tmp_path)

        assert "=== gate: prose/source-residue ===" in result.stdout
        assert "path:" not in result.stdout

    def test_missing_gate_raises(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        gates_dir.mkdir(parents=True, exist_ok=True)

        with pytest.raises(FileNotFoundError, match="prose/nonexistent"):
            resolve_gates.resolve_to_gate_ids(["prose/nonexistent"], gates_dir)

    def test_applicable_gate_ids_for_note_filters_by_requires_trait(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        note = make_note(notes_dir / "plain.md", "Plain", "\nBody.\n")
        make_gate(
            gates_dir / "frontmatter" / "claim-strength.md",
            "frontmatter/claim-strength",
            "frontmatter",
            requires_trait="title-as-claim",
        )
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        ids = resolve_gates.applicable_gate_ids_for_note(
            note,
            ["frontmatter/claim-strength", "prose/source-residue"],
            gates_dir,
        )

        assert ids == ["prose/source-residue"]

    def test_applicable_gate_ids_for_note_filters_by_requires_type(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        note = make_note(notes_dir / "definition.md", "Definition", "\nBody.\n", note_type="kb/types/definition.md")
        make_gate(
            gates_dir / "frontmatter" / "definition-precision.md",
            "frontmatter/definition-precision",
            "frontmatter",
            requires_type="kb/types/definition.md",
        )
        make_gate(
            gates_dir / "frontmatter" / "related-system-fit.md",
            "frontmatter/related-system-fit",
            "frontmatter",
            requires_type="kb/types/note.md",
        )
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        ids = resolve_gates.applicable_gate_ids_for_note(
            note,
            [
                "frontmatter/definition-precision",
                "frontmatter/related-system-fit",
                "prose/source-residue",
            ],
            gates_dir,
        )

        assert ids == ["frontmatter/definition-precision", "prose/source-residue"]

    def test_applicable_gate_ids_for_note_allows_requires_type_lists(self, tmp_path: Path) -> None:
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        note = make_note(notes_dir / "definition.md", "Definition", "\nBody.\n", note_type="kb/types/definition.md")
        write(
            gates_dir / "frontmatter" / "definitionish.md",
            """---
gate_id: frontmatter/definitionish
name: Definitionish
lens: frontmatter
watches: [body]
staleness: changed
requires-type: [kb/types/definition.md, kb/types/glossary-entry.md]
---

## Failure mode

Fixture gate.
""",
        )

        ids = resolve_gates.applicable_gate_ids_for_note(
            note,
            ["frontmatter/definitionish"],
            gates_dir,
        )

        assert ids == ["frontmatter/definitionish"]
