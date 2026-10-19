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

Phase 4 of the port (2026-10-19) moved the code into the package:
`headless.py` is `src/commonplace/headless/harness.py`, `jobs.py` and
`corrections.py` are `src/commonplace/headless/jobs.py` and `corrections.py`,
`analyse.py` is `src/commonplace/lib/agentic_analysis/workflow.py` (its `start`
and `run` commands are `commonplace-analysis run`), `selftest.py` is
`tests/commonplace/headless/test_jobs.py` and `test_workflow.py` is
`tests/commonplace/agentic_analysis/test_workflow.py`. Their designs are in
the modules' docstrings. What stays here:

- `smoke.py`: one tiny real job per named harness, run after removing API-key
  variables (`OPENAI_API_KEY`, `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY` and
  similar) from the environment, so only subscription logins can serve it.
- `probe.py`: phase 0 of [headless-engine-port](../headless-engine-port/README.md):
  an analyst-like task (read, `rg`, a `commonplace-*` command, skill
  availability) under each harness's permission settings, and the model each
  harness records as used.

Both import the package: run them as `uv run python smoke.py codex pi` and
`uv run python probe.py ...` from this directory; both call real models.

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
- Worker self-validation needs no engine resolver: the prompt section now
  names `{command-path}/commonplace-validate {output} --artifact {artifact}
  --role {role}`, the command the engine's `validate-output` resolved to,
  rendered from frame bindings both routes have (changed 2026-10-19; the
  engine route renders it too).
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
  workflow passes each harness an unattended setting (`UNATTENDED` in
  `workflow.py`: Claude Code `acceptEdits`, codex `workspace-write`, pi
  `approve`), which phase 5's pilot checks against what analysts do.

## Closes when

The operator decides whether to replace the engine. If yes, the decision goes
to an ADR and the code to `src/commonplace/`; either way this directory is then
deleted.
