from __future__ import annotations

import importlib.util
import os
import sys
from datetime import datetime
from pathlib import Path

import pytest


VALIDATE_SCRIPT = Path(__file__).resolve().parents[2] / "kb" / "instructions" / "validate" / "validate_notes.py"
SPEC = importlib.util.spec_from_file_location("validate_notes", VALIDATE_SCRIPT)
assert SPEC and SPEC.loader
validate_notes = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate_notes
SPEC.loader.exec_module(validate_notes)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_text_file_has_no_structural_requirements(tmp_path: Path) -> None:
    note = write(tmp_path / "raw-capture.md", "# Raw capture\n\nJust text.\n")

    results = validate_notes.validate_note(note)

    assert results.note_type == "text"
    assert results.fails == []
    assert any("no frontmatter" in item for item in results.passes)


def test_duplicate_frontmatter_keys_fail_validation(tmp_path: Path) -> None:
    note = write(
        tmp_path / "broken.md",
        """---
description: first
description: second
type: note
---

# Broken note
""",
    )

    results = validate_notes.validate_note(note)

    assert results.note_type == "unknown"
    assert any("duplicate key" in item for item in results.fails)


def test_link_validation_skips_code_and_external_urls(tmp_path: Path) -> None:
    target = write(tmp_path / "target.md", "# Target\n")
    note = write(
        tmp_path / "note.md",
        f"""---
description: A note with one real missing link and links that should be ignored by deterministic validation
type: note
traits: []
status: current
---

# Link validation note

Real link: [target](./{target.name})
Missing link: [missing](./missing.md)
External link: [site](https://example.com/foo.md)

`[inline-code](./ignored.md)`

```md
[fenced](./also-ignored.md)
```
""",
    )

    results = validate_notes.validate_note(note)

    assert "link health: all relative markdown links resolve" not in results.passes
    assert "link health: missing target ./missing.md" in results.warns
    assert all("ignored.md" not in item for item in results.warns)
    assert all("example.com" not in item for item in results.warns)


def test_structured_claim_requires_evidence_and_reasoning(tmp_path: Path) -> None:
    note = write(
        tmp_path / "claim.md",
        """---
description: Structured claim missing one required section so the validator should warn deterministically
type: structured-claim
traits: []
status: current
---

# Claims need support

## Evidence

Some evidence.
""",
    )

    results = validate_notes.validate_note(note)

    assert any("missing headings ## Reasoning" in item for item in results.warns)


def test_list_kb_note_paths_skips_nested_git_repos(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(
        notes_root / "kept.md",
        """---
description: Kept note with enough description text to satisfy the deterministic validator heuristics well enough
type: note
traits: []
status: current
---

# Kept note
""",
    )
    nested_repo = notes_root / "related-systems" / "napkin"
    nested_repo.mkdir(parents=True, exist_ok=True)
    (nested_repo / ".git").mkdir()
    write(
        nested_repo / "ignored.md",
        """---
description: This note lives under a cloned repo and should be skipped by batch validation path discovery
type: note
traits: []
status: current
---

# Ignored note
""",
    )

    monkeypatch.setattr(validate_notes, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(validate_notes, "NOTES_ROOT", notes_root)

    discovered = validate_notes.list_kb_note_paths()

    assert notes_root / "kept.md" in discovered
    assert nested_repo / "ignored.md" not in discovered


def test_recent_target_uses_mtime_and_target_lookup(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    notes_root = tmp_path / "kb" / "notes"
    today_note = write(
        notes_root / "today.md",
        """---
description: Note modified today so recent target resolution should find it deterministically
type: note
traits: []
status: current
---

# Today note
""",
    )
    old_note = write(
        notes_root / "old.md",
        """---
description: Older note that should not be picked up by recent target resolution in deterministic validation
type: note
traits: []
status: current
---

# Old note
""",
    )
    old_ts = datetime(2020, 1, 1).timestamp()
    old_note.touch()
    today_note.touch()
    os.utime(old_note, (old_ts, old_ts))

    monkeypatch.setattr(validate_notes, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(validate_notes, "NOTES_ROOT", notes_root)

    recent = validate_notes.resolve_targets("recent")
    named = validate_notes.resolve_targets("today")

    assert today_note in recent
    assert old_note not in recent
    assert named == recent
