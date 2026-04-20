from __future__ import annotations

import sys
from pathlib import Path

import pytest


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib import type_resolver  # noqa: E402


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def write_type_spec(
    root: Path,
    rel_path: str,
    *,
    name: str,
    schema: str | None,
) -> Path:
    schema_value = "null" if schema is None else schema
    return write(
        root / rel_path,
        f"""---
type: kb/types/type-spec.md
name: {name}
description: Type spec for {name}
schema: {schema_value}
---

# {name}
""",
    )


def write_note_schema(root: Path) -> None:
    write(
        root / "kb" / "types" / "note.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
properties:
  frontmatter:
    type: object
    required:
      - description
      - type
    properties:
      description:
        type: string
        minLength: 1
      type:
        const: kb/types/note.md
    additionalProperties: true
""",
    )


def test_path_valued_type_profile_loads_declared_schema(tmp_path: Path) -> None:
    write_note_schema(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/types/note.md",
        name="note",
        schema="kb/types/note.schema.yaml",
    )
    note = write(
        tmp_path / "kb" / "notes" / "sample.md",
        """---
description: Sample
type: kb/types/note.md
---

# Sample
""",
    )

    profile = type_resolver.resolve_type(
        note,
        {"description": "Sample", "type": "kb/types/note.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/types/note.md"
    assert profile.type_doc_path == tmp_path / "kb" / "types" / "note.md"
    assert profile.type_name == "note"
    assert profile.schema_path == tmp_path / "kb" / "types" / "note.schema.yaml"
    assert profile.schema is not None


def test_validate_instance_uses_declared_schema(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note-base.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
properties:
  frontmatter:
    type: object
    required:
      - description
      - type
    properties:
      description:
        type: string
        minLength: 1
      type:
        type: string
    additionalProperties: true
""",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "../../types/note-base.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        properties:
          type:
            const: kb/notes/types/structured-claim.md
        additionalProperties: true
      headings:
        type: array
        contains:
          const: "## Evidence"
""",
    )
    write_type_spec(
        tmp_path,
        "kb/notes/types/structured-claim.md",
        name="structured-claim",
        schema="kb/notes/types/structured-claim.schema.yaml",
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "notes" / "claim.md",
        {"description": "Sample", "type": "kb/notes/types/structured-claim.md"},
        repo_root=tmp_path,
    )
    errors = type_resolver.validate_instance(
        profile,
        {
            "frontmatter": {
                "description": "Sample",
                "type": "kb/notes/types/structured-claim.md",
            },
            "headings": ["# Claim"],
        },
    )

    assert profile.type_name == "structured-claim"
    assert errors


def test_schema_null_skips_schema_validation(tmp_path: Path) -> None:
    write_type_spec(
        tmp_path,
        "kb/tasks/types/task-backlog.md",
        name="task-backlog",
        schema=None,
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "tasks" / "backlog" / "task.md",
        {"type": "kb/tasks/types/task-backlog.md"},
        repo_root=tmp_path,
    )

    assert profile.schema_path is None
    assert type_resolver.validate_instance(profile, {"frontmatter": {}}) == []


def test_text_without_frontmatter_resolves_to_implicit_text_profile(tmp_path: Path) -> None:
    note = write(tmp_path / "kb" / "notes" / "raw.md", "# Raw\n")

    profile = type_resolver.resolve_type(note, None, repo_root=tmp_path)

    assert profile.type_path == "text"
    assert profile.type_name == "text"
    assert profile.type_doc_path is None
    assert profile.schema_path is None


def test_bare_enum_type_is_invalid(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="must start with kb/"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": "note"},
            repo_root=tmp_path,
        )


def test_frontmatter_without_type_is_invalid(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="frontmatter.type is required"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample"},
            repo_root=tmp_path,
        )


def test_missing_type_file_is_invalid(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="missing type spec"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": "kb/types/missing.md"},
            repo_root=tmp_path,
        )


@pytest.mark.parametrize(
    "type_path",
    [
        "/tmp/type.md",
        "https://example.com/type.md",
        "kb/../type.md",
        "types/note.md",
        "kb/types/note.schema.yaml",
    ],
)
def test_invalid_type_paths_fail(type_path: str, tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": type_path},
            repo_root=tmp_path,
        )


def test_type_spec_missing_schema_is_invalid(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note.md",
        """---
type: kb/types/type-spec.md
name: note
description: Missing schema field
---

# Note
""",
    )

    with pytest.raises(ValueError, match="must include schema"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": "kb/types/note.md"},
            repo_root=tmp_path,
        )


def test_root_type_spec_self_reference_terminates(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "type-spec.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
properties:
  frontmatter:
    type: object
    properties:
      type:
        const: kb/types/type-spec.md
    additionalProperties: true
""",
    )
    write_type_spec(
        tmp_path,
        "kb/types/type-spec.md",
        name="type-spec",
        schema="kb/types/type-spec.schema.yaml",
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "types" / "type-spec.md",
        {"type": "kb/types/type-spec.md"},
        repo_root=tmp_path,
    )

    assert profile.type_name == "type-spec"
    assert profile.schema_path == tmp_path / "kb" / "types" / "type-spec.schema.yaml"
