---
gate_id: accessibility/abstract-claim-without-case
name: Abstract claim without a case
description: 'A note whose central contribution is a distinction or an abstract mechanism shows no concrete case of it, so a reader cannot tell what it sorts or how it applies.'
type: types/review-gate.md
lens: accessibility
watches: [title, description, body]
staleness: changed
depth: 3
---

<!-- Draft in kb/work/concrete-cases-for-abstract-notes/. Not in the catalog. -->

## Failure mode

The note's central contribution is a distinction between two or more things, or a mechanism stated in general terms. The note states it and argues for it, but never shows it at work on a particular case. A reader can repeat the wording and still cannot say which side a given situation falls on, or what the mechanism does in one.

This gate asks only about the central contribution. It does not ask for a case under every assertion.

## Test

1. State the note's central contribution in one sentence, from the title, the description and the opening. Decide its kind:
   - **distinction**: the note separates two or more things and says they should not be confused;
   - **mechanism**: the note says how or why something happens, in general terms;
   - **neither**: the note reports a fact, a decision, a procedure or a survey. Return PASS; this gate does not apply.
2. **Wording test.** Read only the sentence or sentences that state the contribution. Can a reader name, from that wording alone, one particular situation it covers and one it excludes? A contribution stated in particular terms is its own case. "The validator checks links when a note is saved" needs none. If yes, return PASS.
3. Look for a **case** in the body. A case names a particular situation: a specific system, document, event, exchange or constructed scenario with enough detail that a reader could disagree about how the contribution applies to it. These are not cases: a list of categories, a restatement in other general terms, a term followed by "such as" and a class of things, or a link to another note that holds a case.
4. Decide what the contribution needs:
   - a **distinction** needs a case on each side, or one case shown falling on one side with a statement of what would put it on the other. It also needs the difference stated: what a reader would do, expect or check differently.
   - a **mechanism** needs one case in which the mechanism can be followed step by step.
5. A constructed case counts when the note marks it as an illustration. Do not require a case to be real, and do not judge here whether a case supports the claim.

WARN when the contribution is a distinction or mechanism, fails the wording test, and the body has no case for it. WARN when a distinction has a case on one side only and no statement of what would put a case on the other.

PASS otherwise. Under a PASS decision, add an INFO finding when cases exist but the difference they make is not stated, or when the only case sits far from the statement of the contribution.

This gate does not return FAIL. A missing case is a detectable gap, not a ground for escalation.

Do not flag here: a term used without a definition (`accessibility/undefined-terms`); a claim worded more abstractly than its argument (`semantic/unearned-generality`); an example from one narrow domain used without framing in a note that claims wider scope (a fix strategy, not this gate); a case that is too long for its role (`compression-bundle/detail-overhang`). When recommending a case, recommend the shortest one that lets a reader apply the contribution.

Do not flag instructions, ADRs, reference documents, indexes or logs. Their commands, paths and decisions are already particular.

## Example (fail)

A note titled "Removing an approval wait differs from removing an evaluation task" defines a wait as something execution cannot proceed without, and a task as something the specification assigns. It argues that reports of automation confuse the two. It never names a process in which one was removed and the other kept.

## Example (pass)

The same note adds: "Suppose adoption of a change is automatic, and the specification still assigns a maintainer a weekly review of adopted changes. Adoption no longer waits for anyone. The review is still owed. If the maintainer does nothing, adoption continues and the review goes undone." The case falls on both sides in a visible way, and the difference is stated.

## Example (pass — wording is already particular)

"A resumed sweep keeps the profile it opened with." No case is needed.
