from __future__ import annotations

import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli import init_project as init_project_module  # noqa: E402
from commonplace.cli.init_project import (  # noqa: E402
    direnv_warnings,
    init_project,
    main,
    _resolve_scaffold_source,
)


def test_init_project_creates_core_directories(tmp_path: Path) -> None:
    report = init_project(tmp_path)

    assert report.created
    assert (tmp_path / "kb" / "notes").is_dir()
    assert (tmp_path / "kb" / "reference").is_dir()
    assert (tmp_path / "kb" / "sources").is_dir()
    assert (tmp_path / "kb" / "instructions").is_dir()
    assert (tmp_path / "kb" / "reports").is_dir()
    assert (tmp_path / "kb" / "types").is_dir()
    assert (tmp_path / "kb" / "reports" / "types").is_dir()
    assert (tmp_path / "kb" / "log.md").is_file()

    rerun = init_project(tmp_path)
    assert rerun.created == []
    assert rerun.preserved_identical
    assert rerun.preserved_different == []


def test_init_project_seeds_scaffold_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    # Shipped library content lives under kb/commonplace/ (ADR-021).
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "README.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "COLLECTION.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "notes" / "COLLECTION.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "reference" / "COLLECTION.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "REVIEW-SYSTEM.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "FIX-SYSTEM.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "cp-skill-write" / "SKILL.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "cp-skill-connect" / "SKILL.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "cp-skill-ingest" / "SKILL.md").is_file()
    assert (
        tmp_path / "kb" / "commonplace" / "instructions" / "cp-skill-health-check" / "SKILL.md"
    ).is_file()
    assert (tmp_path / "kb" / "commonplace" / "instructions" / "review-gates").is_dir()
    assert (tmp_path / "kb" / "commonplace" / "reference" / "README.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "reference" / "types" / "adr.md").is_file()
    assert (tmp_path / "kb" / "commonplace" / "reference" / "types" / "adr.schema.yaml").is_file()
    assert not (tmp_path / "kb" / "commonplace" / "agent-memory-systems").exists()

    # User collections get minimal COLLECTION.md templates to fill in.
    assert (tmp_path / "kb" / "notes" / "COLLECTION.md").is_file()
    assert (tmp_path / "kb" / "reference" / "COLLECTION.md").is_file()
    assert (tmp_path / "kb" / "instructions" / "COLLECTION.md").is_file()

    # Shared global types stay at top-level kb/types/ (ADR-021: B1 paths are
    # invariant when the global types dir is shared, not nested under commonplace).
    assert (tmp_path / "kb" / "types" / "note.schema.yaml").is_file()
    assert (tmp_path / "kb" / "types" / "instruction.md").is_file()
    assert not (tmp_path / "kb" / "types" / "instruction.instructions.md").exists()
    assert (tmp_path / "kb" / "types" / "instruction.schema.yaml").is_file()
    assert (tmp_path / "kb" / "types" / "type-spec.md").is_file()
    assert (tmp_path / "kb" / "types" / "type-spec.schema.yaml").is_file()

    # User-space type scaffolds (sources, reports) stay in the user's tree.
    assert (tmp_path / "kb" / "reports" / "types" / "connect-report.md").is_file()
    assert not (tmp_path / "kb" / "reports" / "types" / "connect-report.instructions.md").exists()
    assert (tmp_path / "kb" / "reports" / "types" / "connect-report.schema.yaml").is_file()
    assert (tmp_path / "kb" / "sources" / "types" / "ingest-report.md").is_file()
    assert (tmp_path / "kb" / "sources" / "types" / "ingest-report.schema.yaml").is_file()
    assert (tmp_path / "kb" / "sources" / "types" / "snapshot.md").is_file()
    assert (tmp_path / "kb" / "sources" / "types" / "snapshot.schema.yaml").is_file()
    assert not (tmp_path / "kb" / "sources" / "types" / "snapshot.template.md").exists()

    assert (tmp_path / "AGENTS.md.template").is_file()


def test_init_project_installs_skills_as_symlinks(tmp_path: Path) -> None:
    init_project(tmp_path)

    for skills_dir in (
        tmp_path / ".claude" / "skills",
        tmp_path / ".agents" / "skills",
    ):
        assert skills_dir.is_dir()
        for skill_name in (
            "cp-skill-write",
            "cp-skill-validate",
            "cp-skill-snapshot-web",
            "cp-skill-connect",
            "cp-skill-health-check",
        ):
            link = skills_dir / skill_name
            assert link.is_symlink(), f"{link} should be a symlink"
            assert (link / "SKILL.md").is_file()
            # Symlink points back into the shipped library.
            assert link.resolve() == (tmp_path / "kb" / "commonplace" / "instructions" / skill_name).resolve()


def test_init_project_skips_skill_projection_when_symlinks_are_unavailable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def fail_symlink(
        self: Path,
        target: str | Path,
        target_is_directory: bool = False,
    ) -> None:
        raise OSError("symbolic link privilege not held")

    monkeypatch.setattr(Path, "symlink_to", fail_symlink)

    report = init_project(tmp_path)

    assert (tmp_path / "kb" / "commonplace" / "instructions" / "cp-skill-write" / "SKILL.md").is_file()
    assert not (tmp_path / ".claude" / "skills" / "cp-skill-write").exists()
    assert len(report.skipped) == (
        len(init_project_module.PROMOTED_SKILLS) * len(init_project_module.SKILLS_DIRS)
    )
    assert any("symbolic link privilege not held" in reason for _, reason in report.skipped)


def test_init_project_preserves_existing_real_skill_projection(tmp_path: Path) -> None:
    link = tmp_path / ".claude" / "skills" / "cp-skill-write"
    link.mkdir(parents=True)
    (link / "SKILL.md").write_text("runtime-specific copy", encoding="utf-8")

    report = init_project(tmp_path)

    assert Path(".claude/skills/cp-skill-write") in report.preserved_different
    assert not link.is_symlink()
    assert (link / "SKILL.md").read_text(encoding="utf-8") == "runtime-specific copy"


def test_init_project_resolves_templates(tmp_path: Path) -> None:
    init_project(tmp_path, name="myproject")

    # .envrc is produced directly (not as .envrc.template)
    envrc = tmp_path / ".envrc"
    assert envrc.is_file()
    text = envrc.read_text(encoding="utf-8")
    assert "UV_CACHE_DIR" in text
    assert "COMMONPLACE_QMD_INDEX" not in text
    assert "<your-project>" not in text

    # AGENTS.md.template has project name filled in
    agents = tmp_path / "AGENTS.md.template"
    text = agents.read_text(encoding="utf-8")
    assert "myproject" in text
    assert "{{project_name}}" not in text
    assert "## Vocabulary" in text
    assert "Terms needed to understand the project" in text
    assert "Call `commonplace-*` commands by bare name" in text
    assert "commands and `pytest`" not in text

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
    assert Path(".envrc") in rerun.preserved_identical
    assert rerun.preserved_different == []


def test_init_project_treats_raw_template_source_as_matching(tmp_path: Path) -> None:
    raw_template = (REPO_ROOT / "AGENTS.md.template").read_text(encoding="utf-8")
    (tmp_path / "AGENTS.md.template").write_text(raw_template, encoding="utf-8")

    report = init_project(tmp_path)

    assert Path("AGENTS.md.template") in report.preserved_identical
    assert Path("AGENTS.md.template") not in report.preserved_different


def test_scaffold_source_resolves_canonical_files_without_data_symlinks() -> None:
    data_root = SRC_ROOT / "commonplace" / "_data"

    assert _resolve_scaffold_source(data_root, "AGENTS.md.template") == (
        REPO_ROOT / "AGENTS.md.template"
    )
    assert _resolve_scaffold_source(data_root, "kb/instructions") == (
        REPO_ROOT / "kb" / "instructions"
    )


def test_package_data_tree_has_no_scaffold_symlinks() -> None:
    data_root = SRC_ROOT / "commonplace" / "_data"

    assert not any(path.is_symlink() for path in data_root.rglob("*"))


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


def test_direnv_warnings_when_direnv_missing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "commonplace.cli.init_project.shutil.which", lambda _: None
    )
    lines = direnv_warnings(tmp_path)
    assert lines
    assert any("direnv is not installed" in line for line in lines)
    assert any("INSTALL.md" in line for line in lines)


