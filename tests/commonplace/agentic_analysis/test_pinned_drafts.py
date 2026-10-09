"""Closed local draft snapshots: no models, acquisition or publication."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from commonplace.artifactrun.checks import criterion_bytes
from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE
from commonplace.lib.validation import validate_draft_in_role

LIBRARY = Path(__file__).resolve().parents[3] / "kb"
BOUNDARY_TYPE = "agentic-system-analyses/types/agentic-system-boundary.md"
BOUNDARY_SCHEMA = BOUNDARY_TYPE.removesuffix(".md") + ".schema.yaml"
CANDIDATE = (f"---\ntype: {BOUNDARY_TYPE}\ndescription: Fixture\n"
             "run-id: fixture\nresult-disposition: blocked\nsource: null\n---\n# Boundary\n").encode()


def criteria():
    return {
        ANALYSIS_TYPE: (LIBRARY / ANALYSIS_TYPE).read_bytes(),
        ANALYSIS_TYPE.removesuffix(".md") + ".schema.yaml": b"type: object\n",
        BOUNDARY_TYPE: (b"---\ntype: types/type-spec.md\nname: agentic-system-boundary\n"
                        b"description: Fixture\nschema: ./agentic-system-boundary.schema.yaml\n"
                        b"---\n# Boundary type\n"),
        BOUNDARY_SCHEMA: b"type: object\n",
    }


def fixed_type(**kwargs):
    """An attempt double carrying the artifact type a run fixes at start."""
    from commonplace.lib.agentic_analysis.analyses import analysis_layout

    return SimpleNamespace(type_text=(LIBRARY / ANALYSIS_TYPE).read_text(), type_spec=ANALYSIS_TYPE,
                           layout=analysis_layout(), **kwargs)


def draft(tmp_path, pinned, candidate=CANDIDATE, **kwargs):
    return validate_draft_in_role(
        tmp_path / "kb/agentic-system-analyses/state/fixture/artifact", "boundary", candidate,
        repo_root=tmp_path, members={}, manifest=f"type: {ANALYSIS_TYPE}\n".encode(),
        criteria=pinned, **kwargs,
    )


def failures(findings):
    return [finding.render() for finding in findings if not finding.absent and not finding.info]


def test_draft_missing_transitive_dependency_never_reads_disk(tmp_path):
    pinned = criteria()
    pinned[BOUNDARY_SCHEMA] = b"if: false\nthen:\n  $ref: ./middle.schema.yaml\n"
    middle = "agentic-system-analyses/types/middle.schema.yaml"
    leaf = "agentic-system-analyses/types/leaf.schema.yaml"
    pinned[middle] = b"$ref: ./leaf.schema.yaml\n"
    path = tmp_path / "kb" / leaf
    path.parent.mkdir(parents=True)
    path.write_text("type: object\n")
    assert any("missing pinned criterion" in failure and "leaf.schema.yaml" in failure
               for failure in failures(draft(tmp_path, pinned)))


@pytest.mark.parametrize("source", ["null", "{}"])
def test_non_complete_boundary_source_does_not_crash(tmp_path, source):
    candidate = CANDIDATE.replace(b"source: null", f"source: {source}".encode())
    result = failures(draft(tmp_path, criteria(), candidate))
    if source == "null":
        assert not result
    else:
        assert result  # Malformed sources still fail; they just do not crash.


def test_criteria_are_the_pinned_library_files_plus_the_fixed_artifact_type():
    files = {BOUNDARY_TYPE: b"pinned", "types/note.schema.yaml": b"schema"}
    result = criterion_bytes(fixed_type(read_files=lambda: dict(files)))
    assert result == {**files, ANALYSIS_TYPE: (LIBRARY / ANALYSIS_TYPE).read_bytes()}


def test_boundary_capture_inspection_requires_exact_source_pin(tmp_path):
    from hashlib import sha256

    import yaml

    capture = tmp_path / "capture.md"
    capture.write_bytes(b"quoted text\n")
    source = {"kind": "capture", "identity": "https://example.invalid/fixture",
              "revision": "fixture", "path": str(capture),
              "sha256": sha256(capture.read_bytes()).hexdigest()}
    candidate = CANDIDATE.replace(b"source: null", yaml.safe_dump({"source": source}).strip().encode())
    candidate += ("\n## Source register\n\n"
                  "| ID | Kind | Identity | Revision | Scope | Layer | Role | Limits |\n"
                  "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
                  "| SRC-1 | capture | https://example.invalid/fixture | fixture | all | docs | evidence | none |\n"
                  f"\n> quoted text\n> --- `{capture}`\n").encode()
    assert any("exact boundary source context" in failure
               for failure in failures(draft(tmp_path, criteria(), candidate)))
    assert not failures(draft(tmp_path, criteria(), candidate, frozen_source=source))
    wrong = {**source, "revision": "other"}
    assert any("exact boundary source context" in failure
               for failure in failures(draft(tmp_path, criteria(), candidate, frozen_source=wrong)))


def test_candidate_review_forwards_declared_criteria_snapshot_and_boundary_source(tmp_path, monkeypatch):
    from commonplace.artifactrun import checks as module

    source = {"kind": "capture", "identity": "fixture", "revision": "pin", "path": str(tmp_path)}
    boundary = ("---\nsource:\n  kind: capture\n  identity: fixture\n  revision: pin\n"
                f"  path: {tmp_path}\n---\n# Boundary\n").encode()
    pinned = criteria()
    declared = {"candidate": CANDIDATE, "boundary": boundary}
    files = {path: data for path, data in pinned.items() if path != ANALYSIS_TYPE}
    attempt = fixed_type(run_dir=tmp_path, read=lambda alias: declared[alias], read_files=lambda: dict(files))
    seen = []

    def validate(*args, **kwargs):
        seen.append((args, kwargs))
        return []

    monkeypatch.setattr(module, "validate_draft_in_role", validate)
    monkeypatch.setattr(module, "frozen_source_refusals", lambda _: [])
    check = module.candidate(attempt, "reconciliation", ("boundary",), repo=tmp_path, source_role="boundary")
    assert module.review(check) == []
    args, kwargs = seen[0]
    assert args[2] == CANDIDATE
    assert kwargs["members"] == {"boundary.md": boundary}
    assert kwargs["criteria"] == pinned
    assert kwargs["frozen_source"] == source
