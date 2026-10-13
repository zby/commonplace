---
description: "Use when coordinating a prepared analysis run: advance the engine, launch its printed hand-outs in fresh contexts, report attempt results, and stop on unresolved failures."
type: types/instruction.md
---

# Drive a code-scheduled run

Let code schedule and judge the analysis; launch only its handed-out workers and
report their completion or failure without doing their work.

`<run>` is the path printed by `commonplace-analysis start`. Run every command from the
prepared worktree with its command directory, as required by
[isolated run setup](./SKILL.md#isolated-run-setup). Use
`<path-prefix>/commonplace-run` and `<path-prefix>/commonplace-analysis` below.
Keep code, method files, lockfile and environment unchanged throughout the run.

## Advance and launch

For a new run, call `commonplace-run advance <run>`. Code runs ready code jobs
and prints model hand-outs, open attempts, stops and publishability. Wait for
each command to finish and inspect its exit status, stdout and stderr before
acting; through a script or tool wrapper, forward the complete result, since
the wrapper's success is not the command's. Exit status 0 means the run
continues, 2 means it stopped, and 1 means the command failed.

Source acquisition runs during advance. If its network requirement is known to
be blocked by the sandbox, request approval for that advance command before
running it. Do not perform a standalone clone or fetch as a repair. Approval does
not override a stop or authorize changing recorded state.

For every printed hand-out:

1. Launch one fresh worker with no parent conversation and this whole message,
   replacing `<prompt-path>` with the exact printed `prompt:` path:

   ```text
   Read the complete invocation at `<prompt-path>` and follow it. Recover any truncated read before proceeding. You may read this supplied prompt file.
   ```

   The generic engine supplies the prompt path; do not construct a path from a
   job name or reuse a prior attempt's prompt. Do not copy its content, add
   context, interpret its feedback, or do the job yourself. Use a harness option
   that excludes parent conversation (for Codex, `fork_turns=none`). If the
   harness cannot provide fresh isolation, report the launch failure rather
   than weakening it. At every launch, either select the `launch-model` and
   effort of the run's worker profile explicitly or verify matching inherited
   settings. Inheritance qualifies only when binding runtime instructions
   establish that workers inherit the coordinator's model and effort, and
   exposed coordinator settings match both profile values. Stop and report a
   launch failure if either value is unknown or mismatched; do not infer a
   match from a successful diagnostic.
2. Launch all hand-outs from this advance as one round. Wait until every worker
   has finished or failed to start before advancing again. Retain the mapping
   between each worker and its exact attempt ID.
3. Report each successful worker completion explicitly, and each launch or
   execution failure explicitly, in the next advance:

   ```bash
   commonplace-run advance <run> \
     --completed <attempt-id> \
     --failed '<failed-attempt-id>=<reason>'
   ```

   Repeat `--completed` and `--failed` as needed for the round; omit absent
   categories. The run's worker profile is its provenance; do not pass
   `--model` or `--effort`. Completion means the worker finished, not that its
   output is accepted. Code judges the submitted bytes. Never launch a worker
   on another model or effort than the profile's.
4. Launch the next hand-outs only as code prints them. Do not choose jobs or
   advance while a worker from the round is still running. The bounded
   transient-worker recovery below is the only caller-authorized exception to
   stopping on an execution failure; code still schedules every retry.

Do not inspect outputs or problem reports to judge workers, repair their prose,
or act on their substantive replies. A short progress update to the operator
is optional; it is not a recorded attempt result.

## Retry transient worker failures when authorized

Preserve useful analytical progress when a provider request fails without
establishing a task defect. One transient worker failure should not discard a
run's completed work when the caller permits a bounded retry. This advice and
authority belong to the run coordinator that launches analysts, not to analysts
or the outer coordinator that schedules whole analyses.

Use this route only when the caller explicitly authorizes bounded transient-worker
retries for this run. Otherwise stop and request a recovery decision. It does not
authorize restarting a failed coordinator or recovering a previously held run.

1. Wait for every worker in the round to return a terminal result. Report all
   completions and failures through the normal `advance` flags first. Preserve
   its exact output, exit status and stderr; do not hide a failed attempt behind
   a retry or label it completed because a partial file exists.
2. Retry only if every stop from that advance identifies a model-worker attempt
   whose terminal tool result reports one of these provider failures:
   - `Our servers are currently overloaded. Please try again later.`
   - `An error occurred while processing your request.` followed by the provider's
     retry/help-center message and request ID.
   - `OpenAI Responses stream ended before a terminal response event`.
   Match the provider failure, not an analyst's quoted text or a problem report
   containing those words. Unknown failures, launch/configuration errors,
   content-validation failures, semantic refusals, code-job failures, uncertain
   effects and command failures do not qualify. A provider error is not proof
   that a live worker terminated; use its terminal launch-tool result.
3. Use `commonplace-analysis inspect <run>` to count recorded model-attempt
   failures for each affected job across this run, including earlier rounds.
   Allow at most **two additional launches per job after transient failures**:
   after its first recorded failure, wait 30 seconds; after its second, wait
   120 seconds; after its third, stop. Any earlier non-transient failure of
   that job needs separate recovery authority. Counts do not reset when a
   worker later succeeds or the coordinator context changes. The engine's
   existing `max-attempts` bound also applies and may allow fewer retries;
   do not raise it or modify records to obtain another attempt. Count all
   affected jobs before retrying; if any is ineligible, stop the round.
4. Keep the same run, prepared worktree, frozen source, method, worker profile
   and effort. After the longest required delay for the failed jobs, call
   `commonplace-run advance <run>` without repeating result flags. The engine
   leaves failed model jobs ready, allocates new attempt IDs and prints their
   new hand-outs. Use only those exact printed prompt paths in fresh workers;
   never replay a closed hand-out or change code, sources or accepted reports.
   Code resolves the new attempt's inputs from current run records and retains
   the normal validation and refusal gates. A retry is not acceptance.
5. Follow the normal round rules for all returned hand-outs. If advance stops,
   returns an unexpected result or exhausts a bound, stop and report it. A later
   transient worker failure may use this route only within the remaining bound.
   Disclose failed and replacement attempt IDs in the final report, even if the
   run ultimately publishes. Preserve the recorded errors and request IDs.

This is instruction-level recovery using the existing engine, not a new automatic
retry service. A failure of this run coordinator itself is outside this route;
its parent records the failure, preserves the run and moves to the next eligible
analysis. It does not restart this coordinator under this authority.

## Stops and completion

On any stop outside the authorized transient-worker route, uncertain effect,
command failure or unrecognized command result, stop the loop and preserve all
evidence. Give the operator the exact output, exit status and stderr. Do not edit
engine records, synthesize acceptance, force progress or use `judge` as a
coordinator bypass. `commonplace-run judge` is an operator judgment surface,
not routine worker-result submission. Other recovery needs a separate operator
decision; do not treat a journal label as proof that an external effect happened
or was rolled back.

When advance returns no hand-outs or open attempts, inspect
`commonplace-analysis inspect <run>`. If it reports `completed`, return
its output under the skill's reporting rules. A local blocked/out-of-scope result
is not publication. If it is not completed, report the unresolved state rather
than repeatedly advancing or declaring success. `publishable: yes` alone is not
completion or a retained-filesystem audit. Preserve the last advance output:
its invocation-specific stops are not reconstructed by the later report.

In the final inspection and operator report, disclose retained `worker-problems`,
including completed attempts. Name their attempt IDs and what later evidence
establishes; summarize rather than reproduce long reports. Do not infer recovery
from later completion or publication. A later passing content check does not
establish that the earlier worker performed its required check.

## Resume without duplicate workers

Before advancing a run from an earlier session, call
`commonplace-run status <run>`. It reprints open hand-outs with their original
attempt IDs and prompt paths. Confirm that prior workers have stopped before
launching replacements or closing attempts; ask the operator if this is unknown,
and stop if confirmation is unavailable.

For each open attempt, explicitly settle whether its worker completed, failed,
or never ran. Report completed and failed attempts through the result flags
above. An unlaunched hand-out may be launched using its exact printed prompt once
no earlier worker can still write it. Do not assume that missing output means
failure or that existing output proves completion. Finish all open hand-outs of
the round before the next advance. Never fabricate result events to clear them.

Old or mixed run directories are rejected, not resumed or converted. Preserve
them; independently authorized old-evidence handling needs the archived method
checkout. This driver has no compatibility route.
