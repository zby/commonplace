"""Shared nonwriting draft validation and the analysis judgment relations."""
from hashlib import sha256

import pytest
import yaml

from commonplace.lib.agentic_analysis.analyses import analysis_layout
from commonplace.lib.agentic_analysis.rules import validate_analysis_artifact
from commonplace.lib.directory_artifact import ArtifactMember, DirectoryArtifact
from commonplace.lib.directory_layout import layout_findings
from commonplace.lib.note_parser import parse_document
from commonplace.lib.validation import ValidationRun, validate_draft_in_role


def document(body, **metadata):
    parsed, error = parse_document("---\n" + yaml.safe_dump(metadata) + "---\n" + body)
    assert error is None and parsed is not None
    return parsed


@pytest.fixture
def draft_artifact(tmp_path, tmp_library):
    note_types = tmp_path / "kb/types"
    note_types.mkdir(parents=True)
    (note_types / "note.md").write_text(
        "---\ntype: types/type-spec.md\nname: note\ndescription: Example note\nschema: null\n---\n# Note\n"
    )
    types = tmp_path / "kb/reports/types"
    types.mkdir(parents=True)
    (types.parent / "COLLECTION.md").write_text("# Reports\n")
    layout = {
        "membership": "closed", "roles": {
            "head": {"path": "head.md", "type": "types/note.md"},
            "body": {"path": "body.md", "type": "types/note.md",
                     "identity": [{"from": "head", "fields": ["run"]}]},
            "later": {"path": "later.md", "type": "types/note.md"},
        }, "required": {"always": ["head", "body", "later"]},
    }
    (types / "set.md").write_text("---\n" + yaml.safe_dump({
        "type": "types/type-spec.md", "name": "set", "description": "Example set",
        "schema": "./set.schema.yaml", "layout": layout,
    }) + "---\n# Set\n")
    (types / "set.schema.yaml").write_text("type: object\n")
    output = types.parent / "output"
    output.mkdir()
    (output / "ARTIFACT.yaml").write_text("type: reports/types/set.md\n")
    (output / "head.md").write_text("---\ntype: types/note.md\nrun: expected\ndescription: Head\n---\n# Head\n")
    return tmp_path, output


def test_overlay_filters_roles_and_never_writes(draft_artifact):
    root, output = draft_artifact
    incumbent = b"---\ntype: types/note.md\nrun: wrong\ndescription: Body\n---\n# Body\n"
    (output / "body.md").write_bytes(incumbent)
    draft = root / "candidate.md"
    draft.write_bytes(incumbent.replace(b"wrong", b"expected"))
    manifest = output / "ARTIFACT.yaml"
    manifest.write_text(yaml.safe_dump({"type": "reports/types/set.md", "members": {
        name: {"sha256": sha256((output / name).read_bytes()).hexdigest()}
        for name in ("head.md", "body.md")
    }}))
    before = {path: path.read_bytes() for path in output.iterdir()}
    findings = validate_draft_in_role(output, "body", draft, repo_root=root)
    assert not findings
    assert {path: path.read_bytes() for path in output.iterdir()} == before
    draft.write_bytes(incumbent)
    findings = validate_draft_in_role(output, "body", draft, repo_root=root)
    assert all(f.role == "body" for f in findings)
    assert any("identity field" in f.message for f in findings)
    assert all(f.repair and "Repair: " in f.render() for f in findings)


def test_exact_snapshot_ignores_disk_members_and_manifest(draft_artifact):
    root, output = draft_artifact
    head = (output / "head.md").read_bytes()
    candidate = b"---\ntype: types/note.md\nrun: expected\ndescription: Body\n---\n# Body\n"
    (output / "head.md").write_bytes(head.replace(b"expected", b"wrong"))
    (output / "body.md").write_text("not the candidate\n")
    (output / "intruder.md").write_text("---\ntype: [bad\n---\n")
    (output / "ARTIFACT.yaml").write_text("invalid: [manifest\n")
    before = {path: path.read_bytes() for path in output.iterdir()}
    findings = validate_draft_in_role(
        output, "body", candidate, repo_root=root, members={"head.md": head},
        manifest=b"type: reports/types/set.md\n",
    )
    assert not findings
    assert {path: path.read_bytes() for path in output.iterdir()} == before
    findings = validate_draft_in_role(
        output, "body", candidate, repo_root=root,
        members={"head.md": head.replace(b"expected", b"wrong")},
        manifest=b"type: reports/types/set.md\n",
    )
    assert any("identity field" in f.message for f in findings)


