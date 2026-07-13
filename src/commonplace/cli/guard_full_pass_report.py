#!/usr/bin/env python3
"""Refuse full-pass transitions whose guarded artifacts no longer match."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from commonplace.lib.full_pass import guard_full_pass_report, load_full_pass_report


class _InvocationError(ValueError):
    pass


class _ArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        raise _InvocationError(message)


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = _ArgumentParser(
        description="Compare every packet capture in one full-pass report with its live artifact.",
        allow_abbrev=False,
    )
    parser.add_argument(
        "report", help="Path to kb/reports/full-pass/.../full-pass-report.md"
    )
    try:
        args = parser.parse_args(argv)
    except _InvocationError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True, sort_keys=True))
        return 2
    repo_root = (cwd if cwd is not None else Path.cwd()).resolve()

    try:
        report = load_full_pass_report(Path(args.report), repo_root=repo_root)
    except (FileNotFoundError, OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True, sort_keys=True))
        return 2

    results = guard_full_pass_report(report)
    all_matching = all(result.status == "matching" for result in results)
    payload = {
        "report": report.path.relative_to(repo_root).as_posix(),
        "all_matching": all_matching,
        "inputs": [result.to_dict() for result in results],
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    if not all_matching:
        print(
            "Full-pass transition refused: every guarded input must be matching.",
            file=sys.stderr,
        )
    return 0 if all_matching else 1


if __name__ == "__main__":
    raise SystemExit(main())
