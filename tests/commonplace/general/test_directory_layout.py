import pytest

from commonplace.lib.directory_layout import Finding, layout_findings, parse_layout
from commonplace.lib.note_parser import parse_document

LAYOUT = {
    "membership": "closed",
    "roles": {
        "head": {"path": "head.md", "type": "t/head.md"},
        "body": {"path": "body.md", "type": "t/body.md",
                 "identity": [{"from": "head", "fields": ["run"]}], "cites": ["head", "body"]},
    },
    "required": {"always": ["head"], "when": {"role": "head", "field": "state", "values": {"done": ["body"]}}},
}


def document(values: str):
    parsed, error = parse_document(f"---\n{values}\n---\n# Member\n")
    assert error is None and parsed is not None
    return parsed


def test_an_incomplete_instance_reports_absence_and_checks_what_is_present() -> None:
    layout = parse_layout(LAYOUT)
    findings = layout_findings(layout, {
        "body.md": document("type: t/other.md\nrun: R"),
        "notes.md": document("type: t/notes.md"),
    })
    assert findings == [
        Finding(None, "notes.md: no layout role; this type has closed membership"),
        Finding("head", "head.md: required member is absent", absent=True),
        Finding("body", "body.md: type 't/other.md' does not match the layout's t/body.md"),
        Finding("body", "body.md: cannot check identity fields run; source member head.md is absent"),
    ]


def test_missing_identity_source_is_a_dependent_finding_even_when_optional() -> None:
    layout = parse_layout({**LAYOUT, "required": {}})
    findings = layout_findings(layout, {"body.md": document("type: t/body.md\nrun: R")})
    assert findings == [Finding(
        "body", "body.md: cannot check identity fields run; source member head.md is absent",
    )]
    # This is a blocked comparison, not an absent candidate to discard mid-run.
    assert not findings[0].absent


@pytest.mark.parametrize("change, error", [
    ({"membership": "sealed"}, "membership"),
    ({"roles": {"a": {"path": "sub/a.md", "type": "t/a.md"}}}, "direct Markdown file"),
    ({"roles": {"a": {"path": "a.md", "type": "t/a.md", "cites": ["b"]}}}, "unknown role 'b'"),
    ({"roles": {"a": {"path": "a.md", "type": "t/a.md", "verifies": ["b"]}}}, "unknown role 'b'"),
    ({"roles": {"a": {"path": "a.md", "type": "t/a.md", "verifies": ["a"]}}}, "cannot verify itself"),
    ({"required": {"always": ["missing"]}}, "unknown role 'missing'"),
])
def test_layout_defects_are_named(change: dict, error: str) -> None:
    with pytest.raises((ValueError, TypeError), match=error):
        parse_layout({**LAYOUT, **change})


def test_a_run_source_binds_fields_to_the_run_values_when_given() -> None:
    layout = parse_layout({**LAYOUT, "roles": {**LAYOUT["roles"], "head": {
        "path": "head.md", "type": "t/head.md", "identity": [{"from": "run", "fields": ["run"]}]}}})
    assert layout.roles["head"].run_identity == ("run",) and layout.roles["head"].identity == ()
    members = {"head.md": document("type: t/head.md\nstate: blocked\nrun: R")}
    assert layout_findings(layout, members) == []  # Outside a run nothing binds.
    assert layout_findings(layout, members, {"run": "R"}) == []
    findings = layout_findings(layout, members, {"run": "S"})
    assert findings == [Finding("head", "head.md: identity field run 'R' does not match the run; expected 'S'")]
    assert "the run's value" in findings[0].repair
