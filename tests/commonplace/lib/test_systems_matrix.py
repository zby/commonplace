from copy import deepcopy

import pytest

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


def test_partial_negative_does_not_establish_absence():
    data = profile()
    data["axes"]["trace_learning"] = known(["no"], ["RT-ABS-missing-route"])
    data["axes"]["trace_learning"]["assessment"] = "partial"
    with pytest.raises(ValueError, match="partial coverage cannot establish no"):
        sm.validate_comparison(data, known_ids=KNOWN)
