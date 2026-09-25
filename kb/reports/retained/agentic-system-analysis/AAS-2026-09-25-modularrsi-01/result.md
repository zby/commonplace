---
type: kb/types/agentic-system-analysis-result.md
description: "Complete code-grounded analysis of ModularRSI's evolution and modular solver subsystem at the frozen release."
run-id: AAS-2026-09-25-modularrsi-01
system: "ModularRSI"
run-date: "2026-09-25"
result-disposition: complete
target-class: "builder or improvement plane"
boundary-kind: subsystem-only
reviewed-boundary: "b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9"
analysis-cutoff: "2026-09-25"
evidence-tier: code-grounded
memory-comparison:
  scope: "Accumulated ModularRSI solver chat/continuations and guard/observation state; trace-derived findings/proposals, imported and evolved module generations, archive/status/access metadata, editor-memory capability, task-history/review state and composition replay cache. Named subsystem and necessary interfaces only; static doctrine, unrelated Harbor agents, external providers and benchmark internals excluded."
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values: ["files", "in-memory"]
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4", "OBJ-5", "OBJ-6", "OBJ-7", "OBJ-8", "OBJ-9"]
      note: "Runtime generations and ledgers are files; active chat, summaries and guard state are in memory. Git is the inspected distribution, not a runtime memory store."
    representational_form:
      assessment: known
      basis: wired
      values: ["natural-language", "symbolic"]
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-4", "OBJ-6", "OBJ-8"]
      note: "Content includes model prose and terminal text; executed Python and structured status/bundle fields carry symbolic semantics. Description strings are not substitutes for the code they describe."
    lineage:
      assessment: known
      basis: wired
      values: ["imported", "other-compiled", "trace-extracted"]
      records: ["OBJ-2", "OBJ-3", "OBJ-6", "OBJ-7", "OBJ-8", "OBJ-9"]
      note: "Seed/merged modules are imported; summaries and diagnoses are trace-extracted; deterministic status, cache, and index construction are other-compiled. Static authored doctrine is outside the memory boundary."
    behavioral_authority:
      assessment: known
      basis: wired
      values: ["knowledge", "instruction", "enforcement", "routing", "ranking", "validation"]
      records: ["RTE-2", "RTE-3", "RTE-4", "RTE-7", "RTE-8", "RTE-9", "RTE-10"]
      note: "Evidence is advisory; briefs and continuations instruct; executable modules and guard state enforce; archive/cache/cooldown route; portfolio ranks; review-health state conditions a validation gate."
    write_agency:
      assessment: known
      basis: wired
      values: ["automatic"]
      records: ["RTE-2", "RTE-3", "RTE-7", "RTE-8", "RTE-9", "RTE-10"]
      note: "Scoped in-use writes are code- or model-produced. Operator configuration and imported seed selection do not establish manual curation of accumulated memory."
    curation_operations:
      assessment: known
      basis: wired
      values: ["consolidate", "decay", "dedup", "evolve", "invalidate", "promote", "synthesize"]
      records: ["RTE-2", "RTE-3", "RTE-4", "RTE-7", "RTE-8", "RTE-10"]
      note: "Summaries consolidate; context and scrollback limits forget; same-intervention clustering merges support; modules/proposal state evolve; supersession withdraws reliance with history kept; promotion activates code; causal diagnoses introduce claims. Per-route meanings are bounded below."
    read_back_direction:
      assessment: known
      basis: wired
      values: ["pull", "push"]
      records: ["RTE-2", "RTE-4", "RTE-7", "RTE-8", "RTE-9", "RTE-10"]
      note: "Editor file/archive requests are pull. Automatic briefs, continuation prompts, module selection, cache replay and guard prompts are push at their named consumers."
    read_back_signal:
      assessment: known
      basis: wired
      values: ["coarse", "identifier", "inferred-judgment"]
      records: ["RTE-4", "RTE-7", "RTE-8", "RTE-9", "RTE-10"]
      note: "Context budgets select coarsely; task/proposal/variant/cache identities select targeted parts; model judgment selects module variants and summary content. Lexical requirement matching updates state but does not select recalled entries for delivery."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: ["RTE-2", "RTE-3", "RTE-7", "RTE-8"]
      note: "Automatic trace-fed diagnoses/code and retained continuation summaries have wired later consumers; raw-log retention alone is excluded."
    trace_source:
      assessment: known
      basis: wired
      values: ["trajectories", "tool-traces", "session-logs"]
      records: ["OBJ-1", "RTE-2", "RTE-3", "RTE-7"]
      note: "Structured solver/editor trajectories feed evolution; terminal command/output traces feed diagnosis and fallback summaries; chat transcripts feed QA summaries (session-logs mapping)."
    learning_scope:
      assessment: known
      basis: wired
      values: ["cross-task", "per-task"]
      records: ["RTE-3", "RTE-4", "RTE-7", "RTE-8"]
      note: "A shared generation and evidence backlog serve different tasks in the run; summaries continue the same original task. No project-wide reuse guarantee is inferred."
    learning_timing:
      assessment: known
      basis: wired
      values: ["online", "staged"]
      records: ["RTE-3", "RTE-7", "RTE-8"]
      note: "Solver summarization runs during the task; evolution writes pass through staged candidate/gate/promotion phases, potentially while other solves continue. No separate offline learning route is asserted."
    distilled_form:
      assessment: known
      basis: wired
      values: ["natural-language", "symbolic"]
      records: ["OBJ-2", "OBJ-3", "RTE-7", "RTE-8"]
      note: "Diagnoses and continuation summaries are prose; promoted module implementations are executable symbolic artifacts."
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-6]
      note: "Inspected source-reported evaluation artifacts show selected-module use, not a test of dependence on recalled content. Unit tests are test code, not execution evidence; the retained corpus was not exhaustively assessed for such an experiment."
---

# ModularRSI agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-modularrsi-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/modularrsi.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-modularrsi-01/memory-report.md`

**Memory analysis report SHA-256:** `a72d514ba58c78fa445bd589b350617ddba2078dce48afcf1021909a89171a30`

Source-only independent construction. No earlier target review, ingest or cross-system findings supplied analytical evidence. No target code was executed. The specialist input hash is `53959a6cc29639bb2ea21445e0c081de2d129fcc3c7733d9033fccf6c7a1eb36`.

## Boundary and evidence

ModularRSI is a builder or improvement plane including its specialized modular solver runtime. This is a named **subsystem-only** analysis within a Harbor-derived repository, not a claim to audit every bundled benchmark adapter, agent or application. Included: the evolution/evaluation launchers, `src/harbor/agents/terminus_2_modular/`, released `generations/merged_active/`, and bounded associated documentation and retained run artifacts. Shared Harbor model, chat, task and environment machinery is followed at the dependency interface when required. External providers, Docker/E2B internals, benchmark evaluators/datasets, unrelated Harbor systems, external paper and all unstated deployments are excluded.

The repository is the sole source allowlist at full Git commit `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`, operational root `/home/zby/llm/commonplace/related-systems/IQuestLab--ModularRSI`. Every evidence read is commit-addressed with replacements disabled. A truncated initial whole-repository tree listing was discarded as evidence; scoped listings and selected complete ranges supplied navigation and findings. This analysis traces main progression and material alternates; it does not prove semantics of every possible generated module. Neither bundled output nor source comments establish a controlled causal experiment.

## Source register

| ID | Kind and identity | Revision / evidence layer | Inspected scope and anchors | Gaps |
|---|---|---|---|---|
| SRC-1 | Git `https://github.com/IQuestLab/ModularRSI` | `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`; implementation | Launchers, modular agent/kernel/composers/library, editor tools, evolution controller and its diagnosis, promotion, confirmation and task interfaces. Concrete full paths accompany records and quotes. Memory report adds scoped storage/context implementation evidence. | Provider and infrastructure internals, external benchmark/task definitions and unrelated Harbor paths unassessed. |
| SRC-2 | Git `https://github.com/IQuestLab/ModularRSI` | Same full revision; doctrine/design and attributed performance report; separately, implementation in selected released modules | `README.md`; `generations/merged_active/README.md`, `PROVENANCE.json`, selected generation modules; native descriptions, prompts and editor doctrine where quoted | External paper/dataset not read; documentation comments can lag executable branches. |
| SRC-3 | Git `https://github.com/IQuestLab/ModularRSI` | Same full revision; observed-run artifacts supplied by author, plus separately identified prospective tests | `trajectories/mergefinal/run-1/result.json:1-100`, `trajectories/mergefinal/run-1/tasks/fix-git/agent/trajectory.json:1-75`; target test filenames used for navigation and specialist's explicit selected tests | Inspectable logs show recorded events, not our execution. No baseline-linked causal experiment or complete run provenance audited. Test source is not a test execution. |

## Shared records

### Components

CMP-1 — evolution controller and installed modular kernel. **Wired** Python orchestration with local archive/generation trees, bounded parallel task rolls, one background reflection, and up to two proposal lanes. Launch defaults select a module to evolve; runtime composition selects implementations separately. SRC-1, `scripts/evolve.sh`, `src/harbor/agents/terminus_2_modular/self_evo/phase0.py:171-255`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:2499-2705,2805-2945,3040-3146`.

CMP-2 — model-facing investigator, routing/clustering, editor, reviewer, composer, solver and context-summary roles. Distributed-parametric computations are resolved through configured model-name/API endpoint strings and LiteLLM-facing interfaces; exact weights/version resolution and provider-side state changes are **uninspected**. The inspected module-edit mechanism changes Python/prose artifacts; it is not evidence of parameter optimization. Each role has a distinct channel: file-tool investigator/editor/reviewer loop; one-shot routing/clustering prompts; per-task module selector; task/tool conversation; summary subagent. Same configured endpoint does not establish independent reviewers or fixed hidden parameters. SRC-1, `src/harbor/agents/terminus_2_modular/agent.py:38-195`, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py:233-252,393-433`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py:426-465`. Local request configuration is **wired**; hidden semantic processing is **uninspected**.

>     async def _ask(prompt: str) -> str:
>         from harbor.llms.base import OutputLengthExceededError
>         from harbor.llms.lite_llm import LiteLLM
> 
>         llm = LiteLLM(model_name=model_name, api_base=api_base, api_key=api_key)
>         # The prompt asks for citations and a per-variant dismissal, so replies
>         # are long by design — and on a reasoning model the hidden reasoning eats
>         # the same budget, so a ceiling sized for the visible answer alone is far
>         # too small.
>         try:
>             resp = await asyncio.wait_for(
>                 llm.call(prompt=prompt, max_tokens=max_tokens), timeout=timeout
> --- `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

