# Headless analysis workflow

Posed 2026-10-18 by the operator: consider replacing the artifact-run engine
(`src/commonplace/artifactrun/`) and its coordinating agent with a workflow
written as a Python script that launches workers through the harnesses'
headless modes (`claude -p`, `codex exec`, `pi -p`). This workshop drafts the
pieces below the script: the harness adapters, retry logic and a result cache.
The workflow script itself, porting `analyse-agentic-system/plan.yaml`, is the
next step.

Background and the design it simplifies:
[step-program demo](../step-program-demo/README.md). With headless workers, a
model job no longer has to be reported to a coordinator: on a cache miss it is
run, like a code job, so `MISSING`, replay and `step`/`fill` are not needed.
A rerun of the script resumes from the cache.

## Constraint: workers load the project's configuration

Workers run in the prepared worktree with the harness's normal configuration:
the project's AGENTS.md / CLAUDE.md, skills, settings and permissions. That is
what workers get today as sub-agents of a coordinator there. mdflow, whose
process handling the adapters adapt, strips ambient context by default; none
of that isolation is copied.

## Files

- `headless.py`: a worker profile (harness, `launch-model`, effort, optional
  `flags`) and one headless launch per call. Commands are built as mdflow
  builds them: a dictionary of flags (the harness's print-mode defaults, then
  the profile's model and effort, then the profile's own `flags`) becomes
  arguments, with `_subcommand` and `_env` for the builder and variadic flags
  such as `--add-dir` written as `--flag=value` so they cannot swallow the
  prompt. Stdin is closed, the worker's process group is killed on a timeout,
  and a harness session ID is recorded for finding the transcript.
  `run_with_retries` relaunches the same prompt after a nonzero exit, waiting
  30 s and then 120 s, at most two relaunches; the coordinator-era rule that
  relaunched only on three known provider messages was dropped on 2026-10-19,
  since those messages were observed in a launch tool's results, not in
  headless exits. A failed launch whose stdout or stderr contains "usage limit"
  (any case) raises `UsageLimited` without a relaunch. A timeout raises
  `LaunchFailed` at once. `model_used` reads the model the harness recorded
  for a launch: Claude Code's JSON result (`modelUsage`), codex's session file
  (`payload.model`) or pi's (`message.model`).
