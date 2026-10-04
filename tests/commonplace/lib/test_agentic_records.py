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


def route_body(identifier: str = "RT-RTE-model-call", answers: str = ROUTE_ANSWERS) -> str:
    return f"## Shared records\n\n### Routes\n\n#### {identifier} — Recall\n\n{answers}"


@pytest.mark.parametrize("prefix", ["RT-", "MEM-", "EPI-"])
def test_route_fields_apply_to_every_analyst(prefix: str) -> None:
    assert route_field_errors(route_body(prefix + "RTE-model-call")) == []
    errors = route_field_errors(route_body(prefix + "RTE-model-call", ""))
    assert len(errors) == 7
    assert all(prefix + "RTE-model-call" in error for error in errors)


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
    for heading in ("#### MEM-RTE-memory-update — Another route", "#### On RT-RTE-model-call — Overlay",
                    "### Claims", "## Discussion"):
        errors = route_field_errors(route_body(answers="") + f"\n{heading}\n\n{ROUTE_ANSWERS}")
        assert sum("RT-RTE-model-call:" in error for error in errors) == 7


def test_source_excerpts_cannot_supply_fields_or_declare_routes() -> None:
    quoted = "\n".join("> " + line for line in ROUTE_ANSWERS.splitlines())
    for fenced in (f"```markdown\n{ROUTE_ANSWERS}```\n", quoted):
        assert len(route_field_errors(route_body(answers=fenced))) == 7
    excerpt = "\n```markdown\n#### RT-RTE-missing — Source example\n```\n"
    assert route_field_errors(route_body() + excerpt) == []


def test_annotation_fields_are_not_required() -> None:
    assert route_field_errors("## Shared records\n\n#### On RT-RTE-model-call — Overlay\n") == []


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

#### RT-OBJ-store — First object

Evidence: SRC-1.

#### RT-OBJ-input — Second object

#### RT-OBJ-third — Third object

### Routes

#### RT-RTE-model-call — S3 invocation

#### RT-RTE-another-route — Another route

## Lens outputs

"""


def test_heading_title_is_not_inferred_to_be_shorthand() -> None:
    assert record_reference_errors(BASE) == []
    assert set_record_errors({"overview.md": BASE})[1] == []


def test_only_complete_references_are_recognized() -> None:
    reference = "RT-OBJ-store/O2"
    assert record_reference_errors(BASE + reference) == []
    assert set_record_errors({"overview.md": BASE + reference})[1] == []


def test_complete_unresolved_references_still_fail() -> None:
    reference = "RT-OBJ-store/RT-OBJ-missing"
    _, errors = set_record_errors({"overview.md": BASE + reference})
    assert errors == ["overview.md: unresolved record RT-OBJ-missing"]


def test_accepts_complete_lists_and_ignores_source_code() -> None:
    content = BASE + """RT-OBJ-store, RT-OBJ-input; `RT-RTE-model-call`/`RT-RTE-another-route`.

> Source example RT-OBJ-example999/O2.

```python
print("RT-RTE-example999–R9")
```

See RT-OBJ-third and SRC-1.
"""
    assert record_reference_errors(content) == []
    assert set_record_errors({"overview.md": content})[1] == []


def test_prose_lists_and_tables_are_references_not_declarations() -> None:
    content = BASE.replace("### Routes", """RT-OBJ-store is retained. Evidence: SRC-1.
- RT-OBJ-store is consumed later.
| RT-OBJ-store | Cross-reference |
SRC-1 supplies the evidence.
| SRC-1 | Source cross-reference |

### Routes""")
    assert declared_ids(content) == ["RT-OBJ-store", "RT-OBJ-input", "RT-OBJ-third", "RT-RTE-model-call", "RT-RTE-another-route"]
    assert record_reference_errors(content) == []
    assert set_record_errors({"overview.md": content})[1] == []


@pytest.mark.parametrize("heading", [
    "### RT-OBJ-missing — Wrong level", "##### RT-OBJ-missing — Wrong level",
    "#### RT-OBJ-missing", "#### RT-OBJ-missing - Wrong separator", "#### SRC-99 — Source",
])
def test_only_prescribed_record_headings_declare(heading: str) -> None:
    assert declared_ids("## Shared records\n\n" + heading + "\n") == []


def test_record_headings_outside_shared_records_do_not_declare() -> None:
    assert declared_ids("## Discussion\n\n#### RT-OBJ-missing — Example\n") == []


