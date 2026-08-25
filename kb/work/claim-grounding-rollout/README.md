# Claim-grounding rollout

## What this is

Retrospective application of
[ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
across source-dependent claims that predate its direct-source rule.

ADR 073 was revised on 2026-08-25 after this rollout had already completed most
cohorts under an earlier design. That design retained normalized source claims
in ingests and checked notes through a source-specific review lens. The accepted
design removes that semantic relay:

- every ingest has exactly one `## Quotes` section containing only verbatim
  source extracts and their locations;
- an ordinary ingest link declares that those quotes are sufficient for the
  linked source use;
- a link whose visible text contains `(snapshot required)` declares that the
  exact name-paired, checksum-matching snapshot is required;
- the ordinary `semantic/grounding-alignment` gate compares the note directly
  with the selected source material.

The all-ingest structural migration shipped in `5e48d2d9`. It gave every
tracked ingest the same Quotes shape, including ingests no note currently cites.
Uniform structure does not mean bulk-populating every ingest with quotations.
Quotes are retained when a concrete source-dependent use can be checked soundly
from a bounded passage; broader uses explicitly require the snapshot.

Prospective writers now apply the same route and standard gate before a new or
materially changed source-dependent claim lands. This workshop owns the
retrospective corpus repair.

It was split out of
[literature-disposition](../literature-disposition/README.md) on 2026-08-24,
where it had been placed by momentum. The populations barely touch: of the 29
notes in the first rollout cohorts, only one was in that workshop's diagnosed
cohort. This rollout is selected by the citation graph, not by prior-art
suspicion.

## Current authority

Use these current contracts for unfinished work:

- [ADR 073](../../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md)
  — route semantics and architectural decision
- [Ground a source-dependent claim](../../instructions/ground-source-dependent-claims.md)
  — choose Quotes or snapshot-required support
- [Ingest skill](../../instructions/cp-skill-ingest/SKILL.md) — the only
  supported mechanical quote-append path
- [Grounding alignment gate](../../instructions/review-gates/semantic/grounding-alignment.md)
  — the sole persisted semantic check
- [Review system](../../reference/README-REVIEW-SYSTEM.md) — selection, jobs,
  finalization, and freshness

The original [cleanup procedure](./procedure.md) preserves the freeze method,
source-blind inventory rationale, and historical cohort protocol. Its
Claims-ledger, normalized-wording, and source-as-gate operations are superseded.
Do not use those portions for new work. An active cohort's revised prompt, ADR
073, and the current grounding instruction take precedence.

Earlier cohort records remain useful evidence about frozen target wording,
source-side needs, repairs, and dispositions. Their old paraphrased ingest
claims are not source evidence. Their retained exact extracts were migrated to
Quotes, while their source-lens review results are obsolete and do not satisfy
the current direct semantic check.

## Governing question

For each claim a note draws from a source it cites: does the source directly
support it at the stated scope through the route declared by that linked use?

The two sound inputs are:

- the ingest's bounded verbatim Quotes; or
- the exact pinned snapshot when the link says `(snapshot required)`.

Summary, Connections Found, Extractable Value, Limitations, and other analytical
ingest prose may help discovery but never count as support. An ordinary link
whose quotes are insufficient fails even when a snapshot happens to be present;
the checker never chooses an undeclared fallback.

What should then happen to the whole note — retire, thin, rewrite around its
local contribution, or leave — is
[literature-disposition](../literature-disposition/README.md)'s question. This
workshop feeds it rather than answering it. A `literature handoff` disposition
is the seam.

## Corpus and migration state

At the 2026-08-24 rollout freeze:

- 68 notes cited an ingest;
- 94 distinct ingests were cited;
- 192 of 286 ingests were cited by no note.

Those 68 notes are the retrospective target population. The 192 uncited ingests
were not source-demand targets, but they were included in the later structural
migration. By `5e48d2d9`, all 292 ingests then tracked had exactly one Quotes
section. The migration converted 119 old normalized entries into 374 retained
verbatim quote items across 79 ingests; the other 213 ingests received the
canonical empty section.

The freeze graph first assigned two notes to cohort 01 and another 29 to
cohorts 02–07. Removing those targets left four connected components: 18 notes
/ 36 ingests, 15 / 20, 2 / 1, and 2 / 1. Cohort 08 combined the two smallest
components; cohorts 09 and 10 owned the 15- and 18-note components.

The structural migration is complete. The retrospective evidential migration
is not:

- cohort 01 has a reconstructed completion record;
- cohorts 02–10a have populated terminal completion records;
- cohort 10b is the remaining unfinished cohort;
- targets completed under the retired source lens still need a fresh standard
  `semantic/grounding-alignment` judgment against Quotes or a declared
  snapshot. The grounding-gate revision stales ordinary prior baselines by
  criterion change; deleted source-lens pairs must not be recreated or
  acknowledged as a substitute.

## Current execution path

The unit remains one source-dependent target use, not one ingest.

1. Preserve or record the target claim and its source-side need before source
   reading. Existing source-blind inventories remain valid historical inputs.
2. Read the complete Quotes section and judge the source-side need directly
   against the exact extracts.
3. If the quotes are insufficient, verify the exact name-paired snapshot. Add
   the minimum bounded quotes through the ingest skill, or select
   `snapshot required` when sound checking depends on broad or distributed
   context.
4. Repair the target against the selected source material. Keep
   target-specific synthesis in the target and make the link route explicit.
5. Run a fresh standard `semantic/grounding-alignment` review for the whole
   note under a real model partition. Resolve in-scope WARN or FAIL findings;
   missing or mismatched required snapshots fail closed.
6. Record the source route, target disposition, deterministic validation, and
   semantic-review result.

Never restore normalized Claim, Scope, Confidence, or Limitation fields to an
ingest. Never treat old ingest analysis as evidence. Never append Quotes by
hand. A need whose actual source falls outside the owned manifest remains a
named literature handoff rather than silently expanding the cohort.

## Concurrency

Artifact ownership still has two conflict axes: target notes and ingests. The
ingest skill preserves incumbent quote items, but it does not provide concurrent
file locking. Two agents must not append to the same ingest or edit the same
target at the same time.

The connected-component cohorts are therefore still useful mutation boundaries.
The top-level cohorts 02–10 are mutually disjoint on both axes. Cohorts 09 and
10 were each split only to bound one agent's context; each split leaves two
bridge ingests shared by its halves. A pair's halves must not overlap while
either agent may mutate a bridge ingest. Once the first half is committed and
no longer owns those paths, the second may preserve and reuse its incumbent
Quotes.

For active work, inspect the shared worktree before every mutation phase and
before committing. Stop on an owned-path overlap, preserve unrelated changes,
and stage only explicit owned files.

Standard review is note-level. There is no source-specific pair to schedule, no
raw-ingest criterion, and no source-lens freshness state.

## Snapshot-pair repair — 2026-08-24

All seven cited ingests that lacked an exact name-paired snapshot at the corpus
freeze now have one in the local snapshot cache. Cohort 02 repaired the first
two pairs. The remaining five expected byte streams were already present under
adapter-derived names; each matched its ingest's recorded SHA-256 and canonical
source. They were moved to the ingest-derived Markdown path without changing
their bytes, and the two X capture companions were moved with them.

This removed the snapshot-identity blocker that existed at the freeze. It did
not itself ground any target use. Snapshot availability must still be checked
when a current route requires it, because snapshots remain ignored local
material rather than durable tracked evidence.

## What closes this workshop

1. Cohort 10b has a terminal completion record under the Quotes/snapshot model,
   including recovery of its set-aside verbatim extracts.
2. Every frozen source-dependent use has a terminal target disposition or a
   named blocker/handoff. Historical records may retain their original
   vocabulary, but no live execution step treats a normalized ingest claim as
   evidence.
3. Every one of the 68 target notes has a fresh standard
   `semantic/grounding-alignment` result under the chosen operational model
   partition after the gate revision. Every ordinary support link is adequately
   quote-backed; every broader use carries the exact snapshot marker and passes
   while the verified snapshot is present.
4. Every changed ingest and target validates. Missing, mismatched, secondary,
   or unsupported source material is repaired or recorded explicitly rather
   than downgraded to a warning.
5. No closure step depends on the retired source lens, per-ingest review pairs,
   whole-Claims-section selection, claim IDs, or paraphrased ingest authority.

Once these conditions hold, durable findings that matter outside the migration
belong in notes or ADRs, and this workshop can close rather than becoming a
permanent second review system.

## Files

- [Historical procedure](./procedure.md) — source-blind freeze rationale and
  the superseded Claims-era execution record; not the authority for current
  grounding mechanics
- [Cohort 01](./cohort-01.md) — reconstructed first run: six narrowed, two
  contradicted, zero grounded as written
- Cohorts [02](./cohort-02.md) · [03](./cohort-03.md) · [04](./cohort-04.md) ·
  [05](./cohort-05.md) · [06](./cohort-06.md) · [07](./cohort-07.md) — frozen
  manifests with terminal completion records and historical prompts
- [Cohort 08](./cohort-08.md) ([prompt](./cohort-08-prompt.md)) — complete;
  four notes across the two smallest residual components
- Cohort 09 — complete sequential pair:
  [09a](./cohort-09a.md) ([prompt](./cohort-09a-prompt.md)) and
  [09b](./cohort-09b.md) ([prompt](./cohort-09b-prompt.md))
- Cohort 10 — [10a](./cohort-10a.md)
  ([historical prompt](./cohort-10a-prompt.md)) is complete;
  [10b](./cohort-10b.md) has a
  [current quote-grounding prompt](./cohort-10b-prompt.md) and is in progress
- [Cohort 02 prediction](./cohort-02-prediction.md) — sealed; open when judging
  that historical run, never while executing it

## What a later session should not assume

**That a clean grounding is the expected outcome.** Cohort 01 returned zero
grounded-as-written across eight source-dependent uses. Every case examined
during the initial design work returned a defect rather than a confirmation. An
executor expecting to confirm citations will confirm them.

**That uniform ingests require quotes everywhere.** Uniformity is the enforced
Quotes section and immutable source identity. Quote contents remain
demand-driven. An uncited ingest with the canonical empty sentence is complete,
not waiting for speculative evidence extraction.

**That an old source-lens PASS is current assurance.** It judged a note through
an ingest paraphrase and belongs only to the historical work record. Current
assurance is a standard grounding-gate result that reads exact Quotes or a
declared verified snapshot.

**That the cohorts are a literature sweep.** They check claims against sources
the notes already cite. They do not search for prior art a note failed to cite.
That is a separate literature-discovery problem, and negative search results
must retain the scope of what was actually searched.
