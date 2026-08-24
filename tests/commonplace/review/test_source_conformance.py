from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.review import review_db, review_target_selector
from commonplace.review.ack_trivial_note_changes import qualifying_pairs
from commonplace.review.freshness import capture_review_inputs
from commonplace.review.paths import (
    criterion_id_for_path,
    criterion_id_from_stored_path,
    criterion_path_for_id,
    normalize_criterion_path,
    review_gates_dir,
)
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.resolve_criteria import criterion_ids_for_cli
from commonplace.review.source_conformance import (
    is_source_ingest_criterion_path,
    note_source_ingest_paths,
    resolve_source_criterion_id,
)
from tests.commonplace.review.pair_helpers import accept_pair, insert_completed_pair

from ._run_cli import run_cli

TEST_MODEL = "test-model"
REVIEWED_AT = "2026-08-24T00:00:00+00:00"
ALPHA_PATH = "kb/sources/alpha.ingest.md"
BETA_PATH = "kb/sources/beta.ingest.md"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_ingest(path: Path, slug: str) -> Path:
    return write(
        path,
        f"""---
source: https://example.com/{slug}
captured: 2026-08-24
capture: test
snapshot_sha256: {slug * 8}
type: ./types/ingest-report.md
---

# {slug.title()} source

## Claims

- **Claim (paraphrase):** {slug.title()} establishes a bounded result.
  - **Source extract (verbatim):** {slug.title()} result.
  - **Source location:** Results
  - **Scope:** Fixture scope.
  - **Confidence:** Directly stated.
  - **Limitation:** No transfer is established.

## Connections Found

None.
""",
    )


def make_note(path: Path, body: str, *, user_verified: bool = True) -> Path:
    verified = "user-verified: true\n" if user_verified else ""
    return write(
        path,
        f"""---
description: Test artifact with source links
type: kb/types/note.md
traits: []
{verified}---

# Source-linked artifact

{body}
""",
    )


def make_gate(path: Path) -> Path:
    return write(
        path,
        """---
gate_id: prose/test
name: Test
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

Fixture.

## Test

Fixture.
""",
    )


def build_fixture(tmp_path: Path) -> dict[str, Path]:
    make_ingest(tmp_path / ALPHA_PATH, "alpha")
    make_ingest(tmp_path / BETA_PATH, "beta")
    write(
        tmp_path / "kb" / "types" / "note.md",
        """---
type: kb/types/type-spec.md
name: note
description: Fixture note type
schema: null
---

# Note
""",
    )
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes\n")
    make_gate(tmp_path / "kb" / "instructions" / "review-gates" / "prose" / "test.md")
    note = make_note(
        tmp_path / "kb" / "notes" / "linked.md",
        """Alpha support comes from [Alpha](../sources/alpha.ingest.md#claims).

The same [Alpha source](../sources/alpha.ingest.md) is linked twice.

- [Beta source](../sources/beta.ingest.md) — adjacent reading
""",
    )
    unlinked = make_note(tmp_path / "kb" / "notes" / "unlinked.md", "No source link here.")
    return {"note": note, "unlinked": unlinked}


def db_path_for(repo_root: Path) -> Path:
    return repo_root / "kb" / "reports" / "commonplace-store.sqlite"


def seed_freshness_baseline(repo_root: Path, *, note_path: str, criterion_path: str) -> None:
    db_path = db_path_for(repo_root)
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=note_path)
        criterion_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=criterion_path)
        review_pair_id = insert_completed_pair(
            conn,
            note_path=note_path,
            criterion_id=criterion_path,
            model_partition=TEST_MODEL,
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
            model_partition=TEST_MODEL,
            baseline_note_snapshot_id=note_snapshot.snapshot_id,
            baseline_criterion_snapshot_id=criterion_snapshot.snapshot_id,
            baseline_updated_at=REVIEWED_AT,
        )
        conn.commit()


