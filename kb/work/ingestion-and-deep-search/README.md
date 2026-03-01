# Workshop: Directed Reading

## Question

What happens when you decouple "get a document" from "analyse it with purpose"?

## Context

The current `/ingest` skill couples snapshot + analysis into one operation with a fixed template. But the interesting part isn't the downloading — it's reading a document through the lens of a specific goal. That goal might be:

- A research question (inline text)
- A note you're developing (a file path)
- A design problem you're exploring (another note)

This reframes source analysis as a general primitive: **directed reading**. Any document + any goal → a purpose-shaped report.

Key properties:
- The document can be anything markdown — source snapshot, existing note, spec
- The goal can be inline text or a note/file, making note-to-note analysis natural
- The same document can be read multiple times with different goals
- Downloading/snapshotting is a separate step (`/snapshot-web`), not coupled to analysis

## What this enables

- **Source ingestion** — `/snapshot-web` then directed-read against your research question
- **Note synthesis** — read one note through the lens of another
- **Literature review** — read multiple documents against the same goal note
- **Deep search** — a loop: goal note → find sources → directed-read each → refine goal

## What we want to discover

- Does the procedure in `directed-reading.md` hold up in practice?
- What does note-to-note directed reading actually produce? Is it useful?
- Does deep search (multiple documents, one goal) feel natural as repeated invocations?
- Where should reports live — next to the document, next to the goal, or somewhere else?

## Experiments

### Experiment 1: A-MEM learning operations (2026-03-01)

**Document:** `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md`
**Goal:** Inline — "how does their system learn, what are the operations, are they all automatic?"
**Report:** `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.report-learning-operations.md`

**What happened:**
- Procedure worked end-to-end: copy → connect → read with purpose → save → cleanup
- `/connect` found connections on the working copy without touching the original (cleanup step was missing from procedure, now added)
- The goal shaped the report structure naturally — came out as an operation inventory + gap analysis, not the generic summary that `/ingest` would have produced
- Inline goal worked fine for a focused question like this

**Observations:**
- The report extracted something the original ingest didn't: the accretion-vs-curation distinction (A-MEM only does accretion operations, never simplification). The goal forced looking at the source from a different angle.
- Reading the full source snapshot was necessary — the ingest summary didn't have enough detail about individual operations and prompt templates.
- Report location next to the document feels right for source analysis. Not yet tested: reports next to a goal note.

**Open questions surfaced:**
- When the goal is a note rather than inline text, should the report also link back into that note?
- The procedure reads both the document and the goal — when both are long, that's a lot of context. Does this degrade quality?
