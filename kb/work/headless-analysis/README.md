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
  and a harness session ID is recorded for finding the transcript. `run_with_retries` relaunches the same
  prompt only after one of the three provider messages that the analysis
  driver's transient-worker rule lists, waiting 30 s and then 120 s, at most two
  relaunches. Any other failure, including a timeout, raises at once.
- `jobs.py`: `Run.ask(job, prompt, outputs, optional)` writes the prompt to an
  attempt directory, points the worker at it with the driver's current
  launch sentence, and returns the output files' contents. Answers are cached by
  the hash of the prompt, output names and profile; only successes are stored,
  each with its provenance. A worker may write `refusal.md` instead, which is a
  result. `Run.checked` is the content retry loop: a failing check asks again
  with the problems in the prompt, up to the attempt limit, then raises
  `OutOfAttempts`. `gather` runs independent calls in parallel. Events go to
  `log.jsonl`.
- `selftest.py`: exercises both modules with a fake harness; no model is called.
- `smoke.py`: one tiny real job per named harness, run after removing API-key
  variables (`OPENAI_API_KEY`, `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY` and
  similar) from the environment, so only subscription logins can serve it.
- `probe.py`: phase 0 of [headless-engine-port](../headless-engine-port/README.md):
  an analyst-like task (read, `rg`, a `commonplace-*` command, skill
  availability) under each harness's permission settings, and the model each
  harness records as used.

Run `python3 selftest.py` from this directory; `python3 smoke.py codex pi`
calls real models.

## Evidence so far

- The selftest passes (2026-10-18): the built commands for all three
  harnesses, a cache hit, one transient failure retried
  after 30 s, a non-transient failure not relaunched, a refusal, one rejected
  attempt then acceptance, three parallel jobs.
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
- **Domain code.** Whether opening, acquisition, the declared checks, the
  verification gate, assembly and publication take engine inputs (attempt
  records, role addresses, coverage) or plain values is unchecked.
- **Billing and usage limits.** `claude -p`, `codex exec` and pi's `openai`
  provider all run on subscription logins. What each prints when a usage
  window is exhausted is unknown, so the script has no wait-for-reset path.
- **Status.** A command that summarises `log.jsonl` and the answer cache, to
  replace `commonplace-analysis inspect`.

## Closes when

The operator decides whether to replace the engine. If yes, the decision goes
to an ADR and the code to `src/commonplace/`; either way this directory is then
deleted.
