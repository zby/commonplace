"""The gate sweep and `commonplace-review` end to end on a fake harness; no model is called.

The fake worker reads the frame it is pointed at, logs `<note>::<criterion>`
per launch (criteria comma-separated for a bundle call), and writes each
review output with a result line that follows the contract the prompt asks for. Words in the note's text choose its behaviour: FAILME gives
FAIL, MALFORMED omits the result line until the prompt carries a rejection,
CANNOT writes the problem file, and STRAY also writes a file in the checkout.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import Harness
from commonplace.lib import library
from commonplace.lib.review_workflows import inbound, observations
from commonplace.lib.review_workflows.results import read_result, result_path
from tests.commonplace.review_workflows.result_helpers import FAKE_RESULT, copy_contract

FAKE = FAKE_RESULT + r"""
import json, os, re, sys
from pathlib import Path
frame = Path(re.search(r"`([^`]+prompt\.txt)`", sys.argv[-1]).group(1)).read_text()
def listed(name):
    return re.search(rf"^- {re.escape(name)}: (.+)$", frame, re.MULTILINE).group(1)
note = Path(listed("note.md")).read_text()
criteria = re.findall(r"The criterion is `([^`]+)`|^- `([^`]+)`: its text is", frame, re.MULTILINE)
pair = re.search(r"The note is `([^`]+)`", frame).group(1) + "::" + ",".join(a or b for a, b in criteria)
with open(os.environ["FAKE_LOG"], "a") as log:
    log.write(pair + "\n")
if "CANNOT" in note:
    problem = frame.split("problem file:\n")[1].splitlines()[0]
    Path(problem).write_text(json.dumps({"kind": "unable", "message": "the note is unreadable"}))
    sys.exit(0)
if "STRAY" in note:
    Path("stray.md").write_text("written by a reviewer\n")
if "MALFORMED" in note and "was rejected" not in frame:
    result = "Verdict: fine"
elif "outcome: report" in frame:
    result = review_text("report", pair)
else:
    result = review_text("fail" if "FAILME" in note else "pass")
for review in re.findall(r"^- (review[^:]*\.md): ", frame, re.MULTILINE):
    Path(listed(review)).write_text(result, encoding="utf-8", newline="\n")
"""

PROFILES = """workflows: {review: {default: fake, harnesses: {fake: {}, claude-code: {}}}}
profiles:
  fake: {harness: fake, launch-model: m, effort: low}
"""


def gate(name: str, watches: str) -> str:
    return (f"---\ngate_id: prose/{name}\ntype: types/review-gate.md\nwatches: [{watches}]\n"
            f"staleness: changed\n---\n\n## Failure mode\n\n{name} fails.\n")


def note(title: str, body: str, description: str = "A note") -> str:
    return f"---\ndescription: {description}\ntype: types/note.md\n---\n\n# {title}\n\n{body}\n"


FILES = {
    "kb/instructions/worker-profiles.yaml": PROFILES,
    "kb/instructions/review-gates/prose/body-gate.md": gate("body-gate", "body"),
    "kb/instructions/review-gates/prose/description-gate.md": gate("description-gate", "description"),
    "kb/instructions/critique-note.md": "# Critique\n\nWrite a critique.\n",
    "kb/types/note.md": "# Note type\n\nWrite one claim.\n",
    "kb/notes/COLLECTION.md": "# Notes\n\nOne claim per note.\n",
    "kb/workflow-state/COLLECTION.md": "---\ntype: types/collection-contract.md\nunquoted-source-limit: 0\n---\n\n# Reports\n\nRetained operational evidence.\n",
    "kb/notes/alpha.md": note("Alpha", "Alpha body."),
    "kb/notes/beta.md": note("Beta", "Beta body FAILME."),
}
GATE_DIR = "kb/instructions/review-gates/prose"
BODY_GATE = f"{GATE_DIR}/body-gate.md"
DESCRIPTION_GATE = f"{GATE_DIR}/description-gate.md"


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True).stdout


LIBRARY_FILES = ("kb/instructions/", "kb/types/")


def _project(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, *, installed: bool):
    """A repository with the fake harness. Installed: the library files live outside it, as shared data does."""
    root, lib = tmp_path / "repo", (tmp_path / "share" / "commonplace" if installed else tmp_path / "repo" / "kb")
    for rel, text in FILES.items():
        target = lib / rel.removeprefix("kb/") if installed and rel.startswith(LIBRARY_FILES) else root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")
    copy_contract(lib)
    git(root, "init", "-q")
    git(root, "config", "user.email", "t@example.com")
    git(root, "config", "user.name", "t")
    git(root, "add", ".")
    git(root, "commit", "-q", "-m", "seed")
    (root / "other.md").write_text("another session's uncommitted work\n")
    monkeypatch.setattr(library, "_library_root", lambda _override: lib.resolve())
    monkeypatch.chdir(root)
    script, log = tmp_path / "fake.py", tmp_path / "launches.log"
    script.write_text(FAKE)
    log.touch()
    harness = Harness(sys.executable, {"_subcommand": [str(script)], "_env": {"FAKE_LOG": str(log)}},
                      lambda profile: {}, model_used=lambda launch: "fake-model-1")
    return root, {"fake": harness}, log


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    return _project(tmp_path, monkeypatch, installed=False)


@pytest.fixture
def installed(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    return _project(tmp_path, monkeypatch, installed=True)


def review(repo, capsys, *args: str) -> tuple[int, dict, list[str]]:
    """Run `commonplace-review NOTES...`; return the exit code, the report and this run's launches."""
    _, harnesses, log = repo
    before = log.read_text().splitlines()
    code = main([*args, "--timeout", "30"], harnesses=harnesses)
    captured = capsys.readouterr()
    assert captured.out, captured.err
    return code, json.loads(captured.out), log.read_text().splitlines()[len(before):]


