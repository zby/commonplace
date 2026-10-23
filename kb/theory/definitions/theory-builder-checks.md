# Checks for the theory-builder definition

Maintenance material for [theory builder](./theory-builder.md). Apply the
checks when changing that definition, including cross-references that change
its meaning. Report affected cases before revising their expected
classifications; keep case numbers stable and make changes to assumptions
explicit.

These cases check selected boundaries. Unchanged answers do not prove that
the entire scope is unchanged. Report any additional scope difference the
proposed change exposes.

Drafted 2026-09-25 to replace the conjectural-learning checks. Cases 1–16
carry over that file's cases with the same numbers and assumptions, and are
reclassified under the new definition. Cases 17–35 are new.

## Purpose

The definition names the arrangement Commonplace builds, so that the research
program's conjectures can be stated about it and tested against named
alternatives. The main conjecture is that such an arrangement learns, in
Simon's sense of improving its capacity for future action. Classifying outside
systems and staying close to Popper are constraints on how the definition is
written. They do not decide its scope.

## Tests for any change to the definition

1. **Design, not outcome.** A condition belongs in the definition only if
   Commonplace's arrangement depends on it by design, and removing it gives a
   named arrangement the program compares against. Localized content,
   consumption, criticism, and iteration pass this test. Localization is the
   minimum of addressability, and iteration is the minimum of persistence.
   Grades above either minimum have no cut-off that names a baseline, so
   fine-grained addressability and long persistence are design commitments,
   not conditions (operator, 2026-09-25). That each commitment pays is a
   conjecture tested against builders at lower grades. Fixed weights are a
   study condition. Improvement is never a condition: a definition that
   required it would settle the program's main question by stipulation.
2. **Every arrangement left outside is named.** It is specified well enough
   to be run as a baseline. Boundary cases also include arrangements inside
   the term; a case need not fail a condition to clarify the boundary.
3. **Each condition is attributed.** Each condition is stated in Popper's
   terms with a quote from an ingested source, or is marked as the KB's
   addition with the grounds for it. A condition may not be attributed to
   Popper when the quote supports only part of it.
4. **Classification requires evidence for the conditions.** Stated
   artifacts, consumption traces, and records of criticism can establish the
   conditions without an account of model internals. Where evidence is
   insufficient, the case remains unclassified. Observer inaccessibility alone
   establishes neither presence nor absence. Stipulated cases are classified
   under their stated assumptions.
5. **Qualifiers stay independent.** Reflective and autonomous are checked
   separately from membership and from each other. A change that makes one
   qualifier imply the other, or makes either a membership condition, is a
   scope decision.
6. **No term without a claim.** A new term enters only when a claim cannot be
   stated without it.
7. **A change reports the cases it flips.** Run the proposed wording against
   the cases below. A change that flips none is a wording change. A change that flips one is a scope decision for the operator and
   names the test it appeals to.

## Cases to check a change against

Condition numbers refer to the definition: 1 localized content,
2 consumption, 3 criticism, 4 iteration. Unless a case says
otherwise, it assumes a continuing system and says nothing about whether the
system improves.

