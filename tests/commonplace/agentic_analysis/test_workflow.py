"""Drive the analysis workflow end to end with a fake harness: local Git source, prepared worktree, no model.

The fake worker reads the invocation it is pointed at, finds the frame lines
(`role`, `output`, `output-answers`, `refusal`, `artifact`), resolves their
references to the input and output paths Workjig lists, and writes a
member that passes the real checks, built with the execution fixtures'
generators. It then validates the member in its role, as a real worker does,
and writes a problem if that fails. A scenario file (`FAKE_SCENARIO`) says what
each role does per call: the boundary's disposition, the report verifier's
blockers per verdict, the calls at which a role writes a problem instead, and
the seconds a role sleeps before answering a correction (`delay`).
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.cli.analysis import main
from commonplace.headless.harness import HARNESSES, Harness
from commonplace.headless.jobs import OutOfAttempts, dismiss, run_lock
from commonplace.lib.agentic_analysis.workflow import Analysis, Problem, Stopped
from commonplace.lib.agentic_analysis.worktree import (
    inspect_analysis,
    start_analysis,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    IDENTITY,
    git,
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    acquisition as local_acquisition,  # noqa: F401 - explicit fixture registration
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared as prepared_checkout,  # noqa: F401 - transitive local fixture
)
from tests.commonplace.agentic_analysis.execution_fixtures import (
    prepared_template as prepared_template,  # noqa: PLC0414 - session baseline registration
)

pytestmark = pytest.mark.slow

ROOT = Path(__file__).resolve().parents[3]

FAKE = r'''
import json, os, re, sys, time
from pathlib import Path

sys.path.insert(0, os.environ["FAKE_ROOT"])
from tests.commonplace.agentic_analysis.execution_fixtures import (
    ScriptedRun, candidate, memory_profile, reconciliation, report, report_verdict, subject_verdict, synthesis,
)

prompt_path = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1))
prompt = prompt_path.read_text()
sections, current = {}, None
for line in prompt.splitlines():
    header = re.fullmatch(r"(Inputs|Required outputs|Optional outputs)(?: \(.*\))?:", line)
    if header:
        current = sections.setdefault(header.group(1), {})
    elif current is not None and line.startswith("- "):
        name, _, path = line[2:].partition(": ")
        current[name] = path
    else:
        current = None
problem_file = prompt.split("write a JSON object to this problem file:\n", 1)[1].splitlines()[0]
frame = {}
for name, value in re.findall(r"^([\w-]+) = (.*)$", prompt, re.M):
    ref = re.fullmatch(r"<(Inputs|Required outputs|Optional outputs): (.+)>", value)
    frame.setdefault(name, sections[ref.group(1)][ref.group(2)] if ref else value)


def problem(message):
    Path(problem_file).write_text(json.dumps({"kind": "unable", "message": message}))
role = frame["role"]
run_dir = Path(frame["artifact"]).parent
scenario = json.loads(Path(os.environ["FAKE_SCENARIO"]).read_text())
counts = Path(os.environ["FAKE_SCENARIO"]).with_name("counts")
counts.mkdir(exist_ok=True)
counter = counts / role
call = int(counter.read_text()) + 1 if counter.exists() else 1
counter.write_text(str(call))

a = ScriptedRun(run_dir)
if call in scenario.get("problem", {}).get(role, []):
    problem(f"{role}: the fixture cannot do this job (call {call})")
    sys.exit(0)

refusal = frame.get("refusal")
refusal = Path(refusal) if refusal and refusal != "absent" and Path(refusal).is_file() else None
blockers = []
if refusal is not None:
    text = refusal.read_text()
    section = re.search(r"^## Blockers\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if section is None:
        blockers = ["unstructured"]
    else:
        blockers = [line for line in section.group(1).splitlines() if line.startswith("- ")]
    time.sleep(scenario.get("delay", {}).get(role, 0))

if role == "boundary":
    member = candidate(a, scenario.get("disposition", "complete"))
elif role in ("runtime", "memory", "epistemic", "workflow"):
    member = report(a, role)
    if call > 1:
        member = member.replace("Local fixture only;", f"Corrected in call {call}; local fixture only;")
elif role == "reconciliation":
    member = reconciliation(a)
elif role == "report-verification":
    verdicts = scenario.get("report-verification", ["none"])
    member = report_verdict(a, verdicts[min(call, len(verdicts)) - 1])
elif role in ("profile-verification", "synthesis-verification"):
    member = subject_verdict(a).decode()
elif role == "memory-profile":
    member = memory_profile(a).decode()
elif role == "synthesis":
    member = synthesis(a).decode()
else:
    raise SystemExit(f"unknown role {role}")
Path(frame["output"]).write_text(member)

# Self-validate as a real worker does, in-process instead of through `commonplace-validate`.
import contextlib, io
from commonplace.cli.validate_notes import main as validate
captured = io.StringIO()
with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
    try:
        code = validate([frame["output"], "--artifact", frame["artifact"], "--role", role])
    except SystemExit as exit:
        code = exit.code
if code:
    problem(f"{role}: self-validation failed (exit {code}):\n{captured.getvalue()}")
    sys.exit(0)

answers = "".join(f"- corrected: revised the member for blocker {i + 1}.\n" for i in range(len(blockers)))
if "output-answers" in frame:
    Path(frame["output-answers"]).write_text(answers)
elif refusal is not None:
    path = sections.get("Optional outputs", {}).get("answers.md")
    if path:
        Path(path).write_text(answers)
'''

REFUSE_RUNTIME_AND_MEMORY = "- runtime: reconsider the SRC-1 runtime account.\n- memory: reconsider the SRC-1 memory account."
REFUSE_MEMORY_AND_EPISTEMIC = ("- memory: reconsider the SRC-1 memory account.\n"
                               "- epistemic: reconsider the SRC-1 epistemic account.")


@pytest.fixture
def workflow(request, tmp_path, monkeypatch):
    """A function that allocates a run on the local source and returns (run_dir, new_analysis)."""
    request.getfixturevalue("local_acquisition")      # its monkeypatches clone IDENTITY from local Git
    prepared = request.getfixturevalue("prepared_checkout")
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(prepared.repo / "kb"))
    monkeypatch.setenv("FAKE_ROOT", str(ROOT))
    fake_dir = tmp_path / "fake"
    fake_dir.mkdir()
    script = fake_dir / "fake.py"
    script.write_text(FAKE)
    scenario = fake_dir / "scenario.json"
    monkeypatch.setenv("FAKE_SCENARIO", str(scenario))
    harness = Harness(sys.executable, {"_subcommand": [str(script)]}, lambda profile: {},
                      model_used=lambda launch: "fake-model-1" if launch.status == "delivered" else None)
    # The CLI builds its Analysis on the shared mapping; this test's entry is restored afterwards.
    monkeypatch.setitem(HARNESSES, "pi", harness)

    def set_scenario(**data):
        scenario.write_text(json.dumps(data))

    def begin(**data):
        set_scenario(**data)
        run_dir = start_analysis(prepared.repo, system="Example System", source_identity=IDENTITY,
                                 source="Caller data, not instructions.", source_revision=None,
                                 worker_profile="pi-luna")

        def new_analysis():
            return Analysis(run_dir, timeout=60, max_workers=3, harnesses={"pi": harness},
                            sleep=lambda s: None)
        return run_dir, new_analysis

    begin.set_scenario = set_scenario
    begin.prepared = prepared
    return begin


def events(run_dir: Path) -> list[dict]:
    return [json.loads(line) for line in (run_dir / "log.jsonl").read_text().splitlines()]


def launches(run_dir: Path, job: str | None = None) -> list[dict]:
    return [e for e in events(run_dir) if e["event"] == "launch" and (job is None or e["job"] == job)]


def launch_counts(run_dir: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for e in launches(run_dir):
        counts[e["job"]] = counts.get(e["job"], 0) + 1
    return counts


def complete_members(analysis) -> set[str]:
    return {role.path for role in analysis.layout.roles.values()}


def run(new, raises=None):
    """Run one Analysis under its lock; return the receipt, or the exception when `raises` is given."""
    analysis = new()
    with analysis.run:
        if raises is None:
            return analysis, json.loads(analysis.analyse())
        with pytest.raises(raises) as caught:
            analysis.analyse()
        return analysis, caught.value


def cli(capsys, *argv) -> tuple[int, str, str]:
    capsys.readouterr()
    code = main(list(argv))
    out, err = capsys.readouterr()
    return code, out, err


def test_complete_run_with_one_correction_round(workflow):
    run_dir, new = workflow(disposition="complete",
                            **{"report-verification": [REFUSE_RUNTIME_AND_MEMORY, "none"]})
    analysis, receipt = run(new)
    assert receipt["published"] is True, receipt
    artifact = run_dir / "artifact"
    assert {p.name for p in artifact.iterdir()} == complete_members(analysis) | {"ARTIFACT.yaml"}
    assert "overview.md" in complete_members(analysis)
    manifest = yaml.safe_load((artifact / "ARTIFACT.yaml").read_text())
    assert manifest["worker"]["model"] == "fake-model-1", manifest

    log = events(run_dir)
    verdicts = [e for e in log if e["event"] == "verdict" and e["role"] == "report-verification"]
    assert [v["refused"] for v in verdicts] == [["memory", "runtime"], []], verdicts
    assert [e["event"] for e in log].count("published") == 1
    jobs = [e for e in log if e["event"] == "job"]
    corrections = [e["role"] for e in jobs if e["correcting"]]
    assert corrections == ["runtime", "memory"], corrections
    runtime_launches = [i for i, e in enumerate(log) if e["event"] == "launch" and e["job"] == "runtime"]
    memory_launches = [i for i, e in enumerate(log) if e["event"] == "launch" and e["job"] == "memory"]
    assert len(runtime_launches) == 2 and len(memory_launches) == 2
    assert runtime_launches[1] < memory_launches[1], "runtime's correction precedes memory's"
    counts = launch_counts(run_dir)
    assert counts["epistemic"] == 1 and counts["workflow"] == 1, counts
    reconciliation = launches(run_dir, "reconciliation")
    assert len({e["key"] for e in reconciliation}) == 2, reconciliation
    assert counts["report-verification"] == 2, counts
    assert counts["memory-profile"] == counts["profile-verification"] == 1, counts
    assert counts["synthesis"] == counts["synthesis-verification"] == 1, counts
    correction = (run_dir / "calls" / "launches" / log[memory_launches[1]]["launch"] / "prompt.txt").read_text()
    inputs = correction[correction.index("Inputs (read these exact files):"):]
    assert "- refusal.md:" in inputs and "- previous-report.md:" in inputs, inputs
    assert "refusal = " in correction and "previous-report = " in correction

    status = inspect_analysis(run_dir)
    assert status["state"] == "published" and status["stopped"] is None, status["state"]
    assert status["receipt"]["published"] is True
    assert status["result-disposition"] == "complete"
    assert {job: entry["launches"] for job, entry in status["jobs"].items()} == counts
    answers = [answer for entry in status["jobs"].values() for answer in entry["answers"]]
    assert answers and all(answer["launches"] for answer in answers)
    assert len(status["jobs"]["runtime"]["answers"]) == 2
    assert status["problems"] == []
    assert set(status["members"]) == complete_members(analysis) | {"ARTIFACT.yaml"}


def digests(members) -> dict[str, str]:
    """Member digests; the copy is atomic, so a sibling thread accepting a member cannot change it mid-iteration."""
    return {role: sha256(data).hexdigest() for role, data in dict(members).items()}


class CheckRecorder:
    """Record each `Analysis.candidate` call with its round and the members it was handed; behaviour unchanged.

    A round is the nth call of `Analysis.parallel` or `Analysis.recheck`, as
    `("parallel", n)`; each round's start records the members before it.
    """

    def __init__(self, monkeypatch):
        self.calls: list[dict] = []
        self.rounds = {"parallel": 0, "recheck": 0}
        self.phase = None
        candidate = Analysis.candidate
        recorder = self

        def phased(kind, original):
            def wrapper(self, *args, **kwargs):
                recorder.rounds[kind] += 1
                recorder.phase = (kind, recorder.rounds[kind])
                recorder.calls.append({"phase": recorder.phase, "before": digests(self.members)})
                try:
                    return original(self, *args, **kwargs)
                finally:
                    recorder.phase = None
            return wrapper

        def recording(self, role, data, members=None):
            recorder.calls.append({"phase": recorder.phase, "role": role,
                                   "given": digests(self.members if members is None else members),
                                   "current": digests(self.members)})
            return candidate(self, role, data, members)

        monkeypatch.setattr(Analysis, "candidate", recording)
        monkeypatch.setattr(Analysis, "parallel", phased("parallel", Analysis.parallel))
        monkeypatch.setattr(Analysis, "recheck", phased("recheck", Analysis.recheck))

    def reset(self) -> None:
        self.calls.clear()
        self.rounds.update(parallel=0, recheck=0)

    def started(self, phase) -> dict[str, str]:
        return next(c["before"] for c in self.calls if c["phase"] == phase and "before" in c)

    def checks(self, phase, *roles) -> list[dict]:
        return [c for c in self.calls if c["phase"] == phase and c.get("role") in roles]


def correction_round(workflow, recorder: CheckRecorder, delayed: str):
    """Run with memory and epistemic refused once and `delayed`'s correction slowed; return the evidence."""
    recorder.reset()
    shutil.rmtree(Path(os.environ["FAKE_SCENARIO"]).with_name("counts"), ignore_errors=True)  # fresh call counts
    run_dir, new = workflow(disposition="complete", delay={delayed: 2},
                            **{"report-verification": [REFUSE_MEMORY_AND_EPISTEMIC, "none"]})
    analysis, receipt = run(new)
    assert receipt["published"] is True, receipt
    verdicts = [e["refused"] for e in events(run_dir)
                if e["event"] == "verdict" and e["role"] == "report-verification"]
    assert verdicts == [["epistemic", "memory"], []], verdicts
    return digests(analysis.members), run_dir, receipt


