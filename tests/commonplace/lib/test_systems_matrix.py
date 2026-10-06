import csv
import io
import json
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest
from jsonschema import Draft202012Validator

from commonplace.lib import systems_matrix as sm

KNOWN = {"RT-OBJ-store", "RT-RTE-model-call", "RT-ABS-missing-route"}


def profile():
    return {
        "scope": "Accumulated project memory",
        "axes": {
            axis: {
                "assessment": "uninspected",
                "evidence": {},
                "values": [],
                "records": [],
                "note": "The evidence does not cover this mechanism.",
            }
            for axis in sm.AXES
        },
    }


def known(values, records=None, basis="wired"):
    return {
        "assessment": "known",
        "evidence": {
            value: {
                "basis": basis,
                "records": records or ["RT-OBJ-store"],
                "note": "Fixture witness.",
            }
            for value in values
        },
        "values": values,
        "records": records or ["RT-OBJ-store"],
        "note": "The named records cover the boundary.",
    }


def test_multiple_stores_and_distinct_unknown_assessments():
    data = profile()
    data["axes"]["storage_substrate"] = known(["files", "sqlite"])
    data["axes"]["curation_operations"].update(assessment="absent", records=["RT-ABS-missing-route"])
    data["axes"]["lineage"]["assessment"] = "not-determinable"
    before = deepcopy(data)
    assert sm.validate_comparison(data, known_ids=KNOWN) == before
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
            lambda p: p["axes"].update(storage_substrate=known(["files", "files"])),
            "duplicate",
        ),
        (
            lambda p: p["axes"].update(storage_substrate=known(["files"], ["RT-OBJ-missing"])),
            "unresolved",
        ),
        (
            lambda p: p["axes"]["curation_operations"].update(assessment="absent"),
            "absence requires",
        ),
        (lambda p: p["axes"]["lineage"].update(values=["authored"]), "empty values"),
        (
            lambda p: p["axes"].update(trace_learning=known(["no"])),
            "must be inapplicable",
        ),
        (lambda p: p["axes"].update(read_back_direction=known(["pull"])), "pull-only"),
    ],
)
def test_rejects_unsupported_or_contradictory_classification(edit, error):
    data = profile()
    edit(data)
    with pytest.raises(ValueError, match=error):
        sm.validate_comparison(data, known_ids=KNOWN)


def test_cross_reference_is_not_a_record_declaration():
    data = profile()
    data["axes"]["storage_substrate"] = known(["files"], ["MEM-OBJ-example9"])
    body = "## Shared records\n\nSee MEM-OBJ-example9 for more details.\n\n#### MEM-OBJ-store — store\n"
    with pytest.raises(ValueError, match="unresolved"):
        sm.profile_member_comparison({"memory-comparison": data}, record_bodies={"overview.md": "", "memory.md": body})


def test_comparison_resolves_canonical_runtime_ids():
    identifier = "RT-OBJ-store"
    data = profile()
    data["axes"]["storage_substrate"] = known(["files"], [identifier])
    body = "## Shared records\n\n### Operative objects\n\n" + "\n".join(f"#### {id_} — Fixture\n" for id_ in KNOWN | {identifier})
    assert sm.profile_member_comparison({"memory-comparison": data}, record_bodies={"overview.md": "", "memory.md": body}) == data


def test_pulled_memory_without_trace_learning_has_inapplicable_subaxes():
    data = profile()
    data["axes"]["read_back_direction"] = known(["pull"], ["RT-RTE-model-call"])
    data["axes"]["trace_learning"] = known(["no"], ["RT-ABS-missing-route"])
    for axis in ("read_back_signal", "trace_source"):
        data["axes"][axis]["assessment"] = "inapplicable"
    sm.validate_comparison(data, known_ids=KNOWN)


def test_removed_axes_are_rejected():
    data = profile()
    data["axes"]["learning_scope"] = deepcopy(data["axes"]["lineage"])
    with pytest.raises(ValueError, match="every registered axis"):
        sm.validate_comparison(data, known_ids=KNOWN)


