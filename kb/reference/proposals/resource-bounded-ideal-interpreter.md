---
description: "Proposal: a resource-bounded ideal interpreter as an attribution device separating errors in interpreting a theory from errors in the theory; the scope to declare, fidelity criteria, completion and abstention, and stress tests before adoption"
type: ../types/design-proposal.md
tags: [foundations, learning-theory]
traits: [has-external-sources]
---

# Resource-bounded ideal interpreter

A [theory builder](../../notes/definitions/theory-builder.md) interprets
theories, cases, and consequences to derive predictions, identify candidate
faults, and assess revisions. When a product fails, the failure may lie in
the theory or in how it was read, and no outcome absorbs both. This proposal
holds the design object for a standard that separates the two: an
interpreter idealized for faithful reading on a declared class of tasks,
under a resource model, whose attempts at conceptual development stay
conjectural. It was worked out in the theory-builder workshop between
2026-09-14 and 2026-09-17 and deferred from the main outcome comparison,
because [a claim without external assessment carries three obligations](../../notes/a-claim-without-external-assessment-carries-three-obligations.md)
and attribution is the third: an externally tested builder can score a
failure without attributing it, and needs this device only for a claim that
asserts a cause. Nothing here is shipped or adopted.

## Current state (as of 2026-09-17)

- The library definitions treat interpretation as a role inside the builder
  and name this device without adopting it. The externally tested case
  records a performance failure without attributing it; attribution binds a
  claim that asserts a cause, and a performance claim only where no
  independent outcome level absorbs interpretation and theory errors
  together.
- The workshop withdrew the earlier guarantee that budget exhaustion is the
  only failure the idealization admits. No guarantee for completed
  interpretations has been established on any specified class.
- The KB's use of *semantic work* is the judgment of meaning and relevance
  in [semantic work can be relocated but not eliminated](../../notes/semantic-work-can-be-relocated-but-not-eliminated.md);
  this proposal extends it with conceptual revision.
- No implementation has been compared to the standard, and no probe suite
  exists for estimating a model's knowledge and procedures.

## Problem

Give an evaluation a standard against which to score a real interpreter on
the tasks it completed, so that an error in interpreting a theory can be
separated from an error in the theory, without the standard assuming the
results the builder is meant to achieve. The standard must permit new
subjects and concepts, charge for the work it performs, admit unresolved
results without making abstention vacuous, and stay consistent when applied
to the builder's theory of itself.

## Semantic work

**Semantic work** is establishing, examining, or revising how expressions
and concepts represent a subject and bear on a question. It makes explicit
the referents, distinctions, commitments, scope, and relevant consequences
of a representation, or proposes changes to them when the current
representation is inadequate. A representation may be a theory, model,
instruction, specification, or account of a case. Interpreting a claim does
not include deciding it: a conjecture may remain unresolved after
successful interpretation.

The work is bounded by its contribution, not by subject area. The same
agent may perform semantic and other work in one episode; executing a fixed
calculation discharges an obligation semantic work identified without
revising an interpretation, and coding includes semantic work when it
settles what a requirement commits the implementation to.

| Operation | Output that makes the work reviewable |
|---|---|
| Interpret an existing expression | A reading with its referents, commitments, contextual assumptions, and consequential ambiguities identified |
| Relate a case to a concept | Grounds for including, excluding, or leaving the case undecided under the concept's stated scope |
| Connect commitments to consequences | A relevant conditional consequence or test obligation, with the premises it depends on |
| Criticize a representation | A conflict, missing distinction, scope failure, or rival interpretation, with the case that makes it matter |
| Develop or revise concepts | A candidate distinction, mechanism, vocabulary, or decomposition, with what changes in interpretation or expected consequences |
| Translate between representations | A mapping of commitments: preserved, omitted, added, still unsettled |

Interpretation and invention have different success conditions. A reading
can misrepresent commitments the context already fixed; a proposed concept
is a candidate way to organize the subject, needs reasons and discriminating
consequences, and may fail. Perfect fidelity to existing commitments does
not imply perfect invention of new ones.

## Option space

1. **Faithful interpretation only.** The ideal preserves fixed commitments
   and reports open alternatives on a declared class of tasks; conceptual
   development is outside it. Cheapest to specify; too narrow for a builder
   that must enter areas whose vocabulary it does not yet have.
