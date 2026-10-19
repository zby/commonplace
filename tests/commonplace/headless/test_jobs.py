"""Tests for the headless job primitives on a fake harness; no model is called.

The fake worker reads the prompt file it is pointed at and writes each listed
output. Words in the prompt choose its behaviour: TRANSIENT exits 1 once with
a provider-overload message, BROKEN exits 1, SLOW-<name> sleeps past the run's
timeout on its first launch only (its marker is in the working directory, so
it spans attempts and runs), INCOMPLETE exits 0 without writing, USAGE prints
a usage-limit message and exits 1, SERIAL exits 1 with OVERLAP if another
SERIAL worker is running, PROBLEM writes a problem, and "Problems found" in a
retry prompt makes it write an accepted answer. On its first launch only (the
TRANSIENT marker), PARTIAL-EXIT writes every listed output and exits 1, its
relaunch then exiting 0 without writing, and PROBLEM-EXIT writes a problem and
exits 1, its relaunch then answering normally. It checks that every listed
input file exists and is not empty. In a correction (a `refusal` input),
ANSWERS=<n> writes n `- corrected:` lines to `answers`, and SAME on a first
attempt repeats the previous primary output's bytes.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

import pytest

from commonplace.headless.corrections import produce
from commonplace.headless.harness import (
    HARNESSES,
    Harness,
    LaunchFailed,
    Profile,
    UsageLimited,
)
from commonplace.headless.jobs import (
    IncompleteOutputs,
    OutOfAttempts,
    Run,
    RunLocked,
    gather,
)

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
if "PARTIAL-EXIT" in prompt:
    if marker.exists():
        sys.exit(0)
    marker.write_text("1")
    for name, path in re.findall(r"- `([\w-]+)`(?: \(optional\))?: write to `([^`]+)`", prompt):
        Path(path).write_text(f"{name}: from the failed launch")
    sys.exit(1)
if "PROBLEM-EXIT" in prompt and not marker.exists():
    marker.write_text("1")
    Path(re.search(r"write why to `([^`]+)`", prompt).group(1)).write_text("left by the failed launch")
    sys.exit(1)
if "USAGE" in prompt:
    print("Usage limit reached. Your limit resets at 5pm.")
    sys.exit(1)
slow = re.search(r"SLOW-(\w+)", prompt)
if slow and not (Path.cwd() / f"slow-{slow.group(1)}").exists():
    (Path.cwd() / f"slow-{slow.group(1)}").write_text("1")
    time.sleep(5)
if "INCOMPLETE" in prompt:
    sys.exit(0)
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
if re.search(r"PROBLEM(?!-EXIT)", prompt):
    Path(re.search(r"write why to `([^`]+)`", prompt).group(1)).write_text("source unavailable")
    sys.exit(0)
inputs = dict(re.findall(r"- `([\w-]+)`: `([^`]+/inputs/[^`]+)`", prompt))
structural = "refusal" in inputs and "not good" in Path(inputs["refusal"]).read_text()  # a check's finding
good = "Problems found" in prompt or "GOOD" in prompt or structural
for name, path in re.findall(r"- `([\w-]+)`(?: \(optional\))?: write to `([^`]+)`", prompt):
    if name == "answers" and "refusal" in inputs:
        n = int(re.search(r"ANSWERS=(\d+)", prompt).group(1))
        Path(path).write_text("".join(f"- corrected: fixed {i}\n" for i in range(n)))
        continue
    if "SAME" in prompt and not structural and f"previous-{name}" in inputs:
        Path(path).write_text(Path(inputs[f"previous-{name}"]).read_text())
        continue
    Path(path).write_text(f"{name}: {'good' if good else 'bad'}")
'''

REFUSAL = ("## Findings\n\n- runtime: the trace skips the fallback branch\n\n"
           "## Blockers\n\n- runtime: trace the fallback branch\n- runtime: bound the exclusion claim\n\n"
           "## Scope\n\nverification of the runtime record\n")


def fake_harness(script):
    return Harness(sys.executable, {"_subcommand": [str(script)]}, lambda profile, d: ({}, "fake-session"),
                   model_used=lambda launch: "fake-model-1" if launch.ok else None)


def fake_run(root, script, **kw):
    """A Run on the fake harness whose workers run in root's parent directory, with a 1 s timeout."""
    return Run(root, root.parent, Profile("fake", "m", "low"), timeout=1,
               harnesses={"fake": fake_harness(script)}, sleep=lambda s: None, **kw)


