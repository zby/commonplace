from __future__ import annotations

import re
import shutil
import subprocess
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.cli import agentic_analysis_handoff, agentic_analysis_publication
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
        "agent-memory-analysis-report.md",
        "agent-memory-analysis-report.schema.yaml",
    ):
        shutil.copyfile(REPO_ROOT / "kb/reports/types" / name, report_types / name)
    write(tmp_path / "kb/reports/COLLECTION.md", "# Reports\n")
    shutil.copytree(
        REPO_ROOT / "kb/instructions/review-gates",
        tmp_path / "kb/instructions/review-gates",
    )


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


def memory_report_fixture(run_dir: Path, revision: str) -> Path:
    handoff = write(run_dir / "memory-input.md", "# Frozen memory input\n\nOBJ-1 fixture object. RTE-1 fixture route.\n")
    profile = {
        "scope": "Fixture scope",
        "axes": {axis: {"assessment": "uninspected", "basis": None,
                         "values": [], "records": [], "note": "Fixture gap."}
                 for axis in systems_matrix.AXES},
    }
    values = {
        "type": "kb/reports/types/agent-memory-analysis-report.md",
        "description": "Fixture specialist report bound to the frozen source and shared input",
        "analysis-run": RUN_ID,
        "source-identity": "https://example.invalid/example-system",
        "reviewed-boundary": revision,
        "report-status": "complete",
        "canonical-register-sha256": digest(handoff),
        "worker-model": "fixture-model",
        "method-sha256": "a" * 64,
        "memory-comparison": profile,
    }
    body = "# Fixture memory analysis\n\n" + "\n\n".join(
        f"## {heading}\n\nFixture evidence."
        for heading in ("Boundary and evidence", "Core ideas", "Shared records",
                        "Write side", "Read-back", "Comparison rationale",
                        "Integration issues", "Limitations and checks")
    )
    return write(run_dir / "memory-report.md", "---\n" + yaml.safe_dump(values) + "---\n\n" + body + "\n")


def valid_run_state(tmp_path: Path) -> Path:
    configure_types(tmp_path)
    run_dir = tmp_path / "kb/reports/state/agentic-system-analysis" / RUN_ID
    source_root, revision = git_checkout(
        tmp_path / "related-systems/example--system"
    )
    result_path = f"kb/reports/state/agentic-system-analysis/{RUN_ID}/result.md"
    report = memory_report_fixture(run_dir, revision)
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

**Memory analysis report:** `{report.relative_to(tmp_path).as_posix()}`

**Memory analysis report SHA-256:** `{digest(report)}`

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
    report = result.parent / "memory-report.md"
    report_values = frontmatter(report)
    report_values.update({"source-identity": values["source"]["identity"],
                          "reviewed-boundary": values["source"]["revision"]})
    replace_frontmatter(report, report_values)
    result.write_text(re.sub(r"(\*\*Memory analysis report SHA-256:\*\* )`[0-9a-f]+`",
                             rf"\g<1>`{digest(report)}`", result.read_text()))
    values["result"]["sha256"] = digest(result)
    generated = tmp_path / values["generated-review"]["path"]
    (tmp_path / systems_matrix.retained_result_path(RUN_ID)).write_bytes(result.read_bytes())
    replace_frontmatter(generated, {**frontmatter(generated), "analysis-result-sha256": digest(result)})


def publication_fixture(tmp_path: Path) -> tuple[Path, PublicationSpec, bytes]:
    state = valid_run_state(tmp_path)
    subprocess.run(["git", "init", "--quiet", str(tmp_path)], check=True)
    values = frontmatter(state)
    destination = values["generated-review"]["path"]
    public = tmp_path / destination
    generated_bytes = public.read_bytes()
    candidate = state.parent / "generated-review.candidate.md"
    candidate.write_bytes(generated_bytes)
    public.unlink()
    (tmp_path / systems_matrix.retained_result_path(RUN_ID)).unlink()
    values.update({"run-status": "running", "result-disposition": None,
                   "result": None, "generated-review": None, "failure": None})
    replace_frontmatter(state, values)
    return state, PublicationSpec(tmp_path, state, candidate, destination), generated_bytes


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



        }
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


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
        )
        + "\n> captured\n> source\n"
        + "> --- [captured source](https://example.invalid/captured-source)\n",
        encoding="utf-8",
    )
    sync_retained_fixture(tmp_path, values)
    values["generated-review"]["sha256"] = digest(generated)  # type: ignore[index]
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("frozen capture" in item for item in results.passes)


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


