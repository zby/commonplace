# Appendix C — Witness protocol

```text
Versioned argument snapshot for: The Reachability Conjecture
Paper version: pending
Mode: paper-native (canonical statement of the witness conditions)
Frozen source tag: pending
Source paths: kb/articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md;
  kb/articles/nearest-existing-constructions-to-a-reachability-witness.md;
  kb/articles/reachability-as-closure-under-the-seed-gate.md
Live successors: the same paths on the main branch
Status: staging — not published
```

This appendix is the one full statement of what a witness must do. The four
obligations in the paper body summarize it. Supplement D's protocol section
points here rather than restating it. Terms are as defined in Appendix A.

## C.1 What the witness declares before the run

A witness run is defined by its regime (A.6). All of the following are written
down and fixed before the first demand is revealed:

1. **Pinned weights.** The exact model versions and every other
   distributed-parametric component the house uses: embedding models,
   rerankers, learned classifiers, adapters. None may change during the run.
2. **Seed.** The complete initial house state: notes, software, production
   machinery, evaluators, retention rules, context assembly. The seed is
   tagged so that any later state can be diffed against it.
3. **Permitted external inputs.** Which kinds of input may reach the house:
   user demands, tool results, operating consequences, and any other channel.
   Anything not listed is not permitted.
4. **Demand process.** The admissible histories and the selection procedure
   (A.8). Demands are revealed incrementally as the run proceeds; the house
   never sees a later demand before handling the current one. The realized
   history is recorded as it unfolds.
5. **Product scope, horizon, and budget** (A.3).
6. **Thresholds.** What hitting probability and continuation reliability the
   witness will count as usable (A.10), with the reasoning that ties them to
   the product and its risk level.
7. **Intervention schedule.** Which withholding and replacement interventions
   will be run, at which points, and what each is predicted to change (C.5).
8. **Accounting rules.** How retries, abstentions, timeouts, rollbacks,
   rescues, and human interventions are counted (C.6).

Nothing on this list may be changed after a failure is seen. A demand that the
house failed may not be removed from the history; a scope may not be narrowed
so that fixed machinery suffices; a newer model may not be substituted.

## C.2 Start of the human-free lineage

The run has a declared **start**: the moment after which no human fills an
internal role. Everything before the start is seed engineering. Human
corrections before the start are logged but do not count against automation;
they are part of how the seed was built. Every state after the start must be a
successor produced by the house's own update machinery from a permitted input
(A.6).

## C.3 What people may supply

After the start, a person may act only as a user (A.2): supplying requirements,
domain facts, preferences, observed outcomes, later demands, and acceptance
judgments about visible behaviour. A person who, after the start, does any of
the following has filled an internal role, whatever they are called:

- diagnoses why an internal candidate or the house's theory failed;
- compares internal candidates or chooses which revision is kept;
- edits notes, code, or machinery inside the house;
- supplies the decisive project-specific understanding the seed withheld;
- restores operation after an internal failure.

Each such act is a human intervention and is accounted for under C.6.

## C.4 The broad conditions

A witness for the broad conjecture must show all of the following within one
regime. The obligation each serves is given in brackets.

1. **Pinned operation.** With every distributed-parametric component pinned,
   the house maintains one user product over the declared horizon under the
   declared demand process. [automated continuation]
2. **Withheld understanding.** The seed withholds at least one decisive piece
   of project-specific understanding, while retaining the permitted records and
   interactions from which the capacity a program theory provides can be
   acquired. The withheld piece is named in the sealed declaration and is not
   disclosed to the house. [initial acquisition]
3. **Unstated implication.** The house later handles a demand whose correct
   handling is not stated verbatim in any retained record, and its handling
   depends on the withheld understanding having been acquired. [holding and
   application; initial acquisition]
4. **Causal use.** Withholding or replacing the relevant retained state, or the
   path by which it reaches the decision, changes proposal, evaluation,
   diagnosis, or recovery in the way predicted in the intervention schedule.
   [holding and application]
5. **Delayed contradiction.** A later dependency change or operating
   consequence makes part of the earlier understanding inadequate. The house
   attributes the evidence to the part that failed and reaches an adequate
   successor state, neither preserving the old account blindly nor rewriting
   it without grounds. [successor acquisition]
6. **Both forms.** Across the sequence, experience causes learning by the house
   (A.7) in both natural-language and symbolic state. The two need not change in
   the same learning step. [initial and successor acquisition]
7. **Internal decisions stay internal.** Candidate admission, rollback,
   conflict resolution, and continuation operate without a person supplying the
   decisive understanding or choosing the successor. [automated continuation]
8. **Not one lucky path.** The evidence in C.7 shows usable hitting probability
   within the budget and usable continuation reliability across the horizon.
   [all four]

The conditions do not require the acquired understanding to persist as a theory
stored as its own artifact. Reliable reconstruction from retained records, or a
mixed carrier, satisfies them if the house passes the same causal tests over
many changes.

## C.5 Interventions

Interventions are how conditions 3 to 5 are tested rather than asserted. Each
is declared in advance with its predicted effect.

- **Withholding.** Remove the retained state suspected of carrying the
  understanding, or block the path by which it reaches the decision, and
  re-run the same demand from the same predecessor state with everything else
  held equal. Prediction: the handling degrades in a stated way.
