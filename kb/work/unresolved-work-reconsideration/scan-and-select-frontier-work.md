---
description: "Use to scan theory and reference for possible work, select up to ten comparatively straightforward useful next steps, and retain enough evidence to reconsider the selection later."
type: types/instruction.md
---

# Scan the unresolved frontier and select straightforward next steps

Help an agent choose useful work it can advance now, while leaving harder items
on the [unresolved frontier](../../reference/definitions/unresolved-frontier.md)
available for later reconsideration.

## Commission

An operator or parent invokes this workshop draft. Start without requesting
configuration: default to improving work in this KB, assessing up to twenty
candidate items and returning up to ten next steps—not a quota. Discovery may
scan more headings; an item counts toward the budget once its substance is
inspected. Use supplied prior results or change ranges when available; otherwise
assess current state. Return the record in the response unless an output
location is authorized. The caller may override these defaults.

Discover candidates only in `kb/theory/` and `kb/reference/`, recursively;
the caller may narrow that scope. Targeted reads elsewhere may verify a candidate
or its contracts, but must not expand discovery. Inspect local files read-only.
Do not execute tasks, delegate, acquire external sources or alter review/freshness
state. Write a new scan record only at an authorized location; otherwise return
it in the response.

## Approach

Choose the search and comparison method within those bounds. Headings such as
Open Questions, Unresolved, Future Work, Remaining and Next Steps are useful
clues; ledger entries and live proposals are others. Read enough context to
identify actual work, combine duplicate occurrences and check whether later
work already answered or superseded it. Respect current ownership and deferral
conditions. A heading match is not an assessed task.

Prefer candidates with a concrete benefit, a bounded next action, a known
approach and a meaningful check. Compare their ease and usefulness rather than
inventing absolute scores. A small probe may qualify even when the surrounding
question is hard. Do not force a speculative solution or redesign a workflow
to fill the shortlist. Stop at the budget and report fewer candidates if needed.

When prior assessments exist, check their versions and reasons before reuse.
Unchanged question text does not guarantee unchanged tractability: new evidence,
capabilities or priorities may unlock it. Include some older, unchanged items
in repeat scans rather than looking only at known dependencies. “Not selected”
means neither resolved nor permanently impossible.

## Deliverable

Return a compact shortlist and its assessment basis:

- For each selected item: source, benefit, proposed next action and file scope,
  why it appears straightforward, verification, permission needed and the
  uncertainty that would stop execution.
- For other assessed items: source and brief finding or blocker. Distinguish
  these from candidates merely discovered but not read.
- For the scan: timestamp, objective, coverage and omissions, plus versions of
  this instruction and the material inputs actually assessed. Use retrievable
  revisions or hashes with retained passages; identify dirty inputs rather
  than treating repository HEAD as their version. Preserve prior scan records.

The result should let another session inspect the recommendation and determine
what needs reassessment. State evidence and version limits; do not claim complete
coverage, successful execution or permanent resolution. No review-store
integration or fixed record schema is adopted by this draft.
