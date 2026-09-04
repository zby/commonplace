"""Render a checked operator handoff for one agentic-system analysis run."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib import validation
from commonplace.lib.agentic_analysis import (
    parse_agentic_analysis_run_state,
    render_agentic_analysis_handoff,
)
from commonplace.lib.note_parser import parse_document


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_state", help="Path to a handoff-ready run-state.md")
    args = parser.parse_args(argv)

    repo_root = Path.cwd().resolve()
    run_state_path = Path(args.run_state)
    if not run_state_path.is_absolute():
        run_state_path = repo_root / run_state_path
    run_state_path = run_state_path.resolve()
    if not run_state_path.is_file():
        print(f"run state does not exist: {run_state_path}", file=sys.stderr)
        return 1

    results = validation.validate_note(run_state_path, repo_root=repo_root)
    if results.fails:
        for failure in results.fails:
            print(failure, file=sys.stderr)
        return 1

    content = run_state_path.read_text(encoding="utf-8")
    document, error = parse_document(content)
    if error is not None or document is None:
        print("run state is not parseable", file=sys.stderr)
        return 1
    try:
        state = parse_agentic_analysis_run_state(
            run_state_path,
            document,
            repo_root=repo_root,
        )
        rendered = render_agentic_analysis_handoff(state)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
