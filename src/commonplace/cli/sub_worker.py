"""One read-mode Workjig call for an operator-directed cross-harness check."""

import argparse
import json
import math
import subprocess
from pathlib import Path
from uuid import uuid4

import yaml

from commonplace.headless.harness import HARNESSES
from commonplace.headless.jobs import (
    Exhausted,
    LaunchFailed,
    Run,
    UsageLimited,
    input_ref,
    output_ref,
)
from commonplace.lib.review_workflows.gates import changed_paths, checkout_state
from commonplace.lib.tasks import load_profile

STATE = Path("kb/workflow-state/data/current/sub-worker")
PROFILES = Path("kb/instructions/sub-worker-profiles.yaml")
FRAME = (f"Read {input_ref('brief')}. Another agent requested this read-only check. Nobody will "
         f"answer questions. Write your answer to {output_ref('answer')} or write the named problem "
         "file if blocked. Inspect only sources needed for the brief. Do not edit any other file, commit, "
         "or launch another worker.")


def launch(root, brief, profile, timeout, *, harnesses=HARNESSES):
    directory = STATE / uuid4().hex
    before = checkout_state(root, exclude=directory)
    report = {"run_dir": str(directory), "model": None}
    try:
        with Run(root / directory, root, profile, timeout=timeout, harnesses=harnesses) as run:
            answer = run.ask("check", FRAME, ["answer"], inputs={"brief": brief})
            report["model"] = answer.record["model"]
            if answer.problem is not None:
                report.update(status="problem", problem=answer.problem)
            else:
                report.update(status="answered", answer=answer.outputs["answer"])
    except UsageLimited as error:
        report.update(status="usage-limit", problem=str(error))
    except (LaunchFailed, Exhausted) as error:
        report.update(status="launch-failed", problem=str(error))
    except (OSError, ValueError, KeyError) as error:
        report.update(status="setup-error", problem=str(error))
    finally:
        changes = changed_paths(before, checkout_state(root, exclude=directory))
        if changes:
            report.pop("answer", None)
            report.update(worker_status=report.get("status"), status="checkout-changed", changes=changes)
    (root / directory).mkdir(parents=True, exist_ok=True)
    (root / directory / "result.json").write_text(json.dumps(
        {k: v for k, v in report.items() if k not in {"answer", "problem"}}, indent=2) + "\n", encoding="utf-8")
    return report


EXIT = {"answered": 0, "problem": 1, "setup-error": 2, "launch-failed": 3, "usage-limit": 4, "checkout-changed": 5}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    run = parser.add_subparsers(dest="command", required=True).add_parser("run")
    run.add_argument("--brief", required=True, type=Path, help="public-safe text brief (retained with the answer)")
    run.add_argument("--profile", required=True, help=f"named profile in {PROFILES}")
    run.add_argument("--timeout", type=float, help="positive per-launch timeout in seconds")
    args = parser.parse_args(argv)
    try:
        if args.timeout is not None and not (math.isfinite(args.timeout) and args.timeout > 0):
            raise ValueError("timeout must be finite and positive")
        root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
        report = launch(root, args.brief.read_text(encoding="utf-8"), load_profile(root, args.profile, PROFILES),
                        args.timeout)
    except (OSError, ValueError, TypeError, KeyError, subprocess.CalledProcessError, yaml.YAMLError) as error:
        report = {"status": "setup-error", "problem": str(error)}
    print(json.dumps(report, indent=2))
    return EXIT[report["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
