import csv
import io
import json
from copy import deepcopy
from types import SimpleNamespace

import pytest

from commonplace.lib import systems_matrix as sm
from tests.commonplace.agentic_analysis.fixtures import comparison_schema

KNOWN = {"RT-OBJ-store", "RT-RTE-model-call", "RT-ABS-missing-route"}
KNOWN2 = dict.fromkeys(KNOWN, "runtime.md")
"""Profiles cite records as member.md#anchor, so known IDs name their member."""
STORE = "runtime.md#rt-obj-store"
ABSENCE = "runtime.md#rt-abs-missing-route"
CALL = "runtime.md#rt-rte-model-call"


def revision2():
    return {
        "version": 2,
        "scope": "Synthetic retained objects and admission routes",
        "axes": {
            axis: {
                "assessment": "uninspected", "units": [], "records": [],
                "note": "Inventory not inspected; completeness prevented.",
            }
            for axis in sm.AXES
        },
    }


def finding(value, basis="wired", records=None):
    return {
        "value": value, "basis": basis,
        "records": records or [STORE], "note": "Synthetic witness only.",
    }


def unit(*findings, assessment="known", scope="Automatic update", records=None):
    return {
        "scope": scope, "assessment": assessment, "findings": list(findings),
        "records": records or [STORE],
        "note": "Coverage is scoped to this route; opaque alternatives remain named.",
    }


def axis2(*units, assessment="known", records=None):
    return {
        "assessment": assessment, "units": list(units),
        "records": records or [STORE], "note": "Synthetic scoped inventory witness.",
    }


def known(values, records=None, basis="wired"):
    """A known axis with one unit per value, every level citing ``records``."""
    return axis2(
        *(unit(finding(value, basis, records), scope=f"Route for {value}", records=records) for value in values),
        records=records,
    )


def test_multiple_stores_and_distinct_unknown_assessments():
    data = revision2()
    data["axes"]["storage_substrate"] = known(["files", "sqlite"])
    data["axes"]["curation_operations"] = axis2(assessment="absent", records=[ABSENCE])
    data["axes"]["lineage"]["assessment"] = "not-determinable"
    before = deepcopy(data)
    assert sm.validate_comparison(data, known_ids=KNOWN2) == before
    assert data == before


@pytest.mark.parametrize(
    "edit, error",
    [
        (lambda p: p["axes"].pop("lineage"), "every registered axis"),
        (
            lambda p: p["axes"].update(storage_substrate=known(["files", "unknown"])),
            "off-vocabulary",
        ),
        (
            lambda p: p["axes"].update(storage_substrate=known(["files"], [STORE, STORE])),
            "duplicate",
        ),
        (
            lambda p: p["axes"].update(storage_substrate=known(["files"], ["runtime.md#rt-obj-missing"])),
            "unresolved",
        ),
        (
            lambda p: p["axes"].update(curation_operations=axis2(assessment="absent")),
            "absence requires",
        ),
        (
            lambda p: p["axes"].update(lineage=axis2(unit(finding("authored")), assessment="uninspected")),
            "empty .*findings",
        ),
        (
            lambda p: p["axes"].update(trace_learning=known(["no"], [ABSENCE])),
            "must be inapplicable",
        ),
        (lambda p: p["axes"].update(read_back_direction=known(["pull"])), "pull-only"),
    ],
)
def test_rejects_unsupported_or_contradictory_classification(edit, error):
    data = revision2()
    edit(data)
    with pytest.raises(ValueError, match=error):
        sm.validate_comparison(data, known_ids=KNOWN2)


def test_cross_reference_is_not_a_record_declaration():
    data = revision2()
    data["axes"]["storage_substrate"] = known(["files"], ["memory.md#mem-obj-example9"])
    body = "## Shared records\n\nSee MEM-OBJ-example9 for more details.\n\n#### MEM-OBJ-store\n\nLabel: store\n"
    with pytest.raises(ValueError, match="unresolved"):
        sm.profile_member_comparison({"memory-comparison": data}, record_bodies={"overview.md": "", "memory.md": body})


