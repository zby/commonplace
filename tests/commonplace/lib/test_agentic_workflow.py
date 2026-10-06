"""The analyse-agentic-system workflow definition, driven by scripted workers.

No model runs here. `ScriptedAgent` plays the agent orchestrator: for each job
the definition hands out, a scripted worker writes the file a sub-agent would.
The run lives in a temporary repository whose analysis set validates and
publishes, built from the fixtures of `test_agentic_analysis.py`.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from collections.abc import Callable
from functools import partial
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.lib import agentic_publication, agentic_set, validation
from commonplace.lib.agentic_set import normalize_source_identity
from commonplace.lib.agentic_workflow import (
    READ_BATCH_BYTES,
    AnalyseAgenticSystem,
    blockers_refusals,
    boundary_refusals,
    reading_batches,
)
from commonplace.workflow import (
    Blocked,
    Done,
    Handout,
    Launch,
    Orchestrator,
    Recognition,
    Uncertain,
)
from commonplace.workflow.engine import render_prompt
from tests.commonplace.lib.test_agentic_analysis import (
    REPO_ROOT,
    RETAINED_OVERVIEW,
    RUN_ID,
    SOURCE,
    STATE_DIR,
    commit_inputs,
    commit_paths,
    configure_types,
    epistemic_text,
    git_checkout,
    memory_report_fixture,
    profile_report_fixture,
    reconciliation_text,
    retained_fixture_paths,
    run_git,
    runtime_text,
)
from tests.commonplace.workflow.definitions import ScriptedAgent

pytestmark = pytest.mark.usefixtures("tmp_library")

SYSTEM = "Example System"
DESCRIPTION = "Example System keeps fixture memory in one store and reads it back by route."
BLOCKER = "- reconciliation: RT-RTE-model-call has an unresolved scope in the reconciled records."
REVIEW_PATH = "kb/agentic-system-analyses/retained/example-system/overview.md"
# Its checkout is the fixture's related-systems/example--system.
GITHUB = "https://github.com/example/system"
INSTRUCTIONS = (
    "kb/agentic-system-analyses/instructions/analyse-agentic-system",
)

Worker = Callable[[Handout], None]
ZERO = {"runtime": 0, "memory": 0, "epistemic": 0}


@pytest.fixture(autouse=True)
def running_package_is_the_fixture_repository(tmp_path, monkeypatch):
    """The run pins inputs-commit in its own repository, not this checkout."""
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: tmp_path)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def frontmatter(path: Path) -> dict:
    document, error = validation.parse_document(path.read_text(encoding="utf-8"))
    assert error is None and document is not None
    return dict(document.frontmatter or {})


class Fixture:
    """A temporary repository with a frozen source and an empty run directory."""

    def __init__(self, root: Path) -> None:
        configure_types(root)
        for relative in INSTRUCTIONS:
            source, target = REPO_ROOT / relative, root / relative
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
        self.root = root
        self.source_root, self.revision = git_checkout(
            root / "related-systems/example--system"
        )
        self.head = commit_inputs(root)
        self.run_dir = root / STATE_DIR / RUN_ID
        self.run_dir.mkdir(parents=True)
        self.scratch = root.parent / f"{root.name}-scratch"
        self.identity = SOURCE

    @property
    def public_path(self) -> Path:
        return self.root / agentic_set.RETAINED_ROOT / agentic_set.source_slug(self.identity, SYSTEM) / "overview.md"

    def params(self) -> dict[str, str]:
        return {"system": SYSTEM, "source-identity": self.identity, "source": SOURCE,
                "model": "fixture-model", "effort": "high"}

    # What each scripted worker writes

    def on_github(self) -> None:
        """Name the source by a GitHub identity whose checkout is a clone of a
        local upstream, so code freezes it before the boundary job."""
        self.identity = GITHUB
        self.upstream = self.scratch / "upstream"
        self.upstream.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(self.source_root, self.upstream)
        run_git(self.root, "clone", "--quiet", str(self.upstream), str(self.source_root))

    def advance_upstream(self) -> str:
        """Commit a new file upstream, leaving the quoted README unchanged."""
        (self.upstream / "NOTES.md").write_text("Newer notes.\n", encoding="utf-8")
        return commit_paths(self.upstream, "Advance the upstream", "NOTES.md")

    def boundary(self, disposition: str = "complete", **changes) -> str:
        identity = {
            "type": "agentic-system-analyses/types/agentic-system-boundary.md",
            "description": "Example System at the frozen fixture boundary, analysed as an enclosing runtime",
            "run-id": RUN_ID,
        }
        if disposition == "complete":
            fields = {
                **identity,
                "result-disposition": "complete",
                "target-class": "enclosing runtime",
                "boundary-kind": "whole-system",
                "reviewed-boundary": self.revision,
                "analysis-cutoff": "2026-09-04",
                "evidence-tier": "code-grounded",
                "source": {
                    "kind": "git",
                    "identity": normalize_source_identity(self.identity),
                    "revision": self.revision,
                    "path": self.source_root.as_posix(),
                    "sha256": None,
                },
            }
            not_reached = ""
        else:
            fields = {
                **identity,
                "result-disposition": disposition,
                "target-class": None,
                "boundary-kind": None,
                "reviewed-boundary": None,
                "analysis-cutoff": None,
                "evidence-tier": None,
                "source": None,
            }
            not_reached = (
                "\n## Not reached\n\nThe target issues no model calls, so no lens "
                "was applied and no conclusion about its runtime is drawn.\n"
            )
        fields.update(changes)
        body = (
            "# Example System boundary\n\n"
            "## Boundary and evidence\n\n"
            f"Fixture boundary at `{self.revision}`.\n\n"
            "## Source register\n\n"
            f"| SRC-1 | git | `{normalize_source_identity(self.identity)}` | `{self.revision}` | implementation "
            "| README.md | `README.md` | none |\n" + not_reached
        )
        return "---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body

    def memory_report(self, round_: int = 0) -> str:
        """The fixture's specialist report, marked with its round."""
        local = memory_report_fixture(self.scratch / "memory", self.revision)
        text = local.read_text(encoding="utf-8").replace(
            SOURCE, normalize_source_identity(self.identity)
        )
        return text + f"\nWritten in round {round_}.\n"

    def memory_profile(self) -> str:
        return profile_report_fixture(self.scratch / "profile", self.revision, version=2).read_text().replace(
            SOURCE, normalize_source_identity(self.identity))

    def reconciliation(self, *, amendment: str = "") -> str:
        return (reconciliation_text(self.revision)
                + (f"\nAmendment: {amendment}\n" if amendment else ""))

    def synthesis(self, *, synthesis: str = "", limitations: str = "None.",
                  description: str = DESCRIPTION) -> str:
        return ("---\ntype: agentic-system-analyses/types/agentic-system-synthesis.md\n"
                f'description: "{description}"\nrun-id: {RUN_ID}\nreviewed-boundary: {self.revision}\n---\n\n'
                "# Example System synthesis\n\n"
                "## Bounded synthesis\n\n"
                "Fixture synthesis over RT-OBJ-store, MEM-OBJ-store, EPI-OBJ-store and RT-RTE-model-call.\n\n"
                + (f"{synthesis}\n\n" if synthesis else "")
                + f"## Limitations\n\n{limitations}\n")

    def verification(self, blockers: str = "none", *, title: str = "Record verification") -> str:
        verifies = {"Record verification": "records", "Profile verification": "profile",
                    "Synthesis verification": "synthesis"}[title]
        return ("---\ntype: agentic-system-analyses/types/agentic-system-verification.md\n"
                f'description: "{title} of Example System at the frozen source boundary"\n'
                f"run-id: {RUN_ID}\nreviewed-boundary: {self.revision}\nverifies: {verifies}\n---\n\n"
                f"# Example System {title.lower()}\n\n## Verification\n\nPassed: every claim checked against "
                f"its records.\n\n## Blockers\n\n{blockers}\n")

    def workers(self, **overrides: Worker) -> dict[str, Worker]:
        def writes(text: Callable[[], str]) -> Worker:
            def worker(handout: Handout) -> None:
                handout.output_path.parent.mkdir(parents=True, exist_ok=True)
                handout.output_path.write_text(text(), encoding="utf-8")

            return worker

        workers = {
            "boundary": writes(self.boundary),
            "runtime-0": writes(lambda: runtime_text(self.revision)),
            "epistemic-0": writes(lambda: epistemic_text(self.revision)),
        }
        workers["memory-0"] = writes(partial(self.memory_report, 0))
        for round_ in range(AnalyseAgenticSystem.correction_rounds + 1):
            workers[f"reconcile-{round_}"] = writes(self.reconciliation)
            workers[f"verify-{round_}"] = writes(self.verification)
            if round_:
                for member in ("runtime", "memory", "epistemic"):
                    workers[f"{member}-{round_}"] = self.corrects(member)
        for round_ in range(AnalyseAgenticSystem.synthesis_correction_rounds + 1):
            workers["synthesize" if round_ == 0 else f"synthesize-{round_}"] = writes(self.synthesis)
            workers["verify-synthesis" if round_ == 0 else f"verify-synthesis-{round_}"] = writes(
                lambda: self.verification(title="Synthesis verification"))
        for round_ in range(AnalyseAgenticSystem.profile_correction_rounds + 1):
            workers["profile" if round_ == 0 else f"profile-{round_}"] = writes(self.memory_profile)
            workers["verify-profile" if round_ == 0 else f"verify-profile-{round_}"] = writes(
                lambda: self.verification(title="Profile verification"))
        workers.update(overrides)
        return workers

    @staticmethod
    def supplied(handout: Handout) -> dict[str, str]:
        """The `key = value` lines of a handed-out invocation."""
        prompt = handout.prompt_path.read_text(encoding="utf-8")
        return dict(re.findall(r"(?m)^([a-z-]+) = (.+)$", prompt.split("\n## Input reading batches", 1)[0]))

    def corrects(
        self, member: str, *, decline: bool = False,
        report: Callable[[Handout, str], str] | None = None,
    ) -> Worker:
        """A correcting analyst: a changed report, or the same one, and one
        answer per blocker addressed to it."""
        def worker(handout: Handout) -> None:
            values = self.supplied(handout)
            blockers = Path(values["requests"]).read_text(encoding="utf-8").split("## Blockers", 1)[1]
            count = len(re.findall(rf"(?m)^- {member}: ", blockers))
            previous = Path(values["previous-report"]).read_text(encoding="utf-8")
            text = previous if decline else previous.rstrip("\n") + f"\n\nCorrected by {handout.name}.\n"
            if report is not None:
                text = report(handout, text)
            handout.output_path.write_text(text, encoding="utf-8")
            verb = "declined" if decline else "corrected"
            Path(values["answers"]).write_text(
                "".join(f"- {verb}: fixture answer {number}.\n" for number in range(count)),
                encoding="utf-8",
            )

        return worker

    def writes(self, text: Callable[[Handout], str]) -> Worker:
        def worker(handout: Handout) -> None:
            handout.output_path.write_text(text(handout), encoding="utf-8")

        return worker


