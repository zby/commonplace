"""Library helpers for resolving criterion requests into selector identities."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from commonplace.lib import frontmatter
from commonplace.review.collection_conformance import COLLECTION_CONFORMANCE_LENS, is_collection_conformance_request
from commonplace.review.critique import is_critique_request
from commonplace.review.type_conformance import TYPE_CONFORMANCE_LENS, is_type_conformance_request


def _reject_unsafe_criterion_arg(arg: str) -> None:
    path = Path(arg)
    if path.is_absolute() or arg.strip() in {"", "."} or ".." in path.parts:
        raise ValueError(f"criterion id or bundle must stay inside the review gate catalog: {arg}")


def resolve_criterion_requests(requests: list[str], gates_dir: Path) -> list[str]:
    """Resolve mixed criterion requests into selector criterion ids.

    Catalog gate ids and bundle names expand against the gate catalog; virtual
    conformance requests (`type`, `type/{name}`, `collection`,
    `collection/{path}`) and the report-kind `critique` assay pass through for
    the selector's derived criterion sources.
    """
    passthrough_requests = [
        arg
        for arg in requests
        if is_type_conformance_request(arg) or is_collection_conformance_request(arg) or is_critique_request(arg)
    ]
    catalog_requests = [
        arg
        for arg in requests
        if not is_type_conformance_request(arg)
        and not is_collection_conformance_request(arg)
        and not is_critique_request(arg)
    ]
    criterion_ids = resolve_to_criterion_ids(catalog_requests, gates_dir) if catalog_requests else []
    criterion_ids.extend(passthrough_requests)
    return criterion_ids


def all_gate_requests(gates_dir: Path) -> list[str]:
    """Every applicable review criterion: all catalog bundles plus the virtual
    `type` and `collection` lenses.

    The single definition of `--all-gates` for every review command, so the
    flag means the same thing everywhere. Commands whose mechanism cannot act
    on a conformance pair (auto-ack needs `watches:`, which neither type specs
    nor COLLECTION.md files declare) skip those pairs by that same rule, not
    by a narrower flag meaning.
    """
    bundles = sorted(d.name for d in gates_dir.iterdir() if d.is_dir())
    # The heavyweight report-kind critique assay is intentionally opt-in.
    return resolve_to_criterion_ids(bundles, gates_dir) + [TYPE_CONFORMANCE_LENS, COLLECTION_CONFORMANCE_LENS]


def resolve_to_criterion_ids(args: list[str], gates_dir: Path) -> list[str]:
    criterion_ids: list[str] = []
    for arg in args:
        arg = arg.strip()
        _reject_unsafe_criterion_arg(arg)
        bundle_dir = gates_dir / arg
        if bundle_dir.is_dir():
            for gate_file in sorted(bundle_dir.glob("*.md")):
                criterion_ids.append(f"{arg}/{gate_file.stem}")
        else:
            gate_file = gates_dir / f"{arg}.md"
            if not gate_file.is_file():
                raise FileNotFoundError(f"gate not found: {arg}")
            criterion_ids.append(arg)
    return criterion_ids


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


def applicable_criterion_ids_for_note(note_path: Path, criterion_ids: list[str], gates_dir: Path) -> list[str]:
    note_meta = _load_frontmatter(note_path)
    note_type_raw = note_meta.get("type")
    note_types = {note_type_raw} if isinstance(note_type_raw, str) else set()
    note_traits_raw = note_meta.get("traits", [])
    note_traits = set(note_traits_raw) if isinstance(note_traits_raw, list) else set()

    applicable: list[str] = []
    for criterion_id in criterion_ids:
        gate_abs = gates_dir / f"{criterion_id}.md"
        gate_meta = _load_frontmatter(gate_abs)
        if not _matches_requirement(note_traits, gate_meta.get("requires_trait")):
            continue
        if not _matches_requirement(note_types, gate_meta.get("requires_type")):
            continue
        applicable.append(criterion_id)
    return applicable
