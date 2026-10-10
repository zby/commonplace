from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml

from commonplace.lib import library, type_resolver


@pytest.fixture(autouse=True)
def _test_repository_is_the_library(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Each test builds its own global types under tmp_path/kb, the library for the test."""
    monkeypatch.setenv(library.LIBRARY_ENV, str(tmp_path / "kb"))


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
type: types/type-spec.md
name: {name}
description: Type spec for {name}
schema: {schema_value}
---

# {name}
""",
    )


def write_schema(root: Path, rel_path: str, *, type_const: str) -> Path:
    """Write a JSON Schema over the parsed-note object pinning ``frontmatter.type``."""
    schema: dict[str, Any] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": ["frontmatter"],
        "properties": {
            "frontmatter": {
                "type": "object",
                "properties": {"type": {"const": type_const}},
                "additionalProperties": True,
            }
        },
    }
    return write(root / rel_path, yaml.safe_dump(schema, sort_keys=False))


def test_peer_collection_local_type_is_ineligible(tmp_path: Path) -> None:
    notes = write_collection(tmp_path, "kb/notes")
    write_collection(tmp_path, "kb/reference")
    write_type_spec(tmp_path, "kb/reference/types/adr.md", name="adr", schema=None)

    with pytest.raises(
        ValueError,
        match=r"kb/reference/types/adr\.md is not eligible in collection kb/notes",
    ):
        type_resolver.resolve_type(
            notes / "decision.md",
            {"type": "reference/types/adr.md"},
            repo_root=tmp_path,
        )


