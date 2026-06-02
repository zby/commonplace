---
description: Code-grounded reviews may anchor load-bearing claims to a verbatim source quote pinned to the reviewed commit, with no byte offsets or ids; resolution is a write-time check against the checkout while the standing validator checks only shape, because the reviewed source is not retained in the KB
type: ../types/adr.md
tags: []
status: accepted
---

# 023-Quote-anchored citations for code-grounded reviews

**Status:** accepted
**Date:** 2026-06-01
**Extends:** [ADR-011](./011-notes-must-be-accessible-to-external-readers.md)

## Context

`agent-memory-system-review` notes make agent-generated claims about external systems. Today those claims cite the source at **document granularity** — a source-relative file path in a code span, or a commit-pinned GitHub URL. That is enough to locate the file but not to check the claim: a cited file can be real while the cited paragraph does not support the assertion. The citation-faithfulness literature names this gap directly (a citation can be structurally correct yet unfaithful) and finds coarse document-level citation insufficient for verification.

The mature anchor format for "point at a span in a source that may drift" is settled prior art. The W3C Web Annotation Data Model and Hypothesis's fuzzy-anchoring implementation both converge on the same answer: the **quoted text is the robust anchor** (a `TextQuoteSelector`), and byte/character offsets are only an optional locating cache — they are brittle and never load-bearing for verification. The same work separates two layers we keep distinct here:

- **Structural grounding** — the quoted text actually appears in the cited source.
- **Semantic faithfulness** — the source actually supports the claim.

Only the first is mechanizable cheaply. The second is not left to ad-hoc judgment either: it is operationalized as the `semantic/grounding-alignment` review gate, which reads the cited source and checks attribution accuracy, scope overreach, and whether the conclusion follows from the evidence. This ADR addresses the structural half; the gate is its semantic complement, and the two are designed to compose — quote-anchoring narrows the structural question to a deterministic check so the gate's LLM judgment can spend itself on faithfulness rather than re-confirming the quote exists.

One constraint is specific to this collection and shapes the whole design: **the reviewed source is not retained in the KB.** ADR-011 and the review type require reviews to remain readable without the source; the type's constraints forbid storing the source tree under `reviews/`; the checkout (`source_dir`) is transient, prepared by the parent skill at review time and gone afterward. So a later, repo-local validator cannot resolve a quote against the source — the bytes are not there. But review citations pin an **immutable commit**, so "does this quote resolve?" is a one-time question answered at authoring time, not a drift question that recurs.

## Decision

Adopt **quote-anchored citations** for code-grounded reviews, defined in the `agent-memory-system-review` type spec's Citations section.

### The convention

A load-bearing claim may be anchored by quoting the verbatim supporting text as a blockquote whose final line is a `---` attribution naming the source location pinned to the reviewed commit (a source-relative path in a code span, or a commit-pinned blob URL). The quoted text is the anchor; the pinned commit is the position. **No byte offsets, character spans, or ids** — the quote is self-relocating and the commit is immutable, so nothing else is needed.

### Optional and additive

Used on the claims that carry a review, not on every sentence. Existing citations and outbound links are untouched; validation fires only where the convention is actually used. No migration.

### Verification splits by where the source lives

- **Resolution is a write-time check.** Confirming a quote appears in its pinned source is owned by a separate instruction (`verify-review-quote-grounding`) run against the live checkout, while the checkout still exists. It is kept *out* of the `write-agent-memory-system-review` skill to keep that skill a thin contract; quote errors are expected to be rare, so a runnable-on-demand procedure is sufficient.
- **The standing validator checks shape only.** For reviews it confirms each quote-anchored citation is well-formed and names a source. It cannot resolve the quote offline, because the source is not retained — and does not need to, because the pinned commit cannot drift.
- **`kb/sources/` is where standing resolution would live.** Snapshots there *are* retained immutably in the repo, so a future standing validator could resolve quotes against them with no network. Not built now (one use site today); recorded as the natural home if the convention is reused.

### It lives in the type spec, not `COLLECTION.md`

`agent-memory-systems/COLLECTION.md` owns outbound links into *other KB collections* (labelled edges drawn from the shared vocabulary). A quote-anchored citation points at the reviewed system's external source, not at another KB artifact — it has no destination collection and no catalogue label, so it is not an outbound-linking rule. The COLLECTION file already delegates this concern ("code-grounded reviews cite the repo directly"; "the workflow and section rules live in `types/agent-memory-system-review.md`"). Per ADR-019, type-specific divergence is owned by the type definition. The convention extends the type spec's existing Citations section.

## Consequences

### Easier

- **Claims become self-evidencing.** A reader sees the supporting text inline instead of a file path they cannot open — this *strengthens* ADR-011 rather than fighting it.
- **The structural half of grounding becomes mechanical.** The `grounding-alignment` gate's "quote-level accuracy" check gets a deterministic component, freeing the gate's judgment for whether the claim follows.
- **No schema, no new file kinds, no offsets.** The anchor is markdown the review already contains; the validator reuses document parsing.

### Harder

- **Authors must quote precisely.** A paraphrase in the blockquote fails resolution. The blockquote must be verbatim.
- **Resolution is only as good as the moment it runs.** Because the source is not retained, a quote that was never verified at write time cannot be verified later from the KB alone — it would require re-fetching the external repo at the pinned commit.

### Not changing

- Document-level citations remain valid for ordinary claims; quote-anchoring is opt-in for load-bearing ones.
- Semantic faithfulness remains the `semantic/grounding-alignment` gate's job; no validator check claims to cover it. This ADR only hands that gate a firmer structural floor to stand on.
- The reviewed source stays out of the KB (ADR-011 and the type constraints stand).

## Relevant Notes

- [ADR-011: notes must be accessible to external readers](./011-notes-must-be-accessible-to-external-readers.md) — foundation: the "readable without the source" requirement this convention serves by carrying evidence inline
- [ADR-019: collection-owned link vocabulary](./019-collection-owned-link-vocabulary.md) — boundary: why a source citation is a type-spec concern, not a COLLECTION outbound-linking rule
- [agent-memory-system-review type spec](../../agent-memory-systems/types/agent-memory-system-review.md) — where the convention is defined
- [verify-review-quote-grounding](../../instructions/verify-review-quote-grounding.md) — the write-time resolution procedure
- [grounding-alignment review gate](../../instructions/review-gates/semantic/grounding-alignment.md) — see-also: the semantic complement — this ADR's structural check narrows the question the gate's judgment then answers