class CountsPublication(AnalyseAgenticSystem):
    """The definition, counting how often publication begins.

    Everything else is the definition's own.
    """

    def __init__(self, params=None) -> None:
        super().__init__(params)
        self.publications = 0

    def publish(self, spec) -> None:
        self.publications += 1
        super().publish(spec)


class LocalOrigin(CountsPublication):
    """Clones and checks origins against the local upstream named by the
    `source` parameter instead of GitHub."""

    def origin(self) -> str:
        return str(self.params["source"])


@pytest.fixture
def fixture(tmp_path: Path) -> Fixture:
    return Fixture(tmp_path)


def agent(
    fixture: Fixture, **workers: Worker
) -> tuple[ScriptedAgent, CountsPublication]:
    definition = CountsPublication(fixture.params())
    orchestrator = Orchestrator(fixture.run_dir, definition)
    return ScriptedAgent(
        orchestrator, fixture.workers(**workers), default=_unscripted
    ), definition


def _unscripted(handout: Handout) -> None:
    raise AssertionError(f"no scripted worker for job {handout.name}")


def prompt_of(result, name: str) -> tuple[int, str]:
    """The attempt and prompt text of one handed-out job."""
    assert isinstance(result, Launch), result
    (handout,) = [job for job in result.jobs if job.name == name]
    return handout.attempt, handout.prompt_path.read_text(encoding="utf-8")


@pytest.mark.slow
def test_job_workspace_does_not_promote_unaccepted_output(fixture: Fixture) -> None:
    scripted, _ = agent(fixture, **{"runtime-0": fixture.writes(lambda _: "invalid runtime\n")})

    first = scripted.round()
    assert isinstance(first, Launch)
    boundary = fixture.run_dir / "boundary.md"
    assert not boundary.exists()
    worker_boundary = fixture.run_dir / "jobs/boundary/boundary.md"
    assert worker_boundary.is_file()

    second = scripted.round()
    assert isinstance(second, Launch)
    assert boundary.read_bytes() == worker_boundary.read_bytes()
    original_boundary = boundary.read_bytes()
    runtime = fixture.run_dir / "output/runtime.md"
    assert not runtime.exists()

    retry = scripted.round()
    assert isinstance(retry, Launch)
    assert [job.name for job in retry.jobs] == ["runtime-0"]
    assert not runtime.exists()
    assert boundary.read_bytes() == original_boundary
    assert retry.jobs[0].output_path.parent == fixture.run_dir / "jobs/runtime-0"
    assert retry.jobs[0].problem_path.parent == fixture.run_dir / "jobs/runtime-0"


# 0. Deriving the repository root


# 1. A complete run


@pytest.mark.slow
def test_complete_run_publishes_and_replays_to_done(fixture: Fixture) -> None:
    scripted, definition = agent(fixture)

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    assert scripted.launched == [
        "boundary",
        "runtime-0",
        "epistemic-0",
        "memory-0",
        "reconcile-0",
        "verify-0",
        "profile",
        "verify-profile",
        "synthesize",
        "verify-synthesis",
    ]
    assert not any(
        name.startswith(("runtime-final", "epistemic-final")) for name in scripted.launched
    )
    assert definition.publications == 1

    for name, canonical in definition.job_destinations.items():
        workspace = fixture.run_dir / "jobs" / name
        assert (workspace / "scratch").is_dir()
        assert (workspace / canonical.name).read_bytes() == canonical.read_bytes()
        assert not canonical.is_relative_to(workspace)
    # Workers write in private job workspaces. The coordinator copies accepted
    # bytes to canonical paths; the published memory member is byte-exact.
    output = fixture.run_dir / "output"
    assert (output / "memory.md").read_bytes() == (
        fixture.run_dir / "memory-report-0.md"
    ).read_bytes()
    assert (output / "runtime.md").read_text(encoding="utf-8") == runtime_text(
        fixture.revision
    )
    assert (output / "epistemic.md").read_text(encoding="utf-8") == epistemic_text(
        fixture.revision
    )
    assert not (fixture.run_dir / "memory-report.md").exists()

    state_path = fixture.run_dir / "run-state.md"
    state = frontmatter(state_path)
    assert state["run-status"] == "complete"
    assert state["result-disposition"] == "complete"
    review = fixture.public_path
    assert state["generated-review"] == {"path": REVIEW_PATH, "sha256": digest(review)}
    candidate = fixture.run_dir / "output/overview.md"
    # Publication preserves the accepted working overview.
    assert candidate.exists()
    assert frontmatter(review)["run-id"] == RUN_ID
    assert state["artifact"]["sha256"] == digest(fixture.run_dir / "output/ARTIFACT.yaml")
    for name, retained in retained_fixture_paths(RUN_ID).items():
        local = fixture.run_dir / ("output/" + name)
        assert (fixture.root / retained).read_bytes() == local.read_bytes(), name
    assert validation.validate_note(state_path, repo_root=fixture.root).fails == []

    overview = frontmatter(fixture.run_dir / "output/overview.md")
    assert overview["inputs-commit"] == fixture.head
    manifest = yaml.safe_load((fixture.run_dir / "output/ARTIFACT.yaml").read_text(encoding="utf-8"))
    assert manifest["worker"] == {"model": "fixture-model", "effort": "high"}
    assert json.loads((fixture.run_dir / "run-metadata.json").read_text())["model"] == "fixture-model"

    before = state_path.read_bytes(), state_path.stat().st_mtime_ns
    assert isinstance(scripted.orchestrator.step(), Done)
    assert (state_path.read_bytes(), state_path.stat().st_mtime_ns) == before
    assert definition.publications == 1
    # Replay renders the candidate again, byte for byte what was published,
    # so the publication effect's recorded inputs still match.
    assert candidate.read_bytes() == review.read_bytes()


@pytest.mark.slow
def test_repairable_publication_block_updates_run_status_and_recovers(fixture: Fixture) -> None:
    class FailsOnce(CountsPublication):
        fail = True

        def publish(self, spec) -> None:
            if self.fail:
                raise ValueError("temporary publication condition")
            super().publish(spec)

    definition = FailsOnce(fixture.params())
    scripted = ScriptedAgent(
        Orchestrator(fixture.run_dir, definition), fixture.workers(), default=_unscripted
    )

    result = scripted.run()[-1]

    assert isinstance(result, Blocked)
    assert result.blocks[0].permitted == "repair"
    state_path = fixture.run_dir / "run-state.md"
    assert frontmatter(state_path)["run-status"] == "blocked"
    assert (
        "Blocked: workflow: ValueError: temporary publication condition"
        in state_path.read_text()
    )
    assert validation.validate_note(state_path, repo_root=fixture.root).fails == []
    scripted.orchestrator.report("stop", text="coordinator stopped")
    assert frontmatter(state_path)["run-status"] == "blocked"

    definition.fail = False
    assert isinstance(scripted.orchestrator.step(), Done)
    assert frontmatter(state_path)["run-status"] == "complete"
    assert fixture.public_path.is_file()


def test_uncertain_effect_updates_run_status(fixture: Fixture) -> None:
    definition = AnalyseAgenticSystem(fixture.params())
    definition.run_id = RUN_ID
    definition.write_run_state(
        fixture.run_dir, {"expected-incumbent-sha256": "absent"}, {}
    )

    definition.record_step_result(
        fixture.run_dir, Uncertain("publish", "completion not established")
    )

    state_path = fixture.run_dir / "run-state.md"
    assert frontmatter(state_path)["run-status"] == "uncertain"
    assert "Uncertain effect publish: completion not established" in state_path.read_text()
    assert validation.validate_note(state_path, repo_root=fixture.root).fails == []


@pytest.mark.slow
@pytest.mark.parametrize(
    ("job_name", "field"),
    [("runtime-0", "run-id"), ("memory-0", "reviewed-boundary")],
)
def test_analyst_identity_is_refused_while_the_member_can_be_repaired(
    fixture: Fixture, job_name: str, field: str,
) -> None:
    original = {
        "runtime-0": lambda: runtime_text(fixture.revision),
        "memory-0": fixture.memory_report,
        "epistemic-0": lambda: epistemic_text(fixture.revision),
    }[job_name]

    def analyst(handout: Handout) -> str:
        text = original()
        if handout.attempt == 1:
            replacement = "AAS-2026-09-04-wrong-system-01" if field == "run-id" else "0" * 40
            text = re.sub(rf"(?m)^{field}:.*$", f'{field}: "{replacement}"', text, count=1)
        return text

    scripted, definition = agent(fixture, **{job_name: fixture.writes(analyst)})
    drive_to(scripted, job_name)
    attempt, prompt = prompt_of(scripted.round(), job_name)
    assert attempt == 2
    assert f"member identity: {field}" in prompt
    assert f"run-id = {RUN_ID}\n" in prompt
    assert "reconcile-0" not in scripted.launched
    assert isinstance(scripted.run()[-1], Done)
    assert definition.publications == 1
    member = fixture.run_dir / "output" / f"{job_name.rsplit('-', 1)[0]}.md"
    assert frontmatter(member)["run-id"] == RUN_ID
    assert frontmatter(member)["reviewed-boundary"] == fixture.revision


@pytest.mark.slow
@pytest.mark.parametrize("source_first", [True])
def test_supersession_index_is_inside_source_register_in_either_boundary_order(
    fixture: Fixture, source_first: bool,
) -> None:
    boundary = fixture.boundary()
    source_heading = "## Source register\n"
    row = next(line for line in boundary.splitlines() if line.startswith("| SRC-1 |"))
    if source_first:
        start = boundary.index("## Boundary and evidence\n")
        middle = boundary.index(source_heading)
        boundary = boundary[:start] + boundary[middle:].rstrip() + "\n\n" + boundary[start:middle]
    amendment = "EPI-OBJ-store is superseded by RT-OBJ-store; both name `README.md` at SRC-1."
    scripted, _ = agent(
        fixture,
        boundary=fixture.writes(lambda _: boundary),
        **{"reconcile-0": fixture.writes(lambda _: fixture.reconciliation(amendment=amendment))},
    )
    assert isinstance(scripted.run()[-1], Done)
    overview = (fixture.run_dir / "output/overview.md").read_text(encoding="utf-8")
    match = re.search(r"(?ms)^## Source register\n(.*?)(?=^## |\Z)", overview)
    assert match is not None
    index = "Amended or superseded records: EPI-OBJ-store; [reconciliation](reconciliation.md)."
    assert overview.count(index) == 1
    assert row in match[1]
    assert match[1].index(row) < match[1].index(index)


# 2. An out-of-scope boundary


