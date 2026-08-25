# Documentation disposition: what a reflective system retains, and where

Reopened 2026-08-25. The earlier workshop of this name closed on 2026-08-24
after deciding the *maintenance form* of reference documentation and yielding
[ADR 074](../../reference/adr/074-git-is-the-change-history-layer.md). This
reopening asks the placement question that ADR 074 answered only for change
history.

## Question

For a reflective, self-improving KB operated by LLM agents: which content must
be retained at all, and of what is retained, what goes into documentation
(instructions, contracts, reference), what goes into ADRs, what goes into
notes, and what is recorded only in commit messages?

## Inputs the analysis rests on

- Naur, *Programming as Theory Building* — the theory a developer holds is a
  mapping between world affairs and the program; documentation cannot carry it
  whole; it has three assessable capabilities (map, justify, modify). Ingest:
  [programming-as-theory-building](../../sources/programming-as-theory-building.ingest.md).
- The operator's observation that *intents* are a high-leverage component of
  such theories: a stated purpose lets an interpreter regenerate many
  justifications that would otherwise each need retaining.
- The KB's account of itself as a reflective system with theory-mediated
  learning: an LLM interpreter over retained text brings part of Naur's theory
  inside the technical boundary, so the retention question becomes which parts
  the interpreter cannot re-derive at read time.
  [Theory-mediated self-improvement needs both interpretation and retention](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

## What closes the workshop

1. A routing table from content kind to destination, each row justified by
   the derivation in `analysis.md` (theory component × re-derivability ×
   consuming operation), aligned with the placement rules already in
   `kb/reference/COLLECTION.md`, `kb/notes/COLLECTION.md`,
   `kb/instructions/COLLECTION.md`, `kb/reference/types/adr.md`, and
   `AGENTS.md` `## Git`, and reconciled with the table in
   `kb/reference/design-rationale-management.md`.
2. A list of specific changes to procedures, contracts, validators, or code
   that make the table operative, each with its consumer and channel named.
   Accepted changes ship as edits plus an ADR; rejected ones are recorded with
   the reason.
3. Durable residue extracted: the table into the reference collection it
   belongs to, any transferable claim into `kb/notes/`, and this directory
   deleted.

## Evaluation boundary

The table is judged by whether an agent performing a named change operation
can decide placement from it without taste, and by whether it contradicts an
existing contract. It is not judged by corpus measurement in this pass; the
change-operations catalogue (`kb/work/change-operations-catalogue/`) supplies
the operation inventory and is not re-derived here.

## Files

- `analysis.md` — the derivation, the draft routing table, and the candidate
  changes.
