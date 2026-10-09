"""Narrow scripted consumers/effect tests, not a pipeline or analytical run.

No model hand-outs are executed. Most consumer plumbing uses scripted validation;
a narrow non-complete snapshot also exercises the real bounded adapter.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import RunStatus, Stop, UncertainEffectError, effects
from commonplace.artifactrun.report import engine_run_report
from commonplace.artifactrun.run import _parse_type
from commonplace.artifactrun.store import RunStore
from commonplace.lib.agentic_analysis import publication
from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE

ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-10-07-example-0123456789ab-01"


def doc(fields, body=""):
    return ("---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body).encode()

WORKER = {"profile": "fixture", "harness": "fixture", "launch-model": "fixture/model", "effort": "high"}


class Attempt:
    """A restricted pinned-input fixture: no hidden run/store introspection."""
    def __init__(self, tmp_path, disposition="blocked", *, overview=False):
        self.run_dir = tmp_path / RUN_ID
        self.run_dir.mkdir(parents=True)
        self.library = tmp_path / "kb"
        # The artifact type a run fixes at start, as CodeAttempt exposes it.
        self.type_text = (ROOT / "kb" / ANALYSIS_TYPE).read_text()
        self.type_spec = ANALYSIS_TYPE
        layout, relations = _parse_type(self.type_text, ANALYSIS_TYPE)
        self.layout, self.relations = layout, tuple(relations)
        self.inputs = {}
        self.files = {}
        boundary_fields = {"run-id": RUN_ID, "result-disposition": disposition,
                           "target-class": None, "boundary-kind": None, "reviewed-boundary": None,
                           "analysis-cutoff": None, "evidence-tier": None}
        present = {"boundary"}
        if disposition == "complete":
            present |= set(publication.PRODUCERS)
        if overview:
            present.add("overview")
        for role in layout.roles:
            if role == "overview" and not overview:
                continue
            data = doc({"type": layout.roles[role].type, **boundary_fields,
                        "description": "Fixture description"}) if role in present else None
            self.inputs[role] = data
            if role != "overview":
                producer, primary = publication.PRODUCERS[role]
                self.inputs[f"{role}-attempt"] = (json.dumps({
                    "job": producer, "state": "completed", "kind": "model", "model": "fixture/model",
                    "effort": "high", "worker_effort": "high", "worker_model": "fixture-model-1", "outputs": {primary: publication._digest(data)},
                }).encode() if data else None)
        self.metadata = {"run-id": RUN_ID, "system": "Example", "run-date": "2026-10-07",
                         "inputs-commit": "a" * 40, "source-identity": "https://example.invalid/example",
                         "review-path": "kb/agentic-system-analyses/retained/example/overview.md",
                         "expected-incumbent-sha256": "absent", "worker": WORKER}
        self.judgments = []

    def read(self, name):
        return self.inputs[name]  # Undeclared means error, never disk fallback.

    def read_files(self):
        return dict(self.files)  # Pinned criteria by library path; none means none.

    def judge(self, subject, **kwargs):
        self.judgments.append((subject, kwargs))


@pytest.fixture
def scripted(monkeypatch):
    checked = []
    monkeypatch.setattr(publication, "_environment", lambda attempt, boundary, **kw: (attempt.metadata, attempt.run_dir.parent))
    monkeypatch.setattr(publication, "_require_opened_method", lambda *args, **kw: None)
    monkeypatch.setattr(publication, "validate_pinned_artifact", lambda *args, **kw: checked.append(kw))
    return checked


def pinned_criteria(attempt):
    """Shipped layout with minimal schemas, like pinned_validation_contracts.

    This isolates the adapter, not the substantive shipped analysis criteria.
    All type/schema bytes still travel as pinned files keyed by library path.
    """
    types = "agentic-system-analyses/types/"
    for path in ("agentic-system-analyses/COLLECTION.md", "reference/validation-contract.md"):
        attempt.files[path] = b"# Fixture contract\n"
    attempt.files[types + "agentic-system-analysis-set.schema.yaml"] = b"type: object\n"
    for spec, name in (("types/type-spec.md", "type-spec"),
                       (types + "agentic-system-boundary.md", "agentic-system-boundary"),
                       (types + "agentic-system-analysis-overview.md", "agentic-system-analysis-overview")):
        attempt.files[spec] = (f"---\ntype: types/type-spec.md\nname: {name}\n"
                               f"description: Pinned fixture\nschema: ./{name}.schema.yaml\n---\n# Fixture\n").encode()
        attempt.files[spec.removesuffix(".md") + ".schema.yaml"] = b"type: object\n"


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope", "complete"])
def test_assembly_returns_pinned_manifest_and_scoped_overview(tmp_path, scripted, disposition):
    attempt = Attempt(tmp_path, disposition)
    # Garbage mutable projections cannot become analytical input.
    (attempt.run_dir / "artifact").mkdir()
    (attempt.run_dir / "artifact" / "memory.md").write_bytes(b"untracked garbage")
    outputs = publication.assemble_analysis(attempt)
    manifest = yaml.safe_load(outputs["manifest"])
    assert manifest["worker"] == {**WORKER, "model": "fixture-model-1"}
    assert manifest["members"]["overview.md"] == {"sha256": publication._digest(outputs["overview"])}
    assert set(manifest["members"]) == set(scripted[0]["members"])
    assert b"untracked garbage" not in outputs["overview"]
    assert attempt.judgments[0][0] == "overview"
    assert "overview:identity:boundary" in attempt.judgments[0][1]["scope"]


# Membership, acceptance and coverage now gate assembly through the engine's
# coverage input; the engine scenario tests pin that it waits, not fails.
@pytest.mark.parametrize("defect,reason", [
    ("provenance", "provenance"), ("mixed-worker", "not the run profile's"),
    ("mixed-report", "every worker must report the same model"),
    ("wrong-effort", "reported worker effort"),
    ("missing-effort", "reported worker effort"),
])
def test_assembly_rejects_misattributed_complete_artifact(tmp_path, scripted, defect, reason):
    attempt = Attempt(tmp_path, "complete")
    record = json.loads(attempt.inputs["memory-attempt"])
    if defect == "mixed-worker":
        record["model"] = "other/model"
    elif defect == "mixed-report":
        record["worker_model"] = "fixture-model-2"
    elif defect == "wrong-effort":
        record["worker_effort"] = "low"
    elif defect == "missing-effort":
        record.pop("worker_effort")
    else:
        record["outputs"] = {"answers": publication._digest(attempt.inputs["memory"])}
    attempt.inputs["memory-attempt"] = json.dumps(record).encode()
    with pytest.raises(ValueError, match=reason):
        publication.assemble_analysis(attempt)
    assert not scripted and not attempt.judgments


@pytest.mark.parametrize("defect,reason", [
    ("missing-criteria", "missing pinned criterion"), ("content", "missing-fixture-field"),
])
def test_validation_failure_prevents_overview_acceptance(tmp_path, monkeypatch, defect, reason):
    attempt = Attempt(tmp_path / "kb/agentic-system-analyses/state")
    if defect == "content":
        pinned_criteria(attempt)
        attempt.files["agentic-system-analyses/types/agentic-system-boundary.schema.yaml"] = (
            b"required: [missing-fixture-field]\n")
    monkeypatch.setattr(publication, "_environment", lambda *args, **kw: (attempt.metadata, tmp_path))
    with pytest.raises(ValueError, match=reason):
        publication.assemble_analysis(attempt)
    assert not attempt.judgments
    assert not (attempt.run_dir / "artifact" / "overview.md").exists()


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_real_bounded_adapter_assembly_and_local_publication(tmp_path, monkeypatch, disposition):
    attempt = Attempt(tmp_path / "kb/agentic-system-analyses/state", disposition)
    pinned_criteria(attempt)
    monkeypatch.setattr(publication, "_environment", lambda *args, **kw: (attempt.metadata, tmp_path))
    monkeypatch.setattr(publication, "_require_opened_method", lambda *args, **kw: None)
    outputs = publication.assemble_analysis(attempt)
    attempt.inputs.update(outputs)
    monkeypatch.setattr(publication, "install_tree", lambda **kw: pytest.fail("must remain local"))
    assert json.loads(publication.publish_analysis(attempt)["receipt"]) == {"published": False}
    assert not (tmp_path / "kb/agentic-system-analyses/retained").exists()
    assert not (attempt.run_dir / "output").exists()
    assert not (attempt.run_dir / "run-state.md").exists()

    # Re-pin an identity-inconsistent overview: hashes alone are not validation.
    members = {"boundary.md": attempt.inputs["boundary"],
               "overview.md": outputs["overview"].replace(RUN_ID.encode(), b"changed-run")}
    manifest = yaml.safe_dump({"type": ANALYSIS_TYPE, "members": {
        name: {"sha256": publication._digest(data)} for name, data in members.items()
    }}).encode()
    with pytest.raises(ValueError, match="identity field run-id"):
        publication.validate_pinned_artifact(attempt, repo=tmp_path, members=members, manifest=manifest)


def assembled_publish_attempt(tmp_path, scripted, disposition="complete"):
    assembly = Attempt(tmp_path / "assemble", disposition)
    outputs = publication.assemble_analysis(assembly)
    publish = Attempt(tmp_path / "publish", disposition, overview=True)
    publish.inputs["overview"] = outputs["overview"]
    publish.inputs["manifest"] = outputs["manifest"]
    return publish


def test_publish_rejects_manifest_not_matching_pinned_members(tmp_path, scripted):
    attempt = assembled_publish_attempt(tmp_path, scripted)
    attempt.inputs["manifest"] = b"type: wrong\n"
    with pytest.raises(ValueError, match="manifest does not pin"):
        publication.publish_analysis(attempt)


def test_engine_report_is_uncertain_without_recovery(tmp_path):
    store = RunStore(tmp_path / "engine-run")
    type_text = (ROOT / "kb" / ANALYSIS_TYPE).read_text()
    store.create({"type": type_text, "type_spec": ANALYSIS_TYPE, "plan": "fixture-plan.yaml", "library": str(ROOT / "kb"),
                  "declaration": yaml.safe_dump({"type_spec": ANALYSIS_TYPE, "jobs": [
                      {"name": "publish", "kind": "code", "handler": "unused.handler", "inputs": {}, "outputs": []}]}),
                  "parameters": {"system": "fixture"}})
    store.fail_attempt({"id": "000001-publish", "seq": 1, "job": "publish", "kind": "code", "pins": {}},
                       "scripted uncertain publication", uncertain=True)
    (store.run_dir / "effects").mkdir()
    (store.run_dir / publication.JOURNAL).write_text('{"state": "completed"}')
    status = RunStatus((), (), (Stop("uncertain effect", "publish", "000001-publish", True),), False)
    report = engine_run_report(store.run_dir, final_job="publish", status=status)
    assert report["state"] == "uncertain"
    assert report["effects"]["publish"] == {"journal-state": "completed", "verified": False}
    assert report["failed-attempts"][0]["uncertain"]
    assert report["invocation-stops"][0]["uncertain"]


@pytest.mark.parametrize("interruption", ["archive", "rollback"])
def test_real_handler_recovery_preserves_guard_and_engine_classification(
        tmp_path, scripted, monkeypatch, interruption):
    from commonplace.artifactrun import CodeAttempt, advance
    from commonplace.lib.agentic_analysis.guards import require_publishable_worktree

    attempt = assembled_publish_attempt(tmp_path, scripted)
    repo = attempt.run_dir.parent
    destination = repo / publication.RETAINED_ROOT / publication.source_slug(
        attempt.metadata["source-identity"], attempt.metadata["system"])
    attempt.metadata["review-path"] = (destination / "overview.md").relative_to(repo).as_posix()
    old_id = "AAS-2026-10-06-example-0123456789ab-01"
    old = {"overview.md": doc({"run-id": old_id}), "memory.md": b"old memory\r\n"}
    destination.mkdir(parents=True)
    for name, data in old.items():
        (destination / name).write_bytes(data)
    attempt.metadata["expected-incumbent-sha256"] = publication._digest(old["overview.md"])

    # A temporary Git index and HEAD tree make the incumbent genuinely tracked.
    # No commit is created, even in this fixture repository.
    def git(*args):
        return subprocess.run(["git", *args], cwd=repo, check=True,
                              capture_output=True, text=True).stdout.strip()

    git("init", "-q")
    (repo / ".git/info/exclude").write_text("kb/agentic-system-analyses/state/\n")
    git("add", str(destination.relative_to(repo)))
    tree = git("write-tree")
    # Git status accepts a tree as HEAD for this isolated worktree guard fixture.
    (repo / ".git" / "HEAD").write_text(tree + "\n")
    require_publishable_worktree(repo)

    def environment(current, boundary, **kwargs):
        require_publishable_worktree(repo)
        return attempt.metadata, repo

    monkeypatch.setattr(publication, "_environment", environment)
    monkeypatch.setattr(publication, "inspect_destination", lambda **kwargs: {
        "expected_incumbent_sha256": attempt.metadata["expected-incumbent-sha256"],
    })
    write = effects.atomic_write

    def interrupt(path, data):
        if path.name == "ARTIFACT.yaml":
            if interruption == "archive":
                raise KeyboardInterrupt("interrupted after archive")
            raise OSError("resolved write failure")
        write(path, data)

    monkeypatch.setattr(effects, "atomic_write", interrupt)
    error = KeyboardInterrupt if interruption == "archive" else OSError
    with pytest.raises(error):
        publication.publish_analysis(attempt)
    journal = attempt.run_dir / publication.JOURNAL
    journal_bytes = journal.read_bytes()
    archive = repo / publication.ARCHIVE_ROOT / old_id
    if interruption == "archive":
        assert effects.tree(destination) == {}
        assert effects.tree(archive) == old
        with pytest.raises(ValueError, match="tracked files with local changes"):
            require_publishable_worktree(repo)
    else:
        assert effects.tree(destination) == old
        assert not archive.exists()
        assert json.loads(journal_bytes)["state"] == "rolled-back"
        require_publishable_worktree(repo)

    # Run the actual registered handler through the engine, with fixture pinned
    # inputs and scripted content validation, not an effect-only replacement.
    store = RunStore(attempt.run_dir)
    store.create({"type": (ROOT / "kb" / ANALYSIS_TYPE).read_text(), "type_spec": ANALYSIS_TYPE, "plan": "fixture-plan.yaml",
                  "library": str(ROOT / "kb"), "parameters": {},
                  "declaration": yaml.safe_dump({"type_spec": ANALYSIS_TYPE, "jobs": [
                      {"name": "publish", "kind": "code", "inputs": {}, "outputs": [],
                       "handler": "commonplace.lib.agentic_analysis.publication.publish_analysis"}]})})
    monkeypatch.setattr(CodeAttempt, "read", lambda self, name: attempt.read(name))
    status = advance(store.run_dir)
    assert len(status.stops) == 1
    uncertain = interruption == "archive"
    assert status.stops[0].uncertain == uncertain
    record = store.attempt_records()[0]
    assert record["state"] == "failed" and record["uncertain"] == uncertain
    assert not record["pins"] and "outputs" not in record
    report = engine_run_report(store.run_dir, final_job="publish", status=status)
    assert report["failed-attempts"][0]["uncertain"] == uncertain
    if uncertain:
        assert report["state"] == "uncertain"
        assert journal.read_bytes() == journal_bytes
        assert effects.tree(destination) == {}
        assert effects.tree(archive) == old
    else:
        assert effects.tree(destination) == old
        # A resolved rollback remains an ordinary failure, and can retry.
        monkeypatch.setattr(effects, "atomic_write", write)
        assert json.loads(publication.publish_analysis(attempt)["receipt"])["published"] is True


@pytest.mark.parametrize("journal", [None, b'{"state": "rolled-back"}', b"malformed"])
def test_preliminary_failure_requires_journal_to_be_uncertain(tmp_path, journal):
    attempt = Attempt(tmp_path, overview=True)
    attempt.inputs["boundary"] = None
    if journal is not None:
        path = attempt.run_dir / publication.JOURNAL
        path.parent.mkdir()
        path.write_bytes(journal)
    expected = ValueError if journal is None else UncertainEffectError
    with pytest.raises(expected, match="classified boundary"):
        publication.publish_analysis(attempt)
    if journal is not None:
        assert path.read_bytes() == journal


def test_environment_rechecks_the_declared_capture_identity(tmp_path, monkeypatch):
    attempt = Attempt(tmp_path)
    capture = attempt.run_dir / "sources" / "capture.txt"
    capture.parent.mkdir()
    capture.write_bytes(b"frozen local fixture bytes")
    source = {"kind": "capture", "identity": attempt.metadata["source-identity"],
              "revision": "local-fixture-v1", "path": str(capture),
              "sha256": publication._digest(capture.read_bytes())}
    attempt.metadata["capture-directory"] = str(capture.parent)
    attempt.inputs["source"] = b"null\n"
    attempt.inputs["metadata"] = json.dumps(attempt.metadata).encode()
    fields = publication._document(attempt.inputs["boundary"]).frontmatter
    attempt.inputs["boundary"] = doc({**fields, "source": source, "reviewed-boundary": source["revision"]})
    monkeypatch.setattr(publication, "locate", lambda *args, **kw: (attempt.metadata, tmp_path))
    publication._environment(attempt, publication._document(attempt.inputs["boundary"]), job="fixture")
    capture.write_bytes(b"changed local fixture bytes")
    with pytest.raises(ValueError, match="SHA-256"):
        publication._environment(attempt, publication._document(attempt.inputs["boundary"]), job="fixture")