def test_parallel_corrections_are_checked_against_the_round_snapshot(workflow, monkeypatch):
    recorder = CheckRecorder(monkeypatch)
    final, run_dir, receipt = correction_round(workflow, recorder, delayed="epistemic")
    correcting, after = ("parallel", 2), ("recheck", 2)
    before = recorder.started(correcting)
    assert before["memory"] != final["memory"] and before["epistemic"] != final["epistemic"], "both corrected"
    memory, epistemic = recorder.checks(correcting, "memory"), recorder.checks(correcting, "epistemic")
    assert memory and epistemic and recorder.checks(correcting, "workflow", "runtime") == []
    assert all(c["given"]["epistemic"] == before["epistemic"] for c in memory), \
        "memory's correction is checked against epistemic's pre-round version"
    assert all(c["given"]["memory"] == before["memory"] for c in epistemic), \
        "epistemic's correction is checked against memory's pre-round version"
    assert all(c["current"]["memory"] == final["memory"] for c in epistemic), \
        "memory's correction was already accepted when epistemic's check ran"
    rechecks = recorder.checks(after, "memory", "epistemic")
    assert {c["role"] for c in rechecks} == {"memory", "epistemic"}, rechecks
    assert all((c["given"]["memory"], c["given"]["epistemic"]) == (final["memory"], final["epistemic"])
               for c in rechecks), "the collective re-check sees both new versions"
    counts = launch_counts(run_dir)
    assert counts["memory"] == counts["epistemic"] == 2 and counts["workflow"] == 1, counts

    # The other completion order spends the same attempts and publishes the same members.
    swapped_final, swapped_dir, swapped = correction_round(workflow, recorder, delayed="memory")
    assert all(c["current"]["epistemic"] == swapped_final["epistemic"]
               for c in recorder.checks(correcting, "memory")), "epistemic's correction was accepted first"
    assert launch_counts(swapped_dir) == counts
    assert list(swapped["members"]) == list(receipt["members"])


