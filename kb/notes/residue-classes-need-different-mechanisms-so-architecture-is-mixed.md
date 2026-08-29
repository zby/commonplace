---
description: "Derives distinct functional requirements from residual human decisions while treating the current natural-language, parametric, symbolic, and evidential split as one inspectable realization rather than a theorem about permanent carriers"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Each residue class needs a different mechanism, so a self-improving architecture must be mixed

A system that preferentially moves warrantable decisions out of its human cut
keeps a selected residue, [because warranted transfer leaves people the
hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).
A residual decision may remain because a required premise is not represented,
a criterion or authority is unresolved, no sufficiently independent check
exists, or the decision arises after the automatic horizon ends. Call these the
**residue classes**.

Each class names a different function that must grow before its decisions can
move: representation, settlement and semantic application, verification, or
continuity. An architecture facing more than one class must preserve more than
one functional role and more than one failure surface. That is the mixedness
derived here.

The derivation does **not** prove that those functions must remain in different
[representational forms](./definitions/representational-form.md). Retained
natural-language theory, a parametric interpreter, symbolic code, and external
evidence are the current inspectable realization. Another substrate could host
several roles, and learned systems may absorb current carrier boundaries. The
requirement is functional separation where failures and evidence differ, not
permanent representational separation.

## Which function answers which residue

| Why the decision remains human | Function that must grow | Current realization |
|---|---|---|
| A required premise is not available to the deciding process | Representation and retrieval | Retained artifacts with addressable content and scope |
| The objective, commitment, criterion, or authority does not determine what may be accepted | Settlement plus semantic application | Declared objectives and methodologies, authoritative commitments, and an interpreter that applies them to unformalized cases |
| No check can defeat a plausible but harmful candidate | Verification | Tests, validators, decorrelated critics, held-out tasks, later demands, and operational consequences |
| The decision arises after the automatic path stops | Continuity | Persistent state, scheduling, installation, rollback, and later reactivation |

**Representation** makes a premise available and revisable. Retained explicit
artifacts are currently the clearest way to give project-specific assumptions,
purposes, and explanations a stable address, [since only explicit retention is
currently durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md).
A sufficiently capable process may reconstruct some premises from its inputs,
but reconstruction supplies no persistent target for later criticism unless the
result is retained.

**Settlement and semantic application** are related but distinct. An objective,
commitment, methodology, or authorized decision can settle what counts as
acceptable. An interpreter applies that settlement where the statement does not
fully specify the case. A fallible empirical program theory usually does not
settle the change by itself. At an open-ended modification crux, it guides
search, diagnosis, backtracking, and recovery while later evidence remains able
to correct it, [because holding a program theory means sustaining coherent
search under delayed feedback](./holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md).

**Verification** supplies grounds that can overturn the candidate's own account.
Mechanical validators sit at the cheap end; held-out tasks and delayed
operational consequences can reach claims that no local test settles. What
matters is not that the checker sits outside the technical system, but that the
candidate cannot guarantee acceptance by authoring both the proposal and the
decisive standard, [since warranted autonomy is bounded by oracle
domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

**Continuity** keeps the path active when evidence or a new decision arrives.
A symbolic runtime is currently the cheap and reliable realization because it
carries state and exact transitions across bounded calls. A model can host some
of this role, but doing so pays the [error-correction cost that motivates
scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).
That is an engineering gradient, not a logical prohibition.

## No function substitutes for another

The derivation depends on non-substitution at the function level.

**Execution does not settle an unresolved criterion.** Code can faithfully
apply a supplied rule. It cannot decide which objective or commitment should
hold merely by executing more exactly. Codifying “use judgment” either freezes
an arbitrary interpretation or leaves the decision unresolved.

**Semantic competence does not supply independent warrant by itself.** A model
may understand a theory, generate a strong candidate, and criticize it. More
capability can improve each operation. It does not by itself show that the
proposal and criticism have sufficiently decorrelated failure modes. Independent
exposure remains a separate evidential question, [because error correction
needs above-chance oracles with decorrelated errors](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md).

**Retention does not execute or continue a path.** A document changes nothing
unless a process retrieves and uses it when the decision arises. Stored state
also does not schedule its own later reactivation.

**Verification does not supply an absent premise or objective.** A failed check
can reveal that something is missing. It cannot determine the missing
project-specific commitment merely by rejecting candidates.

A single process may host several roles. A model may interpret a criterion,
propose a change, drive tools, and perform provisional criticism. The roles
remain analytically separate because evidence for one does not establish the
others and an intervention can impair one while preserving the rest.

## The premise-change test

The claim predicts how the architecture should simplify when the residue
changes.

Where every criterion in a domain is formal and every required premise is in
the input, the semantic interpreter may disappear. A compiler can be wholly
symbolic because no residual decision in its declared domain needs open-ended
settlement or theory-guided search. Where the whole path fits in one bounded
call, a persistent scheduler may be unnecessary. Where no independent evidence
exists, adding more retention or execution cannot by itself warrant transfer.

Conversely, a residual decision whose failure class has no corresponding role
shows that the architecture is incomplete for that decision. A possible fifth
class is authority: the system may represent what should be done and verify the
result while lacking a grant to commit it. Authority may be a special kind of
settlement or a separate function. The current class list does not decide.

## Consequence for the current architecture

The current retained-theory/LLM/runtime/evidence split is valuable because it
makes the roles addressable and their failures inspectable. It supports targeted
interventions: withhold the theory to test mediation, perturb the interpreter,
replace the evaluator, or truncate the horizon. That makes it a strong research
architecture even if later learning collapses some representational boundaries.

The architecture should therefore be defended as a provisional, testable
realization. It should not be defended by claiming that natural-language,
parametric, and symbolic carriers are permanently necessary. [A hand-crafted
bootstrap fits the Bitter Lesson only if learning can outgrow it](./a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md),
including by replacing a present carrier when another realization supplies the
same function more efficiently.

## Scope

- The residue prediction is conditional on preferential transfer of warrantable
  decisions under a fixed boundary, objective, horizon, and workload. Another
  transfer policy can leave a different residue.
- The four classes are not claimed to be exhaustive. The derivation requires
  only that each class in play has a corresponding function.
- “Mixed” means functionally plural. It does not imply a fixed process diagram,
  one process per role, or permanent representational heterogeneity.
- A function can become unnecessary on a narrower task distribution. That does
  not refute the claim for a path whose residue still contains its class.
- Settlement covers objectives, commitments, methodology, and authority. A
  fallible explanatory theory more often orients search than settles acceptance.

## Open Questions

- Can the class list be derived systematically from conditions for warranted
  transfer rather than collected from current cases?
- When does a model-based critic become independent enough that interpretation
  and verification can be hosted by closely related processes?
- Is authority a fifth residue class or a subcase of settlement?
- Which intervention best tests whether the current representational split is
  doing functional work rather than merely reflecting implementation history?

---

Relevant Notes:

- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: supplies the conditional selection effect and residue classes
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back on one path](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: separates the functions on the theory-mediated path
- [Holding a program theory means sustaining coherent search under delayed feedback](./holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md) — grounds: explains why fallible theory guides search rather than fully settling the hardest modification
- [Methodological and computational closure track different changes](./methodological-and-computational-closure-track-different-changes.md) — grounds: distinguishes represented guidance from computational execution
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: keeps verification separate from proposal and interpretation
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: explains the current cost advantage of symbolic continuity
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](./a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md) — extends: treats the representational split as provisional rather than protected
