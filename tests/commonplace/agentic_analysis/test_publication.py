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

from commonplace.lib.agentic_analysis import publication
from commonplace.lib.agentic_analysis.report import engine_run_report
from commonplace.lib.agentic_analysis.sets import SET_TYPE
from commonplace.workflow import RunStatus, Stop, UncertainEffectError
from commonplace.workflow.state import _parse_type
from commonplace.workflow.store import RunStore

ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-10-07-example-0123456789ab-01"


def doc(fields, body=""):
    return ("---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body).encode()


class Attempt:
    """A restricted pinned-input fixture: no hidden run/store introspection."""
    def __init__(self, tmp_path, disposition="blocked", *, overview=False):
        self.run_dir = tmp_path / RUN_ID
        self.run_dir.mkdir(parents=True)
        self.library = tmp_path / "kb"
        # The set type a run fixes at start, as CodeAttempt exposes it.
        self.type_text = (ROOT / "kb" / SET_TYPE).read_text()
        layout, relations = _parse_type(self.type_text, SET_TYPE)
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
                    "effort": "high", "outputs": {primary: publication._digest(data)},
                }).encode() if data else None)
        self.metadata = {"run-id": RUN_ID, "system": "Example", "run-date": "2026-10-07",
                         "inputs-commit": "a" * 40, "source-identity": "https://example.invalid/example",
                         "review-path": "kb/agentic-system-analyses/retained/example/overview.md",
                         "expected-incumbent-sha256": "absent"}
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
    monkeypatch.setattr(publication, "validate_pinned_set", lambda *args, **kw: checked.append(kw))
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
    (attempt.run_dir / "set").mkdir()
    (attempt.run_dir / "set" / "memory.md").write_bytes(b"untracked garbage")
    outputs = publication.assemble_analysis(attempt)
    manifest = yaml.safe_load(outputs["manifest"])
    assert manifest["worker"] == {"model": "fixture/model", "effort": "high"}
    assert manifest["members"]["overview.md"] == {"sha256": publication._digest(outputs["overview"])}
    assert set(manifest["members"]) == set(scripted[0]["members"])
    assert b"untracked garbage" not in outputs["overview"]
    assert attempt.judgments[0][0] == "overview"
    assert "overview:identity:boundary" in attempt.judgments[0][1]["scope"]


# Membership, acceptance and coverage now gate assembly through the engine's
# coverage input; the engine scenario tests pin that it waits, not fails.
@pytest.mark.parametrize("defect,reason", [
    ("provenance", "provenance"), ("mixed-worker", "identical worker"),
])
def test_assembly_rejects_misattributed_complete_set(tmp_path, scripted, defect, reason):
    attempt = Attempt(tmp_path, "complete")
    record = json.loads(attempt.inputs["memory-attempt"])
    record["model" if defect == "mixed-worker" else "outputs"] = (
        "other/model" if defect == "mixed-worker" else {"answers": publication._digest(attempt.inputs["memory"])})
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
    assert not (attempt.run_dir / "set" / "overview.md").exists()


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_real_bounded_adapter_assembly_and_local_publication(tmp_path, monkeypatch, disposition):
    attempt = Attempt(tmp_path / "kb/agentic-system-analyses/state", disposition)
    pinned_criteria(attempt)
    monkeypatch.setattr(publication, "_environment", lambda *args, **kw: (attempt.metadata, tmp_path))
    monkeypatch.setattr(publication, "_require_opened_method", lambda *args, **kw: None)
    outputs = publication.assemble_analysis(attempt)
    attempt.inputs.update(outputs)
    monkeypatch.setattr(publication, "_publish_effect", lambda **kw: pytest.fail("must remain local"))
    assert json.loads(publication.publish_analysis(attempt)["receipt"]) == {"published": False}
    assert not (tmp_path / "kb/agentic-system-analyses/retained").exists()
    assert not (attempt.run_dir / "output").exists()
    assert not (attempt.run_dir / "run-state.md").exists()

    # Re-pin an identity-inconsistent overview: hashes alone are not validation.
    members = {"boundary.md": attempt.inputs["boundary"],
               "overview.md": outputs["overview"].replace(RUN_ID.encode(), b"changed-run")}
    manifest = yaml.safe_dump({"type": SET_TYPE, "members": {
        name: {"sha256": publication._digest(data)} for name, data in members.items()
    }}).encode()
    with pytest.raises(ValueError, match="identity field run-id"):
        publication.validate_pinned_set(attempt, repo=tmp_path, members=members, manifest=manifest)


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


