"""Tests for the headless job primitives on a fake harness over Workjig; no model is called.

The fake worker reads the frame file it is pointed at and writes each listed
output. Words in the task choose its behaviour: BROKEN exits 1, SLOW-<name>
sleeps past the run's timeout on its first launch only (its marker is in the
working directory, so it spans launches and runs), INCOMPLETE exits 0 without
writing, USAGE reports a usage limit in the problem file and exits 1, SERIAL
exits 1 with OVERLAP if another SERIAL worker is running, PROBLEM writes a
problem, and "Problems found" in a retry prompt makes it write an accepted
answer. It checks that every listed input file exists and is not empty.

Launch mechanics Commonplace does not configure, such as fresh output paths
per relaunch, the backoff wait and problem-over-exit classification, are
Workjig's own tests. In a correction (a `refusal` input), ANSWERS=<n>
writes n `- corrected:` lines to `answers`, and SAME on a first attempt
repeats the previous primary output's bytes.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

import pytest

from commonplace.headless.corrections import produce
from commonplace.headless.harness import HARNESSES, Harness, Profile
from commonplace.headless.jobs import (
    LaunchFailed,
    OutOfAttempts,
    Run,
    RunLocked,
    UsageLimited,
    dismiss,
    gather,
    input_ref,
    output_ref,
)

FAKE = r"""
import json, os, re, sys, time
from pathlib import Path
prompt_path = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1))
prompt = prompt_path.read_text()
task = prompt.split("\n\nInputs (", 1)[0].split("\n\nRequired outputs", 1)[0]
sections, current = {}, None
for line in prompt.splitlines():
    header = re.fullmatch(r"(Inputs|Required outputs|Optional outputs)(?: \(.*\))?:", line)
    if header:
        current = sections.setdefault(header.group(1), {})
    elif current is not None and line.startswith("- "):
        name, _, path = line[2:].partition(": ")
        current[name.removesuffix(".md")] = path
    else:
        current = None
problem_file = Path(prompt.split("write a JSON object to this problem file:\n", 1)[1].splitlines()[0])
inputs = sections.get("Inputs", {})
outputs = {**sections.get("Required outputs", {}), **sections.get("Optional outputs", {})}


def problem(kind, message):
    problem_file.write_text(json.dumps({"kind": kind, "message": message}))


if "USAGE" in task:
    problem("usage_limit", "Usage limit reached. Your limit resets at 5pm.")
    sys.exit(1)
slow = re.search(r"SLOW-(\w+)", task)
if slow and not (Path.cwd() / f"slow-{slow.group(1)}").exists():
    (Path.cwd() / f"slow-{slow.group(1)}").write_text("1")
    time.sleep(5)
if "INCOMPLETE" in task:
    sys.exit(0)