def check(answer):
    return [] if answer.outputs["report"].endswith("good") else ["not good"]


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


def test_ask_records_model_and_second_ask_hits_cache(run):
    a = run.ask("draft", "Write GOOD things.", ["report"])
    assert a.outputs == {"report": "report: good"}, a.outputs
    assert a.record["model"] == "fake-model-1", "the harness-recorded model is the provenance"
    again = run.ask("draft", "Write GOOD things.", ["report"])
    assert again.record["attempt"] == a.record["attempt"], "second ask must be a cache hit"


def test_transient_failure_relaunches_after_backoff(run, sleeps):
    t = run.ask("draft", "TRANSIENT then GOOD.", ["report"])
    assert sleeps == [30] and len(t.record["failed-launches"]) == 1, (sleeps, t.record)


def test_broken_launch_raises_after_two_relaunches(run, sleeps):
    run.ask("draft", "Write GOOD things.", ["report"])
    with pytest.raises(LaunchFailed) as e:
        run.ask("draft", "BROKEN.", ["report"])
    assert len(e.value.launches) == 3, "a nonzero exit is relaunched twice"
    assert sleeps == [30, 120], sleeps
    assert list((run.root / "answers").glob("*.json")), "earlier answers remain"


def test_a_failed_launchs_outputs_are_not_the_relaunchs_result(run, sleeps):
    key = run.key("PARTIAL-EXIT.", ["report"], [])
    with pytest.raises(IncompleteOutputs) as e:
        run.ask("draft", "PARTIAL-EXIT.", ["report"])
    assert e.value.missing == ["report"], e.value.missing
    (record,) = run.failure_records(key)
    assert record["kind"] == "incomplete" and run.failures(key) == 1, record
    attempt = Path(record["attempt"])
    assert (attempt / "launch-1" / "outputs" / "report.md").read_text() == "report: from the failed launch"
    assert list((attempt / "outputs").iterdir()) == [], "the relaunch starts from an empty outputs directory"
    assert sleeps == [30]


def test_a_failed_launchs_problem_is_evidence_not_the_answer(run):
    a = run.ask("draft", "PROBLEM-EXIT then GOOD.", ["report"])
    assert a.problem is None and a.outputs == {"report": "report: good"}, (a.problem, a.outputs)
    attempt = Path(a.record["attempt"])
    assert (attempt / "launch-1" / "outputs" / "problem.md").read_text() == "left by the failed launch"
    (failed,) = a.record["failed-launches"]
    assert failed["exit"] == 1, failed


def test_problem_is_a_result_not_a_failure(run):
    r = run.ask("boundary", "PROBLEM.", ["boundary"])
    assert r.problem == "source unavailable" and r.outputs == {}


def test_checked_retries_with_problems_and_reports_attempts(run):
    def prompt(problems):
        return "Write the report." + (f"\n\nProblems found: {problems}" if problems else "")

    c = run.checked("runtime", prompt, check, ["report", "answers"], optional=["answers"])
    assert c.outputs["report"] == "report: good" and c.attempts == 2
    rejected = [line for line in (run.root / "log.jsonl").read_text().splitlines() if '"rejected"' in line]
    assert len(rejected) == 1, rejected


def test_gather_runs_asks_in_parallel(run):
    results = gather(*(lambda r=role: run.ask(r, f"GOOD {r}", ["report"])
                       for role in ("memory", "epistemic", "workflow")))
    assert [x.outputs["report"] for x in results] == ["report: good"] * 3
    assert re.fullmatch(r"[0-9a-f]{64}", results[0].key)


