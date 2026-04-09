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
    required_headings: tuple[str, ...] = ()
    any_headings: tuple[str, ...] = ()
    required_fields: tuple[str, ...] = ()
    allowed_status: tuple[str, ...] = ()
    requires_date: bool = False
    min_links: int | None = None


def _merge_sequences(parent: tuple[str, ...], child: tuple[str, ...]) -> tuple[str, ...]:
    merged = list(parent)
    for item in child:
        if item not in merged:
            merged.append(item)
    return tuple(merged)


def _merge_allowed_status(parent: tuple[str, ...], child: tuple[str, ...]) -> tuple[str, ...]:
    if not child:
        return parent
    if not parent:
        return child
    return tuple(item for item in parent if item in child)


def _schema_candidate_name(type_name: str) -> str:
    return f"{type_name}.schema.yaml"


def _scope_roots(file_path: Path, workspace_root: Path) -> list[Path]:
    try:
        rel = file_path.resolve().relative_to(workspace_root.resolve())
    except ValueError:
        return [workspace_root]

    parts = rel.parts
    scopes: list[Path] = []
    if len(parts) >= 3 and parts[0] == "kb" and parts[1] == "work":
        scopes.append(workspace_root / "kb" / "work" / parts[2])
    if len(parts) >= 2 and parts[0] == "kb":
        scopes.append(workspace_root / "kb" / parts[1])
    scopes.append(workspace_root)
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


def _frontmatter_required_fields(schema: dict[str, Any]) -> tuple[str, ...]:
    frontmatter = schema.get("properties", {}).get("frontmatter")
    if not isinstance(frontmatter, dict):
        return ()
    required = frontmatter.get("required", [])
    if not isinstance(required, list):
        return ()
    return tuple(str(item) for item in required if str(item) != "type")


def _status_enum(schema: dict[str, Any]) -> tuple[str, ...]:
    frontmatter = schema.get("properties", {}).get("frontmatter")
    if not isinstance(frontmatter, dict):
        return ()
    status = frontmatter.get("properties", {}).get("status")
    if not isinstance(status, dict):
        return ()
    enum = status.get("enum")
    if not isinstance(enum, list):
        return ()
    return tuple(str(item) for item in enum)


def _heading_constraints(schema: dict[str, Any], key: str) -> tuple[str, ...]:
    headings = schema.get("properties", {}).get("headings")
    if not isinstance(headings, dict):
        return ()
    subschemas = headings.get(key)
    if not isinstance(subschemas, list):
        return ()

    values: list[str] = []
    for item in subschemas:
        if not isinstance(item, dict):
            continue
        contains = item.get("contains")
        if not isinstance(contains, dict):
            continue
        value = contains.get("const")
        if isinstance(value, str) and value not in values:
            values.append(value)
    return tuple(values)


def _link_min_items(schema: dict[str, Any]) -> int | None:
    links = schema.get("properties", {}).get("links")
    if not isinstance(links, dict):
        return None
    min_items = links.get("minItems")
    if isinstance(min_items, int):
        return min_items
    return None


def _requires_date(schema: dict[str, Any]) -> bool:
    branches = schema.get("anyOf")
    if not isinstance(branches, list):
        return False

    for branch in branches:
        if not isinstance(branch, dict):
            continue
        props = branch.get("properties", {})
        if not isinstance(props, dict):
            continue
        body_dates = props.get("body_dates")
        if isinstance(body_dates, dict) and isinstance(body_dates.get("minItems"), int) and body_dates["minItems"] >= 1:
            return True
        frontmatter = props.get("frontmatter")
        if not isinstance(frontmatter, dict):
            continue
        required = frontmatter.get("required", [])
        if not isinstance(required, list):
            continue
        if any(field in {"date", "last-checked"} for field in required):
            return True
    return False


def _accumulate_schema_metadata(
    schema: dict[str, Any],
    current_path: Path,
    *,
    seen_paths: set[Path] | None = None,
) -> dict[str, Any]:
    if seen_paths is None:
        seen_paths = set()

    metadata = {
        "required_headings": (),
        "any_headings": (),
        "required_fields": (),
        "allowed_status": (),
        "requires_date": False,
        "min_links": None,
    }

    resolved_path = current_path.resolve()
    if resolved_path not in seen_paths:
        seen_paths.add(resolved_path)

    ref = schema.get("$ref")
    if isinstance(ref, str):
        parsed = urlparse(ref)
        if not parsed.scheme and not ref.startswith("#"):
            ref_path = (current_path.parent / ref).resolve()
            ref_schema = _load_schema(str(ref_path))
            ref_meta = _accumulate_schema_metadata(ref_schema, ref_path, seen_paths=seen_paths)
            metadata["required_headings"] = _merge_sequences(metadata["required_headings"], ref_meta["required_headings"])
            metadata["any_headings"] = _merge_sequences(metadata["any_headings"], ref_meta["any_headings"])
            metadata["required_fields"] = _merge_sequences(metadata["required_fields"], ref_meta["required_fields"])
            metadata["allowed_status"] = _merge_allowed_status(metadata["allowed_status"], ref_meta["allowed_status"])
            metadata["requires_date"] = metadata["requires_date"] or ref_meta["requires_date"]
            if ref_meta["min_links"] is not None:
                metadata["min_links"] = ref_meta["min_links"]

    for subschema in schema.get("allOf", []):
        if not isinstance(subschema, dict):
            continue
        sub_meta = _accumulate_schema_metadata(subschema, current_path, seen_paths=seen_paths)
        metadata["required_headings"] = _merge_sequences(metadata["required_headings"], sub_meta["required_headings"])
        metadata["any_headings"] = _merge_sequences(metadata["any_headings"], sub_meta["any_headings"])
        metadata["required_fields"] = _merge_sequences(metadata["required_fields"], sub_meta["required_fields"])
        metadata["allowed_status"] = _merge_allowed_status(metadata["allowed_status"], sub_meta["allowed_status"])
        metadata["requires_date"] = metadata["requires_date"] or sub_meta["requires_date"]
        if sub_meta["min_links"] is not None:
            metadata["min_links"] = sub_meta["min_links"]

    metadata["required_headings"] = _merge_sequences(metadata["required_headings"], _heading_constraints(schema, "allOf"))
    metadata["any_headings"] = _merge_sequences(metadata["any_headings"], _heading_constraints(schema, "anyOf"))
    metadata["required_fields"] = _merge_sequences(metadata["required_fields"], _frontmatter_required_fields(schema))
    metadata["allowed_status"] = _merge_allowed_status(metadata["allowed_status"], _status_enum(schema))
    metadata["requires_date"] = metadata["requires_date"] or _requires_date(schema)

    min_links = _link_min_items(schema)
    if min_links is not None:
        metadata["min_links"] = min_links

    return metadata


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
            raise FileNotFoundError("types/note.schema.yaml is missing")
        return _resolve_known_type("note", file_path, workspace_root)

    schema = _load_schema(str(definition_path.resolve()))
    metadata = _accumulate_schema_metadata(schema, definition_path)
    return TypeProfile(
        resolved_type=type_name if type_name != "text" else "text",
        definition_path=definition_path,
        schema=schema,
        required_headings=metadata["required_headings"],
        any_headings=metadata["any_headings"],
        required_fields=metadata["required_fields"],
        allowed_status=metadata["allowed_status"],
        requires_date=metadata["requires_date"],
        min_links=metadata["min_links"],
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