2. **Faithful interpretation plus conjectural development, under a resource
   model.** The candidate selection below. The ideal reads faithfully and
   may propose distinctions, concepts, procedures, and representations,
   which remain candidates for the evaluators. A budget charges applying
   procedures, searching, interpreting, and developing new procedures.
3. **No ideal; class-declared bounded assessment instead.** Following the
   move in [Russell and Subramanian](../../sources/provably-bounded-optimal-agents.ingest.md),
   evaluate the program on a declared architecture in a declared environment
   class and drop the ideal reasoner. This is what the main-path comparison
   already does for performance. It does not by itself separate
   interpretation error from theory error, which is the problem stated.

## Candidate selection

Option 2, with option 3's class declaration as its scope requirement. The
idealization is faithful interpretation on a declared class, together with
attempts at conceptual development using declared knowledge and procedures
under a resource model. A budget alone does not specify the class or
establish fidelity on it. Scope is fixed by the assessment protocol, not
retrospectively by which tasks the interpreter completed.

| Dimension | Required declaration |
|---|---|
| Tasks and representations | Admitted questions, representation languages and forms, contextual conventions, and what counts as a completed interpretation for each task |
| Program language and architecture | The implementable operations, component boundaries, tools, and interfaces available to the interpreter |
| Context and knowledge | Supplied context, retained knowledge, starting procedures, access limits, and whether any may change during assessment |
| Objective | What the interpretation is for, which commitments must be preserved, which revisions may be proposed, and success criteria fixed before outputs are judged |
| Resources | Compute, context capacity, elapsed time, search, evidence access, and other charged operations, with limits |
| Environment | The cases and evidence the interpreter can encounter, their selection rule, and the conditions under which the assessment applies |
| Horizon | The assessed sequence or duration, stopping rule, and treatment of changes to the declared conditions |

**Fidelity criteria.** A faithful interpretation of a representation, given
its context, preserves the commitments the context fixes; preserves the
alternatives where the context leaves consequential readings open, instead
of selecting one silently; reports a revised commitment as a change, never
as what the text always meant; and identifies what a claim commits to
without deciding whether the claim holds. The last clause keeps the
idealization consistent when applied to the builder's theory of itself: a
sentence such as "reading R was faithful" is read for its commitments and
is not assigned a truth value by the act of reading it.

**Budget.** The resource model charges the work of any solver or tool a
semantic call invokes; a semantic call cannot hide arbitrary computation as
a free primitive. An interpreter that decided every satisfiability instance
in one uncharged call would be assuming an efficient oracle, not describing
one. For a language-model realization the binding resource is often
context, since [soft degradation often binds before the hard cap](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md).
A run can also fail through a wrong reading, inadequate knowledge, or an
unsuccessful conceptual proposal without exhausting its budget; those
outcomes are recorded as such.

**Completion and abstention.** An assessment covers the full admitted
workload: completed interpretations, incorrect readings, partial results,
abstentions, budget exhaustion, and missing outputs, with accuracy on
completed tasks reported beside coverage and cost. An interpreter that
avoids every difficult case cannot establish capacity through fidelity on
the remainder. Reporting alternatives completes an interpretation task when
the task's declared requirements allow it; the underlying question may stay
unresolved.

**Realization.** An implementation is compared to the standard on the
declared class. Its knowledge and procedures are declared where they are
retained artifacts and estimated by probe where they are model weights,
following the [representational form](../../notes/definitions/representational-form.md)
rule.

## Forces

- **Understanding must not become omniscience.** Two situations that supply
  the same evidence and differ in an unobserved outcome are reported as
  alternatives; no fidelity requirement picks the actual one.
- **Meaning must not become a decision procedure.** Understanding a
  specification does not decide termination or every consequence of
  execution; requiring a total solver meets Turing's limits.
- **Reflection must not require unrestricted self-truth.** The interpreter
  can criticize an account of itself without a universal truth predicate;
  the identify-without-deciding clause is the discipline, and Tarski's
  separation of object and metalanguage is the one to investigate.
- **Correct interpretation must not mean mind-reading.** Where context does
  not fix an importance criterion, silently choosing one is not recovery.
- **Concept invention must not certify itself.** Renaming failed cases
  "outside scope" manufactures success; a conceptual repair names what
  commitment changed, what depended on it, and a remaining case that could
  challenge it.
- **Semantic work must not be defined by problem-solving.** If understanding
  a problem meant solving it, the ideal would assume the builder's result.
