import csv
import io
import json
from copy import deepcopy

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


def test_existing_memory_axes_can_cite_workflow_records():
    data = revision2()
    data["axes"]["storage_substrate"] = known(["files"], ["workflow.md#wf-obj-store"])
    assert list(comparison_schema().iter_errors(data)) == []
    body = "## Shared records\n\n### Operative objects\n\n#### WF-OBJ-store\n\nLabel: Fixture store\n"
    assert sm.profile_member_comparison(
        {"memory-comparison": data}, record_bodies={"workflow.md": body},
    ) == data


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
