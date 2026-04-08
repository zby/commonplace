"""Resolve structural note types from scoped YAML definitions."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WORKSPACE_ROOT = Path.cwd().resolve()

_KEY_RE = re.compile(r"^([a-z][a-z0-9_-]*)\s*:\s*(.*)$")
_LIST_ITEM_RE = re.compile(r"^\s*-\s+(.*)$")
_BOOL_MAP = {"true": True, "false": False}


@dataclass(frozen=True)
class TypeProfile:
    resolved_type: str
    definition_path: Path | None
    required_headings: tuple[str, ...] = ()
    any_headings: tuple[str, ...] = ()
    required_fields: tuple[str, ...] = ()
    allowed_status: tuple[str, ...] = ()
    requires_date: bool = False
    min_links: int | None = None


def _parse_scalar(raw: str) -> Any:
    raw = raw.strip()
    if not raw:
        return ""
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ('"', "'"):
        return raw[1:-1]
    low = raw.lower()
    if low in _BOOL_MAP:
        return _BOOL_MAP[low]
    if raw.isdigit():
        return int(raw)
    return raw


def _parse_inline_list(raw: str) -> list[str]:
    inner = raw[1:-1].strip()
    if not inner:
        return []

    items: list[str] = []
    part_chars: list[str] = []
    quote_char: str | None = None
    for char in inner:
        if quote_char is not None:
            part_chars.append(char)
            if char == quote_char:
                quote_char = None
            continue
        if char in ('"', "'"):
            quote_char = char
            part_chars.append(char)
            continue
        if char == ",":
            items.append(str(_parse_scalar("".join(part_chars).strip())))
            part_chars = []
            continue
        part_chars.append(char)

    if quote_char is not None:
        raise ValueError("unterminated quoted string in inline list")
    items.append(str(_parse_scalar("".join(part_chars).strip())))
    return items


def parse_type_yaml(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_list_key: str | None = None

    for lineno, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if line.startswith((" ", "\t")):
            if current_list_key is None:
                raise ValueError(f"{path}:{lineno}: unexpected indentation")
            match = _LIST_ITEM_RE.match(stripped)
            if match is None:
                raise ValueError(f"{path}:{lineno}: expected list item")
            data[current_list_key].append(str(_parse_scalar(match.group(1))))
            continue

        current_list_key = None
        match = _KEY_RE.match(line)
        if match is None:
            raise ValueError(f"{path}:{lineno}: invalid key/value syntax")
        key, value = match.group(1), match.group(2).strip()
        if key in data:
            raise ValueError(f"{path}:{lineno}: duplicate key '{key}'")
        if not value:
            data[key] = []
            current_list_key = key
            continue
        if value.startswith("[") and value.endswith("]"):
            data[key] = _parse_inline_list(value)
        else:
            data[key] = _parse_scalar(value)

    return data


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
        candidate = scope_root / "types" / f"{type_name}.yaml"
        if candidate.is_file():
            return candidate
    return None


def _merge_sequences(parent: tuple[str, ...], child: list[str] | tuple[str, ...] | None) -> tuple[str, ...]:
    if not child:
        return parent
    merged = list(parent)
    for item in child:
        if item not in merged:
            merged.append(item)
    return tuple(merged)


def _resolve_known_type(type_name: str, file_path: Path, workspace_root: Path, seen: set[str]) -> TypeProfile:
    if type_name in seen:
        chain = " -> ".join([*sorted(seen), type_name])
        raise ValueError(f"cyclic type inheritance: {chain}")

    definition_path = _definition_path(type_name, file_path, workspace_root)
    if definition_path is None:
        if type_name == "text":
            return TypeProfile(resolved_type="text", definition_path=None)
        if type_name == "note":
            return TypeProfile(resolved_type="note", definition_path=None)
        return _resolve_known_type("note", file_path, workspace_root, seen | {type_name})

    raw = parse_type_yaml(definition_path)
    base = raw.get("base")

    if type_name == "text":
        base_profile = TypeProfile(resolved_type="text", definition_path=definition_path)
    elif isinstance(base, str) and base:
        base_profile = _resolve_known_type(base, file_path, workspace_root, seen | {type_name})
    elif type_name == "note":
        base_profile = TypeProfile(resolved_type="note", definition_path=definition_path)
    else:
        base_profile = _resolve_known_type("note", file_path, workspace_root, seen | {type_name})

    allowed_status = base_profile.allowed_status
    if "allowed_status" in raw:
        allowed_status = tuple(str(item) for item in raw["allowed_status"])

    min_links = base_profile.min_links
    if "min_links" in raw:
        value = raw["min_links"]
        min_links = int(value) if value is not None else None

    return TypeProfile(
        resolved_type=type_name if definition_path is not None else base_profile.resolved_type,
        definition_path=definition_path,
        required_headings=_merge_sequences(base_profile.required_headings, raw.get("required_headings")),
        any_headings=_merge_sequences(base_profile.any_headings, raw.get("any_headings")),
        required_fields=_merge_sequences(base_profile.required_fields, raw.get("required_fields")),
        allowed_status=allowed_status,
        requires_date=bool(raw.get("requires_date", base_profile.requires_date)),
        min_links=min_links,
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
    return _resolve_known_type(type_name, file_path, workspace_root, set())

