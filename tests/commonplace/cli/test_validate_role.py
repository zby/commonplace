"""Draft-in-role CLI integration; no workflow/job acceptance is implied."""
from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from commonplace.cli import validate_notes
from commonplace.lib.directory_layout import Finding
from commonplace.lib.validation import validate_draft_in_role
from tests.commonplace.agentic_analysis.fixtures import member_fixture

pytestmark = pytest.mark.usefixtures("tmp_library")


def snapshot(root: Path) -> dict:
    return {
        str(path.relative_to(root)): (path.read_bytes(), path.stat().st_mtime_ns)
        for path in root.rglob("*") if path.is_file()
    }


def member_artifact(root: Path) -> tuple[Path, Path]:
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
    directory, candidate = member_artifact(tmp_path)
    monkeypatch.chdir(tmp_path)
    expected = validate_draft_in_role(directory, "main", candidate, repo_root=tmp_path)
    expected = [finding for finding in expected if not finding.absent and not finding.warn]
    assert expected
    before = snapshot(tmp_path)
    argv = [str(candidate), "--artifact", str(directory), "--role", "main"]
    if full:
        argv.append("--full")
    assert validate_notes.main(argv) == 1
    assert capsys.readouterr().out.rstrip() == "\n".join(
        "[artifact] " + finding.render() for finding in expected
    ).rstrip()
    assert snapshot(tmp_path) == before
    assert all(finding.role == "main" for finding in expected)


def test_member_json_retains_repairs_and_does_not_write_receipt(tmp_path, monkeypatch, capsys):
    directory, candidate = member_artifact(tmp_path)
    monkeypatch.chdir(tmp_path)
    before = snapshot(tmp_path)
    assert validate_notes.main([
        str(candidate), "--artifact", str(directory), "--role", "main", "--json",
    ]) == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload["schema"] == "commonplace.validation.role-draft.v1"
    assert payload["scope"] == "content in the role; invocation residue not checked"
    assert payload["diagnostics"]
    assert all(item["role"] == "main" and item["repair"] for item in payload["diagnostics"])
    assert snapshot(tmp_path) == before


def test_clean_draft_is_only_a_content_pass(tmp_path, monkeypatch, capsys):
    directory, candidate = member_artifact(tmp_path)
    candidate.write_text((directory / "main.md").read_text())
    monkeypatch.chdir(tmp_path)
    before = snapshot(tmp_path)
    assert validate_notes.main([
        str(candidate), "--artifact", str(directory), "--role", "main",
    ]) == 0
    assert "not job acceptance" in capsys.readouterr().out
    assert snapshot(tmp_path) == before
    assert not (directory / "later.md").exists()


@pytest.mark.parametrize("flags", [
    ["--artifact", "set"],
    ["--role", "main"],
    ["--artifact", "set", "--role", "main", "--json", "--output", "receipt.json"],
])
def test_invalid_flag_combinations_refuse_before_library_call(tmp_path, monkeypatch, flags):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(validate_notes, "validate_draft_in_role", lambda *a, **kw: pytest.fail("called"))
    with pytest.raises(SystemExit) as error:
        validate_notes.main(["draft.md", *flags])
    assert error.value.code == 2
    assert not (tmp_path / "receipt.json").exists()


@pytest.mark.parametrize("role", ["../main", "/tmp/main", "child/main", "."])
def test_role_must_be_a_plain_name(tmp_path, monkeypatch, capsys, role):
    monkeypatch.chdir(tmp_path)
    assert validate_notes.main(["draft.md", "--artifact", "set", "--role", role]) == 2
    assert "must name a role" in capsys.readouterr().err


def test_unknown_role_or_missing_draft_is_a_check_error(tmp_path, monkeypatch, capsys):
    directory, candidate = member_artifact(tmp_path)
    monkeypatch.chdir(tmp_path)
    assert validate_notes.main([
        str(candidate), "--artifact", str(directory), "--role", "undeclared",
    ]) == 2
    assert "not a role the artifact type declares" in capsys.readouterr().err
    assert validate_notes.main([
        "missing.md", "--artifact", str(directory), "--role", "main",
    ]) == 2
    assert "role validation:" in capsys.readouterr().err


@pytest.mark.parametrize("role", [
    "boundary", "runtime", "memory", "epistemic", "reconciliation",
    "memory-profile", "report-verification", "profile-verification",
    "synthesis", "synthesis-verification", "overview",
])
def test_analysis_role_cli_matches_shared_validator(tmp_path, monkeypatch, capsys, role):
    """Validate each declared member directly, without executing workflow jobs."""
    directory = member_fixture(tmp_path) / "artifact"
    candidate = tmp_path / "draft.md"
    monkeypatch.chdir(tmp_path)
    for content in ("invalid draft\n", (directory / f"{role}.md").read_text()):
        candidate.write_text(content)
        expected = validate_draft_in_role(directory, role, candidate, repo_root=tmp_path)
        before = snapshot(tmp_path)
        validate_notes.main([
            str(candidate), "--artifact", str(directory), "--role", role, "--json",
        ])
        payload = json.loads(capsys.readouterr().out)
        assert [item["text"] for item in payload["diagnostics"]] == [
            "[artifact] " + finding.render() for finding in expected if not finding.absent
        ]
        assert snapshot(tmp_path) == before


def test_absent_is_deliberately_dropped_but_unverified_refuses(tmp_path, monkeypatch, capsys):
    findings = [
        Finding("main", "main.md: required member is absent", absent=True),
        Finding("main", "main.md: advisory", warn=True),
        Finding("main", "main.md: quotation unverified", info=True),
    ]
    monkeypatch.setattr(validate_notes, "validate_draft_in_role", lambda *a, **kw: findings)
    assert validate_notes.check_role_draft(
        tmp_path / "draft.md", directory=tmp_path / "artifact", role="main", repo_root=tmp_path,
    ) == 1
    output = capsys.readouterr().out
    assert "absent" not in output
    assert "WARN: [artifact] " + findings[1].render() in output
    assert "[artifact] " + findings[2].render() in output


def test_an_engine_run_s_artifact_is_checked_against_the_run_values(tmp_path, monkeypatch, capsys):
    run = tmp_path / "AAS-run-01"
    (run / "artifact").mkdir(parents=True)
    (run / "run.json").write_text(json.dumps({"parameters": {"source-identity": "fixture"}}))
    seen = []
    monkeypatch.setattr(validate_notes, "validate_draft_in_role", lambda *a, **kw: seen.append(kw) or [])
    for directory in (run / "artifact", tmp_path / "elsewhere"):
        validate_notes.check_role_draft(tmp_path / "draft.md", directory=directory, role="memory",
                                        repo_root=tmp_path)
    assert [kw["run_values"] for kw in seen] == [{"source-identity": "fixture", "run-id": "AAS-run-01"}, None]