def write(root: Path, rel: str, text: str) -> None:
    (root / rel).write_text(text, encoding="utf-8", newline="\n")


@pytest.mark.slow
def test_sweep_writes_one_result_per_pair_and_a_rerun_launches_nothing(repo, capsys):
    root = repo[0]
    code, report, launches = review(repo, capsys, "kb/notes", "--criteria", "prose", "type", "collection",
                                    "critique")
    assert code == 0, report
    # Two notes (COLLECTION.md is not one) x (two gates, type, collection, critique).
    assert len(launches) == len(set(launches)) == 10 and report["counts"] == {"reviewed": 10}
    assert report["guard"] == {"clean": True, "changed": []}
    outcomes = {(pair["note"], pair["criterion"]): pair["outcome"] for pair in report["pairs"]}
    assert outcomes[("kb/notes/beta.md", BODY_GATE)] == "fail"
    assert outcomes[("kb/notes/alpha.md", "kb/types/note.md")] == "pass"
    assert outcomes[("kb/notes/alpha.md", "kb/notes/COLLECTION.md")] == "pass"
    assert outcomes[("kb/notes/alpha.md", "kb/instructions/critique-note.md")] == "report"

    result = read_result(result_path(root, "kb/notes/beta.md", "prose/body-gate"))
    assert (result.outcome, result.model, result.run) == ("fail", "fake-model-1", report["run-dir"])
    assert result.profile == {"harness": "fake", "launch-model": "m", "effort": "low"}
    assert (root / report["run-dir"] / "calls" / "launches" / result.launch).is_dir()
    assert result.findings[0]["level"] == "fail"

    code, again, launches = review(repo, capsys, "kb/notes", "--criteria", "prose", "type", "collection",
                                   "critique")
    assert (code, launches, again["counts"]) == (0, [], {"fresh": 10})
    assert again["run-dir"] != report["run-dir"]


def test_malformed_review_costs_one_corrected_attempt(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "MALFORMED body."))
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0 and launches == [f"kb/notes/alpha.md::{BODY_GATE}"] * 2
    events = [json.loads(line) for line in (root / report["run-dir"] / "log.jsonl").read_text().splitlines()]
    assert [event["problems"] for event in events if event["event"] == "rejected"] == [
        ["review: worker output must declare type: types/review-result.md"]]
    assert read_result(result_path(root, "kb/notes/alpha.md", "prose/body-gate")).outcome == "pass"


