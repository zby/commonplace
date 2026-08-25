---
description: "Reflective coverage is stated per represented form and operation profile; control of an external dependency does not make that dependency part of the system's reflective coverage"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources, synthesis]
tags: [foundations, computational-model, constraining, self-improving-systems]
---

# Reflective coverage is graded across representational forms

A [reflective system](./definitions/reflective-system.md)'s [behavior-determining organization](./definitions/behavior-determining-organization.md) can span several [representational forms](./definitions/representational-form.md): natural-language interpreted by models and humans, symbolic structures with formal consumers, and distributed-parametric state such as model weights. Reflective coverage follows the represented causal path, not an artifact's authority label. Where behavior spans forms, a form the self-representation does not cover remains outside reflective reach however thoroughly the others are covered.

That need cannot be assessed all-or-nothing. **Reflective coverage** is relative to the declared aspects and operations, and it grades — by which forms the self-representation spans, and by what the system can do to each covered component.

## Two dimensions grade coverage

**Form coverage** asks which forms' aspects enter the self-representation at all. The **operation profile** asks what processes inside the boundary can do to a covered aspect or component of that same system. Four operations:

1. **Observation** — the component can be read or probed, and what is learned is available inside the boundary.
2. **Selection** — the system can change which sealed component occupies a represented role without seeing inside the alternatives. Coverage reaches the system's composition or component-identity aspect, not the component's hidden state.
3. **Configuration** — an in-boundary component exposes parameters the system can set within an interface it did not author. Coverage reaches those exposed parameters, not the machinery behind the interface.
4. **Modification** — the substrate itself can be edited from inside the boundary. The [Commonplace reference case](./evidence/commonplace-as-a-reflective-system.md) traces one instance spanning natural-language and symbolic artifacts.

**The four do not form a ladder.** Two scalarizations suggest themselves, and both fail. Ordering by how far into the component a lever reaches fails on the concrete cases: selection can change component identity without observing component internals, and configuration through a fixed schema grants no ability to replace the configured component, so no operation confers another. Counting how many operations hold gives an order but not a measure: a tally collapses capabilities that differ in kind, and which operations matter depends on the aspect being claimed — a component the system only ever needs to replace can be fully served by selection alone. So a coverage claim states the set of operations that hold over a given aspect or component: an operation profile, in the same profile sense the cluster already uses for [improvement pathways](./self-improving-systems-README.md) and [actor allocation](./methodological-and-computational-closure-track-different-changes.md) — report the named components, do not replace them with a number. "Selection-only" is useful as a bound: the represented role or component identity can change, while observation, configuration, and modification of its hidden state remain unavailable.

The profile is per represented aspect or component, not merely per form, and its boundary condition is strict. A control surface inside the boundary can affect a dependency outside it without making that dependency a covered component. The internal surface and external target then receive different descriptions: editing a model-binding field is modification of a localized part of the system's own organization; when the request is honored, its outward effect is selection among external parametric dependencies. What an artifact denotes does not determine its form, so a symbolic field that names a model does not become distributed-parametric.

[Commonplace makes the distinction concrete](./evidence/commonplace-as-a-reflective-system.md). Its requested model bindings are explicit and revisable, while the provider weights are outside its boundary. The internal request therefore does not establish reflective coverage of the external target; it provides possible dependency-selection control only when honored, and current evidence does not establish a reliable requested-to-realized binding. Under a different declared frame, a sealed model component could be inside the system and its represented identity could have a selection-only operation profile. That would still cover only the identity or composition aspect, not the hidden weights.

Nor does either dimension imply the other, or any form inherit from another. A system may combine modification of natural-language and symbolic artifacts with selection of an in-boundary sealed component, while another system exposes configuration but no replacement operation. Each claim must name the represented aspect, declared boundary, and operations that actually hold.

Two corollaries. The obvious evidence is not evidence: that one agent can edit both Markdown and Python establishes neither that those artifacts form a self-representation nor that changes to them reach later operation through a causally connected path. And a profile describes a design without ranking it — a fixed mapping the system can only observe can be the correct choice, as the kernel-boundary discussion below shows. Each covered form brings its own verification obligation besides: read natural-language, test symbolic artifacts, probe parametric ones behaviorally.

## Coverage does not subsume addressability

Coverage records represented aspects, components, forms, and structurally available operations. [Addressability](./reflection-buys-addressability.md) records what the system can do with a retained change *as a commitment*: retrieve, interpret, criticize, revise, rescope, or transfer it. Coverage of the relevant component is necessary for those operations, but not sufficient. A process can mechanically observe or modify bytes without interpreting the commitment they encode. Report the two profiles separately rather than treating the operation profile as proof of addressability.

## Mapping coverage is not mapping modifiability

Three properties must remain distinct. **Mapping coverage** asks whether a supported observation or intervention is reliably realized across the boundary. **Mapping inspectability** asks whether the system can examine how the transfer works. **Mapping modifiability** asks whether the system can change it. A trusted compiler may sit in an unmodifiable kernel and still preserve full reflective coverage of a desired-state aspect — provided the declared interface exposes its semantics and its relevant failures.

