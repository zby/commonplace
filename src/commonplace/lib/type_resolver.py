"""Resolve structural note types from type-spec documents.

A type value is the spec's path under a KB root, with its `.md` extension:
`types/note.md` for a global type, `reference/types/adr.md` for a
collection-local one (ADR 088). It is looked up on a two-root search path: the
library root, for global types (`types/<name>.md`) only, and the root of the KB
that holds the artifact. A value that finds two different files is an error, so
no root can shadow the other. The written value is the type's identity.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass
from functools import cache
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import url2pathname

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource

from commonplace.lib import frontmatter
from commonplace.lib.library import library_root
from commonplace.lib.project_paths import collection_for_path, kb_root


@dataclass(frozen=True)
class TypeProfile:
    type_path: str
    type_doc_path: Path | None
    type_name: str
    schema_path: Path | None
    schema: dict[str, Any] | None = None


TYPE_SPEC = "types/type-spec.md"
GLOBAL_TYPE_VALUE = re.compile(r"^types/[a-z0-9][a-z0-9-]*\.md$")
_BARE_NAME = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SCHEMA_URI_SCHEME = "commonplace"


def global_types_dir() -> Path:
    return library_root() / "types"


def _is_global_type_doc(path: Path) -> bool:
    return path.resolve().is_relative_to(global_types_dir().resolve())


def _display_path(path: Path, workspace_root: Path) -> str:
    try:
        return path.relative_to(workspace_root).as_posix()
    except ValueError:
        return path.as_posix()


def _validate_repo_relative_kb_path(
    value: Any,
    *,
    workspace_root: Path,
    suffix: str,
    field_name: str,
    source_file: Path | None = None,
    boundary: Path | None = None,
) -> tuple[str, Path]:
    """Validate a path-valued field. Accepts two forms:

    - Repo-relative: starts with ``kb/``. Resolved against ``workspace_root``.
    - File-relative: starts with ``./`` or ``../``. Resolved against
      ``source_file.parent``. Requires ``source_file``.

    In both cases the resolved path must stay under ``boundary``, which defaults
    to ``workspace_root/kb/``. A file inside the library passes the library root
    as its boundary and may only use the file-relative form.
    Returns ``(canonical_repo_rel, resolved_path)`` where
    ``canonical_repo_rel`` is always the normalized ``kb/...`` form (so
    downstream identity comparisons like ``TYPE_SPEC_PATH`` work regardless
    of input style).
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name}: must be a non-empty path")

    rel = value.strip()
    parsed = urlparse(rel)
    if parsed.scheme or parsed.netloc:
        raise ValueError(f"{field_name}: URLs are not valid type paths: {rel}")

    path = Path(rel)
    if path.is_absolute():
        raise ValueError(f"{field_name}: absolute paths are not valid: {rel}")

    is_file_relative = rel.startswith(("./", "../"))
    is_repo_relative = rel.startswith("kb/")

    if not (is_file_relative or is_repo_relative):
        raise ValueError(
            f"{field_name}: must start with kb/ or be file-relative (./ or ../): {rel}"
        )

    if not rel.endswith(suffix):
        raise ValueError(f"{field_name}: must end with {suffix}: {rel}")

    if is_repo_relative:
        if ".." in path.parts:
            raise ValueError(
                f"{field_name}: repo-relative paths must not contain '..': {rel}"
            )
        resolved = (workspace_root / path).resolve()
    else:  # is_file_relative
        if source_file is None:
            raise ValueError(
                f"{field_name}: file-relative path requires source file context: {rel}"
            )
        resolved = (source_file.parent / path).resolve()

    limit = (boundary or kb_root(workspace_root)).resolve()
    try:
        resolved.relative_to(limit)
    except ValueError as exc:
        raise ValueError(f"{field_name}: path must stay under {_display_path(limit, workspace_root)}/: {rel}") from exc

    try:
        canonical = resolved.relative_to(workspace_root.resolve()).as_posix()
    except ValueError:
        canonical = resolved.as_posix()
    return canonical, resolved