def test_worker_problem_leaves_no_result_and_the_other_pairs_complete(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "CANNOT be reviewed."))
    code, report, _ = review(repo, capsys, "kb/notes", "--criteria", "prose/body-gate")
    assert code == 1 and not report["ok"]
    by_note = {pair["note"]: pair for pair in report["pairs"]}
    assert by_note["kb/notes/alpha.md"]["state"] == "problem"
    assert by_note["kb/notes/alpha.md"]["problem"] == "the note is unreadable"
    assert not result_path(root, "kb/notes/alpha.md", "prose/body-gate").exists()
    assert by_note["kb/notes/beta.md"]["state"] == "reviewed"


def test_worker_writing_the_checkout_is_reported_by_the_guard_without_failing_the_run(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "STRAY body."))
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    # The edit of alpha.md happened before the run, so only the worker's file is reported.
    assert code == 0 and report["ok"] and report["guard"] == {"clean": False, "changed": ["stray.md"]}
    assert report["counts"] == {"reviewed": 1}


def test_status_reports_fresh_stale_missing_and_orphaned_results(repo, capsys):
    root, harnesses, _ = repo
    write(root, "kb/notes/gamma.md", note("Gamma", "Gamma body."))
    assert review(repo, capsys, "kb/notes", "--criteria", "prose/body-gate")[0] == 0   # a FAIL is a result
    write(root, "kb/notes/alpha.md", note("Alpha", "Alpha body, edited."))
    write(root, "kb/notes/delta.md", note("Delta", "Delta body."))
    (root / "kb/notes/gamma.md").unlink()
    assert main(["status", "kb/notes", "--criteria", "prose/body-gate", "--json"], harnesses=harnesses) == 0
    status = json.loads(capsys.readouterr().out)
    rows = {row["note"]: (row["freshness"], row["changed"], row["outcome"], row["model"]) for row in status["pairs"]}
    assert rows == {
        "kb/notes/alpha.md": ("stale", ["note"], "pass", "fake-model-1"),
        "kb/notes/beta.md": ("fresh", [], "fail", "fake-model-1"),
        "kb/notes/delta.md": ("missing", [], None, None),
    }
    assert status["orphaned"] == []

    # Only a whole-store query reports results whose target has disappeared.
    assert main(["status", "--json"], harnesses=harnesses) == 0
    stored = json.loads(capsys.readouterr().out)
    assert {row["note"] for row in stored["pairs"]} == {"kb/notes/alpha.md", "kb/notes/beta.md"}
    assert stored["orphaned"] == [
        "kb/workflow-state/data/current/review/results/kb/notes/gamma.md/prose/body-gate.md"]


def test_named_note_status_reads_only_requested_pair_results(repo, capsys, monkeypatch):
    root, harnesses, log = repo
    assert review(repo, capsys, "kb/notes", "--criteria", "prose")[0] == 0
    selected = result_path(root, "kb/notes/alpha.md", "prose/body-gate")
    unselected = {
        result_path(root, "kb/notes/alpha.md", "prose/description-gate"),
        result_path(root, "kb/notes/beta.md", "prose/body-gate"),
        result_path(root, "kb/notes/beta.md", "prose/description-gate"),
    }
    assert selected.is_file() and all(path.is_file() for path in unselected)
    result_root = root / "kb/workflow-state/data/current/review/results"
    reads = []
    read_bytes = Path.read_bytes

    def guarded_read(path):
        if path.is_relative_to(result_root):
            reads.append(path)
            if path in unselected:
                raise PermissionError(f"unselected result is unreadable: {path}")
        return read_bytes(path)

    before = log.read_text()
    monkeypatch.setattr(Path, "read_bytes", guarded_read)
    assert main(["status", "kb/notes/alpha.md", "--criteria", "prose/body-gate", "--json"],
                harnesses=harnesses) == 0
    payload = json.loads(capsys.readouterr().out)
    [row] = payload["pairs"]
    assert (row["note"], row["criterion-id"], row["freshness"], row["outcome"], row["result"]) == (
        "kb/notes/alpha.md", "prose/body-gate", "fresh", "pass", selected.relative_to(root).as_posix())
    assert payload["orphaned"] == []
    assert set(reads) == {selected}
    assert log.read_text() == before


def status_rows(repo, capsys, *args: str) -> list[tuple[str, str, str | None]]:
    _, harnesses, _ = repo
    assert main(["status", *args, "--json"], harnesses=harnesses) == 0
    payload = json.loads(capsys.readouterr().out)
    return [(row["note"], row["freshness"], row["outcome"]) for row in payload["pairs"]]


