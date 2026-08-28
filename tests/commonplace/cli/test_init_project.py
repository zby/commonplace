from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli import init_project as init_project_module
from commonplace.cli.init_project import (
    init_project,
    installation_warnings,
    main,
)
from commonplace.lib.project_paths import is_collection_dir
from commonplace.lib.validation import validate_collection_landings
from commonplace.scaffold_manifest import MANIFEST


def relative_files(root: Path) -> set[Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_file()
    }


def relative_directories(root: Path) -> set[Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_dir()
    }


def test_init_project_creates_core_layout_and_is_idempotent(tmp_path: Path) -> None:
    report = init_project(tmp_path)

    assert report.created
    assert {
        Path("kb/notes"),
        Path("kb/reference"),
        Path("kb/sources"),
        Path("kb/instructions"),
        Path("kb/reports"),
        Path("kb/types"),
        Path("kb/reports/types"),
    } <= relative_directories(tmp_path)
    assert (tmp_path / "kb" / "sources" / ".gitignore").read_text(
        encoding="utf-8"
    ) == ".snapshots/\n"
    assert (tmp_path / "kb" / "log.md").is_file()

    rerun = init_project(tmp_path)
    assert (rerun.created, bool(rerun.preserved_identical), rerun.preserved_different) == (
        [],
        True,
        [],
    )


def test_init_project_seeds_scaffold_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    files = relative_files(tmp_path)
    expected = {
        # Shipped library content.
        Path("kb/commonplace/instructions/README.md"),
        Path("kb/commonplace/instructions/COLLECTION.md"),
        Path("kb/commonplace/notes/COLLECTION.md"),
        Path("kb/commonplace/reference/COLLECTION.md"),
        Path("kb/commonplace/reference/README-REVIEW-SYSTEM.md"),
        Path("kb/commonplace/instructions/FIX-SYSTEM.md"),
        Path("kb/commonplace/instructions/cp-skill-write/SKILL.md"),
        Path("kb/commonplace/instructions/cp-skill-connect/SKILL.md"),
        Path("kb/commonplace/instructions/cp-skill-ingest/SKILL.md"),
        Path("kb/commonplace/instructions/cp-skill-health-check/SKILL.md"),
        Path("kb/commonplace/instructions/ingest-paper-with-code.md"),
        Path("kb/commonplace/instructions/draft-ingest-report.md"),
        Path("kb/commonplace/reference/README.md"),
        Path("kb/commonplace/reference/types/adr.md"),
        Path("kb/commonplace/reference/types/adr.schema.yaml"),
        # User collection landings and global types.
        Path("kb/notes/COLLECTION.md"),
        Path("kb/notes/README.md"),
        Path("kb/reference/COLLECTION.md"),
        Path("kb/reference/README.md"),
        Path("kb/instructions/COLLECTION.md"),
        Path("kb/instructions/README.md"),
        Path("kb/sources/COLLECTION.md"),
        Path("kb/sources/README.md"),
        Path("kb/types/note.schema.yaml"),
        Path("kb/types/instruction.md"),
        Path("kb/types/instruction.schema.yaml"),
        Path("kb/types/type-spec.md"),
        Path("kb/types/type-spec.schema.yaml"),
        # User-space source and report types.
        Path("kb/reports/types/connect-report.md"),
        Path("kb/reports/types/connect-report.schema.yaml"),
        Path("kb/sources/types/ingest-report.md"),
        Path("kb/sources/types/ingest-report.schema.yaml"),
        Path("kb/sources/types/snapshot.md"),
        Path("kb/sources/types/snapshot.schema.yaml"),
        Path("kb/sources/.gitignore"),
        Path("AGENTS.md.template"),
    }
    retired_files = {
        Path("kb/types/instruction.instructions.md"),
        Path("kb/reports/types/connect-report.instructions.md"),
        Path("kb/sources/types/snapshot.template.md"),
    }
    directories = relative_directories(tmp_path)

    assert expected <= files
    assert retired_files.isdisjoint(files)
    assert Path("kb/commonplace/agent-memory-systems") not in directories
    assert Path("kb/commonplace/instructions/review-gates") in directories


