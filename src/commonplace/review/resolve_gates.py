"""Library helpers for resolving gate IDs and bundle names."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from commonplace.lib import frontmatter


def resolve_to_gate_ids(args: list[str], gates_dir: Path) -> list[str]:
    gate_ids: list[str] = []
    for arg in args:
        bundle_dir = gates_dir / arg
        if bundle_dir.is_dir():
            for gate_file in sorted(bundle_dir.glob("*.md")):
                gate_ids.append(f"{arg}/{gate_file.stem}")
        else:
            gate_file = gates_dir / f"{arg}.md"
            if not gate_file.is_file():
                raise FileNotFoundError(f"gate not found: {arg}")
            gate_ids.append(arg)
    return gate_ids


def _load_frontmatter(path: Path) -> dict[str, Any]:
    try:
        parsed = frontmatter.parse(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError):
        return {}
    if not parsed.ok:
        return {}
    return parsed.data


def applicable_gate_ids_for_note(note_path: Path, gate_ids: list[str], gates_dir: Path) -> list[str]:
    note_traits_raw = _load_frontmatter(note_path).get("traits", [])
    note_traits = set(note_traits_raw) if isinstance(note_traits_raw, list) else set()

    applicable: list[str] = []
    for gate_id in gate_ids:
        gate_abs = gates_dir / f"{gate_id}.md"
        gate_meta = _load_frontmatter(gate_abs)
        requires_trait = gate_meta.get("requires_trait")
        if requires_trait and requires_trait not in note_traits:
            continue
        applicable.append(gate_id)
    return applicable
