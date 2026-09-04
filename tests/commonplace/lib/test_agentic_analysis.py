from __future__ import annotations

import shutil
import subprocess
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.cli import agentic_analysis_handoff
from commonplace.lib import validation
from commonplace.lib.agentic_analysis import (
    parse_agentic_analysis_run_state,
    render_agentic_analysis_handoff,
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

**Run state:** `kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md` — complete.

**Generated review:** `kb/agentic-systems/example-system.md`.

**Legacy memory review:** not applicable.

## Boundary and evidence

Fixture boundary at `{revision}`.

## Source register

Source evidence: SRC-1, `README.md:1`.

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
    generated_path = "kb/agentic-systems/example-system.md"
    generated = write(
        tmp_path / generated_path,
        f'''---
description: "Generated fixture review of one external agentic system"
type: kb/types/note.md
generated-by: analyse-agentic-system
analysis-run: {RUN_ID}
source-identity: https://example.invalid/example-system
reviewed-revision: {revision}
---

# Example System

**Evidence basis:** `README.md:1` at `{revision}`.
''',
    )
    legacy_output: dict[str, str] | None = None
    if legacy:
        legacy_path = "kb/agent-memory-systems/reviews/example-system.md"
        legacy_file = write(
            tmp_path / legacy_path,
            '''---
description: "Fixture memory-system review with source-grounded mechanisms"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-09-04"
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
        legacy_output = {"path": legacy_path, "sha256": digest(legacy_file)}

    frontmatter: dict[str, object] = {
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
        "failure": None,
    }
    return write(run_dir / "run-state.md", state_text(frontmatter))


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


def test_complete_run_state_verifies_source_and_outputs(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert results.note_type == "agentic-system-analysis-run-state"
    assert any("run state: complete" in item for item in results.passes)
    assert any("README.md" in item and "resolve" in item for item in results.passes)


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
    result.write_text(content, encoding="utf-8")
    values.update(
        {
            "result-disposition": "blocked",
            "source": None,
            "result": {"path": values["result"]["path"], "sha256": digest(result)},  # type: ignore[index]
            "generated-review": None,
            "memory-review-required": False,
            "legacy-review": None,
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
    assert "**Generated system review:** kb/agentic-systems/example-system.md" in rendered
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
