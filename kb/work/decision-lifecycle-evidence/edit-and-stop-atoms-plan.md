# Plan: edit operations and stops as atoms

## Status

Written on 2026-11-15 at the operator's request, after the first review
slice shipped under
[ADR 132](../../reference/adr/132-review-atoms-retain-observations-behind-current-results.md).
It was written as a plan. Its first two changes were built on 2026-11-15
and 2026-11-16; see "What was built" at the end. It covers the two atom
groups that follow the review operations: edit operations and stops. It
does not arrange atoms into procedures; grouping is decided after all
three groups are done.

The remaining review operations (the compression checks and their
synthesis, composition friction, premise decomposition, connect) are
being admitted separately and are not planned here.

## The target

Each atom meets the same contract as an admitted review operation:

- a typed instruction file;
- inputs that are files;
- a typed stored result;
- a way to run it alone and test it alone.

The plan reuses what the review slice built and adds as little as
possible beside it.

## What the review slice settles for the other groups

Five decisions of ADR 132 carry over unchanged.

1. **The worker supplies content; code supplies provenance.** The worker
   writes the changed text and its report. Code adds the operation, the
   hashes, the model, the run and the launch, and validates the whole
   result.
2. **An execution is an observation.** The exact input text, instruction,
   prompt, contract and raw output are retained per execution. A current
   result can be replaced without losing them.
3. **Acceptance is deterministic and separate from judgment.** Code
   accepts or rejects the form of a result. Acceptance does not say the
   edit is good.
4. **Controller failures stop; only worker defects go back for
   correction.** A correction that would repeat a rejected request stops.
5. **A fixture reruns one execution** from retained inputs, in its own
   tree, publishing nothing.

One decision does not carry over. A review result has a freshness state,
because it is a statement about a note that may since have changed. An
edit result is a candidate text made from one input text. It is never
stale; it either matches the input hash it names or it is about another
text.

## Edit operations

### What exists

- The [edit-operation type draft](./edit-operation-type.md), with a
  schema checked against one pass.
- Eight [simplification passes](../../instructions/simplification-passes/README.md),
  six of which fit the draft.
- Ten fix strategies in
  [one file](../../instructions/fix-warnings/fix-strategy-taxonomy.md).
- Code that already launches a pass worker and checks its candidate:
  `src/commonplace/lib/review_workflows/revise.py` and `edits.py`. The
  bounds check there refuses a changed title, H1, type or description
  and new validation failures.

### Decisions proposed

**E1. Register the type as drafted, with one addition.** The type goes to
`kb/types/edit-operation.md`. Its fields are `effort`, `depth`,
`decision` and `responds-to`, as drafted. The operator's two
declarations map to existing fields: "what it responds to" is
`responds-to`, and "its level" is `depth`. The field keeps the name
`depth`, because `level` already names the severity of a review finding
(`info`, `warn`, `fail`). Both declarations are best effort and are
corrected from runs.

**E2. One typed result, `edit-result`.** The worker returns one of three
things, as the draft states. The result records which:

| `outcome` | Worker supplies | Code checks |
|---|---|---|
| `changed` | the complete candidate text and one report line per change | bounds hold; the candidate differs from the input |
| `unchanged` | a report saying why nothing changed | the candidate equals the input |
| `proposed` | a list of proposed changes, applied to nothing | each entry quotes a passage found once in the input, by the shared quote matcher |
| `problem` | what blocked the operation | nothing else is present |

Code adds the operation path, its hash, the input text hash, the
candidate text hash, the model, the run and the launch. The candidate
text is a file in the observation, not a field of the result.

**E3. Bounds are the deterministic acceptance.** They are the checks
`edits.bounds` already makes, plus two the draft's contract names and
code does not yet check: every link target in the input is still present
unless the report names its removal, and every quoted span is
unchanged. An operation's own `## Preserve` section stays a worker rule;
code checks only the shared contract.

**E4. One execution route, in code.** An edit operation runs alone as

```
commonplace-review run edit OPERATION NOTE [--input ROLE=PATH] [--text PATH]
```

It reuses the observation and fixture machinery. It writes nothing to
the checkout. `--text` supplies a start text other than the checkout's
note, so that operations can be chained by a later procedure and so
that a test can use a saved text. This is the operator's focused pass
in its smallest form: one named operation on one note.

The consumer that justifies the command is the revise workflow. Its
pass launch moves onto this route, so that one writer produces every
pass candidate. The revise workflow keeps its own composition: the
plan, the order and its stops.

