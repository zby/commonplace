---
description: Substrate analysis has four axes — three structural (class, backend, form) and one relational (role); conflating them blurs comparisons and hides missing cells
type: kb/types/note.md
traits: [has-comparison]
tags: [learning-theory]
status: current
---

# Axes of substrate analysis

A recurring comparison in this KB pits "readable artifacts vs weights" — one system stores learned behaviour as readable units (notes, rules, schemas), the other as model parameters. The contrast feels like one axis but isn't. Substrates differ in *representation* (readable vs distributed weights), but they also differ in where they're stored, what a unit looks like, and how a consumer reads them. Collapsing all four into one axis loses every case where two systems share representation but split on the rest.

Agent-learning comparisons turn on four axes. Three are **structural** — properties of the stored object:

- **Substrate class** — how the learned result is represented: as non-interpretable distributed state (**opaque**), as natural-language units (**prose**), or as formal-semantic units (**symbolic**). Prose and symbolic together form the **readable** substrates — the non-opaque side.
- **Backend** — where units live (repo files, database rows, memory services).
- **Artifact form** — what a unit looks like within a substrate (memory entries, rules, schemas, scripts).

The fourth is **relational** — how a consumer reads the object:

- **Role** — whether the artifact is consumed as fact (**knowledge substrate**) or as policy (**system-definition artifact**).

Mixing the axes blurs comparison space. You argue "memory entries vs weights" when the real contrast is across substrate classes. You treat "repo artifacts" as an umbrella when it's one backend among many. You collapse artifact form into substrate, missing that two prose systems can differ on whether a unit is a memory entry or a playbook step. You ask whether an artifact "is" knowledge or "is" policy as if role were a property of the bytes, when it's a property of how the consumer reads them — the same file can be either.

## Substrate class

The three substrate classes differ in representation, consumer, and semantics:

- **Opaque substrate** (the non-interpretable case) — the learned result lives in model weights or other hidden state; consumed by the model itself, not readable as discrete units. AgeMem and [OpenClaw-RL](../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) are clean examples.
- **Prose substrate** — the learned result lives in discrete *natural-language* objects — notes, memory entries, reflections, rules, prompts, playbooks. Consumed by an LLM interpreting [underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md). Readable and diffable, but semantics are underspecified.
- **Symbolic substrate** — the learned result lives in discrete objects with **formal semantics** — schemas, tests, scripts, tools, types. Consumed by a deterministic interpreter. Readable, diffable, *and* exactly verifiable.

The split sits across two sub-axes: opaque vs. readable, and (within readable) informal vs. formal semantics. The prose/symbolic boundary is the phase transition [codification](./definitions/codification.md) crosses and [constraining](./definitions/constraining.md) aims for — medium changes (markdown → code), consumer changes (LLM → interpreter), verification regime changes (underspecified → formal). Intermediate cases — typed prose, schema-validated markdown, prompts with strict templates — sit *on* the boundary: a formal layer wraps prose content, so the same artifact gets read formally for shape and informally for substance.

Opacity isn't binary — any substrate becomes practically opaque at sufficient scale. What distinguishes substrates is the scale at which they cross that threshold. Distributed representations cross almost immediately: meaning is smeared across many weights jointly, so even a modestly-sized network resists per-unit inspection. Truly tiny networks can be read by hand (mechanistic interpretability on toy models does this), but the threshold is very low. Localized substrates stay readable at much larger aggregates — per-unit readability plus search, diffing, and modular revision let you work with scales that would be hopeless in a weight matrix of comparable size.

## Backend

A substrate class says nothing about storage. Prose and symbolic artifacts both live in many backends — repo files, database rows, service-managed memory objects, graph stores, or vector stores with attached records and provenance. This is why "repo artifacts" is too narrow as the umbrella term. Repo-hosted markdown is one important backend, especially for commonplace, but neither substrate is tied to it. [Cognee](../agent-memory-systems/reviews/cognee.md) keeps prose-substrate units in a database-backed poly-store; the backend changed, the substrate class did not.

## Artifact form

Artifact form is the residual axis: once substrate and backend are fixed, what kind of unit is it? Prose-substrate forms include memory entries, reflections, ranked memories, and playbook entries, differing in granularity, retrieval mode, and how directly they constrain later behaviour. Symbolic-substrate forms include schemas, tests, runnable scripts, and extracted tools. Form bites when two systems share the other three axes but diverge on lifecycle and retrieval. Ranked memories and playbook entries are both prose, both file-or-DB-backed, both system-definition — but the consumer pulls one by relevance versus reading the whole set in order. Form is largely orthogonal to backend — you can push code into a database or memory entries into a repo — though backends differ in their affordances for each form.

## Role

The role axis is **relational**, not structural: it describes how a consumer reads the object, so the same bytes can play either part.

