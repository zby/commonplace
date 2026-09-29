"""What the code orchestrator guarantees, shown without a model.

The numbered sections follow the test list in
kb/work/code-scheduled-workflows/README.md.
"""

from __future__ import annotations

import hashlib
import json

import pytest

from commonplace.workflow import (
    Blocked,
    DefinitionError,
    Done,
    Job,
    Launch,
    Orchestrator,
    Recognition,
    StateError,
    Uncertain,
    Workflow,
)
from tests.commonplace.workflow.definitions import (
    Interrupted,
    NamedBeforeWaited,
    OneJob,
    Publishes,
    PublishesIfDecided,
    ScriptedAgent,
    TwoLenses,
    TwoLensesReversed,
    UnequalPaths,
    has_heading,
    lens_job,
    new_run,
    publications,
    write_invalid,
    write_nothing,
    write_problem,
    write_valid,
)


def names(result):
    assert isinstance(result, Launch), result
    return [handout.name for handout in result.jobs]


def kept(run_dir, text):
    """Whether a file with this content is kept in the state directory."""
    return any(
        path.is_file() and path.read_text(encoding="utf-8") == text
        for path in (run_dir / "workflow-state").rglob("*")
    )


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
    assert str(tmp_path / "run" / "source.md") in prompt
    assert handout.output_path == tmp_path / "run" / "only.md"


def test_wait_returns_the_accepted_outputs_in_the_order_asked(tmp_path):
    seen = []

    class ReadsResults(Workflow):
        def run(self, ctx):
            second, first = ctx.wait(
                ctx.agent(lens_job("second")), ctx.agent(lens_job("first"))
            )
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


def test_step_without_worker_activity_consumes_a_round(tmp_path):
    orchestrator = Orchestrator(new_run(tmp_path), TwoLenses())

    first = orchestrator.step()
    second = orchestrator.step()
    third = orchestrator.step()

    assert names(first) == names(second)
    assert [job.attempt for job in first.jobs] == [1, 1]
    assert [job.attempt for job in second.jobs] == [2, 2]
    assert sorted(block.subject for block in third.blocks) == ["lens-a", "lens-b"]


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


def test_a_validator_built_anew_does_not_make_a_job_differ(tmp_path):
    def job():
        return Job(
            name="same",
            prompt="Task.",
            output="same.md",
            validator=lambda path: has_heading(path),
        )

    class Twice(Workflow):
        def run(self, ctx):
            assert ctx.agent(job()) is ctx.agent(job())

    assert job().same_task_as(job())
    assert names(Orchestrator(new_run(tmp_path), Twice()).step()) == ["same"]


@pytest.mark.parametrize(
    "changed",
    [
        {"prompt": "Another task."},
        {"output": "other.md"},
        {"inputs": ("other-source.md",)},
        {"launch": {"model": "large"}},
    ],
)
def test_a_job_differs_by_what_its_result_depends_on(changed):
    fields = {
        "name": "job",
        "prompt": "Task.",
        "output": "job.md",
        "inputs": ("source.md",),
        "launch": {"model": "small"},
    }

    assert not Job(**fields).same_task_as(Job(**{**fields, **changed}))


def test_a_job_can_be_hashed():
    job = Job(name="job", prompt="Task.", output="job.md", launch={"model": "small"})

    assert {job: "kept"}[job] == "kept"


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


def test_a_changed_validator_reopens_an_accepted_job(tmp_path):
    class Stricter(Workflow):
        def run(self, ctx):
            job = lens_job("only")
            ctx.agent(
                Job(
                    name=job.name,
                    prompt=job.prompt,
                    output=job.output,
                    inputs=job.inputs,
                    validator=lambda path: ["nothing is good enough"],
                )
            ).wait()

    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (handout,) = Orchestrator(run_dir, Stricter()).step().jobs

    assert (handout.name, handout.attempt) == ("only", 2)
    assert not (run_dir / "only.md").exists()
    assert kept(run_dir, "# only\n")


def test_a_changed_validator_gives_a_full_set_of_attempts(tmp_path):
    class Stricter(Workflow):
        def run(self, ctx):
            job = lens_job("only")
            ctx.agent(
                Job(
                    job.name,
                    job.prompt,
                    job.output,
                    job.inputs,
                    validator=lambda path: ["nothing is good enough"],
                )
            ).wait()

    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()
    agent = ScriptedAgent(Orchestrator(run_dir, Stricter()))

    assert isinstance(agent.run()[-1], Blocked)
    assert agent.launched == ["only", "only"]


def test_the_first_declaration_of_a_job_supplies_its_validator(tmp_path):
    class TwoValidators(Workflow):
        def run(self, ctx):
            first = ctx.agent(lens_job("same"))
            job = lens_job("same")
            second = ctx.agent(
                Job(
                    job.name,
                    job.prompt,
                    job.output,
                    job.inputs,
                    validator=lambda path: ["nothing is good enough"],
                )
            )
            assert first is second
            first.wait()

    results = ScriptedAgent(Orchestrator(new_run(tmp_path), TwoValidators())).run()

    assert isinstance(results[-1], Done)


