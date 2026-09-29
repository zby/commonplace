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
    Interrupted,
    NamedBeforeWaited,
    OneJob,
    Publishes,
    ScriptedAgent,
    TwoLenses,
    TwoLensesReversed,
    UnequalPaths,
    has_heading,
    lens_job,
    new_run,
    on_request,
    publications,
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


def test_a_completed_effect_whose_inputs_changed_stops_the_run(tmp_path):
    run_dir = new_run(tmp_path)
    ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path))).run()

    # The source changes after publication, and the job gives a new result.
    (run_dir / "source.md").write_text("changed source\n", encoding="utf-8")

    def second_result(handout):
        handout.output_path.write_text("# only, from the changed source\n", encoding="utf-8")

    agent = ScriptedAgent(Orchestrator(run_dir, publisher(tmp_path)), default=second_result)
    result = agent.run()[-1]

    block = one_block(result)
    assert block.subject == "effect publish"
    assert block.permitted == "stop"
    assert publications(tmp_path / "published") == 1
    assert (tmp_path / "published" / "only.md").read_text(encoding="utf-8") == "# only\n"
    assert one_block(Orchestrator(run_dir, publisher(tmp_path)).step()).permitted == "stop"


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


@pytest.mark.parametrize("output", ["workflow-state/result.md", "./workflow-state/jobs/a.md"])
def test_an_output_must_not_be_inside_the_state_directory(output):
    with pytest.raises(DefinitionError):
        owns("job", output)


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
