"""Resolve path-valued structural note types from type-spec documents."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlparse
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource

from commonplace.lib import frontmatter
from commonplace.lib.project_paths import kb_root


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

    is_file_relative = rel.startswith("./") or rel.startswith("../")
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


def _load_type_frontmatter(type_doc_path: Path, workspace_root: Path) -> dict[str, Any]:
    if not type_doc_path.is_file():
        raise FileNotFoundError(
            f"frontmatter.type points to a missing type spec: {_display_path(type_doc_path, workspace_root)}"
        )
    parsed = frontmatter.parse(type_doc_path.read_text(encoding="utf-8"))
    if not parsed.ok:
        raise ValueError(
            f"{_display_path(type_doc_path, workspace_root)}: invalid type-spec frontmatter: {'; '.join(parsed.errors)}"
        )
    if not parsed.data:
        raise ValueError(f"{_display_path(type_doc_path, workspace_root)}: type spec must have frontmatter")
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


@lru_cache(maxsize=None)
def _load_schema(path_str: str) -> dict[str, Any]:
    path = Path(path_str)
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: schema must load to a mapping")
    if "$id" not in raw:
        raw = {"$id": path.resolve().as_uri(), **raw}
    return raw


def _iter_local_refs(node: Any) -> tuple[str, ...]:
    refs: list[str] = []
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str):
            parsed = urlparse(ref)
            if not parsed.scheme and not ref.startswith("#"):
                refs.append(ref)
        for value in node.values():
            refs.extend(_iter_local_refs(value))
    elif isinstance(node, list):
        for item in node:
            refs.extend(_iter_local_refs(item))
    return tuple(refs)


def _resolve_local_schema_ref(base_path: Path, ref: str) -> Path:
    resolved = (base_path.parent / ref).resolve()
    if resolved.exists():
        return resolved

    parts = resolved.parts
    for idx in range(len(parts) - 2):
        if parts[idx : idx + 3] == ("kb", "commonplace", "types"):
            fallback = Path(*parts[: idx + 1], "types", *parts[idx + 3 :])
            if fallback.exists():
                return fallback
    return resolved


def _register_schema_alias_tree(
    registry: Registry,
    *,
    actual_path: Path,
    alias_path: Path,
    seen: set[Path] | None = None,
) -> Registry:
    if seen is None:
        seen = set()

    actual = actual_path.resolve()
    alias = alias_path.resolve()
    if alias in seen:
        return registry
    seen.add(alias)

    schema = {**_load_schema(str(actual)), "$id": alias.as_uri()}
    registry = registry.with_resource(alias.as_uri(), Resource.from_contents(schema))
    for ref in _iter_local_refs(schema):
        unresolved_child = (alias.parent / ref).resolve()
        actual_child = _resolve_local_schema_ref(actual, ref)
        registry = _register_schema_alias_tree(
            registry,
            actual_path=actual_child,
            alias_path=unresolved_child,
            seen=seen,
        )
    return registry


def _build_registry_for_path(path: Path, registry: Registry | None = None, seen: set[Path] | None = None) -> Registry:
    if registry is None:
        registry = Registry()
    if seen is None:
        seen = set()

    resolved = path.resolve()
    if resolved in seen:
        return registry
    seen.add(resolved)

    schema = _load_schema(str(resolved))
    registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))

    for ref in _iter_local_refs(schema):
        unresolved = (resolved.parent / ref).resolve()
        ref_path = _resolve_local_schema_ref(resolved, ref)
        registry = _build_registry_for_path(ref_path, registry, seen)
        if ref_path != unresolved:
            registry = _register_schema_alias_tree(
                registry,
                actual_path=ref_path,
                alias_path=unresolved,
            )
    return registry


@lru_cache(maxsize=None)
def _validator_for_path(path_str: str) -> Draft202012Validator:
    path = Path(path_str).resolve()
    schema = _load_schema(str(path))
    registry = _build_registry_for_path(path)
    return Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())


def _schema_identity_type_path(profile: TypeProfile) -> str:
    parts = Path(profile.type_path).parts
    if len(parts) >= 4 and parts[0] == "kb" and parts[1] == "commonplace":
        return Path("kb", *parts[2:]).as_posix()
    return profile.type_path


def resolve_type(
    file_path: Path,
    frontmatter: dict[str, Any] | None,
    *,
    repo_root: Path,
) -> TypeProfile:
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

    type_doc_rel, type_doc_path = validate_type_path(
        frontmatter["type"],
        repo_root=workspace_root,
        source_file=file_path,
    )
    type_frontmatter = _load_type_frontmatter(type_doc_path, workspace_root)
    declared_type = type_frontmatter.get("type")
    if type_doc_rel == TYPE_SPEC_PATH:
        expected_type = TYPE_SPEC_PATH
    else:
        expected_type = TYPE_SPEC_PATH
    if declared_type != expected_type:
        raise ValueError(
            f"{type_doc_rel}: type spec must declare type: {expected_type}"
        )

    type_name = type_frontmatter.get("name")
    if not isinstance(type_name, str) or not type_name.strip():
        raise ValueError(f"{type_doc_rel}: type spec frontmatter must include name")
    if not isinstance(type_frontmatter.get("description"), str) or not type_frontmatter["description"].strip():
        raise ValueError(f"{type_doc_rel}: type spec frontmatter must include description")

    schema_path = _schema_path_from_type_doc(
        type_doc_rel,
        type_doc_path,
        type_frontmatter,
        workspace_root,
    )
    schema = _load_schema(str(schema_path.resolve())) if schema_path is not None else None
    return TypeProfile(
        type_path=type_doc_rel,
        type_doc_path=type_doc_path,
        type_name=type_name.strip(),
        schema_path=schema_path,
        schema=schema,
    )


def validate_instance(profile: TypeProfile, instance: dict[str, Any]) -> list[ValidationError]:
    if profile.schema_path is None or profile.schema is None:
        return []
    # Normalize frontmatter.type to the canonical kb/... form so schemas with
    # `const: kb/<col>/types/<name>.md` match regardless of whether the source
    # used repo-relative or file-relative form.
    fm = instance.get("frontmatter")
    schema_type_path = _schema_identity_type_path(profile)
    if isinstance(fm, dict) and fm.get("type") != schema_type_path:
        instance = {**instance, "frontmatter": {**fm, "type": schema_type_path}}
    validator = _validator_for_path(str(profile.schema_path.resolve()))
    return sorted(validator.iter_errors(instance), key=lambda error: tuple(str(part) for part in error.absolute_path))


def validate_type_specs(workspace_root: Path) -> list[str]:
    """Return failures for malformed type-spec docs under kb/**/types/*.md."""
    failures: list[str] = []
    boundary = kb_root(workspace_root)
    if not boundary.is_dir():
        return failures
    for path in sorted(boundary.glob("**/types/*.md")):
        if path.name == "text.md":
            continue
        try:
            parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
            if not parsed.ok:
                failures.append(f"{path.relative_to(workspace_root)}: {'; '.join(parsed.errors)}")
                continue
            resolve_type(path, parsed.data, repo_root=workspace_root)
        except (FileNotFoundError, ValueError) as exc:
            failures.append(f"{path.relative_to(workspace_root)}: {exc}")
    return failures
