---
description: "Reflective coverage is graded per representational form and operation depth; selection among opaque components — pinning a model — is real but crude coverage of the parametric form"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources, synthesis]
tags: [foundations, computational-model, constraining, self-improving-systems]
---

# Reflective coverage is graded across representational forms

A [reflective system](./definitions/reflective-system.md)'s behavior can be carried by several kinds of artifact at once. Its [system-definition artifacts](./definitions/system-definition-artifact.md) — the artifacts it consumes with binding force — may take any [representational form](./definitions/representational-form.md): prose interpreted by models and humans, symbolic structures with formal consumers, distributed-parametric state such as model weights. Where they span forms, reflective reach must span them too: a behavior bound by an artifact whose form the self-representation does not cover is outside that reach, however thoroughly the other forms are covered.

That need cannot be assessed all-or-nothing. **Reflective coverage** is relative to the declared aspects and operations, and it grades — by which forms the self-representation spans, and by what the system can do to each covered component.

## Two dimensions grade coverage

**Form coverage** asks which forms' aspects enter the self-representation at all. **Operation depth** asks what processes inside the boundary can do to a covered component, rising through at least four levels:

1. **Observation** — the component can be read or probed, and what is learned is available inside the boundary.
2. **Selection** — the system can swap one sealed component for another without seeing inside either. A skill pinning `model: opus` selects among sealed alternatives and reaches nothing finer.
3. **Configuration** — the component exposes parameters the system can set, within an interface it did not author. Commonplace's skill frontmatter does this to the harness: `allowed-tools: Read, Write, Grep, Glob, Bash, Skill` and `context: fork` set the tool surface and context regime for a skill run, through a schema the harness owns. The system can set those fields and cannot inspect or edit the machinery that honours them.
4. **Modification** — the substrate itself can be edited from inside the boundary. Editing `kb/types/tag-readme.md` changes what the validator enforces, because the spec's own path is the validator's dispatch key.

The rungs are per component, not per form: the two instances above sit at different depths over different components — selection over the weights, configuration over the harness — and both are outside the declared boundary in the [case classification](../reference/commonplace-as-a-reflective-system.md). Nothing in this repository configures the parametric form itself; that rung is instanced against the harness, not the weights.

Neither dimension implies the other, and no form inherits either from another. The instructive case pairs modification depth on prose and symbolic artifacts with selection depth on a parametric component: an agent system whose instructions can require a particular model, or a class of models, exercises real intercession over its distributed-parametric form — the choice of weights is represented, causally connected, and revisable by the system's own processes — yet nothing inside the boundary can inspect or edit what the weights do. Calling this "no reflection over the model" misses the lever that exists; calling it "reflective coverage of the weights" overstates what the lever reaches. It is selection-grade coverage of the parametric form, and should be claimed as exactly that.

A coverage claim therefore states form and depth, separately for each form the behavior lives in — neither form inherits coverage from the other, and the obvious evidence is not evidence: that one agent can edit both Markdown and Python establishes neither that those artifacts form a self-representation nor that changes to them reach later operation through a causally connected path. Depth describes a design; it does not rank it — a fixed mapping held at shallow depth can be the correct choice, as the kernel-boundary discussion below shows. Each covered form also brings its own verification obligations: read prose, test symbolic artifacts, probe parametric ones behaviorally.

## Mapping coverage is not mapping modifiability

Three properties must remain distinct. **Mapping coverage** asks whether a supported observation or intervention is reliably realized across the boundary. **Mapping inspectability** asks whether the system can examine how the transfer works. **Mapping modifiability** asks whether the system can change it. A trusted compiler may sit in an unmodifiable kernel and still preserve full reflective coverage of a desired-state aspect — provided the declared interface exposes its semantics and its relevant failures.

The properties come apart in practice. Commonplace's type-spec-to-validator mapping is unusually well covered: the validator dispatches on the spec's own path (`@type_rule("kb/types/tag-readme.md")`), so a prose spec and the code enforcing it cannot drift silently — the specification file *is* the enforcement key. That is high mapping coverage bought by a naming convention, not by making the dispatch mechanism modifiable. Most other prose-to-code relationships in the same repository have no such binding, and there the mapping is uncovered: the prose can change with nothing to notice that the code no longer matches.

The demand rises only when a system claims to inspect or adapt the transfer itself. Then the mapping must enter the self-representation: its interface, authority rule, rationale-to-implementation lineage, [codification](./definitions/codification.md) boundary, or consistency mechanism. Declaring a terminal kernel keeps this from becoming an infinite demand to represent every mechanism that represents another mechanism.

