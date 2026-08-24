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

## Why this is open now

Two measurements, both taken 2026-08-24:

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

**The current ingest contract has no slot for any of the four extractions the
question needs.** `.ingest.md` files are `kb/sources/types/ingest-report.md`,
schema-enforced to `## Classification`, `## Summary`, `## Connections Found`,
`## Extractable Value`, `## Limitations (our opinion)`, and
`## Recommended Next Action`. Measured against what a subsumption judgment
needs:

| Needed | Present today |
|---|---|
| Exact claims the source establishes | No slot. `## Summary` is a read/skip decision aid; `## Extractable Value` is defined *relative to the installed KB*, not as what the source itself establishes |
| Population studied, costs modelled, scope conditions | No slot. `## Limitations (our opinion)` is the nearest, but it is a negative editorial framing, not a positive record |
| What transfers to LLM agents and what does not | No slot anywhere in the ingest type |
| Which existing notes the source subsumes | Weak. `## Connections Found` records fit and is instructed to *drop* duplicate edges; retirement is reachable only as one advisory sentence in `## Recommended Next Action` |

**There is a hard constraint on adding the subsumption field.** The ingest
drafting worker in [`draft-ingest-report.md`](../../instructions/draft-ingest-report.md)
runs in a clean isolated context and is forbidden from browsing the web,
rerunning connect, or running broad KB searches — its only view of the KB is the
connect report plus the artifacts that report names. A field asking "which notes
does this subsume?" requires corpus-wide comparison, which that worker
contractually cannot do. So the field either moves to a different stage, or the
isolation contract changes, or subsumption is recorded from the note side
instead. Do not design a field that quietly assumes the worker can search.

**One local note already has the target shape.**
[an enforced tag-README is a MOC with a machine-checked contract](../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md)
names its inherited tradition openly and identifies the machine-checked
completeness contract as the added part. Read it before designing anything new;
it may show that the shape needs no new machinery at all.

## What a later session should not assume

**That a "claim adapter" is a new artifact kind.** The
[input critique](../literature-disposition/chatgpt-critique.md) proposes a thin
normalized-claim node between ingest and delta note. It may turn out to be an
ordinary note written to the existing `note` contract, a section in a tag
README, a field on the ingest, or unnecessary. All four are legitimate findings.

**That the proposed corpus is the corpus.** The critique's list — Bates,
Pirolli and Card, Marchionini, Teevan, Ranganathan, Broughton, Hearst/Yee,
Scatter/Gather, adaptive hypermedia — is a candidate, generated without reading
Commonplace's actual claims. Which sources are *authoritative for the claims
this KB actually makes* is a finding, and a source that turns out not to bear on
any local claim should not be ingested to complete a reading list.

**That every borrowed claim needs the same treatment.** The architecture may be
uniform (ingest → node → delta → operative) or may differ by how many local
notes depend on the borrowed claim, by whether several sources jointly establish
it, and by whether local terminology diverges from the literature's.

**That the notes collection contract permits a pure pointer.**
`kb/notes/COLLECTION.md` carries a theory-independence constraint — the claim
must stand if any single cited description is removed. A node whose whole
content is "this is information scent, see Pirolli and Card" may not satisfy it.
Check the contract before proposing the shape, and if the shape is right and the
contract forbids it, that is a contract question to hand off, not a shape to
abandon quietly.

## Horizon: eventually a maintenance sweep

The destination is an operation the KB can re-run — a sweep that asks of the
corpus, not of one note, "which claims here rest on established results the KB
has never read?" Recording that constrains what a good answer looks like: an
extraction contract only a careful human reader can apply is not on the path,
and a finding phrased as "these twelve notes" is worth less than one phrased as
a rule a sweep could apply.

It is not what this workshop builds, and the first move must not be the command.

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

## Where to start

Simpler than the sweep, and simpler than the schema question: take **one claim
through the whole chain by hand**. Pick a claim, find and capture the source
that would settle it, ingest it under the existing contract, then try to use
that ingest to judge the note — and record what the ingest fails to carry.

The ordering is the point. The extraction contract is this workshop's main
question, and it is far easier to answer from one instance of the contract
failing than from reasoning about what a contract ought to contain. The same
holds for the intermediate node: whether it is needed becomes visible once a
real ingest and a real note exist for it to sit between.

Do not begin by ingesting the corpus. Ingests made before anyone has tried to
use one for this purpose will be shaped by the current contract's questions,
and finding where those questions fall short is the reason to do the work.

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

1. A decided source corpus, with the sources judged authoritative actually
   ingested — and the ones considered and rejected recorded with the reason.
2. An answer on the ingest extraction contract: either promoted changes to
   `kb/sources/types/ingest-report.md`, its schema, and the drafting
   instruction, or the recorded finding that the existing sections suffice and
   why. If the answer requires relaxing the drafting worker's isolation, that is
   a proposal with its cost stated, not a silent edit.
3. An answer on the intermediate node: a promoted shape with at least one worked
   instance, or the recorded finding that no new shape is needed.

"No new machinery is needed" is a legitimate close for 2 and 3, but only after a
worked case, not from the armchair.

The maintenance sweep is a **successor**, not a closure condition. Recording
which half is deterministic and which is an assay criterion is in scope;
building either is not.

## Bookkeeping

Date every finding. A disposition of the source corpus is a judgment about what
the KB claims at a time, and the claims move.

Record rejected sources, not just ingested ones — otherwise a later session
re-proposes them.

## Input

- [External critique of the navigation cluster](../literature-disposition/chatgpt-critique.md)
  — draws-on: the pasted ChatGPT critique that opened this work; its source-corpus
  proposal and its source→adapter→delta→operative chain are this workshop's
  starting candidates, held in the disposition workshop because most of its
  content is disposition-side
