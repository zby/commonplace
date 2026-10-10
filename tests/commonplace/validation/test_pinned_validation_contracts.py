"""Local contract fixtures only: no analysis runs or publication effects."""
from pathlib import Path

import pytest
import yaml

from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE
from commonplace.lib.type_resolver import (
    CriterionSnapshot,
    resolve_type,
    resolve_type_definition,
    validate_instance,
)
from commonplace.lib.validation import ValidationRun, validate_pinned_artifact_snapshot

TYPE = b"""---
type: types/type-spec.md
name: pinned
description: Pinned fixture
schema: ./fixture.schema.yaml
---
# Fixture
"""


def snapshot(tmp_path, schema, **extra):
    return CriterionSnapshot(tmp_path / "kb", {
        "types/fixture.md": TYPE,
        "types/fixture.schema.yaml": yaml.safe_dump(schema).encode(),
        **extra,
    })


def profile(tmp_path, criteria):
    return resolve_type(
        tmp_path / "kb/notes/fixture.md", {"type": "types/fixture.md"},
        repo_root=tmp_path, criteria=criteria,
    )


def test_virtual_type_overrides_disk_and_loader(tmp_path):
    path = tmp_path / "kb/types/fixture.md"
    path.parent.mkdir(parents=True)
    path.write_text("not a type")
    criteria = snapshot(tmp_path, {"type": "object"})
    resolved = resolve_type_definition(
        path, repo_root=tmp_path, criteria=criteria,
        load_frontmatter=lambda _: pytest.fail("legacy loader called"),
    )
    assert resolved.type_name == "pinned"
    assert not validate_instance(resolved, {})


def test_missing_type_does_not_use_disk(tmp_path):
    path = tmp_path / "kb/types/fixture.md"
    path.parent.mkdir(parents=True)
    path.write_bytes(TYPE)
    with pytest.raises(FileNotFoundError, match="missing pinned criterion"):
        profile(tmp_path, CriterionSnapshot(tmp_path / "kb", {}))


def test_missing_transitive_dependency_even_in_inactive_branch(tmp_path):
    criteria = snapshot(tmp_path, {
        "if": False, "then": {"$ref": "./middle.schema.yaml"},
    }, **{"types/middle.schema.yaml": b"$ref: ./leaf.schema.yaml\n"})
    leaf = tmp_path / "kb/types/leaf.schema.yaml"
    leaf.parent.mkdir(parents=True)
    leaf.write_text("type: object\n")
    with pytest.raises(FileNotFoundError, match="leaf.schema.yaml"):
        profile(tmp_path, criteria)


def test_changed_transitive_schema_and_cross_run_cache_isolation(tmp_path):
    root = {"$ref": "commonplace:types/middle.schema.yaml#/$defs/value"}
    middle = b"$defs:\n  value:\n    $ref: ./leaf.schema.yaml\n"
    first = snapshot(tmp_path, root, **{
        "types/middle.schema.yaml": middle,
        "types/leaf.schema.yaml": b"type: object\n",
    })
    second = snapshot(tmp_path, root, **{
        "types/middle.schema.yaml": middle,
        "types/leaf.schema.yaml": b"type: string\n",
    })
    p1, p2 = profile(tmp_path, first), profile(tmp_path, second)
    assert not validate_instance(p1, {})
    assert validate_instance(p2, {})
    assert not validate_instance(p1, {})


def test_invalid_fragment_is_preflighted(tmp_path):
    criteria = snapshot(tmp_path, {"if": False, "then": {"$ref": "#/missing"}})
    with pytest.raises(ValueError, match="invalid pinned schema reference"):
        profile(tmp_path, criteria)


@pytest.mark.parametrize("schema", [
    {"$ref": "https://example.invalid/schema"},
    {"$id": "https://example.invalid/schema"},
    {"$dynamicRef": "#node"},
    {"type": "invalid-type"},
])
def test_unsupported_schema_fails_closed(tmp_path, schema):
    with pytest.raises(ValueError):
        profile(tmp_path, snapshot(tmp_path, schema))


def test_validation_run_threads_pinned_type_and_schema(tmp_path):
    note = tmp_path / "kb/notes/fixture.md"
    data = b"---\ntype: types/fixture.md\ndescription: Fixture\n---\n# Fixture\n"
    good = ValidationRun(tmp_path, (note,), content_overrides={note: data},
                         criteria=snapshot(tmp_path, {"type": "object"}))
    bad = ValidationRun(tmp_path, (note,), content_overrides={note: data},
                        criteria=snapshot(tmp_path, {"required": ["absent"]}))
    assert not good.validate(note).fails
    assert bad.validate(note).fails
    assert not good.validate(note).fails
    assert good.parse_note(note)[0].note_type == "pinned"


def test_virtual_verbatim_sources_require_supplied_bytes(tmp_path):
    note = tmp_path / "kb/notes/fixture.md"
    data = (b"---\ntype: types/fixture.md\ndescription: Fixture\n---\n# Fixture\n\n"
            b'It states, verbatim, "source text" ([source](./source.md)).\n')
    source = note.parent / "source.md"
    run = ValidationRun(tmp_path, (note,), content_overrides={note: data, source: b"source text\n"},
                        criteria=snapshot(tmp_path, {"type": "object"}))
    parsed, error = run.parse_note(note)
    assert error is None
    assert [quote.status for quote in run.verbatim_quotes(parsed)] == ["match"]
    missing = ValidationRun(tmp_path, (note,), content_overrides={note: data},
                            criteria=snapshot(tmp_path, {"type": "object"}))
    source.parent.mkdir(parents=True)
    source.write_text("source text\n")
    assert any("verbatim quote cannot be verified" in failure for failure in missing.validate(note).fails)