@pytest.mark.parametrize("name", ["../escape.md", ".hidden.md", "bad\\\\name.md", "not-markdown.json"])
def test_snapshot_member_names_cannot_expand_scope(draft_artifact, name):
    root, output = draft_artifact
    with pytest.raises(ValueError, match="snapshot member"):
        validate_draft_in_role(
            output, "body", b"# Body\n", repo_root=root,
            members={name: b"# Intruder\n"}, manifest=b"type: reports/types/set.md\n",
        )


def test_snapshot_requires_its_manifest_and_refuses_unreadable_candidate(draft_artifact):
    root, output = draft_artifact
    with pytest.raises(ValueError, match="explicit manifest"):
        validate_draft_in_role(output, "body", b"# Body\n", repo_root=root, members={})
    findings = validate_draft_in_role(
        output, "body", b"\xff", repo_root=root, members={},
        manifest=b"type: reports/types/set.md\n",
    )
    assert findings and all(f.role == "body" for f in findings)


def test_overlay_new_slot_and_candidate_file_failures(draft_artifact):
    root, output = draft_artifact
    draft = root / "candidate.md"
    draft.write_text("---\ntype: types/missing.md\nrun: expected\n---\n# Candidate\n")
    findings = validate_draft_in_role(output, "body", draft, repo_root=root)
    assert findings and all(f.role == "body" for f in findings)
    assert any("missing" in f.message for f in findings)
    assert not (output / "body.md").exists()


def test_bad_candidate_reports_failure_instead_of_aborting(draft_artifact):
    root, output = draft_artifact
    draft = root / "candidate.md"
    draft.write_text("---\ntype: [bad\n---\n# Candidate\n")
    findings = validate_draft_in_role(output, "body", draft, repo_root=root)
    assert findings and all(f.role == "body" for f in findings)
    assert all(f.repair for f in findings)


@pytest.mark.parametrize("role", ["../escape", "unknown"])
def test_role_must_be_declared(draft_artifact, role):
    root, output = draft_artifact
    draft = root / "candidate.md"
    draft.write_text("# Candidate\n")
    with pytest.raises(ValueError):
        validate_draft_in_role(output, role, draft, repo_root=root)


def analysis_artifact(tmp_path, documents):
    layout = analysis_layout()
    members = {}
    for name, doc in documents.items():
        path = tmp_path / layout.path(name)
        members[path.name] = ArtifactMember(path, doc.body.encode(), doc)
    return DirectoryArtifact(tmp_path, b"", {}, members)


def test_complete_requires_four_new_members_and_identity_is_from_boundary():
    layout = analysis_layout()
    new = {"synthesis", "record-verification", "profile-verification", "synthesis-verification"}
    docs = {"overview.md": document("# Entry\n", **{"result-disposition": "complete"}),
            "boundary.md": document("# Boundary\n", **{
                "run-id": "R", "reviewed-boundary": "B", "result-disposition": "complete",
            })}
    findings = layout_findings(layout, docs)
    assert new <= {f.role for f in findings if f.absent}


@pytest.mark.parametrize("name", ["record-verification", "profile-verification", "synthesis-verification"])
def test_limits_are_a_relation_owned_by_synthesis(tmp_path, name):
    layout = analysis_layout()
    documents = {
        name: document("# Judgment\n\n## Verification\nChecked.\n\n## Blockers\nnone\n\n## Limits\n"
                       "- [RT-OBJ-store](runtime.md#rt-obj-store): incomplete inspection.\n"
                       "  Withhold complete coverage.\n"),
        "synthesis": document("# Synthesis\n\n## Bounded synthesis\nAccount.\n\n## Limitations\nnone\n"),
        "runtime": document("# Runtime\n\n## Shared records\n#### RT-OBJ-store\n\nLabel: Store\n"),
    }
    artifact = analysis_artifact(tmp_path, documents)
    findings = validate_analysis_artifact(artifact, layout=layout, run=ValidationRun(tmp_path, ()))
    carried = [f for f in findings if "limit not carried" in f.message]
    assert len(carried) == 1 and carried[0].role == "synthesis"
    documents["synthesis"] = document(
        "# Synthesis\n\n## Limitations\n[RT-OBJ-store](runtime.md#rt-obj-store) has incomplete coverage.\n")
    findings = validate_analysis_artifact(analysis_artifact(tmp_path, documents), layout=layout, run=ValidationRun(tmp_path, ()))
    assert not any("limit not carried" in f.message for f in findings)