def test_construction_writes_the_type_manifest_that_publication_replaces(workflow):
    run_dir, new = workflow(disposition="complete")
    manifest = run_dir / "artifact" / "ARTIFACT.yaml"
    with new().run:      # construction holds the run's lock; release it before the run
        assert yaml.safe_load(manifest.read_text()) == {
            "type": "agentic-system-analyses/types/agentic-system-analysis-set.md"}
        assert not (run_dir / "log.jsonl").exists() or launches(run_dir) == []

    analysis, receipt = run(new)
    assert receipt["published"] is True, receipt
    pinned = yaml.safe_load(manifest.read_text())
    assert pinned["type"] == "agentic-system-analyses/types/agentic-system-analysis-set.md"
    assert set(pinned["members"]) == complete_members(analysis), pinned
    for name, entry in pinned["members"].items():
        assert entry["sha256"] == sha256((run_dir / "artifact" / name).read_bytes()).hexdigest(), name


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_non_complete_boundary_publishes_nothing(workflow, disposition):
    run_dir, new = workflow(disposition=disposition)
    _, receipt = run(new)
    assert receipt["published"] is False, receipt
    assert set(launch_counts(run_dir)) == {"boundary"}
    assert {p.name for p in (run_dir / "artifact").iterdir()} == {"boundary.md", "overview.md", "ARTIFACT.yaml"}