def test_a_moved_run_directory_keeps_its_acceptances(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, TwoLenses())).run()

    moved = run_dir.rename(tmp_path / "moved")

    assert isinstance(Orchestrator(moved, TwoLenses()).step(), Done)


def test_an_absolute_input_inside_the_run_directory_survives_a_move(tmp_path):
    class ReadsByAbsolutePath(Workflow):
        def run(self, ctx):
            ctx.agent(
                Job(
                    name="only",
                    prompt="Task.",
                    output="only.md",
                    inputs=(str(ctx.run_dir / "source.md"),),
                    validator=has_heading,
                )
            ).wait()

    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, ReadsByAbsolutePath())).run()

    moved = run_dir.rename(tmp_path / "moved")

    assert isinstance(Orchestrator(moved, ReadsByAbsolutePath()).step(), Done)


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
    assert kept(run_dir, "# only\n")


def test_a_refused_output_cannot_be_accepted_later(tmp_path):
    run_dir = new_run(tmp_path)

    def slow_worker(handout):
        (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
        write_valid(handout)

    ScriptedAgent(Orchestrator(run_dir, OneJob()), {"only": slow_worker}).round()
    # The job is handed out again, and this time no worker writes anything.
    ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_nothing).round()

    block = one_block(Orchestrator(run_dir, OneJob()).step())

    assert "no output" in block.reason
    assert not (run_dir / "only.md").exists()


def test_a_refusal_for_a_changed_input_counts_as_a_failed_attempt(tmp_path):
    run_dir = new_run(tmp_path)
    changes = iter(["first change\n", "second change\n"])

    def slow_worker(handout):
        (run_dir / "source.md").write_text(next(changes), encoding="utf-8")
        write_valid(handout)

    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), {"only": slow_worker})

    block = one_block(agent.run()[-1])

    assert agent.launched == ["only", "only"]
    assert "input changed" in block.reason


def test_changing_an_accepted_output_reopens_the_job(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (run_dir / "only.md").write_text(
        "# written later by someone else\n", encoding="utf-8"
    )

    assert names(Orchestrator(run_dir, OneJob()).step()) == ["only"]
    assert not (run_dir / "only.md").exists()
    assert kept(run_dir, "# written later by someone else\n")


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
    # The prompt file of the retry carries the validator's message. The input
    # state does not, so the acceptance holds when the definition runs again.
    assert isinstance(Orchestrator(run_dir, OneJob()).step(), Done)


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
        handout.output_path.with_name("wrong-name.md").write_text(
            "# only\n", encoding="utf-8"
        )

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


def test_the_retry_limit_starts_over_after_a_blocked_outcome(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)

    agent.run()
    assert agent.launched == ["only", "only"]
    agent.run()

    assert OneJob.retry_limit == 1
    assert agent.launched == ["only", "only", "only", "only"]


def test_a_stopped_job_stays_stopped(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)
    agent.run()
    agent.run()
    launched = list(agent.launched)

    again = one_block(Orchestrator(run_dir, OneJob()).step())

    assert again.permitted == "stop"
    assert agent.launched == launched


def stopped_job(tmp_path):
    """A run whose only job has used up its repairs. Returns the run directory."""
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)
    agent.run()
    assert one_block(agent.run()[-1]).permitted == "stop"
    return run_dir


def test_the_operator_releases_a_stopped_job_and_the_run_continues(tmp_path):
    run_dir = stopped_job(tmp_path)

    Orchestrator(run_dir, OneJob()).release("only")
    results = ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    assert isinstance(results[-1], Done)


def test_a_released_job_has_its_attempts_and_repairs_again(tmp_path):
    run_dir = stopped_job(tmp_path)

    Orchestrator(run_dir, OneJob()).release("only")
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)
    block = one_block(agent.run()[-1])

    assert agent.launched == ["only", "only"]
    assert block.permitted == "repair"


def test_a_release_leaves_accepted_outputs_alone(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, TwoLenses()), {"lens-b": write_invalid})
    agent.run()
    assert one_block(agent.run()[-1]).permitted == "stop"

    Orchestrator(run_dir, TwoLenses()).release("lens-b")
    repaired = ScriptedAgent(Orchestrator(run_dir, TwoLenses()))
    results = repaired.run()

    assert isinstance(results[-1], Done)
    assert repaired.launched == ["lens-b", "reconcile"]


def test_only_a_stopped_subject_can_be_released(tmp_path):
    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)
    assert one_block(agent.run()[-1]).permitted == "repair"

    with pytest.raises(ValueError, match="only"):
        Orchestrator(run_dir, OneJob()).release("only")
    with pytest.raises(ValueError, match="never-named"):
        Orchestrator(run_dir, OneJob()).release("never-named")


def test_a_reopened_job_gets_a_full_set_of_attempts(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)

    assert isinstance(agent.run()[-1], Blocked)
    assert agent.launched == ["only", "only"]


