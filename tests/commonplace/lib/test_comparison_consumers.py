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
            "value": value, "basis": basis, "records": ["MEM-RTE-update"],
            "note": "Synthetic support.",
        }],
        "records": ["MEM-RTE-update"],
        "note": note,
    }


def profile_fixture(version=2):
    if version == 2:
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
            "records": ["MEM-RTE-update"], "note": "Initial control unresolved.",
        }
        profile = {"version": 2, "scope": "synthetic memory", "axes": axes}
    else:
        axes = {axis: {
            "assessment": "uninspected", "values": [], "evidence": {},
            "records": [], "note": "Not inspected.",
        } for axis in sm.AXES}
        axes["write_agency"] = {
            "assessment": "known", "values": ["manual"],
            "evidence": {"manual": {"basis": "wired", "records": ["MEM-RTE-update"], "note": "Original caller-based meaning."}},
            "records": ["MEM-RTE-update"], "note": "Original semantics.",
        }
        profile = {"scope": "synthetic memory", "axes": axes}
    return profile


def row(version=2, profile=None):
    profile = profile if profile is not None else profile_fixture(version)
    sm.validate_comparison(profile, known_ids={"MEM-RTE-update", "MEM-ABS-static"})
    result = {key: "synthetic" for key in sm.METADATA}
    result.update(sm.project_comparison(profile))
    result.update(source_tier="code-grounded", system_name=f"Synthetic v{version}",
                  comparison_scope=profile["scope"], review_file="kb/example/overview.md",
                  artifact_file="kb/example/ARTIFACT.yaml")
    return result


def test_builder_exports_units_revision_and_compatibility_projection(tmp_path, monkeypatch):
    rows = [row(1), row(2)]
    monkeypatch.setattr(builder, "load_results", lambda *_: sm.MatrixInputs(rows, {}))
    output = tmp_path / "matrix.csv"
    assert builder.main(["--output", str(output)]) == 0
    exported = list(csv.DictReader(StringIO(output.read_text())))
    assert [r["comparison_version"] for r in exported] == ["1", "2"]
    assert json.loads(exported[0]["write_agency_units"]) == []
    assert json.loads(exported[1]["write_agency_units"]) == rows[1]["write_agency_units"]
    assert json.loads(exported[1]["write_agency"]) == ["automatic"]
    assert exported[1]["write_agency_assessment"] == "partial"
    assert exported[1]["write_agency_note"] == "Initial control unresolved."
    assert exported[0]["write_agency_note"] == "Original semantics."
    assert json.loads(exported[1]["write_agency_evidence"])["automatic"]["basis"] == "wired"
    assert exported[1]["write_agency_records"] == "MEM-RTE-update"


def test_table_keeps_local_weakness_and_uncertainty(tmp_path):
    text = renderer.render([row(1), row(2)], tmp_path / "table.md")
    assert "Profile revision" in text
    assert "Write agency" in text
    assert "curator: known — automatic [wired]" in text
    assert "alternate API: known — automatic [afforded]" in text
    assert "initial sheet: not-determinable" in text
    assert "Caller identity unknown; manual control not established." in text
    assert "manual [wired]" in text  # Original v1 value, not reclassified.
    assert "Store not inspected." in text
    assert "Initial control unresolved." in text
    assert "Original semantics." in text


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
    legacy = profile_fixture(1)
    legacy["axes"]["storage_substrate"]["note"] = "Legacy storage scope unresolved."
    assert "uninspected (Legacy storage scope unresolved.)" in renderer.render(
        [row(1, profile=legacy)], tmp_path / "legacy.md",
    )


def test_statistics_stratify_revisions_and_keep_partial_positive(monkeypatch, capsys):
    rows = [row(1), row(2), row(2)]
    rows[2]["source_tier"] = "doc-grounded"
    monkeypatch.setattr(stats, "load_results", lambda *_: sm.MatrixInputs(rows, {}))
    assert stats.main([]) == 0
    text = capsys.readouterr().out
    assert "doc-grounded excluded from statistics: 1" in text
    legacy, revised = text.split("comparison version 2:")
    assert "comparison version 1: 1 code-grounded rows" in legacy
    assert "supported write_agency: {'manual': 1} / 1" in legacy
    assert "supported write_agency: {'automatic': 1} / 1" in revised
    assert "finding bases: {'known:afforded': 1, 'known:wired': 1}" in revised
    assert "complete write_agency: 0 of 1" in revised
    assert "complete storage_substrate: 0 of 1" in revised
    assert "remainder is not absence" in revised


def test_complete_statistics_do_not_upgrade_weak_duplicate_witness(monkeypatch, capsys):
    profile = deepcopy(profile_fixture())
    profile["axes"]["write_agency"]["assessment"] = "known"
    profile["axes"]["write_agency"]["units"] = profile["axes"]["write_agency"]["units"][:2]
    profile["axes"]["storage_substrate"].update(
        assessment="absent", units=[], records=["MEM-ABS-static"],
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
    negative["findings"][0]["records"] = ["MEM-ABS-static"]
    negative["records"] = ["MEM-ABS-static"]
    units = [unit("update", "known", "yes"), negative,
             unit("opaque branch", "uninspected")]
    profile["axes"]["trace_learning"] = {
        "assessment": "partial", "units": units, "records": ["MEM-RTE-update"],
        "note": "Opaque branch prevents complete trace inventory.",
    }
    revised = row(profile=profile)
    assert revised["trace_learning"] == ["yes"]
    text = renderer.render([revised], tmp_path / "table.md")
    assert "update: known — yes [wired]" in text
    assert "static branch: known — no [wired]" in text
    assert "opaque branch: uninspected" in text
    assert sm.complete_values(revised, "trace_learning") is None