def test_exhausted_verifier_budget_stops_before_correcting(workflow):
    run_dir, new = workflow(disposition="complete",
                            **{"report-verification": ["- runtime: reconsider the SRC-1 runtime account."]})
    # The script's own stop: the verifier's budget is spent, not an analyst's (runtime has exactly 3).
    _, stop = run(new, (Stopped, OutOfAttempts))
    assert isinstance(stop, Stopped) and "last attempt" in str(stop), repr(stop)
    log = events(run_dir)
    verdicts = [i for i, e in enumerate(log) if e["event"] == "verdict"]
    assert len(verdicts) == 3, [log[i] for i in verdicts]
    assert all(v["refused"] == ["runtime"] for v in (log[i] for i in verdicts))
    after = [e for e in log[verdicts[-1]:] if e["event"] in ("job", "launch")]
    assert not after, f"asked after the third verdict: {after}"
    assert [e["role"] for e in log if e["event"] == "job" and e["correcting"]] == ["runtime", "runtime"]
    assert not (run_dir / "receipt.json").exists()
    assert "published" not in [e["event"] for e in log]
    assert launch_counts(run_dir)["runtime"] == 3


def test_rerun_resumes_from_the_cache(workflow):
    run_dir, new = workflow(disposition="complete", problem={"synthesis": [1]})
    _, stop = run(new, Problem)
    assert stop.role == "synthesis"
    before = launch_counts(run_dir)
    assert before["synthesis"] == 1 and "synthesis-verification" not in before
    workflow.set_scenario(disposition="complete")
    status = inspect_analysis(run_dir)
    assert [problem["job"] for problem in status["problems"]] == ["synthesis"]
    answers = status["jobs"]["synthesis"]["answers"]
    assert len(answers) == 1 and answers[0]["problem"]
    assert [call["call"] for call in dismiss(run_dir, "synthesis")] == [answers[0]["call"]]
    _, receipt = run(new)
    assert receipt["published"] is True, receipt
    after = launch_counts(run_dir)
    assert {job: n for job, n in after.items() if job not in ("synthesis", "synthesis-verification")} == \
        {job: n for job, n in before.items() if job != "synthesis"}, (before, after)
    assert after["synthesis"] == 2 and after["synthesis-verification"] == 1


