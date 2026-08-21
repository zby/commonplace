---
description: Artifact analysis records retained behavior-shaping artifacts by storage substrate, representational form, lineage, and behavioral authority so review evidence, invalidation, and rollback follow how artifacts actually act
type: kb/types/note.md
traits: [has-comparison, has-external-sources]
tags: [learning-theory, artifact-analysis]
---

# Axes of artifact analysis

A recurring comparison in this KB used to pit "repo artifacts vs weights": one system stores learned behaviour as files, another as model parameters. That contrast packs together questions that need to stay separate. A retained lesson can live in a repository, database, vector store, prompt registry, configuration service, or checkpoint store; it can act as natural-language content, symbolic control, or distributed-parametric state; it can be canonical source or a derived view; and it can advise, instruct, enforce, rank, validate, or train.

The useful unit is therefore not always the stored object. It is the **operative part or consumption path**: the behavior-shaping part of a [retained artifact](./definitions/retained-artifact.md) and the route through which a future consumer can use it. The same Markdown file can be low-priority evidence in one path, high-priority instruction in another, and archival provenance in a third. The bytes did not change; the behavioral authority did.

Artifact analysis records four fields:

| Field | Question | Why it matters |
|---|---|---|
| [Storage substrate](./definitions/storage-substrate.md) | Where does retained state persist? | Access, deletion, versioning, deployment, latency, and rollback paths |
| [Representational form](./definitions/representational-form.md) | How is the operative part encoded and consumed? | Default review evidence: reading, tests/static checks, or behavioral probes |
| [Lineage](./definitions/lineage.md) | What sources or derivations does this retained behavior depend on? | Invalidation, regeneration, source alignment, and retirement |
| [Behavioral authority](./definitions/behavioral-authority.md) | Who consumes it, through which channel, and with what force? | Security, precedence, activation, scope, and behavioral consequence |

These fields replace the older shorthand of **class/backend/role**. Backend becomes storage substrate. Class becomes representational form. Source relation becomes lineage. Role and control path become behavioral authority. The replacement is not cosmetic: the new names force the record to say what the artifact's operative part is, which consumption path gives it force, and what evidence would actually review it.

## Representational form

Representational form is the main replacement for the old opaque/natural-language/symbolic class axis.

- **Natural-language** operative parts carry behavior-shaping content interpreted by a model or human: notes, prompts, memory entries, reflections, rules, policies, playbooks, workflow descriptions, and many skills. They are readable and diffable, but their effect varies with context, prompt position, retrieval order, and model behavior.
- **Symbolic** artifacts carry behavior-shaping content in localized units whose consequences are assigned by a parser, interpreter, runtime, validator, schema, route table, or other defined consumer. Tests, scripts, schemas, route tables, typed records, and deterministic validators are symbolic where that consumer gives fields or operations defined consequences.
- **Distributed-parametric** artifacts carry behavior-shaping content in numerical state distributed across parameters or dense representations: model checkpoints, adapters, embedding spaces, dense-vector indexes, reward models, learned controllers, and learned memory-management policies.

The term **opaque** should now be used for practical inspectability, not as the form name. Distributed-parametric artifacts become opaque at very small scales because their behavior is not localized in readable units. Natural-language and symbolic systems can also become practically opaque at sufficient scale, as [opacity is a scale threshold, not a class property](./opacity-is-a-scale-threshold.md) argues.

The natural-language/symbolic boundary is the phase transition [codification](./definitions/codification.md) crosses and [constraining](./definitions/constraining.md) often aims toward: the medium changes, the consumer changes, and the verification regime changes. Intermediate cases - typed natural-language content, schema-validated Markdown, prompts with required sections - are mixed artifacts. Classify the operative parts separately: natural-language content for interpretation, symbolic structure for validation or assembly.

## Storage substrate

Storage substrate records where retained state persists: repo files, database rows, service-managed objects, graph stores, vector stores with attached records, prompt registries, runtime configuration, audit logs, or model-artifact stores. Substrate is operationally important because it determines permissions, deletion, versioning, rollback, deployment, and latency.

Substrate is not representational form. A repository may contain natural-language workflows, symbolic validators, generated prompt views, route tables, and pointers to checkpoints. A vector store may package natural-language records together with distributed-parametric embeddings and ranking behavior. [Cognee](../agent-memory-systems/reviews/cognee.md) keeps natural-language records in a database-backed poly-store; the substrate changed, the natural-language form did not.

## Lineage

Lineage records whether retained behavior is source material, canonical source, derived view, generated index, compiled artifact, assembled package, learned update, or archival evidence, and what source changes should invalidate or refresh it.

