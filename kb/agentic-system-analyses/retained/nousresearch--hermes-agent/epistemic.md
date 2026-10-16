---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Hermes Agent epistemic routes: retained facts and skills, recalled-context authority, compression checks and goal evaluation at the frozen revision."
run-id: AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01
reviewed-boundary: "0e427d788d253630d38a3a51cd76849e73cd6925"
---

# Hermes Agent epistemic report

## Source-and-claim boundary

The question is how Hermes turns task and tool content into later reliance, and what its checks license. Scope, exclusions and evidence identity: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). All additional source inspection below is SRC-1 implementation or explicitly labelled doctrine/design at that same commit. No target execution was performed. This is a partial-loop account, not a system-complete negative about acceptance or knowledge production.

The public learning/persistence claim is [RT-CLM-product-work](runtime.md#rt-clm-product-work). A narrower warrant claim appears in the recalled-context wrapper: [EPI-CLM-reference-data](#epi-clm-reference-data). The runtime is provisional: goal gates and the auxiliary completion judge add consequential evaluators beyond the ordinary open-request path. This supplements, rather than supersedes, [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn): its lack of an answer oracle concerns the selected one-shot route, not every shipped mode.

| Entry point or operation | Source path | Coverage and records, or remaining limit |
|---|---|---|
| One-shot, generic dispatch and finalization | SRC-1 `hermes_cli/oneshot.py`, `agent/turn_tool_round.py`, `agent/turn_finalizer.py` | Supplied findings: [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn), [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch), [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff). No new end-to-end read. |
| Tool hooks and admission | SRC-1 `agent/tool_executor.py` | Direct bounded read of pre-hook/authorized-dispatch code; [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch). Hooks may modify or block; hook exceptions return original arguments. These are operational gates, not factual endorsement. |
| Registered memory tool | SRC-1 `tools/memory_tool.py`, `tools/memory_tool_store.py` | Direct registry search and write/load implementation reads: [EPI-RTE-memory-scan](#epi-rte-memory-scan), [EPI-RTE-memory-gate](#epi-rte-memory-gate), [EPI-RTE-memory-retain](#epi-rte-memory-retain). Full pending replay and human UI remain uninspected; prevents claiming every approval path has equivalent semantics. |
| Background fact/skill review | SRC-1 `agent/background_review.py`, `tools/skill_manager_guards.py` | Direct prompt and guard reads; handoff supplied by [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff). [EPI-RTE-review-candidate](#epi-rte-review-candidate), [EPI-RTE-skill-guard](#epi-rte-skill-guard). Fork construction/cancellation only searched, not fully traced. |
| Registered skill management and loading | SRC-1 `tools/skill_manager_tool.py`, `tools/skills_tool.py`, `tools/skills_guard.py` | Direct registry search, guarded-write, scanner policy/cache and loader reads: [EPI-RTE-skill-guard](#epi-rte-skill-guard). Import/install CLI, batch management, preprocessing and full archive/restore paths uninspected; prevents universal safety and replay claims. |
| External recalled context | SRC-1 `agent/memory_manager.py`, `agent/turn_context.py`, `plugins/memory/retaindb/__init__.py`, `plugins/memory/byterover/__init__.py` | Direct sanitizer, deduper, wrapper, API projection and provider prefetch/queue reads: [EPI-RTE-recall-reshape](#epi-rte-recall-reshape), [EPI-RTE-recall-consume](#epi-rte-recall-consume); supplied [MEM-RTE-provider-cycle](memory.md#mem-rte-provider-cycle). RetainDB consumes prior queued results; ByteRover queries at prefetch time. Remote extraction/ranking and initial fact provenance remain uninspected or external. |
| Compression | SRC-1 `agent/context_compressor.py` | Direct summary generation, provenance rejection and message assembly reads: [EPI-RTE-summary-check](#epi-rte-summary-check). Full failure/fallback, pruning and durable archive paths uninspected; prevents complete lineage and recovery assessment. |
| Goal mode in CLI and gateway | SRC-1 `hermes_cli/goals.py`, `hermes_cli/cli_loops_mixin.py`, `gateway/run_goals.py` | Direct gate execution, judge, manager and next-turn enqueue reads: [EPI-RTE-goal-check](#epi-rte-goal-check), [EPI-RTE-goal-disposition](#epi-rte-goal-disposition). Kanban goal variant only searched; cannot generalize manager behavior to it. |
| Session search, web and file acquisition | SRC-1 `tools/session_search_tool.py`, `tools/web_tools.py` | Session-search operations and registry searched, not substantively traced; web/file paths enumerated. Retrieval and output truncation details remain unassessed, preventing a complete source-warrant preservation account. |
| Codex, delegation, plugins and script execution | SRC-1 `agent/codex_runtime.py`, `tools/delegate_tool.py`, `tools/code_execution_tool.py`, `hermes_cli/plugins.py` | Supplied [RT-RTE-codex-turn](runtime.md#rt-rte-codex-turn), [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation), [RT-RTE-code-execution](runtime.md#rt-rte-code-execution), [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission). External internals/actual handlers unresolved; no claim of one universal evaluator. |
| Other CLI and maintenance operations | SRC-1 `hermes_cli/main.py`, `agent/curator.py`, `agent/learning_graph.py`, `agent/learning_mutations.py` | Main CLI searched for memory, skills, curator, learning, memory-graph and update dispatch. Curator/graph modules located but not read; their admission and withdrawal mechanisms remain unassessed. Bounded direct reads of `agent/learning_mutations.py` and `hermes_cli/web_routers/status.py` establish a separate learning-node edit/delete path invoking MemoryStore._mutate directly, not the memory tool's optional approval gate. Full caller authorization, CLI dispatch and prompt refresh remain untraced; memory admission-control coverage is incomplete. Full scheduler, ACP, update and loop-until evaluators remain uninspected. Prevents a system-complete negative about evidence-responsive policy change. |
| Shipped evaluations | SRC-1 `evals/` | File inventory only, including compaction, session-search schema and browser-use experiments. Results and harnesses not inspected. No reported, observed or causal result is imported from their mere existence. |

Missing execution traces prevent findings that any write, evaluator or recalled content actually changed a later action. Missing numerical checkpoints/provider internals prevent training or parameter-update findings; see [RT-CMP-inference-model](runtime.md#rt-cmp-inference-model). Missing user state prevents identifying actual retained propositions. Available but uninspected operations above are inspection limits, not access gaps or evidenced absences.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-entries](#epi-obj-memory-entries) | see record | see record | SRC-1 `tools/memory_tool_store.py` | Actual entries unavailable; policy/preferences are not all truth-apt. |
| [EPI-OBJ-skill-content](#epi-obj-skill-content) | see record | see record | SRC-1 `tools/skills_tool.py` | Procedure correctness and explanatory claims require separate assessment. |
| [EPI-OBJ-recalled-context](#epi-obj-recalled-context) | see record | see record | SRC-1 `agent/memory_manager.py` | Provider provenance unknown. |
| [EPI-OBJ-summary-content](#epi-obj-summary-content) | see record | see record | SRC-1 `agent/context_compressor.py` | Semantic fidelity not established by guard success. |
| [EPI-OBJ-goal-verdict](#epi-obj-goal-verdict) | see record | see record | SRC-1 `hermes_cli/goals.py` | Distinguishes executable gate reference from model completion judgment. |
| [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages) | see record | see record | SRC-1 `agent/turn_context.py` | Container, not a truth certificate. |
| [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call) | see record | see record | SRC-1 `agent/turn_tool_round.py` | Control envelope, not evidence of argument truth. |
| [RT-CMP-inference-model](runtime.md#rt-cmp-inference-model) | not determinable for individuated stored propositions | see record | SRC-1 `agent/turn_api_call.py` | Numerical internals unavailable; inference outputs can be truth-apt independently. |

## Authority-route ledger

Each row is a separate function. Fields owned by canonical records say `see`; implementation is not observed activation. Retention and disposition remain separate even when they share source code. No lifecycle integration after evidence-consuming factual acceptance is established for the inspected memory writes; that is not a system-wide absence.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Candidate generation, not general factual warrant | see record | see [RT-BAP-task-prompt](runtime.md#rt-bap-task-prompt) | SRC-1 `hermes_cli/oneshot.py` | none | none | Non-entailment of an actual output not evidenced. |
| [EPI-RTE-review-candidate](#epi-rte-review-candidate) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/background_review.py` | see record | none | Rule-generation request does not establish produced conjecture or accepted generalization. |
| [EPI-RTE-memory-scan](#epi-rte-memory-scan) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `tools/memory_tool_store.py` | none | none | Threat pattern domain, not fact truth. |
| [EPI-RTE-memory-gate](#epi-rte-memory-gate) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `tools/memory_tool.py` | none | none | Operational admission; human epistemic criterion uninspected. |
| [EPI-RTE-memory-retain](#epi-rte-memory-retain) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `tools/memory_tool_store.py` | see record | none | Saving is not evidence-consuming factual acceptance. |
| [EPI-RTE-recall-reshape](#epi-rte-recall-reshape) | content transformation | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/memory_manager.py` | none | none | Applies to exact dedupe only; sanitizer is separately bounded in record. |
| [EPI-RTE-recall-consume](#epi-rte-recall-consume) | operational admission/selection/consumption | implemented | see record | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/turn_context.py` | see record | see record | Source warrant unknown; delivered authority label is not endorsement evidence. |
| [EPI-RTE-summary-check](#epi-rte-summary-check) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/context_compressor.py` | none | none | Compression intent does not prove preservation. |
| [EPI-RTE-summary-check](#epi-rte-summary-check) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/context_compressor.py` | none | none | Narrow user-attribution test. |
| [EPI-RTE-summary-check](#epi-rte-summary-check) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `agent/context_compressor.py` | none | none | Passing permits summary use, not all summary assertions. |
| [EPI-RTE-skill-guard](#epi-rte-skill-guard) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `tools/skill_manager_tool.py` | none | none | Opt-in security scan and read-before-write have different domains. |
| [EPI-RTE-skill-guard](#epi-rte-skill-guard) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `tools/skill_manager_guards.py` | none | none | Write rollback, deletion refusal and load quarantine are distinct dispositions described in record. |
| [EPI-RTE-goal-check](#epi-rte-goal-check) | check/evidence production | implemented | see record | truth-apt transformation: entailed derivation | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `hermes_cli/goals.py` | none | none | Only exit-status pass/fail proposition is entailed; model completion judgment is indeterminate. |
| [EPI-RTE-goal-disposition](#epi-rte-goal-disposition) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `hermes_cli/goals.py` | none | none | Completion accepted for session stopping, not all task-output claims. |
| [EPI-RTE-goal-disposition](#epi-rte-goal-disposition) | behavior/policy adaptation | implemented | see record | non-truth-apt policy/content update: continuation or parked/done state | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1 `gateway/run_goals.py` | none | none | Direct control adaptation; successful repair unobserved. |
| [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) | operational admission/selection/consumption | implemented | see record | non-truth-apt policy/content update: executable capability registration | see record | see record | see record | see record | see record | Version/configuration checks do not license handler correctness | see record | see [RT-BAP-plugin-handler](runtime.md#rt-bap-plugin-handler) | SRC-1 `hermes_cli/plugins.py` | none | none | Arbitrary handler factual checks unresolved. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-product-work](runtime.md#rt-clm-product-work) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-review-candidate](#epi-rte-review-candidate), [EPI-RTE-memory-retain](#epi-rte-memory-retain), [EPI-RTE-skill-guard](#epi-rte-skill-guard); supplied delegation/RPC records | None supplied | No component intervention or later capacity comparison inspected | There are experience-review requests, writable stores and later model-input channels | Improved capacity and exercised self-improvement are not established by these routes alone; other learning/curation planes remain unassessed. |
| [EPI-CLM-reference-data](#epi-clm-reference-data) | see record | SRC-1 `agent/memory_manager.py`, doctrine/design in implemented wrapper | see record | [EPI-RTE-recall-reshape](#epi-rte-recall-reshape), [EPI-RTE-recall-consume](#epi-rte-recall-consume) | None supplied | No correctness/endorsement evaluator in the inspected wrapper and projection functions; opaque providers may have their own | Recalled text is delivered with a strong reliance instruction | Operational instruction exceeds demonstrated epistemic warrant; unknown original provenance and model compliance. |

## Bounded conclusion

Hermes has several different kinds of consequential check, not one truth oracle. Tool dispatch and configured approvals grant operational permission; memory and skill security scans address suspicious content; compression rejects a particular impossible user attribution; goal gates and a model judge determine continuation or completion. Their domains and consumers must remain separate.

The inspected memory route retains candidate facts and preferences and later exposes a load-time snapshot to system-prompt assembly. It does not consume source evidence against a named factual acceptance criterion before saving. Review guidance requests generalizable rules with mechanisms, but source code alone does not establish that any actual rule is novel, entailed, criticized or accepted. For specific retained facts or skill explanations, truth-apt transformation remains indeterminate without the inputs and outputs. Lifecycle integration after epistemic acceptance is consequently unestablished in these selected routes, not absent throughout Hermes.

The exact recall deduper preserves one copy of repeated standalone bullets; continued bullets retain their provenance. The sanitizer can remove whole embedded context blocks, so preservation of all incoming claims cannot be inferred. Imported recalled content has unknown source warrant and is supplied under an authoritative-reference instruction. The next inference request receives the shaped content, not necessarily the provider's original payload. Selection timing is provider-specific: RetainDB consumes cached results from earlier queued queries and an agent-model fetch, without using the current prefetch query; ByteRover queries at prefetch time. Current-request targeting cannot be inferred for every recalled block. Delivery is wired; compliance and benefit are unobserved.

Goal mode supplies a countercase to an overly broad claim that Hermes merely saves content without consequential evaluation. A shell gate yields a pass proposition entailed by the checked return code in that execution-status domain. Success does not establish adequate tests, truthful source premises or mechanism correctness. An auxiliary model then judges bounded task-completion evidence, and the manager records completion or changes continuation. This is evidence-consuming acceptance of a completion decision for stopping the current goal, not acceptance of every generated claim for future reuse. Failed gates feed output into repair prompts; blocked judgments pause; wait judgments park. These paths provide direct behavioral control without requiring truth-apt policy production.

Numerical state remains provider-owned and uninspected as specified by [RT-CMP-inference-model](runtime.md#rt-cmp-inference-model). Retained text updates can coexist with fixed or changing weights; neither is established here. Learning, reflection, autonomous theory building and self-improvement must not be bundled. The public learning claim has implemented review/write/read channels, but improved future capacity lacks comparison evidence. Exercised self-improvement lacks traced subsequent behavior causally dependent on a retained change; source requests for improvement do not close that link. A formulated-theory assessment cannot be made for unavailable user skills merely because prompts ask for a WHY clause. Goal continuation establishes bounded automation, not autonomy of every internal theory-building operation. Uninspected curator, learning graph, loop, scheduler and evaluation operations prevent broader positive or negative conclusions.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-memory-entries
Label: Memory entries

Identity: entries of MEMORY.md and USER.md loaded by MemoryStore. Form: natural-language fact candidates, user descriptions and preferences; delimiter and target keys are symbolic packaging. Substrate: profile-scoped text files, mutable in-process entry lists and a frozen system-prompt snapshot. Candidate truth-apt content includes claims about environment paths/tool behavior and user characteristics; directives/preferences need not assert a proposition. SRC-1 `tools/memory_tool_store.py` supplies implementation evidence. Closest supplied object is [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages); these are separate files, not its transcript envelope.

> ENTRY_DELIMITER = "\n§\n"
> --- `tools/memory_tool_store.py`

> return self._system_prompt_snapshot.get(target, "") or None
> --- `tools/memory_tool_store.py:618-621`

#### EPI-OBJ-skill-content
Label: Skill content

Identity: selected SKILL.md and supporting files consumed by skill_view and changed by skill_manage. Form: natural-language procedural guidance and potential explanatory/factual assertions; embedded scripts can have separate symbolic executors not assessed as prose truth. Substrate: skill-tree files and tool-result content. Claimed role is reusable task procedure, not historical incident narration. SRC-1 `tools/skills_tool.py`, `agent/background_review.py`; implementation and prompt doctrine/design respectively. Distinct from [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call), which names the call rather than its returned guidance.

> "What a skill IS: the instructions for doing a class of task the most efficient and correct "
> "way, to THIS user's specifications — the procedure, the tools and commands that work, the "
> "order, the user's preferences for how the result should look, and the pitfalls that cost time. "
> --- `agent/background_review.py`

#### EPI-OBJ-recalled-context
Label: Recalled context

Identity: raw external prefetch text, shaped recalled block and user-message API-content sidecar. Form: natural-language claims under an instruction wrapper; symbolic sidecar keys and tags control projection. Substrate: provider-return strings, process messages and optional persisted sidecars. Part of the material reaching [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages), but raw provider text also exists before insertion, so it is not exclusively a part of that container. Content source and initial warrant remain provider-dependent. SRC-1 `agent/memory_manager.py`, `agent/turn_context.py`, implementation evidence.

> fenced = build_memory_context_block(ext_prefetch_cache) if ext_prefetch_cache else ""
> --- `agent/turn_context.py`

#### EPI-OBJ-summary-content
Label: Summary content

Part of: [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages)

Identity: compressed-history summary inserted or merged into the surviving message sequence. Form: natural-language historical assertions with symbolic summary metadata. Substrate: compressor state and assembled messages; full durable archive behavior uninspected. SRC-1 `agent/context_compressor.py`, implementation. Candidate truth is scoped to what occurred or was requested in the selected history, not the correctness of the historical statements themselves.

> "role": summary_role, "content": summary + "\n\n" + _SUMMARY_END_MARKER,
> COMPRESSED_SUMMARY_METADATA_KEY: True,
> --- `agent/context_compressor.py`

#### EPI-OBJ-goal-verdict
Label: Goal verdict

Identity: gate return tuples, stored gate exit/output fields and model done/blocked/continue/wait judgments. Split consumers are described by the goal records. Form: symbolic verdict and control state; natural-language reason and bounded output/response evidence. Substrate: process results, GoalState and session metadata persistence through manager save. Candidate propositions are gate-command success in the selected workspace and task completion against the goal/contract. Closest supplied route [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn) does not identify these optional post-turn decision objects. SRC-1 `hermes_cli/goals.py`, implementation.

> state.last_verdict = verdict
> state.last_reason = reason
> --- `hermes_cli/goals.py`

### Routes

#### EPI-RTE-review-candidate
Label: Review candidate generation

Distinct downstream operation from [RT-RTE-review-handoff](runtime.md#rt-rte-review-handoff), which only schedules the fork. SRC-1 `agent/background_review.py` provides implemented prompt construction and doctrine/design for the requested semantic behavior. Owner: review runtime/model; context: completed conversation and selected memory/skill guidance. Endpoints: snapshot → review prompt → proposed memory/skill calls. The model proposes and selects worth-saving content; code/store gates can veto changes. Open heuristic review, with no expected factual answer supplied. User authorship of each candidate is not established. Guidance separates user facts from environmental facts, asks for procedural rules and a mechanism, and permits saving nothing. Intended retention is the file content, not proof of its truth. Content relation remains indeterminate without an actual candidate and its premises. Claim: [RT-CLM-product-work](runtime.md#rt-clm-product-work).

- Immediate return: requested tool proposals or nothing-to-save response; no observed output supplied.
- Later read-back: uninspected — complete fork route and retained instance not supplied; downstream stores are separately assessed.
- Delegated visibility: completed-turn snapshot is handed off per the supplied runtime record, not evidence of complete user-state access.
- Selection predicate: review interval/tool availability at handoff, then model interpretation of worth-saving guidance.
- Invalidation or expiry: uninspected — full fork cancellation and iteration completion were not traced.
- Activation or effect: implemented request for candidate generation, not observed rule production or later compliance.
- Evidence limits: prompt guidance does not establish novelty, criticism, acceptance or improvement; no individual theory is supplied for conditions 1–4.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "If something stands out, save it once, in the right store, using the memory tool with the "
> "matching target. If nothing is worth saving, just say 'Nothing to save.' and stop."
> --- `agent/background_review.py`

> "  • A pitfall is a generalizable rule + one clause of WHY (the mechanism), imperative. 'Grep the "
> "test tree for the SYMBOL before widening a helper signature — hand-rolled mocks reimplement the "
> "old shape and fail on a shard you did not run.' Not a narrative of what happened this session.\n"
> --- `agent/background_review.py`

#### EPI-RTE-memory-scan
Label: Memory threat scan

Material safety-check part of [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch), but also reached at disk load outside a tool round; not exclusively contained by that route. Owner: MemoryStore. Endpoints: candidate entry → strict threat-pattern check → error or mutation eligibility; disk entry → scan → safe snapshot or blocked placeholder. Target/domain: injection/exfiltration pattern membership, not factual correctness. The program evaluates; no factual answer oracle or per-entry human judgment is established. Write-time rejection prevents saving that candidate through covered operations; load-time disposition removes its text from the snapshot while retaining raw entries for removal. These checking and disposition functions must not be confused with deleting false knowledge. SRC-1 `tools/memory_tool_store.py`, implementation.

- Immediate return: scan error on rejected write, or sanitized load-time snapshot.
- Later read-back: load-time snapshot is exposed by format_for_system_prompt; raw poisoned entry remains stored until explicitly removed.
- Delegated visibility: inapplicable — scanner itself has no child delivery operation.
- Selection predicate: nonempty content, strict pattern scope; add and patched content are checked, disk entries except already-blocked placeholders are checked.
- Invalidation or expiry: candidate rejection does not alter the file; load quarantine is snapshot-local and later loading can reevaluate changed entries.
- Activation or effect: rejection and snapshot suppression are wired; no observed threat detection or false-positive rate supplied.
- Evidence limits: detection establishes pattern match only; does not warrant source truth or comprehensive attack exclusion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return _first_threat_message(content, scope="strict")
> --- `tools/memory_tool_store.py`

> if scan_error := _scan_memory_content(content):
>     return _error(scan_error, "scan_blocked")
> --- `tools/memory_tool_store.py:369-375`

> """Load MEMORY.md / USER.md and capture the frozen system-prompt snapshot.
> Threat hits are replaced by a ``[BLOCKED: …]`` placeholder in the SNAPSHOT only;
> live lists keep the raw text so the user can see and remove poisoned entries
> (dropping them silently would hide the attack)."""
> --- `tools/memory_tool_store.py`

#### EPI-RTE-memory-gate
Label: Memory write gate

Distinct per-content write admission behind [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch); unattended-review path additionally serves the supplied handoff. Owner: memory tool and write-approval module. Endpoints: model-proposed add/patch/remove → argument validation → unattended-delete gate → optional configured gate → store call or staged/blocked response. Computational checks and configured approval permit or veto physical mutation, not factual acceptance. The optional gate is documented off by default and fails open if its module cannot load. Unattended review patch/remove, including batches, instead stages and fails closed on staging failure; add remains available. Staging pins the matched entry, preventing approval from silently retargeting a later matching entry. Full pending approval/replay is uninspected, so no epistemic human criterion is inferred. SRC-1 `tools/memory_tool.py`, implementation.

- Immediate return: rejected, staged-with-pending-ID or applied result.
- Later read-back: pending proposals can be surfaced through /memory pending; replay implementation is uninspected.
- Delegated visibility: unattended-review provenance changes the admissible actions; it is not equivalent to foreground admission.
- Selection predicate: action/target/arguments, unattended-review provenance and configured gate decision.
- Invalidation or expiry: matched-entry pinning and validation; full expiry/revocation handling uninspected.
- Activation or effect: controls whether the covered store mutation is reached; no factual warrant granted by mere permission.
- Evidence limits: direct file writes and external writers are alternate paths; shipped learning-node UI edits/deletes invoke MemoryStore._mutate directly rather than this tool gate. Their complete caller authorization and prompt refresh remain untraced, preventing a complete admission-control inventory or UI/tool equivalence. A configured human prompt does not prove a human reviewed truth.

Bounded alternate-path evidence: SRC-1 `agent/learning_mutations.py`, `hermes_cli/web_routers/status.py`, implementation. This limits the gate's coverage; it does not establish factual acceptance or unsafe deployment.

> result = load_on_disk_store()._mutate(_STORE_TARGETS[source], _apply)
> if not result.get("success"):
>     return {"ok": False, "message": result.get("error", f"{name} write failed")}
> return {"ok": True, "message": message}
> --- `agent/learning_mutations.py`
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Approval gate: stages (background/gateway) or prompts inline (CLI); off by default.
> gate_result = _apply_write_gate(store, "batch", target, None, None, operations)
> if gate_result is not None:
>     return "rejected", gate_result
> --- `tools/memory_tool.py`

> try:
>     from tools import write_approval as wa
> except Exception:
>     return None
> --- `tools/memory_tool.py:84-91`

> """Fail-closed operation gate for unattended background-review forks (#105921): ``add``
> stays available (it is all any review prompt asks for), while ``patch``/``remove`` —
> single or inside a batch — are never applied unattended.
> --- `tools/memory_tool.py`

#### EPI-RTE-memory-retain
Label: Memory file retention

Distinct file-retention endpoint from the transcript persistence in [RT-OBJ-session-messages](runtime.md#rt-obj-session-messages). Owner: MemoryStore. Endpoints: admitted mutation → locked reread/parse → dedupe and budget/drift conditions → file rewrite → success; later load → frozen prompt snapshot. Target is file consistency and bounded content size. Physical mutation is permitted by software conditions, not an evidence-consuming truth criterion. Input could be imported fact, paraphrase, conjecture or non-truth-apt preference; saving itself performs no new semantic acceptance. Readback is model-input authority, advisory through language, across later loads/sessions. Claim: [RT-CLM-product-work](runtime.md#rt-clm-product-work). SRC-1 `tools/memory_tool_store.py`, implementation. Raw disk modifications can exceed budget; load warns and does not truncate, a countercase to an unconditional size guarantee.

- Immediate return: saved entry/result, duplicate no-op or budget/read/drift error.
- Later read-back: load_from_disk captures the snapshot returned by format_for_system_prompt; current snapshot is not automatically replaced by each mutation.
- Delegated visibility: inapplicable — store mutation itself has no child-context transport.
- Selection predicate: enabled target and admitted action; duplicate/budget/read checks and mutation-specific drift handling.
- Invalidation or expiry: explicit patch/remove; external drift can block destructive rewrite; full recovery UI uninspected.
- Activation or effect: candidate text becomes retained file content; later prompt access is wired, behavioral activation unobserved.
- Evidence limits: retained candidate is not accepted knowledge; no actual entries, provenance or later-use trace supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._write_file(path, result[0])
> extra_fields = result[2] if len(result) > 2 else {}
> return self._success_response(target, result[1], **extra_fields)
> --- `tools/memory_tool_store.py`

> logger.warning("%s exceeds its char limit on load: %d/%d chars. Entries stay loaded; "
>                "further additions are blocked until it is back under the limit.",
>                path.name, count, limit)
> --- `tools/memory_tool_store.py`

#### EPI-RTE-recall-reshape
Label: Recall text reshaping

Distinct transformation of provider text before the model-input channel in [RT-BAP-task-prompt](runtime.md#rt-bap-task-prompt). Owner/evaluator: fixed code. Target/domain: repeated standalone bullets within a section. Endpoints: raw recall → sanitizer → deduper → wrapper. Dedupe is non-ampliative reshaping: for input `- uses uv\n- uses uv`, first bullet enters seen, second identical standalone bullet is skipped, and output contains one copy. With `- uses uv\n  (source A)\n- uses uv\n  (source B)`, both carry continuations, neither enters seen and both remain. This is an implementation deduction, not target execution. Sanitization is separate: `<memory-context>claim</memory-context>` is removed wholesale by the inspected regex, so overall payload preservation is not guaranteed. No check of claim truth occurs. SRC-1 `agent/memory_manager.py`, implementation.

- Immediate return: shaped recalled-context string.
- Later read-back: shaped block is stamped into API sidecar and replayed through the separate consumption route.
- Delegated visibility: inapplicable — transformation itself has no child delivery.
- Selection predicate: same-section exact stripped bullet equality, with no following indented continuation; sanitation matches fence/context-note patterns.
- Invalidation or expiry: seen set resets at column-zero non-bullet content; each call recomputes shaping.
- Activation or effect: duplicate reduction and wrapper construction are wired, not evidence of better decisions.
- Evidence limits: no source truth, endorsement or semantic paraphrase matching; sanitizer may discard content before dedupe.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not carries_continuation:
>     if stripped in seen:
>         continue
>     seen.add(stripped)
> --- `agent/memory_manager.py`

> _INTERNAL_CONTEXT_RE = re.compile(r'<\s*memory-context\s*>[\s\S]*?</\s*memory-context\s*>', re.IGNORECASE)
> --- `agent/memory_manager.py`

#### EPI-RTE-recall-consume
Label: Recall authority consumption

Material recalled-content part of the broader [RT-BAP-task-prompt](runtime.md#rt-bap-task-prompt), not a duplicate general prompt route. Owner: turn-context assembly; consumer: configured inference model. Endpoints: provider-return content → shaped wrapper → current user API sidecar → provider request; historical rows replay recorded bytes. Acquisition/import, with source warrant unknown: the inspected projection supplies no truth check or original evidence. Operational force is advisory natural-language authority, not guaranteed compliance; horizon is current request and later requests while the historical sidecar survives. Claim and mismatch: [EPI-CLM-reference-data](#epi-clm-reference-data) asks for authoritative reliance without a factual acceptance decision in these inspected functions. Opaque upstream providers may supply additional warrant; none is assumed. SRC-1 `agent/turn_context.py`, `agent/memory_manager.py`, `plugins/memory/retaindb/__init__.py`, `plugins/memory/byterover/__init__.py`, implementation. The supplied [MEM-RTE-provider-cycle](memory.md#mem-rte-provider-cycle) overlaps in provider recall and distinguishes cached RetainDB selection from ByteRover query-time selection; this record retains its narrower wrapper/projection identity.

- Immediate return: outgoing request content includes the shaped block.
- Later read-back: historical user/assistant API-content sidecars replay the bytes sent live; persistence and complete resume coverage uninspected.
- Delegated visibility: uninspected — per-child provider configuration/skip behavior cannot be inferred from the foreground route.
- Selection predicate: provider-specific prefetch, nonempty context, current versus historical row and available sidecar. RetainDB consumes and clears cached context/user-synthesis/agent-model results from earlier queued background jobs; its current prefetch query argument does not select those results. ByteRover calls _query with the prefetch-time query, stripped and capped to 5000 characters. Historical sidecars replay recorded bytes rather than reselecting from a current query.
- Invalidation or expiry: stale API-content drop helper exists; complete rewrite/compaction callers uninspected.
- Activation or effect: model-input delivery is wired; model interpretation, compliance and improved answers are unobserved.
- Evidence limits: no individual recalled fact or source endorsement supplied; authoritative wording is not a correctness certificate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> def prefetch(self, query: str, *, session_id: str = "") -> str:
>     """Consume prefetched results and return them as a context block."""
>     with self._lock:
>         context, dialectic, agent_model = self._context_result, self._dialectic_result, self._agent_model
>         self._context_result, self._dialectic_result, self._agent_model = "", "", {}
> --- `plugins/memory/retaindb/__init__.py`

> ("retaindb-ctx", "context", "_context_result", lambda: self._context_overlay(query)["context"]),
> --- `plugins/memory/retaindb/__init__.py`

> result = self._query(query)
> output = (result.get("output") or "").strip() if result["success"] else ""
> --- `plugins/memory/byterover/__init__.py`

> # Historical row: replay the exact bytes sent live so the prompt-cache
> # prefix stays byte-stable. User rows carry the injection sidecar; user
> # and assistant rows may carry a sanitize-divergence sidecar.
> api_msg["content"] = _api_content
> --- `agent/turn_context.py`

#### EPI-RTE-summary-check
Label: Summary provenance check

Specific transformation/check/disposition inside working-context control described by [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn), not another whole-turn record. Owner: compressor code and configured summary model. Endpoints: selected/bounded history → model summary → redaction/marker restoration/task grounding → provenance check → previous-summary state and assembled summary-bearing messages; failure → summary failure handler. The model proposes semantic compression; relation is indeterminate without concrete source/output comparison. Code checks the narrow target of user attribution when there is no real user turn. It requires the no-user sentinel and rejects a `User asked:` attribution; has_user_turn skips this check. Passing is operational admission to compression state, not warrant for all statements. Summary assembly supplies natural-language history to later model calls, advisory, within later invocations. SRC-1 `agent/context_compressor.py`, implementation.

- Immediate return: prefixed summary or failure-handler result; assembled message list contains or merges the summary.
- Later read-back: previous summary shapes iterative summary calls and assembled messages can enter later inference; full durable archive/reload route uninspected.
- Delegated visibility: selected/bounded history reaches auxiliary summarization, not automatically all original turns.
- Selection predicate: compression eligibility, cooldown, bounded input selection and real-user-turn determination.
- Invalidation or expiry: cancellation/stale-attempt checks prevent late publication; provenance error enters failure handling, whose complete fallback route remains uninspected.
- Activation or effect: summary replacement/use is wired; semantic fidelity, successful recovery and model compliance unobserved.
- Evidence limits: a transcript with any real user turn passes the narrow guard regardless of other factual inaccuracies; no general truth oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._validate_summary_user_provenance(summary, has_user_turn)
> --- `agent/context_compressor.py`

> if has_user_turn:
>     return
> --- `agent/context_compressor.py:4360-4364`

> if task_snapshot != _NO_USER_TASK_SENTINEL or re.search(r"\bUser\s+asked\s*:", summary, re.IGNORECASE):
>     raise RuntimeError(
>         "Context compression summary invented user attribution for a session with no user-authored turns",
>     )
> --- `agent/context_compressor.py`

#### EPI-RTE-skill-guard
Label: Skill guarded mutation

Specific skill-content admission and withdrawal mechanism, distinct from the generic tool dispatch and [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) of executable handlers. Owner: skill manager, provenance guards and loader. Model proposes changes under review guidance; code can veto. Existing-target writes in background review require a fresh read mark; autonomous deletion is separately restricted by pinned/external/bundled/hub/curator-managed provenance. Read marks establish exposure, not that the revision fits the evidence. Guarded writes atomically write then optionally scan; scan rejection restores original or unlinks new target. Agent-created security scanning defaults off and scan exceptions log but permit the write. Targets/domains: fresh-read provenance, deletion ownership and threat patterns, not procedural success or explanatory truth. Project-tier dangerous skills are separately quarantined by loader, even explicit-name requests; loaded skills return rendered content, with preprocessing semantics not fully inspected. SRC-1 `tools/skill_manager_tool.py`, `tools/skill_manager_guards.py`, `tools/skills_tool.py`, `tools/skills_guard.py`, implementation. Stored procedure guidance has advisory model-input force on later skill_view calls; script effects remain a separate executor boundary.

- Immediate return: mutation/load error or saved/loaded result; opt-in scan failure rolls back the covered target write.
- Later read-back: skill_view selects files and returns rendered content; exact preprocessor transformations and complete archive restore route uninspected.
- Delegated visibility: fresh-read requirement is specific to background-review provenance; other contexts differ.
- Selection predicate: target existence, review read mark, ownership/protection flags, optional scan configuration and project quarantine.
- Invalidation or expiry: failed guarded-write scan restores/unlinks; dangerous project skill remains unavailable pending changed content/re-scan; delete archival and later restoration only partially inspected.
- Activation or effect: operational write/load/delete permission changes are wired; factual endorsement and later behavior changes unobserved.
- Evidence limits: no outcome/reference test of a candidate procedure here; direct terminal writes are a counterroute, and opt-in scan exceptions fail open.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not _guard_agent_created_enabled():
>     return None
> --- `tools/skill_manager_tool.py`

> except Exception as e:
>     logger.warning("Security scan failed for %s: %s", skill_dir, e, exc_info=True)
> return None
> --- `tools/skill_manager_tool.py:50-64`

> if original is not None:
>     atomic_write_text(target, original, preserve_mode=True)
> else:
>     target.unlink(missing_ok=True)
> return _err(scan_error)
> --- `tools/skill_manager_tool.py`

> if not _is_background_review() or _background_review_has_read(target):
>     return None
> --- `tools/skill_manager_guards.py`

#### EPI-RTE-goal-check
Label: Goal completion check

New optional-mode evaluator not identical to [RT-RTE-oneshot-turn](runtime.md#rt-rte-oneshot-turn). Owner: GoalManager, shell backend and auxiliary judge model. Endpoints: active goal/contract and last response → configured gates → pass/exit/output → if all pass, bounded judge prompt → parsed verdict/reason. Two distinct check targets: shell command exit success in configured workspace; goal completion as evidenced by truncated last response, goal/contract/subgoals and background/delegation metadata. Gate reference is exit zero, with command author/adequacy unresolved. Completion model has no independently supplied expected factual answer; goal text is the criterion, not ground truth. The gate pass proposition is an entailed derivation from proc.returncode under the inspected equality rule. Model judgment is indeterminate as a semantic transformation; it is not entitled to the gate's deterministic license. Program gates veto judge invocation on failure; humans can configure/remove gates and pause/rescope; the model proposes the completion verdict. Operating mode: goal pursuit with bounded turns/retries, not a controlled component experiment. SRC-1 `hermes_cli/goals.py`, implementation.

- Immediate return: gate pass/exit/output tuple or parsed done/blocked/continue/wait judgment, with parse/transport flags.
- Later read-back: exit/output and last verdict/reason enter GoalState used by later manager boundaries.
- Delegated visibility: judge receives active delegation count and selected running-process metadata, not full child histories.
- Selection predicate: active nonparked goal; gates run first; goal, response and contract/subgoal text are bounded before judging.
- Invalidation or expiry: gate timeouts become failure; failed gates reexecute on eligible boundaries; judge errors/parse failures feed continuation/backstop handling.
- Activation or effect: evidence results reach the disposition route; no target run or completion accuracy demonstrated.
- Evidence limits: shell success licenses only the executed command's return status; truncation and response self-report limit completion judgment; no causal benefit measured.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return proc.returncode == 0, proc.returncode, combined[-_GATE_OUTPUT_TAIL_CHARS:]
> --- `hermes_cli/goals.py`

> goal=_truncate(goal, 2000),
> response=_truncate(last_response, _JUDGE_RESPONSE_SNIPPET_CHARS),
> --- `hermes_cli/goals.py`

> gate_decision = self._check_gates()
> if gate_decision is not None:
>     if gate_decision.get("should_continue") and state.turns_used >= state.max_turns:
>         return self._budget_pause(state, "gate_failed", gate_decision.get("reason", ""), note=" (a quality gate is still failing)")
>     return gate_decision
> --- `hermes_cli/goals.py`

#### EPI-RTE-goal-disposition
Label: Goal result disposition

Distinct consumer of [EPI-RTE-goal-check](#epi-rte-goal-check), with no counterpart among supplied whole-turn records. Owner: GoalManager plus CLI/gateway queues. Endpoints: check results → manager state/continuation decision → saved status and queued synthetic user prompt or parked/paused/done outcome. Acceptance criterion: configured gates pass, then parsed completion judgment against current goal/contract. Intended use/scope: stopping this session's goal pursuit, not certifying every work-product assertion. Gate failure output forms the repair prompt, subject to retry/turn caps. Blocked pauses for rescope/override; done saves and suppresses continuation; wait parks; continue can enqueue another request. Code decides actual continuation and enforces budgets; model supplies verdict; user may pause, resume, rescope or remove gates. No independent truth oracle added by disposition. This is evidence-responsive control-state adaptation, not automatically retained theory revision. SRC-1 `hermes_cli/goals.py`, `hermes_cli/cli_loops_mixin.py`, `gateway/run_goals.py`, implementation.

- Immediate return: decision dictionary with status, should_continue, continuation_prompt, verdict and reason; caller displays/enqueues as applicable.
- Later read-back: GoalState saves last verdict, reason and status for later session boundaries; repair prompt reaches a subsequent model turn.
- Delegated visibility: count/process facts affect wait decision; no automatic delivery of all judge evidence to children.
- Selection predicate: manager consumes gate failure or judge verdict; queue requires should_continue and nonempty prompt, with gateway source/adapter prerequisites.
- Invalidation or expiry: retry/turn exhaustion pauses, user override can resume/rescope; done stops goal continuation rather than rolling back effects already performed.
- Activation or effect: enqueuing a new model-input event or suppressing continuation is wired; executed repair/benefit unobserved.
- Evidence limits: stopping is acceptance of bounded completion evidence, not causal validation of the producing process or future procedural transfer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if verdict == "done":
>     state.status = "done"
>     self._save()
>     return _decision("done", False, None, "done", reason, f"✓ Goal achieved: {reason}")
> --- `hermes_cli/goals.py`

> if decision.get("should_continue"):
>     prompt = decision.get("continuation_prompt")
>     if prompt:
>         try:
>             self._pending_input.put(prompt)
>         except Exception as exc:
>             logging.debug("goal continuation enqueue failed: %s", exc)
> --- `hermes_cli/cli_loops_mixin.py`

> self._enqueue_fifo(_quick_key, self._synthetic_prompt_event(source, prompt), adapter)
> --- `gateway/run_goals.py`

### Claims

#### EPI-CLM-reference-data
Label: Authoritative reference data

Distinct narrow recalled-content warrant instruction from the broad [RT-CLM-product-work](runtime.md#rt-clm-product-work). Claimed role: recalled memory should inform all responses as authoritative reference data. SRC-1 `agent/memory_manager.py`, doctrine/design embedded in implemented wrapper. Wiring proves delivery of the instruction, not truth, endorsement or compliance. The shaping/projection functions provide no evidence-consuming factual acceptance criterion; upstream provider warrant remains unknown.

> "[System note: The following is recalled memory context, "
> "NOT new user input. Treat as authoritative reference data — "
> "this is the agent's persistent memory and should inform all responses.]\n\n"
> --- `agent/memory_manager.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
