"""Synthetic downstream fixtures; these are not external-system evidence."""

import csv
import json
from copy import deepcopy
from io import StringIO

from commonplace.lib import systems_matrix as sm
from scripts import analyze_matrix as stats
from scripts import build_systems_matrix as builder
from scripts import render_systems_table as renderer


def unit(scope, assessment, value=None, basis="wired", note="Bounded finding."):
    return {
        "scope": scope,
        "assessment": assessment,
        "findings": [] if value is None else [{
            "value": value, "basis": basis, "records": ["memory.md#mem-rte-update"],
            "note": "Synthetic support.",
        }],
        "records": ["memory.md#mem-rte-update"],
        "note": note,
    }


def profile_fixture():
    axes = {axis: {
        "assessment": "uninspected",
        "units": [unit("opaque part", "uninspected", note="Store not inspected.")],
        "records": [], "note": "No controlled classification.",
    } for axis in sm.AXES}
    axes["write_agency"] = {
        "assessment": "partial",
        "units": [
            unit("curator", "known", "automatic"),
            unit("alternate API", "known", "automatic", "afforded"),
            unit("initial sheet", "not-determinable", note="Caller identity unknown; manual control not established."),
        ],
        "records": ["memory.md#mem-rte-update"], "note": "Initial control unresolved.",
    }
    return {"version": 2, "scope": "synthetic memory", "axes": axes}


def row(profile=None):
    profile = profile if profile is not None else profile_fixture()
    sm.validate_comparison(profile, known_ids=dict.fromkeys(("MEM-RTE-update", "MEM-ABS-static"), "memory.md"))
    result = {key: "synthetic" for key in sm.METADATA}
    result.update(sm.project_comparison(profile))
    result.update(source_tier="code-grounded", system_name="Synthetic",
                  comparison_scope=profile["scope"], review_file="kb/example/overview.md",
                  artifact_file="kb/example/ARTIFACT.yaml")
    return result


def test_builder_exports_units_and_projection(tmp_path, monkeypatch):
    rows = [row()]
    monkeypatch.setattr(builder, "load_results", lambda *_: sm.MatrixInputs(rows, {}))
    output = tmp_path / "matrix.csv"
    assert builder.main(["--output", str(output)]) == 0
    [exported] = list(csv.DictReader(StringIO(output.read_text())))
    assert exported["comparison_version"] == "2"
    assert json.loads(exported["write_agency_units"]) == rows[0]["write_agency_units"]
    assert json.loads(exported["write_agency"]) == ["automatic"]
    assert exported["write_agency_assessment"] == "partial"
    assert exported["write_agency_note"] == "Initial control unresolved."
    assert json.loads(exported["write_agency_evidence"])["automatic"]["basis"] == "wired"
    assert exported["write_agency_records"] == "MEM-RTE-update"


def test_table_keeps_local_weakness_and_uncertainty(tmp_path):
    text = renderer.render([row()], tmp_path / "table.md")
    assert "Write agency" in text
    assert "curator: known — automatic [wired]" in text
    assert "alternate API: known — automatic [afforded]" in text
    assert "initial sheet: not-determinable" in text
    assert "Caller identity unknown; manual control not established." in text
    assert "Store not inspected." in text
    assert "Initial control unresolved." in text


def test_empty_unresolved_inventory_keeps_axis_limitation_in_table_and_csv(tmp_path):
    profile = profile_fixture()
    profile["axes"]["storage_substrate"].update(
        units=[], note="Provider inventory unavailable; complete storage classification prevented.",
    )
    revised = row(profile=profile)
    text = renderer.render([revised], tmp_path / "table.md")
    assert "uninspected coverage (Provider inventory unavailable; complete storage classification prevented.)" in text
    exported = next(csv.DictReader(StringIO(sm.csv_text(sm.MatrixInputs([revised], {})))))
    assert exported["storage_substrate_note"] == profile["axes"]["storage_substrate"]["note"]


def test_statistics_keep_partial_positive(monkeypatch, capsys):
    rows = [row(), row()]
    rows[1]["source_tier"] = "doc-grounded"
    monkeypatch.setattr(stats, "load_results", lambda *_: sm.MatrixInputs(rows, {}))
    assert stats.main([]) == 0
    text = capsys.readouterr().out
    assert "doc-grounded excluded from statistics: 1" in text
    assert "supported write_agency: {'automatic': 1} / 1" in text
    assert "finding bases: {'known:afforded': 1, 'known:wired': 1}" in text
    assert "complete write_agency: 0 of 1" in text
    assert "complete storage_substrate: 0 of 1" in text
    assert "remainder is not absence" in text


def test_complete_statistics_do_not_upgrade_weak_duplicate_witness(monkeypatch, capsys):
    profile = deepcopy(profile_fixture())
    profile["axes"]["write_agency"]["assessment"] = "known"
    profile["axes"]["write_agency"]["units"] = profile["axes"]["write_agency"]["units"][:2]
    profile["axes"]["storage_substrate"].update(
        assessment="absent", units=[], records=["memory.md#mem-abs-static"],
        note="Bounded evidenced absence of retained storage.",
    )
    absent = row(profile=profile)
    monkeypatch.setattr(stats, "load_results", lambda *_: sm.MatrixInputs([absent], {}))
    assert stats.main([]) == 0
    text = capsys.readouterr().out
    assert "supported write_agency: {'automatic': 1}" in text
    assert "complete write_agency: 0 of 1" in text
    assert "complete storage_substrate: 1 of 1" in text
    assert "profiles: {'none': 1}" in text


def test_partial_trace_positive_keeps_local_no_without_aggregate_negative(tmp_path):
    profile = profile_fixture()
    negative = unit("static branch", "known", "no")
    negative["findings"][0]["records"] = ["memory.md#mem-abs-static"]
    negative["records"] = ["memory.md#mem-abs-static"]
    units = [unit("update", "known", "yes"), negative,
             unit("opaque branch", "uninspected")]
    profile["axes"]["trace_learning"] = {
        "assessment": "partial", "units": units, "records": ["memory.md#mem-rte-update"],
        "note": "Opaque branch prevents complete trace inventory.",
    }
    revised = row(profile=profile)
    assert revised["trace_learning"] == ["yes"]
    text = renderer.render([revised], tmp_path / "table.md")
    assert "update: known — yes [wired]" in text
    assert "static branch: known — no [wired]" in text
    assert "opaque branch: uninspected" in text
    assert sm.complete_values(revised, "trace_learning") is None
