---
description: Multi-role iterative control plane that turns repeated scenario runs into playbooks, typed lessons, harness mutations, and optionally distilled MLX models — now reorganized around a canonical concept model (Scenario/Task/Mission/Campaign) with a data-driven role DAG and trend-aware gating
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-12"
---

# Autocontext

Autocontext is a closed-loop control plane that takes a plain-language task or a saved scenario, runs multi-generation improvement loops against it, accumulates validated knowledge, and optionally distils the result into a cheaper local model. The current layout organises around a canonical vocabulary — `Scenario`, `Task`, `Mission`, `Campaign` as user-facing objects; `Run`, `Step`, `Verifier`, `Artifact`, `Knowledge`, `Budget`, `Policy` as runtime objects — documented in `docs/concept-model.md`. The repo ships two installable packages sharing SQLite schemas: `autocontext` on PyPI (full Python control plane: CLI, FastAPI server, training, MCP) and `autoctx` on npm (TypeScript package focused on simulations, investigations, analysis, mission/campaign control, and MCP serving). Built by Greyhaven AI, MIT-licensed. Eleven scenario families are now executable in both runtimes (Python via subprocess executors, TypeScript via V8 isolate codegen).

**Repository:** https://github.com/greyhaven-ai/autocontext

## Core Ideas

**Role DAG replaces the fixed orchestration pipeline.** Agent roles (competitor, translator, analyst, coach, architect, curator, skeptic) are declared as `RoleSpec` entries with explicit `depends_on` dependencies. `RoleDAG` in `harness/orchestration/dag.py` validates acyclicity and computes execution batches via topological sort — each batch runs in parallel. Adding a role no longer requires editing the pipeline; it requires registering a `RoleSpec`. The fixed four-role pipeline from earlier versions is now a data-driven graph, and the skeptic role (adversarial red-team reviewer) and curator role are first-class participants rather than optional add-ons.

**Skeptic gate adds adversarial review before advancement.** Before a candidate playbook is accepted, `SkepticAgent` in `agents/skeptic.py` is asked to argue *against* advancing: look for overfit, rubric gaming, fragile gains, contradictions with prior lessons, suspicious score jumps. Output is structured (`SKEPTIC_RISK: high|medium|low`, concerns list, `SKEPTIC_RECOMMENDATION: proceed|caution|block`, confidence 1-10). This sits alongside the curator's accept/reject/merge decision in the advancement pipeline. A constraint-mode toggle injects explicit "do not" preambles — the constraint list is present for every role (competitor, analyst, coach, architect, curator, skeptic) and is the system's mechanism for enforcing behavioural contracts at the prompt level.

**Trend-aware gate with plateau relaxation and consecutive-rollback detection.** The simple `BackpressureGate` (advance/retry/rollback on score delta) is still present, but the default when `backpressure_mode == "trend"` is `TrendAwareGate`: if the recent score window is flat (spread under `min_delta`), the effective threshold relaxes by `plateau_relaxation_factor`; if the last N gate decisions were all rollback, the threshold also relaxes. This tries to prevent the system from getting stuck in a retry-rollback loop when the scenario has hit a genuine plateau — a real control-theory refinement over the earlier one-step delta check.

**Typed lessons with applicability metadata and staleness tracking.** `Lesson` objects (`knowledge/lessons.py`) carry `ApplicabilityMeta` with `generation`, `schema_version`, `upstream_sig`, `operation_type`, `superseded_by`, and `last_validated_gen`. `LessonStore` persists them as JSON and supports `get_applicable_lessons`, `get_stale_lessons`, `invalidate_by_schema_change`, `supersede_lesson`, `validate_lesson`, and `staleness_report`. A lesson becomes stale if it has not been validated within a configurable staleness window; schema changes can invalidate all older lessons at once. This is a genuine maturation model for knowledge units — the earlier "accumulate forever" flat-list shape has been replaced with a lifecycle.

**Harness mutations as a promotion target alongside playbooks.** The architect now emits not only Python tools but also typed `HarnessMutation` specs — `prompt_fragment` (per-role), `context_policy` (per-component), `completion_check`, or `tool_instruction`. These carry forward across generations via `mutations/applier.py` and are gated through `mutations/gate.py`. The architect can now modify the harness itself, not just the tool layer. This widens what "learning" can produce: strategy updates, lessons, generated tools, harness prompt fragments, and context policies — four increasingly meta layers.

