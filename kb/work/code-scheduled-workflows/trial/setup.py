"""Create a trial run of the loop text.

From the repository root:

    uv run python kb/work/code-scheduled-workflows/trial/setup.py <scenario> [name]
        [--launch KEY=VALUE ...] [--hold SECONDS]

Scenarios are described in trial_workflow.py. The run goes under `runs/`,
which git ignores. The agent orchestrator sees the run's path, so the name
must not tell it the scenario: without a name the run gets a random one. The
script prints the run directory and the `<shell>` value for the loop text,
with absolute paths and the interpreter's own path, so the value works from any
directory and without `uv`.

`--launch` gives the launch parameters of the `parameters` scenario. `--hold`
gives the seconds the `busy` scenario holds the run. For `busy`, setup starts
the holding `step` itself and returns only once that step holds the run, so a
session started after setup always meets a busy run.
"""

from __future__ import annotations

import argparse
import json
import os
import secrets
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from trial_workflow import beside

from commonplace.workflow import Orchestrator

SCENARIOS = (
    "clean",
    "retry",
    "problem",
    "stop",
    "stop-only",
    "parameters",
    "uncertain",
    "busy",
)

SOURCE = """\
Teams that write their decisions down make fewer repeated mistakes. A decision
record lets a newcomer see why a choice was made, so the choice is not
reopened every few months. Records only help if they are kept next to the code
they govern, and if someone reviews them when the code changes.
"""

NOTES = """\
- The decision log was started in March.
- Two decisions were reversed after review.
- Nobody owns the log since the reorganisation.
"""


def start_holding_step(run_dir: Path) -> subprocess.Popen:
    """Start a `step` in the background and wait until it holds the run.

    The holding step removes the hold file once it is inside the definition,
    which runs under the run's lock.
    """
    log = beside(run_dir, "hold.log").open("w", encoding="utf-8")
    env = dict(
        os.environ,
        PYTHONPATH=os.pathsep.join(
            filter(None, [str(HERE), os.environ.get("PYTHONPATH")])
        ),
    )
    process = subprocess.Popen(
        [sys.executable, "-m", "commonplace.workflow.shell", "step", str(run_dir)],
        stdout=log,
        stderr=subprocess.STDOUT,
        env=env,
        start_new_session=True,
    )
    marker = beside(run_dir, "hold")
    deadline = time.monotonic() + 30
    while marker.exists():
        if process.poll() is not None or time.monotonic() > deadline:
            process.kill()
            raise RuntimeError(f"the holding step did not take the run; see {log.name}")
        time.sleep(0.1)
    return process


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("scenario", choices=SCENARIOS)
    parser.add_argument("name", nargs="?", help="the run's name; random when left out")
    parser.add_argument("--launch", action="append", default=[], metavar="KEY=VALUE")
    parser.add_argument("--hold", type=float, default=90.0, metavar="SECONDS")
    args = parser.parse_args(argv)

    name = args.name or f"run-{secrets.token_hex(3)}"
    if any(scenario in name for scenario in SCENARIOS):
        print(f"the name {name!r} contains a scenario's name", file=sys.stderr)
        return 1
    launch = {}
    for item in args.launch:
        key, separator, value = item.partition("=")
        if not key or not separator:
            print(f"--launch {item!r} is not of the form KEY=VALUE", file=sys.stderr)
            return 1
        launch[key] = value

    run_dir = HERE / "runs" / name
    if run_dir.exists():
        print(f"{run_dir} exists; remove it or choose another name", file=sys.stderr)
        return 1
    run_dir.mkdir(parents=True)
    (run_dir / "source.md").write_text(SOURCE, encoding="utf-8")
    params = {"scenario": args.scenario}
    if args.scenario == "problem":
        (run_dir / "incoming").mkdir()
        (run_dir / "incoming" / "notes.md").write_text(NOTES, encoding="utf-8")
    if args.scenario == "parameters":
        params["launch"] = json.dumps(launch, sort_keys=True)
    if args.scenario == "uncertain":
        beside(run_dir, "interrupt").write_text("", encoding="utf-8")
    if args.scenario == "busy":
        beside(run_dir, "hold").write_text("", encoding="utf-8")
        params["hold"] = str(args.hold)
    Orchestrator.create(run_dir, "trial_workflow:Trial", params)
    print(f"run: {run_dir}")
    print(f"shell: PYTHONPATH={HERE} {sys.executable} -m commonplace.workflow.shell")
    if args.scenario == "busy":
        start_holding_step(run_dir)
        until = time.strftime("%H:%M:%S", time.localtime(time.time() + args.hold))
        print(f"held: until about {until}; start the session now")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
