"""Exercise headless.py, jobs.py and corrections.py with a fake harness; no model is called.

    uv run python selftest.py

(`uv run` from this directory finds the worktree's project, whose venv has the
`commonplace` package that corrections.py imports.)

The fake worker reads the prompt file it is pointed at and writes each listed
output. Words in the prompt choose its behaviour: TRANSIENT fails once with a
provider-overload message, BROKEN exits 1, FLAKY-<name> exits 1 on its first
launch only (its marker is in the working directory, so it spans attempts and
runs), USAGE prints a usage-limit message and exits 1, SERIAL exits 1 with
OVERLAP if another SERIAL worker is running, REFUSE writes a refusal, and
"Problems found" in a retry prompt makes it write an accepted answer. It
checks that every listed input file exists and is not empty. In a correction
(a `refusal` input), ANSWERS=<n> writes n `- corrected:` lines to `answers`,
and SAME on a first attempt repeats the previous primary output's bytes.
"""

import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

from corrections import correct
from headless import HARNESSES, Harness, LaunchFailed, Profile, UsageLimited
from jobs import OutOfAttempts, Run, RunLocked, gather

FAKE = r'''
import os, re, sys, time
from pathlib import Path
pointer = sys.argv[-1]
prompt_path = Path(re.search(r"`([^`]+prompt\.md)`", pointer).group(1))
prompt = prompt_path.read_text()
marker = prompt_path.parent / "seen"
if "TRANSIENT" in prompt and not marker.exists():
    marker.write_text("1")
    print("Our servers are currently overloaded. Please try again later.", file=sys.stderr)
    sys.exit(1)
if "USAGE" in prompt:
    print("Usage limit reached. Your limit resets at 5pm.")
    sys.exit(1)
flaky = re.search(r"FLAKY-(\w+)", prompt)
if flaky and not (Path.cwd() / f"flaky-{flaky.group(1)}").exists():
    (Path.cwd() / f"flaky-{flaky.group(1)}").write_text("1")
    print("tool error", file=sys.stderr)
    sys.exit(1)
if "SERIAL" in prompt:
    try:
        fd = os.open(Path.cwd() / "running", os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        print("OVERLAP", file=sys.stderr)
        sys.exit(1)
    time.sleep(0.3)
    os.close(fd)
    os.unlink(Path.cwd() / "running")
for name, path in re.findall(r"- `([\w-]+)`: `([^`]+/inputs/[^`]+)`", prompt):
    assert Path(path).read_text(), name
if "BROKEN" in prompt:
    print("tool error", file=sys.stderr)
    sys.exit(1)
if "REFUSE" in prompt:
    Path(re.search(r"reason to `([^`]+)`", prompt).group(1)).write_text("out of scope")
    sys.exit(0)
good = "Problems found" in prompt or "GOOD" in prompt
inputs = dict(re.findall(r"- `([\w-]+)`: `([^`]+/inputs/[^`]+)`", prompt))
for name, path in re.findall(r"- `([\w-]+)`(?: \(optional\))?: write to `([^`]+)`", prompt):
    if name == "answers" and "refusal" in inputs:
        n = int(re.search(r"ANSWERS=(\d+)", prompt).group(1))
        Path(path).write_text("".join(f"- corrected: fixed {i}\n" for i in range(n)))
        continue
    if "SAME" in prompt and "Problems found" not in prompt and f"previous-{name}" in inputs:
        Path(path).write_text(Path(inputs[f"previous-{name}"]).read_text())
        continue
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

        check_inputs(run)
        check_usage_limit(run, sleeps, check)
        run.close()
        check_attempt_counting(tmp, script, check)
        check_worker_limit(tmp, script)
        check_run_lock(tmp, script)
        check_accept(tmp, script)
        check_corrections(tmp, script, check)
    print("selftest passed")


def fake_run(root, script, **kw):
    """A Run on the fake harness whose workers run in root's parent directory."""
    return Run(root, root.parent, Profile("fake", "m", "low"),
               harnesses={"fake": fake_harness(script)}, sleep=lambda s: None, **kw)


def check_inputs(run):
    a = run.ask("runtime", "Write GOOD things.", ["report"], inputs={"source": "v1"})
    prompt_md = (Path(a.record["attempt"]) / "prompt.md").read_text()
    assert prompt_md.index("## Inputs") < prompt_md.index("## Outputs"), prompt_md
    assert (Path(a.record["attempt"]) / "inputs" / "source.md").read_text() == "v1"
    assert a.record["inputs"] == {"source": hashlib.sha256(b"v1").hexdigest()}
    assert '"v1"' not in json.dumps(a.record), "the record keeps digests, not input text"
    same = run.ask("runtime", "Write GOOD things.", ["report"], inputs={"source": "v1"})
    assert same.record["attempt"] == a.record["attempt"], "same input bytes: a cache hit"
    changed = run.ask("runtime", "Write GOOD things.", ["report"], inputs={"source": "v2"})
    assert changed.key != a.key, "a changed input asks again"
    assert run.ask("draft", "Write GOOD things.", ["report"]).key != a.key


def check_usage_limit(run, sleeps, check):
    before = list(sleeps)
    key = run.key("USAGE.", ["report"], [])
    try:
        run.ask("draft", "USAGE.", ["report"])
        raise AssertionError("USAGE must raise")
    except UsageLimited as e:
        assert len(e.launches) == 1, "a usage-limited launch is not relaunched"
    assert sleeps == before and run.failures(key) == 0, "no wait and no failure record"
    try:   # attempts=1 is not consumed: checked launches again and stops on the limit
        run.checked("draft", lambda problems: "USAGE.", check, ["report"], attempts=1)
        raise AssertionError("USAGE must raise")
    except UsageLimited:
        pass
    assert run.failures(key) == 0


def check_attempt_counting(tmp, script, check):
    root = tmp / "counting"
    with fake_run(root, script) as run:
        ok = run.checked("runtime", lambda p: "FLAKY-a then GOOD.", check, ["report"], attempts=2)
        assert ok.outputs["report"] == "report: good" and run.failures(ok.key) == 1
        try:
            run.checked("runtime", lambda p: "FLAKY-b then GOOD.", check, ["report"], attempts=1)
            raise AssertionError("one attempt must not suffice")
        except OutOfAttempts as e:
            assert e.problems == [] and "exit 1" in e.failure, (e.problems, e.failure)
        key_b = run.key("FLAKY-b then GOOD.", ["report"], [])
        launches = (root / "log.jsonl").read_text().count('"launch"')
    with fake_run(root, script) as rerun:   # a fresh Run sees the persisted failure
        assert rerun.failures(key_b) == 1
        try:
            rerun.checked("runtime", lambda p: "FLAKY-b then GOOD.", check, ["report"], attempts=1)
            raise AssertionError("the persisted failure must count")
        except OutOfAttempts:
            pass
        assert (root / "log.jsonl").read_text().count('"launch"') == launches, "stopped before launching"
        b = rerun.checked("runtime", lambda p: "FLAKY-b then GOOD.", check, ["report"], attempts=2)
        assert b.outputs["report"] == "report: good"


def check_worker_limit(tmp, script):
    with fake_run(tmp / "serial", script, max_workers=1) as run:
        results = gather(*(lambda r=role: run.ask(r, f"SERIAL GOOD {r}", ["report"])
                           for role in ("memory", "epistemic", "workflow")))
        assert [x.outputs["report"] for x in results] == ["report: good"] * 3


def check_run_lock(tmp, script):
    first = fake_run(tmp / "locked", script)
    try:
        fake_run(tmp / "locked", script)
        raise AssertionError("a second Run on a held root must fail")
    except RunLocked as e:
        assert e.root == tmp / "locked"
    first.close()
    fake_run(tmp / "locked", script).close()


def check_accept(tmp, script):
    with fake_run(tmp / "accept", script) as run:
        path = run.accept("members/report.md", "accepted text")
        assert path == (run.artifact / "members" / "report.md").resolve()
        assert path.read_text() == "accepted text"
        run.accept("members/report.md", "accepted text")       # a rerun re-accepts
        assert [p.name for p in path.parent.iterdir()] == ["report.md"], "no temp file left"
        events = [json.loads(line) for line in (run.root / "log.jsonl").read_text().splitlines()]
        assert [e["path"] for e in events if e["event"] == "accepted"] == ["members/report.md"] * 2


REFUSAL = ("## Findings\n\n- runtime: the trace skips the fallback branch\n\n"
           "## Blockers\n\n- runtime: trace the fallback branch\n- runtime: bound the exclusion claim\n\n"
           "## Scope\n\nverification of the runtime record\n")


def check_corrections(tmp, script, check):
    previous = {"report": "report: bad v0"}       # a first attempt answers no refusal

    def prompt(problems):
        return "Correct the report. ANSWERS=2 SAME" + (f"\n\nProblems found: {problems}" if problems else "")

    with fake_run(tmp / "corrections", script) as run:
        # A "corrected" answer over identical bytes is refused; the next attempt
        # answers a structural refusal carrying the blockers, over the rejected output.
        fixed = correct(run, "runtime", prompt, check, ["report"], member="runtime",
                        refusal=REFUSAL, previous=previous, attempts=2)
        assert fixed.outputs["report"] == "report: good", fixed.outputs
        assert fixed.outputs["answers"].count("- corrected:") == 2
        events = [json.loads(line) for line in (run.root / "log.jsonl").read_text().splitlines()]
        rejected = [e for e in events if e["event"] == "rejected"]
        assert len(rejected) == 1 and "identical to its predecessor" in rejected[0]["problems"][-1], rejected
        retry = Path(fixed.record["attempt"]) / "inputs"
        handed = (retry / "refusal.md").read_text()
        assert handed.startswith("## Findings\n\nnot good\n[correction]"), handed
        assert "- runtime: trace the fallback branch\n- runtime: bound the exclusion claim" in handed, handed
        assert "## Scope\n\nverification of the runtime record" in handed, "other sections carry forward"
        assert (retry / "previous-report.md").read_text() == "report: bad v0"
        assert fixed.record["inputs"].keys() == {"refusal", "previous-report", "previous-answers"}

        # Too few answers for the blockers: one attempt, then out of attempts with the finding.
        try:
            correct(run, "memory", lambda p: "Correct GOOD. ANSWERS=1", check, ["report"],
                    member="memory", refusal=REFUSAL, previous=previous, attempts=1)
            raise AssertionError("one answer for two blockers must be refused")
        except OutOfAttempts as e:
            assert "needs exactly 2 entries" in e.problems[-1][0], e.problems

        # Unstructured operator findings count as one blocker.
        one = correct(run, "memory", lambda p: "Correct GOOD. ANSWERS=1", check, ["report"],
                      member="memory", refusal="the profile omits the eviction rule", previous=previous,
                      attempts=1)
        assert one.outputs["report"] == "report: good"


if __name__ == "__main__":
    main()
