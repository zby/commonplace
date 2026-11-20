---
description: "Why Commonplace removed the ordinary note’s status field rather than letting current stand for endorsement in one collection and accurate attribution in another."
type: types/note.md
---

# What would `status: current` assert?

A casebook can accurately report that a source made a claim without endorsing the claim. When Commonplace reconsidered the `status` field on ordinary notes, one proposal would have let each collection say what `current` meant. In a theory collection it could mean “we endorse this”; in a casebook it could mean “we have attributed this accurately.” A reader seeing only the field could not tell which judgment had been made. This was a proposed design, not an observed misreading.

The difficulty was not just that readers would need to look up the collection. For the casebook, endorsement was **not a question the artifact answered**. Giving `current` a different interpretation would not make it an answer. And even within one collection, the existing status choices mixed maturity, currency and acceptance: a conjecture can be up to date without anyone having verified it.

[ADR 044](../adr/044-user-verification-replaces-global-note-status.md#considered-alternatives) records the choice. Commonplace removed the global field from ordinary notes. An optional `user-verified: true` records a narrower act: a human explicitly verified the note’s current substantive contents. Its absence records no such attestation; it is not a negative verdict. An old `current` value was not converted into verification. Authors could still describe a conjecture in prose, and specialised types such as ADRs kept their own lifecycle statuses. Letting each collection select separate status axes was considered, but the case did not require building that mechanism.

For a future field, the useful question is: **if this artifact moved unchanged, would a reader take it to assert something different, and would that matter here?** In this case the distinction mattered to readers and renderers working from the file alone. The decision does not establish that collection context must never affect interpretation. A later design needs its own account of who reads the field, what context they have, and what they might conclude incorrectly.
