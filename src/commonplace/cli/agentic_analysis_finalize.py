"""Finalize the memory member and build the manifest of one running analysis."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from commonplace.lib.agentic_analysis import load_run_state
from commonplace.lib.agentic_finalize import (
    build_manifest,
    finalize_memory,
    render_finalization_summary,
)
from commonplace.lib.library import checks_library


@checks_library
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
        ("memory", "Write output/memory.md from memory-report.md and the Reconciliation table"),
        ("manifest", "Write output/ARTIFACT.yaml pinning the members present in output/"),
    ):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("run_state", help="Path to a running run-state.md")
    args = parser.parse_args(argv)

    repo_root = Path.cwd().resolve()
    try:
        state = load_run_state(
            (repo_root / args.run_state).resolve(), repo_root=repo_root
        )
        if state.status != "running":
            raise ValueError(f"run is {state.status}, not running")
        if args.command == "memory":
            print(render_finalization_summary(finalize_memory(state.run_dir)))
        else:
            print(build_manifest(state.run_dir), end="")
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
