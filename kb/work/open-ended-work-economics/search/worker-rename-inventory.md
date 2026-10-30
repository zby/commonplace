# Inventory: renaming the delegation sense of "worker" to "sub-agent"

Raw material for an operator decision; it decides nothing. It follows step 2
of the [terminology migration method candidate](../../vocabulary-governance/terminology-migration-method-candidate.md):
it classifies occurrences before anyone replaces them. Baseline: the working
tree on 2026-10-30, with HEAD at `123ca2418`. Counts are matching lines from
`rg -i -w 'workers?'` (so `worker_profile`, `WORKER_PROFILES` and
`CommandWorker` are *not* in the `-w` counts; code identifier forms are
counted separately below).

## Summary

**Finding first: the rename is not a one-to-one substitution.** The KB's
delegation-sense "worker" covers three runtimes. Only one of them is a
sub-agent in the KB's own sense, and two accepted texts say that a headless
launch is *not* a sub-agent (ADR 086's worker amendment, and
`test-installed-commonplace`). The largest executable surface,
analyse-agentic-system on Workjig, uses "worker" for exactly the case that
ADR 086 excludes from "sub-agent". See the coincidence analysis below.

To keep that difference visible, class (a) is split by runtime:

- **a-gen**: runtime-neutral delegate. Any agent that receives a handoff
  under a parent's authority (AGENTS.md Delegation, doctrine, instruction
  type).
- **a-sub**: a harness sub-agent, meaning a fresh child context that a
  native tool launches (review batches, ingest drafting, autoreason).
- **a-head**: a headless harness process. This is a one-way subprocess
  launch: analysis workflow workers, `commonplace-task` workers, and the
  installed-test CLI agent.

Matching lines (`-w`), by class and surface. "Prose" means authored, live KB
text, including `tests/scenarios/`.

| Class | Prose (live) | Skills/instructions (subset of prose) | KB data (YAML/schema) | Code `src/` | Tests `tests/commonplace/` | Scripts | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| a-gen | 58 | 13 | — | — | — | — | 58 |
| a-sub | 177 | 97 | — | ~5 (review prompt/strings) | 1 | 1 | ~184 |
| a-head | 162 | 32 (+46 in the analysis method) | — | ~60 (docstrings, help text) | ~25 (docstrings) | 4 | ~251 |
| b ordinary / external | 40 | 0 | — | — | — | — | 40 |
| c identifier / schema | — | — | 14 (+192 frozen `ARTIFACT.yaml` keys, counted in d) | ~60 (code identifiers, CLI flags, metadata keys) | ~37 | — | ~111 |
| d frozen / historical | 3,927 | — | — | — | — | — | 3,927 |

Code splits (a-head versus c) are approximate. The code totals are exact:
`src/commonplace` has 125 `-w` lines in 24 files (160 lines with any form of
`worker`); `tests/commonplace` has 63 `-w` lines in 19 files; `scripts/` has
5 lines in 2 files. `tests/scenarios/` (8 lines) is counted as prose.

Class d breakdown: retained analyses, 3,323 lines in 1,052 files under
`kb/agentic-system-analyses/retained/` (192 of them are `ARTIFACT.yaml`
`worker:` keys); `kb/agentic-systems/reports/`, 349 lines in 124 files; ADRs,
133 lines in 29 files; archived proposals, 55 lines in 8 files; the generated
memory comparisons (`memory-systems.csv`, `memory-systems-table.md`,
`agent-memory-landscape.md`), 66 lines; `agentic-system-analyses/retained-archive`,
1 line.

**Size of a migration that leaves frozen text alone:** about 451 live prose
and KB-data lines in about 115 files, plus about 190 code and test lines in
45 files, with any-form identifier hits on top. The workshop vocabulary row
says "74 files". That figure is lower than the 115 live-prose files found
here, probably because the row came from a narrower search.

## Coincidence analysis (task 3)

### What "sub-agent" means in the KB