**Evidence manifest and session consolidation as separate pipelines.** `evidence/` (manifest, materializer, tracker, workspace) provides evidence tracking for investigation scenarios, with evidence manifests injected into analyst and architect prompts. `session/memory_consolidation.py` adds a background consolidation pass with file-based `ConsolidationLock`, threshold-gated triggers (completed turns or completed sessions), and structured `ConsolidationResult` audit output. These are two distinct memory pipelines running alongside the main generation loop.

**Context budget over ~15 components with protected hints and dead ends.** `ContextBudget` in `prompts/context_budget.py` still does char/4 token estimation and a progressive trimming cascade, but the cascade now covers 15 named components (session reports, evidence manifest, four notebook contexts by role, experiment log, research protocol, environment snapshot, trajectory, analysis, tools, lessons, playbook). `hints` and `dead_ends` remain the only two protected components never trimmed. The cascade order is hardcoded globally — no per-task adaptation.

**Dual-language dead-end registry and strategy-score registry.** `DeadEndEntry` records rolled-back strategies with generation, score, and reason; `consolidate_dead_ends` trims the registry to the most recent N entries. These flow into the dead-ends prompt block that the competitor and analyst see. The strategy-score registry is a markdown table of every generation's strategy, best score, and gate decision. Both are injected into every agent prompt as running context.

**MLX training and model registry promote trace signal into weights.** `training/runner.py`, `training/backends.py`, and `training/model_registry.py` expose the offline path from exported JSONL to a fine-tuned MLX model on Apple Silicon, with the resulting model registered by scenario, backend, and runtime. A TypeScript `training/` tree mirrors this for CUDA backends, with prompt alignment and promotion modules. This is the second promotion target: filesystem artifacts first, model weights second, both fed by the same run trace.

**Canonical concept model as a naming-debt ledger.** `docs/concept-model.md` explicitly catalogues naming collisions (`task` as queue row vs user-facing task, `scenario` as env vs saved agent task) and stages a rename without rushing it. It is the most transparent documentation of a still-incomplete migration — the model explicitly marks `Campaign` as TypeScript-only, `Mission` as TypeScript-first, and flags ongoing vocabulary mismatches between code and product copy rather than pretending they are resolved.

## Comparison with Our System

Autocontext and commonplace occupy adjacent but not overlapping positions: autocontext automates *how an agent gets better at a measurable task over many runs*; commonplace structures *how a team's knowledge about agent systems accumulates and composes across domains*.

| Dimension | Autocontext | Commonplace |
|---|---|---|
| Primary object | Scenario/Task/Mission with runtime `Run` | Typed note with frontmatter and semantic links |
| Primary concern | Iterative behavioural improvement, measured by score | Knowledge accumulation and maturation, measured by downstream utility |
| Loop shape | Multi-role DAG (competitor → analyst/coach/architect/curator/skeptic) with gate | Human+agent write → connect → validate → status transitions |
| Knowledge unit | Playbook (markdown, versioned), typed `Lesson` with applicability meta, tools, harness mutations | Note with type, status, tags, links; definition/structured-claim/instruction types |
| Knowledge lifecycle | Validation by `last_validated_gen`, staleness windows, `supersede_lesson`, schema-version invalidation | `seedling → current → superseded` status transitions, semantic links that articulate relationships |
| Evaluation | Tournament Elo, LLM judge with rubric, skeptic red-team review, curator quality gate | Advisory validation, human judgment, review-system bundles |
| Gate mechanism | BackpressureGate and TrendAwareGate with plateau relaxation | Static validation; no dynamic performance gate |
| Cross-unit relations | Implicit (playbook injection); lessons can be `superseded_by` another lesson id | Explicit typed links (extends, grounds, contradicts, exemplifies) |
| Scope | Per-scenario silo; no cross-scenario lesson transfer in Python runtime | Cross-domain KB; links are the transfer mechanism |
| Promotion target | Filesystem artifacts + optionally model weights via MLX/CUDA | Filesystem artifacts only |
| Storage | SQLite (structured run data) + filesystem (knowledge artifacts) | Markdown files in git |
| Surface | CLI, API server, MCP server, TUI | CLI commands, skills, git |
| Agency model | Fully automated (agents orchestrate agents) | Human+agent collaborative |

