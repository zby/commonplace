"""Render a checked operator handoff for one agentic-system analysis run."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.agentic_analysis import (
    load_run_state,
    render_agentic_analysis_handoff,
)
from commonplace.lib.analysis_worktree import require_run_code
from commonplace.lib.library import checks_library


@checks_library
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_state", help="Path to a complete run-state.md")
    args = parser.parse_args(argv)

    repo_root = Path.cwd().resolve()
    run_state_path = (repo_root / args.run_state).resolve()
    try:
        require_run_code(run_state_path, cwd=repo_root)
        state = load_run_state(run_state_path, repo_root=repo_root)
        rendered = render_agentic_analysis_handoff(state)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
