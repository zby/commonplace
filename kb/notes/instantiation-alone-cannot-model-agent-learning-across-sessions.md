---
description: "Instantiation explains session startup; cross-session learning needs selected write-back and revisable content placement — a governed transformation class-based OO fences behind meta-protocols and agent harnesses must rebuild in process"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [computational-model, deploy-time-learning, learning-theory]
---

# Instantiation alone cannot model agent learning across sessions

An agent has a durable definition: its model choice, system prompt, tools, skills, instruction files, memory stores, and configuration. Object-oriented programming supplies a useful analogy. The definition resembles a class, and each session resembles an instance. Shared structure configures many disposable runs, each with local state.

This analogy captures session startup, but not the whole learning lifecycle. Learning across sessions requires a second relation: experience from one session informs a candidate change to the durable definition, a selection step decides whether later sessions should receive it, and the system may revise where reusable content belongs. Reflection lets some class-based systems represent runtime mutation, but instantiation alone does not model this governed transformation.

## Instantiation does not include selected write-back

The common closed-world reading of the analogy treats the class as fixed before an instance starts. An instance receives shared behavior but does not change what later instances inherit.

This restriction is not a property of every class-based system. In a reflective system, classes can be runtime objects, and instance activity can help change shared behavior. [Reflection](./definitions/reflective-system.md) supplies a causally connected path into the system's own organization. It does not by itself supply learning: mutation still needs evidence, evaluation, and retention before it counts as improvement.

Those reflective paths do not make the closed-world reading naive. The fixed class is class-based object orientation's first-order model — the idealization that buys invariants, substitution reasoning, and compiled dispatch — and the paradigm prices its own exceptions. Class mutation goes through a marked reflection interface rather than ordinary class syntax; the practice carries a warning name in monkey-patching; runtimes charge for it by deoptimizing code specialized on the old shape; and where class change must happen in production, it is ritualized into versioned changesets and migration callbacks. On the criterion in [domain pricing routes an exception to idealization assessment but does not decide it](./domain-pricing-routes-an-exception-to-idealization-assessment.md), that pricing routes the reflective counterexamples to idealization assessment rather than letting them defeat the model outright: in the model, instances do not modify their class, and real class-based systems mark every path that does. The assessment's second half is still owed — how much behaviour reflective mutation carries in the systems this note reasons about, and what the model's declared use tolerates, are not yet established — so the idealization is declared here with its adequacy record open for a future pass to attack.