def test_run_command_refuses_a_held_run(workflow, capsys):
    run_dir, _ = workflow(disposition="complete")
    with run_lock(run_dir):
        code, _, err = cli(capsys, "run", str(run_dir))
    assert code == 1
    assert "another process runs this analysis" in err, err
    assert not (run_dir / "log.jsonl").exists(), "the refused run wrote no records"


def test_run_command_stops_then_resumes_after_a_retry(workflow, capsys):
    run_dir, _ = workflow(disposition="complete", problem={"synthesis": [1]})
    code, _, err = cli(capsys, "run", str(run_dir))
    assert code == 2, err
    assert "synthesis reported a problem" in err, err

    status = inspect_analysis(run_dir)
    assert status["state"] == "stopped", status["state"]
    assert "synthesis" in status["stopped"], status["stopped"]
    assert status["receipt"] is None
    assert [problem["job"] for problem in status["problems"]] == ["synthesis"]
    (answer,) = status["jobs"]["synthesis"]["answers"]
    assert answer["problem"]

    code, out, _ = cli(capsys, "inspect", str(run_dir))
    assert code == 0 and json.loads(out)["state"] == "stopped"

    # A retry is dismissing the recorded problem and rerunning.
    workflow.set_scenario(disposition="complete")
    code, _, err = cli(capsys, "retry", str(run_dir), "synthesis")
    assert code == 0, err
    code, out, err = cli(capsys, "run", str(run_dir))
    assert code == 0, err
    first, _, rest = out.partition("\n")
    assert first == f"run: {run_dir}"
    receipt = json.loads(rest)
    assert receipt["published"] is True, receipt
    assert receipt == json.loads((run_dir / "receipt.json").read_text())

    code, out, _ = cli(capsys, "inspect", str(run_dir))
    assert code == 0 and json.loads(out)["state"] == "published"