def test_init_project_satisfies_collection_landing_invariant(tmp_path: Path) -> None:
    init_project(tmp_path)

    assert is_collection_dir(tmp_path / "kb" / "sources")

    results = validate_collection_landings(repo_root=tmp_path)

    assert results.fails == []
    assert (
        "[repository] collection landings: all 5 top-level collections have README.md"
        in results.passes
    )


def test_init_project_seeds_quote_or_snapshot_source_contract(tmp_path: Path) -> None:
    init_project(tmp_path)

    contract = (tmp_path / "kb" / "sources" / "COLLECTION.md").read_text(
        encoding="utf-8"
    )
    normalized_contract = " ".join(contract.split())

    assert "## Quotes in ingest reports" in contract
    assert "No source quotes have been retained yet." in contract
    assert "Never change an existing ingest's `snapshot_sha256`." in contract
    assert "exact marker `(snapshot required)`" in contract
    assert "never silently falls back from an unmarked link" in normalized_contract


def test_init_project_preserves_source_collection_heads(tmp_path: Path) -> None:
    init_project(tmp_path)
    collection = tmp_path / "kb" / "sources" / "COLLECTION.md"
    landing = tmp_path / "kb" / "sources" / "README.md"
    collection.write_text("project source contract\n", encoding="utf-8")
    landing.write_text("project source landing\n", encoding="utf-8")

    rerun = init_project(tmp_path)

    assert rerun.created == []
    assert Path("kb/sources/COLLECTION.md") in rerun.preserved_different
    assert Path("kb/sources/README.md") in rerun.preserved_different
    assert collection.read_text(encoding="utf-8") == "project source contract\n"
    assert landing.read_text(encoding="utf-8") == "project source landing\n"


def test_init_project_installs_skills_as_copies(tmp_path: Path) -> None:
    init_project(tmp_path)

    for skills_dir in (
        tmp_path / ".claude" / "skills",
        tmp_path / ".agents" / "skills",
    ):
        assert skills_dir.is_dir()
        for skill_name in MANIFEST.promoted_skills:
            dest = skills_dir / skill_name
            assert dest.is_dir()
            assert not dest.is_symlink(), f"{dest} should be a real directory"
            source = tmp_path / "kb" / "commonplace" / "instructions" / skill_name
            assert (dest / "SKILL.md").read_bytes() == (source / "SKILL.md").read_bytes()


def test_init_project_preserves_existing_real_skill_projection(tmp_path: Path) -> None:
    dest = tmp_path / ".claude" / "skills" / "cp-skill-write"
    dest.mkdir(parents=True)
    (dest / "SKILL.md").write_text("runtime-specific copy", encoding="utf-8")

    report = init_project(tmp_path)

    assert Path(".claude/skills/cp-skill-write/SKILL.md") in report.preserved_different
    assert (dest / "SKILL.md").read_text(encoding="utf-8") == "runtime-specific copy"


def test_init_project_resolves_templates(tmp_path: Path) -> None:
    init_project(tmp_path, name="myproject")

    assert not (tmp_path / ".envrc").exists()

    # AGENTS.md.template has project name filled in
    agents = tmp_path / "AGENTS.md.template"
    text = agents.read_text(encoding="utf-8")
    assert "myproject" in text
    assert "{{project_name}}" not in text
    assert "## Vocabulary" in text
    assert "Terms needed to understand the project" in text
    assert "Call `commonplace-*` commands by bare name" in text
    assert "user-level `llm-commonplace` uv tool installation" in text
    assert ".venv" not in text

    assert not (tmp_path / "qmd-collections.yml").exists()


def test_init_project_defaults_name_to_directory(tmp_path: Path) -> None:
    init_project(tmp_path)

    agents = tmp_path / "AGENTS.md.template"
    text = agents.read_text(encoding="utf-8")
    assert tmp_path.name in text