@pytest.mark.slow
def test_out_of_scope_boundary_closes_with_an_overview_only_set(
    fixture: Fixture,
) -> None:
    scripted, definition = agent(
        fixture,
        boundary=fixture.writes(lambda _: fixture.boundary("out-of-scope")),
    )

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    assert scripted.launched == ["boundary"]
    assert definition.publications == 0
    output = fixture.run_dir / "output"
    assert sorted(path.name for path in output.iterdir()) == [
        "ARTIFACT.yaml",
        "overview.md",
    ]
    state_path = fixture.run_dir / "run-state.md"
    state = frontmatter(state_path)
    assert state["run-status"] == "complete"
    assert state["result-disposition"] == "out-of-scope"
    assert state["generated-review"] is None
    assert state["artifact"]["sha256"] == digest(output / "ARTIFACT.yaml")
    assert validation.validate_note(state_path, repo_root=fixture.root).fails == []
    assert not (fixture.public_path).exists()
    assert not (fixture.root / agentic_set.RETAINED_ROOT).exists()

    assert isinstance(scripted.orchestrator.step(), Done)


@pytest.mark.slow
def test_synthesis_blockers_correct_public_text_without_reopening_records(fixture: Fixture) -> None:
    blocked = fixture.verification(
        "- MEM-OBJ-store has a record scope gap; state its prevented conclusion in Limitations.",
        title="Synthesis verification",
    )
    corrected = fixture.synthesis(limitations="MEM-OBJ-store has a scope gap; its deployment use is unknown.")
    scripted, _ = agent(fixture, **{
        "verify-synthesis": fixture.writes(lambda _: blocked),
        "synthesize-1": fixture.writes(lambda _: corrected),
    })
    assert isinstance(scripted.run()[-1], Done)
    assert [name for name in scripted.launched if name.startswith("reconcile-")] == ["reconcile-0"]
    assert [name for name in scripted.launched if name.startswith("synthesize")] == ["synthesize", "synthesize-1"]
    prompt = last_prompt(fixture, "synthesize-1")
    assert "previous-synthesis =" in prompt and "synthesis-verification-0.md" in prompt
    assert "MEM-OBJ-store has a scope gap" in (fixture.public_path).read_text()
    assert "### Record verification" in (fixture.run_dir / "output/overview.md").read_text()
    assert "### Synthesis verification" in (fixture.run_dir / "output/overview.md").read_text()


@pytest.mark.slow
def test_last_synthesis_blockers_stop_before_publication(fixture: Fixture) -> None:
    blocked = fixture.verification("- RT-OBJ-store is overstated in the synthesis.", title="Synthesis verification")
    scripted, definition = agent(fixture, **{
        "verify-synthesis": fixture.writes(lambda _: blocked),
        "verify-synthesis-1": fixture.writes(lambda _: blocked),
    })
    outcome = scripted.run()[-1]
    assert isinstance(outcome, Blocked)
    assert "synthesis verification of the last round names blockers" in outcome.blocks[0].reason
    assert definition.publications == 0
    assert not (fixture.public_path).exists()
    assert not (fixture.run_dir / "output/overview.md").exists()


@pytest.mark.slow
def test_synthesis_with_an_undeclared_record_is_refused(fixture: Fixture) -> None:
    bad = fixture.synthesis(synthesis="RT-OBJ-missing proves this result.")
    scripted, _ = agent(fixture, synthesize=fixture.writes(lambda _: bad))
    drive_to(scripted, "synthesize")
    attempt, prompt = prompt_of(scripted.round(), "synthesize")
    assert attempt == 2
    assert "synthesis.md: unresolved record RT-OBJ-missing" in prompt


@pytest.mark.slow
@pytest.mark.parametrize("link", ["../../notes/theory.md"])
def test_synthesis_links_are_repaired_before_the_verifier(
    fixture: Fixture, link: str,
) -> None:
    def synthesize(handout: Handout) -> None:
        if handout.attempt == 1:
            text = fixture.synthesis(synthesis=f"See [theory]({link}).")
        else:
            prompt = handout.prompt_path.read_text(encoding="utf-8")
            preserved = Path(re.search(r"^previous-output = (.+)$", prompt, re.MULTILINE)[1])
            text = preserved.read_text(encoding="utf-8").replace(
                f"[theory]({link})", f"`{link}`",
            )
        handout.output_path.write_text(text, encoding="utf-8")

    scripted, _ = agent(fixture, synthesize=synthesize)
    drive_to(scripted, "synthesize")
    attempt, prompt = prompt_of(scripted.round(), "synthesize")
    assert attempt == 2
    assert "set member link:" in prompt
    assert "verify-synthesis" not in scripted.launched
    assert isinstance(scripted.run()[-1], Done)
    assert scripted.launched.count("verify-synthesis") == 1


# 3. The correction cycle


def record_loop(scripted: ScriptedAgent) -> list[str]:
    """The record loop's jobs in launch order, without the round-0 analysts."""
    return [
        name for name in scripted.launched
        if re.fullmatch(r"(runtime|memory|epistemic|reconcile|verify)-[1-9]|(reconcile|verify)-0", name)
    ]


@pytest.mark.slow
def test_a_blocker_addressed_to_an_analyst_corrects_that_report(fixture: Fixture) -> None:
    blocked = fixture.verification("- epistemic: EPI-OBJ-store overstates its scope at SRC-1.")
    scripted, definition = agent(fixture, **{"verify-0": fixture.writes(lambda _: blocked)})

    assert isinstance(scripted.run()[-1], Done)

    assert record_loop(scripted) == ["reconcile-0", "verify-0", "epistemic-1", "reconcile-1", "verify-1"]
    run = fixture.run_dir
    original = epistemic_text(fixture.revision)
    corrected = (run / "epistemic-report-1.md").read_text(encoding="utf-8")
    # The predecessor stays in the run directory; the output set holds the successor.
    assert (run / "epistemic-report-0.md").read_text(encoding="utf-8") == original
    assert corrected == original.rstrip("\n") + "\n\nCorrected by epistemic-1.\n"
    assert (run / "output/epistemic.md").read_text(encoding="utf-8") == corrected
    assert (run / "output/runtime.md").read_bytes() == (run / "runtime-report-0.md").read_bytes()
    assert not (run / "runtime-report-1.md").exists() and not (run / "memory-report-1.md").exists()
    correction = last_prompt(fixture, "epistemic-1")
    assert "round = correction\n" in correction
    assert "epistemic-report-0.md" in correction and "epistemic-requests-1.md" in correction
    # A correcting analyst reads fragments, not the other reports.
    assert "runtime-report" not in correction and "memory-report" not in correction
    packet = (run / "epistemic-requests-1.md").read_text()
    assert "- epistemic: EPI-OBJ-store overstates its scope at SRC-1." in packet
    assert "## Cited records from other reports\n\nnone" in packet
    assert f"answers = {run}/jobs/epistemic-1/answers.md\n" in correction
    assert (run / "epistemic-answers-1.md").read_text() == "- corrected: fixture answer 0.\n"
    assert "+Corrected by epistemic-1." in (run / "epistemic-changes-1.md").read_text()
    for judge in ("reconcile-1", "verify-1"):
        prompt = last_prompt(fixture, judge)
        assert "epistemic-report-1.md" in prompt and "runtime-report-0.md" in prompt
        assert "epistemic-answers-1.md" in prompt and "epistemic-changes-1.md" in prompt
        assert "round = after-blockers\n" in prompt
    assert "previous-verification =" in last_prompt(fixture, "verify-1")
    # Later jobs and publication receive the versions the last verification judged.
    for later in ("profile", "synthesize"):
        assert f"epistemic = {run}/output/epistemic.md\n" in last_prompt(fixture, later)
    retained = fixture.public_path.parent
    assert (retained / "epistemic.md").read_text(encoding="utf-8") == corrected
    assert sorted(path.name for path in retained.iterdir()) == sorted(
        ["ARTIFACT.yaml", "epistemic.md", "memory.md", "memory-profile.md",
         "overview.md", "reconciliation.md", "runtime.md"])
    assert definition.publications == 1
    # A replay rewrites the current versions in the same order and changes nothing.
    assert isinstance(scripted.orchestrator.step(), Done)
    assert (run / "output/epistemic.md").read_text(encoding="utf-8") == corrected
    assert definition.publications == 1


@pytest.mark.slow
def test_a_runtime_correction_finishes_before_the_reports_that_read_it(fixture: Fixture) -> None:
    blocked = fixture.verification(
        "- memory: MEM-OBJ-store repeats the scope of RT-OBJ-store.\n"
        "- runtime: RT-OBJ-store overstates its scope at SRC-1.\n"
        "  Its Later read-back field says the same.\n"
        "- runtime: RT-RTE-model-call repeats that scope."
    )
    scripted, definition = agent(fixture, **{"verify-0": fixture.writes(lambda _: blocked)})
    drive_to(scripted, "verify-0")

    first = scripted.round()
    assert isinstance(first, Launch) and [job.name for job in first.jobs] == ["runtime-1"]
    second = scripted.round()
    assert isinstance(second, Launch) and [job.name for job in second.jobs] == ["memory-1"]
    assert isinstance(scripted.run()[-1], Done)

    # One verification's blockers are one correction step, whatever it names.
    assert record_loop(scripted) == [
        "reconcile-0", "verify-0", "runtime-1", "memory-1", "reconcile-1", "verify-1"]
    run = fixture.run_dir
    memory = last_prompt(fixture, "memory-1")
    assert f"requests = {run}/memory-requests-1.md\n" in memory
    assert "runtime-report" not in memory and "epistemic-report" not in memory
    # The packet carries the cited runtime record as the runtime analyst just corrected it.
    packet = (run / "memory-requests-1.md").read_text()
    assert "- memory: MEM-OBJ-store repeats the scope of RT-OBJ-store." in packet
    assert "- runtime:" not in packet
    assert "From the runtime report:\n\n#### RT-OBJ-store — " in packet
    assert "Corrected by runtime-1." not in packet  # the cut ends at the next heading
    assert "RT-RTE-model-call" not in packet.split("## Cited records", 1)[1]
    runtime_packet = (run / "runtime-requests-1.md").read_text()
    assert "  Its Later read-back field says the same." in runtime_packet
    assert (run / "runtime-answers-1.md").read_text().count("- corrected:") == 2
    assert (run / "memory-answers-1.md").read_text().count("- corrected:") == 1
    reconcile = last_prompt(fixture, "reconcile-1")
    for name in ("runtime-report-1.md", "memory-report-1.md", "epistemic-report-0.md",
                 "runtime-changes-1.md", "memory-answers-1.md"):
        assert name in reconcile
    assert "epistemic-answers" not in reconcile
    assert definition.publications == 1


@pytest.mark.slow
def test_a_declined_blocker_keeps_the_report_and_delivers_the_reason(fixture: Fixture) -> None:
    blocked = fixture.verification("- epistemic: EPI-OBJ-store overstates its scope at SRC-1.")
    scripted, definition = agent(fixture, **{
        "verify-0": fixture.writes(lambda _: blocked),
        "epistemic-1": fixture.corrects("epistemic", decline=True),
    })

    assert isinstance(scripted.run()[-1], Done)

    run = fixture.run_dir
    assert (run / "epistemic-report-1.md").read_bytes() == (run / "epistemic-report-0.md").read_bytes()
    assert (run / "epistemic-answers-1.md").read_text() == "- declined: fixture answer 0.\n"
    assert "None: `epistemic-report-1.md` is identical" in (run / "epistemic-changes-1.md").read_text()
    assert "epistemic-answers-1.md" in last_prompt(fixture, "verify-1")
    assert definition.publications == 1