def link_to_origin(prepared, monkeypatch) -> Path:
    """Turn the prepared checkout into a linked worktree of an origin on clean `main`, as `prepare` leaves it."""
    origin = prepared.repo.with_name("origin")
    prepared.repo.rename(origin)
    git(origin, "branch", "-M", "main")
    git(origin, "worktree", "add", "--quiet", "--detach", str(prepared.repo), prepared.commit)
    prepared.record(origin=str(origin))
    monkeypatch.chdir(prepared.repo)                   # the old cwd moved with the rename
    assert git(origin, "status", "--porcelain", "--untracked-files=all") == ""
    return origin


def test_integrate_merges_a_published_run_into_main(workflow, monkeypatch, capsys):
    origin = link_to_origin(workflow.prepared, monkeypatch)
    run_dir, new = workflow(disposition="complete")
    _, receipt = run(new)
    assert receipt["published"] is True, receipt
    destination = Path(receipt["destination"])

    code, out, err = cli(capsys, "integrate", str(run_dir))
    assert code == 0, err
    head = out.strip()
    assert head == git(origin, "rev-parse", "main")
    merged = git(origin, "show", "--name-only", "--format=", f"{head}^2")
    relative = destination.relative_to(workflow.prepared.repo).as_posix()
    assert merged.splitlines() and all(path.startswith(relative + "/") for path in merged.splitlines()), merged
    assert git(origin, "log", "-1", "--format=%s", f"{head}^2") == "Publish analysis result"
    assert f"Run: {run_dir.name}" in git(origin, "log", "-1", "--format=%b", f"{head}^2")
    assert {name: sha256((origin / relative / name).read_bytes()).hexdigest()
            for name in receipt["members"]} == receipt["members"]
    assert git(origin, "status", "--porcelain") == ""