def test_comparison_resolves_canonical_runtime_ids():
    data = revision2()
    data["axes"]["storage_substrate"] = known(["files"], [STORE])
    body = "## Shared records\n\n### Operative objects\n\n" + "\n".join(
        f"#### {id_}\n\nLabel: Fixture\n" for id_ in sorted(KNOWN))
    assert sm.profile_member_comparison(
        {"memory-comparison": data}, record_bodies={"overview.md": "", "runtime.md": body},
    ) == data


def test_existing_memory_axes_can_cite_workflow_records():
    data = revision2()
    data["axes"]["storage_substrate"] = known(["files"], ["workflow.md#wf-obj-store"])
    assert list(comparison_schema().iter_errors(data)) == []
    body = "## Shared records\n\n### Operative objects\n\n#### WF-OBJ-store\n\nLabel: Fixture store\n"
    assert sm.profile_member_comparison(
        {"memory-comparison": data}, record_bodies={"workflow.md": body},
    ) == data


def test_pulled_memory_without_trace_learning_has_inapplicable_subaxes():
    data = revision2()
    data["axes"]["read_back_direction"] = known(["pull"], [CALL])
    data["axes"]["trace_learning"] = known(["no"], [ABSENCE])
    for axis in ("read_back_signal", "trace_source"):
        data["axes"][axis] = axis2(assessment="inapplicable")
    sm.validate_comparison(data, known_ids=KNOWN2)


def test_removed_axes_are_rejected():
    data = revision2()
    data["axes"]["learning_scope"] = deepcopy(data["axes"]["lineage"])
    with pytest.raises(ValueError, match="every registered axis"):
        sm.validate_comparison(data, known_ids=KNOWN2)


def test_mixed_strength_and_partial_coverage_preserve_only_supported_positives():
    from scripts.render_systems_table import assessment

    data = revision2()
    entry = known(["automatic", "manual"], [CALL])
    entry["units"][1]["findings"][0]["basis"] = "afforded"
    data["axes"]["write_agency"] = entry
    for disposition in ("known", "partial"):
        entry["assessment"] = disposition
        if disposition == "partial":
            entry["units"].append(unit(assessment="not-determinable", scope="Opaque admission"))
        sm.validate_comparison(data, known_ids=KNOWN2)
        row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
        assert sm.supported_values(row, "write_agency") == {"automatic"}
        assert sm.complete_values(row, "write_agency") is None
        text = assessment(row, "write_agency")
        assert "automatic [wired]" in text and "manual [afforded]" in text
        assert text.startswith(f"{disposition} coverage")
        row["source_tier"] = "doc-grounded"
        assert sm.supported_values(row, "write_agency") == set()
    entry["units"][1]["findings"][0]["basis"] = "wired"
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, "write_agency") is None  # still partial
    entry["units"].pop()
    entry["assessment"] = "known"
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, "write_agency") == ("automatic", "manual")


def test_revision2_partial_positive_roundtrip_and_nonmutation():
    data = revision2()
    data["axes"]["write_agency"] = axis2(
        unit(finding("automatic")),
        unit(assessment="not-determinable", scope="Initial sheet: caller identity unknown"),
        assessment="partial",
    )
    before = deepcopy(data)
    comparison_schema().validate(data)
    assert sm.validate_comparison(data, known_ids=KNOWN2) == before
    row = sm.project_comparison(data)
    row.update(source_tier="code-grounded")
    assert row["write_agency"] == ["automatic"]
    assert sm.supported_values(row, "write_agency") == {"automatic"}
    assert sm.complete_values(row, "write_agency") is None
    assert row["write_agency_units"] == data["axes"]["write_agency"]["units"]
    row.update({name: row.get(name, "fixture") for name in sm.METADATA})
    serialized = next(csv.DictReader(io.StringIO(sm.csv_text(sm.MatrixInputs([row], {})))))
    assert serialized["comparison_version"] == "2"
    assert json.loads(serialized["write_agency_units"]) == row["write_agency_units"]
    assert json.loads(serialized["write_agency"]) == ["automatic"]
    assert data == before


