# Plan

Revised 2026-11-20 after the operator's direction on marginal measurement. The
earlier plan was built around one ruling on the objective's accounting (D4) and
a cold-reader check. The direction replaced that ruling, so the plan is
rebuilt around what the operator settled.

## Basis

Consider adding one line to `AGENTS.md` that sends an agent to the right instructions for a task it would otherwise mishandle. Other prompts load that line too. On a task already near the limit of what the agent can use effectively, one extra line could tip a correct answer into failure. The cost on that task is failure and rework, not just the extra text. That is a possible loss, not an observed failure. How often are important tasks that close to the limit? If we cannot tell and the answer could reverse the decision, the routing gain alone does not settle it.

Four points, recorded with their history in [the settlement record](./settlement.md#operator-direction-2026-11-20):

1. Progress is measured on the margin, in a declared application area.
2. A marginal claim is a conjecture about a total order that nobody specifies.
   The declared objective names that order. The evidence gives a partial order
   that approximates it.
3. The claim is that the change is better on balance. The operator and users
   weigh the observed gain against losses elsewhere, considering both how
   likely each loss is and how much it would matter. No numerical estimate is required.
4. Name how a loss could arise, who would bear it, and under what conditions
   it would matter. Give the judgment for current conditions, or say what is
   unknown. A larger table or a change in the task mix can warrant another look.

## Step 1 — test the claim form on three real changes

Before anything is written into the library, check that the form produces
claims someone can judge. Apply it to three past Commonplace changes of
different kinds:

- the tag-readme change of ADR 026, where a symbolic check was added;
- one addition of routing to `AGENTS.md`, the operator's own example;
- one added or tightened review gate.

For each, write the claim in the form: the area, the gain and its evidence,
the prior state it is compared with, and the regression argument with its four
parts. Record where the form was awkward or a part could not be filled.

Output: `worked-cases.md`. If a part cannot be filled in two of three cases,
check why before step 2. Revise a question that does not fit the changes.
Missing evidence is a different result: record “local gain shown; overall
judgment open” when the evidence supports only that conclusion.

## Step 2 — write the claim form as a theory note

The form is a transferable claim, so it belongs in `kb/theory/`, written with
`cp-skill-write` after reading the collection contract and type spec.

Working title: "Improvement over an open task space is claimed on the margin".
Lead with the routing example, then explain the two relations, the claim
form, and its assumptions.

It must state its relation to
[a better-factory claim](../../theory/a-better-factory-claim-compares-operative-states.md),
which asks for non-regression checked against thresholds and leaves open how
to do that for an open-ended family. The new note is the answer for that case:
the check is replaced by a judgeable argument. Whether the better-factory note
is then revised is a separate decision; it carries a TODO of its own.

Named gaps the note states and does not close:

- when a regression stops being trivial;
- the task population that "elsewhere" ranges over. The candidate is tasks
  that arise, weighted by frequency and importance;
- how often prior scope must be re-checked so that uncertainty does not
  accumulate over many changes;
- whether one total order exists, which rests on the declared objective.

## Step 3 — the objective declaration

In the instrument note, at L11. Proposed wording, for the operator to change:

> Commonplace's objective is more useful and better-warranted knowledge work
> per unit of human judgment. The objective names what improvement claims are
> about; it is not a measure. Progress is claimed on the margin: a gain in a
> declared area, compared with the prior state, with an argument that the change is better
> on balance. The operator and users weigh the gain against losses elsewhere,
> considering how likely those losses are and how much they would matter.

with a link to the step 2 note. The "not automation" sentence stays.

This replaces the accounting block of the earlier plan. Position D leaned
toward moving the objective into the frame note because that block would
change the instrument note's character. The block is gone, so the declaration
stays in the instrument note unless D's author objects on other grounds.

## Step 4 — dependent edits

- **Baseline-gap bullet, instrument note L39, and "What would change the
  status", L49.** Both ask for a program-wide baseline comparison "per unit of
  human judgment". Restate them as marginal comparisons in declared areas.
- **Two proposals.** Replace the copied objective sentence with a citation.
  The ablation proposal's arms become comparisons in declared areas; say so in
  one sentence and leave its design alone.
- **Frame note.** One sentence: it fixes boundary and partition; horizon and
  improvement objective are declared per attribution.
- **Instrument note L17.** Replace "components" with a word that does not
  collide with the partition's.

## Step 5 — one cold-reader check, after the edits

An agent other than position B's author reads the revised instrument note with
no workshop context and answers two open questions: "What does this note claim
the tag-readme trace shows about Commonplace?" and "How would you tell whether
Commonplace had improved?" Score the first for overclaims and the second
for the reasoning, not the terminology: can the reader identify the local
comparison and explain what would justify or withhold an overall judgment? Record it in `cold-reader-check.md`. A miss on
the second question means step 3's wording failed, and it is revised.

## Left for the operator, not planned here

- **The bootstrap article's measure.** It measures "human decisions each
  completed, verified improvement requires". Under the direction that is one
  dimension a marginal claim may name, not a program measure. The article is a
  draft under the operator's byline; this workshop does not edit it.
- **The frame note's person-based boundary.** The software-house investigation
  found that the frame note places people by designation while the
  theory-builder and software-house definitions place them by role. No
  position has argued it. It needs a decision on whether it belongs in this
  workshop.
- **A review or writing rule (D8).** None is planned. Revisit only if the
  claim form is used and misused.

## Close

Mark D4 reframed by the operator's direction, D1 and D3 moot, D2, D6 and D8
resolved as "no addition". Settle D5 + D7 by step 3 and the frame-note
sentence. Validate changed files with `commonplace-validate`. Delete the
directory and remove its entry from `kb/work/README.md`.

The software-house investigation is not extracted by this plan. Its
conjectures are untested. On closing, either move it to its own workshop or
record its two established findings in `kb/log.md`.

## Commits

One for the theory note, one for the instrument, frame and proposal edits, one
for closure. Each carries `Workshop: kb/work/frame-and-objective-declaration`.
