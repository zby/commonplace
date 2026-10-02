from __future__ import annotations

import pytest

from commonplace.lib.agentic_records import (
    annotated_ids,
    declared_ids,
    record_reference_errors,
    route_field_errors,
    set_record_errors,
)

ROUTE_ANSWERS = """- Immediate return: A stored preference is returned.
- Later read-back: The next invocation reads the retained preference.
- Delegated visibility: inapplicable — this route does not delegate.
- Selection predicate: The caller's key selects the preference.
- Invalidation or expiry: inapplicable — no expiry is implemented.
- Activation or effect: uninspected — model behavior was not observed.
- Evidence limits: Static inspection; no execution trace.
"""


def route_body(identifier: str = "RTE-1", answers: str = ROUTE_ANSWERS) -> str:
    return f"## Shared records\n\n### Routes\n\n#### {identifier} — Recall\n\n{answers}"


@pytest.mark.parametrize("prefix", ["", "MEM-", "EPI-"])
def test_route_fields_apply_to_every_analyst(prefix: str) -> None:
    assert route_field_errors(route_body(prefix + "RTE-1")) == []
    errors = route_field_errors(route_body(prefix + "RTE-1", ""))
    assert len(errors) == 7
    assert all(prefix + "RTE-1" in error for error in errors)


@pytest.mark.parametrize(("replacement", "diagnostic"), [
    ("", "missing field"),
    ("- Later read-back:   \n", "empty field"),
    ("- Later read-back: one\n- Later read-back: two\n", "duplicate field"),
    ("- Later read-back: uninspected\n", "reason"),
    ("- Later read-back: inapplicable — \n", "reason"),
    ("- Later read-back: uninspected because no trace\n", "reason"),
])
def test_route_field_failures(replacement: str, diagnostic: str) -> None:
    answers = ROUTE_ANSWERS.replace(
        "- Later read-back: The next invocation reads the retained preference.\n", replacement
    )
    errors = route_field_errors(route_body(answers=answers))
    assert len(errors) == 1
    assert "Later read-back" in errors[0] and diagnostic in errors[0]


def test_other_records_and_annotations_cannot_supply_missing_fields() -> None:
    for heading in ("#### MEM-RTE-2 — Another route", "#### On RTE-1 — Overlay",
                    "### Claims", "## Discussion"):
        errors = route_field_errors(route_body(answers="") + f"\n{heading}\n\n{ROUTE_ANSWERS}")
        assert sum("RTE-1:" in error for error in errors) == 7


def test_source_excerpts_cannot_supply_fields_or_declare_routes() -> None:
    quoted = "\n".join("> " + line for line in ROUTE_ANSWERS.splitlines())
    for fenced in (f"```markdown\n{ROUTE_ANSWERS}```\n", quoted):
        assert len(route_field_errors(route_body(answers=fenced))) == 7
    excerpt = "\n```markdown\n#### RTE-99 — Source example\n```\n"
    assert route_field_errors(route_body() + excerpt) == []


def test_annotation_fields_are_not_required() -> None:
    assert route_field_errors("## Shared records\n\n#### On RTE-1 — Overlay\n") == []


def test_route_field_labels_match_the_delivered_contract() -> None:
    from pathlib import Path

    from commonplace.lib.agentic_records import ROUTE_FIELDS

    contract = (Path(__file__).resolve().parents[3] / "kb/agentic-systems/instructions/"
                "agentic-analysis-records.md").read_text()
    import re

    labels = re.findall(r"(?m)^- ([^:\n]+): \.\.\.$", contract)
    assert tuple(labels) == ROUTE_FIELDS

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


def test_member_can_reference_ids_other_members_declare() -> None:
    assert record_reference_errors("Uses OBJ-40 and MEM-OBJ-2.") == []


