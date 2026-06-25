"""Gate packing helpers for note-local review execution."""

from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.paths import gate_path_for_id, review_gates_dir
from commonplace.review.resolve_gates import applicable_gate_ids_for_note, resolve_to_gate_ids


@dataclass(frozen=True)
class GateBundleGroup:
    bundle: str
    gate_ids: list[str]
    gate_paths: list[str]


def bundle_for_gate_id(gate_id: str) -> str:
    bundle, separator, _ = gate_id.partition("/")
    if not separator:
        return ""
    return bundle


def group_requested_gates_by_bundle(
    *,
    repo_root: Path,
    note_path: str,
    gate_or_bundle: list[str],
) -> list[GateBundleGroup]:
    note_abs = repo_root / note_path
    gates_dir = review_gates_dir(repo_root)
    requested_gate_ids = resolve_to_gate_ids(gate_or_bundle, gates_dir)
    gate_ids = applicable_gate_ids_for_note(note_abs, requested_gate_ids, gates_dir)
    if not gate_ids:
        raise ValueError(f"no applicable gates resolved for note: {note_path}")

    grouped: OrderedDict[str, list[str]] = OrderedDict()
    for gate_id in gate_ids:
        grouped.setdefault(bundle_for_gate_id(gate_id), []).append(gate_id)

    return [
        GateBundleGroup(
            bundle=bundle,
            gate_ids=bundle_gate_ids,
            gate_paths=[gate_path_for_id(repo_root, gate_id) for gate_id in bundle_gate_ids],
        )
        for bundle, bundle_gate_ids in grouped.items()
    ]
