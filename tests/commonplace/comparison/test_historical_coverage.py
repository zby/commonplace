"""Exact-byte historical coverage compatibility must not become a writer bypass."""
from copy import deepcopy
from hashlib import sha256
from types import SimpleNamespace

import pytest
import yaml

from commonplace.lib import systems_matrix as sm
from commonplace.lib import validation
from commonplace.lib.agentic_analysis import analyses
from tests.commonplace.agentic_analysis.fixtures import (
    REPO_ROOT,
    frontmatter,
    member_fixture,
    repin,
    replace_frontmatter,
    uninspected_profile,
)
from tests.commonplace.platforms import analysis_linux_only

ABSENCE = "runtime.md#rt-abs-static-branch"
STORE = "runtime.md#rt-obj-store"
BODIES = {"runtime.md": (
    "## Shared records\n\n### Operative objects\n\n"
    "#### RT-OBJ-store\n\nLabel: Store\n\n"
    "### Evidenced absences\n\n#### RT-ABS-static-branch\n\nLabel: Static branch\n"
)}
KNOWN = {"RT-OBJ-store": "runtime.md", "RT-ABS-static-branch": "runtime.md"}
PINNED = {
    "mohammadmaso--echowiki": "0712abad6df9c56751dcef17d50008ee46962eb0e40bac836df5b5a2178ed32a",
    "shilren--interview-doc-agent": "a5a82049e2fcb5538700295acfc63d41285cd37717879ade977b99c7c9ef434d",
}


def historical_profile(assessment="not-determinable"):
    data = uninspected_profile("Synthetic static branch and opaque writer")
    data["axes"]["trace_learning"] = {
        "assessment": assessment, "records": [ABSENCE, STORE],
        "note": "Historical aggregate; only the static branch was classified.",
        "units": [
            {"scope": "Static branch", "assessment": "known", "records": [ABSENCE],
             "note": "Bounded absence covers only this branch.",
             "findings": [{"value": "no", "basis": "wired", "records": [ABSENCE],
                           "note": "No trace-fed write in the inspected branch."}]},
            {"scope": "Opaque writer", "assessment": "not-determinable", "records": [STORE],
             "note": "Writer inaccessible; completeness prevented.", "findings": []},
        ],
    }
    return {
        "type": "agentic-system-analyses/types/agentic-system-memory-profile.md",
        "description": "Synthetic historical coverage fixture",
        "memory-comparison": data,
    }


def encoded(metadata):
    return ("---\n" + yaml.safe_dump(metadata, sort_keys=False)
            + "---\n\n# Synthetic memory profile\n\n## Comparison rationale\n\n"
            "The opaque writer remains unresolved.\n").encode()


def pin(monkeypatch, content):
    monkeypatch.setattr(sm, "_HISTORICAL_COVERAGE_PROFILES", {sha256(content).hexdigest()})


def read_profile(metadata, content=None, bodies=None):
    return sm.profile_member_comparison(
        metadata, record_bodies=BODIES if bodies is None else bodies,
        retained_content=content,
    )


def test_real_allowlist_pins_exact_unchanged_publications():
    assert set(sm._HISTORICAL_COVERAGE_PROFILES) == set(PINNED.values())
    for name, expected in PINNED.items():
        path = REPO_ROOT / analyses.RETAINED_ROOT / name / "memory-profile.md"
        assert sha256(path.read_bytes()).hexdigest() == expected


@pytest.mark.parametrize("assessment", ["uninspected", "not-determinable"])
def test_native_validation_and_unpinned_member_remain_strict(assessment):
    metadata = historical_profile(assessment)
    with pytest.raises(ValueError, match="empty.*findings"):
        sm.validate_comparison(metadata["memory-comparison"], known_ids=KNOWN)
    with pytest.raises(ValueError, match="empty.*findings"):
        read_profile(metadata, encoded(metadata))


def test_exact_pinned_bytes_preserve_historical_aggregate_and_local_negative(monkeypatch):
    metadata = historical_profile()
    content = encoded(metadata)
    pin(monkeypatch, content)
    before = deepcopy(metadata)
    data = read_profile(metadata, content)
    assert data == before["memory-comparison"]
    row = sm.project_comparison(data) | {"source_tier": "code-grounded"}
    assert row["trace_learning_assessment"] == "not-determinable"
    assert row["trace_learning"] == []
    assert row["trace_learning_units"] == data["axes"]["trace_learning"]["units"]
    assert row["trace_learning_units"][0]["findings"][0]["value"] == "no"
    assert sm.complete_values(row, "trace_learning") is None
    assert sm.supported_values(row, "trace_learning") == set()
    assert metadata == before


