"""Prepared analysis lifecycle; generic engine operations live in commonplace-run."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from commonplace.lib.agentic_analysis.worktree import (
    command_environment,
    integrate_analysis,
    prepare_analysis,
    start_analysis,
)
from commonplace.workflow import UncertainEffectError


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="commonplace-workflow", description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare-analysis", help="prepare a commit-bound worktree and local commands")
    prepare.add_argument("--name", required=True)
    prepare.add_argument("--revision")
    prepare.add_argument("--worktree", type=Path)
    prepare.add_argument("--allow-dirty-origin", action="store_true")
    prepare.add_argument("launch", nargs=argparse.REMAINDER, help="optional fresh harness command after --")
    start = commands.add_parser("start-analysis", help="allocate a run without advancing or acquiring sources")
    start.add_argument("--system", required=True)
    start.add_argument("--source-identity", required=True)
    start.add_argument("--source", required=True)
    start.add_argument("--source-revision")
    integrate = commands.add_parser("integrate-analysis", help="commit exact published bytes and merge into main")
    integrate.add_argument("run", type=Path)
    integrate.add_argument("--model")
    report = commands.add_parser("report-analysis", help="print engine evidence as JSON, not a publication audit")
    report.add_argument("run", type=Path)
    arguments = parser.parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if arguments.command == "start-analysis":
            print(start_analysis(Path.cwd(), system=arguments.system, source_identity=arguments.source_identity,
                                 source=arguments.source, source_revision=arguments.source_revision))
        elif arguments.command == "integrate-analysis":
            print(integrate_analysis(arguments.run, model=arguments.model))
        elif arguments.command == "report-analysis":
            from commonplace.lib.agentic_analysis.report import render_engine_run_report

            rendered = json.loads(render_engine_run_report(arguments.run))
            if rendered["state"] == "completed":
                from hashlib import sha256

                from commonplace.lib.note_parser import parse_document

                version = rendered["members"].get("boundary")
                if version is None:
                    raise ValueError("completed analysis has no boundary member")
                # The set directory holds the members materialized; content identity ties it to the report.
                data = (Path(rendered["set"]) / "boundary.md").read_bytes()
                if sha256(data).hexdigest() != version:
                    raise ValueError("the materialized boundary differs from the reported member")
                document, error = parse_document(data.decode("utf-8"))
                if error or document is None or not document.frontmatter:
                    raise ValueError("completed analysis has an unreadable boundary member")
                disposition = document.frontmatter.get("result-disposition")
                if disposition not in ("complete", "blocked", "out-of-scope"):
                    raise ValueError("completed analysis has no classified disposition")
                rendered["result-disposition"] = disposition
                rendered["completion"] = "local" if disposition != "complete" else "publication-job-completed"
            print(json.dumps(rendered, indent=2, sort_keys=True))
        else:
            preparation = prepare_analysis(
                Path.cwd(), name=arguments.name, allow_dirty_origin=arguments.allow_dirty_origin,
                revision=arguments.revision, worktree=arguments.worktree,
            )
            print(json.dumps(preparation, indent=2), flush=True)
            launch = arguments.launch
            if launch[:1] == ["--"]:
                launch = launch[1:]
            if launch:
                worktree = Path(str(preparation["worktree"]))
                try:
                    return subprocess.run(launch, cwd=worktree, env=command_environment(worktree), check=False).returncode
                except OSError as error:
                    raise ValueError(f"could not launch {launch[0]}: {error}; prepared worktree retained") from error
    except (ValueError, OSError, KeyError, TypeError, UncertainEffectError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
