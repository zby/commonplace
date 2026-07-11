from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.review import review_db, review_target_selector
from commonplace.review.acknowledgement import ack_pairs
from commonplace.review.collection_conformance import (
    is_collection_md_criterion_path,
    note_collection_md_path,
    resolve_collection_criterion_id,
)
from commonplace.review.paths import (
    criterion_id_for_path,
    criterion_id_from_stored_path,
    normalize_criterion_path,
)
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair

from ._run_cli import run_cli

TEST_MODEL = "test-model"
REVIEWED_AT = "2026-07-01T00:00:00+00:00"


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
    note_type: str = "kb/types/note.md",
) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: {note_type}
traits: []
status: {status}
---

# {title}
{body}
""",
    )


def make_collection_md(path: Path, name: str, *, conventions: str = "Use claim-shaped titles.") -> Path:
    """COLLECTION.md files carry no frontmatter; they open with a heading."""
    return write(
        path,
        f"""# Writing conventions for {name}

## Conventions

{conventions}
""",
    )


def build_fixture(tmp_path: Path) -> dict[str, Path]:
    """Two collections with contracts, one note in each."""
    notes_contract = make_collection_md(tmp_path / "kb" / "notes" / "COLLECTION.md", "kb/notes/")
    reference_contract = make_collection_md(tmp_path / "kb" / "reference" / "COLLECTION.md", "kb/reference/")
    note = make_note(tmp_path / "kb" / "notes" / "plain.md", "Plain note", "\nBody.\n")
    reference_note = make_note(tmp_path / "kb" / "reference" / "doc.md", "Doc note", "\nBody.\n")
    return {
        "notes_contract": notes_contract,
        "reference_contract": reference_contract,
        "note": note,
        "reference_note": reference_note,
    }


def seed_acceptance(
    repo_root: Path,
    *,
    note_path: str,
    criterion_path: str,
    model_partition: str = TEST_MODEL,
) -> None:
    review_db.ensure_db(db_path_for(repo_root))
    with review_db.connect(db_path_for(repo_root)) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=note_path)
        criterion_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=criterion_path)
        review_pair_id = insert_completed_pair(
            conn,
            note_path=note_path,
            criterion_id=criterion_path,
            model_partition=model_partition,
            decision="pass",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
            reviewed_at=REVIEWED_AT,
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path=note_path,
            criterion_id=criterion_path,
            model_partition=model_partition,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_criterion_snapshot_id=criterion_snapshot.snapshot_id,
            accepted_at=REVIEWED_AT,
        )
        conn.commit()


class TestGateIdPlumbing:
    def test_collection_shorthand_resolves_to_collection_md(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        assert normalize_criterion_path(tmp_path, "collection/notes") == "kb/notes/COLLECTION.md"

    def test_collection_md_repo_path_normalizes(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        assert normalize_criterion_path(tmp_path, "kb/notes/COLLECTION.md") == "kb/notes/COLLECTION.md"

    def test_criterion_id_for_collection_md_path_uses_collection_lens(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        assert criterion_id_for_path(tmp_path, "kb/notes/COLLECTION.md") == "collection/notes"

    def test_stored_collection_md_path_renders_collection_lens_without_fs(self) -> None:
        assert criterion_id_from_stored_path("kb/notes/COLLECTION.md") == "collection/notes"
        assert criterion_id_from_stored_path("kb/commonplace/notes/COLLECTION.md") == "collection/commonplace/notes"
        assert criterion_id_from_stored_path("kb/instructions/review-gates/prose/source-residue.md") == (
            "prose/source-residue"
        )

    def test_namespaced_collection_resolves(self, tmp_path: Path) -> None:
        make_collection_md(tmp_path / "kb" / "commonplace" / "notes" / "COLLECTION.md", "kb/commonplace/notes/")
        assert (
            resolve_collection_criterion_id(tmp_path, "collection/commonplace/notes")
            == "kb/commonplace/notes/COLLECTION.md"
        )

    def test_missing_collection_contract_errors(self, tmp_path: Path) -> None:
        (tmp_path / "kb").mkdir()
        with pytest.raises(FileNotFoundError, match="collection/nonexistent"):
            resolve_collection_criterion_id(tmp_path, "collection/nonexistent")

    def test_collection_criterion_id_rejects_traversal(self, tmp_path: Path) -> None:
        with pytest.raises(ValueError, match="invalid collection gate id"):
            resolve_collection_criterion_id(tmp_path, "collection/../secrets")
        with pytest.raises(ValueError, match="invalid collection gate id"):
            resolve_collection_criterion_id(tmp_path, "collection/")

    def test_non_collection_paths_are_not_collection_criterion_paths(self) -> None:
        assert not is_collection_md_criterion_path("kb/COLLECTION.md")
        assert not is_collection_md_criterion_path("kb/notes/types/COLLECTION.md")
        assert not is_collection_md_criterion_path("kb/notes/plain.md")
        assert not is_collection_md_criterion_path("docs/COLLECTION.md")
        assert is_collection_md_criterion_path("kb/notes/COLLECTION.md")
        assert is_collection_md_criterion_path("kb/commonplace/notes/COLLECTION.md")


class TestNoteCollectionMdPath:
    def test_note_maps_to_its_collection_contract(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        assert note_collection_md_path(tmp_path, fixture["note"]) == "kb/notes/COLLECTION.md"

    def test_subdirectory_note_maps_to_nearest_contract(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        nested = make_note(tmp_path / "kb" / "notes" / "definitions" / "term.md", "Term", "\nBody.\n")
        assert note_collection_md_path(tmp_path, nested) == "kb/notes/COLLECTION.md"

    def test_note_outside_any_collection_yields_none(self, tmp_path: Path) -> None:
        (tmp_path / "kb").mkdir()
        stray = make_note(tmp_path / "kb" / "stray.md", "Stray", "\nBody.\n")
        assert note_collection_md_path(tmp_path, stray) is None

    def test_collection_md_never_pairs_with_itself(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        assert note_collection_md_path(tmp_path, fixture["notes_contract"]) is None


class TestSelectorCollectionPairs:
    def test_collection_request_derives_pair_from_note_location(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection"],
            note_filter=["kb/notes/plain.md"],
        )
        assert [(s.note_path, s.criterion_path, s.criterion_id, s.reason) for s in stale] == [
            ("kb/notes/plain.md", "kb/notes/COLLECTION.md", "collection/notes", "missing-review"),
        ]

    def test_collection_path_request_filters_to_cohort(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection/reference"],
            current_only=True,
        )
        assert [(s.note_path, s.criterion_id) for s in stale] == [
            ("kb/reference/doc.md", "collection/reference"),
        ]

    def test_fresh_collection_pair_is_not_selected(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        seed_acceptance(tmp_path, note_path="kb/notes/plain.md", criterion_path="kb/notes/COLLECTION.md")
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection"],
            note_filter=["kb/notes/plain.md"],
        )
        assert stale == []

    def test_collection_md_edit_marks_cohort_gate_changed(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        seed_acceptance(tmp_path, note_path="kb/notes/plain.md", criterion_path="kb/notes/COLLECTION.md")
        seed_acceptance(tmp_path, note_path="kb/reference/doc.md", criterion_path="kb/reference/COLLECTION.md")

        fixture["notes_contract"].write_text(
            fixture["notes_contract"].read_text(encoding="utf-8") + "\nRaised conventions bar.\n",
            encoding="utf-8",
        )

        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection"],
            current_only=True,
        )
        assert [(s.note_path, s.criterion_id, s.reason) for s in stale] == [
            ("kb/notes/plain.md", "collection/notes", "criterion-changed"),
        ]

    def test_note_edit_marks_collection_pair_note_changed_with_diff(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        seed_acceptance(tmp_path, note_path="kb/notes/plain.md", criterion_path="kb/notes/COLLECTION.md")
        make_note(fixture["note"], "Plain note", "\nUpdated body.\n")

        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection"],
            note_filter=["kb/notes/plain.md"],
            include_diff=True,
        )
        assert [(s.criterion_id, s.reason) for s in stale] == [("collection/notes", "note-changed")]
        assert stale[0].diff is not None
        assert "Updated body" in stale[0].diff

    def test_note_outside_any_collection_gets_no_collection_pair(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        make_note(tmp_path / "kb" / "notes2.md", "Stray", "\nBody.\n")
        # A stray file directly under kb/ is outside every collection.
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection"],
            note_filter=["kb/notes2.md"],
        )
        assert stale == []

    def test_mixed_catalog_type_and_collection_requests(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        write(
            tmp_path / "kb" / "types" / "note.md",
            """---