@pytest.mark.slow
@pytest.mark.parametrize(("defect", "refusal"), [
    ("dropped-record", "a corrected report keeps every record its predecessor declared, because other reports cite them: EPI-OBJ-store"),
    ("no-answers", "correction answers: write answers.md beside the report"),
    ("wrong-count", "answers.md needs exactly 1 entries"),
    ("unchanged", "an entry says corrected but the report is identical to its predecessor"),
])
def test_a_refused_correction_leaves_the_current_report(
    fixture: Fixture, defect: str, refusal: str,
) -> None:
    valid = fixture.corrects("epistemic")

    def correct(handout: Handout) -> None:
        valid(handout)
        if handout.attempt > 1:
            return
        answers = Path(fixture.supplied(handout)["answers"])
        if defect == "dropped-record":
            handout.output_path.write_text(
                handout.output_path.read_text().replace("EPI-OBJ-store", "EPI-OBJ-shelf"))
        elif defect == "no-answers":
            answers.unlink()
        elif defect == "wrong-count":
            answers.write_text("- corrected: one.\n- declined: two.\n")
        else:
            handout.output_path.write_bytes(
                Path(fixture.supplied(handout)["previous-report"]).read_bytes())

    blocked = fixture.verification("- epistemic: EPI-OBJ-store overstates its scope at SRC-1.")
    scripted, definition = agent(
        fixture, **{"verify-0": fixture.writes(lambda _: blocked), "epistemic-1": correct})
    drive_to(scripted, "epistemic-1")

    attempt, prompt = prompt_of(scripted.round(), "epistemic-1")

    assert attempt == 2
    assert refusal in prompt
    run = fixture.run_dir
    assert not (run / "epistemic-report-1.md").exists()
    assert (run / "output/epistemic.md").read_bytes() == (run / "epistemic-report-0.md").read_bytes()
    assert "reconcile-1" not in scripted.launched
    assert isinstance(scripted.run()[-1], Done)
    assert definition.publications == 1


@pytest.mark.slow
def test_a_blocker_without_an_addressee_is_refused(fixture: Fixture) -> None:
    def verify(handout: Handout) -> str:
        blocker = "RT-RTE-model-call has an unresolved scope."
        return fixture.verification(
            f"- {blocker}\n- memories: {blocker}" if handout.attempt == 1 else f"- runtime: {blocker}")

    scripted, _ = agent(fixture, **{"verify-0": fixture.writes(verify)})
    drive_to(scripted, "verify-0")

    attempt, prompt = prompt_of(scripted.round(), "verify-0")

    assert attempt == 2
    assert prompt.count("blocker addressee: start each blocker with `runtime:`") == 2
    assert "runtime-1" not in scripted.launched
    assert isinstance(scripted.run()[-1], Done)
    assert "runtime-1" in scripted.launched


@pytest.mark.slow
def test_a_value_amendment_in_reconciliation_is_refused(fixture: Fixture) -> None:
    amending = fixture.reconciliation(
        amendment="RT-OBJ-store has a narrower scope; replace the broad scope at SRC-1.")
    scripted, _ = agent(fixture, **{"reconcile-0": fixture.writes(lambda _: amending)})
    drive_to(scripted, "reconcile-0")

    attempt, prompt = prompt_of(scripted.round(), "reconcile-0")

    assert attempt == 2
    assert "value amendment: reconciliation states connections between reports" in prompt
    assert "verify-0" not in scripted.launched


def last_prompt(fixture: Fixture, name: str) -> str:
    """The prompt file of a job's last hand-out."""
    prompts = (fixture.run_dir / "workflow-state").rglob("prompt.md")
    (found,) = [prompt for prompt in prompts if prompt.parent.name == name]
    return found.read_text(encoding="utf-8")


@pytest.mark.slow
def test_split_dispositions_preserve_members_and_publish(fixture: Fixture) -> None:
    """Scripted findings exercise workflow handling, not analyst judgment."""
    amendment = (
        "RT-OBJ-store is superseded by EPI-OBJ-store and EPI-OBJ-input; "
        "the combined finding conflates two parts. Evidence: SRC-1 README.md. "
        "Affected findings: runtime object identity and epistemic objects."
    )
    epistemic = epistemic_text(fixture.revision).replace(
        "Object the epistemic lens established. Evidence: SRC-1.",
        "Part of: RT-OBJ-store\n\nStore part. Evidence: SRC-1.\n\n"
        "#### EPI-OBJ-input — Access-policy part\n\n"
        "Part of: RT-OBJ-store\n\nPolicy part. Evidence: SRC-1.",
    )
    workers = {
        "epistemic-0": fixture.writes(lambda _: epistemic),
        "reconcile-0": fixture.writes(lambda _: fixture.reconciliation(amendment=amendment)),
    }

    scripted, definition = agent(fixture, **workers)
    results = scripted.run()
    assert isinstance(results[-1], Done), results[-1]
    assert definition.publications == 1
    output = fixture.run_dir / "output"
    assert (output / "runtime.md").read_text(encoding="utf-8") == runtime_text(fixture.revision)
    assert (output / "epistemic.md").read_text(encoding="utf-8") == epistemic
    reconciliation = (output / "reconciliation.md").read_text(encoding="utf-8")
    assert "Amendment: " + amendment in reconciliation
    assert record_loop(scripted) == ["reconcile-0", "verify-0"]
    for name, retained in retained_fixture_paths(RUN_ID).items():
        assert (fixture.root / retained).read_bytes() == (output / name).read_bytes()


# 4. Validators refuse


def drive_to(scripted: ScriptedAgent, name: str) -> None:
    """Step until the job is handed out and its scripted worker has written."""
    for _ in range(20):
        result = scripted.round()
        assert isinstance(result, Launch), result
        if any(job.name == name for job in result.jobs):
            return
    raise AssertionError(f"{name} was never handed out")


@pytest.mark.slow
def test_boundary_with_a_wrong_field_set_is_refused(fixture: Fixture) -> None:
    bad = fixture.boundary()
    bad = bad.replace("evidence-tier:", "evidence-level:")
    scripted, _ = agent(fixture, boundary=fixture.writes(lambda _: bad))
    drive_to(scripted, "boundary")

    attempt, prompt = prompt_of(scripted.round(), "boundary")

    assert attempt == 2
    assert "evidence-level" in prompt and "evidence-tier" in prompt
    assert "run-status: running\nresult-disposition: null\nsource: null\n" in (
        fixture.run_dir / "run-state.md"
    ).read_text(encoding="utf-8")


@pytest.mark.parametrize("duplicate", [False, True])
def test_boundary_source_register_checks_unique_ids_across_layers(fixture: Fixture, duplicate: bool) -> None:
    boundary = fixture.boundary()
    row = next(line for line in boundary.splitlines() if line.startswith("| SRC-1 |"))
    if duplicate:
        boundary = boundary.replace(row, row + "\n" + row.replace("| implementation |", "| doctrine/design |"))
    else:
        boundary = boundary.replace("| implementation |", "| implementation; doctrine/design |")
    path = fixture.run_dir / "jobs/boundary/boundary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(boundary, encoding="utf-8")

    refusals = boundary_refusals(path, repo_root=fixture.root, run_id=RUN_ID, identity=SOURCE)

    assert refusals == ([
        ("duplicate source declaration: SRC-1; keep one row per source ID "
         "and separate evidence layers and scopes within that row")
    ] if duplicate else [])


def test_boundary_with_an_unquoted_date_is_refused(fixture: Fixture) -> None:
    path = fixture.run_dir / "jobs/boundary/boundary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        fixture.boundary().replace(
            "analysis-cutoff: '2026-09-04'", "analysis-cutoff: 2026-09-04"
        ),
        encoding="utf-8",
    )
    assert "analysis-cutoff: 2026-09-04\n" in path.read_text(encoding="utf-8")

    assert (
        boundary_refusals(path, repo_root=fixture.root, run_id=RUN_ID, identity=SOURCE)
        != []
    )


@pytest.mark.parametrize("cutoff, valid", [
    ("2026-10-04", True), ("2024-02-29", True),
    ("not-a-date", False), ("2026-02-29", False),
    ("2026-13-01", False), ("2026-10-4", False),
    ("2026-10-04T00:00:00Z", False),
])
def test_boundary_cutoff_uses_the_overview_date_format(fixture: Fixture, cutoff: str, valid: bool) -> None:
    path = fixture.run_dir / "jobs/boundary/boundary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fixture.boundary(**{"analysis-cutoff": cutoff}), encoding="utf-8")

    refusals = boundary_refusals(path, repo_root=fixture.root, run_id=RUN_ID, identity=SOURCE)

    assert refusals == ([] if valid else [f"[schema] frontmatter.analysis-cutoff: '{cutoff}' is not a 'date'"])


@pytest.mark.parametrize("defect", ["missing", "fenced", "quoted", "kind", "identity", "revision", "columns"])
def test_boundary_register_must_declare_the_frozen_source(fixture: Fixture, defect: str) -> None:
    boundary = fixture.boundary()
    row = next(line for line in boundary.splitlines() if line.startswith("| SRC-1 |"))
    cells = [cell.strip() for cell in row.strip("|").split("|")]
    if defect == "missing":
        replacement = "No frozen source declared."
    elif defect == "fenced":
        replacement = "```markdown\n" + row + "\n```"
    elif defect == "quoted":
        replacement = "> " + row
    else:
        if defect == "columns":
            cells = cells[:4]
        else:
            position = {"kind": 1, "identity": 2, "revision": 3}[defect]
            cells[position] = {"kind": "capture", "identity": "`https://example.invalid/other`", "revision": "`" + "0" * 40 + "`"}[defect]
        replacement = "| " + " | ".join(cells) + " |"
    path = fixture.run_dir / "jobs/boundary/boundary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(boundary.replace(row, replacement), encoding="utf-8")

    refusals = boundary_refusals(path, repo_root=fixture.root, run_id=RUN_ID, identity=SOURCE)

    assert any("source register must declare the frozen source" in reason for reason in refusals)
    assert any(f"identity `{SOURCE}`, revision or capture `{fixture.revision}`" in reason for reason in refusals)
    if defect == "columns":
        assert any("needs all eight columns" in reason for reason in refusals)


def test_boundary_register_accepts_a_frozen_capture(fixture: Fixture) -> None:
    capture = fixture.root / "capture.txt"
    capture.write_text("Frozen capture.\n", encoding="utf-8")
    source = {"kind": "capture", "identity": SOURCE, "revision": "capture-1",
              "path": str(capture), "sha256": digest(capture)}
    boundary = fixture.boundary(source=source, **{"reviewed-boundary": "capture-1"})
    row = next(line for line in boundary.splitlines() if line.startswith("| SRC-1 |"))
    replacement = f"| SRC-1 | capture | `{SOURCE}` | `capture-1` | doctrine/design | capture | `{capture}` | none |"
    path = fixture.run_dir / "jobs/boundary/boundary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(boundary.replace(row, replacement), encoding="utf-8")

    assert boundary_refusals(path, repo_root=fixture.root, run_id=RUN_ID, identity=SOURCE) == []


