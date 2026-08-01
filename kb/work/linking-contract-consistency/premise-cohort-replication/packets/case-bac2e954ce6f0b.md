# Case packet

Neutral case identifier: case-bac2e954ce6f0b

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Retaining the episode keeps a distilled rule re-derivable

A lesson learned in operation admits two explicit retention forms. The **episode** is the trace of the situation the lesson came from — a session transcript, an execution trace, a worked case. The **rule** is the distilled statement of the lesson, separated from its occasion. Memory designs tend to treat these as rivals — episodic stores versus extracted facts — but they are layers of one system, and the choice that matters is not which to keep but whether the pair stays linked.

Linked, the pair instantiates a [two-layer execution system] at artifact scale: the rule is the derived fast path — action-shaped, cheap to load, strictly narrower than what the episode contains — and the episode is the generator-side evidence a consumer drops back to when the rule's coverage fails or its scope is contested. That fallback is what the title names. A challenged rule with its episode retained and lineage recorded can be re-derived: read the episode again, judge whether the generalization survives, revise its scope from evidence. This is semantic re-derivation under the managed-staleness regime, not deterministic recomputation — but it is real recourse. A rule whose episode is gone has none: it can be trusted or discarded, never re-examined against what taught it. Discarding the episode converts the rule from an evidence-backed derivation into a bare commitment, and [an upstream change can then name no downstream worklist] because the dependency record died with the source.

## Distillation is earned by recurrence

The timing of distillation is a lifecycle question, not a storage preference. A rule distilled from a single episode is a conjecture that has skipped its test: the [discovery lifecycle] places one surprising case at observation and the posited generalization at conjecture, with acceptance gated on accumulated cases. Retaining the episode first and distilling on recurrence respects those phases — the episode store is where candidate generalizations wait for their second and third occurrence, and recurrence is the same promotion signal the two-layer architecture uses to grow a fast path. Distill-on-first-occurrence fixes a generalization exactly when the evidence for its scope is thinnest.

## What distillation sheds, and where each layer wins

Distillation keeps the articulable part of a lesson and sheds the rest. The residue — calibration, situational feel, what a counterpart means by their words — is competence the episode still carries latently, because replaying an episode into context partially re-induces the conditioned state that held the lesson, while no statement of the rule can. The episode is the explicit trace of a tacit state, and the loss direction follows from [only explicit retention being durable, writable, and addressable at once]: the rule is the more addressable object, the episode preserves more of what resisted articulation. The practical familiar form of this asymmetry is that worked examples routinely outperform stated instructions for style- and calibration-shaped competence.

Governability runs the other way. Rules collide detectably — two contradictory statements can be noticed at write time — and are individually citable, revisable, and retirable. Episodes teaching opposite lessons coexist silently, and no lesson inside an episode can be revised; it can only be annotated or re-distilled. So governance lives at the rule layer, evidence and residue at the episode layer — a division of labor, not a contest. Between the raw trace and the bare rule sits a spectrum of intermediate forms — the cleaned worked trace, the rule with its attached example — and the residue share of a lesson's value is a guide to where on that spectrum it should be retained.

## Costs the pair must manage

- **Loading.** Retaining episodes is a capture posture, not a context posture: [persistence and loading are separate decisions], and [evidence can be preserved without becoming the next context]. Rules load by default because [a fast path should carry answers, not work]; episodes load on demand — scope disputes, re-derivation, residue-heavy tasks.
- **Model relativity.** An episode's lesson is a joint product of the trace and the model that reads it; replay under different weights re-conditions differently. Episode retention therefore carries a quiet selection-grade dependency on the parametric form — faithful replay pins the reader — while a rule is comparatively model-portable. The [operation-profile vocabulary] makes the dependency statable.

## Scope

- Which episodes to keep at all is the inclusion question, and it belongs to the [declared output spec]; this note owns the form question — given a lesson worth keeping, in which layer its value survives.
- Nothing here claims raw transcripts are the right episode form; the claim is that some episode-grade record must survive distillation for the rule to remain re-derivable.

## Open Questions

- Eviction: episodes accumulate linearly with operation; what retires one — the promotion of its lesson, a staleness horizon, or contradiction by later episodes?
- Recall: the rule layer is findable by statement; what routing lets an agent find the episode it needs when the rule's scope fails?
- How much residue actually survives replay, and how it degrades across model versions, is measurable and unmeasured.

---

Relevant Notes:

## Artifact B

# Reflective coverage is graded across representational forms