type: kb/types/type-spec.md
name: note
description: Test type spec for note
schema: null
---

# Note

## Authoring Instructions

State one claim per note.
""",
        )
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type", "collection"],
            note_filter=["kb/notes/plain.md"],
        )
        assert [(s.criterion_id, s.reason) for s in stale] == [
            ("collection/notes", "missing-review"),
            ("type/note", "missing-review"),
        ]

    def test_requested_mode_emits_collection_pairs(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        requested = review_target_selector.select_requested_criteria(
            tmp_path,
            criterion_ids=["collection"],
            current_only=True,
        )
        assert [(s.note_path, s.criterion_id, s.reason) for s in requested] == [
            ("kb/notes/plain.md", "collection/notes", "requested"),
            ("kb/reference/doc.md", "collection/reference", "requested"),
        ]

    def test_all_gates_cli_includes_collection_pairs(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        write(
            tmp_path / "kb" / "instructions" / "review-gates" / "prose" / "source-residue.md",
            """---
gate_id: prose/source-residue
name: Source Residue
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
        )
        write(
            tmp_path / "kb" / "types" / "note.md",
            """---
type: kb/types/type-spec.md
name: note
description: Test type spec for note
schema: null
---

# Note

## Authoring Instructions

State one claim per note.
""",
        )

        result = run_cli(
            "review_target_selector",
            "--all-gates",
            "--note",
            "kb/notes/plain.md",
            "--json",
            cwd=tmp_path,
        )
        payload = json.loads(result.stdout)
        assert sorted(item["criterion_id"] for item in payload["targets"]) == [
            "collection/notes",
            "prose/source-residue",
            "type/note",
        ]