@pytest.mark.parametrize("prefix", ["", "MEM-", "EPI-"])
def test_rejects_duplicate_declarations_of_every_prefix(prefix: str) -> None:
    body = f"""## Shared records

#### {prefix}OBJ-1 — First object

#### {prefix}OBJ-1 — Different object
"""
    assert record_reference_errors(body) == [
        f"record references: duplicate declarations: {prefix}OBJ-1"
    ]


def test_lens_prefix_is_part_of_the_declared_id() -> None:
    body = """## Shared records

#### MEM-RTE-1 — S3 invocation

#### EPI-RTE-1 — Admission check

#### RTE-1 — Ordinary invocation

MEM-RTE-1 and EPI-RTE-1 read the bucket RTE-1 writes.
"""
    assert declared_ids(body) == ["MEM-RTE-1", "EPI-RTE-1", "RTE-1"]
    assert record_reference_errors(body) == []
    assert set_record_errors({"overview.md": body})[1] == []


RUNTIME = """# Runtime

## Shared records

### Routes

#### RTE-1 — Ordinary invocation

Record citing SRC-1.

## Annotations

#### On MEM-RTE-10 — Benchmark import

Theory-route overlay on the memory route MEM-RTE-10.
"""

MEMORY = """# Memory

## Shared records

### Routes

#### On RTE-1 — Ordinary invocation

Memory fields on the seeded route.

#### MEM-RTE-10 — Benchmark import

Record citing SRC-2 and MEM-OBJ-1.
"""

EPISTEMIC = """# Epistemic

## Authority-route ledger

EPI-RTE-1 checks what MEM-RTE-10 imports before RTE-1 uses it.

## Shared records

### Routes

#### EPI-RTE-1 — Import check

Record citing SRC-1.
"""


def test_annotation_headings_are_not_declarations() -> None:
    assert declared_ids(MEMORY) == ["MEM-RTE-10"]
    assert annotated_ids(MEMORY) == {"RTE-1"}
    assert annotated_ids(RUNTIME) == {"MEM-RTE-10"}
    assert declared_ids(RUNTIME) == ["RTE-1"]


OVERVIEW = "## Source register\n\n| SRC-1 | Runtime source |\n| SRC-2 | Memory source |\n"


def test_set_resolves_lens_prefixed_records_across_members() -> None:
    memory = MEMORY + "\n#### MEM-OBJ-1 — Stored object\n"
    known, errors = set_record_errors({
        "overview.md": OVERVIEW, "runtime.md": RUNTIME, "memory.md": memory,
        "epistemic.md": EPISTEMIC,
    })
    assert known == {"SRC-1", "SRC-2", "RTE-1", "MEM-RTE-10", "MEM-OBJ-1", "EPI-RTE-1"}
    assert errors == []


def test_set_rejects_a_lens_record_declared_by_two_members() -> None:
    memory = MEMORY + "\n#### MEM-OBJ-1 — Stored object\n"
    epistemic = EPISTEMIC + "\n#### MEM-OBJ-1 — The same object again\n"
    _, errors = set_record_errors({
        "overview.md": OVERVIEW, "runtime.md": RUNTIME, "memory.md": memory,
        "epistemic.md": epistemic,
    })
    assert errors == ["duplicate set declaration: MEM-OBJ-1"]


def test_an_amendment_in_the_reconciliation_resolves_against_the_set() -> None:
    memory = MEMORY + "\n#### MEM-OBJ-1 — Stored object\n"
    supersession = (
        "\n## Reconciliation\n\nAmendment: MEM-RTE-10 is superseded by RTE-1; both "
        "trace the same call at SRC-1.\n"
    )
    bodies = {"runtime.md": RUNTIME, "memory.md": memory, "epistemic.md": EPISTEMIC}
    assert set_record_errors({"overview.md": OVERVIEW, "reconciliation.md": supersession, **bodies})[1] == []

    undeclared = supersession.replace("RTE-1;", "RTE-7;")
    _, errors = set_record_errors({"overview.md": OVERVIEW, "reconciliation.md": undeclared, **bodies})
    assert errors == ["reconciliation.md: unresolved record RTE-7"]


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
