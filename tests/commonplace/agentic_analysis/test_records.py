"""Record declarations, linked citations and route fields.

A record is declared by a heading that is exactly its ID; a citation is a
Markdown link to that heading's anchor, `[RT-OBJ-store](runtime.md#rt-obj-store)`.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis.records import (
    ROUTE_FIELDS,
    amendment_index,
    anchor,
    annotated_ids,
    artifact_record_findings,
    declared_ids,
    identifier_from_anchor,
    record_declaration,
    record_links,
    record_reference_errors,
    record_references,
    route_field_errors,
    source_register_rows,
    value_amendments,
)
from tests.commonplace.agentic_analysis.fixtures import artifact_record_errors

ROUTE_ANSWERS = """- Immediate return: A stored preference is returned.
- Later read-back: The next invocation reads the retained preference.
- Delegated visibility: inapplicable — this route does not delegate.
- Selection predicate: The caller's key selects the preference.
- Invalidation or expiry: inapplicable — no expiry is implemented.
- Activation or effect: uninspected — model behavior was not observed.
- Evidence limits: Static inspection; no execution trace.
"""


def route_body(identifier: str = "RT-RTE-model-call", answers: str = ROUTE_ANSWERS) -> str:
    return f"## Shared records\n\n### Routes\n\n#### {identifier}\n\nLabel: Recall\n\n{answers}"


# Route fields


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
    for heading in ("#### MEM-RTE-memory-update", "#### On [RT-RTE-model-call](#rt-rte-model-call)",
                    "### Claims", "## Discussion"):
        errors = route_field_errors(route_body(answers="") + f"\n{heading}\n\n{ROUTE_ANSWERS}")
        assert sum("RT-RTE-model-call:" in error for error in errors) == 7


def test_source_excerpts_cannot_supply_fields_or_declare_routes() -> None:
    quoted = "\n".join("> " + line for line in ROUTE_ANSWERS.splitlines())
    for fenced in (f"```markdown\n{ROUTE_ANSWERS}```\n", quoted):
        assert len(route_field_errors(route_body(answers=fenced))) == 7
    excerpt = "\n```markdown\n#### RT-RTE-missing\n```\n"
    assert route_field_errors(route_body() + excerpt) == []


def test_annotation_fields_are_not_required() -> None:
    assert route_field_errors("## Shared records\n\n#### On [RT-RTE-model-call](runtime.md#rt-rte-model-call)\n") == []


def test_route_field_labels_match_the_delivered_contract() -> None:
    contract = (Path(__file__).resolve().parents[3] / "kb/agentic-system-analyses/instructions/"
                "agentic-analysis-records.md").read_text()
    labels = re.findall(r"(?m)^- ([^:\n]+): \.\.\.$", contract)
    assert tuple(labels) == ROUTE_FIELDS


# Declarations


def declaration(identifier: str, label: str = "Fixture", text: str = "") -> str:
    return f"#### {identifier}\n\nLabel: {label}\n\n{text}\n"


RUNTIME = "# Runtime\n\n## Shared records\n\n### Routes\n\n" + declaration(
    "RT-RTE-model-call", "Ordinary invocation", "Reads [RT-OBJ-store](#rt-obj-store) at SRC-1.",
) + "\n### Operative objects\n\n" + declaration("RT-OBJ-store", "Persistent store")
MEMORY = "# Memory\n\n## Shared records\n\n" + declaration(
    "MEM-RTE-import", "Benchmark import",
    "Feeds [RT-OBJ-store](runtime.md#rt-obj-store), from SRC-2.",
) + "\n## Annotations\n\n#### On [RT-RTE-model-call](runtime.md#rt-rte-model-call)\n\nMemory fields.\n"
BOUNDARY = "## Source register\n\n| SRC-1 | Runtime source |\n| SRC-2 | Memory source |\n"
CITES = {"runtime.md": ["boundary.md", "runtime.md", "memory.md"],
         "memory.md": ["boundary.md", "runtime.md", "memory.md"],
         "profile.md": ["memory.md"]}


def bodies(**changes: str) -> dict[str, str]:
    return {"boundary.md": BOUNDARY, "runtime.md": RUNTIME, "memory.md": MEMORY, **changes}


def errors(**changes: str) -> list[str]:
    return artifact_record_errors("boundary.md", bodies(**changes), cites=CITES)[1]


def test_a_declaration_is_a_heading_that_is_exactly_the_id() -> None:
    assert declared_ids(RUNTIME) == ["RT-RTE-model-call", "RT-OBJ-store"]
    assert record_reference_errors(RUNTIME) == []
    assert record_declaration(RUNTIME, "RT-OBJ-store").startswith("#### RT-OBJ-store\n\nLabel: Persistent store")


def test_a_labelled_heading_is_refused_with_its_repair() -> None:
    body = "## Shared records\n\n#### RT-OBJ-store — Persistent store\n\nLabel: Store\n"
    assert declared_ids(body) == []
    assert any("the heading is exactly the record ID" in error for error in record_reference_errors(body))


def test_every_declaration_opens_with_its_label() -> None:
    body = "## Shared records\n\n#### RT-OBJ-store\n\nA store without its label line.\n"
    assert record_reference_errors(body) == ["record declarations: RT-OBJ-store: missing 'Label: <label>' first line"]
    assert any("missing 'Label" in error for error in record_reference_errors("## Shared records\n\n#### RT-OBJ-store\n"))


@pytest.mark.parametrize("heading", [
    "### RT-OBJ-missing", "##### RT-OBJ-missing", "#### SRC-99", "#### OBJ-missing",
])
def test_only_the_prescribed_heading_declares(heading: str) -> None:
    assert declared_ids("## Shared records\n\n" + heading + "\n") == []


def test_record_headings_outside_shared_records_do_not_declare() -> None:
    assert declared_ids("## Discussion\n\n#### RT-OBJ-missing\n") == []


@pytest.mark.parametrize("prefix", ["RT-", "MEM-", "EPI-"])
def test_duplicate_declarations_are_refused(prefix: str) -> None:
    body = "## Shared records\n\n" + declaration(f"{prefix}OBJ-store") + declaration(f"{prefix}OBJ-store")
    assert record_reference_errors(body) == [f"record references: duplicate declarations: {prefix}OBJ-store"]


def test_a_record_declared_by_two_members_is_refused_in_both() -> None:
    memory = MEMORY.replace("## Annotations", declaration("RT-OBJ-store") + "\n## Annotations")
    found = errors(**{"memory.md": memory})
    assert "runtime.md: duplicate artifact declaration: RT-OBJ-store" in found
    assert "memory.md: duplicate artifact declaration: RT-OBJ-store" in found


def test_ids_that_extend_one_another_can_coexist() -> None:
    body = "## Shared records\n\n" + declaration("MEM-OBJ-sheet") + declaration("MEM-OBJ-sheet-cache")
    assert record_reference_errors(body) == []


# Citations


def test_anchor_and_id_are_one_mapping() -> None:
    assert anchor("RT-OBJ-store") == "rt-obj-store"
    assert identifier_from_anchor("rt-obj-store") == "RT-OBJ-store"
    assert identifier_from_anchor("mem-rte-update2-path") == "MEM-RTE-update2-path"
    assert identifier_from_anchor("persistent-store") is None


def test_valid_cross_member_and_within_member_citations_resolve() -> None:
    assert errors() == []
    assert record_references(MEMORY) == {"RT-OBJ-store", "RT-RTE-model-call"}


def test_a_missing_destination_member_fails() -> None:
    _known, found = artifact_record_errors("boundary.md", {
        "boundary.md": BOUNDARY, "memory.md": MEMORY,
    }, cites=CITES)
    assert any("member runtime.md is not present" in error for error in found)


def test_a_missing_record_fails_even_when_the_member_exists() -> None:
    memory = MEMORY.replace("[RT-OBJ-store](runtime.md#rt-obj-store)", "[RT-OBJ-cache](runtime.md#rt-obj-cache)")
    assert errors(**{"memory.md": memory}) == [
        "memory.md: unresolved record citation [RT-OBJ-cache](runtime.md#rt-obj-cache): runtime.md declares no RT-OBJ-cache"]


def test_a_non_record_fragment_fails_in_its_member() -> None:
    memory = MEMORY.replace("[RT-OBJ-store](runtime.md#rt-obj-store)", "[RT-OBJ-store](runtime.md#routes)")
    assert record_reference_errors(memory) == [
        ("record citations: [RT-OBJ-store] links to #routes, which is not a record anchor; "
        "link to #rt-obj-store")]
    assert errors(**{"memory.md": memory}) == []  # Syntax is the member's finding, reported once.


def test_a_record_declared_in_another_member_than_the_link_names_fails_with_a_hint() -> None:
    memory = MEMORY.replace("(runtime.md#rt-obj-store)", "(memory.md#rt-obj-store)")
    assert errors(**{"memory.md": memory}) == [
        ("memory.md: unresolved record citation [RT-OBJ-store](memory.md#rt-obj-store): memory.md declares "
        "no RT-OBJ-store; it is declared in runtime.md")]


def test_a_destination_outside_the_citing_roles_cites_fails() -> None:
    profile = "Uses [RT-OBJ-store](runtime.md#rt-obj-store).\n"
    assert errors(**{"profile.md": profile}) == [
        ("profile.md: record citation [RT-OBJ-store](runtime.md#rt-obj-store): runtime.md is not among the "
        "documents this one may cite: memory.md")]


def test_a_within_member_citation_needs_the_member_in_its_own_cites() -> None:
    cites = {**CITES, "runtime.md": ["boundary.md", "memory.md"]}
    _, found = artifact_record_errors("boundary.md", bodies(), cites=cites)
    assert found == [
        ("runtime.md: record citation [RT-OBJ-store](#rt-obj-store): runtime.md is not among the documents "
        "this one may cite: boundary.md, memory.md")]


def test_a_label_naming_another_record_fails_in_its_member() -> None:
    memory = MEMORY.replace("[RT-OBJ-store](runtime.md#rt-obj-store)", "[RT-OBJ-cache](runtime.md#rt-obj-store)")
    assert record_reference_errors(memory) == [
        "record citations: [RT-OBJ-cache] links to the record RT-OBJ-store; use that record's ID as the label"]
    assert errors(**{"memory.md": memory}) == []


def test_a_record_declared_twice_is_the_declaring_member_s_finding() -> None:
    runtime = RUNTIME + declaration("RT-OBJ-store")
    assert record_reference_errors(runtime) == ["record references: duplicate declarations: RT-OBJ-store"]
    assert errors(**{"runtime.md": runtime}) == []  # Not repeated for the declarer or its citers.


def test_changing_a_declarations_label_leaves_citations_valid() -> None:
    assert errors(**{"runtime.md": RUNTIME.replace("Label: Persistent store", "Label: Shared storage")}) == []


def test_bare_ids_are_text_not_citations() -> None:
    memory = MEMORY + "\nThe bare RT-OBJ-missing and MEM-OBJ-UPPER are literal text.\n"
    assert errors(**{"memory.md": memory}) == []
    assert "RT-OBJ-missing" not in record_references(memory)


def test_quotations_and_fenced_examples_are_not_citations() -> None:
    memory = MEMORY + (
        "\n> Source text [RT-OBJ-missing](runtime.md#rt-obj-missing).\n> ---\n> `src/file.py`\n"
        "\n```markdown\n[RT-OBJ-missing](runtime.md#rt-obj-missing)\n```\n"
        "\nInline `[RT-OBJ-missing](runtime.md#rt-obj-missing)` code.\n"
    )
    assert errors(**{"memory.md": memory}) == []


def test_ordinary_links_stay_ordinary() -> None:
    memory = MEMORY + (
        "\nSee the [runtime report](runtime.md), its [Routes](runtime.md#routes) section, "
        "the [upstream code](https://example.invalid/repo#readme) and the [boundary](boundary.md).\n"
    )
    assert errors(**{"memory.md": memory}) == []
    assert record_links(memory)[-1].identifier == "RT-RTE-model-call", "only the record citations are collected"


def test_a_citation_leaving_the_artifact_directory_is_left_to_the_member_link_rule() -> None:
    memory = MEMORY.replace("(runtime.md#rt-obj-store)", "(../other/runtime.md#rt-obj-store)")
    assert errors(**{"memory.md": memory}) == []


# Annotations, parts and supersessions


def test_an_annotation_heading_links_its_record_and_declares_nothing() -> None:
    assert annotated_ids(MEMORY) == {"RT-RTE-model-call"}
    assert declared_ids(MEMORY) == ["MEM-RTE-import"]
    broken = MEMORY.replace("(runtime.md#rt-rte-model-call)", "(runtime.md#rt-rte-missing)")
    assert any("declares no RT-RTE-missing" in error
               for error in errors(**{"memory.md": broken.replace("[RT-RTE-model-call]", "[RT-RTE-missing]")}))


def test_an_annotation_without_a_record_link_is_refused() -> None:
    body = "## Annotations\n\n#### On RT-RTE-model-call — Overlay\n"
    assert any("must link exactly one record" in error for error in record_reference_errors(body))


@pytest.mark.parametrize(("field", "diagnostic"), [
    ("Part of: [RT-OBJ-store](runtime.md#rt-obj-store)", None),
    ("Part of: RT-OBJ-store", "exactly one record citation"),
    ("Part of: [RT-OBJ-store](runtime.md#rt-obj-store), [RT-RTE-model-call](runtime.md#rt-rte-model-call)",
     "exactly one record citation"),
    ("Part of: [MEM-OBJ-part](#mem-obj-part)", "cannot name itself"),
    ("- Part of: [RT-OBJ-store](runtime.md#rt-obj-store)", "unindented"),
])
def test_a_part_field_cites_exactly_one_other_record(field: str, diagnostic: str | None) -> None:
    body = "## Shared records\n\n" + declaration("MEM-OBJ-part", text=field)
    found = record_reference_errors(body)
    assert (not found) if diagnostic is None else any(diagnostic in error for error in found)


def test_a_part_field_needs_a_declaration_owner() -> None:
    body = "## Discussion\n\nPart of: [RT-OBJ-store](runtime.md#rt-obj-store)\n"
    assert record_reference_errors(body) == ["record references: Part of: must belong to a declared record"]


def test_a_supersession_links_both_records_and_indexes_the_superseded_one() -> None:
    reconciliation = ("## Reconciliation\n\nAmendment: [MEM-RTE-import](memory.md#mem-rte-import) is superseded by "
                      "[RT-RTE-model-call](runtime.md#rt-rte-model-call); both trace one call at SRC-1.\n")
    cites = {**CITES, "reconciliation.md": ["boundary.md", "runtime.md", "memory.md"]}
    _, found = artifact_record_errors("boundary.md", bodies(**{"reconciliation.md": reconciliation}), cites=cites)
    assert found == []
    assert value_amendments(reconciliation) == []
    assert amendment_index(reconciliation).startswith("Amended or superseded records: MEM-RTE-import;")
    changed = "## Reconciliation\n\nAmendment: [MEM-RTE-import](memory.md#mem-rte-import) has a new value.\n"
    assert value_amendments(changed) == ["Amendment: [MEM-RTE-import](memory.md#mem-rte-import) has a new value."]


# Sources


def test_bare_source_ids_resolve_against_the_register_in_scope() -> None:
    assert errors(**{"profile.md": "Evidence: SRC-1.\n"}) == [
        ("profile.md: unresolved source SRC-1; the Source register is outside the documents this one may "
        "cite: memory.md")]
    assert errors(**{"memory.md": MEMORY + "\nAlso SRC-9.\n"}) == [
        "memory.md: unresolved source SRC-9; the Source register does not declare it"]


def test_duplicate_source_rows_are_the_boundary_rule_s_finding() -> None:
    # The boundary's register rule refuses the second row; resolution does not repeat it.
    assert errors(**{"boundary.md": BOUNDARY + "| SRC-1 | Again |\n"}) == []


@pytest.mark.parametrize("reference", [
    "SRC-1 through SRC-2", "SRC-1–SRC-2", "SRC-1–2", "`SRC-1`–`SRC-2`", "SRC-1-2",
])
def test_source_ranges_are_refused(reference: str) -> None:
    assert any("ranges are not expanded" in error for error in record_reference_errors(RUNTIME + reference))


def test_source_register_rows_preserve_escaped_pipes_and_ignore_examples() -> None:
    row = r"| SRC-1 | git | `https://example.invalid/source` | `revision` | implementation | `a\|b.txt` | `a\|b.txt` | none |"
    body = "## Source register\n\n" + row
    body += "\n> " + row.replace("SRC-1", "SRC-2")
    body += "\n```markdown\n" + row.replace("SRC-1", "SRC-3") + "\n```\n"
    assert source_register_rows(body) == [[
        "SRC-1", "git", "`https://example.invalid/source`", "`revision`",
        "implementation", "`a|b.txt`", "`a|b.txt`", "none",
    ]]


def test_findings_name_the_member_they_belong_to() -> None:
    profile = "Uses [RT-OBJ-store](runtime.md#rt-obj-store).\n"
    _, findings = artifact_record_findings("boundary.md", bodies(**{"profile.md": profile}), cites=CITES)
    assert [name for name, _, _ in findings] == ["profile.md"]