@pytest.mark.slow
def test_reconciliation_superseding_an_undeclared_record_is_refused(fixture: Fixture) -> None:
    dangling = fixture.reconciliation(
        amendment="MEM-OBJ-example9 is superseded by RT-OBJ-store; both name `README.md`."
    )
    scripted, _ = agent(fixture, **{"reconcile-0": fixture.writes(lambda _: dangling)})
    drive_to(scripted, "reconcile-0")

    attempt, prompt = prompt_of(scripted.round(), "reconcile-0")

    assert attempt == 2
    assert "reconciliation.md: unresolved record MEM-OBJ-example9" in prompt


@pytest.mark.slow
def test_verification_relation_prose_is_accepted_without_a_retry(fixture: Fixture) -> None:
    text = fixture.verification().replace(
        "its records.", "its records. Compared EPI-OBJ-store to RT-OBJ-store at SRC-1."
    )
    scripted, _ = agent(fixture, **{"verify-0": fixture.writes(lambda _: text)})
    results = scripted.run()
    assert isinstance(results[-1], Done), results[-1]
    assert scripted.launched.count("verify-0") == 1


@pytest.mark.slow
def test_reconciliation_refuses_prose_line_anchors_at_acceptance(fixture: Fixture) -> None:
    text = fixture.reconciliation() + "\nEvidence: `README.md:1-2`.\n"
    scripted, _ = agent(fixture, **{"reconcile-0": fixture.writes(lambda _: text)})
    drive_to(scripted, "reconcile-0")
    attempt, prompt = prompt_of(scripted.round(), "reconcile-0")
    assert attempt == 2
    assert "source anchor" in prompt and "carries a line range" in prompt
    assert "verify-0" not in scripted.launched


@pytest.mark.slow
def test_reconciliation_preserves_permitted_quote_attributions(fixture: Fixture) -> None:
    # This syntax check preserves quotation exclusions; it does not certify occurrence.
    quote = f"\n> Source text.\n> --- `README.md:1-2` @ `{fixture.revision}`\n"
    text = fixture.reconciliation() + quote
    scripted, _ = agent(fixture, **{"reconcile-0": fixture.writes(lambda _: text)})
    drive_to(scripted, "reconcile-0")
    result = scripted.round()
    assert isinstance(result, Launch)
    assert "reconcile-0" not in [job.name for job in result.jobs]
    assert "verify-0" in scripted.launched


@pytest.mark.slow
def test_reconciliation_superseding_a_lens_record_is_accepted(fixture: Fixture) -> None:
    supersedes = fixture.reconciliation(
        amendment="EPI-OBJ-store is superseded by RT-OBJ-store; both name `README.md` at SRC-1."
    )
    scripted, definition = agent(
        fixture, **{"reconcile-0": fixture.writes(lambda _: supersedes)}
    )

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    overview = (fixture.run_dir / "output/overview.md").read_text(encoding="utf-8")
    assert "Amendment:" not in overview
    assert "Amended or superseded records: EPI-OBJ-store" in overview
    assert "Amendment: EPI-OBJ-store is superseded by RT-OBJ-store" in (
        fixture.run_dir / "output/reconciliation.md").read_text()
    assert definition.publications == 1


@pytest.mark.slow
def test_synthesis_with_a_short_description_is_refused(fixture: Fixture) -> None:
    short = fixture.synthesis(description="Too short.")
    scripted, _ = agent(fixture, synthesize=fixture.writes(lambda _: short))
    drive_to(scripted, "synthesize")

    attempt, prompt = prompt_of(scripted.round(), "synthesize")

    assert attempt == 2
    assert "frontmatter.description: 'Too short.' is too short" in prompt


@pytest.mark.slow
def test_the_description_and_synthesis_become_the_public_review(
    fixture: Fixture,
) -> None:
    linked = fixture.synthesis(
        synthesis=(
            "The route is traced in [the runtime member](./runtime.md#routes), "
            "summarized in [the overview](overview.md), described at "
            "[the project](https://example.invalid/example-system), and limited "
            "under [Limitations](#limitations)."
        )
    )
    scripted, definition = agent(
        fixture, synthesize=fixture.writes(lambda _: linked)
    )

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    assert definition.publications == 1
    overview = fixture.run_dir / "output/overview.md"
    assert frontmatter(overview)["description"] == DESCRIPTION
    review_path = fixture.public_path
    assert frontmatter(review_path)["description"] == DESCRIPTION
    review = review_path.read_text(encoding="utf-8")
    assert review_path.read_bytes() == overview.read_bytes()
    assert frontmatter(review_path)["evidence-tier"] == "code-grounded"
    assert frontmatter(review_path)["analysis-cutoff"] == "2026-09-04"
    assert "Fixture synthesis over RT-OBJ-store, MEM-OBJ-store, EPI-OBJ-store and RT-RTE-model-call." in review
    assert "## Limitations\n\nNone.\n" in review
    assert "[the runtime member](./runtime.md#routes)" in review
    assert "[the overview](overview.md)" in review
    assert "[the project](https://example.invalid/example-system)" in review
    assert "[Limitations](#limitations)" in review
    # Every rewritten link resolves once the set is retained.
    assert validation.validate_note(review_path, repo_root=fixture.root).warns == []


# 5. A named blocker stops before publication


@pytest.mark.slow
def test_a_named_blocker_starts_another_reconciliation_round(fixture: Fixture) -> None:
    blocked = fixture.verification(BLOCKER)
    scripted, definition = agent(
        fixture, **{"verify-0": fixture.writes(lambda _: blocked)}
    )

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    order = [
        name
        for name in scripted.launched
        if name.startswith(("reconcile-", "verify-")) and not name.startswith(("verify-synthesis", "verify-profile"))
    ]
    assert order == [
        "reconcile-0",
        "verify-0",
        "reconcile-1",
        "verify-1",
    ]
    prompt = last_prompt(fixture, "reconcile-1")
    assert "verification-0.md" in prompt and "set-check-0.md" in prompt
    assert "round = after-blockers\n" in prompt
    # A blocker addressed to reconciliation runs no analyst.
    assert record_loop(scripted) == order
    assert "-answers" not in prompt and "-changes" not in prompt
    assert definition.publications == 1
    overview = (fixture.run_dir / "output/overview.md").read_text(encoding="utf-8")
    assert "never traced" not in overview


@pytest.mark.parametrize(
    ("blockers", "accepted"),
    [
        ("none", True),
        ("- RT-RTE-model-call is never traced.", True),
        ("None found", False),
        ("- RT-RTE-model-call is never traced.\nRT-OBJ-store is thin.", False),
    ],
)
def test_blockers_are_none_or_a_list(blockers: str, accepted: bool) -> None:
    assert (blockers_refusals(blockers) == []) is accepted


@pytest.mark.slow
def test_blockers_in_the_last_round_stop_before_publication(fixture: Fixture) -> None:
    blocked = fixture.verification(BLOCKER)
    verifiers = {
        f"verify-{round_}": fixture.writes(lambda _: blocked)
        for round_ in range(AnalyseAgenticSystem.correction_rounds + 1)
    }
    scripted, definition = agent(fixture, **verifiers)

    results = scripted.run()

    result = results[-1]
    assert isinstance(result, Blocked), result
    (block,) = result.blocks
    assert block.subject == "workflow"
    assert "the last round names blockers" in block.reason
    assert block.permitted == "stop"
    assert scripted.launched.count("verify-2") == 1 and "profile" not in scripted.launched
    assert definition.publications == 0
    assert not (fixture.public_path).exists()
    assert frontmatter(fixture.run_dir / "run-state.md")["run-status"] == "stopped"
    assert validation.validate_note(
        fixture.run_dir / "run-state.md", repo_root=fixture.root
    ).fails == []


@pytest.mark.slow
def test_memory_report_re_declaring_a_runtime_record_is_refused(
    fixture: Fixture,
) -> None:
    def redeclared(_: Handout) -> str:
        route = runtime_text(fixture.revision).split("#### RT-RTE-model-call — Fixture route\n\n", 1)[1]
        route = route.split("\n### Claims", 1)[0]
        return fixture.memory_report().replace(
            "#### On RT-RTE-model-call — Fixture route", "#### RT-RTE-model-call — Fixture route"
        ).replace(
            "Seeded route with the specialist's memory fields.", route
        )

    scripted, _ = agent(fixture, **{"memory-0": fixture.writes(redeclared)})
    drive_to(scripted, "memory-0")

    attempt, prompt = prompt_of(scripted.round(), "memory-0")

    assert attempt == 2
    assert "duplicate set declaration: RT-RTE-model-call" in prompt


@pytest.mark.slow
@pytest.mark.parametrize("job", ["runtime-0", "memory-1"])
def test_altered_analyst_quote_is_repaired_before_reconciliation(
    fixture: Fixture, job: str,
) -> None:
    citation = f"> # Frozen source\n> --- `README.md:1-1` @ `{fixture.revision}`\n"
    reports = {
        "runtime-0": lambda: runtime_text(fixture.revision),
        "epistemic-0": lambda: epistemic_text(fixture.revision),
        "memory-0": fixture.memory_report,
        "memory-1": lambda: fixture.memory_report(1),
    }

    def analyst(handout: Handout) -> None:
        if job == "memory-1":
            Path(fixture.supplied(handout)["answers"]).write_text("- corrected: fixture.\n")
        if handout.attempt == 1:
            text = reports[job]() + "\n" + citation.replace("Frozen source", "Frozen call source")
        else:
            prompt = handout.prompt_path.read_text(encoding="utf-8")
            preserved = Path(re.search(r"^previous-output = (.+)$", prompt, re.MULTILINE)[1])
            text = preserved.read_text(encoding="utf-8").replace("Frozen call source", "Frozen source")
            assert text == reports[job]() + "\n" + citation
        handout.output_path.write_text(text, encoding="utf-8")
        # The observed failure passed standing structural validation.
        assert validation.validate_note(handout.output_path, repo_root=fixture.root).fails == []

    workers = {job: analyst}
    if job == "memory-1":
        workers["verify-0"] = fixture.writes(
            lambda _: fixture.verification("- memory: MEM-OBJ-store lacks its write-side anchor."))
    scripted, definition = agent(fixture, **workers)
    drive_to(scripted, job)

    attempt, prompt = prompt_of(scripted.round(), job)

    assert attempt == 2
    assert "quote does not occur in the cited line range" in prompt
    assert "README.md at the recorded commit" in prompt
    assert isinstance(scripted.run()[-1], Done)
    assert scripted.launched.count(job) == 2
    assert [name for name in scripted.launched if name.startswith("reconcile-")] == (
        ["reconcile-0", "reconcile-1"] if job == "memory-1" else ["reconcile-0"]
    )
    assert definition.publications == 1