- Mechanism sense (theory). [llm-context-is-composed-without-scoping](../../../theory/llm-context-is-composed-without-scoping.md):
  "**Sub-agents** are the canonical architectural move: code outside the LLM
  constructs a fresh flat context". [agent-is-a-tool-loop](../../../theory/agent-is-a-tool-loop.md):
  "A sub-agent is a child loop with its own prompt and capability surface."
  The computational-model tag: "sub-agents are the one isolation mechanism".
  [context-engineering](../../../theory/definitions/context-engineering.md)
  treats sub-agents as "the scoping component". None of these mentions a
  packet, a handoff, or the parent's authority. They name a context-isolation
  structure, not a delegation role.
- Harness-facility sense (reference). [ADR 086](../../../reference/adr/086-projects-read-the-library-from-the-installed-package.md),
  in its worker amendment (2026-10-24): "Skills that need a worker with a
  fresh context use only a sub-agent facility the harness itself provides; a
  headless harness process launched from the shell is not an emulation of
  one". Its reason: "a sub-agent is a two-way, inspectable relationship …
  while a headless launch is a one-way action."
- Role sense (instructions). [instruction type](../../../types/instruction.md):
  "work packets handed to sub-agents". `cp-skill-revise-autoreason`,
  `run-review-batches`, `run-full-improvement-pass-on-note` and `review-code`
  use "sub-agent" for the delegate itself. These are the only places where
  "sub-agent" and the delegation-sense "worker" are used interchangeably.
- No uses of "sub-agent" or "subagent" in `src/commonplace/`.
  `scripts/session-tools.py` uses `subagent` as the Claude Code session-log
  directory name, an external format (class c).

### Where a KB "worker" is not a sub-agent

1. **Analysis workers are headless launches by definition.** [ADR 118](../../../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md):
   "**Workers are headless launches.** A worker is one launch of the run's
   profile's harness in its headless mode". ADR 118 also fixes the term: "The
   words are workflow, run, worker, launch, attempt". [ADR 119](../../../reference/adr/119-analysis-workers-launch-through-workjig.md)
   turns "a worker profile into a Workjig command worker". The
   analyse-agentic-system SKILL: "Each worker is a fresh headless session of
   the profile's harness". Under ADR 086's amendment these are explicitly not
   sub-agents. Renaming them "sub-agent" would contradict ADR 086 and ADR 118.
2. **Workjig's API names them workers.** `workjig.CommandWorker`,
   `Harness.worker()` and `Run(max_workers=n)` are external-library or
   API-mirroring identifiers (`src/commonplace/headless/harness.py`,
   `jobs.py`). Workjig is a separate package (`workjig>=0.2.0`, pyproject).
3. **`commonplace-task` workers.** `src/commonplace/lib/tasks.py`: "asks one
   worker to follow the runbook". This is a headless worker from
   `kb/tasks/profiles.yaml` ("Worker profiles for `commonplace-task run`").
4. **The installed-test agent is explicitly not a sub-agent.**
   `test-installed-commonplace.md`: "Launch each task in a separate process
   with fresh context, not an internal sub-agent or resumed chat". Later in
   the same file: "The worker may use native sub-agents when an installed
   skill requires them." `tests/scenarios/installed/README.md`: "without
   substituting an internal sub-agent". Here the worker and the sub-agent are
   *different and nested*.
5. **`check-subagent-harness` is a misnomer in the other direction.** Its
   filename and heading ("Check a subagent harness") say sub-agent, but its
   body checks "the headless worker launches … as a fresh headless session of
   the worker profile's harness (`claude -p`, `codex exec` or `pi -p`)".
