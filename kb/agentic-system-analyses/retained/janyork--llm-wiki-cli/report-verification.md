---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of llm-wiki-cli's persistence, context, admission and learning routes at the frozen Git revision."
run-id: AAS-2026-11-08-llm-wiki-cli-135ef8fbe608-01
reviewed-boundary: e1be6ab30e83947e4b0dba97ba910acfe3bd9821
---

# llm-wiki-cli report verification

## Verification

### Boundary, checks and disposition

The five reviewed members support a bounded account of agent-operated persistence, mechanical admission and later consumption. No material correction is required. One local inventory limit is retained below.

I read every supplied report, its declarations and annotations, the reconciliation, all four empty correction-answer files and the structural report. The structural report says `none`; there is no structural failure to route. No previous semantic refusal was supplied. I assessed record referents, evidence meanings, source anchors, separate implementation/operation statuses, the annotations' scope, containment and both supersessions. This is semantic verification, not a rerun of code's quotation-occurrence and reference-resolution checks.

The checkout HEAD equals the reviewed revision. The top-level tracked tree agrees with the [boundary coverage](boundary.md#top-level-coverage). Its memory-system classification includes the shipped callers, instructions, optional learning stores and readers; it does not incorrectly attribute the external host's inference to LWC. All direct inspection was source text under SRC-1 at that revision. No target, test, host, benchmark or optional runtime was executed. Provider internals, actual release bytes and deployed services remain outside the evidence. No evidence contradicts the frozen target or boundary kind.

### Runtime and Wiki workflow

I independently followed CLI page dispatch into Store replacement and later show, then compared it with [RT-RTE-page-write](runtime.md#rt-rte-page-write). SRC-1, `src/cli/dispatch.rs`, `src/store/content_search.rs`: citation/provenance sets are deleted and reinserted from caller input; the immediate transaction compares the prepared base, commits canonical content, and only afterwards reconciles graph projection. The report correctly distinguishes structural admission, semantic authorship, later availability and ambiguous postcommit errors. Immutable source insertion and guarded page/source deletion support the separate identities and bounded withdrawal findings in [MEM-OBJ-sources](memory.md#mem-obj-sources), [MEM-OBJ-pages](memory.md#mem-obj-pages), [MEM-RTE-source-admit](memory.md#mem-rte-source-admit) and [MEM-RTE-content-withdraw](memory.md#mem-rte-content-withdraw). SRC-1, `src/store/changeset_merge.rs`, `src/store/content_search.rs`.

For [RT-RTE-changeset-commit](runtime.md#rt-rte-changeset-commit), I inspected the already-committed return, fresh-publication branch, conflict/integrity/lint checks and postpublication queue failure. SRC-1, `src/changeset.rs`. The early receipt is recovery of an existing commit, not a demonstrated first-publication bypass. The supported selector-free CLI write and MCP core route independently establish that draft lint is not universal. The reports preserve that distinction rather than inferring safety from the guarded branch alone.

The source job's claim/next, analyze, fail/retry and completion transitions agree with [WF-RTE-ingest-preparation](workflow.md#wf-rte-ingest-preparation) and [RT-RTE-ingest-complete](runtime.md#rt-rte-ingest-complete). SRC-1, `src/store/graph_ingest.rs`, `src/store/materialize.rs`: next selects ascending source ID; packets include purpose/schema and bounded context; completion counts cited page kinds and permits the stated no-derived-pages exception. Nothing in that consumer checks exhaustive reading or semantic fidelity. The [workflow account](workflow.md#workflow-account) is a coherent shipped procedure, not a manufactured sequence of capabilities. Its live validation and delivery conditions follow the active-memory instructions, while its implementation claims remain narrower.

I checked the structural lint predicate against [EPI-RTE-lint-check](epistemic.md#epi-rte-lint-check) and the instructed review against [EPI-RTE-milestone-review](epistemic.md#epi-rte-milestone-review). SRC-1, `src/store/types.rs`, `src/store/materialize.rs`, `skills/using-lwc/references/active-memory.md`. Explicit provenance defeats the particular uncited-page predicate, not every lint rule. Fixed retrieval/source checks are host policy, not independently observed semantic acceptance. This preserves [RT-CLM-agent-memory](runtime.md#rt-clm-agent-memory) as doctrine rather than measured compounding benefit.

[RT-RTE-work-runner](runtime.md#rt-rte-work-runner) correctly separates queued receipt, persisted terminal result and recovery bookkeeping. I traced active-kind coalescing, spawn failure, request/root correspondence, fixed-kind execution and terminal-state writing in SRC-1, `src/work/runner.rs`. No reliability or crash-recovery success is inferred from that wiring.

### Context, memory and authority

For [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) and [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), I followed selection through the delivered payload rather than relying on producer labels. SRC-1, `src/agent.rs`, `src/store/tags.rs`, `src/mcp.rs`, `integrations/pi-lwc/extensions/lwc.js`. Enabled policies, membership order, duplicate handling, whole-page omissions and final rendering budget constrain hooks; MCP code-only mode returns before memory retrieval, and memory mode truncates selected page bodies with flags. Pi clears/consumes pending context and appends the result to the system prompt. These support bounded supply, not universal delivery or safe model interpretation. [MEM-OBJ-tags](memory.md#mem-obj-tags), [MEM-OBJ-purpose-schema](memory.md#mem-obj-purpose-schema) and [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) keep selector metadata, domain guidance and model-mediated reference authority distinct.

[RT-RTE-core-command](runtime.md#rt-rte-core-command) is a separate mutation surface: the inspected allowlist, prohibited selector flags, subprocess construction and timeout/error paths support the report. SRC-1, `src/mcp.rs`. Read-only explore does not make the MCP server read-only, and an interrupted response need not undo a completed write.

I checked both persistent retrieval-state producers and their numeric search consumer for [MEM-OBJ-retrieval-state](memory.md#mem-obj-retrieval-state) and [MEM-RTE-retrieval-adjust](memory.md#mem-rte-retrieval-adjust). SRC-1, `src/store/graph_ingest.rs`, `src/store/graph_search.rs`: effective provenance precedence and exact token fingerprint determine adjustments. Retained reasons do not become semantic evaluators.

Temporal admission, recall arithmetic, relation-based visibility/conflict flags, feedback and retention agree with [MEM-RTE-temporal-cycle](memory.md#mem-rte-temporal-cycle) and [EPI-RTE-temporal-feedback](epistemic.md#epi-rte-temporal-feedback). SRC-1, `src/store/temporal_memory.rs`. Replica retention takes a distinct preserve/reject branch. The event/control objects and the epistemic event grouping correctly distinguish prose, symbolic relations, feedback and access metadata; `latest_known` is not live verification. The arithmetic example is a valid code deduction, not an observed run.

For [MEM-RTE-discussion-revise](memory.md#mem-rte-discussion-revise) and [MEM-RTE-discussion-capture](memory.md#mem-rte-discussion-capture), I checked dependency invalidation and raw-reply capture/replay. SRC-1, `src/store/discussion.rs`, `src/agent.rs`. Capture precedes the prompt's 4096-character intent truncation and requires the stated exact raw form/message/context conditions. It is not a universal transcript collector. Derived summaries and caller confirmation remain separate from raw capture and authorization, as [MEM-BAP-discussion-summary](memory.md#mem-bap-discussion-summary) states.

The Plan/Todo objects and [MEM-RTE-task-continuity](memory.md#mem-rte-task-continuity) retain a deliberately partial Store assessment. The inspected context-qualified readiness consumer removes/replaces aggregate task fields and caps reminders; it does not establish universal isolation across all readiness/host paths. SRC-1, `src/agent.rs`, `src/cli/dispatch.rs`. The derived-index object likewise distinguishes canonical material from rebuildable retrieval/graph views and does not claim semantic equivalence or exhaustive graph coverage.

### Optional learning and transport

I traced Tutor begin/commit and both Soul publication families, including receipt replay, owner/revision checks, ordinary sensitivity and caller-supplied approval. SRC-1, `src/learning/tutor.rs`, `skills/using-tutor/SKILL.md`. [RT-RTE-tutor-turn](runtime.md#rt-rte-tutor-turn), [RT-RTE-soul-publish](runtime.md#rt-rte-soul-publish), their memory objects and [RT-BAP-soul-guidance](runtime.md#rt-bap-soul-guidance) correctly separate stored exact I/O, checkpoint state and durable guidance. Commit-before-display and cached Soul use are agent protocols; local owner/approval fields are not authenticated learner consent. The broader supplier statement about Soul does not override the narrower command-specific account.

Book's blob/report objects and [MEM-RTE-book-window](memory.md#mem-rte-book-window) are supported by the cursor, active lease, whole-block selection, report admission and ordered coverage consumer. I also inspected initial/correction synthesis admission for [MEM-RTE-book-synthesis](memory.md#mem-rte-book-synthesis). SRC-1, `src/learning/book.rs`. Existing active-lease recovery and replay return prior ranges rather than granting new coverage. The budget's token-labelled branch is character arithmetic, exactly as qualified; synthesis checks coverage, ranges and anomaly disposition, not comprehension.

Practice item verification, objective/subjective grades, overrides, ratings and later queue selection agree across the item/response/grade/card objects and [EPI-RTE-practice-verify](epistemic.md#epi-rte-practice-verify), [EPI-RTE-practice-grade](epistemic.md#epi-rte-practice-grade), [MEM-RTE-practice-assess](memory.md#mem-rte-practice-assess), [MEM-RTE-practice-review](memory.md#mem-rte-practice-review). SRC-1, `src/learning/practice.rs`. Source checks query identity/hash/revision; exact answer equality warrants only equality in that domain; subjective confidence changes accepted/pending state and mistake membership. Ratings derive durable cards/debt that queue code actually consumes under a budget. [MEM-BAP-review-schedule](memory.md#mem-bap-review-schedule) therefore has a positive symbolic behavioral path without establishing learning benefit. No route needs an invented internal model or independent semantic oracle.

For [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install), inspected configuration, fixed version/platform selection, archive checksum/layout validation and child forwarding support executable admission, not adaptive capability generation. SRC-1, `src/learning_runtime.rs`. For [RT-RTE-team-sync](runtime.md#rt-rte-team-sync), I checked conflict session/digest/claim matching, copy-before-resolution and the team push's receipt replay versus fresh publication guard. SRC-1, `src/replica/engine.rs`, `src/team/hub.rs`. The claim is explicitly restricted to that guarded push, not every recovery/administration path. [MEM-RTE-archive-admit](memory.md#mem-rte-archive-admit) correctly distinguishes missing-store import, identical state, staged differences and bound overwrite confirmation in SRC-1, `src/archive.rs`. Neither transport route establishes semantic preservation across every uninspected transformation.

### Relations, conflicts and omission stopping decision

The [reconciliation](reconciliation.md#reconciliation) preserves the reports' evidence strengths and local gaps. Its item-object and temporal-route supersessions identify the same referents without erasing epistemic findings. Event grouping versus separate content/control objects and grades versus response/grade containers are not whole-record aliases. Assessment and grading overlap, but override coverage differs. I checked the declarations for required `Part of:` relations against their supplied-record context; no unsupported containment relation or missing mandatory supplied-parent relation is established. No required operative part is silently treated as absent. No unresolved disagreement between reports needs a conflict paragraph: hook writes, Book budget and Soul wording are compatible additions or source-layer qualifications, not competing report conclusions.

Omission questions were selected from the frozen tree and producer/consumer dependencies: could direct mutation evade a claimed universal review gate; could lifecycle hooks write as well as read; could separate learning stores supply stronger checking or automatic retained adaptation than the ordinary Wiki account; and could a shipped evaluator exercise a different memory loop? The first three have supported dispositions above. The last led to direct inspection of SRC-1, `benchmarks/agent_memory/lwc_backend.py`, with the local inventory limit below. Inspection of `src/agent/targets/pi.rs` also confirms a shipped installation surface, not an excluded caller. No host-parity claim is inferred from it.

The evaluator's raw-source admission has a direct implementation witness:

> command = ["source", "add-manifest", str(manifest_path)]
> if acknowledge_sensitive_source:
>     command.append("--acknowledge-sensitive-source")
> self._run(root, command)
> --- `benchmarks/agent_memory/lwc_backend.py`

Further optional expansion stopped because the central claims remain route-specific and every identified challenge has a disposition. Private Sync, restore, other host adapters, rendering, graph/span internals and learner-update alternatives remain available but incompletely inspected, not evidenced absent. The reports already withhold exhaustive preservation, privacy, semantic quality, acceptance and adaptation conclusions; searching them merely to enlarge an inventory would not justify promoting or negating those conclusions. The epistemic ledger and bounded conclusion do not turn missing executions into absent architecture, or storage/selection into accepted ampliative knowledge. [RT-CMP-host-model](runtime.md#rt-cmp-host-model) retains provider uncertainty independently.

## Blockers

none

## Limits

- The memory route inventory does not separately characterize the benchmark adapter's automatic raw-message import and evidence read-back. This is a shipped evaluation caller, not hidden reasoning capture or the model-operated Wiki synthesis workflow. SRC-1, `benchmarks/agent_memory/lwc_backend.py`: `add_many` prepares supplied messages, writes source files and invokes source add-manifest; `search` requests source passages and then rereads full source content. The [boundary](boundary.md#boundary-and-evidence) already distinguishes this path, and [MEM-RTE-source-admit](memory.md#mem-rte-source-admit) supports its storage endpoint, but [memory coverage](memory.md#boundary-and-evidence) leaves evaluation details partial. Retain the positive Wiki, temporal and private-learning findings; withhold a complete inventory of trace origins, automatic raw-trace admission and evaluator-specific delivery. This does not establish exercised learning, useful synthesis or causal benefit.
