"""The build hook that prepares the shipped library copy."""

from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_hook_module():
    # hatchling is a build dependency, not a test dependency; stub its hook interface.
    for name in ("hatchling", "hatchling.builders", "hatchling.builders.hooks", "hatchling.builders.hooks.plugin"):
        sys.modules.setdefault(name, types.ModuleType(name))
    interface = types.ModuleType("hatchling.builders.hooks.plugin.interface")
    interface.BuildHookInterface = object
    sys.modules.setdefault("hatchling.builders.hooks.plugin.interface", interface)
    spec = importlib.util.spec_from_file_location("hatch_build", REPO_ROOT / "hatch_build.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _repo(tmp_path: Path, note_body: str) -> Path:
    repo = tmp_path / "repo"
    for name in ("instructions", "reference", "tags", "types"):
        (repo / "kb" / name).mkdir(parents=True)
    _write(repo / "kb" / "notes" / "other.md", "# Other\n")
    _write(repo / "kb" / "notes" / "note.md", note_body)
    _write(
        repo / "kb" / "sources" / "paper.ingest.md",
        "---\nsource: https://example.org/paper.pdf\ntype: types/ingest-report.md\n---\n\n# Paper\n",
    )
    _write(repo / "kb" / "agentic-systems" / "tool.md", "# Tool\n")
    return repo


def test_links_leaving_the_library_are_rewritten(tmp_path: Path) -> None:
    hook = _load_hook_module()
    repo = _repo(
        tmp_path,
        "[paper](../sources/paper.ingest.md), [tool](../agentic-systems/tool.md#top), "
        "[other](./other.md), and `[example](./missing.md)`.\n",
    )
    out = tmp_path / "out"

    hook.prepare_library(repo, out)

    text = (out / "notes" / "note.md").read_text(encoding="utf-8")
    assert "[paper](https://example.org/paper.pdf)" in text
    assert f"[tool]({hook.GITHUB_BLOB}kb/agentic-systems/tool.md#top)" in text
    assert "[other](./other.md)" in text
    assert "`[example](./missing.md)`" in text


def test_a_link_that_resolves_to_nothing_fails_the_build(tmp_path: Path) -> None:
    hook = _load_hook_module()
    repo = _repo(tmp_path, "[gone](./gone.md)\n")

    with pytest.raises(RuntimeError, match="unresolved link ./gone.md"):
        hook.prepare_library(repo, tmp_path / "out")