6. **Runtime-neutral spine.** AGENTS.md ("A worker inherits this file … only
   when its runtime loads them") and [Commonplace doctrine](../../../reference/definitions/commonplace-doctrine.md)
   ("the standing instruction a worker inherits … when its runtime loads it")
   cover any runtime, including headless analysis workers. Those workers load
   AGENTS.md from the worktree: `guards.py`, "A worker loads the worktree's
   startup instructions". The spine sense is therefore wider than the
   sub-agent sense.
7. **Instructions offer the two as alternatives.** `cp-skill-ingest`: "Use
   only a harness-provided sub-agent or worker mechanism"; "Launch one newly
   isolated sub-agent or worker". `run-review-batches`: "If the harness
   cannot launch sub-agents or workers". These lines read "worker" as broader
   than, or distinct from, "sub-agent".
8. **No human workers in the delegation sense.** No live text uses "worker"
   for a human delegate. Ordinary senses already in theory are the
   benchmarked contractor or system ([holding-the-client-fixed](../../../theory/holding-the-client-fixed-exports-the-least-warrantable-decisions.md):
   "A fixed-client benchmark measures worker capability"; [warranted-transfer](../../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md):
   "the worker role moved"), external systems (Slate workers, Swamp remote
   workers), and forked instances in `conversation-vs-prompt-refinement`
   ("N workers via KV-cache sharing"). The ordinary sense the operator wants
   to free is therefore already present, in two theory notes and two tag
   READMEs.

### Where "sub-agent" is not a worker in the delegation sense

- The mechanism sense in the theory notes above: an isolated frame, with no
  packet or authority claim.
- RLM's model-written orchestrators "over sub-agents" ([rlm note](../../../theory/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md)).
  The children are spawned by model-authored code, not commissioned by a
  handoff in AGENTS.md's sense.
- External systems' subagents (for example, oh-my-pi "Subagent result" in
  archived reports), and the OpenAI "Responses API subagents" in
  `harness-sub-agent-model-selection-regression.md`.
- ADR 086's "sub-agent facility": the harness capability, not the delegate.

### How the senses differ

The delegation-sense "worker" is a **role**: the receiver of a handoff under
the parent's authority, on any runtime. "Sub-agent" is a **runtime mechanism**:
a child context that the harness launches and keeps a two-way relationship
with (ADR 086), or an isolated frame (theory).

- worker ⊇ sub-agent-launched delegates.
- worker ∖ sub-agent = headless launches: analysis, tasks, installed tests.
- sub-agent ∖ worker = mechanism, external and RLM uses.

A rename to "sub-agent" would be accurate for the a-sub class (about 184
lines). It would be inaccurate for the a-head class (about 251 lines), whose
own ADRs define it against sub-agents. The a-gen spine (58 lines) would
narrow from "any delegate" to "harness child". Possible ways forward (not
evaluated): a role word distinct from both "worker" and "sub-agent", such as
"delegate", for a-gen and a-sub, with a-head keeping "worker" or taking
"headless launch"; or renaming only a-sub and a-gen and accepting that
analysis code and Workjig keep "worker".

## Spine files (change first)

These define or fix the term. A migration would change them before dependent
uses.

| File | Lines | Defines |
|---|---:|---|
| `AGENTS.md` (Delegation) | 1 | worker as runtime-neutral delegate (a-gen) |
| `kb/reference/definitions/commonplace-doctrine.md` | 4 | doctrine relative to "a worker" and "worker runtime" (a-gen) |
| `kb/types/instruction.md` | 3 (+1 "sub-agents") | "consequential-worker handoff", "worker packets", "work packets handed to sub-agents" (a-gen; already mixes both words) |
| `kb/instructions/COLLECTION.md` | 7 | "worker packet as a delta" (a-gen) |
| `kb/reference/control-plane-goals.md` | 4 | "worker packet" baseline (a-gen) |
| `kb/reference/adr/086-…installed-package.md` | 2 | worker amendment: sub-agent ≠ headless launch |
| `kb/reference/adr/118-…headless-harnesses.md` | 14 | "Workers are headless launches"; fixes the word list |
| `kb/reference/adr/119-analysis-workers-launch-through-workjig.md` | 11 | worker profile → Workjig command worker |
| `kb/reference/adr/067-review-workers-read-one-prompt-and-write-one-output.md` | 18 | review-worker boundary (a-sub) |
| `kb/reference/adr/116-one-word-per-concept-across-prose-and-code.md` | 4 | the rule a rename must satisfy: rename code first when surfaces disagree |
| `kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/follow-worker-rules.md` | 5 | the analysis worker contract (a-head) |
| `kb/agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml` | 2 | worker-profile data |
| `kb/agentic-system-analyses/types/agentic-system-analysis-set.md` and `.schema.yaml` | 3 + 1 | `worker` provenance key in published `ARTIFACT.yaml` |
| `kb/theory/llm-context-is-composed-without-scoping.md`, `kb/theory/agent-is-a-tool-loop.md` | 0 worker / several sub-agent | the sub-agent (mechanism) definitions the rename would load |