def test_rejects_declarations_without_an_analyst_prefix() -> None:
    body = "## Shared records\n\n#### OBJ-store — Bare heading\n\n#### RT-OBJ-input — Prefixed\n"
    assert record_reference_errors(body) == [
        "record references: declarations without an analyst prefix: OBJ-store; use RT-, MEM- or EPI-"
    ]
    assert record_reference_errors("## Discussion\n\n#### OBJ-store — Not a declaration\n") == []


def test_member_can_reference_ids_other_members_declare() -> None:
    assert record_reference_errors("Uses RT-OBJ-example40 and MEM-OBJ-input.") == []


@pytest.mark.parametrize("prefix", ["RT-", "MEM-", "EPI-"])
def test_rejects_duplicate_declarations_of_every_prefix(prefix: str) -> None:
    body = f"""## Shared records

#### {prefix}OBJ-store — First object

#### {prefix}OBJ-store — Different object
"""
    assert record_reference_errors(body) == [
        f"record references: duplicate declarations: {prefix}OBJ-store"
    ]


def test_analyst_prefix_is_part_of_the_declared_id() -> None:
    body = """## Shared records

#### MEM-RTE-model-call — S3 invocation

#### EPI-RTE-model-call — Admission check

#### RT-RTE-model-call — Ordinary invocation

MEM-RTE-model-call and EPI-RTE-model-call read the bucket RT-RTE-model-call writes.
"""
    assert declared_ids(body) == ["MEM-RTE-model-call", "EPI-RTE-model-call", "RT-RTE-model-call"]
    assert record_reference_errors(body) == []
    assert set_record_errors({"overview.md": body})[1] == []


@pytest.mark.parametrize("kind", ["OBJ", "ABS"])
def test_bare_kind_tokens_are_neither_declarations_nor_references(kind: str) -> None:
    identifier = f"RT-{kind}-record"
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

#### RT-RTE-model-call — Ordinary invocation

Record citing SRC-1.

## Annotations

#### On MEM-RTE-example10 — Benchmark import

Theory-route overlay on the memory route MEM-RTE-example10.
"""

MEMORY = """# Memory

## Shared records

### Routes

#### On RT-RTE-model-call — Ordinary invocation

Memory fields on the seeded route.

#### MEM-RTE-example10 — Benchmark import

Record citing SRC-2 and MEM-OBJ-store.
"""

EPISTEMIC = """# Epistemic

## Authority-route ledger

EPI-RTE-model-call checks what MEM-RTE-example10 imports before RT-RTE-model-call uses it.

## Shared records

### Routes

#### EPI-RTE-model-call — Import check