**Where autocontext is stronger.** The typed `Lesson` with `last_validated_gen` and `supersede_lesson` is closer to knowledge maturation than the earlier flat-accumulation playbook. The skeptic gate is a cheap, specific mechanism for catching overfit and rubric gaming that commonplace's advisory validation cannot perform. The harness-mutation layer means the architect can reshape the next generation's prompts, not just its tools — autocontext learns about its own harness, which commonplace does not. The trend-aware gate with plateau detection is a real control refinement: it prevents the system from treating temporary plateaus as permanent failure. The MLX/CUDA distillation path remains the only reviewed system that promotes trace-derived signal into weights as a deliberate second stage.

**Where commonplace is stronger.** Our links articulate *why* units relate — `extends`, `grounds`, `contradicts`, `exemplifies` — while autocontext's knowledge graph is implicit in playbook injection and `supersede_lesson` pointers. Our notes are cross-domain; autocontext's knowledge is scenario-scoped (each scenario has its own `playbook.md`, `hints.md`, `lessons.json`). The [title-as-claim](../../notes/title-as-claim-enables-traversal-as-reasoning.md) convention has no analogue in autocontext's knowledge artifacts: playbook sections are instrumental prose, not standalone claims addressable from elsewhere. Our [progressive disclosure](../../notes/agents-navigate-by-deciding-what-to-read-next.md) lets agents decide what to read; autocontext's `build_prompt_bundle` front-loads all 15+ components into every generation prompt and then trims.

**The underlying divergence** is still what learning means. Autocontext measures learning by score improvement on a bounded scenario — the TrendAwareGate, skeptic review, and staleness windows are all instruments for validating that measurement. Commonplace measures learning by whether the KB is more capable of supporting good decisions across contexts, which has no numeric oracle. This is the same [constraining-and-distillation trade-off](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md): autocontext constrains aggressively within a scenario to get reliable, measurable improvement; commonplace distils broadly across domains and accepts weaker per-step verification.

## Borrowable Ideas

**Typed lessons with applicability metadata and staleness.** `Lesson.is_stale(current_generation, staleness_window)` with `last_validated_gen`, `schema_version`, and `superseded_by` is a concrete model for our note lifecycle. For commonplace, we could add a `last-validated` frontmatter field and a `superseded-by` pointer to make `status: superseded` carry the successor reference explicitly. The `schema_version` invalidation pattern maps to the case where our shipped type instructions change and older notes should be re-reviewed against the new type. *Partially ready — needs a trigger event (what changes "validation" in our KB?) before it pays off.*

**Skeptic as a dedicated adversarial role.** A read-only `/skeptic` bundle or skill that specifically looks for overfit claims, contradictions with existing notes, and fragile generalisations — distinct from the broader `/review` bundles — would be cheap to add. The key design detail in autocontext's version is the structured output (`SKEPTIC_RISK`, `SKEPTIC_RECOMMENDATION: proceed|caution|block`): adversarial review produces a decision, not just a comment. *Ready to borrow — low cost, maps onto our existing review bundle pattern.*

**Explicit dead-end registry with consolidation.** Same recommendation as before, now more crisply: a `dead-ends.md` index listing approaches that were tried and abandoned, with `consolidate_dead_ends(entries, max_entries)` semantics — keep the most recent N. Prevents repeated exploration of known failures without bloating context. *Ready to borrow.*

**Role DAG for multi-step operations.** If we ever decompose `/ingest` or `/review` into parallelisable sub-roles with explicit dependencies, `RoleDAG` is a clean pattern: declare role specs with `depends_on`, let the harness compute execution batches. The payoff is predictability plus parallelism without having to hand-edit a pipeline function. *Needs a use case first — current single-agent operations are fine at our scale.*

**Constraint-mode prompt suffixes.** Every agent role in autocontext has an optional "do not" preamble (do not report findings without evidence, do not remove working strategies without justification, do not accept a playbook that removes validated high-scoring strategies). This is prompt-level enforcement of behavioural contracts. For commonplace, structured "do not" bullets in type instructions (do not introduce orphan links, do not leave descriptions < 50 chars) would make the same contracts visible to the model at generation time rather than only at validation time. *Ready to try — cheap addition to existing type instructions.*

