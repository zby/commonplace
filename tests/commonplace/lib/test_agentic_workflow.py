"""The analyse-agentic-system workflow definition, driven by scripted workers.

No model runs here. `ScriptedAgent` plays the agent orchestrator: for each job
the definition hands out, a scripted worker writes the file a sub-agent would.
The run lives in a temporary repository whose analysis set validates and
publishes, built from the fixtures of `test_agentic_analysis.py`.
"""

from __future__ import annotations

import re
import shutil
from collections.abc import Callable
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.lib import agentic_publication, agentic_set, validation
from commonplace.lib.agentic_workflow import (
    AnalyseAgenticSystem,
    boundary_refusals,
    overview_enums,
)
from commonplace.workflow import Blocked, Done, Handout, Launch, Orchestrator
from tests.commonplace.lib.test_agentic_analysis import (
    MAPPING,
    REPO_ROOT,
    RUN_ID,
    SOURCE,
    STATE_DIR,
    commit_inputs,
    configure_types,
    epistemic_text,
    git_checkout,
    memory_report_fixture,
    runtime_text,
)
from tests.commonplace.workflow.definitions import ScriptedAgent

pytestmark = pytest.mark.usefixtures("tmp_library")

SYSTEM = "Example System"
REVIEW_PATH = f"{agentic_set.REVIEWS_ROOT}/example-system.md"
INSTRUCTIONS = (
    "kb/instructions/analyse-agentic-system",
    "kb/instructions/analyse-agent-memory.md",
    "kb/instructions/analyse-external-system-epistemic-architecture.md",
)
((PROPOSAL, CANONICAL),) = MAPPING.items()

Worker = Callable[[Handout], None]


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

    def params(self) -> dict[str, str]:
        return {"system": SYSTEM, "source-identity": SOURCE, "source": SOURCE}

    # What each scripted worker writes

    def boundary(self, disposition: str = "complete", **changes) -> str:
        if disposition == "complete":
            fields = {
                "result-disposition": "complete",
                "target-class": "enclosing runtime",
                "boundary-kind": "whole-system",
                "reviewed-boundary": self.revision,
                "analysis-cutoff": "2026-09-04",
                "evidence-tier": "code-grounded",
                "source": {
                    "kind": "git",
                    "identity": SOURCE,
                    "revision": self.revision,
                    "path": self.source_root.as_posix(),
                    "sha256": None,
                },
            }
            not_reached = ""
        else:
            fields = {
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
            "## Boundary and evidence\n\n"
            f"Fixture boundary at `{self.revision}`.\n\n"
            "## Source register\n\n"
            f"| SRC-1 | git | `{SOURCE}` | `{self.revision}` | implementation "
            "| README.md | `README.md` | none |\n" + not_reached
        )
        return "---\n" + yaml.safe_dump(fields, sort_keys=False) + "---\n\n" + body

    def memory_report(self) -> str:
        """The fixture's specialist report, bound to the run's memory input."""
        scratch = self.scratch / "memory"
        local = memory_report_fixture(scratch, self.revision)
        return local.read_text(encoding="utf-8").replace(
            digest(scratch / "memory-input.md"),
            digest(self.run_dir / agentic_set.LOCAL_INPUT_NAME),
        )

    @staticmethod
    def reconciliation(*, returned: bool = False, table: dict | None = None) -> str:
        rows = "".join(
            f"| {proposal} | {canonical} | registered |\n"
            for proposal, canonical in (table or MAPPING).items()
        )
        text = (
            "## Reconciliation\n\n"
            "| specialist proposal | canonical record | disposition |\n"
            "|---|---|---|\n" + rows + "\n"
            "## Bounded synthesis\n\n"
            f"Fixture synthesis over OBJ-1, {CANONICAL} and RTE-1.\n\n"
            "## Limitations\n\nNone.\n"
        )
        if returned:
            text += (
                "\n## Returned to the specialist\n\n"
                f"- {PROPOSAL}: the write-side anchor does not resolve at `README.md`.\n"
            )
        return text

    @staticmethod
    def verification(blockers: str = "None.") -> str:
        return (
            "### Semantic verification\n\nPassed: every claim checked against "
            f"its records.\n\n### Blockers\n\n{blockers}\n"
        )

    def review_body(self, *, evidence: bool = True) -> str:
        basis = (
            f"Evidence basis: `README.md` at `{self.revision}`.\n"
            if evidence
            else (f"Built from `README.md` at `{self.revision}`.\n")
        )
        return (
            '---\ndescription: "Generated fixture review of one external agentic system"\n'
            f"---\n\n# {SYSTEM}\n\n{basis}"
        )

    def workers(self, **overrides: Worker) -> dict[str, Worker]:
        def writes(text: Callable[[], str]) -> Worker:
            def worker(handout: Handout) -> None:
                handout.output_path.parent.mkdir(parents=True, exist_ok=True)
                handout.output_path.write_text(text(), encoding="utf-8")

            return worker

        workers = {
            "boundary": writes(self.boundary),
            "runtime": writes(lambda: runtime_text(self.revision)),
            "scoping": writes(
                lambda: (
                    "### Memory/context scope\n\nBrief fixture scope.\n\n"
                    "### Epistemic scope\n\nBrief fixture scope.\n"
                )
            ),
            "epistemic": writes(lambda: "# Epistemic draft\n\nOBJ-1 and RTE-1.\n"),
            "review": writes(self.review_body),
        }
        for round_ in range(AnalyseAgenticSystem.correction_rounds + 1):
            workers[f"memory-{round_}"] = writes(self.memory_report)
            workers[f"reconcile-{round_}"] = writes(self.reconciliation)
            workers[f"runtime-final-{round_}"] = writes(
                lambda: runtime_text(self.revision)
            )
            workers[f"epistemic-final-{round_}"] = writes(
                lambda: epistemic_text(self.revision)
            )
            workers[f"verify-{round_}"] = writes(self.verification)
        workers.update(overrides)
        return workers

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


