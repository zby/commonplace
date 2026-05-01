---
description: Artifact analysis separates retained artifact properties from future-use properties; class, backend, form, source relation, control path, authority, scope, and eligibility jointly determine how retained adaptation changes behavior
type: kb/types/note.md
traits: [has-comparison]
tags: [learning-theory]
status: current
---

# Axes of artifact analysis

A recurring comparison in this KB used to pit "repo artifacts vs weights" — one system stores learned behaviour as repo files, the other as model parameters. That contrast packs several independent questions:

- what kind of retained object exists;
- where its persistent state lives;
- whether it is canonical or derived;
- how a future system can consume it;
- what authority that use has;
- whether that use is currently eligible.

The useful unit is therefore not the artifact alone. It is the **artifact-use pairing**: a retained artifact plus the specific future use through which it can affect behavior. The same markdown file can be low-priority evidence in one pairing, high-priority instruction in another, and archival provenance in a third. The bytes did not change; the future use did.

This note separates artifact properties from future-use properties. Artifact properties describe the retained object. Future-use properties describe the route by which the object becomes consequential later.

| Layer | Axis | Question |
|---|---|---|
| Artifact | Class | Is the operative content opaque, prose, symbolic, or mixed? |
| Artifact | Backend | Where does persistent state live? |
| Artifact | Form | What concrete package or unit carries the content? |
| Artifact | Source relation | Is it canonical, derived, generated, summarized, compiled, or archival relative to other artifacts? |
| Future use | Control path | Who consumes it, what activates it, and how is it consumed? |
| Future use | Authority and scope | How strongly may this use shape behavior, and where does that authority apply? |
| Future use | Eligibility | Is this use candidate, active, superseded, deprecated, retired, or archival now? |

## Artifact Properties

**Artifact class** asks how the learned result is represented.