def test_acceptance_resets_the_repair_count(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid).run()
    ScriptedAgent(Orchestrator(run_dir, OneJob())).run()

    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid)

    assert one_block(agent.run()[-1]).permitted == "repair"


# 9. and 10. Missing outputs and problem reports


def test_a_missing_output_makes_step_name_the_job_again(tmp_path):
    agent = ScriptedAgent(
        Orchestrator(new_run(tmp_path), OneJob()), default=write_nothing
    )
    agent.round()

    assert names(agent.round()) == ["only"]


def test_a_job_whose_output_stays_missing_blocks(tmp_path):
    agent = ScriptedAgent(
        Orchestrator(new_run(tmp_path), OneJob()), default=write_nothing
    )

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


def test_a_problem_report_blocks_even_when_an_output_was_written(tmp_path):
    def both(handout):
        write_valid(handout)
        handout.problem_path.write_text("the result is a guess", encoding="utf-8")

    run_dir = new_run(tmp_path)
    agent = ScriptedAgent(Orchestrator(run_dir, OneJob()), default=both)

    block = one_block(agent.run()[-1])

    assert agent.launched == ["only"]
    assert "problem" in block.reason
    assert not (run_dir / "only.md").exists()
    assert kept(run_dir, "# only\n")
    assert kept(run_dir, "the result is a guess")
    # The flagged output is not accepted after the repair; the job is handed out.
    assert names(Orchestrator(run_dir, OneJob()).step()) == ["only"]


@pytest.mark.parametrize(
    ("output", "problem"),
    [
        ("lens-a.md", "lens-a.problem.md"),
        ("result", "result.problem.md"),
        ("a.tar.gz", "a.tar.problem.md"),
        ("sub/dir/x.md", "sub/dir/x.problem.md"),
    ],
)
def test_the_problem_report_is_named_after_the_output(tmp_path, output, problem):
    job = Job(name="job", prompt="Task.", output=output)

    assert job.output_path(tmp_path) == tmp_path / output
    assert job.problem_path(tmp_path) == tmp_path / problem


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

    assert "harness: rate limit reached" in block.record_path.read_text(
        encoding="utf-8"
    )


def test_a_report_survives_the_session_that_made_it(tmp_path):
    run_dir = new_run(tmp_path)
    Orchestrator(run_dir, OneJob()).report(
        "stop", text="handing the run to the operator"
    )

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


def publisher(tmp_path, **params):
    return Publishes({"target": str(tmp_path / "published"), **params})


def end_the_process(tmp_path, when):
    marker = tmp_path / "marker"
    marker.write_text(f"raise {when}", encoding="utf-8")
    return str(marker)


def interrupted_publication(tmp_path, when, **params):
    """A run whose process ended while publishing. Returns the run directory."""
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).round()
    params["marker"] = end_the_process(tmp_path, when)
    with pytest.raises(Interrupted):
        Orchestrator(run_dir, publisher(tmp_path, **params)).step()
    return run_dir


def test_an_effect_runs_once_across_replays(tmp_path):
    run_dir = new_run(tmp_path)

    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()
    assert isinstance(Orchestrator(run_dir, publisher(tmp_path)).step(), Done)

    assert publications(tmp_path / "published") == 1


def test_an_effect_does_not_run_before_the_job_it_follows_is_accepted(tmp_path):
    Orchestrator(new_run(tmp_path), publisher(tmp_path)).step()

    assert publications(tmp_path / "published") == 0


def test_an_effect_completed_before_the_process_ended_is_not_repeated(tmp_path):
    run_dir = interrupted_publication(tmp_path, "after")

    result = Orchestrator(run_dir, publisher(tmp_path)).step()

    assert isinstance(result, Done)
    assert publications(tmp_path / "published") == 1


def test_an_effect_that_did_not_begin_before_the_process_ended_is_run(tmp_path):
    run_dir = interrupted_publication(tmp_path, "before")

    result = Orchestrator(run_dir, publisher(tmp_path)).step()

    assert isinstance(result, Done)
    assert publications(tmp_path / "published") == 1


def test_an_effect_that_took_place_in_part_is_uncertain(tmp_path):
    run_dir = interrupted_publication(tmp_path, "between")

    result = Orchestrator(run_dir, publisher(tmp_path)).step()

    assert isinstance(result, Uncertain)
    assert result.effect == "publish"
    assert publications(tmp_path / "published") == 1
    assert not (tmp_path / "published" / "index.md").exists()


def test_an_effect_without_a_recognizer_is_uncertain(tmp_path):
    run_dir = interrupted_publication(tmp_path, "after", recognize="none")

    result = Orchestrator(run_dir, publisher(tmp_path, recognize="none")).step()

    assert isinstance(result, Uncertain)
    assert publications(tmp_path / "published") == 1


