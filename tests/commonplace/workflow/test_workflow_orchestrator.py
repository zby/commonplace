"""What the code orchestrator guarantees, shown without a model.

The numbered sections follow the test list in
kb/work/code-scheduled-workflows/README.md.
"""

from __future__ import annotations

import pytest

from commonplace.workflow import (
    Blocked,
    DefinitionError,
    Done,
    Job,
    Launch,
    Orchestrator,
    Uncertain,
    Workflow,
)
from tests.commonplace.workflow.definitions import (
    NamedBeforeWaited,
    OneJob,
    ScriptedAgent,
    TwoLenses,
    TwoLensesReversed,
    UnequalPaths,
    has_heading,
    lens_job,
    new_run,
    on_request,
    write_invalid,
    write_nothing,
    write_problem,
    write_valid,
)

pytestmark = on_request


def names(result):
    assert isinstance(result, Launch), result
    return [handout.name for handout in result.jobs]


def one_block(result):
    assert isinstance(result, Blocked), result
    assert len(result.blocks) == 1
    return result.blocks[0]


# 1. Independent paths


def test_pending_jobs_on_independent_paths_are_returned_in_one_round(tmp_path):
    orchestrator = Orchestrator(new_run(tmp_path), TwoLenses())

    assert names(orchestrator.step()) == ["lens-a", "lens-b"]


def test_a_job_is_launched_once_named_even_before_it_is_waited_on(tmp_path):
    orchestrator = Orchestrator(new_run(tmp_path), NamedBeforeWaited())

    assert names(orchestrator.step()) == ["first", "second"]


def test_paths_of_unequal_length_advance_round_by_round(tmp_path):
    agent = ScriptedAgent(Orchestrator(new_run(tmp_path), UnequalPaths()))

    results = agent.run()

    assert [names(result) for result in results[:-1]] == [
        ["long-first", "short"],
        ["long-second"],
    ]
    assert isinstance(results[-1], Done)


def test_a_whole_run_launches_each_job_once(tmp_path):
    agent = ScriptedAgent(Orchestrator(new_run(tmp_path), TwoLenses()))

    results = agent.run()

    assert isinstance(results[-1], Done)
    assert agent.launched == ["lens-a", "lens-b", "reconcile"]


def test_a_handout_names_a_prompt_file_that_carries_the_whole_task(tmp_path):
    orchestrator = Orchestrator(new_run(tmp_path), OneJob())

    (handout,) = orchestrator.step().jobs
    prompt = handout.prompt_path.read_text(encoding="utf-8")

    assert "Apply only to the source." in prompt
    assert str(handout.output_path) in prompt
    assert str(handout.problem_path) in prompt
    assert handout.output_path == tmp_path / "run" / "only.md"


def test_wait_returns_the_accepted_outputs_in_the_order_asked(tmp_path):
    seen = []

    class ReadsResults(Workflow):
        def run(self, ctx):
            second, first = ctx.wait(ctx.agent(lens_job("second")), ctx.agent(lens_job("first")))
            seen.append((second.name, first.name))

    run_dir = new_run(tmp_path)
    results = ScriptedAgent(Orchestrator(run_dir, ReadsResults())).run()

    assert isinstance(results[-1], Done)
    assert seen == [("second.md", "first.md")]


def test_parallel_returns_what_each_path_returned(tmp_path):
    seen = []

    class ReadsPaths(Workflow):
        def run(self, ctx):
            seen.append(
                ctx.parallel(
                    lambda: ctx.agent(lens_job("first")).wait().name,
                    lambda: "no job on this path",
                )
            )

    results = ScriptedAgent(Orchestrator(new_run(tmp_path), ReadsPaths())).run()

    assert isinstance(results[-1], Done)
    assert seen == [["first.md", "no job on this path"]]


def test_a_definition_that_catches_exceptions_does_not_swallow_a_wait(tmp_path):
    reached = []

    class CatchesBroadly(Workflow):
        def run(self, ctx):
            try:
                ctx.agent(lens_job("only")).wait()
            except Exception:  # noqa: BLE001 - the broad catch is what the test is about
                reached.append("swallowed")
            reached.append("after the wait")

    result = Orchestrator(new_run(tmp_path), CatchesBroadly()).step()

    assert names(result) == ["only"]
    assert reached == []


# 2. Replay


