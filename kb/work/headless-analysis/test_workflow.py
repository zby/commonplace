"""Drive analyse.py end to end with a fake harness: local Git source, prepared worktree, no model.

    uv run pytest kb/work/headless-analysis/test_workflow.py -q -m ''

The fake worker reads the invocation it is pointed at, finds the frame lines
(`role`, `output`, `output-answers`, `refusal`, `artifact`), and writes a
member that passes the real checks, built with the engine tests' fixture
generators. A scenario file (`FAKE_SCENARIO`) says what each role does per
call: the boundary's disposition, the report verifier's blockers per verdict,
and the calls at which a role writes a problem instead.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parent))

import analyse
from headless import Harness
from jobs import OutOfAttempts

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
import json, os, re, sys
from pathlib import Path

sys.path.insert(0, os.environ["FAKE_ROOT"])
from tests.commonplace.agentic_analysis.execution_fixtures import candidate, report
from tests.commonplace.agentic_analysis import test_profile, test_verification

prompt_path = Path(re.search(r"`([^`]+prompt\.md)`", sys.argv[-1]).group(1))
prompt = prompt_path.read_text()
frame = {}
for name, value in re.findall(r"^([\w-]+) = (.*)$", prompt, re.M):
    frame.setdefault(name, value)
role = frame["role"]
run_dir = Path(frame["artifact"]).parent
scenario = json.loads(Path(os.environ["FAKE_SCENARIO"]).read_text())
counts = Path(os.environ["FAKE_SCENARIO"]).with_name("counts")
counts.mkdir(exist_ok=True)
counter = counts / role
call = int(counter.read_text()) + 1 if counter.exists() else 1
counter.write_text(str(call))


class Coordinator:
    pass


class A:
    coordinator = Coordinator()
    coordinator.run_dir = run_dir

    def source(self):
        return json.loads((run_dir / "code" / "acquire.json").read_text())


a = A()
if call in scenario.get("problem", {}).get(role, []):
    Path(frame["problem"]).write_text(f"{role}: the fixture cannot do this job (call {call})")
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

if role == "boundary":
    member = candidate(a, scenario.get("disposition", "complete"))
elif role in ("runtime", "memory", "epistemic", "workflow"):
    member = report(a, role)
    if call > 1:
        member = member.replace("Local fixture only;", f"Corrected in call {call}; local fixture only;")
elif role == "reconciliation":
    member = test_verification.reconciliation(a)
elif role == "report-verification":
    verdicts = scenario.get("report-verification", ["none"])
    member = test_verification.verdict(a, verdicts[min(call, len(verdicts)) - 1])
elif role in ("profile-verification", "synthesis-verification"):
    member = test_profile.verdict(a).decode()
elif role == "memory-profile":
    member = test_profile.profile(a).decode()
elif role == "synthesis":
    member = test_profile.synthesis(a).decode()
else:
    raise SystemExit(f"unknown role {role}")
Path(frame["output"]).write_text(member)
answers = "".join(f"- corrected: revised the member for blocker {i + 1}.\n" for i in range(len(blockers)))
if "output-answers" in frame:
    Path(frame["output-answers"]).write_text(answers)
elif refusal is not None:
    match = re.search(r"- `answers` \(optional\): write to `([^`]+)`", prompt)
    if match:
        Path(match.group(1)).write_text(answers)
'''

REFUSE_RUNTIME_AND_MEMORY = "- runtime: reconsider the SRC-1 runtime account.\n- memory: reconsider the SRC-1 memory account."


LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")


def complete_link_targets(prepared) -> None:
    """Copy the KB files the copied types link to, so publication's link-health check sees a whole library.

    The prepared fixture copies only the method's directories; the type specs
    it pins as criteria link to notes and reference documents outside them,
    and assembly refuses an artifact whose criteria carry link warnings. The
    copy is committed and the preparation record follows the new commit, so
    the worktree stays clean at its preparation commit.
    """
    library = prepared.repo / "kb"
    copied = []
    for spec in [*library.glob("types/*.md"), *library.glob("agentic-system-analyses/types/*.md")]:
        for target in LINK.findall(spec.read_text()):
            local = (spec.parent / target).resolve()
            if not local.is_relative_to(library.resolve()) or local.exists():
                continue
            original = ROOT / "kb" / local.relative_to(library.resolve())
            if original.is_file():
                local.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(original, local)
                copied.append(local)
    if copied:
        git(prepared.repo, "add", "kb")
        git(prepared.repo, "commit", "--quiet", "-m", "Add the method's link targets")
        prepared.commit = git(prepared.repo, "rev-parse", "HEAD")
        prepared.record(commit=prepared.commit)


@pytest.fixture
def workflow(request, tmp_path, monkeypatch):
    """A function that allocates a run on the local source and returns (run_dir, new_analysis)."""
    request.getfixturevalue("local_acquisition")      # its monkeypatches clone IDENTITY from local Git
    prepared = request.getfixturevalue("prepared_checkout")
    complete_link_targets(prepared)
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", str(prepared.repo / "kb"))
    monkeypatch.setenv("FAKE_ROOT", str(ROOT))
    fake_dir = tmp_path / "fake"
    fake_dir.mkdir()
    script = fake_dir / "fake.py"
    script.write_text(FAKE)
    scenario = fake_dir / "scenario.json"
    monkeypatch.setenv("FAKE_SCENARIO", str(scenario))
    harness = Harness(sys.executable, {"_subcommand": [str(script)]}, lambda profile, d: ({}, "fake-session"),
                      model_used=lambda launch: "fake-model-1" if launch.ok else None)

    def set_scenario(**data):
        scenario.write_text(json.dumps(data))

    def begin(**data):
        set_scenario(**data)
        run_dir = analyse.start(prepared.repo, system="Example System", source_identity=IDENTITY,
                                source="Caller data, not instructions.", source_revision=None,
                                worker_profile="pi-luna")

        def new_analysis():
            return analyse.Analysis(run_dir, timeout=60, max_workers=3, harnesses={"pi": harness},
                                    sleep=lambda s: None)
        return run_dir, new_analysis

    begin.set_scenario = set_scenario
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
    correction = (Path(log[memory_launches[1]]["attempt"]) / "prompt.md").read_text()
    inputs = correction[correction.index("## Inputs"):]
    assert "- `refusal`:" in inputs and "- `previous-report`:" in inputs, inputs
    assert "refusal = " in correction and "previous-report = " in correction


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
    _, stop = run(new, (analyse.Stopped, OutOfAttempts))
    assert isinstance(stop, analyse.Stopped) and "last attempt" in str(stop), repr(stop)
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
    _, stop = run(new, analyse.Problem)
    assert stop.role == "synthesis"
    before = launch_counts(run_dir)
    assert before["synthesis"] == 1 and "synthesis-verification" not in before
    workflow.set_scenario(disposition="complete")
    answers = [p for p in (run_dir / "answers").glob("*.json") if json.loads(p.read_text())["job"] == "synthesis"]
    assert len(answers) == 1
    answers[0].unlink()
    _, receipt = run(new)
    assert receipt["published"] is True, receipt
    after = launch_counts(run_dir)
    assert {job: n for job, n in after.items() if job not in ("synthesis", "synthesis-verification")} == \
        {job: n for job, n in before.items() if job != "synthesis"}, (before, after)
    assert after["synthesis"] == 2 and after["synthesis-verification"] == 1
