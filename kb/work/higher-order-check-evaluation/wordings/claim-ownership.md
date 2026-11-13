---
gate_id: higher-order/claim-ownership
name: Higher-order concern, from claim ownership
description: 'The note needs a change to what it is (a split, a merge, a rehome, a rejection or a different claim), judged by stating its claim and finding which notes own each part of it.'
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

Work through these steps and show the results of steps 1 to 4 in
`### Summary`.

1. **Claim.** State in one sentence the claim the body argues, in your own
   words and without reusing the title. Then state what the title claims.
   Say whether the two are the same claim.
2. **Contributions.** List the note's distinct contributions: claims,
   mechanisms, conditions and arguments that carry weight. List at most
   five. For each, say what kind of content it is: a transferable claim or
   mechanism, or a policy, procedure, proposal or description of one
   system.
3. **Owners.** For each contribution, name the note that owns it: this note,
   or another note that states it as its own claim or develops it in a
   section. Look among the notes this note links to, and among the notes in
   the same directory whose file names share the contribution's key terms.
   Give the owner's path. Write "this note" only when no other note you
   found makes the contribution.
4. **Support.** Say whether the central claim is supported by the note's
   argument and the notes it relies on, contradicted by any of them, or true
   only by definition.
5. **Decide.** Map the findings to a proposal:
   - title and body claims differ materially: `different-claim`;
   - most contributions are owned by one other note, and what remains would
     fit there as a section: `merge`; if nothing of its own remains and no
     receiver needs it, `reject`;
   - contributions of different kinds, or contributions owned by different
     homes with nothing tying them together: `split`, or `rehome` when the
     whole note is of a kind its collection does not hold;
   - the central claim is unsupported, contradicted or true only by
     definition: `reject`;
   - otherwise: no proposal.

Choose the result:

- PASS: no proposal. The note owns its central contribution, argues it, and
  is in the right place. Problems that remain are lower-order.
- WARN: a weak proposal. Step 5 points to a change, but the note can stand as
  it is, and lower-order editing on it would not be wasted.
- FAIL: a strong proposal. You expect that an operator who reads your steps
  would change what the note is before anyone edits its wording, because an
  edit to the current text would likely be thrown away.

Most notes in a maintained collection need no change of this kind. Use WARN
only when step 3 names the other note or step 4 names the defect; do not use
WARN to record doubt you cannot ground.

Report the proposal in `### Findings`:

- For PASS, write one line `- INFO: no proposal`, optionally followed by
  lower-order observations marked INFO.
- For WARN or FAIL, write one line first:
  `- <WARN|FAIL>: kind=<split|merge|rehome|reject|different-claim>; <grounds>`.
  The grounds name the passages of the note and the paths of the other notes
  they rest on. If more than one kind applies, give the line for the one you
  would do first and list the others after it as INFO.