def test_revision2_every_finding_must_be_strong_even_for_same_value():
    data = revision2()
    data["axes"]["write_agency"] = axis2(
        unit(finding("automatic")),
        unit(finding("automatic", basis="claimed"), scope="Other admission"),
        unit(finding("manual"), scope="Explicit operator replacement"),
    )
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.supported_values(row, "write_agency") == {"automatic", "manual"}
    assert row["write_agency_evidence"]["automatic"]["basis"] == "wired"
    assert sm.complete_values(row, "write_agency") is None
    data["axes"]["write_agency"]["units"][1]["findings"][0]["basis"] = "observed"
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, "write_agency") == ("automatic", "manual")
    row["source_tier"] = "doc-grounded"
    assert sm.complete_values(row, "write_agency") is None


@pytest.mark.parametrize("assessment", ["known", "partial"])
def test_revision2_trace_local_no_does_not_negate_yes(assessment):
    data = revision2()
    units = [
        unit(finding("yes"), scope="Trace-fed later guidance"),
        unit(finding("no", records=["runtime.md#rt-abs-missing-route"]), scope="Bounded static branch"),
    ]
    if assessment == "partial":
        units.append(unit(assessment="uninspected", scope="Opaque branch"))
    data["axes"]["trace_learning"] = axis2(*units, assessment=assessment)
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning"] == ["yes"]
    assert row["trace_learning_units"][1]["findings"][0]["value"] == "no"
    assert sm.complete_values(row, "trace_learning") == (("yes",) if assessment == "known" else None)


def test_revision2_bounded_absence_and_unknown_are_distinct():
    data = revision2()
    data["axes"]["curation_operations"] = axis2(assessment="absent")
    data["axes"]["curation_operations"]["records"] = ["runtime.md#rt-abs-missing-route"]
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, "curation_operations") == ()
    assert sm.complete_values(row, "storage_substrate") is None
    data["axes"]["trace_learning"] = axis2(unit(finding("no", records=["runtime.md#rt-abs-missing-route"])))
    data["axes"]["trace_source"] = axis2(assessment="inapplicable")
    sm.validate_comparison(data, known_ids=KNOWN2)
    assert sm.project_comparison(data)["trace_learning"] == ["no"]


@pytest.mark.parametrize("axis, values", [
    ("storage_substrate", ["files", "vector"]),
    ("representational_form", ["natural-language", "symbolic"]),
    ("lineage", ["imported", "trace-extracted"]),
    ("behavioral_authority", ["knowledge", "learning"]),
    ("curation_operations", ["consolidate"]),
    ("read_back_direction", ["pull", "push"]),
    ("read_back_signal", ["identifier"]),
    ("trace_source", ["session-logs", "tool-traces"]),
])
def test_revision2_partial_unions_keep_heterogeneous_parts(axis, values):
    data = revision2()
    data["axes"][axis] = axis2(
        *(unit(finding(value), scope=f"Part for {value}") for value in values),
        unit(assessment="not-determinable", scope="Opaque included part"),
        assessment="partial",
    )
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row[axis] == sorted(values)
    assert sm.complete_values(row, axis) is None