def test_a_recognizer_that_fails_gives_uncertain(tmp_path):
    run_dir = interrupted_publication(tmp_path, "after")

    result = Orchestrator(run_dir, publisher(tmp_path, recognize="raises")).step()

    assert isinstance(result, Uncertain)
    assert "the published directory cannot be read" in result.detail
    assert publications(tmp_path / "published") == 1


def test_an_uncertain_effect_stays_uncertain(tmp_path):
    run_dir = interrupted_publication(tmp_path, "between")

    Orchestrator(run_dir, publisher(tmp_path)).step()

    assert isinstance(Orchestrator(run_dir, publisher(tmp_path)).step(), Uncertain)
    assert publications(tmp_path / "published") == 1


def test_a_recognizer_is_not_asked_about_an_effect_that_was_recorded(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()

    result = Orchestrator(run_dir, publisher(tmp_path, recognize="raises")).step()

    assert isinstance(result, Done)


def test_an_error_in_an_effect_that_did_not_begin_blocks_and_is_run_after_repair(
    tmp_path,
):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).round()
    marker = tmp_path / "marker"
    marker.write_text("error before", encoding="utf-8")

    block = one_block(
        Orchestrator(run_dir, publisher(tmp_path, marker=str(marker))).step()
    )

    assert block.subject == "workflow"
    assert "publishing failed" in block.record_path.read_text(encoding="utf-8")
    assert isinstance(Orchestrator(run_dir, publisher(tmp_path)).step(), Done)
    assert publications(tmp_path / "published") == 1


def test_an_error_part_way_through_an_effect_blocks_and_is_then_uncertain(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).round()
    marker = tmp_path / "marker"
    marker.write_text("error between", encoding="utf-8")

    block = one_block(
        Orchestrator(run_dir, publisher(tmp_path, marker=str(marker))).step()
    )

    assert block.subject == "workflow"
    assert isinstance(Orchestrator(run_dir, publisher(tmp_path)).step(), Uncertain)
    assert publications(tmp_path / "published") == 1


def test_an_error_in_an_effect_blocks_even_when_the_definition_catches_it(tmp_path):
    class CatchesBroadly(Publishes):
        def run(self, ctx):
            ctx.agent(lens_job("only")).wait()
            try:
                self.declare(ctx)
            except Exception:  # noqa: BLE001, S110 - the broad catch is what the test is about
                pass

    run_dir = new_run(tmp_path)
    params = {"target": str(tmp_path / "published")}
    ScriptedAgent(Orchestrator(run_dir, CatchesBroadly(params))).round()
    marker = tmp_path / "marker"
    marker.write_text("error before", encoding="utf-8")

    block = one_block(
        Orchestrator(run_dir, CatchesBroadly({**params, "marker": str(marker)})).step()
    )

    assert block.subject == "workflow"
    assert "publishing failed" in block.record_path.read_text(encoding="utf-8")


def test_a_stopped_workflow_with_a_started_effect_is_uncertain(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).round()
    marker = tmp_path / "marker"
    for _ in range(2):
        marker.write_text("error before", encoding="utf-8")
        last = one_block(
            Orchestrator(run_dir, publisher(tmp_path, marker=str(marker))).step()
        )
    assert (last.subject, last.permitted) == ("workflow", "stop")

    result = Orchestrator(run_dir, publisher(tmp_path)).step()

    assert isinstance(result, Uncertain)
    assert result.effect == "publish"
    assert [block.subject for block in result.blocks] == ["workflow"]
    assert publications(tmp_path / "published") == 0


def test_the_operator_resolves_an_uncertain_effect_as_completed(tmp_path):
    run_dir = interrupted_publication(tmp_path, "between")
    orchestrator = Orchestrator(run_dir, publisher(tmp_path))
    assert isinstance(orchestrator.step(), Uncertain)

    # The operator looked, finished the publication by hand, and says so.
    (tmp_path / "published" / "index.md").write_text("- only.md\n", encoding="utf-8")
    orchestrator.resolve("publish", Recognition.COMPLETED)

    assert isinstance(Orchestrator(run_dir, publisher(tmp_path)).step(), Done)
    assert publications(tmp_path / "published") == 1


def test_the_operator_resolves_an_uncertain_effect_as_absent(tmp_path):
    run_dir = interrupted_publication(tmp_path, "between")
    orchestrator = Orchestrator(run_dir, publisher(tmp_path))
    assert isinstance(orchestrator.step(), Uncertain)

    # The operator removed what was published in part, and says so.
    (tmp_path / "published" / "only.md").unlink()
    orchestrator.resolve("publish", Recognition.ABSENT)

    assert isinstance(Orchestrator(run_dir, publisher(tmp_path)).step(), Done)
    assert publications(tmp_path / "published") == 2
    assert (tmp_path / "published" / "index.md").is_file()


def test_an_uncertain_effect_cannot_be_resolved_as_unknown(tmp_path):
    run_dir = interrupted_publication(tmp_path, "between")
    orchestrator = Orchestrator(run_dir, publisher(tmp_path))
    orchestrator.step()

    with pytest.raises(ValueError, match="unknown"):
        orchestrator.resolve("publish", Recognition.UNKNOWN)


