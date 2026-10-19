"""Assembly and publication over plain values: members, provenance and opening metadata.

No workers and no workflow: each test hands `publication` the bytes the
workflow would, with scripted guards where a test isolates one concern.
`test_workflow.py` covers publication through the workflow.
"""
from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import pytest
import yaml

from commonplace.lib.agentic_analysis import effects, publication
from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE
from commonplace.lib.agentic_analysis.effects import UncertainEffectError
from commonplace.lib.directory_layout import Layout, type_layout

ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-10-07-example-0123456789ab-01"
OLD_ID = "AAS-2026-10-06-example-0123456789ab-01"
WORKER = {"profile": "fixture", "harness": "fixture", "launch-model": "fixture/model", "effort": "high"}
LAYOUT: Layout = type_layout((ROOT / "kb" / ANALYSIS_TYPE).read_text(encoding="utf-8"), ANALYSIS_TYPE)


def doc(fields, body=""):
    return ("---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body).encode()


@dataclass
class Fixture:
    """One run's plain publication inputs: the members by role, their provenance and the opening metadata."""

    run_dir: Path
    disposition: str
    members: dict[str, bytes] = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    criteria: dict[str, bytes] = field(default_factory=dict)
    source: bytes = b"null\n"

    @property
    def repo(self) -> Path:
        return self.run_dir.parent

    def provenance(self, model="fixture-model-1") -> dict[str, publication.Provenance]:
        return {role: publication.Provenance(model, publication._digest(data))
                for role, data in self.members.items() if role != "overview"}

    def common(self) -> dict:
        return {"metadata": json.dumps(self.metadata).encode(), "source": self.source,
                "provenance": self.provenance(), "layout": LAYOUT, "type_spec": ANALYSIS_TYPE,
                "criteria": self.criteria, "run_dir": self.run_dir}

    def assemble(self) -> tuple[bytes, bytes]:
        return publication.assemble_analysis(self.members, **self.common())

    def publish(self, overview: bytes, manifest: bytes) -> dict:
        receipt = publication.publish_analysis({**self.members, "overview": overview}, manifest=manifest,
                                               library=self.repo / "kb", **self.common())
        return json.loads(receipt)

    def destination(self) -> Path:
        return self.repo / publication.RETAINED_ROOT / publication.publication_slug(
            self.metadata["source-identity"], self.metadata["system"])


def fixture(root: Path, disposition: str = "blocked") -> Fixture:
    """Every non-overview member when complete, else the boundary only; all with one identity."""
    run_dir = root / RUN_ID
    run_dir.mkdir(parents=True)
    identity = {"run-id": RUN_ID, "result-disposition": disposition, "target-class": None, "boundary-kind": None,
                "reviewed-boundary": None, "analysis-cutoff": None, "evidence-tier": None}
    roles = [r for r in LAYOUT.roles if r != "overview"] if disposition == "complete" else ["boundary"]
    members = {role: doc({"type": LAYOUT.roles[role].type, **identity, "description": "Fixture description"})
               for role in roles}
    metadata = {"run-id": RUN_ID, "system": "Example", "run-date": "2026-10-07", "inputs-commit": "a" * 40,
                "source-identity": "https://example.invalid/example",
                "review-path": "kb/agentic-system-analyses/retained/example/overview.md",
                "expected-incumbent-sha256": "absent", "worker": WORKER}
    return Fixture(run_dir, disposition, members, metadata)


def located(monkeypatch, repo=None):
    """Each run's checkout is its parent directory, or ``repo``; no location guard runs."""
    monkeypatch.setattr(publication, "checkout", lambda run_dir: repo or run_dir.parent)
    monkeypatch.setattr(publication, "_opened_environment", lambda metadata, run_dir, library, **kw: (
        json.loads(metadata), repo or run_dir.parent))


@pytest.fixture
def scripted(monkeypatch):
    """Guards and content validation scripted away; returns the validation calls."""
    checked = []
    located(monkeypatch)
    monkeypatch.setattr(publication, "_environment", lambda *args, **kw: None)
    monkeypatch.setattr(publication, "_require_opened_method", lambda *args, **kw: None)
    monkeypatch.setattr(publication, "validate_pinned_artifact", lambda *args, **kw: checked.append(kw))
    return checked


def pinned_criteria(f: Fixture):
    """Shipped layout with minimal schemas, isolating validation from the shipped analysis criteria."""
    types = "agentic-system-analyses/types/"
    f.criteria[ANALYSIS_TYPE] = (ROOT / "kb" / ANALYSIS_TYPE).read_bytes()
    for path in ("agentic-system-analyses/COLLECTION.md", "reference/validation-contract.md"):
        f.criteria[path] = b"# Fixture contract\n"
    f.criteria[types + "agentic-system-analysis-set.schema.yaml"] = b"type: object\n"
    for spec, name in (("types/type-spec.md", "type-spec"),
                       (types + "agentic-system-boundary.md", "agentic-system-boundary"),
                       (types + "agentic-system-analysis-overview.md", "agentic-system-analysis-overview")):
        f.criteria[spec] = (f"---\ntype: types/type-spec.md\nname: {name}\n"
                            f"description: Pinned fixture\nschema: ./{name}.schema.yaml\n---\n# Fixture\n").encode()
        f.criteria[spec.removesuffix(".md") + ".schema.yaml"] = b"type: object\n"


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope", "complete"])
def test_assembly_pins_the_members_and_the_worker_model(tmp_path, scripted, disposition):
    f = fixture(tmp_path, disposition)
    # Bytes in the working artifact directory are not assembly input.
    (f.run_dir / "artifact").mkdir()
    (f.run_dir / "artifact" / "memory.md").write_bytes(b"untracked garbage")
    overview, manifest = f.assemble()
    pinned = yaml.safe_load(manifest)
    assert pinned["type"] == ANALYSIS_TYPE
    assert pinned["members"] == {LAYOUT.path(role): {"sha256": publication._digest(data)}
                                 for role, data in {**f.members, "overview": overview}.items()}
    assert pinned["worker"] == {**WORKER, "model": "fixture-model-1"}
    assert b"untracked garbage" not in overview
    assert publication._document(overview).frontmatter["system"] == "Example"
    assert scripted[0]["manifest"] == manifest
    assert set(scripted[0]["members"]) == set(pinned["members"])


@pytest.mark.parametrize("defect,reason", [
    ("stale", "memory provenance does not identify its completed output"),
    ("mixed", "every worker must report the same model"),
])
def test_assembly_refuses_misattributed_members(tmp_path, scripted, monkeypatch, defect, reason):
    f = fixture(tmp_path, "complete")
    provenance = f.provenance()
    if defect == "stale":
        provenance["memory"] = publication.Provenance("fixture-model-1", publication._digest(b"an older output"))
    else:
        provenance["memory"] = publication.Provenance("fixture-model-2", provenance["memory"].output_sha256)
    monkeypatch.setattr(Fixture, "provenance", lambda self: provenance)
    with pytest.raises(ValueError, match=reason):
        f.assemble()
    assert not scripted


@pytest.mark.parametrize("defect,reason", [
    ("missing-criteria", "missing pinned criterion"), ("content", "missing-fixture-field"),
])
def test_validation_failure_prevents_assembly(tmp_path, monkeypatch, defect, reason):
    f = fixture(tmp_path / "kb/agentic-system-analyses/state")
    if defect == "content":
        pinned_criteria(f)
        f.criteria["agentic-system-analyses/types/agentic-system-boundary.schema.yaml"] = (
            b"required: [missing-fixture-field]\n")
    located(monkeypatch, tmp_path)
    monkeypatch.setattr(publication, "_environment", lambda *args, **kw: None)
    with pytest.raises(ValueError, match=reason):
        f.assemble()


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_a_non_complete_artifact_is_validated_and_stays_local(tmp_path, monkeypatch, disposition):
    f = fixture(tmp_path / "kb/agentic-system-analyses/state", disposition)
    pinned_criteria(f)
    located(monkeypatch, tmp_path)
    monkeypatch.setattr(publication, "_environment", lambda *args, **kw: None)
    monkeypatch.setattr(publication, "_require_opened_method", lambda *args, **kw: None)
    overview, manifest = f.assemble()
    monkeypatch.setattr(publication, "install_tree", lambda **kw: pytest.fail("must remain local"))
    assert f.publish(overview, manifest) == {"published": False}
    assert not (tmp_path / "kb/agentic-system-analyses/retained").exists()
    assert not (f.run_dir / "effects").exists()

    # Re-pin an identity-inconsistent overview: hashes alone are not validation.
    members = {"boundary.md": f.members["boundary"],
               "overview.md": overview.replace(RUN_ID.encode(), b"changed-run")}
    repinned = yaml.safe_dump({"type": ANALYSIS_TYPE, "members": {
        name: {"sha256": publication._digest(data)} for name, data in members.items()}}).encode()
    with pytest.raises(ValueError, match="identity field run-id"):
        publication.validate_pinned_artifact(
            repo=tmp_path, members=members, manifest=repinned, layout=LAYOUT,
            type_spec=ANALYSIS_TYPE, criteria=f.criteria, run_dir=f.run_dir)


def test_publish_refuses_a_manifest_that_does_not_pin_the_members(tmp_path, scripted):
    f = fixture(tmp_path, "complete")
    overview, _ = f.assemble()
    with pytest.raises(ValueError, match="manifest does not pin"):
        f.publish(overview, b"type: wrong\n")


def test_interrupted_archive_is_uncertain_and_a_resolved_rollback_retries(tmp_path, scripted, monkeypatch):
    """An interruption after the archive move leaves the evidence; a rolled-back failure publishes on retry."""
    from commonplace.lib.agentic_analysis.guards import require_publishable_worktree

    def published_incumbent(root: Path):
        f = fixture(root, "complete")
        destination = f.destination()
        f.metadata["review-path"] = (destination / "overview.md").relative_to(f.repo).as_posix()
        old = {"overview.md": doc({"run-id": OLD_ID}), "memory.md": b"old memory\r\n"}
        destination.mkdir(parents=True)
        for name, data in old.items():
            (destination / name).write_bytes(data)
        f.metadata["expected-incumbent-sha256"] = publication._digest(old["overview.md"])

        # A temporary Git index and HEAD tree make the incumbent tracked without a commit.
        def git(*args):
            return subprocess.run(["git", *args], cwd=f.repo, check=True, capture_output=True,
                                  text=True).stdout.strip()

        git("init", "-q")
        (f.repo / ".git/info/exclude").write_text(f"{RUN_ID}/\nkb/agentic-system-analyses/state/\n")
        git("add", str(destination.relative_to(f.repo)))
        (f.repo / ".git" / "HEAD").write_text(git("write-tree") + "\n")
        require_publishable_worktree(f.repo)
        overview, manifest = f.assemble()
        return f, overview, manifest, destination, old

    monkeypatch.setattr(publication, "_environment", lambda *a, **kw: require_publishable_worktree(a[1]))
    monkeypatch.setattr(publication, "inspect_destination", lambda **kw: {
        "expected_incumbent_sha256": publication._digest(doc({"run-id": OLD_ID}))})
    write = effects.atomic_write

    def interrupting(error):
        def atomic_write(path, data):
            if path.name == "ARTIFACT.yaml":
                raise error
            write(path, data)
        return atomic_write

    # Interrupted after the archive move: the journal says started, nothing is rolled back.
    f, overview, manifest, destination, old = published_incumbent(tmp_path / "archive")
    monkeypatch.setattr(effects, "atomic_write", interrupting(KeyboardInterrupt("interrupted after archive")))
    with pytest.raises(KeyboardInterrupt):
        f.publish(overview, manifest)
    journal = f.run_dir / publication.JOURNAL
    evidence = journal.read_bytes()
    archive = f.repo / publication.ARCHIVE_ROOT / OLD_ID
    assert effects.tree(destination) == {} and effects.tree(archive) == old
    with pytest.raises(ValueError, match="tracked files with local changes"):
        require_publishable_worktree(f.repo)
    monkeypatch.setattr(effects, "atomic_write", write)
    with pytest.raises(UncertainEffectError):
        f.publish(overview, manifest)
    assert journal.read_bytes() == evidence
    assert effects.tree(destination) == {} and effects.tree(archive) == old

    # A write failure rolls back: the incumbent is restored and a retry publishes.
    f, overview, manifest, destination, old = published_incumbent(tmp_path / "rollback")
    monkeypatch.setattr(effects, "atomic_write", interrupting(OSError("resolved write failure")))
    with pytest.raises(OSError, match="resolved write failure"):
        f.publish(overview, manifest)
    assert effects.tree(destination) == old
    assert not (f.repo / publication.ARCHIVE_ROOT / OLD_ID).exists()
    assert json.loads((f.run_dir / publication.JOURNAL).read_bytes())["state"] == "rolled-back"
    require_publishable_worktree(f.repo)
    monkeypatch.setattr(effects, "atomic_write", write)
    assert f.publish(overview, manifest)["published"] is True
    assert effects.tree(f.repo / publication.ARCHIVE_ROOT / OLD_ID) == old


@pytest.mark.parametrize("journal", [None, b'{"state": "rolled-back"}', b"malformed"])
def test_a_preliminary_failure_is_uncertain_once_a_journal_exists(tmp_path, scripted, journal):
    f = fixture(tmp_path)
    if journal is not None:
        path = f.run_dir / publication.JOURNAL
        path.parent.mkdir()
        path.write_bytes(journal)
    f.members.pop("boundary")
    expected = ValueError if journal is None else UncertainEffectError
    with pytest.raises(expected, match="classified boundary"):
        f.publish(doc({"run-id": RUN_ID}), b"manifest")
    if journal is not None:
        assert path.read_bytes() == journal


def test_environment_rechecks_the_declared_capture_identity(tmp_path):
    f = fixture(tmp_path)
    capture = f.run_dir / "sources" / "capture.txt"
    capture.parent.mkdir()
    capture.write_bytes(b"frozen local fixture bytes")
    source = {"kind": "capture", "identity": f.metadata["source-identity"],
              "revision": "local-fixture-v1", "path": str(capture),
              "sha256": publication._digest(capture.read_bytes())}
    fields = publication._document(f.members["boundary"]).frontmatter
    boundary = doc({**fields, "source": source, "reviewed-boundary": source["revision"]})

    def environment():
        publication._environment(f.metadata, tmp_path, boundary, b"null\n", f.run_dir, job="fixture")

    environment()
    capture.write_bytes(b"changed local fixture bytes")
    with pytest.raises(ValueError, match="SHA-256"):
        environment()