## Titles, filenames, slugs and anchors (task 4)

These are relocations with redirect consequences. The count is files that
reference the slug, excluding `.claude/worktrees`.

| Path | Kind | Inbound refs |
|---|---|---:|
| `kb/reference/adr/067-review-workers-read-one-prompt-and-write-one-output.md` | filename and H1 | 44 |
| `kb/reference/adr/119-analysis-workers-launch-through-workjig.md` | filename and H1 | 8 |
| `kb/reference/proposals/code-navigation-tool-portfolio-for-analysis-workers.md` | filename and H1 | 3 |
| `kb/reference/proposals/worktree-relative-worker-paths.md` | filename and H1 | 1 |
| `kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/follow-worker-rules.md` | filename and H1; also the `worker-rules` prompt variable in `plan.yaml` | 6 |
| `kb/agentic-system-analyses/instructions/analyse-agentic-system/worker-profiles.yaml` | filename; path constant `WORKER_PROFILES` in `analyses.py` and tests | 13 |
| `kb/reports/retained/analysis-worker-code-navigation-*` (2 files), `dynamic-cheatsheet-worker-instruction-comparison-2026-10-10.md` | retained report filenames (outside scope; frozen) | — |
| `kb/instructions/check-subagent-harness.md` | filename and H1 say "subagent" for headless worker launches | 1 |
| `kb/theory/skill-discovery-re-fires-in-every-sub-agent-context.md` | already "sub-agent"; the architecture tag labels it "Skill discovery re-fires in worker contexts" | 98 |
| `kb/reference/harness-sub-agent-model-selection-regression.md` | already "sub-agent" | 64 |
| `kb/theory/acceptance-authority-does-not-require-a-separate-repair-session.md` | H2 headings "Exact checking can be a worker capability", "A check the worker can repeat …" (anchors) | — |
| `kb/reference/adr/034-…` | H3 "Keep workers hermetic" (anchor) | — |
| `tests/scenarios/ingest-a-source.md` | H3 "Fork 5 — ingest-report drafting worker" | — |
| retained analyses | record-handle anchors such as `#rt-rte-worker` and `#rt-bap-worker` (frozen handles from analysed systems) | — |

## Occurrences by file

Paths are repository-relative. "n" is the number of matching `-w` lines.

### Spine and runtime-neutral prose (a-gen)

| File | n | Note |
|---|---:|---|
| `AGENTS.md` | 1 | Delegation section |
| `kb/types/instruction.md` | 3 | worker packets, consequential-worker handoff |
| `kb/reference/definitions/commonplace-doctrine.md` | 4 | worker runtime |
| `kb/instructions/COLLECTION.md` | 7 | worker packet as delta; `invokes` row |
| `kb/reference/control-plane-goals.md` | 4 | worker packet baseline |
| `kb/instructions/review-design-pressure-behind-recurring-errors.md` | 6 | the worker at the point of deviation |
| `kb/agentic-systems/COLLECTION.md` | 1 | "each worker's required role/type inputs" |
| `kb/reference/README.md` | 1 of 3 | doctrine gloss (the other 2 are a-sub, review) |
| `kb/theory/acceptance-authority-does-not-require-a-separate-repair-session.md` | 22 | orchestrator and worker; "one-way worker session" (fits headless too) |
| `kb/theory/weight-resident-methodologies-compress-behavior-in-context.md` | 2 | worker packets |
| `kb/theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md` | 2 | consequential worker packets |
| `kb/theory/fix-what-the-executor-cant-determine-not-what-it-will.md` | 2 | workers choose |
| `kb/theory/definitions/representational-form.md` | 1 | "can bind a worker" |
| `kb/reference/proposals/tag-maintenance-and-derived-browsing.md`, `type-selected-python-validation-checks.md` | 1 + 1 | maintenance worker; worker's authority |