Lineage is separate from substrate and form. A natural-language workflow may be canonical in a repo file, summarized into a prompt view, and compiled into a symbolic validator. A generated directory index may be a derived view over canonical notes. A model checkpoint may be a distributed-parametric learned update derived from trace records and reward signals. The question is whether the system can tell what the derived artifact depends on, when it should refresh, what form change occurred, and what authority it carries relative to its sources.

Derived artifacts are useful because they put material where it can act, but they introduce drift. A workflow can be revised while an old skill manifest still routes tasks to the old procedure. A prompt summary can omit an exception from the canonical policy. These are lineage failures, not merely stale-memory failures.

## Behavioral authority

Behavioral authority records the consumer, channel, and force of a retained artifact's use.

| Part | Question | Examples |
|---|---|---|
| Consumer | Who or what uses it? | Acting agent, retriever, context scheduler, planner, runtime service, validator, router, view assembler, reviewer, maintainer, learning loop |
| Channel | How does it reach the consumer? | Retrieval, prompt assembly, explicit invocation, execution, configuration, validation, routing, ranking, review, training |
| Force | What kind of behavioral effect can it have? | Advice, instruction, enforcement, selection or ranking influence, audit trigger, learning input |

This field replaces the old role axis. A [knowledge artifact](./definitions/knowledge-artifact.md) is consumed as evidence, reference, context, explanation, or advice that a future agent or human may weigh. A [system-definition artifact](./definitions/system-definition-artifact.md) is consumed with instruction, enforcement, routing, validation, configuration, evaluation, memory-operation, or learning force. These are useful authority-path shorthands, but the architectural record should name the actual consumer, channel, and force.

The distinction is not between intrinsic artifact types. A Markdown file of domain terms is a knowledge artifact when retrieved as reference and a system-definition artifact when loaded as standing instruction. A schema is a knowledge artifact when read as documentation and a system-definition artifact when an interpreter uses it to validate inputs. Model weights can encode stored associations and learned policy in the same parameters. The [homoiconic context](./llm-context-interprets-instructions-and-content-through-one-medium.md) is what makes the natural-language authority switch possible without changing the stored bytes.

Authority is use-specific and can diverge from declared intent. A nominally advisory memory can dominate behavior if it is always included, placed late in a prompt, repeated often, or phrased imperatively. A formally authoritative rule can have little effect if no acting component loads it. Record both assigned authority and evidence of effective authority when that distinction matters.

## Eligibility and scope

Eligibility is not one of the four core fields in the paper's compact record, but it remains useful local policy metadata for memory systems. It asks whether a specific use is currently allowed: candidate, active, superseded, deprecated, retired, or archival. Scope records where the use applies: user, project, repository, organization, deployment, task class, benchmark, or runtime stage.

These attach to the consumption path. A note can be current as an artifact while one high-authority use of it is deprecated. A workflow can be active for manual reviewer use while still candidate for runtime enforcement.

## Why the fields matter

Each field blocks a different category mistake.

- **Substrate does not decide form, lineage, or authority.** [Canonical files may defer a shared schema while database authority remains a separate commitment](./files-defer-centralized-schema-commitment-until-invariants-stabilize.md) uses file-backed state to analyze schema timing, then separates that timing choice from where state persists and which record governs. Moving a representation into a database neither changes its form automatically nor makes it canonical.
- **Form, not storage label.** Comparing trajectory-informed memory tips to AgeMem policy weights is not "tips vs weights" but natural-language form vs distributed-parametric form. Tips are one natural-language package; weights are one distributed-parametric package.
- **Lineage, not co-location.** A generated prompt view and its source notes may both live in repo files. The risk is not that the substrate differs, but that the derived view drifts from the canonical source while retaining high authority.
- **Authority, not object identity.** "Knowledge artifact" and "system-definition artifact" are useful shorthands for authority families, but the precise claim is that an operative part is being consumed with a named force. A reflection retrieved as evidence and the same reflection loaded as standing instruction have different authority.
- **Eligibility, not existence.** A memory, validator, prompt summary, or skill package can exist without being eligible for a given future use. "Stored" does not mean "active"; "current" does not mean "safe to enforce."
- **Learning is not decided by authority.** Both advice-like knowledge-artifact use and high-authority system-definition-artifact use are [learning](./learning-is-not-only-about-generality.md) by Simon's capacity-change test. The field separates what durable change affects, not whether it counts.

## Examples

