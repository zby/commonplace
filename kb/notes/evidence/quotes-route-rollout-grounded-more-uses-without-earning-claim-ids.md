---
description: "A Commonplace grounding rollout recorded 30% grounded claim uses under a paraphrased claims ledger and 75% under verbatim quotes or pinned snapshots, with no case needing claim identifiers; the non-random cohorts make the gap descriptive"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [kb-maintenance]
---

# A quotes-route rollout grounded more claim uses without earning claim identifiers

Commonplace's 2026-08 grounding rollout checked source-dependent claim uses in
notes against their ingested sources in successive cohorts. Cohorts 01–10a used
a normalized claims ledger: each ingest entry held a paraphrased claim, exact
extracts, and authored scope, confidence, and limitation fields, and a review
compared the note's wording with the paraphrase. Cohort 10b used the direct
model adopted by [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md):
the note's use is judged against retained verbatim quotes or against the exact
pinned snapshot. The unit of comparison is one source-dependent claim use in a
target note, not a note, ingest, quote pair, or link.

## Terminal dispositions

| Population | Claim uses | Grounded, n (%) | Narrowed | Contradicted or repaired | Retained local delta | Literature handoff | False positive | Unavailable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Normalized claims ledger, cohorts 01–10a | 205 | 62 (30.2%) | 93 | 15 | 24 | 9 | 1 | 1 |
| Quotes or snapshot, cohort 10b | 59 | 44 (74.6%) | 2 | 1 | 5 | 7 | 0 | 0 |

Cohort 01's table was reconstructed from committed artifacts and review state
after its workshop closed.

## What this establishes

Under the direct model, a much larger share of claim uses ended grounded and a
much smaller share ended narrowed. The rollout also recorded no case that
needed a stable claim identifier, semantic deduplication of quotes, or
reconciliation between overlapping entries. The normalized-ledger cohorts
showed reuse and denser sections; cohort 08 was the nearest counter-signal,
where partly overlapping premises created modest reconciliation pressure, but
exact paraphrase plus scope and limitation still selected every use. In cohort
10b, six atomic recoveries appended 51 distinct verbatim source and location
pairs; similar passages with different local contexts coexisted and no accepted
pair required an identifier. A deterministic scan on 2026-08-25 found 19 link
occurrences carrying the `(snapshot required)` marker across seven of 68
frozen target notes, each with its exact-byte snapshot present, so the
snapshot route was used rather than merely available.

For a corpus of this size and shape, the direct model did not earn claim
identifiers, deduplication, or reconciliation machinery. That is the inference
this record supports.

## What this does not establish

The cohorts were successive and non-random, differed in content and execution
phase, and ran under non-equivalent review protocols. The gap between 30.2% and
74.6% is descriptive, not a causal estimate of the representation's effect.
Neither rate tests whether a grounded use preserves the source's proposition.
The record supplies no threshold at which a larger, more repetitive, contested,
or multi-writer corpus would need identifier or reconciliation machinery, and
does not show that such a corpus never would.

---

Relevant Notes:

- [ADR 073: untracked source snapshots require ingest grounding](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md) — see-also: the decision whose V1 scope this record bounds
