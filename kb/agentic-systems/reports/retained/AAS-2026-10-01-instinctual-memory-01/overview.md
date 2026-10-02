---
type: agentic-systems/types/agentic-system-analysis-overview.md
description: instinctual-memory turns session events and imported notes into filtered Git-backed facts, then serves them through requested APIs and optional lexical hooks; host uptake is unknown.
run-id: AAS-2026-10-01-instinctual-memory-01
system: instinctual-memory
run-date: '2026-10-01'
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
analysis-cutoff: '2026-10-01'
evidence-tier: code-grounded
inputs-commit: fdbbd10e0ba29e8788f7f4cad13f05c9e694f588
---

# instinctual-memory agentic-system analysis

## Boundary and evidence

The target is `mem`, a Git-first durable memory system for AI agents, at the requested commit. The analysis covers its CLI and library behavior for ingesting session and instruction files, journaling events, consolidating sourced facts, searching and reading memory, validated changes and erasure, MCP and HTTP access, hooks, writeback, and setup integrations. It treats the repository's implementation and its own operational/design documentation as evidence. The intended consumers are coding agents and their operators; the repository describes project-local and global stores and integration with Claude Code, Codex, and OpenCode (`README.md`, `src/`).

The boundary includes the memory store, its journal and Git-backed fact repository, retrieval and reranking paths, adapters, hooks, and setup behavior implemented here. It excludes the enclosing agent runtimes, their session scheduling and prompt assembly beyond this system's hooks and tool responses, providers and model services, host configuration outside changes made by this system, and user/project source repositories. These dependencies are not part of the selected target, so this analysis cannot establish their independent behavior or whether delivered memory changes an agent's decisions. The code-grounded tier supports mechanisms visible in the repository; it does not establish operational outcomes or causal benefit.

The checkout was verified to have origin `https://github.com/jasonkneen/instinctual-memory`, the requested commit, and no reported working-tree changes before source inspection. The evidence boundary is the repository at that commit, with an applicability cutoff of 2026-10-01.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/jasonkneen/instinctual-memory` (access root: `related-systems/jasonkneen--instinctual-memory/`) | `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` | implementation | CLI/library modules for ingestion, journal, consolidation, search, changes, erasure, adapters, hooks, and setup | `src/main.rs`, `src/lib.rs`, `src/ops.rs`, `src/mcp.rs`, `src/hook.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` | No execution traces, provider calls, or host-runtime observations are in scope; this prevents claims about deployed operation, agent uptake, or benefit. |
| SRC-2 | Git | `https://github.com/jasonkneen/instinctual-memory` (access root: `related-systems/jasonkneen--instinctual-memory/`) | `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` | doctrine/design | README's stated purpose, data flow, command surface, integration behavior, and configuration | `README.md` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` | Documentation describes intended behavior; absent runtime evidence prevents treating those declarations as observed use. |

Amended or superseded records: EPI-OBJ-1, EPI-OBJ-2, EPI-OBJ-4; [reconciliation](reconciliation.md).

## Bounded synthesis