| # | Case | Class | Settled by |
|---|---|---|---|
| 1 | A retained theory with separate parts is criticized and revised part by part, whether stored in separate documents or exposed through indexed traces | Inside | All four conditions; storage representation does not distinguish the cases |
| 2 | A retained prose theory is criticized for what it says and replaced whole | Inside | Condition 3: rejecting a theory whole and proposing a new conjecture is error elimination. Fine-grained addressability is not a condition; the prose is localized (operator, 2026-09-25) |
| 3 | Formulated criticisms are retained and a theory is rebuilt from them when needed | Inside | Condition 4: the rebuilt theory is a new conjecture informed by retained criticism, as in case 2 (operator, 2026-09-25) |
| 4 | Records containing only inputs and outcomes are retained for reconstruction | Not classified by this case; the baseline for the persistence conjecture | The records carry nothing criticism produced, so nothing formulated persists across runs. A reconstructor that states, criticizes, and revises within a run is a builder at that run's grade |
| 5 | Prompts or programs are varied and selected by score, with no formulated reason for failure bearing on their content | Outside: trial and error | Condition 3; does not classify unknown processing in a model proposer |
| 6 | A theory is built while reasoning and then discarded | Inside at the lowest persistence grade if the reasoning states, criticizes, and revises it; outside if it is merely applied | Conditions 3 and 4 inside the episode; persistence is graded, not a condition (operator, 2026-09-25) |
| 7 | Weights are adapted and no formulated theory guides decisions | Outside | Condition 1: no unit carries content; gradient updates also fail condition 3. An opaque model with no visible theory is a different case; insufficient evidence leaves it unclassified |
| 8 | Weights, prompts, and code evolve together around a formulated, consumed, criticized, retained theory | Inside | Weight change is not excluded; fixed weights are a study condition (test 1) |
| 9 | A formulated theory guides decisions and the system would never criticize it | Outside: the frozen-seed baseline | Condition 3; test 2 |
| 10 | A theory is stored and no process in the system would consume it | Outside; as a baseline it is the system run without the theory | Condition 2. A theory that a process would consume when an occasion arises is not this case |
| 11 | A theory survives an attempted refutation, and the recorded result guides later reliance on it or the choice of further tests | Inside | Condition 3 counts attempted refutation. Condition 4: the text is unchanged but the testing record changed, and the next round uses it (operator, 2026-09-25) |
| 12 | One model proposes and criticizes its own theories | Inside | Test 1: decorrelating the critic changes how well criticism works, not the arrangement |
| 13 | Criticisms are written down, but a test detects no difference from placebo text of the same form | Not shown to be inside by that test | Condition 2 for the criticisms is unestablished; non-detection alone does not establish absence (test 4) |
| 14 | A formulated theory licenses revisions only by proof from premises closed to criticism | Outside | Condition 3, excluded by stipulation. Proof-governed switching alone does not establish this closure in a complete system |
| 15 | A new theory is retained and consumed; the system has a working criticism process that has not yet been applied to it | Inside | Condition 3 requires the process, not that it has run on every theory |
| 16 | A conjecture produces most of the improvement; criticism follows and changes only reliance on it | Inside | Membership does not depend on how improvement is attributed |
| 17 | A system meets all four conditions, and its criticism and revisions never improve later work | Inside; learning is not established | Test 1: improvement is not a condition. This is the case the program's experiments must be able to find |
| 18 | Commonplace today: operators perform criticism and selection, and method texts guide the work and are revised in response to criticism | Inside; reflective; not autonomous | The boundary follows the operation, so operators performing internal operations are inside |
| 19 | A builder's users only supply problems and judge products; all internal operations are computational | Inside; autonomous | Users stay outside the boundary; test 5 |
| 20 | A builder's method texts are fixed and never criticized, while its theories about its subject are | Inside; not reflective | Test 5 |
| 21 | A reflective builder has a procedure with no stated purpose | The builder stays reflective relative to its other method texts; that procedure lies outside reflection | Criticism aims at a procedure's stated conjecture about why it works; without one the procedure can be tried but not criticized |
| 22 | A reflective builder replaces its model and leaves its method texts unchanged | Still reflective; text and operation may diverge until criticism finds the gap | The connection runs through consumption and criticism, not automatic update |
| 23 | A research community, declared as the system | Inside | Popper's own case; no member holds the whole theory or supplies all the criticism |
| 24 | One invocation of a refinement procedure such as FORTE over a supplied theory | Inside at a low persistence grade | Conditions 1–4 hold within the run: a repaired theory is a new conjecture, so re-testing it on the same examples is a real test. Nothing persists beyond the run (operator, 2026-09-25) |
| 25 | The Gödel machine | Open | Whether a deployment criticizes its proof premises elsewhere is not settled by the construction |
| 26 | A retained theory has no stated assumptions, scope conditions, or parts that criticism could name; it is criticized for what it says and replaced whole | Inside at minimum addressability; the baseline for the addressability conjecture | The whole theory is one localized unit, which meets condition 1 (operator, 2026-09-25) |
| 27 | A builder revises its model only by replacing it whole | Inside | The model is an addressable part of the machinery: a stated choice names it, criticism can blame the choice, and replacement revises it (operator, 2026-09-25). The weights' content stays out of reach |
| 28 | A system states a criticism and uses it to update weights (critique-trained RL, textual gradients); no stated theory is retained and consumed | Outside | Conditions 1 and 3: the revised theory is the weights, where no unit says anything. Inside only if the criticism aims at a retained, consumed stated theory |
| 29 | Model editing locates a fact in particular weights, and the system criticizes and edits that fact | Partly localized; classify on evidence | Condition 1 tracks localization, not substrate (test 4). The located parts can meet conditions 1 and 3; the rest of the model cannot |
| 30 | Weights are trained by gradient descent against a loss on examples | Outside: the gradient-descent contrast | Blame reaches every parameter, but no parameter says anything, and the process cannot blame the loss or the data. Conditions 1 and 3 |
| 31 | One run pursues a sequence of different experiments, and each later experiment consumes the stated findings and criticisms of earlier ones | Inside | Condition 4; persistence within the run |
| 32 | A bounded optimization run revises one solution for one task over many rounds, keeping a store of variants and critiques | Inside if criticism aims at what the variants say; outside if variants are kept by score alone | Condition 3 decides; condition 4 holds within the run, and freezing the result afterwards ends the builder |
| 33 | A critic reports errors in stated theories, but no next round takes the report up | Outside | Condition 4: criticism that feeds nothing is not iteration |
| 34 | A person only notices problems in the builder's theories or work, such as a stale theory or a recurring failure, and computation performs every other operation | Inside for that act; the builder is not autonomous | Noticing a problem in its own theories or work is an internal operation (operator, 2026-09-25) |
| 35 | A user poses a task and judges the product, and notices nothing about the builder's theories | Outside the builder | Supplying problems as tasks is external; noticing concerns the builder's own theories or work |
