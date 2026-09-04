---
description: "Code-grounded analysis of Apache Maka's Runtime Host, event authority, context projection, tool settlement, graph coordination, and separate memory routes"
type: kb/types/note.md
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-04-apache-maka-01
source-identity: https://github.com/apache/maka
reviewed-revision: fcfa0550e192c65854052aa354cd435b1422ebce
traits: [has-external-sources, has-implementation]
tags: [agent-memory, context-engineering, evaluation, tool-loop]
---

# Apache Maka

**Evidence basis:** code-grounded inspection of [Apache Maka at commit `fcfa0550e192c65854052aa354cd435b1422ebce`](https://github.com/apache/maka/tree/fcfa0550e192c65854052aa354cd435b1422ebce), captured 2026-09-04. All implementation findings below are wired in that revision, but no deployed run or causal experiment was observed.

Maka is an agent workspace built around one Runtime Host. Desktop, TUI, CLI, bot, and evaluation clients enter the same host protocol. The host owns admission and composes Session management, an agent runtime, model adapters, tools, recovery, memory, and graph execution. The repository is a complete distributed artifact, but its operating loop crosses external model providers, operating-system enforcement, optional services, and user-controlled workspaces. The analysis can therefore characterize the artifact and its contracts, not the behavior of a complete deployed loop. Maka's [system map](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/ARCHITECTURE.md#L22-L84) and [product claims](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/README.md#L36-L94) state this shared-runtime design.

## Immutable events are part of execution authority

The ordinary route is:

`client -> Runtime Host -> SessionManager/RuntimeKernel -> AgentRun -> provider -> tools -> durable events -> client projection`

Before provider or tool dispatch, AgentRun commits a hidden `invocation_opened_v1` event. It fixes the provider route, configuration, root authority, source, and lineage for that invocation. Runtime readers later reconstruct the invocation from this opening, its RuntimeEvents, and its first terminal event. The opening is not a mutable header and does not enter model-visible history. The [invocation fact types](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/core/src/runtime-invocation.ts#L20-L120) and [AgentRun opening path](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime/src/agent-run.ts#L1030-L1210) implement this boundary.

Provider output follows the reverse route. Maka's model adapter streams provider events, maps them into RuntimeEvents, and durably accepts required facts before downstream delivery. Terminal settlement has one claimant, and a terminal event is committed before the terminal projection reaches clients. Session and UI state are derived views over this stronger event record. The event ledger is therefore not only diagnostic history. Its facts control admission, replay, recovery, and terminal ordering.

This design supports recoverable execution provenance. It does not support bit-exact provider replay: the ledger does not retain one complete byte-level snapshot of every materialized request, provider state, and external dependency.

## Working context is a validated projection

InteractiveRunComposer assembles the next provider request from policy, workspace instructions, skills, eligible local memory, prior visible RuntimeEvents or a compact projection, active tools, and the current user message. The [composer](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime-host/src/server/interactive-run-composer.ts#L127-L260) owns this context selection; the [AI SDK backend](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime/src/ai-sdk-backend.ts#L1660-L1845) owns the provider loop.

Compaction shortens working context without deleting canonical history. A `HistoryCompactCheckpoint` can replace an exact event prefix with either a text summary or compatible provider-native state. Coverage, digest, lineage, and provider checks decide whether that substitution is valid. Raw events remain authoritative and can reject a stale or incompatible checkpoint. Maka's [compaction design](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/docs/architecture/llm-compaction-events-log-projection-draft.md#L55-L270) makes this distinction explicit.

The checks warrant structural substitution, not semantic fidelity. They show which prefix a checkpoint covers and whether it belongs to the invocation and provider route. They do not show that a model-written summary preserved every constraint or proposition. Canonical retention, context presence, and behavioral activation are three separate claims here: the code establishes the first two routes, while activation remains unobserved.

## Tool control is layered and route-specific

A model-visible tool schema advertises capability, but ToolRuntime applies separate controls before an effect. These include availability, loop limits, permission, execution boundary, managed-mutation rules, and capacity. After admission, Maka records a durable T1 dispatch fact, executes the in-process or external capability, then records T2 and a correlated Tool Result before the result can drive another model step. The [tool settlement path](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime/src/tool-runtime.ts#L2160-L2445) implements that ordering.

This creates three distinct surfaces:

- the capability surface exposed to the model;
- the grant set permitted by current policy;
- the isolation envelope supplied by the deployed tool, profile, and operating system.

Restricted managed paths can use OS-backed enforcement and fail closed when required enforcement is unavailable. The guarantee is not universal containment. Bypass and external profiles, some PTY and resource routes, client-executed tools, and platform gaps have different envelopes. Maka's [sandbox contract](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime/src/sandbox/README.md#L20-L108) therefore supports claims only for a named tool, profile, and platform.

Recovery preserves unresolved effect state. If a process dies after T1 but before T2, Maka does not silently convert the missing outcome into success or failure. It repairs readable ledgers, checks whether continuation is safe, and either parks or admits a fresh invocation. The [resume design](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/docs/architecture/runtime-resume-architecture.md#L50-L260) makes safe-boundary continuation feature-flagged. General tool-specific external-effect reconciliation and workspace checkpoint restore are not wired in the reviewed production composition, so recovery cannot safely settle every ambiguous effect.

## Agent Graph reuses the same runtime spine

Agent Graph adds durable scheduling rather than a second execution model. SQLite owns schedule updates, claims, and wakes. A claimed child gets its own Session, invocation identity, and RuntimeEvent history. The root supervisor wakes and explicitly reads bounded child results by reference. The [graph execution coordinator](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime-host/src/server/agent-graph-execution-coordinator.ts#L55-L210) connects graph control to ordinary runtime execution.

This gives scheduling and child results inspectable identities across restart. It does not implicitly merge child transcripts into the parent, attenuate all delegated capabilities, or establish that a child's propositions are true. Durable coordination and trustworthy synthesis remain different properties.

## Maka has three different retained-context routes

The repository uses “memory” for mechanisms with different producers, stores, selectors, and later consumers.

### Approved document memory

`MemoryBundle` is a user-edited, approved document store. The [host memory coordinator](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime-host/src/server/memory-coordinator.ts#L98-L245) applies runtime privacy and memory policy. The [prompt-body builder](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/core/src/local-memory.ts#L291-L313) selects active entries by Session scope, redacts secrets, and truncates the result to a character budget. The [composer](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime-host/src/server/interactive-run-composer.ts#L570-L631) inserts that body into a main-session `<local-memory>` fragment and marks it as untrusted advisory material. This is a wired read-back route: material retained across invocations can re-enter a later model request. Its actual influence is unobserved, and the child-instruction prompt does not receive the same implicit memory.

### Structured extraction

`MemoryExtractionEngine` is a separate write path. It selects bounded user-authored event evidence, asks an auxiliary model to propose and canonicalize items, then applies exact-quote, secret, and schema gates before committing `MemoryItem` records, cursors, and receipts to SQLite. The [extraction implementation](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime/src/memory-extraction.ts#L780-L1145) warrants source linkage and shape for accepted items.

No production route in the inspected runtime, Runtime Host, or Desktop composition reads those persistent items back into later agent requests or promotes them into `MemoryBundle`. The explicit remember tool can return a same-invocation result, but that is not persistent recall. Maka therefore wires durable structured extraction without wiring durable structured-memory influence on later agent decisions.

### Image context offload

A successful image `Read` can store content-addressed bytes under a Session-owned `SessionContextRef` and retain only the reference in its Tool Result. A later vision-capable request can rehydrate those bytes after ownership, digest, media-type, availability, and budget checks. The route spans the [image Read implementation](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime/src/builtin-tools.ts#L330-L455), the [snapshot store](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/storage/src/read-image-snapshot-store.ts#L37-L110), and [provider materialization](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/runtime/src/ai-sdk-backend.ts#L4480-L4635).

This route avoids duplicating image bytes through the event ledger while preserving byte provenance. It can warrant byte identity and ownership within its storage contract. It cannot warrant what the image means, whether it is relevant, or whether the model used it well.

## Operational checks do not become semantic acceptance

Maka has strong checks around operational facts. Event durability warrants identity, order, correlation, and occurrence. Permission gates authorize an attempted action. Tool settlement records an outcome. Memory approval permits advisory prompt use. Graph claims authorize execution. Compaction validates coverage. Extraction gates validate evidence linkage and shape. Image checks validate byte identity. None of these checks accepts a proposition as true.

Model and child outputs are retained as conjectural content. Tool Results, approved document memory, evaluation results, and image bytes are imported with provenance but without general truth acceptance. Compaction summaries and extracted `MemoryItem` content are semantically indeterminate because model-mediated transformation may preserve or add meaning; their deterministic gates do not test entailment. No general evidence-consuming route tests and accepts model, tool, child, or memory propositions for later reliance.

The evaluation package keeps declarative experiment structure, immutable attempts, and earliest-compatible non-replaceable result selection. Maka subjects enter Runtime Host, while external subjects use adapters. The [result selector](https://github.com/apache/maka/blob/fcfa0550e192c65854052aa354cd435b1422ebce/packages/eval/src/runner.ts#L160-L245) is operational machinery: the inspected production system does not consume scores to update runtime policy or behavior. Benchmark validity, agent quality, and causal component effects depend on excluded tasks, verifiers, outputs, and experimental design.

## Assessment

At the reviewed revision, Maka's strongest system property is explicit ownership of execution facts. One host admits work; immutable opening and event records constrain dispatch, replay, recovery, and termination; context is a replaceable projection over canonical history; tool effects use staged settlement; and graph work retains child identities. These are implemented routes, not merely documentation claims.

The main limits sit at the system's external and semantic boundaries. Containment depends on the exact tool, profile, platform, and external executor. Recovery parks effects it cannot reconcile. Persistent structured extraction has no later agent read-back. Operational provenance never becomes general truth acceptance. Evaluation results do not feed an adaptation loop. These limits narrow the guarantees without implying that the core runtime and event spine are missing.

## Scope

- The evidence boundary is commit `fcfa0550e192c65854052aa354cd435b1422ebce` on 2026-09-04. Later changes are outside this analysis.
- Inspection covered material runtime, storage, Runtime Host, graph, memory, compaction, sandbox, recovery, and evaluation paths. Optional MCP, bot, computer-use, and client-capability integrations were not exhaustively traced.
- No candidate-linked deployed run, model-provider implementation, OS-level sandbox observation, benchmark corpus, verifier output, or causal comparison was available. The analysis establishes code wiring and bounded absences, not deployed behavior, output quality, activation, or causality.
- External model behavior, external service correctness, user decisions, and machine-specific containment remain outside the repository boundary.

---

Relevant Notes:

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — provides the responsibility split used to read Maka's shared Runtime Host
- [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) — distinguishes Maka's retained stores, read-back routes, context presence, and unobserved effects
- [Runtime structure determines the control surfaces available to governance](../notes/runtime-structure-determines-governance-control-surfaces.md) — explains why Maka's execution spine and tool routes expose different enforcement points
- [Apache Maka repository at the reviewed commit](https://github.com/apache/maka/tree/fcfa0550e192c65854052aa354cd435b1422ebce) — evidenced-by: the frozen implementation and doctrine boundary for this analysis
