"""Local source authorization and member-link guards; no workflow effects."""
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import sources
from commonplace.lib.agentic_analysis import boundary as agentic_boundary
from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE
from commonplace.lib.type_resolver import CriterionSnapshot
from commonplace.lib.validation import (
    ValidationRun,
    validate_draft_at_slot,
    validate_pinned_artifact_snapshot,
)

IDENTITY = "https://example.invalid/source"
REVISION = "a" * 40


def boundary(source, **fields):
    return ("---\n" + yaml.safe_dump({
        "run-id": "fixture", "source": source,
        "reviewed-boundary": source["revision"], **fields,
    }) + "---\n# Boundary\n").encode()


def source_at(path, kind="capture"):
    return {"kind": kind, "identity": IDENTITY, "path": str(path),
            "revision": "capture-fixture" if kind == "capture" else REVISION,
            "sha256": sha256(b"frozen bytes").hexdigest() if kind == "capture" else None}


def check(data, root, **kwargs):
    return agentic_boundary.boundary_refusals(
        data, repo_root=root, run_id="fixture", identity=IDENTITY, **kwargs,
    )


FROZEN_CASES = [f"frozen-{kind}-{field}" for kind in ("capture", "git")
                for field in ("path", "identity", "revision", "sha256", "kind")]
UNPINNED_CASES = [f"unpinned-{defect}" for defect in
                  ("outside", "traversal", "relative", "git", "identity", "legacy-identity")]


@pytest.mark.parametrize("case", [*FROZEN_CASES, *UNPINNED_CASES])
def test_unauthorized_source_is_refused_before_inspection(tmp_path, monkeypatch, case):
    mode, _, detail = case.partition("-")
    if mode == "frozen":
        kind, field = detail.split("-")
        frozen = source_at(tmp_path / "frozen", kind)
        source = {**frozen, field: "different"}
        if field == "path":
            source[field] = str(tmp_path / "unauthorized")
        data = boundary(source, **{"run-id": "wrong"})
        options = {"frozen": frozen}
    else:
        directory = tmp_path / "captures"
        source = source_at(directory / "capture.md")
        if detail == "outside":
            source["path"] = str(tmp_path / "captures-other/capture.md")
        elif detail == "traversal":
            source["path"] = str(directory / "../outside.md")
        elif detail == "relative":
            source["path"] = "captures/capture.md"
        elif detail == "git":
            source = source_at(directory / "checkout", "git")
        else:
            source["identity"] = "wrong"
        data = boundary(source)
        options = {"capture_directory": None if detail == "legacy-identity" else directory}
    calls = []

    def forbidden(*args, **kwargs):
        calls.append(args)
        raise AssertionError("unauthorized source inspection")

    with monkeypatch.context() as patch:
        for name in ("read_bytes", "read_text", "is_file", "is_dir", "is_symlink", "resolve"):
            patch.setattr(Path, name, forbidden)
        patch.setattr(sources.subprocess, "run", forbidden)
        reasons = check(data, tmp_path, **options)
    assert reasons and not calls
    if mode == "frozen":
        assert any("source must" in reason for reason in reasons)
        assert any("run-id" in reason for reason in reasons)
        if field == "identity":
            assert any("source.identity" in reason for reason in reasons)


@pytest.mark.parametrize("guard", ["file-symlink", "parent-symlink", "traversal"])
def test_canonical_guard_prevents_reads_and_git(tmp_path, monkeypatch, guard):
    captures = tmp_path / "captures"
    captures.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "capture.md").write_bytes(b"frozen bytes")
    if guard == "file-symlink":
        path = captures / "capture.md"
        path.symlink_to(outside / "capture.md")
    elif guard == "parent-symlink":
        (captures / "alias").symlink_to(outside, target_is_directory=True)
        path = captures / "alias/capture.md"
    else:
        path = captures / "../outside/capture.md"
    source = source_at(path)
    calls = []

    def forbidden(*args, **kwargs):
        calls.append(args)
        raise AssertionError("redirected source read")

    monkeypatch.setattr(Path, "read_bytes", forbidden)
    monkeypatch.setattr(sources.subprocess, "run", forbidden)
    assert check(boundary(source), tmp_path, capture_directory=captures)
    # Frozen and legacy callers retain the canonical-path guard too.
    assert check(boundary(source), tmp_path, frozen=source)
    assert check(boundary(source), tmp_path)
    assert not calls


