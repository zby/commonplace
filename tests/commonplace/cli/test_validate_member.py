"""Draft-at-slot CLI integration; no workflow/job acceptance is implied."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from commonplace.cli import validate_notes
from commonplace.lib.directory_layout import Finding
from commonplace.lib.validation import validate_draft_at_slot
from tests.commonplace.lib.test_agentic_analysis import member_fixture

pytestmark = pytest.mark.usefixtures("tmp_library")


def snapshot(root: Path) -> dict:
    return {
        str(path.relative_to(root)): (path.read_bytes(), path.stat().st_mtime_ns)
        for path in root.rglob("*") if path.is_file()
    }


def member_set(root: Path) -> tuple[Path, Path]:
    types = root / "kb/reports/types"
    types.mkdir(parents=True)
    (root / "kb/reports/COLLECTION.md").write_text("# Reports\n")
    layout = {
        "membership": "closed",
        "roles": {
            "main": {"path": "main.md", "type": "reports/types/member.md"},
            "later": {"path": "later.md", "type": "reports/types/member.md"},
        },
        "required": {"always": ["main", "later"]},
    }
    (types / "set.md").write_text("---\n" + yaml.safe_dump({
        "type": "types/type-spec.md", "name": "set", "description": "Example set",
        "schema": "./set.schema.yaml", "layout": layout,
    }) + "---\n# Set\n")
    (types / "set.schema.yaml").write_text("type: object\n")
    (types / "member.md").write_text(
        "---\ntype: types/type-spec.md\nname: member\ndescription: Example member\n"
        "schema: ./member.schema.yaml\n---\n# Member\n"
    )
    (types / "member.schema.yaml").write_text(yaml.safe_dump({
        "type": "object",
        "properties": {"frontmatter": {
            "type": "object", "required": ["description"],
            "properties": {"description": {"type": "string"}},
        }},
    }))
    directory = root / "kb/reports/retained/example"
    directory.mkdir(parents=True)
    (directory / "ARTIFACT.yaml").write_text("type: reports/types/set.md\n")
    (directory / "main.md").write_text(
        "---\ntype: reports/types/member.md\ndescription: Incumbent\n---\n# Main\n"
    )
    candidate = root / "scratch/draft.md"
    candidate.parent.mkdir()
    candidate.write_text("---\ntype: reports/types/member.md\n---\n# Main\n")
    return directory, candidate


@pytest.mark.parametrize("full", [False, True])
def test_cli_uses_shared_findings_and_writes_nothing(tmp_path, monkeypatch, capsys, full):
    directory, candidate = member_set(tmp_path)
    monkeypatch.chdir(tmp_path)
    expected = validate_draft_at_slot(directory, "main.md", candidate, repo_root=tmp_path)
    expected = [finding for finding in expected if not finding.absent and not finding.warn]
    assert expected
    before = snapshot(tmp_path)
    argv = [str(candidate), "--set", str(directory), "--member", "main.md"]
    if full:
        argv.append("--full")
    assert validate_notes.main(argv) == 1
    assert capsys.readouterr().out.rstrip() == "\n".join(
        "[set] " + finding.render() for finding in expected
    ).rstrip()
    assert snapshot(tmp_path) == before
    assert all(finding.role == "main" for finding in expected)


def test_member_json_retains_repairs_and_does_not_write_receipt(tmp_path, monkeypatch, capsys):
    directory, candidate = member_set(tmp_path)
    monkeypatch.chdir(tmp_path)
    before = snapshot(tmp_path)
    assert validate_notes.main([
        str(candidate), "--set", str(directory), "--member", "main.md", "--json",
    ]) == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload["schema"] == "commonplace.validation.member.v1"
    assert payload["scope"] == "member content; invocation residue not checked"
    assert payload["diagnostics"]
    assert all(item["role"] == "main" and item["repair"] for item in payload["diagnostics"])
    assert snapshot(tmp_path) == before


def test_clean_draft_is_only_a_content_pass(tmp_path, monkeypatch, capsys):
    directory, candidate = member_set(tmp_path)
    candidate.write_text((directory / "main.md").read_text())
    monkeypatch.chdir(tmp_path)
    before = snapshot(tmp_path)
    assert validate_notes.main([
        str(candidate), "--set", str(directory), "--member", "main.md",
    ]) == 0
    assert "not job acceptance" in capsys.readouterr().out
    assert snapshot(tmp_path) == before
    assert not (directory / "later.md").exists()


@pytest.mark.parametrize("flags", [
    ["--set", "set"],
    ["--member", "main.md"],
    ["--set", "set", "--member", "main.md", "--json", "--output", "receipt.json"],
])
def test_invalid_flag_combinations_refuse_before_library_call(tmp_path, monkeypatch, flags):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validate_notes, "validate_draft_at_slot", lambda *a, **kw: pytest.fail("called"))
    with pytest.raises(SystemExit) as error:
        validate_notes.main(["draft.md", *flags])
    assert error.value.code == 2
    assert not (tmp_path / "receipt.json").exists()


@pytest.mark.parametrize("slot", ["../main.md", "/tmp/main.md", "child/main.md", "."])
def test_slot_must_be_relative_and_direct(tmp_path, monkeypatch, capsys, slot):
    monkeypatch.chdir(tmp_path)
    assert validate_notes.main(["draft.md", "--set", "set", "--member", slot]) == 2
    assert "relative member filename" in capsys.readouterr().err


def test_unknown_slot_or_missing_draft_is_a_check_error(tmp_path, monkeypatch, capsys):
    directory, candidate = member_set(tmp_path)
    monkeypatch.chdir(tmp_path)
    assert validate_notes.main([
        str(candidate), "--set", str(directory), "--member", "undeclared.md",
    ]) == 2
    assert "no declared layout role" in capsys.readouterr().err
    assert validate_notes.main([
        "missing.md", "--set", str(directory), "--member", "main.md",
    ]) == 2
    assert "member validation:" in capsys.readouterr().err


@pytest.mark.parametrize("slot", [
    "boundary.md", "runtime.md", "memory.md", "epistemic.md", "reconciliation.md",
    "memory-profile.md", "record-verification.md", "profile-verification.md",
    "synthesis.md", "synthesis-verification.md", "overview.md",
])
def test_analysis_member_cli_matches_shared_validator(tmp_path, monkeypatch, capsys, slot):
    """Validate each declared member directly, without executing workflow jobs."""
    directory = member_fixture(tmp_path) / "set"
    candidate = tmp_path / "draft.md"
    monkeypatch.chdir(tmp_path)
    for content in ("invalid draft\n", (directory / slot).read_text()):
        candidate.write_text(content)
        expected = validate_draft_at_slot(directory, slot, candidate, repo_root=tmp_path)
        before = snapshot(tmp_path)
        validate_notes.main([
            str(candidate), "--set", str(directory), "--member", slot, "--json",
        ])
        payload = json.loads(capsys.readouterr().out)
        assert [item["text"] for item in payload["diagnostics"]] == [
            "[set] " + finding.render() for finding in expected if not finding.absent
        ]
        assert snapshot(tmp_path) == before


def test_absent_is_deliberately_dropped_but_unverified_refuses(tmp_path, monkeypatch, capsys):
    findings = [
        Finding("main", "main.md: required member is absent", absent=True),
        Finding("main", "main.md: advisory", warn=True),
        Finding("main", "main.md: quotation unverified", info=True),
    ]
    monkeypatch.setattr(validate_notes, "validate_draft_at_slot", lambda *a, **kw: findings)
    assert validate_notes.check_member_draft(
        tmp_path / "draft.md", directory=tmp_path / "set", slot=Path("main.md"), repo_root=tmp_path,
    ) == 1
    output = capsys.readouterr().out
    assert "absent" not in output
    assert "WARN: [set] " + findings[1].render() in output
    assert "[set] " + findings[2].render() in output