def test_status_filters_list_current_findings_and_what_a_sweep_would_ask(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/gamma.md", note("Gamma", "Gamma FAILME body."))
    assert review(repo, capsys, "kb/notes", "--criteria", "prose/body-gate")[0] == 0
    write(root, "kb/notes/gamma.md", note("Gamma", "Gamma FAILME body, edited."))      # its fail is stale
    write(root, "kb/notes/delta.md", note("Delta", "Delta body."))                     # never reviewed

    # Without NOTES: every stored result, so a fixer needs no note list to find the current failures.
    assert status_rows(repo, capsys, "--fresh", "--outcome", "fail") == [("kb/notes/beta.md", "fresh", "fail")]
    assert status_rows(repo, capsys, "--outcome", "fail", "--outcome", "pass") == [
        ("kb/notes/alpha.md", "fresh", "pass"), ("kb/notes/beta.md", "fresh", "fail"),
        ("kb/notes/gamma.md", "stale", "fail")]
    assert status_rows(repo, capsys, "--stale") == [("kb/notes/gamma.md", "stale", "fail")]
    # With NOTES, a pair never reviewed is not fresh either.
    assert status_rows(repo, capsys, "kb/notes", "--criteria", "prose/body-gate", "--stale") == [
        ("kb/notes/delta.md", "missing", None), ("kb/notes/gamma.md", "stale", "fail")]

    assert main(["status", "--fresh", "--outcome", "fail", "--json"], harnesses=repo[1]) == 0
    [row] = json.loads(capsys.readouterr().out)["pairs"]
    assert row["criterion-id"] == "prose/body-gate"
    assert read_result(root / row["result"]).findings[0]["level"] == "fail"
    assert main(["status", "--criteria", "prose", "--json"], harnesses=repo[1]) == 2


@pytest.mark.slow
def test_installed_project_reviews_against_library_criteria(installed, capsys):
    root = installed[0]
    lib = library.library_root()
    assert not lib.is_relative_to(root)
    code, report, launches = review(installed, capsys, "kb/notes/beta.md", "--criteria", "prose/body-gate", "type",
                                    "collection", "critique")
    assert code == 0, report
    assert sorted(launches) == sorted(f"kb/notes/beta.md::{criterion}" for criterion in (
        "commonplace:instructions/review-gates/prose/body-gate.md", "commonplace:types/note.md",
        "kb/notes/COLLECTION.md", "commonplace:instructions/critique-note.md"))
    gate = read_result(result_path(root, "kb/notes/beta.md", "prose/body-gate"))
    assert (gate.criterion, gate.outcome) == ("commonplace:instructions/review-gates/prose/body-gate.md", "fail")
    assert result_path(root, "kb/notes/beta.md", "commonplace/types/note").is_file()
    assert result_path(root, "kb/notes/beta.md", "commonplace/instructions/critique-note").is_file()

    (lib / "types/note.md").write_text("# Note type\n\nWrite one claim, sharply.\n", encoding="utf-8")
    assert status_rows(installed, capsys, "--stale") == [("kb/notes/beta.md", "stale", "fail")]
    code, report, launches = review(installed, capsys, "kb/notes/beta.md", "--criteria", "prose/body-gate", "type")
    assert (code, launches) == (0, ["kb/notes/beta.md::commonplace:types/note.md"])
    (lib / "instructions/critique-note.md").unlink()
    assert main(["status", "--json"], harnesses=installed[1]) == 0
    assert json.loads(capsys.readouterr().out)["orphaned"] == [
        "kb/workflow-state/data/current/review/results/kb/notes/beta.md/commonplace/instructions/critique-note.md"]


@pytest.mark.slow
def test_bundle_grouping_writes_one_result_per_gate_from_one_launch(repo, capsys):
    root = repo[0]
    write(root, f"{GATE_DIR}/title-gate.md", gate("title-gate", "title"))
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose", "type",
                                    "--grouping", "bundle")
    assert code == 0, report
    assert sorted(launches) == sorted([f"kb/notes/alpha.md::{BODY_GATE},{DESCRIPTION_GATE},{GATE_DIR}/title-gate.md",
                                       "kb/notes/alpha.md::kb/types/note.md"])
    written = [read_result(result_path(root, "kb/notes/alpha.md", f"prose/{name}"))
               for name in ("body-gate", "description-gate", "title-gate")]
    assert {(result.outcome, result.launch) for result in written} == {("pass", written[0].launch)}

    # An edit of body and description stales two of the three gates: one launch re-asks those two.
    write(root, "kb/notes/alpha.md", note("Alpha", "Alpha body, edited.", description="Alpha restated"))
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose",
                                    "--grouping", "bundle")
    assert (code, launches, report["counts"]) == (0, [f"kb/notes/alpha.md::{BODY_GATE},{DESCRIPTION_GATE}"],
                                                  {"fresh": 1, "reviewed": 2})
    # One stale gate is a pair call, with the pair's own job.
    write(root, "kb/notes/alpha.md", note("Alpha", "Alpha body, edited twice.", description="Alpha restated"))
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose",
                                    "--grouping", "bundle")
    assert (code, launches) == (0, [f"kb/notes/alpha.md::{BODY_GATE}"])
    assert [pair["job"] for pair in report["pairs"] if pair["state"] == "reviewed"] == [
        "kb/notes/alpha.md::prose/body-gate"]