### Harness sub-agent delegates (a-sub)

| File | n | Note |
|---|---:|---|
| `kb/instructions/cp-skill-ingest/SKILL.md` | 30 | drafting worker; "sub-agent or worker mechanism" |
| `kb/instructions/cp-skill-health-check/SKILL.md` | 17 | worker launch, nesting depth, worker slots |
| `kb/instructions/run-review-batches.md` | 12 | sub-agents and workers interchangeable; `--runner {worker}`, `{worker-model}` placeholders (CLI values) |
| `kb/instructions/cp-skill-write-multistage/SKILL.md` | 8 | fresh workers |
| `kb/instructions/simplification-passes/README.md`, `revise-an-article-or-note.md` | 2 + 6 | worker packet, fresh worker |
| `kb/instructions/fix-warnings/fix-review-warnings-sweep.md` | 5 | single-use worker |
| `kb/instructions/run-full-improvement-pass-on-note.md` | 4 | defines "fresh sub-agent"; "follow-up turn to an earlier worker" |
| `kb/instructions/assess-a-claim-bearing-artifact-against-external-literature.md` | 3 | target-blind source worker |
| `kb/instructions/ingest-paper-with-code.md` | 2 | drafting worker |
| `draft-ingest-report.md`, `example-onboard-second-brain.md`, `FIX-SYSTEM.md`, `re-ingest.md`, `review-triage.md`, `revise-note.md`, `run-compression-bundle-on-note.md`, `scan-agentic-system-transfer/SKILL.md` (all under `kb/instructions/`) | 1 each | fresh or single-use worker; `scan-…` says "invoking worker packet" |
| `kb/reference/review-architecture.md` | 10 | review worker; "external worker" |
| `kb/reference/README-REVIEW-SYSTEM.md` | 10 | "a worker (typically a sub-agent)" |
| `kb/reference/harness-sub-agent-model-selection-regression.md` | 12 | per-worker model overrides |
| `kb/reference/freshness-architecture.md`, `storage-architecture.md` | 1 + 1 | review worker output |
| `kb/reference/README.md` | 2 of 3 | review delegation |
| `kb/reference/commands.md` | ~4 of 15 | review-execution section (external worker, worker-model provenance) |
| `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md` | 10 | drafting worker brief |
| `kb/reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md` | 7 | worker lifecycle |
| `kb/reference/proposals/routine-bilateral-isolation-for-literature-assessment.md` | 1 | source worker |
| `kb/theory/skill-discovery-re-fires-in-every-sub-agent-context.md` | 15 | "a fresh sub-agent worker" (uses both words for one thing) |
| `kb/theory/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md` | 1 | "One fresh worker" (evidence note, describes a run) |
| `kb/tags/architecture-README.md` | 1 | link label "worker contexts" for a sub-agent note |
| `tests/scenarios/ingest-a-source.md` | 5 | drafting worker; H3 heading |

### Headless harness launches (a-head)

