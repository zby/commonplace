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

| ID | Source |
| --- | --- |
| SRC-1 | Frozen source |

## Shared records

### Operative objects

#### OBJ-1 — First object

Evidence: SRC-1.

#### OBJ-2 — Second object

#### OBJ-15 — Third object

### Routes

#### RTE-1 — S3 invocation

#### RTE-20 — Another route

## Lens outputs

"""


def test_heading_title_is_not_inferred_to_be_shorthand() -> None:
    assert record_reference_errors(BASE) == []
    assert set_record_errors({"overview.md": BASE})[1] == []


@pytest.mark.parametrize("reference", ["OBJ-1/O2", "RTE-20–R9", "OBJ-1, O2"])
def test_only_complete_references_are_recognized(reference: str) -> None:
    assert record_reference_errors(BASE + reference) == []
    assert set_record_errors({"overview.md": BASE + reference})[1] == []


@pytest.mark.parametrize("reference", ["OBJ-1/OBJ-99", "OBJ-1–OBJ-99"])
def test_complete_unresolved_references_still_fail(reference: str) -> None:
    _, errors = set_record_errors({"overview.md": BASE + reference})
    assert errors == ["overview.md: unresolved record OBJ-99"]


def test_accepts_complete_lists_and_ignores_source_code() -> None:
    content = BASE + """OBJ-1, OBJ-2; `RTE-1`/`RTE-20`.

> Source example OBJ-999/O2.

```python
print("RTE-999–R9")
```

See OBJ-15 and SRC-1.
"""
    assert record_reference_errors(content) == []
    assert set_record_errors({"overview.md": content})[1] == []


def test_prose_lists_and_tables_are_references_not_declarations() -> None:
    content = BASE.replace("### Routes", """OBJ-1 is retained. Evidence: SRC-1.
- OBJ-1 is consumed later.
| OBJ-1 | Cross-reference |
SRC-1 supplies the evidence.
| SRC-1 | Source cross-reference |

### Routes""")
    assert declared_ids(content) == ["OBJ-1", "OBJ-2", "OBJ-15", "RTE-1", "RTE-20"]
    assert record_reference_errors(content) == []
    assert set_record_errors({"overview.md": content})[1] == []


@pytest.mark.parametrize("heading", [
    "### OBJ-99 — Wrong level", "##### OBJ-99 — Wrong level",
    "#### OBJ-99", "#### OBJ-99 - Wrong separator", "#### SRC-99 — Source",
])
def test_only_prescribed_record_headings_declare(heading: str) -> None:
    assert declared_ids("## Shared records\n\n" + heading + "\n") == []


def test_record_headings_outside_shared_records_do_not_declare() -> None:
    assert declared_ids("## Discussion\n\n#### OBJ-99 — Example\n") == []


def test_rejects_duplicate_declarations() -> None:
    content = BASE.replace("#### OBJ-2 — Second object", "#### OBJ-1 — Second object")
    assert any("duplicate declarations: OBJ-1" in error for error in record_reference_errors(content))


def test_report_can_reference_commissioned_ids() -> None:
    assert record_reference_errors("Uses OBJ-40 and MEM-OBJ-2.", memory_report=True) == []


@pytest.mark.parametrize("prefix", ["", "MEM-"])
def test_local_report_rejects_duplicate_declarations(prefix: str) -> None:
    body = f"""## Shared records

#### {prefix}OBJ-1 — First object

#### {prefix}OBJ-1 — Different object
"""
    assert record_reference_errors(body, memory_report=True) == [
        f"record references: duplicate declarations: {prefix}OBJ-1"
    ]


def test_proposal_and_final_record_have_the_same_declaration_grammar() -> None:
    local = """## Shared records

#### MEM-RTE-1 — S3 invocation

MEM-RTE-1 reads the bucket.
"""
    finalized = local.replace("MEM-RTE-1", "RTE-1")
    assert declared_ids(local, proposals=True) == ["MEM-RTE-1"]
    assert declared_ids(local) == []
    assert declared_ids(finalized) == ["RTE-1"]
    assert record_reference_errors(local, memory_report=True) == []
    assert record_reference_errors(finalized) == []


def test_result_rejects_unintegrated_proposal_records() -> None:
    assert any("unintegrated proposal" in error
               for error in record_reference_errors(BASE + "See MEM-OBJ-1 and EPI-OBJ-2."))


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


def test_annotation_headings_are_not_declarations() -> None:
    assert declared_ids(MEMORY) == ["RTE-10"]
    assert annotated_ids(MEMORY) == {"RTE-1"}
    assert declared_ids(RUNTIME) == ["RTE-1"]


def test_set_resolves_cross_member_references_and_annotations() -> None:
    overview = "## Source register\n\n| SRC-1 | Runtime source |\n| SRC-2 | Memory source |\n"
    memory = MEMORY + "\n#### OBJ-1 — Stored object\n"
    known, errors = set_record_errors({
        "overview.md": overview, "runtime.md": RUNTIME, "memory.md": memory,
    })
    assert known == {"SRC-1", "SRC-2", "RTE-1", "RTE-10", "OBJ-1"}
    assert errors == []


def test_set_rejects_duplicate_record_across_members() -> None:
    _, errors = set_record_errors({"overview.md": BASE, "runtime.md": RUNTIME})
    assert "duplicate set declaration: RTE-1" in errors


def test_set_rejects_duplicate_source_rows() -> None:
    content = BASE.replace("| SRC-1 | Frozen source |", "| SRC-1 | First |\n| SRC-1 | Second |")
    _, errors = set_record_errors({"overview.md": content})
    assert errors == ["duplicate set declaration: SRC-1"]


def test_only_overview_source_register_table_declares_sources() -> None:
    overview = """## Source register

SRC-1 is mentioned in prose.
- SRC-2 is mentioned in a list.
#### SRC-3 — Heading
| Other column | SRC-4 |
| SRC-5 | Actual source |

## Other section

| SRC-6 | Not in the register |
"""
    known, errors = set_record_errors({
        "overview.md": overview,
        "memory.md": "## Source register\n\n| SRC-7 | Not in the overview |\n",
    })
    assert known == {"SRC-5"}
    assert len(errors) == 6
    assert all("unresolved record SRC-" in error for error in errors)