def test_mixed_strength_and_partial_coverage_preserve_only_supported_positives():
    from scripts.render_systems_table import assessment

    data = profile()
    entry = known(["automatic", "manual"], ["RT-RTE-model-call"])
    entry["evidence"]["manual"]["basis"] = "afforded"
    data["axes"]["write_agency"] = entry
    for disposition in ("known", "partial"):
        entry["assessment"] = disposition
        sm.validate_comparison(data, known_ids=KNOWN)
        row = {
            "source_tier": "code-grounded",
            "write_agency": entry["values"],
            "write_agency_assessment": disposition,
            "write_agency_evidence": entry["evidence"],
            "write_agency_note": entry["note"],
        }
        assert sm.supported_values(row, "write_agency") == {"automatic"}
        assert sm.complete_values(row, "write_agency") is None
        assert "automatic [wired], manual [afforded]" in assessment(row, "write_agency")
        assert ("partial coverage" in assessment(row, "write_agency")) == (
            disposition == "partial"
        )
        row["source_tier"] = "doc-grounded"
        assert sm.supported_values(row, "write_agency") == set()
    entry["evidence"]["manual"]["basis"] = "wired"
    row.update(source_tier="code-grounded", write_agency_evidence=entry["evidence"])
    assert sm.complete_values(row, "write_agency") is None  # still partial
    row["write_agency_assessment"] = "known"
    assert sm.complete_values(row, "write_agency") == ("automatic", "manual")


@pytest.mark.parametrize(
    "mutation, error",
    [
        ("missing", "evidence must cover exactly the declared values"),
        ("unknown-record", "write_agency.manual: unresolved"),
        ("no-basis", "invalid evidence basis"),
        ("empty-note", "missing evidence rationale"),
    ],
)
def test_each_value_requires_its_own_witness(mutation, error):
    data = profile()
    entry = known(["automatic", "manual"], ["RT-RTE-model-call"])
    data["axes"]["write_agency"] = entry
    if mutation == "missing":
        del entry["evidence"]["manual"]
    elif mutation == "unknown-record":
        entry["evidence"]["manual"]["records"] = ["RT-RTE-missing"]
    elif mutation == "no-basis":
        entry["evidence"]["manual"]["basis"] = None
    else:
        entry["evidence"]["manual"]["note"] = ""
    with pytest.raises(ValueError, match=error):
        sm.validate_comparison(data, known_ids=KNOWN)


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
        "records": records or ["RT-OBJ-store"], "note": "Synthetic witness only.",
    }


def unit(*findings, assessment="known", scope="Automatic update"):
    return {
        "scope": scope, "assessment": assessment, "findings": list(findings),
        "records": ["RT-OBJ-store"],
        "note": "Coverage is scoped to this route; opaque alternatives remain named.",
    }


def axis2(*units, assessment="known"):
    return {
        "assessment": assessment, "units": list(units),
        "records": ["RT-OBJ-store"], "note": "Synthetic scoped inventory witness.",
    }


def comparison_schema():
    schema = json.loads((Path(__file__).resolve().parents[3] /
                         "kb/agentic-system-analyses/types/agent-memory-profile.schema.yaml").read_text())
    comparison = deepcopy(schema["allOf"][1]["properties"]["frontmatter"]["properties"]["memory-comparison"])
    comparison["$defs"] = schema["$defs"]
    Draft202012Validator.check_schema(comparison)
    return Draft202012Validator(comparison)


def test_revision2_partial_positive_roundtrip_and_nonmutation():
    data = revision2()
    data["axes"]["write_agency"] = axis2(
        unit(finding("automatic")),
        unit(assessment="not-determinable", scope="Initial sheet: caller identity unknown"),
        assessment="partial",
    )
    before = deepcopy(data)
    comparison_schema().validate(data)
    assert sm.validate_comparison(data, known_ids=KNOWN) == before
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
    sm.validate_comparison(data, known_ids=KNOWN)
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
        unit(finding("no", records=["RT-ABS-missing-route"]), scope="Bounded static branch"),
    ]
    if assessment == "partial":
        units.append(unit(assessment="uninspected", scope="Opaque branch"))
    data["axes"]["trace_learning"] = axis2(*units, assessment=assessment)
    sm.validate_comparison(data, known_ids=KNOWN)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning"] == ["yes"]
    assert row["trace_learning_units"][1]["findings"][0]["value"] == "no"
    assert sm.complete_values(row, "trace_learning") == (("yes",) if assessment == "known" else None)