def test_direnv_warnings_when_direnv_present(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "commonplace.cli.init_project.shutil.which", lambda _: "/usr/bin/direnv"
    )
    lines = direnv_warnings(tmp_path)
    assert lines
    assert any("direnv allow" in line for line in lines)


def test_environment_warnings_on_windows(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(init_project_module.sys, "platform", "win32")

    lines = direnv_warnings(tmp_path)

    assert lines
    assert any("Windows detected" in line for line in lines)
    assert any("Activate.ps1" in line for line in lines)
    assert any("Load the project environment" in line for line in lines)


def test_main_prints_windows_guidance_when_init_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(init_project_module.sys, "platform", "win32")

    def fail_init_project(root: Path, name: str | None = None) -> init_project_module.InitReport:
        raise OSError("symbolic link privilege not held")

    monkeypatch.setattr(init_project_module, "init_project", fail_init_project)

    exit_code = init_project_module.main(["--root", str(tmp_path), "--name", "myproject"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Windows detected" in captured.out
    assert "Activate.ps1" in captured.out
    assert "Failed to initialize Commonplace project" in captured.out
    assert "symbolic link privilege not held" in captured.out


def test_main_emits_direnv_setup_section(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(
        "commonplace.cli.init_project.shutil.which", lambda _: None
    )
    exit_code = main(["--root", str(tmp_path), "--name", "myproject"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Environment setup:" in captured.out
    assert "direnv is not installed" in captured.out
