# Grounding Commonplace claims in established sources

## Governing question

When a Commonplace claim is already established outside Commonplace, what
should carry the established part, and what must Commonplace author itself?

Concretely, two sub-questions that have to be answered together:

1. **What must a source ingest extract** so that "this note is subsumed by this
   source" becomes a determinable finding rather than an impression?
2. **Does the graph need a node between an ingest and a delta note** — a thin,
   normalized statement of the borrowed claim that several local notes can cite
   — or does an ingest plus a well-written delta note already carry it?

This workshop owns the upstream half: sources, what they must yield, and how
the borrowed claim attaches. The sibling
[literature-disposition](../literature-disposition/README.md) workshop owns the
downstream half — what happens to notes that turn out to restate a source.

## Current status — 2026-08-26

**Ready to close. The V1 extraction and attachment questions and the dated
source-corpus selection are complete for the current cohort.**

| Closure condition | State | Evidence or remaining work |
|---|---|---|
| Authoritative source corpus | **Done for the 2026-08-26 cohort** | [Wider source-corpus selection](./corpus-selection.md) records seven accepted, quote-backed source cases, the rejected or deferred candidates, and each transfer boundary. |
| Ingest extraction contract | **Done for V1, 2026-08-25** | [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md) retains minimum exact passages in `## Quotes`; broader support uses an explicit `(snapshot required)` route. |
| Intermediate claim node | **No new node in V1, decided 2026-08-25** | The rollout did not find enough identity, reconciliation, or reuse pressure to justify normalized claim or quote IDs. Target-specific transfer reasoning stays in the target. |

The operative path is source material → target claim, not source → ingest
paraphrase → target claim. A normal ingest link declares that its tracked exact
quotes are sufficient. A `(snapshot required)` link declares that the exact
name-paired, checksum-verified local snapshot is necessary. Both routes use the
standard `semantic/grounding-alignment` gate. The old normalized `## Claims`
ledger, virtual source lens, link-derived source review pairs, and
source-specific freshness behavior are retired.

The in-scope evidential blocker is now cleared for the claims in the dated
cohort. This is not an exhaustive literature claim: the selection records which
sources adjudicate the live claims, why other candidates were deferred, and
where each human or practitioner source stops. Target edits, grounding assays,
and final note dispositions are downstream handoffs to
[literature-disposition](../literature-disposition/README.md), not remaining
source-corpus work.

## Opening evidence — 2026-08-24

These measurements explain why the workshop opened. They are historical
baselines, not claims about the current corpus.

**The relevant literature is not ingested.** `kb/sources/` holds 289 ingests. A
search across it for `pirolli|foraging|information scent|berrypicking|
marchionini|ranganathan|faceted|orienteering|scatter/gather|hedden` returns
nothing. The information-seeking and knowledge-organization traditions that the
navigation and pointer notes reason inside have no source ingest anywhere in
the KB. Three notes mention the names in passing; none cites a captured source.

**The KB already recorded the gap and did not act on it.**
[`links-README.md`](../../notes/links-README.md) carries a "Prior work" section
naming hypertext theory, RDF, and ISO 25964 thesauri, followed by a standing
note: "**TODO:** This survey is from the agent's training data, not systematic."
That is an author flagging exactly this problem and leaving it open.

So the local theory in this area was written from recalled background rather
than from read sources. That is a fact about provenance. It is *not* by itself a
finding that any particular claim is a rediscovery — establishing that is work,
and it is the sibling workshop's work.

## What is already settled

**The transfer argument is not optional and does not come from the source.** A
result about human information seeking does not establish an LLM-agent design
conclusion. Whatever the final architecture is, it must keep a stated argument
about which mechanism carries over, what changes in the consumer model, and
which conclusion follows. Deleting local exposition in favour of a source route
must not silently delete that argument.

**Commonplace already has an adoption policy, and this workshop does not own
it.** [`source-adoption-policy.md`](../../reference/source-adoption-policy.md)
sets the programming fast pass, the first-principles gate for everything else,
and direct observation as a separate path. Cite it; do not restate or fork it.
An amendment to it is an ADR, not a workshop conclusion.
[philosophy-borrowing](../philosophy-borrowing/README.md) explicitly "retains
the general adoption test rather than growing a second link theory" — so a
second general adoption test is the thing not to build here.

**The ingest retains source evidence, while the target owns interpretation.**
Every ingest has one append-only `## Quotes` section containing exact source
wording and human-resolvable locations. Scope judgments, confidence,
limitations, normalized claims, and target-specific transfer arguments do not
belong there. This keeps the semantic check direct and prevents an ingest
paraphrase from acquiring source authority merely because it is tracked.

**The target-side comparison is a separate operation.** The first worked case
showed that source ingestion and connection discovery can detect overlap but do
not determine whether a local claim survives contact with the source. The writer
or reviewer must compare the target's exact source-dependent passage with the
retained quotes or pinned snapshot. This is where contradiction, scope, and
transfer are judged.

