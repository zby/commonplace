---
gate_id: frontmatter/claim-strength
name: Claim strength
description: 'The title is phrased as a claim but only asserts a truism or a point nobody knowledgeable would contest.'
type: types/review-gate.md
lens: frontmatter
watches: [title]
staleness: changed
depth: 2
requires_trait: title-as-claim
---

## Failure mode

The title is phrased as a claim but only asserts a truism or a point nobody knowledgeable would contest.

## Test

Ask whether someone informed could reasonably argue the opposite. If not, the claim is weak.

Watch for **presupposed claims**: titles shaped like "`<hard noun phrase>` lets / enables / allows `<obvious consequence>`" smuggle the contestable claim into the subject and leave a near-truism as the main predicate. Ask whether the main verb asserts the hard point or assumes the subject already exists; if it assumes it, promote the presupposition into the main claim.

The fix is usually to sharpen the title to the non-obvious point the note actually establishes, or to switch to a topical title when the note is not making a contestable claim.

Topical titles remain valid for multi-claim specs, frameworks, definitional notes, indexes, and exploratory drafts.

## Example (fail)

- `continuous learning is substrate-independent`
- `validation should be fast`
- `a unified interface lets programmers choose prompts or code` *(presupposes prompts and code can share one interface; the predicate only restates what an interface does)*

## Example (pass)

- `continuous learning can happen outside of weights`
- `deterministic validation should be a script`
- `code and prompts can share a unified interface so programmers choose between them`