def effect(tmp_path, *, incumbent=False):
    run = tmp_path / RUN_ID
    run.mkdir()
    destination = tmp_path / "retained" / "example"
    archive = tmp_path / "archive"
    old = {"overview.md": doc({"run-id": "AAS-2026-10-06-example-0123456789ab-01"}),
           "ARTIFACT.yaml": b"old manifest\n", "memory.md": b"old memory\r\n"}
    if incumbent:
        destination.mkdir(parents=True)
        for name, data in old.items():
            (destination / name).write_bytes(data)
    new = {"ARTIFACT.yaml": b"new manifest\n", "overview.md": b"new overview\r\n", "memory.md": b"new memory\n"}
    args = {"run_dir": run, "destination": destination, "archive_root": archive, "files": new,
            "expected": publication._digest(old["overview.md"]) if incumbent else "absent",
            "identity": "fixture/source", "inspect_incumbent": lambda: None}
    return args, old


@pytest.mark.parametrize("incumbent", [False, True])
def test_exact_byte_effect_and_replay(tmp_path, incumbent):
    args, old = effect(tmp_path, incumbent=incumbent)
    first = publication._publish_effect(**args)
    assert publication._tree(args["destination"]) == args["files"]
    if incumbent:
        assert publication._tree(args["archive_root"] / "AAS-2026-10-06-example-0123456789ab-01") == old
    args["inspect_incumbent"] = lambda: pytest.fail("recognizable replay must not reinspect the new incumbent")
    assert publication._publish_effect(**args) == first
    assert json.loads((args["run_dir"] / publication.JOURNAL).read_bytes())["state"] == "completed"


def test_incumbent_guard_has_no_effect(tmp_path):
    args, old = effect(tmp_path, incumbent=True)
    args["expected"] = "f" * 64
    with pytest.raises(ValueError, match="changed since"):
        publication._publish_effect(**args)
    assert publication._tree(args["destination"]) == old
    assert not (args["run_dir"] / publication.JOURNAL).exists()


def test_failed_write_rolls_back_exact_old_tree_and_retries(tmp_path, monkeypatch):
    args, old = effect(tmp_path, incumbent=True)
    original = publication.atomic_write

    def fail_member(path, data):
        if path.name == "memory.md":
            raise OSError("scripted member failure")
        original(path, data)

    monkeypatch.setattr(publication, "atomic_write", fail_member)
    with pytest.raises(OSError, match="scripted"):
        publication._publish_effect(**args)
    assert publication._tree(args["destination"]) == old
    assert json.loads((args["run_dir"] / publication.JOURNAL).read_bytes())["state"] == "rolled-back"
    monkeypatch.setattr(publication, "atomic_write", original)
    publication._publish_effect(**args)
    assert publication._tree(args["destination"]) == args["files"]


@pytest.mark.parametrize("point", ["before-effect", "after-move", "after-install"])
def test_interrupted_effect_recognition(tmp_path, monkeypatch, point):
    args, old = effect(tmp_path, incumbent=True)
    original = publication._write_record
    write = publication.atomic_write

    def interrupt(path, record):
        if record["state"] == ("completed" if point == "after-install" else "started"):
            original(path, record) if point == "before-effect" else None
            if point != "after-move":
                raise KeyboardInterrupt("scripted interrupt")
        original(path, record)

    def interrupt_member(path, data):
        if point == "after-move" and path.name == "ARTIFACT.yaml":
            raise KeyboardInterrupt("scripted interrupt")
        write(path, data)

    monkeypatch.setattr(publication, "_write_record", interrupt)
    monkeypatch.setattr(publication, "atomic_write", interrupt_member)
    with pytest.raises(KeyboardInterrupt):
        publication._publish_effect(**args)
    monkeypatch.setattr(publication, "_write_record", original)
    monkeypatch.setattr(publication, "atomic_write", write)
    if point == "after-move":
        with pytest.raises(UncertainEffectError, match="interrupted publication"):
            publication._publish_effect(**args)
        assert publication._tree(args["destination"]) == {}
        assert publication._tree(args["archive_root"] / "AAS-2026-10-06-example-0123456789ab-01") == old
    else:
        publication._publish_effect(**args)
        assert publication._tree(args["destination"]) == args["files"]


def test_changed_journal_inputs_and_changed_completed_bytes_stop(tmp_path):
    args, _ = effect(tmp_path)
    publication._publish_effect(**args)
    args["files"] = {**args["files"], "memory.md": b"different pin"}
    with pytest.raises(UncertainEffectError, match="identity"):
        publication._publish_effect(**args)
    args["files"]["memory.md"] = b"new memory\n"
    (args["destination"] / "memory.md").write_bytes(b"unexpected mutation")
    with pytest.raises(UncertainEffectError, match="completed publication"):
        publication._publish_effect(**args)


def test_rollback_failure_is_uncertain_and_preserves_evidence(tmp_path, monkeypatch):
    args, _ = effect(tmp_path, incumbent=True)
    original = publication.atomic_write

    def fail(path, data):
        if path.name == "memory.md":
            raise OSError("cannot write member")
        original(path, data)

    monkeypatch.setattr(publication, "atomic_write", fail)
    monkeypatch.setattr(publication.shutil, "rmtree", lambda path: (_ for _ in ()).throw(OSError("cannot rollback")))
    with pytest.raises(UncertainEffectError, match="rollback uncertain"):
        publication._publish_effect(**args)
    assert (args["run_dir"] / publication.JOURNAL).exists()
    assert args["archive_root"].exists()