CMP-3 — Harbor task/environment interfaces and operating principal. Human operator supplies dataset, module lock, endpoints, credentials, concurrency and timeout configuration. Solver effects go through the chosen Harbor environment; local editors run with `environment=None`. Candidate Python is imported in the host process by discovery/smoke, so file-tool path checks are not a deployment-wide isolation envelope. Capability surface includes local file reads/edits, dynamic Python execution and solver terminal/tool effects; current grants are configured paths/endpoints and inherited process privileges. The deployed host/container/network isolation is **uninspected**. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py:120-239`, `src/harbor/agents/terminus_2_modular/self_evo/task_runner.py:47-215`, RTE-3 and RTE-5.

### Operative objects

OBJ-1 — task trajectories and outcome evidence. JSON trial outcomes plus ATIF trajectories, episode observations, module-call traces, bundles and scalar reward summaries. Producers are task runtime and external task verifier; diagnosis, routing and confirmation consume derived summaries and raw permitted paths. Reward values are acquisition of evaluator output, not a proven answer oracle. Retained sample trace directly records `planning_with_guard` selection and invocation; aggregate run output records completed/error counts and scores. Full linkage of those artifacts to this release's exact source tree is **uninspected**. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/task_runner.py:188-215`; SRC-3 sample above.

>       "bundle": {
>         "agent_loop": "planning_with_guard",
>         "observation": "baseline",
>         "context_mgmt": "baseline",
>         "tools": "baseline",
>         "verification": "baseline",
>         "tool_helper": []
>       },
> --- `trajectories/mergefinal/run-1/tasks/fix-git/agent/trajectory.json` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

>           "module": "agent_loop:planning_with_guard",
>           "call": "run",
>           "summary": "→ start"
>         },
> --- `trajectories/mergefinal/run-1/tasks/fix-git/agent/trajectory.json` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

OBJ-2 — diagnosis findings and proposals, a retained structured family with distinct operative parts: observations/gaps, causal hypotheses, proposed behavioral deltas, supporting finding identifiers, scope/routing judgments and proposal states. Natural-language claims inside JSON-like records are individually addressable by fields and references. A finding that a module caused a failure is a candidate explanation, not implied by the outcome. Proposal content reaches implementers together with its retained reason and all resolved supporting findings; missing support is explicitly marked. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py:191-243`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py:117-175`, RTE-2/RTE-3. Operational proposal status and causal content are assessed separately in the epistemic overlay; storage does not promote either into truth.

