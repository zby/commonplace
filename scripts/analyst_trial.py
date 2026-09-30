#!/usr/bin/env python3
"""Prepare one analyst of a recorded analysis run to run again in isolation.

    uv run python scripts/analyst_trial.py prepare <recorded-run-dir> <analyst> [--label L]

<analyst> is runtime, memory or epistemic. The command creates a trial
directory beside the run directories, named like a run
(AAS-<today>-trial-<analyst>[-<label>]-<system>-<nn>) because the run-state
schema requires one, copies the recorded run's frozen
inputs into it (boundary.md, opening.json, run-state.md set back to running,
and output/runtime.md for the memory and epistemic analysts), and writes
prompt.md: the analyst's prompt as the current workflow code builds it, with
every path pointing into the trial directory. It prints the prompt path.

Launch the analyst with the loop's instruction, "Read `<prompt.md>` and follow
it.", in whatever harness and model the trial is for. The instruction files
the prompt lists are read from the working tree, so an edited instruction
takes effect in the next trial without a commit. trial.json records the
recorded run, the analyst, and the SHA-256 of every input the prompt lists.

The command only prepares. It launches nothing and judges nothing.
"""

import argparse
import datetime
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

from commonplace.lib.agentic_workflow import (
    BOUNDARY,
    JOBS,
    OPENING,
    RUN_STATE,
    RUNTIME,
    STATE_ROOT,
    AnalyseAgenticSystem,
)
from commonplace.workflow.engine import render_prompt

ANALYSTS = ("runtime", "memory", "epistemic")
RESET = {
    "run-status": "running",
    "result-disposition": "null",
    "artifact": "null",
    "generated-review": "null",
    "failure": "null",
}


def running_state(text: str, run_id: str) -> str:
    """The recorded run state as the trial's own running run, keeping its
    frozen source. `run-id` must name the directory the state sits in."""
    reset = {**RESET, "run-id": run_id, "description": f"Trial state for {run_id}"}
    head, body = text.split("\n---\n", 1)
    lines, skipping = [], False
    for line in head.splitlines():
        key = line.split(":", 1)[0]
        if skipping and line.startswith((" ", "\t")):
            continue
        skipping = False
        if key in reset:
            lines.append(f"{key}: {reset[key]}")
            skipping = True
        else:
            lines.append(line)
    return "\n".join(lines) + "\n---\n" + body


def trial_dir(root: Path, recorded: str, analyst: str, label: str) -> Path:
    """`AAS-<today>-trial-<analyst>[-<label>]-<system slug>-<nn>`: a run ID, which
    the run-state schema requires, marked as a trial in its slug."""
    today = datetime.datetime.now(datetime.UTC).date().isoformat()
    system = recorded[len("AAS-YYYY-MM-DD-") : -len("-nn")]
    stem = "-".join(part for part in (f"AAS-{today}-trial", analyst, label, system) if part)
    number = 1
    while (root / f"{stem}-{number:02d}").exists():
        number += 1
    return root / f"{stem}-{number:02d}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(recorded: Path, analyst: str, label: str) -> Path:
    recorded = recorded.resolve()
    repo = recorded.parents[len(STATE_ROOT.parts)]
    if repo / STATE_ROOT != recorded.parent:
        raise ValueError(f"not a run directory under {STATE_ROOT}: {recorded}")
    wanted = [BOUNDARY, OPENING, RUN_STATE]
    if analyst != "runtime":
        wanted.append(RUNTIME)
    missing = [name for name in wanted if not (recorded / name).is_file()]
    if missing:
        raise ValueError(f"the recorded run lacks {', '.join(missing)}")
    params = json.loads(
        (recorded / "workflow-state/run.json").read_text(encoding="utf-8")
    )["params"]

    trial = trial_dir(repo / STATE_ROOT, recorded.name, analyst, label)
    (trial / "output").mkdir(parents=True)
    for name in (BOUNDARY, OPENING):
        shutil.copy2(recorded / name, trial / name)
    (trial / RUN_STATE).write_text(
        running_state((recorded / RUN_STATE).read_text(encoding="utf-8"), trial.name),
        encoding="utf-8",
    )
    if analyst != "runtime":
        shutil.copy2(recorded / RUNTIME, trial / RUNTIME)

    definition = AnalyseAgenticSystem(params)
    definition.run_id = trial.name
    definition.repo = repo
    definition.jobs_dir = repo / JOBS
    job = {
        "runtime": lambda: definition.runtime_job(trial),
        "memory": lambda: definition.memory_job(trial, 0, 0),
        "epistemic": lambda: definition.epistemic_job(trial),
    }[analyst]()
    prompt = render_prompt(job, trial)
    (trial / "prompt.md").write_text(prompt, encoding="utf-8")

    inputs = re.findall(r"(?m)^- `(/[^`]+)`$", prompt)
    record = {
        "recorded-run": recorded.name,
        "analyst": analyst,
        "label": label,
        "prepared": datetime.datetime.now(datetime.UTC).isoformat(timespec="seconds"),
        "output": job.output,
        "inputs": {path: sha256(Path(path)) for path in inputs},
    }
    (trial / "trial.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return trial / "prompt.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("prepare", help="copy a recorded run's inputs for one analyst")
    command.add_argument("recorded_run", type=Path, help="a run directory under the state root")
    command.add_argument("analyst", choices=ANALYSTS)
    command.add_argument("--label", default="", help="a name for this trial, e.g. a model or wording")
    args = parser.parse_args(argv)
    if args.label and not re.fullmatch(r"[a-z0-9-]+", args.label):
        parser.error("--label takes lowercase letters, digits and hyphens")
    try:
        print(prepare(args.recorded_run, args.analyst, args.label))
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