@pytest.mark.parametrize("defect", ["no-raw", "body-tamper", "frontmatter-tamper", "metadata-mismatch", "other-metadata-mismatch"])
def test_historical_permission_requires_exact_bytes_and_matching_metadata(monkeypatch, defect):
    metadata = historical_profile()
    content = encoded(metadata)
    pin(monkeypatch, content)
    if defect == "no-raw":
        content = None
    elif defect == "body-tamper":
        content += b"\nChanged body.\n"
    elif defect == "frontmatter-tamper":
        content = content.replace(b"Synthetic static branch", b"Edited static branch")
    elif defect == "metadata-mismatch":
        metadata["memory-comparison"]["scope"] = "Different parsed metadata"
    else:
        metadata["description"] = "Different non-comparison metadata"
    with pytest.raises(ValueError):
        read_profile(metadata, content)


@pytest.mark.parametrize("defect", ["vocabulary", "unresolved-record", "absence-warrant"])
def test_pinned_bytes_do_not_bypass_other_guards(monkeypatch, defect):
    metadata = historical_profile()
    finding = metadata["memory-comparison"]["axes"]["trace_learning"]["units"][0]["findings"][0]
    if defect == "vocabulary":
        finding["value"] = "invented"
    elif defect == "unresolved-record":
        finding["records"] = ["runtime.md#rt-abs-missing"]
    else:
        finding["records"] = [STORE]
    content = encoded(metadata)
    pin(monkeypatch, content)
    with pytest.raises(ValueError):
        read_profile(metadata, content)


def test_matrix_reader_passes_retained_bytes_without_reclassifying(tmp_path, monkeypatch):
    metadata = historical_profile()
    content = encoded(metadata)
    pin(monkeypatch, content)
    overview = SimpleNamespace(
        path=tmp_path / analyses.RETAINED_ROOT / "fixture/overview.md",
        name="overview.md", body="", content=b"overview", sha256=sha256(b"overview").hexdigest(),
        frontmatter={"system": "Synthetic", "run-id": "fixture", "reviewed-boundary": "fixture",
                     "analysis-cutoff": "2026-10-05", "evidence-tier": "code-grounded",
                     "boundary-kind": "runtime", "description": "Fixture only"},
    )
    profile = SimpleNamespace(name="memory-profile.md", body="", content=content,
                              sha256=sha256(content).hexdigest(), frontmatter=metadata)
    memory = SimpleNamespace(name="memory.md", body="", content=b"memory", sha256="memory-digest",
                             frontmatter={"source-identity": "synthetic"})
    runtime = SimpleNamespace(name="runtime.md", body=BODIES["runtime.md"])
    analysis = SimpleNamespace(
        overview=overview, memory=memory, memory_profile=profile,
        artifact=SimpleNamespace(path=overview.path.parent, content=b"manifest"),
        documents=[overview, memory, profile],
        roles={"overview": overview, "memory": memory, "memory-profile": profile, "runtime": runtime},
    )
    monkeypatch.setattr(sm, "current_analyses", lambda root, run: [analysis])
    row, = sm.load_results(tmp_path).rows
    assert row["trace_learning_assessment"] == "not-determinable"
    assert row["trace_learning"] == []
    assert row["trace_learning_units"] == metadata["memory-comparison"]["axes"]["trace_learning"]["units"]


@pytest.mark.usefixtures("tmp_library")
@pytest.mark.parametrize("retained", [False, pytest.param(True, marks=analysis_linux_only)])
def test_working_or_draft_artifact_cannot_borrow_retained_byte_permission(tmp_path, monkeypatch, retained):
    directory = member_fixture(tmp_path) / "artifact"
    if retained:
        slug = analyses.publication_slug(frontmatter(directory / "memory.md")["source-identity"],
                                frontmatter(directory / "overview.md")["system"])
        destination = tmp_path / analyses.RETAINED_ROOT / slug
        destination.parent.mkdir(parents=True)
        directory.rename(destination)
        directory = destination
    runtime = directory / "runtime.md"
    runtime.write_text(runtime.read_text().replace(
        "none found within the fixture boundary.",
        "#### RT-ABS-static-branch\n\nLabel: Static branch\n\nBounded absence at SRC-1.",
    ))
    path = directory / "memory-profile.md"
    metadata = frontmatter(path)
    metadata["memory-comparison"] = historical_profile()["memory-comparison"]
    replace_frontmatter(path, metadata)
    content = path.read_bytes()
    pin(monkeypatch, content)
    repin(directory)
    # Published reads may preserve exact bytes; working directories cannot.
    checked = validation.validate_note(directory, repo_root=tmp_path)
    coverage_errors = [error for error in checked.fails if "empty" in error and "findings" in error]
    assert bool(coverage_errors) is not retained, checked.fails
    # Role-draft validation strips manifest pins, even for an existing retained
    # artifact. Exact old bytes must not authorize a newly submitted candidate.
    findings = validation.validate_draft_in_role(directory, "memory-profile", content, repo_root=tmp_path)
    assert any("empty" in finding.message and "findings" in finding.message
               for finding in findings if not finding.info and not finding.warn)