This departs from the procedure proposal, which has a session agent run
edit operations by following instructions. The reason is testability.
Running an operation alone, repeating it on the same input and
rerunning it from a fixture all need the exact inputs retained, and
code already does that for reviews. A session agent can still call the
command.

**E5. Convert the material in one change.**

| Material | Change |
|---|---|
| readability-and-flow, narrow-overclaims | type, `decision: none`, three headings |
| plain-wording, abstractions | type, `decision: per-item`, three headings; the strike list becomes the `proposed` outcome |
| audit-a-prior-pass, place-external-systems | type; the extra files they read are named as `--input` roles |
| opening-and-title | type; title proposals are reported, not applied |
| the ten fix strategies | one operation, "fix a finding by a named strategy", with the finding supplied as an input file |
| split-out-a-treatment | stays outside the type; it writes a second file |
| full-pass body edits and copyedit | not converted; they are steps of the full pass until grouping |

**E6. Applying an approved list is the same operation run again.** A
`per-item` operation returns `proposed`. After the stop, it runs a
second time with the answered list as an input and returns `changed`.
Code checks that only approved entries were applied.

### How one edit operation is tested

1. **Acceptance tests with a fake worker**, for each outcome and each
   bounds failure.
2. **One live run per converted operation** on a real note, read by the
   operator.
3. **A fixture from that run**, so that a changed wording of the
   operation can be rerun on the same input.

A review of the text before and after is weak evidence that an edit
worked. The [first run](./first-run.md) showed verdicts moving for
reasons other than the edits. The plan therefore does not make a
re-review part of an edit operation's test. The operator's decisions on
`per-item` lists are the first calibration evidence.

## Stops

### What exists

Four stops, in three procedures:

| Stop | Question put to the operator | Where the answer is kept today |
|---|---|---|
| strike list | approve or strike each proposed replacement, with a reason per strike | the list file and the run's operator record |
| hand-back disposition | what to do with each claim-level proposal | packet resolution fields |
| `deferred` item | none; the agent sets it | a free-form fix report |
| exact publication approval | may this exact text replace the note | `publication.json` in the run |

There is also the
[answers schema draft](./improvement-run-answers-schema.md), which
already defines one item per decision with `state`, `reason` and
`decided-by`.

### Decisions proposed

**S1. A stop is an instruction for a session agent with the operator.**
It is the one kind of atom that no worker runs. Its contract: it reads a
question file, presents each item, records the operator's answer, and
decides nothing itself.

**S2. Two stops, not four.**

- **Decide items.** The operator answers each item of a list. The strike
  list and the hand-back disposition are this stop over different item
  kinds. [Resolve a strike list](../../instructions/decide-items.md)
  is already this procedure and becomes its general form.
- **Approve a text.** The operator approves one exact candidate text for
  publication.

`deferred` is not a stop. It is a state of an item that the operator has
seen and not decided. An agent may not set it without the operator.

**S3. One typed result, `answers`.** It is the drafted answers schema,
registered as a shared type. The question file is whatever produced the
items: an `edit-result` with outcome `proposed`, or a review result
whose findings are proposals. The answers file names the question file
by hash, so an answer cannot be read against a list that has changed.
An approval of a text is an answers file with one item that names the
candidate's hash.

**S4. Deterministic acceptance for answers.** Code checks:

- every item of the question appears once, unaltered;
- every item is `pending`, `approved`, `rejected` or `deferred`;
- `rejected` and `deferred` carry a reason, and `deferred` a condition
  for revisiting;
- `decided-by` is `operator` for every decided item;
- the question hash matches.

The revise workflow enforces most of this for strike lists today, in
its own format. That check moves to the shared validator.

**S5. Publication stays in code.** Writing an approved candidate to the
checkout is not an edit operation and not a stop. Code performs it when
an `answers` file approves the candidate's exact hash and the note in
the checkout still has the input hash. The existing publication code
does this; it changes only in what it reads.

### How a stop is tested

A stop cannot be tested by repeated model trials, because the operator
is the one who answers. Two things can be tested:

1. **The acceptance rules**, with valid and invalid answers files.
2. **The presentation**, by one live session per stop in which the
   operator answers a real list, and by reading whether the recorded
   answers say what the operator said.

## Order of work

Three changes, each large and each cut over without a compatibility
layer.

