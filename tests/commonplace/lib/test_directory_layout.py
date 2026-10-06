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
    "required": {"always": ["head"], "by": {"role": "head", "field": "state", "values": {"done": ["body"]}}},
}


def document(values: str):
    parsed, error = parse_document(f"---\n{values}\n---\n# Member\n")
    assert error is None and parsed is not None
    return parsed


def test_a_finished_value_requires_its_roles() -> None:
    layout = parse_layout(LAYOUT)
    findings = layout_findings(layout, {"head.md": document("type: t/head.md\nstate: done")})
    assert findings == [Finding("body", "body.md: required member is absent")]


def test_another_value_admits_only_the_roles_always_required() -> None:
    layout = parse_layout(LAYOUT)
    findings = layout_findings(layout, {
        "head.md": document("type: t/head.md\nstate: blocked\nrun: R"),
        "body.md": document("type: t/body.md\nrun: R"),
    })
    assert findings == [Finding("body", "body.md: not a member when head.md state is 'blocked'")]


def test_an_incomplete_instance_reports_absence_and_checks_what_is_present() -> None:
    layout = parse_layout(LAYOUT)
    findings = layout_findings(layout, {
        "body.md": document("type: t/other.md\nrun: R"),
        "notes.md": document("type: t/notes.md"),
    })
    assert findings == [
        Finding(None, "notes.md: no layout role; this type has closed membership"),
        Finding("head", "head.md: required member is absent"),
        Finding("body", "body.md: type 't/other.md' does not match the layout's t/body.md"),
    ]


def test_open_membership_admits_unmatched_files() -> None:
    layout = parse_layout({**LAYOUT, "membership": "open", "required": {}})
    assert layout_findings(layout, {"notes.md": document("type: t/notes.md")}) == []


@pytest.mark.parametrize("change, error", [
    ({"membership": "sealed"}, "membership"),
    ({"roles": {"a": {"path": "sub/a.md", "type": "t/a.md"}}}, "direct Markdown file"),
    ({"roles": {"a": {"path": "a.md", "type": "t/a.md", "cites": ["b"]}}}, "unknown role 'b'"),
    ({"required": {"always": ["missing"]}}, "unknown role 'missing'"),
])
def test_layout_defects_are_named(change: dict, error: str) -> None:
    with pytest.raises((ValueError, TypeError), match=error):
        parse_layout({**LAYOUT, **change})
