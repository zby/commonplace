---
gate_id: semantic/vocabulary-reconciliation
name: Vocabulary reconciliation
description: "A technical meaning conflicts with existing usage, or different technical names may duplicate one concept without a consequential distinction."
type: types/review-gate.md
lens: semantic
watches: [body, frontmatter]
staleness: changed
---

## Failure mode

An artifact uses a technical name with a meaning that conflicts with existing KB
usage, or different names may duplicate one concept without a consequential
distinction.

## Test

Find specific vocabulary decisions worth revisiting during revision. Return
evidence-backed collision and unification candidates for the respective ledgers,
not adopted definitions, forced renames or instructions to avoid new terms.

### Evidence and discretion

Judge the artifact against the invoking KB's active vocabulary, definitions and
existing ledger decisions. Discover comparison material within the authorized
local corpus; do not acquire external sources. Choose search terms, comparison
cases and reading depth to resolve the candidate meanings. Exact-name search can
expose collisions but cannot establish that a concept has no existing name.
Record the inspected scope and limits; do not claim exhaustive coverage.

Recognize technical meanings even without an announced definition: ask whether
a name carries a distinction on which the argument or procedure depends.
Unfamiliarity, typography or repetition alone is insufficient. Ordinary wording,
quotations and historical mentions are not new bindings unless the artifact
adopts them as its own terminology.

This test requires authorized corpus discovery and identifiable KB vocabulary
context. If either is unavailable, return ERROR naming the gap; do not silently
substitute a linked-definitions-only check. Missing optional ledgers need not
block review, but their absence belongs in the scope report.

### Finding threshold

- **Collision:** establish the same name's competing meanings and show how
  confusing them could change an inference, classification, action, obligation
  or attribution. Respect explicit scope and schema positions; shared spelling
  is not enough.
- **Unification candidate:** propose a common account of the differently named
  concepts, explain what each contributes, and identify a condition that could
  distinguish them. Similar wording, shared examples or related goals alone
  justify neither a candidate nor a declaration of equivalence.

Honor existing ledger decisions unless the artifact violates their writing rule
or new evidence challenges them. Reference a matching pending entry instead of
proposing a duplicate. If both patterns apply, explain what each ledger would
track.

### Verdict and handoff

Return WARN for a supported, consequential unresolved finding; PASS when none
is found within the inspected scope. INFO may retain a weak lead but must not
be submitted as a supported ledger candidate. ERROR means the review could not
be completed under the evidence requirements above.

Each WARN must give:

- the kind, destination ledger and any matching entry;
- the names, meanings and exact supporting passages;
- artifact paths and inspected revisions or content hashes, including the target;
- the consequential misreading, or common account and distinguishing condition;
- the unresolved question, identifying new evidence or a violated rule when
  an existing decision applies.

New candidates are pending. Existing definitions and writing decisions remain
in force; adjudication chooses whether to tolerate, distinguish, unify or rename.
Whether a name earns its place or needs a gloss belongs to jargon/accessibility
review, not this gate. A clear, useful definition can still collide.

The reviewer owns only its review result. The coordinating workflow owns ledger
insertion, version checks and duplicate handling; it must retain candidates as
pending rather than manufacture decisions for writers. Do not edit the target,
definitions or shared ledgers, or claim that a candidate was saved without the
workflow's confirmation.

## Example (fail — collision)

An existing definition uses “capture” for preserving source text verbatim. A
new artifact uses it for inferring a reusable rule, then requires checking the
capture against the original text. The meanings imply different verification
obligations. Flag the conflicting passages, not a preferred replacement name.

## Example (fail — unification candidate)

“Inspection block” and “review cluster” both denote claims selected for joint
checking under a context limit, with the same membership rule and no stated
difference. Record that common account and ask whether their membership or
lifecycle conditions ever differ; do not declare them synonyms.

## Example (pass)

A browsing set favors discovery; a joint-checking set must fit a checking budget.
Their memberships can differ. Related members do not erase that distinction.
