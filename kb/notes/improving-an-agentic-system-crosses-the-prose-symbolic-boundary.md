---
description: "The error-correction asymmetry sorts agentic behavior between prose and code, so reliability-improving changes cross the boundary; reflective coverage of one form cannot carry them"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, constraining, self-improving-systems]
---

# Improving an agentic system crosses the prose-symbolic boundary

In an agentic system — one whose operation runs through a model interpreting retained artifacts — the changes that improve reliability characteristically move behavior across the boundary between prose and symbolic form rather than staying within either. A self-representation covering only one form can therefore represent the side such a change starts from but not the side it must land on, and the change escapes governance at exactly the point where the improvement happens.

## The asymmetry sorts behavior between the forms

The engine is an error profile, [since scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md): work that can be fully specified — counting, membership, state tracking, scoping — is exact on a symbolic substrate and error-prone inside a model, while judgment that cannot be fully specified has nowhere to live but prose. A system under reliability pressure is therefore continuously sorting. New behavior enters as prose, because prose is where a half-understood constraint can first be stated; as operation clarifies which part of it is bookkeeping, that part is pushed into code. The movement is [codification](./definitions/codification.md), the pressure behind it is the [constraining gradient from convention to enforcement](./methodology-enforcement-is-constraining.md), and the sorting is never finished, because codifying a rule requires an oracle for it and [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md).

## The improving changes are crossings

The sorting runs in both directions, and each direction is a boundary crossing:

**Prose to symbolic.** A convention that decays into violations becomes a validator; a membership claim becomes an enforced mark. The improvement is precisely the acquisition of a formal consumer — the unenforced prose version of a completeness claim is a trap, [since stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md): it tells an exhaustive consumer to stop looking while members are missing. What made the system more reliable was not better prose but the crossing itself.

The [Commonplace reference case](../reference/commonplace-as-a-reflective-system.md) records one observed crossing in which a prose completeness rule acquired formal consumers.

**Symbolic to prose.** An enforcement cannot be repaired from inside itself, because the standard it should have applied is not in the code — the code *is* the thing under suspicion. The correction has to land in prose. That happens two ways: the enforcement misfires, rejecting what it should accept or encoding a decision the system has outgrown, and the rule must be re-derived from revised intent; or the enforcement runs correctly and its output shows that the prose was wrong. Enforcement whose rationale is not revisable drifts opaque; prose whose enforcement is not updatable decays into advice.

The same [reference case](../reference/commonplace-as-a-reflective-system.md) records the reverse crossing: symbolic execution exposed a faulty prose search recipe, which was then revised.

Changes confined to one form exist, and some of them matter: a code-only bug fix under an unchanged prose contract genuinely improves reliability. The claim is not that single-form changes are worthless but that they cannot move the *line* — what the system leaves to interpretation and what it enforces. Moving that line is what a crossing is, and it is where the reliability gains that survive a change of operator concentrate.

## Consequence for reflective coverage

[Since reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md), the question is which grades suffice, and for agentic systems the answer follows from where the improving changes live. Prose-only coverage lets the system revise what it recommends but not what it enforces, so accepted recommendations accumulate as advice. Symbolic-only coverage lets it adjust what it enforces but not why, so enforcement loses its path back to intent. Either way the improving change lands outside the self-representation, so it reaches later behavior without passing through anything the system represents about itself — and nothing in the loop governs it. Governed self-extension in an agentic system therefore needs modification-grade coverage of both forms, and of the mappings between them.

## Scope

- The claim characterizes where reliability gains concentrate under the stated pressure; it is not a universal over every improvement. A system without reliability pressure, or with no formal consumers at all, is outside the argument.
- It concerns the prose-symbolic pair. The distributed-parametric form sits under selection-grade levers in current agent systems, and this argument does not extend to it.
- The mechanism carries the claim; the direct evidence base is the single repository trace used in both directions above, set out in full in [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md). One trace is not a sample; classifying external agent systems by which forms their improvements touch is the test beyond this repository. A first such classification: [Knowledge-Centric Self-Improvement](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) is a prose-only improvement loop — accepted claims accumulate as advice to fresh agents, as prose-only coverage predicts — that succeeds because its symbolic half, benchmark verification, is supplied externally, fixed, and already adequate, so the enforcement line never needs to move; the settings its authors leave untested are those where it would.

---

Relevant Notes:

- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — grounds: supplies the form and operation-profile vocabulary this claim selects sufficient grades from
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — mechanism: the error profile that sorts bookkeeping into code and judgment into prose
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: the representational-form meta-decision a recommendation raises is, by this claim, the decision most improvements must settle
- [Codification](./definitions/codification.md) — defined-in: the prose-to-symbolic crossing
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: the observed trace where one decision crossed into four forms and a symbolic check corrected the prose recipe
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — contrasts: an orthogonal axis of improvement movement — theory-to-methodology promotion can stay prose-to-prose, and only its codification special case crosses the form boundary
- [Knowledge-Centric Self-Improvement ingest](../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) — evidence: a first external classification — a prose-only improvement loop whose gains sit inside fixed, externally supplied symbolic verification
