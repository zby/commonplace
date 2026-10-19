"""Phase 0 probe: can a headless worker do an analyst's kind of work unattended?

    python3 probe.py RUN_ROOT codex pi claude-code

Each worker runs in this checkout (read-only use) with the project's normal
configuration and writes its outputs under RUN_ROOT, outside the checkout.
It must read a file, search with rg, run a commonplace-* command, and say
whether the analyse-agentic-system skill is available to it. The probe then
prints what each harness records as the model actually used. API-key
variables are removed first, as in smoke.py.
"""

import json
import os
import sys
from pathlib import Path

from commonplace.headless.harness import Profile
from commonplace.headless.jobs import Run
from smoke import STRIPPED

CHECKOUT = Path(__file__).resolve().parents[3]

TASK = """This is a permissions probe. Do each step and report exactly what happened,
including any step that was denied or failed; do not work around a denial.

1. Read the first heading of AGENTS.md.
2. Run `rg -l "workshop layer" kb/notes` and count the files listed.
3. Run `commonplace-validate --help` and copy its first line.
4. Say whether a skill named analyse-agentic-system is available to you, and how you know.
5. State the model you are running as, if you know it.

Write one line per step, numbered, to the `report` output."""


def profiles(root: Path) -> dict[str, Profile]:
    return {
        "claude-code": Profile("claude-code", "haiku", "low",
                               {"permission-mode": "acceptEdits", "add-dir": str(root)}),
        "codex": Profile("codex", "gpt-6-luna", "low", {"sandbox": "workspace-write"}),
        # --approve trusts project-local files (AGENTS.md, .pi/), which workers must load.
        "pi": Profile("pi", "gpt-6-luna", "low", {"approve": True}),
    }


def reported_model(harness: str, record: dict) -> str | None:
    """The model the harness itself recorded, as opposed to the one requested."""
    launch = json.loads((Path(record["attempt"]) / "launch-1" / "launch.json").read_text())
    session = record["session"]
    if harness == "claude-code":
        return ", ".join(json.loads(launch["stdout"]).get("modelUsage", {})) or None
    roots = {"codex": Path.home() / ".codex" / "sessions", "pi": Path.home() / ".pi" / "agent" / "sessions"}
    for path in roots[harness].rglob(f"*{session}*.jsonl"):
        models = set()
        for line in path.read_text().splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            # codex: payload.model on turn_context; pi: message.model on each reply.
            for holder in (event.get("payload"), event.get("message")) if isinstance(event, dict) else ():
                if isinstance(holder, dict) and isinstance(holder.get("model"), str):
                    models.add(holder["model"])
        return ", ".join(sorted(models)) or None
    return None


def main(root: str, names: list[str]) -> None:
    for var in STRIPPED:
        os.environ.pop(var, None)
    root = Path(root).resolve()
    for name in names:
        run = Run(root / name, CHECKOUT, profiles(root)[name], timeout=600)
        try:
            a = run.ask("probe", TASK, ["report"])
        except Exception as e:
            print(f"== {name}: FAILED: {e}")
            continue
        print(f"== {name} ({a.record['seconds']:.0f} s), reported model: {reported_model(name, a.record)}")
        print(a.outputs["report"].strip())


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:] or ["claude-code", "codex", "pi"])