def test_replay_continues_past_accepted_outputs(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, TwoLenses())).round()

    # A fresh orchestrator stands for a fresh process and a fresh session.
    assert names(Orchestrator(run_dir, TwoLenses()).step()) == ["reconcile"]


def test_step_on_a_finished_run_reports_done_again(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, TwoLenses())).run()

    assert isinstance(Orchestrator(run_dir, TwoLenses()).step(), Done)
    assert isinstance(Orchestrator(run_dir, TwoLenses()).step(), Done)


def test_step_repeated_without_workers_names_the_same_jobs(tmp_path):
    orchestrator = Orchestrator(new_run(tmp_path), TwoLenses())

    assert names(orchestrator.step()) == names(orchestrator.step())


# 3. Job identity


def test_job_identity_does_not_depend_on_the_order_of_paths(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, TwoLenses())).round()

    assert names(Orchestrator(run_dir, TwoLensesReversed()).step()) == ["reconcile"]


def test_launch_order_does_not_depend_on_the_order_of_paths(tmp_path):
    first = Orchestrator(new_run(tmp_path / "a"), TwoLenses()).step()
    second = Orchestrator(new_run(tmp_path / "b"), TwoLensesReversed()).step()

    assert names(first) == names(second)


def test_one_name_for_two_different_jobs_is_a_definition_error(tmp_path):
    class Clash(Workflow):
        def run(self, ctx):
            ctx.agent(lens_job("same"))
            ctx.agent(Job(name="same", prompt="Another task.", output="other.md"))

    with pytest.raises(DefinitionError, match="same"):
        Orchestrator(new_run(tmp_path), Clash()).step()


def test_naming_the_same_job_twice_gives_the_same_handle(tmp_path):
    class Twice(Workflow):
        def run(self, ctx):
            assert ctx.agent(lens_job("same")) is ctx.agent(lens_job("same"))

    assert names(Orchestrator(new_run(tmp_path), Twice()).step()) == ["same"]


# 4. to 6. Acceptance ties one input state to one output


def test_changing_a_declared_input_reopens_an_accepted_job(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")

    assert names(Orchestrator(run_dir, OneJob()).step()) == ["only"]


def test_changing_the_prompt_reopens_an_accepted_job(tmp_path):
    class Reworded(Workflow):
        def run(self, ctx):
            job = lens_job("only")
            ctx.agent(
                Job(
                    name=job.name,
                    prompt="Apply only to the source, briefly.",
                    output=job.output,
                    inputs=job.inputs,
                    validator=job.validator,
                )
            ).wait()

    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    assert names(Orchestrator(run_dir, Reworded()).step()) == ["only"]


def test_an_output_is_refused_when_an_input_changed_after_hand_out(tmp_path):
    run_dir = new_run(tmp_path)

    def slow_worker(handout):
        # The input changes while the worker runs; the output is from the old input.
        (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
        write_valid(handout)

    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), {"only": slow_worker})
    agent.round()

    result = Orchestrator(run_dir, OneJob()).step()

    assert names(result) == ["only"]
    assert not (run_dir / "only.md").exists()


def test_a_refused_output_cannot_be_accepted_later(tmp_path):
    run_dir = new_run(tmp_path)

    def slow_worker(handout):
        (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
        write_valid(handout)

    ScriptedAgent(Orchestrator(run_dir, OneJob()), {"only": slow_worker}).round()
    # The job is handed out again, and this time no worker writes anything.
    ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_nothing).round()

    assert not isinstance(Orchestrator(run_dir, OneJob()).step(), Done)


