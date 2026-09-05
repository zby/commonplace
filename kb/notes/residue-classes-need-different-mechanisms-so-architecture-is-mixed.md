---
description: "Different reasons for an untransferred decision identify different missing functions; a single process can supply several, and the current carrier split is not a permanent requirement"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Distinct residue classes require distinct functions in a self-improving architecture

A system that preferentially transfers its best-supported human decisions
leaves a selected residue, [because warranted transfer leaves people the
hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).
A decision may remain because a needed premise is unavailable, acceptance or
authority is unresolved, checking is inadequate, or the decision arises after
the automatic process stops. These are different reasons for a transfer to fail.

Each reason identifies a function that must be supplied before that obstacle
is removed. It does not establish that a new component must be built: existing
machinery may supply the function once represented inputs, routing, or authority
change. Several obstacles may also require one coupled redesign.

The functional distinction does not prove that the roles must occupy different
[representational forms](./definitions/representational-form.md).
Natural-language theory, models, symbolic machinery, and retained evidence are
one inspectable arrangement. A single process can supply several roles while
evidence for one remains insufficient to establish the others.

## Which function answers which obstacle

| Why the decision remains human | Function needed | Possible realization |
|---|---|---|
| A needed premise is unavailable | Acquisition, representation, retrieval, or reconstruction | Records, theory, observations, and operations that recover the premise |
| Acceptance or authority is unresolved | A usable decision basis and adequate semantic application, or a grant of authority | Criteria, examples, fallible judgment within declared limits, and represented authorization |
| A harmful candidate cannot be adequately distinguished | Checking and corrective exposure | Tests, validators, differently failing critics, held-out tasks, and later consequences |
| The decision arises after the automatic path stops | Continuity | Persistent state, scheduling, installation, rollback, and reactivation |

**Representation** makes a premise available. [Explicit
retention](./only-explicit-retention-is-durable-writable-and-addressable.md)
also supplies a direct revision target. Reconstruction from records can supply
the premise without keeping a separate theory document. Whether retaining that
document helps is a further question about reliability, cost, and later revision.

**Settlement and semantic application** differ. A method can constrain an
answer without spelling out every judgment needed to apply it. A model can
also make a decision whose full criterion is unstated. That can advance
[computational closure without methodological
closure](./methodological-and-computational-closure-track-different-changes.md).
A fallible program theory often guides search, diagnosis, and recovery rather
than determining acceptance by itself, [especially under delayed
feedback](./program-theory-sustains-search-under-delayed-feedback.md).
Authority remains a separate practical limit: a plausible judgment is not a
grant to make it operative.

**Checking** must be able to challenge the proposed result. A checker need not
sit outside the technical system, but acceptance cannot rest only on the
candidate's own claim that it is good. Different failure modes and later
operating consequences provide different strengths of correction. [Available
checks](./warranted-autonomy-is-bounded-by-oracle-domain.md) limit what the evidence
warrants, not what a system can happen to produce correctly.

**Continuity** makes evidence and decisions available after the current call.
A symbolic runtime can carry queues, checkpoints, and state transitions without
asking a model to reconstruct them each time. [Scheduler–LLM
separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
explains that engineering advantage. It is not a logical prohibition on another
process supplying the same continuity.

## Evidence for one role does not establish the others

Executing a rule exactly does not establish that it expresses the right
objective. A program can contain a decision procedure or call a model to choose
one, but that judgment then needs its own assessment. The extra role is not
supplied merely by exact execution.

Understanding a theory does not independently warrant it. A model may propose
and criticize a change; whether those operations have sufficiently different
failure modes remains an evidential question. The [error-correction
account](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md)
explains why more repeated criticism alone is insufficient.

Retaining a document does not show that a process uses it or schedules its
later use. Conversely, a failed check can reveal a missing premise and support
learning it, but rejection alone does not guarantee a correct diagnosis or
settle an unobserved user preference.

These are limits on inference from evidence, not claims that functions cannot
interact. One observation can support diagnosis, theory revision, and a new
check. A single model can interpret, propose, and criticize while each role
remains separately testable.

## The premise-change test

Identify the claimed obstacle and the missing function before testing a transfer.
If an existing procedure already supplies it under the same conditions, the
claim that new machinery is required is defeated. If changing one function
repairs the decision while unrelated functions remain fixed, that supports the
proposed diagnosis.

A complete formal criterion and all necessary inputs may remove the need for
open-ended semantic judgment on that decision. A path completed within one call
may need no cross-call scheduler. But narrowing the assessed work must be
reported: removing the cases that require a function does not demonstrate that
the broader problem was solved.

The class list is not exhaustive or necessarily disjoint. Lack of authority may
need a distinct treatment from an unsettled acceptance criterion, and a
prohibitively costly decision can require a different method rather than a new
semantic capability. The classification earns its place by identifying repairs
and predicting their consequences.

## Consequence for the architecture

The theory/model/runtime/evidence arrangement is useful when it makes these
roles accessible to intervention: vary a retained account, replace a checker,
or change when evidence arrives. Its inspection advantages must still cover
coordination, retrieval, and maintenance costs.

[A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow
it](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
A later implementation can merge or replace today's carriers while preserving
the needed functions. The architecture is therefore a testable proposal, not a
permanent division of labour established by the class names.

## Scope

The selected-residue prediction assumes preferential transfer of warrantable
decisions under comparable conditions. Another transfer policy can leave a
different residue. Functions are distinguished where failure and evidence differ;
this does not require one component per role, a fixed process order, or steady
progress toward automation.

---

Relevant Notes:

- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: supplies the conditional selection effect
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: separates roles on the theory-mediated path
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: separates explicit decision content from human-free execution
- [Explicit retention provides direct targets for selective revision](./only-explicit-retention-is-durable-writable-and-addressable.md) — mechanism: supplies a useful, nonexclusive representation path
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: keeps warrant separate from operation
- [A fixed-model house must retain missing procedures for theory use](./a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md) — extends: tests when existing operations are inadequate and machinery revision is needed