Agent systems make the additional relation explicit. A session may edit a skill, append to a memory store, rewrite a routing rule, or add a validator. Such a write changes the [behavior-determining organization](./definitions/behavior-determining-organization.md): retained structure that can shape later behavior. But a write is only a candidate change. It becomes learning when a selection process makes it operative for later runs. That is the retention half of [a proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

The missing relation is therefore not mutation in general. It is a governed transformation from one session-start definition to a later one.

## Content placement is a revisable policy

Reusable content can occupy several places. A checklist can be rediscovered in each session, retained in a file and retrieved when needed, loaded at session start, or inlined into an always-loaded prompt. A convention can remain a parametric prior, become a retrieved note, or be enforced by a validator.

These choices vary along separate axes. Retention creates a maintenance obligation but can prevent rediscovery. Loading policy determines whether retained content spends context on every run or only when retrieved. Session-local derivation avoids storage and maintenance, but incurs computation whenever the content is needed. Durable does not mean always loaded, and session-local does not mean free.

The allocation can change after deployment. [Frontloading](./frontloading-spares-execution-context.md) moves work whose inputs are already known into reusable starting structure. [Ephemeral computation](./ephemeral-computation-prevents-accumulation.md) leaves work local when reuse would not repay maintenance. [Promotion](./promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) supplies criteria for moving a candidate into a durable form or loading path. A fixed class/instance shorthand tends to hide this policy decision, even when the implementation language can express the move.

## Session-loaded material can carry episode-scoped authority

Content placement matters because material loaded during a session can still direct behavior. In an LLM-based agent, an instruction read mid-session can alter the procedure the model follows even if it was absent from the starting prompt. System roles, position, and harness rules may give some inputs structural priority, but the material assembled into context still shapes behavior. The relevant runtime property is interpreter-like consumption: session data can function as instructions, not only as parameters selected by fixed dispatch.

This does not make every piece of transient context a [system-definition artifact](./definitions/system-definition-artifact.md). That term is reserved for retained material consumed with binding instructional, configuration, routing, validation, evaluation, or learning force. Transient material can instead carry behavioral authority within the episode. It is [operative](./definitions/operative-change.md) over that horizon when a consumer and channel let it affect subsequent behavior, even though it determines nothing after the session ends.

Agent warm-up provides an anecdotal signal. A coding agent often becomes more effective after exploring a project's layout, conventions, and constraints. Ordinary accumulation of session-local state can explain this improvement, so warm-up does not refute the class/instance analogy. It does show that the durable starting definition may omit useful context. If later sessions repeatedly reconstruct the same material, that recurrence is evidence for considering promotion. Task-specific findings remain correctly session-local.

## Cross-session learning requires two relations

The analogy remains useful for session startup. Sessions are disposable, begin from shared durable structure, and lack the tacit navigational familiarity of a returning human developer. That is why [routing stays architectural rather than learned](./agent-statelessness-makes-routing-architectural-not-learned.md) within a fresh run.

But a complete model needs two relations. Instantiation maps a durable definition to a session with starting context. Cross-session learning maps the current definition, session experience, and a selection result to a revised definition. That revision can change both the retained content and the boundary between retrieved, always-loaded, and locally derived material.

Read through the idealization, the paradigm does not merely lack the second relation — it contains a fenced version of it. Where class-based systems support definition change at runtime, they separate it into a meta level with its own protocol: a metaobject protocol makes class mutation a distinct, governed kind of act rather than ordinary execution, and production systems treat class change as deployment, with versioned upgrades and migration callbacks such as Smalltalk changesets and Erlang's `code_change`. That is established vocabulary for a governed transformation between definition versions. What an LLM-based agent lacks is the enforcement, not the concept: a session edits a skill file through the same interface it uses for ordinary work, so no runtime marks the crossing from base-level work to definition change. The fence has to be rebuilt in process — write permissions, review gates, versioned retention — which is what [a proposal-selection loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) over retained artifacts amounts to.

The Machine Studying practitioner report gives one version of this distinction. It defines an agent as `(model, harness)` and a studying algorithm as a map from an agent and a corpus to a changed agent. This formulation describes transformation between agent definitions, not instantiation from an unchanged definition. Its preliminary cheatsheet result is a bounded example: a study pass writes a reusable repository map, and the measured gain is concentrated at inference budgets where an unprepared session cannot afford equivalent exploration.

Using the startup analogy as a learning model therefore invites three design mistakes:

- **Treating the startup definition as authored-only.** This excludes session-produced proposals from the improvement loop by assumption.
- **Treating session state as mere scratch.** This discards evidence about what the durable definition failed to supply, including recurring warm-up work.
- **Treating content placement as fixed.** This prevents frontloading, retrieval policy, and promotion from being evaluated as revisable decisions.

## Scope

- Selected write-back requires a deployment where sessions or operators can change definition-side artifacts. A locked-down deployment with read-only skills and operator-only configuration remains close to the immutable class/instance shorthand.
- Episode-scoped behavioral authority is argued directly for LLM-style, context-mediated runtimes. It transfers to other agents only when their runtime can interpret session-provided material as behavior rather than enforcing a closed repertoire through typed state or dispatch.
- Not every placement is open. The user's current question, working file set, and run-specific intermediate results are genuinely session-local. The claim concerns reusable content whose placement is a real design choice.
- The note does not decide where a particular item should sit. That depends on rediscovery cost, activation reliability, retrieval policy, context cost, and maintenance burden.
- Where a session ends can vary under compaction, resumption, and sub-agent spawning. This note assumes a settled session boundary rather than deriving one.

## Open Questions

- Metaobject protocols and versioned hot code swap supply established vocabulary for governed definition change. How much of their machinery transfers to a runtime that cannot enforce the base/meta fence — where any session write is potentially a definition change — is open.
- What is the natural unit of placement? Systems often move whole files, while the reusable unit may be a claim, rule, or procedure.

---

Relevant Notes:

- [Domain pricing routes an exception to idealization assessment but does not decide it](./domain-pricing-routes-an-exception-to-idealization-assessment.md) — grounds: supplies the two-stage criterion under which this note's reflective counterexamples are routed to idealization assessment; the pricing is carried here, the adequacy record is still open
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why a correction outside the chosen update surface cannot be reached by optimizing within it
- [Orchestration strategies and run state have opposite persistence requirements](./orchestration-strategies-and-run-state-have-opposite-persistence.md) — extends: applies the retained-versus-episode distinction to schedulers and run state
- [Machine Studying](../sources/machine-studying.ingest.md) — evidenced-by: supplies the changed-agent formulation and the bounded low-budget cheatsheet result
