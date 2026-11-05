---
description: "Separating an interpretation error from a theory error needs a designated reference set and a three-way sort of the failure, not an ideal interpreter; draft that connects the semantic-reference account to this workshop's goal"
type: types/note.md
traits: [title-as-claim]
tags: [llm-reliability, learning-theory]
---

# Attributing a failure to interpretation or theory needs a reference set, not an ideal interpreter

Draft, 2026-11-05. Written in the workshop to connect what the library now
says to the problem this workshop posed. Nothing here is adopted.

## Why this note is needed

When a theory builder's product fails, the fault may lie in the theory or in
how it was read. The [fence note](../../theory/a-claim-without-external-assessment-carries-three-obligations.md)
makes attribution an obligation for any claim that asserts a cause, and then
records that no adopted standard separates an interpretation error from a
theory error. Without that separation a failure can be scored but not
localized. The builder then risks the wrong repair: revising a correct
theory because the executor misread it, or narrowing a sufficient
specification because the theory was wrong.

This workshop tried to supply the standard as an idealized interpreter and
could not state when a reading is correct. This note shows that the library
now holds the needed pieces under a different construction, states the
procedure that connects them, and gives the fence note's attribution
section something to point to. That is what lets the workshop close.

## The library's construction

The [epistemic stance](../../reference/epistemic-stance.md) reads the
meaning of an instruction as the reading a designated reference set of
interpreters converges on, under a stated rule for when two outputs count as
the same answer. The set is chosen; whether it converges is a fact that can
fail. This supplies the correctness relation the sketch lacked without an
oracle for objective content.

Given a designated reference set, a failure sorts three ways:

1. **The reading is unsettled.** The referees do not converge, or the
   contract leaves the case open. The outcome is not yet an interpreter
   failure or a theory failure. Repair: settle the requirement.
2. **The reading is settled and the output lies outside the permitted
   set.** This is [interpreter failure](../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md).
   Repair: detection and correction.
3. **The reading is settled, the output lies inside the permitted set, and
   the result is still wrong.** A [program refinement](../../theory/definitions/program-refinement.md)
   of a wrong specification is a wrong program. The fault is in the
   requirement, which is the theory-side error. Repair: revise the theory.

The [fence note](../../theory/a-claim-without-external-assessment-carries-three-obligations.md)
adds causes outside this sort, such as the evaluator, retrieval or a skipped
check, and asks for a discriminating trace, intervention or test. The sort
above is that test for the interpretation-versus-theory question.

## The workshop's stress cases under the sort

| Case | Expected disposition |
|---|---|
| One text with two contextually legitimate readings | Branch 1 if the referees split; retaining both readings is the correct output, selecting one silently is branch 2 |
| A precisely understood but unresolved program property | Reading settled; failing to decide the property is not branch 2, since the permitted set does not require a decision |
| Two worlds consistent with the observations | Reporting both is inside the permitted set; asserting one is branch 2 |
| A self-description that praises its own evaluator | Representing the claim is settled reading; treating it as support is branch 3 or an evaluator fault |
| A new concept introduced after an operating failure | Outside the sort; a conjecture judged by the theory builder's conditions, not by reading fidelity |

## Scope

- The sort applies where a reference set has been designated and a
  same-answer rule stated. Without them the first branch absorbs everything.
- The library's interpreter role is the whole executor held to public
  meaning. The sort does not separate a misread from a correct read followed
  by failed reasoning. Whether that finer split changes any repair is open.

## Open Questions

- Reading versus reasoning inside branch 2: does any repair depend on it?
- A clarification policy cannot promise to ask exactly when a distinction
  matters, for arbitrary acceptance conditions. Where does that limit belong?
- Full-workload reporting, with abstentions beside completed tasks, has no
  library statement and no consumer yet.

---

Relevant Notes:

- [Epistemic stance](../../reference/epistemic-stance.md) — grounds: meaning as reference-set convergence
- [Out-of-spec output is a failure of the interpreter, not the spec](../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — mechanism: branch 2
- [Prompting changes failure diagnosis with the semantic reference](../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — mechanism: branch 1 and the three membership limits
- [Program refinement](../../theory/definitions/program-refinement.md) — mechanism: branch 3
- [A claim without external assessment carries three obligations](../../theory/a-claim-without-external-assessment-carries-three-obligations.md) — extends: supplies the discriminating test its attribution section asks for
- [Resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md) — contrasts: the device this construction replaces
