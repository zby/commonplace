# Next-session plan: finish the source-grounding handoff

Date: 2026-08-26

Suggested opening instruction for a fresh agent:

> Continue from `kb/work/source-grounding/next-session-plan.md`. Execute the
> downstream handoff in order, preserve the source-transfer boundaries, record
> dispositions in the sibling workshop, and close the source-grounding
> workshop when its findings have been consumed.

## Current state

The upstream source-grounding work is complete for the dated cohort. The V1
grounding mechanism is settled, the wider corpus is selected, all seven
accepted source cases have tracked ingests with exact retained quotes, and the
unselected candidates have recorded deferral reasons. Do not restart literature
selection or re-ingest these sources unless target-side comparison exposes a
specific support gap.

The workshop is marked ready to close because the remaining work belongs to
the downstream [literature-disposition](../literature-disposition/README.md)
workflow: edit or assay target notes, record their dispositions, then consume
and remove this workshop.

## Read first

1. [Workshop README](./README.md) — settled architecture, boundaries, and
   closure status.
2. [Wider source-corpus selection](./corpus-selection.md) — accepted and
   deferred sources, exact local claims, and transfer boundaries.
3. [Literature-disposition README](../literature-disposition/README.md) and its
   [claim inventory](../literature-disposition/claim-inventory.md) — owner of
   target-note outcomes.
4. `kb/notes/COLLECTION.md` before editing a note. Before review work, read
   `kb/reference/README-REVIEW-SYSTEM.md` and use the standard
   `semantic/grounding-alignment` assay path.

Use the applicable writing skill for each target. The MOC rewrite requires
multi-source claim separation and is a likely `cp-skill-write-multistage` case.
The source Quotes blocks are already grounded; do not edit them as part of a
target rewrite.

## Work queue

### 1. Finish the activation disposition

Target:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md)

Sources:

- [Tulving and Pearlstone](../../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md)
- [Gick and Holyoak](../../sources/gick-holyoak-analogical-problem-solving.ingest.md)

The target already states the required boundary: these human experiments are
historical antecedents, not direct evidence for LLM activation. Run the pending
target-side grounding assay. If it passes, record the disposition without
rewriting the note. If it warns or fails, repair only the finding the assay
identifies, validate, and rerun the affected pair.

### 2. Ground the navigation targets

Use [Teevan et al.](../../sources/teevan-perfect-search-engine-orienteering.ingest.md)
for the bounded human observation that known-item seeking often used contextual
local steps rather than direct keyword jumps. Add it to
[link-following and search impose different metadata requirements](../../notes/link-following-and-search-impose-different-metadata-requirements.md).
The target must own the transfer from human file, email, and Web behavior to
LLM-agent KB navigation and its metadata prescription.

Use [Tombros and Sanderson](../../sources/tombros-sanderson-query-biased-summaries.ingest.md)
for the human relevance-judgment comparison between query-biased summaries and
static title-plus-leading-text surrogates. Add it to
[pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md).
Preserve the same-length rerun's limit on any speed claim. Do not present the
study as evidence for LLM context cost or for the target's entire pointer
taxonomy.

Both ingests have sufficient retained quotes for normal ingest links; neither
needs `(snapshot required)` for these bounded uses. Validate each edited note
and run its grounding assay.

### 3. Repair the MOC inheritance note

Target:

- [An enforced tag-README is a MOC with a machine-checked contract](../../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md)

Keep the two source traditions separate:

- [Nick Milo](../../sources/nick-milo-mocs-definition.ingest.md) supports a
  first-party definition of an MOC as contextual mapping that helps gather,
  develop, and navigate ideas, with a grouped-link note as one example. It does
  not establish that every MOC is annotated or selective by design, that a
  tag-README is exactly equivalent, that nobody promises completeness, or that
  MOCs deliver the page's claimed cognitive effects.
- The [Niklas Luhmann Archive](../../sources/luhmann-archive-schlagwortregister.ingest.md)
  supports only that Luhmann's own keyword registers disclaimed complete term
  locations and named relevant entry points. It does not identify those
  registers as MOCs, establish hub-card behavior, or generalize to other
  Zettelkasten practitioners.

Replace the combined tradition claim with source-bounded statements. Remove or
separately support the universal negative that no Zettelkasten or LYT
practitioner made a completeness promise. Treat the claims about human readers
recovering gracefully and human maintainers being unable to check completeness
as local reasoning or hypotheses unless independent evidence is supplied; do
not attribute them to Milo or the Archive.

Both ingests support normal links for the quoted claims. Validate the rewritten
note and run its grounding assay.

### 4. Record dispositions and close

Record the activation, navigation, and MOC target outcomes in the sibling
literature-disposition workshop. If a target-side assay reveals a concrete
source gap, reopen only that source decision in
[corpus-selection.md](./corpus-selection.md). Do not reopen the famous reading
list as residual work.

Once the target outcomes are recorded and no source gap remains, move any
lasting finding that still exists only under this workshop to its proper
library or sibling-workshop destination, then delete
`kb/work/source-grounding/` as a consumed workshop. Preserve history with
scoped, non-destructive Git operations and follow the repository's commit
rules.

## Evidence inventory

The four new source snapshots and their connection reports are intentionally
ignored; their tracked ingests are the durable routes. The snapshot checksums
are:

| Ingest | Snapshot SHA-256 |
|---|---|
| [Teevan et al.](../../sources/teevan-perfect-search-engine-orienteering.ingest.md) | `a8b4b8839b5c0401ced39586bc4d03f99ed747253e0418972eedc635c5450b26` |
| [Tombros and Sanderson](../../sources/tombros-sanderson-query-biased-summaries.ingest.md) | `19c22c213a4c44e8bb75f12811624b08425398fa9de577e05ef341818cd16e65` |
| [Niklas Luhmann Archive](../../sources/luhmann-archive-schlagwortregister.ingest.md) | `c46e2c0074e392eaf6dca508b3aab267b9392158fd978a685eb794de51bf87ba` |
| [Nick Milo](../../sources/nick-milo-mocs-definition.ingest.md) | `836f40a0a4b455408795524d08fee9fbb2d00eb2c8ef05a5f2c23181733bb6f8` |

The Luhmann snapshot is a `manual-paste` capture of the rendered
`Schlagwortregister` page because automated extraction returned only a
JavaScript placeholder. Scope any use to the exact retained German wording.

## Definition of done

- The activation target has a current grounding-alignment disposition.
- The Teevan and Tombros claims are integrated with explicit human-to-LLM
  boundaries and pass deterministic validation plus grounding review.
- The MOC note separates Milo from Luhmann, drops or independently supports the
  universal practitioner claim, and passes deterministic validation plus
  grounding review.
- The sibling workshop records all resulting note dispositions.
- No accepted-source support gap remains, durable findings have left the
  workshop layer, and `kb/work/source-grounding/` is removed.

At session start, inspect `git status` and preserve unrelated work. At this
handoff an unrelated untracked `kb/work/multistage-skill-coherence-audit/`
directory may still be present; it is not part of this plan.
