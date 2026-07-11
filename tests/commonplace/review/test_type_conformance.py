from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.review import review_db, review_target_selector
from commonplace.review.acknowledgement import ack_pairs
from commonplace.review.paths import (
    criterion_id_for_path,
    criterion_id_from_stored_path,
    normalize_criterion_path,
)
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.type_conformance import (
    is_type_spec_criterion_path,
    note_type_spec_path,
    resolve_type_criterion_id,
)
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
    note_type: str = "kb/types/note.md",
) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: {note_type}
traits: []
user-verified: true
---

# {title}
{body}
""",
    )


def make_type_spec(path: Path, name: str, *, instructions: str = "State one claim per note.") -> Path:
    return write(
        path,
        f"""---
type: kb/types/type-spec.md
name: {name}
description: Test type spec for {name}
schema: null
---

# {name.title()}

## Authoring Instructions

{instructions}
""",
    )


def make_gate(path: Path, criterion_id: str, lens: str) -> Path:
    return write(
        path,
        f"""---
gate_id: {criterion_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
watches: [body]
staleness: changed
---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
    )


def seed_freshness_baseline(
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
            outcome="pass",
            reviewed_note_snapshot_id=note_snapshot.snapshot_id,
            reviewed_criterion_snapshot_id=criterion_snapshot.snapshot_id,
            completed_at=REVIEWED_AT,
        )
        accept_pair(
            conn,
            review_pair_id=review_pair_id,
            note_path=note_path,
            criterion_id=criterion_path,
            model_partition=model_partition,
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
            baseline_updated_at=REVIEWED_AT,
        )
        conn.commit()


def build_fixture(tmp_path: Path) -> dict[str, Path]:
    """One note-typed note, one definition-typed note, both global type specs."""
    notes_dir = tmp_path / "kb" / "notes"
    types_dir = tmp_path / "kb" / "types"

    note_spec = make_type_spec(types_dir / "note.md", "note")
    definition_spec = make_type_spec(types_dir / "definition.md", "definition")
    plain = make_note(notes_dir / "plain.md", "Plain note", "\nBody.\n")
    definition = make_note(
        notes_dir / "definition.md",
        "Definition note",
        "\nBody.\n",
        note_type="kb/types/definition.md",
    )
    return {
        "note_spec": note_spec,
        "definition_spec": definition_spec,
        "plain": plain,
        "definition": definition,
    }


