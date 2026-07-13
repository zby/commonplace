#!/usr/bin/env python3
"""Run full integrity checks on the commonplace operational store."""

from __future__ import annotations

import argparse
from pathlib import Path

from commonplace.store import check_store_health, resolve_db_path


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Verify snapshot hashes and freshness baseline invariants in the operational store.",
        allow_abbrev=False,
    )
    parser.add_argument("--db", help="Override operational store path.")
    args = parser.parse_args(argv)

    repo_root = cwd if cwd is not None else Path.cwd()
    db_path = resolve_db_path(repo_root, args.db)
    try:
        check_store_health(db_path)
    except (OSError, RuntimeError) as exc:
        parser.error(str(exc))

    print("healthy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())