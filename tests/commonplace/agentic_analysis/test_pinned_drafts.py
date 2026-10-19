"""Closed local draft snapshots: no models, acquisition or publication."""
from pathlib import Path

import pytest

from commonplace.lib.agentic_analysis.analyses import ANALYSIS_TYPE
from commonplace.lib.agentic_analysis.workflow import Method
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


def test_criteria_are_the_pinned_groups_plus_the_types_closure():
    method = Method(LIBRARY)
    pinned = method.criteria()
    grouped = {path for group in method.groups.values() for path in group.values()}
    assert grouped <= pinned.keys()
    member_types = {role.type for role in method.layout.roles.values()}
    schemas = {path.removesuffix(".md") + ".schema.yaml" for path in member_types | {ANALYSIS_TYPE}}
    assert member_types | schemas | {ANALYSIS_TYPE, "types/note.schema.yaml"} <= pinned.keys()
    assert not any(path.startswith("work/") for path in pinned)
    assert all(data == (LIBRARY / path).read_bytes() for path, data in pinned.items())


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


def test_candidate_review_forwards_pinned_criteria_snapshot_and_source(tmp_path, monkeypatch):
    from commonplace.lib.agentic_analysis import checks as module
    from commonplace.lib.agentic_analysis.analyses import analysis_layout

    source = {"kind": "capture", "identity": "fixture", "revision": "pin", "path": str(tmp_path)}
    boundary = ("---\nsource:\n  kind: capture\n  identity: fixture\n  revision: pin\n"
                f"  path: {tmp_path}\n---\n# Boundary\n").encode()
    pinned = criteria()
    run_values = {"source-identity": "fixture", "run-id": tmp_path.name}
    seen = []

    def validate(*args, **kwargs):
        seen.append((args, kwargs))
        return []

    monkeypatch.setattr(module, "validate_draft_in_role", validate)
    monkeypatch.setattr(module, "frozen_source_refusals", lambda _: [])
    check = module.Candidate("reconciliation", CANDIDATE, {"boundary.md": boundary}, tmp_path, source,
                             run_dir=tmp_path, layout=analysis_layout(), type_spec=ANALYSIS_TYPE,
                             criteria=pinned, run_values=run_values)
    assert module.review(check) == []
    args, kwargs = seen[0]
    assert args[2] == CANDIDATE
    assert kwargs["members"] == {"boundary.md": boundary}
    assert kwargs["criteria"] == pinned
    assert kwargs["frozen_source"] == source
    assert kwargs["run_values"] == {"source-identity": "fixture", "run-id": tmp_path.name}


def test_the_type_closure_follows_library_root_schema_references(tmp_path):
    import yaml

    from commonplace.lib.agentic_analysis.checks import type_closure

    types = tmp_path / "kb" / "types"
    types.mkdir(parents=True)
    (types / "toy-report.md").write_text(
        "---\ntype: types/type-spec.md\nname: toy-report\ndescription: Fixture\n"
        "schema: ./toy-report.schema.yaml\n---\n# Toy report\n", encoding="utf-8")
    (types / "base.schema.yaml").write_text(yaml.safe_dump({"type": "object"}), encoding="utf-8")
    schema = {"type": "object", "allOf": [{"$ref": "commonplace:types/base.schema.yaml#/definitions/x"}]}
    (types / "toy-report.schema.yaml").write_text(yaml.safe_dump(schema), encoding="utf-8")
    closure = type_closure(tmp_path / "kb", ["types/toy-report.md"])
    assert closure == ["types/toy-report.md", "types/toy-report.schema.yaml", "types/base.schema.yaml"]
