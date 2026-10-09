from __future__ import annotations

from pathlib import Path

from commonplace.lib import validation

REPO_ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-09-28-example-system-01"
REVISION = "0123456789abcdef0123456789abcdef01234567"
INPUTS_COMMIT = "fedcba9876543210fedcba9876543210fedcba98"


def overview_text(*, disposition: str = "complete") -> str:
    complete = disposition == "complete"
    return f'''---
type: agentic-system-analyses/types/agentic-system-analysis-overview.md
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
---

# Example System agentic-system analysis

## Members

- [Boundary](./boundary.md)
- [Synthesis](./synthesis.md)

## Amendment index

None.

## Deterministic validation

Passed.
'''


RUNTIME_TEXT = f'''---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of Example System"
run-id: {RUN_ID}
reviewed-boundary: "{REVISION}"
---

# Example System runtime report

## Runtime account

Trace.

## Shared records

### Components

#### RT-CMP-model — Model endpoint

Record.

### Operative objects

none declared in this member.

### Routes

#### RT-RTE-model-call — Ordinary invocation

- implementation conclusion status: wired

- Immediate return: The checked object is returned to the caller.
- Later read-back: uninspected — no later consumer was inspected.
- Delegated visibility: inapplicable — there is no delegation in this fixture.
- Selection predicate: The caller selects the object.
- Invalidation or expiry: inapplicable — no expiry is implemented here.
- Activation or effect: uninspected — operation was not observed.
- Evidence limits: Static fixture evidence at SRC-1.

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
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
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

Route ID: RT-RTE-model-call
Route function: operational admission/selection/consumption
Architectural status: implemented
Content/update relation: no content change.

## System-claim versus route comparison

None found.

## Bounded conclusion

Conclusion.

## Shared records

### Routes

#### EPI-RTE-model-call — Admission check

- implementation conclusion status: wired

- Immediate return: The checked object is returned to the caller.
- Later read-back: uninspected — no later consumer was inspected.
- Delegated visibility: inapplicable — there is no delegation in this fixture.
- Selection predicate: The caller selects the object.
- Invalidation or expiry: inapplicable — no expiry is implemented here.
- Activation or effect: uninspected — operation was not observed.
- Evidence limits: Static fixture evidence at SRC-1.

Record. Evidence: SRC-1.
'''

RECONCILIATION_TEXT = f'''---
type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
description: "Reconciled Example System records at the frozen source boundary"
run-id: {RUN_ID}
reviewed-boundary: "{REVISION}"
---

# Example System reconciliation

## Reconciliation

Amendment: EPI-OBJ-store is superseded by RT-OBJ-store; both name the same store at SRC-1.
'''


def validate(tmp_path: Path, name: str, content: str) -> validation.CheckResults:
    path = tmp_path / name
    path.write_text(content, encoding="utf-8")
    return validation.validate_note(path, repo_root=REPO_ROOT)


def test_overview_validates_independently_of_siblings(tmp_path: Path) -> None:
    results = validate(tmp_path, "overview.md", overview_text())
    assert results.fails == []
    assert results.note_type == "agentic-system-analysis-overview"


def test_blocked_overview_has_nullable_boundary(tmp_path: Path) -> None:
    results = validate(tmp_path, "overview.md", overview_text(disposition="blocked"))
    assert results.fails == []


def test_overview_rejects_obsolete_manifest_metadata(tmp_path: Path) -> None:
    content = overview_text().replace("inputs-commit:", "members: []\ninputs-commit:")
    results = validate(tmp_path, "overview.md", content)
    assert results.fails


def test_overview_requires_the_canonical_section_order(tmp_path: Path) -> None:
    content = overview_text()
    content = content.replace("## Members", "## TEMP", 1)
    content = content.replace("## Amendment index", "## Members", 1)
    content = content.replace("## TEMP", "## Amendment index", 1)
    results = validate(tmp_path, "overview.md", content)
    assert any("canonical reading order" in failure for failure in results.fails)


def test_runtime_report_validates(tmp_path: Path) -> None:
    results = validate(tmp_path, "runtime.md", RUNTIME_TEXT)
    assert results.fails == []
    assert results.note_type == "agentic-system-runtime-report"


def test_member_validation_rejects_missing_route_answers(tmp_path: Path) -> None:
    content = RUNTIME_TEXT.replace(
        "- Selection predicate: The caller selects the object.\n", ""
    )
    failures = validate(tmp_path, "runtime.md", content).fails
    assert any("RT-RTE-model-call: Selection predicate: missing field" in error for error in failures)


def test_runtime_report_requires_record_kinds_under_shared_records(tmp_path: Path) -> None:
    content = RUNTIME_TEXT.replace("### Claims\n\nnone declared in this member.\n\n", "")
    results = validate(tmp_path, "runtime.md", content)
    assert any("Claims" in failure for failure in results.fails)


def test_runtime_report_has_no_amendments_section(tmp_path: Path) -> None:
    amended = RUNTIME_TEXT + "\n## Amendments\n\nAmendment: RT-OBJ-store label changed.\n"
    assert validate(tmp_path, "runtime.md", amended).fails != []


def test_epistemic_report_validates_and_orders_blocks(tmp_path: Path) -> None:
    assert validate(tmp_path, "epistemic.md", EPISTEMIC_TEXT).fails == []
    swapped = EPISTEMIC_TEXT.replace("## Authority-route ledger", "## TEMP", 1)
    swapped = swapped.replace("## Epistemic-object inventory", "## Authority-route ledger", 1)
    swapped = swapped.replace("## TEMP", "## Epistemic-object inventory", 1)
    assert validate(tmp_path, "epistemic.md", swapped).fails != []


def test_epistemic_report_declares_its_records_under_shared_records(tmp_path: Path) -> None:
    missing = EPISTEMIC_TEXT[: EPISTEMIC_TEXT.index("## Shared records")]
    assert validate(tmp_path, "epistemic.md", missing).fails != []


def test_reconciliation_report_validates_and_has_one_section(tmp_path: Path) -> None:
    assert validate(tmp_path, "reconciliation.md", RECONCILIATION_TEXT).fails == []
    extra = RECONCILIATION_TEXT + "\n## Open questions\n\nMEM-OBJ-store needs a second look.\n"
    assert validate(tmp_path, "reconciliation.md", extra).fails
