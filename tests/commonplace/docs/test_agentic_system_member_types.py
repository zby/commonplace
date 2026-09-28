from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import validation

REPO_ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-09-28-example-system-01"
REVISION = "0123456789abcdef0123456789abcdef01234567"
INPUTS_COMMIT = "fedcba9876543210fedcba9876543210fedcba98"
MEMBERS = "\n".join(
    f"  - path: {name}.md\n    sha256: \"{'a' * 64}\"\n    type: types/{kind}.md"
    for name, kind in (
        ("runtime", "agentic-system-runtime-report"),
        ("memory", "agent-memory-analysis-report"),
        ("epistemic", "agentic-system-epistemic-report"),
    )
)


def overview_text(*, disposition: str = "complete") -> str:
    complete = disposition == "complete"
    return f'''---
type: types/agentic-system-analysis-overview.md
description: "Complete analysis of Example System at one frozen boundary"
run-id: {RUN_ID}
system: "Example System"
run-date: "2026-09-28"
result-disposition: {disposition}
target-class: {'"enclosing runtime"' if complete else "null"}
boundary-kind: {"whole-system" if complete else "null"}
reviewed-boundary: {f'"{REVISION}"' if complete else "null"}
analysis-cutoff: {'"2026-09-28"' if complete else "null"}
evidence-tier: {"code-grounded" if complete else "null"}
inputs-commit: "{INPUTS_COMMIT}"
members:{chr(10) + MEMBERS if complete else " []"}
---

# Example System agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/example-system.md`

## Boundary and evidence

Boundary record.

## Source register

| SRC-1 | Git | `https://example.invalid/example-system` | `{REVISION}` | implementation | README.md | anchors | none |

## Lens scoping

### Memory/context scope

Scope.

### Epistemic scope

Scope.

## Reconciliation

None.

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


RUNTIME_TEXT = f'''---
type: types/agentic-system-runtime-report.md
description: "Runtime baseline of Example System"
run-id: {RUN_ID}
reviewed-boundary: "{REVISION}"
---

# Example System runtime report

## Runtime account

Trace.

## Probe evidence

none

## Shared records

### Components

#### CMP-1 — Model endpoint

Record.

### Operative objects

none declared in this member.

### Routes

#### RTE-1 — Ordinary invocation

Record. Evidence: SRC-1.

### Claims

none declared in this member.

### Evidenced absences

none declared in this member.

### Behavioral-authority paths

none declared in this member.

## Annotations

none
'''

EPISTEMIC_TEXT = f'''---
type: types/agentic-system-epistemic-report.md
description: "Epistemic routes of Example System"
run-id: {RUN_ID}
reviewed-boundary: "{REVISION}"
---

# Example System epistemic report

## Source-and-claim boundary

Boundary.

## Epistemic-object inventory

Inventory.

## Authority-route ledger

Ledger.

## Per-object lifecycle disposition

Disposition.

## System-claim versus route comparison

None found.

## Bounded conclusion

Conclusion.
'''

REVIEW_TEXT = f'''---
type: agentic-systems/types/generated-review.md
description: "Example System's mechanism in one sentence."
generated-by: analyse-agentic-system
analysis-run: {RUN_ID}
source-identity: https://example.invalid/example-system
reviewed-revision: "{REVISION}"
analysis-overview: kb/reports/retained/agentic-system-analysis/{RUN_ID}/overview.md
analysis-overview-sha256: "{'b' * 64}"
---

# Example System

Evidence basis: source at `{REVISION}`, inspected 2026-09-28.

Body.
'''


def validate(tmp_path: Path, name: str, content: str) -> validation.CheckResults:
    path = tmp_path / name
    path.write_text(content, encoding="utf-8")
    return validation.validate_note(path, repo_root=REPO_ROOT)


def test_complete_overview_validates_with_three_members(tmp_path: Path) -> None:
    results = validate(tmp_path, "overview.md", overview_text())
    assert results.fails == []
    assert results.note_type == "agentic-system-analysis-overview"


def test_blocked_overview_has_no_members_and_nullable_boundary(tmp_path: Path) -> None:
    results = validate(tmp_path, "overview.md", overview_text(disposition="blocked"))
    assert results.fails == []


def test_complete_overview_requires_every_member(tmp_path: Path) -> None:
    content = overview_text().replace(
        "  - path: epistemic.md\n    sha256: \"" + "a" * 64 + "\"\n    type: types/agentic-system-epistemic-report.md",
        "",
    )
    results = validate(tmp_path, "overview.md", content)
    assert any("frontmatter" in failure for failure in results.fails)


def test_blocked_overview_rejects_members(tmp_path: Path) -> None:
    content = overview_text(disposition="blocked").replace("members: []", "members:\n" + MEMBERS)
    results = validate(tmp_path, "overview.md", content)
    assert any("frontmatter" in failure for failure in results.fails)


def test_overview_requires_the_canonical_section_order(tmp_path: Path) -> None:
    content = overview_text()
    content = content.replace("## Boundary and evidence", "## TEMP", 1)
    content = content.replace("## Source register", "## Boundary and evidence", 1)
    content = content.replace("## TEMP", "## Source register", 1)
    results = validate(tmp_path, "overview.md", content)
    assert any("canonical reading order" in failure for failure in results.fails)


@pytest.mark.parametrize(
    "line",
    [
        f"**Run state:** `kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md`\n\n",
        "**Generated review:** `kb/agentic-systems/reviews/example-system.md`\n\n",
    ],
)
def test_overview_requires_each_run_identity_field(tmp_path: Path, line: str) -> None:
    results = validate(tmp_path, "overview.md", overview_text().replace(line, ""))
    assert len(results.fails) == 1
    assert "Run identity" in results.fails[0]


def test_runtime_report_validates(tmp_path: Path) -> None:
    results = validate(tmp_path, "runtime.md", RUNTIME_TEXT)
    assert results.fails == []
    assert results.note_type == "agentic-system-runtime-report"


def test_runtime_report_requires_record_kinds_under_shared_records(tmp_path: Path) -> None:
    content = RUNTIME_TEXT.replace("### Claims\n\nnone declared in this member.\n\n", "")
    results = validate(tmp_path, "runtime.md", content)
    assert any("Claims" in failure for failure in results.fails)


def test_epistemic_report_validates_and_orders_blocks(tmp_path: Path) -> None:
    assert validate(tmp_path, "epistemic.md", EPISTEMIC_TEXT).fails == []
    swapped = EPISTEMIC_TEXT.replace("## Authority-route ledger", "## TEMP", 1)
    swapped = swapped.replace("## Epistemic-object inventory", "## Authority-route ledger", 1)
    swapped = swapped.replace("## TEMP", "## Epistemic-object inventory", 1)
    assert validate(tmp_path, "epistemic.md", swapped).fails != []


def test_generated_review_validates_and_pins_the_overview(tmp_path: Path) -> None:
    results = validate(tmp_path, "example-system.md", REVIEW_TEXT)
    assert results.fails == []
    assert results.note_type == "generated-review"
    broken = REVIEW_TEXT.replace("/overview.md", "/result.md")
    assert any("frontmatter" in failure for failure in validate(tmp_path, "example-system.md", broken).fails)
    no_basis = REVIEW_TEXT.replace("Evidence basis: ", "Basis: ")
    assert validate(tmp_path, "example-system.md", no_basis).fails != []