@pytest.mark.slow
def test_missing_route_field_is_repaired_before_reconciliation(fixture: Fixture) -> None:
    def runtime(handout: Handout) -> None:
        if handout.attempt == 1:
            text = runtime_text(fixture.revision).replace(
                "- Later read-back: A later invocation reads RT-OBJ-store.\n", ""
            )
        else:
            prompt = handout.prompt_path.read_text(encoding="utf-8")
            preserved = Path(re.search(r"^previous-output = (.+)$", prompt, re.MULTILINE)[1])
            assert "- Later read-back:" not in preserved.read_text(encoding="utf-8")
            text = runtime_text(fixture.revision)
        handout.output_path.write_text(text, encoding="utf-8")

    scripted, definition = agent(fixture, **{"runtime-0": runtime})
    drive_to(scripted, "runtime-0")
    attempt, prompt = prompt_of(scripted.round(), "runtime-0")
    assert attempt == 2
    assert "RT-RTE-model-call: Later read-back: missing field" in prompt
    assert isinstance(scripted.run()[-1], Done)
    assert scripted.launched.count("runtime-0") == 2
    assert scripted.launched.count("reconcile-0") == 1
    assert definition.publications == 1


@pytest.mark.slow
@pytest.mark.parametrize("prefix", ["", "MEM-"])
def test_runtime_declaration_prefix_is_repaired_before_specialists(
    fixture: Fixture, prefix: str,
) -> None:
    valid = runtime_text(fixture.revision)
    invalid = valid.replace("RT-", prefix)

    def runtime(handout: Handout) -> None:
        if handout.attempt == 1:
            text = invalid
        else:
            prompt = handout.prompt_path.read_text(encoding="utf-8")
            preserved = Path(re.search(r"^previous-output = (.+)$", prompt, re.MULTILINE)[1])
            assert preserved.read_text(encoding="utf-8") == invalid
            text = valid
        handout.output_path.write_text(text, encoding="utf-8")

    scripted, definition = agent(fixture, **{"runtime-0": runtime})
    drive_to(scripted, "runtime-0")
    attempt, prompt = prompt_of(scripted.round(), "runtime-0")
    assert attempt == 2
    expected = (
        "declarations without an analyst prefix" if prefix == ""
        else "record declarations: this analyst must use RT-:"
    )
    assert expected in prompt
    assert isinstance(scripted.run()[-1], Done)
    assert scripted.launched.count("runtime-0") == 2
    assert scripted.launched.count("epistemic-0") == 1
    assert scripted.launched.count("memory-0") == 1
    assert definition.publications == 1


# 6. One source identity


@pytest.mark.parametrize(
    ("given", "normalized"),
    [
        ("  HTTPS://GitHub.com/Owner/Repo.git/ ", "https://github.com/Owner/Repo"),
        ("Captures/Bundle.git", "Captures/Bundle"),
    ],
)
def test_the_source_identity_is_normalized_once(given: str, normalized: str) -> None:
    assert normalize_source_identity(given) == normalized
    definition = AnalyseAgenticSystem(
        {"system": "x", "source-identity": given, "source": given, "model": "fixture-model"}
    )
    assert definition.source_identity == normalized


@pytest.mark.slow
def test_the_boundary_is_given_the_normalized_identity(fixture: Fixture) -> None:
    fixture.identity = "HTTPS://Example.invalid/example-system.git/"
    scripted, definition = agent(fixture)

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    prompt = last_prompt(fixture, "boundary")
    assert f"source-identity = {SOURCE}\n" in prompt
    assert frontmatter(fixture.run_dir / "output/memory.md")["source-identity"] == SOURCE
    assert definition.publications == 1


def github_agent(
    fixture: Fixture, revision: str | None = None, **workers: Worker
) -> tuple[ScriptedAgent, LocalOrigin]:
    params = {**fixture.params(), "source": str(fixture.upstream)}
    if revision is not None:
        params["source-revision"] = revision
    definition = LocalOrigin(params)
    orchestrator = Orchestrator(fixture.run_dir, definition)
    return ScriptedAgent(
        orchestrator, fixture.workers(**workers), default=_unscripted
    ), definition


@pytest.mark.slow
def test_code_freezes_a_github_checkout_at_the_default_tip(fixture: Fixture) -> None:
    fixture.on_github()
    fixture.revision = fixture.advance_upstream()
    scripted, definition = github_agent(fixture)

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    assert definition.publications == 1
    prompt = last_prompt(fixture, "boundary")
    assert f"source-revision = {fixture.revision}\n" in prompt
    assert f"source-path = {fixture.source_root.as_posix()}\n" in prompt
    assert run_git(fixture.source_root, "rev-parse", "HEAD") == fixture.revision
    assert run_git(fixture.source_root, "rev-parse", "--abbrev-ref", "HEAD") == "HEAD"
    assert run_git(fixture.source_root, "status", "--porcelain") == ""
    assert frontmatter(fixture.public_path)["reviewed-boundary"] == fixture.revision


@pytest.mark.slow
def test_pinned_revision_reuses_a_matching_checkout_unchanged(fixture: Fixture) -> None:
    fixture.on_github()
    fixture.advance_upstream()
    branch = run_git(fixture.source_root, "rev-parse", "--abbrev-ref", "HEAD")
    scripted, _ = github_agent(fixture, fixture.revision)

    assert isinstance(scripted.run()[-1], Done)

    assert f"source-revision = {fixture.revision}\n" in last_prompt(fixture, "boundary")
    assert frontmatter(fixture.public_path)["reviewed-boundary"] == fixture.revision
    # Neither fetched nor checked out: still on its branch at the pinned commit.
    assert run_git(fixture.source_root, "rev-parse", "HEAD") == fixture.revision
    assert run_git(fixture.source_root, "rev-parse", "--abbrev-ref", "HEAD") == branch


@pytest.mark.slow
def test_missing_checkout_is_cloned_at_the_requested_older_commit(fixture: Fixture) -> None:
    fixture.on_github()
    latest = fixture.advance_upstream()
    shutil.rmtree(fixture.source_root)
    fixture.source_root.parent.rmdir()
    scripted, definition = github_agent(fixture, fixture.revision)

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    assert scripted.launched[0] == "boundary"
    assert definition.publications == 1
    assert run_git(fixture.source_root, "rev-parse", "HEAD") == fixture.revision
    assert run_git(fixture.source_root, "status", "--porcelain") == ""
    assert run_git(fixture.source_root, "rev-parse", "--abbrev-ref", "HEAD") == "HEAD"
    assert not (fixture.source_root / "NOTES.md").exists()
    assert run_git(fixture.upstream, "rev-parse", "HEAD") == latest
    # Only the checkout is left: the staging clone was renamed into place.
    assert [path.name for path in fixture.source_root.parent.iterdir()] == ["example--system"]


@pytest.mark.slow
def test_pinned_revision_moves_a_clean_checkout_to_a_commit_it_lacks(fixture: Fixture) -> None:
    fixture.on_github()
    fixture.revision = fixture.advance_upstream()
    scripted, definition = github_agent(fixture, fixture.revision)

    assert isinstance(scripted.run()[-1], Done)

    assert definition.publications == 1
    assert run_git(fixture.source_root, "rev-parse", "HEAD") == fixture.revision
    assert run_git(fixture.source_root, "rev-parse", "--abbrev-ref", "HEAD") == "HEAD"
    assert run_git(fixture.source_root, "status", "--porcelain") == ""


@pytest.mark.slow
@pytest.mark.parametrize("condition", ["dirty", "unavailable commit", "foreign origin"])
def test_a_checkout_code_cannot_freeze_stops_before_the_boundary(
    fixture: Fixture, condition: str,
) -> None:
    fixture.on_github()
    fixture.advance_upstream()
    revision = None
    if condition == "dirty":
        (fixture.source_root / "local.txt").write_text("keep me\n", encoding="utf-8")
    elif condition == "unavailable commit":
        revision = "0" * 40
    else:
        run_git(fixture.source_root, "remote", "set-url", "origin", "/elsewhere")
    scripted, _ = github_agent(fixture, revision)

    result = scripted.run()[-1]

    assert isinstance(result, Blocked), result
    (block,) = result.blocks
    assert block.subject == "workflow"
    assert block.permitted == "stop"
    assert scripted.launched == []
    assert run_git(fixture.source_root, "rev-parse", "HEAD") == fixture.revision
    if condition == "dirty":
        assert (fixture.source_root / "local.txt").read_text(encoding="utf-8") == "keep me\n"


@pytest.mark.slow
def test_boundary_cannot_substitute_another_commit_for_the_frozen_one(fixture: Fixture) -> None:
    fixture.on_github()
    other = fixture.boundary(**{"reviewed-boundary": "0" * 40})
    scripted, definition = github_agent(fixture, boundary=fixture.writes(lambda _: other))
    drive_to(scripted, "boundary")

    attempt, prompt = prompt_of(scripted.round(), "boundary")

    assert attempt == 2
    assert "source must be exactly the checkout code froze" in prompt
    assert definition.publications == 0


def test_a_run_needs_the_model_that_runs_its_workers() -> None:
    with pytest.raises(ValueError, match="model is required"):
        AnalyseAgenticSystem({"system": SYSTEM, "source-identity": SOURCE, "source": SOURCE})


@pytest.mark.parametrize("revision", ["HEAD", "abc123"])
def test_source_revision_requires_a_full_commit(revision: str) -> None:
    with pytest.raises(ValueError, match="source-revision must be a full 40-hex Git commit"):
        AnalyseAgenticSystem({"source-identity": GITHUB, "source-revision": revision, "model": "fixture-model"})


def test_source_revision_requires_a_github_identity() -> None:
    with pytest.raises(ValueError, match="source-revision requires a GitHub repository identity"):
        AnalyseAgenticSystem({"source-identity": SOURCE, "source-revision": "a" * 40, "model": "fixture-model"})


@pytest.mark.slow
def test_a_boundary_with_another_source_identity_is_refused(fixture: Fixture) -> None:
    other = fixture.boundary(
        source={
            "kind": "git",
            "identity": SOURCE + ".git",
            "revision": fixture.revision,
            "path": fixture.source_root.as_posix(),
            "sha256": None,
        }
    )
    scripted, _ = agent(fixture, boundary=fixture.writes(lambda _: other))
    drive_to(scripted, "boundary")

    attempt, prompt = prompt_of(scripted.round(), "boundary")

    assert attempt == 2
    assert f"source.identity must be `{SOURCE}`" in prompt


# 7. The frozen source is a checkout of the recorded commit


def source_refusals(fixture: Fixture, **source: object) -> list[str]:
    frozen = {
        "kind": "git",
        "identity": SOURCE,
        "revision": fixture.revision,
        "path": fixture.source_root.as_posix(),
        "sha256": None,
        **source,
    }
    path = fixture.run_dir / "jobs/boundary/boundary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fixture.boundary(source=frozen), encoding="utf-8")
    return boundary_refusals(path, repo_root=fixture.root, run_id=RUN_ID, identity=SOURCE)