>     instruction = _PREAMBLE.format(
>         pid=proposal.proposal_id,
>         lane=proposal.lane,
>         action=proposal.action or "?",
>         target=target,
>         delta=proposal.behavioral_delta or "(not stated)",
>         why=proposal.causal_hypothesis or "(not stated)",
>         shape=shape,
>         n=len(found),
>         findings="\n\n".join(_render_finding(r) for r in found) or "(none)",
>         missing=missing_block,
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

OBJ-3 — candidate and retained generation module source trees. Python source plus descriptions, niche metadata and optional bundle configuration. They are operational code, may also express claims about suitable task conditions, and can be imported before final promotion during smoke. Staging, generation rename and archive filtering provide recoverable version selection, not transactional rollback of arbitrary module effects. Released variants constitute inspectable candidate artifacts, so their original evolutionary production, critique and acceptance phases are **not determinable**, not “no instance observed.” A sampled runtime artifact evidences use of a named variant, without establishing exact byte identity or causal benefit. SRC-1 library path import; SRC-2 release README; SRC-3 sample.

>             spec = importlib.util.spec_from_file_location(synthetic_name, mod_file)
>             if spec is None or spec.loader is None:
>                 _logger.warning("Could not build spec for %s", mod_file)
>                 continue
>             mod = importlib.util.module_from_spec(spec)
>             sys.modules[synthetic_name] = mod
>             try:
>                 spec.loader.exec_module(mod)
>             except Exception as exc:
>                 _logger.warning("Failed to load %s: %s", mod_file, exc)
>                 sys.modules.pop(synthetic_name, None)
>                 continue
>             register_fn = getattr(mod, "register", None)
>             if callable(register_fn):
> --- `src/harbor/agents/terminus_2_modular/library.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

OBJ-4 — module archive and selection metadata. Retained names, niches, ancestry/status and optional pins determine which implementations the composer can choose; runtime cache can retain a task's selected bundle. These records represent the system's own available machinery. Archive sync follows a successful generation move, and an exception does not undo that move, so source tree and registry can diverge. Scalar comparison later marks regressors superseded. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py:193-223`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py:187-350`, RTE-4.

OBJ-5 — editor-memory entries. Retained change/verdict records written by promotion/rollback orchestration, separately from the active proposal backlog. Whether a formatter is actually consumed is settled by the integrated memory audit below, not by its filename. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:2921-2958,2962-2988`.

OBJ-6 — solver invocation state/context. In-memory chat, task/loop progress, selected module instances, terminal observations, completion counters and summary/handoff material, with logs emitted through the recorder. Model-produced summaries may preserve, omit or reinterpret prior content. The installed package and released generation contain distinct module implementations, resolved by selected library and installed imports; no all-variant equivalence is inferred. SRC-1, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py:194-218,348-433`, `src/harbor/agents/terminus_2_modular/modules/agent_loop/baseline.py:111-378`.

| ID | Additional retained object |
|---|---|
| OBJ-7 |  `history_pass.json`, `router_ledger.json`, `review_health.json`. These persist per-task latest-pass addresses, outcome/cooldown counters and review skip history; symbolic access/control state derived from operation. SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:1270-1322`; `src/harbor/agents/terminus_2_modular/self_evo/router.py:110-215`; `src/harbor/agents/terminus_2_modular/self_evo/review_verdict.py:100-126`. |
| OBJ-8 |  optional instruction-hashed composer cache. Files retain chosen symbolic bundle names/params, not a reasoning trace. SRC-1 `src/harbor/agents/terminus_2_modular/kernel/orchestration.py:80-134,215-265`. |
| OBJ-9 |  accumulated terminal scrollback, requirement-completion set, command history, parse-recovery response and verifier-reason state inside selected released variants. In-memory working memory; terminal log is a file-backed input. SRC-2 `generations/merged_active/gen_0/modules/observation/terminal_scrollback.py:98-218`; `generations/merged_active/gen_0/modules/agent_loop/planning_with_guard.py:199-217,240-307,431-575,1028-1068`; `generations/merged_active/gen_0/modules/agent_loop/parse_error_recovery.py:82-147`. |

| Annotation | Evidence and precise scope |
|---|---|
| Memory annotation for OBJ-1 | Raw solver/editor trajectories, tool messages, bundle/module traces and outcome fields. JSON/files plus in-memory trial summaries; prose and symbolic metadata. Source evidence for investigators and gate/confirmation routines, not automatically distilled memory. SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py:483-550`; `src/harbor/agents/terminus_2_modular/kernel/orchestration.py:265-307`. |
| Memory annotation for OBJ-2 | Findings and proposals. Backlog findings keep raw parsed findings, parse status, supporting tasks and provenance. Proposals preserve causal hypothesis, behavioral delta, finding IDs and event-folded lifecycle state. Files under `backlog/`, primarily JSONL; prose plus symbolic fields. SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/backlog.py:41-82,155-182`; `src/harbor/agents/terminus_2_modular/self_evo/proposals.py:68-83,121-168,221-252`. |
| Memory annotation for OBJ-3 | Imported seed/merged modules and staged/promoted `gen_N/modules` Python trees. Executable content, with descriptive prose carried alongside; persisted filesystem generations, loaded into Python. SRC-1 `src/harbor/agents/terminus_2_modular/library.py:128-193`; SRC-2 `generations/merged_active/README.md:1-17`. Shipped provenance is a source claim, not reconstruction of the missing training history. |
| Memory annotation for OBJ-4 | `archive.json`, module descriptions/niches, parent IDs, addresses, generation and active/superseded/excluded status. Access/selection metadata, not the full executable payload. SRC-1 `src/harbor/agents/terminus_2_modular/archive.py:79-104,218-261`; `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py:66-121,353-441`. |
| Memory annotation for OBJ-5 | `editor_memory.jsonl`: automatic append-only attempted-change/verdict entries; 280-character change cap. Formatter offers recent 12 entries for a module plus rolled-back/no-help taboo entries. Storage and formatting are implemented; no production caller of `compact_index` was found in the named implementation subtree. SRC-1 `src/harbor/agents/terminus_2_modular/self_evo/editor_memory.py:15-90`; `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:2393-2413,2925-2990`. |
| Memory annotation for OBJ-6 | Solver invocation chat/context and continuation state; natural-language messages, structured role/history data and retained subagent trajectory files. Includes proactive and reactive QA, short-summary and terminal-screen alternatives. SRC-1 `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py:73-224,247-285,384-433,506-703`; SRC-2 `generations/merged_active/gen_0/modules/context_mgmt/baseline.py:188-221`. |

### Routes

RTE-1 — evolution scheduling and recovery. **Wired**. Operator starts the launcher; phase0 supplies bounded task list, locked module, epochs, attempts and limits. Controller seeds module-only generation and archive, validates inherited pins, creates deterministic shuffled task order, resumes aligned progress, and runs tasks concurrently. One per-task dynamic composition is captured for subsequent same-bundle rolls. Valid groups supply pending summaries; invalid groups are excluded from reflection. After configured completed-task count, one background reflection receives a batch while solver work continues on the prior generation. On promotion, newly launched work uses the newest generation. Tail work is reflected before final metadata. Task order mismatch moves old progress aside; other provider/task failure handling is local. Return is OnlineEvoOutcome with records and final generation; source artifacts and progress persist. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:2499-2705,2805-2945,3040-3146`. Same-bundle repetition reduces one source of variation; it is not by itself an intervention separating module effect from sampling or other changes.

>         _save_progress(archive_root, records, prior=prior_progress)
>         # Rolling reflection: every `reflect_every` COMPLETED TASKS (not rolls),
>         # run in the BACKGROUND so the pool keeps launching. One at a time
>         # (mutex): while a reflection is in flight, completions accumulate and
>         # the next window fires as soon as it returns.
>         if reflect_task is None and tasks_since_reflect >= reflect_every:
>             batch = pending_summaries
>             pending_summaries = []
>             tasks_since_reflect = 0
>             anchor = records[-1] if records else None
>             reflect_task = asyncio.create_task(_do_reflect(batch, anchor))
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

The RTE-1 improvement trigger is bounded experiment/curriculum operation. All-pass batches skip the reflection path before efficiency investigation; within a failing batch, diagnosis can prioritize correctness then consider wasteful passing cases. No open-request deployment learning is inferred from the experiment launcher. Controller task ledger is a self-representation of progress and prior outcomes; changed outcomes update it and modify routing/recovery. No improved capacity follows merely from that reflection.

>     """Collect findings, implement selected proposals, and run the gates."""
>     if not any((summary.reward or 0) < 1.0 for summary in pending_summaries):
>         _logger.info(
>             "all %d pending trials passed; skipping reflection",
>             len(pending_summaries),
>         )
>         return _ReflectionOutcome(
>             triggered=False, promoted_gen=None, discard_reason=None
>         )
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

RTE-2 — trajectory investigation, evidence routing and proposal retention. **Wired** interfaces. Task classifier separates mixed outcomes, fixable all-fail and cooldown/stuck cases, excludes infrastructure-only rolls, and pairs same-task success/failure where available; historical pass or single-sided failure are alternatives. Investigators read module source and permitted raw trajectories in disposable staging, then return structured findings. Errors become explicitly nonculprit/error records. Findings enter backlog; model judgments assess routing, equivalent interventions and whether a successor covers a gap. Those judgments shape proposal evidence and later work selection; they are not independent task tests. Source: `src/harbor/agents/terminus_2_modular/self_evo/router.py:194-324`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:1324-1477`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py:117-175,426-465` (SRC-1).

>     findings = list(await asyncio.gather(*[_investigate(it) for it in route.diagnose]))
>     snapshot = {"step": step_id, "router": route.buckets, "findings": findings}
>     (findings_root / f"{step_id}.json").write_text(
>         json.dumps(snapshot, indent=2, ensure_ascii=False)
>     )
>     _ingest_findings_to_backlog(archive_root, snapshot, route.diagnose)
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

For this route, formulation of causal hypotheses is **afforded** by explicit fields/prompts and model calls; delivering retained hypothesis and evidence into the implementer is **wired**. Actual validity of a new hypothesis is **uninspected**. Recurrence broadens supporting examples but does not identify causality. Natural-language equivalence/coverage classification is **wired** as a model-judgment route, with semantic correctness **uninspected**. Prior rationale is retained in the proposal and read by the implementer; historical editor-memory advice is a separate route audited below.

RTE-3 — proposal implementation, gate checks, promotion and later retirement. **Wired**, with branch-specific guarantee strength. Portfolio selects at most one open proposal per lane by untried first, older first, broader task/window support then deterministic tie-break. Each implementer receives its own proposal's behavioral delta, causal rationale and evidence; new files, modifications and replacements are distinct intended actions. Local editor must finish with executed commit action and at least one edit, then pass fast smoke, action-shape and niche checks. Review examines diff/intent/trajectory evidence for effectiveness and overfit in a disposable copy. Structured verdicts can reject proposal direction or implementation, shaping the one rewrite opportunity and eventual taboo state. SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py:60-132`, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py:212-238`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:1480-2007`, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py:226-450`.

>     # Critical: a clean run (no exception) where the editor never emitted
>     # <commit_patch/> means the editor used all its turns without finalizing.
>     # That should NOT count as success — driver would otherwise promote an
>     # unintended no-op or partial patch.
>     committed, n_edits = _trajectory_commit_and_edit_counts(traj_path_opt)
>     success = ran_clean and committed
> --- `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

The RTE-3 model review is a consequential criticism route: it asks whether the mechanism targets evidenced failure and avoids task-specific overfit, then its accepted/rejected result can control admission. Actual content-directed criticism of a particular evolved candidate and improved capacity attributable to it remain **uninspected** without linked evolutionary records. Its force is not unconditional. Timeout or raised error returns passed/skipped before skip-health counting. Missing structured submissions pass until the health breaker blocks. Thus “every promoted candidate received affirmative critique” is not an invariant. File-level partial acceptance is disabled in the actual verdict return despite an older downstream branch.

>         discard_staging(review_root)
>         return _ReviewResult(
>             passed=True, verdict="skipped", reason="review timed out (infra)"
>         )
>     except Exception as exc:
>         _logger.warning("review gate errored (%s); NOT blocking promotion", exc)
>         discard_staging(review_root)
>         return _ReviewResult(
>             passed=True, verdict="skipped", reason=f"review errored: {exc}"
>         )
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

>     verdict = review_verdict.read_verdict_file(review_staging)
>     discard_staging(review_root)
>     if verdict is None:
>         # No structured submission: pass through ONCE (lenient, like the
>         # review-errored path) — but count it, and trip the run-level breaker
>         # on 3 consecutive skips or >10% of >=10 reviews.
>         health = review_verdict.record_review_outcome(archive_root, skipped=True)
>         if review_verdict.breaker_tripped(health):
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

The RTE-3 sanity gate forces the changed variant in a private source copy and checks invocation/activation evidence and code crashes. Ordinary composer selection is recorded by a separate probe and does not gate. Parent/candidate task scores are recorded, not an improvement threshold. A candidate may pass without fixing any task. Bounded smoke/crash repair re-enters editing and reruns relevant smoke/sanity checks; the later sanity-repair branch does not call the preceding model review/action/niche gates again, so their verdict concerns the earlier candidate version. This is a static control-flow inference, not an observed bypass experiment.

>     # The sanity battery discards code crashes. Task failure and infrastructure
>     # timeouts are not treated as implementation breakage.
>     # parent_mean is the batch's IN-SAMPLE reward on the CURRENT gen — recorded
>     # for the evolution log as a reference only, never used to gate.
>     parent_rewards = [
>         float(s.reward) if (s.reward is not None) else 0.0 for s in pending_summaries
>     ]
>     out.parent_mean_reward = (
>         sum(parent_rewards) / len(parent_rewards) if parent_rewards else 0.0
>     )
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

>             if not break_reasons:
>                 out.sanity_passed = True
>                 _logger.info(
>                     "sanity gate passed (all %d tasks ran clean%s)",
>                     len(tasks_to_run),
>                     f", after {repair_attempts} repair(s)" if repair_attempts else "",
>                 )
>                 break
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

>             if not run_fast_smoke(staging_modules).passed:
>                 out.sanity_passed = False
>                 out.discard_reason = "sanity repair broke smoke"
>                 discard_staging(staging_root)
>                 return out
>             out.editor_n_edits += repaired.n_edits
>             out.files_changed = _changed(staging_modules)
>             # loop: re-run the sanity tasks on the repaired staging
> 
>     # Promotion order belongs to the two-lane window because both candidates
>     # share a parent and the second may need to rebase onto the first.
>     out.gates_passed = True
>     return out
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Passing lanes are ordered and promoted by generation move. A second lane rebases onto the first; conflicts reject it, exact absorption supersedes it, and changed-tree gates rerun. Unchanged diff permits reuse of change-local judgment while tree-wide checks rerun. A bookkeeping callback failure leaves the promoted generation standing. Later confirmation compares per-task average pass rates for baseline and variant on shared tasks; default at least three shared tasks and delta below -0.34 retires the variant via archive status. This is a coarse regression policy over opportunistic records, not proof of transfer or component causality. Other module/model/time changes may confound comparison; rollback changes subsequent selection, not prior external effects.

>     target = archive_root / f"gen_{_staging.next_gen_number(archive_root)}"
>     promoted = _staging.atomic_promote(tree, target)
>     if on_promote is not None:
>         try:
>             on_promote(promoted, parent_gen, result)
>         except Exception as exc:
>             _logger.warning(
>                 "archive sync after promoting %s failed (the generation stands): %s",
>                 promoted.name,
>                 exc,
>             )
>     return promoted
> --- `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

>         d = paired_delta(samples, module_type, v, baseline)
>         if d and d["shared_tasks"] >= min_shared and d["delta"] < -margin:
>             out.append({"variant": v, **d})
>     return out
> --- `src/harbor/agents/terminus_2_modular/self_evo/confirm.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

File-tool enforcement owner is EditorFileTools: resolved writes must stay in staging; module lock narrows paths, baseline/pin files are always protected, and selected enforcement paths are off limits. Read helpers permit staging, skill and trajectory roots while blocking named reward/answer files. These are **wired** invariants of those handlers. They are not an OS sandbox: smoke and discovery execute generated Python under host process authority. The real deployment contract must trust candidate code or provide isolation outside these handlers. Reviews' read-only instructions and throwaway copies do not turn all candidate code execution into read-only computation.

>     # Foundation files: refused ALWAYS, lock or no lock. Checked first on purpose.
>     if Path(rel_path).name in ("baseline.py", "active_bundle.json"):
>         return False
>     if not locked_type:
>         return True
>     # Solver helpers are the `tools` type's extension point but live in their own
>     # top-level dir (`modules/tool_helper/`), so a tools-locked lineage must be
>     # able to write there — otherwise it could add no new agent action at all.
>     allowed = {locked_type}
>     if locked_type == "tools":
>         allowed.add("tool_helper")
>     parts = Path(rel_path).parts
>     return len(parts) >= 1 and parts[0] in allowed
> --- `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

>             spec = importlib.util.spec_from_file_location(synthetic_name, mod_file)
>             if spec is None or spec.loader is None:
>                 report.fail(f"could not build spec for {mod_file}")
>                 continue
>             mod = importlib.util.module_from_spec(spec)
>             sys.modules[synthetic_name] = mod
>             try:
>                 spec.loader.exec_module(mod)
> --- `src/harbor/agents/terminus_2_modular/self_evo/smoke_tests.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

RTE-4 — per-task module composition and module loading. **Wired**. Kernel loads available implementations, optionally consumes instruction-keyed composer cache, else selects editor-static, dynamic or static composition. Dynamic composer filters archived superseded/excluded variants, non-solver implementations and duplicate declared niches, retains pinned foundation, and offers variable types plus helpers to a model using task instruction/descriptions. Invalid choices retain baseline; exceptional failure returns default bundle with available pin preservation. Helper selection defaults to inclusion and allows removals. Chosen names instantiate code and are written into trajectory metadata; installed kernel traces protocol-method calls. Calls establish execution at that instrumentation grain, not causal improvement. Static/cache branches bypass normal dynamic ranking; default evaluation uses all types from released modules. SRC-1, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py:215-311,348-433`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py:187-350`.

>             if (info.type, info.name) in _NON_SOLVER_IMPLS or not (
>                 _niche.is_solver_selectable(info.niche)
>             ):
>                 continue
>             if f"{info.type}/{info.name}" in skip:
>                 continue  # superseded / excluded per archive.json (F2)
>             key = _niche.niche_key(info.type, info.niche)
>             if key and key in seen_cells[info.type]:
>                 continue
>             if key:
>                 seen_cells[info.type].add(key)
>             by_type[info.type].append(info)
> --- `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

>     if cache_mode == "read":
>         if cache_dir is None:
>             raise ValueError("composer cache read mode requires composer_cache_dir")
>         bundle, cache_path = _read_composer_cache(cache_dir, instruction)
>         services.logger.info("composer cache read: %s", cache_path.name)
>     else:
>         if composer_name == "editor_static":
>             composer = EditorStaticComposer()
>         elif composer_name == "llm_dynamic":
> --- `src/harbor/agents/terminus_2_modular/kernel/orchestration.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

RTE-5 — selected solver loop, observation, tool execution, context changes and completion. **Wired**, with sample named-variant execution **observed** in SRC-3. Installed baseline repeatedly checks session, compresses context if triggered, prepares prompt, calls model, parses tool actions, executes all commands, captures observation and checks selected termination policy. Two malformed responses can end baseline explicitly; model-call failures produce failure result; turn cap and environment timeouts bound operation. Default completion requires repeated model declarations, not benchmark correctness. Variants can change these hooks and may override verifier decisions. Kernel finally tears down tools and exports usage/trajectory metrics; return to Harbor is through AgentContext and files, with external task verification separate. Context compression and released-vs-installed alternatives are audited by the memory lens. SRC-1, `src/harbor/agents/terminus_2_modular/modules/agent_loop/baseline.py:111-378`, `src/harbor/agents/terminus_2_modular/modules/verification/baseline.py:27-35`, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py:393-489`. Generated code can access supplied services/environment; no universal isolation or termination proof covers arbitrary future variants.

>     async def should_terminate(
>         self,
>         state: AgentLoopState,
>         ctx: ModuleCtx,
>     ) -> tuple[bool, str]:
>         consec = getattr(state, "consecutive_complete_signals", 0)
>         if consec >= self.required:
>             return True, f"task_complete confirmed {consec} consecutive times"
>         return False, ""
> --- `src/harbor/agents/terminus_2_modular/modules/verification/baseline.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

The released planning variant can terminate after two completion declarations even if its selected verifier has not requested termination; source comments are not used as proof that its pending-requirement heuristic is sound. SRC-1/SRC-2, `generations/merged_active/gen_0/modules/agent_loop/planning_with_guard.py:1069-1115`.

>         if parse.is_task_complete and state.consecutive_complete_signals >= 2:
>             ctx.services.logger.info(
>                 "PlanningWithGuard: forced termination after 2 consecutive "
>                 "task_complete declarations (iteration %d)",
>                 iteration,
>             )
>             return False
> --- `generations/merged_active/gen_0/modules/agent_loop/planning_with_guard.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

RTE-6 — evaluation launcher. **Wired**. Operator selects fixed module tree, dataset/tasks, model, attempts/concurrency and environment; launcher invokes Harbor run with those agent arguments. Default is released merged tree, dynamic composer, all-type selection and one fix-git task. No evolution controller is invoked by this launcher. Freezing a directory choice does not validate immutable provider identity or protect against arbitrary module-side mutation. Scores originate in external task verifiers and are recorded for analysis; final answer correctness and evaluator validity require their contracts. Source-reported README metrics cover broader experiments than inspected sample artifacts. SRC-1, `scripts/evaluate.sh:19-36,88-124`, SRC-2 README, SRC-3 sample aggregate.

| ID | Additional memory route |
|---|---|
| RTE-7 |  context compaction/continuation. Budget or overflow trigger; model/code producer; prior chat/tool state input; chat and subagent files retention; next solver prompt consumer. Wired, per-task, online, natural-language distilled continuation. |
| RTE-8 |  backlog consolidation and portfolio-to-implementer read-back. Reflection produces findings, model judgment clusters interventions, portfolio ranks open proposals, and identifier-matched evidence/rationale is pushed into a lane brief. Wired, cross-task within the evolution run, staged, natural-language intermediate and symbolic code output via RTE-3. |
| RTE-9 |  operational-history and cached-composition reuse. Per-task outcome history controls diagnosis/cooldown, review history can stop promotion, and configured cache read injects a stored bundle into runtime instantiation. Wired conditional branches; no learning-benefit claim. |
| RTE-10 |  released-variant working-state reuse. Terminal capture supplies retained output automatically; keyword-derived progress and verifier reasons are inserted into later solver prompts; pending requirements and repetition counters affect continuation. Wired within task. |

#### Core ideas in the memory routes

ModularRSI retains two kinds of behavior-shaping content: within-task continuations and cross-task improvement material. Solver chat can be transformed into a summary, questions and answers that the next solver turn receives. Separately, investigators turn solver traces into findings; those findings support proposals whose causal hypotheses and evidence guide an implementer; accepted code becomes a generation that a later solver can execute. These are different task horizons and different forms of authority.

The active evidence route is more concrete than the name `editor_memory` suggests. The proposal route explicitly reconstructs the implementer's instruction from its stored rationale and linked findings:



Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py:226-230`.

By contrast, the append-only editor-memory formatter is a capability with an intended consolidator reader, not an established production injection path at this pin. The current two-lane route explicitly replaces that consolidator. Read-back should therefore be attributed to proposals, archive views and raw-trace tools where it is wired, not inferred from the editor-memory filename.

Context reduction trades retained detail for room to continue. The QA branch first unwinds the existing conversation to free room, then summarizes that remaining history, gives a fresh model the summary/task/screen, and answers its questions using the remaining history plus summary. The next solver receives the resulting compact conversation and answer handoff. Neither the source's word “faithful” nor the three-stage design demonstrates dependence on recalled content.

>         chat._messages = [
>             chat.messages[0],
>             {"role": "user", "content": question_prompt},
>             {"role": "assistant", "content": model_questions},
>         ]
> --- `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py:687-691`.

#### Write side in the memory routes

Memory annotation for RTE-2 is automatic acquisition and transformation. The controller records summaries, chooses tasks to diagnose, lets an investigator inspect allowed code/raw traces, parses its trajectory into a finding, writes a findings snapshot and ingests it into the append-only backlog. `finding_id` includes step/task/lens/position; repeat ingestion avoids duplicate events, but this identity check alone is not semantic deduplication. Parse status is preserved, so an unreadable finding is not automatically an innocent-module verdict.

Memory annotation for RTE-8 adds actual semantic merging: model judgment compares the proposed intervention with open proposals. A match links its finding and support to the existing proposal; otherwise a new proposal retains the behavioral delta and causal hypothesis. A retryable comparison remains distinct from a completed disposition. Causal hypotheses are new claims, so that part is synthesis rather than mere consolidation. Reasons survive and are consumed again by comparison and implementation.

>         if same:
>             _proposals.link_finding(
>                 archive_root,
>                 candidate.proposal_id,
>                 step=step,
>                 finding_id=finding.finding_id,
>                 support_tasks=finding.support_tasks,
>                 reason=why,
>             )
> --- `src/harbor/agents/terminus_2_modular/self_evo/clustering.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/clustering.py:280-288`.

Memory annotation for RTE-3 turns those trace-derived directions into code under staging, records intent before staging is removed, and promotes accepted trees. Adoption raises candidate code to current runtime use. Archive refresh updates niches and tracks parent/supersession relationships; rollback marks a regressing variant superseded. Withdrawal retains history instead of deleting the source tree. A merge can consolidate existing behaviors, but the action label alone does not guarantee that the generated code introduces no new claims or behavior.

>         for e in existing.values():
>             if e.qual in sup_quals and e.status != "superseded":
>                 e.status = "superseded"
>                 updates.append(e)
>         _archive.update_archive(archive_root, updates)
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:847-851`.

The gate is conditional, not an absolute trust certificate. Review timeout/error returns `passed=True` with a skipped verdict. Missing structured verdicts have a separate persisted circuit breaker. Isolated imports can resolve sibling imports to installed package code; the source explicitly limits that check. Discovery executes imported modules during registration, before composer filtering, so an excluded entry is not thereby isolated from import-time execution. These qualifications affect the authority of OBJ-3, not whether code read-back is wired.



Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:1090-1092`.



Source anchor: `src/harbor/agents/terminus_2_modular/library.py:159-161`.

Memory annotation for OBJ-5 records provisional changes and later rollback observations automatically, but the stored short change description need not retain the causal reason. The formatter can truncate it further to 90 or 110 characters. The production route searches described below found writes, not a subsequent consumer of the formatted result. Do not count this capability as an additional demonstrated learning loop.

Memory annotation for RTE-7 has three branches. The main QA transformation retains a summary in the question prompt and an answer continuation, plus subagent trajectory files. It asks what was learned and how problems were resolved, so reasons can be retained and delivered; it does not ensure that every prescription keeps its reason. At defaults, proactive summarization begins below 8,000 free tokens, and unwinding seeks 4,000 free tokens by dropping tail message pairs before summarization. Overflow may instead yield a short model-generated continuation from the task and last 1,000 terminal characters, or use the task/screen directly without an LLM. The short model response is a trace-fed derived continuation; the final raw screen fallback is retained observation, not a new learned claim.

>             short_response = await chat._model.call(prompt=short_prompt)
>             self._update_subagent_metrics(short_response.usage)
>             self._collect_subagent_rollout_detail(short_response)
>             handoff_prompt = (
>                 f"{original_instruction}\n\nSummary: {short_response.content}"
>             )
> --- `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py:190-195`.

The package resets history to the system message on the two fallback branches. The released context baseline omits that reset; it returns the existing unwound chat. The released baseline loop also uses `comp.handoff_prompt` directly and synthesizes a “Technical difficulties” response when fallback chat fails. The package rebuilds the selected tool protocol around the summary and propagates failure. Released `planning_with_guard` and `parse_error_recovery` import the package `BaselineAgentLoop`, so one selected bundle can combine release context management with package loop behavior. This is an executable dependency distinction, not merely stale prose.

>             self._reset_chat_to_system_message(chat)
>             return CompressResult(
>                 chat=chat,
>                 handoff_prompt=handoff_prompt,
> --- `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py:196-199`.

>             handoff_prompt = (
>                 f"{original_instruction}\n\nSummary: {short_response.content}"
>             )
>             return CompressResult(
>                 chat=chat,
> --- `generations/merged_active/gen_0/modules/context_mgmt/baseline.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `generations/merged_active/gen_0/modules/context_mgmt/baseline.py:193-197`.

>                 llm_response = LLMResponse(
>                     content="Technical difficulties. Please continue with the task.",
>                 )
> --- `generations/merged_active/gen_0/modules/agent_loop/baseline.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `generations/merged_active/gen_0/modules/agent_loop/baseline.py:615-617`.

> from harbor.agents.terminus_2_modular.modules.agent_loop.baseline import (
>     BaselineAgentLoop,
> )
> --- `generations/merged_active/gen_0/modules/agent_loop/planning_with_guard.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `generations/merged_active/gen_0/modules/agent_loop/planning_with_guard.py:33-35`.

Memory annotation for RTE-10 retains a bounded working state. Scrollback fallback retains at most twice its configured output budget (default output budget 200,000 bytes); older content is forgotten. Requirement completion uses heuristic keyword overlap with commands, output and terminal observations; it is not proof that a requirement was met. A hard reset clears accumulated chat, command history and completion state and reconstructs requirements from the original task. Parsed responses and reasons can guide subsequent prompts without being persisted as reusable cross-task knowledge.

>             encoded = self._accumulated.encode("utf-8")
>             if len(encoded) > self.max_bytes * 2:
>                 self._accumulated = encoded[-(self.max_bytes * 2) :].decode(
>                     "utf-8", errors="ignore"
>                 )
> --- `generations/merged_active/gen_0/modules/observation/terminal_scrollback.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `generations/merged_active/gen_0/modules/observation/terminal_scrollback.py:174-178`.

#### Read-back in the memory routes

Memory annotation for RTE-8 pushes at most one open proposal per lane (default maximum two). The portfolio orders by attempts, age, distinct supporting tasks/windows and stable jitter. The lane brief selects all stored findings by the proposal's finding IDs, with a 6,000-character cap per rendered finding and an explicit missing-evidence notice. There is no aggregate finding-count or token cap at this assembly point. The implementer receives the causal hypothesis as well as the prescribed behavior, so later diagnosis can address the stated reason. This supports rationale consumption, not correct reasoning or benefit.

>         proposal.attempts,  # 1. never attempted first
>         _age_key(proposal.created_step),  # 2. waiting longest first
>         -unique_tasks,  # 3. broader task support first
>         -unique_windows,  # 4. seen in more windows first
>         _stable_jitter(seed, proposal.proposal_id),  # 5. stable random
> --- `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py:65-69`.

>     found = [findings_by_id[f] for f in proposal.finding_ids if f in findings_by_id]
>     missing = [f for f in proposal.finding_ids if f not in findings_by_id]
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py:205-206`.

Editors/investigators can additionally pull retained evidence through `read_file`, `grep` and the `archive` tool. Read paths are restricted to staging, skills and the supplied trajectory root; reward/answer-bearing files under trajectories are refused. Scalar pass/fail information is already delivered in the reflection instruction. The archive tool reads actual archive metadata when available and explicitly labels its fallback staging-derived view when an expected archive is missing. It supplies genealogy/status summaries, not arbitrary access to the archive root's JSONL files. These are named consumer interfaces; whether a particular editor called them requires a trace.

>             if lineage:
>                 out = _arch.render_lineage(entries, lineage)
>             elif type_:
>                 out = _arch.render_type(entries, type_)
> --- `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py:855-858`.

>                 rp.relative_to(traj_root.resolve())
>                 if not _is_reward_file(rp):
>                     return rp
> --- `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py:389-391`.

Memory annotation for RTE-4 supplies evolved code to later task runtimes. Dynamic selection uses task text capped at 2,000 characters and available variant descriptions, filtered by status, niche, locks and pins; it makes one model choice rather than retrieving code by embeddings. Helper tools use subset selection biased to keeping all active helpers. The selected payload is Python code: importing/instantiating it gives stronger authority than reading its description. Static baseline and editor-specific composition differ from dynamic selection. Archive failures can fail open, so metadata withdrawal is not an unconditional exclusion guarantee.

>             "There is no reward signal — judge from the descriptions and the task.\n\n"
> --- `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py:399-399`.

Memory annotation for RTE-9 also supports optional cache replay keyed by the exact instruction hash. In read mode it bypasses dynamic composition and supplies the stored bundle to runtime; this is an actual identifier-selected push, not merely a cache-writing API. Cache entries retain names/params and an instruction hash, not the composer's rationale or source-tree hash. The path does not re-run dynamic status filtering. Selection is reproducible only subject to compatible available module implementations.



Source anchor: `src/harbor/agents/terminus_2_modular/kernel/orchestration.py:227-230`.

The same operational route supplies historical passing trials by task name to later diagnosis. The lookup re-summarizes the retained trial and requires its reward still indicate a pass; missing data becomes a single-sided investigation. Router cooldown controls whether repeated failure warrants further reflection, and review-health counters can condition promotion. These are symbolic updates that alter future operation, separate from model-authored hypotheses.

>             summary = summarize_trial(Path(d))
>         except Exception:
>             return None
>         # only a still-verifiably-passing summary is a valid contrast partner
>         if summary is None or summary.reward is None or summary.reward < 1.0:
>             return None
>         return summary
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:1313-1319`.

Memory annotation for RTE-7 injects its handoff on the next solver turn. The package's `_protocol_safe_handoff` reconstructs the tool contract with at most 20,000 characters of the last terminal prompt; this static contract restoration accompanies memory delivery but is not itself learned memory. Summaries may omit rationale or contain errors; no semantic guarantee is added by grammar restoration.

>         return (
>             f"Compacted progress summary:\n{clean}\n\n"
>             f"Active task and response protocol:\n{protocol_prompt}"
>         )
> --- `src/harbor/agents/terminus_2_modular/modules/agent_loop/baseline.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/modules/agent_loop/baseline.py:606-609`.

Memory annotation for RTE-10 injects accumulated progress and a previous verifier reason before later model calls. All current requirement statuses are rendered; lexical matching decides status changes, not which stored entry to recall. Accordingly `inferred-lexical` is not added to the push-selector union solely because the guard uses keywords.

>         progress_section = self._build_progress_section()
>         if progress_section:
>             prompt = progress_section + prompt
> --- `generations/merged_active/gen_0/modules/agent_loop/planning_with_guard.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `generations/merged_active/gen_0/modules/agent_loop/planning_with_guard.py:1061-1063`.

Memory annotation for OBJ-5 has weaker read-back evidence. A complete commit-addressed search for `compact_index`, `editor_memory` and `editor_memory.jsonl` in the named production subtree found the formatter/loader and write sites, but no external formatter/loader invocation or prompt injection. The editor's allowed file roots do not include the archive root merely because it receives `archive_path`. The unit test calls the formatter; that proves the intended component interface in test code, not deployed injection. The live route says:

>     Note what is NOT here: no consolidator. In the legacy path the editor picks
>     its own direction out of the batch, which is exactly the greedy selection
>     this phase replaces. Here the direction arrives from the backlog and the
>     editor only implements it.
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py:2220-2223`.

#### Comparison rationale in the memory routes

The fourteen-axis profile uses one coherent memory boundary. Files and in-memory objects cover the operative stores; repository distribution is not counted as a runtime repo substrate. Natural-language and symbolic form cover both readable content and executable/control fields. Imported seeds, trace-derived material and deterministic compilation explain lineage; shipped static instruction text is not added as authored memory merely because it is readable.

Knowledge authority belongs to raw traces and diagnoses; instruction to briefs/continuations; enforcement to loaded code and guard state; routing to status/cache/history selection; ranking to portfolio metadata; validation to the review-health gate. No separate `learning` authority value is needed to repeat the existence of trace learning. Write agency is automatic for the scoped acquisition/maintenance routes; starting a run, selecting a seed directory or manually editing release scripts is not an observed manual memory-write route.

The curation union is deliberately route-specific: consolidate summaries, decay bounded history, dedup same-intervention support, evolve code/state, invalidate superseded variants, promote accepted generations, synthesize causal diagnoses. Pure ingestion idempotence and index construction do not establish these operations. A model's merge label is not a guarantee of semantics-preserving consolidation.

Push signals combine coarse budget/status availability, explicit task/proposal/variant/instruction identity matches, and model judgment. Pull applies only to the editor's supported requested reads; an internal `load` function alone is not an additional pull route. Instructions asking a model to read do not prove that it did so. The source-reported sample establishes activation of selected modules, while most memory mechanisms remain statically wired.

Trace-learning fields cover RTE-2/RTE-3 and RTE-7/RTE-8 together: trajectories/tool traces/chat history are transformed automatically into later-consumed prose or code; cross-task staged generation work coexists with per-task online continuation. Intermediate JSON schemas do not erase the natural-language form of the hypotheses or summaries. Raw log retention, raw-screen fallback, lookup caches and unchanged static instruction delivery do not independently establish learning.

Memory annotation for RTE-6 keeps faithfulness not-determinable. The source's retained evaluation README states that held-out runs are not evolution feedback, and the bounded inspected trace reports module invocation, not a recalled-content intervention:

> These are held-out evaluation artifacts. They are released for analysis and
> reproducibility and are not used as evolution feedback.
> --- `trajectories/mergefinal/README.md` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `trajectories/mergefinal/README.md:12-13`.

>           "module": "context_mgmt:baseline",
>           "call": "maybe_compress",
>           "summary": "→ no-op"
> --- `trajectories/mergefinal/run-1/tasks/fix-git/agent/trajectory.json` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

Source anchor: `trajectories/mergefinal/run-1/tasks/fix-git/agent/trajectory.json:27-29`.

Module presence, successful outcomes, proposed same-task comparison logic, and unit test definitions do not by themselves test dependence on remembered content. The retained corpus was not exhaustively searched for all possible such experiments, so “no” would be stronger than this inspection supports.

| Memory route audit | Immediate output and later consumer | Selector/recovery/effect limits |
|---|---|---|
| Audit of RTE-7 | Compact chat and handoff to next solver call; summary subagent files retained | Token/overflow trigger, model-selected summary; raw screen fallback is not derived learning; package/release differ |
| Audit of RTE-8 | Linked proposal evidence and identifier-selected lane brief | Automatic work selection and rationale/evidence delivery; missing support flagged; quality and aggregate prompt size not guaranteed |
| Audit of RTE-9 | Historical success partner, cooldown/review decision, or stored bundle | Task/instruction identifiers and counters; failed historical lookup means no partner; cache lacks source-tree identity and bypasses dynamic filters |
| Audit of RTE-10 | Updated scrollback/requirement/guard state and later prompt/continuation control | Coarse current-state delivery; bounded retention/reset; lexical completion heuristic does not warrant actual requirement satisfaction |


#### Route return, selection and effect audit

| Route | Immediate return/terminal result | Later read-back and consumer | Delegated visibility, invalidation and effect limits |
|---|---|---|---|
| Audit of RTE-1 | OnlineEvoOutcome, records/final generation or propagated failure | Progress and pending evidence restored on matching task order; current generation affects subsequent launches | Task and model/environment config delegated; mismatch resets skips, not full input identity assurance |
| Audit of RTE-2 | Finding snapshot and retained proposal/evidence state | Proposal selector and implementer read referenced evidence and rationale; historical successful trials support future diagnosis | Raw permitted trajectory paths visible; model semantic judgment can be wrong; bounded routing and stale-status handling from memory overlay |
| Audit of RTE-3 | Gate result, discarded staging or promoted generation; later superseded archive status | Composer loads retained variants, later investigations inspect source/trace; proposal state guides rewrite | Review may skip; sanity checks call presence/crashes; loadable code can cause host effects before promotion; no rollback of external effects |
| Audit of RTE-4 | ModuleBundle or fallback; optional cache-only return | Selected code executes; task-keyed cache replay repeats choice | Dynamic filtering is not applied by all static/cache paths; names and call traces do not prove contribution |
| Audit of RTE-5 | Loop result and context/trajectory metrics | Within-task summary/context and observations reach later model calls; exported traces feed evolution via RTE-1 | Variant-specific semantics; environment effects persist externally; completion not correctness |
| Audit of RTE-6 | Harbor evaluation result files/exit | Offline reader and explicitly subsequent analysis; no native training admission in launcher | Evaluator and immutable dataset/model contracts excluded; no inferred feedback from simple results retention |

### Claims

CLM-1 — **claimed** generalizable harness improvement from independent execution experience, successful/failed contrasts and module-wise changes. SRC-2 `README.md:25-41,47-53`; implemented pathway RTE-1/RTE-2/RTE-3/RTE-4, transfer causality **uninspected**.

> ```
> 
> It learns from a benchmark-independent evolution pool, contrasts successful and
> failed trajectories, applies scoped module changes, and integrates only
> candidates that pass validation gates. The study improves Terminal-Bench 2.0
> accuracy from **47.57% to 52.43%** with DeepSeek-V4-Flash-Preview and evaluates
> --- `README.md` @ `b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9`

CLM-2 — **claimed** program checks, diff review and execution validation filter changes, and frozen module library supports evaluation. SRC-2 `README.md:49-53`, `generations/merged_active/README.md`; implementation **wired** with RTE-3 review-skip and repair-version qualifications, RTE-6 selected-tree evaluation. No unconditional improvement, safety, full critique or immutable deployed behavior follows.

CLM-3 — **claimed** README table improves TB2 47.57 to52.43 and reports transfer to other tasks/models. SRC-2 `README.md:57-70`. SRC-3 inspected run aggregate and named-variant trace are direct retained artifacts, but no audited baseline/current-source experiment supports causal attribution here. Cross-task generalization is reported rather than independently established in this result.

### Evidenced absences

Uninspected dependencies, unseen causal experiments and omitted generated-variant internals remain limitations. The narrow read-back absence below has explicit search scope.

ABS-1 — **absent**, bounded production consumer of the named editor-memory formatter/loader in `src/harbor/agents/terminus_2_modular/` at this commit. Exact parent corroboration: `git --no-replace-objects -C /home/zby/llm/commonplace/related-systems/IQuestLab--ModularRSI grep -n -E 'compact_index|editor_memory|editor_memory\.jsonl' b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9 -- src/harbor/agents/terminus_2_modular`. Complete output: editor_memory.py filename constant and compact_index definition; online_evo.py import and three `editor_memory.record` calls. Full editor_memory.py:1-90 inspection confirms `load` is internal to the formatter, and the specialist traces current two-lane implementation and permitted tool roots. This establishes no wired consolidator prompt injection through those named APIs in this subtree. It does not exclude a manual/external caller, arbitrary generated code, or every possible reflective file access. Active proposal read-back is RTE-8, not negated by this absence.


### Behavioral-authority paths

BAP-1 — investigator/router/implementer consumes OBJ-1/OBJ-2 through prompts and file reads; evidence/advisory rationale and work-ranking force; horizon diagnosis window through later proposal reuse. Not epistemic certification.

BAP-2 — editor file-action dispatch controls requested reads/writes within configured roots/module lock; enforcing at those handlers for current edit session. Candidate Python imports have separate host effect boundary.

BAP-3 — evolution controller consumes structural/action/niche/model-review/sanity results and proposal dispositions; permissive/enforcing admission per branch, retaining candidate into later generations. Review errors can bypass affirmation; numeric task improvement is not the admission condition.

BAP-4 — composer/kernel consumes archive/pins/cache/descriptions and selected Python; ranking/routing followed by executable control of later task invocations. Subsequent supersession filters dynamic choice; statically pinned/cached choices require their own validation.

BAP-5 — solver receives accumulated context summaries/observations and module-specific prompt/control changes; advisory model input and executable completion/tool policy during a task. Correctness oracle remains outside model completion.

BAP-6 — historical task lookup/cooldown, review-health and composition cache control later diagnosis, gate admission or instantiated bundle. Consumer is controller/kernel; symbolic file fields have routing/validation force within run or configured cache lifetime. Cache match does not license semantic freshness of code.


## Runtime account

Ordinary evolution uses bounded source-dataset tasks, three attempts by launcher default, one locked module, and periodic diagnosis. Human contribution is configuration and initiation; model investigators propose causal repairs, model routing organizes evidence, fixed ranking schedules proposals, model implementers write, explicit gates can veto, and controller promotes/retires. Source-native “reflection” names this pipeline; the analytical reflection finding separately traces self-representation below. Training task verifier supplies scalar outcome and may use reference answers, but its expected-answer content/provider contract is outside the selected subsystem. Investigators see training outcome summaries; review formatter suppresses reward and file-tool reader blocks answer-bearing paths. Model judgment itself is not an answer oracle. Crash repair may read task execution evidence, so “no benchmark feedback whatsoever” exceeds this code boundary.

The runtime is both a bounded evolution experiment and a separately invocable task solver/evaluation mode. The ordinary solver chooses module implementations, builds a chat from instruction/observation, executes structured terminal/file actions, stores trajectories and ends on selected completion logic or failure/limits. Only outer Harbor task verification supplies task success. Installed kernel/source modules and released generation copies are not interchangeable by assertion; module imports and composition are part of reproducibility.

Four static forcing cases establish limits without execution: (1) review timeout or exception passes a candidate onward, while absent structured verdict can later trip a breaker; (2) a candidate can execute successfully without improving reward, because sanity admission uses crashes/required calls; (3) valid editor file paths do not confine candidate import effects, since smoke/discovery execute Python; (4) a promoted variant may remain unused under normal composition, and later regression retirement relies on enough opportunistic shared-task outcomes. Two-lane rebase additionally scopes reused verdicts to diff versus tree identity. These are control-flow consequences, not observed failure incidents.

**Execution preflight:** no dynamic check planned. Considered launching smoke tests, a stubbed review-error scenario, and real task/evolution runs. Static branches directly settle the described policy distinctions; target execution would additionally import candidate code or require project packages, datasets, model credentials and Docker/E2B. None was run, and no test pass/fail or operational reliability inference is made from nonexecution. Local artifact validation is separate from target-system testing.

## Lens scoping

### Memory/context scope

Full depth. Trigger SRC-1 retained trajectories/findings/proposals/generation archives and context-management routes; OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, RTE-1, RTE-2, RTE-3, RTE-4, RTE-5. Scope is accumulated memory and actual later consumers within named subsystem, not all filesystem or shipped static instructions. Fresh specialist owns detailed source-native inventory, axis profile and bounded uncertainty.

### Epistemic scope

Full depth. Trigger CLM-1 and CLM-2, causal-hypothesis fields, critique/review admission, execution checks and regression retirement. Assess acquisition/diagnosis, proposal work selection, implementation/criticism, gate/recovery/promotion, composition and solver completion/context paths. Omitted benchmark proof/oracle implementations, provider internals and arbitrary future module semantics prevent a system-wide correctness or causal-learning conclusion. Standalone epistemic procedure applied locally as sparse overlay with architectural and candidate-state vocabulary separate.

## Lens outputs

### Memory/context lens

The fresh specialist inventories OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8 and OBJ-9 across RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, RTE-8, RTE-9 and RTE-10. Its adopted source-native findings and minimum source passages are retained on Shared records above; the local report is provenance, not required reading.

Within-task summary continuations coexist with cross-task proposed/evolved harness machinery. Active reason-bearing read-back comes through proposal/evidence briefs and supported file/archive reads. The separately named editor-memory file has writes and a formatter, with no located production consumer in the recorded subtree. Files/in-memory storage and prose/symbolic content have distinct consumers. Automatic accumulation, semantic proposal merging, bounded forgetting, promotion and invalidation are mapped to their actual branches.

All qualifying trace-fed derived writes remain in the profile: RTE-2/RTE-8 diagnosis/proposals to RTE-3 code and later RTE-4 use; RTE-7 QA and short-summary continuation to later solver calls. These establish wired cross-task staged and per-task online trace learning; raw traces, raw-screen fallback and static protocol restoration do not independently do so. Known push signals are coarse, identifier and inferred judgment, alongside requested file/archive pull. Keyword-based requirement status does not become inferred-lexical retrieval merely because it uses text matching. Faithfulness remains not-determinable: the sample shows method invocation, not a remembered-content intervention, and the larger artifact corpus is not exhausted.

Released context/loop alternatives and installed imports prevent a uniform baseline claim. Archive filters do not confine import-time execution, and composition-cache replay bypasses normal selection. No comparison axis asserts actual semantic correctness or attributable improvement.


### Epistemic lens

#### 1. Source-and-claim boundary

System/revision/boundary: see Run identity and SRC-1, SRC-2, SRC-3. Question: how does retained execution evidence become a repair hypothesis, selected code and later relied-on machinery, and what do the admission gates warrant? Assessed: acquisition, contrast diagnosis, proposal work selection, implementation/review, mechanical and execution checks, promotion/retirement, module selection and context-mediated solver behavior. Unassessed: external answer-oracle construction, provider internals, all benchmark experiments and semantics of arbitrary future generated code. Claims: CLM-1 generalizable harness improvement; CLM-2 gated/frozen changes; CLM-3 performance/transfer. These omissions prevent a whole-repository epistemic judgment, a universal correctness guarantee and causal-learning attribution.

#### 2. Epistemic-object inventory

Generic identity/form/storage/progression is canonical-owned; the rows below split operative parts by epistemic content and force.

| Object part | Candidate truth-apt content or none | Input/consumer and warrant limit |
|---|---|---|
| OBJ-1 outcomes/trace | Task success scores and claims that actions/calls occurred | External verifier/runtime supplies; diagnosis and confirmation consume. Validity of underlying reference answer and trace instrumentation outside sampled checks uninspected. |
| OBJ-2 finding part | Alleged failure, gap, causal attribution to module, suggested repair | Investigator receives traces/source. A causal explanation can go beyond observed success/failure; actual new diagnosis not inspected. |
| OBJ-2 proposal part | Causal hypothesis, expected behavioral delta and scope/support claims | Finding router and equivalence judgments assemble; implementation prompt consumes. Connection to a file or repeated task is not causal warrant. |
| OBJ-2 control/status part | No truth-apt candidate in work-state enums and scheduling identifiers | Controller selects, rewrites, rejects or retires; source links/justifications are truth-apt metadata assessed separately. |
| OBJ-3 code behavior | Proposed operational policy; descriptions additionally assert applicability and expected effects | Code supplies formal operational behavior; reader/model interprets description. Existing released candidate artifacts do not establish original generation or acceptance provenance. |
| OBJ-4 selection/status part | Claims about current variant identity/lineage; cache/status primarily control future use | Controller/archive, then composer/kernel. Identity/scope validity is distinct from truth of effectiveness. |
| OBJ-5 change/verdict text | Assertions about what changed and what happened | Controller writes reported disposition; specific later consumer is settled in memory audit. Stored claims are not corroborated explanations. |
| OBJ-6 observation/summary part | Claims about environment, completed work and remaining requirements | Environment/model supplies; subsequent solver consumes. Generated summary's semantic preservation is indeterminate without comparison. |
| OBJ-7 history/review/cooldown parts | Stored outcome references and counters; no new theory in threshold state | Rechecks retained success for historical partner; counters route/stop later work, BAP-6. |
| OBJ-8 bundle cache | No candidate truth-apt output in selected names/params; identity assertion is bounded | Exact task instruction selects cached choice; code freshness unverified, RTE-9. |
| OBJ-9 progress/guard parts | Heuristic assertions of requirements completed, prior failures and terminal state | Variant updates from task/tool evidence and reuses for prompts/continuation; semantic correctness untested, RTE-10. |
| OBJ-6 counters/control part | No new proposed truth-apt theory in counters and selected module references | Loop/completion handlers directly adapt continuation. Correctness cannot be inferred from stop flags. |

For additional retained objects from the specialist, the inventory distinguishes payload inherited from these parts from routing/recovery metadata. Their storage/retrieval/lineage functions are epistemically non-endorsing unless an explicit acceptance route is named.

#### 3. Authority-route ledger

Every row has architectural status **implemented** on the SRC-1 anchors of its canonical route; this status describes available code, not observed operation of a particular proposed repair. The distinct candidate-state account is below. All rows have no mismatch marker unless their Limits cell names one. Force/horizon references the named BAP; retention and checking never imply lifecycle integration.

| Route / single function | Target and content/update relation | Evaluator/condition and timing | Result, epistemic scope and operational authority | Limits / claims |
|---|---|---|---|---|
| RTE-1 check/evidence production | OBJ-1; acquisition/import of verifier outcome, entailed summary/counts | Harbor trial results after each task | Recorded outcome feeds diagnosis, BAP-1; warrants supplied measurement only | External oracle validity and error missingness; CLM-1 |
| RTE-1 lineage/freshness/recovery | Progress identity; no content change to past outcomes | Task index/name alignment on restart | Restore pending work or discard old skip list; controls next tasks | Model/config/evidence identity is not proven by task-order match |
| RTE-2 content transformation | OBJ-2 findings; indeterminate, potentially ampliative causal conjecture | Model compares same-task traces/source, historical pass or single-sided failure | Proposed cause and repair to backlog; advisory BAP-1 | Contrast not intervention; actual semantic conclusion uninspected; CLM-1 |
| RTE-2 content transformation | OBJ-2 proposal grouping; indeterminate semantic consolidation | Model equivalence/successor coverage judgment | Attach evidence, retain or reroute proposal support | YES parsing makes a decision operative, not necessarily correct |
| RTE-2 retention | OBJ-2; no content change on persistence | Findings/proposal write | Availability to later selector/implementer | Retention before acceptance is not lifecycle integration |
| RTE-3 operational admission/selection/consumption | OBJ-2; no content change | Open state, lane, attempts/age/support rank | Grants implementation opportunity, BAP-1/BAP-3 | Prioritization is not epistemic acceptance; broader support is a tie-break after attempts/age |
| RTE-3 content transformation | OBJ-3; non-truth-apt policy/code update plus indeterminate claims in descriptions | Editor given behavioral delta, hypothesis, evidence and action instruction | Staged implementation; formal code can execute during validation | Correctness of translating rationale into code uninspected |
| RTE-3 check/evidence production | OBJ-3; no content change | AST/import/discovery/static contracts, action/niche tests, model review | Structural/mechanism judgments; BAP-3 candidate veto inputs | Load checks not task benefit; critique quality unknown; CLM-2 |
| RTE-3 check/evidence production | OBJ-3; acquisition/import of sanity outcomes and call traces | Forced variant invocation, crash classification | Evidence changed implementation executes and avoids selected crash classes | No task-score improvement criterion; forced invocation not natural selection |
| RTE-3 disposition/acceptance | OBJ-3; no content change | Gate conjunction with skip and repair branches | Allows selected implementation into later library, BAP-3 | Scope is operational admissibility, not accepted general effectiveness; CLM-2 |
| RTE-3 retention | OBJ-3; no content change | Generation move after passing candidate | Preserved code available to subsequent tasks | Registry update nontransactional; no automatic rollback of host effects |
| RTE-3 behavior/policy adaptation | OBJ-4; non-truth-apt selection-status update | Opportunistic paired pass rates below margin, sufficient shared tasks | Superseded status filters future dynamic selection, BAP-4 | Same-task association not isolated component effect; no retrospective undo |
| RTE-4 operational admission/selection/consumption | OBJ-3/OBJ-4; no content change | Archive/niche filters, pins, model choice or static/cache | Choose and instantiate operative machinery, BAP-4 | Selected description is not endorsement of its truth; bypass branches separate |
| RTE-4 check/evidence production | OBJ-1 bundle/call record; acquisition/import | Installed trace wrappers around selected methods | Available execution evidence for later investigation | Tracing failure is nonfatal, and method entry not causal benefit |
| RTE-5 content transformation | OBJ-6 summary; indeterminate semantic reshaping | Context manager/model on token/call pressure | Later solver input, BAP-5 | Semantic preservation and omission effects uninspected; release/package alternatives |
| RTE-5 operational admission/selection/consumption | OBJ-6 and external effects; no content change to retained code | Model tool actions and selected executable hooks | Tool/environment behavior and subsequent prompts, BAP-5 | Arbitrary module semantics and host grants prevent global guarantee |
| RTE-5 disposition/acceptance | Completion signal; no content change | Selected verification/loop policy, baseline repeated declarations | Ends local task loop | Stop permission, not answer acceptance; external verifier separate |
| RTE-7 retention | OBJ-6; no content change after derived continuation | Prompt/history replacement on compaction | Preserves selected summary for next call, BAP-5 | Summary transformation inherits RTE-5 indeterminate content relation |
| RTE-8 operational admission/selection/consumption | OBJ-2; no content change | Proposal identifier chooses supporting findings and rationale | Assembles implementer brief, BAP-1 | Missing support explicit; delivery does not prove reasoning |
| RTE-9 lineage/freshness/recovery | OBJ-7 historical success; no content change | Re-summarize saved task trial and require current recorded reward≥1 | Supplies diagnosis contrast or none, BAP-6 | Re-reading a reward is not rerunning its oracle |
| RTE-9 operational admission/selection/consumption | OBJ-7/OBJ-8; no content change | Cooldown/review counters or instruction-hash match | Skip/allow work or instantiate stored bundle, BAP-6 | Cache bypass and exception branches bound force |
| RTE-10 content transformation | OBJ-9; indeterminate heuristic requirement state | Command/output keyword match and selected loop hooks | Changes progress assertion and subsequent prompts | Semantic task completion not proven |
| RTE-10 behavior/policy adaptation | OBJ-9; non-truth-apt control update | Guard counters, reset and continuation conditions | Changes subsequent calls/stop policy, BAP-5 | No epistemic endorsement from enforcement |
| RTE-6 check/evidence production | OBJ-1 evaluation outputs; acquisition/import | External task evaluator after fixed-tree solver run | Reported score, available experimental outcome | Experimental design/current identity not established by launcher; CLM-3 |

Reason retention and theory use require separate statuses. The source explicitly provides causal-hypothesis and behavioral-delta fields and prompts an implementer to act on them: **formulation afforded**, retained-field delivery **wired**, correct operative application of a particular hypothesis **uninspected**. Reviewer instructions ask for errors in mechanism/overfit: **content-directed criticism afforded**, structured consequence channel **wired**, valid criticism of an inspected evolutionary candidate **uninspected**. Proposal versus implementation rejection and rewrite are **wired** changed-reliance/revision mechanisms, but actual content-level revision and attributable capacity improvement are **uninspected**. A theory surviving review could change later reliance; no text change is required by this analysis, and no particular such event is evidenced.

#### 4. Per-object lifecycle disposition

For OBJ-1, acquisition/import and deterministic summaries are non-ampliative or entailed within the supplied fields; discovery lifecycle **not applicable**. The sampled trace/aggregate is an observed artifact of runtime recording, not direct evidence that the verifier was correct. Its provenance is bounded to supplied Git bytes.

For OBJ-2 finding/proposal content, transformation is **indeterminate** without an actual instantiated diagnosis: restatement, implication, or ampliative causal explanation remain possible. If a diagnosis asserts that a module change would prevent an observed failure, that non-entailed causal claim would be an ampliative conjecture. Architecture has **implemented** observation acquisition (RTE-1), formulation opportunity and support routing (RTE-2), implementation/criticism opportunity and operational admission (RTE-3), and retained later machinery (RTE-4/RTE-5). For each particular diagnosis's observation linkage, conjecture, derived consequence, semantic test, epistemic acceptance and post-acceptance integration, observed candidate state is **no instance observed** in the parent's bounded evolution evidence; no candidate-linked proposal/review/gate chain was inspected. No stronger state follows from source prompts. Metadata-only OBJ-2 status has no candidate truth-apt output; relevant direct-update routes RTE-2/RTE-3.

For OBJ-3 code, transformation is a non-truth-apt operational policy update where it merely changes procedure. Its applicability descriptions and claimed mechanisms are truth-apt, and transformation remains **indeterminate**: the released candidate source exists, but original evidence-to-claim derivation is uninspected. Therefore its original conjecture, derived consequence, test, acceptance and post-acceptance epistemic integration have observed candidate state **not determinable**. RTE-3's checks/admission and RTE-4/RTE-5's use are **implemented**. The SRC-3 sample establishes **phase evidenced** for a named variant's recorded selection/method invocation only; it does not pin that name to identical current source bytes or establish knowledge integration after epistemic acceptance. No accepted causal explanation is inferred from operational deployment.

For OBJ-4, source identity/status arithmetic is acquisition, entailed derivation or no-content-change control; discovery lifecycle **not applicable**. Archive/cached identity is not epistemic endorsement. For OBJ-5, retained change/verdict text preserves a controller's report through a **non-ampliative reshaping** route; actual reason truth and any informal hypothesizing beyond its fields remain unknown. A serialized verdict is not a newly validated causal theory. For OBJ-6 summary, transformation is **indeterminate** between preservation, selective abstraction and unsupported reinterpretation; reset/retrieval/formatting does not test semantic faithfulness. Its control counters/references have no candidate truth-apt output; direct update routes are RTE-5 and the memory overlay.

For OBJ-7, historical records/counters have acquisition or entailed-control semantics, discovery lifecycle **not applicable**; RTE-9 checks recorded identity/status only. No lifecycle record for OBJ-8: no candidate truth-apt output in the chosen bundle itself; relevant consumption route RTE-9. For OBJ-9, terminal-state retention is non-ampliative while inferred requirement completion is **indeterminate**: a lexical match can misrepresent fulfillment. RTE-10 implements updates and later prompt/control use; particular semantic correctness or criticism is not evidenced. Additional payloads inherit the explicitly named admission boundary in their canonical record. No undisclosed lifecycle acceptance is imputed to finding identity, expiry, selection, copied code or retained cache state.

#### 5. System claims versus routes

| Claim | Doctrine/design | Implementation | Observed-run and causal support | Bounded finding |
|---|---|---|---|---|
| CLM-1 | Contrastive, module-wise generalizable improvement | RTE-1, RTE-2, RTE-3, RTE-4 establish evidence→proposal→code→later-use pathway | Released variants and bounded trace sample; no linked causal evolutionary comparison | Concrete improvement machinery; attributable theory-guided improvement not established |
| CLM-2 | Program/diff/execution gates and frozen evaluation library | RTE-3 checks, RTE-6 fixed selected tree; skip/repair/host-import alternatives explicit | Current sample is not full candidate gate history | Operational filtering has scoped force; no unconditional critique, performance or isolation guarantee |
| CLM-3 | README reported aggregate gains and transfer | Launchers can collect task results | One run aggregate and named invocation do not reproduce compared populations/design | Reported benefit stays attributed; component effect/generalization uninspected |

#### 6. Bounded conclusion

ModularRSI acquires task outcomes, proposes module-level explanations, organizes retained support, and gives those proposals concrete code-producing and admission routes. It preserves reasons at the proposal-to-implementer interface and distinguishes mistaken direction from faulty implementation. Its validators license loadability, contract conformance, allowed change shapes and selected execution facts at specific boundaries; model review may permit or reject on interpreted mechanism evidence. Neither that judgment nor numeric regression retirement supplies a general correctness or causal-learning license. Operational admission and subsequent code use are supported separately from accepted ampliative knowledge. Provider opacity neither proves nor disproves hidden reasoning; the missing evidence is candidate-linked criticism and attributable capacity improvement at a stable comparison boundary.


## Reconciliation

The complete fresh specialist report matches system/run, full revision, boundary and frozen input hash; method hash `7e86ed242caadc095d7f20ccd7fcbcb837b9d62e94fca50656b782c65cb0d675`. Its report digest is in Run identity. Exact mappings:

| Local proposal | Canonical disposition |
|---|---|
| MEM-OBJ-1 | OBJ-7, operational-history/review-state files |
| MEM-OBJ-2 | OBJ-8, instruction-keyed bundle cache |
| MEM-OBJ-3 | OBJ-9, released-variant accumulated working state |
| MEM-RTE-1 | RTE-7, context compaction/continuation |
| MEM-RTE-2 | RTE-8, proposal consolidation and brief read-back |
| MEM-RTE-3 | RTE-9, history and cached composition reuse |
| MEM-RTE-4 | RTE-10, variant working-state reuse |

Existing seed IDs retain their referents. Adopted all seven proposed records, profile and bounded uncertainties. Clarified SRC-2's separately identified released-module implementation layer as well as its doctrine/report layers. Package/release differences amend RTE-5 without asserting all variants identical. OBJ-5 storage/formatting is separate from active RTE-8 proposal delivery; parent corroborated bounded ABS-1 by exact named-subtree search. Payload execution, descriptions, dynamic filters and cache bypass are separate authority paths. Both passes independently found review-skip/import authority limits; all evidence is now attached once to canonical records. Retained run artifacts keep observed-run status at the sampled event grain, without claiming causal origin, current-byte identity or faithfulness. No unresolved conflict, precomputed classification or older analysis supplied the specialist's findings.


## Bounded synthesis

ModularRSI joins a retained proposal-and-evidence workflow to an executable library of specialized harness modules. Its strongest supported contribution is **wired** use of task evidence to formulate candidate repairs, submit their code to content-directed model scrutiny plus mechanical/execution gates, and preserve selected variants for later task-specific composition. The repository additionally contains a released variant library and a bounded sampled execution trace showing a named variant ran. These are stronger evidence than a design sketch, but do not establish the complete causal production and benefit of that variant.

**Conjectural learning is uninspected as an attributable improvement claim.** Causal hypotheses and criticisms have operative destinations, retained reasons can guide implementation, and selected code can affect later runs; however the inspected artifacts do not link a specific formulated/criticized theory through valid comparative testing to improved future capacity. The score-reporting claims remain attributed, with no finer component attribution. **Reflection is wired** through representations of the system's own module source, archive status, selected bundle and execution traces: runtime changes alter this evidence, investigators/editors reason over it, and proposal/promotion/selection changes subsequent machinery. A validated self-theory of the theory-building organization is not established. **Self-improvement is wired as a proposal/admission pathway and claimed as empirical benefit; demonstrated attributable improvement remains uninspected** at this evidence boundary.

Three distinctions govern interpreting the result. Passing execution gates establishes narrower facts than improved task performance. Editor file restrictions establish narrower control than sandboxing imported Python. Retained source and descriptions establish available choices, while dynamic selection and actual method calls establish separate degrees of use. Review's lenient branches, later repair paths and archive-sync failures further limit universal admission claims. Concrete candidate-linked evolution records, version-bound module/provider/dataset identities, and controlled held-out comparisons would allow stronger findings without changing these architectural distinctions.

## Limitations

| Limitation | Affected records | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| Excluded Harbor/provider/evaluator internals | CMP-2, CMP-3, RTE-5, RTE-6 | Named subsystem/interface calls | End-to-end isolation, exact model weights and answer-oracle validity | Pinned dependency/deployment and evaluator inspection |
| Partial retained-run coverage | SRC-3, OBJ-1, OBJ-3, CLM-3 | One aggregate and one bounded named-variant trace sample | Complete experiment reproduction or benefit attribution | Linked baseline/candidate trials and experimental design |
| Review skips and version-specific gates | RTE-3, BAP-3 | Exception/timeout, no-verdict, repair branches | Every final candidate affirmatively criticized under same bytes | Candidate-linked gate identity and all-branch audit/tests |
| Arbitrary generated Python | CMP-3, OBJ-3, RTE-3, RTE-4 | Host imports plus file-tool restrictions | Global execution confinement or rollback | Deployed isolation and code-effect controls |
| Selection differs from invocation and effect | RTE-3, RTE-4, BAP-4 | Routing probe, forced sanity, trace | Natural activation, faithful reliance or component benefit | Unforced use and controlled read-back/variant intervention |
| Opportunistic regression samples | RTE-3, OBJ-4 | Same-task averages, minimum/margin | Unconfounded causal ranking or transfer | Stable paired comparisons with relevant confounds controlled |
| Distinct release/package variants | OBJ-3, OBJ-6, RTE-4, RTE-5 | Selected source variants and import path | All variants share baseline guarantees | Exact bundle/dependency resolution and variant-specific runs |

Further memory limits: model summary accuracy and omitted rationale remain uninspected (RTE-7); missing supporting findings and no aggregate assembly budget can weaken the evidence brief (RTE-8); composition replay lacks code-version identity (OBJ-8/RTE-9); and explicit editor-memory consumer absence is limited to ABS-1's named subtree. Candidate-linked traces, current matching code identity and controlled recall interventions would resolve the corresponding conclusions.


## Verification and blockers

### Semantic verification

Checked source boundary and actor ownership, ordinary evolution and solver paths, direct/static/cache alternatives, two-lane rebase, review-skip/repair and host-import forcing cases. Separate code wiring, role prompts, supplied observed artifacts and uninspected causal experiments. Every new ID is mapped without changing existing referents. Hypothesis delivery, actual operative application, criticism validity and attributable capacity remain separate.

Checked complete memory scope/profile against OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8 and OBJ-9, including installed/released context variants and composite payloads. Qualifying trace-fed routes RTE-2/RTE-3/RTE-7/RTE-8 have source, later consumer, task horizon, timing and form retained. Named consumer/trigger/selector distinguishes targeted push, coarse push and genuine requested pull; no lexical selector was inferred from heuristic state updates. Faithfulness uncertainty was preserved. All material integrated claims have bounded primary anchors and supporting quotes; ABS-1 includes exact search scope. Epistemic function rows separate checks, disposition, retention and operational use; architecture and observed candidate states remain distinct. Full-file source quote matching and report/input hashes are verified before publication.


### Deterministic validation

Exact target: `commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-25-modularrsi-01/result.md`; completion checked before publication. Publication verifies source quote occurrence, report/input identity and destination guard. No target runtime test is implied.

### Blockers

none
