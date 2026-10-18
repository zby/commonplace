"""Exercise headless.py and jobs.py with a fake harness; no model is called.

    python3 selftest.py

The fake worker reads the prompt file it is pointed at and writes each listed
output. Words in the prompt choose its behaviour: TRANSIENT fails once with a
provider-overload message, BROKEN exits 1, REFUSE writes a refusal, and
"Problems found" in a retry prompt makes it write an accepted answer.
"""

import re
import sys
import tempfile
from pathlib import Path

from headless import HARNESSES, Harness, LaunchFailed, Profile
from jobs import Run, gather

FAKE = r'''
import re, sys
from pathlib import Path
pointer = sys.argv[-1]
prompt_path = Path(re.search(r"`([^`]+prompt\.md)`", pointer).group(1))
prompt = prompt_path.read_text()
marker = prompt_path.parent / "seen"
if "TRANSIENT" in prompt and not marker.exists():
    marker.write_text("1")
    print("Our servers are currently overloaded. Please try again later.", file=sys.stderr)
    sys.exit(1)
if "BROKEN" in prompt:
    print("tool error", file=sys.stderr)
    sys.exit(1)
if "REFUSE" in prompt:
    Path(re.search(r"reason to `([^`]+)`", prompt).group(1)).write_text("out of scope")
    sys.exit(0)
good = "Problems found" in prompt or "GOOD" in prompt
for name, path in re.findall(r"- `([\w-]+)`(?: \(optional\))?: write to `([^`]+)`", prompt):
    Path(path).write_text(f"{name}: {'good' if good else 'bad'}")
'''


def fake_harness(script):
    return Harness(sys.executable, {"_subcommand": [str(script)]}, lambda profile, d: ({}, "fake-session"))


def check_commands():
    d = Path("/run/x")
    spec, session = HARNESSES["claude-code"].command(
        Profile("claude-code", "opus", "medium",
                {"permission-mode": "acceptEdits", "add-dir": "../a, ../b", "verbose": False}),
        "PROMPT", d)
    assert spec.argv() == ["claude", "--print", "--output-format", "json", "--model", "opus",
                           "--effort", "medium", "--session-id", session,
                           "--permission-mode", "acceptEdits", "--add-dir=../a", "--add-dir=../b",
                           "PROMPT"], spec.argv()
    assert spec.env == {"CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS": "0"}
    spec, session = HARNESSES["codex"].command(
        Profile("codex", "gpt-6.1-sol", "low", {"sandbox": "workspace-write"}), "PROMPT", d)
    assert session is None
    assert spec.argv() == ["codex", "exec", "--json", "--model", "gpt-6.1-sol",
                           "--config", "model_reasoning_effort=low",
                           "--output-last-message", "/run/x/last-message.md",
                           "--sandbox", "workspace-write", "PROMPT"], spec.argv()
    spec, _ = HARNESSES["pi"].command(Profile("pi", "gpt-6-luna", "low"), "PROMPT", d)
    assert spec.argv()[:4] == ["pi", "--print", "--model", "gpt-6-luna:low"], spec.argv()


def main():
    check_commands()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        script = tmp / "fake.py"
        script.write_text(FAKE)
        sleeps = []
        run = Run(tmp / "run", tmp, Profile("fake", "m", "low"),
                  harnesses={"fake": fake_harness(script)}, sleep=sleeps.append)

        a = run.ask("draft", "Write GOOD things.", ["report"])
        assert a.outputs == {"report": "report: good"}, a.outputs
        again = run.ask("draft", "Write GOOD things.", ["report"])
        assert again.record["attempt"] == a.record["attempt"], "second ask must be a cache hit"

        t = run.ask("draft", "TRANSIENT then GOOD.", ["report"])
        assert sleeps == [30] and len(t.record["transient-failures"]) == 1, (sleeps, t.record)

        try:
            run.ask("draft", "BROKEN.", ["report"])
            raise AssertionError("BROKEN must raise")
        except LaunchFailed as e:
            assert len(e.launches) == 1, "a non-transient failure is not relaunched"
        assert list((run.root / "answers").glob("*.json")), "earlier answers remain"

        r = run.ask("boundary", "REFUSE.", ["boundary"])
        assert r.refusal == "out of scope" and r.outputs == {}

        def prompt(problems):
            return "Write the report." + (f"\n\nProblems found: {problems}" if problems else "")

        def check(answer):
            return [] if answer.outputs["report"].endswith("good") else ["not good"]

        c = run.checked("runtime", prompt, check, ["report", "answers"], optional=["answers"])
        assert c.outputs["report"] == "report: good"
        rejected = [line for line in (run.root / "log.jsonl").read_text().splitlines() if '"rejected"' in line]
        assert len(rejected) == 1, rejected

        results = gather(*(lambda r=role: run.ask(r, f"GOOD {r}", ["report"])
                           for role in ("memory", "epistemic", "workflow")))
        assert [x.outputs["report"] for x in results] == ["report: good"] * 3
        assert re.fullmatch(r"[0-9a-f]{64}", results[0].key)
    print("selftest passed")


if __name__ == "__main__":
    main()