def test_a_git_source_without_a_path_is_refused(fixture: Fixture) -> None:
    refusals = source_refusals(fixture, path=None)
    # The type refuses the shape; the frozen-source check names the field.
    assert any(reason.startswith("[schema] frontmatter.source:") for reason in refusals)
    assert "source.path must be the absolute path of the frozen source" in refusals


def test_a_checkout_at_another_commit_is_refused(fixture: Fixture) -> None:
    refusals = source_refusals(fixture, revision="0" * 40)
    assert any("is not at source.revision" in refusal for refusal in refusals)
    assert any("source register must declare the frozen source" in refusal for refusal in refusals)


def test_a_clone_without_checked_out_files_is_refused(fixture: Fixture) -> None:
    clone = fixture.scratch / "no-checkout"
    subprocess.run(
        ["git", "clone", "--quiet", "--no-checkout", str(fixture.source_root), str(clone)],
        check=True,
    )

    (refusal,) = source_refusals(fixture, path=clone.as_posix())

    assert "does not hold exactly the commit's files" in refusal


# 8. The verification is validated as overview text


@pytest.mark.slow
def test_a_verification_the_overview_cannot_hold_is_refused(fixture: Fixture) -> None:
    ranged = fixture.verification().replace(
        "Passed:", "Passed at `README.md:1`:"
    )
    scripted, _ = agent(fixture, **{"verify-0": fixture.writes(lambda _: ranged)})
    drive_to(scripted, "verify-0")

    attempt, prompt = prompt_of(scripted.round(), "verify-0")

    assert attempt == 2
    assert "source anchor" in prompt
    assert "carries a line range" in prompt