# 0. Deriving the repository root


def test_repo_root_is_the_repository(fixture: Fixture) -> None:
    assert AnalyseAgenticSystem.repo_root(fixture.run_dir) == fixture.root


# 1. A complete run


def test_complete_run_publishes_and_replays_to_done(fixture: Fixture) -> None:
    scripted, definition = agent(fixture)

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    assert scripted.launched == [
        "boundary",
        "runtime",
        "scoping",
        "epistemic",
        "memory-0",
        "reconcile-0",
        "runtime-final-0",
        "epistemic-final-0",
        "verify-0",
        "review",
    ]
    assert definition.publications == 1

    state_path = fixture.run_dir / "run-state.md"
    state = frontmatter(state_path)
    assert state["run-status"] == "complete"
    assert state["result-disposition"] == "complete"
    review = fixture.root / REVIEW_PATH
    assert state["generated-review"] == {"path": REVIEW_PATH, "sha256": digest(review)}
    candidate = fixture.run_dir / "review-candidate.md"
    # Publication removes the candidate it published.
    assert not candidate.exists()
    assert frontmatter(review)["analysis-run"] == RUN_ID
    assert frontmatter(review)["analysis-artifact-sha256"] == digest(
        fixture.run_dir / "output/ARTIFACT.yaml"
    )
    for name, retained in agentic_set.retained_set_paths(RUN_ID).items():
        local = fixture.run_dir / ("output/" + name)
        assert (fixture.root / retained).read_bytes() == local.read_bytes(), name
    assert validation.validate_note(state_path, repo_root=fixture.root).fails == []

    overview = frontmatter(fixture.run_dir / "output/overview.md")
    assert overview["inputs-commit"] == fixture.head

    before = state_path.read_bytes(), state_path.stat().st_mtime_ns
    assert isinstance(scripted.orchestrator.step(), Done)
    assert (state_path.read_bytes(), state_path.stat().st_mtime_ns) == before
    assert definition.publications == 1
    # Replay renders the candidate again, byte for byte what was published,
    # so the publication effect's recorded inputs still match.
    assert candidate.read_bytes() == review.read_bytes()