def kb_root_for(file_path: Path | None, repo_root: Path) -> Path:
    """The root of the KB that holds file_path: the library root for a library file."""
    project_kb = kb_root(repo_root).resolve()
    if file_path is None:
        return project_kb
    resolved = file_path.resolve()
    library = library_root().resolve()
    if resolved.is_relative_to(library) and not resolved.is_relative_to(project_kb):
        return library
    return project_kb


def _suggested_type_value(rel: str, repo_root: Path, source_file: Path | None) -> str | None:
    """The ADR 088 spelling of a retired type value, when it can be derived."""
    if _BARE_NAME.match(rel):
        return f"types/{rel}.md"
    if rel.startswith("kb/"):
        return rel[len("kb/") :]
    if rel.startswith(("./", "../")) and source_file is not None:
        target = (source_file.parent / rel).resolve()
        for root in (kb_root_for(source_file, repo_root), library_root().resolve()):
            if target.is_relative_to(root):
                return target.relative_to(root).as_posix()
    return None


def validate_type_path(
    value: Any,
    *,
    repo_root: Path,
    source_file: Path | None = None,
) -> tuple[str, Path]:
    """Validate a frontmatter type value and find its spec on the search path.

    Returns the value, which is the type's identity, and the spec path. A value
    that names no file returns the path it would name, so the caller reports a
    missing spec. A value found under both roots as two different files is
    rejected.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError("frontmatter.type: must be a non-empty path")
    rel = value.strip()
    path = Path(rel)
    retired = (
        _BARE_NAME.match(rel)
        or rel.startswith(("./", "../", "kb/"))
    )
    if retired:
        suggestion = _suggested_type_value(rel, repo_root, source_file)
        hint = f"; use `type: {suggestion}`" if suggestion else ""
        raise ValueError(
            "frontmatter.type: a type value is the spec's path under a KB root, "
            f"such as types/note.md or reference/types/adr.md, not {rel}{hint}"
        )
    if urlparse(rel).scheme or path.is_absolute() or ".." in path.parts:
        raise ValueError(f"frontmatter.type: not a KB-relative path: {rel}")
    if not rel.endswith(".md"):
        raise ValueError(f"frontmatter.type: must end with .md: {rel}")

    candidates = []
    if GLOBAL_TYPE_VALUE.match(rel):
        candidates.append((library_root() / path).resolve())
    candidates.append((kb_root_for(source_file, repo_root) / path).resolve())
    found = list(dict.fromkeys(c for c in candidates if c.is_file()))
    if len(found) > 1:
        shown = " and ".join(_display_path(f, repo_root.resolve()) for f in found)
        raise ValueError(
            f"frontmatter.type: {rel} names two different files, {shown}; "
            "delete or rename the project's copy"
        )
    return rel, (found[0] if found else candidates[0])


def validate_type_eligibility(
    file_path: Path,
    type_doc_path: Path,
    *,
    repo_root: Path,
) -> None:
    """Reject collection-local types used outside their owning collection.

    Global types in the library are eligible everywhere. A collection may
    also use specs under its own ``types/`` directory. The ``kb/work/``
    lifecycle subtree may use any valid type spec. Files that are not inside a
    declared collection retain the referential-only behavior.
    """
    workspace_root = repo_root.resolve()
    boundary = kb_root(workspace_root).resolve()
    artifact = file_path.resolve()
    type_doc = type_doc_path.resolve()

    try:
        artifact_rel = artifact.relative_to(boundary)
    except ValueError:
        return

    if artifact_rel.parts and artifact_rel.parts[0] == "work":
        return

    try:
        collection = collection_for_path(artifact, workspace_root)
    except ValueError:
        return

    if _is_global_type_doc(type_doc):
        return

    local_types = collection / "types"
    if type_doc.is_relative_to(local_types):
        return

    type_display = _display_path(type_doc, workspace_root)
    collection_display = _display_path(collection, workspace_root)
    local_display = _display_path(local_types, workspace_root)
    raise ValueError(
        f"frontmatter.type: {type_display} is not eligible in collection "
        f"{collection_display}; use a global type (types/<name>.md) or a local "
        f"type under {local_display}/"
    )


# Reads a type spec's frontmatter. Validation runs pass a loader backed by their
# parse cache so each type document is read once per run, not once per artifact.
FrontmatterLoader = Callable[[Path], frontmatter.FrontmatterResult]


def read_frontmatter(path: Path) -> frontmatter.FrontmatterResult:
    return frontmatter.parse(path.read_text(encoding="utf-8"))


def _load_type_frontmatter(
    type_doc_path: Path, type_doc_rel: str, load: FrontmatterLoader
) -> dict[str, Any]:
    if not type_doc_path.is_file():
        raise FileNotFoundError(
            f"frontmatter.type points to a missing type spec: {type_doc_rel}"
        )
    parsed = load(type_doc_path)
    if not parsed.ok:
        raise ValueError(
            f"{type_doc_rel}: invalid type-spec frontmatter: {'; '.join(parsed.errors)}"
        )
    if not parsed.data:
        raise ValueError(f"{type_doc_rel}: type spec must have frontmatter")
    return parsed.data


def _schema_path_from_type_doc(
    type_doc_rel: str,
    type_doc_path: Path,
    type_frontmatter: dict[str, Any],
    workspace_root: Path,
    boundary: Path | None = None,
) -> Path | None:
    if "schema" not in type_frontmatter:
        raise ValueError(f"{type_doc_rel}: type spec frontmatter must include schema")

    schema_value = type_frontmatter["schema"]
    if schema_value is None:
        return None

    schema_rel, schema_path = _validate_repo_relative_kb_path(
        schema_value,
        workspace_root=workspace_root,
        suffix=".schema.yaml",
        field_name=f"{type_doc_rel}.schema",
        source_file=type_doc_path,
        boundary=boundary,
    )
    if not schema_path.is_file():
        raise FileNotFoundError(f"{type_doc_rel}: schema file is missing: {schema_rel}")
    return schema_path


def _load_schema(path_str: str) -> dict[str, Any]:
    return _load_schema_with_library(path_str, str(library_root()))


def _library_refs_to_files(node: Any, library: Path) -> Any:
    """Rewrite `commonplace:<path>` $refs to the library file's URI.

    Relative refs inside the referenced schema then resolve against an ordinary
    file URI; urljoin does not join relative paths onto an unknown scheme.
    """
    prefix = f"{SCHEMA_URI_SCHEME}:"
    if isinstance(node, dict):
        return {
            key: (
                (library / value[len(prefix) :]).resolve().as_uri()
                if key == "$ref" and isinstance(value, str) and value.startswith(prefix)
                else _library_refs_to_files(value, library)
            )
            for key, value in node.items()
        }
    if isinstance(node, list):
        return [_library_refs_to_files(item, library) for item in node]
    return node


@cache
def _load_schema_with_library(path_str: str, library_str: str) -> dict[str, Any]:
    path = Path(path_str)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise TypeError(f"{path}: schema must load to a mapping")
    raw = _library_refs_to_files(raw, Path(library_str))
    if "$id" not in raw:
        raw = {"$id": path.resolve().as_uri(), **raw}
    return raw


def _retrieve_schema(uri: str) -> Resource:
    parsed = urlparse(uri)
    if parsed.scheme != "file":
        raise NoSuchResource(ref=uri)
    path = Path(url2pathname(parsed.path))
    # Keep the requested URI as the base so nested relative refs resolve from
    # where the referencing schema expected this one to live.
    return Resource.from_contents({**_load_schema(str(path)), "$id": uri})


def _validator_for_path(path_str: str) -> Draft202012Validator:
    return _validator_for_path_with_library(path_str, str(library_root()))


@cache
def _validator_for_path_with_library(path_str: str, library_str: str) -> Draft202012Validator:
    return Draft202012Validator(
        _load_schema(path_str),
        registry=Registry(retrieve=_retrieve_schema),
        format_checker=FormatChecker(),
    )


def canonical_type_identity(profile: TypeProfile) -> str:
    """Return the identity used for type-owned behavior.

    It is the spec's path under its KB root, as written in `type:` values.
    """
    return profile.type_path


def resolve_type_definition(
    type_doc_path: Path,
    *,
    repo_root: Path,
    load_frontmatter: FrontmatterLoader = read_frontmatter,
) -> TypeProfile:
    """Load one identified type-spec document and its declared schema."""
    workspace_root = repo_root.resolve()
    resolved_type_doc = type_doc_path.resolve()
    project_kb = kb_root(workspace_root).resolve()
    library = library_root().resolve()
    if resolved_type_doc.is_relative_to(project_kb):
        root = project_kb
    elif resolved_type_doc.is_relative_to(library):
        root = library
    else:
        raise ValueError(
            f"type definition path must stay under a KB root: {type_doc_path}"
        )
    # A library file outside the project may only use file-relative schema paths.
    boundary = library if root == library and root != project_kb else None
    type_doc_rel = resolved_type_doc.relative_to(root).as_posix()
    type_frontmatter = _load_type_frontmatter(
        resolved_type_doc, type_doc_rel, load_frontmatter
    )

    if type_frontmatter.get("type") != TYPE_SPEC:
        raise ValueError(f"{type_doc_rel}: type spec must declare type: {TYPE_SPEC}")

    type_name = type_frontmatter.get("name")
    if not isinstance(type_name, str) or not type_name.strip():
        raise ValueError(f"{type_doc_rel}: type spec frontmatter must include name")
    if (
        not isinstance(type_frontmatter.get("description"), str)
        or not type_frontmatter["description"].strip()
    ):
        raise ValueError(
            f"{type_doc_rel}: type spec frontmatter must include description"
        )

    schema_path = _schema_path_from_type_doc(
        type_doc_rel,
        resolved_type_doc,
        type_frontmatter,
        workspace_root,
        boundary=boundary,
    )
    schema = (
        _load_schema(str(schema_path.resolve())) if schema_path is not None else None
    )
    return TypeProfile(
        type_path=type_doc_rel,
        type_doc_path=resolved_type_doc,
        type_name=type_name.strip(),
        schema_path=schema_path,
        schema=schema,
    )


def resolve_type(
    file_path: Path,
    frontmatter: dict[str, Any] | None,
    *,
    repo_root: Path,
    load_frontmatter: FrontmatterLoader = read_frontmatter,
) -> TypeProfile:
    """Resolve a note's type profile from its frontmatter."""
    workspace_root = repo_root.resolve()
    if frontmatter is None:
        return TypeProfile(
            type_path="text",
            type_doc_path=None,
            type_name="text",
            schema_path=None,
            schema=None,
        )

    if "type" not in frontmatter:
        raise ValueError("frontmatter.type is required for files with frontmatter")

    _, type_doc_path = validate_type_path(
        frontmatter["type"],
        repo_root=workspace_root,
        source_file=file_path,
    )
    profile = resolve_type_definition(
        type_doc_path,
        repo_root=workspace_root,
        load_frontmatter=load_frontmatter,
    )
    assert profile.type_doc_path is not None
    validate_type_eligibility(
        file_path,
        profile.type_doc_path,
        repo_root=workspace_root,
    )
    return profile


def validate_instance(
    profile: TypeProfile, instance: dict[str, Any]
) -> list[ValidationError]:
    if profile.schema_path is None or profile.schema is None:
        return []
    # Schemas pin `const: <identity>`; the written value is the identity already,
    # but a caller may pass an instance built from a differently spelled value.
    fm = instance.get("frontmatter")
    schema_type_path = canonical_type_identity(profile)
    if isinstance(fm, dict) and fm.get("type") != schema_type_path:
        instance = {**instance, "frontmatter": {**fm, "type": schema_type_path}}
    validator = _validator_for_path(str(profile.schema_path.resolve()))
    return sorted(
        validator.iter_errors(instance),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