At the requested repository commit, `mem` is a caller-invoked local memory store, not an agent scheduler. It appends session and imported material to a local journal, then processes checkpoint-bounded batches into versioned entity facts in a Git repository. Deterministic patterns or an optional model propose facts; source-quote, lastingness, duplicate, blocked-ID, and domain checks constrain publication. The quote check establishes that cited text occurs in the source event, not that the fact is true or follows from it. [MEM-OBJ-1](memory.md#mem-obj-1-source-event-journal), [MEM-OBJ-2](memory.md#mem-obj-2-entity-fact-snapshots), [MEM-OBJ-4](memory.md#mem-obj-4-consolidation-checkpoint-and-dispositions), [MEM-RTE-2](memory.md#mem-rte-2-consolidate-events-into-facts), [EPI-RTE-2](epistemic.md#epi-rte-2--model-extraction), [EPI-RTE-4](epistemic.md#epi-rte-4--domain-validation)

Callers can request search, read, or history through the CLI and service adapters. Search selects eligible facts and journal events by query and filters, with optional reranking. A separate installed Claude hook path can supply general guidance at session start and choose up to six facts by lexical overlap with a qualifying prompt. Explicit writeback can export eligible facts to a project instruction file. These mechanisms make material available or construct context; this repository evidence does not establish hook installation, host delivery, agent use, or changed behavior. [RTE-1](runtime.md#rte-1--local-cli-operation), [RTE-2](runtime.md#rte-2--mcp-stdio-operation), [MEM-RTE-4](memory.md#mem-rte-4--requested-search-read-and-history), [MEM-RTE-5](memory.md#mem-rte-5--installed-hook-context-injection), [MEM-RTE-7](memory.md#mem-rte-7--explicit-writeback-to-project-instructions)

The write path has operational safeguards: explicit corrections supersede facts, soft forget retracts and suppresses them, and hard erase redacts source events and rewrites memory history. These controls govern availability and re-extraction; they do not judge whether a proposition is false. [MEM-OBJ-3](memory.md#mem-obj-3-retrieval-and-admission-controls), [MEM-RTE-3](memory.md#mem-rte-3--explicit-remember-correction-and-soft-forget), [MEM-RTE-6](memory.md#mem-rte-6--tidy-and-hard-erase), [EPI-RTE-7](epistemic.md#epi-rte-7--explicit-memory-changes)

The repository wires trace-fed durable writes from user session turns, which supports a memory-route classification of trace learning. It does not show that retained facts improve future capacity. The lastingness prompt is a formulated rule (theory-builder condition 1 is afforded); dependence on its meaning, content-directed criticism, and iterative revision are not established. Reflection, autonomous theory building, and self-improvement are likewise not established by the inspected routes. These are separate limits on the available evidence, not a system-wide claim about inaccessible providers or deployments. [MEM-RTE-2](memory.md#mem-rte-2--consolidate-events-into-facts), [EPI-RTE-2](epistemic.md#epi-rte-2--model-extraction), [EPI-RTE-3](epistemic.md#epi-rte-3--consolidation-disposition), [MEM-OBJ-4](memory.md#mem-obj-4-consolidation-checkpoint-and-dispositions)

## Limitations

| limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| No execution traces or host prompt records were supplied. | SRC-1, SRC-2, OBJ-1, RTE-1, RTE-2, RTE-3, MEM-RTE-1 through MEM-RTE-7, EPI-RTE-6 | Repository implementation and README at commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`; host runtimes and deployments excluded. | Actual installation, invocation, provider outcomes, context delivery, agent uptake, and behavioral effect. | Inspectable deployed traces linking ingestion, extraction, retrieval or hook delivery to later agent behavior. |
| Candidate filtering and source-quote matching do not supply an evidence-consuming truth criterion; no independent truth acceptance route was found in the inspected repository. | EPI-OBJ-3, EPI-RTE-1 through EPI-RTE-5, EPI-CLM-1, MEM-RTE-2 | Consolidation, validation, and publication paths at the pinned commit; provider internals and external deployment checks excluded. | Truth, entailment, reliability, or warranted acceptance of persisted facts; the absence of checks outside this boundary. | A specified truth or intended-use criterion, evidence-consuming evaluation route, and inspectable outcomes within the claimed scope. |
| Durable trace-fed writes and a lastingness rule are implemented, but criticism does not feed a demonstrated improvement cycle. | MEM-RTE-2, MEM-OBJ-4, EPI-RTE-2, EPI-RTE-3 | Inspected extraction, dispositions, checkpoint, and later retrieval code; no operational comparisons supplied. | Improved future capacity, theory-builder conditions 2–4, reflective or autonomous theory building, or self-improvement. | Evidence that decisions depend on the rule's content, that criticism changes reliance or the rule and shapes a next round, plus attributable future-capacity comparisons and role coverage for reflection or autonomy. |

## Verification and blockers

### Record verification

The set is bounded consistently to `https://github.com/jasonkneen/instinctual-memory` at `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`. The boundary registers implementation as SRC-1 and design documentation as SRC-2, excludes host/provider internals, and limits claims about actual operation, uptake, and benefit. The source IDs used by the members resolve to those entries. I checked the referenced source paths in runtime, memory, and epistemic records against the pinned tree; they exist. The structural set check reports `none`. Member types, run ID, and reviewed boundary agree.

Canonical identities and ownership are coherent after reconciliation. OBJ-1 remains the CLI/service. MEM-OBJ-1 through MEM-OBJ-5 cover the journal, fact snapshots, controls, checkpoint/dispositions, and generated index. EPI-OBJ-1 and EPI-OBJ-2 are explicitly superseded by MEM-OBJ-1 and MEM-OBJ-2; EPI-OBJ-4 is superseded by MEM-OBJ-3. EPI-OBJ-3 remains the distinct transient candidate object. The reconciliation preserves the superseded IDs and redirects affected route references. Runtime routes RTE-1 through RTE-3 remain broad entry routes; memory routes MEM-RTE-1 through MEM-RTE-7 and epistemic routes EPI-RTE-1 through EPI-RTE-7 describe distinct scoped mechanisms or functions. The records consistently distinguish implementation from observed operation and availability from host delivery, activation, or benefit.

The memory-comparison profile agrees with the records across its scope and all ten axes. `storage_substrate` and `representational_form` map to the five retained objects. `lineage` maps authored changes, imported notes, compiled index state, and trace-extracted facts to their respective routes and objects. `behavioral_authority` is scoped to in-repository consumers and distinguishes enforcement, instruction, knowledge, learning, ranking, routing, and validation. `write_agency` distinguishes automatic ingestion/consolidation and hook processing from caller-authored changes. `curation_operations` maps consolidate, dedup, evolve, and invalidate to the described routes and does not claim promotion or synthesis. `read_back_direction` distinguishes requested pull, hook push, and explicit writeback; `read_back_signal` identifies coarse session-start context and the prompt-conditioned lexical selector. `trace_learning` and `trace_source` are limited to the wired user-session-to-fact path in MEM-RTE-2, with session turns as the source. The epistemic records leave semantic preservation/entailment indeterminate and do not establish truth acceptance or improved capacity; this is compatible with the profile's expressly operational classification of a trace-fed durable write. Reconciliation resolves the apparent route-scope differences, including hook push versus requested search, without strengthening the profile.

Material dispositions are represented consistently: consolidation candidates pass provenance/shape and operational admission checks, then domain validation and publication; these do not amount to truth acceptance. Explicit remember/correct/forget changes alter store state without establishing truth or falsity. Search/read and hooks make eligible content available, while actual host delivery and use remain unobserved. Controls suppress/retract or erase; checkpoint chooses the next processing window; retained dispositions are not shown to feed later proposal decisions. The reconciliation resolves the “only path” wording as limited to live-agent authored changes and distinguishes automatic consolidation. The claim that consolidation produces “curated facts” is assessed as operational filtering and storage, with its stronger warrant implication unsupported. No unresolved conflict is marked, and none is needed: the remaining limits are explicit and bounded by the inspected repository evidence.

### Synthesis verification

The Description identifies the source-to-fact flow and its deployment limit. The Bounded synthesis is readable without the member prose: its record links identify the supporting entries, and each operational claim is paired with a scoped record. The account of caller-invoked local operation, journal ingestion, checkpoint-bounded consolidation, Git-backed entity facts, rule/model proposals, and the distinct source-quote, lastingness, duplicate, blocked-ID, and domain checks is supported by MEM-OBJ-1, MEM-OBJ-2, MEM-OBJ-4, MEM-RTE-2, EPI-RTE-2, and EPI-RTE-4. Its caveat that quote matching establishes occurrence rather than truth or entailment matches EPI-RTE-2 through EPI-RTE-5.

The CLI/service search, optional reranking, hook-supplied guidance and lexical fact selection, and explicit writeback account matches RTE-1, RTE-2, MEM-RTE-4, MEM-RTE-5, and MEM-RTE-7. The synthesis properly bounds these as implementation paths and does not claim installation, delivery, uptake, or behavior change. The correction, soft-forget, and hard-erase descriptions match MEM-OBJ-3, MEM-RTE-3, MEM-RTE-6, and EPI-RTE-7; the distinction between operational availability and truth judgment is supported.

The final paragraph keeps trace-learning classification separate from capacity improvement. The lastingness rule is formulated (condition 1 afforded); dependence on its meaning, content-directed criticism, iteration, reflection, autonomous theory building, and self-improvement are not established. These are appropriately presented as separate evidence limits, consistent with MEM-RTE-2, MEM-OBJ-4, and EPI-RTE-2/3. All three Limitations rows name affected IDs, the inspected boundary, the prevented conclusion, and resolving evidence. They carry the source/deployment, truth-warrant, and improvement-cycle limits. Reconciliation contains no `Unresolved conflict:` entry requiring an additional limitation. No unsupported substantive statement found.

### Deterministic validation

`commonplace-validate kb/agentic-systems/reports/state/AAS-2026-10-01-instinctual-memory-01/output --full` runs after the manifest is written, over every member, the manifest and the set's cross-member checks; code publishes only when it passes, and publication runs it again.

### Blockers

none
