# Case packet

Neutral case identifier: case-3d16fd3a85e16a

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

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

## Artifact B

# A methodology governs its own extension only as far as it settles the meta-decisions it raises

A [methodology] maps represented conditions to a choice among interventions, and is actionable for an operator who can carry that choice through. But when the system a methodology governs is asked to extend *itself* by following that methodology, its prescriptions raise further decisions. Extension proceeds under the methodology's governance only as far as the methodology settles those decisions. Call this **closure under its own recommendations**.

## Closure is a stronger property than reflection

A [reflective system] has a causally connected self-representation available to its own processes. That is a structural condition, and it is weaker than closure. A reflective system may modify itself without possessing any methodology that governs how those modifications should be made — it changes, but nothing prescribes the change.

Closure asks a different question: how far can methodology-governed self-extension proceed before it must import a meta-decision the methodology does not supply? A system can be reflective without being closed, and a methodology can be closed on some axis for a system that never modifies itself at all.

## The system, not the lone agent

Closure is a property of the methodology-as-input, not of any one system or agent's capabilities. The governed system may include human reviewers, agents, deterministic tools, and authority procedures. Closure asks whether that combined system has a governed route for each relevant meta-decision — not whether one model can act unassisted. The gap is where the methodology specifies nothing and someone must improvise.

## Closure comes in three strengths

A methodology can settle a decision three ways, and they are not equivalent:

1. **Name the decider.** "A maintainer approves this class of change." The routing is governed; the *content* of the decision is not.
2. **Supply criteria.** Hand over a rule the decider applies, so two competent operators reach the same answer.
3. **Determine the result.** Leave nothing to decide — the methodology, or a tool it invokes, fixes the outcome.

Naming a decider is the weakest, and treating it as full closure would empty the concept: any methodology could close every axis by writing "ask the maintainer." It is a real closure only where the assigned decider carries criteria the methodology need not restate, or where divergence on that decision is tolerable. Where the decision is consequential and divergence-prone, assignment alone leaves the frontier exactly where it was — which is why the three axes below demand criteria and oracles rather than owners.

The stakes are that improvised meta-decisions are where two sessions diverge, [since agentic systems interpret underspecified instructions] rather than executing them.

## Three meta-decisions a recommendation raises

Carrying out a recommendation forces the system to settle:

1. **Representational form** — should the artifact stay in natural-language form to be interpreted, or be frozen into deterministic code, schema, or grammar? A methodology is closed on this axis when it hands over criteria rather than leaving the choice to be guessed. Commonplace supplies the [codify-versus-LLM decision heuristics] and the [constraining gradient] from convention to code; the decision itself is [codification]. Where a recommendation spans several representations, the choice extends to the mappings between them, since [reflective coverage is graded across representational forms].
2. **Verification** — once the artifact exists, what establishes that it is correct? A methodology is closed on this axis when it tells the system which oracle to build or invoke. This is the binding constraint: an artifact can be produced only as reliably as it can be checked, [since the boundary of automation is the boundary of verification]. A methodology closed on form but open on verification generates artifacts nobody can confirm — output, not automation.
3. **Authority and retention** — how does the accepted artifact acquire a consumer, a channel, and a force, so that it affects later behavior? In [behavioral authority] terms, a recommendation that produces an artifact but specifies no consumption path leaves the change loop open. A methodology that prescribes a new gate without saying what invokes it, or a new note without saying who reads it, is not closed on this axis.

This is what a methodology's verification and authority machinery — typed artifacts, validators, review gates, routing contracts — is *for*: it raises the ceiling on how far the system can extend itself from the methodology alone.

## Worked application

The [Commonplace reference case] applies all three axes to ADR 026: form, verification, and authority were settled for the completeness mark, while noticing the design problem and choosing the type split remained improvised. The example lives there so this note owns the criterion rather than a second telling of the trace.

## Closure under recommendations is not search closure

Methodology-governed extension runs as a proposal-selection improvement loop, which also [requires search, evaluation, and retention]: something must find a candidate before anything can accept it. But search closure — how the system finds problems and generates candidates — is a different property from closure under recommendations, which asks how the system resolves the meta-decisions entailed by a recommendation it already has.

The three axes above belong to closure under recommendations because the recommendation itself raises each of them: the prescribed artifact must take some form, be checked somehow, and acquire force to matter. Search is a precondition of the loop, not a decision the recommendation forces. A methodology could separately prescribe how to search — Commonplace largely does not — but that is a claim about search closure, and it should be argued as one.

## Scope

- **Closure is a direction, not a binary.** No real methodology settles every extension decision it could face. The claim is that methodology-governed self-extension scales with how much it settles, and stalls at the first consequential meta-decision it leaves open — the self-extension frontier. What operates past that frontier has a named architecture: in [the two-layer execution system], dropping back to the generator layer — theory, or the judgment the methodology did not settle — is an expected operation, and recurring fallback results are promotion candidates that move the frontier outward.
- **The counter worth taking seriously.** A capable agent brings general competence and can improvise the decisions a methodology omits. Where that improvisation is reliable, closure buys less. The claim's force therefore tracks how *consequential and divergence-prone* the omitted decisions are — high for what-to-codify, how-to-verify, and what-grants-force; low for cosmetic choices.
- **Whether Commonplace is closed is a separate assessment.** This note supplies the criterion; the [reference case] applies it to one pathway, not the whole system.
- **Closure explains production, not retention.** Why the codified artifact is then kept rather than re-derived each session is a separate argument — a persisted symbolic artifact is deterministic and inspectable, and in agent systems [the prescription and the code it becomes are the same retained thing] at different points on the constraining gradient.

---

Relevant Notes:

## Under-review context phrase

supplies the methodological reading of closure