**Trend-aware gating with plateau relaxation.** If we ever build a measurable process (link-graph quality score, validation-error count), the plateau-relaxation pattern is portable: when recent measurements are flat, relax the improvement threshold rather than rolling back. *Needs a use case first — we lack a numeric quality signal.*

## Curiosity Pass

### Broad pass

**The refactor frenzy is the signal.** Between March 17 and April 9, the repo landed dozens of PRs titled "extract generation X workflow", "extract generation phase state", "refactor mission status transitions", "generation-lifecycle-workflow". The code is under active architectural pressure. What was one `GenerationRunner` is becoming a stack of coordinators (cycle coordinator, event coordinator, side-effect coordinator, execution step coordinator, attempt orchestrator, loop orchestrator, lifecycle workflow, attempt workflow facade). This is either convergent decomposition — the team has learned where the joints are — or accidental fragmentation. The concept-model doc suggests convergent: they are naming the joints deliberately and migrating code to match. But the number of layers now between "call run_generation" and "execute a competitor" is high enough that reading the code is harder than reading the concept doc.

**"Autocontext" as a name is still overstated.** The context-budget mechanism is still char/4 estimation and priority-ordered concatenation with lossy removal. The budget now covers 15+ components instead of ~8, which is progress, but the fundamental shape is the same: read artifacts from disk, format as markdown, concatenate, trim. The real context transformation happens in the coach (playbook synthesis) and curator (lesson consolidation), both of which are LLM-mediated prompt operations, not "automatic" anything. The name continues to market context transformation that the code does not perform.

**Two memory pipelines now sit alongside the main loop.** `evidence/` supports investigation scenarios with evidence tracking. `session/memory_consolidation.py` runs a separate threshold-triggered consolidation of completed sessions with file-locked concurrency. These are new since the last review and suggest the team is moving from "one scenario loop" toward "several concurrent knowledge-engineering tasks sharing a runtime". Whether they stay distinct or collapse into a unified pipeline is worth watching.

### Systematic pass: each Core Idea

**Role DAG replaces the fixed orchestration pipeline.**
1. *Property claimed:* Data-driven role orchestration with parallel execution of independent roles.
2. *Transform or relocate?* Genuine structural change. Previously the role order was hardcoded in generation runner; now `RoleDAG.execution_batches()` computes it via topological sort. Adding a role is a registration, not an edit.
3. *Simpler alternative:* Hardcoded role order works if the set of roles is small and stable. The DAG pays off when roles are added often or by third parties — otherwise the topo-sort machinery is overkill for ~6 roles.
4. *Ceiling:* The DAG can parallelise roles that have no data dependency. It cannot discover that the skeptic's concerns should feed back into the coach's next pass — that still requires explicit edge-adding.

**Skeptic gate adds adversarial review before advancement.**
1. *Property claimed:* Independent red-team check against overfit, rubric gaming, fragile gains.
2. *Transform or relocate?* LLM transformation — the skeptic reads playbook + trajectory + analysis and produces a risk classification. Real synthesis, not concatenation.
3. *Simpler alternative:* A constraint-mode prompt for the coach ("do not recommend strategies that only worked against one opponent") achieves part of the same effect at lower cost. The skeptic adds value if it genuinely catches cases the coach misses, but autocontext provides no evidence the two prompts produce different findings. The separation is architecturally clean; its empirical value is an open question.
4. *Ceiling:* The skeptic can catch overfit patterns that are visible from the same trajectory/analysis context. It cannot catch scenario-definition flaws or evaluation-metric gaming, because it reads the same artifacts the coach reads.

**Trend-aware gate with plateau relaxation.**
1. *Property claimed:* Avoids spurious rollbacks when the scenario has plateaued.
2. *Transform or relocate?* Genuine control logic — the threshold is computed from score history, not fixed. Small change with real semantic content.
3. *Simpler alternative:* A monotonically relaxing `min_delta` over generations achieves similar behaviour without computing spread. But the plateau-detection phrasing is more interpretable to operators ("the score has been flat for N generations, so we're relaxing").
4. *Ceiling:* The gate detects flat regions in the score trajectory. It cannot detect that the flat region is a local optimum versus a global one — more relaxation just lets the system accept smaller and smaller improvements.

