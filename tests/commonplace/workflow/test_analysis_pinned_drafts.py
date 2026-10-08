"""Closed local draft snapshots: no models, acquisition or publication."""
from pathlib import Path
from types import SimpleNamespace

import pytest

from commonplace.lib.agentic_job_validation import CRITERIA, criterion_bytes
from commonplace.lib.agentic_set import SET_TYPE
from commonplace.lib.validation import validate_draft_at_slot

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


def draft(tmp_path, pinned, candidate=CANDIDATE, **kwargs):
    return validate_draft_at_slot(
        tmp_path / "kb/agentic-system-analyses/state/fixture/set", "boundary.md", candidate,
        repo_root=tmp_path, members={}, manifest=f"type: {SET_TYPE}\n".encode(),
        criteria=pinned, **kwargs,
    )


def failures(findings):
    return [finding.render() for finding in findings if not finding.absent and not finding.info]


def test_pinned_draft_schema_differs_from_disk_and_between_runs(tmp_path):
    pinned = criteria()
    for name, data in pinned.items():
        path = tmp_path / "kb" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    (tmp_path / "kb" / BOUNDARY_SCHEMA).write_text("required: [disk_only]\n")
    assert not failures(draft(tmp_path, pinned))
    changed = {**pinned, BOUNDARY_SCHEMA: b"required: [pinned_only]\n"}
    assert any("pinned_only" in failure for failure in failures(draft(tmp_path, changed)))
    assert not failures(draft(tmp_path, pinned))


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


def test_missing_set_type_returns_findings_without_disk_fallback(tmp_path):
    pinned = criteria()
    path = tmp_path / "kb" / SET_TYPE
    path.parent.mkdir(parents=True)
    path.write_bytes(pinned.pop(SET_TYPE))
    assert any("missing pinned criterion" in failure for failure in failures(draft(tmp_path, pinned)))


@pytest.mark.parametrize("source", ["null", "{}"])
def test_non_complete_boundary_source_does_not_crash(tmp_path, source):
    candidate = CANDIDATE.replace(b"source: null", f"source: {source}".encode())
    result = failures(draft(tmp_path, criteria(), candidate))
    if source == "null":
        assert not result
    else:
        assert result  # Malformed sources still fail; they just do not crash.


def test_quotes_without_source_are_refused_not_crashes(tmp_path):
    candidate = CANDIDATE + b"\n> quoted\n> --- `README.md`\n"
    assert any("quotations need" in failure for failure in failures(draft(tmp_path, criteria(), candidate)))


def test_criterion_collection_reads_only_declared_known_aliases():
    calls = []
    data = {"boundary-type": b"pinned", "note-schema": b"schema", "unrelated": b"not a criterion"}

    def read(alias):
        calls.append(alias)
        if alias not in data:
            raise KeyError(alias)
        return data[alias]

    result = criterion_bytes(SimpleNamespace(read=read))
    assert result == {CRITERIA[alias]: data[alias] for alias in ("boundary-type", "note-schema")}
    assert set(calls) == set(CRITERIA)


def test_conflicting_criterion_aliases_are_rejected():
    def read(alias):
        if alias in ("record-verification-type", "profile-verification-type"):
            return alias.encode()
        raise KeyError(alias)

    with pytest.raises(ValueError, match="conflicting pinned criterion aliases"):
        criterion_bytes(SimpleNamespace(read=read))


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


@pytest.mark.parametrize("module,role", [
    ("agentic_job_profile", "memory-profile"),
    ("agentic_job_profile", "synthesis-verification"),
    ("agentic_job_verification", "reconciliation"),
    ("agentic_job_verification", "record-verification"),
])
def test_member_helpers_forward_declared_criteria_and_boundary_source(tmp_path, monkeypatch, module, role):
    import importlib

    handlers = importlib.import_module("commonplace.lib." + module)
    source = {"kind": "capture", "identity": "fixture", "revision": "pin", "path": str(tmp_path)}
    boundary = ("---\nsource:\n  kind: capture\n  identity: fixture\n  revision: pin\n"
                f"  path: {tmp_path}\n---\n# Boundary\n").encode()
    pinned = criteria()
    declared = {alias: pinned[path] for alias, path in CRITERIA.items() if path in pinned}
    attempt = SimpleNamespace(run_dir=tmp_path, read=lambda alias: declared[alias])
    seen = []

    def validate(*args, **kwargs):
        seen.append((args, kwargs))
        return []

    monkeypatch.setattr(handlers, "validate_draft_at_slot", validate)
    snapshot = {"boundary.md": boundary}
    if module == "agentic_job_profile":
        handlers._content(attempt, tmp_path, role, CANDIDATE, snapshot)
    else:
        monkeypatch.setattr(handlers, "frozen_source_refusals", lambda _: [])
        handlers._candidate_reasons(attempt, tmp_path, {"run-id": "fixture"}, role, CANDIDATE, snapshot)
    args, kwargs = seen[0]
    assert args[2] == CANDIDATE
    assert kwargs["members"] is snapshot
    assert kwargs["criteria"] == pinned
    assert kwargs["frozen_source"] == source


def test_boundary_handler_forwards_closed_criteria_with_null_acquisition(tmp_path, monkeypatch):
    from commonplace.lib import agentic_job_handlers as handlers

    pinned = criteria()
    declared = {alias: pinned[path] for alias, path in CRITERIA.items() if path in pinned}
    declared.update({"candidate": CANDIDATE, "source": b"null", "metadata": b"{}",
                     "incumbent-boundary": None})
    judgments = []
    attempt = SimpleNamespace(run_dir=tmp_path, read=lambda alias: declared[alias],
                              judge=lambda *args, **kwargs: judgments.append(kwargs))
    metadata = {"run-id": "fixture", "source-identity": "fixture", "capture-directory": str(tmp_path)}
    monkeypatch.setattr(handlers, "_opened_environment", lambda *args, **kwargs: (metadata, tmp_path))
    monkeypatch.setattr(handlers, "_require_opened_method", lambda *args, **kwargs: None)
    seen = []
    monkeypatch.setattr(handlers, "validate_draft_at_slot", lambda *args, **kwargs: seen.append(kwargs) or [])
    handlers.check_boundary(attempt)
    assert seen[0]["criteria"] == pinned
    assert seen[0]["frozen_source"] is None
    assert seen[0]["members"] == {}
    assert judgments[0]["outcome"] == "accepted"


def test_record_set_check_forwards_same_source_and_member_snapshot(tmp_path, monkeypatch):
    from commonplace.lib import agentic_job_verification as handlers
    from commonplace.lib.validation import CheckResults

    pinned = criteria()
    declared = {alias: pinned[path] for alias, path in CRITERIA.items() if path in pinned}
    declared["metadata"] = b"{}"
    attempt = SimpleNamespace(run_dir=tmp_path, read=lambda alias: declared[alias])
    source = {"kind": "capture", "identity": "fixture", "revision": "fixture", "path": str(tmp_path)}
    snapshot = {"boundary.md": b"pinned boundary"}
    monkeypatch.setattr(handlers, "_opened_environment", lambda *args, **kwargs: ({}, tmp_path))
    monkeypatch.setattr(handlers, "_require_opened_method", lambda *args, **kwargs: None)
    monkeypatch.setattr(handlers, "_snapshot", lambda *args: snapshot)
    monkeypatch.setattr(handlers, "_source", lambda *args: source)
    monkeypatch.setattr(handlers, "_source_reasons", lambda *args: [])
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
