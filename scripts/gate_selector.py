#!/usr/bin/env python3
"""Select stale (note, gate) pairs for gate-based review."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from gate_core import (
    GateDefinition,
    body_change_ratio,
    compute_watched_hash,
    load_all_gate_definitions,
    load_bundle_gate_ids,
    load_gate_definition,
    load_note_regions,
    non_body_watches,
    path_changed_since_commit,
    read_note_text_at_commit,
    resolve_reviewable_note_paths,
)
from gate_reviews import gate_review_csv_path, load_gate_review_index, require_review_model
from review_metadata import git_blob_sha


@dataclass(frozen=True)
class StaleGate:
    note_path: str
    gate_id: str
    reason: str
    lens: str


def render_stale_gate(record: StaleGate) -> dict[str, str]:
    return {
        "note_path": record.note_path,
        "gate_id": record.gate_id,
        "reason": record.reason,
    }


def _load_target_gates(
    repo_root: Path,
    bundle_id: str | None,
    include_all_gates: bool,
) -> list[GateDefinition]:
    gates_root = repo_root / "kb" / "instructions" / "review-gates"
    bundles_root = repo_root / "kb" / "instructions" / "review-bundles"

    if include_all_gates:
        return load_all_gate_definitions(gates_root)
    if bundle_id is None:
        raise ValueError("provide a bundle id or pass --all-gates")

    gate_ids = load_bundle_gate_ids(bundles_root, bundle_id)
    return [load_gate_definition(gates_root, gate_id) for gate_id in gate_ids]


def _evaluate_gate(
    repo_root: Path,
    note_path: Path,
    gate: GateDefinition,
    review_index: dict[tuple[str, str, str], object],
    current_model: str,
) -> StaleGate | None:
    note = load_note_regions(note_path, repo_root)
    record = review_index.get((note.rel_path, gate.gate_id, current_model))
    if record is None:
        return StaleGate(note.rel_path, gate.gate_id, "missing-review", gate.lens)

    current_gate_hash = git_blob_sha(gate.path)
    if record.gate_hash != current_gate_hash:
        return StaleGate(note.rel_path, gate.gate_id, "gate-changed", gate.lens)

    note_rel_path = Path(note.rel_path)
    try:
        note_changed = path_changed_since_commit(
            repo_root,
            note_rel_path,
            record.recorded_commit,
        )
    except ValueError:
        return StaleGate(
            note.rel_path,
            gate.gate_id,
            "invalid-recorded-commit",
            gate.lens,
        )

    if not note_changed:
        return None

    if gate.staleness.mode == "changed":
        current_watched_hash = compute_watched_hash(note, gate.watches)
        if current_watched_hash != record.watched_hash:
            return StaleGate(note.rel_path, gate.gate_id, "watched-changed", gate.lens)
        return None

    exact_watches = non_body_watches(gate)
    current_watched_hash = compute_watched_hash(note, exact_watches)
    if current_watched_hash != record.watched_hash:
        return StaleGate(note.rel_path, gate.gate_id, "watched-changed", gate.lens)

    if "body" not in gate.watches:
        return None

    try:
        accepted_text = read_note_text_at_commit(
            repo_root,
            note_rel_path,
            record.recorded_commit,
        )
    except ValueError:
        return StaleGate(
            note.rel_path,
            gate.gate_id,
            "invalid-recorded-commit",
            gate.lens,
        )

    ratio = body_change_ratio(accepted_text, note.text)
    threshold = gate.staleness.threshold or 0.0
    if ratio > threshold:
        return StaleGate(note.rel_path, gate.gate_id, "body-rewrite", gate.lens)
    return None


def select_stale_gates(
    repo_root: Path,
    *,
    bundle_id: str | None = None,
    include_all_gates: bool = False,
    raw_note_paths: list[str] | None = None,
) -> list[StaleGate]:
    review_index = load_gate_review_index(
        gate_review_csv_path(repo_root)
    )
    current_model = require_review_model()
    notes = resolve_reviewable_note_paths(repo_root, raw_note_paths)
    gates = _load_target_gates(repo_root, bundle_id, include_all_gates)

    stale_records: list[StaleGate] = []
    for note_path in notes:
        for gate in gates:
            stale = _evaluate_gate(repo_root, note_path, gate, review_index, current_model)
            if stale is not None:
                stale_records.append(stale)
    return sorted(stale_records, key=lambda item: (item.note_path, item.gate_id))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="List stale (note, gate) review pairs.",
    )
    parser.add_argument(
        "bundle_id",
        nargs="?",
        help="Bundle id such as frontmatter-review or prose-review.",
    )
    parser.add_argument(
        "note_paths",
        nargs="*",
        help="Optional note path filter, for example kb/notes/backlinks.md.",
    )
    parser.add_argument(
        "--all-gates",
        action="store_true",
        help="Select against every gate definition instead of one bundle.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON change records.",
    )
    return parser


def _print_grouped(stale_records: list[StaleGate]) -> None:
    grouped: dict[str, list[StaleGate]] = {}
    for record in stale_records:
        grouped.setdefault(record.note_path, []).append(record)

    for note_path in sorted(grouped):
        print(note_path)
        for record in sorted(grouped[note_path], key=lambda item: item.gate_id):
            print(f"  - {record.gate_id} ({record.reason})")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if args.bundle_id is None and not args.all_gates:
        parser.error("provide a bundle id or pass --all-gates")
    if args.bundle_id is not None and args.all_gates:
        parser.error("bundle id and --all-gates are mutually exclusive")

    repo_root = Path.cwd()
    try:
        stale_records = select_stale_gates(
            repo_root,
            bundle_id=args.bundle_id,
            include_all_gates=args.all_gates,
            raw_note_paths=args.note_paths,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    if args.json:
        print(json.dumps([render_stale_gate(item) for item in stale_records], indent=2))
        return

    _print_grouped(stale_records)


if __name__ == "__main__":
    main()
