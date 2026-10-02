---
type: agentic-systems/types/agentic-system-analysis-overview.md
description: '`mem` turns imported events into Git-backed facts for later search and hook context, with source truth, host delivery, activation, and benefit unverified.'
run-id: AAS-2026-10-02-instinctual-memory-01
system: instinctual-memory
run-date: '2026-10-02'
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
analysis-cutoff: '2026-10-02'
evidence-tier: code-grounded
inputs-commit: a7d04e9bbf113dc448de19d07740cc90347b4961
---

# instinctual-memory agentic-system analysis

## Boundary and evidence

The target is `mem`, a portable Git-backed memory system for AI agents. The
whole-system boundary is the repository's CLI and library, including its
journal, fact consolidation and validation, search and reranking, MCP and HTTP
interfaces, setup hooks, writeback, and erasure mechanisms. This is a memory
system because it turns agent conversation and project-file inputs into
retained facts and exposes those facts to agent clients. The README describes
this intended flow and the implementation is organized around those functions
(`SRC-1`, `README.md`, `src/lib.rs`, `src/cli.rs`, `src/consolidate.rs`,
`src/search/mod.rs`, `src/mcp.rs`, `src/http_serve.rs`, `src/setup.rs`).

The boundary excludes Claude Code, Codex, OpenCode, other agent runtimes and
MCP clients; `mem` integrates with these hosts but does not own their prompt
assembly, model decisions, or session lifecycle. It also excludes actual user
stores, session records, and operation traces, which are not included in this
repository snapshot. Model-provider services and downloaded reranker models
are external dependencies, not part of the frozen implementation. The code
and documentation establish available mechanisms and declared behavior; they
do not establish that an operator installed them, that a host delivered
memory to a model, or that memory improved task outcomes (`SRC-1`, `README.md`,
`Cargo.toml`). Those operational and benefit conclusions are outside the
evidence reached here.

The target is in scope as a complete software system for the functions its
repository defines. Evidence is code-grounded: the reviewed commit contains
the CLI/library implementation and its accompanying design and usage
 documentation. This boundary does not claim observed operation.

## Source register

| Source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git repository | `https://github.com/jasonkneen/instinctual-memory`; access root `related-systems/jasonkneen--instinctual-memory/` | `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` | doctrine/design | README product description, command and integration descriptions, storage model, declared trust model; Cargo package metadata | `README.md`, `Cargo.toml` | No actual operator stores, host configuration, service calls, or operation traces are included; deployment, runtime delivery, and benefit are not established. |
| SRC-2 | Git repository | `https://github.com/jasonkneen/instinctual-memory`; access root `related-systems/jasonkneen--instinctual-memory/` | `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` | implementation | CLI and library entry points plus ingestion, journal, consolidation, search, MCP, HTTP, setup, and writeback implementation modules | `src/main.rs`, `src/lib.rs`, `src/cli.rs`, `src/ingest.rs`, `src/journal.rs`, `src/consolidate.rs`, `src/search/mod.rs`, `src/mcp.rs`, `src/http_serve.rs`, `src/setup.rs` | Source inspection establishes implemented paths and affordances only; without frozen host-side evidence or observed runs it cannot establish activation or model-visible delivery. |

Amended or superseded records: none; [reconciliation](reconciliation.md).

## Bounded synthesis