@pytest.mark.parametrize("name", ["synthesis", "record-verification", "profile-verification", "synthesis-verification"])
def test_citation_scope_is_enforced_for_new_roles(tmp_path, name):
    docs = {
        "boundary": document("# Boundary\n\n## Source register\n| SRC-1 | frozen repository |\n"),
        name: document("# Member\n\nSRC-1 supports this statement.\n"),
    }
    findings = validate_analysis_artifact(analysis_artifact(tmp_path, docs), layout=analysis_layout(), run=ValidationRun(tmp_path, ()))
    unresolved = [f for f in findings if "unresolved source SRC-1" in f.message]
    if name == "profile-verification":
        assert len(unresolved) == 1 and unresolved[0].role == name
        assert "outside" in unresolved[0].message
    else:
        assert not unresolved


def test_context_parse_failure_is_explicit_and_nonwriting(draft_artifact):
    root, output = draft_artifact
    broken = output / "later.md"
    broken.write_text("---\ntype: [broken\n---\n# Later\n")
    draft = root / "candidate.md"
    draft.write_text("---\ntype: types/note.md\nrun: expected\ndescription: Body\n---\n# Body\n")
    findings = validate_draft_in_role(output, "body", draft, repo_root=root)
    assert all(f.role == "body" for f in findings)
    assert any("artifact input cannot be checked" in f.message and "later.md" in f.message for f in findings)
    assert not (output / "body.md").exists()


def test_verification_grammar_findings_are_role_findings(tmp_path):
    docs = {"record-verification": document("# Judgment\n\n## Blockers\n- No addressee.\n\n## Limits\nprose\n")}
    findings = validate_analysis_artifact(analysis_artifact(tmp_path, docs), layout=analysis_layout(), run=ValidationRun(tmp_path, ()))
    assert len(findings) == 2
    assert all(f.role == "record-verification" for f in findings)
    assert any("addressee" in f.message for f in findings)
    assert any("Limits" in f.message for f in findings)


@pytest.fixture
def content_member_artifact(draft_artifact):
    """Use real rule dispatch with minimal type contracts and a local layout."""
    root, _ = draft_artifact
    types = root / "kb/agentic-system-analyses/types"
    types.mkdir(parents=True)
    (types.parent / "COLLECTION.md").write_text("# Analyses\n")
    roles = {}
    for role, name in (("boundary", "agentic-system-boundary"),
                       ("reconciliation", "agentic-system-reconciliation-report")):
        type_path = f"agentic-system-analyses/types/{name}.md"
        (types / f"{name}.md").write_text("---\n" + yaml.safe_dump({
            "type": "types/type-spec.md", "name": name,
            "description": "Content validation fixture", "schema": None,
        }) + "---\n# Type\n")
        roles[role] = {"path": role + ".md", "type": type_path}
    (types / "set.md").write_text("---\n" + yaml.safe_dump({
        "type": "types/type-spec.md", "name": "set", "description": "Example set",
        "schema": "./set.schema.yaml", "layout": {"membership": "closed", "roles": roles},
    }) + "---\n# Set\n")
    (types / "set.schema.yaml").write_text("type: object\n")
    output = types.parent / "output"
    output.mkdir()
    (output / "ARTIFACT.yaml").write_text("type: agentic-system-analyses/types/set.md\n")
    return root, output