# 2. An out-of-scope boundary


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
    assert not (fixture.root / REVIEW_PATH).exists()
    assert not (fixture.root / agentic_set.RETAINED_ROOT).exists()

    assert isinstance(scripted.orchestrator.step(), Done)


# 3. The correction cycle


def test_returned_findings_run_correction_rounds_until_the_last(
    fixture: Fixture,
) -> None:
    last = f"reconcile-{AnalyseAgenticSystem.correction_rounds}"

    def reconcile(returned_on_first_attempt: bool) -> Worker:
        return fixture.writes(
            lambda handout: fixture.reconciliation(
                returned=returned_on_first_attempt and handout.attempt == 1
            )
        )

    returning = {
        f"reconcile-{round_}": fixture.writes(
            lambda _: fixture.reconciliation(returned=True)
        )
        for round_ in range(AnalyseAgenticSystem.correction_rounds)
    }
    scripted, definition = agent(fixture, **returning, **{last: reconcile(True)})

    result = None
    while not (
        isinstance(result, Launch) and any(job.name == last for job in result.jobs)
    ):
        result = scripted.round()
        assert isinstance(result, Launch), result
    # The last round returned findings on its first attempt; it is refused.
    refused = scripted.round()
    attempt, prompt = prompt_of(refused, last)
    assert attempt == 2
    assert "this is the last round: remove `## Returned to the specialist`" in prompt
    assert "This is the last round: it may not return findings." in prompt

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    rounds = AnalyseAgenticSystem.correction_rounds
    order = [
        name for name in scripted.launched if name.startswith(("memory-", "reconcile-"))
    ]
    expected = ["memory-0", "reconcile-0"]
    for round_ in range(1, rounds + 1):
        expected += [f"memory-{round_}", f"reconcile-{round_}"]
    expected.append(last)
    assert order == expected
    prompt = last_prompt(fixture, "memory-1")
    assert "memory-report-0.md" in prompt and "reconcile-0.md" in prompt
    assert definition.publications == 1
    overview = (fixture.run_dir / "output/overview.md").read_text(encoding="utf-8")
    assert "Returned to the specialist" not in overview


def last_prompt(fixture: Fixture, name: str) -> str:
    """The prompt file of a job's last hand-out."""
    prompts = (fixture.run_dir / "workflow-state").rglob("prompt.md")
    (found,) = [prompt for prompt in prompts if prompt.parent.name == name]
    return found.read_text(encoding="utf-8")


# 4. Validators refuse


def drive_to(scripted: ScriptedAgent, name: str) -> None:
    """Step until the job is handed out and its scripted worker has written."""
    for _ in range(20):
        result = scripted.round()
        assert isinstance(result, Launch), result
        if any(job.name == name for job in result.jobs):
            return
    raise AssertionError(f"{name} was never handed out")


def test_boundary_with_a_wrong_field_set_is_refused(fixture: Fixture) -> None:
    bad = fixture.boundary()
    bad = bad.replace("evidence-tier:", "evidence-level:")
    scripted, _ = agent(fixture, boundary=fixture.writes(lambda _: bad))
    drive_to(scripted, "boundary")

    attempt, prompt = prompt_of(scripted.round(), "boundary")

    assert attempt == 2
    assert "the frontmatter must have exactly these fields" in prompt
    assert "run-status: running\nresult-disposition: null\nsource: null\n" in (
        fixture.run_dir / "run-state.md"
    ).read_text(encoding="utf-8")


def test_boundary_with_an_unquoted_date_is_refused(fixture: Fixture) -> None:
    path = fixture.scratch / "boundary.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        fixture.boundary().replace(
            "analysis-cutoff: '2026-09-04'", "analysis-cutoff: 2026-09-04"
        ),
        encoding="utf-8",
    )
    assert "analysis-cutoff: 2026-09-04\n" in path.read_text(encoding="utf-8")

    assert boundary_refusals(path, enums=overview_enums(fixture.root)) != []