def test_revision2_bounded_absence_and_unknown_are_distinct():
    data = revision2()
    data["axes"]["curation_operations"] = axis2(assessment="absent")
    data["axes"]["curation_operations"]["records"] = ["RT-ABS-missing-route"]
    sm.validate_comparison(data, known_ids=KNOWN)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, "curation_operations") == ()
    assert sm.complete_values(row, "storage_substrate") is None
    data["axes"]["trace_learning"] = axis2(unit(finding("no", records=["RT-ABS-missing-route"])))
    data["axes"]["trace_source"] = axis2(assessment="inapplicable")
    sm.validate_comparison(data, known_ids=KNOWN)
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
    sm.validate_comparison(data, known_ids=KNOWN)
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
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=["RT-OBJ-missing"]), "unresolved"),
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=["SRC-1"]), "canonical record ID"),
    (lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(note=" "), "missing evidence rationale"),
])
def test_revision2_rejects_malformed_and_unsupported_assertions(mutation, error):
    data = revision2()
    data["axes"]["write_agency"] = axis2(unit(finding("automatic")))
    mutation(data)
    with pytest.raises(ValueError, match=error):
        sm.validate_comparison(data, known_ids=KNOWN | {"SRC-1"})


@pytest.mark.parametrize("assessment", ["known", "partial"])
def test_revision2_no_without_bounded_absence_is_rejected(assessment):
    data = revision2()
    data["axes"]["trace_learning"] = axis2(unit(finding("no"), assessment=assessment))
    with pytest.raises(ValueError, match="bounded absence"):
        sm.validate_comparison(data, known_ids=KNOWN)


def test_revision2_canonical_declarations_not_mentions():
    data = revision2()
    data["axes"]["write_agency"] = axis2(unit(finding("automatic")))
    with pytest.raises(ValueError, match="unresolved"):
        sm.profile_member_comparison({"memory-comparison": data}, record_bodies={
            "overview.md": "", "memory.md": "## Shared records\n\nSee RT-OBJ-store.\n",
        })
    assert sm.profile_member_comparison({"memory-comparison": data}, record_bodies={
        "overview.md": "", "memory.md": "## Shared records\n\n#### RT-OBJ-store — Fixture store\n",
    }) == data


@pytest.mark.parametrize("data", [profile(), revision2()])
def test_schema_accepts_only_the_two_versioned_shapes(data):
    validator = comparison_schema()
    validator.validate(data)
    wrong = deepcopy(data)
    if "version" in wrong:
        del wrong["version"]
    else:
        wrong["version"] = 2
    assert list(validator.iter_errors(wrong))


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
        body="## Shared records\n\n#### RT-OBJ-store — Fixture store\n",
    )
    profile_member = SimpleNamespace(
        name="memory-profile.md", sha256="profile-digest", body="",
        frontmatter={"memory-comparison": data},
    )
    member_set = SimpleNamespace(
        overview=overview, memory=memory, profile=profile_member,
        artifact=SimpleNamespace(path=overview.path.parent, content=b"manifest"),
        documents=[overview, memory, profile_member],
        roles={"overview": overview, "memory": memory, "memory-profile": profile_member},
    )
    monkeypatch.setattr(sm, "current_analyses", lambda root, run: [member_set])
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
    lambda p: p["axes"]["write_agency"]["units"][0]["findings"][0].update(records=["RT-OBJ-store", "RT-OBJ-store"]),
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
    sm.validate_comparison(data, known_ids=KNOWN)
    assert sm.project_comparison(data)["write_agency"] == ["automatic"]


def test_revision2_partial_axis_cannot_promote_only_local_negatives():
    data = revision2()
    data["axes"]["trace_learning"] = axis2(
        unit(finding("no", records=["RT-ABS-missing-route"])),
        unit(assessment="uninspected", scope="Uninspected write"), assessment="partial",
    )
    with pytest.raises(ValueError, match="partial coverage needs positives"):
        sm.validate_comparison(data, known_ids=KNOWN)


@pytest.mark.parametrize("assessment", ["uninspected", "not-determinable"])
def test_revision2_local_negative_survives_unresolved_axis_without_system_no(assessment):
    data = revision2()
    data["axes"]["trace_learning"] = axis2(
        unit(finding("no", records=["RT-ABS-missing-route"]), scope="Inspected static branch"),
        unit(assessment=assessment, scope="Unresolved alternative write"), assessment=assessment,
    )
    comparison_schema().validate(data)
    sm.validate_comparison(data, known_ids=KNOWN)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning"] == []
    assert row["trace_learning_units"][0]["findings"][0]["value"] == "no"
    assert sm.supported_values(row, "trace_learning") == set()
    assert sm.complete_values(row, "trace_learning") is None