| Example | Storage substrate / lineage | Representational form | Behavioral authority |
|---|---|---|---|
| AgeMem memory policy | Model-artifact store; learned update from memory-operation trajectories | Distributed-parametric learned controller | Learning loop or controller selects memory operations |
| Trajectory-informed memory | Memory store, DB, or file; derived from completed trajectories | Natural-language tips | Retrieved or loaded as task advice |
| Commonplace notes | Repo; canonical library artifacts or derived notes from workshops/sources | Natural-language content, with symbolic frontmatter where validators consume it | Retrieved as knowledge, loaded as guidance, or validated as typed artifacts depending on path |
| Commonplace skills | Repo / skill directory; derived from methodology notes | Mixed natural-language instructions, symbolic metadata, optional scripts | Invoked procedure with routing and execution policy |
| Commonplace validators | Repo / installed package; codified from conventions | Symbolic Python checks | Advisory or enforcing validation depending on command or hook |
| Generated directory index | Repo; derived view over directory contents | Structured Markdown: natural-language labels plus symbolic frontmatter | Navigation aid; should refresh when sources change |
| RAG corpus | Vector store; canonical or derived depending on ingestion | Natural-language records plus distributed-parametric embedding/ranking path | Retriever/ranker influences selection; selected records advise the model |
| Intern-S2-Mobius checkpoint | Model-artifact store; learned update with paper-reported conversion and training lineage | Distributed-parametric shared routed experts and layer-local token mixers and experts | Hidden-state routing selects shared experts; decoder traversal and residual integration give the selected parameters behavioral force |

The [code-grounded Mobius ingest](../sources/intern-s2-mobius-arxiv-v1.ingest.md) makes the checkpoint a bounded same-form role-separation case. In the inspected release, each decoder layer is assigned to one of four default shared MoE blocks by layer index; a learned top-k router selects eight of 256 experts by default, and the routed output is combined with a per-layer shared expert. The paper calls the shared FFN pools Memory and the attention or linear-attention stages Reasoners. These labels mark different architectural roles and authority paths, but both operative parts remain distributed-parametric. The split therefore does not supply localized-artifact governance: it does not create readable claims with claim-level provenance, selective invalidation, or selective rollback. Static inspection establishes the routing mechanism, not the paper's efficiency, latent-reasoning, self-evolution, or semantic-memory claims.

## Consequences for memory design

Memory design adds operational policies on top of this artifact analysis: capture, derivation, activation, authority assignment, lifecycle, and evaluation. Those policies should attach to operative parts and consumption paths. The question is not simply "what memory exists?" but "which retained artifact can be used how, with what authority, in which scope, and under what eligibility state?"

That shift explains why memory labels are too coarse. A retained lesson can become a prompt patch, workflow, script, validator, route, derived prompt view, retrieval index, learned controller, or checkpoint. Those differ in storage substrate, representational form, lineage, and authority: read, loaded, invoked, executed, enforced, routed through, assembled, audited, ranked, or used as training input.

---

Relevant Notes:

- [Continual learning requires governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md) - applies: the older role axis becomes behavioral authority over a consumption path
- [codification](./definitions/codification.md) - defines the phase transition from natural-language into symbolic form
- [constraining](./definitions/constraining.md) - mechanism that operates across natural-language artifacts and reaches symbolic artifacts at its far end
- [LLM contexts interpret instructions and content through the same token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md) - mechanism: lets the same natural-language content function as a knowledge artifact or system-definition artifact depending on authority path
- [deploy-time learning](./retained-artifacts-enable-persistent-deployment-time-adaptation.md) - applies: deploy-time learning is timing-defined and can land in natural-language, symbolic, or distributed-parametric forms
- [treat continual learning as representational-form coevolution](./treat-continual-learning-as-representational-form-coevolution.md) - extends: builds on the natural-language/symbolic/distributed-parametric split to ask how improvement loops should relate
- [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) - extends: system-definition artifacts split into heuristic crystallized reasoning and authority-bearing constraints
- [Memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) - extends: memory operational policies should attach to operative parts and consumption paths
- [trace-learning techniques in related systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) - grounds: surveyed systems distinguish promotion targets and future uses that span these fields
- [Canonical files may defer a shared schema while database authority remains a separate commitment](./files-defer-centralized-schema-commitment-until-invariants-stabilize.md) - sharpens: centralized-schema timing, storage substrate, lineage, and authority are separate decisions
- [inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) - grounds: readability is shared by natural-language and symbolic forms
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) - contrasts: AgeMem is a distributed-parametric policy case that makes form and authority visible
- [Cognee](../agent-memory-systems/reviews/cognee.md) - counterexample: database-backed natural-language artifacts show that files are not the only substrate
- [learning is not only about generality](./learning-is-not-only-about-generality.md) - grounds: Simon's capacity-change test catches both advice-like and high-authority uses