def test_inputs_keyed_by_digest_and_tokens_filled_after_keying(run):
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
    # Attempt-path tokens are filled after keying, so the key is the same for any attempt directory.
    tokens = "Write GOOD things to {output:report} from {input:source}; scratch in {scratch}; or {problem}"
    t = run.ask("runtime", tokens, ["report"], inputs={"source": "v1"})
    assert t.key == run.key(tokens, ["report"], [], {"source": "v1"})
    attempt = Path(t.record["attempt"])
    written = (attempt / "prompt.md").read_text()
    assert f"to {attempt / 'outputs' / 'report.md'} from {attempt / 'inputs' / 'source.md'}" in written, written
    assert f"scratch in {attempt / 'scratch'}; or {attempt / 'outputs' / 'problem.md'}" in written, written
    assert (attempt / "scratch").is_dir()
    with pytest.raises(ValueError, match=re.escape("{output:nope}")):
        run.ask("runtime", "Write to {output:nope}", ["report"])


def test_usage_limit_is_neither_relaunched_nor_counted(run, sleeps):
    key = run.key("USAGE.", ["report"], [])
    with pytest.raises(UsageLimited) as e:
        run.ask("draft", "USAGE.", ["report"])
    assert len(e.value.launches) == 1, "a usage-limited launch is not relaunched"
    assert sleeps == [] and run.failures(key) == 0, "no wait and no failure record"
    # attempts=1 is not consumed: checked launches again and stops on the limit
    with pytest.raises(UsageLimited):
        run.checked("draft", lambda problems: "USAGE.", check, ["report"], attempts=1)
    assert run.failures(key) == 0


def test_timeouts_and_incomplete_results_spend_attempts_across_runs(tmp_path, script):
    root = tmp_path / "counting"
    with fake_run(root, script) as run:
        ok = run.checked("runtime", lambda p: "SLOW-a then GOOD.", check, ["report"], attempts=2)
        assert ok.outputs["report"] == "report: good" and run.failures(ok.key) == 1 and ok.attempts == 2
        assert run.failure_records(ok.key)[0]["kind"] == "timeout"
        with pytest.raises(OutOfAttempts) as e:
            run.checked("runtime", lambda p: "SLOW-b then GOOD.", check, ["report"], attempts=1)
        assert e.value.problems == [] and "timed out" in e.value.failure, (e.value.problems, e.value.failure)
        key_b = run.key("SLOW-b then GOOD.", ["report"], [])
        launches = (root / "log.jsonl").read_text().count('"launch"')
    with fake_run(root, script) as rerun:   # a fresh Run sees the persisted failure
        assert rerun.failures(key_b) == 1
        with pytest.raises(OutOfAttempts):
            rerun.checked("runtime", lambda p: "SLOW-b then GOOD.", check, ["report"], attempts=1)
        assert (root / "log.jsonl").read_text().count('"launch"') == launches, "stopped before launching"
        b = rerun.checked("runtime", lambda p: "SLOW-b then GOOD.", check, ["report"], attempts=2)
        assert b.outputs["report"] == "report: good"

        # An incomplete result spends an attempt; a persistent nonzero exit stops the run without one.
        with pytest.raises(OutOfAttempts) as e:
            rerun.checked("memory", lambda p: "INCOMPLETE.", check, ["report"], attempts=2)
        assert "without outputs ['report']" in e.value.failure, e.value.failure
        assert rerun.failures(rerun.key("INCOMPLETE.", ["report"], [])) == 2
        with pytest.raises(LaunchFailed):
            rerun.checked("memory", lambda p: "BROKEN.", check, ["report"], attempts=1)
        key_broken = rerun.key("BROKEN.", ["report"], [])
        assert rerun.failures(key_broken) == 0 and rerun.failure_records(key_broken)[0]["kind"] == "exit"
        launches = (root / "log.jsonl").read_text().count('"launch"')
    with fake_run(root, script) as third:    # the exit failure is evidence, not a spent attempt
        with pytest.raises(LaunchFailed):
            third.checked("memory", lambda p: "BROKEN.", check, ["report"], attempts=1)
        assert (root / "log.jsonl").read_text().count('"launch"') == launches + 1, "asked again after the rerun"


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
        events = [json.loads(line) for line in (run.root / "log.jsonl").read_text().splitlines()]
        assert [e["path"] for e in events if e["event"] == "accepted"] == ["members/report.md"] * 2


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
        handed = (Path(first.record["attempt"]) / "inputs" / "refusal.md").read_text()
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