The reviewed repository implements a portable memory workflow: file or history inputs enter an append-only journal, bounded consolidation proposes source-linked facts, validated publication stores facts and controls in a Git tree, and callers can search or read them later ([OBJ-1](runtime.md#obj-1--append-only-source-journal), [OBJ-2](runtime.md#obj-2--published-memory-tree), [RTE-1](runtime.md#rte-1--file-backfill-to-journal), [RTE-2](runtime.md#rte-2--journal-consolidation-to-published-facts), [RTE-3](runtime.md#rte-3--search-and-rerank-to-caller)). This is implementation evidence for available mechanisms, not evidence that an operator deployed them ([ABS-1](runtime.md#abs-1--no-operation-traces-or-deployed-host-configuration-in-this-boundary)).

The journal preserves source events separately from curated facts. Consolidation processes events after a retained checkpoint in bounded batches; rules or an optional LLM propose facts, while code checks source excerpt occurrence, filters candidates, validates the candidate tree, and publishes it with a compare-and-swap. This publication gate protects writes through that repository path from stale-base overwrite; it does not check proposition truth or guarantee correctness ([RTE-2](runtime.md#rte-2--journal-consolidation-to-published-facts), [OBJ-2](runtime.md#obj-2--published-memory-tree), [RTE-2](epistemic.md)).

Recall has both pull and push paths. CLI, MCP, HTTP, and shell search return ranked facts and journal events to a caller; a separate Claude hook path selects preferences at session start and lexically matched facts for prompts, emitting them as advisory additional context. Setup and generated project-instruction writeback are separate routes. The code establishes these output paths, while host installation, delivery to a model, model reliance, and behavior change are not observed ([RTE-3](runtime.md#rte-3--search-and-rerank-to-caller), [MEM-RTE-6](memory.md#mem-rte-6--hook-selected-context-supply-and-session-sync), [EPI-RTE-1](epistemic.md#epi-rte-1--prompt-hook-fact-injection), [RTE-5](runtime.md#rte-5--generated-writeback-and-host-setup)).

The system also supports caller-authored remember, correction, forget, and erase operations. Retained controls can suppress, retract, delete, or redact material from later access or extraction. `mem tidy` can identify duplicate facts; an operator must apply the result for duplicate facts to be retracted and suppressed. These are maintenance and availability decisions, not truth judgments ([RTE-4](runtime.md#rte-4--explicit-change-and-erasure), [MEM-OBJ-2](memory.md#mem-obj-2--retained-access-and-control-state), [EPI-OBJ-1](epistemic.md#epi-obj-1--tidy-findings), [EPI-RTE-2](epistemic.md#epi-rte-2--tidy-classification-and-withdrawal)).

The strongest supported contribution is a wired path from prior session material through durable fact updates to later retrieval and hook context. That supports a memory-route classification of trace learning, but there is no observed comparison showing improved capacity or task outcomes. The held-out evaluation command can score retrieval against caller-supplied expected IDs and strings; no supplied rubric or run establishes claim truth or system improvement ([RTE-2](memory.md#rte-2), [MEM-RTE-6](memory.md#mem-rte-6--hook-selected-context-supply-and-session-sync), [EPI-RTE-3](epistemic.md#epi-rte-3--held-out-retrieval-evaluation), [CLM-1](epistemic.md)).

## Limitations

| limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| No operation traces, deployed stores, or host configuration were supplied. | `SRC-1`, `SRC-2`, `ABS-1`, `MEM-RTE-6`, `EPI-RTE-1` | Reviewed repository at `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`; host runtimes, stores, services, and traces excluded. | Whether ingestion or hooks ran in deployment, context reached a model, retrieved material changed behavior, or memory improved outcomes. | Frozen deployment configuration, actual stores, and inspectable operation traces tied to this revision. |
| Consolidation checks textual evidence occurrence and structural validity, not source truth or semantic entailment; the event-to-fact transformation remains indeterminate. | `OBJ-1`, `OBJ-2`, `RTE-2`, `EPI-RTE-2` | Inspected ingestion, extraction, validation, and publication code; no proposal/input execution pairs supplied. | Whether retained assertions are true, faithfully preserve source meaning, or have an independent warrant. | Reviewed input/proposal pairs with evidence of semantic relation and source reliability, plus an explicit truth criterion if one is claimed. |
| **Unresolved conflict:** `OBJ-3` and `RTE-5` show generated project instruction text derived from selected retained facts, but `memory-comparison.axes.lineage` lists only authored, imported, and trace-extracted values. Reconciliation supports a further `other-compiled` classification; the memory profile cannot be amended in this round. | `OBJ-3`, `RTE-5` | Included generated instruction region and writeback route in the whole-system memory scope; profile checked against supplied records. | That the profile's lineage values exhaust all included retained material. | Amend and revalidate the memory comparison lineage profile to include the supported derived-material classification. |
| Custom adapter note origins are opaque, leaving the trace-source union partial. | `RTE-1`, `RTE-2` | Inspected built-in adapters and generic custom-adapter route in the reviewed repository. | A complete inventory of source classes that can enter automatic consolidation. | Inspectable custom-adapter origin metadata and a bounded inventory of configured adapters and inputs. |

## Verification and blockers

### Record verification

The boundary, runtime, memory, epistemic and reconciliation members agree on run ID `AAS-2026-10-02-instinctual-memory-01` and reviewed commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`. The bounded evidence is the registered repository snapshot: `SRC-1` supplies product and design claims and `SRC-2` supplies implementation evidence. The exclusion of host configuration, stores, traces, provider behavior and operation evidence is consistent across the members. Their conclusions remain about implemented mechanisms; deployment, activation, model consumption, proposition truth and benefit are not established.

The canonical declarations and references resolve across the set: runtime declares `OBJ-1`–`OBJ-3`, `RTE-1`–`RTE-5`, `CLM-1` and `ABS-1`; memory declares `MEM-OBJ-1`, `MEM-OBJ-2`, `MEM-RTE-6` and `MEM-RTE-7`; epistemic declares `EPI-OBJ-1`, `EPI-OBJ-2`, `EPI-RTE-1`–`EPI-RTE-3`. Memory and epistemic annotations attach to the supplied records without redeclaring them. The hook route and `RTE-3` overlap is accurately bounded: requested search is pull, while `MEM-RTE-6`/`EPI-RTE-1` describe hook-selected context; `RTE-5` separately covers setup and project-file writeback. Tidy's `EPI-RTE-2` applies to already-retained facts and supports `dedup`; that finding is distinct from consolidation's rejection of duplicate proposals.

The memory profile's scope agrees with its declarations and prose, including journal, published memory and controls, task state, generated project instructions, and hook-supplied context. Storage, form, behavioral-authority, write-agency, curation, read-back direction and signal, trace-learning, and trace-source values are supported by the named records. In particular, push selection is tied to the fixed `pref_user` identifier and prompt-term overlap, and the selected parts and hook consumer are identified. The automatic trace-fed journal-to-fact write and later-consumer path supports wired `trace_learning: yes`; the partial `trace_source` assessment preserves the unresolved custom-adapter origin and does not assert tool traces or trajectories.

One conflict remains, as the reconciliation explicitly records: `OBJ-3` and the known `lineage` profile. The included project-instruction text is derived from selected retained facts through `RTE-5`, supporting `other-compiled`, which the profile's complete value set omits. The reconciliation names the affected IDs, `SRC-2`/`src/cli.rs` evidence and the prevented conclusion. With `memory-return = no`, this is a properly marked unresolved conflict and limits the lineage-completeness conclusion; it is not an unmarked defect requiring another round.

All 28 distinct repository paths cited by the members exist in the registered snapshot. All 26 retained quotation blocks in runtime, memory and epistemic members occur within their cited source line ranges. Source-dependent findings retain source IDs and local anchors; citations support implementation claims without upgrading them to observed operation. The structural check reports `none`.

### Synthesis verification

Checked the Description against the runtime and memory records: `mem` uses a Git-backed store and provides later search and hook-context routes; source truth, host delivery, activation, and benefit remain unverified. The description is bounded to these mechanisms and limits.

Checked the Bounded synthesis paragraph by paragraph. The first paragraph accurately describes the implemented journal, consolidation, publication, and retrieval routes and distinguishes implementation evidence from deployment. The second accurately separates source-event retention and fact curation, describes bounded extraction and publication controls, and limits compare-and-swap protection to writes through that repository path; it does not imply truth checking. The third accurately distinguishes caller-requested pull retrieval, hook context supply, setup, and writeback, and carries the host-installation and activation limits. The fourth accurately characterizes explicit changes, retained controls, and the operator-applied tidy duplicate route as availability and maintenance mechanisms. The fifth accurately states the memory-route `trace_learning` classification and distinguishes it from observed improvement; its evaluation description is limited to caller-supplied retrieval criteria and does not claim truth assessment. The linked IDs resolve to the supplied records, including the overlapping hook records as reconciled.

The synthesis reads without member prose: it identifies the system and operational progression, explains what the cited mechanisms do, and states the evidence limits needed to interpret its claims. It makes no unsupported claim about operation, truth, improvement, reflection, autonomy, or self-improvement. The Limitations table carries the full unresolved conflict for `OBJ-3` and the lineage profile, states the affected IDs and prevented conclusion, and gives the profile amendment and revalidation as resolution evidence. It also bounds the unobserved deployment and effects, indeterminate event-to-fact meaning and truth, and opaque custom-adapter origins. These limitations make the public account complete without reopening reconciliation.

### Deterministic validation

`commonplace-validate kb/agentic-systems/reports/state/AAS-2026-10-02-instinctual-memory-01/output --full` runs after the manifest is written, over every member, the manifest and the set's cross-member checks; code publishes only when it passes, and publication runs it again.

### Blockers

none