**Typed lessons with applicability metadata and staleness tracking.**
1. *Property claimed:* Knowledge units have a genuine lifecycle — creation, validation, staleness, supersession, schema invalidation.
2. *Transform or relocate?* Structural transformation — the schema carries semantic metadata the flat-bullet format could not carry. `invalidate_by_schema_change` is real: one call marks a whole cohort of lessons stale.
3. *Simpler alternative:* Timestamp-only staleness (drop lessons older than N generations) is simpler and captures most of the value. The `schema_version` and `upstream_sig` fields pay off when the underlying scenario schema genuinely changes between runs — otherwise they are dead metadata.
4. *Ceiling:* The lifecycle is still run-local. A lesson invalidated in scenario A cannot inform lesson validity in scenario B, because scenarios do not share lesson stores.

**Harness mutations as a promotion target alongside playbooks.**
1. *Property claimed:* The architect can modify the harness (prompt fragments, context policies) not just add tools.
2. *Transform or relocate?* Genuine — mutations are applied to prompt assembly and context-policy selection at runtime, changing what the next generation's prompts look like. This is real self-modification.
3. *Simpler alternative:* A fixed prompt library with A/B switches the architect can flip achieves most of the same benefit without arbitrary mutation. The fully general mutation type (`content: str`) is powerful but harder to validate and easier to corrupt.
4. *Ceiling:* Harness mutations can adjust what the next generation sees. They cannot reshape the scoring function, the scenario semantics, or the role DAG itself.

**MLX training and model registry promote trace signal into weights.**
1. *Property claimed:* Scenario-specific fine-tuning captures strategic knowledge in cheap local models.
2. *Transform or relocate?* Real transformation — JSONL training data produces fine-tuned weights via MLX/CUDA. Output is structurally different from input.
3. *Simpler alternative:* Few-shot prompting with the accumulated playbook may capture most of the behaviour at zero training cost. Training wins when inference cost savings over many runs justify the one-time training cost and when the behaviour is narrow enough to converge.
4. *Ceiling:* The distilled model can reproduce patterns present in training data. It cannot exceed the frontier model's capability on the scenario, and training data quality is determined by how well the earlier generations' gating did.

### Findings that update Core Ideas and Comparison

The review-over-review finding is that autocontext has moved in the direction we called out last time. Knowledge units have a lifecycle now (typed lessons, staleness, supersession). The orchestration is data-driven (role DAG) instead of hardcoded. A new adversarial role (skeptic) explicitly checks for overfit. Gating has trend awareness. These are real improvements on the fronts where the previous review flagged gaps.

The single-scenario knowledge silo remains. Lessons in scenario A still do not inform scenario B at the Python runtime layer. The TypeScript `campaign` surface may eventually coordinate mission-level knowledge, but it is not yet a Python capability. This remains the opposite architectural bet from commonplace.

The coach is still the critical path — the curator, skeptic, and constraint-mode prompts mitigate coach drift, but the playbook is still written by one LLM reading accumulated context and producing markdown. There is no structural check that playbook sections are consistent across revisions, only LLM-judged quality scores.

**Trace-derived learning placement.** Autocontext consumes repeated run trajectories over a fixed scenario, not open-ended conversation logs. The *source trace* is per-generation records — competitor output, tournament/judge scores, gate decisions, analyst markdown, coach output, execution traces — persisted to SQLite and artifact files. Trigger boundaries are per-generation for accumulation and per-run for session reports, with a separate offline trigger for MLX export/train. *Extraction* pulls structured lessons with applicability metadata (`accumulate_lessons`), a consolidated playbook (coach-synthesised), typed harness mutations (architect), dead-end entries (on rollback), and optionally JSONL training records. The *oracle* stack is layered: tournament Elo for game scenarios (hard), LLM judge with rubric for agent tasks (soft), skeptic red-team review (meta), curator quality gate (meta). *Promotion target* is filesystem artifacts first (playbooks, lessons.json, hints, session reports, harness mutations), and optionally weights second (MLX/CUDA fine-tuned models registered in `model_registry`). *Scope* is scenario-local — each scenario has its own knowledge directory, no cross-scenario transfer at the Python layer. *Timing* is online within a run (per generation), offline-staged for distillation (export → train → publish). On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md): axis 1 trajectory-run ingestion (repeated bounded attempts, not live sessions); axis 2 **split** — autocontext still spans both substrate-classes, inspectable symbolic artifacts and optional model weights. Compared with the previous review, the artifact side now has a richer lifecycle (typed lessons with supersession, harness mutations) but the cross-scenario silo claim still holds. No new subtype needed, but the survey's one-line summary could note the typed-lesson addition and the harness-mutation layer as extensions of the artifact structure spectrum.