class TestSourceIdentity:
    def test_source_shorthand_and_path_normalize_uniformly(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        assert criterion_path_for_id(tmp_path, "source/alpha") == ALPHA_PATH
        assert normalize_criterion_path(tmp_path, "source/alpha") == ALPHA_PATH
        assert normalize_criterion_path(tmp_path, ALPHA_PATH) == ALPHA_PATH
        assert criterion_id_for_path(tmp_path, ALPHA_PATH) == "source/alpha"
        assert criterion_id_from_stored_path(ALPHA_PATH) == "source/alpha"

    def test_source_path_shape_is_strict(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        write(tmp_path / "kb" / "sources" / "alpha.md", "# Not an ingest\n")
        write(tmp_path / "kb" / "sources" / "nested" / "alpha.ingest.md", "# Nested\n")
        write(tmp_path / "kb" / "reference" / "alpha.ingest.md", "# Outside\n")

        assert is_source_ingest_criterion_path(ALPHA_PATH)
        assert not is_source_ingest_criterion_path("kb/sources/alpha.md")
        assert not is_source_ingest_criterion_path("kb/sources/nested/alpha.ingest.md")
        assert not is_source_ingest_criterion_path("kb/reference/alpha.ingest.md")
        with pytest.raises(ValueError, match="outside the review gate catalog"):
            normalize_criterion_path(tmp_path, "kb/sources/alpha.md")
        with pytest.raises(ValueError, match="outside the review gate catalog"):
            normalize_criterion_path(tmp_path, "kb/sources/nested/alpha.ingest.md")
        with pytest.raises(ValueError, match="outside the review gate catalog"):
            normalize_criterion_path(tmp_path, "kb/reference/alpha.ingest.md")

    def test_unknown_or_malformed_source_id_is_rejected(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        with pytest.raises(FileNotFoundError, match="source/missing"):
            resolve_source_criterion_id(tmp_path, "source/missing")
        with pytest.raises(ValueError, match="artifact scope"):
            resolve_source_criterion_id(tmp_path, "source")
        with pytest.raises(ValueError, match="invalid source criterion id"):
            resolve_source_criterion_id(tmp_path, "source/nested/alpha")


class TestSourceSelection:
    def test_source_derives_and_deduplicates_resolved_ingest_links(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        assert note_source_ingest_paths(tmp_path, fixture["note"]) == [ALPHA_PATH, BETA_PATH]

        records = review_target_selector.select_requested_criteria(
            tmp_path,
            criterion_ids=["source"],
            note_filter=["kb/notes/linked.md"],
        )
        assert [(record.note_path, record.criterion_path, record.criterion_id) for record in records] == [
            ("kb/notes/linked.md", ALPHA_PATH, "source/alpha"),
            ("kb/notes/linked.md", BETA_PATH, "source/beta"),
        ]

    def test_specific_source_filters_to_linked_cohort(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        records = review_target_selector.select_requested_criteria(
            tmp_path,
            criterion_ids=["source/alpha"],
            user_verified_only=True,
        )
        assert [(record.note_path, record.criterion_path) for record in records] == [
            ("kb/notes/linked.md", ALPHA_PATH),
        ]

    def test_no_resolved_ingest_link_produces_no_pair(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        records = review_target_selector.select_requested_criteria(
            tmp_path,
            criterion_ids=["source"],
            note_filter=["kb/notes/unlinked.md"],
        )
        assert records == []

    def test_artifact_scope_is_not_widened(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        outside = make_note(
            tmp_path / "kb" / "instructions" / "linked.md",
            "[Alpha](../sources/alpha.ingest.md)",
        )
        assert outside.is_file()

        user_verified = review_target_selector.select_requested_criteria(
            tmp_path,
            criterion_ids=["source"],
            user_verified_only=True,
        )
        assert {record.note_path for record in user_verified} == {"kb/notes/linked.md"}

        explicit = review_target_selector.select_requested_criteria(
            tmp_path,
            criterion_ids=["source"],
            note_filter=["kb/instructions/linked.md"],
        )
        assert [(record.note_path, record.criterion_path) for record in explicit] == [
            ("kb/instructions/linked.md", ALPHA_PATH),
        ]

    def test_all_gates_includes_source_pairs(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        criterion_ids = criterion_ids_for_cli(review_gates_dir(tmp_path), [], all_gates=True)
        assert "source" in criterion_ids

        result = run_cli(
            "review_target_selector",
            "--mode",
            "requested",
            "--model-partition",
            TEST_MODEL,
            "--all-gates",
            "--note",
            "kb/notes/linked.md",
            "--json",
            cwd=tmp_path,
        )
        payload = json.loads(result.stdout)
        assert {target["criterion_id"] for target in payload["targets"]}.issuperset(
            {"source/alpha", "source/beta"}
        )


class TestSourceFreshnessAndJobs:
    def test_source_pair_stales_when_either_input_changes(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        seed_freshness_baseline(tmp_path, note_path="kb/notes/linked.md", criterion_path=ALPHA_PATH)

        assert review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["source/alpha"],
            note_filter=["kb/notes/linked.md"],
        ) == []

        with (tmp_path / ALPHA_PATH).open("a", encoding="utf-8") as stream:
            stream.write("\nCriterion changed.\n")
        criterion_stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["source/alpha"],
            note_filter=["kb/notes/linked.md"],
        )
        assert [(record.criterion_id, record.reason) for record in criterion_stale] == [
            ("source/alpha", "criterion-changed")
        ]

    def test_note_change_stales_source_pair(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        seed_freshness_baseline(tmp_path, note_path="kb/notes/linked.md", criterion_path=ALPHA_PATH)
        with (tmp_path / "kb" / "notes" / "linked.md").open("a", encoding="utf-8") as stream:
            stream.write("\nThe linked claim is reused.\n")

        stale = review_target_selector.select_stale_criteria(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["source/alpha"],
            note_filter=["kb/notes/linked.md"],
        )
        assert [(record.criterion_id, record.reason) for record in stale] == [
            ("source/alpha", "note-changed")
        ]

    def test_create_jobs_revalidates_current_link_applicability(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        targets_path = tmp_path / "targets.json"
        targets_path.write_text(
            json.dumps(
                {
                    "model_partition": TEST_MODEL,
                    "targets": [
                        {
                            "note_path": "kb/notes/linked.md",
                            "criterion_path": ALPHA_PATH,
                            "criterion_id": "source/alpha",
                            "reason": "requested",
                            "result_kind": "verdict",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        make_note(tmp_path / "kb" / "notes" / "linked.md", "No source link remains.")

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
                "note_path": "kb/notes/linked.md",
                "criterion_path": ALPHA_PATH,
                "criterion_id": "source/alpha",
                "reason": "not applicable",
            }
        ]

    def test_source_pairs_never_qualify_for_trivial_ack(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        seed_freshness_baseline(tmp_path, note_path="kb/notes/linked.md", criterion_path=ALPHA_PATH)
        with (tmp_path / "kb" / "notes" / "linked.md").open("a", encoding="utf-8") as stream:
            stream.write("\nA cosmetic-looking but source-relevant change.\n")

        assert qualifying_pairs(
            tmp_path,
            model=TEST_MODEL,
            criterion_ids=["source/alpha"],
            note_filter=["kb/notes/linked.md"],
            db_path=db_path_for(tmp_path),
        ) == []


class TestSourcePrompt:
    def test_prompt_receives_raw_ingest_and_mechanical_outcome_mapping(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        db_path = db_path_for(tmp_path)
        review_db.ensure_db(db_path)
        with review_db.connect(db_path) as conn:
            captured = capture_review_inputs(
                conn,
                repo_root=tmp_path,
                pairs=[("kb/notes/linked.md", ALPHA_PATH, "verdict")],
            )

        criterion_text = captured.criterion_texts[ALPHA_PATH]
        assert criterion_text.startswith("---\nsource: https://example.com/alpha")
        prompt = render_pairs_prompt(
            notes=[
                NoteReviewTarget(
                    note_path="kb/notes/linked.md",
                    criterion_paths=(ALPHA_PATH,),
                    note_text=captured.note_texts["kb/notes/linked.md"],
                )
            ],
            criterion_texts=captured.criterion_texts,
            result_kind="verdict",
            job_output_path="kb/reports/review-jobs/review-job-1/job-output.md",
        )
        assert "This is a source-conformance gate." in prompt
        assert "A purely adjacent link makes no support claim and passes this pair." in prompt
        assert "Return the worst outcome across all uses" in prompt
        assert "source: https://example.com/alpha" in prompt
        assert "## Claims" in prompt

    def test_resolve_cli_emits_raw_source_ingest(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        result = run_cli("resolve_criteria", "source/alpha", cwd=tmp_path)
        assert result.stdout.startswith("=== criterion: source/alpha ===\n---\n")
        assert "source: https://example.com/alpha" in result.stdout

    def test_resolve_cli_rejects_bare_source_without_artifact_scope(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        result = run_cli("resolve_criteria", "source", cwd=tmp_path, check=False)
        assert result.returncode == 1
        assert "source requires an artifact scope" in result.stderr