if "SERIAL" in task:
    try:
        fd = os.open(Path.cwd() / "running", os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        print("OVERLAP", file=sys.stderr)
        sys.exit(1)
    time.sleep(0.3)
    os.close(fd)
    os.unlink(Path.cwd() / "running")
for name, path in inputs.items():
    assert Path(path).read_text(), name
if "BROKEN" in task:
    print("tool error", file=sys.stderr)
    sys.exit(1)
if re.search(r"PROBLEM(?!-EXIT)", task):
    problem("unable", "source unavailable")
    sys.exit(0)
structural = "refusal" in inputs and "not good" in Path(inputs["refusal"]).read_text()  # a check's finding
good = "Problems found" in task or "GOOD" in task or structural
for name, path in outputs.items():
    if name == "answers" and "refusal" in inputs:
        n = int(re.search(r"ANSWERS=(\d+)", task).group(1))
        Path(path).write_text("".join(f"- corrected: fixed {i}\n" for i in range(n)))
        continue
    if "SAME" in task and not structural and f"previous-{name}" in inputs:
        Path(path).write_text(Path(inputs[f"previous-{name}"]).read_text())
        continue
    Path(path).write_text(f"{name}: {'good' if good else 'bad'}")
"""

REFUSAL = ("## Findings\n\n- runtime: the trace skips the fallback branch\n\n"
           "## Blockers\n\n- runtime: trace the fallback branch\n- runtime: bound the exclusion claim\n\n"
           "## Scope\n\nverification of the runtime record\n")


def fake_harness(script):
    return Harness(sys.executable, {"_subcommand": [str(script)]}, lambda profile: {},
                   model_used=lambda launch: "fake-model-1" if launch.status == "delivered" else None)


def fake_run(root, script, **kw):
    """A Run on the fake harness whose workers run in root's parent directory, with a 1 s timeout."""
    return Run(root, root.parent, Profile("fake", "m", "low"), timeout=1,
               harnesses={"fake": fake_harness(script)}, sleep=lambda s: None, **kw)


def check(answer):
    return [] if answer.outputs["report"].endswith("good") else ["not good"]


def events(root):
    return [json.loads(line) for line in (root / "log.jsonl").read_text().splitlines()]


def launch_count(root):
    return sum(1 for e in events(root) if e["event"] == "launch")


@pytest.fixture
def script(tmp_path):
    path = tmp_path / "fake.py"
    path.write_text(FAKE)
    return path


@pytest.fixture
def sleeps():
    return []


@pytest.fixture
def run(tmp_path, script, sleeps):
    """A Run with no timeout that records the backoff waits instead of sleeping."""
    run = Run(tmp_path / "run", tmp_path, Profile("fake", "m", "low"),
              harnesses={"fake": fake_harness(script)}, sleep=sleeps.append)
    yield run
    run.close()


def test_harness_commands():
    worker = HARNESSES["claude-code"].worker(
        Profile("claude-code", "opus", "medium",
                {"permission-mode": "acceptEdits", "add-dir": "../a, ../b", "verbose": False}))
    assert list(worker.argv) == ["claude", "--print", "--output-format", "stream-json", "--model", "opus",
                                 "--effort", "medium", "--permission-mode", "acceptEdits",
                                 "--add-dir=../a", "--add-dir=../b", worker.argv[-1]], worker.argv
    assert "{prompt}" in worker.argv[-1]
    assert dict(worker.env) == {"CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS": "0"}
    assert worker.output_protocol == "claude-stream-json"
    worker = HARNESSES["codex"].worker(Profile("codex", "gpt-6.1-sol", "low", {"sandbox": "workspace-write"}))
    assert list(worker.argv[:-1]) == ["codex", "exec", "--json", "--model", "gpt-6.1-sol",
                                      "--config", "model_reasoning_effort=low",
                                      "--output-last-message", "{launch_dir}/last-message.md",
                                      "--sandbox", "workspace-write"], worker.argv
    assert worker.output_protocol == "codex-json"
    worker = HARNESSES["pi"].worker(Profile("pi", "gpt-6-luna", "low"))
    assert list(worker.argv[:6]) == ["pi", "--print", "--mode", "json", "--model", "gpt-6-luna:low"], worker.argv
    assert worker.output_protocol == "pi-json"


def test_ask_records_model_and_second_ask_replays(run):
    a = run.ask("draft", "Write GOOD things.", ["report"])
    assert a.outputs == {"report": "report: good"}, a.outputs
    assert a.record["model"] == "fake-model-1", "the harness-recorded model is the provenance"
    again = run.ask("draft", "Write GOOD things.", ["report"])
    assert again.record["launches"] == a.record["launches"], "second ask must replay the record"
    assert launch_count(run.root) == 1


def test_broken_launch_raises_after_two_relaunches(run, sleeps):
    run.ask("draft", "Write GOOD things.", ["report"])
    with pytest.raises(LaunchFailed) as e:
        run.ask("draft", "BROKEN.", ["report"])
    assert len(e.value.result.launches) == 3, "a nonzero exit is relaunched twice"
    assert sleeps == [30, 30], sleeps
    assert run.ask("draft", "Write GOOD things.", ["report"]).record["model"], "earlier answers remain"


def test_problem_is_a_result_not_a_failure(run):
    r = run.ask("boundary", "PROBLEM.", ["boundary"])
    assert r.problem == "source unavailable" and r.outputs == {}


def test_checked_retries_with_problems_and_reports_attempts(run):
    def prompt(problems):
        return "Write the report." + (f"\n\nProblems found: {problems}" if problems else "")

    c = run.checked("runtime", prompt, check, ["report"], optional=["answers"])
    assert c.outputs["report"] == "report: good" and c.attempts == 2
    rejected = [e for e in events(run.root) if e["event"] == "rejected"]
    assert len(rejected) == 1, rejected


def test_gather_runs_asks_in_parallel(run):
    results = gather(*(lambda r=role: run.ask(r, f"GOOD {r}", ["report"])
                       for role in ("memory", "epistemic", "workflow")))
    assert [x.outputs["report"] for x in results] == ["report: good"] * 3
    assert re.fullmatch(r"[0-9a-f]{64}", results[0].key)


def test_inputs_keyed_by_content_and_named_by_reference(run):
    a = run.ask("runtime", "Write GOOD things.", ["report"], inputs={"source": "v1"})
    launch = Path(a.record["launches"][-1])
    frame = (launch / "prompt.txt").read_text()
    assert frame.index("Inputs (read these exact files):") < frame.index("Required outputs"), frame
    assert (launch / "inputs" / "source.md").read_text() == "v1"
    assert a.record["inputs"] == {"source": hashlib.sha256(b"v1").hexdigest()}
    assert '"v1"' not in json.dumps(a.record), "the record keeps digests, not input text"
    same = run.ask("runtime", "Write GOOD things.", ["report"], inputs={"source": "v1"})
    assert same.record["launches"] == a.record["launches"], "same input bytes: replayed"
    changed = run.ask("runtime", "Write GOOD things.", ["report"], inputs={"source": "v2"})
    assert changed.key != a.key, "a changed input asks again"
    assert run.ask("draft", "Write GOOD things.", ["report"]).key != a.key
    # References name inputs and outputs; Workjig lists each launch's paths after the task.
    task = f"Write GOOD things to {output_ref('report')} from {input_ref('source')}."
    t = run.ask("runtime", task, ["report"], inputs={"source": "v1"})
    launch = Path(t.record["launches"][-1])
    written = (launch / "prompt.txt").read_text()
    assert "to <Required outputs: report.md> from <Inputs: source.md>." in written, written
    assert f"- source.md: {launch / 'inputs' / 'source.md'}" in written, written
    assert f"- report.md: {launch / 'outputs' / 'report.md'}" in written, written
    assert run.scratch("runtime").is_dir() and run.scratch("runtime") == run.scratch("runtime")


def test_usage_limit_is_neither_relaunched_nor_counted(run, sleeps):
    with pytest.raises(UsageLimited) as e:
        run.ask("draft", "USAGE.", ["report"])
    assert len(e.value.result.launches) == 1, "a usage-limited launch is not relaunched"
    assert sleeps == [] and not [ev for ev in events(run.root) if ev["event"] == "failed"], "no wait, not counted"
    # attempts=1 is not consumed: checked launches again and stops on the limit
    with pytest.raises(UsageLimited):
        run.checked("draft", lambda problems: "USAGE.", check, ["report"], attempts=1)
    assert launch_count(run.root) == 2
    assert not [ev for ev in events(run.root) if ev["event"] == "failed"]


def test_timeouts_and_incomplete_results_spend_attempts_across_runs(tmp_path, script):
    root = tmp_path / "counting"
    with fake_run(root, script) as run:
        ok = run.checked("runtime", lambda p: "SLOW-a then GOOD.", check, ["report"], attempts=2)
        assert ok.outputs["report"] == "report: good" and ok.attempts == 2
        (failed,) = [e for e in events(root) if e["event"] == "failed"]
        assert failed["reason"].startswith("timeout"), failed
        with pytest.raises(OutOfAttempts) as e:
            run.checked("runtime", lambda p: "SLOW-b then GOOD.", check, ["report"], attempts=1)
        assert e.value.problems == [] and "timeout" in e.value.failure, (e.value.problems, e.value.failure)
        launches = launch_count(root)
    with fake_run(root, script) as rerun:   # a fresh Run replays the recorded failure
        with pytest.raises(OutOfAttempts):
            rerun.checked("runtime", lambda p: "SLOW-b then GOOD.", check, ["report"], attempts=1)
        assert launch_count(root) == launches, "stopped before launching"
        b = rerun.checked("runtime", lambda p: "SLOW-b then GOOD.", check, ["report"], attempts=2)
        assert b.outputs["report"] == "report: good"

        # An incomplete result spends an attempt; a persistent nonzero exit stops the run without one.
        with pytest.raises(OutOfAttempts) as e:
            rerun.checked("memory", lambda p: "INCOMPLETE.", check, ["report"], attempts=2)
        assert "without outputs ['report.md']" in e.value.failure, e.value.failure
        failed = [e for e in events(root) if e["event"] == "failed" and e["job"] == "memory"]
        assert len(failed) == 2, failed
        with pytest.raises(LaunchFailed):
            rerun.checked("memory", lambda p: "BROKEN.", check, ["report"], attempts=1)
        assert len([e for e in events(root) if e["event"] == "failed" and e["job"] == "memory"]) == 2
        launches = launch_count(root)
    with fake_run(root, script) as third:    # the exit failure is evidence, not a spent attempt
        with pytest.raises(LaunchFailed):
            third.checked("memory", lambda p: "BROKEN.", check, ["report"], attempts=1)
        assert launch_count(root) == launches + 3, "asked again after the rerun, with its relaunches"


def test_worker_limit_serialises_launches(tmp_path, script):
    with fake_run(tmp_path / "serial", script, max_workers=1) as run:
        results = gather(*(lambda r=role: run.ask(r, f"SERIAL GOOD {r}", ["report"])
                           for role in ("memory", "epistemic", "workflow")))
        assert [x.outputs["report"] for x in results] == ["report: good"] * 3


def test_run_lock_refuses_a_second_run(tmp_path, script):
    first = fake_run(tmp_path / "locked", script)
    with pytest.raises(RunLocked) as e:
        fake_run(tmp_path / "locked", script)
    assert e.value.root == tmp_path / "locked"
    first.close()
    fake_run(tmp_path / "locked", script).close()


def test_accept_writes_the_artifact_and_logs_each_acceptance(tmp_path, script):
    with fake_run(tmp_path / "accept", script) as run:
        path = run.accept("members/report.md", "accepted text")
        assert path == (run.artifact / "members" / "report.md").resolve()
        assert path.read_text() == "accepted text"
        run.accept("members/report.md", "accepted text")       # a rerun re-accepts
        assert [p.name for p in path.parent.iterdir()] == ["report.md"], "no temp file left"
        assert [e["path"] for e in events(run.root) if e["event"] == "accepted"] == ["members/report.md"] * 2


def test_produce_runs_the_correction_protocol(tmp_path, script):
    previous = {"report": "report: bad v0"}       # the verifier refused this version

    def prompt(given):
        assert given.keys() >= {"refusal", "previous-report"}, given.keys()
        return "Correct the report. ANSWERS=2 SAME"

    with fake_run(tmp_path / "corrections", script) as run:
        # A "corrected" answer over identical bytes is refused; the next attempt
        # answers a structural refusal carrying the blockers, over the rejected output.
        fixed = produce(run, "runtime", prompt, check, ["report", "answers"], member="runtime",
                        refusal=REFUSAL, previous=previous, attempts=2)
        assert fixed.outputs["report"] == "report: good", fixed.outputs
        assert fixed.outputs["answers"].count("- corrected:") == 2 and fixed.attempts == 2
        rejected = [e for e in events(run.root) if e["event"] == "rejected"]
        assert len(rejected) == 1 and "identical to its predecessor" in rejected[0]["problems"][-1], rejected
        retry = Path(fixed.record["launches"][-1]) / "inputs"
        handed = (retry / "refusal.md").read_text()
        assert handed.startswith("## Findings\n\nnot good\n[correction]"), handed
        assert "- runtime: trace the fallback branch\n- runtime: bound the exclusion claim" in handed, handed
        assert "## Scope\n\nverification of the runtime record" in handed, "other sections carry forward"
        assert (retry / "previous-report.md").read_text() == "report: bad v0"
        assert fixed.record["inputs"].keys() == {"refusal", "previous-report", "previous-answers"}

        # Too few answers for the blockers: one attempt, then out of attempts with the finding.
        with pytest.raises(OutOfAttempts) as e:
            produce(run, "memory", lambda c: "Correct GOOD. ANSWERS=1", check, ["report", "answers"],
                    member="memory", refusal=REFUSAL, previous=previous, attempts=1)
        assert "needs exactly 2 entries" in e.value.problems[-1][0], e.value.problems

        # Unstructured operator findings count as one blocker.
        one = produce(run, "memory", lambda c: "Correct GOOD. ANSWERS=1", check, ["report", "answers"],
                      member="memory", refusal="the profile omits the eviction rule", previous=previous,
                      attempts=1)
        assert one.outputs["report"] == "report: good"

        # A first attempt answers no refusal; its rejection hands the next attempt a
        # structural refusal with no blockers (so no answer entries) over the rejected output.
        seen = []
        first = produce(run, "epistemic", lambda g: seen.append("refusal" in g) or "Write the report. ANSWERS=0",
                        check, ["report", "answers"], member="epistemic", attempts=2, inputs={"boundary": "b1"})
        assert seen == [False, True] and first.attempts == 2
        assert first.outputs == {"report": "report: good", "answers": ""}, first.outputs
        assert first.record["inputs"].keys() == {"boundary", "refusal", "previous-report", "previous-answers"}
        handed = (Path(first.record["launches"][-1]) / "inputs" / "refusal.md").read_text()
        assert handed == "## Findings\n\nnot good\n\n## Blockers\n\nnone\n", handed

        # A role without an answers output repairs in its primary output alone: an unchanged
        # refused version is refused, a changed one is accepted without answers.
        with pytest.raises(OutOfAttempts) as e:
            produce(run, "reconciliation", lambda g: "Reconcile. SAME", check, ["report"], member="reconciliation",
                    refusal="the conflict table omits a record", previous={"report": "report: good"}, attempts=1)
        assert e.value.problems[-1] == [("[correction] answered a refusal with the refused version unchanged "
                                         "and no new auxiliary output")], e.value.problems
        changed = produce(run, "reconciliation", lambda g: "Reconcile GOOD.", check, ["report"],
                          member="reconciliation", refusal="the conflict table omits a record",
                          previous={"report": "report: good v0"}, attempts=1)
        assert changed.outputs == {"report": "report: good"} and changed.record["inputs"].keys() == {
            "refusal", "previous-report"}
        # A rerun without a refusal still hands the previous outputs.
        again = produce(run, "reconciliation", lambda g: f"Reconcile GOOD. {sorted(g)}", check, ["report"],
                        member="reconciliation", previous={"report": "report: good"}, attempts=1)
        assert again.record["inputs"].keys() == {"previous-report"} and "previous-report" in again.record["prompt"]


def test_dismissed_results_are_asked_again_without_spending_attempts(tmp_path, script):
    root = tmp_path / "dismissed"
    with fake_run(root, script) as run:
        answer = run.ask("draft", "Write GOOD things.", ["report"])
        assert run.ask("boundary", "PROBLEM.", ["boundary"]).problem
    with pytest.raises(RunLocked), fake_run(root, script):
        dismiss(root, "draft", answer.key)
    assert [call["call"] for call in dismiss(root, "draft", answer.key)] == ["draft"]
    assert [call["call"] for call in dismiss(root, "boundary")] == ["boundary"]
    with pytest.raises(ValueError, match="no worker problem"):
        dismiss(root, "boundary")
    with fake_run(root, script) as rerun:
        again = rerun.ask("draft", "Write GOOD things.", ["report"], attempts=1)
        assert again.record["call"] == "draft#1" and again.attempts == 1, again.record
        # A dismissed problem continues its own call; a delivered call cannot, so it takes the next identity.
        problem = rerun.ask("boundary", "PROBLEM.", ["boundary"])
        assert problem.record["call"] == "boundary" and len(problem.record["launches"]) == 2
    assert launch_count(root) == 4


def test_a_changed_timeout_replays_answers_and_continues_failures(tmp_path, script):
    root = tmp_path / "timeouts"
    with fake_run(root, script) as run:
        answer = run.ask("draft", "Write GOOD things.", ["report"])
        with pytest.raises(OutOfAttempts):
            run.checked("runtime", lambda p: "SLOW-c then GOOD.", check, ["report"], attempts=1)
        launches = launch_count(root)
    with Run(root, root.parent, Profile("fake", "m", "low"), timeout=30,
             harnesses={"fake": fake_harness(script)}, sleep=lambda s: None) as rerun:
        assert rerun.ask("draft", "Write GOOD things.", ["report"]).record["launches"] == answer.record["launches"]
        assert launch_count(root) == launches, "a longer timeout replays the delivered answer"
        b = rerun.checked("runtime", lambda p: "SLOW-c then GOOD.", check, ["report"], attempts=2)
        assert b.outputs["report"] == "report: good" and b.attempts == 2
        assert b.record["call"] == "runtime" and len(b.record["launches"]) == 2, "one call, its timeout counted"