- `jobs.py`: `Run.ask(job, prompt, outputs, optional, inputs)` writes the
  prompt and each input (`inputs/<name>.md`, listed under "## Inputs") to an
  attempt directory, points the worker at it, and returns the output files'
  contents. Answers are cached by the hash of the prompt, the inputs' sha256
  digests, output names and profile; only successes are stored, each with its
  provenance (profile, the harness-recorded model, session, times) and input
  digests. A failed launch or incomplete result is appended to
  `answers/<key>.failures.jsonl` with its kind (`timeout`, `incomplete` or
  `exit`); a usage-limited launch is not. A worker may write `problem.md`
  instead, which is a result the script decides about (the workflow's
  `problem`; a refusal is code's rejection of a candidate). `Run.checked` is
  the content retry loop: a failing check asks again with the problems in the
  prompt; a timeout or incomplete result asks the same prompt again. Answered
  asks, timeouts and incomplete results count toward the attempt limit,
  including ones from an earlier run of the script; at the limit it raises
  `OutOfAttempts`. A launch that still exits nonzero after its relaunches is
  an environment failure: logged, not counted, and propagated like
  `UsageLimited`, so the script stops and a rerun after the repair or the
  reset resumes from the cache. `Run(max_workers=n)` bounds concurrent launches;
  `gather` runs independent calls in parallel. A `Run` holds an exclusive
  flock on `<root>/lock` until `close()` (it is a context manager); a second
  `Run` on the root raises `RunLocked`. `Run.accept(path, content)` writes an
  accepted output to `artifact/<path>` atomically. Events go to `log.jsonl`.
- `corrections.py`: `correct(run, job, build_prompt, check, outputs, member=,
  refusal=, previous=, attempts=)` asks a producer to answer a refusal over
  its previous outputs under the engine's correction protocol: inputs
  `refusal` and `previous-<name>`, an `answers` output with one `corrected:`
  or `declined:` entry per blocker in order, "corrected" over identical bytes
  refused, and a rejected correction attempt followed by a structural refusal
  that carries the blockers forward over the rejected output. It reuses the
  engine's `correction_findings` and `refusal_findings`, so it needs the
  `commonplace` package; phase 2 of the port moves those functions out of the
  engine.
- `selftest.py`: exercises the three modules with a fake harness; no model is
  called. Run it as `uv run python selftest.py` from this directory, which
  uses the worktree's venv.
- `smoke.py`: one tiny real job per named harness, run after removing API-key
  variables (`OPENAI_API_KEY`, `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY` and
  similar) from the environment, so only subscription logins can serve it.
- `probe.py`: phase 0 of [headless-engine-port](../headless-engine-port/README.md):
  an analyst-like task (read, `rg`, a `commonplace-*` command, skill
  availability) under each harness's permission settings, and the model each
  harness records as used.

Run `uv run python selftest.py` from this directory; `python3 smoke.py codex pi`
calls real models.

## Evidence so far

- The selftest passes (2026-10-18): the built commands for all three
  harnesses, a cache hit, one transient failure retried
  after 30 s, a non-transient failure not relaunched, a refusal, one rejected
  attempt then acceptance, three parallel jobs. Revised 2026-10-19 with the
  simplifications: a nonzero exit is relaunched twice (waits 30 s, 120 s) and
  then propagates without spending an attempt, and a rerun asks again; a
  timed-out first launch succeeds with two attempts and stops with one, and
  a fresh `Run` counts the persisted timeout; incomplete results exhaust the
  attempts; a worker's `problem.md` is returned as a result; the record holds
  the harness-recorded model.
- The extended selftest passes (2026-10-18): an input written and listed
  before the outputs, its digest in the record and the key (changed bytes ask
  again); a job whose first launch fails succeeds with two attempts and stops
  with one, and a fresh `Run` on the same root counts the persisted failure
  and stops without launching; a usage-limited launch is not relaunched,
  leaves no failure record and consumes no attempt; with `max_workers=1`
  three gathered jobs do not overlap (without the limit the fake detects
  overlap); a second `Run` on a held root raises `RunLocked` and succeeds
  after the first closes; `accept` writes and re-writes one artifact file.
  The usage-limit messages are taken from the installed builds' strings; no
  real exhaustion has been observed.
- The correction selftest passes (2026-10-18): a "corrected" answer over
  identical bytes is refused, the retry receives a structural refusal with the
  findings, the carried blockers and the other sections over the rejected
  output and is accepted; one answer for two blockers is refused; an
  unstructured refusal counts as one blocker.
- Worker self-validation needs no engine resolver: the script knows the
  output path, the run's `artifact/` and the role when it composes a prompt,
  so the prompt names `<path-prefix>/commonplace-validate <output>
  --artifact <artifact> --role <role>` directly, the command the engine's
  `validate-output` resolved to. The prompt section changes in phase 4.
- One real `claude -p` job on Haiku (Claude Code 2.1.302) wrote its output file
  and returned its session ID in about 7 s. It ran in a temporary directory with
  `permission-mode: acceptEdits` in the profile's flags; rerun through the
  ported builder with the same result.
- `smoke.py codex pi` passed (2026-10-18) with no API-key variables set:
  codex-cli 0.162.1 and pi 1.3.0, both `gpt-6-luna` at low effort, each wrote
  its output in about 9 s. Codex ran on the ChatGPT login (its session file
  records `plan_type: pro`); pi ran on its `openai` provider's OAuth
  credential. The session ID `_codex_session` reads from codex's events
  matches the rollout file name, and pi created the session with the ID
  passed in `--session-id`.

## Open

- **Permissions.** A headless worker cannot answer a permission prompt. The
  project's settings must allow what analysts do, or the profile passes a
  permission mode; which is right for the worktree is undecided.
- **Status.** A command that summarises `log.jsonl` and the answer cache, to
  replace `commonplace-analysis inspect`.

## Closes when

The operator decides whether to replace the engine. If yes, the decision goes
to an ADR and the code to `src/commonplace/`; either way this directory is then
deleted.