@pytest.mark.parametrize("mutation, error", [
    (lambda p: p.update(version=3), "unsupported version"),
    (lambda p: p.update(version=True), "unsupported version"),
    (lambda p: p["axes"].pop("lineage"), "every registered axis"),
    (lambda p: p["axes"]["write_agency"].update(values=["automatic"]), "requires assessment"),
    (lambda p: p["axes"]["write_agency"].update(assessment="partial"), "unresolved coverage"),
    (lambda p: p["axes"]["write_agency"]["units"].append(unit(assessment="uninspected")), "resolved units"),
    (lambda p: p["axes"]["write_agency"]["units"][0].update(scope=" "), "missing unit scope"),
    (lambda p: p["axes"]["write_agency"]["units"][0].update(assessment="uninspected"), "empty findings"),
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(value="caller"), "off-vocabulary"),
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(basis="requested"), "invalid evidence basis"),
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=["runtime.md#rt-obj-missing"]), "unresolved"),
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=["SRC-1"]), "invalid record citation"),
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(note=" "), "missing evidence rationale"),
])
def test_revision2_rejects_malformed_and_unsupported_assertions(mutation, error):
    data = revision2()
    data["axes"]["write_agency"] = axis2(unit(finding("automatic")))
    mutation(data)
    with pytest.raises(ValueError, match=error):
        sm.validate_comparison(data, known_ids={**KNOWN2, "SRC-1": "boundary.md"})


@pytest.mark.parametrize("assessment", ["known", "partial"])
def test_revision2_no_without_bounded_absence_is_rejected(assessment):
    data = revision2()
    data["axes"]["trace_learning"] = axis2(unit(finding("no"), assessment=assessment))
    # A partial unit is also invalid: no requires both known coverage and an
    # absence warrant. This case deliberately lacks the warrant for either.
    with pytest.raises(ValueError, match="bounded absence"):
        sm.validate_comparison(data, known_ids=KNOWN2)


def test_revision2_canonical_declarations_not_mentions():
    data = revision2()
    data["axes"]["write_agency"] = axis2(unit(finding("automatic")))
    with pytest.raises(ValueError, match="unresolved"):
        sm.profile_member_comparison({"memory-comparison": data}, record_bodies={
            "overview.md": "", "memory.md": "## Shared records\n\nSee RT-OBJ-store.\n",
        })
    assert sm.profile_member_comparison({"memory-comparison": data}, record_bodies={
        "overview.md": "", "runtime.md": "## Shared records\n\n#### RT-OBJ-store\n\nLabel: Fixture store\n",
    }) == data


def test_load_results_projects_revision2_member(tmp_path, monkeypatch):
    data = revision2()
    data["axes"]["storage_substrate"] = axis2(
        unit(finding("files")), unit(assessment="not-determinable", scope="Provider state"),
        assessment="partial",
    )
    overview = SimpleNamespace(
        path=tmp_path / "kb/agentic-system-analyses/retained/example/overview.md",
        name="overview.md", body="", content=b"overview", sha256="overview-digest",
        frontmatter={
            "system": "Synthetic example", "run-id": "fixture", "reviewed-boundary": "fixture-rev",
            "analysis-cutoff": "2026-10-05", "evidence-tier": "code-grounded",
            "boundary-kind": "runtime", "description": "Fixture only",
        },
    )
    memory = SimpleNamespace(
        name="memory.md", sha256="memory-digest",
        frontmatter={"source-identity": "synthetic"},
        body="## Shared records\n\n",
    )
    runtime = SimpleNamespace(name="runtime.md", body="## Shared records\n\n#### RT-OBJ-store\n\nLabel: Fixture store\n")
    profile_member = SimpleNamespace(
        name="memory-profile.md", sha256="profile-digest", body="",
        content=("---\n" + json.dumps({"memory-comparison": data}) + "\n---\n").encode(),
        frontmatter={"memory-comparison": data},
    )
    analysis = SimpleNamespace(
        overview=overview, memory=memory, memory_profile=profile_member,
        artifact=SimpleNamespace(path=overview.path.parent, content=b"manifest"),
        documents=[overview, memory, profile_member],
        roles={"overview": overview, "runtime": runtime, "memory": memory, "memory-profile": profile_member},
    )
    monkeypatch.setattr(sm, "current_analyses", lambda root, run: [analysis])
    inputs = sm.load_results(tmp_path)
    row = inputs.rows[0]
    assert row["comparison_version"] == 2
    assert row["storage_substrate"] == ["files"]
    assert row["storage_substrate_units"] == data["axes"]["storage_substrate"]["units"]
    assert sm.complete_values(row, "storage_substrate") is None
    assert next(csv.DictReader(io.StringIO(sm.csv_text(inputs)))) == sm.csv_row(row)