- **Knowledge substrate** — consumed as fact. The policy that reads it is defined elsewhere and is unchanged by writes. Durable writes grow the system's reach, not its disposition. Databases, RAG corpora, vector stores of retrieved facts, user profiles.
- **System-definition artifact** — consumed as policy. Reading the artifact *is* (part of) the disposition. Durable writes change what the system does next session. Prompts, tips, notes, schemas, tools, tests; also model weights when they encode learned policy.

Both satisfy [Simon's capacity-change definition of learning](./learning-is-not-only-about-generality.md); they differ in what a durable write changes. The same bytes can play either role depending on the consumer:

- A markdown file of domain terms is **knowledge** when retrieved as reference, **system-definition** when loaded as an instruction.
- A schema is **knowledge** when it describes a data structure, **system-definition** when an interpreter uses it to validate inputs.
- Model weights encode both stored associations (knowledge-like) and learned policy (system-definition) in the same parameters.

Any cell in the structural 3-axis grid can host either role; the structural axes don't determine it, the consumer does. The [homoiconic context](./llm-context-is-a-homoiconic-medium.md) is what makes the switch possible without changing the stored bytes.

## Why the axes matter

Each axis blocks a specific category mistake: substrate-class confusions ("readable artifacts vs weights"), backend confusions ("repo artifacts" as an umbrella), form-vs-substrate slippage, and role confusions ("learning = adding RAG"). The recurring examples across this KB:

- **Backend, not substrate.** [Files beat a database for agent-operated knowledge bases](./files-not-database.md) argues that a database schema forces premature commitment to access patterns — a claim about which backend to pick, not which substrate class to use. Files can beat a database for a young KB without implying anything about the prose/symbolic boundary.
- **Substrate, not artifact form.** Comparing [trajectory-informed memory generation](../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) — whose learned result is short natural-language entries the paper calls *tips* — to [AgeMem](./memory-management-policy-is-learnable-but-oracle-dependent.md) is not "tips vs weights" but **prose substrate vs opaque substrate**. Tips are one artifact form on the prose side.
- **One concept can span all three substrate classes.** [Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) is defined by *when* the system updates, not what it updates — so it shows up in all three classes. Fine-tuning and LoRA do it in the opaque substrate; commonplace's version stays on the readable substrates, with prose dominating day-to-day and [codification](./definitions/codification.md) as the move to symbolic. Treating "deploy-time learning" as synonymous with weight updates is a substrate-class assumption smuggled in.
- **Role is orthogonal to substrate.** AgeMem keeps remembered facts in a memory store and learns a memory-management policy in model weights. The shorthand "facts in store, policy in weights" bundles two axes at once — role (knowledge vs system-definition) and structural substrate (prose vs opaque) — that happen to line up in this design but don't have to: a different system could put the policy in prose, or carry both roles on the same substrate. [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) applies the axis directly: the readable system-definition side is the open half of continual learning, and "adding RAG is learning" is true only for the knowledge role.

The taxonomy that falls out:

| Example | Substrate class | Backend | Artifact form | Role |
|---|---|---|---|---|
| AgeMem memory policy | Opaque | Model weights | Learned policy | System-definition |
| Trajectory-informed memory | Prose | Memory store / DB / files | Tips | System-definition |
| Commonplace notes, skills, prompts | Prose | Repo | Notes, rules, playbooks | System-definition |
| Commonplace codified procedures | Symbolic | Repo | Schemas, tests, scripts, tools | System-definition |
| RAG reference corpus | Prose | Vector store | Documents | Knowledge |

With the axes separated, substrate trade-offs become easier to state. Opaque learning buys tighter optimisation at the cost of per-unit inspection. Prose learning recovers readability, diffability, and composability but keeps underspecified semantics and leans on retrieval and lifecycle design. Symbolic learning adds formal semantics — exact verification, deterministic execution — at the cost of needing a strong enough oracle to commit to one interpretation. Across all three, the role axis decides whether durable writes grow reach (knowledge) or change disposition (system-definition).

---

Relevant Notes:

- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — applies: uses the role axis to argue that readable system-definition artifacts are the cheap, under-addressed half of continual learning
- [codification](./definitions/codification.md) — defines the phase transition between prose and symbolic substrates
- [constraining](./definitions/constraining.md) — the mechanism that operates across prose substrate and reaches symbolic substrate at its far end
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: lets the same content play either role
- [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) — applies: deploy-time learning is timing-defined and lands in all three substrate classes (fine-tuning in opaque, commonplace in prose+symbolic)
- [treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: builds on the opaque/prose/symbolic split to ask how the three improvement loops should relate
- [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md) — explains: the role axis exists because context/compute is bounded; under unbounded context most system-definition collapses into knowledge, but codified symbolic artifacts survive
- [trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — grounds: surveyed systems distinguish promotion targets that span these axes
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — sharpens: backend choice is downstream of substrate choice
- [inspectable substrate, not supervision, defeats the blackbox problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — grounds: readability is shared by both non-opaque substrates
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is a clean opaque case that makes the role axis visible
- [Cognee](../agent-memory-systems/reviews/cognee.md) — counterexample: database-backed prose artifacts show that files are not the only backend