- **Replacement.** Substitute a state carrying a different, plausible but wrong
  account, and re-run. Prediction: the handling follows the wrong account in a
  stated way.
- **Delayed contradiction.** Introduce, through a permitted input, a change
  that falsifies part of the current understanding. Prediction: the house
  revises that part, and later demands that depend on it are handled under the
  revised account.

A stored rationale that the house cites but whose removal changes nothing has
failed the causal-use test however complete it looks. An intervention whose
prediction was not written down before the run is exploratory evidence, not a
condition met.

## C.6 Run accounting

Every run keeps a log from which the following are countable. The rules decide
what each event means for the claim.

- **Retry.** The house re-attempts a demand or a step by its own decision. A
  retry counts against the budget and against nothing else. Unbounded retrying
  is a budget failure, not automation.
- **Abstention.** The house declines a demand within scope, or reports that it
  cannot handle it. An abstention is visible to the user and is honest; it is
  still a failure on that demand for adequacy (A.9). An abstention on a demand
  outside the declared scope is not a failure.
- **Timeout.** A demand exhausts its share of the budget without a result. A
  timeout is a failure on that demand.
- **Rollback.** The house reverts a change by its own machinery. A rollback is
  a permitted transition. It is learning by the house only if what caused it is
  retained and changes a later job.
- **Rescue.** A person restores operation or repairs an internal failure after
  the start. A rescue is a human intervention in an internal role. The
  human-free lineage ends at the first rescue; the run establishes reachability
  at most up to that point, and continuation reliability is measured only on
  the rescue-free part.
- **Human intervention.** Every act by a person after the start is logged and
  classified as user input (C.3) or internal role. An internal-role act ends
  the human-free lineage in the same way as a rescue.

A run in which the house needs rescues that become rarer over training is
evidence about the training path. It is not a witness until a run completes the
horizon with none.

## C.7 Evidence for the two probabilities

Hitting probability and continuation reliability (A.10) are properties of the
regime, not of one run. The witness supplies one of:

- **Repeated runs.** Several runs from the same seed under the declared
  selection procedure, each with its own realized history. Hitting probability
  is estimated from how many reach an adequate state within the budget;
  continuation reliability from how many of those stay adequate to the end of
  the horizon.
- **A justified estimate.** Where repeated full runs are unaffordable, a
  declared estimation method: for example, repeated runs over a shorter horizon
  with an argument for why the remainder behaves the same, or held-out demands
  within one run. The method is declared before the run and its limits are
  stated with the result.

Adequacy is judged on **untouched later changes**: demands the house handled
after the state under test was reached, without intervention, and not used to
select that state. The declared thresholds (C.1, item 6) decide whether the
result is usable. The paper fixes no universal threshold.

## C.8 What a run establishes

A completed run with all of C.4 met establishes practical reachability (A.11)
under its regime: for that scope, horizon, budget, and demand process, with
those pinned models. It does not establish reachability for a wider scope or a
different model.

A failed run eliminates that regime. It does not refute the conjecture, which is
existential (paper body, Boundaries), unless the search over regimes has itself
been bounded.

A run using models newer than the cutoff, or any state that a newer model
produced, establishes nothing about reachability with cutoff models, however
useful it is as evidence about the value of accumulated state.

## C.9 The stronger explicit-theory protocol

The broad conditions are neutral about whether the theory is stored. The
stronger hypothesis (paper body, Nearest existing constructions) predicts that a
rationale stored as its own artifact, one that can be found and revised on its
own, improves coherent modification, diagnosis, or recovery over reconstructing
understanding from raw records or searching the artifacts directly. Testing it
adds the following to C.4:

1. **Withheld rationale.** The seed withholds a decisive project rationale
   while retaining the records from which it can be synthesized.
2. **Synthesis and loading.** The house writes a rationale-bearing
   natural-language artifact and demonstrably loads it at later decisions where
   its unstated implications matter. Loading is shown in the context assembled
   for the decision, not inferred from the artifact's existence.
3. **Locally valid conflict.** A later change passes all tests but conflicts
   with the acquired rationale. The house preserves coherence without receiving
   the answer from a person.
4. **Falsified rationale.** A later dependency change or operating consequence
   makes the old rationale false. The house attributes the evidence, admits a
   successor rationale and the matching software or machinery change, and
   avoids both blind preservation and ungrounded rewrite.
5. **Internal decisions stay internal**, as in C.4 item 7, now including the
   retirement of a rationale.
6. **Matched baselines.** With the model, source evidence, demand sequence,
   and inference budget held fixed, the same demands are run against a house
   that reconstructs from raw records and a house that searches the artifacts
   directly. The explicit route must do better on untouched later changes.
7. **Causal effect, not trace.** Counterfactual removal or replacement of the
   stored rationale (C.5) changes the outcome. A mediation trace, showing that
   the rationale was loaded and cited, is not enough; the removal must change
   what the house does.

Meeting C.9 establishes the mechanism claim. Failing it while meeting C.4 leaves
the reachability claim standing: the house reached adequate states by
reconstruction, and the stored theory added nothing measurable in that regime.