def tree_bytes(directory: Path) -> dict[str, bytes]:
    return {p.relative_to(directory).as_posix(): p.read_bytes() for p in sorted(directory.rglob("*")) if p.is_file()}


def published_run(workflow, capsys) -> tuple[Path, dict]:
    """A run published through the CLI; returns the run directory and its receipt."""
    run_dir, _ = workflow(disposition="complete")
    code, out, err = cli(capsys, "run", str(run_dir))
    assert code == 0, err
    receipt = json.loads(out.partition("\n")[2])
    assert receipt["published"] is True, receipt
    return run_dir, receipt


def test_reset_withdraws_a_publication_and_a_rerun_publishes_again(workflow, monkeypatch, capsys):
    link_to_origin(workflow.prepared, monkeypatch)
    run_dir, receipt = published_run(workflow, capsys)
    destination = Path(receipt["destination"])
    published = tree_bytes(destination)

    code, out, err = cli(capsys, "reset", str(run_dir))
    assert code == 0, err
    report = json.loads(out)
    assert report["state"] == "established", report
    assert not destination.exists()
    evidence = Path(report["evidence"])
    assert evidence.parent == run_dir / "withdrawn"
    assert tree_bytes(evidence / destination.name) == published
    assert (evidence / "publish.json").is_file()
    assert not (run_dir / "effects" / "publish.json").exists()
    assert not (run_dir / "receipt.json").exists()
    assert inspect_analysis(run_dir)["state"] == "withdrawn"

    before = launch_counts(run_dir)
    code, out, err = cli(capsys, "run", str(run_dir))
    assert code == 0, err
    again = json.loads(out.partition("\n")[2])
    # Byte for byte, overview and manifest included: members are listed in the layout's order, not the
    # order the workers finished in.
    assert again["published"] is True and again["members"] == receipt["members"], again
    assert {name: sha256((destination / name).read_bytes()).hexdigest()
            for name in again["members"]} == again["members"]
    assert launch_counts(run_dir) == before, "the rerun launched no worker"
    assert inspect_analysis(run_dir)["state"] == "published"


def test_reset_restores_the_incumbent(workflow, monkeypatch, capsys):
    link_to_origin(workflow.prepared, monkeypatch)
    first, receipt = published_run(workflow, capsys)
    destination = Path(receipt["destination"])
    incumbent = tree_bytes(destination)
    # The first publication stays uncommitted: retained and archive locations may be dirty.
    second, second_receipt = published_run(workflow, capsys)
    assert Path(second_receipt["destination"]) == destination
    archive = workflow.prepared.repo / "kb/agentic-system-analyses/retained-archive" / first.name
    assert tree_bytes(archive) == incumbent
    assert tree_bytes(destination) != incumbent

    code, out, err = cli(capsys, "reset", str(second))
    assert code == 0, err
    assert json.loads(out)["state"] == "established"
    assert tree_bytes(destination) == incumbent
    assert not archive.exists()
    assert inspect_analysis(second)["state"] == "withdrawn"


@pytest.mark.parametrize("scenario", ["local", "never-published"])
def test_reset_refuses_when_nothing_was_published(workflow, monkeypatch, capsys, scenario):
    link_to_origin(workflow.prepared, monkeypatch)
    if scenario == "local":
        run_dir, _ = workflow(disposition="blocked")
        code, _, err = cli(capsys, "run", str(run_dir))
        assert code == 0, err
    else:
        run_dir, _ = workflow(disposition="complete", problem={"synthesis": [1]})
        code, _, err = cli(capsys, "run", str(run_dir))
        assert code == 2, err
    receipt = (run_dir / "receipt.json").read_bytes() if scenario == "local" else None
    assert scenario == "local" or not (run_dir / "receipt.json").exists()

    code, _, err = cli(capsys, "reset", str(run_dir))
    assert code == 1
    assert "nothing to withdraw" in err, err
    if receipt is not None:
        assert (run_dir / "receipt.json").read_bytes() == receipt
    assert "withdrawn" not in [e["event"] for e in events(run_dir)]


