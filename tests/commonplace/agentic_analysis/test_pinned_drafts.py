"""Closed local draft snapshots: no models, acquisition or publication."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from commonplace.lib.agentic_analysis.sets import SET_TYPE
from commonplace.lib.validation import validate_draft_at_slot
from commonplace.setrun.checks import criterion_bytes

LIBRARY = Path(__file__).resolve().parents[3] / "kb"
BOUNDARY_TYPE = "agentic-system-analyses/types/agentic-system-boundary.md"
BOUNDARY_SCHEMA = BOUNDARY_TYPE.removesuffix(".md") + ".schema.yaml"
CANDIDATE = (f"---\ntype: {BOUNDARY_TYPE}\ndescription: Fixture\n"
             "run-id: fixture\nresult-disposition: blocked\nsource: null\n---\n# Boundary\n").encode()


def criteria():
    return {
        SET_TYPE: (LIBRARY / SET_TYPE).read_bytes(),
        SET_TYPE.removesuffix(".md") + ".schema.yaml": b"type: object\n",
        BOUNDARY_TYPE: (b"---\ntype: types/type-spec.md\nname: agentic-system-boundary\n"
                        b"description: Fixture\nschema: ./agentic-system-boundary.schema.yaml\n"
                        b"---\n# Boundary type\n"),
        BOUNDARY_SCHEMA: b"type: object\n",
    }


def fixed_type(**kwargs):
    """An attempt double carrying the set type a run fixes at start."""
    from commonplace.lib.agentic_analysis.sets import analysis_layout

    return SimpleNamespace(type_text=(LIBRARY / SET_TYPE).read_text(), type_spec=SET_TYPE,
                           layout=analysis_layout(), **kwargs)


def draft(tmp_path, pinned, candidate=CANDIDATE, **kwargs):
    return validate_draft_at_slot(
        tmp_path / "kb/agentic-system-analyses/state/fixture/set", "boundary.md", candidate,
        repo_root=tmp_path, members={}, manifest=f"type: {SET_TYPE}\n".encode(),
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


def test_criteria_are_the_pinned_library_files_plus_the_fixed_set_type():
    files = {BOUNDARY_TYPE: b"pinned", "types/note.schema.yaml": b"schema"}
    result = criterion_bytes(fixed_type(read_files=lambda: dict(files)))
    assert result == {**files, SET_TYPE: (LIBRARY / SET_TYPE).read_bytes()}


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
    from commonplace.setrun import checks as module

    source = {"kind": "capture", "identity": "fixture", "revision": "pin", "path": str(tmp_path)}
    boundary = ("---\nsource:\n  kind: capture\n  identity: fixture\n  revision: pin\n"
                f"  path: {tmp_path}\n---\n# Boundary\n").encode()
    pinned = criteria()
    declared = {"candidate": CANDIDATE, "boundary": boundary}
    files = {path: data for path, data in pinned.items() if path != SET_TYPE}
    attempt = fixed_type(run_dir=tmp_path, read=lambda alias: declared[alias], read_files=lambda: dict(files))
    seen = []

    def validate(*args, **kwargs):
        seen.append((args, kwargs))
        return []

    monkeypatch.setattr(module, "checkout", lambda _: tmp_path)
    monkeypatch.setattr(module, "validate_draft_at_slot", validate)
    monkeypatch.setattr(module, "frozen_source_refusals", lambda _: [])
    check = module.candidate(attempt, "reconciliation", ("boundary",), source_role="boundary")
    assert module.review(check) == []
    args, kwargs = seen[0]
    assert args[2] == CANDIDATE
    assert kwargs["members"] == {"boundary.md": boundary}
    assert kwargs["criteria"] == pinned
    assert kwargs["frozen_source"] == source


def test_boundary_handler_forwards_closed_criteria_with_null_acquisition(tmp_path, monkeypatch):
    from commonplace.lib.agentic_analysis import handlers
    from commonplace.setrun import checks as candidate

    pinned = criteria()
    declared = {}
    files = {path: data for path, data in pinned.items() if path != SET_TYPE}
    declared.update({"candidate": CANDIDATE, "source": b"null", "metadata": b"{}",
                     "incumbent-boundary": None, "answered-refusal": None})
    judgments = []
    attempt = fixed_type(run_dir=tmp_path, read=lambda alias: declared[alias], read_files=lambda: dict(files),
                         relations=(), judge=lambda *args, **kwargs: judgments.append(kwargs))
    metadata = {"run-id": "fixture", "source-identity": "fixture", "capture-directory": str(tmp_path)}
    monkeypatch.setattr(handlers, "_locate", lambda *args, **kwargs: (metadata, tmp_path))
    monkeypatch.setattr(candidate, "checkout", lambda _: tmp_path)
    seen = []
    monkeypatch.setattr(candidate, "validate_draft_at_slot", lambda *args, **kwargs: seen.append(kwargs) or [])
    handlers.check_boundary(attempt)
    assert seen[0]["criteria"] == pinned
    assert seen[0]["frozen_source"] is None
    assert seen[0]["members"] == {}
    assert judgments[0]["outcome"] == "accepted"


def test_record_set_check_forwards_same_source_and_member_snapshot(tmp_path, monkeypatch):
    from commonplace.lib.agentic_analysis import verification as handlers
    from commonplace.lib.validation import CheckResults

    pinned = criteria()
    declared = {}
    files = {path: data for path, data in pinned.items() if path != SET_TYPE}
    attempt = fixed_type(run_dir=tmp_path, read=lambda alias: declared[alias], read_files=lambda: dict(files))
    source = {"kind": "capture", "identity": "fixture", "revision": "fixture", "path": str(tmp_path)}
    snapshot = {"boundary.md": b"pinned boundary"}
    monkeypatch.setattr(handlers, "checkout", lambda _: tmp_path)
    monkeypatch.setattr(handlers, "snapshot", lambda *args: snapshot)
    monkeypatch.setattr(handlers, "frozen_source", lambda *args: source)
    monkeypatch.setattr(handlers, "frozen_source_refusals", lambda _: [])
    seen = []

    def run(*args, **kwargs):
        seen.append(kwargs)
        return SimpleNamespace(validate=lambda _: CheckResults("fixture"), artifact_findings=lambda _: [])

    monkeypatch.setattr(handlers, "ValidationRun", run)
    assert handlers.set_check(attempt)["findings"].endswith(b"none\n")
    kwargs = seen[0]
    assert kwargs["frozen_source"] is source
    assert next(iter(kwargs["member_snapshots"].values())) is snapshot
    assert {path.relative_to(tmp_path / "kb").as_posix(): data
            for path, data in kwargs["criteria"].contents.items()} == pinned