| File | n | Note |
|---|---:|---|
| `kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md` | 21 | "fresh headless session"; `--worker-profile`, `--max-workers` |
| `kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/follow-worker-rules.md` | 5 | worker contract |
| `…/jobs/prompt-section.md` | 3 | `worker-rules` variable |
| `…/meta-analyser.md` | 2 | worker prompts, launches |
| `…/worker-profiles.yaml` | 2 | comments |
| `…/plan.yaml` | 2 of 15 | comments ("Every worker …") |
| `kb/agentic-system-analyses/instructions/maintain-analysis-method.md` | 5 | worker inputs |
| `kb/agentic-system-analyses/instructions/publish-analysis.md` | 1 | workers do not load it |
| `kb/agentic-system-analyses/COLLECTION.md` | 3 | analysis workers |
| `kb/agentic-system-analyses/types/agentic-system-analysis-set.md` | 3 | `worker` provenance field |
| `kb/agentic-system-analyses/types/agentic-system-memory-profile.md` | 1 | worker rules |
| `kb/instructions/check-subagent-harness.md` | 21 | worker launches as `claude -p` and similar |
| `kb/instructions/test-installed-commonplace.md` | 8 | CLI process, "not an internal sub-agent" |
| `kb/instructions/test-installed-commonplace-codex.md` | 3 | worker launch settings |
| `kb/reference/commands.md` | ~11 of 15 | `commonplace-task`, `commonplace-analysis` (`--worker-profile`, `--max-workers`) |
| `kb/reference/agentic-system-analysis-design-brief.md` | 3 | worker instructions, worker roles |
| `kb/reference/proposals/code-navigation-tool-portfolio-for-analysis-workers.md` | 17 | title |
| `kb/reference/proposals/replaceable-workflow-orchestrators.md` | 17 | headless workers |
| `kb/reference/proposals/worktree-relative-worker-paths.md` | 16 | title |
| `kb/reference/proposals/workflow-recovery-history.md` | 9 | worker session traces |
| `shared-analysis-contract-conformance.md`, `source-registers-without-duplicated-path-inventories.md`, `temporary-amendments-to-published-analyses.md`, `adopt-declared-layout-in-the-analysis-workflow.md` (under `kb/reference/proposals/`) | 2 + 2 + 1 + 1 | worker rules, analysis workers |
| `tests/scenarios/installed/README.md` | 3 | CLI worker, not a sub-agent |

### Ordinary sense and external systems (b)

| File | n | Note |
|---|---:|---|
| `kb/theory/holding-the-client-fixed-exports-the-least-warrantable-decisions.md` | 8 | benchmarked contractor or system ("worker capability") |
| `kb/theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md` | 1 | "the worker role moved" (economic sense) |
| `kb/tags/evaluation-README.md`, `kb/tags/warranted-autonomy-README.md` | 1 + 1 | the same note's gloss |
| `kb/theory/session-history-should-not-be-the-default-next-context.md` | 2 | Slate workers |
| `kb/theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md` | 1 | N forked workers (external pattern) |
| `kb/theory/research/adaptation-agentic-ai-analysis.md` | 1 | "A worker always runs the same sequence" (generic) |
| `kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs/trace-runtime.md` | 1 | "remote workers" in analysed systems |
| `kb/agentic-systems/reviews/` (swamp 8, ai-agent-book 3, academic-research-skills 2, agno-agentos 1) | 14 | external systems' workers |
| `kb/agentic-systems/reviews-archive/` (enoch 3, oh-my-pi 2, openrsi 2, prime-agent 2, jaz 1) | 10 | external; archived |

### Identifiers and schema (c)

