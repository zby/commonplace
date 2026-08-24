# Cleanup cohort 04 — frozen 2026-08-24

Frozen at repository `15f4080f`. Follow [the procedure](./procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.16 MB across 5 ingests.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `agent-orchestration-occupies-a-multi-dimensional-design-space` | `c39e3c97` | `mini-exercise-mismanaged-geniuses-longcot-rlm`<br>`the-mismanaged-geniuses-hypothesis-2042588627260018751`<br>`the-y-combinator-for-llms-solving-long-context-rot` |
| `brainstorming-how-to-test-whether-pairwise-comparison-can-harden` | `640ff9a4` | `position-bias` |
| `operational-signals-that-a-component-is-a-relaxing-candidate` | `efa704c2` | `position-bias` |
| `out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec` | `866ecb1a` | `position-bias` |
| `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | `3ee7f191` | `recursive-language-models-what-finally-gave-me-the-aha-moment`<br>`the-y-combinator-for-llms-solving-long-context-rot` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Frozen claim inventory

Recorded from the target blobs above before reading any ingest or snapshot.

| ID | target | claim as frozen | source-side need |
|---|---|---|---|
| AO-1 | `agent-orchestration-occupies-a-multi-dimensional-design-space` | “The LongCoT-mini RLM case shows the trace-extracted natural-language point: Claude Code inspected failing RLM trajectories and produced prompt tips that shifted a free-form RLM away from brute force and toward checked graph decomposition.” | Whether Claude Code derived prompt guidance from failing LongCoT-mini RLM trajectories, and whether the reported rerun shifted from brute force toward checked graph decomposition. |
| AO-2 | `agent-orchestration-occupies-a-multi-dimensional-design-space` | “The Mismanaged Geniuses hypothesis points at yet another point: codify the decomposition language, then relax the policy that chooses within it into a distributed-parametric learned artifact.” | Whether the source proposes a codified decomposition language with a learned policy choosing decompositions within it. |
| AO-3 | `agent-orchestration-occupies-a-multi-dimensional-design-space` | “λ-RLM takes a different route by restricting orchestration to a pre-verified symbolic combinator library, improving verifiability without changing the per-run persistence boundary.” | Whether λ-RLM restricts orchestration to pre-verified symbolic combinators, what verification benefit is claimed, and whether its execution state remains per-run rather than durable. |
| BP-1 | `brainstorming-how-to-test-whether-pairwise-comparison-can-harden` | “Across 27 LLM judges on 193 sibling-edit story pairs, the median model flips its pairwise winner in 44.8% of decisive cases when display order is swapped (preprint-tier; sibling-edit surface only).” | The benchmark population, item count and relationship, swap protocol, definition of decisive cases, median flip statistic, and publication/scope boundary. |
| OR-1 | `operational-signals-that-a-component-is-a-relaxing-candidate` | “Across 27 judges on 193 sibling-edit story pairs, the median judge flips its pairwise winner in 44.8% of decisive cases when display order alone is swapped — the signal measured on the evaluator, not the task-solver.” | The benchmark population, sibling-edit item count, order-swap intervention, median decisive-case flip statistic, and whether the evaluated systems act as judges. |
| OR-2 | `operational-signals-that-a-component-is-a-relaxing-candidate` | “Order-swap alone shifts 27 LLMs' pairwise winners on 44.8% of decisive cases, and some models (Mistral Large 3) invert the direction rather than attenuate it — heterogeneity that matters for decorrelation (preprint-tier, sibling-edit surface).” | The order-swap result and aggregation, the model-level result for Mistral Large 3, cross-model heterogeneity, and the source’s publication and task scope; decorrelation relevance is a target-side transfer. |
| OS-1 | `out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec` | “The Mazur position-bias benchmark shows 27 LLM judges flip their pairwise winner in 44.8% of decisive cases when candidate display order is swapped — identical content in both views, interpretation driven by an ordering cue the spec does not mention.” | The judge count, swap-only protocol, decisive-case flip statistic, and whether candidate content is held fixed apart from display order; interpreter/spec diagnosis is a target-side transfer. |
| OS-2 | `out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec` | “Judge-layer interpreter failure — 27 LLMs flip their pairwise winner in 44.8% of decisive cases under display-order swap alone; parallel peg to Ma et al. at the LLM-as-judge layer (preprint-tier, sibling-edit surface).” | The empirical population, intervention, statistic, judge-layer setting, publication status, and sibling-edit scope; interpreter-failure classification and comparison with Ma et al. are target-side transfers. |
| RP-1 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “Standard RLM and λ-RLM both keep the RLM prompt-as-environment architecture and per-task persistence boundary. They differ inside that boundary: standard RLM lets the model write arbitrary REPL code, while λ-RLM constrains orchestration to a pre-verified typed combinator library selected by a planner.” | Whether both systems use a prompt-as-environment, whether state is task-local, and how arbitrary REPL code differs from planner-selected pre-verified typed combinators. |
| RP-2 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | λ-RLM table row: “REPL environment plus typed combinator runtime (`SPLIT`, `MAP`, `FILTER`, `REDUCE`)”; planner-selected pre-verified chain with bounded model leaves; discarded per-task state; recursive executor; restricted vocabulary; “auditable control flow and formal bounds.” | Each asserted λ-RLM mechanism: named combinators, planner role, verification status, bounded leaf calls, persistence, recursion, control restriction, auditability, and formal bounds. |
| RP-3 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “Instead of letting the model synthesize arbitrary Python at each step, it executes a planner-built chain over typed, pre-verified combinators and reserves neural calls for bounded leaves. That means λ-RLM addresses RLM's verifiability and predictability problem without addressing RLM's accumulation problem: the run still does not promote useful orchestration strategies into durable project artifacts.” | Whether λ-RLM uses planner-built, typed and pre-verified combinator chains with bounded neural leaves; what verifiability or predictability properties are established; and whether run products persist durably. |
| RP-4 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “λ-RLM encodes recursion in a fixed executor over the combinator library.” | Whether recursion is implemented by a fixed executor operating over the combinator library. |
| RP-5 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “λ-RLM is the restricted-runtime variant of [the RLM scratchpad] pattern.” | Whether λ-RLM retains the RLM task-local execution pattern while restricting its orchestration runtime. |
| RP-6 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “λ-RLM is an RLM variant that keeps task-local prompt-as-environment recursion while replacing arbitrary REPL code with a typed combinator runtime.” | Whether λ-RLM keeps task-local prompt-as-environment recursion and replaces arbitrary REPL orchestration with a typed combinator runtime. |
| RP-7 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | Standard RLM table row: Python REPL plus `recursive_llm()`; model-authored task-local code; discarded per task; recursive calls built in; arbitrary REPL control; “cheap external bookkeeping without committing artifacts.” | Whether standard RLM exposes a Python REPL and `recursive_llm()`, has the model author orchestration code, keeps/discards state per task, and places bookkeeping in that ephemeral symbolic substrate. |
| RP-8 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “In standard RLM, the model writes orchestration code, but the REPL state is only a task-local substrate…bookkeeping lives in variables and loops rather than in chat history…there is no approval state, lifecycle, or stale code problem for an artifact that disappears after use.” | Whether the model writes orchestration code, whether REPL state and generated code are task-local and discarded, and whether variables and loops carry bookkeeping outside chat history; governance consequences are target-side transfer. |
| RP-9 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “Standard RLM generated code can call `recursive_llm()` as part of its orchestration.” | Whether model-authored REPL code can invoke `recursive_llm()` during orchestration. |
| RP-10 | `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence` | “Practitioner walkthrough of RLM's REPL mechanism and symbolic variable return.” | What REPL mechanism the walkthrough describes and whether/how the model returns a symbolic variable as its answer. |

## Completion record

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| AO-1 | narrowed | Replaced the asserted shift to checked graph decomposition with the grounded trace failures, Claude Code tip-writing intervention, and reported 50.6%/65.6% results; states that no updated trace analysis proves the qualitative shift. | target PASS; source pair PASS |
| AO-2 | narrowed; retained local delta | Uses the source's define-the-decomposition-space then train-the-selection-policy proposal; marks codified language, distributed-parametric form, and codify-then-relax as the note's placement rather than source terminology. | target PASS; source pair PASS |
| AO-3 | narrowed | Retains the typed, pre-verified combinator runtime and deterministic planner; adds bounded task-selection/synthesis calls and removes the unsupported claim that λ-RLM's post-return persistence matches standard RLM. | target PASS; source pair PASS |
| BP-1 | narrowed | Preserves the 27-model, 193-pair, median 44.8% result while making the decisive-pair denominator explicit and replacing unsupported “preprint-tier” with pinned repository-snapshot scope. | target PASS; source pair PASS |
| OR-1 | grounded | Normalized the use to the exact benchmark units: 27 judge models, 193 sibling-edit pairs, both display orders, and the median model's 44.8% decisive-pair flip rate. | target PASS; source pair PASS |
| OR-2 | narrowed | Replaced the all-model-sounding 44.8% wording with the median-model statistic, described Mistral Large 3's opposite-direction second-position bias exactly, and scoped the decorrelation claim as target-side transfer. | target PASS; source pair PASS |
| OS-1 | narrowed | Replaced “27 judges flip … in 44.8%” with the median-model statistic and made the interpreter/spec diagnosis explicitly target-side. | target PASS; source pair PASS |
| OS-2 | narrowed | Applied the same median/decisive-pair repair, removed “preprint-tier,” and scoped the comparison with Ma et al. as the note's transfer. | target PASS; source pair PASS |
| RP-1 | narrowed | Removed the unsupported shared per-task persistence boundary; retains shared prompt-as-environment execution and the grounded control-language contrast while leaving post-return lifecycle open. | target PASS; both source pairs PASS |
| RP-2 | contradicted / repaired | Rebuilt the λ-RLM table row: the source does not establish discarded post-return state, its planner is deterministic, and it includes bounded task-selection and specified synthesis calls rather than leaf calls only. | target PASS; λ-RLM source pair PASS |
| RP-3 | contradicted / repaired | Replaced “same persistence boundary,” leaf-only neural work, and “does not promote” with the grounded restricted runtime plus an explicit statement that the paper does not settle disposal, reuse, or promotion. | target PASS; λ-RLM source pair PASS |
| RP-4 | grounded | Retained the claim that λ-RLM recursion is implemented by a fixed executor over its combinator library. | target PASS; λ-RLM source pair PASS |
| RP-5 | narrowed | Keeps λ-RLM as the restricted-runtime variant of within-execution RLM orchestration, but no longer classifies either source's post-return lifecycle. | target PASS; λ-RLM source pair PASS |
| RP-6 | narrowed | Replaced “task-local” with prompt-as-environment recursion and a deterministic typed combinator runtime; the footer now says post-return persistence is unspecified. | target PASS; λ-RLM source pair PASS |
| RP-7 | narrowed | Replaced the exact `recursive_llm()` and discarded-per-task assertions with the grounded scaffold-supplied recursive sub-call, within-execution variable persistence, and unknown post-return lifecycle. | target PASS; walkthrough source pair PASS |
| RP-8 | literature handoff | Removed the unsupported task-local/disappears/governance claims while retaining within-run REPL bookkeeping; an implementation-specific lifecycle source is required before reinstating cross-run discard. | target PASS; walkthrough source pair PASS |
| RP-9 | narrowed | Replaced the unsupported exact `recursive_llm()` API attribution with recursive sub-agent invocation through a scaffold-supplied sub-call. | target PASS; walkthrough source pair PASS |
| RP-10 | grounded | Retained the REPL-mechanism and symbolic-variable-return use, adding the source's within-execution boundary and its silence on the exact API and post-return lifecycle. | target PASS; walkthrough source pair PASS |

All target validations are clean. All five ingest validations pass; the RLM
walkthrough ingest retains one pre-existing link-health warning for missing
`../notes/definitions/distillation.md`, outside the Claims splice. Source review
ran as eight requested source-conformance pairs under the `codex` partition;
all eight finalized `pass` between `2026-08-24T19:39:42+00:00` and
`2026-08-24T19:40:50+00:00`, and the follow-up selector returned no stale
targets.

## Run observations

- Six normalized Claims entries were added across five ingests: one each for
  LongCoT-mini, Mismanaged Geniuses, position bias, and the RLM walkthrough;
  two for λ-RLM, separating runtime mechanism from the execution-lifecycle
  boundary.
- The position-bias entry served five target uses. The two λ-RLM entries served
  seven. Whole-section selection remained unambiguous; no similar-entry
  accumulation or need for claim IDs appeared.
- No snapshot was missing or mismatched, so no re-ingest or unavailable-source
  disposition was needed.
- Distribution across 18 frozen uses: three grounded, twelve narrowed, two
  contradicted-and-repaired, and one literature handoff. The handoff is the
  standard-RLM post-return lifecycle: the named walkthrough establishes state
  persistence only across REPL calls inside an execution, not disposal after
  the answer returns.
