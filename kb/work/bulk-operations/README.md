# Workshop: Bulk Operations

## Question

How should Commonplace plan, shard, execute, validate, merge, and close operations that touch many artifacts without mixing selection, per-target work, review, and promotion authority into one overloaded task?

## Why this replaces ingestion-and-deep-search

The older `ingestion-and-deep-search` workshop asked how agents should run deep search over a KB without mixing discovery, source processing, synthesis, and promotion. That was a real case, but it is now one instance of a broader problem. The same shape appears in review reruns, connect-report triage, source re-ingest, whole-corpus type migrations, validation sweeps, matrix refreshes, relocation moves, and future lineage-driven refresh.

This workshop keeps the deep-search lesson, but generalizes the frame from "research over sources" to **bulk operations over corpora** — both maintenance over existing KB artifacts and generation of new derived structures from an external corpus.

## Current Claim

A safe bulk operation is a staged context-engineering pipeline, not one long agent task.

The recurring stages are:

1. **Select** - identify targets and record why each target is in scope. For maintenance operations this finds existing artifacts; for generative operations this enumerates documents that ought to exist, by instantiating a structure spec against the corpus. When per-target execution is expensive, selection is a **funnel** — tiered cheap recall stages (lexical, vector, metadata) feeding the expensive precision stage — with the drop decisions recorded so the recall trade-off is auditable.
2. **Classify** - decide the operation class per target: read-only review, source processing, rewrite, move, merge-back, validation, generation, or promotion candidate.
3. **Shard** - split work into bounded packets with explicit input paths, output paths, authority, and collision boundaries. Frontload shared context once (e.g. a comparison brief distilled from a query document) rather than re-deriving it per packet.
4. **Execute** - run each packet in a clean context or deterministic command, writing only its owned artifact(s).
5. **Integrate** - inspect outputs, apply valid changes, regenerate derived views, and leave uncertain findings as follow-up state. When packets produce judgments or scores from independent contexts, integration includes calibration — a rubric or a comparative re-ranking pass — not just concatenation.
6. **Validate** - run structural checks, semantic gates, or command-specific verification appropriate to the authority of the outputs. For generated document sets this includes set-level checks: membership completeness, cross-member links, index coverage.
7. **Close** - either promote durable conclusions, update the operating instruction/command, or delete the workshop state.

This separates judgment-heavy target selection from focused execution and keeps promotion authority out of intermediate reports.

## Prerequisite: structures bigger than a document

Generative bulk operations cannot be sharded, validated, or refreshed without a spec of the structure they produce — a **document-set spec**: membership rule (fixed + corpus-derived members), member types, cross-member obligations, derived views, set-level validation, and lineage to the corpus. A code wiki is the clearest case: "write a wiki" is unboundable until the spec exists; once it does, the membership rule is the target list, the member type is the packet contract, and set-level validation is deterministic.

This may be a separate direction in its own right (a type-system question, with `kb/agent-memory-systems/` as the existing implicit precedent: `systems.csv` registry + review member type + generated matrix), but the dependency runs one way — this workshop consumes the spec as an input contract. Analysis: [Generative bulk operations and document-set specs](./generative-bulk-operations.md).

## Case Families

Use these existing workflows as witnesses:

- **Deep research / directed reading** - source discovery, snapshot/ingest, instruction packet, clean-context synthesis, and promotion decision.
- **Agent-memory review reruns** - select rows from `systems.csv`, dispatch one source-grounded worker per review, edit only the review, then regenerate the matrix.
- **Review batches** - selector JSON, queued jobs, one output file per job, finalization, and freshness verification.
- **Connect maintenance triage** - scan generated reports, extract maintenance observations, classify each as done/open/moved/watch, and promote only the durable residue.
- **Source re-ingest / bulk import** - preserve source boundaries, update ingests, detect downstream references, and avoid promoting raw source claims directly.
- **Whole-corpus migrations** - type migration, path rewrites, directory relocation, link rewriting, generated-index refresh, and rollback boundaries.
- **Validation sweeps** - deterministic structural checks, semantic gates, and corpus-level consistency checks with different oracle strengths.
- **Lineage-driven refresh** - a future freshness layer emits refresh targets, but execution remains owned by review, connect, source-processing, or agent workflows.

And two aspirational generative cases that stress the frame (detailed in [generative-bulk-operations.md](./generative-bulk-operations.md)):

- **Code wiki** - generate a structured document set (overview, per-module pages, index, cross-links) from a codebase; bulk in the write direction, with corpus-derived membership, cross-member link obligations, and set-level lineage for refresh.
- **Deep-similarity corpus search** - compare a query document (law case, patent claim) against a large corpus with judgment deeper than embedding adjacency; bulk in the read direction, requiring a tiered selection funnel, a frontloaded comparison brief, calibrated merge, and per-candidate justifications as the durable product.

## Design Questions

- What minimal run record should every bulk operation keep: target list, source revision, output paths, model/tool provenance, decisions, skipped targets, and residual warnings?
- When should the target list be a committed artifact, a gitignored report, a SQLite state row, or just command output?
- What should be deterministic selection versus agent judgment?
- Which operations can safely run in parallel, and what write scopes make conflicts impossible?
- How should a parent agent merge worker outputs without silently laundering uncertain findings into library artifacts?
- What validation is proportional to each output's behavioral authority?
- When should a recurring bulk operation become a command, a skill, an instruction, or a review-system feature?
- What is the minimal document-set spec, and where does it live: a new type kind, an extension of `COLLECTION.md`, or a standalone manifest generalizing `systems.csv`?
- In a selection funnel, which tiers are deterministic commands versus cheap agent passes, and how are drop decisions recorded?
- How are judgments from independent worker contexts made comparable at merge time (rubric in packet, comparative re-ranking pass, or both)?
- Where does the member-to-sources lineage mapping live so a corpus diff can be turned into a refresh target list mechanically?

## Retained Inputs From Deep Search

- [Directed-reading contract inventory](./directed-reading-inventory.md) - map of stable and ad hoc reading contracts that already exist in the KB.
- [Instructions: A-MEM automation-quality trade-off](./instructions-amem-automation-quality.md) - concrete example of a frontloaded instruction packet used in an experiment.

These files are historical inputs to the broader bulk-operations pattern. They should be revised or promoted only if the new frame needs a durable directed-reading subpattern.

## What Would Close This Workshop

Close when this workshop produces one of:

- a reusable bulk-operation runbook under `kb/instructions/`;
- a skill or command contract for recurring bulk operations;
- a reference design for target selection, sharding, output ownership, provenance, merge-back, and validation;
- or a decision that existing domain-specific workflows are sufficient, with the boundary conditions named.

If the document-set-spec prerequisite grows into its own direction, spinning it off into a separate workshop (or a design proposal in `kb/reference/proposals/`) also counts as partial progress — this workshop then narrows to pipeline mechanics and consumes the spec as an input contract.

Before closing, remove stale active-workshop entries for superseded or missing workshops and decide whether the directed-reading files above should be promoted, retained as examples, or deleted.
