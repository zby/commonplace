from __future__ import annotations

import sys
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib import type_resolver


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_root_note_profile_is_loaded_from_yaml(tmp_path: Path) -> None:
    write(
        tmp_path / "types" / "note.yaml",
        """required_fields:
  - description
allowed_status:
  - seedling
  - current
""",
    )
    note = write(
        tmp_path / "kb" / "notes" / "sample.md",
        """---
description: Sample
type: note
---

# Sample
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Sample", "type": "note"}, repo_root=tmp_path)

    assert profile.resolved_type == "note"
    assert profile.required_fields == ("description",)
    assert profile.allowed_status == ("seedling", "current")


def test_collection_definition_extends_note_profile(tmp_path: Path) -> None:
    write(
        tmp_path / "types" / "note.yaml",
        """required_fields:
  - description
allowed_status:
  - seedling
  - current
""",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "structured-claim.yaml",
        """base: note
required_headings:
  - "## Evidence"
  - "## Reasoning"
""",
    )
    note = write(
        tmp_path / "kb" / "notes" / "claim.md",
        """---
description: Sample
type: structured-claim
---

# Claim
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Sample", "type": "structured-claim"}, repo_root=tmp_path)

    assert profile.resolved_type == "structured-claim"
    assert profile.required_fields == ("description",)
    assert profile.required_headings == ("## Evidence", "## Reasoning")


def test_missing_type_definition_falls_back_to_note(tmp_path: Path) -> None:
    write(
        tmp_path / "types" / "note.yaml",
        """required_fields:
  - description
allowed_status:
  - seedling
""",
    )
    note = write(
        tmp_path / "kb" / "notes" / "sample.md",
        """---
description: Sample
type: unknown-type
---

# Sample
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Sample", "type": "unknown-type"}, repo_root=tmp_path)

    assert profile.resolved_type == "note"
    assert profile.required_fields == ("description",)
    assert profile.required_headings == ()


def test_workshop_scope_overrides_collection_and_root(tmp_path: Path) -> None:
    write(
        tmp_path / "types" / "note.yaml",
        """required_fields:
  - description
allowed_status:
  - current
""",
    )
    write(
        tmp_path / "kb" / "work" / "types" / "memo.yaml",
        """base: note
required_fields:
  - collection-field
""",
    )
    write(
        tmp_path / "kb" / "work" / "demo" / "types" / "memo.yaml",
        """base: note
required_fields:
  - workshop-field
""",
    )
    note = write(
        tmp_path / "kb" / "work" / "demo" / "note.md",
        """---
description: Workshop note
type: memo
---

# Demo
""",
    )

    profile = type_resolver.resolve_type(note, {"description": "Workshop note", "type": "memo"}, repo_root=tmp_path)

    assert profile.resolved_type == "memo"
    assert profile.required_fields == ("description", "workshop-field")


def test_text_without_frontmatter_resolves_to_text_profile(tmp_path: Path) -> None:
    note = write(tmp_path / "kb" / "notes" / "raw.md", "# Raw\n")

    profile = type_resolver.resolve_type(note, None, repo_root=tmp_path)

    assert profile.resolved_type == "text"
    assert profile.required_fields == ()

