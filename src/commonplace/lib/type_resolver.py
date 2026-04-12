"""Resolve structural note types from scoped JSON Schema definitions."""

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


WORKSPACE_ROOT = Path.cwd().resolve()


@dataclass(frozen=True)
class TypeProfile:
    resolved_type: str
    definition_path: Path | None
    schema: dict[str, Any] | None = None


_SCHEMA_SUFFIX = ".schema.yaml"
_TEMPLATE_SUFFIX = ".template.md"


def _schema_candidate_name(type_name: str) -> str:
    return f"{type_name}{_SCHEMA_SUFFIX}"


def discover_all_types(workspace_root: Path) -> dict[str, list[Path]]:
    """Scan all kb/*/types/ directories for type definitions.

    Returns a mapping of type name → list of definition paths.
    A well-formed KB has exactly one path per type name.
    """
    kb_root = workspace_root / "kb"
    result: dict[str, list[Path]] = {}
    if not kb_root.is_dir():
        return result

    for schema_path in kb_root.rglob(f"types/*{_SCHEMA_SUFFIX}"):
        type_name = schema_path.name.removesuffix(_SCHEMA_SUFFIX)
        result.setdefault(type_name, []).append(schema_path)

    return result


def _collection_names(workspace_root: Path) -> set[str]:
    """Return the names of top-level KB collection directories."""
    kb_root = workspace_root / "kb"
    if not kb_root.is_dir():
        return set()
    return {
        p.name
        for p in kb_root.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    }


def check_type_uniqueness(workspace_root: Path) -> list[str]:
    """Return warnings for type names that collide with each other or with collection names."""
    all_types = discover_all_types(workspace_root)
    collection_names = _collection_names(workspace_root)
    warnings: list[str] = []

    for type_name, paths in sorted(all_types.items()):
        if len(paths) > 1:
            locations = ", ".join(
                str(p.relative_to(workspace_root)) for p in sorted(paths)
            )
            warnings.append(
                f"type {type_name!r} defined in multiple scopes: {locations}"
            )
        if type_name in collection_names:
            warnings.append(
                f"type {type_name!r} collides with collection directory kb/{type_name}/"
            )

    return warnings


def _scope_roots(file_path: Path, workspace_root: Path) -> list[Path]:
    try:
        rel = file_path.resolve().relative_to(workspace_root.resolve())
    except ValueError:
        kb_root = workspace_root / "kb"
        return [kb_root] if kb_root.is_dir() else [workspace_root]

    parts = rel.parts
    scopes: list[Path] = []
    if len(parts) >= 3 and parts[0] == "kb" and parts[1] == "work":
        scopes.append(workspace_root / "kb" / parts[1] / parts[2])
    if len(parts) >= 2 and parts[0] == "kb":
        scopes.append(workspace_root / "kb" / parts[1])
        scopes.append(workspace_root / "kb")
    else:
        kb_root = workspace_root / "kb"
        scopes.append(kb_root if kb_root.is_dir() else workspace_root)
    return scopes


def _definition_path(type_name: str, file_path: Path, workspace_root: Path) -> Path | None:
    for scope_root in _scope_roots(file_path, workspace_root):
        candidate = scope_root / "types" / _schema_candidate_name(type_name)
        if candidate.is_file():
            return candidate
    return None


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
        registry = _build_registry_for_path((resolved.parent / ref).resolve(), registry, seen)
    return registry


@lru_cache(maxsize=None)
def _validator_for_path(path_str: str) -> Draft202012Validator:
    path = Path(path_str).resolve()
    schema = _load_schema(str(path))
    registry = _build_registry_for_path(path)
    return Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())


def _resolve_known_type(type_name: str, file_path: Path, workspace_root: Path) -> TypeProfile:
    definition_path = _definition_path(type_name, file_path, workspace_root)
    if definition_path is None:
        if type_name == "text":
            return TypeProfile(resolved_type="text", definition_path=None)
        if type_name == "note":
            raise FileNotFoundError("kb/types/note.schema.yaml is missing")
        return _resolve_known_type("note", file_path, workspace_root)

    schema = _load_schema(str(definition_path.resolve()))
    return TypeProfile(
        resolved_type=type_name if type_name != "text" else "text",
        definition_path=definition_path,
        schema=schema,
    )


def resolve_type(
    file_path: Path,
    frontmatter: dict[str, Any] | None,
    *,
    repo_root: Path | None = None,
) -> TypeProfile:
    workspace_root = repo_root.resolve() if repo_root is not None else WORKSPACE_ROOT
    if frontmatter is None:
        type_name = "text"
    else:
        type_name = str(frontmatter.get("type", "note") or "note")
    return _resolve_known_type(type_name, file_path, workspace_root)


def validate_instance(profile: TypeProfile, instance: dict[str, Any]) -> list[ValidationError]:
    if profile.definition_path is None or profile.schema is None:
        return []
    validator = _validator_for_path(str(profile.definition_path.resolve()))
    return sorted(validator.iter_errors(instance), key=lambda error: tuple(str(part) for part in error.absolute_path))
