from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


sync_generated_index = load_module("sync_generated_index_test", SCRIPTS_DIR / "sync_generated_index.py")


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_sync_generated_index_main_dry_run_reports_changes(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    index_path = write(
        notes_root / "kb-design-index.md",
        """---
description: Index page for kb-design notes with a generated section maintained by the sync script
type: index
traits: []
status: current
---

# KB design index

Curated introduction.
""",
    )
    original = index_path.read_text(encoding="utf-8")
    write(
        notes_root / "example-note.md",
        """---
description: Example note tagged for kb-design so the generated section should report one pending update
type: note
traits: []
status: current
tags: [kb-design]
---

# Example note
""",
    )

    monkeypatch.setattr(sync_generated_index, "NOTES_DIR", notes_root)
    monkeypatch.setattr(sys, "argv", ["sync_generated_index.py", "--dry-run", str(index_path)])

    sync_generated_index.main()

    captured = capsys.readouterr()
    assert "Would change 1 index(es):" in captured.out
    assert "Would update kb-design-index.md: 1 notes for tag 'kb-design'" in captured.out
    assert index_path.read_text(encoding="utf-8") == original