def test_public_adapter_missing_substantive_criterion(tmp_path):
    result = validate_pinned_artifact_snapshot(
        repo=tmp_path, artifact_type=ANALYSIS_TYPE, intended_artifact_path=Path("kb/agentic-system-analyses/state/local/artifact"),
        members={}, manifest=b"type: ignored\n", criteria={},
    )
    assert any("missing pinned criterion" in failure for failure in result.fails)


def test_public_adapter_checks_exact_members_and_cross_member_identity(tmp_path):
    from hashlib import sha256

    from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE

    # Keep the shipped layout, but use minimal schemas to isolate the adapter.
    library = Path(__file__).resolve().parents[3] / "kb"
    criteria = {
        ANALYSIS_TYPE: (library / ANALYSIS_TYPE).read_bytes(),
        ANALYSIS_TYPE.removesuffix(".md") + ".schema.yaml": b"type: object\n",
        "agentic-system-analyses/COLLECTION.md": b"# Fixture collection\n",
        "reference/validation-contract.md": b"# Fixture validation contract\n",
        "types/type-spec.md": TYPE.replace(b"./fixture.schema.yaml", b"./type-spec.schema.yaml"),
        "types/type-spec.schema.yaml": b"type: object\n",
    }
    members = {}
    for role, type_name in (("boundary", "agentic-system-boundary"),
                            ("overview", "agentic-system-analysis-overview")):
        type_path = f"agentic-system-analyses/types/{type_name}.md"
        criteria[type_path] = TYPE.replace(b"name: pinned", f"name: {type_name}".encode())
        criteria["agentic-system-analyses/types/fixture.schema.yaml"] = b"type: object\n"
        data = (f"---\ntype: {type_path}\ndescription: Fixture\nrun-id: fixture\n"
                f"result-disposition: blocked\n---\n# {role}\n").encode()
        if role == "overview":
            data += b"\n## Members\n\n[Boundary](./boundary.md)\n"
        members[role + ".md"] = data

    directory = tmp_path / "kb/agentic-system-analyses/state/fixture/artifact"
    directory.mkdir(parents=True)
    (directory / "unrelated.md").write_text("--- invalid untracked file")

    def validate():
        manifest = yaml.safe_dump({
            "type": ANALYSIS_TYPE,
            "members": {name: {"sha256": sha256(data).hexdigest()}
                        for name, data in members.items()},
        }).encode()
        return validate_pinned_artifact_snapshot(
            repo=tmp_path, artifact_type=ANALYSIS_TYPE, intended_artifact_path=directory, members=members,
            manifest=manifest, criteria=criteria,
        )

    assert not validate().fails
    members["overview.md"] = members["overview.md"].replace(b"run-id: fixture", b"run-id: changed")
    assert any("identity field run-id" in failure for failure in validate().fails)
    members["overview.md"] = members["overview.md"].replace(b"run-id: changed", b"run-id: fixture")
    members["overview.md"] += b"\n> source text\n> --- `README.md`\n"
    assert any("quotations need the boundary" in failure for failure in validate().fails)
    del criteria["agentic-system-analyses/types/fixture.schema.yaml"]
    assert any("missing pinned criterion" in failure for failure in validate().fails)


def test_frozen_git_reader_uses_committed_objects_not_checkout(tmp_path, monkeypatch):
    import subprocess

    from commonplace.lib.quote_grounding import FrozenGitObjects
    from commonplace.lib.quote_matching import Citation

    revision = "a" * 40
    source = FrozenGitObjects({"kind": "git", "path": str(tmp_path),
                                "identity": "https://github.com/fixture/repo", "revision": revision})
    (tmp_path / "tracked.md").write_text("mutated checkout text")
    (tmp_path / "untracked.md").write_text("untracked text")
    calls = []

    def git(*args):
        calls.append(args)
        if args == ("rev-parse", "HEAD"):
            return subprocess.CompletedProcess(args, 0, (revision + "\n").encode(), b"")
        if args == ("cat-file", "-t", revision + ":tracked.md"):
            return subprocess.CompletedProcess(args, 0, b"blob\n", b"")
        if args == ("cat-file", "blob", revision + ":tracked.md"):
            return subprocess.CompletedProcess(args, 0, b"committed text", b"")
        return subprocess.CompletedProcess(args, 1, b"", b"missing")

    monkeypatch.setattr(source, "_git", git)
    assert source.read(Citation("", "tracked.md")).text == "committed text"
    assert source.read(Citation("", "untracked.md")).error
    assert source.read(Citation("", "../escape.md")).error
    assert not any("untracked" in str(args) and args[:2] == ("cat-file", "blob") for args in calls)


def test_pinned_read_cannot_load_unrelated_document(tmp_path):
    file = tmp_path / "kb/unrelated.md"
    file.parent.mkdir(parents=True)
    file.write_text("# Unrelated\n")
    run = ValidationRun(tmp_path, (), criteria=CriterionSnapshot(tmp_path / "kb", {}))
    with pytest.raises(FileNotFoundError, match="missing pinned criterion"):
        run.read_bytes(file)