## What to Watch

- Whether the Python package gains cross-scenario knowledge sharing (shared lesson store, cross-scenario similarity search, mission-spanning playbooks). The `campaign` concept exists in TypeScript; Python catching up would validate the cross-domain hypothesis commonplace is built on.
- Whether the architectural refactor stabilises. The April commit log is dominated by "extract generation X workflow" PRs. Either the team converges on a clean layering or we see a second wave renaming the coordinators.
- Whether the MLX/CUDA distillation produces practically useful scenario-specific models at scale. If yes, it validates adjacent deployment-derived weight learning; if no, the artifact-only path stays dominant.
- Whether harness mutations (prompt fragments, context policies) prove durable across generations or accumulate into a garbage heap. This is the core question for self-modifying prompt systems: does the architect's edit history stay coherent, or does it drift into contradictory fragments?
- Whether the skeptic role measurably catches things the coach misses. If the skeptic is rarely raising high-risk flags, the separation is architectural ceremony; if it often blocks advances that the coach would have accepted, it is a real gate.
- Whether the concept-model migration completes. If `Task` stays overloaded (queue row vs user-facing task), the rename debt compounds; if the migration lands, autocontext will have a cleaner vocabulary than most peer systems.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: autocontext is the clearest inspected system spanning both artifact learning and weight promotion; the current review refines the artifact side with typed lessons and harness mutations
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: the 15-component context budget with protected hints/dead-ends is a concrete response to context scarcity, using a fixed global priority cascade rather than task-adaptive loading
- [distillation](../../notes/definitions/distillation.md) — exemplifies: the coach's playbook synthesis and the curator's lesson consolidation are both automated distillations from trajectory + analysis into compressed knowledge; MLX/CUDA training is a second distillation layer (context → weights)
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — exemplifies: constraint-mode prompts make the constraining explicit at generation time, aggressive per-scenario optimisation contrasts with our cross-domain distillation
- [automating-kb-learning-is-an-open-problem](../../notes/automating-kb-learning-is-an-open-problem.md) — contrasts: autocontext automates learning within a measurable loop (tournament scores, LLM judges, skeptic review); knowledge still has limited cross-scenario synthesis, marking the same automation boundary
- [the-boundary-of-automation-is-the-boundary-of-verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — exemplifies: the system works best where evaluation is cheapest (game tournaments with deterministic scoring) and degrades where verification is soft (LLM-judged agent tasks, skeptic-judged playbook quality)
- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — exemplifies: tournament Elo is a hard oracle, LLM judges and skeptic/curator reviews are soft oracles, and coach-produced playbook quality has no independent oracle — layered gating with varying oracle strength
- [agents-navigate-by-deciding-what-to-read-next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) — contrasts: autocontext front-loads 15+ context components and then trims, while commonplace lets agents navigate incrementally — opposite context-delivery models with different task-adaptivity properties
- [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — complicates: playbook accumulation, typed lessons with lifecycle, and harness mutations extend deploy-time learning; MLX distillation is adjacent deployment-derived weight learning rather than deploy-time learning in the linked note's stricter sense
- [files-not-database](../../notes/files-not-database.md) — complicates: autocontext uses SQLite for structured operational data (runs, generations, matches, mutations store) and filesystem for knowledge artifacts (playbooks, lessons.json, tools, snapshots); migrations are cross-compatible between Python and TypeScript, suggesting per-artifact-type rather than system-wide choice
- [codification](../../notes/definitions/codification.md) — exemplifies: the architect role generates Python tool functions and typed harness mutations (prompt fragments, context policies) from capability gaps, which is codification; the rest of the knowledge pipeline stays in natural language
