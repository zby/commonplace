# Candidate procedure: pull the claim through the ingest before using it

Proposed by the operator 2026-08-24, after the
[first worked case](./worked-case-agents-navigate.md). Recorded as a candidate
under evaluation, not adopted.

## The procedure

When a note needs to use a claim from a source:

1. read the source snapshot, or the source directly;
2. extract the claim;
3. look in the ingest for that claim, and **add it there if missing**;
4. only then use the claim in the target note.

## Why the worked case supports it

The run found that the ingest contract carries three of four needed extractions
**voluntarily** — nothing requires them, and the contract's stated polarity points
the other way. `Extractable Value` is defined as "what is new relative to the
connection context," and `Connections Found` is instructed to "drop weak,
speculative, or duplicate edges." Both are novelty-oriented: they describe what a
source *adds*. A premise a note leans on is often the opposite — the least novel
thing the source contains, and the first thing a novelty filter discards.

This procedure inverts the direction. Ingest-time extraction is a push, and it
has to guess what will be needed. Use-time extraction is a pull: the ingest grows
a claim ledger driven by what notes actually cite, so coverage follows demand and
nothing has to be anticipated. It also makes ingest cost incremental rather than
a full mining pass up front, which matters when the corpus is dozens of papers.

## What it inherits for free

The fidelity half is already built. [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)
resolves every `verbatim`-marked quotation against the source it links, failing a
false verbatim claim, and `commonplace-verify-quotes` audits them across files. A
ledger entry carrying a verbatim quote is therefore **machine-checked with no new
machinery** — which is most of the deterministic half of the maintenance sweep
the [README](./README.md) anticipates.

One measured obstacle: the ingest run reported that this `pdftotext` capture
garbles the figure regions and Bayesian equations, so verbatim quotation from
those spans will fail ADR 046 resolution, while numeric results in running prose
captured cleanly. Claim extraction that depends on quote resolution therefore
depends on capture quality in a way nothing currently checks.

## What it does not do

**It does not repair the existing corpus.** The procedure fires when an author
reaches for a source. `agents-navigate-by-deciding-what-to-read-next` was written
without knowing the source existed, which is the whole problem. This is the
write-time half; the audit half is still the sweep.

**It does not catch contradiction.** The worked case's most valuable finding was
that the note's C4 is wrong by the source's own lights. That comparison needs the
note's claim inventory as an input. Steps 1–3 build a source-side ledger; nothing
in them asks whether a claim the note already makes survives contact.

## Open decisions

- **What triggers it.** "Uses a claim" needs a boundary or every passing mention
  pays the full cost. Probably: the note *rests on* the claim as a load-bearing
  premise, not merely mentions it.
- **Where the ledger lives.** The ingest schema fixes `headings.contains`, so a
  `## Claims` section is a schema change plus a migration story for 289 existing
  ingests that will not have one.
- **What an entry carries.** Candidate minimum: the normalized claim, a verbatim
  quote with locator, the scope conditions *for that claim*, and the transfer
  status. The worked case showed the last two are per-claim, not per-source —
  within one source the structural claim transfers and the learned-strengths
  mechanism does not, and the source settles what the construct is while settling
  no magnitudes.
- **Whether the ledger and the thin claim node are the same object.** If an
  ingest carries normalized citable claims, the [README](./README.md)'s open
  question about an intermediate node may already be answered — the ledger entry
  *is* the node, and no new artifact kind is needed. This is the strongest
  candidate answer to that question so far.
- **Link vocabulary.** Connect reported no label for "this source states the
  established version of a local claim written from recall," and routed the gap
  here. `is-evidence-for` was used as the nearest fit. Whether that needs a label
  is a conclusion for [linking-foundations](../linking-foundations/README.md);
  surfacing the need is this workshop's part.

## The retention gap this exposes — and a correction

An earlier claim in this file's "inherits for free" section was **wrong**: a
ledger entry carrying a verbatim quote is *not* machine-checked today, and the
wiring cannot exist under the current rules.

Measured 2026-08-24 with `commonplace-verify-quotes` over `kb/sources`,
`kb/notes`, `kb/reference`, and `kb/agent-memory-systems`:

```
Checked 1257 Markdown files: 0 match, 0 mismatch, 12 unresolved.
```

Not one verbatim quote resolves anywhere in this repo, and all twelve candidates
cite an **internal KB note**, not a source. No source quotation in the tracked
corpus is verifiable, because none exists in a checkable form.

The cause is structural, and two artifacts state the opposing halves:

- [ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)
  resolves a quote "against the markdown source it links," and lists as its
  third precondition that "the source snapshot is a checked-in file present at
  validation time."
- [`kb/sources/COLLECTION.md`](../../sources/COLLECTION.md) makes that false here:
  snapshots are "local materializations, not tracked authority," `.snapshots/` is
  ignored (`kb/sources/.gitignore:1`), authors must "never author a durable link
  to `.snapshots/`," and "a citation of what the source says points to the
  external `source` URL" — which the resolver cannot dereference, since it
  resolves file paths.

The mechanism is not broken. ADR 046 was prototyped on the sibling
`epistack-casebooks` corpus, where sources *are* checked in, and found 63 match /
18 mismatch / 6 unresolved over 87 candidates. Its precondition simply does not
hold in Commonplace.

**This makes carrying the quote in the ingest necessary, not merely tidy.** The
ingest is the only tracked artifact in the chain. Under a contract that declares
the snapshot non-authority and forbids linking to it, the quoted span has nowhere
else durable to live. A ledger that pointed at the snapshot would be pointing at
something a fresh clone does not have.

It is plausibly also the licensing-compatible retention form — a public repo can
carry short quotations where it cannot carry whole papers, which would explain
why `.snapshots/` is ignored in the first place. Recorded as a likely reason; the
motivation has not been verified against a decision record.

**The honest cost.** Once the quote lives in the ingest and the snapshot is gone,
nothing can re-derive it from the repo alone. The guarantee drops from
continuously checked to **attested once, with a recomputation path**:
`snapshot_sha256` names exactly which bytes the attestation was made against, so
verification is recoverable by re-fetching or by any local snapshot matching that
checksum — but it is not standing enforcement. That is weaker than
[enforce-or-omit](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md),
whose precondition 3 is precisely source-present-at-validation-time. The
weakening should be stated in whatever ships, not glossed.

It also extends a claim the KB already holds:
[a citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md).
The wrinkle here is retention rather than capture — a citation cannot assert more
*verifiability* than its retention preserves.

**Options, none selected.** Track snapshots for sources that claims are drawn
from; resolve opportunistically against a checksum-matched local snapshot when
one is present; extend ADR 046 to resolve through `source` plus checksum rather
than a body link; or accept attestation and say so. Each trades repo weight,
licensing exposure, and enforcement strength differently, and the option space is
what a proposal owes before an ADR — this belongs in
[`kb/reference/proposals/`](../../reference/proposals/README.md) once the forces
are laid out, not in a workshop conclusion.

**One incidental defect found on the way.** `commonplace-verify-quotes` walks
into the ignored `.snapshots/` directory and tries to resolve a mangled URL as a
file path (`kb/sources/.snapshots/http:/memory.md`). It scans ignored files.
