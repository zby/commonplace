from copy import deepcopy

import pytest

from commonplace.lib import systems_matrix as sm

BODY = "## Shared records\n\n### Operative objects\n\n| OBJ-1 | memory stores |\n\n### Routes\n\nRTE-1 retrieval route.\n\n### Evidenced absences\n\nABS-1 searched without finding curation.\n\n## Runtime account\n"


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
                "records": records or ["OBJ-1"],
                "note": "Fixture witness.",
            }
            for value in values
        },
        "values": values,
        "records": records or ["OBJ-1"],
        "note": "The named records cover the boundary.",
    }


def test_multiple_stores_and_distinct_unknown_assessments():
    data = profile()
    data["axes"]["storage_substrate"] = known(["files", "sqlite"])
    data["axes"]["curation_operations"].update(assessment="absent", records=["ABS-1"])
    data["axes"]["lineage"]["assessment"] = "not-determinable"
    before = deepcopy(data)
    assert sm.validate_comparison(data, BODY) == before
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
            lambda p: p["axes"].update(storage_substrate=known(["files"], ["OBJ-99"])),
            "unresolved",
        ),
        (
            lambda p: p["axes"]["curation_operations"].update(assessment="absent"),
            "absence requires",
        ),
        (lambda p: p["axes"]["lineage"].update(values=["authored"]), "empty values"),
        (
            lambda p: p["axes"].update(faithfulness_tested=known(["yes"])),
            "execution evidence",
        ),
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
        sm.validate_comparison(data, BODY)


def test_cross_reference_is_not_a_record_declaration():
    data = profile()
    data["axes"]["storage_substrate"] = known(["files"], ["OBJ-99"])
    body = BODY.replace("### Routes", "See OBJ-99 for more details.\n\n### Routes")
    with pytest.raises(ValueError, match="unresolved"):
        sm.validate_comparison(data, body)


def test_pulled_memory_without_trace_learning_has_inapplicable_subaxes():
    data = profile()
    data["axes"]["read_back_direction"] = known(["pull"], ["RTE-1"])
    data["axes"]["trace_learning"] = known(["no"], ["ABS-1"])
    for axis in (
        "read_back_signal",
        "trace_source",
        "learning_scope",
        "learning_timing",
        "distilled_form",
    ):
        data["axes"][axis]["assessment"] = "inapplicable"
    sm.validate_comparison(data, BODY)


def test_mixed_strength_and_partial_coverage_preserve_only_supported_positives():
    from scripts.render_systems_table import assessment

    data = profile()
    entry = known(["automatic", "manual"], ["RTE-1"])
    entry["evidence"]["manual"]["basis"] = "afforded"
    data["axes"]["write_agency"] = entry
    for disposition in ("known", "partial"):
        entry["assessment"] = disposition
        sm.validate_comparison(data, BODY)
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
    "mutation",
    ["missing", "extra", "unknown-record", "no-basis", "empty-note", "legacy"],
)
def test_each_value_requires_its_own_witness(mutation):
    data = profile()
    entry = known(["automatic", "manual"], ["RTE-1"])
    data["axes"]["write_agency"] = entry
    if mutation == "missing":
        del entry["evidence"]["manual"]
    elif mutation == "extra":
        entry["evidence"]["invented"] = entry["evidence"]["manual"]
    elif mutation == "unknown-record":
        entry["evidence"]["manual"]["records"] = ["RTE-99"]
    elif mutation == "no-basis":
        entry["evidence"]["manual"]["basis"] = None
    elif mutation == "empty-note":
        entry["evidence"]["manual"]["note"] = ""
    else:
        del entry["evidence"]
        entry["basis"] = "afforded"
    with pytest.raises(ValueError):
        sm.validate_comparison(data, BODY)


def test_partial_negative_does_not_establish_absence():
    data = profile()
    data["axes"]["trace_learning"] = known(["no"], ["ABS-1"])
    data["axes"]["trace_learning"]["assessment"] = "partial"
    with pytest.raises(ValueError, match="partial coverage cannot establish no"):
        sm.validate_comparison(data, BODY)


def test_known_ids_replace_the_body_declarations():
    data = profile()
    data["axes"]["storage_substrate"] = known(["files"], records=["RTE-7"])
    with pytest.raises(ValueError, match="unresolved"):
        sm.validate_comparison(data, BODY)
    assert sm.validate_comparison(data, BODY, known_ids={"RTE-7"}) == data