The properties come apart in practice. A trusted compiler may preserve a fully covered transfer while remaining unmodifiable; a modifiable glue script may expose no reliable account of what it transfers. The [Commonplace reference case](./evidence/commonplace-as-a-reflective-system.md) applies the distinction to its natural-language-to-validator mapping rather than making that repository-specific trace part of the general claim.

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

The pass separates cases the rules treat together — a policy rendered into an `AGENTS.md` excerpt stays natural-language, while a convention rendered into a lint rule crosses into symbolic form and acquires a formal consumer, the [codification](./definitions/codification.md) crossing where transfer can fail silently. And it locates the defect precisely: the renderer's non-modifiability is compatible with full coverage; what breaks the claim is the unexposed failure — filtering that can silently drop a policy for one target while keeping it for another.

## Computational precedents

The analytical questions have computational precedents. Pattie Maes distinguishes **procedural reflection**, where one procedural self-representation is both the implementation and the object of reasoning, from **declarative reflection**, where an implicit procedural representation serves implementation and a separate explicit declarative representation serves reasoning ([1988, printed p. 14; PDF p. 14](../sources/maes-computational-reflection-1988.ingest.md)). Separating those roles creates a consistency obligation; that obligation is this note's inference, not Maes's stated definition. Maes does make the underlying tradeoff explicit: the effective and efficient representation needed for implementation may not be the representation best suited to reasoning. Cross-language reflection supplies the precedent for spanning access. In Roel Wuyts and Stéphane Ducasse's SOUL/Smalltalk construction, reflective integration lets the two languages reason about and act on each other, while an upping/downing schema maps Smalltalk objects to SOUL terms and terms back to objects ([2001, printed pp. 4–7; PDF pp. 4–7](../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md)); entity transfer is one mechanism in that construction, not sufficient by itself. Kris Gybels and colleagues then distinguish a base-level **data mapping**, which makes each language's data appear native in the other and entails translating invoked operations, from a meta-level **protocol mapping**, which makes the receiving interpreter's meta-operations applicable to those data's representations ([2006, printed pp. 111–112; PDF pp. 3–4](../sources/gybels-et-al-2006-inter-language-reflection.ingest.md)).

## What this establishes

Combining natural-language and code does not increase computational universality. The stronger and narrower claim is:

> Combining representational forms extends reflective coverage over a system whose behavior is already distributed across them — and that coverage is graded: a claim must name the form and the operations that hold, and no form inherits either from another.

Joint adaptation, movement between forms, and shared callable interfaces may support that coverage, but none of them establishes it without a causally connected self-representation. What this note supplies is a vocabulary and a graded coverage criterion. It does not, by itself, classify Commonplace or any other system.

## Open Questions

Reflection makes the system's own organization one of its possible intervention targets — when action is model-mediated, part of the represented environment the process must reason about, [since an action model matters only through its consumption path](./an-action-model-matters-only-through-its-consumption-path.md). Appending an explicit lesson needs no comprehensive self-model, but autonomous diagnosis and planning must distinguish enough of the system's artifacts, processes, dependencies, capabilities, and limitations to tell which component a problem belongs to — making every file editable is insufficient. Which distinctions must become explicit and machine-operable for that work remains open:

- Which distinctions about the system must be retained rather than reconstructed by a model on each task?
- How should a retained self-model separate the system from hosted models, runtimes, tools, and other dependencies?
- What evidence would show that an agent used the retained self-model to catch a bug, recognize a limitation, or interpret a genuinely new task?

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — grounds: supplies the aspect-relative causal self-representation criterion
- [An action model matters only through its consumption path](./an-action-model-matters-only-through-its-consumption-path.md) — grounds: the model-mediated action case whose self-directed instance raises the open self-modeling questions
- [Representational form](./definitions/representational-form.md) — defined-in: the natural-language / symbolic / distributed-parametric axis coverage grades over
- [Behavior-determining organization](./definitions/behavior-determining-organization.md) — defined-in: the represented organization whose components and forms a coverage claim spans
- [Lineage](./definitions/lineage.md) — defined-in: records dependencies that require invalidation, regeneration, retirement, or review across representations
- [Behavioral authority](./definitions/behavioral-authority.md) — defined-in: identifies the consumer, channel, and force by which one representation governs behavior
- [Moving the interpretation–enforcement boundary requires cross-form coverage](./moving-the-interpretation-enforcement-boundary-requires-coverage.md) — extends: why governing a transfer of responsibility between interpreted guidance and formal enforcement requires modification-grade coverage of both forms and their mapping
- [Commonplace as a reflective system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: modification-grade coverage of natural-language and symbolic artifacts, plus an internal binding that requests selection of an uncovered external parametric dependency
- [Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — worked case: source-of-truth, regeneration, and staleness rules for behavior-changing derivatives, read here as a mapping whose transfer and kernel boundary stay unrepresented
- [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — mechanism: supplies one interface-level mapping while leaving aspect coverage, authority, and lineage as separate obligations
