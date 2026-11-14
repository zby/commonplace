---
gate_id: higher-order/direct-tests
name: Higher-order concern, asked directly with three tests
description: 'The note needs a change to what it is (a split, a merge, a rehome, a rejection or a different claim), judged directly with a parent-loss test, a title-against-body test and a policy-or-claim place test.'
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
  that has one;
- the notes it links to, where you need them to judge whether its
  contribution is its own;
- the notes that link to it, where you can find them by searching for its
  file name.

Then ask one question: does this note need a change to what it is? Apply
three tests on the way and report each one's answer in `### Summary`.

- **Parent-loss test.** Name the note's parent: the note it most directly
  extends or applies. Suppose this note were deleted and its one best
  sentence added to that parent. List what a reader of the parent would
  then miss. Count only a claim, a mechanism or a condition that the parent
  does not already state, even briefly. Elaboration of a point the parent
  already states does not count, however developed it is: worked
  mechanisms, defeat conditions, scope sections, open questions and
  examples belong to the parent's point. If the list is empty or holds only
  elaboration, the note is a `merge` candidate, or a `reject` candidate if
  no note would take the sentence. A parent that links to this note with
  `extends`, or says this note develops a point, shows only that someone
  once split the point out. Treat such a link as neutral.
- **Title-against-body test.** State the claim the body ends up arguing,
  taken from its later sections: the last argued section, the scope or
  conclusion, and any test, ablation or revision the note reports. Do not
  take it from the opening paragraph, which usually repeats the title. Then
  compare that claim with the title. If the title asserts something the
  later sections deny, narrow, generalize to a different subject, or no
  longer argue, the note is a `different-claim` candidate. Name the
  sentence of the later sections that diverges.
- **Policy-or-claim test.** Decide whether the note tells the reader what
  to do, or says what this knowledge base or its maintainers do, adopt or
  require, for example in the first person ("we adopt", "we treat") or as a
  rule for this system. Such content is a policy, procedure or proposal.
  Compare that with a claim about what is true of systems of this kind,
  which holds whether or not anyone adopts it. Decide this from the note's
  text before you read the collection contract. A note whose central
  content is a policy, procedure or proposal is a `rehome` candidate, or a
  `split` candidate if it also carries a claim of its own. Then quote the
  collection contract's sentence on what the collection holds, and say
  whether it changes your answer.

Choose the result:

- PASS: no proposal. The parent-loss test names a claim, mechanism or
  condition the parent lacks; the later sections argue the title's claim;
  the central content is a claim, not a policy; and the claim is supported
  well enough to stand. Problems that remain are lower-order.
- WARN: a weak proposal. A change of one of the five kinds might be
  beneficial, but the note can stand as it is, and lower-order editing on
  it would not be wasted.
- FAIL: a strong proposal. You expect that an operator who reads your grounds
  would change what the note is before anyone edits its wording, because an
  edit to the current text would likely be thrown away.

Most notes in a maintained collection need no change of this kind. Use WARN
only when you can name the specific change and, for a merge, the note that
would receive the content; do not use WARN to record doubt you cannot ground.

Report the proposal in `### Findings`:

- For PASS, write one line `- INFO: no proposal`, optionally followed by
  lower-order observations marked INFO.
- For WARN or FAIL, write one line first:
  `- <WARN|FAIL>: kind=<split|merge|rehome|reject|different-claim>; <grounds>`.
  The grounds name the passages of the note and the paths of the other notes
  they rest on. If more than one kind applies, give the line for the one you
  would do first and list the others after it as INFO.