class TestAckCollectionPair:
    def test_ack_after_collection_md_edit_repins_current_contract(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        seed_acceptance(tmp_path, note_path="kb/notes/plain.md", criterion_path="kb/notes/COLLECTION.md")
        fixture["notes_contract"].write_text(
            fixture["notes_contract"].read_text(encoding="utf-8") + "\nTrivial wording tweak.\n",
            encoding="utf-8",
        )
        stale_before = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection"],
            note_filter=["kb/notes/plain.md"],
        )
        assert [s.reason for s in stale_before] == ["criterion-changed"]

        acked = ack_pairs(
            tmp_path,
            ["kb/notes/plain.md:collection/notes"],
            TEST_MODEL,
        )
        assert acked == [("kb/notes/plain.md", "collection/notes")]

        stale_after = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["collection"],
            note_filter=["kb/notes/plain.md"],
        )
        assert stale_after == []


class TestPromptWrapper:
    def test_collection_md_gate_is_referenced_not_embedded(self) -> None:
        prompt = render_pairs_prompt(
            notes=[
                NoteReviewTarget(
                    note_path="kb/notes/plain.md",
                    review_job_id=1,
                    criterion_paths=("kb/notes/COLLECTION.md",),
                    note_text="# Plain note\n\nBody.",
                )
            ],
            criterion_texts={"kb/notes/COLLECTION.md": "# Writing conventions\n\nUse claim titles."},
            result_kind="verdict",
        )
        assert "=== criterion: kb/notes/COLLECTION.md ===" in prompt
        assert "This is a collection-conformance gate." in prompt
        assert "Read `kb/notes/COLLECTION.md` (repo-relative)" in prompt
        assert "Use claim titles." not in prompt
        assert "- Exception: collection-conformance gates reference the collection's COLLECTION.md" in prompt

    def test_collection_md_gate_needs_no_criterion_text(self) -> None:
        prompt = render_pairs_prompt(
            notes=[
                NoteReviewTarget(
                    note_path="kb/notes/plain.md",
                    review_job_id=1,
                    criterion_paths=("kb/notes/COLLECTION.md",),
                    note_text="# Plain note\n\nBody.",
                )
            ],
            criterion_texts={},
            result_kind="verdict",
        )
        assert "Read `kb/notes/COLLECTION.md` (repo-relative)" in prompt

    def test_catalog_gate_has_no_collection_wrapper(self) -> None:
        prompt = render_pairs_prompt(
            notes=[
                NoteReviewTarget(
                    note_path="kb/notes/plain.md",
                    review_job_id=1,
                    criterion_paths=("kb/instructions/review-gates/prose/source-residue.md",),
                    note_text="# Plain\n\nBody.",
                )
            ],
            criterion_texts={"kb/instructions/review-gates/prose/source-residue.md": "## Failure mode\n\nFixture."},
            result_kind="verdict",
        )
        assert "This is a collection-conformance gate." not in prompt
        assert "- Exception: collection-conformance gates reference" not in prompt

    def test_wrapper_states_type_conformance_boundary(self) -> None:
        prompt = render_pairs_prompt(
            notes=[
                NoteReviewTarget(
                    note_path="kb/notes/plain.md",
                    review_job_id=1,
                    criterion_paths=("kb/notes/COLLECTION.md",),
                    note_text="# Plain note\n\nBody.",
                )
            ],
            criterion_texts={},
            result_kind="verdict",
        )
        assert "type-conformance pair's job" in prompt