def test_only_an_uncertain_effect_can_be_resolved(tmp_path):
    run_dir = new_run(tmp_path)
    orchestrator = Orchestrator(run_dir, publisher(tmp_path))
    ScriptedAgent(orchestrator).run()

    with pytest.raises(ValueError, match="publish"):
        orchestrator.resolve("publish", Recognition.ABSENT)
    with pytest.raises(ValueError, match="never-named"):
        orchestrator.resolve("never-named", Recognition.COMPLETED)


class PublishesBesideOtherWork(Publishes):
    """One path publishes; an independent path has a job of its own."""

    def run(self, ctx):
        ctx.parallel(
            lambda: ctx.agent(lens_job("other")).wait(),
            lambda: Publishes.run(self, ctx),
        )


def uncertain_beside_other_work(tmp_path, other_worker):
    run_dir = new_run(tmp_path)
    params = {"target": str(tmp_path / "published")}
    agent = ScriptedAgent(
        Orchestrator(run_dir, PublishesBesideOtherWork(params)), {"other": other_worker}
    )
    agent.round()
    marker = end_the_process(tmp_path, "between")
    with pytest.raises(Interrupted):
        Orchestrator(
            run_dir, PublishesBesideOtherWork({**params, "marker": marker})
        ).step()
    return Orchestrator(run_dir, PublishesBesideOtherWork(params))


def test_an_uncertain_step_hands_out_nothing(tmp_path):
    orchestrator = uncertain_beside_other_work(tmp_path, write_nothing)

    assert isinstance(orchestrator.step(), Uncertain)
    assert isinstance(orchestrator.step(), Uncertain)
    orchestrator.resolve("publish", Recognition.COMPLETED)
    (handout,) = orchestrator.step().jobs

    # Handed out once before the effect was uncertain, and once after.
    assert (handout.name, handout.attempt) == ("other", 2)


def test_an_uncertain_step_counts_no_repair(tmp_path):
    orchestrator = uncertain_beside_other_work(tmp_path, write_problem("cannot do it"))

    assert isinstance(orchestrator.step(), Uncertain)
    assert isinstance(orchestrator.step(), Uncertain)
    orchestrator.resolve("publish", Recognition.COMPLETED)

    block = one_block(orchestrator.step())
    assert (block.subject, block.permitted) == ("other", "repair")


def test_an_uncertain_step_keeps_the_blocks_found_with_it(tmp_path):
    orchestrator = uncertain_beside_other_work(tmp_path, write_problem("cannot do it"))

    result = orchestrator.step()

    assert isinstance(result, Uncertain)
    assert [block.subject for block in result.blocks] == ["other"]


SECOND_RESULT = "# only, from the changed source\n"


def published_then_changed(tmp_path):
    """A run that published, and whose job then gave a new result."""
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()
    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")

    def second_result(handout):
        handout.output_path.write_text(SECOND_RESULT, encoding="utf-8")

    agent = ScriptedAgent(
        Orchestrator(run_dir, publisher(tmp_path)), default=second_result
    )
    return run_dir, agent.run()[-1]


def test_a_completed_effect_whose_inputs_changed_stops_the_run(tmp_path):
    run_dir, result = published_then_changed(tmp_path)

    block = one_block(result)
    assert block.subject == "effect publish"
    assert block.permitted == "stop"
    assert publications(tmp_path / "published") == 1
    assert (tmp_path / "published" / "only.md").read_text(
        encoding="utf-8"
    ) == "# only\n"
    assert (
        one_block(Orchestrator(run_dir, publisher(tmp_path)).step()).permitted == "stop"
    )


def test_the_block_on_an_effect_goes_away_when_its_inputs_are_restored(tmp_path):
    run_dir, _ = published_then_changed(tmp_path)

    # The source is put back, and the job gives its first result again.
    (run_dir / "source.md").write_text("source text\n", encoding="utf-8")
    results = ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()

    assert isinstance(results[-1], Done)
    assert publications(tmp_path / "published") == 1


def test_the_operator_has_a_changed_effect_run_again(tmp_path):
    run_dir, _ = published_then_changed(tmp_path)
    orchestrator = Orchestrator(run_dir, publisher(tmp_path))

    # The operator withdrew the publication, and says so.
    for name in Publishes.FILES:
        (tmp_path / "published" / name).unlink()
    orchestrator.resolve("publish", Recognition.ABSENT)

    assert isinstance(orchestrator.step(), Done)
    assert publications(tmp_path / "published") == 2
    assert (tmp_path / "published" / "only.md").read_text(
        encoding="utf-8"
    ) == SECOND_RESULT


