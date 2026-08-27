---
description: "The class/instance analogy captures session startup but omits the retained update relation that can revise later agent definitions and reusable-content placement"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [computational-model, deploy-time-learning, learning-theory]
---

# Instantiation alone cannot model agent learning across sessions

An agent begins each session from a durable definition: its model choice, system prompt, tools, skills, instruction files, memory stores, and configuration. Object-oriented programming offers a useful analogy. The durable definition resembles a class, and each session resembles an instance created from shared structure plus local state.

That analogy captures one important relation: a durable definition produces a session with starting context. Cross-session learning needs a second relation: evidence from one session changes the definition that later sessions inherit. A persistent object graph or state machine can model both relations, but only if it includes this retained update path. The claim here is narrower. It concerns instantiation alone, not the full expressive power of object orientation or stateful computation.

## Instantiation does not include retained update

In the common closed-world reading of the analogy, the class is fixed before an instance starts. The instance receives shared behavior, but it does not change what later instances inherit.

That restriction is not universal. In a [reflective system](./definitions/reflective-system.md), classes can themselves be runtime objects, and instance activity can help modify shared behavior. Reflection creates a causally connected path into the system's own organization. But it does not make the change itself an act of instantiation, and it does not by itself amount to learning. The update still must be evidence-responsive and durable enough to change later capacity.

Class-based systems often expose or price crossings from ordinary behavior into changes to shared definitions or runtime shape assumptions. A [metaobject protocol](../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md) exposes a separate interface for changing language organization. *[Monkey-patching](../sources/monkey-patch.ingest.md)* gives runtime modification a warning name and records incompatibility, overwrite, and source-versus-behavior risks. V8 represents changing object shapes with [dynamically updated HiddenClasses](../sources/fast-properties-in-v8.ingest.md); property-type changes can create type pollution that prevents optimal-code generation. The Erlang/OTP language platform treats live definition change as [versioned release work with state migration, reboot fallback, and explicit downgrade](../sources/erlang-release-handling.ingest.md).

The MOP, monkey-patch, and Erlang cases explicitly mark a path from ordinary execution into definition change; V8 supplies the narrower evidence that shape variation can carry an optimization price. Under [the domain-pricing criterion](./domain-pricing-routes-an-exception-to-idealization-assessment.md), they route the fixed-class model to an adequacy assessment rather than settling the question outright. For this note, the relevant issue is fence integrity, not how often reflective mutation occurs. Marked crossings still give us vocabulary for the second relation. If class change became ordinary and unmarked in the systems being compared, the idealization would fail for this purpose. Its broader adequacy outside that use remains open.

Agent systems make the update relation concrete. A session may edit a skill, append to a memory store, rewrite a routing rule, or add a validator. Any of these writes can change the [behavior-determining organization](./definitions/behavior-determining-organization.md) that shapes later runs.

Cross-session learning therefore requires an evidence-responsive retained update that changes later capacity. It does not always require a reject-capable selection gate: gradient-, error-, reward-, or viability-driven learning can determine an update directly. Readable artifact changes often follow the narrower [proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md). In that architecture, a session write is only a candidate until evaluation can reject it, and only an accepted change becomes operative for later runs.

## Content placement is a revisable policy

Reusable content can live in several places. A checklist can be rediscovered in each session, retained and retrieved when needed, loaded at session start, or inlined into an always-loaded prompt. A convention can remain only in model weights, become a retrieved note, or be enforced by a validator.

These choices vary along separate axes. Retention creates a maintenance obligation, but it can prevent repeated rediscovery. Loading policy determines whether retained content spends context on every run or only when retrieved. Session-local derivation avoids storage and maintenance, but it pays the computation cost each time the content is needed. Durable does not mean always loaded, and session-local does not mean free.

When placement is writable, the update relation can revise this allocation. [Frontloading](./frontloading-spares-execution-context.md) moves work whose inputs are already known into reusable starting structure. [Ephemeral computation](./ephemeral-computation-prevents-accumulation.md) keeps work local when reuse would not repay the maintenance cost. [Promotion](./promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) supplies criteria for moving a candidate into a durable form or loading path. A system can also learn while keeping placement fixed. Placement revision is one possible update surface, not a requirement for every learning process.