1. **Edit operations.** E1 to E6: the type, the result, the command, the
   bounds, the converted passes and fix strategies, the revise workflow
   moved onto the route. Live check: each converted operation once.
2. **Stops.** S1 to S5: the answers type, the two stop instructions, the
   shared validator, the revise strike-list format replaced by
   `edit-result` and `answers`, publication reading `answers`.
3. **Declarations on review operations.** Each review operation gains
   `depth`, so that a later procedure can order all three groups by one
   field. What a review operation responds to is its own criterion, so
   it needs no second field. This is small and can ride with either
   change above.

After these, the grouping into a full pass, a quick pass and a focused
pass can be decided with every atom runnable alone.

## What this plan changes in earlier drafts

- **The run types are no longer the harness for one edit operation.** The
  [README](./README.md) kept the five improvement-run types for that
  purpose. With observations retained by code, a single execution needs
  only its `edit-result`. The run types return when a procedure with
  several steps needs one record; that is a grouping question.
- **The edit-operation draft's fourth open choice is closed.** The pass
  headings are renamed now, in the same change that moves the revise
  workflow.
- **The proposal's "what this gives up" shrinks.** The proposal accepted
  losing the code refusal of a changed title and the binding of an
  approval to an exact text. Under E3 and S5 both are kept.

## Choices for the operator

1. **A code route for edit operations (E4).** Recommended, for
   testability. The alternative is the proposal's session-run edits,
   which are cheaper to build and cannot be rerun from a fixture.
2. **Two stops (S2).** Recommended. The alternative keeps the four
   existing stops and types each.
3. **Operations that write a second file.** Recommended: keep
   split-out-a-treatment outside the type until a procedure needs it.
4. **The full pass's body edits and copyedit.** Recommended: leave them
   until grouping. The alternative writes them as two edit operations
   now, which would let the full pass retire sooner.
5. **A check of a proposed fix before it is applied.** The
   [README](./README.md#candidate-for-the-later-edit-operation-work-check-a-proposed-fix)
   holds this candidate. It is a review operation whose target is a
   candidate text with its input, so it needs no new machinery once E4
   exists. Recommended: draft it after the first live edit runs show
   which defects the bounds miss.
6. **INFO-level findings.** The first run read them and recorded
   nothing. This plan does not decide whether a fix operation receives
   them; it is a grouping question unless the operator wants it settled
   with E5.

## What is not known

- No edit operation has been run on the proposed route. The bounds for
  links and quoted spans may reject sound edits, as byte-exact quote
  anchors did for reviews.
- Whether one wrapped fix-strategy operation gives results that can be
  told apart by strategy is untested.
- The `depth` values on the passes were set for the revise workflow's
  order. Nothing shows they are right as a general order of concerns.

## What was built

The first two changes are on main, each from this plan.

| Change | Decision record | Live check |
|---|---|---|
| Edit operations | [ADR 133](../../reference/adr/133-edit-operations-run-alone-through-one-typed-route.md) | one operation that edits directly and one that asks first, on one note; three launches, no rejection |
| Stops | [ADR 134](../../reference/adr/134-stops-record-the-operators-answers-in-one-typed-file.md) | proposals, a typed answers file with one rejected, one deferred, one pending and seven approved items, then the apply run; only the approved passages changed |

The remaining review operations were admitted in the same period under
[ADR 132](../../reference/adr/132-review-atoms-retain-observations-behind-current-results.md):
the four compression checks, their synthesis, composition friction and
premise decomposition. Connect stays on its own route.

Where the build departs from the plan:

- **E6 is weaker.** Code checks that the passage of every item that is not
  approved is unchanged. It does not detect a change outside the list,
  because one operation replaces a term throughout the text.
- **The full pass's hand-back disposition stays on its packet.** Its
  states and its single resolution for the whole hand-back are not
  answers states. Moving it means redesigning the packet, which is a
  grouping question.
- **The fix procedure keeps its free-form report.** Only its wording
  changed: an undecided item is `pending`, and `deferred` needs the
  operator's word.
- **Publication changed for the full pass too,** because it shares the
  publication code with the revise workflow.

Not yet done:

- **No operator session has used either stop.** The answers in the live
  check were written by the agent as a mechanism test and marked as
  such. "How a stop is tested" asks for one live session per stop.
- **No revise run has gone through to publication** on the new route
  outside the tests.
- **The third change,** `depth` on review operations, is not built.
- **Edit quality is unjudged.** The live checks show that real output is
  accepted, not that the edits are good.
