---
description: Artifact analysis has three axes — two structural (class, backend) and one relational (role); conflating them blurs comparisons and hides missing cells
type: kb/types/note.md
traits: [has-comparison]
tags: [learning-theory]
status: current
---

# Axes of artifact analysis

A recurring comparison in this KB used to pit "repo artifacts vs weights" — one system stores learned behaviour as repo files, the other as model parameters. That contrast packs three axes: **class** (opaque, prose, or symbolic), **backend** (where units live), and **role** (how the consumer reads the object). Every case where two systems agree on one axis but split on the others vanishes into the one-axis framing.

Class and backend are **structural** — properties of the stored object. Role is **relational**: the same bytes can play either part depending on who reads them.

**Artifact class** — how the learned result is represented. Three options:

- **Opaque** artifacts live in model weights or other hidden state, consumed by the model itself and not readable as discrete units. AgeMem and [OpenClaw-RL](https://arxiv.org/html/2603.10165v1) are clean examples.
- **Prose** artifacts are discrete natural-language objects — notes, memory entries, reflections, rules, prompts, playbooks — consumed by an LLM interpreting [underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md); readable and diffable, but semantics are underspecified. Because prose lacks interpreter-enforced scoping, each prose invocation also carries a consumption-frame choice — flat (parent context) or bounded (sub-agent) — treated as a prose-specific axis in [llm context is composed without scoping](./llm-context-is-composed-without-scoping.md).
- **Symbolic** artifacts have formal semantics — schemas, tests, scripts, tools, types — consumed by a deterministic interpreter; readable, diffable, *and* exactly verifiable.

Prose and symbolic together form the **readable** artifacts. The split runs across two sub-axes: opaque vs. readable, and (within readable) informal vs. formal semantics. The prose/symbolic boundary is the phase transition [codification](./definitions/codification.md) crosses and [constraining](./definitions/constraining.md) aims for — medium changes (markdown → code), consumer changes (LLM → interpreter), verification regime changes (underspecified → formal). Intermediate cases — typed prose, schema-validated markdown, prompts with strict templates — sit *on* the boundary: a formal layer wraps prose content, so the same artifact gets read formally for shape and informally for substance.

The opaque/readable line isn't a hard categorical split: [any class becomes practically opaque at sufficient scale](./opacity-is-a-scale-threshold.md), just at different thresholds.

Within each class, artifacts take different **forms**: prose forms include memory entries, reflections, ranked memories, and playbook entries; symbolic forms include schemas, tests, runnable scripts, and extracted tools. Form matters when two systems share class, backend, and role but diverge on lifecycle and retrieval — ranked memories and playbook entries are both prose, both file-or-DB-backed, both system-definition, yet the consumer pulls one by relevance versus reading the whole set in order.

**Backend** — where units live: repo files, database rows, service-managed memory objects, graph stores, or vector stores with attached records and provenance. An artifact class says nothing about backend. Prose and symbolic artifacts can live in any of the above — "repo artifacts" is too narrow an umbrella. [Cognee](../agent-memory-systems/reviews/cognee.md) keeps prose-class units in a database-backed poly-store; the backend changed, the class did not.

**Role** — how the consumer reads the object. Two options:

- **Knowledge role** — consumed as fact. Durable writes grow the system's reach, not its disposition. Databases, RAG corpora, vector stores of retrieved facts, user profiles.
- **System-definition role** — consumed as policy. Durable writes change what the system does. Prompts, tips, notes, schemas, tools, tests; also model weights when they encode learned policy.

Role depends on the consumer, not the bytes. A markdown file of domain terms is **knowledge** when retrieved as reference, **system-definition** when loaded as an instruction. A schema is **knowledge** when it describes a data structure, **system-definition** when an interpreter uses it to validate inputs. Model weights encode both — stored associations (knowledge-like) and learned policy (system-definition) — in the same parameters. The [homoiconic context](./llm-context-is-a-homoiconic-medium.md) is what makes the switch possible without changing the stored bytes.

## Why the axes matter

Each axis blocks a specific category mistake: class confusions ("readable artifacts vs weights"), backend confusions ("repo artifacts" as an umbrella), and role confusions ("learning = adding RAG"). The recurring examples across this KB:

- **Backend, not class.** [Files beat a database for agent-operated knowledge bases](./files-not-database.md) argues that a database schema forces premature commitment to access patterns — a claim about which backend to pick, not which artifact class to use. Files can beat a database for a young KB without implying anything about the prose/symbolic boundary.
- **Name the class, not the form.** Comparing [trajectory-informed memory generation](https://arxiv.org/html/2603.10600v1) — whose learned result is short natural-language entries the paper calls *tips* — to [AgeMem](./memory-management-policy-is-learnable-but-oracle-dependent.md) is not "tips vs weights" but **prose artifact vs opaque artifact**. Tips are one prose form; weights are an opaque class — the right contrast is class-to-class.
- **One concept can span all three classes.** [Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) is defined by *when* the system updates, not what it updates — so it shows up in all three classes. Fine-tuning and LoRA do it in the opaque class; commonplace's version stays on the readable artifacts, with prose dominating day-to-day and [codification](./definitions/codification.md) as the move to symbolic. Treating "deploy-time learning" as synonymous with weight updates is a class assumption smuggled in.
- **Role is orthogonal to class.** AgeMem's shorthand "facts in store, policy in weights" bundles role (knowledge vs system-definition) with class (prose vs opaque). The two line up in this design but don't have to — a different system could put the policy in prose, or carry both roles on the same class. [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) applies the axis: the readable system-definition side is the open half of continual learning, and "adding RAG is learning" holds only for the knowledge role.
- **But role doesn't decide what counts as learning.** Both roles are [learning](./learning-is-not-only-about-generality.md) by Simon's capacity-change test — knowledge writes grow reach, system-definition writes change disposition. The axis separates what a durable write changes, not whether change counts.

The taxonomy that falls out:

| Example | Artifact class | Backend | Artifact form | Role |
|---|---|---|---|---|
| AgeMem memory policy | Opaque | Model weights | Learned policy | System-definition |
| Trajectory-informed memory | Prose | Memory store / DB / files | Tips | System-definition |
| Commonplace notes, skills, prompts | Prose | Repo | Notes, rules, playbooks | System-definition |
| Commonplace codified procedures | Symbolic | Repo | Schemas, tests, scripts, tools | System-definition |
| RAG reference corpus | Prose | Vector store | Documents | Knowledge |

---

Relevant Notes:

- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — applies: uses the role axis to argue that readable system-definition artifacts are the cheap, under-addressed half of continual learning
- [codification](./definitions/codification.md) — defines the phase transition between prose and symbolic artifacts
- [constraining](./definitions/constraining.md) — the mechanism that operates across prose artifacts and reaches symbolic artifacts at its far end
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: lets the same content play either role
- [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) — applies: deploy-time learning is timing-defined and lands in all three artifact classes (fine-tuning in opaque, commonplace in prose+symbolic)
- [treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: builds on the opaque/prose/symbolic split to ask how the three improvement loops should relate
- [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md) — explains: the role axis exists because context/compute is bounded; under unbounded context most system-definition collapses into knowledge, but codified symbolic artifacts survive
- [trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — grounds: surveyed systems distinguish promotion targets that span these axes
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — sharpens: backend choice is downstream of class choice
- [inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: readability is shared by both non-opaque artifact classes
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is a clean opaque case that makes the role axis visible
- [Cognee](../agent-memory-systems/reviews/cognee.md) — counterexample: database-backed prose artifacts show that files are not the only backend
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: Simon's capacity-change test catches both roles — knowledge writes grow reach, system-definition writes change disposition