**The subsumption signal can reach the drafting worker.** The worker in
[`draft-ingest-report.md`](../../instructions/draft-ingest-report.md) runs in an
isolated context, but `cp-skill-connect` runs in the parent and can find local
overlap. That signal is useful for routing. It is not a subsumption verdict and
does not replace the target-side grounding check.

**No separate claim adapter is justified in V1.** The first direct-route rollout
covered 59 source uses after a larger normalized-Claims prototype. It found no
semantic reconciliation or reuse pressure that earned stable claim or quote
identity. Whole-ingest links plus target-local transfer reasoning were enough.
This is a provisional architecture decision, not a claim that a larger, denser
corpus can never justify identifiers.

**One local note already has the target shape.**
[an enforced tag-README is a MOC with a machine-checked contract](../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md)
names its inherited tradition openly and identifies the machine-checked
completeness contract as the added part. Read it before designing anything new;
it may show that the shape needs no new machinery at all.

## What a later session should not assume

**That the absence of claim identifiers is permanent.** V1 deliberately has no
normalized claim node or quote ID. Reopen that decision only if later cases show
concrete identity, reconciliation, or reuse failures that whole-ingest links
cannot carry.

**That direct grounding discovers prior art.** ADR 073 guards a source
dependency once an author names it. It does not detect an uncited claim that an
external literature already establishes. Model recall may propose a reading
assignment, but it has no verdict authority until a source is captured and read.

**That the corpus is a navigation corpus.** The critique proposed a
foraging/LIS reading list, and the first ingest fit it. But the sibling
workshop's [claim inventory](../literature-disposition/claim-inventory.md)
placed eleven cohort notes' claims across cognitive psychology of memory and
transfer, human-factors automation bias, materialized-view maintenance,
single-source publishing, and storage read amplification — with foraging
covering a minority. **Decide the corpus from the claims, not from the cluster's
name.** A corpus chosen for the wrong tradition does not merely miss the source;
it makes a claim look local because the wrong shelf was searched.

**That the proposed corpus is the corpus.** The critique's list — Bates,
Pirolli and Card, Marchionini, Teevan, Ranganathan, Broughton, Hearst/Yee,
Scatter/Gather, adaptive hypermedia — is a candidate, generated without reading
Commonplace's actual claims. Which sources are *authoritative for the claims
this KB actually makes* is a finding, and a source that turns out not to bear on
any local claim should not be ingested to complete a reading list.

**That every borrowed claim needs the same amount of retained source text.** A
bounded claim may fit the Quotes route. A distributed argument may require the
declared snapshot route. Either way, the target still owns the transfer from the
source's population and mechanism to Commonplace's LLM-agent setting.

**That the notes collection contract permits a pure pointer.**
`kb/notes/COLLECTION.md` carries a theory-independence constraint — the claim
must stand if any single cited description is removed. A node whose whole
content is "this is information scent, see Pirolli and Card" may not satisfy it.
Check the contract before proposing the shape, and if the shape is right and the
contract forbids it, that is a contract question to hand off, not a shape to
abandon quietly.

## Landed V1 and the maintenance successor

The destination is an operation the KB can re-run — a sweep that asks of the
corpus, not of one note, "which claims here rest on established results the KB
has never read?" Recording that constrains what a good answer looks like: an
extraction contract only a careful human reader can apply is not on the path,
and a finding phrased as "these twelve notes" is worth less than one phrased as
a rule a sweep could apply.

[ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
and the promoted grounding instructions make the rule operative. Their final V1
shape supersedes the earlier claim-ledger prototype: retain exact source
passages, declare when the full pinned snapshot is required, and judge the
target directly. The rollout retained 374 exact extracts and found only 4 of 65
sampled note-to-ingest pairs reusing the same normalized claim string. That
evidence supported removing interpreted claim entries rather than assigning
them stable identity.

The Pirolli case confirmed the target/source division. Pirolli grounds the human
proximal-cue/distal-source structure. The target note separately argues what
carries to bounded-context LLM agents, prices cue inspection in tokens and tool
calls, and removes the unsupported monotone claim that more pointer context is
always cheaper. The sibling workshop kept the repaired note on 2026-08-26.

Two reasons to expect the destination is smaller than a new command, both worth
checking before proposing one:

- **The deterministic half is probably a validator check or a report.** Does a
  note cite any source? Does the citation resolve to an ingest in `kb/sources/`
  rather than a bare URL or an unattributed surname? Does a tag-README's prior-
  work section route to captured sources? All mechanically decidable.
  `commonplace-verify-quotes` is the existing precedent for a deterministic
  source-fidelity check.
- **The judgment half is already the review system's shape.** "Is this claim
  established outside Commonplace?" is an open-ended, report-kind assay
  criterion over `(note, criterion, model partition)` — what
  `commonplace-review-target-selector`, `commonplace-create-review-jobs`, and
  the freshness baselines already execute. If that holds, the deliverable is a
  criterion under `kb/instructions/review-gates/`, not a command.

The judgment half carries the same defect this workshop exists to fix, and the
design has to absorb it rather than route around it: a model asked "is this
already established?" answers from training data, which is precisely how
`links-README.md`'s unsystematic prior-work survey came to be written. The
resolution is to give that answer no verdict authority —
[candidacy evidence licenses escalation to assessment, not acceptance](../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md).
A recall that a claim "sounds like Pirolli" is cheap author-external evidence
that routes to the expensive step, capturing and reading the source, and settles
nothing on its own. A sweep that emitted verdicts instead of reading assignments
would industrialize the original error at corpus scale.

## Wider corpus selected — 2026-08-26

The source-blind [claim inventory](../literature-disposition/claim-inventory.md)
was worked in source-coherent batches and recorded in
[corpus-selection.md](./corpus-selection.md). The accepted set is Pirolli;
Tulving and Pearlstone; Gick and Holyoak; Teevan et al.; Tombros and Sanderson;
the Niklas Luhmann Archive; and Nick Milo. Each accepted source now has a
tracked ingest with exact retained quotes. The record also explains why the
other proposed information-seeking, human-factors, database, publishing, and
retrieval traditions are deferred for the current live claims.

The transfer boundaries are load-bearing. Teevan and Tombros report human
information-seeking judgments, not LLM-agent behavior. Milo defines an LYT
artifact but does not establish its claimed cognitive effects or a completeness
history. The Luhmann Archive page describes Luhmann's own keyword registers as
non-exhaustive entry-point indexes; it does not identify them as MOCs or license
a claim about every Zettelkasten practitioner. The current MOC note's combined
tradition claim and universal negative therefore remain downstream repair work,
not conclusions supplied by these sources.

## Boundaries

In scope:

- deciding which external sources are authoritative for claims this KB makes,
  and ingesting them
- what an ingest must extract for subsumption and transfer to be determinable,
  including where in the pipeline each extraction can actually be produced
- the shape of the chain from source to operative consequence, and whether it
  needs an artifact kind or link labels it does not have
- proposing amendments to the ingest type, schema, or skill — as proposals, with
  the reasoning that earns them

Out of scope:

- dispositioning existing notes — [literature-disposition](../literature-disposition/README.md)
- a second general adoption test — [`source-adoption-policy.md`](../../reference/source-adoption-policy.md)
  owns it, [philosophy-borrowing](../philosophy-borrowing/README.md) applies it
- what an authored link *means*. [linking-foundations](../linking-foundations/README.md)
  owns "the deeper link-specific synthesis, including cognitive-science and
  discourse-theory evidence." Ingested sources that bear on link semantics are
  fine to produce here; the conclusions drawn from them go there
- migrating a live link label — [linking-contract-consistency](../linking-contract-consistency/README.md)

## What closes this workshop

The closure condition was satisfied on 2026-08-26: the corpus is decided for
the dated cohort, every source judged authoritative is ingested with retained
quotes, and every considered source not used has a rejection or deferral
reason. The V1 extraction contract and intermediate-node questions were already
decided in the status table above.

The maintenance sweep is a **successor**, not a closure condition. Recording
which half is deterministic and which is an assay criterion is in scope;
building either is not.

## Bookkeeping

Date every finding. A disposition of the source corpus is a judgment about what
the KB claims at a time, and the claims move.

Record rejected sources, not just ingested ones — otherwise a later session
re-proposes them.

## Files

- [Next-session plan](./next-session-plan.md) — restart-ready work queue for
  target grounding, disposition recording, and consuming this workshop
- [Wider source-corpus selection](./corpus-selection.md) — dated accepted,
  rejected, and deferred sources, with source/target transfer boundaries and
  downstream handoffs

- [Worked case: `agents-navigate-by-deciding-what-to-read-next`](./worked-case-agents-navigate.md)
  — the first claim taken through the whole chain by hand, 2026-08-24. Falsified
  this README's "no slot for any of the four" and found the gap the pipeline
  cannot close by ingestion alone: it detects overlap but target-side comparison
  is needed for contradiction
- [Three channels](../literature-disposition/three-channels.md) — channel 3 is
  the dated implementation and backlog ledger: direct grounding is landed;
  prior-art discovery, identifiable provenance, and one quote-walker bug remain
- [Candidate procedure: pull the claim through the ingest before using it](./candidate-procedure-claim-pull.md)
  — historical operator proposal, 2026-08-24. Its demand-driven retention
  direction survived, but ADR 073 replaced normalized claim entries with exact
  quotes or an explicit snapshot requirement

## Input

- [External critique of the navigation cluster](../literature-disposition/chatgpt-critique.md)
  — draws-on: the pasted ChatGPT critique that opened this work; its source-corpus
  proposal and its source→adapter→delta→operative chain are this workshop's
  starting candidates, held in the disposition workshop because most of its
  content is disposition-side