def test_malformed_review_in_a_bundle_reasks_the_bundle(repo, capsys):
    root = repo[0]
    write(root, "kb/notes/alpha.md", note("Alpha", "MALFORMED body."))
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose",
                                    "--grouping", "bundle")
    assert code == 0 and launches == [f"kb/notes/alpha.md::{BODY_GATE},{DESCRIPTION_GATE}"] * 2
    assert report["counts"] == {"reviewed": 2}


def test_a_review_without_criteria_covers_all_gates(repo, capsys) -> None:
    # The same default as `status`: every bundle plus `type` and `collection`, one launch per stale pair.
    _, harnesses, _ = repo
    _, _, launches = review(repo, capsys, "kb/notes")
    assert main(["status", "kb/notes", "--json"], harnesses=harnesses) == 0
    pairs = json.loads(capsys.readouterr().out)["pairs"]
    assert len(launches) == len(pairs) > 1


def compression(name: str) -> str:
    return (f"---\ngate_id: compression/{name}\nname: {name}\ntype: types/review-gate.md\nlens: compression\n"
            f"watches: [body]\nstaleness: changed\n---\n\n## Failure mode\n\n{name} fails.\n")


@pytest.mark.slow
@pytest.mark.parametrize("layout", ["repo"])
def test_compression_check_runs_alone_as_a_fresh_verdict_outside_the_defaults(layout, request, capsys):
    from commonplace.lib.review_workflows import fixtures

    project = request.getfixturevalue(layout)
    root, harnesses, _ = project
    checks = library.library_root() / "instructions/compression-bundle"
    checks.mkdir(parents=True, exist_ok=True)
    for name in ("detail-overhang", "core-claim-obscured"):
        (checks / f"{name}.md").write_text(compression(name), encoding="utf-8")
    prefix = "kb/" if layout == "repo" else "commonplace:"
    identity = f"{prefix}instructions/compression-bundle/detail-overhang.md"
    criterion_id = f"{'kb' if layout == 'repo' else 'commonplace'}/instructions/compression-bundle/detail-overhang"
    requested = ("--criteria", "compression/detail-overhang", "compression/core-claim-obscured")

    # Bundle grouping does not join the checks: each one is its own launch and its own result.
    code, report, launches = review(project, capsys, "kb/notes/alpha.md", *requested, "--grouping", "bundle")
    assert code == 0, report
    assert sorted(launches) == sorted(f"kb/notes/alpha.md::{prefix}instructions/compression-bundle/{name}.md"
                                      for name in ("detail-overhang", "core-claim-obscured"))
    result = read_result(result_path(root, "kb/notes/alpha.md", criterion_id))
    assert (result.criterion, result.contract, result.outcome) == (identity, "verdict", "pass")
    prompt = observations.read_inputs((root / result.observation).parent)["inputs/prompt.txt"].decode()
    assert "INFO as outcome: pass with info findings" in prompt

    # Freshness follows the check's `watches: [body]`.
    assert review(project, capsys, "kb/notes/alpha.md", *requested)[2] == []
    write(root, "kb/notes/alpha.md", note("Alpha", "Alpha body.", description="Alpha restated"))
    assert review(project, capsys, "kb/notes/alpha.md", *requested)[2] == []
    write(root, "kb/notes/alpha.md", note("Alpha", "Alpha body, edited.", description="Alpha restated"))
    assert len(review(project, capsys, "kb/notes/alpha.md", *requested)[2]) == 2

    # Neither the default status set nor a bare `compression` request reaches the checks.
    assert main(["status", "kb/notes/alpha.md", "--json"], harnesses=harnesses) == 0
    assert not any("compression-bundle" in row["criterion"] for row in json.loads(capsys.readouterr().out)["pairs"])
    assert main(["kb/notes/alpha.md", "--criteria", "compression"], harnesses=harnesses) == 2
    assert "one at a time" in capsys.readouterr().err

    if layout == "repo":
        # One retained observation is a fixture baseline, and a trial re-runs that check alone.
        observation = (root / result.observation).parent
        fixture = fixtures.create(root, result.run, observation.name, substitute_executor=True)
        assert main(["--fixture", fixture.relative_to(root).as_posix()], harnesses=harnesses) == 0
        trial = json.loads(capsys.readouterr().out)
        assert [item["state"] for item in trial["observations"]] == ["reviewed"]
        assert trial["observations"][0]["criterion"] == identity