def test_reconciliation_leaving_a_proposal_unmapped_is_refused(
    fixture: Fixture,
) -> None:
    unmapped = fixture.reconciliation(table={"MEM-OBJ-9": CANONICAL})
    scripted, _ = agent(fixture, **{"reconcile-0": fixture.writes(lambda _: unmapped)})
    drive_to(scripted, "reconcile-0")

    attempt, prompt = prompt_of(scripted.round(), "reconcile-0")

    assert attempt == 2
    assert "the memory report cannot be finalized from this reconciliation" in prompt
    assert f"proposals missing from the Reconciliation table: {PROPOSAL}" in prompt


def test_review_body_without_evidence_basis_is_refused(fixture: Fixture) -> None:
    body = fixture.review_body(evidence=False)
    scripted, definition = agent(fixture, review=fixture.writes(lambda _: body))
    drive_to(scripted, "review")

    attempt, prompt = prompt_of(scripted.round(), "review")

    assert attempt == 2
    assert "the body needs one line starting `Evidence basis:`" in prompt
    assert definition.publications == 0
    assert not (fixture.root / REVIEW_PATH).exists()


# 5. A named blocker stops before publication


def test_a_named_blocker_starts_another_reconciliation_round(fixture: Fixture) -> None:
    blocked = fixture.verification("RTE-1 is cited by the synthesis but never traced.")
    scripted, definition = agent(
        fixture, **{"verify-0": fixture.writes(lambda _: blocked)}
    )

    results = scripted.run()

    assert isinstance(results[-1], Done), results[-1]
    order = [
        name
        for name in scripted.launched
        if name.startswith(("reconcile-", "runtime-final-", "verify-", "review"))
    ]
    assert order == [
        "reconcile-0",
        "runtime-final-0",
        "verify-0",
        "reconcile-1",
        "runtime-final-1",
        "verify-1",
        "review",
    ]
    prompt = last_prompt(fixture, "reconcile-1")
    assert "verification-0.md" in prompt and "set-check-0.md" in prompt
    assert "named blockers" in prompt
    assert definition.publications == 1
    overview = (fixture.run_dir / "output/overview.md").read_text(encoding="utf-8")
    assert "never traced" not in overview


def test_blockers_in_the_last_round_stop_before_publication(fixture: Fixture) -> None:
    blocked = fixture.verification("RTE-1 is cited by the synthesis but never traced.")
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
    assert "review" not in scripted.launched
    assert definition.publications == 0
    assert not (fixture.root / REVIEW_PATH).exists()
    assert frontmatter(fixture.run_dir / "run-state.md")["run-status"] == "running"


def test_runtime_member_leaving_a_cited_record_undeclared_is_refused(
    fixture: Fixture,
) -> None:
    def epistemic_citing_a_new_record(handout: Handout) -> None:
        handout.output_path.write_text(
            "# Epistemic draft\n\nOBJ-1, RTE-1 and the registered OBJ-99.\n",
            encoding="utf-8",
        )

    scripted, _ = agent(fixture, epistemic=epistemic_citing_a_new_record)
    drive_to(scripted, "runtime-final-0")

    attempt, prompt = prompt_of(scripted.round(), "runtime-final-0")

    assert attempt == 2
    assert "unresolved record OBJ-99" in prompt


def test_start_allocates_the_run_id_under_the_state_root(tmp_path: Path) -> None:
    from commonplace.workflow import Orchestrator as Runs

    params = {"system": "Example System", "source-identity": "x", "source": "x"}
    reference = "commonplace.lib.agentic_workflow:AnalyseAgenticSystem"

    first = Runs.start(reference, params, base=tmp_path).run_dir
    second = Runs.start(reference, params, base=tmp_path).run_dir

    assert first.parent == tmp_path / "kb/reports/state/agentic-system-analysis"
    assert re.fullmatch(r"AAS-\d{4}-\d{2}-\d{2}-example-system-01", first.name)
    assert second.name == first.name[:-2] + "02"
    assert AnalyseAgenticSystem.repo_root(first) == tmp_path