A [reflective system]'s [behavior-determining organization] can span several [representational forms]: natural-language interpreted by models and humans, symbolic structures with formal consumers, and distributed-parametric state such as model weights. Reflective coverage follows the represented causal path, not an artifact's authority label. Where behavior spans forms, a form the self-representation does not cover remains outside reflective reach however thoroughly the others are covered.

That need cannot be assessed all-or-nothing. **Reflective coverage** is relative to the declared aspects and operations, and it grades — by which forms the self-representation spans, and by what the system can do to each covered component.

## Two dimensions grade coverage

**Form coverage** asks which forms' aspects enter the self-representation at all. The **operation profile** asks what processes inside the boundary can do to a covered component. Four operations:

1. **Observation** — the component can be read or probed, and what is learned is available inside the boundary.
2. **Selection** — the system can swap one sealed component for another without seeing inside either. A skill pinning `model: opus` selects among sealed alternatives and reaches nothing finer.
3. **Configuration** — the component exposes parameters the system can set, within an interface it did not author. Commonplace's skill frontmatter does this to the harness: `allowed-tools: Read, Write, Grep, Glob, Bash, Skill` and `context: fork` set the tool surface and context regime for a skill run, through a schema the harness owns. The system can set those fields and cannot inspect or edit the machinery that honours them.
4. **Modification** — the substrate itself can be edited from inside the boundary. The [Commonplace reference case] traces one instance spanning natural-language and symbolic artifacts.

**The four do not form a ladder.** Two scalarizations suggest themselves, and both fail. Ordering by how far into the component a lever reaches fails on the concrete cases: selection operates over components it cannot observe — that is what makes them sealed — and configuration through a vendor's schema grants no ability to swap the vendor out, so no operation confers another. Counting how many operations hold gives an order but not a measure: a tally collapses capabilities that differ in kind, and which operations matter depends on the aspect being claimed — a component the system only ever needs to replace is fully served by selection alone. So a coverage claim states the set of operations that hold over a given component: an operation profile, in the same profile sense the cluster already uses for [improvement pathways] and [actor allocation] — report the named components, do not replace them with a number. What survives of rank-talk is its negative use: naming an operation a lever does *not* have ("selection-grade" says the weights can be swapped and nothing finer) remains the precise way to bound a claim.

The profile is also per component rather than per form. The two instances above sit over different components — selection over the weights, configuration over the harness — and both components are outside the declared boundary in the [case classification]. Nothing in this repository configures the parametric form itself.

Nor does either dimension imply the other, or any form inherit from another. The instructive case pairs modification-grade coverage of natural-language and symbolic artifacts with selection-grade coverage of a parametric component: an agent system whose instructions can require a particular model, or a class of models, exercises real intercession over its distributed-parametric form — the choice of weights is represented, causally connected, and revisable by the system's own processes — yet nothing inside the boundary can inspect or edit what the weights do. Calling this "no reflection over the model" misses the lever that exists; calling it "reflective coverage of the weights" overstates what the lever reaches. It is selection-grade coverage of the parametric form, and should be claimed as exactly that.

Two corollaries. The obvious evidence is not evidence: that one agent can edit both Markdown and Python establishes neither that those artifacts form a self-representation nor that changes to them reach later operation through a causally connected path. And a profile describes a design without ranking it — a fixed mapping the system can only observe can be the correct choice, as the kernel-boundary discussion below shows. Each covered form brings its own verification obligation besides: read natural-language, test symbolic artifacts, probe parametric ones behaviorally.

## Coverage does not subsume addressability

Coverage records represented aspects, components, forms, and structurally available operations. [Addressability] records what the system can do with a retained change *as a commitment*: retrieve, interpret, criticize, revise, rescope, or transfer it. Coverage of the relevant component is necessary for those operations, but not sufficient. A process can mechanically observe or modify bytes without interpreting the commitment they encode. Report the two profiles separately rather than treating the operation profile as proof of addressability.

## Mapping coverage is not mapping modifiability

Three properties must remain distinct. **Mapping coverage** asks whether a supported observation or intervention is reliably realized across the boundary. **Mapping inspectability** asks whether the system can examine how the transfer works. **Mapping modifiability** asks whether the system can change it. A trusted compiler may sit in an unmodifiable kernel and still preserve full reflective coverage of a desired-state aspect — provided the declared interface exposes its semantics and its relevant failures.

The properties come apart in practice. A trusted compiler may preserve a fully covered transfer while remaining unmodifiable; a modifiable glue script may expose no reliable account of what it transfers. The [Commonplace reference case] applies the distinction to its natural-language-to-validator mapping rather than making that repository-specific trace part of the general claim.

