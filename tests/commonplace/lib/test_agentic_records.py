from __future__ import annotations

import pytest

from commonplace.lib.agentic_records import (
    annotated_ids,
    declared_ids,
    record_reference_errors,
    set_record_errors,
)

BASE = """# Example

## Source register

SRC-1 frozen source.

## Shared records

### Operative objects

OBJ-1 first object, from SRC-1.
OBJ-2 second object.
OBJ-15 third object.

### Routes

RTE-1 route.
RTE-20 another route.

## Lens outputs

"""


@pytest.mark.parametrize("reference", [
    "OBJ-15/O2/O3/O4/O5", "RTE-20–R9", "OBJ-1, O2", "OBJ-1/2",
    "OBJ-1/OBJ-2/O3", "OBJ-1–OBJ-2", "MEM-OBJ-1/O2", "RTE-1-RTE-20",
])
def test_rejects_abbreviated_identifiers_and_ranges(reference: str) -> None:
    assert any("expand shorthand" in error for error in record_reference_errors(BASE + reference))


def test_accepts_complete_lists_and_ignores_source_code() -> None:
    content = BASE + """OBJ-1, OBJ-2; `RTE-1`/`RTE-20`.

> Source example OBJ-999/O2.

```python
print("RTE-999–R9")
```

See OBJ-15 and SRC-1.
"""
    assert record_reference_errors(content) == []


def test_rejects_reference_outside_comparison_fields() -> None:
    assert record_reference_errors(BASE + "Conclusion depends on OBJ-1/OBJ-99.") == [
        "record references: unresolved IDs: OBJ-99"
    ]


def test_rejects_duplicate_declarations() -> None:
    content = BASE.replace("OBJ-2 second object.", "OBJ-1 second object.")
    assert any("duplicate declarations: OBJ-1" in error for error in record_reference_errors(content))


def test_report_can_reference_commissioned_ids_but_not_shorthand() -> None:
    assert record_reference_errors("Uses OBJ-40 and MEM-OBJ-2.", memory_report=True) == []
    assert record_reference_errors("Uses MEM-OBJ-2/O3.", memory_report=True)


def test_result_rejects_unintegrated_proposal_records() -> None:
    assert any("unintegrated proposal" in error
               for error in record_reference_errors(BASE + "See MEM-OBJ-1 and EPI-O2."))


def test_result_allows_explicit_proposal_mapping_in_reconciliation() -> None:
    assert record_reference_errors(BASE + "## Reconciliation\n\nMEM-OBJ-1 maps to OBJ-1.\n") == []


RUNTIME = """# Runtime

## Shared records

### Routes

#### RTE-1 — Ordinary invocation

Record citing SRC-1.

## Annotations

#### On RTE-10 — Benchmark import

Theory-route overlay on the memory route RTE-10.
"""

MEMORY = """# Memory

## Shared records

### Routes

#### On RTE-1 — Ordinary invocation

Memory fields on the seeded route.

#### RTE-10 — Benchmark import

Record citing SRC-2 and OBJ-1.
"""

OVERVIEW = """# Overview

## Source register

| SRC-1 | Git | x |
| SRC-2 | Git | y |
"""


def test_annotation_headings_are_not_declarations() -> None:
    assert declared_ids(MEMORY) == ["RTE-10"]
    assert annotated_ids(MEMORY) == {"RTE-1"}
    assert declared_ids(RUNTIME) == ["RTE-1"]


def test_member_mode_checks_syntax_but_leaves_resolution_to_the_set() -> None:
    assert record_reference_errors(RUNTIME, member=True) == []
    assert any("unresolved" in error for error in record_reference_errors(RUNTIME))


def test_set_resolves_references_across_members() -> None:
    errors = set_record_errors(
        {"runtime.md": RUNTIME, "memory.md": MEMORY}, register_body=OVERVIEW
    )
    assert errors == ["record references: memory.md: unresolved IDs: OBJ-1"]


def test_set_rejects_a_record_declared_in_two_members() -> None:
    twice = MEMORY.replace("#### RTE-10 — Benchmark import", "#### RTE-1 — Again")
    errors = set_record_errors(
        {"runtime.md": RUNTIME, "memory.md": twice}, register_body=OVERVIEW
    )
    assert any("RTE-1 declared in more than one member" in error for error in errors)


def test_set_rejects_surviving_proposal_ids() -> None:
    leaked = MEMORY.replace("OBJ-1", "MEM-OBJ-1")
    errors = set_record_errors(
        {"runtime.md": RUNTIME, "memory.md": leaked}, register_body=OVERVIEW
    )
    assert any("proposal IDs survive finalization: MEM-OBJ-1" in error for error in errors)