- **Opaque** artifacts live in model weights or other hidden state, consumed by the model or controller itself and not readable as discrete operational units. AgeMem and [OpenClaw-RL](https://arxiv.org/html/2603.10165v1) are clean examples.
- **Prose** artifacts are discrete natural-language objects — notes, memory entries, reflections, rules, prompts, playbooks — consumed by an LLM interpreting [underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md). They are readable and diffable, but their semantics are underspecified. Because prose lacks interpreter-enforced scoping, each prose use also carries a consumption-frame choice — flat parent context or bounded sub-agent — treated as a prose-specific axis in [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md).
- **Symbolic** artifacts have formal semantics — schemas, tests, scripts, tools, types, validators, route tables — consumed by a deterministic interpreter, runtime, or checker. They are readable, diffable, and exactly verifiable within the limits of their specification.

Prose and symbolic together form the **readable** artifacts. The split runs across two sub-axes: opaque vs readable, and within readable, informal vs formal semantics. The prose/symbolic boundary is the phase transition [codification](./definitions/codification.md) crosses and [constraining](./definitions/constraining.md) aims for: the medium changes, the consumer changes, and the verification regime changes. Intermediate cases — typed prose, schema-validated markdown, prompts with strict templates — sit on the boundary: a formal layer wraps prose content, so the same artifact is read formally for shape and informally for substance.

The opaque/readable line is not absolute. [Any representation becomes practically opaque at sufficient scale](./opacity-is-a-scale-threshold.md), just at different thresholds.

**Backend** asks where the artifact's persistent state lives: repo files, database rows, service-managed objects, graph stores, vector stores with attached records, prompt registries, runtime configuration, or model/policy weights. Artifact class says nothing about backend. Prose and symbolic artifacts can live in any of these. "Repo artifacts" is therefore too narrow an umbrella. [Cognee](../agent-memory-systems/reviews/cognee.md) keeps prose-class units in a database-backed poly-store; the backend changed, the class did not.

**Artifact form** asks what concrete unit or package carries the content. Prose forms include notes, memory entries, reflections, ranked memories, workflow descriptions, prompt fragments, and playbook entries. Symbolic forms include schemas, tests, validators, route tables, runnable scripts, extracted tools, and typed records. Opaque forms include checkpoints, adapters, learned controllers, and memory-management policies.

Form matters when two systems share class and backend but diverge in lifecycle and control path. Ranked memories and playbook entries are both prose and may both live in files or databases, but one may be retrieved by relevance while the other is read in order as a standing procedure.

**Source relation** asks whether the artifact is canonical or derived relative to other retained artifacts. Canonical artifacts are the source of truth for a fact, workflow, rule, policy, validator, or configuration. Derived artifacts are views assembled from one or more sources for a particular consumer or use: prompt summaries, skill bundles, manifests, generated indexes, route tables, client-specific loading files, or compiled validators.

Source relation is separate from backend and class. A prose workflow may be canonical in a repo file, summarized into a prompt view, and compiled into a symbolic validator. A generated index may be a derived view over canonical notes. A model checkpoint may be a derived opaque artifact produced from trace records and reward signals. The design question is whether the system can tell what the derived artifact depends on, when it should refresh, what form change occurred, and what authority it carries relative to its sources.

Derived artifacts are useful because they put material where it can act, but they introduce drift. A workflow can be revised while an old skill manifest still routes tasks to the old procedure. A prompt summary can omit an exception from the canonical policy. These are source-relation failures, not merely stale-memory failures.

## Future-Use Properties

Future-use properties describe how a retained artifact later affects a system. They are not intrinsic to the stored bytes.

**Control path** asks who consumes the artifact, what activates it, and how it is consumed.

| Part | Question | Examples |
|---|---|---|
| Consumer | Who or what uses it? | Acting agent, retriever, context scheduler, planner, runtime service, validator, router, view assembler, reviewer, maintainer, learning loop |
| Activation | What makes it relevant? | Retrieval, preloading, trigger match, scheduler selection, explicit invocation, service lookup, runtime enforcement, route selection, derived-view assembly |
| Consumption mode | How is it used? | Read, loaded, invoked, executed, enforced, inspected, reviewed, routed through, assembled into another view |

The old "role" axis belongs here. An artifact has **knowledge use** when it is consumed as evidence, context, or advice that a future agent or human may weigh. It has **system-definition use** when its use gives it authority over instructions, routing, execution, validation, evaluation, memory operations, or policy.

The distinction is not between two intrinsic artifact types. A markdown file of domain terms is knowledge when retrieved as reference and system definition when loaded as instruction. A schema is knowledge when read as documentation and system definition when an interpreter uses it to validate inputs. Model weights can encode stored associations and learned policy in the same parameters. The [homoiconic context](./llm-context-is-a-homoiconic-medium.md) is what makes the prose switch possible without changing the stored bytes.

**Authority and scope** ask how strongly a particular future use may shape behavior and where that use applies. A retrieved memory can be low-priority advice. A loaded instruction can outrank ordinary context. A validator can block writes. A route table can decide which skill or model is used. A learned controller can select retrieval, writing, deletion, or summarization operations.

Authority is use-specific and can diverge from declared intent. A nominally advisory memory can dominate behavior if it is always included, placed late in a prompt, repeated often, or phrased imperatively. A formally authoritative rule can have little effect if it is never surfaced to the component that acts. Future-use analysis should therefore record both assigned authority and evidence of effective authority.

Scope is also part of the use: user, project, repository, organization, deployment, task class, benchmark, or runtime stage. The same artifact may be active for one project, candidate for another, and archival for a third.

**Eligibility** asks whether this particular use is currently allowed.

| State | Meaning for a future use |
|---|---|
| Candidate | Persisted for review, testing, or possible activation; not eligible for ordinary activation except as marked evidence |
| Active | Approved for its stated use within defined authority and scope |
| Superseded | Replaced by a newer artifact or binding; retained for provenance but yields precedence |
| Deprecated | No longer recommended or trusted for ordinary use; blocked, down-ranked, warning-labeled, or explicit-access only |
| Retired | Removed from behavior-shaping use; retained only if needed for audit, rollback, or investigation |
| Archival | Preserved as historical evidence; not behavior-shaping by default |

This is different from a note's artifact-level `status`. A note can be current as an artifact while one high-authority use of it is deprecated. A workflow can be active for manual reviewer use while still candidate for runtime enforcement. Eligibility attaches to the artifact-use pairing.

## Why the Axes Matter

Each axis blocks a different category mistake.

- **Backend, not class.** [Files beat a database for agent-operated knowledge bases](./files-not-database.md) argues that a database schema forces premature commitment to access patterns. That is a backend claim, not a claim about whether artifacts should be prose, symbolic, or opaque.
- **Name the class, not the form.** Comparing [trajectory-informed memory generation](https://arxiv.org/html/2603.10600v1) — whose learned result is short natural-language entries the paper calls tips — to [AgeMem](./memory-management-policy-is-learnable-but-oracle-dependent.md) is not "tips vs weights" but prose artifact vs opaque artifact. Tips are one prose form; weights are an opaque class.
- **Separate object from use.** "System-definition artifact" is a useful shorthand, but the precise claim is that an artifact is being used as system definition. A reflection retrieved as evidence and the same reflection loaded as standing instruction have different control paths, authority, and eligibility.
- **One concept can span all classes.** [Deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) is defined by when the system updates, not what it updates. Fine-tuning and LoRA do it in opaque artifacts; commonplace does it through readable artifacts, with prose dominating day-to-day and codification moving some cases to symbolic.
- **Source relation is not backend.** A generated prompt view and its source notes may both live in repo files. The risk is not that the backend differs, but that the derived view drifts from the canonical source while retaining high-authority use.
- **Eligibility is not existence.** A memory, validator, prompt summary, or skill package can exist without being eligible for a given future use. "Stored" does not mean "active"; "current" does not mean "safe to enforce."
- **Learning is not decided by role.** Both knowledge use and system-definition use are [learning](./learning-is-not-only-about-generality.md) by Simon's capacity-change test. Knowledge writes grow reach. System-definition writes change disposition. The axis separates what durable change affects, not whether it counts.

The taxonomy that falls out:

| Example | Artifact class | Backend | Form | Source relation | Future use |
|---|---|---|---|---|---|
| AgeMem memory policy | Opaque | Model weights | Learned policy | Derived from memory-operation trajectories | Active learned controller for memory decisions |
| Trajectory-informed memory | Prose | Memory store / DB / files | Tips | Derived from completed trajectories | Retrieved or loaded as task advice |
| Commonplace notes | Prose | Repo | Notes | Canonical library artifacts | Retrieved as knowledge or loaded as guidance depending on route |
| Commonplace skills | Prose + symbolic package | Repo / skill directory | Instructions, metadata, optional scripts | Derived from methodology notes | Invoked as procedures with routing and execution policy |
| Commonplace validators | Symbolic | Repo / installed package | Python checks | Codified from conventions | Enforced or advisory checks depending on command/hook |
| Generated directory index | Prose / structured markdown | Repo | Index | Derived view over directory contents | Navigation aid; should refresh when sources change |
| RAG corpus | Prose | Vector store | Documents / chunks | Canonical or derived, depending on ingestion | Retrieved as knowledge |

## Consequences for Memory Design

Memory design adds operational policy axes on top of this artifact analysis: capture, derivation, activation, authority, lifecycle, and evaluation. Those policies should attach to artifact-use pairings. The question is not simply "what memory exists?" but "which retained artifact can be used how, with what authority, in which scope, and under what eligibility state?"

That shift explains why memory labels are too coarse. A retained lesson can become a prompt patch, workflow, script, validator, route, derived prompt view, learned controller, or checkpoint. Those differ not only in class and backend, but in future system use: read, loaded, invoked, executed, enforced, routed through, assembled, audited, or used to control another artifact.

---

Relevant Notes:

- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — applies: the old role axis becomes a use-specific distinction between knowledge use and system-definition use
- [codification](./definitions/codification.md) — defines the phase transition between prose and symbolic artifacts
- [constraining](./definitions/constraining.md) — the mechanism that operates across prose artifacts and reaches symbolic artifacts at its far end
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: lets the same prose content play knowledge or system-definition roles depending on future use
- [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) — applies: deploy-time learning is timing-defined and lands in all three artifact classes
- [treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — extends: builds on the opaque/prose/symbolic split to ask how the three improvement loops should relate
- [system-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md) — needs revision: the artifact-use framing sharpens when system-definition is a use rather than an intrinsic artifact type
- [Memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) — extends: the operational axes should attach to artifact-use pairings
- [trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — grounds: surveyed systems distinguish promotion targets and future uses that span these axes
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — sharpens: backend choice is downstream of artifact class and use
- [inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: readability is shared by both non-opaque artifact classes
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — contrasts: AgeMem is a clean opaque case that makes the class and future-use split visible
- [Cognee](../agent-memory-systems/reviews/cognee.md) — counterexample: database-backed prose artifacts show that files are not the only backend
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: Simon's capacity-change test catches both knowledge use and system-definition use
