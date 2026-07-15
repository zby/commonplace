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

## The system, not the lone agent

Closure is a property of the methodology-as-input, not of any one system or agent's capabilities. The governed system may include human reviewers, agents, deterministic tools, and authority procedures. Closure asks whether that combined system has a governed route for each relevant meta-decision — not whether one model can act unassisted. The gap is where the methodology specifies nothing and someone must improvise.

## Closure comes in three strengths

A methodology can settle a decision three ways, and they are not equivalent:

1. **Name the decider.** "A maintainer approves this class of change." The routing is governed; the *content* of the decision is not.
2. **Supply criteria.** Hand over a rule the decider applies, so two competent operators reach the same answer.
3. **Determine the result.** Leave nothing to decide — the methodology, or a tool it invokes, fixes the outcome.

Naming a decider is the weakest, and treating it as full closure would empty the concept: any methodology could close every axis by writing "ask the maintainer." It is a real closure only where the assigned decider carries criteria the methodology need not restate, or where divergence on that decision is tolerable. Where the decision is consequential and divergence-prone, assignment alone leaves the frontier exactly where it was — which is why the three axes below demand criteria and oracles rather than owners.

The stakes are that improvised meta-decisions are where two sessions diverge, [since agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) rather than executing them.

## Three meta-decisions a recommendation raises

Carrying out a recommendation forces the system to settle:

1. **Representational form** — should the artifact stay prose to be interpreted, or be frozen into deterministic code, schema, or grammar? A methodology is closed on this axis when it hands over criteria rather than leaving the choice to be guessed. Commonplace supplies the [codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) and the [constraining gradient](./methodology-enforcement-is-constraining.md) from convention to code; the decision itself is [codification](./definitions/codification.md). Where a recommendation spans several representations, the choice extends to the mappings between them, since [reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md).
2. **Verification** — once the artifact exists, what establishes that it is correct? A methodology is closed on this axis when it tells the system which oracle to build or invoke. This is the binding constraint: an artifact can be produced only as reliably as it can be checked, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). A methodology closed on form but open on verification generates artifacts nobody can confirm — output, not automation.
3. **Authority and retention** — how does the accepted artifact acquire a consumer, a channel, and a force, so that it affects later behavior? In [behavioral authority](./definitions/behavioral-authority.md) terms, a recommendation that produces an artifact but specifies no consumption path leaves the improvement loop open. A methodology that prescribes a new gate without saying what invokes it, or a new note without saying who reads it, is not closed on this axis.

This is what a methodology's verification and authority machinery — typed artifacts, validators, review gates, routing contracts — is *for*: it raises the ceiling on how far the system can extend itself from the methodology alone.

## A worked case: the `complete` mark

Commonplace's [ADR 026](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) carries out one recommendation — *a tag head may claim it links every note carrying the tag* — and settles all three axes, which is what makes it a closure rather than an improvisation.

- **Form.** The methodology supplied the criterion, not the answer: a completeness claim is worthless unless machine-enforced, [since stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md). That decided the crossing into symbolic form — a frontmatter field plus a schema — rather than leaving prose to be trusted.
- **Verification.** The oracle was named with the artifact: the validator checks membership using the same query the documented `rg` recipe uses. The check is what the mark *means*, so the mark could not have shipped unenforced.
- **Authority and retention.** The mark acquires a consumer (`cp-skill-connect` skips the by-tag sweep when it is present), a channel (the validator, run on the head), and a force (a missing member fails validation). The failure message even names the instruction that fixes it, closing the loop back into the maintenance path.

Because all three were settled, the extension proceeded without anyone improvising. And the case locates the frontier precisely: nothing in the methodology prescribed *noticing* that the `index` type was doing two jobs at once, or that an unenforced completeness claim is a trap. That came from a person. Closure held over the recommendation and ran out at search — which is the distinction the next section draws.

## Closure under recommendations is not search closure

The full improvement loop also [requires search, evaluation, and retention](./an-improvement-loop-requires-search-evaluation-and-operative-retention.md): something must find a candidate before anything can accept it. But search closure — how the system finds problems and generates candidates — is a different property from closure under recommendations, which asks how the system resolves the meta-decisions entailed by a recommendation it already has.

The three axes above belong to closure under recommendations because the recommendation itself raises each of them: the prescribed artifact must take some form, be checked somehow, and acquire force to matter. Search is a precondition of the loop, not a decision the recommendation forces. A methodology could separately prescribe how to search — Commonplace largely does not — but that is a claim about search closure, and it should be argued as one.

## Scope

- **Closure is a direction, not a binary.** No real methodology settles every extension decision it could face. The claim is that methodology-governed self-extension scales with how much it settles, and stalls at the first consequential meta-decision it leaves open. The self-extension frontier is that first open decision.
- **The counter worth taking seriously.** A capable agent brings general competence and can improvise the decisions a methodology omits. Where that improvisation is reliable, closure buys less. The claim's force therefore tracks how *consequential and divergence-prone* the omitted decisions are — high for what-to-codify, how-to-verify, and what-grants-force; low for cosmetic choices.
- **Whether Commonplace is closed is a separate assessment.** This note supplies the criterion, not the verdict. One recommendation traced end-to-end shows the axes can be settled; it does not show they usually are, and [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) establishes only the weaker structural property, leaving closure unassessed. The full per-axis assessment is open work for the reference layer.
- **Closure explains production, not retention.** Why the codified artifact is then kept rather than re-derived each session is a separate argument — a persisted symbolic artifact is deterministic and inspectable, and in agent systems [the prescription and the code it becomes are the same retained thing](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) at different points on the constraining gradient.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — contrasts: reflection is a structural condition on self-representation; closure is a stronger condition on methodology-governed change
- [Actionable methodology](./definitions/actionable-methodology.md) — grounds: supplies the methodology–operator–target relation a governed recommendation presupposes
- [An improvement loop requires search, evaluation, and operative retention](./an-improvement-loop-requires-search-evaluation-and-operative-retention.md) — contrasts: separates the improvement loop's functions from the meta-decisions a recommendation raises
- [Behavioral authority](./definitions/behavioral-authority.md) — enables: names the consumer, channel, and force the authority axis demands
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — extends: the representational-form axis widens to the mappings between forms when a recommendation spans them
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: why the verification axis is the ceiling
- [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — grounds: the criterion that settled the form axis in the worked case — an unenforced completeness claim is a trap, not a weaker version of the enforced one
- [ADR 026: tag-readme type with completeness and coverage marks](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — evidence: the worked case, where form, verification, and authority were all settled and the frontier fell at search