def test_work_subtree_accepts_peer_collection_local_type(tmp_path: Path) -> None:
    write_collection(tmp_path, "kb/work")
    nested_workshop = write_collection(tmp_path, "kb/work/type-trial")
    write_collection(tmp_path, "kb/reference")
    write_type_spec(tmp_path, "kb/reference/types/adr.md", name="adr", schema=None)

    profile = type_resolver.resolve_type(
        nested_workshop / "decision.md",
        {"type": "reference/types/adr.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "reference/types/adr.md"


def test_collectionless_namespace_keeps_referential_type_resolution(
    tmp_path: Path,
) -> None:
    write_type_spec(tmp_path, "kb/reference/types/adr.md", name="adr", schema=None)

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "unclassified" / "decision.md",
        {"type": "reference/types/adr.md"},
        repo_root=tmp_path,
    )

    assert profile.type_path == "reference/types/adr.md"


def test_schema_null_skips_schema_validation(tmp_path: Path) -> None:
    write_type_spec(
        tmp_path,
        "kb/tasks/types/task-backlog.md",
        name="task-backlog",
        schema=None,
    )

    profile = type_resolver.resolve_type(
        tmp_path / "kb" / "tasks" / "backlog" / "task.md",
        {"type": "tasks/types/task-backlog.md"},
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


@pytest.mark.parametrize("value", ["kb/types/note.md", "../reference/types/adr.md"])
def test_retired_type_values_are_rejected(tmp_path: Path, value: str) -> None:
    with pytest.raises(ValueError, match="spec's path under a KB root"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": value},
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
            {"description": "Sample", "type": "types/missing.md"},
            repo_root=tmp_path,
        )


@pytest.mark.parametrize("type_path", ["/tmp/type.md", "types/../type.md"])
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
type: types/type-spec.md
name: note
description: Missing schema field
---

# Note
""",
    )

    with pytest.raises(ValueError, match="must include schema"):
        type_resolver.resolve_type(
            tmp_path / "kb" / "notes" / "sample.md",
            {"description": "Sample", "type": "types/note.md"},
            repo_root=tmp_path,
        )


def test_a_type_value_is_the_same_at_any_depth(tmp_path: Path) -> None:
    write_schema(tmp_path, "kb/reference/types/adr.schema.yaml", type_const="reference/types/adr.md")
    write_type_spec(tmp_path, "kb/reference/types/adr.md", name="adr", schema="./adr.schema.yaml")

    for artifact in ("reference/overview.md", "reference/adr/001-example.md"):
        profile = type_resolver.resolve_type(
            tmp_path / "kb" / artifact,
            {"type": "reference/types/adr.md"},
            repo_root=tmp_path,
        )
        errors = type_resolver.validate_instance(
            profile, {"frontmatter": {"type": "reference/types/adr.md"}}
        )
        assert profile.type_doc_path == tmp_path / "kb" / "reference" / "types" / "adr.md"
        assert errors == []


def test_local_schema_builds_on_a_global_schema_through_a_library_ref(tmp_path: Path) -> None:
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
    additionalProperties: true
""",
    )
    write(
        tmp_path / "kb" / "types" / "note.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "./note-base.schema.yaml"
""",
    )
    notes = write_collection(tmp_path, "kb/notes")
    write_type_spec(
        tmp_path,
        "kb/notes/types/structured-claim.md",
        name="structured-claim",
        schema="./structured-claim.schema.yaml",
    )
    write(
        notes / "types" / "structured-claim.schema.yaml",
        """$schema: "https://json-schema.org/draft/2020-12/schema"
allOf:
  - $ref: "commonplace:types/note.schema.yaml"
""",
    )

    value = "notes/types/structured-claim.md"
    profile = type_resolver.resolve_type(
        notes / "claim.md", {"description": "Sample", "type": value}, repo_root=tmp_path
    )
    missing_description = type_resolver.validate_instance(profile, {"frontmatter": {"type": value}})
    complete = type_resolver.validate_instance(
        profile, {"frontmatter": {"description": "Sample", "type": value}}
    )

    assert missing_description
    assert complete == []


def installed_project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path]:
    """A project whose library lives elsewhere, as in an installed project."""
    project = tmp_path / "project"
    library_root = tmp_path / "library"
    monkeypatch.setenv(library.LIBRARY_ENV, str(library_root))
    write_type_spec(library_root, "types/note.md", name="note", schema=None)
    write_type_spec(library_root, "reference/types/adr.md", name="adr", schema=None)
    return project, library_root


def test_installed_project_finds_global_types_in_the_library(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, library_root = installed_project(tmp_path, monkeypatch)
    notes = write_collection(project, "kb/notes")

    profile = type_resolver.resolve_type(
        notes / "sample.md", {"type": "types/note.md"}, repo_root=project
    )

    assert profile.type_doc_path == library_root / "types" / "note.md"
    assert profile.type_path == "types/note.md"


def test_a_project_copy_of_a_global_type_collides_with_the_library(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, _ = installed_project(tmp_path, monkeypatch)
    notes = write_collection(project, "kb/notes")
    write_type_spec(project, "kb/types/note.md", name="note", schema=None)

    with pytest.raises(ValueError, match="names two different files"):
        type_resolver.resolve_type(
            notes / "sample.md", {"type": "types/note.md"}, repo_root=project
        )


def test_library_collection_local_types_are_not_on_a_projects_search_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, _ = installed_project(tmp_path, monkeypatch)
    reference = write_collection(project, "kb/reference")
    write_type_spec(project, "kb/reference/types/adr.md", name="adr", schema=None)

    profile = type_resolver.resolve_type(
        reference / "decision.md", {"type": "reference/types/adr.md"}, repo_root=project
    )

    assert profile.type_doc_path == project / "kb" / "reference" / "types" / "adr.md"


def test_project_types_directory_has_no_shared_standing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project, _ = installed_project(tmp_path, monkeypatch)
    notes = write_collection(project, "kb/notes")
    write_type_spec(project, "kb/types/my-type.md", name="my-type", schema=None)

    with pytest.raises(ValueError, match="is not eligible in collection"):
        type_resolver.resolve_type(
            notes / "sample.md", {"type": "types/my-type.md"}, repo_root=project
        )