| Location | Identifiers | Effect of a rename |
|---|---|---|
| `plan.yaml` | criteria group key `worker:` (12 references `criteria: [worker…]`); prompt variable `worker-rules` | plan data and composed prompts |
| `agentic-system-analysis-set.schema.yaml` and the 192 frozen `ARTIFACT.yaml` files under `retained/` (also 16 under `kb/work/agentic-system-completion/evidence/`) | `worker:` provenance key | file format of published analyses; `publication.py` validates manifests against it |
| `src/commonplace/lib/agentic_analysis/` (`analyses.py`, `opening.py`, `worktree.py`, `workflow.py`, `publication.py`, `audit.py`) | `WORKER_PROFILES`, `resolve_worker_profile`, `worker_profile`, `DEFAULT_WORKER_PROFILE`, parameter key `"worker-profile"`, metadata key `"worker"`, audit reads Workjig `request["worker"]` | run parameters, opening metadata, manifests; Workjig cache keys |
| `src/commonplace/headless/` (`harness.py`, `jobs.py`, `__init__.py`, `corrections.py`) | `Harness.worker()`, `self.worker`, `workjig.CommandWorker`, `max_workers`, `worker_problem` | wraps the external Workjig API; not renamable on Commonplace's side alone |
| `src/commonplace/cli/analysis.py`, `cli/task.py` | `--worker-profile`, `--max-workers`, help text | CLI interface; documented in `commands.md` and the skill |
| `src/commonplace/cli/review/finalize_review_job.py` | help text for `--runner`, `--model` | wording only |
| `src/commonplace/review/protocol/prompt.py:190` | prompt string "This prompt is the complete worker brief." | text delivered to review sub-agents (a-sub) |
| `src/commonplace/review/protocol/outcomes.py:50` | error string "worker reported ERROR", asserted in `tests/commonplace/review/test_review_batch.py:507` | stored `failure_reason` value |
| `src/commonplace/lib/tasks.py`; `kb/tasks/profiles.yaml` (outside scope) | worker profile for `commonplace-task` | task runner data |
| `tests/commonplace/` (19 files, 63 lines) | fixtures `WORKER`, `"worker-profile"` keys, test names such as `test_worker_limit_serialises_launches`, `test_worktree.py` fixture path `kb/instructions/worker/SKILL.md` | follow the code |
| `scripts/synthesis_distinction_trial.py` | "worker directory", file `worker-rules.md` | script output layout |
| `scripts/session-tools.py` | `subagent` / `subagents` directory names | external Claude Code log format; leave as is |

### Frozen or historical (d)

| Location | Lines / files | Note |
|---|---:|---|
| `kb/agentic-system-analyses/retained/` | 3,323 / 1,052 | Frozen per collection contract. Mostly analysed systems' workers ("python-worker", "fork-worker", "remote workers"), record handles (`rte-worker` and similar), and "Delegated visibility" fields. Includes 192 `ARTIFACT.yaml` `worker:` keys. |
| `kb/agentic-system-analyses/retained-archive/` | 1 / 1 | archived |
| `kb/agentic-systems/reports/` (mainly `retained-archive/`) | 349 / 124 | archived run results; external workers and early-method workers |
| `kb/agentic-systems/comparisons/memory/` | 66 / 3 | generated from retained analyses; regenerate rather than edit |
| `kb/reference/adr/` | 133 / 29 | Decision history. Review-worker ADRs (010, 030, 034, 035, 038, 043, 067) are a-sub. Analysis ADRs (097–120) are a-head. 078–081 are ingest and grounding (a-sub). 086 and 116 are spine. Amendments, not edits, would be the route. |
| `kb/reference/proposals/archive/` | 55 / 8 | `code-scheduled-workflows.md:44` once defined "**Worker** — the sub-agent that executes one job.", later superseded by ADR 118's headless workers |

## Not checked

- `.claude/worktrees/` (1,591 lines in 373 files): agent worktree copies of
  the repository, not separate sources. `.claude/skills/` and
  `.agents/skills/` are symlinks into `kb/`, so `rg` (which does not follow
  symlinks) counted their targets once, in place.
- Paths outside the requested scope: `kb/work/` (beyond noting the
  `ARTIFACT.yaml` evidence keys), `kb/reports/` (beyond the filenames above),
  `kb/sources/`, `kb/log.md`, `kb/messages/`, `kb/tasks/` (beyond
  `profiles.yaml`), `.pi/extensions/subagent`, and the Workjig package
  itself.
- Line-level classification inside class d, and the a-head/c split in code,
  which is approximate. The `-w` counts miss compounds joined by underscores
  or camel case. Any-form counts are given for code only.
- Compounds such as "delegate", "delegated agent", "child", "actor" and
  "executor", which may overlap the delegation sense without using either
  word.
- Whether `rg -w` matched every "worker-*" hyphen compound: it does, because
  "-" is a word boundary. The list shown is therefore inclusive of
  `worker-profile` and `worker-rules`.