class TestCreateJobsForCollectionPairs:
    def test_selector_json_feeds_create_review_jobs(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        selector_result = run_cli(
            "review_target_selector",
            "--mode",
            "requested",
            "--model-partition",
            TEST_MODEL,
            "collection",
            "--note",
            "kb/notes/plain.md",
            "--json",
            cwd=tmp_path,
        )
        input_path = tmp_path / "targets.json"
        input_path.write_text(selector_result.stdout, encoding="utf-8")

        create_result = run_cli(
            "create_review_jobs",
            "--input",
            "targets.json",
            "--grouping",
            "note",
            cwd=tmp_path,
            db_path=db_path_for(tmp_path),
        )

        payload = json.loads(create_result.stdout)
        assert payload["created_count"] == 1
        pairs = payload["jobs"][0]["pairs"]
        assert [(pair["criterion_path"], pair["criterion_id"]) for pair in pairs] == [
            ("kb/notes/COLLECTION.md", "collection/notes"),
        ]

        prompt_path = tmp_path / payload["jobs"][0]["prompt_path"]
        prompt = prompt_path.read_text(encoding="utf-8")
        assert "=== criterion: kb/notes/COLLECTION.md ===" in prompt
        assert "This is a collection-conformance gate." in prompt
        assert "Read `kb/notes/COLLECTION.md` (repo-relative)" in prompt
        assert "Use claim-shaped titles." not in prompt

    def test_collection_pair_for_wrong_collection_is_skipped_as_not_applicable(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        selector_json = json.dumps(
            {
                "model_partition": TEST_MODEL,
                "targets": [
                    {
                        "note_path": "kb/notes/plain.md",
                        "criterion_path": "kb/reference/COLLECTION.md",
                        "criterion_id": "collection/reference",
                        "reason": "requested",
                    }
                ],
            }
        )
        input_path = tmp_path / "targets.json"
        input_path.write_text(selector_json, encoding="utf-8")

        result = run_cli(
            "create_review_jobs",
            "--input",
            "targets.json",
            "--grouping",
            "note",
            cwd=tmp_path,
            db_path=db_path_for(tmp_path),
        )

        payload = json.loads(result.stdout)
        assert payload["created_count"] == 0
        assert payload["skipped_pairs"] == [
            {
                "reason": "not applicable",
                "note_path": "kb/notes/plain.md",
                "criterion_path": "kb/reference/COLLECTION.md",
                "criterion_id": "collection/reference",
            }
        ]