def test_the_operator_records_a_changed_effect_as_completed(tmp_path):
    run_dir, _ = published_then_changed(tmp_path)
    orchestrator = Orchestrator(run_dir, publisher(tmp_path))

    # The operator published the new result by hand, and says so.
    (tmp_path / "published" / "only.md").write_text(SECOND_RESULT, encoding="utf-8")
    orchestrator.resolve("publish", Recognition.COMPLETED)

    assert isinstance(orchestrator.step(), Done)
    assert isinstance(Orchestrator(run_dir, publisher(tmp_path)).step(), Done)
    assert publications(tmp_path / "published") == 1


def test_an_effect_is_not_released_but_resolved(tmp_path):
    run_dir, _ = published_then_changed(tmp_path)

    with pytest.raises(ValueError, match="resolve"):
        Orchestrator(run_dir, publisher(tmp_path)).release("effect publish")


def decided(tmp_path, **params):
    return PublishesIfDecided({"target": str(tmp_path / "published"), **params})


def decide(run_dir, decision):
    (run_dir / "decision.md").write_text(f"{decision}\n", encoding="utf-8")


def published_then_withdrawn(tmp_path):
    """A run that published, whose decision then stopped reaching the effect."""
    run_dir = new_run(tmp_path)
    decide(run_dir, "publish")
    assert isinstance(
        ScriptedAgent(Orchestrator(run_dir, decided(tmp_path))).run()[-1], Done
    )
    decide(run_dir, "hold")
    return run_dir


def test_a_completed_effect_no_longer_reached_stops_the_run(tmp_path):
    run_dir = published_then_withdrawn(tmp_path)

    block = one_block(Orchestrator(run_dir, decided(tmp_path)).step())

    assert (block.subject, block.permitted) == ("effect publish", "stop")
    assert (
        one_block(Orchestrator(run_dir, decided(tmp_path)).step()).permitted == "stop"
    )
    assert publications(tmp_path / "published") == 1


def test_an_effect_no_longer_reached_is_checked_only_at_the_definitions_end(tmp_path):
    run_dir = published_then_withdrawn(tmp_path)
    decide(run_dir, "review")

    assert names(Orchestrator(run_dir, decided(tmp_path)).step()) == ["review"]


def test_the_operator_lets_an_effect_no_longer_reached_stand(tmp_path):
    run_dir = published_then_withdrawn(tmp_path)
    orchestrator = Orchestrator(run_dir, decided(tmp_path))
    orchestrator.step()

    orchestrator.resolve("publish", Recognition.COMPLETED)

    assert isinstance(Orchestrator(run_dir, decided(tmp_path)).step(), Done)
    assert publications(tmp_path / "published") == 1


def test_the_operator_withdraws_an_effect_no_longer_reached(tmp_path):
    run_dir = published_then_withdrawn(tmp_path)
    orchestrator = Orchestrator(run_dir, decided(tmp_path))
    orchestrator.step()

    # The operator removed the publication, and says so.
    for name in Publishes.FILES:
        (tmp_path / "published" / name).unlink()
    orchestrator.resolve("publish", Recognition.ABSENT)

    assert isinstance(Orchestrator(run_dir, decided(tmp_path)).step(), Done)
    # Reached again later, the effect runs once more.
    decide(run_dir, "publish")
    assert isinstance(Orchestrator(run_dir, decided(tmp_path)).step(), Done)
    assert publications(tmp_path / "published") == 2


def test_an_interrupted_effect_no_longer_reached_is_uncertain(tmp_path):
    run_dir = new_run(tmp_path)
    decide(run_dir, "publish")
    ScriptedAgent(Orchestrator(run_dir, decided(tmp_path))).round()
    marker = end_the_process(tmp_path, "between")
    with pytest.raises(Interrupted):
        Orchestrator(run_dir, decided(tmp_path, marker=marker)).step()
    decide(run_dir, "hold")

    result = Orchestrator(run_dir, decided(tmp_path)).step()

    assert isinstance(result, Uncertain)
    assert result.effect == "publish"
    assert publications(tmp_path / "published") == 1
    # The operator removed what was published in part, and says so.
    (tmp_path / "published" / "only.md").unlink()
    Orchestrator(run_dir, decided(tmp_path)).resolve("publish", Recognition.ABSENT)
    assert isinstance(Orchestrator(run_dir, decided(tmp_path)).step(), Done)


