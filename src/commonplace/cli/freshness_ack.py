#!/usr/bin/env python3
"""Acknowledge changed inputs for a registered freshness target."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.cli.freshness_io import read_input_payload
from commonplace.freshness.transitions import ack_target_inputs, parse_input_observation, parse_target_key
from commonplace.review.review_db import connect, ensure_db, prune_superseded_freshness_baselines, resolve_db_path


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Acknowledge changed inputs for a registered freshness target.",
        allow_abbrev=False,
    )
    parser.add_argument("--input", required=True, help="Ack manifest JSON path, or '-' for stdin.")
    parser.add_argument("--db", help="Override operational store path.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = resolve_db_path(repo_root, args.db)
    try:
        payload = read_input_payload(args.input)
        schema = payload.get("schema")
        if schema != "commonplace-freshness-ack/1":
            raise ValueError("schema must be commonplace-freshness-ack/1")
        target_kind = payload.get("target_kind")
        if not isinstance(target_kind, str) or not target_kind.strip():
            raise ValueError("target_kind is required")
        target_key = parse_target_key(payload.get("target_key"))
        raw_revision = payload.get("expected_baseline_revision")
        if not isinstance(raw_revision, int) or raw_revision < 1:
            raise ValueError("expected_baseline_revision must be >= 1")

        selected_inputs = None
        raw_selected = payload.get("selected_inputs")
        if raw_selected is not None:
            if not isinstance(raw_selected, list):
                raise ValueError("selected_inputs must be an array")
            selected_inputs = tuple(parse_input_observation(item) for item in raw_selected)

        ensure_db(db_path)
        with connect(db_path) as conn:
            superseded = ack_target_inputs(
                conn,
                repo_root=repo_root,
                target_kind=target_kind.strip(),
                target_key=target_key,
                expected_baseline_revision=raw_revision,
                selected_inputs=selected_inputs,
            )
            prune_superseded_freshness_baselines(conn, [superseded])
            conn.commit()
    except (OSError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))

    print("acked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())