@pytest.mark.parametrize("mutation", [
    lambda p: p.update(version=1),
    lambda p: p.update(version=True),
    lambda p: p["axes"]["write_agency"]["units"][0].update(scope=" "),
    lambda p: p["axes"]["write_agency"]["units"][0].update(assessment="uninspected"),
    lambda p: p["axes"]["write_agency"]["units"][0].update(findings=[]),
    lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=["SRC-1"]),
    lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=[]),
    lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=["runtime.md#rt-obj-store", "runtime.md#rt-obj-store"]),
    lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(note=" "),
])
def test_revision2_schema_rejects_malformed_structure(mutation):
    data = revision2()
    data["axes"]["write_agency"] = axis2(unit(finding("automatic")))
    mutation(data)
    assert list(comparison_schema().iter_errors(data))


def test_revision2_partial_unit_can_name_its_own_unresolved_parts():
    data = revision2()
    data["axes"]["write_agency"] = axis2(
        unit(finding("automatic"), assessment="partial", scope="Update with opaque admission alternative"),
        assessment="partial",
    )
    comparison_schema().validate(data)
    sm.validate_comparison(data, known_ids=KNOWN2)
    assert sm.project_comparison(data)["write_agency"] == ["automatic"]


@pytest.mark.parametrize("unresolved", ["uninspected", "not-determinable"])
def test_revision2_local_no_counts_as_partial_classification_not_system_absence(unresolved):
    data = revision2()
    data["axes"]["trace_learning"] = axis2(
        unit(finding("no", records=["runtime.md#rt-abs-missing-route"])),
        unit(assessment=unresolved, scope="Unresolved write"), assessment="partial",
    )
    # Revised contract: a warranted local no classifies a unit, even though it
    # establishes neither learning existence nor a system-wide negative.
    before = deepcopy(data)
    comparison_schema().validate(data)
    assert sm.validate_comparison(data, known_ids=KNOWN2) == before
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning_assessment"] == "partial"
    assert row["trace_learning"] == []
    assert row["trace_learning_evidence"] == {}
    assert row["trace_learning_units"] == before["axes"]["trace_learning"]["units"]
    assert sm.supported_values(row, "trace_learning") == set()
    assert sm.complete_values(row, "trace_learning") is None
    assert row["trace_source_assessment"] == "uninspected"
    assert sm.complete_values(row, "trace_source") is None
    row.update({name: row.get(name, "fixture") for name in sm.METADATA})
    serialized = next(csv.DictReader(io.StringIO(sm.csv_text(sm.MatrixInputs([row], {})))))
    assert serialized["trace_learning_assessment"] == "partial"
    assert json.loads(serialized["trace_learning"]) == []
    assert json.loads(serialized["trace_learning_units"]) == row["trace_learning_units"]
    assert data == before


@pytest.mark.parametrize("assessment", ["uninspected", "not-determinable"])
@pytest.mark.parametrize("value, records", [("no", [ABSENCE]), ("yes", [STORE])])
def test_revision2_unresolved_axis_cannot_hide_a_classified_unit(assessment, value, records):
    data = revision2()
    data["axes"]["trace_learning"] = axis2(
        unit(finding(value, records=records), scope="Inspected branch"),
        unit(assessment=assessment, scope="Unresolved alternative write"), assessment=assessment,
    )
    comparison_schema().validate(data)
    # Previously local no was allowed under an unresolved aggregate. Both
    # controlled values now require partial coverage when alternatives remain.
    with pytest.raises(ValueError, match="empty .*findings"):
        sm.validate_comparison(data, known_ids=KNOWN2)
    data["axes"]["trace_learning"]["assessment"] = "partial"
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning"] == (["yes"] if value == "yes" else [])
    assert row["trace_learning_units"][0]["findings"][0]["value"] == value
    assert sm.supported_values(row, "trace_learning") == ({"yes"} if value == "yes" else set())
    assert sm.complete_values(row, "trace_learning") is None


