---
description: "Proposal: make a note's use of a grounded source claim mechanically checkable, by carrying the ingest's normalized claim string or by requiring the verbatim citation convention, rather than resting on a semantic review lens"
type: ../types/design-proposal.md
tags: []
---

# Deterministic note-to-ingest claim checking

Source grounding under [ADR 073](../adr/073-untracked-source-snapshots-require-ingest-grounding.md)
has three hops. Two are now deterministic. The third is not, and the reason is
that nothing durable connects a note's wording to the ingest entry it depends on.

| Hop | Assertion | State |
|---|---|---|
| source → ingest | `Source extract (verbatim)` occurs in the pinned snapshot | deterministic; base validator check |
| ingest entry | `Claim (paraphrase)` normalizes the source proposition | authored, not checkable |
| ingest → note | the note's use is supported by that entry | **semantic assay only** |

## Current state (as of 2026-08-24)

- The `source` review lens derives `(artifact, ingest)` pairs with the ingest on
  the criterion side, and asks an LLM whether `Claims` support the target's
  articulated use. 33 pairs recorded, all `pass`. It restales when either file
  changes.
- [`ground-source-dependent-claims.md`](../../instructions/ground-source-dependent-claims.md)
  says to reuse "its exact `Claim (paraphrase)` wording without mutation", and
  `cp-skill-write`'s guard says to *prefer* it. **Measured adherence: 4 of 65
  note-to-ingest pairs — 6%.** In the other 61 the note paraphrases the
  paraphrase, so no shared string exists.
- [ADR 046](../adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)'s
  checker is a `base` rule applying to every typed note. [ADR 069](../adr/069-collection-contract-bundles-become-one-time-prototypes.md)
  retired the profile that mandated the convention but not the check, so the
  convention is **universally enforced and nowhere required**. Corpus-wide the
  checker reports 1 match across 1264 files; that one was added deliberately as
  the first real use.
- Notes do quote — 55 citing notes contain long quotations — but only 3 distinct
  quoted spans occur in a cited ingest. Notes mostly quote something other than
  the source they cite.

## The problem

The semantic lens is **compensating for a lost invariant, not answering an
inherently semantic question.** If a note carried the ingest's normalized claim
string, "is this use supported?" would be substring containment — the same shape
ADR 046 already runs. Because the string is absent, only a judgment is left, so
an LLM assay becomes the sole instrument on the hop where a note actually
commits to a source.

That matters beyond elegance: the assay costs a model call per pair and yields a
verdict no one can re-derive offline, on the relationship most likely to drift.

## Forces

- **Exactness costs prose.** A normalized source-side proposition is often clumsy
  inside a note's argument. That is presumably why 61 of 65 reworded and why the
  instruction says *prefer* rather than *must*. Any option demanding verbatim
  reuse in body prose trades writing quality for checkability.
- **Not every citation can be `verbatim`.** [A citation cannot assert more
  fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md):
  a passage an ingest reproduces from a third party is `second-hand`, which ADR
  046 leaves unchecked by construction. A blanket requirement would push authors
  to overstate fidelity.
- **The semantic lens is not wasted either way.** Transfer and scope — whether a
  human-subject result carries to a bounded-context agent — are irreducibly
  judgments. A deterministic hop would narrow what the assay must decide, not
  remove it.
- **Enforced constraints outperform stated ones here, measurably.** In one run,
  the same agents scored 59/59 on the schema-checked entry shape and 179/184 on a
  fidelity rule three documents stated and no code implemented.

## Options

**A. Require exact reuse of `Claim (paraphrase)` in the note body.** Strongest
check, highest prose cost. Operativity: `cp-skill-write` hardens *prefer* to
*must*; a base check resolves the string against the linked ingest.

**B. Carry the normalized claim in a designated slot** — a footer line or the
labelled link context — where exactness costs the prose nothing and code can
still find it. Operativity: a slot convention in the notes contract plus the
same base check. Leaves body prose free.

**C. Require the `verbatim` convention on ingest citations.** No new machinery —
ADR 046's checker already runs universally. Operativity: a `kb/notes/COLLECTION.md`
clause. Bounded by the `second-hand` force above, so it cannot cover every use.

**D. Status quo.** The semantic lens carries the hop. Cheapest now; leaves the
commitment hop unverifiable offline and paying per-pair model cost.

These are not exclusive: B or C could cover load-bearing uses while D handles the
rest.

## Adoption criteria

Adopt when a worked cohort shows either that the semantic lens misses a use the
string check would have caught, or that its per-pair cost is material at corpus
scale. Until then the evidence supports opening the question, not settling it.

Whichever option ships, record what happens to prose quality — the 6% figure is
evidence that authors resist exact reuse, and an option that ignores that will be
complied with on paper and reworded in practice.