## Assessing a claim

Six questions establish what a coverage claim actually covers:

- **Represented aspects and operations:** What can be observed or changed?
- **Transfer:** What carries values, distinctions, or operations across the boundary?
- **Authority:** Which representation governs when the two disagree?
- **Lineage:** Which dependencies require invalidation, regeneration, or review after a change?
- **Consistency and failure:** How are drift, rejected translations, and stale derivatives exposed?
- **Kernel boundary:** Which interpreter, compiler, runtime, human practice, or learned substrate is fixed outside the reflective surface?

## A worked pass

[Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) gives source-of-truth rules for a memory system whose authored source renders into cues, prompt files, indexes, lint rules, and assistant-specific views. Put to the six questions:

- **Aspects and operations.** Behavior-shaping knowledge — policies, conventions, cues; observation via provenance and version metadata, intervention directional: edit the source, then regenerate the view or mark it stale.
- **Transfer.** A renderer with target-specific filtering — named, but not represented.
- **Authority.** Answered, the rules' strongest item: the source governs; a compiled view is never a separate policy.
- **Lineage.** Answered: a source change obliges regeneration or a staleness mark; direct edits to a view flow back to the source or stay candidate-stage.
- **Consistency and failure.** Partial: staleness after a source change is covered; rejected translations are not — a source item that cannot render into a target can vanish silently.
- **Kernel boundary.** Not declared: the renderer and the harness's context-loading mechanism sit outside the reflective surface, unnamed.

The pass separates cases the rules treat together — a policy rendered into an `AGENTS.md` excerpt stays prose, while a convention rendered into a lint rule crosses into symbolic form and acquires a formal consumer, the [codification](./definitions/codification.md) crossing where transfer can fail silently. And it locates the defect precisely: the renderer's non-modifiability is compatible with full coverage; what breaks the claim is the unexposed failure — filtering that can silently drop a policy for one target while keeping it for another.

## Computational precedents

The analytical questions have computational precedents. Pattie Maes distinguishes **procedural reflection**, where implementation and self-representation share one operative representation, from **declarative reflection**, where explicit constraints must be kept consistent with procedural behavior ([1988, printed p. 14; PDF p. 14](../sources/maes-computational-reflection-1988.ingest.md)) — which is why the representation best suited to implementation may differ from the one best suited to reasoning. Cross-language reflection supplies the precedent for spanning access: Roel Wuyts and Stéphane Ducasse make entity transfer explicit so each language can reason about and act on the other ([2001, printed pp. 4–10; PDF pp. 4–10](../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md)), and Kris Gybels and colleagues separate **data mappings**, which move values across a boundary, from **protocol mappings**, which make the receiving side's operations applicable to representations of those values ([2006, printed pp. 110–112; PDF pp. 2–4](../sources/gybels-et-al-2006-inter-language-reflection.ingest.md)).

## What this establishes

Combining prose and code does not increase computational universality. The stronger and narrower claim is:

> Combining representational forms extends reflective coverage over a system whose behavior is already distributed across them — and that coverage is graded: a claim must name the form and the operation depth, and no form inherits either from another.

Joint adaptation, movement between forms, and shared callable interfaces may support that coverage, but none of them establishes it without a causally connected self-representation. What this note supplies is a vocabulary and a graded coverage criterion. It does not, by itself, classify Commonplace or any other system.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the aspect-relative causal self-representation criterion
- [Representational form](./definitions/representational-form.md) — defined-in: the prose / symbolic / distributed-parametric axis coverage grades over
- [System-definition artifact](./definitions/system-definition-artifact.md) — defined-in: the binding artifacts whose forms a coverage claim must span
- [Lineage](./definitions/lineage.md) — defined-in: records dependencies that require invalidation, regeneration, retirement, or review across representations
- [Behavioral authority](./definitions/behavioral-authority.md) — defined-in: identifies the consumer, channel, and force by which one representation governs behavior
- [Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — extends: why single-form coverage is insufficient for agentic systems — the reliability-improving changes are the crossings
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: a system graded across forms — modification-depth coverage of prose and symbolic artifacts, selection-grade control over the parametric form
- [Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — worked case: source-of-truth, regeneration, and staleness rules for behavior-changing derivatives, read here as a mapping whose transfer and kernel boundary stay unrepresented
- [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — mechanism: supplies one interface-level mapping while leaving aspect coverage, authority, and lineage as separate obligations
