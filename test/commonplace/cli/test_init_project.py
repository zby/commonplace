from __future__ import annotations

import sys
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli.init_project import init_project


def test_init_project_creates_core_directories(tmp_path: Path) -> None:
    created = init_project(tmp_path)

    assert created
    assert (tmp_path / "kb" / "notes").is_dir()
    assert (tmp_path / "kb" / "sources").is_dir()
    assert (tmp_path / "kb" / "instructions").is_dir()
    assert (tmp_path / "kb" / "reports").is_dir()
    assert (tmp_path / "types").is_dir()
    assert (tmp_path / "kb" / "log.md").is_file()

    rerun = init_project(tmp_path)
    assert rerun == []


def test_init_project_seeds_scaffold_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    assert (tmp_path / "kb" / "instructions" / "WRITING.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "REVIEW-SYSTEM.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "FIX-SYSTEM.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "review-gates").is_dir()
    assert (tmp_path / "types" / "note.yaml").is_file()
    assert (tmp_path / "AGENTS.md.template").is_file()


def test_init_project_installs_skills_with_prefix(tmp_path: Path) -> None:
    init_project(tmp_path)

    skills_dir = tmp_path / ".claude" / "skills"
    assert skills_dir.is_dir()
    assert (skills_dir / "commonplace-write" / "SKILL.md").is_file()
    assert (skills_dir / "commonplace-validate" / "SKILL.md").is_file()
    assert (skills_dir / "commonplace-snapshot-web" / "SKILL.md").is_file()
    assert (skills_dir / "commonplace-connect" / "SKILL.md").is_file()
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
    assert rerun == []
    assert writing.read_text(encoding="utf-8") == "custom content"