def test_changing_an_accepted_output_reopens_the_job(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (run_dir / "only.md").write_text("# written later by someone else\n", encoding="utf-8")

    assert names(Orchestrator(run_dir, OneJob()).step()) == ["only"]
    assert not (run_dir / "only.md").exists()


def test_removing_an_accepted_output_reopens_the_job(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (run_dir / "only.md").unlink()

    assert names(Orchestrator(run_dir, OneJob()).step()) == ["only"]


# 7. and 8. Retry, then the blocked outcome


def test_an_invalid_output_is_handed_out_once_more_with_the_message(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)
    (first,) = agent.round().jobs

    (second,) = agent.round().jobs

    assert second.name == "only"
    assert second.attempt == first.attempt + 1
    assert "output must start with a level-one heading" in second.prompt_path.read_text(
        encoding="utf-8"
    )


def test_a_valid_retry_is_accepted(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid).round()

    results = ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    assert isinstance(results[-1], Done)


def test_a_second_invalid_output_gives_a_blocked_outcome(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)

    results = agent.run()

    assert agent.launched == ["only", "only"]
    block = one_block(results[-1])
    assert block.subject == "only"
    assert block.permitted == "repair"
    assert block.scope == OneJob.repair_scope
    record = block.record_path.read_text(encoding="utf-8")
    assert "output must start with a level-one heading" in record


def test_a_blocked_step_hands_out_nothing(tmp_path):
    class OneBadOneWaiting(Workflow):
        def run(self, ctx):
            ctx.wait(ctx.agent(lens_job("bad")), ctx.agent(lens_job("slow")))

    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(
        Orchestrator(run_dir, OneBadOneWaiting()),
        {"bad": write_problem("the source is unreadable"), "slow": write_nothing},
    )
    agent.round()

    assert one_block(agent.round()).subject == "bad"
    assert agent.launched == ["bad", "slow"]


def test_a_repair_that_puts_a_valid_output_in_place_is_accepted(tmp_path):
    run_dir = new_run(tmp_path)
    checked = []

    def validator(path):
        checked.append(path.read_text(encoding="utf-8"))
        return has_heading(path)

    class Counted(Workflow):
        def run(self, ctx):
            job = lens_job("only")
            ctx.agent(
                Job(job.name, job.prompt, job.output, job.inputs, validator=validator)
            ).wait()

    def misnamed(handout):
        handout.output_path.with_name("wrong-name.md").write_text("# only\n", encoding="utf-8")

    agent = ScriptedAgent(Orchestrator(run_dir, Counted()), default=misnamed)
    assert isinstance(agent.run()[-1], Blocked)

    # The repair: the agent orchestrator renames the file. It writes no content.
    (run_dir / "wrong-name.md").rename(run_dir / "only.md")

    assert isinstance(Orchestrator(run_dir, Counted()).step(), Done)
    assert checked == ["# only\n"]


def test_a_repair_cannot_get_an_invalid_output_accepted(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_nothing)
    assert isinstance(agent.run()[-1], Blocked)

    (run_dir / "only.md").write_text("no heading\n", encoding="utf-8")

    assert names(Orchestrator(run_dir, OneJob()).step()) == ["only"]


def test_step_after_a_block_hands_the_job_out_again(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)
    assert isinstance(agent.run()[-1], Blocked)

    results = ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    assert isinstance(results[-1], Done)


def test_at_the_repair_limit_the_block_permits_only_stopping(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)

    first = one_block(agent.run()[-1])
    second = one_block(agent.run()[-1])

    assert OneJob.repair_limit == 1
    assert first.permitted == "repair"
    assert second.permitted == "stop"


def test_a_stopped_job_stays_stopped(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)
    agent.run()
    agent.run()
    launched = list(agent.launched)

    again = one_block(Orchestrator(run_dir, OneJob()).step())

    assert again.permitted == "stop"
    assert agent.launched == launched


def test_acceptance_resets_the_repair_count(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid).run()
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)

    assert one_block(agent.run()[-1]).permitted == "repair"


# 9. and 10. Missing outputs and problem reports


def test_a_missing_output_makes_step_name_the_job_again(tmp_path):
    agent = ScriptedAgent(Orchestrator(new_run(tmp_path), OneJob()), default=write_nothing)
    agent.round()

    assert names(agent.round()) == ["only"]


def test_a_job_whose_output_stays_missing_blocks(tmp_path):
    agent = ScriptedAgent(Orchestrator(new_run(tmp_path), OneJob()), default=write_nothing)

    block = one_block(agent.run()[-1])

    assert agent.launched == ["only", "only"]
    assert "no output" in block.reason


def test_a_problem_report_blocks_at_once_and_is_shown(tmp_path):
    agent = ScriptedAgent(
        Orchestrator(new_run(tmp_path), OneJob()),
        default=write_problem("the source names a file that does not exist"),
    )

    block = one_block(agent.run()[-1])

    assert agent.launched == ["only"]
    assert "the source names a file that does not exist" in block.record_path.read_text(
        encoding="utf-8"
    )


def test_a_problem_report_does_not_block_again_after_the_repair(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(
        Orchestrator(run_dir, OneJob()), default=write_problem("cannot read the source")
    ).run()

    results = ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    assert isinstance(results[-1], Done)
    assert not (run_dir / "only.problem.md").exists()


# 11. Reports


def test_a_report_is_kept_and_shown_in_the_failure_record(tmp_path):
    run_dir = new_run(tmp_path)
    orchestrator = Orchestrator(run_dir, OneJob())
    agent = ScriptedAgent(orchestrator, default=write_nothing)
    agent.round()
    orchestrator.report("launch-failed", job="only", text="harness: rate limit reached")

    block = one_block(agent.run()[-1])

    assert "harness: rate limit reached" in block.record_path.read_text(encoding="utf-8")


def test_a_report_survives_the_session_that_made_it(tmp_path):
    run_dir = new_run(tmp_path)
    Orchestrator(run_dir, OneJob()).report("stop", text="handing the run to the operator")

    reports = Orchestrator(run_dir, OneJob()).reports()

    assert [(report.event, report.text) for report in reports] == [
        ("stop", "handing the run to the operator")
    ]


def test_a_report_never_causes_an_acceptance(tmp_path):
    orchestrator = Orchestrator(new_run(tmp_path), OneJob())
    agent = ScriptedAgent(orchestrator, default=write_nothing)
    agent.round()

    orchestrator.report("repair", job="only", text="the output is in place and valid")

    assert names(agent.round()) == ["only"]


def test_an_unlisted_event_is_refused(tmp_path):
    orchestrator = Orchestrator(new_run(tmp_path), OneJob())

    with pytest.raises(ValueError, match="finished"):
        orchestrator.report("finished", job="only")


def test_a_report_does_not_advance_the_run(tmp_path):
    run_dir = new_run(tmp_path)
    orchestrator = Orchestrator(run_dir, OneJob())
    (first,) = orchestrator.step().jobs

    orchestrator.report("launch-failed", job="only", text="refused")
    (second,) = orchestrator.step().jobs

    assert second.attempt == first.attempt + 1


# 12. Steps with effects outside the run directory


class Interrupted(BaseException):
    """Stands for the process ending: nothing after it runs, nothing is recorded."""


class Publishes(Workflow):
    """Publishes once the job is accepted."""

    def __init__(self, published, *, interrupt=False, recognizable=True):
        super().__init__()
        self.published = published
        self.interrupt = interrupt
        self.recognizable = recognizable

    def publish(self):
        self.published.append("published")
        if self.interrupt:
            raise Interrupted

    def was_published(self):
        return bool(self.published)

    def run(self, ctx):
        ctx.agent(lens_job("only")).wait()
        ctx.effect(
            "publish",
            self.publish,
            happened=self.was_published if self.recognizable else None,
        )


def test_an_effect_runs_once_across_replays(tmp_path):
    run_dir = new_run(tmp_path)
    published = []

    ScriptedAgent(Orchestrator(run_dir, Publishes(published))).run()
    assert isinstance(Orchestrator(run_dir, Publishes(published)).step(), Done)

    assert published == ["published"]


def test_an_effect_does_not_run_before_the_job_it_follows_is_accepted(tmp_path):
    published = []

    Orchestrator(new_run(tmp_path), Publishes(published)).step()

    assert published == []


def test_an_interrupted_effect_is_recognized_and_not_repeated(tmp_path):
    run_dir = new_run(tmp_path)
    published = []
    ScriptedAgent(Orchestrator(run_dir, Publishes(published))).round()
    with pytest.raises(Interrupted):
        Orchestrator(run_dir, Publishes(published, interrupt=True)).step()

    result = Orchestrator(run_dir, Publishes(published)).step()

    assert isinstance(result, Done)
    assert published == ["published"]


def test_an_interrupted_effect_that_did_not_happen_is_run(tmp_path):
    run_dir = new_run(tmp_path)
    published = []
    ScriptedAgent(Orchestrator(run_dir, Publishes(published))).round()
    with pytest.raises(Interrupted):
        Orchestrator(run_dir, Publishes(published, interrupt=True)).step()
    published.clear()  # the process ended before the effect, not after it

    result = Orchestrator(run_dir, Publishes(published)).step()

    assert isinstance(result, Done)
    assert published == ["published"]


def test_an_interrupted_effect_that_cannot_be_recognized_is_uncertain(tmp_path):
    run_dir = new_run(tmp_path)
    published = []
    ScriptedAgent(Orchestrator(run_dir, Publishes(published, recognizable=False))).round()
    with pytest.raises(Interrupted):
        Orchestrator(
            run_dir, Publishes(published, interrupt=True, recognizable=False)
        ).step()

    result = Orchestrator(run_dir, Publishes(published, recognizable=False)).step()

    assert isinstance(result, Uncertain)
    assert result.effect == "publish"
    assert published == ["published"]
    assert isinstance(
        Orchestrator(run_dir, Publishes(published, recognizable=False)).step(), Uncertain
    )


# Mechanical steps


def test_a_mechanical_step_is_not_shown_to_the_agent_orchestrator(tmp_path):
    ran = []

    class Mechanical(Workflow):
        def run(self, ctx):
            ran.append("prepare")
            (ctx.run_dir / "prepared.md").write_text("prepared\n", encoding="utf-8")
            ctx.agent(lens_job("only")).wait()

    result = Orchestrator(new_run(tmp_path), Mechanical()).step()

    assert ran == ["prepare"]
    assert names(result) == ["only"]


def test_a_failing_mechanical_step_blocks_with_the_error(tmp_path):
    class Breaks(Workflow):
        def run(self, ctx):
            if not (ctx.run_dir / "needed.md").exists():
                raise FileNotFoundError("needed.md is missing")
            ctx.agent(lens_job("only")).wait()

    run_dir = new_run(tmp_path)

    block = one_block(Orchestrator(run_dir, Breaks()).step())

    assert block.subject == "workflow"
    assert block.permitted == "repair"
    assert "needed.md is missing" in block.record_path.read_text(encoding="utf-8")

    (run_dir / "needed.md").write_text("now present\n", encoding="utf-8")
    assert names(Orchestrator(run_dir, Breaks()).step()) == ["only"]


def test_a_mechanical_step_that_keeps_failing_permits_only_stopping(tmp_path):
    class Breaks(Workflow):
        def run(self, ctx):
            raise RuntimeError("still broken")

    run_dir = new_run(tmp_path)

    first = one_block(Orchestrator(run_dir, Breaks()).step())
    second = one_block(Orchestrator(run_dir, Breaks()).step())

    assert (first.permitted, second.permitted) == ("repair", "stop")


def test_an_error_on_one_path_does_not_hide_a_block_on_another(tmp_path):
    class ErrorAndProblem(Workflow):
        def broken(self, ctx):
            ctx.agent(lens_job("first")).wait()
            raise RuntimeError("step after first failed")

        def run(self, ctx):
            ctx.parallel(
                lambda: self.broken(ctx),
                lambda: ctx.agent(lens_job("second")).wait(),
            )

    agent = ScriptedAgent(
        Orchestrator(new_run(tmp_path), ErrorAndProblem()),
        {"second": write_problem("cannot do it")},
    )
    agent.round()

    result = agent.round()

    assert isinstance(result, Blocked)
    assert sorted(block.subject for block in result.blocks) == ["second", "workflow"]


# Job records


@pytest.mark.parametrize("name", ["", "Upper", "has space", "../escape", "a/b"])
def test_a_job_name_must_be_a_plain_identifier(name):
    with pytest.raises(DefinitionError):
        Job(name=name, prompt="Task.", output="out.md")


@pytest.mark.parametrize("output", ["/absolute.md", "../outside.md", ""])
def test_an_output_must_be_inside_the_run_directory(output):
    with pytest.raises(DefinitionError):
        Job(name="job", prompt="Task.", output=output)


def test_a_job_without_a_validator_is_accepted_when_its_output_exists(tmp_path):
    class Unchecked(Workflow):
        def run(self, ctx):
            ctx.agent(Job(name="free", prompt="Write anything.", output="free.md")).wait()

    results = ScriptedAgent(Orchestrator(new_run(tmp_path), Unchecked())).run()

    assert isinstance(results[-1], Done)


def test_launch_parameters_are_passed_through_as_data(tmp_path):
    class WithParameters(Workflow):
        def run(self, ctx):
            ctx.agent(
                Job(
                    name="scoped",
                    prompt="Task.",
                    output="scoped.md",
                    launch={"model": "small", "read": ["source.md"]},
                )
            ).wait()

    (handout,) = Orchestrator(new_run(tmp_path), WithParameters()).step().jobs

    assert handout.launch == {"model": "small", "read": ["source.md"]}
