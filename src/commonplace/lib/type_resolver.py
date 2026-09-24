"""Resolve path-valued structural note types from type-spec documents."""

from __future__ import annotations

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
from commonplace.lib.project_paths import collection_for_path, kb_root


@dataclass(frozen=True)
class TypeProfile:
    type_path: str
    type_doc_path: Path | None
    type_name: str
    schema_path: Path | None
    schema: dict[str, Any] | None = None


TYPE_SPEC_PATH = "kb/types/type-spec.md"


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
) -> tuple[str, Path]:
    """Validate a path-valued field. Accepts two forms:

    - Repo-relative: starts with ``kb/``. Resolved against ``workspace_root``.
    - File-relative: starts with ``./`` or ``../``. Resolved against
      ``source_file.parent``. Requires ``source_file``.

    In both cases the resolved path must stay under ``workspace_root/kb/``.
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

    boundary = kb_root(workspace_root).resolve()
    try:
        resolved.relative_to(boundary)
    except ValueError as exc:
        raise ValueError(f"{field_name}: path must stay under kb/: {rel}") from exc

    canonical_repo_rel = resolved.relative_to(workspace_root.resolve()).as_posix()
    return canonical_repo_rel, resolved


def validate_type_path(
    value: Any,
    *,
    repo_root: Path,
    source_file: Path | None = None,
) -> tuple[str, Path]:
    """Validate and resolve a path-valued frontmatter type.

    Accepts repo-relative ``kb/...`` paths or file-relative ``./``/``../``
    paths when ``source_file`` is given. The returned path string is always
    normalized to the ``kb/...`` form.
    """
    return _validate_repo_relative_kb_path(
        value,
        workspace_root=repo_root.resolve(),
        suffix=".md",
        field_name="frontmatter.type",
        source_file=source_file,
    )


def validate_type_eligibility(
    file_path: Path,
    type_doc_path: Path,
    *,
    repo_root: Path,
) -> None:
    """Reject collection-local types used outside their owning collection.

    Global types under ``kb/types/`` are eligible everywhere. A collection may
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

    if type_doc.is_relative_to(boundary / "types"):
        return

    local_types = collection / "types"
    if type_doc.is_relative_to(local_types):
        return

    type_display = _display_path(type_doc, workspace_root)
    collection_display = _display_path(collection, workspace_root)
    local_display = _display_path(local_types, workspace_root)
    raise ValueError(
        f"frontmatter.type: {type_display} is not eligible in collection "
        f"{collection_display}; use a global type under kb/types/ or a local "
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
    )
    if not schema_path.is_file():
        raise FileNotFoundError(f"{type_doc_rel}: schema file is missing: {schema_rel}")
    return schema_path


@cache
def _load_schema(path_str: str) -> dict[str, Any]:
    path = Path(path_str)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise TypeError(f"{path}: schema must load to a mapping")
    if "$id" not in raw:
        raw = {"$id": path.resolve().as_uri(), **raw}
    return raw


def _installed_schema_path(path: Path) -> Path:
    """Map a missing ``kb/commonplace/types/`` ref onto the shared ``kb/types/``.

    Installed framework collections live below ``kb/commonplace/`` while the
    global types they reference stay at ``kb/types/``, so their relative
    ``../../types/`` refs point one level too deep.
    """
    if path.exists():
        return path
    parts = path.parts
    for idx in range(len(parts) - 2):
        if parts[idx : idx + 3] == ("kb", "commonplace", "types"):
            fallback = Path(*parts[: idx + 1], "types", *parts[idx + 3 :])
            if fallback.exists():
                return fallback
    return path


def _retrieve_schema(uri: str) -> Resource:
    parsed = urlparse(uri)
    if parsed.scheme != "file":
        raise NoSuchResource(ref=uri)
    path = _installed_schema_path(Path(url2pathname(parsed.path)))
    # Keep the requested URI as the base so nested relative refs resolve from
    # where the referencing schema expected this one to live.
    return Resource.from_contents({**_load_schema(str(path)), "$id": uri})


@cache
def _validator_for_path(path_str: str) -> Draft202012Validator:
    return Draft202012Validator(
        _load_schema(path_str),
        registry=Registry(retrieve=_retrieve_schema),
        format_checker=FormatChecker(),
    )


def canonical_type_identity(profile: TypeProfile) -> str:
    """Return the portable path identity used for type-owned behavior.

    Installed framework types live below ``kb/commonplace/`` but retain the
    same logical identity as their source paths so schemas and imperative rules
    behave identically in author and installed-reader repositories.
    """
    parts = Path(profile.type_path).parts
    if len(parts) >= 4 and parts[0] == "kb" and parts[1] == "commonplace":
        return Path("kb", *parts[2:]).as_posix()
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
    boundary = kb_root(workspace_root).resolve()
    try:
        resolved_type_doc.relative_to(boundary)
    except ValueError as exc:
        raise ValueError(
            f"type definition path must stay under kb/: {type_doc_path}"
        ) from exc

    type_doc_rel = resolved_type_doc.relative_to(workspace_root).as_posix()
    type_frontmatter = _load_type_frontmatter(
        resolved_type_doc, type_doc_rel, load_frontmatter
    )

    if type_frontmatter.get("type") != TYPE_SPEC_PATH:
        raise ValueError(
            f"{type_doc_rel}: type spec must declare type: {TYPE_SPEC_PATH}"
        )

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
    # Normalize frontmatter.type to the canonical kb/... form so schemas with
    # `const: kb/<col>/types/<name>.md` match regardless of whether the source
    # used repo-relative or file-relative form.
    fm = instance.get("frontmatter")
    schema_type_path = canonical_type_identity(profile)
    if isinstance(fm, dict) and fm.get("type") != schema_type_path:
        instance = {**instance, "frontmatter": {**fm, "type": schema_type_path}}
    validator = _validator_for_path(str(profile.schema_path.resolve()))
    return sorted(
        validator.iter_errors(instance),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
