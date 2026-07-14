---
description: "The error-correction asymmetry sorts agentic behavior between prose and code, so reliability-improving changes cross the boundary; reflective coverage of one form cannot carry them"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, constraining, reflective-systems]
---

# Improving an agentic system crosses the prose-symbolic boundary

In an agentic system — one whose operation runs through a model interpreting retained artifacts — the changes that improve reliability characteristically move behavior across the boundary between prose and symbolic form rather than staying within either. A self-representation covering only one form can therefore represent the side such a change starts from but not the side it must land on, and the change escapes governance at exactly the point where the improvement happens.

## The asymmetry sorts behavior between the forms

The engine is an error profile, [since scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md): work that can be fully specified — counting, membership, state tracking, scoping — is exact on a symbolic substrate and error-prone inside a model, while judgment that cannot be fully specified has nowhere to live but prose. A system under reliability pressure is therefore continuously sorting. New behavior enters as prose, because prose is where a half-understood constraint can first be stated; as operation clarifies which part of it is bookkeeping, that part is pushed into code. The movement is [codification](./definitions/codification.md), the pressure behind it is the [constraining gradient from convention to enforcement](./methodology-enforcement-is-constraining.md), and the sorting is never finished, because codifying a rule requires an oracle for it and [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

## The improving changes are crossings

The sorting runs in both directions, and each direction is a boundary crossing:

**Prose to symbolic.** A convention that decays into violations becomes a validator; a membership claim becomes an enforced mark. The improvement is precisely the acquisition of a formal consumer — the unenforced prose version of a completeness claim is a trap, [since stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md): it tells an exhaustive consumer to stop looking while members are missing. What made the system more reliable was not better prose but the crossing itself.

**Symbolic to prose.** An enforcement that misfires — rejecting what it should accept, or encoding a decision the system has outgrown — cannot be fixed by editing code alone, because the fix must be *derived* from somewhere. The correction runs through the recorded rationale: revise the intent, then re-derive the rule. Enforcement whose rationale is not revisable drifts opaque; prose whose enforcement is not updatable decays into advice.

Changes confined to one form exist — rewording a note, refactoring under a fixed contract — but they polish behavior rather than change what the system can rely on. The reliability gains concentrate where interpretation is replaced by enforcement, or enforcement is re-grounded in revised intent.

## Consequence for reflective coverage

[Since reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md), the question is which grades suffice, and for agentic systems the answer follows from where the improving changes live. Prose-only coverage lets the system revise what it recommends but not what it enforces, so accepted recommendations accumulate as advice. Symbolic-only coverage lets it adjust what it enforces but not why, so enforcement loses its path back to intent. Either way, the improving change must be made outside the self-representation — out-of-band intervention, which is the failure reflection exists to remove. Governed self-extension in an agentic system therefore needs modification-depth coverage of both forms, and of the mappings between them.

## Scope

- The claim characterizes where reliability gains concentrate under the stated pressure; it is not a universal over every improvement. A system without reliability pressure, or with no formal consumers at all, is outside the argument.
- It concerns the prose-symbolic pair. The distributed-parametric form sits under selection-grade levers in current agent systems, and this argument does not extend to it.
- The mechanism carries the claim; the direct evidence base is currently one repository trace — a single decision landing as prose spec, schema, validator, and renderer in one commit, and a symbolic check later catching a member the prose recipe had missed. Classifying external agent-memory systems by which forms their improvements touch would test the claim beyond this repository.

---

Relevant Notes:

- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: supplies the form and operation-depth vocabulary this claim selects sufficient grades from
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: the error profile that sorts bookkeeping into code and judgment into prose
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: the representational-form meta-decision a recommendation raises is, by this claim, the decision most improvements must settle
- [Codification](./definitions/codification.md) — defined-in: the prose-to-symbolic crossing
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: the observed trace where one decision crossed into four forms and a symbolic check corrected the prose recipe