def test_a_completed_effect_whose_inputs_came_out_the_same_is_kept(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()

    # The job runs again and gives the same bytes as before.
    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
    result = ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()[-1]

    assert isinstance(result, Done)
    assert publications(tmp_path / "published") == 1


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


def test_the_operator_releases_a_stopped_workflow(tmp_path):
    class Breaks(Workflow):
        def run(self, ctx):
            if not (ctx.run_dir / "needed.md").exists():
                raise FileNotFoundError("needed.md is missing")
            ctx.agent(lens_job("only")).wait()

    run_dir = new_run(tmp_path)
    Orchestrator(run_dir, Breaks()).step()
    assert one_block(Orchestrator(run_dir, Breaks()).step()).permitted == "stop"

    Orchestrator(run_dir, Breaks()).release("workflow")

    assert one_block(Orchestrator(run_dir, Breaks()).step()).permitted == "repair"
    (run_dir / "needed.md").write_text("now present\n", encoding="utf-8")
    assert names(Orchestrator(run_dir, Breaks()).step()) == ["only"]


def test_unrelated_failing_steps_each_get_their_repair(tmp_path):
    class TwoPlaces(Workflow):
        def run(self, ctx):
            if not (ctx.run_dir / "first.md").exists():
                raise FileNotFoundError("first.md is missing")
            if not (ctx.run_dir / "second.md").exists():
                raise FileNotFoundError("second.md is missing")

    run_dir = new_run(tmp_path)

    first = one_block(Orchestrator(run_dir, TwoPlaces()).step())
    (run_dir / "first.md").write_text("repaired\n", encoding="utf-8")
    second = one_block(Orchestrator(run_dir, TwoPlaces()).step())
    third = one_block(Orchestrator(run_dir, TwoPlaces()).step())

    assert (first.permitted, second.permitted, third.permitted) == (
        "repair",
        "repair",
        "stop",
    )
    assert "second.md is missing" in second.record_path.read_text(encoding="utf-8")


def test_errors_raised_in_a_shared_helper_are_counted_at_the_definitions_line(tmp_path):
    class TwoReads(Workflow):
        def run(self, ctx):
            # Both errors are raised inside pathlib, at the same line there.
            (ctx.run_dir / "first.md").read_text(encoding="utf-8")
            (ctx.run_dir / "second.md").read_text(encoding="utf-8")

    run_dir = new_run(tmp_path)

    first = one_block(Orchestrator(run_dir, TwoReads()).step())
    (run_dir / "first.md").write_text("repaired\n", encoding="utf-8")
    second = one_block(Orchestrator(run_dir, TwoReads()).step())

    assert (first.permitted, second.permitted) == ("repair", "repair")


def test_a_step_without_failures_resets_the_count_of_a_failing_place(tmp_path):
    class Flaky(Workflow):
        def run(self, ctx):
            if (ctx.run_dir / "broken").exists():
                raise RuntimeError("the environment is broken")
            ctx.agent(lens_job("only")).wait()

    run_dir = new_run(tmp_path)
    (run_dir / "broken").write_text("", encoding="utf-8")
    assert one_block(Orchestrator(run_dir, Flaky()).step()).permitted == "repair"
    (run_dir / "broken").unlink()
    ScriptedAgent(Orchestrator(run_dir, Flaky())).run()

    (run_dir / "broken").write_text("", encoding="utf-8")

    assert one_block(Orchestrator(run_dir, Flaky()).step()).permitted == "repair"


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


# The step's own records


def test_a_step_that_ends_before_its_records_are_written_changes_nothing(tmp_path):
    class EndsAfterJudging(Workflow):
        def run(self, ctx):
            ctx.agent(lens_job("only"))
            raise Interrupted

    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, OneJob()), default=write_invalid).round()

    with pytest.raises(Interrupted):
        Orchestrator(run_dir, EndsAfterJudging()).step()

    assert (run_dir / "only.md").read_text(encoding="utf-8") == "no heading\n"
    (handout,) = Orchestrator(run_dir, OneJob()).step().jobs
    assert handout.attempt == 2


@pytest.mark.parametrize("garbage", ["", "not a record\n"])
def test_unreadable_state_raises_and_repeats_no_effect(tmp_path, garbage):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()
    for path in (run_dir / "workflow-state").rglob("*"):
        if path.is_file():
            path.write_text(garbage, encoding="utf-8")

    with pytest.raises(StateError):
        Orchestrator(run_dir, publisher(tmp_path)).step()

    assert publications(tmp_path / "published") == 1


def test_the_default_repair_scope_excludes_the_state_directory():
    assert "workflow-state/" in Workflow.repair_scope


# Runs made through the constructor


def test_a_run_driven_through_the_constructor_cannot_be_opened(tmp_path):
    run_dir = new_run(tmp_path)
    Orchestrator(run_dir, OneJob()).step()

    with pytest.raises(ValueError, match="not a run"):
        Orchestrator.open(run_dir)


# File ownership


def owns(name, output):
    return Job(name=name, prompt=f"Task {name}.", output=output)


def handed_out(run_dir):
    return sorted(path.name for path in run_dir.rglob("prompt.md"))


@pytest.mark.parametrize(
    ("first", "second"),
    [
        ("lens.md", "lens.md"),
        ("lens.md", "./lens.md"),
        ("lens.md", "lens.problem.md"),
        ("lens.problem.md", "lens.md"),
        ("lens.problem.md", "lens.problem.problem.md"),
    ],
)
def test_a_path_owned_by_two_jobs_is_a_definition_error(tmp_path, first, second):
    class Collides(Workflow):
        def run(self, ctx):
            ctx.agent(owns("first", first))
            ctx.agent(owns("second", second))

    run_dir = new_run(tmp_path)

    with pytest.raises(DefinitionError):
        Orchestrator(run_dir, Collides()).step()
    assert handed_out(run_dir) == []