The demand rises only when a system claims to inspect or adapt the transfer itself. Then the mapping must enter the self-representation: its interface, authority rule, rationale-to-implementation lineage, [codification] boundary, or consistency mechanism. Declaring a terminal kernel keeps this from becoming an infinite demand to represent every mechanism that represents another mechanism.

## Assessing a claim

Six questions establish what a coverage claim actually covers:

- **Represented aspects and operations:** What can be observed or changed?
- **Transfer:** What carries values, distinctions, or operations across the boundary?
- **Authority:** Which representation governs when the two disagree?
- **Lineage:** Which dependencies require invalidation, regeneration, or review after a change?
- **Consistency and failure:** How are drift, rejected translations, and stale derivatives exposed?
- **Kernel boundary:** Which interpreter, compiler, runtime, human practice, or learned substrate is fixed outside the reflective surface?

## A worked pass

[Keep lineage and compiled views from drifting] gives source-of-truth rules for a memory system whose authored source renders into cues, prompt files, indexes, lint rules, and assistant-specific views. Put to the six questions:

- **Aspects and operations.** Behavior-shaping knowledge — policies, conventions, cues; observation via provenance and version metadata, intervention directional: edit the source, then regenerate the view or mark it stale.
- **Transfer.** A renderer with target-specific filtering — named, but not represented.
- **Authority.** Answered, the rules' strongest item: the source governs; a compiled view is never a separate policy.
- **Lineage.** Answered: a source change obliges regeneration or a staleness mark; direct edits to a view flow back to the source or stay candidate-stage.
- **Consistency and failure.** Partial: staleness after a source change is covered; rejected translations are not — a source item that cannot render into a target can vanish silently.
- **Kernel boundary.** Not declared: the renderer and the harness's context-loading mechanism sit outside the reflective surface, unnamed.

The pass separates cases the rules treat together — a policy rendered into an `AGENTS.md` excerpt stays natural-language, while a convention rendered into a lint rule crosses into symbolic form and acquires a formal consumer, the [codification] crossing where transfer can fail silently. And it locates the defect precisely: the renderer's non-modifiability is compatible with full coverage; what breaks the claim is the unexposed failure — filtering that can silently drop a policy for one target while keeping it for another.

## Computational precedents

The analytical questions have computational precedents. Pattie Maes distinguishes **procedural reflection**, where implementation and self-representation share one operative representation, from **declarative reflection**, where explicit constraints must be kept consistent with procedural behavior ([1988, printed p. 14; PDF p. 14]) — which is why the representation best suited to implementation may differ from the one best suited to reasoning. Cross-language reflection supplies the precedent for spanning access: Roel Wuyts and Stéphane Ducasse make entity transfer explicit so each language can reason about and act on the other ([2001, printed pp. 4–10; PDF pp. 4–10]), and Kris Gybels and colleagues separate **data mappings**, which move values across a boundary, from **protocol mappings**, which make the receiving side's operations applicable to representations of those values ([2006, printed pp. 110–112; PDF pp. 2–4]).

## What this establishes

Combining natural-language and code does not increase computational universality. The stronger and narrower claim is:

> Combining representational forms extends reflective coverage over a system whose behavior is already distributed across them — and that coverage is graded: a claim must name the form and the operations that hold, and no form inherits either from another.

Joint adaptation, movement between forms, and shared callable interfaces may support that coverage, but none of them establishes it without a causally connected self-representation. What this note supplies is a vocabulary and a graded coverage criterion. It does not, by itself, classify Commonplace or any other system.

## Open Questions

Reflection makes the system's own organization one of its possible intervention targets — when action is model-mediated, part of the represented environment the process must reason about, [since an action model matters only through its consumption path]. Appending an explicit lesson needs no comprehensive self-model, but autonomous diagnosis and planning must distinguish enough of the system's artifacts, processes, dependencies, capabilities, and limitations to tell which component a problem belongs to — making every file editable is insufficient. Which distinctions must become explicit and machine-operable for that work remains open:

- Which distinctions about the system must be retained rather than reconstructed by a model on each task?
- How should a retained self-model separate the system from hosted models, runtimes, tools, and other dependencies?
- What evidence would show that an agent used the retained self-model to catch a bug, recognize a limitation, or interpret a genuinely new task?

---

Relevant Notes:

- [Keep lineage and compiled views from drifting] — worked case: source-of-truth, regeneration, and staleness rules for behavior-changing derivatives, read here as a mapping whose transfer and kernel boundary stay unrepresented

## Under-review context phrase

the profile vocabulary that states episode replay's selection-grade dependency on the reader model
