---
description: "Code-grounded analysis of Apache Maka's host-owned execution spine, context projections, effect settlement, alternate forcing routes, and distinct memory lifecycles"
type: kb/types/note.md
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-04-apache-maka-02
source-identity: https://github.com/apache/maka
reviewed-revision: ece69ab3e7a1629a6073831005711d8aa7160ca4
traits: [has-external-sources, has-implementation]
tags: [agent-memory, context-engineering, evaluation, tool-loop]
---

# Apache Maka

**Evidence basis:** code-grounded inspection of [Apache Maka at commit
`ece69ab3e7a1629a6073831005711d8aa7160ca4`](https://github.com/apache/maka/tree/ece69ab3e7a1629a6073831005711d8aa7160ca4),
with an applicability cutoff of 2026-09-04. The repository is a complete
artifact, but its operating loop crosses external model providers, operating
systems, tools and services, peer deployments, and user workspaces. The
analysis establishes static wiring and bounded absences, not deployed behavior,
output quality, universal isolation, or causality.

Maka is an agent workspace built around one Runtime Host. Desktop, TUI, CLI,
bot, and evaluation clients enter the same host protocol. The host owns one
State Root, admits top-level work, composes model requests, mediates effects,
and persists execution facts. Interactive turns, graph children, approved
remote requests, scheduled tasks, and goal continuations change how work is
triggered, but they return to the same root-execution path. Maka's [system
map](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/ARCHITECTURE.md#L22-L84)
and [Runtime Host
architecture](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/docs/architecture/runtime-host-architecture.md#L41-L112)
state this design.

## Immutable events participate in execution authority

The ordinary route is:

`client -> Runtime Host -> SessionManager/AgentRun -> provider -> tools -> durable events -> client projection`

Before provider or tool dispatch, AgentRun commits an invocation opening. It
fixes provider route, configuration, root authority, source, and lineage. Run
Composer separately persists the prompt and tool basis. Provider output is
normalized into RuntimeEvents, and required facts are committed before
downstream projection. One first terminal fact controls completion. The
[composition and opening
path](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/agent-run.ts#L1120-L1258)
and [event settlement
path](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/agent-run.ts#L948-L1015)
make the event ledger part of execution authority rather than diagnostic history
alone.

This supports recoverable execution provenance, not bit-exact provider replay.
The inspected system does not retain one complete byte-level snapshot of every
materialized request, provider state, and external dependency.

## Working context is a validated projection

Run Composer assembles a provider request from system and workspace
instructions, skills, eligible local memory, prior visible RuntimeEvents or a
compact projection, tool schemas, capability bindings, and the current message.
The [composer](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/interactive-run-composer.ts#L126-L254)
owns selection; the [AI SDK
backend](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/ai-sdk-backend.ts#L2050-L2205)
materializes the provider call.

Compaction shortens working context without deleting canonical history. A
checkpoint may replace an exact event prefix with a text summary or compatible
provider state only after coverage, digest, lineage, and provider checks. A
mismatch falls back to raw events. The [compaction
design](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/docs/architecture/llm-compaction-events-log-projection-draft.md#L55-L288)
therefore separates retained history from model-visible projection. Its checks
warrant structural substitution, not semantic fidelity or observed influence.

## Effect control is layered and recovery is conservative

A tool schema only affords a call. ToolRuntime separately applies availability,
loop, capacity, permission, managed-path, client-capability, and execution-
boundary gates. After admission, it persists a T1 dispatch fact, attempts the
effect, then persists T2 and a correlated Tool Result before the result can
drive another model step. The [tool settlement
path](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/tool-runtime.ts#L1400-L1735)
and [durable T1/T2
ordering](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/tool-runtime.ts#L2250-L2445)
implement these distinct authorities.

Containment remains route-specific. Restricted managed paths can require
OS-backed enforcement, while bypass profiles, some PTY and resource routes,
client-executed capabilities, external services, and platform gaps have
different envelopes. Maka's [sandbox
contract](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/sandbox/README.md#L20-L108)
supports a guarantee only for a named tool, profile, adapter, and platform.

If a process dies after T1 but before T2, recovery does not silently invent an
outcome. It repairs readable ledgers, checks whether continuation is safe, and
parks or admits a fresh invocation. General tool-specific effect reconciliation
and workspace checkpoint restore are not wired for every route. The [resume
architecture](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/docs/architecture/runtime-resume-architecture.md#L50-L164)
makes that limit explicit.

## Alternate forcing routes reuse the host spine

Agent Graph stores schedules, claims, wakes, and child references durably. A
claimed child receives its own Session and execution identities; the root
supervisor must explicitly read a bounded child result. The [graph execution
coordinator](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/agent-graph-execution-coordinator.ts#L1-L220)
connects this work to ordinary Host admission. Durable coordination does not
make child propositions true or merge their transcripts implicitly.

Session collaboration also preserves Host ownership. A guest can submit only a
grant-authorized turn request. An owner approval changes the request's durable
state; the coordinator then calls ordinary `turn.start` or regeneration with an
approved Host connection context. The [request
protocol](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/protocol/session-collaboration.ts#L30-L180)
and [approved-turn
coordinator](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/session-turn-access-request-coordinator.ts#L20-L159)
do not transfer runtime authority to the guest.

Scheduled tasks retain intent and stable execution identities, then submit a
durability-required user turn through Host admission. Goals add a more active
continuation policy. After a completed goal turn, a bounded, tool-free model
call judges progress from the goal condition and recent messages. Deterministic
coordinator policy and durable state settle, wait, pause, or start a fresh Host
turn after lease, task, iteration, token, and stall gates. The [goal
evaluator](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/goal-evaluator.ts#L20-L235)
and [continuation
coordinator](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/goal-continuation.ts#L640-L860)
separate the model judgment from the state transition. Evaluator failure is
fail-open continuation, so the judgment is not treated as semantic proof.

## Retained context has distinct lifecycles

Maka uses “memory” for mechanisms with different producers, stores, selectors,
and later consumers.

### Approved document memory

`MemoryBundle` is a user-approved document store. Runtime policy gates reading;
the prompt selector filters active entries by Session scope, redacts secrets,
and applies a character budget. Run Composer inserts the result into a main-
session `<local-memory>` fragment explicitly marked as user-authorized but
untrusted. The [selection
path](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/core/src/local-memory.ts#L291-L383)
and [prompt
injection](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/interactive-run-composer.ts#L588-L623)
form a wired later-read route. Child compositions omit this implicit memory.
Static wiring does not show that an entry changed a model decision. The parsed
`decayTtlMs` metadata is not enforced by the inspected prompt selector, so it
does not establish automatic expiry.

### Structured extraction

`MemoryExtractionEngine` is a separate write route. It selects bounded user-
authored event evidence, asks an auxiliary model to propose and canonicalize
items, then applies quote, secret, schema, coverage, scope, and budget gates
before atomically committing `MemoryItem` records, cursors, and receipts. The
[extraction
implementation](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/memory-extraction.ts#L780-L1166)
warrants provenance and admission shape for retained items.

The store affords item lookup, but no production route in the inspected
Runtime, Runtime Host server, or Desktop main composition reads those items into
a later agent request or promotes them into `MemoryBundle`. An explicit remember
operation can return a same-invocation result, which is not persistent recall.
Durable structured extraction is therefore wired; durable structured-memory
influence on later model behavior is not.

### Image context offload

An image Read can store Session-owned, content-addressed bytes and retain only a
reference in the Tool Result. A later vision-capable request rehydrates the
bytes after ownership, digest, media-type, availability, and budget checks. The
[snapshot store](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/storage/src/read-image-snapshot-store.ts#L37-L115)
and [provider
materialization](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/ai-sdk-backend.ts#L4560-L4655)
warrant byte provenance within that contract, not image meaning or relevance.

## Operational acceptance is not truth acceptance

Maka has strong, distinct authorities for execution facts: event durability
accepts identity and occurrence; permission authorizes an attempted action;
tool settlement records an outcome; graph claims authorize work; memory gates
authorize retention or prompt eligibility; remote approval authorizes a turn;
evaluation selection chooses a verifier-relative result; and goal policy chooses
a transition. None is a general route that accepts model, tool, child, memory,
image, or summary propositions as true.

Model-mediated compaction and extraction make the distinction sharp. Their
deterministic gates check coverage, quotation, secrets, schema, and provenance,
not entailment. The evaluation package similarly retains declarative cells,
immutable attempts, verifier output, and earliest-compatible selection. The
inspected production runtime does not consume evaluation results to update
policy or behavior. [Evaluation
selection](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/eval/src/runner.ts#L145-L245)
is operational machinery, not an online learning loop.

## Assessment

At this revision, Maka's strongest architectural property is explicit ownership
of execution decisions. One Host admits work; immutable composition and opening
records precede dispatch; canonical events control replay and termination;
ToolRuntime stages effect settlement; and graph, remote, scheduled, and goal
routes retain distinct identities while returning to the same runtime spine.
Context is a replaceable projection over stronger state, and memory mechanisms
are separable by later consumer rather than name.

The main limits sit at external and semantic boundaries. Containment depends on
the exact route and deployed platform. Recovery parks effects it cannot
reconcile. Structured extraction has no later agent read-back. Goal judgments
can force continuation without becoming truth. Operational provenance never
becomes general semantic acceptance. Evaluation results do not feed runtime
adaptation. No candidate-linked run shows activation or causal value. These
limits qualify the guarantees without negating the implemented Host and event
spine.

---

Relevant Notes:

- [Apache Maka repository at the reviewed commit](https://github.com/apache/maka/tree/ece69ab3e7a1629a6073831005711d8aa7160ca4) — evidenced-by: frozen implementation and doctrine boundary for this analysis