@pytest.mark.parametrize(
    "output", ["workflow-state/result.md", "./workflow-state/jobs/a.md"]
)
def test_an_output_must_not_be_inside_the_state_directory(output):
    with pytest.raises(DefinitionError):
        owns("job", output)


def test_a_job_may_not_read_the_output_of_a_job_not_yet_accepted(tmp_path):
    class ReadsBeforeWaiting(Workflow):
        def run(self, ctx):
            # Named before the job it reads, so the check cannot rely on order.
            ctx.agent(
                Job(
                    name="second",
                    prompt="Check the first result.",
                    output="second.md",
                    inputs=("first.md",),
                )
            )
            ctx.agent(lens_job("first")).wait()

    run_dir = new_run(tmp_path)

    with pytest.raises(DefinitionError, match="first"):
        Orchestrator(run_dir, ReadsBeforeWaiting()).step()
    assert not (run_dir / "workflow-state").exists() or not any(
        path.name == "prompt.md" for path in (run_dir / "workflow-state").rglob("*")
    )


@pytest.mark.parametrize("own", ["job.md", "./job.md", "job.problem.md"])
def test_a_job_may_not_read_its_own_output(own):
    with pytest.raises(DefinitionError):
        Job(name="job", prompt="Task.", output="job.md", inputs=(own,))


def test_recovery_does_not_move_a_new_output_with_the_same_bytes(tmp_path):
    run_dir = new_run(tmp_path)

    def slow_worker(handout):
        (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
        write_valid(handout)

    ScriptedAgent(Orchestrator(run_dir, OneJob()), {"only": slow_worker}).round()
    # The refused output is kept, and the job is handed out again.
    assert names(Orchestrator(run_dir, OneJob()).step()) == ["only"]
    (kept_copy,) = (run_dir / "workflow-state").rglob("kept/*")
    # The process ended after the move and before the move list was cleared.
    state_path = run_dir / "workflow-state" / "state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state["moves"] = [
        {
            "source": "only.md",
            "target": kept_copy.relative_to(run_dir).as_posix(),
            "sha": hashlib.sha256(b"# only\n").hexdigest(),
        }
    ]
    state_path.write_text(json.dumps(state), encoding="utf-8")
    # The replacement worker gives the same bytes as the refused output.
    (run_dir / "only.md").write_text("# only\n", encoding="utf-8")

    assert isinstance(Orchestrator(run_dir, OneJob()).step(), Done)
    assert (run_dir / "only.md").read_text(encoding="utf-8") == "# only\n"


class ConsumerBehindAnotherWait(Workflow):
    """Names a producer but reaches its consumer through a wait on another job."""

    reached: list[str]

    def run(self, ctx):
        ctx.agent(lens_job("producer"))
        ctx.agent(
            Job(
                name="gate",
                prompt="Open the gate.",
                output="gate.md",
                validator=has_heading,
            )
        ).wait()
        ctx.agent(
            Job(
                name="consumer",
                prompt="Use the producer's result.",
                output="consumer.md",
                inputs=("producer.md",),
                validator=has_heading,
            )
        ).wait()
        self.reached.append("past the consumer")


def test_a_cached_consumer_is_refused_while_its_producer_is_pending(tmp_path):
    run_dir = new_run(tmp_path)
    first = ConsumerBehindAnotherWait()
    first.reached = []
    assert isinstance(ScriptedAgent(Orchestrator(run_dir, first)).run()[-1], Done)

    # The producer's input changes; its old output is still in place.
    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")
    replay = ConsumerBehindAnotherWait()
    replay.reached = []

    with pytest.raises(DefinitionError, match="producer"):
        Orchestrator(run_dir, replay).step()
    assert replay.reached == []


# Job records


@pytest.mark.parametrize(
    "name", ["", "Upper", "has space", "../escape", "a/b", "workflow"]
)
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
            ctx.agent(
                Job(name="free", prompt="Write anything.", output="free.md")
            ).wait()

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


def test_changing_the_launch_parameters_reopens_an_accepted_job(tmp_path):
    class Scoped(Workflow):
        def run(self, ctx):
            ctx.agent(
                Job(
                    name="scoped",
                    prompt="Task.",
                    output="scoped.md",
                    launch={"read": self.params["read"]},
                )
            ).wait()

    run_dir = new_run(tmp_path)
    wide = Scoped({"read": ["source.md", "earlier-analysis.md"]})
    ScriptedAgent(Orchestrator(run_dir, wide)).run()

    narrow = Scoped({"read": ["source.md"]})

    assert isinstance(Orchestrator(run_dir, wide).step(), Done)
    assert names(Orchestrator(run_dir, narrow).step()) == ["scoped"]


def test_launch_parameters_must_be_serializable(tmp_path):
    with pytest.raises(DefinitionError):
        Job(name="job", prompt="Task.", output="out.md", launch={"scope": object()})
