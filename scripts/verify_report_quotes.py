"""Resolve the quote-anchored citations of Markdown files against a run's frozen source.

Complete-run verification already resolves every citation in the exact result
and the memory report. This script gives the same check to a file inside a run
that has not completed, such as a specialist report produced in a
specialist-only trial. It prints one line per citation and exits 1 on any
failure. It changes nothing.

Run: uv run python scripts/verify_report_quotes.py <run-state.md> <file.md> [<file.md> ...]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.agentic_analysis import (
    _verify_quote_anchors,
    parse_agentic_analysis_run_state,
)
from commonplace.lib.note_parser import parse_document


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_state", type=Path)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    repo_root = Path.cwd().resolve()
    state_path = (repo_root / args.run_state).resolve()
    document, error = parse_document(state_path.read_text(encoding="utf-8"))
    if error or document is None:
        print(f"cannot parse run state: {error}", file=sys.stderr)
        return 1
    state = parse_agentic_analysis_run_state(state_path, document, repo_root=repo_root)
    if state.source is None:
        print("run state has no frozen source", file=sys.stderr)
        return 1
    failed = False
    for file in args.files:
        content = (repo_root / file).read_text(encoding="utf-8")
        passes, failures = _verify_quote_anchors(content, source=state.source)
        print(f"== {file}: {len(passes)} resolved, {len(failures)} failed")
        for line in passes:
            print(f"  ok   {line}")
        for line in failures:
            print(f"  FAIL {line}")
        failed = failed or bool(failures)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