REPORT_FILES = {"friction": "instructions/composition-friction-gate.md",
                "premises": "instructions/premise-decomposition-gate.md",
                "compression-synthesis": "instructions/compression-bundle/high-impact-simplification-synthesis.md"}


@pytest.mark.parametrize("layout", ["installed"])
def test_friction_and_premises_run_alone_as_fresh_reports(layout, request, capsys):
    project = request.getfixturevalue(layout)
    root, harnesses, _ = project
    lib = library.library_root()
    for rel in REPORT_FILES.values():
        (lib / rel).parent.mkdir(parents=True, exist_ok=True)
        (lib / rel).write_text("# Method\n\nReport.\n", encoding="utf-8")
    prefix = "kb" if layout == "repo" else "commonplace"
    code, report, launches = review(project, capsys, "kb/notes/alpha.md", "--criteria", "friction", "premises")
    assert code == 0, report
    assert len(launches) == 2 and {pair["outcome"] for pair in report["pairs"]} == {"report"}
    friction = read_result(result_path(root, "kb/notes/alpha.md", f"{prefix}/{REPORT_FILES['friction'][:-3]}"))
    premises = read_result(result_path(root, "kb/notes/alpha.md", f"{prefix}/{REPORT_FILES['premises'][:-3]}"))
    assert (friction.contract, friction.attack_outcome) == ("report", None)
    assert friction.findings[0]["reason"].startswith("THIN") and premises.findings[0]["reason"].startswith("DOUBTFUL")
    prompt = observations.read_inputs((root / friction.observation).parent)["inputs/prompt.txt"].decode()
    assert "No attack-outcome" in prompt and "critique body" not in prompt
    # Their freshness is the ordinary note, criterion and contract freshness.
    assert review(project, capsys, "kb/notes/alpha.md", "--criteria", "friction", "premises")[2] == []
    assert main(["status", "kb/notes/alpha.md", "--json"], harnesses=harnesses) == 0
    assert not any("gate.md" in row["criterion"] and "review-gates" not in row["criterion"]
                   for row in json.loads(capsys.readouterr().out)["pairs"])


