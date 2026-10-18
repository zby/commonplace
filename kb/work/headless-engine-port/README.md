# Port the analysis workflow onto headless workers

Posed 2026-10-18 by the operator: plan porting `analyse-agentic-system` from
the artifact-run engine (`src/commonplace/artifactrun/`, about 4,530 lines)
and its coordinating agent onto a Python workflow script that launches each
worker through a harness's headless mode (`claude -p`, `codex exec`,
`pi -p`). The primitives are drafted and tested in
[headless-analysis](../headless-analysis/README.md); this workshop plans and
tracks the port. The operator asked for the plan; executing each phase is not
yet authorized beyond the probes in phase 0.

## Why headless now

The coordinator was an agent because, until recently, launching workers
programmatically on a subscription was not known to work. On 2026-10-18 one
real job each through `claude -p` (Haiku), `codex exec` and `pi -p` (both
`gpt-6-luna`) wrote its output with no API-key variables in the environment:
Claude Code on the claude.ai Max login, Codex on the ChatGPT login
(`plan_type: pro`), pi on its `openai` OAuth credential
([evidence](../headless-analysis/README.md#evidence-so-far)). With workers
launched from code, the coordinating agent, its driver instruction and the
hand-out/report protocol have no remaining job: scheduling, retries and
judgment become code.

## Constraints

- **Workers load the project's configuration** (operator, 2026-10-18): each
  runs in the prepared worktree with that harness's normal AGENTS.md /
  CLAUDE.md, skills, settings and permissions. No mdflow-style isolation.
- **The workflow's requirements do not change in the port**: roles, inputs,
  output types, acceptance checks, correction and verification rules,
  attempt limits, publication conditions and provenance stay as ADRs 098–117
  state them. A behaviour change is a separate decision, recorded as one.
  [Replaceable workflow orchestrators](../../reference/proposals/replaceable-workflow-orchestrators.md)
  is the frame: requirements portable, machinery replaceable.
- **Batch 22 and earlier runs are not disturbed.** Batch 22's packets in
  [agentic-system-reruns](../agentic-system-reruns/README.md) pin method
  commit `5af51ae1f` and the Pi coordinator route; about 290 prepared
  worktrees hold engine runs, some failed or unintegrated. The port lands on
  main without changing them; a run on the new method needs a deliberate new
  release selection there. Before deleting the engine, confirm how old runs
  are inspected, reset and integrated (phase 6).
- **Compare only same-model runs** when judging equivalence (Luna on pi for
  tests, Sol on Codex for production).

## What stays, what goes

From the engine survey (2026-10-18):

| Engine part | Lines | Fate |
|---|---|---|
| `plan.py`, `compact.py` (plan loading, role expansion into check/apply jobs) | 850 | Replaced by the script; the derived check and apply steps become explicit calls |
| `engine.py`, `run.py`, `store.py` (advance, readiness, records, attempt counting, coverage) | 1,460 | Replaced by `Run.ask`/`checked`/`gather` and the answer cache; coverage becomes an explicit final assertion |
| `handouts.py` (prompt composition) | 300 | Coordinator protocol goes; prompt shape (instruction, bindings, inputs, outputs, prompt section) moves into the script |
| `reset.py`, `inspection.py` | 340 | Replaced by deleting cache entries and a status command over `log.jsonl` |
| `handlers.py`, `checks.py` (check, apply-verification, artifact check, correction protocol) | 440 | Kept as domain logic, re-signed from `CodeAttempt`/`Candidate` to plain values |
| `sources.py`, `effects.py`, `worktree.py` | 1,060 | Kept; mostly already plain-value |

About 3,000 lines go. In `src/commonplace/lib/agentic_analysis/` about
2,260 lines import engine types (`CodeAttempt`, `Run`, `RunStore`,
`Candidate`); their cores already call plain-value functions.

## Gaps in the primitives

Found by comparing the engine with `headless-analysis/jobs.py`; each is
resolved in phase 1 or 2, or deliberately dropped with a reason:

1. **Cache by input content.** The key hashes the prompt only; a prompt that
   names an input file by path would hit a stale answer after that file
   changes. Inputs must enter the key by digest (instructions, upstream
   outputs, type specs).
2. **Corrections as the engine does them.** A rerun receives the previous
   outputs and the blockers and must write an `answers` output with one
   `corrected:`/`declined:` line per blocker; "corrected" with identical
   bytes is rejected. `checked()` only appends problems.
3. **Cross-job verification loops.** A verifier's refusal reruns the authors
   it refused, their checks, then the verifier, all within the attempt
   limits. `checked()` covers one job.
4. **Problem, refusal and failure.** Engine `problem` is a failed attempt
   that counts toward the limit; engine refusals are code judgments; the
   draft's `refusal.md` is a cached result. Map these explicitly, and count
   failed launches and incomplete outputs toward the attempt limit.
5. **Worker identity and provenance.** Publication requires each role's
   attempt record with model and effort and that all workers used one model.
   The engine trusts self-report; headless launches pass `--model`, and the
   harness output or session file may record the model actually used.
6. **Worker self-validation.** The prompt section tells workers to run
   `commonplace-run validate-output <prompt-path>`, which resolves only
   engine hand-outs.
7. **Artifact materialization.** Draft validation reads accepted members in
   the run's `artifact/`; the cache stores outputs only in its records.
8. **Concurrency and locking.** No global worker limit, no cross-process run
   lock.
9. **Usage limits and permissions.** Unknown exhaustion messages; headless
   workers cannot answer permission prompts.

## Plan

Each phase ends with the selected tests passing and a commit.

0. **Probes** (authorized). Find each harness's usage-limit message and exit
   status; choose a permission setting per harness that lets an analyst read,
   write and run `commonplace-*` in a worktree without prompts; check whether
   Claude's JSON result, Codex's events and pi's session record the model
   actually used. Decides gaps 5 and 9.
1. **Primitives** in `headless-analysis`: inputs by digest in the key, a
   correction call matching the engine's protocol, attempt counting that
   includes failures, a worker limit, a run lock, materialized accepted
   outputs, a replacement for `validate-output`. Fake-harness tests for each.
2. **Domain code to plain values.** Re-sign `opening`, `acquire`, the
   declared checks, `apply_verification`, `artifact_check`, `assemble` and
   `publish` in `lib/agentic_analysis/` so the script calls them with bytes
   and paths. The engine keeps working through thin adapters until phase 6,
   so batch work on main is not blocked.
3. **The workflow script.** Port `plan.yaml`'s 14 jobs: opening, acquire,
   boundary (2 attempts, branch on its disposition), runtime then memory,
   epistemic and workflow in parallel, reconciliation, artifact check, report
   verification with its correction loop, memory profile and its
   verification, synthesis and its verification, assemble, publish. Prompts
   are composed from the existing `jobs-engine/*.md` instructions and prompt
   section. A fake-harness end-to-end test drives the complete, blocked and
   out-of-scope branches.
4. **Commands and instructions.** `commonplace-analysis prepare` and
   `integrate` stay; `start` plus the driver become one `run` command;
   `inspect` reads the new records. Rewrite `SKILL.md`; delete
   `drive-a-code-scheduled-run.md` and the Pi coordinator agent if nothing
   else needs them; update `commands.md` and the prompt section.
5. **Equivalence pilot.** Run one system already analysed on the engine,
   same profile, and compare: validation result, accepted members, attempts
   used, corrections, wall time. Operator decides whether differences are
   defects of the port. Then a small batch (3–5 systems) driven by a loop over
   systems.
6. **Retire the engine.** ADR revising 113 and 117 (and 101/106 where run
   start and IDs change). Decide how old worktree runs stay inspectable and
   integrable (likely: their own pinned `.venv`, since `prepare` installs one
   per worktree; verify). Delete `artifactrun/`, its tests, `commonplace-run`,
   and `run_values` in `validate_notes`. Close this workshop and
   `headless-analysis`.

## Phase 2 results (2026-10-18)

The domain code takes plain values; the engine keeps working through thin
adapters. Three extractions, each with its tests and an independent review
of the diff by a fresh agent:

- **Candidate checks** (`artifactrun/checks.py`). `Candidate` carries plain
  values (run directory, layout, relations, type, criteria, run values, the
  declared inputs' bytes); `check_candidate`, `apply_verdict`,
  `artifact_check` and `judgment_scope` return findings and judgments. The
  engine's standard handlers (`artifactrun/handlers.py`) build the candidate
  from the attempt and stage what they return. The analysis's declared
  checks read `Candidate.inputs`.
- **Opening and acquisition** (`lib/agentic_analysis/opening.py`) take the
  parameters, the worker profiles, the run directory and the library.
- **Assembly and publication** (`lib/agentic_analysis/publication.py`) take
  the members by role, the metadata, the acquisition result, a `Provenance`
  per role (coordinator-reported model and effort, worker-reported model and
  effort, the output digest), the layout, type, criteria and run directory.
  The record-structure part of provenance (kind, job, output key) stays in
  the adapter; the headless script will fill `Provenance` from harness
  records (gap 5).

The analysis's engine adapters live in `lib/agentic_analysis/handlers.py`,
which `plan.yaml` names; it also re-exports the publication reset hook,
which the engine looks up beside the handler. Known drift, accepted: when a
run has several defects at once, the adapters may report a different first
error than the old handlers did (provenance structure is now checked before
the boundary classification). A run started before this change has the old
handler paths frozen in its run store; advancing it with this code would call
a plain function with an attempt. Old runs advance with their worktree-local
commands, which pin their own code, so this only bars advancing an old run
from a newer checkout. Full fast suite: 1,591 passed; the slow analysis
tests pass.

## Phase 1 results (2026-10-18)

In `headless-analysis` ([evidence](../headless-analysis/README.md#evidence-so-far)),
with fake-harness selftests for each:

- Gap 1: inputs enter the key by digest; records keep the digests.
- Gap 2: `corrections.py` implements the engine's correction protocol over
  the engine's own `correction_findings` and `refusal_findings`.
- Gap 4: a failed launch or incomplete result is persisted per key and counts
  toward the attempt limit across reruns; a usage-limited launch stops the
  run without counting and without a relaunch (gap 9, usage half; the
  messages are build strings, unobserved in a real exhaustion).
- Gap 6: no resolver; the prompt names the `commonplace-validate` command
  with the output, artifact and role the script already knows.
- Gap 7: `Run.accept` materializes accepted outputs under `artifact/`.
- Gap 8: `Run(max_workers=)` and an exclusive run lock.

Open after phase 1: gap 3 (phase 3), gap 5 (the harness-recorded model is
not yet read into the record) and gap 9's permission half.

## Phase 0 results (2026-10-18)

Probes: `headless-analysis/probe.py`, run in this checkout with outputs in a
scratch directory and no API-key variables, Haiku on Claude Code and
`gpt-6-luna` on Codex and pi, low effort.

- **Unattended work.** All three workers read AGENTS.md, ran `rg`, ran
  `commonplace-validate --help` and listed the `analyse-agentic-system` skill,
  in about 16 s each, with no prompt. Settings that sufficed:
  - Claude Code: `permission-mode: acceptEdits`, the project's
    `Bash(commonplace-*)` allowance, and `add-dir` for a run directory outside
    the checkout (not needed when the run directory is in the worktree).
  - Codex: `sandbox: workspace-write`; writes outside the checkout went to
    the scratch directory under `/tmp`.
  - pi: `--approve`, without which pi ignores project-local files; this is the
    flag that makes a pi worker load the project's configuration, so it
    belongs in the pi defaults.
  Not probed: a denied action (what a headless worker does when a tool is not
  allowed), and runs inside a prepared worktree.
- **Model actually used.** Each harness records it: Claude Code's JSON result
  (`modelUsage`: `claude-haiku-5-5`), Codex's session file (`turn_context`
  payload `model`) and pi's session file (`model` on each reply). This can
  replace the workers' self-reported `worker-identity` (gap 5); the workers
  themselves could not name their model on Codex or pi.
- **Usage limits.** Not triggered; strings in the installed builds only.
  Claude Code 2.1.302 says "Usage limit reached" in several forms; codex-cli
  0.162.1 says "You've hit your usage limit…"; pi passes provider errors
  through and retries HTTP 429 itself with backoff. Proposed rule for phase 1:
  a failed launch whose output contains "usage limit" (any case) stops the run
  as usage-limited instead of retrying, and the operator reruns after the
  reset; the answer cache resumes it. Exit status and stream are unverified.
- **Resumption.** Rerunning the probe returned all three answers from the
  cache without launching a worker.

## For the ADR

Points the ADR retiring the engine must state:

- **Why the step program did not stay simple** (operator, 2026-10-18). With one
  execution thread, a step program is simple: replay the script, and every
  model job is either recorded or the next one to hand out. With parallel
  executions it unravels: several attempts are open at once, so the shared
  run state needs consistency rules for each open attempt, which round it
  belongs to, inputs changing while it runs, results reported late or twice,
  and which workers are known to have stopped. The engine's run lock,
  readiness rules, attempt closing and reset machinery largely exist to
  enforce them.
- **What the headless script keeps of that** (proposed, to confirm in phase
  3). Control flow lives in one process's call stack, and parallel calls share
  only the answer cache, where each entry is written once under its own key.
  The consistency needed reduces to a per-key lock, atomic record writes and
  a run lock against a second process. Whether the verification cascade keeps
  it that small is what phase 3 shows.

## Returns to decision

- After phase 0: if a harness cannot run unattended (permissions or usage
  limits), the port targets the others, and that harness is listed as
  unsupported.
- After phase 3: if the script exceeds about 600 lines of control flow, or
  the verification cascade does not fit plain calls, reconsider a small
  declarative layer before phase 4.
- Phase 5 is the decision point for adoption; nothing in phases 1–3 deletes
  engine code.
- Batch launching (a shell loop over systems) is barred for batch 22; for the
  new method it is the operator's call at phase 5.

## Working arrangement (2026-10-18)

Batches 21 and 22 run from the main checkout at `/home/zby/llm/commonplace`:
each Pi coordinator starts there, loads that checkout's startup files and
calls `commonplace-analysis prepare` through the user-level editable tool,
whose code is that checkout's `src/`. Preparation refuses a launch when any
startup file there differs from the pinned method commit, and a `src/` edit
there is run by the next coordinator. So the port is developed on branch
`headless-port` in the sibling worktree `/home/zby/llm/commonplace-headless`,
created from `b12b855f4`.

- The worktree has its own `.venv` from `uv sync`. Tests run as `uv run
  pytest`. When a command must run the branch's code, call the worktree's
  `.venv/bin/commonplace-*`: this deviates from the rule against project-venv
  paths because the user-level tool is the live coordinators' code and
  [INSTALL.md](../../../INSTALL.md) forbids repointing it during an analysis.
- Merge main into the branch before each phase commit; main advances with
  integration commits from the reruns.
- Land a phase on main by fast-forward merge in the main checkout only while
  no `bash-2x.sh` batch is running. Phase 1 touches only
  `kb/work/headless-analysis/` and may land at any time; phases 2 and 4 change
  `src/` and `SKILL.md` and wait for a gap between batches. A batch script
  captures `HEAD` at start, so the next batch runs the landed method
  deliberately.
- Sessions started in the worktree share the main checkout's auto-memory
  through a symlinked memory directory.

## Closes when

The engine is retired by ADR and its code deleted, or the operator abandons
the port after the pilot. Either way the conclusion goes to an ADR (or a note
on why headless orchestration did not fit) and this directory is deleted.
