"""Create a trial run of the loop text.

From the repository root:

    uv run python kb/work/code-scheduled-workflows/trial/setup.py <scenario> [name]

Scenarios are described in trial_workflow.py. The run goes under `runs/`,
which git ignores. The script prints the run directory and the `<shell>` value
for the loop text.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from commonplace.workflow import Orchestrator  # noqa: E402

SCENARIOS = ("clean", "retry", "problem", "stop")

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


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in SCENARIOS:
        print(f"usage: setup.py {{{'|'.join(SCENARIOS)}}} [name]", file=sys.stderr)
        return 2
    scenario = argv[0]
    run_dir = HERE / "runs" / (argv[1] if len(argv) > 1 else scenario)
    if run_dir.exists():
        print(f"{run_dir} exists; remove it or choose another name", file=sys.stderr)
        return 1
    run_dir.mkdir(parents=True)
    (run_dir / "source.md").write_text(SOURCE, encoding="utf-8")
    if scenario == "problem":
        (run_dir / "incoming").mkdir()
        (run_dir / "incoming" / "notes.md").write_text(NOTES, encoding="utf-8")
    Orchestrator.create(run_dir, "trial_workflow:Trial", {"scenario": scenario})
    relative = HERE.relative_to(Path.cwd()) if HERE.is_relative_to(Path.cwd()) else HERE
    print(f"run: {run_dir}")
    print(f"shell: PYTHONPATH={relative} uv run python -m commonplace.workflow.shell")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