@pytest.mark.parametrize("parent, child, positive", [
    ("trace_learning", "trace_source", "yes"),
    ("read_back_direction", "read_back_signal", "push"),
])
@pytest.mark.parametrize("status", ["known", "partial", "uninspected", "not-determinable", "inapplicable"])
def test_whole_inapplicability_rejects_positive_or_unresolved_inventory(parent, child, positive, status):
    data = revision2()
    units = [unit(finding(positive))] if status in {"known", "partial"} else []
    if status == "partial":
        units.append(unit(assessment="uninspected"))
    data["axes"][parent] = axis2(*units, assessment=status)
    data["axes"][child] = axis2(assessment="inapplicable")
    with pytest.raises(ValueError, match=f"{child}: inapplicability requires"):
        sm.validate_comparison(data, known_ids=KNOWN2)


@pytest.mark.parametrize("parent, child, value", [
    ("trace_learning", "trace_source", "no"),
    ("read_back_direction", "read_back_signal", "pull"),
])
def test_local_negative_cannot_make_unresolved_inventory_inapplicable(parent, child, value):
    data = revision2()
    data["axes"][parent] = axis2(
        unit(finding(value, records=["runtime.md#rt-abs-missing-route"])),
        unit(assessment="uninspected", scope="Opaque alternative"),
        # Local no is classified coverage too; the unresolved alternative makes
        # either inventory partial, but cannot justify child inapplicability.
        assessment="partial",
    )
    data["axes"][child] = axis2(assessment="inapplicable")
    with pytest.raises(ValueError, match=f"{child}: inapplicability requires"):
        sm.validate_comparison(data, known_ids=KNOWN2)


@pytest.mark.parametrize("parent, child, value", [
    ("trace_learning", "trace_source", "no"),
    ("read_back_direction", "read_back_signal", "pull"),
])
@pytest.mark.parametrize("status", ["known", "absent"])
def test_whole_inapplicability_accepts_only_complete_negative_boundaries(parent, child, value, status):
    data = revision2()
    data["axes"][parent] = axis2(
        *([unit(finding(value, records=[ABSENCE]))] if status == "known" else []),
        assessment=status, records=[ABSENCE],
    )
    data["axes"][child] = axis2(assessment="inapplicable")
    sm.validate_comparison(data, known_ids=KNOWN2)


@pytest.mark.parametrize("axis", list(sm.AXES))
def test_known_axis_cannot_be_wholly_inapplicable(axis):
    data = revision2()
    data["axes"][axis] = axis2(unit(assessment="inapplicable"))
    with pytest.raises(ValueError, match="wholly inapplicable"):
        sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, axis) is None
    row[axis + "_assessment"] = "inapplicable"
    assert sm.complete_values(row, axis) is None
    row[axis + "_assessment"] = "absent"
    assert sm.complete_values(row, axis) == ()


def test_partial_negative_does_not_establish_absence():
    data = revision2()
    data["axes"]["trace_learning"] = axis2(
        unit(finding("no", records=[ABSENCE]), assessment="partial"), assessment="partial",
    )
    with pytest.raises(ValueError, match="local no requires resolved bounded absence"):
        sm.validate_comparison(data, known_ids=KNOWN2)


