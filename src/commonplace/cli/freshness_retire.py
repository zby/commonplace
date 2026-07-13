#!/usr/bin/env python3
"""Retire a registered freshness target."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.cli.freshness_io import read_input_payload
from commonplace.freshness.transitions import parse_target_key, retire_target
from commonplace.review.review_db import connect, ensure_db, resolve_db_path


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Retire a registered freshness target.",
        allow_abbrev=False,
    )
    parser.add_argument("--input", required=True, help="Retire manifest JSON path, or '-' for stdin.")
    parser.add_argument("--db", help="Override operational store path.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = resolve_db_path(repo_root, args.db)
    try:
        payload = read_input_payload(args.input)
        schema = payload.get("schema")
        if schema != "commonplace-freshness-retire/1":
            raise ValueError("schema must be commonplace-freshness-retire/1")
        target_kind = payload.get("target_kind")
        if not isinstance(target_kind, str) or not target_kind.strip():
            raise ValueError("target_kind is required")
        target_key = parse_target_key(payload.get("target_key"))

        ensure_db(db_path)
        with connect(db_path) as conn:
            retired = retire_target(
                conn,
                target_kind=target_kind.strip(),
                target_key=target_key,
            )
            conn.commit()
    except (OSError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))

    print("retired" if retired else "already-absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())