In an LLM-based agent, material loaded during a session can still direct current behavior because [instructions and content share the same token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md). That episode-scoped influence is not itself durable learning. It does, however, provide evidence about what the starting definition omitted and whether later sessions should retrieve, preload, codify, or continue to derive the material locally.

## Cross-session learning adds a definition-update relation

The startup relation maps a durable definition to a session. The update relation maps the current definition plus session evidence to a later definition. That second relation may change retained content, its behavioral authority, or its placement among retrieval, startup loading, and local derivation.

Class-based systems already give us vocabulary for this distinction. Definition change happens through a meta level or a deployment path rather than through ordinary instance execution. Agent harnesses often lack an equally enforced crossing, because a session can edit a skill file using the same tools it uses for ordinary work. In those systems, permissions, review authority, and versioned retention have to establish the process boundary. A proposal-selection loop can then search, evaluate, and retain candidate changes within that boundary; it does not replace the surrounding governance.

The Machine Studying practitioner report provides one bounded example. In preliminary Qwen3.5-9B Studying-DSPy runs, its study pass changes an agent by writing a reusable repository map before later inference. The report finds that "the gains from the cheatsheet are concentrated at the low inference budgets" ([*Machine Studying*, section 7](../sources/machine-studying.ingest.md), verbatim), and the unmodified agent catches up under forced 20-iteration search. This supports the distinction between starting a fresh session from an unchanged definition and preparing a changed definition for later sessions. The source reports no corresponding OpenClaw effect, so it does not establish a general performance law.

If the startup analogy is treated as the complete model of learning, three questions remain unanswered:

- **What can alter the durable definition?** If session-produced candidates are excluded by assumption, one possible improvement path disappears by definition.
- **What does repeated session work reveal?** Reconstructing the same context again and again can be evidence that the starting definition or retrieval policy omitted reusable material.
- **Can placement change?** Retention, retrieval, frontloading, local derivation, and codification are policies that an update process may reconsider.

## Scope

- The general claim requires an evidence-responsive retained update, not always proposal and rejection. The proposal-selection analysis applies to candidate-based readable artifact changes.
- The placement argument applies when a deployment exposes placement as a writable policy. A fixed-store learner can still change across sessions without moving content among loading paths.
- Episode-scoped behavioral influence is argued here for LLM-style, context-mediated runtimes. It transfers only where session-provided material can alter behavior rather than merely parameterize a closed repertoire.
- The user's current question, working files, and run-specific intermediates can remain correctly session-local. The claim concerns reusable material whose placement is a genuine design choice.
- Session boundaries vary under compaction, resumption, and sub-agent spawning. This note assumes a settled boundary rather than deriving one.

## Open Questions

- Metaobject protocols and versioned hot code swap supply vocabulary for governed definition change. How much of their machinery transfers to a runtime that cannot enforce the base/meta fence remains open.
- What is the natural unit of placement? Systems often move whole files, while the reusable unit may be a claim, rule, or procedure.

---

Relevant Notes:

- [Domain pricing routes an exception to idealization assessment but does not decide it](./domain-pricing-routes-an-exception-to-idealization-assessment.md) — grounds: supplies the two-stage criterion under which reflective counterexamples are routed to an adequacy assessment rather than treated as automatic refutations or automatic acceptance
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why a correction outside the chosen update surface cannot be reached by optimizing within it
- [Orchestration strategies and run state have opposite persistence requirements](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — extends: applies the retained-versus-episode distinction to schedulers and run state
- [Machine Studying](../sources/machine-studying.ingest.md) — evidenced-by: supplies the changed-agent formulation and the bounded low-budget repository-map result
- [Metaobject Protocols: Why We Want Them and What Else They Can Do](../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md) — evidenced-by: attests explicit base/meta separation and protocol entry points for reflective definition change
- [Monkey patch](../sources/monkey-patch.ingest.md) — evidenced-by: attests warning vocabulary and documented coordination risks around runtime modification
- [Fast properties in V8](../sources/fast-properties-in-v8.ingest.md) — evidenced-by: attests shape-sensitive property optimization and the risk that type pollution prevents optimal-code generation; the capture does not establish deoptimization of already optimized code
- [Erlang/OTP release handling](../sources/erlang-release-handling.ingest.md) — evidenced-by: attests live definition change as versioned deployment with state migration, reboot fallback, and explicit downgrade
