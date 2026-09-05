from __future__ import annotations

import pytest

from commonplace.lib.agentic_records import record_reference_errors

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