@pytest.mark.parametrize("mode", ["frozen", "capture-directory", "legacy"])
@pytest.mark.parametrize("bad_member", [False, True])
def test_authorized_capture_is_read_and_independent_diagnostics_survive(tmp_path, monkeypatch, mode, bad_member):
    path = tmp_path / "capture.md"
    path.write_bytes(b"frozen bytes")
    source = source_at(path)
    reads = []
    original = Path.read_bytes

    def read(file):
        reads.append(file)
        return original(file)

    monkeypatch.setattr(Path, "read_bytes", read)
    options = {"frozen": source} if mode == "frozen" else (
        {"capture_directory": tmp_path} if mode == "capture-directory" else {})
    fields = {"run-id": "wrong", "reviewed-boundary": "wrong"} if bad_member else {}
    reasons = check(boundary(source, **fields), tmp_path, **options)
    assert reads == [path]
    assert bool(reasons) == bad_member
    path.write_bytes(b"changed")
    reasons = check(boundary(source, **fields), tmp_path, **options)
    assert any("source.sha256" in reason for reason in reasons)
    if bad_member:
        assert any("run-id" in reason for reason in reasons)
        if mode != "legacy":
            assert any("reviewed-boundary" in reason for reason in reasons)


@pytest.fixture
def link_snapshot():
    # Real layout and rule dispatch, minimal schemas to isolate the link rule.
    library = Path(__file__).resolve().parents[3] / "kb"
    criteria = {
        ANALYSIS_TYPE: (library / ANALYSIS_TYPE).read_bytes(),
        ANALYSIS_TYPE.removesuffix(".md") + ".schema.yaml": b"type: object\n",
        "agentic-system-analyses/COLLECTION.md": b"# Fixture collection\n",
        "reference/validation-contract.md": b"# Fixture validation contract\n",
        "types/type-spec.md": (
            b"---\ntype: types/type-spec.md\nname: type-spec\ndescription: Fixture\n"
            b"schema: ./type-spec.schema.yaml\n---\n# Type\n"
        ),
        "types/type-spec.schema.yaml": b"type: object\n",
    }
    members = {}
    for role, name in (("boundary", "agentic-system-boundary"),
                       ("overview", "agentic-system-analysis-overview")):
        type_path = f"agentic-system-analyses/types/{name}.md"
        criteria[type_path] = (f"---\ntype: types/type-spec.md\nname: {name}\n"
                               "description: Fixture\nschema: ./fixture.schema.yaml\n---\n# Type\n").encode()
        criteria["agentic-system-analyses/types/fixture.schema.yaml"] = b"type: object\n"
        members[role + ".md"] = (f"---\ntype: {type_path}\ndescription: Fixture\n"
                                  "run-id: fixture\nresult-disposition: blocked\n---\n# Member\n").encode()
    members["overview.md"] += b"\n## Members\n\n[Boundary](./boundary.md)\n"
    return criteria, members


@pytest.mark.parametrize("link,refused", [
    ("../outside.md", True), ("./nested/outside.md", True),
    ("./overview.md", False), ("#boundary-and-evidence", False),
    ("https://example.invalid/evidence", False),
])
def test_boundary_links_consistent_at_member_slot_and_relocated_pinned_artifact(tmp_path, link_snapshot, link, refused):
    criteria, members = link_snapshot
    members["boundary.md"] += f"\n[Evidence]({link})\n".encode()
    manifest = yaml.safe_dump({
        "type": ANALYSIS_TYPE,
        "members": {name: {"sha256": sha256(data).hexdigest()} for name, data in members.items()},
    }).encode()
    expected = f"artifact member link: {link} leaves the artifact directory"
    for location in ("state/fixture/artifact", "retained/fixture"):
        directory = tmp_path / "kb/agentic-system-analyses" / location
        path = directory / "boundary.md"
        standalone = ValidationRun(
            tmp_path, (), criteria=CriterionSnapshot(tmp_path / "kb", criteria),
            content_overrides={directory / name: data for name, data in members.items()},
        ).validate(path)
        draft = validate_draft_at_slot(
            directory, "boundary.md", members["boundary.md"], repo_root=tmp_path,
            members={"overview.md": members["overview.md"]}, manifest=manifest, criteria=criteria,
        )
        pinned = validate_pinned_artifact_snapshot(
            repo=tmp_path, artifact_type=ANALYSIS_TYPE, intended_artifact_path=directory, members=members,
            manifest=manifest, criteria=criteria,
        )
        assert not any("[pinned contracts]" in message for message in pinned.fails), pinned.fails
        for messages in (standalone.fails, [finding.message for finding in draft], pinned.fails):
            failures = [message for message in messages if "artifact member link:" in message]
            assert bool(failures) == refused, messages
            if refused:
                assert any(expected in message for message in failures)
        assert not directory.exists()  # Location-aware validation never publishes.
