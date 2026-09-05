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
                "basis": None,
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
        "basis": basis,
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
