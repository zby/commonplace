---
gate_id: higher-order/claim-need
name: Higher-order concern, from who would need the claim
description: 'The note needs a change to what it is (a split, a merge, a rehome, a rejection or a different claim), judged by stating its claim, asking which notes would need it, and checking it against the collection contract.'
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

Read the note and the `COLLECTION.md` of the collection it belongs to: the
file of that name in the note's own directory, or in the nearest parent
directory that has one. Work through these steps and show the results of
steps 1 to 5 in `### Summary`.

1. **Claim.** State in one sentence the claim the body argues, in your own
   words and without reusing the title. Then state what the title claims.
   Say whether the two are the same claim.
2. **Contributions.** List the note's distinct contributions: claims,
   mechanisms, conditions and arguments that carry weight. List at most
   five. For each, say what kind of content it is: a transferable claim or
   mechanism, or a policy, procedure, proposal or description of one
   system.
3. **Need.** For each contribution, ask who would need it. Find the notes
   that link to this note (search for its file name) and the notes it
   links to. Name each note that would lose an argument, a premise or a
   condition if this note were deleted, and say what it would lose. A link
   alone is not need: a parent that links here with `extends`, or says
   this note develops a point, shows only that the point was split out once.
   If the parent could carry the contribution in one sentence or one
   paragraph, say so and name the parent.
4. **Beyond the premises.** Say whether the central claim adds anything
   beyond the premises it is built from. A claim that follows from its
   premises by definition, or restates what the premise notes already say
   with a new name, adds nothing. Say also whether the claim is supported by
   the note's argument, or contradicted by its own text or by the notes it
   relies on.
5. **Place.** Quote the sentence of the collection contract that decides
   whether this kind of content belongs in this collection, and say whether
   the note fits it. If you could not read the contract, say so.
6. **Decide.** Map the findings to a proposal:
   - title and body claims differ materially: `different-claim`;
   - the parent could carry the note's contributions in a section or less,
     and no other note needs them separately: `merge`; if nothing would be
     lost at all, `reject`;
   - the central claim adds nothing beyond its premises, or is unsupported
     or contradicted: `reject`;
   - contributions of different kinds, or contributions needed by different
     notes with nothing tying them together: `split`;
   - the note is of a kind its collection contract does not hold: `rehome`;
   - otherwise: no proposal.

Choose the result:

- PASS: no proposal. Some note needs the central contribution as this note
  states it, the claim adds something beyond its premises, and the note
  fits its collection. Problems that remain are lower-order.
- WARN: a weak proposal. Step 6 points to a change, but the note can stand
  as it is, and lower-order editing on it would not be wasted.
- FAIL: a strong proposal. You expect that an operator who reads your steps
  would change what the note is before anyone edits its wording, because an
  edit to the current text would likely be thrown away.

Most notes in a maintained collection need no change of this kind. Use WARN
only when step 3, 4 or 5 names the ground; do not use WARN to record doubt
you cannot ground.

Report the proposal in `### Findings`:

- For PASS, write one line `- INFO: no proposal`, optionally followed by
  lower-order observations marked INFO.
- For WARN or FAIL, write one line first:
  `- <WARN|FAIL>: kind=<split|merge|rehome|reject|different-claim>; <grounds>`.
  The grounds name the passages of the note and the paths of the other notes
  they rest on. If more than one kind applies, give the line for the one you
  would do first and list the others after it as INFO.
