---
description: "Reflective coverage is graded per representational form and operation depth; selection among opaque components — pinning a model — is real but crude coverage of the parametric form"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources, synthesis]
tags: [foundations, computational-model, constraining, reflective-systems]
---

# Reflective coverage is graded across representational forms

A [reflective system](./definitions/reflective-system.md)'s behavior is rarely carried by one kind of artifact. Its [system-definition artifacts](./definitions/system-definition-artifact.md) — the artifacts it consumes with binding force — take different [representational forms](./definitions/representational-form.md): prose interpreted by models and humans, symbolic structures with formal consumers, and distributed-parametric state such as model weights. Reflective reach must span all of them: a behavior bound by an artifact whose form the self-representation does not cover is outside that reach, however thoroughly the other forms are covered.

That need cannot be assessed all-or-nothing. **Reflective coverage** is relative to the declared aspects and operations, and it grades — by which forms the self-representation spans, and by what the system can do to each covered component. Processes inside the boundary may inspect or intervene on aspects across the mappings that connect the forms without being able to inspect or modify the mappings themselves; inspection and modification are separate dimensions throughout.

## Two dimensions grade coverage

Coverage grades along two independent dimensions. **Form coverage** asks which forms' aspects enter the self-representation at all. **Operation depth** asks what processes inside the boundary can do to a covered component. Depth rises through at least four levels:

1. **Observation** — the component can be read or probed, and what is learned is available inside the boundary as a representation of the system.
2. **Selection** — the system can choose among opaque alternatives: swap one sealed component for another without seeing inside either.
3. **Configuration** — the component exposes parameters the system can set, within an interface it did not author.
4. **Modification** — the substrate itself can be edited by processes inside the boundary.

Neither dimension implies the other, and no form inherits either from another. The instructive case is modification-depth coverage of prose and symbolic artifacts coexisting with selection-depth coverage of a parametric component. An agent system whose instructions can require a particular model, or a class of models, exercises real intercession over its distributed-parametric form: the choice of weights is represented in a system-definition artifact, causally connected to everything downstream, and revisable by the system's own processes. Yet nothing inside the boundary can inspect or edit what those weights do — the intervention granularity is swapping a sealed unit. Calling this "no reflection over the model" misses the lever that exists; calling it "reflective coverage of the weights" overstates what the lever reaches. It is selection-grade coverage of the parametric form, and it should be claimed as exactly that.

Grading dissolves the binary question. A system need not cover all its forms to be reflective — reflection is aspect-bound — but a coverage claim must state the form and the depth, separately for each form the system's behavior lives in. Depth describes a design; it does not rank it — the kernel-boundary discussion below shows why a fixed mapping held at shallow depth can be the correct choice. Each covered form also brings its own verification obligations, since form sets the default review method: read prose, test symbolic artifacts, probe parametric ones behaviorally.

## Coverage patterns

1. **A semantic endpoint with a fixed formal mapping.** A process may revise a desired-state specification that a compiler or reconciler translates into formal behavior. Coverage can be complete for the declared desired-state aspect even if the generated program is never directly exposed. Coverage is partial only if the formal layer makes independently significant choices that the self-representation can neither observe nor control.
2. **A formal endpoint without its semantic context.** A process may inspect or modify implemented operations yet lack the purposes, authority claims, or rationale through which those operations are interpreted and maintained. Formal access covers the implementation and leaves those separately represented aspects outside the reflective surface.
3. **Spanning access.** When each regime carries independently represented aspects, coverage must be demonstrated for each of them separately. Neither regime inherits coverage from the other: reaching a formal artifact establishes nothing about the semantic aspects that govern how it is interpreted, and reaching a specification establishes nothing about formal choices the specification does not determine.

These patterns are not exhaustive; a system may cover any subset of its represented aspects and supported operations. But they are enough to show why the obvious evidence is not evidence. That one agent can edit both Markdown and Python establishes neither that those artifacts form a self-representation nor that changes to them reach later operation through a causally connected path.

## Mapping coverage is not mapping modifiability

Three properties must remain distinct. **Mapping coverage** asks whether a supported observation or intervention is reliably realized across the boundary. **Mapping inspectability** asks whether the system can examine how the transfer works. **Mapping modifiability** asks whether the system can change it. A trusted compiler may sit in an unmodifiable kernel and still preserve full reflective coverage of a desired-state aspect — provided the declared interface exposes its semantics and its relevant failures.

The demand rises only when a system claims to inspect or adapt the transfer itself. Then the mapping must enter the self-representation, and the represented material might include its interface, its authority rule, its rationale-to-implementation lineage, its [codification](./definitions/codification.md) boundary, or its consistency mechanism. Declaring a terminal kernel is what keeps this from becoming an infinite demand to represent every mechanism that represents another mechanism.

## Assessing a claim

Six questions establish what a claimed cross-representational capability actually covers:

- **Represented aspects and operations:** What can be observed or changed?
- **Transfer:** What carries values, distinctions, or operations across the boundary?
- **Authority:** Which representation governs when the two disagree?
- **Lineage:** Which dependencies require invalidation, regeneration, or review after a change?
- **Consistency and failure:** How are drift, rejected translations, and stale derivatives exposed?
- **Kernel boundary:** Which interpreter, compiler, runtime, human practice, or learned substrate is fixed outside the reflective surface?

## A worked pass

[Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) gives the source-of-truth rules for a memory system's derived surfaces, where an authored source renders into cues, prompt files, indexes, lint rules, and assistant-specific views. Put those rules to the six questions:

- **Represented aspects and operations.** The declared aspect is behavior-shaping knowledge: policies, conventions, cues. Observation is specified — provenance, source version or hash, generation time, owner. Intervention is specified and directional: edit the source, then regenerate the view or mark it stale.
- **Transfer.** A renderer with target-specific filtering. Named, but not represented.
- **Authority.** Answered, and this is the pattern's strongest item: the source governs, a compiled view is never a separate policy, and an external surface may retain authority even when the system keeps a distilled view of it.
- **Lineage.** Answered: a source change obliges regeneration or a staleness mark, and direct edits to a view flow back to the source or stay candidate-stage.
- **Consistency and failure.** Partially answered. Staleness after a source change is covered; rejected translations are not. When a source item cannot render into a target — filtered out, unsupported, too long — nothing requires that omission to surface.
- **Kernel boundary.** Not declared. The renderer and the harness's context-loading mechanism both sit outside the reflective surface, unnamed.

The pass separates cases the source rules treat together. A policy rendered into an `AGENTS.md` excerpt stays prose, consumed by natural-language interpretation on both sides; a convention rendered into a lint rule crosses into symbolic form and acquires a formal consumer. Only the second crosses representational forms, and that [codification](./definitions/codification.md) crossing is where transfer can fail silently.

It also locates the gap precisely. The renderer's non-modifiability is not the defect — an unmodifiable kernel is compatible with full coverage. But that compatibility was conditional on the interface exposing its semantics and its relevant failures, and target-specific filtering that can silently drop a policy for one assistant while keeping it for another is exactly such a failure. The unexposed failure is the defect, not the fixed mapping.

## Computational precedents

Pattie Maes's *Computational Reflection* distinguishes **procedural reflection**, in which implementation and self-representation share one operative representation, from **declarative reflection**, in which explicit constraints must be translated into and kept consistent with procedural behavior ([1988, printed p. 14; PDF p. 14](../sources/maes-computational-reflection-1988.ingest.md)). The distinction is not simply between prose and code. It explains why the representation best suited to implementation may differ from the one best suited to reasoning, and why reflection remains relative to the aspects the self-representation exposes.

Cross-language reflection offers the closest direct precedent for spanning access. In *Symbiotic Reflection between an Object-Oriented and a Logic Programming Language*, Roel Wuyts and Stéphane Ducasse make entity transfer explicit, enabling each language to reason about and act on the other ([2001, printed pp. 4–10; PDF pp. 4–10](../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md)). In *Inter-language Reflection*, Kris Gybels and colleagues distinguish **data mappings**, which move values across a boundary, from **protocol mappings**, which make the receiving side's operations applicable to representations of those values ([2006, printed pp. 110–112; PDF pp. 2–4](../sources/gybels-et-al-2006-inter-language-reflection.ingest.md)). Their architecture exposes both ordinary program behavior and reflective operations over its representations.

The graded-coverage criterion carries the same analytical questions beyond programming languages: what is represented, what crosses each boundary, which operations remain available, and how changes acquire consequences. The precedents do not establish that asynchronous artifacts, human interpretation, or repository workflows behave like language interpreters. Such systems must demonstrate their own boundaries and causal paths.

## Semantic–formal is broader than neuro-symbolic

In this KB's [representational-form](./definitions/representational-form.md) vocabulary, code is **symbolic** when a parser, compiler, runtime, or other formal consumer assigns consequences to its structures, while prose is consumed through natural-language interpretation. That classification does not make every prose-and-code system **neuro-symbolic**. Established neuro-symbolic AI usage combines an operative neural component with explicit symbolic representation or reasoning, as illustrated by [a survey of neuro-symbolic AI](https://arxiv.org/abs/2305.08876) and the [Neuro-Symbolic Concept Learner](https://arxiv.org/abs/1904.12584). This note therefore uses **semantic–formal hybrid** for the general prose-and-code case, and reserves **neuro-symbolic** for systems in which neural and symbolic components jointly shape behavior.

## What this establishes

Combining prose and code does not increase computational universality. The stronger and narrower claim is:

> Combining semantic and formal representations extends reflective coverage over a system whose behavior is already distributed across both — and that coverage is graded: a claim must name the form and the operation depth, and no form inherits either from another.

Joint adaptation, movement between forms, and shared callable interfaces may support that coverage, but none of them establishes it without a causally connected self-representation. What this note supplies is a vocabulary and a graded coverage criterion. It does not, by itself, classify Commonplace or any other system.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the aspect-relative causal self-representation criterion
- [Representational form](./definitions/representational-form.md) — defined-in: the prose / symbolic / distributed-parametric axis coverage grades over
- [System-definition artifact](./definitions/system-definition-artifact.md) — defined-in: the binding artifacts whose forms a coverage claim must span
- [Lineage](./definitions/lineage.md) — defined-in: records dependencies that require invalidation, regeneration, retirement, or review across representations
- [Behavioral authority](./definitions/behavioral-authority.md) — defined-in: identifies the consumer, channel, and force by which one representation governs behavior
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: a system graded across forms — modification-depth coverage of prose and symbolic artifacts, selection-grade control over the parametric form
- [Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — worked case: source-of-truth, regeneration, and staleness rules for behavior-changing derivatives, read here as a mapping whose transfer and kernel boundary stay unrepresented
- [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — mechanism: supplies one interface-level mapping while leaving aspect coverage, authority, and lineage as separate obligations
