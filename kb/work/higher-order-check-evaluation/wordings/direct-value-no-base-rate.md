---
gate_id: higher-order/direct-value-no-base-rate
name: Higher-order concern, asked directly with a value test
description: 'The note needs a change to what it is (a split, a merge, a rehome, a rejection or a different claim), judged directly with a value test and the collection contract.'
type: types/review-gate.md
lens: higher-order
watches: [title, description, body]
staleness: changed
---

## Failure mode

The note should not stay what it is. A higher-order concern is about what
the note is: its claim, its boundary, whether it should exist and where it
belongs. Five kinds count:

- `split`: the note carries two or more contributions that each need their
  own note, or a claim together with content of another kind, such as a
  policy, a procedure or a design proposal.
- `merge`: the note's contribution is already made by another existing note,
  or would fit there as a section or a paragraph; this note adds little of
  its own.
- `rehome`: the content belongs in another collection or another type, for
  example an operational policy or a design proposal sitting in a theory
  collection.
- `reject`: the central claim is unsupported, contradicted by the note's own
  text or by the notes it relies on, true only by definition, or obsolete
  against the system it describes, so that little worth keeping would remain
  after repair.
- `different-claim`: the title asserts something the body does not argue or
  denies, or the body's argument supports a materially different claim than
  the one the note makes.

A lower-order concern is about how the note says it: wording, flow, framing,
a missing link, a local error fixable without changing the claim, or a
qualifier to add or drop. Lower-order concerns are not this gate's subject;
they never justify WARN or FAIL here.

## Test

Read these inputs before choosing a result:

- the note;
- the `COLLECTION.md` of the collection the note belongs to: the file of
  that name in the note's own directory, or in the nearest parent directory
  that has one. Quote it when you judge whether the note is in the right
  place;
- the notes it links to, where you need them to judge whether its
  contribution is its own;
- the notes that link to it, where you can find them by searching for its
  file name.

Then ask one question: does this note need a change to what it is? Apply
two tests on the way.

- **Value test.** Suppose this note were deleted and its one best sentence
  added to its parent: the note it most directly extends or applies. What
  would a reader lose? Name the lost argument, mechanism or condition. If
  the answer is "little", the note is a `merge` candidate, or a `reject`
  candidate if no note would take the sentence.
- **Links are not ownership.** A parent that links to this note with
  `extends`, or that says this note develops a point, shows only that
  someone once split the point out. Treat such a link as neutral. It is not
  evidence that this note's contribution is worth a separate note.

Choose the result:

- PASS: no proposal. The note makes a distinct claim that it argues, the
  claim is supported well enough to stand, the value test names a real loss,
  and the note is in the right place under its collection contract.
  Problems that remain are lower-order.
- WARN: a weak proposal. A change of one of the five kinds might be
  beneficial, but the note can stand as it is, and lower-order editing on
  it would not be wasted.
- FAIL: a strong proposal. You expect that an operator who reads your grounds
  would change what the note is before anyone edits its wording, because an
  edit to the current text would likely be thrown away.

Report the proposal in `### Findings`:

- For PASS, write one line `- INFO: no proposal`, optionally followed by
  lower-order observations marked INFO.
- For WARN or FAIL, write one line first:
  `- <WARN|FAIL>: kind=<split|merge|rehome|reject|different-claim>; <grounds>`.
  The grounds name the passages of the note and the paths of the other notes
  they rest on. If more than one kind applies, give the line for the one you
  would do first and list the others after it as INFO.
- State in `### Summary` the value test's answer and the sentence of the
  collection contract you relied on for place, or say that you could not
  read the contract.
