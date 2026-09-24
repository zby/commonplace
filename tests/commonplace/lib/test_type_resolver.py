from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from commonplace.lib import type_resolver


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def write_collection(root: Path, rel_path: str) -> Path:
    collection = root / rel_path
    write(collection / "COLLECTION.md", "# Collection\n")
    return collection


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


def write_schema(
    root: Path,
    rel_path: str,
    *,
    type_const: str | None = None,
    require_description: bool = False,
    ref: str | None = None,
    heading: str | None = None,
) -> Path:
    """Write a JSON Schema over the parsed-note object.

    ``type_const`` pins ``frontmatter.type``; ``ref`` wraps the body in an
    ``allOf`` with that ``$ref``; ``heading`` requires the headings to contain it.
    """
    fm_properties: dict[str, Any] = {
        "type": {"const": type_const} if type_const else {"type": "string"}
    }
    fm_schema: dict[str, Any] = {"type": "object", "properties": fm_properties}
    if require_description:
        fm_schema["required"] = ["description", "type"]
        fm_properties["description"] = {"type": "string", "minLength": 1}
    fm_schema["additionalProperties"] = True
    body: dict[str, Any] = {
        "type": "object",
        "required": ["frontmatter"],
        "properties": {"frontmatter": fm_schema},
    }
    if heading is not None:
        body["properties"]["headings"] = {"type": "array", "contains": {"const": heading}}
    schema = {"$schema": "https://json-schema.org/draft/2020-12/schema"}
    schema.update({"allOf": [{"$ref": ref}, body]} if ref else body)
    return write(root / rel_path, yaml.safe_dump(schema, sort_keys=False))


def test_canonical_type_identity_unwraps_installed_framework_namespace() -> None:
    profile = type_resolver.TypeProfile(
        type_path="kb/commonplace/types/tag-readme.md",
        type_doc_path=Path("/repo/kb/commonplace/types/tag-readme.md"),
        type_name="tag-readme",
        schema_path=None,
    )

    assert type_resolver.canonical_type_identity(profile) == "kb/types/tag-readme.md"


def test_global_type_in_declared_collection_loads_declared_schema(
    tmp_path: Path,
) -> None:
    notes = write_collection(tmp_path, "kb/notes")
    write_schema(
        tmp_path,
        "kb/types/note.schema.yaml",
        type_const="kb/types/note.md",
        require_description=True,
    )
    write_type_spec(
        tmp_path,
        "kb/types/note.md",
        name="note",
        schema="kb/types/note.schema.yaml",
    )

    profile = type_resolver.resolve_type(
        notes / "sample.md",
        {"description": "Sample", "type": "kb/types/note.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/types/note.md"
    assert profile.type_doc_path == tmp_path / "kb" / "types" / "note.md"
    assert profile.type_name == "note"
    assert profile.schema_path == tmp_path / "kb" / "types" / "note.schema.yaml"
    assert profile.schema is not None


@pytest.mark.parametrize(
    "type_value",
    ["kb/notes/types/structured-claim.md", "./types/structured-claim.md"],
    ids=["repo-relative", "file-relative"],
)
def test_own_collection_local_type_resolves_with_file_relative_schema(
    tmp_path: Path, type_value: str
) -> None:
    notes = write_collection(tmp_path, "kb/notes")
    types_dir = tmp_path / "kb" / "notes" / "types"
    write_schema(
        tmp_path,
        "kb/notes/types/structured-claim.schema.yaml",
        type_const="kb/notes/types/structured-claim.md",
    )
    write_type_spec(
        tmp_path,
        "kb/notes/types/structured-claim.md",
        name="structured-claim",
        schema="./structured-claim.schema.yaml",
    )

    profile = type_resolver.resolve_type(
        notes / "claim.md",
        {"description": "Sample", "type": type_value},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/notes/types/structured-claim.md"
    assert profile.type_doc_path == types_dir / "structured-claim.md"
    assert profile.type_name == "structured-claim"
    assert profile.schema_path == types_dir / "structured-claim.schema.yaml"


@pytest.mark.parametrize(
    "type_value",
    ["kb/reference/types/adr.md", "../reference/types/adr.md"],
    ids=["repo-relative", "file-relative"],
)
def test_peer_collection_local_type_is_ineligible(
    tmp_path: Path, type_value: str
) -> None:
    notes = write_collection(tmp_path, "kb/notes")
    write_collection(tmp_path, "kb/reference")
    write_type_spec(
        tmp_path,
        "kb/reference/types/adr.md",
        name="adr",
        schema=None,
    )

    with pytest.raises(
        ValueError,
        match=r"kb/reference/types/adr\.md is not eligible in collection kb/notes",
    ):
        type_resolver.resolve_type(
            notes / "decision.md",
            {"type": type_value},
            repo_root=tmp_path,
        )


def test_work_subtree_accepts_peer_collection_local_type(tmp_path: Path) -> None:
    write_collection(tmp_path, "kb/work")
    nested_workshop = write_collection(tmp_path, "kb/work/type-trial")
    write_collection(tmp_path, "kb/reference")
    write_type_spec(
        tmp_path,
        "kb/reference/types/adr.md",
        name="adr",
        schema=None,
    )

    profile = type_resolver.resolve_type(
        nested_workshop / "decision.md",
        {"type": "kb/reference/types/adr.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/reference/types/adr.md"


def test_installed_collection_local_type_is_eligible(tmp_path: Path) -> None:
    notes = write_collection(tmp_path, "kb/commonplace/notes")
    write_type_spec(
        tmp_path,
        "kb/commonplace/notes/types/structured-claim.md",
        name="structured-claim",
        schema=None,
    )

    profile = type_resolver.resolve_type(
        notes / "claim.md",
        {"type": "./types/structured-claim.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/commonplace/notes/types/structured-claim.md"


def test_collectionless_namespace_keeps_referential_type_resolution(
    tmp_path: Path,
) -> None:
    write_type_spec(
        tmp_path,
        "kb/reference/types/adr.md",
        name="adr",
        schema=None,
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "unclassified" / "decision.md",
        {"type": "kb/reference/types/adr.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "kb/reference/types/adr.md"


def test_validate_instance_uses_declared_schema(tmp_path: Path) -> None:
    write_schema(tmp_path, "kb/types/note-base.schema.yaml", require_description=True)
    write_schema(
        tmp_path,
        "kb/notes/types/structured-claim.schema.yaml",
        type_const="kb/notes/types/structured-claim.md",
        ref="../../types/note-base.schema.yaml",
        heading="## Evidence",
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

    assert [(error.validator, list(error.absolute_path)) for error in errors] == [
        ("contains", ["headings"])
    ]


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


def test_file_relative_type_escape_attempt_is_invalid(tmp_path: Path) -> None:
    """A file-relative type that resolves outside kb/ must be rejected."""
    with pytest.raises(ValueError, match="must stay under kb/"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": "../../../etc/passwd.md"},
            repo_root=tmp_path,
        )


def test_file_relative_type_from_subdirectory_matches_schema_const(
    tmp_path: Path,
) -> None:
    """`../types/adr.md` from a note one level below the collection resolves to
    the collection's types/ sibling, and validate_instance normalizes the
    frontmatter.type to the canonical `kb/...` form so a `const` check matches."""
    write_schema(
        tmp_path,
        "kb/reference/types/adr.schema.yaml",
        type_const="kb/reference/types/adr.md",
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

    assert profile.type_path == "kb/reference/types/adr.md"
    assert profile.type_doc_path == tmp_path / "kb" / "reference" / "types" / "adr.md"
    assert errors == []


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
