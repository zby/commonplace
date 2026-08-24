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

## Argument 1: it fixes a polarity the contract has backwards

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

## Argument 2: the ingest is the only tracked link in the chain

This is the stronger argument, and it does not depend on the polarity point at
all.

`kb/sources/.snapshots/` is ignored (`kb/sources/.gitignore:1`), and
[`kb/sources/COLLECTION.md`](../../sources/COLLECTION.md) says why: snapshots are
"local materializations, not tracked authority." Nothing durable may link to
them, and "a citation of what the source says points to the external `source`
URL." So the evidence behind every source claim in this KB currently lives in a
directory a fresh clone does not have.

Measured 2026-08-24 with `commonplace-verify-quotes` over `kb/sources`,
`kb/notes`, `kb/reference`, and `kb/agent-memory-systems`:

```
Checked 1257 Markdown files: 0 match, 0 mismatch, 12 unresolved.
```

Not one verbatim quote resolves, and all twelve candidates cite an **internal KB
note** rather than a source. No source quotation in the tracked corpus is
verifiable, because none exists in a checkable form.

That reframes what the procedure is for. Step 3 — add the claim to the ingest if
missing — is not bookkeeping that makes premises easier to cite. It is **the
mechanism that moves source evidence from ignored local state into tracked
state**, one claim at a time, at the moment someone actually needs it. Without
something playing that role, the KB's source grounding is unbacked by
construction, not merely awkward to navigate.

Doing it per-claim is also what makes it affordable. Tracking whole snapshots
would mean carrying entire papers in a public repository, with the weight and the
licensing exposure that implies; short quotations are the retention form a public
repo can actually carry. So the incremental, demand-driven shape is not a
concession — it is the only version of this that is cheap enough and clean enough
to run.

## What already exists, and what does not

The convention exists; the enforcement does not reach sources.
[ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)
resolves `verbatim`-marked quotations against "the markdown source it links" and
fails a false claim, with `commonplace-verify-quotes` giving the corpus view. But
its third precondition is that "the source snapshot is a checked-in file present
at validation time," and in Commonplace that is false. The mechanism is not
broken — prototyped on the sibling `epistack-casebooks` corpus, where sources
*are* checked in, it found 63 match / 18 mismatch / 6 unresolved over 87
candidates. Its precondition simply does not hold here.

So a ledger entry would **not** be machine-checked today, and the wiring cannot
exist under current rules: the resolver dereferences file paths, and the only
file that holds the source text is one authors are forbidden to link.

Two consequences for the design.

**The guarantee available is weaker than enforce-or-omit, and should be stated as
such.** Once the quote is in the ingest and the snapshot is gone, nothing
re-derives it from the repo alone. What is achievable is *attested once, with a
recomputation path*: `snapshot_sha256` names exactly which bytes the attestation
was made against, so verification is recoverable by re-fetching or from any local
snapshot matching that checksum. That is not standing enforcement, and
[enforce-or-omit](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)'s
own precondition 3 is precisely source-present-at-validation-time. It extends a
claim the KB already holds —
[a citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md)
— with a retention wrinkle: a citation cannot assert more *verifiability* than
its retention preserves.

**Capture quality becomes load-bearing.** The ingest run reported that this
`pdftotext` capture garbles figure regions and the Bayesian equations, so
verbatim quotation from those spans would fail resolution, while numeric results
in running prose captured cleanly. Nothing currently checks that.

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

## Options for the enforcement question, none selected

Track snapshots for the sources claims are drawn from; resolve opportunistically
against a checksum-matched local snapshot when one is present; extend ADR 046 to
resolve through `source` plus checksum rather than a body link; or accept
attestation and say so plainly. Each trades repository weight, licensing
exposure, and enforcement strength differently. Laying out those forces is what a
proposal owes before an ADR, so the option space belongs in
[`kb/reference/proposals/`](../../reference/proposals/README.md) once it is
understood — not settled as a workshop conclusion.

Note that this question is *downstream* of the procedure, not a precondition for
it. Argument 2 holds whatever the enforcement answer turns out to be: the quoted
span has to reach a tracked artifact before there is anything to enforce against.

**One incidental defect found on the way.** `commonplace-verify-quotes` walks
into the ignored `.snapshots/` directory and tries to resolve a mangled URL as a
file path (`kb/sources/.snapshots/http:/memory.md`). It scans ignored files.