def content_checks(content_member_artifact, role, body, **metadata):
    root, output = content_member_artifact
    name = {"boundary": "agentic-system-boundary",
            "reconciliation": "agentic-system-reconciliation-report"}[role]
    content = "---\n" + yaml.safe_dump({
        "type": f"agentic-system-analyses/types/{name}.md",
        "description": "Content validation fixture", **metadata,
    }) + "---\n# Member\n\n" + body
    incumbent = output / (role + ".md")
    incumbent.write_text(content)
    candidate = root / "candidate.md"
    candidate.write_text(content)
    before = {path: path.read_bytes() for path in output.iterdir()}
    standalone = ValidationRun(root, ()).validate(incumbent)
    draft = validate_draft_in_role(output, role, candidate, repo_root=root)
    assert {path: path.read_bytes() for path in output.iterdir()} == before
    assert all(f.role == role and f.repair for f in draft)
    # A defect must travel unchanged from the standalone type rule to the role.
    for message in standalone.fails:
        assert any(message in f.message for f in draft)
    return standalone.fails


def source_row(kind="git", identity="https://example.org/repo", revision="a" * 40):
    return f"| SRC-1 | `{kind}` | `{identity}` | `{revision}` | code | whole | frozen | limits |\n"


@pytest.mark.parametrize("kind,revision", [("git", "a" * 40), ("capture", "capture-2026")])
def test_boundary_register_matches_git_or_capture(content_member_artifact, kind, revision):
    errors = content_checks(content_member_artifact, "boundary", "## Source register\n" + source_row(kind, revision=revision),
                            source={"kind": kind, "identity": "https://example.org/repo", "revision": revision})
    assert not errors


@pytest.mark.parametrize("defect", ["shape", "missing", "kind", "identity", "revision", "duplicate"])
def test_boundary_register_content_defects(content_member_artifact, defect):
    row = source_row()
    if defect == "shape":
        row = row.replace(" | limits", "")
    elif defect == "missing":
        row = "none\n"
    elif defect == "duplicate":
        row += row
    else:
        replacements = {"kind": ("`git`", "`capture`"),
                        "identity": ("https://example.org/repo", "https://example.org/other"),
                        "revision": ("a" * 40, "b" * 40)}
        row = row.replace(*replacements[defect])
    errors = content_checks(content_member_artifact, "boundary", "## Source register\n" + row,
                            source={"kind": "git", "identity": "https://example.org/repo", "revision": "a" * 40})
    expected = {"shape": "all eight columns", "duplicate": "duplicate source declaration"}.get(
        defect, "source register must declare the frozen source")
    assert any(expected in error for error in errors)


def test_boundary_register_checks_shape_and_duplicates_without_frozen_source(content_member_artifact):
    errors = content_checks(content_member_artifact, "boundary", "## Source register\n| SRC-1 | short |\n| SRC-1 | short |\n", source=None)
    assert sum("all eight columns" in error for error in errors) == 2
    assert sum("duplicate source declaration" in error for error in errors) == 1
    assert not any("must declare the frozen source" in error for error in errors)


def test_boundary_register_ignores_quoted_and_fenced_examples(content_member_artifact):
    row = source_row()
    body = "## Source register\n" + row + "> | SRC-1 | short |\n\n```markdown\n" + row + "```\n"
    assert not content_checks(content_member_artifact, "boundary", body,
                              source={"kind": "git", "identity": "https://example.org/repo", "revision": "a" * 40})


@pytest.mark.parametrize("amendment,refused", [
    ("Amendment: RT-OBJ-store has a new value.", True),
    ("Amendment: RT-OBJ-store\nis superseded by MEM-OBJ-store.", False),
    ("> Amendment: RT-OBJ-store has a new value.", False),
    ("```markdown\nAmendment: RT-OBJ-store has a new value.\n```", False),
])
def test_reconciliation_value_amendments_are_content_findings(content_member_artifact, amendment, refused):
    errors = content_checks(content_member_artifact, "reconciliation", "## Reconciliation\n\n" + amendment + "\n")
    assert any("value amendment: reconciliation states connections between reports" in error for error in errors) == refused


def test_overview_has_links_not_copy_relations(tmp_path):
    docs = {
        "boundary": document("# Boundary\n\n## Boundary and evidence\nOriginal boundary.\n\n## Source register\nnone\n"),
        "overview": document("# Entry\n\n## Members\n[Boundary](boundary.md)\n\n## Amendment index\nNot reached.\n\n## Deterministic validation\nChecked.\n"),
    }
    findings = validate_analysis_artifact(analysis_artifact(tmp_path, docs), layout=analysis_layout(), run=ValidationRun(tmp_path, ()))
    assert not findings
