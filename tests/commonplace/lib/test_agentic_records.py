from __future__ import annotations

import pytest

from commonplace.lib.agentic_records import (
    amendment_index,
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


def route_body(identifier: str = "RT-RTE-1", answers: str = ROUTE_ANSWERS) -> str:
    return f"## Shared records\n\n### Routes\n\n#### {identifier} — Recall\n\n{answers}"


@pytest.mark.parametrize("prefix", ["RT-", "MEM-", "EPI-"])
def test_route_fields_apply_to_every_analyst(prefix: str) -> None:
    assert route_field_errors(route_body(prefix + "RTE-1")) == []
    errors = route_field_errors(route_body(prefix + "RTE-1", ""))
    assert len(errors) == 7
    assert all(prefix + "RTE-1" in error for error in errors)


@pytest.mark.parametrize(("replacement", "diagnostic"), [
    ("", "missing field"),
    ("- Later read-back:   \n", "empty field"),
    ("- Later read-back: one\n- Later read-back: two\n", "duplicate field"),
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
    for heading in ("#### MEM-RTE-2 — Another route", "#### On RT-RTE-1 — Overlay",
                    "### Claims", "## Discussion"):
        errors = route_field_errors(route_body(answers="") + f"\n{heading}\n\n{ROUTE_ANSWERS}")
        assert sum("RT-RTE-1:" in error for error in errors) == 7


def test_source_excerpts_cannot_supply_fields_or_declare_routes() -> None:
    quoted = "\n".join("> " + line for line in ROUTE_ANSWERS.splitlines())
    for fenced in (f"```markdown\n{ROUTE_ANSWERS}```\n", quoted):
        assert len(route_field_errors(route_body(answers=fenced))) == 7
    excerpt = "\n```markdown\n#### RT-RTE-99 — Source example\n```\n"
    assert route_field_errors(route_body() + excerpt) == []


def test_annotation_fields_are_not_required() -> None:
    assert route_field_errors("## Shared records\n\n#### On RT-RTE-1 — Overlay\n") == []


def test_route_field_labels_match_the_delivered_contract() -> None:
    from pathlib import Path

    from commonplace.lib.agentic_records import ROUTE_FIELDS

    contract = (Path(__file__).resolve().parents[3] / "kb/agentic-system-analyses/instructions/"
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

#### RT-OBJ-1 — First object

Evidence: SRC-1.

#### RT-OBJ-2 — Second object

#### RT-OBJ-15 — Third object

### Routes

#### RT-RTE-1 — S3 invocation

#### RT-RTE-20 — Another route

## Lens outputs

"""


def test_heading_title_is_not_inferred_to_be_shorthand() -> None:
    assert record_reference_errors(BASE) == []
    assert set_record_errors({"overview.md": BASE})[1] == []


def test_only_complete_references_are_recognized() -> None:
    reference = "RT-OBJ-1/O2"
    assert record_reference_errors(BASE + reference) == []
    assert set_record_errors({"overview.md": BASE + reference})[1] == []


def test_complete_unresolved_references_still_fail() -> None:
    reference = "RT-OBJ-1/RT-OBJ-99"
    _, errors = set_record_errors({"overview.md": BASE + reference})
    assert errors == ["overview.md: unresolved record RT-OBJ-99"]


def test_accepts_complete_lists_and_ignores_source_code() -> None:
    content = BASE + """RT-OBJ-1, RT-OBJ-2; `RT-RTE-1`/`RT-RTE-20`.

> Source example RT-OBJ-999/O2.

```python
print("RT-RTE-999–R9")
```

See RT-OBJ-15 and SRC-1.
"""
    assert record_reference_errors(content) == []
    assert set_record_errors({"overview.md": content})[1] == []


def test_prose_lists_and_tables_are_references_not_declarations() -> None:
    content = BASE.replace("### Routes", """RT-OBJ-1 is retained. Evidence: SRC-1.
- RT-OBJ-1 is consumed later.
| RT-OBJ-1 | Cross-reference |
SRC-1 supplies the evidence.
| SRC-1 | Source cross-reference |

### Routes""")
    assert declared_ids(content) == ["RT-OBJ-1", "RT-OBJ-2", "RT-OBJ-15", "RT-RTE-1", "RT-RTE-20"]
    assert record_reference_errors(content) == []
    assert set_record_errors({"overview.md": content})[1] == []


@pytest.mark.parametrize("heading", [
    "### RT-OBJ-99 — Wrong level", "##### RT-OBJ-99 — Wrong level",
    "#### RT-OBJ-99", "#### RT-OBJ-99 - Wrong separator", "#### SRC-99 — Source",
])
def test_only_prescribed_record_headings_declare(heading: str) -> None:
    assert declared_ids("## Shared records\n\n" + heading + "\n") == []


def test_record_headings_outside_shared_records_do_not_declare() -> None:
    assert declared_ids("## Discussion\n\n#### RT-OBJ-99 — Example\n") == []


def test_rejects_declarations_without_an_analyst_prefix() -> None:
    body = "## Shared records\n\n#### OBJ-1 — Bare heading\n\n#### RT-OBJ-2 — Prefixed\n"
    assert record_reference_errors(body) == [
        "record references: declarations without an analyst prefix: OBJ-1; use RT-, MEM- or EPI-"
    ]
    assert record_reference_errors("## Discussion\n\n#### OBJ-1 — Not a declaration\n") == []


def test_member_can_reference_ids_other_members_declare() -> None:
    assert record_reference_errors("Uses RT-OBJ-40 and MEM-OBJ-2.") == []


@pytest.mark.parametrize("prefix", ["RT-", "MEM-", "EPI-"])
def test_rejects_duplicate_declarations_of_every_prefix(prefix: str) -> None:
    body = f"""## Shared records

#### {prefix}OBJ-1 — First object

#### {prefix}OBJ-1 — Different object
"""
    assert record_reference_errors(body) == [
        f"record references: duplicate declarations: {prefix}OBJ-1"
    ]


def test_analyst_prefix_is_part_of_the_declared_id() -> None:
    body = """## Shared records

#### MEM-RTE-1 — S3 invocation

#### EPI-RTE-1 — Admission check

#### RT-RTE-1 — Ordinary invocation

MEM-RTE-1 and EPI-RTE-1 read the bucket RT-RTE-1 writes.
"""
    assert declared_ids(body) == ["MEM-RTE-1", "EPI-RTE-1", "RT-RTE-1"]
    assert record_reference_errors(body) == []
    assert set_record_errors({"overview.md": body})[1] == []


@pytest.mark.parametrize("kind", ["OBJ", "ABS"])
def test_bare_kind_tokens_are_neither_declarations_nor_references(kind: str) -> None:
    identifier = f"RT-{kind}-1"
    bodies = {
        "overview.md": "## Source register\n\n| SRC-1 | Source |\n",
        "runtime.md": f"## Shared records\n\n#### {identifier} — Record\nEvidence: SRC-1.\n",
        "memory.md": f"## Shared records\n\n#### On {identifier} — Finding\n",
        "epistemic.md": f"Assessment of {identifier} at SRC-1.",
        "reconciliation.md": f"## Reconciliation\n\nAmendment: {identifier} — correction at SRC-1.\n",
    }
    known, errors = set_record_errors(bodies)
    assert known == {identifier, "SRC-1"} and errors == []
    assert annotated_ids(bodies["memory.md"]) == {identifier}
    assert identifier in amendment_index(bodies["reconciliation.md"])
    bodies["epistemic.md"] = f"Assessment of {kind}-1."
    bodies["runtime.md"] += f"\n#### {kind}-2 — Unprefixed heading\n"
    assert set_record_errors(bodies) == ({identifier, "SRC-1"}, [])


RUNTIME = """# Runtime

## Shared records

### Routes

#### RT-RTE-1 — Ordinary invocation

Record citing SRC-1.

## Annotations

#### On MEM-RTE-10 — Benchmark import

Theory-route overlay on the memory route MEM-RTE-10.
"""

MEMORY = """# Memory

## Shared records

### Routes

#### On RT-RTE-1 — Ordinary invocation

Memory fields on the seeded route.

#### MEM-RTE-10 — Benchmark import

Record citing SRC-2 and MEM-OBJ-1.
"""

EPISTEMIC = """# Epistemic

## Authority-route ledger

EPI-RTE-1 checks what MEM-RTE-10 imports before RT-RTE-1 uses it.

## Shared records

### Routes

#### EPI-RTE-1 — Import check

Record citing SRC-1.
"""


def test_annotation_headings_are_not_declarations() -> None:
    assert declared_ids(MEMORY) == ["MEM-RTE-10"]
    assert annotated_ids(MEMORY) == {"RT-RTE-1"}
    assert annotated_ids(RUNTIME) == {"MEM-RTE-10"}
    assert declared_ids(RUNTIME) == ["RT-RTE-1"]


OVERVIEW = "## Source register\n\n| SRC-1 | Runtime source |\n| SRC-2 | Memory source |\n"


def test_set_resolves_lens_prefixed_records_across_members() -> None:
    memory = MEMORY + "\n#### MEM-OBJ-1 — Stored object\n"
    known, errors = set_record_errors({
        "overview.md": OVERVIEW, "runtime.md": RUNTIME, "memory.md": memory,
        "epistemic.md": EPISTEMIC,
    })
    assert known == {"SRC-1", "SRC-2", "RT-RTE-1", "MEM-RTE-10", "MEM-OBJ-1", "EPI-RTE-1"}
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
        "\n## Reconciliation\n\nAmendment: MEM-RTE-10 is superseded by RT-RTE-1; both "
        "trace the same call at SRC-1.\n"
    )
    bodies = {"runtime.md": RUNTIME, "memory.md": memory, "epistemic.md": EPISTEMIC}
    assert set_record_errors({"overview.md": OVERVIEW, "reconciliation.md": supersession, **bodies})[1] == []

    undeclared = supersession.replace("RT-RTE-1;", "RT-RTE-7;")
    _, errors = set_record_errors({"overview.md": OVERVIEW, "reconciliation.md": undeclared, **bodies})
    assert errors == ["reconciliation.md: unresolved record RT-RTE-7"]


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


@pytest.mark.parametrize("reference", [
    "RT-OBJ-1 through RT-OBJ-15", "RT-OBJ-1–RT-OBJ-15", "RT-OBJ-1–15",
    "`RT-RTE-1`–`RT-RTE-8`", "SRC-1 through SRC-2",
])
def test_ranges_are_refused_independently_of_endpoint_resolution(reference: str) -> None:
    body = BASE + reference
    assert any("ranges are not expanded" in error for error in record_reference_errors(body))
    assert any("ranges are not expanded" in error
               for error in set_record_errors({"overview.md": body})[1])


@pytest.mark.parametrize("reference", [
    "The inventory compares `EPI-OBJ-8` to `RT-OBJ-1`.",
    "Move EPI-OBJ-8 to RT-OBJ-1.",
    "RT-OBJ-1, RT-OBJ-2 and RT-OBJ-15.",
])
def test_relation_prose_does_not_enumerate_a_record_range(reference: str) -> None:
    body = BASE + reference
    epistemic = "## Shared records\n\n#### EPI-OBJ-8 — Candidate\n"
    assert record_reference_errors(body) == []
    assert set_record_errors({"overview.md": body, "epistemic.md": epistemic})[1] == []


def test_unresolved_record_suggests_all_prefix_matches_without_changing_identity() -> None:
    bodies = {
        "overview.md": OVERVIEW,
        "runtime.md": "## Shared records\n\n#### RT-OBJ-3 — Runtime object\n",
        "epistemic.md": "## Shared records\n\n#### EPI-OBJ-3 — Epistemic object\n",
        "memory.md": "MEM-OBJ-3 and MEM-OBJ-4 and MEM-RTE-3.",
    }
    assert set_record_errors(bodies)[1] == [
        "memory.md: unresolved record MEM-OBJ-3; declared with another analyst prefix: EPI-OBJ-3, RT-OBJ-3",
        "memory.md: unresolved record MEM-OBJ-4",
        "memory.md: unresolved record MEM-RTE-3",
    ]


@pytest.mark.parametrize(("field", "diagnostic"), [
    ("Part of: RT-OBJ-1", None),
    ("Part of: RT-OBJ-99", "unresolved record RT-OBJ-99"),
    ("Part of: MEM-OBJ-1", "cannot name itself"),
    ("Part of:", "exactly one full record ID"),
    ("- Part of: RT-OBJ-1", "unindented"),
    ("Part of: RT-OBJ-1\nPart of: RT-OBJ-2", "duplicate Part of:"),
])
def test_part_field_syntax_and_existing_target_resolution(field: str, diagnostic: str | None) -> None:
    memory = f"## Shared records\n\n### Operative objects\n\n#### MEM-OBJ-1 — Part\n\n{field}\n"
    errors = set_record_errors({"overview.md": BASE, "memory.md": memory})[1]
    if diagnostic is None:
        assert errors == []
    else:
        assert any(diagnostic in error for error in errors)
    if field == "Part of: RT-OBJ-99":
        assert record_reference_errors(memory) == []


@pytest.mark.parametrize("heading", ["## Discussion", "#### On RT-OBJ-1 — Annotation"])
def test_part_field_requires_a_declaration_owner(heading: str) -> None:
    body = BASE + heading + "\n\nPart of: RT-OBJ-2\n"
    assert "Part of: must belong" in record_reference_errors(body)[0]


def test_range_and_part_examples_in_source_excerpts_are_ignored() -> None:
    body = BASE + "\n> RT-OBJ-1 through RT-OBJ-99\n> Part of: RT-OBJ-99\n"
    body += "\n```markdown\nRT-OBJ-1–RT-OBJ-99\nPart of: RT-OBJ-99\n```\n"
    assert record_reference_errors(body) == []
    assert set_record_errors({"overview.md": body})[1] == []