def test_init_project_preserves_existing_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    collection = tmp_path / "kb" / "instructions" / "COLLECTION.md"
    collection.write_text("custom content", encoding="utf-8")

    rerun = init_project(tmp_path)
    assert rerun.created == []
    assert Path("kb/instructions/COLLECTION.md") in rerun.preserved_different
    assert collection.read_text(encoding="utf-8") == "custom content"


def test_init_project_reports_identical_existing_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    rerun = init_project(tmp_path)

    assert Path("kb/instructions/COLLECTION.md") in rerun.preserved_identical
    assert rerun.preserved_different == []


def test_init_project_treats_raw_template_source_as_matching(tmp_path: Path) -> None:
    raw_template = (REPO_ROOT / "AGENTS.md.template").read_text(encoding="utf-8")
    (tmp_path / "AGENTS.md.template").write_text(raw_template, encoding="utf-8")

    report = init_project(tmp_path)

    assert Path("AGENTS.md.template") in report.preserved_identical
    assert Path("AGENTS.md.template") not in report.preserved_different


def test_main_reports_preserved_file_statuses(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    init_project(tmp_path)
    (tmp_path / "kb" / "instructions" / "COLLECTION.md").write_text(
        "custom content",
        encoding="utf-8",
    )

    exit_code = main(["--root", str(tmp_path), "--name", "myproject"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Preserved existing files already matching scaffold:" in captured.out
    assert "Preserved existing files differing from current scaffold output:" in captured.out
    assert "- kb/instructions/COLLECTION.md" in captured.out


def test_main_does_not_imply_manual_edits_for_template_name_drift(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    init_project(tmp_path, name="custom-name")

    exit_code = main(["--root", str(tmp_path)])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Preserved existing files differing from current scaffold output:" in captured.out
    assert "- AGENTS.md.template" in captured.out
    assert "local changes" not in captured.out


def test_installation_warnings_report_missing_package_commands(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        init_project_module,
        "_installed_command_names",
        lambda: ("commonplace-init", "commonplace-validate"),
    )
    monkeypatch.setattr(
        init_project_module.shutil,
        "which",
        lambda name: "/tool/bin/commonplace-init" if name == "commonplace-init" else None,
    )
    monkeypatch.setattr(init_project_module, "_uv_tool_bin", lambda: None)

    lines = installation_warnings()

    assert any("commonplace-validate" in line and "not on PATH" in line for line in lines)
    assert any("uv tool update-shell" in line for line in lines)


def test_installation_warnings_report_missing_uv(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(init_project_module.shutil, "which", lambda _: None)
    monkeypatch.setattr(init_project_module, "_installed_command_names", lambda: ())
    monkeypatch.setattr(init_project_module, "_uv_tool_bin", lambda: None)

    lines = installation_warnings()

    assert any("uv is not on PATH" in line for line in lines)


def test_installation_warnings_report_shadowing_commands(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        init_project_module,
        "_installed_command_names",
        lambda: ("commonplace-validate",),
    )
    monkeypatch.setattr(
        init_project_module.shutil,
        "which",
        lambda _: "/project/.venv/bin/commonplace-validate",
    )
    monkeypatch.setattr(
        init_project_module, "_uv_tool_bin", lambda: Path("/user/uv-tool-bin")
    )

    lines = installation_warnings()

    assert any("resolve outside uv's tool executable directory" in line for line in lines)
    assert any("do not use uv tool install --force" in line for line in lines)


def test_installation_warnings_empty_for_healthy_tool_install(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        init_project_module,
        "_installed_command_names",
        lambda: ("commonplace-validate",),
    )
    monkeypatch.setattr(
        init_project_module.shutil,
        "which",
        lambda _: "/user/uv-tool-bin/commonplace-validate",
    )
    monkeypatch.setattr(
        init_project_module, "_uv_tool_bin", lambda: Path("/user/uv-tool-bin")
    )

    assert installation_warnings() == []
