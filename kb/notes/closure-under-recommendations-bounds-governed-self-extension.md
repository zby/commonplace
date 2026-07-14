---
description: "A methodology governs its own extension only as far as it settles the meta-decisions its recommendations raise — representational form, verification, and authority"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, constraining, reflective-systems]
---

# Closure under recommendations bounds methodology-governed self-extension

A methodology is a theory for design and action: in the hands of an operator that can follow it, it is an [actionable theory](./definitions/actionable-theory.md), mapping represented conditions to a choice among interventions. But when the system a methodology governs is asked to extend *itself* by following that methodology, its prescriptions raise further decisions. Extension proceeds under the methodology's governance only as far as the methodology settles those decisions. Call this **closure under its own recommendations**.

## Closure is not reflection

A [reflective system](./definitions/reflective-system.md) has a causally connected self-representation available to its own processes. That is a structural condition, and it is weaker than closure. A reflective system may modify itself without possessing any methodology that governs how those modifications should be made — it changes, but nothing prescribes the change.

Closure asks a different question: how far can methodology-governed self-extension proceed before it must import a meta-decision the methodology does not supply? A system can be reflective without being closed, and a methodology can be closed on some axis for a system that never modifies itself at all.

## The system, not the lone agent

Closure is a property of the methodology-as-input, not of any one system or agent's capabilities. The governed system may include human reviewers, agents, deterministic tools, and authority procedures. Closure asks whether that combined system has a governed route for each relevant meta-decision — not whether one model can act unassisted. Where a methodology specifies "a maintainer approves this class of change," that is a closure, not a gap: the decision has a governed route. The gap is where the methodology specifies nothing and someone must improvise.

This matters because improvised meta-decisions are where two sessions diverge, [since agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) rather than executing them.

## Three meta-decisions a recommendation raises

Carrying out a recommendation forces the system to settle:

1. **Representational form** — should the artifact stay prose to be interpreted, or be frozen into deterministic code, schema, or grammar? A methodology is closed on this axis when it hands over criteria rather than leaving the choice to be guessed. Commonplace supplies the [codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) and the [constraining gradient](./methodology-enforcement-is-constraining.md) from convention to code; the decision itself is [codification](./definitions/codification.md). Where a recommendation spans several representations, the choice extends to the mappings between them, since [reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md).
2. **Verification** — once the artifact exists, what establishes that it is correct? A methodology is closed on this axis when it tells the system which oracle to build or invoke. This is the binding constraint: an artifact can be produced only as reliably as it can be checked, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). A methodology closed on form but open on verification generates artifacts nobody can confirm — output, not automation.
3. **Authority and retention** — how does the accepted artifact acquire a consumer, a channel, and a force, so that it affects later behavior? In [behavioral authority](./definitions/behavioral-authority.md) terms, a recommendation that produces an artifact but specifies no consumption path leaves the change loop open. A methodology that prescribes a new gate without saying what invokes it, or a new note without saying who reads it, is not closed on this axis.

This is what a methodology's verification and authority machinery — typed artifacts, validators, review gates, routing contracts — is *for*: it raises the ceiling on how far the system can extend itself from the methodology alone.

## Closure under recommendations is not search closure

The full change loop also [requires search, evaluation, and retention](./governed-adaptation-requires-search-evaluation-and-retention.md): something must find a candidate before anything can accept it. But search closure — how the system finds problems and generates candidates — is a different property from closure under recommendations, which asks how the system resolves the meta-decisions entailed by a recommendation it already has.

The three axes above belong to closure under recommendations because the recommendation itself raises each of them: the prescribed artifact must take some form, be checked somehow, and acquire force to matter. Search is a precondition of the loop, not a decision the recommendation forces. A methodology could separately prescribe how to search — Commonplace largely does not — but that is a claim about search closure, and it should be argued as one.

## Scope

- **Closure is a direction, not a binary.** No real methodology settles every extension decision it could face. The claim is that methodology-governed self-extension scales with how much it settles, and stalls at the first consequential meta-decision it leaves open. The self-extension frontier is that first open decision.
- **The counter worth taking seriously.** A capable agent brings general competence and can improvise the decisions a methodology omits. Where that improvisation is reliable, closure buys less. The claim's force therefore tracks how *consequential and divergence-prone* the omitted decisions are — high for what-to-codify, how-to-verify, and what-grants-force; low for cosmetic choices.
- **Why the artifact is retained, not re-derived.** Closure explains how the system produces a codified artifact from the methodology; retention is a separate argument. A persisted symbolic artifact is deterministic and inspectable, while re-derivation pays the cost each session and risks divergent interpretations. In agent systems [the prescription/implementation boundary collapses](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — the prescription and the code it becomes are the same retained thing at different points on the constraining gradient.

---

Relevant Notes:

- [Reflective system](./definitions/reflective-system.md) — contrasts: reflection is a structural condition on self-representation; closure is a stronger condition on methodology-governed change
- [Actionable theory](./definitions/actionable-theory.md) — grounds: supplies the theory–operator–target relation a governed recommendation presupposes
- [Governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — contrasts: separates the change loop's functions from the meta-decisions a recommendation raises
- [Behavioral authority](./definitions/behavioral-authority.md) — enables: names the consumer, channel, and force the authority axis demands
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — extends: the representational-form axis widens to the mappings between forms when a recommendation spans them
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — mechanism: why the verification axis is the ceiling