@pytest.mark.parametrize("output_role", ["result", "generated-review"])
@pytest.mark.parametrize("citation_kind", ["local", "github"])
def test_quote_anchors_resolve_from_the_recorded_commit(
    tmp_path: Path, output_role: str, citation_kind: str
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    revision = values["source"]["revision"]
    if citation_kind == "github":
        source_identity = "https://github.com/example/system"
        values["source"]["identity"] = source_identity
        generated = tmp_path / values["generated-review"]["path"]
        replace_frontmatter(
            generated,
            {**frontmatter(generated), "source-identity": source_identity},
        )
        attribution = (
            "[README.md](https://github.com/example/system/blob/"
            f"{revision}/README.md)"
        )
    else:
        attribution = f"`README.md` @ `{revision}`"

    source_root = Path(values["source"]["path"])
    write(source_root / "README.md", "# Changed worktree\n")
    output = tmp_path / values[output_role]["path"]
    with output.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> # Frozen\n> source\n"
            f"> --- {attribution}\n"
        )
    sync_retained_fixture(tmp_path, values)
    for role in ("result", "generated-review"):
        values[role]["sha256"] = digest(tmp_path / values[role]["path"])
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("quote resolves" in item for item in results.passes)


def test_quote_anchor_rejects_text_found_only_in_the_worktree(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    revision = values["source"]["revision"]
    source_root = Path(values["source"]["path"])
    write(source_root / "README.md", "# Changed worktree\n")
    generated = tmp_path / values["generated-review"]["path"]
    with generated.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> # Changed worktree\n"
            f"> --- `README.md` @ `{revision}`\n"
        )
    sync_retained_fixture(tmp_path, values)
    values["result"]["sha256"] = digest(tmp_path / values["result"]["path"])
    values["generated-review"]["sha256"] = digest(generated)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("quote does not occur" in item for item in results.fails)


def test_quote_anchor_rejects_a_local_revision_mismatch(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    generated = tmp_path / values["generated-review"]["path"]
    with generated.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> # Frozen source\n"
            f"> --- `README.md` @ `{'0' * 40}`\n"
        )
    sync_retained_fixture(tmp_path, values)
    values["result"]["sha256"] = digest(tmp_path / values["result"]["path"])
    values["generated-review"]["sha256"] = digest(generated)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("local attribution uses revision" in item for item in results.fails)


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