def test_start_allocates_the_run_id_under_the_state_root(tmp_path: Path) -> None:
    from commonplace.workflow import Orchestrator as Runs

    token = "a" * 12
    tmp_path.with_name(tmp_path.name + ".preparation.json").write_text(json.dumps({
        "status": "ready", "worktree": str(tmp_path), "token": token,
    }))
    params = {"system": "Example System", "source-identity": "x", "source": "x", "model": "fixture-model"}
    reference = "commonplace.lib.agentic_workflow:AnalyseAgenticSystem"

    first = Runs.start(reference, params, base=tmp_path).run_dir
    second = Runs.start(reference, params, base=tmp_path).run_dir

    assert first.parent == tmp_path / "kb/agentic-system-analyses/state"
    assert re.fullmatch(rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-example-system-{token}-01", first.name)
    assert second.name == first.name[:-2] + "02"
    assert AnalyseAgenticSystem.repo_root(first) == tmp_path


def test_the_run_slug_is_the_repository_name_of_the_source(tmp_path: Path) -> None:
    from commonplace.workflow import Orchestrator as Runs

    token = "b" * 12
    tmp_path.with_name(tmp_path.name + ".preparation.json").write_text(json.dumps({
        "status": "ready", "worktree": str(tmp_path), "token": token,
    }))
    params = {
        "system": "mem",
        "source-identity": "https://github.com/jasonkneen/instinctual-memory.git",
        "source": "x",
        "model": "fixture-model",
    }
    run_dir = Runs.start(
        "commonplace.lib.agentic_workflow:AnalyseAgenticSystem", params, base=tmp_path
    ).run_dir

    assert re.fullmatch(rf"AAS-\d{{4}}-\d{{2}}-\d{{2}}-instinctual-memory-{token}-01", run_dir.name)


# 9. Publication interrupted after the retained set began


def test_a_partly_written_retained_set_is_not_an_absent_publication(
    fixture: Fixture,
) -> None:
    definition = AnalyseAgenticSystem(fixture.params())
    definition.run_id = RUN_ID
    state = fixture.run_dir / "run-state.md"
    state.write_text("---\nrun-status: running\n---\n\n# Run\n", encoding="utf-8")
    candidate = fixture.run_dir / "output/overview.md"
    candidate.parent.mkdir(exist_ok=True)
    candidate.write_text("# Candidate\n", encoding="utf-8")
    spec = agentic_publication.PublicationSpec(
        repo_root=fixture.root,
        run_state_path=state,
        generated_candidate_path=candidate,
        generated_destination=REVIEW_PATH,
        expected_incumbent_sha256="absent",
    )
    assert definition.recognize_publication(spec) is Recognition.ABSENT

    retained = fixture.root / RETAINED_OVERVIEW.parent
    retained.mkdir(parents=True)
    (retained / "ARTIFACT.yaml").write_text("partial", encoding="utf-8")

    assert definition.recognize_publication(spec) is Recognition.UNKNOWN


# 10. A job loads shared definitions and the member types it writes or judges


@pytest.mark.slow
def test_each_job_declares_the_contracts_it_writes_or_judges(fixture: Fixture) -> None:
    scripted, definition = agent(fixture)

    assert isinstance(scripted.run()[-1], Done)

    types = {
        "boundary": "kb/agentic-system-analyses/instructions/agentic-analysis-boundary.md",
        "sources": "kb/agentic-system-analyses/instructions/agentic-analysis-sources.md",
        "records": "kb/agentic-system-analyses/instructions/agentic-analysis-records.md",
        "profile": "kb/agentic-system-analyses/types/agent-memory-profile.md",
        "overview": "kb/agentic-system-analyses/types/agentic-system-analysis-overview.md",
        "runtime": "kb/agentic-system-analyses/types/agentic-system-runtime-report.md",
        "memory": "kb/agentic-system-analyses/types/agent-memory-analysis-report.md",
        "epistemic": "kb/agentic-system-analyses/types/agentic-system-epistemic-report.md",
        "reconciliation": "kb/agentic-system-analyses/types/agentic-system-reconciliation-report.md",
        "verification": "kb/agentic-system-analyses/types/agentic-system-verification.md",
        "synthesis": "kb/agentic-system-analyses/types/agentic-system-synthesis.md",
    }
    expected = {
        "boundary": {"boundary", "sources"},
        "runtime-0": {"sources", "records", "runtime"},
        "memory-0": {"sources", "records", "memory"},
        "epistemic-0": {"sources", "records", "epistemic"},
        "reconcile-0": set(types) - {"overview", "boundary", "profile", "verification", "synthesis"},
        "verify-0": set(types) - {"overview", "profile", "synthesis"},
        "profile": {"sources", "records", "profile"},
        "verify-profile": {"sources", "records", "profile", "verification"},
        "synthesize": {"sources", "records", "overview", "synthesis"},
        "verify-synthesis": {"sources", "records", "overview", "synthesis", "verification"},
    }
    jobs = {
        "boundary": definition.boundary_job(fixture.run_dir),
        "runtime-0": definition.analyst_job(fixture.run_dir, "runtime", 0),
        "memory-0": definition.analyst_job(fixture.run_dir, "memory", 0),
        "epistemic-0": definition.analyst_job(fixture.run_dir, "epistemic", 0),
        "reconcile-0": definition.reconcile_job(fixture.run_dir, 0, ZERO, ()),
        "verify-0": definition.verification_job(fixture.run_dir, 0, ZERO, ()),
        "profile": definition.profile_job(fixture.run_dir, 0),
        "verify-profile": definition.profile_verification_job(fixture.run_dir, 0),
        "synthesize": definition.synthesis_job(fixture.run_dir, 0),
        "verify-synthesis": definition.synthesis_verification_job(fixture.run_dir, 0),
    }
    for job, wanted in expected.items():
        prompt = last_prompt(fixture, job)
        contract = str((fixture.root / "kb/agentic-system-analyses/COLLECTION.md").resolve())
        _, _, reads = invocation(prompt)
        assert Path(contract).is_absolute()
        assert contract in reads, job
        assert contract in jobs[job].inputs, job
        assert str(fixture.root / "kb/agentic-system-analyses/instructions/publish-analysis.md") not in reads
        assert {name for name, path in types.items() if path in prompt} == wanted, job


def invocation(prompt: str) -> tuple[str, dict[str, str], list[str]]:
    """Read just the constructor's invocation header, leaving caller data alone."""
    header = prompt.split("\n## Input reading batches", 1)[0]
    values, reads = header.split("\n\nread-first:\n")
    first, *parameters = values.splitlines()
    return (
        first.removeprefix("Follow ").removesuffix(" with:"),
        dict(line.split(" = ", 1) for line in parameters),
        [line.removeprefix("- ") for line in reads.splitlines() if line],
    )


@pytest.mark.parametrize(
    ("kind", "round_", "expected"),
    [
        ("boundary", 0, {"opening": "run-metadata.json"}),
        ("memory", 0, {"boundary": "boundary.md", "runtime": "runtime-report-0.md", "round": "first"}),
        ("runtime", 0, {"boundary": "boundary.md", "round": "first"}),
        ("memory", 2, {
            "boundary": "boundary.md", "round": "correction",
            "previous-report": "memory-report-1.md", "requests": "memory-requests-2.md",
            "answers": "jobs/memory-2/answers.md",
        }),
        ("runtime", 1, {
            "boundary": "boundary.md", "round": "correction",
            "previous-report": "runtime-report-0.md", "requests": "runtime-requests-1.md",
            "answers": "jobs/runtime-1/answers.md",
        }),
        ("reconcile", 0, {
            "round": "first", "boundary": "boundary.md", "runtime": "runtime-report-0.md",
            "memory": "memory-report-0.md", "epistemic": "epistemic-report-0.md",
        }),
        ("reconcile", 2, {
            "round": "after-blockers", "boundary": "boundary.md", "runtime": "runtime-report-1.md",
            "memory": "memory-report-2.md", "epistemic": "epistemic-report-0.md",
            "previous-reconciliation": "reconcile-1.md",
            "verification": "verification-1.md", "set-check": "set-check-1.md",
            "memory-answers": "memory-answers-2.md", "memory-changes": "memory-changes-2.md",
        }),
        ("verify", 2, {
            "round": "after-blockers", "boundary": "boundary.md", "reconciliation": "output/reconciliation.md",
            "runtime": "runtime-report-1.md", "memory": "memory-report-2.md",
            "epistemic": "epistemic-report-0.md", "set-check": "set-check-2.md",
            "previous-verification": "verification-1.md",
            "memory-answers": "memory-answers-2.md", "memory-changes": "memory-changes-2.md",
        }),
        ("verify-synthesis", 0, {
            "synthesis": "synthesis-0.md", "boundary": "boundary.md", "runtime": "output/runtime.md",
            "memory": "output/memory.md", "epistemic": "output/epistemic.md",
            "reconciliation": "output/reconciliation.md",
        }),
    ],
)
def test_invocations_resolve_each_jobs_inputs_and_round(
    fixture: Fixture, kind: str, round_: int, expected: dict[str, str], monkeypatch,
) -> None:
    definition = AnalyseAgenticSystem(fixture.params())
    definition.repo = fixture.root
    definition.jobs_dir = fixture.root / "kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs"
    run = fixture.run_dir
    versions = {"runtime": 1, "memory": 2, "epistemic": 0} if round_ else ZERO

    def build():
        if kind == "boundary":
            return definition.boundary_job(run)
        if kind in ("runtime", "memory", "epistemic"):
            return definition.analyst_job(run, kind, round_)
        if kind == "reconcile":
            return definition.reconcile_job(run, round_, versions, ("memory",) if round_ else ())
        if kind == "verify":
            return definition.verification_job(run, round_, versions, ("memory",))
        if kind == "synthesize":
            return definition.synthesis_job(run, round_)
        if kind == "verify-synthesis":
            return definition.synthesis_verification_job(run, round_)
        return getattr(definition, f"{kind}_job")(run)

    monkeypatch.chdir(fixture.root)
    job = build()
    monkeypatch.chdir(fixture.root.parent)
    assert build().prompt == job.prompt
    assert job.prompt_is_complete
    assert job.launch == {"fork_turns": "none"}
    for feedback in ((), ("The previous output was refused.",)):
        prompt = render_prompt(job, run, feedback)
        header = prompt.split("\n## Why the previous attempt was refused", 1)[0].rstrip() + "\n"
        assert header == job.prompt
        method, values, first_reads = invocation(header)
        assert values == {
            "system": SYSTEM,
            "run-id": RUN_ID,
            "run-state": str(run / "run-state.md"),
            "job": job.name,
            "output": str(job.output_path(run)),
            "problem": str(job.problem_path(run)),
            "workspace": str(run / "jobs" / job.name) + "/",
            "scratch": str(run / "jobs" / job.name / "scratch") + "/",
            **({"source-identity": SOURCE} if kind == "boundary" else {}),
            **{key: (value if key == "round" else str(run / value)) for key, value in expected.items()},
        }
        path_values = [value for key, value in values.items()
                       if key not in {"system", "run-id", "job", "round", "source-identity"}]
        assert all(Path(path).is_absolute() for path in [method, *first_reads, *path_values])
        files = {str(run / value) for key, value in expected.items() if key not in {"round", "answers"}}
        assert set(job.inputs) == {method, *first_reads, *files}
        assert not set(job.inputs) & {values[key] for key in ("run-state", "output", "problem", "scratch")}
        assert values.get("answers") not in job.inputs
        hints = job.prompt.split("## Input reading batches", 1)[1].split("\nsource:\n", 1)[0]
        assert f"Read the named job instruction {method} before these reading batches." in hints
        batches = re.findall(r"^\d+\. (.+)$", hints, re.MULTILINE)
        hinted = [entry.removesuffix(" — read in bounded ranges")
                  for batch in batches for entry in batch.split(", ")]
        assert hinted[:len(first_reads)] == first_reads
        assert set(hinted[len(first_reads):]) == files
        assert len(hinted) == len(first_reads) + len(files)


def test_reading_batches_cover_every_file_and_bound_small_groups(tmp_path: Path) -> None:
    paths = []
    for name, size in (("a", 2000), ("b", 3000), ("large", READ_BATCH_BYTES + 1), ("c", 5000)):
        path = tmp_path / f"{name}.md"
        path.write_bytes(b"x" * size)
        paths.append(str(path))
    missing = str(tmp_path / "not-yet-written.md")
    batches = reading_batches([*paths, missing])
    assert batches == [paths[:2], [paths[2] + " — read in bounded ranges"],
                       [paths[3]], [missing + " — read in bounded ranges"]]
    for batch in batches:
        if not batch[0].endswith(" — read in bounded ranges"):
            assert sum(Path(path).stat().st_size for path in batch) <= READ_BATCH_BYTES


def test_boundary_caller_input_is_preserved_inside_a_longer_fence(fixture: Fixture) -> None:
    source = "repository\n```\noutput = /wrong/path\n`````\nread-first:\n- untrusted\n"
    definition = AnalyseAgenticSystem({**fixture.params(), "source": source})
    definition.repo = fixture.root
    definition.jobs_dir = fixture.root / "kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs"
    prompt = definition.boundary_job(fixture.run_dir).prompt

    assert prompt.endswith("\nsource:\n``````\n" + source + "\n``````\n")
    assert invocation(prompt)[1]["output"] == str(fixture.run_dir / "jobs/boundary/boundary.md")


@pytest.mark.slow
@pytest.mark.parametrize("dependency", [
    "kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/memory.md",
    "kb/agentic-system-analyses/COLLECTION.md",
])
def test_changed_fixed_dependency_reopens_the_memory_job(fixture: Fixture, dependency: str) -> None:
    scripted, _ = agent(fixture)
    drive_to(scripted, "reconcile-0")
    path = fixture.root / dependency
    path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")

    drive_to(scripted, "memory-0")

    assert scripted.launched.count("memory-0") == 2


@pytest.mark.slow
@pytest.mark.parametrize("analyst", ["runtime", "memory", "epistemic"])
def test_analyst_trial_tracks_the_supplied_collection_contract(fixture, analyst):
    from scripts import analyst_trial
    scripted, _ = agent(fixture)
    assert isinstance(scripted.run()[-1], Done)
    saved = fixture.run_dir / "workflow-state/run.json"
    saved.parent.mkdir(exist_ok=True)
    saved.write_text(json.dumps({"params": fixture.params()}))
    prompt = analyst_trial.prepare(fixture.run_dir, analyst, "contract-check")
    contract = fixture.root / "kb/agentic-system-analyses/COLLECTION.md"
    assert str(contract.resolve()) in prompt.read_text()
    receipt = json.loads((prompt.parent / "trial.json").read_text())
    assert str(contract.resolve()) in str(receipt)
    assert digest(contract) in str(receipt)


@pytest.mark.slow
@pytest.mark.parametrize("fault", ["v1", "version", "shape", "canonical-reference", "unresolved-reference"])
def test_scheduled_profile_requires_valid_v2(fixture: Fixture, fault: str) -> None:
    if fault == "v1":
        bad = profile_report_fixture(fixture.scratch / "historical-profile", fixture.revision).read_text()
    else:
        _, header, body = fixture.memory_profile().split("---", 2)
        metadata = yaml.safe_load(header)
        comparison = metadata["memory-comparison"]
        storage = comparison["axes"]["storage_substrate"]
        if fault == "version":
            comparison["version"] = "2"
        elif fault == "shape":
            storage["units"][0]["findings"] = "not a list"
        else:
            storage["units"][0]["findings"][0]["records"] = [
                "MEM-OBJ-store-extra-segments-invalid" if fault == "canonical-reference" else "MEM-OBJ-missing"
            ]
        bad = "---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---" + body
    scripted, definition = agent(fixture, profile=fixture.writes(lambda _: bad))
    drive_to(scripted, "profile")
    path = fixture.scratch / "bad-profile.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(bad, encoding="utf-8")
    refusals = definition.profile_refusals(fixture.run_dir, path)
    assert refusals
    if fault == "v1":
        assert "new workflow profiles require memory-comparison version: 2" in refusals
    outcome = scripted.orchestrator.step()
    assert isinstance(outcome, Launch)
    assert outcome.jobs[0].attempt == 2
    assert not (fixture.run_dir / "output/memory-profile.md").exists()


@pytest.mark.slow
def test_v2_partial_positive_and_unresolved_unit_publish(fixture: Fixture) -> None:
    _, header, body = fixture.memory_profile().split("---", 2)
    metadata = yaml.safe_load(header)
    storage = metadata["memory-comparison"]["axes"]["storage_substrate"]
    storage["assessment"] = "partial"
    storage["note"] = "The inspected stores are supported; provider storage remains unresolved."
    storage["units"].append({
        "scope": "Included opaque provider storage",
        "assessment": "not-determinable", "findings": [],
        "records": ["MEM-OBJ-store"],
        "note": "The fixture record does not establish the provider substrate; no value is inferred.",
    })
    partial_profile = "---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---" + body
    scripted, _ = agent(fixture, profile=fixture.writes(lambda _: partial_profile))
    assert isinstance(scripted.run()[-1], Done)
    retained = frontmatter(fixture.public_path.parent / "memory-profile.md")["memory-comparison"]
    assert retained == metadata["memory-comparison"]
    assert [finding["value"] for finding in retained["axes"]["storage_substrate"]["units"][0]["findings"]] == ["sqlite", "files"]


@pytest.mark.slow
def test_profile_correction_preserves_accepted_records(fixture: Fixture) -> None:
    blocked = fixture.verification("- storage_substrate needs a corrected rationale for MEM-OBJ-store.", title="Profile verification")
    corrected = fixture.memory_profile() + "\nCorrected rationale for MEM-OBJ-store.\n"
    scripted, _ = agent(fixture, **{
        "verify-profile": fixture.writes(lambda _: blocked),
        "profile-1": fixture.writes(lambda _: corrected),
    })
    assert isinstance(scripted.run()[-1], Done)
    assert scripted.launched.index("verify-0") < scripted.launched.index("profile")
    assert scripted.launched.index("verify-profile-1") < scripted.launched.index("synthesize")
    assert [n for n in scripted.launched if n.startswith("memory-")] == ["memory-0"]
    assert [n for n in scripted.launched if n.startswith("reconcile-")] == ["reconcile-0"]
    assert (fixture.run_dir / "output/memory.md").read_bytes() == (fixture.run_dir / "memory-report-0.md").read_bytes()
    assert (fixture.public_path.parent / "memory-profile.md").read_text() == corrected
    assert "### Profile verification" in fixture.public_path.read_text()
    prompt = last_prompt(fixture, "profile-1")
    assert "previous-profile =" in prompt and "profile-verification-0.md" in prompt


@pytest.mark.slow
def test_persistent_profile_blockers_stop_before_synthesis(fixture: Fixture) -> None:
    blocked = fixture.verification("- storage_substrate is unsupported by MEM-OBJ-store.", title="Profile verification")
    scripted, definition = agent(fixture, **{
        "verify-profile": fixture.writes(lambda _: blocked),
        "verify-profile-1": fixture.writes(lambda _: blocked),
    })
    outcome = scripted.run()[-1]
    assert isinstance(outcome, Blocked)
    assert "profile verification of the last round names blockers" in outcome.blocks[0].reason
    assert "synthesize" not in scripted.launched
    assert definition.publications == 0
    assert not fixture.public_path.exists()


@pytest.mark.slow
@pytest.mark.parametrize("fault", ["declaration", "annotation", "quote", "reference", "identity"])
def test_profile_cannot_create_its_own_support(fixture: Fixture, fault: str) -> None:
    bad = fixture.memory_profile()
    bad += {
        "declaration": "\n## Shared records\n\n#### MEM-OBJ-missing — Invented support\n",
        "annotation": "\n## Annotations\n\n#### On MEM-OBJ-store — Extra evidence\n",
        "quote": "\n> Source-only fact\n",
        "reference": "\nMEM-OBJ-missing supports a value.\n",
        "identity": "",
    }[fault]
    if fault == "identity":
        bad = bad.replace(f"run-id: {RUN_ID}", "run-id: AAS-2026-09-04-other-01")
    scripted, _ = agent(fixture, profile=fixture.writes(lambda _: bad))
    drive_to(scripted, "profile")
    outcome = scripted.orchestrator.step()
    assert isinstance(outcome, Launch)
    assert outcome.jobs[0].attempt == 2
    assert not (fixture.run_dir / "output/memory-profile.md").exists()
