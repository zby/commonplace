from __future__ import annotations

import shutil
import subprocess
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.cli import agentic_analysis_handoff
from commonplace.freshness.snapshots import load_snapshot_by_id
from commonplace.lib import agentic_publication, systems_matrix, validation
from commonplace.lib.agentic_analysis import (
    parse_agentic_analysis_run_state,
    render_agentic_analysis_handoff,
)
from commonplace.lib.agentic_publication import (
    PublicationSpec,
    prepare_publication,
    publish_publication,
)
from commonplace.review import review_db
from commonplace.review.paths import criterion_path_for_id, review_gates_dir
from commonplace.review.resolve_criteria import (
    applicable_criterion_ids_for_note,
    resolve_to_criterion_ids,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-09-04-example-system-01"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def configure_types(tmp_path: Path) -> None:
    shutil.copytree(REPO_ROOT / "kb/types", tmp_path / "kb/types")
    shutil.copytree(
        REPO_ROOT / "kb/agent-memory-systems/types",
        tmp_path / "kb/agent-memory-systems/types",
    )
    report_types = tmp_path / "kb/reports/types"
    report_types.mkdir(parents=True)
    for name in (
        "agentic-system-analysis-run-state.md",
        "agentic-system-analysis-run-state.schema.yaml",
    ):
        shutil.copyfile(REPO_ROOT / "kb/reports/types" / name, report_types / name)
    write(tmp_path / "kb/reports/COLLECTION.md", "# Reports\n")
    shutil.copytree(
        REPO_ROOT / "kb/instructions/review-gates",
        tmp_path / "kb/instructions/review-gates",
    )


def seed_semantic_baselines(tmp_path: Path, note_path: str) -> None:
    gates_dir = review_gates_dir(tmp_path)
    criterion_ids = applicable_criterion_ids_for_note(
        tmp_path / note_path,
        resolve_to_criterion_ids(["semantic"], gates_dir),
        gates_dir,
    )
    db_path = review_db.prepare_review_db(tmp_path)
    completed_at = "2026-09-04T12:00:00Z"
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(
            conn, repo_root=tmp_path, path=note_path
        )
        criterion_snapshots = {
            criterion_id: review_db.snapshot_file(
                conn,
                repo_root=tmp_path,
                path=criterion_path_for_id(tmp_path, criterion_id),
            )
            for criterion_id in criterion_ids
        }
        requests = [
            review_db.ReviewPairRequest(
                note_path=note_path,
                criterion_path=criterion_path_for_id(tmp_path, criterion_id),
                pair_ordinal=ordinal,
                result_kind="verdict",
                reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                reviewed_criterion_snapshot_id=criterion_snapshots[
                    criterion_id
                ].snapshot_id,
            )
            for ordinal, criterion_id in enumerate(criterion_ids, start=1)
        ]
        job_id = review_db.create_job_with_pairs(
            conn,
            model_partition="codex",
            runner="test",
            created_at=completed_at,
            status="queued",
            grouping="note",
            pairs=requests,
        )
        review_db.complete_review_pairs(
            conn,
            review_job_id=job_id,
            review_pairs=[
                review_db.ReviewPairCompletion(
                    note_path=request.note_path,
                    criterion_path=request.criterion_path,
                    outcome="pass",
                    completed_at=completed_at,
                )
                for request in requests
            ],
            completed_at=completed_at,
        )
        review_db.complete_review_job(
            conn, review_job_id=job_id, completed_at=completed_at
        )
        rows = review_db.load_review_pairs_for_job(conn, review_job_id=job_id)
        for row in rows:
            criterion_id = next(
                item
                for item in criterion_ids
                if criterion_path_for_id(tmp_path, item) == row.criterion_path
            )
            review_db.upsert_freshness_baseline(
                conn,
                note_path=note_path,
                criterion_path=row.criterion_path,
                model_partition="codex",
                evidence_review_pair_id=row.review_pair_id,
                baseline_note_snapshot_id=note_snapshot.snapshot_id,
                baseline_criterion_snapshot_id=criterion_snapshots[
                    criterion_id
                ].snapshot_id,
                baseline_updated_at=completed_at,
            )
        conn.commit()


def git_checkout(path: Path) -> tuple[Path, str]:
    path.mkdir(parents=True)
    subprocess.run(["git", "init", "--quiet", str(path)], check=True)
    write(path / "README.md", "# Frozen source\n")
    subprocess.run(["git", "-C", str(path), "add", "README.md"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(path),
            "-c",
            "user.name=Commonplace Test",
            "-c",
            "user.email=test@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "Create source fixture",
        ],
        check=True,
    )
    revision = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return path, revision


def state_text(frontmatter: dict[str, object]) -> str:
    return (
        "---\n"
        + yaml.safe_dump(frontmatter, sort_keys=False)
        + "---\n\n"
        + f"# Agentic-system analysis run — {RUN_ID}\n\n"
        + "## Run\n\nFixture run.\n\n"
        + "## Outcome\n\nFixture outcome.\n"
    )


def valid_run_state(tmp_path: Path, *, legacy: bool = False) -> Path:
    configure_types(tmp_path)
    run_dir = tmp_path / "kb/reports/state/agentic-system-analysis" / RUN_ID
    source_root, revision = git_checkout(
        tmp_path / "related-systems/example--system"
    )
    result_path = f"kb/reports/state/agentic-system-analysis/{RUN_ID}/result.md"
    legacy_path = "kb/agent-memory-systems/reviews/example-system.md"
    legacy_projection = f"`{legacy_path}`" if legacy else "not applicable"
    result = write(
        tmp_path / result_path,
        f'''---
type: kb/types/agentic-system-analysis-result.md
description: "Complete fixture analysis at one frozen source boundary"
run-id: {RUN_ID}
system: "Example System"
run-date: "2026-09-04"
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: {revision}
analysis-cutoff: "2026-09-04"
evidence-tier: code-grounded
---

# Example result

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/example-system.md`

**Legacy memory review:** {legacy_projection}

## Boundary and evidence

Fixture boundary at `{revision}`.

## Source register

Source evidence: SRC-1, `https://example.invalid/example-system`, `README.md:1`.

## Shared records

### Components

CMP-1 fixture component.

### Operative objects

OBJ-1 fixture object.

### Routes

RTE-1 fixture route.

### Claims

CLM-1 fixture claim.

### Evidenced absences

None found within the fixture boundary.

### Behavioral-authority paths

BAP-1 fixture authority path.

## Runtime account

No dynamic check planned.

## Lens scoping

### Memory/context scope

Brief fixture scope.

### Epistemic scope

Brief fixture scope.

## Lens outputs

### Memory/context lens

Fixture finding.

### Epistemic lens

Fixture finding.

## Reconciliation

No conflicts.

## Bounded synthesis

Fixture synthesis.

## Limitations

None.

## Verification and blockers

### Semantic verification

Passed.

### Deterministic validation

Passed.

### Blockers

None.
''',
    )
    profile = {
        "scope": "The fixture's accumulated project memory and retrieval routes",
        "axes": {
            axis: {"assessment": "uninspected", "basis": None, "values": [],
                   "records": [], "note": "Not inspected in this fixture."}
            for axis in systems_matrix.AXES
        },
    }
    profile["axes"]["storage_substrate"] = {
        "assessment": "known", "basis": "wired", "values": ["sqlite", "files"],
        "records": ["OBJ-1"], "note": "Both stores occur within the fixture boundary.",
    }
    replace_frontmatter(result, {**frontmatter(result), "memory-comparison": profile})
    retained = tmp_path / systems_matrix.retained_result_path(RUN_ID)
    retained.parent.mkdir(parents=True, exist_ok=True)
    retained.write_bytes(result.read_bytes())
    generated_path = "kb/agentic-systems/reviews/example-system.md"
    generated = write(
        tmp_path / generated_path,
        f'''---
description: "Generated fixture review of one external agentic system"
type: kb/types/note.md
generated-by: analyse-agentic-system
analysis-run: {RUN_ID}
source-identity: https://example.invalid/example-system
reviewed-revision: {revision}
analysis-result: {systems_matrix.retained_result_path(RUN_ID).as_posix()}
analysis-result-sha256: {digest(result)}
---

# Example System

**Evidence basis:** `README.md:1` at `{revision}`.
''',
    )
    legacy_output: dict[str, str] | None = None
    if legacy:
        legacy_file = write(
            tmp_path / legacy_path,
            '''---
description: "Fixture memory-system review with source-grounded mechanisms"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-09-04"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-04-example-system-01
source-identity: https://example.invalid/example-system
reviewed-revision: PLACEHOLDER_REVISION
---

# Example memory system

## Core Ideas

Fixture mechanism.

## Artifact analysis

- **Storage substrate:** `files` — fixture storage.
- **Representational form:** `natural-language` — fixture content.
- **Lineage:** `authored` — fixture authorship.
- **Behavioral authority:** `knowledge` — fixture advice.

## Write side

**Write agency:** `manual` — fixture writes are manual.

## Read-back

**Read-back:** `pull` — the fixture requires lookup.

## Curiosity Pass

None.
''',
        )
        legacy_file.write_text(
            legacy_file.read_text(encoding="utf-8").replace(
                "PLACEHOLDER_REVISION", revision
            ),
            encoding="utf-8",
        )
        legacy_output = {"path": legacy_path, "sha256": digest(legacy_file)}
        seed_semantic_baselines(tmp_path, legacy_path)

    run_frontmatter: dict[str, object] = {
        "type": "kb/reports/types/agentic-system-analysis-run-state.md",
        "description": f"Minimal completion state for {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "complete",
        "result-disposition": "complete",
        "source": {
            "kind": "git",
            "identity": "https://example.invalid/example-system",
            "revision": revision,
            "path": source_root.as_posix(),
            "sha256": None,
        },
        "result": {"path": result_path, "sha256": digest(result)},
        "generated-review": {
            "path": generated_path,
            "sha256": digest(generated),
        },
        "memory-review-required": legacy,
        "legacy-review": legacy_output,
        "legacy-review-model-partition": "codex" if legacy else None,
        "failure": None,
    }
    return write(run_dir / "run-state.md", state_text(run_frontmatter))


def frontmatter(path: Path) -> dict[str, object]:
    content = path.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    return document.frontmatter


def replace_frontmatter(path: Path, values: dict[str, object]) -> None:
    content = path.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None
    path.write_text(
        "---\n"
        + yaml.safe_dump(values, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )


def sync_retained_fixture(tmp_path: Path, values: dict) -> None:
    result = tmp_path / values["result"]["path"]
    generated = tmp_path / values["generated-review"]["path"]
    (tmp_path / systems_matrix.retained_result_path(RUN_ID)).write_bytes(result.read_bytes())
    replace_frontmatter(generated, {**frontmatter(generated), "analysis-result-sha256": digest(result)})


def publication_fixture(tmp_path: Path) -> tuple[Path, PublicationSpec, bytes, bytes]:
    state = valid_run_state(tmp_path, legacy=True)
    subprocess.run(["git", "init", "--quiet", str(tmp_path)], check=True)
    values = frontmatter(state)
    generated_destination = values["generated-review"]["path"]  # type: ignore[index]
    legacy_destination = values["legacy-review"]["path"]  # type: ignore[index]
    generated_public = tmp_path / generated_destination
    legacy_public = tmp_path / legacy_destination
    generated_bytes = generated_public.read_bytes()
    legacy_bytes = legacy_public.read_bytes()
    generated_candidate = state.parent / "generated-review.candidate.md"
    legacy_candidate = state.parent / "legacy-review.candidate.md"
    generated_candidate.write_bytes(generated_bytes)
    legacy_candidate.write_bytes(legacy_bytes)
    generated_public.unlink()
    legacy_public.unlink()
    (tmp_path / systems_matrix.retained_result_path(RUN_ID)).unlink()
    db_path = review_db.resolve_db_path(tmp_path)
    db_path.unlink()

    values.update(
        {
            "run-status": "running",
            "result-disposition": None,
            "result": None,
            "generated-review": None,
            "memory-review-required": None,
            "legacy-review": None,
            "legacy-review-model-partition": None,
            "failure": None,
        }
    )
    replace_frontmatter(state, values)
    spec = PublicationSpec(
        repo_root=tmp_path,
        run_state_path=state,
        generated_candidate_path=generated_candidate,
        generated_destination=generated_destination,
        legacy_candidate_path=legacy_candidate,
        legacy_destination=legacy_destination,
        legacy_model_partition="codex",
    )
    return state, spec, generated_bytes, legacy_bytes


def accept_prepared_semantic_review(tmp_path: Path, spec: PublicationSpec) -> int:
    prepared = prepare_publication(spec)
    assert prepared.review_batch is not None
    batch = prepared.review_batch
    completed_at = "2026-09-05T12:00:00Z"
    db_path = review_db.resolve_db_path(tmp_path)
    with review_db.connect(db_path) as conn:
        completions = [
            review_db.ReviewPairCompletion(
                note_path=row.note_path,
                criterion_path=row.criterion_path,
                outcome="pass",
                completed_at=completed_at,
            )
            for row in batch.pairs
        ]
        review_db.complete_review_pairs(
            conn,
            review_job_id=batch.review_job_id,
            review_pairs=completions,
            completed_at=completed_at,
        )
        review_db.complete_review_job(
            conn,
            review_job_id=batch.review_job_id,
            completed_at=completed_at,
        )
        for row in batch.pairs:
            assert row.reviewed_note_snapshot_id is not None
            assert row.reviewed_criterion_snapshot_id is not None
            review_db.upsert_freshness_baseline(
                conn,
                note_path=row.note_path,
                criterion_path=row.criterion_path,
                model_partition=row.model_partition,
                evidence_review_pair_id=row.review_pair_id,
                baseline_note_snapshot_id=row.reviewed_note_snapshot_id,
                baseline_criterion_snapshot_id=row.reviewed_criterion_snapshot_id,
                baseline_updated_at=completed_at,
                expected_baseline_revision=row.expected_baseline_revision,
                expected_generation_next_revision=(
                    row.expected_generation_next_revision
                ),
            )
        conn.commit()
    return batch.review_job_id


def test_complete_run_state_verifies_source_and_outputs(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert results.note_type == "agentic-system-analysis-run-state"
    assert any("run state: complete" in item for item in results.passes)
    assert any("README.md" in item and "resolve" in item for item in results.passes)


def test_generated_review_must_live_in_reviews_directory(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    values["generated-review"]["path"] = (  # type: ignore[index]
        "kb/agentic-systems/example-system.md"
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(
        "expected kb/agentic-systems/reviews/<name>.md" in item
        for item in results.fails
    )


def test_running_state_needs_no_recovery_records(tmp_path: Path) -> None:
    configure_types(tmp_path)
    state = tmp_path / f"kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md"
    values: dict[str, object] = {
        "type": "kb/reports/types/agentic-system-analysis-run-state.md",
        "description": f"Minimal completion state for {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "running",
        "result-disposition": None,
        "source": None,
        "result": None,
        "generated-review": None,
        "memory-review-required": None,
        "legacy-review": None,
        "legacy-review-model-partition": None,
        "failure": None,
    }
    write(state, state_text(values))

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


def test_failed_state_requires_only_a_reason(tmp_path: Path) -> None:
    configure_types(tmp_path)
    state = tmp_path / f"kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md"
    values: dict[str, object] = {
        "type": "kb/reports/types/agentic-system-analysis-run-state.md",
        "description": f"Failed run {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "failed",
        "result-disposition": None,
        "source": None,
        "result": None,
        "generated-review": None,
        "memory-review-required": None,
        "legacy-review": None,
        "legacy-review-model-partition": None,
        "failure": "Generated review candidate failed validation; rerun required.",
    }
    write(state, state_text(values))

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


def test_failed_state_without_reason_is_rejected(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    values.update(
        {
            "run-status": "failed",
            "result-disposition": None,
            "source": None,
            "result": None,
            "generated-review": None,
            "memory-review-required": None,
            "legacy-review": None,
            "legacy-review-model-partition": None,
            "failure": None,
        }
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("failure" in item for item in results.fails)


def test_complete_state_rejects_changed_result_bytes(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    result = state.parent / "result.md"
    result.write_text(result.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("result: SHA-256 mismatch" in item for item in results.fails)


def test_complete_state_rejects_invalid_exact_result_with_matching_hash(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    result = state.parent / "result.md"
    result.write_text(
        result.read_text(encoding="utf-8").replace(
            "## Reconciliation\n\nNo conflicts.\n\n",
            "",
        ),
        encoding="utf-8",
    )
    values = frontmatter(state)
    values["result"]["sha256"] = digest(result)  # type: ignore[index]
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("result validation" in item for item in results.fails)


def test_complete_state_rejects_generated_review_from_another_source(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    generated = tmp_path / values["generated-review"]["path"]  # type: ignore[index]
    content = generated.read_text(encoding="utf-8").replace(
        "https://example.invalid/example-system",
        "https://example.invalid/another-system",
    )
    generated.write_text(content, encoding="utf-8")
    values["generated-review"]["sha256"] = digest(generated)  # type: ignore[index]
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("source-identity" in item for item in results.fails)


def test_blocked_result_completes_without_public_review(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    result = state.parent / "result.md"
    content = result.read_text(encoding="utf-8")
    content = content.replace("result-disposition: complete", "result-disposition: blocked")
    content = content.replace(
        f"reviewed-boundary: {values['source']['revision']}",  # type: ignore[index]
        "reviewed-boundary: null",
    )
    content = content.replace(
        "**Generated review:** `kb/agentic-systems/reviews/example-system.md`",
        "**Generated review:** not applicable",
    )
    result.write_text(content, encoding="utf-8")
    values.update(
        {
            "result-disposition": "blocked",
            "source": None,
            "result": {"path": values["result"]["path"], "sha256": digest(result)},  # type: ignore[index]
            "generated-review": None,
            "memory-review-required": False,
            "legacy-review": None,
            "legacy-review-model-partition": None,
        }
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


def test_required_memory_review_must_exist(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    values["memory-review-required"] = True
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("legacy-review" in item or "legacy review" in item for item in results.fails)


def test_required_memory_review_is_byte_verified(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path, legacy=True)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("legacy review: byte identity" in item for item in results.passes)


def test_capture_source_is_byte_verified(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    capture = write(tmp_path / "source.bundle", "captured source\n")
    values = frontmatter(state)
    values["source"] = {
        "kind": "capture",
        "identity": "document bundle",
        "revision": "capture-2026-09-04",
        "path": capture.as_posix(),
        "sha256": digest(capture),
    }
    result = state.parent / "result.md"
    content = result.read_text(encoding="utf-8")
    old_revision = frontmatter(result)["reviewed-boundary"]
    result.write_text(
        content.replace(
            f"reviewed-boundary: {old_revision}",
            "reviewed-boundary: capture-2026-09-04",
        ),
        encoding="utf-8",
    )
    values["result"]["sha256"] = digest(result)  # type: ignore[index]
    generated = tmp_path / values["generated-review"]["path"]  # type: ignore[index]
    generated.write_text(
        generated.read_text(encoding="utf-8").replace(
            f"reviewed-revision: {old_revision}",
            "reviewed-revision: capture-2026-09-04",
        ).replace(
            "source-identity: https://example.invalid/example-system",
            "source-identity: document bundle",
        ),
        encoding="utf-8",
    )
    sync_retained_fixture(tmp_path, values)
    values["generated-review"]["sha256"] = digest(generated)  # type: ignore[index]
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


def test_source_anchor_past_blob_end_is_rejected(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    result = state.parent / "result.md"
    result.write_text(
        result.read_text(encoding="utf-8") + "\nBad citation: `README.md:99`.\n",
        encoding="utf-8",
    )
    values = frontmatter(state)
    values["result"]["sha256"] = digest(result)  # type: ignore[index]
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("outside the recorded blob" in item for item in results.fails)


@pytest.mark.parametrize("output_role", ["result", "generated-review"])
@pytest.mark.parametrize(
    ("citation", "expected_error"),
    [
        ("example/system/blob/{revision}/README.md#L1", None),
        ("EXAMPLE/System/blob/{revision}/README.md#L1-L1", None),
        ("example/system/blob/{revision}/README.md", None),
        ("unrelated/other/blob/{revision}/README.md#L1", "uses repository"),
        ("example/system/blob/main/README.md#L999", "uses revision"),
        ("example/system/blob/main/README.md", "uses revision"),
        ("example/system/blob/{short_revision}/README.md#L1", "uses revision"),
        ("example/system/blob/{wrong_revision}/README.md#L1", "uses revision"),
        ("example/system/blob/{revision}/missing.md#L1", "does not resolve to a blob"),
        ("example/system/blob/{revision}/README.md#L999", "outside the recorded blob"),
        ("example/system/blob/{revision}/README.md#L1oops", "invalid GitHub line anchor"),
        ("example/system/blob/{revision}", "incomplete GitHub blob path"),
    ],
)
def test_github_citations_match_the_frozen_source(
    tmp_path: Path, output_role: str, citation: str, expected_error: str | None
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    source_identity = "https://github.com/example/system"
    values["source"]["identity"] = source_identity
    revision = values["source"]["revision"]
    generated = tmp_path / values["generated-review"]["path"]
    generated_values = frontmatter(generated)
    generated_values["source-identity"] = source_identity
    replace_frontmatter(generated, generated_values)

    output = tmp_path / values[output_role]["path"]
    target = citation.format(
        revision=revision,
        short_revision=revision[:8],
        wrong_revision="0" * len(revision),
    )
    with output.open("a", encoding="utf-8") as handle:
        handle.write(f"\nSource evidence: [source](https://github.com/{target}).\n")
    sync_retained_fixture(tmp_path, values)
    for role in ("result", "generated-review"):
        values[role]["sha256"] = digest(tmp_path / values[role]["path"])
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    if expected_error is None:
        assert results.fails == []
        assert any("resolve" in item and "GitHub" in item for item in results.passes)
    else:
        assert any(expected_error in item for item in results.fails)


def test_operator_handoff_is_rendered_from_complete_state(tmp_path: Path) -> None:
    state_path = valid_run_state(tmp_path)
    content = state_path.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None
    state = parse_agentic_analysis_run_state(
        state_path,
        document,
        repo_root=tmp_path,
    )

    rendered = render_agentic_analysis_handoff(state)

    assert RUN_ID in rendered
    assert "**Result:**" in rendered
    assert "**Frozen source:**" in rendered
    assert (
        "**Generated system review:** "
        "kb/agentic-systems/reviews/example-system.md"
    ) in rendered
    assert "**Run status:** complete" in rendered


def test_handoff_command_refuses_a_running_run(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    values.update(
        {
            "run-status": "running",
            "result-disposition": None,
            "source": None,
            "result": None,
            "generated-review": None,
            "memory-review-required": None,
            "legacy-review": None,
            "legacy-review-model-partition": None,
        }
    )
    replace_frontmatter(state, values)
    monkeypatch.chdir(tmp_path)

    exit_code = agentic_analysis_handoff.main(
        [state.relative_to(tmp_path).as_posix()]
    )

    assert exit_code == 1
    assert "complete run state" in capsys.readouterr().err


def test_handoff_command_renders_a_valid_run(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    state = valid_run_state(tmp_path)
    monkeypatch.chdir(tmp_path)

    exit_code = agentic_analysis_handoff.main(
        [state.relative_to(tmp_path).as_posix()]
    )

    assert exit_code == 0
    assert f"# Agentic-system analysis handoff — {RUN_ID}" in capsys.readouterr().out


def test_prepare_reviews_candidate_bytes_under_the_public_identity(
    tmp_path: Path,
) -> None:
    state, spec, _, legacy_bytes = publication_fixture(tmp_path)
    assert spec.legacy_candidate_path is not None
    direct = validation.validate_note(spec.legacy_candidate_path, repo_root=tmp_path)
    assert direct.fails

    prepared = prepare_publication(spec)

    assert prepared.review_batch is not None
    batch = prepared.review_batch
    assert {row.note_path for row in batch.pairs} == {spec.legacy_destination}
    with review_db.connect(review_db.resolve_db_path(tmp_path)) as conn:
        snapshots = {
            load_snapshot_by_id(conn, row.reviewed_note_snapshot_id)
            for row in batch.pairs
        }
    assert {snapshot.content_text.encode("utf-8") for snapshot in snapshots if snapshot} == {
        legacy_bytes
    }
    assert not (tmp_path / spec.generated_destination).exists()
    assert spec.legacy_destination is not None
    assert not (tmp_path / spec.legacy_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def commit_incumbent(tmp_path: Path, path: Path) -> None:
    subprocess.run(["git", "-C", str(tmp_path), "add", str(path)], check=True)
    subprocess.run(
        [
            "git", "-C", str(tmp_path),
            "-c", "user.name=Commonplace Test",
            "-c", "user.email=test@example.invalid",
            "commit", "--quiet", "-m", "Record incumbent",
        ],
        check=True,
    )


@pytest.mark.parametrize(
    ("recorded_identity", "header_identity", "accepted"),
    [
        ("https://example.invalid/example-system", "", True),
        ("https://example.invalid/example-system-other", "", False),
        (
            "https://example.invalid/example-system-other",
            "https://example.invalid/example-system",
            False,
        ),
        (None, "https://example.invalid/example-system", True),
        (None, "https://example.invalid/example-system-other", False),
    ],
)
def test_prepare_requires_an_exact_legacy_source_identity(
    tmp_path: Path, recorded_identity: str | None, header_identity: str, accepted: bool
) -> None:
    state, spec, _, legacy_bytes = publication_fixture(tmp_path)
    assert spec.legacy_destination is not None
    incumbent = tmp_path / spec.legacy_destination
    incumbent.parent.mkdir(parents=True, exist_ok=True)
    incumbent.write_bytes(legacy_bytes)
    values = frontmatter(incumbent)
    if recorded_identity is None:
        del values["source-identity"]
    else:
        values["source-identity"] = recorded_identity
    replace_frontmatter(incumbent, values)
    content = incumbent.read_text(encoding="utf-8").replace(
        "## Core Ideas", f"**Repository:** {header_identity}\n\n## Core Ideas", 1
    )
    incumbent.write_text(content, encoding="utf-8")
    commit_incumbent(tmp_path, incumbent)

    if accepted:
        assert prepare_publication(spec).review_batch is not None
    else:
        with pytest.raises(ValueError, match="same source"):
            prepare_publication(spec)

    assert incumbent.read_text(encoding="utf-8") == content
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("generated", [True, False])
@pytest.mark.parametrize("staged", [True, False])
def test_prepare_rejects_a_locally_deleted_review(
    tmp_path: Path, generated: bool, staged: bool
) -> None:
    state, spec, generated_bytes, legacy_bytes = publication_fixture(tmp_path)
    destination = spec.generated_destination if generated else spec.legacy_destination
    assert destination is not None
    incumbent = tmp_path / destination
    incumbent.parent.mkdir(parents=True, exist_ok=True)
    incumbent.write_bytes(generated_bytes if generated else legacy_bytes)
    commit_incumbent(tmp_path, incumbent)
    incumbent.unlink()
    if staged:
        subprocess.run(["git", "-C", str(tmp_path), "add", destination], check=True)

    with pytest.raises(ValueError, match="has local changes"):
        prepare_publication(spec)

    assert not incumbent.exists()
    assert frontmatter(state)["run-status"] == "running"


def test_publish_rejects_a_source_mismatch_before_replacing_an_incumbent(
    tmp_path: Path,
) -> None:
    state, spec, _, legacy_bytes = publication_fixture(tmp_path)
    accept_prepared_semantic_review(tmp_path, spec)
    assert spec.legacy_destination is not None
    incumbent = tmp_path / spec.legacy_destination
    incumbent.parent.mkdir(parents=True, exist_ok=True)
    incumbent.write_bytes(legacy_bytes)
    values = frontmatter(incumbent)
    values["source-identity"] = "https://example.invalid/example-system-other"
    replace_frontmatter(incumbent, values)
    old_bytes = incumbent.read_bytes()
    commit_incumbent(tmp_path, incumbent)

    with pytest.raises(ValueError, match="same source"):
        publish_publication(spec)

    assert incumbent.read_bytes() == old_bytes
    assert frontmatter(state)["run-status"] == "running"


def test_publish_requires_current_semantic_passes_and_leaves_incumbents_alone(
    tmp_path: Path,
) -> None:
    state, spec, _, _ = publication_fixture(tmp_path)

    try:
        publish_publication(spec)
    except ValueError as exc:
        assert "semantic baselines" in str(exc)
    else:
        raise AssertionError("publication unexpectedly succeeded without semantic passes")

    assert not (tmp_path / spec.generated_destination).exists()
    assert spec.legacy_destination is not None
    assert not (tmp_path / spec.legacy_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_publish_replaces_the_bundle_and_completes_run_state(tmp_path: Path) -> None:
    state, spec, generated_bytes, legacy_bytes = publication_fixture(tmp_path)
    accept_prepared_semantic_review(tmp_path, spec)

    published = publish_publication(spec)

    assert (tmp_path / spec.generated_destination).read_bytes() == generated_bytes
    assert spec.legacy_destination is not None
    assert (tmp_path / spec.legacy_destination).read_bytes() == legacy_bytes
    assert not spec.generated_candidate_path.exists()
    assert spec.legacy_candidate_path is not None
    assert not spec.legacy_candidate_path.exists()
    values = frontmatter(state)
    assert values["run-status"] == "complete"
    assert values["legacy-review-model-partition"] == "codex"
    assert (tmp_path / published.retained_path).read_bytes() == (state.parent / "result.md").read_bytes()
    assert published.cleanup_warnings == ()
    assert validation.validate_note(state, repo_root=tmp_path).fails == []


def test_publish_rolls_back_an_ordinary_multi_file_write_failure(
    tmp_path: Path,
    monkeypatch,
) -> None:
    state, spec, _, _ = publication_fixture(tmp_path)
    accept_prepared_semantic_review(tmp_path, spec)
    original_state = state.read_bytes()
    assert spec.legacy_destination is not None
    legacy_destination = tmp_path / spec.legacy_destination
    real_atomic_write = agentic_publication._atomic_write

    def fail_on_legacy(path: Path, content: bytes) -> None:
        if path == legacy_destination:
            raise OSError("injected write failure")
        real_atomic_write(path, content)

    monkeypatch.setattr(agentic_publication, "_atomic_write", fail_on_legacy)

    try:
        publish_publication(spec)
    except OSError as exc:
        assert "injected write failure" in str(exc)
    else:
        raise AssertionError("publication unexpectedly survived injected failure")

    assert not (tmp_path / spec.generated_destination).exists()
    assert not legacy_destination.exists()
    assert not (tmp_path / systems_matrix.retained_result_path(RUN_ID)).exists()
    assert state.read_bytes() == original_state
    assert spec.generated_candidate_path.exists()
    assert spec.legacy_candidate_path is not None
    assert spec.legacy_candidate_path.exists()



def test_comparison_tools_use_retained_results_without_local_or_legacy_inputs(tmp_path, monkeypatch, capsys):
    import csv
    import io

    from scripts import analyze_matrix, build_systems_matrix, render_systems_table

    state = valid_run_state(tmp_path)
    retained = tmp_path / systems_matrix.retained_result_path(RUN_ID)
    shutil.rmtree(tmp_path / "kb/reports/state")
    shutil.rmtree(tmp_path / "kb/agent-memory-systems")
    shutil.rmtree(tmp_path / "related-systems")
    assert not state.exists()
    write(tmp_path / "kb/agentic-systems/reviews/README.md", "# Ordinary navigation\n")
    inputs = systems_matrix.load_results(tmp_path)
    assert len(inputs.rows) == 1
    assert inputs.rows[0]["storage_substrate"] == '["files","sqlite"]'
    assert inputs.rows[0]["lineage_assessment"] == "uninspected"
    assert inputs.rows[0]["result_sha256"] == digest(retained)
    for module in (analyze_matrix, build_systems_matrix, render_systems_table):
        monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    matrix = tmp_path / "kb/agentic-systems/comparisons/memory-systems.csv"
    table = matrix.with_suffix(".md")
    assert build_systems_matrix.main(["--output", str(matrix)]) == 0
    assert list(csv.DictReader(io.StringIO(matrix.read_text()))) == inputs.rows
    assert render_systems_table.main(["--output", str(table)]) == 0
    assert "files, sqlite [wired]" in table.read_text()
    assert "## code-grounded (1)" in table.read_text()
    assert digest(retained) in table.read_text()
    assert validation.validate_note(table, repo_root=tmp_path).fails == []
    assert analyze_matrix.main([]) == 0
    output = capsys.readouterr().out
    line = next(line for line in output.splitlines() if line.startswith("storage_substrate "))
    assert line.split()[:3] == ["storage_substrate", "100%", "1"]
    assert "uninspected:" in output
    assert "doc-grounded excluded from statistics: 0" in output


@pytest.mark.parametrize("mutation, error", [
    ("bytes", "SHA-256 mismatch"), ("profile", "memory-comparison"),
    ("source", "source identity missing"), ("revision", "identity mismatch"),
    ("missing", "No such file"),
])
def test_comparison_reader_rejects_incomplete_or_mismatched_evidence(tmp_path, mutation, error):
    valid_run_state(tmp_path)
    retained = tmp_path / systems_matrix.retained_result_path(RUN_ID)
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"
    if mutation == "bytes":
        retained.write_bytes(retained.read_bytes() + b"drift\n")
    elif mutation == "missing":
        retained.unlink()
    elif mutation == "profile":
        data = frontmatter(retained)
        data.pop("memory-comparison")
        replace_frontmatter(retained, data)
        replace_frontmatter(review, {**frontmatter(review), "analysis-result-sha256": digest(retained)})
    else:
        key = "source-identity" if mutation == "source" else "reviewed-revision"
        value = "https://example.invalid/example-system-other" if mutation == "source" else "other"
        replace_frontmatter(review, {**frontmatter(review), key: value})
    with pytest.raises((ValueError, OSError), match=error):
        systems_matrix.load_results(tmp_path)


def test_comparison_population_must_select_one_review_per_source(tmp_path):
    valid_run_state(tmp_path)
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"
    second = review.with_name("second.md")
    second.write_bytes(review.read_bytes())
    with pytest.raises(ValueError, match="multiple selected reviews"):
        systems_matrix.load_results(tmp_path)
    assert len(systems_matrix.load_results(tmp_path, [review]).rows) == 1
    inputs = systems_matrix.load_results(tmp_path, [review])
    review.write_bytes(review.read_bytes() + b"changed\n")
    with pytest.raises(ValueError, match="input changed"):
        inputs.recheck(tmp_path)


def test_publication_requires_comparison_fields_and_preserves_retained_bytes(tmp_path):
    state, spec, _, _ = publication_fixture(tmp_path)
    result = state.parent / "result.md"
    data = frontmatter(result)
    data.pop("memory-comparison")
    old_bytes = result.read_bytes()
    replace_frontmatter(result, data)
    with pytest.raises(ValueError, match="memory-comparison"):
        prepare_publication(spec)
    result.write_bytes(old_bytes)
    retained = write(tmp_path / systems_matrix.retained_result_path(RUN_ID), "frozen earlier result\n")
    with pytest.raises(ValueError, match="already exists"):
        prepare_publication(spec)
    assert retained.read_text() == "frozen earlier result\n"
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("tier,basis,expected_rows,expected_fill", [
    ("code-grounded", "wired", 1, "100%"),
    ("code-grounded", "claimed", 1, "0%"),
    ("code-grounded", "afforded", 1, "0%"),
    ("doc-grounded", "wired", 0, "0%"),
])
def test_statistics_keep_evidence_tiers_and_weaker_bases_separate(tmp_path, monkeypatch, capsys, tier, basis, expected_rows, expected_fill):
    from scripts import analyze_matrix

    valid_run_state(tmp_path)
    retained = tmp_path / systems_matrix.retained_result_path(RUN_ID)
    data = frontmatter(retained)
    data["evidence-tier"] = tier
    data["memory-comparison"]["axes"]["storage_substrate"]["basis"] = basis
    replace_frontmatter(retained, data)
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"
    replace_frontmatter(review, {**frontmatter(review), "analysis-result-sha256": digest(retained)})
    monkeypatch.setattr(analyze_matrix, "REPO_ROOT", tmp_path)
    assert analyze_matrix.main([]) == 0
    output = capsys.readouterr().out
    assert f"rows: {expected_rows}  (code-grounded" in output
    line = next(line for line in output.splitlines() if line.startswith("storage_substrate "))
    assert line.split()[1] == expected_fill
    if expected_rows:
        assert f"known:{basis}" in output
