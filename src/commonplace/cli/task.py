"""Run one task from `kb/tasks/` unattended and check its commit.

    commonplace-task run NAME [--profile NAME] [--timeout SECONDS]

Runs in the current checkout, on the current branch, as the task's runbook
says; prints a JSON report and checks git commit count, subject, write scope,
and uncommitted leftovers. Records live under kb/reports/state/tasks/.
Exits 0 when all checks pass, 1 when any check fails, and 2 when the runbook
or profile cannot be loaded. The worker's own report is shown but decides
nothing.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from commonplace.lib.tasks import launch, load_profile, load_runbook, report_dict


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="commonplace-task",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run", help="run one task unattended in this checkout and check its commit")
    run.add_argument("name", help="the runbook kb/tasks/<name>.md")
    run.add_argument("--profile", help="worker profile from kb/tasks/profiles.yaml (default: its `default`)")
    run.add_argument("--timeout", type=float, help="seconds a launch may take")
    arguments = parser.parse_args(argv)
    try:
        root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True,
                                   text=True).stdout.strip())
        report = launch(root, load_runbook(root, arguments.name), load_profile(root, arguments.profile),
                        timeout=arguments.timeout)
    except (ValueError, subprocess.CalledProcessError) as error:
        print(f"commonplace-task: {error}", file=sys.stderr)
        return 2
    print(json.dumps(report_dict(report), indent=2))
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
