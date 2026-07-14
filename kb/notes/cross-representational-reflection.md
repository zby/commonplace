---
description: "Coverage, inspectability, and modifiability of the mappings between representational forms are three separate properties; a fixed trusted kernel is compatible with full reflective coverage"
type: kb/types/note.md
traits: [has-comparison, has-external-sources, synthesis]
tags: [foundations, computational-model, constraining, reflective-systems]
---

# Cross-representational reflection

**Cross-representational reflection** occurs when a causally connected self-representation spans aspects expressed in different representational regimes. Processes within a declared system boundary can inspect or intervene on those aspects across the mappings that connect the regimes. They need not be able to inspect or modify the mappings themselves.

**Reflective coverage** is relative to the aspects and operations declared to be part of the self-representation: the artifacts or structures through which the system represents its own behavior. Coverage does not require unlimited access to every encoding in the causal implementation chain. Inspection and modification are also separate dimensions — a [reflective system](./definitions/reflective-system.md) may expose an aspect to introspection without permitting intercession.

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

The pass separates cases the source rules treat together. A policy rendered into an `AGENTS.md` excerpt stays prose, consumed by natural-language interpretation on both sides; a convention rendered into a lint rule crosses into symbolic form and acquires a formal consumer. Only the second is cross-representational, and that [codification](./definitions/codification.md) crossing is where transfer can fail silently.

It also locates the gap precisely. The renderer's non-modifiability is not the defect — an unmodifiable kernel is compatible with full coverage. But that compatibility was conditional on the interface exposing its semantics and its relevant failures, and target-specific filtering that can silently drop a policy for one assistant while keeping it for another is exactly such a failure. The unexposed failure is the defect, not the fixed mapping.

## Computational precedents

Pattie Maes's *Computational Reflection* distinguishes **procedural reflection**, in which implementation and self-representation share one operative representation, from **declarative reflection**, in which explicit constraints must be translated into and kept consistent with procedural behavior ([1988, printed p. 14; PDF p. 14](../sources/maes-computational-reflection-1988.ingest.md)). The distinction is not simply between prose and code. It explains why the representation best suited to implementation may differ from the one best suited to reasoning, and why reflection remains relative to the aspects the self-representation exposes.

Cross-language reflection offers the closest direct precedent for spanning access. In *Symbiotic Reflection between an Object-Oriented and a Logic Programming Language*, Roel Wuyts and Stéphane Ducasse make entity transfer explicit, enabling each language to reason about and act on the other ([2001, printed pp. 4–10; PDF pp. 4–10](../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md)). In *Inter-language Reflection*, Kris Gybels and colleagues distinguish **data mappings**, which move values across a boundary, from **protocol mappings**, which make the receiving side's operations applicable to representations of those values ([2006, printed pp. 110–112; PDF pp. 2–4](../sources/gybels-et-al-2006-inter-language-reflection.ingest.md)). Their architecture exposes both ordinary program behavior and reflective operations over its representations.

Cross-representational reflection carries the same analytical questions beyond programming languages: what is represented, what crosses each boundary, which operations remain available, and how changes acquire consequences. The precedents do not establish that asynchronous artifacts, human interpretation, or repository workflows behave like language interpreters. Such systems must demonstrate their own boundaries and causal paths.

## Semantic–formal is broader than neuro-symbolic

In this KB's [representational-form](./definitions/representational-form.md) vocabulary, code is **symbolic** when a parser, compiler, runtime, or other formal consumer assigns consequences to its structures, while prose is consumed through natural-language interpretation. That classification does not make every prose-and-code system **neuro-symbolic**. Established neuro-symbolic AI usage combines an operative neural component with explicit symbolic representation or reasoning, as illustrated by [a survey of neuro-symbolic AI](https://arxiv.org/abs/2305.08876) and the [Neuro-Symbolic Concept Learner](https://arxiv.org/abs/1904.12584). This note therefore uses **semantic–formal hybrid** for the general prose-and-code case, and reserves **neuro-symbolic** for systems in which neural and symbolic components jointly shape behavior.

## What this establishes

Combining prose and code does not increase computational universality. The stronger and narrower claim is:

> Combining semantic and formal representations extends reflective coverage over a system whose behavior is already distributed across both.

Joint adaptation, movement between forms, and shared callable interfaces may support that coverage, but none of them establishes it without a causally connected self-representation. What the concept supplies is a vocabulary and a coverage criterion. It does not, by itself, classify Commonplace or any other system.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the aspect-relative causal self-representation criterion
- [Lineage](./definitions/lineage.md) — defined-in: records dependencies that require invalidation, regeneration, retirement, or review across representations
- [Behavioral authority](./definitions/behavioral-authority.md) — defined-in: identifies the consumer, channel, and force by which one representation governs behavior
- [Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — worked case: source-of-truth, regeneration, and staleness rules for behavior-changing derivatives, read here as a mapping whose transfer and kernel boundary stay unrepresented
- [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — mechanism: supplies one interface-level mapping while leaving aspect coverage, authority, and lineage as separate obligations