def test_legacy_projection_keeps_revision_identity_without_inventing_units():
    data = profile()
    data["axes"]["write_agency"] = known(["manual"])
    comparison_schema().validate(data)
    sm.validate_comparison(data, known_ids=KNOWN)
    row = sm.project_comparison(data)
    assert row["comparison_version"] == 1
    assert row["write_agency"] == ["manual"]
    assert row["write_agency_units"] == []
    assert "version" not in data


@pytest.mark.parametrize("version", [1, 2])
@pytest.mark.parametrize("parent, child, positive", [
    ("trace_learning", "trace_source", "yes"),
    ("read_back_direction", "read_back_signal", "push"),
])
@pytest.mark.parametrize("status", ["known", "partial", "uninspected", "not-determinable", "inapplicable"])
def test_whole_inapplicability_rejects_positive_or_unresolved_inventory(version, parent, child, positive, status):
    data = profile() if version == 1 else revision2()
    if version == 1:
        if status in {"known", "partial"}:
            data["axes"][parent] = known([positive])
        data["axes"][parent]["assessment"] = status
        data["axes"][child]["assessment"] = "inapplicable"
    else:
        units = [unit(finding(positive))] if status in {"known", "partial"} else []
        if status == "partial":
            units.append(unit(assessment="uninspected"))
        data["axes"][parent] = axis2(*units, assessment=status)
        data["axes"][child] = axis2(assessment="inapplicable")
    with pytest.raises(ValueError, match=f"{child}: inapplicability requires"):
        sm.validate_comparison(data, known_ids=KNOWN)


@pytest.mark.parametrize("parent, child, value", [
    ("trace_learning", "trace_source", "no"),
    ("read_back_direction", "read_back_signal", "pull"),
])
def test_local_negative_cannot_make_unresolved_inventory_inapplicable(parent, child, value):
    data = revision2()
    data["axes"][parent] = axis2(
        unit(finding(value, records=["RT-ABS-missing-route"])),
        unit(assessment="uninspected", scope="Opaque alternative"),
        assessment="uninspected" if value == "no" else "partial",
    )
    data["axes"][child] = axis2(assessment="inapplicable")
    with pytest.raises(ValueError, match=f"{child}: inapplicability requires"):
        sm.validate_comparison(data, known_ids=KNOWN)


@pytest.mark.parametrize("version", [1, 2])
@pytest.mark.parametrize("parent, child, value", [
    ("trace_learning", "trace_source", "no"),
    ("read_back_direction", "read_back_signal", "pull"),
])
@pytest.mark.parametrize("status", ["known", "absent"])
def test_whole_inapplicability_accepts_only_complete_negative_boundaries(version, parent, child, value, status):
    data = profile() if version == 1 else revision2()
    if version == 1:
        data["axes"][parent] = known([value], ["RT-ABS-missing-route"])
        if status == "absent":
            data["axes"][parent].update(assessment=status, values=[], evidence={})
        data["axes"][child]["assessment"] = "inapplicable"
    else:
        data["axes"][parent] = axis2(
            *([unit(finding(value, records=["RT-ABS-missing-route"]))] if status == "known" else []),
            assessment=status,
        )
        data["axes"][parent]["records"] = ["RT-ABS-missing-route"]
        data["axes"][child] = axis2(assessment="inapplicable")
    sm.validate_comparison(data, known_ids=KNOWN)


@pytest.mark.parametrize("axis", list(sm.AXES))
def test_known_axis_cannot_be_wholly_inapplicable(axis):
    data = revision2()
    data["axes"][axis] = axis2(unit(assessment="inapplicable"))
    with pytest.raises(ValueError, match="wholly inapplicable"):
        sm.validate_comparison(data, known_ids=KNOWN)
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert sm.complete_values(row, axis) is None
    row[axis + "_assessment"] = "inapplicable"
    assert sm.complete_values(row, axis) is None
    row[axis + "_assessment"] = "absent"
    assert sm.complete_values(row, axis) == ()


def test_partial_negative_does_not_establish_absence():
    data = profile()
    data["axes"]["trace_learning"] = known(["no"], ["RT-ABS-missing-route"])
    data["axes"]["trace_learning"]["assessment"] = "partial"
    with pytest.raises(ValueError, match="partial coverage cannot establish no"):
        sm.validate_comparison(data, known_ids=KNOWN)
