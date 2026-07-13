#!/usr/bin/env python3
"""Create queued review jobs from selector output."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.batch import prepare_grouped_review_job
from commonplace.review.paths import criterion_id_for_path, normalize_criterion_path, review_gates_dir
from commonplace.review.resolve_criteria import applicable_criterion_ids_for_note
from commonplace.review.review_db import (
    connect,
    load_review_job_plan,
    prepare_review_db,
)
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.collection_conformance import is_collection_md_criterion_path, note_collection_md_path
from commonplace.review.critique import is_critique_criterion_path, result_kind_for_criterion_path
from commonplace.review.type_conformance import is_type_spec_criterion_path, note_type_spec_path


@dataclass(frozen=True)
class RequestedPair:
    note_path: str
    criterion_path: str
    criterion_id: str
    reason: str
    result_kind: str


@dataclass(frozen=True)
class SkippedRequestedPair:
    note_path: str | None
    criterion_path: str | None
    criterion_id: str | None
    reason: str


def _normalize_note_path(repo_root: Path, raw: str) -> str:
    raw_path = Path(raw)
    if raw_path.is_absolute():
        raise ValueError(f"note path must be repo-relative: {raw}")
    normalized = raw_path.as_posix()
    if not (repo_root / normalized).is_file():
        raise ValueError(f"note not found: {raw}")
    return normalized


def _normalize_criterion(repo_root: Path, raw: str) -> tuple[str, str]:
    criterion_path = normalize_criterion_path(repo_root, raw)
    criterion_id = criterion_id_for_path(repo_root, criterion_path)
    return criterion_path, criterion_id


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
    fallback_model: str | None = None,
) -> tuple[str, list[RequestedPair]]:
    payload = _load_selector_json(raw_json)
    raw_model = payload.get("model_partition")
    if raw_model is None:
        raw_model = fallback_model
    if not isinstance(raw_model, str) or not raw_model.strip():
        raise ValueError("selector JSON model_partition is required unless --model-partition is provided")
    model_partition = normalize_model_partition(raw_model)
    raw_targets = payload.get("targets")
    if not isinstance(raw_targets, list):
        raise ValueError("selector JSON targets must be a list")

    pairs: list[RequestedPair] = []
    for index, target in enumerate(raw_targets, start=1):
        if not isinstance(target, dict):
            raise ValueError(f"selector target {index} must be an object")
        note_raw = target.get("note_path")
        criterion_raw = target.get("criterion_path")
        criterion_id_raw = target.get("criterion_id")
        reason_raw = target.get("reason", "stale")
        result_kind_raw = target.get("result_kind", "verdict")
        if not isinstance(note_raw, str) or not note_raw.strip():
            raise ValueError(f"selector target {index} missing note_path")
        if not isinstance(criterion_raw, str) or not criterion_raw.strip():
            raise ValueError(f"selector target {index} missing criterion_path")
        if not isinstance(criterion_id_raw, str) or not criterion_id_raw.strip():
            raise ValueError(f"selector target {index} missing criterion_id")
        if not isinstance(reason_raw, str) or not reason_raw.strip():
            reason_raw = "stale"
        if result_kind_raw not in {"verdict", "report"}:
            raise ValueError(f"selector target {index} has invalid result_kind: {result_kind_raw!r}")
        note_path = _normalize_note_path(repo_root, note_raw)
        criterion_path, criterion_id = _normalize_criterion(repo_root, criterion_raw)
        if criterion_id != criterion_id_raw.strip():
            raise ValueError(
                f"selector target {index} criterion_id {criterion_id_raw!r} does not match criterion_path {criterion_path!r}"
            )
        expected_result_kind = result_kind_for_criterion_path(criterion_path)
        if result_kind_raw != expected_result_kind:
            raise ValueError(
                f"selector target {index} result_kind {result_kind_raw!r} does not match "
                f"criterion contract {expected_result_kind!r}"
            )
        pairs.append(
            RequestedPair(
                note_path=note_path,
                criterion_path=criterion_path,
                criterion_id=criterion_id,
                reason=reason_raw.strip(),
                result_kind=result_kind_raw,
            )
        )
    return model_partition, pairs


def _drop_duplicate_pairs(pairs: list[RequestedPair]) -> tuple[list[RequestedPair], list[SkippedRequestedPair]]:
    seen: set[tuple[str, str]] = set()
    unique: list[RequestedPair] = []
    skipped: list[SkippedRequestedPair] = []
    for pair in pairs:
        key = (pair.note_path, pair.criterion_path)
        if key in seen:
            skipped.append(
                SkippedRequestedPair(
                    note_path=pair.note_path,
                    criterion_path=pair.criterion_path,
                    criterion_id=pair.criterion_id,
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
        catalog_pairs = [
            pair
            for pair in note_pairs
            if not is_type_spec_criterion_path(pair.criterion_path)
            and not is_collection_md_criterion_path(pair.criterion_path)
            and not is_critique_criterion_path(pair.criterion_path)
        ]
        has_type_pairs = any(is_type_spec_criterion_path(pair.criterion_path) for pair in note_pairs)
        has_collection_pairs = any(is_collection_md_criterion_path(pair.criterion_path) for pair in note_pairs)
        applicable_criterion_ids = set(
            applicable_criterion_ids_for_note(
                note_abs,
                [pair.criterion_id for pair in catalog_pairs],
                gates_dir,
            )
        )
        note_type_path = note_type_spec_path(repo_root, note_abs) if has_type_pairs else None
        note_collection_path = note_collection_md_path(repo_root, note_abs) if has_collection_pairs else None
        for pair in note_pairs:
            if is_type_spec_criterion_path(pair.criterion_path):
                pair_applies = pair.criterion_path == note_type_path
            elif is_collection_md_criterion_path(pair.criterion_path):
                pair_applies = pair.criterion_path == note_collection_path
            elif is_critique_criterion_path(pair.criterion_path):
                pair_applies = True
            else:
                pair_applies = pair.criterion_id in applicable_criterion_ids
            if pair_applies:
                applicable.append(pair)
            else:
                skipped.append(
                    SkippedRequestedPair(
                        note_path=pair.note_path,
                        criterion_path=pair.criterion_path,
                        criterion_id=pair.criterion_id,
                        reason="not applicable",
                    )
                )
    return applicable, skipped


def _bundle_for_criterion_id(criterion_id: str) -> str:
    bundle, separator, _ = criterion_id.partition("/")
    if not separator:
        return ""
    return bundle


def _note_groups(pairs: list[RequestedPair]) -> list[list[RequestedPair]]:
    grouped: dict[tuple[str, str], list[RequestedPair]] = {}
    for pair in pairs:
        grouped.setdefault((pair.note_path, _bundle_for_criterion_id(pair.criterion_id)), []).append(pair)
    return list(grouped.values())


def _chunks(items: list[RequestedPair], size: int) -> list[list[RequestedPair]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def _criterion_groups(pairs: list[RequestedPair], batch_size: int) -> list[list[RequestedPair]]:
    grouped: dict[str, list[RequestedPair]] = {}
    for pair in pairs:
        grouped.setdefault(pair.criterion_path, []).append(pair)
    result: list[list[RequestedPair]] = []
    for criterion_pairs in grouped.values():
        result.extend(_chunks(criterion_pairs, batch_size))
    return result


def _group_pairs(pairs: list[RequestedPair], *, grouping: str, batch_size: int) -> list[list[RequestedPair]]:
    if grouping == "note":
        return _note_groups(pairs)
    if grouping == "criterion":
        return _criterion_groups(pairs, batch_size)
    raise ValueError(f"invalid grouping: {grouping}")


def _skipped_payload(skipped: list[SkippedRequestedPair]) -> list[dict[str, object]]:
    payload: list[dict[str, object]] = []
    for pair in skipped:
        item: dict[str, object] = {"reason": pair.reason}
        if pair.note_path is not None:
            item["note_path"] = pair.note_path
        if pair.criterion_path is not None:
            item["criterion_path"] = pair.criterion_path
        if pair.criterion_id is not None:
            item["criterion_id"] = pair.criterion_id
        payload.append(item)
    return payload


def _read_input(repo_root: Path, path: str | None) -> str:
    if path is None or path == "-":
        return sys.stdin.read()
    input_path = Path(path)
    if not input_path.is_absolute():
        input_path = repo_root / input_path
    return input_path.read_text(encoding="utf-8")


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create queued review jobs from selector JSON.",
        allow_abbrev=False,
    )
    parser.add_argument("--input", required=True, help="Selector JSON path, or '-' for stdin.")
    parser.add_argument(
        "--model-partition",
        help="Review model partition (a partition name, not a concrete model). Required for direct input; validation-only for selector input.",
    )
    parser.add_argument("--grouping", required=True, choices=["note", "criterion"], help="Job grouping axis.")
    parser.add_argument("--batch-size", type=int, help="Note targets per criterion-packed job. Defaults to 5.")
    parser.add_argument("--db", help="Override COMMONPLACE_STORE.")
    args = parser.parse_args(argv)

    if args.grouping == "note" and args.batch_size is not None:
        parser.error("--batch-size is only valid with --grouping criterion")
    if args.batch_size is not None and args.batch_size < 1:
        parser.error("--batch-size must be a positive integer")
    batch_size = args.batch_size or 5
    repo_root = cwd if cwd is not None else Path.cwd()

    try:
        model_partition, requested_pairs = _selector_pairs(
            repo_root=repo_root,
            raw_json=_read_input(repo_root, args.input),
            fallback_model=args.model_partition,
        )
        if args.model_partition is not None:
            requested_model = args.model_partition.strip()
            if not requested_model:
                parser.error("--model-partition must not be empty")
            requested_model = normalize_model_partition(requested_model)
            if requested_model != model_partition:
                parser.error(
                    f"--model-partition {requested_model!r} does not match selector model_partition {model_partition!r}"
                )

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
                pairs=[(pair.note_path, pair.criterion_path, pair.result_kind) for pair in group],
                grouping=args.grouping,
                runner=None,
                model_partition=model_partition,
            )
            created_job_ids.append(prepared.review_job_id)

        with connect(db_path) as conn:
            plans = []
            for review_job_id in sorted(created_job_ids):
                plan = load_review_job_plan(conn, review_job_id=review_job_id)
                if plan is None:
                    raise ValueError(f"created review job not found: {review_job_id}")
                plans.append(plan)
    except (FileNotFoundError, ValueError, OSError) as exc:
        parser.error(str(exc))

    payload = {
        "input_mode": "selector",
        "model_partition": model_partition,
        "grouping": args.grouping,
        "created_count": len(plans),
        "skipped_count": len(skipped_pairs),
        "jobs": [plan.to_payload() for plan in plans],
        "skipped_pairs": _skipped_payload(skipped_pairs),
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
