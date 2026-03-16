---
description: Evaluate a kb/log.md entry that suggests a new note — read the notes index first, load related notes, and decide whether to reject, fold into existing artifacts, keep in the log, or create a genuinely new note
---

# Evaluate a log entry for note creation

Use this instruction when a `kb/log.md` entry looks like it wants promotion into a new note. Treat the log entry as a **proposal**, not as evidence that a new note should exist.

Do not start drafting the note until the evaluation is complete.

## When to use

- When reviewing `kb/log.md`
- When a synthesis or abstraction entry seems like it wants promotion
- When you are unsure whether to create a note or make a smaller change

## Steps

### 1. Read the log entry precisely

Extract:

- the candidate claim or pattern
- the notes or sources named in the entry
- whether the entry is proposing a synthesis, abstraction, update, or gap

Rewrite the proposal in one sentence in your own words. If you cannot restate it clearly, do not create a note yet.

### 2. Read the full notes index first

Read `kb/notes/index.md` before opening individual notes.

Scan the entire index, not just keyword matches. Flag notes whose descriptions suggest they may already cover:

- the same mechanism
- the same distinction
- the same failure mode
- the same design implication

This is the primary duplicate-detection step. Do not rely on the log entry's cited notes alone.

### 3. Load the most relevant existing notes

Read the notes and source ingests most likely to overlap with the proposal.

Prioritise:

1. Notes explicitly named in the log entry
2. Notes flagged from `kb/notes/index.md`
3. Any directly relevant source ingests

Read enough to answer:

- What does the KB already say?
- Which note currently gives the deepest mechanism?
- Is the proposal actually new, or just a rephrasing of existing material?

Cap at 8 notes and 4 source ingests. Load depth matters more than breadth.

### 4. Run the novelty tests

Reject the proposal unless it passes **all** of these tests.

#### A. Delta test

What would a future reader learn from the proposed note that they would not already get from the strongest existing note?

If the answer is "the same idea, phrased more clearly" or "a cleaner summary," do not create a note.

#### B. Mechanism test

Does the proposal explain **why** something works, fails, or matters?

If it only groups cases into phases, levels, categories, or strategies without adding causal structure, do not create a note.

#### C. Compression test

Could the useful content fit as:

- one paragraph in an existing note
- one added link in an ingest report
- one sharpened open question
- one line kept in `kb/log.md`

If yes, prefer that over a new note.

#### D. Traversal test

Ask: when would a future agent load this proposed note instead of the strongest existing note?

If the existing note is always the better destination, the proposal is redundant.

#### E. Prediction test

Does the proposal imply at least one non-obvious consequence?

Examples of acceptable consequences:

- a failure mode to watch for
- a design choice that follows from the claim
- a boundary where one approach stops working
- a testable distinction between similar-looking cases

If the proposal does not change what a reader would do or predict, do not create a note.

### 5. Choose the smallest sufficient outcome

Choose exactly one outcome:

#### Outcome A: Reject

Use when the proposal is redundant, obvious, or weaker than existing notes.

Action:

- do not create a note
- remove the log entry if it is now resolved or misleading

#### Outcome B: Fold into existing notes

Use when the proposal contains one useful clarification but not enough for a standalone note.

Action:

- update the strongest existing note, open question, or footer links

#### Outcome C: Add links in source ingests

Use when the proposal's main value is improved graph connectivity rather than a new claim.

Action:

- update the relevant `.ingest.md` files with missing connections and relationship text

#### Outcome D: Keep in the log

Use when the proposal points at something real but the mechanism is not yet clear.

Action:

- leave the log entry in place
- optionally sharpen its wording so the unresolved question is easier to revisit

#### Outcome E: Create the new note

Use only when the proposal survives the novelty tests and cannot be compressed into a smaller change.

Action:

- write the note following `kb/instructions/WRITING.md`
- connect it to the strongest related notes and indexes
- remove or revise the originating log entry

### 6. If creating a note, define the claim before writing

Before drafting, write a short note plan:

- one-sentence claim
- what existing note it most directly differs from
- what mechanism it adds
- what consequence or prediction it adds

If you cannot fill in all four, stop and choose a smaller outcome.

## Red flags

These usually mean "do not create a note":

- "X, Y, and Z are really phases/levels/strategies" with no new mechanism
- the proposal is justified mainly by combining two or three already-strong notes
- the best summary is "use the right approach at the right time"
- the proposal adds vocabulary but no decision value
- every useful connection is `extends` or `exemplifies`, but nothing depends on the new note

## Verify

Before creating a note, confirm all of the following:

- This note adds a mechanism the KB does not already have.
- This note would be a better traversal target than at least one existing note for a specific future question.
- This note cannot be replaced by a paragraph, link addition, or sharper open question.
- This note changes what a reader would predict, look for, or build.

If any line is false, do not create the note.