- **The ideal must not erase acquisition or its cost.** If the component
  synthesized, installed, and warranted every needed procedure, machinery
  extension would follow by stipulation. The interpreter proposes; the
  evaluators assess; the builder retains.
- **Naming.** *Interpreter* may be too narrow for the constructive
  operations. The name is retained; the distinction between faithful reading
  and conjectural invention is what matters.

## Stress tests the specification must pass

Open mathematical problems test the boundary because their statements are
precise, so difficulty cannot be assigned to ambiguous wording.

| Request | What the contract can require | What ideality must not guarantee |
|---|---|---|
| Explain P versus NP | Preserve the quantifiers, decision-problem setting, certificate condition, and asymptotic resource bound | Decide whether P equals NP |
| Propose a new approach | Make the proposed concepts and intermediate obligations explicit; separate established steps from conjectures | An approach that succeeds |
| Examine an attempted proof | Identify the claim each step purports to establish and its dependencies; use separate proof-checking machinery for a formal derivation | Find every gap in an informal argument, or find a proof whenever one exists |
| Interpret the Riemann hypothesis after many verified cases | Preserve its universal scope; separate tested cases from the assertion | Turn finite checks into a proof |
| Explain why every prime above two is odd | Give the short argument, as a declared positive test | Use unresolved status as an excuse on every task |

A sentence independent of specified axioms is a further case: the
interpreter may investigate consistent extensions and grounds for adopting
an axiom, and adoption changes the assumptions rather than proving the
sentence from the original ones. Algorithmic undecidability is a different
matter and excludes a terminating correct procedure for every instance.

| Case to work through | Required discrimination |
|---|---|
| One text with two contextually legitimate readings | Preserving alternatives versus imposing a reading |
| A new concept introduced after an operating failure | A change with testable consequences versus a new label for the same account |
| A precisely understood but unresolved program property | Understanding the question versus having a decision procedure |
| A sentence independent of specified axioms | Investigating consistent extensions versus proving from the original axioms |
| Two worlds consistent with the observations | Conditional reasoning versus invented certainty |
| A self-description that praises its own evaluator | A represented claim versus independent support for it |
| A sound conceptual proposal that cannot be deployed | Semantic progress versus operational extension |

The first probe is a scheduler theory that assumes fixed capacity, supplied
with evidence compatible with both external contention and an internal
leak: the expected result reopens the commitments and names a
discriminating measurement without naming the cause first. A matched
fixed-vocabulary case tests faithful interpretation separately from
conceptual invention.

## Operativity and warrant

Adoption produces a specification and a probe suite consumed as evidence
when a claim attributes a failure to interpretation rather than to the
theory. No behavior-determining organization changes until an evaluation
uses the standard. The standard is itself an assessment instrument; what
warrants a fidelity verdict is the declared class and the independently
specified acceptance conditions of each task, and that warrant stops at the
class boundary. "No consumer yet; a first probe must be authored" is the
current operativity answer.

## Adoption criteria

- A declared class for the first assessment, with the seven dimensions
  filled and success criteria fixed before outputs are judged.
- The stress-test cases worked through with recorded expected results, so
  a candidate specification can fail them.
- A comparison with existing work on interpretation, conceptual change,
  belief-base revision, and truth maintenance, so the constructive semantic
  operations are shown to add something to the explicit-premise and
  consequence-operator separation those fields already supply.
- A stated balance of positive completion, fidelity, and justified
  abstention. The unresolved choice is how much positive success to require
  of conceptual invention without assuming general problem-solving or
  making "can propose something" vacuous.
- A named claim in a downstream evaluation that the verdict would change.

---

Relevant Notes:

- [Theory builder](../../notes/definitions/theory-builder.md) — rests-on: interpretation as a role inside the builder, and retention as the builder's rather than the interpreter's
- [A claim without external assessment carries three obligations](../../notes/a-claim-without-external-assessment-carries-three-obligations.md) — rests-on: attribution as the obligation this device serves, and the condition under which it binds
- [Semantic work can be relocated but not eliminated](../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) — rests-on: the KB's existing sense of semantic work, which this proposal extends with conceptual revision
- [Soft degradation often binds before the hard cap when evidence fits](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — rests-on: why context capacity is a charged resource for a language-model realization
- [Representational form](../../notes/definitions/representational-form.md) — rests-on: declare retained artifacts, probe weights
- [Provably bounded-optimal agents](../../sources/provably-bounded-optimal-agents.ingest.md) — rests-on: evaluation relative to a declared architecture and environment class instead of an ideal reasoner
