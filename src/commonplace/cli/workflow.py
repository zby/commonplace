"""Commonplace setup around the independent code-scheduled workflow shell."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from commonplace.lib.analysis_worktree import (
    command_environment,
    prepare_analysis,
    require_run_code,
)
from commonplace.workflow.shell import main as workflow_main


def _require_bound_code(args: list[str]) -> None:
    """A run in a source checkout is advanced only by that checkout's code."""
    cwd = Path.cwd()
    if args[:1] == ["start"]:
        run = Path(args[args.index("--run") + 1]) if "--run" in args[:-1] else cwd
    elif len(args) > 1 and args[0] in ("step", "report", "resolve", "release"):
        run = Path(args[1])
    else:
        return
    require_run_code(run, cwd=cwd)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] != "prepare-analysis":
        if args in (["--help"], ["-h"]):
            print("Additional Commonplace setup command: prepare-analysis --help\n")
        try:
            _require_bound_code(args)
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 1
        return workflow_main(args)
    parser = argparse.ArgumentParser(
        prog="commonplace-workflow prepare-analysis",
        description="Prepare a commit-bound Commonplace worktree and local commands, optionally launching a fresh harness.",
    )
    parser.add_argument("--name", required=True, help="lowercase system label")
    parser.add_argument("--revision", help="committed method revision (default: HEAD, refused when behind the default branch)")
    parser.add_argument("--worktree", type=Path, help="new destination (default: ignored .commonplace/worktrees/)")
    parser.add_argument("--allow-dirty-origin", action="store_true", help="exclude unrelated uncommitted changes; startup changes still stop preparation")
    parser.add_argument("launch", nargs=argparse.REMAINDER, help="optional harness command after --")
    arguments = parser.parse_args(args[1:])
    try:
        launch = arguments.launch
        if launch[:1] == ["--"]:
            launch = launch[1:]
        preparation = prepare_analysis(
            Path.cwd(), name=arguments.name,
            allow_dirty_origin=arguments.allow_dirty_origin,
            revision=arguments.revision, worktree=arguments.worktree,
        )
        print(json.dumps(preparation, indent=2), flush=True)
        if launch:
            worktree = Path(str(preparation["worktree"]))
            try:
                return subprocess.run(
                    launch, cwd=worktree, env=command_environment(worktree), check=False
                ).returncode
            except OSError as error:
                raise ValueError(f"could not launch {launch[0]}: {error}; prepared worktree retained") from error
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
