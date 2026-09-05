from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import validation

REPO_ROOT = Path(__file__).resolve().parents[3]


def result_text(*, disposition: str = "complete", complete_boundary: bool = True) -> str:
    if complete_boundary:
        target_class = '"enclosing runtime"'
        boundary_kind = "whole-system"
        reviewed_boundary = '"0123456789abcdef"'
        analysis_cutoff = '"2026-08-30"'
        evidence_tier = "code-grounded"
    else:
        target_class = "null"
        boundary_kind = "null"
        reviewed_boundary = "null"
        analysis_cutoff = "null"
        evidence_tier = "null"

    return f'''---
type: kb/types/agentic-system-analysis-result.md
description: "Complete external agentic-system analysis at one frozen source boundary with an explicit run disposition"
run-id: AAS-2026-08-30-example-system-01
system: "Example System"
run-date: "2026-08-30"
result-disposition: {disposition}
target-class: {target_class}
boundary-kind: {boundary_kind}
reviewed-boundary: {reviewed_boundary}
analysis-cutoff: {analysis_cutoff}
evidence-tier: {evidence_tier}
---

# Example System agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-08-30-example-system-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/example-system.md`

**Legacy memory review:** not applicable

## Boundary and evidence

Boundary record.

## Source register

Source records.

## Shared records

### Components

Component records.

### Operative objects

Object records.

### Routes

Route records.

### Claims

Claim records.

### Evidenced absences

Absence records.

### Behavioral-authority paths

Authority records.

## Runtime account

Runtime records.

## Lens scoping

### Memory/context scope

Memory scope.

### Epistemic scope

Epistemic scope.

## Lens outputs

### Memory/context lens

Memory findings.

### Epistemic lens

Epistemic findings.

## Reconciliation

Reconciliation records.

## Bounded synthesis

Synthesis.

## Limitations

None.

## Verification and blockers

### Semantic verification

Passed.

### Deterministic validation

Passed.

### Blockers

None.
'''


def validate_external_result(tmp_path: Path, content: str) -> validation.CheckResults:
    result = tmp_path / "example-system-analysis.md"
    result.write_text(content, encoding="utf-8")
    return validation.validate_note(result, repo_root=REPO_ROOT)


def test_complete_response_artifact_validates_outside_a_collection(
    tmp_path: Path,
) -> None:
    results = validate_external_result(tmp_path, result_text())

    assert results.fails == []
    assert results.note_type == "agentic-system-analysis-result"


def test_blocked_result_uses_the_same_shape_with_nullable_boundary(
    tmp_path: Path,
) -> None:
    results = validate_external_result(
        tmp_path,
        result_text(disposition="blocked", complete_boundary=False),
    )

    assert results.fails == []


def test_complete_result_requires_an_established_boundary(tmp_path: Path) -> None:
    results = validate_external_result(
        tmp_path,
        result_text(disposition="complete", complete_boundary=False),
    )

    assert any("frontmatter" in failure for failure in results.fails)


def test_result_requires_every_logical_section(tmp_path: Path) -> None:
    content = result_text().replace("## Reconciliation\n\nReconciliation records.\n\n", "")
    results = validate_external_result(tmp_path, content)

    assert any("Reconciliation" in failure for failure in results.fails)


def test_result_requires_the_canonical_section_order(tmp_path: Path) -> None:
    content = result_text()
    content = content.replace("## Boundary and evidence", "## TEMP", 1)
    content = content.replace("## Source register", "## Boundary and evidence", 1)
    content = content.replace("## TEMP", "## Source register", 1)

    results = validate_external_result(tmp_path, content)

    assert any("canonical reading order" in failure for failure in results.fails)


@pytest.mark.parametrize(
    "line",
    [
        "**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-08-30-example-system-01/run-state.md`\n\n",
        "**Generated review:** `kb/agentic-systems/reviews/example-system.md`\n\n",
        "**Legacy memory review:** not applicable\n\n",
    ],
)
def test_result_requires_each_run_identity_field(tmp_path: Path, line: str) -> None:
    results = validate_external_result(tmp_path, result_text().replace(line, ""))

    assert any("Run identity must" in failure for failure in results.fails)


def test_run_identity_field_value_must_be_on_its_labelled_line(tmp_path: Path) -> None:
    content = result_text().replace(
        "**Generated review:** `kb/agentic-systems/reviews/example-system.md`",
        "**Generated review:**",
    )

    results = validate_external_result(tmp_path, content)

    assert any("generated review" in failure for failure in results.fails)


def test_required_subheadings_must_be_nested_under_their_section(
    tmp_path: Path,
) -> None:
    content = result_text().replace(
        "### Components\n\nComponent records.\n\n",
        "",
    ).replace(
        "## Runtime account\n\nRuntime records.",
        "## Runtime account\n\n### Components\n\nComponent records.\n\nRuntime records.",
    )

    results = validate_external_result(tmp_path, content)

    assert any("Shared-record subheadings" in failure for failure in results.fails)


def test_run_identity_projects_outputs_without_workflow_bookkeeping() -> None:
    contract = (
        REPO_ROOT / "kb" / "types" / "agentic-system-analysis-result.md"
    ).read_text(encoding="utf-8")
    run_identity = contract[
        contract.index("### Run identity") : contract.index("### Boundary and evidence")
    ]

    assert "run-state path" in run_identity
    assert "generated whole-system review path" in run_identity
    assert "legacy memory-review path" in run_identity
    assert "without reproducing workflow bookkeeping" in run_identity