Record citing SRC-1.
"""


def test_annotation_headings_are_not_declarations() -> None:
    assert declared_ids(MEMORY) == ["MEM-RTE-example10"]
    assert annotated_ids(MEMORY) == {"RT-RTE-model-call"}
    assert annotated_ids(RUNTIME) == {"MEM-RTE-example10"}
    assert declared_ids(RUNTIME) == ["RT-RTE-model-call"]


OVERVIEW = "## Source register\n\n| SRC-1 | Runtime source |\n| SRC-2 | Memory source |\n"


def test_set_resolves_lens_prefixed_records_across_members() -> None:
    memory = MEMORY + "\n#### MEM-OBJ-store — Stored object\n"
    known, errors = set_record_errors({
        "overview.md": OVERVIEW, "runtime.md": RUNTIME, "memory.md": memory,
        "epistemic.md": EPISTEMIC,
    })
    assert known == {"SRC-1", "SRC-2", "RT-RTE-model-call", "MEM-RTE-example10", "MEM-OBJ-store", "EPI-RTE-model-call"}
    assert errors == []


def test_set_rejects_a_lens_record_declared_by_two_members() -> None:
    memory = MEMORY + "\n#### MEM-OBJ-store — Stored object\n"
    epistemic = EPISTEMIC + "\n#### MEM-OBJ-store — The same object again\n"
    _, errors = set_record_errors({
        "overview.md": OVERVIEW, "runtime.md": RUNTIME, "memory.md": memory,
        "epistemic.md": epistemic,
    })
    assert errors == ["duplicate set declaration: MEM-OBJ-store"]


def test_an_amendment_in_the_reconciliation_resolves_against_the_set() -> None:
    memory = MEMORY + "\n#### MEM-OBJ-store — Stored object\n"
    supersession = (
        "\n## Reconciliation\n\nAmendment: MEM-RTE-example10 is superseded by RT-RTE-model-call; both "
        "trace the same call at SRC-1.\n"
    )
    bodies = {"runtime.md": RUNTIME, "memory.md": memory, "epistemic.md": EPISTEMIC}
    assert set_record_errors({"overview.md": OVERVIEW, "reconciliation.md": supersession, **bodies})[1] == []

    undeclared = supersession.replace("RT-RTE-model-call;", "RT-RTE-policy-check;")
    _, errors = set_record_errors({"overview.md": OVERVIEW, "reconciliation.md": undeclared, **bodies})
    assert errors == ["reconciliation.md: unresolved record RT-RTE-policy-check"]


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
    "SRC-1 through SRC-2", "SRC-1–SRC-2", "SRC-1–2", "`SRC-1`–`SRC-2`", "SRC-1-2",
])
def test_source_ranges_are_refused_independently_of_endpoint_resolution(reference: str) -> None:
    body = BASE + reference
    assert any("ranges are not expanded" in error for error in record_reference_errors(body))
    assert any("ranges are not expanded" in error
               for error in set_record_errors({"overview.md": body})[1])


@pytest.mark.parametrize("reference", [
    "The inventory compares `EPI-OBJ-candidate` to `RT-OBJ-store`.",
    "Move EPI-OBJ-candidate to RT-OBJ-store.",
    "RT-OBJ-store, RT-OBJ-input and RT-OBJ-third.",
])
def test_relation_prose_does_not_enumerate_a_record_range(reference: str) -> None:
    body = BASE + reference
    epistemic = "## Shared records\n\n#### EPI-OBJ-candidate — Candidate\n"
    assert record_reference_errors(body) == []
    assert set_record_errors({"overview.md": body, "epistemic.md": epistemic})[1] == []


def test_unresolved_record_suggests_all_prefix_matches_without_changing_identity() -> None:
    bodies = {
        "overview.md": OVERVIEW,
        "runtime.md": "## Shared records\n\n#### RT-OBJ-output — Runtime object\n",
        "epistemic.md": "## Shared records\n\n#### EPI-OBJ-output — Epistemic object\n",
        "memory.md": "MEM-OBJ-output and MEM-OBJ-payload and MEM-RTE-selection-route.",
    }
    assert set_record_errors(bodies)[1] == [
        "memory.md: unresolved record MEM-OBJ-output; declared with another analyst prefix: EPI-OBJ-output, RT-OBJ-output",
        "memory.md: unresolved record MEM-OBJ-payload",
        "memory.md: unresolved record MEM-RTE-selection-route",
    ]


@pytest.mark.parametrize(("field", "diagnostic"), [
    ("Part of: RT-OBJ-store", None),
    ("Part of: RT-OBJ-missing", "unresolved record RT-OBJ-missing"),
    ("Part of: MEM-OBJ-store", "cannot name itself"),
    ("Part of:", "exactly one full record ID"),
    ("- Part of: RT-OBJ-store", "unindented"),
    ("Part of: RT-OBJ-store\nPart of: RT-OBJ-input", "duplicate Part of:"),
])
def test_part_field_syntax_and_existing_target_resolution(field: str, diagnostic: str | None) -> None:
    memory = f"## Shared records\n\n### Operative objects\n\n#### MEM-OBJ-store — Part\n\n{field}\n"
    errors = set_record_errors({"overview.md": BASE, "memory.md": memory})[1]
    if diagnostic is None:
        assert errors == []
    else:
        assert any(diagnostic in error for error in errors)
    if field == "Part of: RT-OBJ-missing":
        assert record_reference_errors(memory) == []


@pytest.mark.parametrize("heading", ["## Discussion", "#### On RT-OBJ-store — Annotation"])
def test_part_field_requires_a_declaration_owner(heading: str) -> None:
    body = BASE + heading + "\n\nPart of: RT-OBJ-input\n"
    assert "Part of: must belong" in record_reference_errors(body)[0]


def test_range_and_part_examples_in_source_excerpts_are_ignored() -> None:
    body = BASE + "\n> RT-OBJ-store through RT-OBJ-missing\n> Part of: RT-OBJ-missing\n"
    body += "\n```markdown\nRT-OBJ-1–RT-OBJ-missing\nPart of: RT-OBJ-missing\n```\n"
    assert record_reference_errors(body) == []
    assert set_record_errors({"overview.md": body})[1] == []


@pytest.mark.parametrize('name', ['sheet', 'original-input-corpus', 'gpt4', 'top-k-examples'])
def test_named_ids_resolve_in_declarations_annotations_and_parts(name: str) -> None:
    identifier = f'RT-OBJ-{name}'
    runtime = f'## Shared records\n\n#### {identifier} — Object\n'
    memory = f'## Shared records\n\n#### On {identifier} — Annotation\n\n'
    memory += f'#### MEM-OBJ-part — Part\n\nPart of: {identifier}\n'
    assert declared_ids(runtime) == [identifier]
    assert annotated_ids(memory) == {identifier}
    assert set_record_errors({'overview.md': OVERVIEW, 'runtime.md': runtime, 'memory.md': memory})[1] == []


@pytest.mark.parametrize('name', ['1', 'sheet-2', 'Sheet', 'one-two-three-four',
                                  'sheet_', 'sheet-', 'sheet--cache', 'café'])
@pytest.mark.parametrize('context', ['#### {id} — Object', '{id} supports this finding.',
                                      '#### On {id} — Annotation', 'Amendment: {id} corrected.'])
def test_malformed_candidate_tokens_are_refused_whole(name: str, context: str) -> None:
    identifier = f'RT-OBJ-{name}'
    body = '## Shared records\n\n' + context.format(id=identifier) + '\n'
    errors = record_reference_errors(body)
    assert any(f'invalid ID {identifier}' in error for error in errors)
    assert any(f'invalid ID {identifier}' in error
               for error in set_record_errors({'overview.md': OVERVIEW, 'runtime.md': body})[1])


@pytest.mark.parametrize('separator', [' through ', ' to ', '–', '—', '-', '`–`'])
def test_named_group_resolves_written_endpoints_without_expansion(separator: str) -> None:
    declarations = '## Shared records\n\n#### MEM-OBJ-sheet — Sheet\n\n'
    declarations += '#### MEM-OBJ-vectors — Vectors\n\n'
    reference = f'MEM-OBJ-sheet{separator}MEM-OBJ-vectors'
    assert set_record_errors({'overview.md': OVERVIEW, 'memory.md': declarations + reference})[1] == []
    errors = set_record_errors({'overview.md': OVERVIEW, 'memory.md': declarations.replace(
        '#### MEM-OBJ-vectors — Vectors', '#### MEM-OBJ-input — Input') + reference})[1]
    assert any('unresolved record MEM-OBJ-vectors' in error for error in errors)


def test_attached_word_is_not_silently_resolved_to_declared_prefix() -> None:
    body = '## Shared records\n\n#### MEM-OBJ-sheet — Sheet\n\nMEM-OBJ-sheet-based'
    assert set_record_errors({'overview.md': OVERVIEW, 'memory.md': body})[1] == [
        'memory.md: unresolved record MEM-OBJ-sheet-based; nearest declared ID: MEM-OBJ-sheet']


def test_prefix_collision_is_refused_at_member_and_set_acceptance() -> None:
    body = '## Shared records\n\n#### MEM-OBJ-sheet — Sheet\n\n'
    body += '#### MEM-OBJ-sheet-cache — Cache\n'
    assert any('extends declared ID' in error for error in record_reference_errors(body))
    assert any('extends declared ID' in error for error in set_record_errors({'overview.md': OVERVIEW, 'memory.md': body})[1])
    distinct = body.replace('MEM-OBJ-sheet-cache', 'EPI-OBJ-sheet-cache')
    assert record_reference_errors(distinct) == []
    distinct = body.replace('MEM-OBJ-sheet-cache', 'MEM-CMP-sheet-cache')
    assert record_reference_errors(distinct) == []


def test_misspelling_refuses_reference_and_suggests_declared_name() -> None:
    body = '## Shared records\n\n#### MEM-OBJ-embeddings — Embeddings\n\nMEM-OBJ-embedings'
    assert set_record_errors({'overview.md': OVERVIEW, 'memory.md': body})[1] == [
        'memory.md: unresolved record MEM-OBJ-embedings; nearest declared ID: MEM-OBJ-embeddings']


def test_named_group_cannot_replace_single_part_identifier() -> None:
    body = '## Shared records\n\n#### MEM-OBJ-part — Part\n\nPart of: RT-OBJ-store through RT-OBJ-input\n'
    assert any('exactly one full record ID' in error for error in record_reference_errors(body))


def test_invalid_names_and_source_ranges_inside_source_excerpts_are_ignored() -> None:
    body = BASE + '\n> RT-OBJ-1 SRC-1 through SRC-9 RT-OBJ-UPPER\n'
    body += '\n```markdown\nRT-OBJ-one-two-three-four SRC-1–9\n```\n'
    assert record_reference_errors(body) == []
    assert set_record_errors({'overview.md': body})[1] == []
