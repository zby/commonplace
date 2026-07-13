#!/usr/bin/env python3
"""Accept a non-review freshness target from live file observations."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.cli.freshness_io import read_input_payload
from commonplace.freshness.transitions import InputObservation, accept_target_observations, parse_input_observation, parse_target_key
from commonplace.review.review_db import connect, ensure_db, resolve_db_path


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Accept or refresh a non-review freshness target from live observations.",
        allow_abbrev=False,
    )
    parser.add_argument("--input", required=True, help="Accept manifest JSON path, or '-' for stdin.")
    parser.add_argument("--db", help="Override operational store path.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = resolve_db_path(repo_root, args.db)
    try:
        payload = read_input_payload(args.input)
        target_kind = payload.get("target_kind")
        if not isinstance(target_kind, str) or not target_kind.strip():
            raise ValueError("target_kind is required")
        target_key = parse_target_key(payload.get("target_key"))
        transition = payload.get("transition")
        if transition == "initial":
            expected_revision = None
        elif transition == "refresh":
            raw_revision = payload.get("expected_baseline_revision")
            if not isinstance(raw_revision, int) or raw_revision < 1:
                raise ValueError("refresh transition requires expected_baseline_revision >= 1")
            expected_revision = raw_revision
        else:
            raise ValueError("transition must be 'initial' or 'refresh'")

        raw_inputs = payload.get("inputs")
        if not isinstance(raw_inputs, dict):
            raise ValueError("inputs must be an object keyed by input role")
        observations: dict[str, InputObservation] = {}
        for role, raw_observation in raw_inputs.items():
            if not isinstance(role, str) or not role.strip():
                raise ValueError("input role keys must be non-empty strings")
            observations[role.strip()] = parse_input_observation(raw_observation)

        ensure_db(db_path)
        with connect(db_path) as conn:
            accept_target_observations(
                conn,
                repo_root=repo_root,
                target_kind=target_kind.strip(),
                target_key=target_key,
                inputs=observations,
                expected_baseline_revision=expected_revision,
            )
            conn.commit()
    except (OSError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))

    print("accepted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())