def test_synthesis_runs_alone_on_supplied_findings_and_publishes_nothing(repo, capsys):
    root, harnesses, _ = repo
    for rel in REPORT_FILES.values():
        (root / "kb" / rel).parent.mkdir(parents=True, exist_ok=True)
        write(root, f"kb/{rel}", "# Method\n\nReport.\n")
    write(root, "kb/instructions/compression-bundle/detail-overhang.md", compression("detail-overhang"))
    assert review(repo, capsys, "kb/notes/alpha.md", "--criteria", "compression/detail-overhang")[0] == 0
    check = result_path(root, "kb/notes/alpha.md", "kb/instructions/compression-bundle/detail-overhang")
    finding = f"detail-overhang={check.relative_to(root).as_posix()}"
    synthesis = "kb/instructions/compression-bundle/high-impact-simplification-synthesis"

    # Refused: without findings, beside another criterion, or over two notes; nothing launches.
    for args, message in ((["kb/notes/alpha.md"], "needs its operational inputs"),
                          (["kb/notes/alpha.md", "--input", finding, "--criteria", "friction"], "runs alone"),
                          (["kb/notes", "--input", finding], "runs alone")):
        before = repo[2].read_text()
        if "--criteria" in args:
            args = [*args, "compression-synthesis"]
        else:
            args = [*args, "--criteria", "compression-synthesis"]
        command = [*args, "--timeout", "30"]
        assert main(command, harnesses=harnesses) == 2
        assert message in capsys.readouterr().err and repo[2].read_text() == before

    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "compression-synthesis",
                                    "--input", finding)
    assert code == 0, report
    assert launches == [f"kb/notes/alpha.md::{synthesis}.md"] and report["pairs"][0]["outcome"] == "report"
    assert not result_path(root, "kb/notes/alpha.md", synthesis).exists()
    [record] = (root / report["run-dir"] / "artifact/reviews").glob("*/observation.json")
    data = json.loads(record.read_text())
    assert [item["origin"] for item in data["inputs"] if item["role"] == "operational"] == [
        check.relative_to(root).as_posix()]
    assert data["completed-results"]
    # Unassessed freshness: a repeat launches again, and status refuses the pair.
    assert len(review(repo, capsys, "kb/notes/alpha.md", "--criteria", "compression-synthesis",
                      "--input", finding)[2]) == 1
    assert main(["status", "kb/notes/alpha.md", "--criteria", "compression-synthesis"], harnesses=harnesses) == 2
    assert "unassessed" in capsys.readouterr().err


def test_role_report_runs_alone_on_collected_or_supplied_inbound_contexts(repo, capsys):
    root, harnesses, _ = repo
    role = "kb/instructions/role-in-the-kb-gate.md"
    write(root, role, "# Role\n\nReport the role.\n")
    write(root, "kb/instructions/composition-friction-gate.md", "# Method\n\nReport.\n")
    write(root, "kb/notes/gamma.md", note("Gamma", "- [Alpha](./alpha.md) supplies the term.\n- Other item."))
    (root / "kb/work").mkdir()
    write(root, "kb/work/draft.md", note("Draft", "See [Alpha](../notes/alpha.md)."))

    def observation(report) -> dict:
        [record] = (root / report["run-dir"] / "artifact/reviews").glob("*/observation.json")
        return json.loads(record.read_text())

    # Without --input, the command collects the inbound contexts; nothing is published.
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "role")
    assert code == 0, report
    assert launches == [f"kb/notes/alpha.md::{role}"] and report["pairs"][0]["outcome"] == "report"
    assert not result_path(root, "kb/notes/alpha.md", role[:-3]).exists()
    [given] = [item for item in observation(report)["inputs"] if item["role"] == "operational"]
    assert given["origin"] == inbound.ORIGIN and given["path"] == "inputs/operational/inbound.md"
    directory = root / report["run-dir"] / "artifact/reviews" / observation(report)["id"]
    text = observations.read_inputs(directory)[given["path"]].decode()
    assert "kb/notes/gamma.md" in text and "supplies the term" in text
    assert "Other item" not in text and "kb/work/draft.md" not in text

    # A supplied file replaces the collection; a repeat launches again.
    write(root, "inbound.md", "# Inbound\n\nNothing links here.\n")
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "role",
                                    "--input", "inbound=inbound.md")
    assert code == 0 and len(launches) == 1
    assert [item["origin"] for item in observation(report)["inputs"] if item["role"] == "operational"] == ["inbound.md"]

    # Refused: another role name, beside another criterion; status refuses it.
    for args, message in ((["--criteria", "role", "--input", "other=inbound.md"], "--input inbound=PATH"),
                          (["--criteria", "role", "friction"], "runs alone")):
        before = repo[2].read_text()
        assert main(["kb/notes/alpha.md", *args, "--timeout", "30"], harnesses=harnesses) == 2
        assert message in capsys.readouterr().err and repo[2].read_text() == before
    assert main(["status", "kb/notes/alpha.md", "--criteria", "role"], harnesses=harnesses) == 2
    assert "role has no current result" in capsys.readouterr().err
