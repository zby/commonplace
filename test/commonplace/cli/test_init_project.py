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


def test_init_project_preserves_existing_files(tmp_path: Path) -> None:
    init_project(tmp_path)

    writing = tmp_path / "kb" / "instructions" / "WRITING.md"
    writing.write_text("custom content", encoding="utf-8")

    rerun = init_project(tmp_path)
    assert rerun == []
    assert writing.read_text(encoding="utf-8") == "custom content"

