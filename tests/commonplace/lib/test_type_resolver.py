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


def test_canonical_type_identity_unwraps_installed_framework_namespace() -> None:
    profile = type_resolver.TypeProfile(
        type_path="kb/commonplace/types/tag-readme.md",
        type_doc_path=Path("/repo/kb/commonplace/types/tag-readme.md"),
        type_name="tag-readme",
        schema_path=None,
    )

    assert type_resolver.canonical_type_identity(profile) == "kb/types/tag-readme.md"


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


def test_resolve_type_definition_uses_already_parsed_frontmatter(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    schema = write(
        tmp_path / "kb" / "notes" / "types" / "local.schema.yaml",
        '$schema: "https://json-schema.org/draft/2020-12/schema"\ntype: object\n',
    )
    type_doc = write_type_spec(
        tmp_path,
        "kb/notes/types/local.md",
        name="local",
        schema="./local.schema.yaml",
    )
    parsed_frontmatter = {
        "type": "kb/types/type-spec.md",
        "name": "local",
        "description": "Type spec for local",
        "schema": "./local.schema.yaml",
    }

    def fail_if_reloaded(*args: object, **kwargs: object) -> None:
        raise AssertionError("type frontmatter should not be reloaded")

    monkeypatch.setattr(type_resolver, "_load_type_frontmatter", fail_if_reloaded)

    profile = type_resolver.resolve_type_definition(
        type_doc,
        repo_root=tmp_path,
        type_frontmatter=parsed_frontmatter,
    )

    assert profile.type_path == "kb/notes/types/local.md"
    assert profile.type_name == "local"
    assert profile.schema_path == schema


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


def test_file_relative_type_same_directory(tmp_path: Path) -> None:
    """`type: ./types/foo.md` from a note at the collection root resolves
    to the sibling `types/` directory."""
    write_note_schema(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/notes/types/structured-claim.md",
        name="structured-claim",
        schema="kb/types/note.schema.yaml",
    )

    note_path = tmp_path / "kb" / "notes" / "sample.md"
    write(note_path, "---\ndescription: Sample\ntype: ./types/structured-claim.md\n---\n# Sample\n")

    profile = type_resolver.resolve_type(
        note_path,
        {"description": "Sample", "type": "./types/structured-claim.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/notes/types/structured-claim.md"
    assert profile.type_doc_path == tmp_path / "kb" / "notes" / "types" / "structured-claim.md"
    assert profile.type_name == "structured-claim"


def test_file_relative_type_parent_directory(tmp_path: Path) -> None:
    """`type: ../types/foo.md` from a note in a subdirectory resolves
    to the collection's types/ sibling."""
    write_note_schema(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/reference/types/adr.md",
        name="adr",
        schema="kb/types/note.schema.yaml",
    )

    adr_path = tmp_path / "kb" / "reference" / "adr" / "001-example.md"
    write(adr_path, "---\ndescription: ADR\ntype: ../types/adr.md\n---\n# ADR\n")

    profile = type_resolver.resolve_type(
        adr_path,
        {"description": "ADR", "type": "../types/adr.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/reference/types/adr.md"
    assert profile.type_doc_path == tmp_path / "kb" / "reference" / "types" / "adr.md"


def test_file_relative_type_escape_attempt_is_invalid(tmp_path: Path) -> None:
    """A file-relative type that resolves outside kb/ must be rejected."""
    with pytest.raises(ValueError, match="must stay under kb/"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": "../../../etc/passwd.md"},
            repo_root=tmp_path,
        )


def test_repo_relative_type_still_works_with_source_file_context(tmp_path: Path) -> None:
    """Absolute `kb/...` paths keep working unchanged when source_file is
    also available (B1 path — global types stay absolute)."""
    write_note_schema(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/types/note.md",
        name="note",
        schema="kb/types/note.schema.yaml",
    )

    note_path = tmp_path / "kb" / "notes" / "sample.md"
    write(note_path, "---\ndescription: Sample\ntype: kb/types/note.md\n---\n# Sample\n")

    profile = type_resolver.resolve_type(
        note_path,
        {"description": "Sample", "type": "kb/types/note.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/types/note.md"


def test_validate_instance_normalizes_file_relative_type_for_const_match(tmp_path: Path) -> None:
    """When a note uses file-relative type (`../types/adr.md`), the schema
    validator still matches a `const: kb/...` check because validate_instance
    normalizes the frontmatter.type to the canonical form first."""
    write(
        tmp_path / "kb" / "reference" / "types" / "adr.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
properties:
  frontmatter:
    type: object
    required:
      - type
    properties:
      type:
        const: kb/reference/types/adr.md
    additionalProperties: true
""",
    )
    write_type_spec(
        tmp_path,
        "kb/reference/types/adr.md",
        name="adr",
        schema="kb/reference/types/adr.schema.yaml",
    )

    adr_path = tmp_path / "kb" / "reference" / "adr" / "001-example.md"
    profile = type_resolver.resolve_type(
        adr_path,
        {"type": "../types/adr.md"},
        repo_root=tmp_path,
    )
    errors = type_resolver.validate_instance(
        profile,
        {"frontmatter": {"type": "../types/adr.md"}},
    )

    assert errors == []


def test_file_relative_schema_path_resolves_from_type_spec(tmp_path: Path) -> None:
    write_note_schema(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/notes/types/structured-claim.md",
        name="structured-claim",
        schema="./structured-claim.schema.yaml",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
required:
  - frontmatter
properties:
  frontmatter:
    type: object
    required:
      - type
    properties:
      type:
        const: kb/notes/types/structured-claim.md
    additionalProperties: true
""",
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "notes" / "claim.md",
        {"description": "Sample", "type": "./types/structured-claim.md"},
        repo_root=tmp_path,
    )

    assert profile.schema_path == tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml"


def test_repo_relative_collection_local_type_still_works(tmp_path: Path) -> None:
    write_note_schema(tmp_path)
    write_type_spec(
        tmp_path,
        "kb/notes/types/structured-claim.md",
        name="structured-claim",
        schema="./structured-claim.schema.yaml",
    )
    write(
        tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
type: object
properties:
  frontmatter:
    type: object
    properties:
      type:
        const: kb/notes/types/structured-claim.md
    additionalProperties: true
""",
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "notes" / "claim.md",
        {"description": "Sample", "type": "kb/notes/types/structured-claim.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/notes/types/structured-claim.md"
    assert profile.schema_path == tmp_path / "kb" / "notes" / "types" / "structured-claim.schema.yaml"


def test_wrapped_library_schema_refs_fall_back_to_shared_global_types(tmp_path: Path) -> None:
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
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
    write_type_spec(
        tmp_path,
        "kb/commonplace/notes/types/structured-claim.md",
        name="structured-claim",
        schema="./structured-claim.schema.yaml",
    )
    write(
        tmp_path / "kb" / "commonplace" / "notes" / "types" / "structured-claim.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "../../types/note.schema.yaml"
  - type: object
    properties:
      frontmatter:
        type: object
        properties:
          type:
            const: kb/notes/types/structured-claim.md
        additionalProperties: true
""",
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "commonplace" / "notes" / "claim.md",
        {"description": "Sample", "type": "./types/structured-claim.md"},
        repo_root=tmp_path,
    )
    errors = type_resolver.validate_instance(
        profile,
        {
            "frontmatter": {
                "description": "Sample",
                "type": "./types/structured-claim.md",
            },
            "headings": ["# Claim"],
        },
    )

    assert errors == []


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
