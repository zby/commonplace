# Case packet

Neutral case identifier: case-f2af1a1b9045ca

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Increasing computational autonomy relocates human effort to the frontier instead of reducing it

The naive test of increasing computational autonomy is falling human hours: if more pathway functions become computationally closed, the human should be needed less and less. In an open-ended improvement system, that is usually not what happens. The observed pattern runs the other way around:

1. a class of routine work becomes computationally executable;
2. the system can therefore process more material or attempt harder improvements;
3. human attention moves to that new frontier;
4. total human time stays roughly constant — while the human contribution *per completed improvement* falls.

In miniature: once link checking becomes a validator, nobody banks the freed minutes. Review attention moves to whether the linked claims are actually right — a harder question that previously went unasked because the cheap question consumed the session. The hours are the same; what an hour buys has changed.

The mechanism is an elastic workload. An open-ended system has an unbounded backlog of possible improvements, so attention freed from routine work moves to work that previously went unattempted. Bainbridge's ironies of automation identified the broader pattern: automation transforms rather than removes the operator's role, leaving the residue that could not be automated ([Bainbridge 1983]). Here that residue is the work past the oracles — noticing, objective-setting, and the shape judgments no automatic check covers, [since warranted autonomy is bounded by oracle domain].

> As computational autonomy increases, a fixed amount of human judgment supports a larger volume, longer horizon, or greater difficulty of self-improvement.

Total hours confound a change in actor allocation with the ambition it enables. The relevant change is in what each human judgment supports.

## What to measure instead

Ratio and frontier measures separate the two:

- improvements completed per human judgment supplied;
- computational steps between human interventions;
- proportion of candidates accepted or rejected computationally;
- breadth of artifacts changeable without bespoke human instruction;
- the difficulty frontier at which human intervention becomes necessary.

Concretely: a session that drafts a note, validates it, discovers its connections, and commits, with one human judgment at the merge, has several computational steps per intervention; the same note produced by dictation has nearly none — at identical human hours.

These are proxies, and comparing them across time inherits the open commensurability problem — the function list itself changes as the system grows, [since measuring autonomy well enough to see it improve is an open problem]. What this note adds is the purpose such measurement should serve: not “are humans spending fewer hours?” but “is the intervention frontier moving outward?”

## Scope

- The claim concerns computational allocation, not methodological closure: a person can execute a settled gate, while an unattended model can improvise. The two often advance together when settled criteria become executable, [but they track different changes].
- The load-bearing premise is the elastic backlog. Where the workload is genuinely fixed — a bounded migration, a system in maintenance-only mode — increasing computational autonomy *should* reduce human hours, and observing it there would confirm the mechanism rather than refute this note.
- The pattern is stated from one system class (agent-operated knowledge systems, [Commonplace among them]) and Bainbridge's industrial precedent; whether it holds across self-improving systems generally is the conjecture.

## Open Questions

- Whether intervention density and computational run length can be recovered retroactively from repository history, giving the frontier claim a cheap first test.
- Whether the difficulty frontier can be operationalized at all, or only ranked ordinally by cases that did and did not need intervention.

---

Relevant Notes:

## Artifact B

# Methodological and computational closure track different changes

An improvement pathway can stop depending on improvised judgment without stopping its dependence on a human actor, and it can stop depending on a human actor while continuing to improvise. Those are different architectural changes and need different readings of **closure**.

**Methodological closure** asks whether the retained methodology settles the consequential decisions that the pathway raises. A method is less closed where it merely says “use judgment,” names an approver, or leaves a meta-decision to be reconstructed from scratch.

**Computational closure** asks who supplies the decision. A function is computationally closed when its execution needs no human decision; a whole pathway is computationally closed only when every required function meets that condition.

Computational closure and machine autonomy therefore read the same actor allocation: human, computational, or joint for each pathway function. “More computationally autonomous” describes movement in that allocation; “more computationally closed” describes the resulting reduction in functions that still require a human decision.

Neither reading is the cybernetic sense. **Organizational closure** — the recursive regeneration of a network of component interactions in the autopoiesis tradition — is a different property, already excluded from this cluster's vocabulary in the [reflective-system exclusions]; nothing here asserts or requires it.

## Human-inclusive boundaries make allocation load-bearing

A [reflective system] may include established human processes. Put a maintainer with a standing causal role inside the boundary of a maintained system with readable source, and reflective attribution becomes cheap: the maintainer inspects the source as a representation, edits it, and the build carries the edit into operation. The attribution can be true while saying little about machine performance.

Actor allocation restores the missing discrimination. Under a fixed human-inclusive boundary, report each consequential function as human, computational, or joint; computational closure is the no-human endpoint of that profile. Do not replace the profile with a percentage: functions differ in decomposition, authority, and stakes, and cross-system comparison remains [an open measurement problem].

