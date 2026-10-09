---
description: "Use when coordinating a prepared analysis run: advance the engine, launch its printed handouts in fresh contexts, report attempt results, and stop on unresolved failures."
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

For a new run, call `commonplace-run advance <run>`. Inspect the exit status,
stdout and stderr; wait for the command to finish before taking another action.
Code runs ready code jobs and prints model handouts, open attempts, stops and
publishability. There is no separate launch/done outcome line.

Source acquisition runs during advance. If its network requirement is known to
be blocked by the sandbox, request approval for that advance command before
running it. Do not perform a standalone clone or fetch as a repair. Approval does
not override a stop or authorize changing recorded state.

For every printed handout:

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
   than weakening it. Select the `launch-model` and effort of the run's worker
   profile explicitly at every launch.
2. Launch all handouts from this advance as one round. Wait until every worker
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
4. Launch the next handouts only as code prints them. Do not choose jobs,
   schedule retries yourself, or advance while a worker from the round is still
   running.

Do not inspect outputs or problem reports to judge workers, repair their prose,
or act on their substantive replies. A short progress update to the operator
is optional; it is not a recorded attempt result.

## Stops and completion

On a stop, uncertain effect, command failure or unrecognized command result,
stop the loop and preserve all evidence. Give the operator the exact output,
exit status and stderr. Do not edit engine records, synthesize acceptance,
force progress or use `judge` as a coordinator bypass. `commonplace-run judge`
is an operator judgment surface, not routine worker-result submission.
Recovery needs a separate operator decision; do not treat a journal label as
proof that an external effect happened or was rolled back.

When advance returns no handouts or open attempts, inspect
`commonplace-analysis report <run>`. If it reports `completed`, return
its output under the skill's reporting rules. A local blocked/out-of-scope result
is not publication. If it is not completed, report the unresolved state rather
than repeatedly advancing or declaring success. `publishable: yes` alone is not
completion or a retained-filesystem audit. Preserve the last advance output:
its invocation-specific stops are not reconstructed by the later report.

## Resume without duplicate workers

Before advancing a run from an earlier session, call
`commonplace-run status <run>`. It reprints open handouts with their original
attempt IDs and prompt paths. Confirm that prior workers have stopped before
launching replacements or closing attempts; ask the operator if this is unknown,
and stop if confirmation is unavailable.

For each open attempt, explicitly settle whether its worker completed, failed,
or never ran. Report completed and failed attempts through the result flags
above. An unlaunched handout may be launched using its exact printed prompt once
no earlier worker can still write it. Do not assume that missing output means
failure or that existing output proves completion. Finish all open handouts of
the round before the next advance. Never fabricate result events to clear them.

Old or mixed run directories are rejected, not resumed or converted. Preserve
them; independently authorized old-evidence handling needs the archived method
checkout. This driver has no compatibility route.
