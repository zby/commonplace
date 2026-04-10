from __future__ import annotations

import sys
from importlib.resources import as_file, files
from pathlib import Path

import pytest


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli.init_project import init_project, main


def test_init_project_creates_core_directories(tmp_path: Path) -> None:
    report = init_project(tmp_path)

    assert report.created
    assert (tmp_path / "kb" / "notes").is_dir()
    assert (tmp_path / "kb" / "reference").is_dir()
    assert (tmp_path / "kb" / "sources").is_dir()
    assert (tmp_path / "kb" / "instructions").is_dir()
    assert (tmp_path / "kb" / "reports").is_dir()
    assert (tmp_path / "kb" / "types").is_dir()
    assert (tmp_path / "kb" / "log.md").is_file()

    rerun = init_project(tmp_path)
    assert rerun.created == []
    assert rerun.preserved_identical
    assert rerun.preserved_different == []


def test_init_project_seeds_scaffold_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    assert (tmp_path / "kb" / "instructions" / "README.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "WRITING.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "REVIEW-SYSTEM.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "FIX-SYSTEM.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "write" / "SKILL.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "connect" / "SKILL.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "ingest" / "SKILL.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "review-gates").is_dir()
    assert (tmp_path / "kb" / "reference" / "README.md").is_file()
    assert (tmp_path / "kb" / "reference" / "types" / "adr.template.md").is_file()
    assert (tmp_path / "kb" / "reference" / "types" / "adr.instructions.md").is_file()
    assert (tmp_path / "kb" / "reference" / "types" / "adr.schema.yaml").is_file()
    assert (tmp_path / "kb" / "types" / "note.schema.yaml").is_file()
    assert (tmp_path / "AGENTS.md.template").is_file()


def test_init_project_installs_skills_with_prefix(tmp_path: Path) -> None:
    init_project(tmp_path)

    for skills_dir in (
        tmp_path / ".claude" / "skills",
        tmp_path / ".agents" / "skills",
    ):
        assert skills_dir.is_dir()
        assert (skills_dir / "cp-skill-write" / "SKILL.md").is_file()
        assert (skills_dir / "cp-skill-validate" / "SKILL.md").is_file()
        assert (skills_dir / "cp-skill-snapshot-web" / "SKILL.md").is_file()
        assert (skills_dir / "cp-skill-connect" / "SKILL.md").is_file()
        # No unprefixed directories
        assert not (skills_dir / "write").exists()


def test_init_project_resolves_templates(tmp_path: Path) -> None:
    init_project(tmp_path, name="myproject")

    # .envrc is produced directly (not as .envrc.template)
    envrc = tmp_path / ".envrc"
    assert envrc.is_file()
    text = envrc.read_text(encoding="utf-8")
    assert "myproject" in text
    assert "<your-project>" not in text

    # AGENTS.md.template has project name filled in
    agents = tmp_path / "AGENTS.md.template"
    text = agents.read_text(encoding="utf-8")
    assert "myproject" in text
    assert "{{project_name}}" not in text

    # qmd config has paths filled in
    qmd = tmp_path / "qmd-collections.yml"
    assert qmd.is_file()
    text = qmd.read_text(encoding="utf-8")
    assert str(tmp_path) in text
    assert "/PATH/TO/COMMONPLACE/" not in text


def test_init_project_defaults_name_to_directory(tmp_path: Path) -> None:
    init_project(tmp_path)

    envrc = tmp_path / ".envrc"
    text = envrc.read_text(encoding="utf-8")
    assert tmp_path.name in text


def test_init_project_preserves_existing_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    writing = tmp_path / "kb" / "instructions" / "WRITING.md"
    writing.write_text("custom content", encoding="utf-8")

    rerun = init_project(tmp_path)
    assert rerun.created == []
    assert Path("kb/instructions/WRITING.md") in rerun.preserved_different
    assert writing.read_text(encoding="utf-8") == "custom content"


def test_init_project_reports_identical_existing_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    rerun = init_project(tmp_path)

    assert Path("kb/instructions/WRITING.md") in rerun.preserved_identical
    assert Path(".envrc") in rerun.preserved_identical
    assert rerun.preserved_different == []


def test_init_project_treats_raw_template_source_as_matching(tmp_path: Path) -> None:
    scaffold_pkg = files("commonplace.scaffold")
    with as_file(scaffold_pkg) as scaffold_root:
        raw_template = (scaffold_root / "AGENTS.md.template").read_text(encoding="utf-8")
    (tmp_path / "AGENTS.md.template").write_text(raw_template, encoding="utf-8")

    report = init_project(tmp_path)

    assert Path("AGENTS.md.template") in report.preserved_identical
    assert Path("AGENTS.md.template") not in report.preserved_different


def test_main_reports_preserved_file_statuses(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    init_project(tmp_path)
    (tmp_path / "kb" / "instructions" / "WRITING.md").write_text(
        "custom content",
        encoding="utf-8",
    )

    exit_code = main(["--root", str(tmp_path), "--name", "myproject"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Preserved existing files already matching scaffold:" in captured.out
    assert "Preserved existing files differing from current scaffold output:" in captured.out
    assert "- kb/instructions/WRITING.md" in captured.out


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
