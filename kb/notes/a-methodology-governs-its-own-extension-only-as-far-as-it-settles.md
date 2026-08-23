---
description: "A methodology governs its own extension only as far as it settles the meta-decisions its recommendations raise — representational form, verification, and authority"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, constraining, self-improving-systems]
---

# A methodology governs its own extension only as far as it settles the meta-decisions it raises

A [methodology](./definitions/actionable-methodology.md) maps represented conditions to a choice among interventions, and is actionable for an operator who can carry that choice through. But when the system a methodology governs is asked to extend *itself* by following that methodology, its prescriptions raise further decisions. Extension proceeds under the methodology's governance only as far as the methodology settles those decisions. Call this **closure under its own recommendations**.

## Closure is a stronger property than reflection

A [reflective system](./definitions/reflective-system.md) has a causally connected self-representation available to its own processes. That is a structural condition, and it is weaker than closure. A reflective system may modify itself without possessing any methodology that governs how those modifications should be made — it changes, but nothing prescribes the change.

Closure asks a different question: how far can methodology-governed self-extension proceed before it must import a meta-decision the methodology does not supply? A system can be reflective without being closed, and a methodology can be closed on some axis for a system that never modifies itself at all.

## Closure reads retained methodology, not actor capability

Closure is a property of the retained methodology relative to a named pathway, not of any participant's unrecorded capabilities. The governed system may include human reviewers, agents, deterministic tools, and authority procedures. Their availability can make the methodology actionable, but it does not supply decision content the methodology leaves open. Closure asks whether the methodology settles each relevant meta-decision directly or explicitly imports a retained criterion or result that the pathway will use. The gap is where the retained method specifies or references nothing and an actor must improvise.

## Routing and decision content settle separately

A methodology can govern a decision three ways, and they are not equivalent:

1. **Name the decider.** "A maintainer approves this class of change." The routing is governed; the *content* of the decision is not.
2. **Supply or import criteria.** Hand over an explicit rule, or bind the pathway to an explicitly retained criterion elsewhere, so the retained materials constrain the choice rather than requiring the decider to invent its basis.
3. **Determine the result.** Leave nothing to decide — the methodology, or a tool it invokes, fixes the outcome.

Only the second and third provide decision-content closure, and a criterion closes content only as far as it constrains the answer. In the rest of this note, unqualified **closure** means decision-content closure.

Naming a decider closes routing, not decision content. Treating it as content closure would empty the concept: any methodology could close every axis by writing "ask the maintainer." A decider's stable but tacit criteria remain actor capability rather than retained methodology, [since only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md). The methodology need not duplicate a criterion, but it must explicitly reference a retained criterion or decision procedure that constrains or determines the result, and the pathway must operatively use it. If divergence is tolerable, the methodology can declare the choice outside the consequential decision set; that narrows the closure claim rather than settling the choice. Where the decision is consequential and divergence-prone, assignment alone leaves the frontier exactly where it was — which is why the three axes below demand criteria and oracles rather than owners.

The stakes are that improvised meta-decisions are where two sessions diverge, [since agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) rather than executing them.

## Three meta-decisions a recommendation raises

Carrying out a recommendation forces the system to settle:

1. **Representational form** — should the artifact stay in natural-language form to be interpreted, or be frozen into deterministic code, schema, or grammar? A methodology is closed on this axis when it hands over criteria rather than leaving the choice to be guessed. Commonplace supplies the [codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) and the [constraining gradient](./methodology-enforcement-is-constraining.md) from convention to code; the decision itself is [codification](./definitions/codification.md). Where a recommendation spans several representations, the choice extends to the mappings between them, since [reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md).
2. **Verification** — once the artifact exists, what establishes that it is correct? A methodology is closed on this axis when it tells the system which oracle to build or invoke. This is the binding constraint: an artifact can be produced only as reliably as it can be checked, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). A methodology closed on form but open on verification generates artifacts nobody can confirm — output, not automation.
3. **Authority and retention** — how does the accepted artifact acquire a consumer, a channel, and a force, so that it affects later behavior? In [behavioral authority](./definitions/behavioral-authority.md) terms, a recommendation that produces an artifact but specifies no consumption path leaves the change loop open. A methodology that prescribes a new gate without saying what invokes it, or a new note without saying who reads it, is not closed on this axis.

This is what a methodology's verification and authority machinery — typed artifacts, validators, review gates, routing contracts — is *for*: it raises the ceiling on how far the system can extend itself from the methodology alone.

## Worked application

The [Commonplace reference case](./evidence/commonplace-as-a-reflective-system.md) applies all three axes to ADR 026: form, verification, and authority were settled for the completeness mark, while noticing the design problem and choosing the type split remained improvised. The example lives there so this note owns the criterion rather than a second telling of the trace.

## Closure under recommendations is not search closure

Methodology-governed extension runs as a proposal-selection improvement loop, which also [requires search, evaluation, and retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md): something must find a candidate before anything can accept it. But search closure — how the system finds problems and generates candidates — is a different property from closure under recommendations, which asks how the system resolves the meta-decisions entailed by a recommendation it already has.

The three axes above belong to closure under recommendations because the recommendation itself raises each of them: the prescribed artifact must take some form, be checked somehow, and acquire force to matter. Search is a precondition of the loop, not a decision the recommendation forces. A methodology could separately prescribe how to search — Commonplace largely does not — but that is a claim about search closure, and it should be argued as one.

## Scope

- **Closure is a direction, not a binary.** No real methodology settles every extension decision it could face. The claim is that methodology-governed self-extension scales with how much it settles, and stalls at the first consequential meta-decision it leaves open — the self-extension frontier. What operates past that frontier has a named architecture: in [the two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md), dropping back to the generator layer — theory, or the judgment the methodology did not settle — is an expected operation, and recurring fallback results are promotion candidates that move the frontier outward.
- **The counter worth taking seriously.** A capable agent brings general competence and can improvise the decisions a methodology omits. Where that improvisation is reliable, closure buys less. The claim's force therefore tracks how *consequential and divergence-prone* the omitted decisions are. Choices whose divergence cannot affect the governed outcome are outside the assessed decision set rather than weakly closed.
- **Whether Commonplace is closed is a separate assessment.** This note supplies the criterion; the [reference case](./evidence/commonplace-as-a-reflective-system.md) applies it to one pathway, not the whole system.
- **Closure explains production, not retention.** Whether a codified artifact should then be kept rather than re-derived each session is a separate question. A persisted [symbolic artifact](./definitions/representational-form.md) can be deterministic and inspectable, but those properties do not by themselves settle its retention.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — contrasts: reflection is a structural condition on self-representation; closure is a stronger condition on methodology-governed change
- [Actionable methodology](./definitions/actionable-methodology.md) — grounds: supplies the methodology–operator–target relation a governed recommendation presupposes
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — contrasts: separates the change loop's functions from the meta-decisions a recommendation raises
- [Behavioral authority](./definitions/behavioral-authority.md) — enables: names the consumer, channel, and force the authority axis demands
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — extends: the representational-form axis widens to the mappings between forms when a recommendation spans them
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: why the verification axis is the ceiling
- [Commonplace as a reflective system](./evidence/commonplace-as-a-reflective-system.md) — evidenced-by: applies the three closure axes to the centralized ADR 026 trace
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — extends: the execution architecture past the closure frontier — fallback to the generator as expected operation, recurrence as the promotion signal that moves the frontier
- [Only explicit retention is currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: why an imported explicit criterion can belong to retained methodology while a decider's tacit criterion cannot
