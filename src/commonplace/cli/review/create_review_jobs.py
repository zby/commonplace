#!/usr/bin/env python3
"""Create queued review jobs from selector output or direct requested pairs."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.batch import prepare_grouped_review_job
from commonplace.review.gate_packing import bundle_for_gate_id
from commonplace.review.paths import gate_id_for_path, normalize_gate_path, review_gates_dir
from commonplace.review.resolve_gates import applicable_gate_ids_for_note
from commonplace.review.review_db import (
    ReviewJobPlan,
    connect,
    list_review_job_plans,
    prepare_review_db,
)
from commonplace.review.review_model import normalize_model_partition


@dataclass(frozen=True)
class RequestedPair:
    note_path: str
    gate_path: str
    gate_id: str
    reason: str


@dataclass(frozen=True)
class SkippedRequestedPair:
    note_path: str | None
    gate_path: str | None
    gate_id: str | None
    reason: str


def _normalize_note_path(repo_root: Path, raw: str) -> str:
    raw_path = Path(raw)
    if raw_path.is_absolute():
        raise ValueError(f"note path must be repo-relative: {raw}")
    normalized = raw_path.as_posix()
    if not (repo_root / normalized).is_file():
        raise ValueError(f"note not found: {raw}")
    return normalized


def _normalize_gate(repo_root: Path, raw: str) -> tuple[str, str]:
    gate_path = normalize_gate_path(repo_root, raw)
    gate_id = gate_id_for_path(repo_root, gate_path)
    return gate_path, gate_id


def _resolve_gate_or_bundle_inputs(repo_root: Path, raw_inputs: list[str]) -> list[tuple[str, str]]:
    gates_dir = review_gates_dir(repo_root)
    resolved: list[tuple[str, str]] = []
    for raw in raw_inputs:
        bundle_dir = gates_dir / raw
        if bundle_dir.is_dir():
            for gate_file in sorted(bundle_dir.glob("*.md")):
                gate_id = f"{raw}/{gate_file.stem}"
                gate_path = gate_file.relative_to(repo_root).as_posix()
                resolved.append((gate_path, gate_id))
            continue
        resolved.append(_normalize_gate(repo_root, raw))
    return resolved


def _parse_pair_arg(repo_root: Path, raw_pair: str) -> RequestedPair:
    note_raw, separator, gate_raw = raw_pair.partition("::")
    note_raw = note_raw.strip()
    gate_raw = gate_raw.strip()
    if not separator or not note_raw or not gate_raw:
        raise ValueError(f"malformed pair (expected note-path::gate): {raw_pair}")
    note_path = _normalize_note_path(repo_root, note_raw)
    gate_path, gate_id = _normalize_gate(repo_root, gate_raw)
    return RequestedPair(note_path=note_path, gate_path=gate_path, gate_id=gate_id, reason="requested")


def _load_selector_json(raw_json: str) -> dict[str, object]:
    try:
        payload = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid selector JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("selector JSON must be an object with model_partition and targets")
    return payload


def _selector_pairs(
    *,
    repo_root: Path,
    raw_json: str,
) -> tuple[str, list[RequestedPair]]:
    payload = _load_selector_json(raw_json)
    raw_model = payload.get("model_partition")
    if raw_model is None:
        raise ValueError("selector JSON model_partition is required for job creation")
    if not isinstance(raw_model, str) or not raw_model.strip():
        raise ValueError("selector JSON model_partition must be a non-empty string")
    model_partition = normalize_model_partition(raw_model)
    raw_targets = payload.get("targets")
    if not isinstance(raw_targets, list):
        raise ValueError("selector JSON targets must be a list")

    pairs: list[RequestedPair] = []
    for index, target in enumerate(raw_targets, start=1):
        if not isinstance(target, dict):
            raise ValueError(f"selector target {index} must be an object")
        note_raw = target.get("note_path")
        gate_raw = target.get("gate_path")
        gate_id_raw = target.get("gate_id")
        reason_raw = target.get("reason", "stale")
        if not isinstance(note_raw, str) or not note_raw.strip():
            raise ValueError(f"selector target {index} missing note_path")
        if not isinstance(gate_raw, str) or not gate_raw.strip():
            raise ValueError(f"selector target {index} missing gate_path")
        if not isinstance(gate_id_raw, str) or not gate_id_raw.strip():
            raise ValueError(f"selector target {index} missing gate_id")
        if not isinstance(reason_raw, str) or not reason_raw.strip():
            reason_raw = "stale"
        note_path = _normalize_note_path(repo_root, note_raw)
        gate_path, gate_id = _normalize_gate(repo_root, gate_raw)
        if gate_id != gate_id_raw.strip():
            raise ValueError(
                f"selector target {index} gate_id {gate_id_raw!r} does not match gate_path {gate_path!r}"
            )
        pairs.append(
            RequestedPair(
                note_path=note_path,
                gate_path=gate_path,
                gate_id=gate_id,
                reason=reason_raw.strip(),
            )
        )
    return model_partition, pairs


def _drop_duplicate_pairs(pairs: list[RequestedPair]) -> tuple[list[RequestedPair], list[SkippedRequestedPair]]:
    seen: set[tuple[str, str]] = set()
    unique: list[RequestedPair] = []
    skipped: list[SkippedRequestedPair] = []
    for pair in pairs:
        key = (pair.note_path, pair.gate_path)
        if key in seen:
            skipped.append(
                SkippedRequestedPair(
                    note_path=pair.note_path,
                    gate_path=pair.gate_path,
                    gate_id=pair.gate_id,
                    reason="duplicate",
                )
            )
            continue
        seen.add(key)
        unique.append(pair)
    return unique, skipped


def _filter_applicable_pairs(
    repo_root: Path,
    pairs: list[RequestedPair],
) -> tuple[list[RequestedPair], list[SkippedRequestedPair]]:
    gates_dir = review_gates_dir(repo_root)
    by_note: dict[str, list[RequestedPair]] = {}
    for pair in pairs:
        by_note.setdefault(pair.note_path, []).append(pair)

    applicable: list[RequestedPair] = []
    skipped: list[SkippedRequestedPair] = []
    for note_path, note_pairs in by_note.items():
        note_abs = repo_root / note_path
        if not note_abs.is_file():
            raise ValueError(f"note not found: {note_path}")
        applicable_gate_ids = set(
            applicable_gate_ids_for_note(
                note_abs,
                [pair.gate_id for pair in note_pairs],
                gates_dir,
            )
        )
        for pair in note_pairs:
            if pair.gate_id in applicable_gate_ids:
                applicable.append(pair)
            else:
                skipped.append(
                    SkippedRequestedPair(
                        note_path=pair.note_path,
                        gate_path=pair.gate_path,
                        gate_id=pair.gate_id,
                        reason="not applicable",
                    )
                )
    return applicable, skipped


def _note_groups(pairs: list[RequestedPair]) -> list[list[RequestedPair]]:
    grouped: dict[tuple[str, str], list[RequestedPair]] = {}
    for pair in pairs:
        grouped.setdefault((pair.note_path, bundle_for_gate_id(pair.gate_id)), []).append(pair)
    return list(grouped.values())


def _chunks(items: list[RequestedPair], size: int) -> list[list[RequestedPair]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def _gate_groups(pairs: list[RequestedPair], batch_size: int) -> list[list[RequestedPair]]:
    grouped: dict[str, list[RequestedPair]] = {}
    for pair in pairs:
        grouped.setdefault(pair.gate_path, []).append(pair)
    result: list[list[RequestedPair]] = []
    for gate_pairs in grouped.values():
        result.extend(_chunks(gate_pairs, batch_size))
    return result


def _group_pairs(pairs: list[RequestedPair], *, grouping: str, batch_size: int) -> list[list[RequestedPair]]:
    if grouping == "note":
        return _note_groups(pairs)
    if grouping == "gate":
        return _gate_groups(pairs, batch_size)
    raise ValueError(f"invalid grouping: {grouping}")


def _pair_payload(pair) -> dict[str, object]:
    return {
        "review_pair_id": pair.review_pair_id,
        "note_path": pair.note_path,
        "gate_path": pair.gate_path,
        "gate_id": pair.gate_id,
        "pair_ordinal": pair.pair_ordinal,
        "pair_status": pair.pair_status,
        "decision": pair.decision,
        "result_path": pair.result_path,
    }


def _job_payload(plan: ReviewJobPlan, *, include_timestamps: bool = False) -> dict[str, object]:
    payload: dict[str, object] = {
        "review_job_id": plan.review_job_id,
        "status": plan.status,
        "model_partition": plan.model_partition,
        "runner": plan.runner,
        "runner_model": plan.runner_model,
        "runner_effort": plan.runner_effort,
        "packing": plan.packing,
        "prompt_path": plan.prompt_path,
        "bundle_output_path": plan.bundle_output_path,
        "pair_count": len(plan.pairs),
        "pairs": [_pair_payload(pair) for pair in sorted(plan.pairs, key=lambda item: item.pair_ordinal)],
    }
    if include_timestamps:
        payload.update(
            {
                "created_at": plan.created_at,
                "started_at": plan.started_at,
                "completed_at": plan.completed_at,
                "failure_reason": plan.failure_reason,
            }
        )
        for item, pair in zip(payload["pairs"], sorted(plan.pairs, key=lambda p: p.pair_ordinal), strict=True):
            assert isinstance(item, dict)
            item["reviewed_at"] = pair.reviewed_at
    return payload


def _skipped_payload(skipped: list[SkippedRequestedPair]) -> list[dict[str, object]]:
    payload: list[dict[str, object]] = []
    for pair in skipped:
        item: dict[str, object] = {"reason": pair.reason}
        if pair.note_path is not None:
            item["note_path"] = pair.note_path
        if pair.gate_path is not None:
            item["gate_path"] = pair.gate_path
        if pair.gate_id is not None:
            item["gate_id"] = pair.gate_id
        payload.append(item)
    return payload


def _read_input(repo_root: Path, path: str | None) -> str:
    if path is None or path == "-":
        return sys.stdin.read()
    input_path = Path(path)
    if not input_path.is_absolute():
        input_path = repo_root / input_path
    return input_path.read_text(encoding="utf-8")


def _validate_mode(args: argparse.Namespace, parser: argparse.ArgumentParser) -> str:
    has_input = args.input is not None
    has_note = args.note is not None
    has_pair = bool(args.pairs)
    has_positional = bool(args.gate_or_bundle)

    if args.grouping == "note" and args.batch_size is not None:
        parser.error("--batch-size is only valid with --grouping gate")

    if has_input and (has_note or has_pair or has_positional):
        parser.error("--input cannot be combined with --note, --pair, or positional gate/bundle arguments")
    if has_note and has_pair:
        parser.error("--note and --pair are mutually exclusive")
    if has_pair and has_positional:
        parser.error("--pair cannot be combined with positional gate/bundle arguments")
    if has_note:
        if not has_positional:
            parser.error("direct note input requires one or more gate/bundle arguments")
        return "direct-note"
    if has_pair:
        return "direct-pair"
    if has_positional:
        parser.error("positional gate/bundle arguments require --note")
    return "selector"


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create queued review jobs from selector JSON or direct requested pairs.",
    )
    parser.add_argument("gate_or_bundle", nargs="*", help="Direct-note gate IDs, gate paths, or bundle names.")
    parser.add_argument("--input", help="Selector JSON path, or '-' for stdin.")
    parser.add_argument("--note", help="Direct-note repo-relative note path.")
    parser.add_argument("--pair", dest="pairs", action="append", help="Direct pair as NOTE::GATE. May be repeated.")
    parser.add_argument("--model", help="Review model partition. Required for direct input; validation-only for selector input.")
    parser.add_argument("--grouping", required=True, choices=["note", "gate"], help="Job grouping axis.")
    parser.add_argument("--batch-size", type=int, help="Note targets per gate-packed job. Defaults to 5.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    args = parser.parse_args(argv)

    if args.batch_size is not None and args.batch_size < 1:
        parser.error("--batch-size must be a positive integer")
    batch_size = args.batch_size or 5
    repo_root = cwd if cwd is not None else Path.cwd()
    input_mode = _validate_mode(args, parser)

    try:
        if input_mode == "selector":
            model_partition, requested_pairs = _selector_pairs(
                repo_root=repo_root,
                raw_json=_read_input(repo_root, args.input),
            )
            if args.model is not None:
                requested_model = args.model.strip()
                if not requested_model:
                    parser.error("--model must not be empty")
                requested_model = normalize_model_partition(requested_model)
                if requested_model != model_partition:
                    parser.error(
                        f"--model {requested_model!r} does not match selector model_partition {model_partition!r}"
                    )
        else:
            if args.model is None or not args.model.strip():
                parser.error("--model is required for direct input")
            model_partition = normalize_model_partition(args.model)
            if input_mode == "direct-note":
                assert args.note is not None
                note_path = _normalize_note_path(repo_root, args.note)
                requested_pairs = [
                    RequestedPair(note_path=note_path, gate_path=gate_path, gate_id=gate_id, reason="requested")
                    for gate_path, gate_id in _resolve_gate_or_bundle_inputs(repo_root, args.gate_or_bundle)
                ]
            else:
                requested_pairs = [_parse_pair_arg(repo_root, raw_pair) for raw_pair in args.pairs or []]

        unique_pairs, skipped_duplicates = _drop_duplicate_pairs(requested_pairs)
        applicable_pairs, skipped_inapplicable = _filter_applicable_pairs(repo_root, unique_pairs)
        skipped_pairs = skipped_duplicates + skipped_inapplicable
        groups = _group_pairs(applicable_pairs, grouping=args.grouping, batch_size=batch_size)
        db_path = prepare_review_db(repo_root, args.db)

        created_job_ids: list[int] = []
        for group in groups:
            prepared = prepare_grouped_review_job(
                repo_root=repo_root,
                db_path=db_path,
                pairs=[(pair.note_path, pair.gate_path) for pair in group],
                skipped=[],
                packing=args.grouping,
                runner=None,
                model_partition=model_partition,
            )
            created_job_ids.append(prepared.review_job_id)

        with connect(db_path) as conn:
            plans_by_id = {
                plan.review_job_id: plan
                for plan in list_review_job_plans(conn)
                if plan.review_job_id in set(created_job_ids)
            }
        plans = [plans_by_id[review_job_id] for review_job_id in sorted(created_job_ids)]
    except (FileNotFoundError, ValueError, OSError) as exc:
        parser.error(str(exc))

    payload = {
        "input_mode": input_mode,
        "model_partition": model_partition,
        "grouping": args.grouping,
        "created_count": len(plans),
        "skipped_count": len(skipped_pairs),
        "jobs": [_job_payload(plan) for plan in plans],
        "skipped_pairs": _skipped_payload(skipped_pairs),
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
