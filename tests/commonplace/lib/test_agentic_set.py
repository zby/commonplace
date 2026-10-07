from commonplace.lib import agentic_set
from commonplace.lib.directory_layout import Finding, layout_findings
from commonplace.lib.note_parser import parse_document


def document(values: str):
    parsed, error = parse_document(f"---\n{values}\n---\n# Member\n")
    assert error is None and parsed is not None
    return parsed


def test_identity_findings_belong_to_the_member_that_disagrees() -> None:
    layout = agentic_set.analysis_layout()
    types = {role.path: role.type for role in layout.roles.values()}
    members = {
        "boundary.md": document(f"type: {types['boundary.md']}\nrun-id: R\nreviewed-boundary: B\nresult-disposition: complete"),
        "runtime.md": document(f"type: {types['runtime.md']}\nrun-id: R\nreviewed-boundary: other"),
        "memory.md": document(f"type: {types['memory.md']}\nrun-id: R\nreviewed-boundary: B\nsource-identity: s"),
        "epistemic.md": document(f"type: {types['epistemic.md']}\nrun-id: other\nreviewed-boundary: B"),
        "memory-profile.md": document(
            f"type: {types['memory-profile.md']}\nrun-id: R\nreviewed-boundary: B\nsource-identity: t"),
    }
    findings = [finding for finding in layout_findings(layout, members) if not finding.absent]
    assert findings == [
        Finding("runtime", "runtime.md: identity field reviewed-boundary 'other' does not match boundary.md; expected 'B'"),
        Finding("epistemic", "epistemic.md: identity field run-id 'other' does not match boundary.md; expected 'R'"),
        Finding("memory-profile", "memory-profile.md: identity field source-identity 't' does not match memory.md; expected 's'"),
    ]


def test_the_profile_cannot_cite_a_source_directly() -> None:
    layout = agentic_set.analysis_layout()
    assert "boundary" not in layout.roles["memory-profile"].cites
    assert set(layout.roles["overview"].cites) == {"boundary", "runtime", "memory", "epistemic"}


def test_verifications_can_cite_the_members_they_judge() -> None:
    layout = agentic_set.analysis_layout()
    assert set(layout.roles["record-verification"].cites) == {
        "boundary", "runtime", "memory", "epistemic", "reconciliation",
    }
    assert set(layout.roles["profile-verification"].cites) == {
        "runtime", "memory", "epistemic", "memory-profile",
    }
    assert set(layout.roles["synthesis-verification"].cites) == {
        "boundary", "runtime", "memory", "epistemic", "synthesis",
    }


def test_boundary_disposition_selects_roles_before_overview_exists() -> None:
    layout = agentic_set.analysis_layout()
    assert layout.required.by_role == "boundary"
    assert layout.required.by_field == "result-disposition"
    for disposition in ("complete", "blocked", "out-of-scope"):
        members = {"boundary.md": document(f"result-disposition: {disposition}")}
        required, permitted = layout.requirement(members)
        expected = set(layout.roles) if disposition == "complete" else {"boundary", "overview"}
        assert required == permitted == expected
        # The overview repeats the boundary's disposition; it does not select roles.
        members["overview.md"] = document("result-disposition: complete")
        assert layout.requirement(members) == (expected, expected)
