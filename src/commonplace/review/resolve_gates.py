"""Library helpers for resolving gate IDs and bundle names."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from commonplace.lib import frontmatter
from commonplace.review.type_conformance import TYPE_GATE_LENS, is_type_gate_request


def _reject_unsafe_gate_arg(arg: str) -> None:
    path = Path(arg)
    if path.is_absolute() or arg.strip() in {"", "."} or ".." in path.parts:
        raise ValueError(f"gate id or bundle must stay inside the review gate catalog: {arg}")


def resolve_gate_requests(requests: list[str], gates_dir: Path) -> list[str]:
    """Resolve mixed gate/bundle/type requests into selector gate ids.

    Catalog gate ids and bundle names expand against the gate catalog; virtual
    type-conformance requests (`type`, `type/{name}`) pass through for the
    selector's second gate source.
    """
    type_requests = [arg for arg in requests if is_type_gate_request(arg)]
    catalog_requests = [arg for arg in requests if not is_type_gate_request(arg)]
    gate_ids = resolve_to_gate_ids(catalog_requests, gates_dir) if catalog_requests else []
    gate_ids.extend(type_requests)
    return gate_ids


def all_gate_requests(gates_dir: Path) -> list[str]:
    """Every applicable review criterion: all catalog bundles plus the virtual `type` lens.

    The single definition of `--all-gates` for every review command, so the
    flag means the same thing everywhere. Commands whose mechanism cannot act
    on a type pair (auto-ack needs `watches:`, which type specs do not declare)
    skip those pairs by that same rule, not by a narrower flag meaning.
    """
    bundles = sorted(d.name for d in gates_dir.iterdir() if d.is_dir())
    return resolve_to_gate_ids(bundles, gates_dir) + [TYPE_GATE_LENS]


def resolve_to_gate_ids(args: list[str], gates_dir: Path) -> list[str]:
    gate_ids: list[str] = []
    for arg in args:
        arg = arg.strip()
        _reject_unsafe_gate_arg(arg)
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


def _matches_requirement(actual_values: set[str], required: Any) -> bool:
    if required is None or required == "":
        return True
    if isinstance(required, str):
        return required in actual_values
    if isinstance(required, list):
        required_values = {item for item in required if isinstance(item, str)}
        return not required or bool(actual_values & required_values)
    return False


def applicable_gate_ids_for_note(note_path: Path, gate_ids: list[str], gates_dir: Path) -> list[str]:
    note_meta = _load_frontmatter(note_path)
    note_type_raw = note_meta.get("type")
    note_types = {note_type_raw} if isinstance(note_type_raw, str) else set()
    note_traits_raw = note_meta.get("traits", [])
    note_traits = set(note_traits_raw) if isinstance(note_traits_raw, list) else set()

    applicable: list[str] = []
    for gate_id in gate_ids:
        gate_abs = gates_dir / f"{gate_id}.md"
        gate_meta = _load_frontmatter(gate_abs)
        if not _matches_requirement(note_traits, gate_meta.get("requires_trait")):
            continue
        if not _matches_requirement(note_types, gate_meta.get("requires-type")):
            continue
        applicable.append(gate_id)
    return applicable