def test_prepare_checks_handoff_without_publishing(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    assert prepare_publication(spec).prepared
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("mutation", ["valid", "vocabulary", "empty", "outside", "absence", "dependency"])
def test_standing_memory_report_comparison_validation(tmp_path: Path, mutation: str) -> None:
    state = valid_run_state(tmp_path)
    report = state.parent / "memory-report.md"
    body = report.read_text().replace(
        "## Shared records\n", "## Shared records\n\nMEM-OBJ-1 fixture object.\nMEM-ABS-1 inspected absence.\n"
    )
    report.write_text(body)
    metadata = frontmatter(report)
    axes = metadata["memory-comparison"]["axes"]
    axes["storage_substrate"] = {
        "assessment": "known", "basis": "wired", "values": ["files"],
        "records": ["MEM-OBJ-1"], "note": "Fixture source writes files.",
    }
    axes["trace_learning"] = {
        "assessment": "absent", "basis": None, "values": [],
        "records": ["MEM-ABS-1"], "note": "Fixture source was inspected.",
    }
    expected_error = None
    if mutation == "vocabulary":
        axes["storage_substrate"]["values"] = ["invented"]
        expected_error = "off-vocabulary"
    elif mutation == "empty":
        axes["storage_substrate"]["values"] = []
        expected_error = "known assessment needs"
    elif mutation == "outside":
        report.write_text(report.read_text().replace("MEM-OBJ-1 fixture object.\n", "") + "\nMEM-OBJ-1 outside the register.\n")
        expected_error = "unresolved shared or proposed"
    elif mutation == "absence":
        axes["trace_learning"]["records"] = ["MEM-OBJ-1"]
        expected_error = "absence requires"
    elif mutation == "dependency":
        axes["trace_learning"].update({"assessment": "known", "basis": "wired", "values": ["no"]})
        expected_error = "must be inapplicable"
    replace_frontmatter(report, metadata)
    checked = validation.validate_note(report, repo_root=tmp_path)
    if expected_error:
        assert any(expected_error in error for error in checked.fails)
    else:
        assert checked.fails == []
        assert any("shared or proposed references resolve" in message for message in checked.passes)
        document, error = validation.parse_document(report.read_text())
        assert error is None
        with pytest.raises(ValueError, match="unresolved canonical"):
            systems_matrix.validate_comparison(metadata["memory-comparison"], document.body)


@pytest.mark.parametrize("name", ["memory-report.md", "memory-input.md"])
def test_publication_cannot_consume_specialist_evidence_as_candidate(tmp_path: Path, name: str) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    with pytest.raises(ValueError, match="reserved"):
        prepare_publication(PublicationSpec(tmp_path, state, state.parent / name, spec.generated_destination))


def test_publication_cli_rejects_retired_legacy_arguments(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    with pytest.raises(SystemExit) as error:
        agentic_analysis_publication.main([
            "prepare", str(state), "--generated-candidate", str(spec.generated_candidate_path),
            "--generated-destination", spec.generated_destination,
            "--legacy-candidate", "retired.md",
        ], cwd=tmp_path)
    assert error.value.code == 2


def test_memory_report_quote_is_checked_at_the_frozen_source(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    report = state.parent / "memory-report.md"
    revision = frontmatter(state)["source"]["revision"]
    report.write_text(report.read_text() + f"\n> absent quotation\n> --- `README.md` @ `{revision}`\n")
    result = state.parent / "result.md"
    result.write_text(re.sub(r"(\*\*Memory analysis report SHA-256:\*\* )`[0-9a-f]+`",
                             rf"\g<1>`{digest(report)}`", result.read_text()))
    with pytest.raises(ValueError, match="memory report:.*quote does not occur"):
        prepare_publication(spec)


def test_prepare_rejects_an_unresolved_quote_in_a_candidate(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    running_values = frontmatter(state)
    revision = running_values["source"]["revision"]
    with spec.generated_candidate_path.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> text absent from the source\n"
            f"> --- `README.md` @ `{revision}`\n"
        )

    with pytest.raises(ValueError, match="quote does not occur"):
        prepare_publication(spec)

    assert not (tmp_path / spec.generated_destination).exists()
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


@pytest.mark.parametrize("staged", [True, False])
def test_prepare_rejects_a_locally_deleted_review(
    tmp_path: Path, staged: bool
) -> None:
    state, spec, generated_bytes = publication_fixture(tmp_path)
    destination = spec.generated_destination
    assert destination is not None
    incumbent = tmp_path / destination
    incumbent.parent.mkdir(parents=True, exist_ok=True)
    incumbent.write_bytes(generated_bytes)
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
    state, spec, generated_bytes = publication_fixture(tmp_path)
    prepare_publication(spec)
    incumbent = tmp_path / spec.generated_destination
    incumbent.parent.mkdir(parents=True, exist_ok=True)
    incumbent.write_bytes(generated_bytes)
    values = frontmatter(incumbent)
    values["source-identity"] = "https://example.invalid/example-system-other"
    replace_frontmatter(incumbent, values)
    old_bytes = incumbent.read_bytes()
    commit_incumbent(tmp_path, incumbent)

    with pytest.raises(ValueError, match="same source"):
        publish_publication(spec)

    assert incumbent.read_bytes() == old_bytes
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("mutation", ["missing", "bytes", "input", "run", "source", "boundary", "blocked"])
def test_publication_requires_exact_completed_memory_handoff(tmp_path: Path, mutation: str) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    report = state.parent / "memory-report.md"
    if mutation == "missing":
        report.unlink()
    elif mutation == "bytes":
        report.write_text(report.read_text() + "\nChanged.\n")
    elif mutation == "input":
        (state.parent / "memory-input.md").write_text("Changed input.\n")
    else:
        values = frontmatter(report)
        field = {"run": "analysis-run", "source": "source-identity", "boundary": "reviewed-boundary", "blocked": "report-status"}[mutation]
        values[field] = "blocked" if mutation == "blocked" else "different"
        replace_frontmatter(report, values)
        result = state.parent / "result.md"
        result.write_text(re.sub(r"(\*\*Memory analysis report SHA-256:\*\* )`[0-9a-f]+`", rf"\g<1>`{digest(report)}`", result.read_text()))
    with pytest.raises(ValueError, match="memory report"):
        publish_publication(spec)
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_publish_replaces_the_bundle_and_completes_run_state(tmp_path: Path) -> None:
    state, spec, generated_bytes = publication_fixture(tmp_path)
    prepare_publication(spec)

    published = publish_publication(spec)

    assert (tmp_path / spec.generated_destination).read_bytes() == generated_bytes
    assert not spec.generated_candidate_path.exists()
    values = frontmatter(state)
    assert values["run-status"] == "complete"
    assert (tmp_path / published.retained_path).read_bytes() == (state.parent / "result.md").read_bytes()
    assert published.cleanup_warnings == ()
    assert validation.validate_note(state, repo_root=tmp_path).fails == []


def test_publication_resolves_links_to_results_in_the_same_bundle(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    retained = tmp_path / systems_matrix.retained_result_path(RUN_ID)
    candidate = spec.generated_candidate_path
    content = candidate.read_text() + (
        f"\n[Exact analysis](../../reports/retained/agentic-system-analysis/{RUN_ID}/result.md)\n"
    )
    candidate.write_text(content)

    assert prepare_publication(spec).prepared
    assert not retained.exists()
    assert not (tmp_path / spec.generated_destination).exists()

    candidate.write_text(content + "\n[Missing](./not-in-the-bundle.md)\n")
    with pytest.raises(ValueError, match="missing target ./not-in-the-bundle.md"):
        prepare_publication(spec)
    assert not retained.exists()

    candidate.write_text(content)
    prepare_publication(spec)
    publish_publication(spec)
    assert retained.read_bytes() == (state.parent / "result.md").read_bytes()
    assert (tmp_path / spec.generated_destination).read_text() == content
    checks = validation.validate_note(state, repo_root=tmp_path)
    assert checks.fails == []
    assert checks.warns == []


def test_publish_rolls_back_an_ordinary_multi_file_write_failure(
    tmp_path: Path,
    monkeypatch,
) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    prepare_publication(spec)
    original_state = state.read_bytes()
    failure_destination = state
    real_atomic_write = agentic_publication._atomic_write

    def fail_on_state(path: Path, content: bytes) -> None:
        if path == failure_destination:
            raise OSError("injected write failure")
        real_atomic_write(path, content)

    monkeypatch.setattr(agentic_publication, "_atomic_write", fail_on_state)

    try:
        publish_publication(spec)
    except OSError as exc:
        assert "injected write failure" in str(exc)
    else:
        raise AssertionError("publication unexpectedly survived injected failure")

    assert not (tmp_path / spec.generated_destination).exists()
    assert not (tmp_path / systems_matrix.retained_result_path(RUN_ID)).exists()
    assert state.read_bytes() == original_state
    assert spec.generated_candidate_path.exists()



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
    state, spec, _ = publication_fixture(tmp_path)
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