The form is inherited rather than invented. [Parasuraman, Sheridan, and Wickens] report automation per function — information acquisition, analysis, decision and action selection, action implementation — and hold that an allocation is judged by its performance consequences, its reliability, and the cost of the consequences it admits, not by how much of the work the machine has taken over. That shape is what carries across, with three departures. The functions allocated here are the improvement pathway's own — search, evaluation, and retention where the pathway is proposal-selection — rather than task-performance stages. Their within-function ten-level scale is not inherited: the paper's validation is strongest for decision selection, and a graded level per function would reintroduce the percentage this profile refuses. And allocation still establishes nothing about warrant.

## Four concrete combinations

| Improvement decision | Methodologically closed? | Computationally closed? | Why |
|---|---:|---:|---|
| A maintainer manually applies an exact checklist before accepting a patch | Yes | No | The criterion is settled, but a human supplies the verdict. |
| A validator accepts an artifact only when an exact structural predicate holds | Yes | Yes | The criterion and its execution are both explicit and computational. |
| An unattended coding agent is told to inspect failures and “improve the repository” using its own judgment | No | Yes | No human intervenes, but consequential choices remain improvised. |
| A maintainer and agent jointly judge a theory note against “is this good?” | No | No | The criterion is unsettled and a human participates in the verdict. |

Stable but tacit expertise does not count as retained methodology. A maintainer may apply a repeatable internal criterion that was never externalized — settled in practice, unsettled in representation — but methodological closure reads the representation, and the reading has one ground rather than a human-specific rule, [since only explicit retention is currently durable, writable, and addressable at once]: a criterion that cannot be retrieved, cited, criticized, or selectively revised is not available to the pathway as methodology, however consistently it is applied — it is available only as the human actor. The state deserves its own name instead of a closure grade: stable-but-unexternalized practice is a promotion candidate, noticeable by recurrence and convertible by externalization. The last row therefore stands even when the joint judgment is secretly consistent.

The third row needs a named exclusion, not a stronger definition. Computational closure reads actor allocation within the declared frame: a hosted model is a computational actor wherever it runs, so a pathway can be computationally closed while depending on inference infrastructure and a provider outside the selected subsystem. That dependency is real, but it is a boundary and coverage fact — in profile terms, selection-grade coverage of a sealed parametric component, [as reflective coverage is graded across representational forms] — not an actor fact. Widening closure to swallow substrate dependency would leave almost no model-mediated function ever computationally closed and destroy the discrimination the table exists to provide, the same reason the organizational-closure sense is excluded above.

## When the two changes advance together

A recurring human decision becomes easier to allocate computationally after its inputs, criterion, and failure response have been made explicit. The conversion usually has three parts:

1. **Representation** — the relevant inputs and commitments become available to the deciding process, [since reflection buys addressability].
2. **Settlement** — the methodology supplies the criterion or determines the result instead of merely naming a decider, [since a methodology governs its own extension only as far as it settles the meta-decisions it raises].
3. **Warranted execution** — a computational procedure or oracle implements the criterion with evidence adequate to the case, [since warranted autonomy is bounded by oracle domain].

The order is forced, not conventional: externalization is allocation's transport. A computational actor can receive a criterion only through an explicit representation — under a selection-only parametric profile nothing else inside the boundary is both writable and durable, and even where fine-tuning adds a write channel the transfer is unaddressable, escaping governance at the moment it succeeds ([only explicit retention is currently durable, writable, and addressable at once]).

These are engineering dependencies, not definitions of one another. A settled gate can remain human-executed; an agent can read explicit commitments yet improvise how to apply them; and a computational procedure can encode a poor proxy. Moving evaluation to a model changes allocation without establishing that its acceptances are trustworthy.

The [Commonplace reference case] applies this conversion to ADR 026 and keeps the trace-specific facts in one place.

## Reflection is a separate question

Reflectivity does not require methodological closure. It requires a causally connected representation of the system's own behavior that processes inside the declared frame can read and change. A reflective pathway may expose its rules for criticism while leaving the next revision to open-ended judgment. Conversely, a fixed pipeline may settle every operational choice without representing or revising itself.

The properties reinforce each other when the represented object is the improvement methodology itself: an addressable criterion can be revised, then a settled and warranted version can be executed computationally. That is a trajectory through a [multi-part profile], not one scale of reflectivity or closure.

## Scope

- Both closure readings are per decision and per pathway, so mixed profiles are normal: exact validators can coexist with joint review, and settled acceptance rules with improvised objective-setting.
- A loop instance **completes** when search, evaluation, and operative retention occur. Calling that event closure would conflate completion with architecture.
- Both readings require a declared frame. A whole-system closure claim without named decisions and pathways hides the mixed architecture.
- Comparing allocation profiles across releases or systems inherits the open commensurability problem: [measuring autonomy well enough to see it improve is an open problem].

## Open Questions

- When an initial human instruction makes a downstream agent-performed function joint rather than computational; counting every instruction hides agent performance, while counting none hides decision content supplied up front.
- Whether objective-setting can become methodologically closed without freezing the improvement objective rather than improving it.
- How much representational explicitness computational internalization requires when learned components can execute a decision without exposing its criterion.
- How to distinguish a computational implementation of a settled method from a proxy that silently changes what the method decides.

---

Relevant Notes:

## Under-review context phrase

identifies computational closure as an actor-allocation endpoint rather than methodological settlement