def test_engine_report_is_separate_and_uncertain_without_recovery(tmp_path):
    store = RunStore(tmp_path / "engine-run")
    type_text = (ROOT / "kb" / SET_TYPE).read_text()
    store.create({"type": type_text, "type_spec": SET_TYPE, "job_set": "fixture-job-set.yaml", "library": str(ROOT / "kb"),
                  "declaration": yaml.safe_dump({"type_spec": SET_TYPE, "jobs": [
                      {"name": "publish", "kind": "code", "handler": "unused.handler", "inputs": {}, "outputs": []}]}),
                  "parameters": {"system": "fixture"}})
    store.fail_attempt({"id": "000001-publish", "seq": 1, "job": "publish", "kind": "code", "pins": {}},
                       "scripted uncertain publication", uncertain=True)
    (store.run_dir / "effects").mkdir()
    (store.run_dir / publication.JOURNAL).write_text('{"state": "completed"}')
    status = RunStatus((), (), (Stop("uncertain effect", "publish", "000001-publish", True),), False)
    report = engine_run_report(store.run_dir, status=status)
    assert report["state"] == "uncertain"
    assert report["effects"]["publish"] == {"journal-state": "completed", "verified": False}
    assert report["failed-attempts"][0]["uncertain"]
    assert report["invocation-stops"][0]["uncertain"]
    assert not (store.run_dir / "run-state.md").exists()
    assert not (store.run_dir / "output").exists()
    assert "round" not in report
    (store.run_dir / "output").mkdir()
    with pytest.raises(ValueError, match="legacy/mixed"):
        engine_run_report(store.run_dir)


@pytest.mark.parametrize("interruption", ["archive", "rollback"])
def test_real_handler_recovery_preserves_guard_and_engine_classification(
        tmp_path, scripted, monkeypatch, interruption):
    from commonplace.lib.agentic_analysis.guards import require_publishable_worktree
    from commonplace.workflow import CodeAttempt, advance

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
    write = publication.atomic_write

    def interrupt(path, data):
        if path.name == "ARTIFACT.yaml":
            if interruption == "archive":
                raise KeyboardInterrupt("interrupted after archive")
            raise OSError("resolved write failure")
        write(path, data)

    monkeypatch.setattr(publication, "atomic_write", interrupt)
    error = KeyboardInterrupt if interruption == "archive" else OSError
    with pytest.raises(error):
        publication.publish_analysis(attempt)
    journal = attempt.run_dir / publication.JOURNAL
    journal_bytes = journal.read_bytes()
    archive = repo / publication.ARCHIVE_ROOT / old_id
    if interruption == "archive":
        assert publication._tree(destination) == {}
        assert publication._tree(archive) == old
        with pytest.raises(ValueError, match="tracked files with local changes"):
            require_publishable_worktree(repo)
    else:
        assert publication._tree(destination) == old
        assert not archive.exists()
        assert json.loads(journal_bytes)["state"] == "rolled-back"
        require_publishable_worktree(repo)

    # Run the actual registered handler through the engine, with fixture pinned
    # inputs and scripted content validation, not an effect-only replacement.
    store = RunStore(attempt.run_dir)
    store.create({"type": (ROOT / "kb" / SET_TYPE).read_text(), "type_spec": SET_TYPE, "job_set": "fixture-job-set.yaml",
                  "library": str(ROOT / "kb"), "parameters": {},
                  "declaration": yaml.safe_dump({"type_spec": SET_TYPE, "jobs": [
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
    report = engine_run_report(store.run_dir, status=status)
    assert report["failed-attempts"][0]["uncertain"] == uncertain
    if uncertain:
        assert report["state"] == "uncertain"
        assert journal.read_bytes() == journal_bytes
        assert publication._tree(destination) == {}
        assert publication._tree(archive) == old
    else:
        assert publication._tree(destination) == old
        # A resolved rollback remains an ordinary failure, and can retry.
        monkeypatch.setattr(publication, "atomic_write", write)
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
    monkeypatch.setattr(publication, "_locate", lambda *args, **kw: (attempt.metadata, tmp_path))
    publication._environment(attempt, publication._document(attempt.inputs["boundary"]), job="fixture")
    capture.write_bytes(b"changed local fixture bytes")
    with pytest.raises(ValueError, match="SHA-256"):
        publication._environment(attempt, publication._document(attempt.inputs["boundary"]), job="fixture")


def test_effect_rejects_symlinked_destination_without_mutation(tmp_path):
    args, _ = effect(tmp_path)
    external = tmp_path / "external"
    external.mkdir()
    args["destination"].parent.mkdir()
    args["destination"].symlink_to(external, target_is_directory=True)
    with pytest.raises(UncertainEffectError, match="symlinks"):
        publication._publish_effect(**args)
    assert list(external.iterdir()) == []
