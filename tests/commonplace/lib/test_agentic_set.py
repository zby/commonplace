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
        "boundary.md": document(f"type: {types['boundary.md']}\nrun-id: R\nreviewed-boundary: B"),
        "runtime.md": document(f"type: {types['runtime.md']}\nrun-id: R\nreviewed-boundary: other"),
        "memory.md": document(f"type: {types['memory.md']}\nrun-id: R\nreviewed-boundary: B\nsource-identity: s"),
        "epistemic.md": document(f"type: {types['epistemic.md']}\nrun-id: other\nreviewed-boundary: B"),
        "memory-profile.md": document(
            f"type: {types['memory-profile.md']}\nrun-id: R\nreviewed-boundary: B\nsource-identity: t"),
    }
    findings = [finding for finding in layout_findings(layout, members) if finding.role != "overview"]
    assert findings == [
        Finding("runtime", "runtime.md: identity field reviewed-boundary 'other' does not match boundary.md; expected 'B'"),
        Finding("epistemic", "epistemic.md: identity field run-id 'other' does not match boundary.md; expected 'R'"),
        Finding("memory-profile", "memory-profile.md: identity field source-identity 't' does not match memory.md; expected 's'"),
    ]


def test_the_profile_cannot_cite_a_source_directly() -> None:
    layout = agentic_set.analysis_layout()
    assert "boundary" not in layout.roles["memory-profile"].cites
    assert set(layout.roles["overview"].cites) == {"boundary", "runtime", "memory", "epistemic"}