class TestGateIdPlumbing:
    def test_type_shorthand_resolves_to_global_type_spec(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        assert normalize_criterion_path(tmp_path, "type/definition") == "kb/types/definition.md"

    def test_type_spec_repo_path_normalizes(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        assert normalize_criterion_path(tmp_path, "kb/types/definition.md") == "kb/types/definition.md"

    def test_criterion_id_for_type_spec_path_uses_type_lens(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        assert criterion_id_for_path(tmp_path, "kb/types/definition.md") == "type/definition"

    def test_stored_type_spec_path_renders_type_lens_without_fs(self) -> None:
        assert criterion_id_from_stored_path("kb/types/definition.md") == "type/definition"
        assert criterion_id_from_stored_path("kb/notes/types/structured-claim.md") == "type/structured-claim"
        assert criterion_id_from_stored_path("kb/instructions/review-gates/prose/source-residue.md") == (
            "prose/source-residue"
        )

    def test_collection_local_type_resolves_when_unique(self, tmp_path: Path) -> None:
        make_type_spec(tmp_path / "kb" / "notes" / "types" / "structured-claim.md", "structured-claim")
        assert resolve_type_criterion_id(tmp_path, "type/structured-claim") == "kb/notes/types/structured-claim.md"

    def test_global_type_spec_wins_over_collection_local(self, tmp_path: Path) -> None:
        make_type_spec(tmp_path / "kb" / "types" / "definition.md", "definition")
        make_type_spec(tmp_path / "kb" / "notes" / "types" / "definition.md", "definition")
        assert resolve_type_criterion_id(tmp_path, "type/definition") == "kb/types/definition.md"

    def test_ambiguous_collection_local_type_errors(self, tmp_path: Path) -> None:
        make_type_spec(tmp_path / "kb" / "notes" / "types" / "adr.md", "adr")
        make_type_spec(tmp_path / "kb" / "reference" / "types" / "adr.md", "adr")
        with pytest.raises(ValueError, match="ambiguous"):
            resolve_type_criterion_id(tmp_path, "type/adr")

    def test_missing_type_spec_errors(self, tmp_path: Path) -> None:
        (tmp_path / "kb").mkdir()
        with pytest.raises(FileNotFoundError, match="type/nonexistent"):
            resolve_type_criterion_id(tmp_path, "type/nonexistent")

    def test_type_criterion_id_rejects_nested_names(self, tmp_path: Path) -> None:
        with pytest.raises(ValueError, match="invalid type gate id"):
            resolve_type_criterion_id(tmp_path, "type/nested/name")

    def test_review_gate_catalog_paths_are_not_type_spec_paths(self) -> None:
        assert not is_type_spec_criterion_path("kb/instructions/review-gates/types/sneaky.md")
        assert not is_type_spec_criterion_path("kb/types/definition.schema.yaml")
        assert is_type_spec_criterion_path("kb/types/definition.md")


class TestNoteTypeSpecPath:
    def test_repo_relative_type_resolves(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        assert note_type_spec_path(tmp_path, fixture["definition"]) == "kb/types/definition.md"

    def test_file_relative_type_canonicalizes(self, tmp_path: Path) -> None:
        make_type_spec(tmp_path / "kb" / "notes" / "types" / "structured-claim.md", "structured-claim")
        note = make_note(
            tmp_path / "kb" / "notes" / "claim.md",
            "Claim",
            "\nBody.\n",
            note_type="./types/structured-claim.md",
        )
        assert note_type_spec_path(tmp_path, note) == "kb/notes/types/structured-claim.md"

    def test_malformed_type_value_yields_none(self, tmp_path: Path) -> None:
        note = make_note(tmp_path / "kb" / "notes" / "broken.md", "Broken", "\nBody.\n", note_type="not-a-path")
        assert note_type_spec_path(tmp_path, note) is None

    def test_declared_but_missing_type_spec_raises(self, tmp_path: Path) -> None:
        note = make_note(
            tmp_path / "kb" / "notes" / "orphan.md",
            "Orphan",
            "\nBody.\n",
            note_type="kb/types/ghost.md",
        )
        with pytest.raises(FileNotFoundError, match="kb/types/ghost.md"):
            note_type_spec_path(tmp_path, note)


class TestSelectorTypePairs:
    def test_type_request_derives_pair_from_note_frontmatter(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type"],
            note_filter=["kb/notes/plain.md"],
        )
        assert [(s.note_path, s.criterion_path, s.criterion_id, s.reason) for s in stale] == [
            ("kb/notes/plain.md", "kb/types/note.md", "type/note", "missing-baseline"),
        ]

    def test_type_name_request_filters_to_cohort(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type/definition"],
            user_verified_only=True,
        )
        assert [(s.note_path, s.criterion_id) for s in stale] == [
            ("kb/notes/definition.md", "type/definition"),
        ]

    def test_type_pair_supports_model_agnostic_missing_review(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=None,
            criterion_ids=["type/definition"],
            note_filter=["kb/notes/definition.md"],
        )
        assert [(s.criterion_id, s.reason) for s in stale] == [("type/definition", "missing-baseline")]

    def test_fresh_type_pair_is_not_selected(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        seed_freshness_baseline(tmp_path, note_path="kb/notes/definition.md", criterion_path="kb/types/definition.md")
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type"],
            note_filter=["kb/notes/definition.md"],
        )
        assert stale == []

    def test_type_spec_edit_marks_cohort_gate_changed(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        seed_freshness_baseline(tmp_path, note_path="kb/notes/definition.md", criterion_path="kb/types/definition.md")
        seed_freshness_baseline(tmp_path, note_path="kb/notes/plain.md", criterion_path="kb/types/note.md")

        fixture["definition_spec"].write_text(
            fixture["definition_spec"].read_text(encoding="utf-8") + "\nRaised authoring bar.\n",
            encoding="utf-8",
        )

        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type"],
            user_verified_only=True,
        )
        assert [(s.note_path, s.criterion_id, s.reason) for s in stale] == [
            ("kb/notes/definition.md", "type/definition", "criterion-changed"),
        ]

    def test_note_edit_marks_type_pair_note_changed_with_diff(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        seed_freshness_baseline(tmp_path, note_path="kb/notes/definition.md", criterion_path="kb/types/definition.md")
        make_note(fixture["definition"], "Definition note", "\nUpdated body.\n", note_type="kb/types/definition.md")

        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type"],
            note_filter=["kb/notes/definition.md"],
            include_diff=True,
        )
        assert [(s.criterion_id, s.reason) for s in stale] == [("type/definition", "note-changed")]
        assert stale[0].diff is not None
        assert "Updated body" in stale[0].diff

    def test_note_without_valid_type_binding_gets_no_type_pair(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        make_note(tmp_path / "kb" / "notes" / "broken.md", "Broken", "\nBody.\n", note_type="not-a-path")
        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type"],
            note_filter=["kb/notes/broken.md"],
        )
        assert stale == []

    def test_mixed_catalog_and_type_requests(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["prose/source-residue", "type"],
            note_filter=["kb/notes/plain.md"],
        )
        assert [(s.criterion_id, s.reason) for s in stale] == [
            ("prose/source-residue", "missing-baseline"),
            ("type/note", "missing-baseline"),
        ]

    def test_requested_mode_emits_type_pairs(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        requested = review_target_selector.select_requested_criteria(
            tmp_path,
            criterion_ids=["type"],
            user_verified_only=True,
        )
        assert [(s.note_path, s.criterion_id, s.reason) for s in requested] == [
            ("kb/notes/definition.md", "type/definition", "requested"),
            ("kb/notes/plain.md", "type/note", "requested"),
        ]

    def test_all_gates_cli_includes_type_pairs(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

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
            "prose/source-residue",
            "type/note",
        ]


class TestAckTypePair:
    def test_ack_after_type_spec_edit_repins_current_spec(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        seed_freshness_baseline(tmp_path, note_path="kb/notes/definition.md", criterion_path="kb/types/definition.md")
        fixture["definition_spec"].write_text(
            fixture["definition_spec"].read_text(encoding="utf-8") + "\nTrivial wording tweak.\n",
            encoding="utf-8",
        )
        stale_before = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type"],
            note_filter=["kb/notes/definition.md"],
        )
        assert [s.reason for s in stale_before] == ["criterion-changed"]

        acked = ack_pairs(
            tmp_path,
            ["kb/notes/definition.md:type/definition"],
            TEST_MODEL,
        )
        assert acked == [("kb/notes/definition.md", "type/definition")]

        stale_after = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["type"],
            note_filter=["kb/notes/definition.md"],
        )
        assert stale_after == []


class TestPromptWrapper:
    def test_type_spec_gate_embeds_captured_text(self) -> None:
        prompt = render_pairs_prompt(
            notes=[
                NoteReviewTarget(
                    note_path="kb/notes/definition.md",
                    review_job_id=1,
                    criterion_paths=("kb/types/definition.md",),
                    note_text="# Definition note\n\nBody.",
                )
            ],
            criterion_texts={"kb/types/definition.md": "# Definition\n\n## Authoring Instructions\n\nSharpen the term."},
            result_kind="verdict",
            job_output_path="job-output.md",
        )
        assert "=== criterion: kb/types/definition.md ===" in prompt
        assert "This is a type-conformance gate." in prompt
        assert "Sharpen the term." in prompt

    def test_catalog_gate_has_no_conformance_wrapper(self) -> None:
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
            job_output_path="job-output.md",
        )
        assert "This is a type-conformance gate." not in prompt


class TestCreateJobsForTypePairs:
    def test_selector_json_feeds_create_review_jobs(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        selector_result = run_cli(
            "review_target_selector",
            "--mode",
            "requested",
            "--model-partition",
            TEST_MODEL,
            "type",
            "--note",
            "kb/notes/definition.md",
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
            ("kb/types/definition.md", "type/definition"),
        ]

        prompt_path = tmp_path / payload["jobs"][0]["prompt_path"]
        prompt = prompt_path.read_text(encoding="utf-8")
        assert "=== criterion: kb/types/definition.md ===" in prompt
        assert "This is a type-conformance gate." in prompt
        assert "State one claim per note." in prompt

    def test_type_pair_for_wrong_type_is_skipped_as_not_applicable(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        selector_json = json.dumps(
            {
                "model_partition": TEST_MODEL,
                "targets": [
                    {
                        "note_path": "kb/notes/plain.md",
                        "criterion_path": "kb/types/definition.md",
                        "criterion_id": "type/definition",
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
                "criterion_path": "kb/types/definition.md",
                "criterion_id": "type/definition",
            }
        ]