def test_second_reset_finishes_an_interrupted_withdrawal(workflow, monkeypatch, capsys):
    link_to_origin(workflow.prepared, monkeypatch)
    run_dir, receipt = published_run(workflow, capsys)
    destination = Path(receipt["destination"])
    journal = run_dir / "effects" / "publish.json"
    # What `withdraw_publication` leaves when it crashes after its first move (no incumbent, no archive).
    record = json.loads(journal.read_text())
    assert record["archive"] is None
    journal.write_text(json.dumps({**record, "state": "withdrawing"}))
    evidence = run_dir / "withdrawn" / "20260101T000000Z-crash0"
    evidence.mkdir(parents=True)
    destination.rename(evidence / destination.name)

    code, _, err = cli(capsys, "run", str(run_dir))
    assert code == 2, err
    assert "cannot establish publication outcome" in err, err
    assert journal.is_file() and not destination.exists()

    code, out, err = cli(capsys, "reset", str(run_dir))
    assert code == 0, err
    assert json.loads(out)["state"] == "rolled-back"
    assert not journal.exists()
    assert inspect_analysis(run_dir)["state"] == "withdrawn"


def test_a_start_without_an_end_is_interrupted(workflow, capsys):
    run_dir, _ = workflow(disposition="complete", problem={"synthesis": [1]})
    code, _, err = cli(capsys, "run", str(run_dir))
    assert code == 2, err
    assert inspect_analysis(run_dir)["state"] == "stopped"
    with (run_dir / "log.jsonl").open("a") as log:
        log.write(json.dumps({"event": "start"}) + "\n")
    status = inspect_analysis(run_dir)
    assert status["state"] == "interrupted" and status["stopped"] is None, status["state"]


def test_a_published_receipt_stands_through_a_later_start_without_an_end(workflow, capsys):
    run_dir, _ = published_run(workflow, capsys)
    with (run_dir / "log.jsonl").open("a") as log:
        log.write(json.dumps({"event": "start"}) + "\n")
    assert inspect_analysis(run_dir)["state"] == "published"


def test_analysis_refuses_an_unusable_worker_profile_before_launching(workflow):
    run_dir, new = workflow(disposition="complete")
    with pytest.raises(ValueError, match="unknown harness 'pi'"):
        Analysis(run_dir, timeout=60, max_workers=3, harnesses={})
    missing = Harness("no-such-command-xyz", {}, lambda profile, d: ({}, None))
    with pytest.raises(ValueError, match="no-such-command-xyz"):
        Analysis(run_dir, timeout=60, max_workers=3, harnesses={"pi": missing})
    profiles = (workflow.prepared.repo / "kb/agentic-system-analyses/instructions/analyse-agentic-system"
                / "worker-profiles.yaml")
    data = yaml.safe_load(profiles.read_text())
    data["profiles"]["pi-luna"]["flags"] = {"approve": False}
    profiles.write_text(yaml.safe_dump(data))
    with pytest.raises(ValueError, match="unattended"):
        new()
    assert not (run_dir / "log.jsonl").exists(), "nothing ran"


def test_run_command_stops_with_2_on_a_guard_refusal(workflow, capsys):
    run_dir, _ = workflow(disposition="complete")
    tracked = workflow.prepared.repo / git(workflow.prepared.repo, "ls-files", "*.md").splitlines()[0]
    tracked.write_text(tracked.read_text() + "\nuncommitted\n")
    code, _, err = cli(capsys, "run", str(run_dir))
    assert code == 2, err
    status = inspect_analysis(run_dir)
    assert status["state"] == "stopped" and "ValueError" in status["stopped"], status["stopped"]
    assert launch_counts(run_dir) == {}