@pytest.mark.parametrize("assessment", ["uninspected", "not-determinable"])
def test_revision2_unresolved_only_learning_has_no_classified_coverage(assessment):
    data = revision2()
    data["axes"]["trace_learning"] = axis2(
        unit(assessment=assessment, scope="Included opaque write"), assessment=assessment,
    )
    before = deepcopy(data)
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning"] == []
    assert sm.supported_values(row, "trace_learning") == set()
    assert sm.complete_values(row, "trace_learning") is None
    assert data == before
    data["axes"]["trace_learning"]["assessment"] = "partial"
    with pytest.raises(ValueError, match="partial coverage needs"):
        sm.validate_comparison(data, known_ids=KNOWN2)


def test_revision2_yes_and_no_must_describe_distinct_units():
    data = revision2()
    data["axes"]["trace_learning"] = axis2(unit(
        finding("yes"), finding("no", records=[ABSENCE]),
    ))
    with pytest.raises(ValueError, match="yes and no require distinct units"):
        sm.validate_comparison(data, known_ids=KNOWN2)


@pytest.mark.parametrize("unresolved", ["uninspected", "not-determinable"])
@pytest.mark.parametrize("include_yes", [False, True])
def test_revision2_partial_learning_matrix_statistics_keep_local_warrants(unresolved, include_yes, monkeypatch, capsys):
    from scripts import analyze_matrix as stats

    data = revision2()
    data["axes"]["trace_learning"] = axis2(
        *([unit(finding("yes"), scope="Trace-fed guidance")] if include_yes else []),
        unit(finding("no", records=[ABSENCE]), scope="Static branch", records=[ABSENCE]),
        unit(assessment=unresolved, scope="Opaque writer"), assessment="partial",
    )
    if include_yes:
        data["axes"]["trace_source"] = axis2(
            unit(finding("session-logs"), scope="Trace-fed guidance input"),
            unit(assessment=unresolved, scope="Opaque writer input"), assessment="partial",
        )
    before = deepcopy(data)
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = {**dict.fromkeys(sm.METADATA, "fixture"), **sm.project_comparison(data),
           "source_tier": "code-grounded"}
    expected = ["yes"] if include_yes else []
    assert row["trace_learning"] == expected
    assert row["trace_learning_units"][int(include_yes)]["findings"][0]["records"] == [ABSENCE]
    assert sm.supported_values(row, "trace_learning") == set(expected)
    assert sm.complete_values(row, "trace_learning") is None
    assert row["trace_source"] == (["session-logs"] if include_yes else [])
    assert sm.complete_values(row, "trace_source") is None
    inputs = sm.MatrixInputs([row], {})
    exported = next(csv.DictReader(io.StringIO(sm.csv_text(inputs))))
    assert json.loads(exported["trace_learning_units"]) == before["axes"]["trace_learning"]["units"]
    assert json.loads(exported["trace_source_units"]) == before["axes"]["trace_source"]["units"]
    monkeypatch.setattr(stats, "load_results", lambda *_: inputs)
    assert stats.main([]) == 0
    text = capsys.readouterr().out
    assert "assessment trace_learning: {'partial': 1}" in text
    assert f"finding bases: {{'known:wired': {2 if include_yes else 1}}}" in text
    assert f"supported trace_learning: { {'yes': 1} if include_yes else {} } / 1" in text
    assert "complete trace_learning: 0 of 1 rows" in text
    assert "complete trace_source: 0 of 1 rows" in text
    assert data == before


def test_revision2_complete_no_is_not_global_axis_absence():
    data = revision2()
    data["axes"]["trace_learning"] = known(["no"], [ABSENCE])
    data["axes"]["trace_source"] = axis2(assessment="inapplicable", records=[ABSENCE])
    before = deepcopy(data)
    comparison_schema().validate(data)
    sm.validate_comparison(data, known_ids=KNOWN2)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning_assessment"] == "known"
    assert row["trace_learning"] == ["no"]
    assert sm.supported_values(row, "trace_learning") == {"no"}
    assert sm.complete_values(row, "trace_learning") == ("no",)
    assert row["trace_source"] == []
    assert sm.complete_values(row, "trace_source") is None  # Inapplicable is not absent.
    assert data == before
