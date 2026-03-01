# Workshop: Instructions and Directed Reading

## Question

What happens when agent work is mediated by self-contained instruction notes?

## Context

Started from a narrower question: how to decouple source analysis from downloading. The `/ingest` skill couples snapshot + analysis with a fixed template, but different tasks need different things from the same source.

The first insight was **directed reading** — any document + any goal → a purpose-shaped report. But trying to generalize it (multiple documents, goal as a note) revealed a deeper pattern:

**Instructions notes** — self-contained work packets that a sub-agent can execute with clean context.

An instructions note contains:
- **Inputs** — links to the documents to work with
- **Goal** — what to do with them (inline or by reference to another note)
- **Output spec** — where to put results, what form they should take

The key property: a sub-agent can pick up an instructions note cold and execute it, without the conversation history that produced it. This is a **clean context boundary** — the gathering phase explores broadly, then crystallizes into a compact handoff.

Directed reading is one case: "read these documents through this lens, produce a report." But instructions could also say "extract claims," "compare these designs," "update this index."

## What this enables

- **Source ingestion** — gather phase writes instructions, sub-agent executes directed reading
- **Note synthesis** — instructions note links two notes + says how to combine them
- **Literature review** — one instructions note, many input documents, one goal
- **Deep search** — a loop: each iteration writes instructions for the next sub-agent
- **Any delegatable work** — the pattern is general: research → write instructions → spawn clean sub-agent

## What we want to discover

- What does an instructions note actually look like? Enough structure to be unambiguous, loose enough to be general.
- Does the ingestion workflow become "research → write instructions → spawn sub-agent"?
- Is `directed-reading.md` a skill that instructions reference, or is it inlined into the instructions?
- What other workflows naturally produce instructions notes?
- Where do instructions notes live — in `kb/work/`? Next to the goal? Ephemeral or persistent?

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

### Experiment 2: Frontloaded instructions → sub-agent (2026-03-01)

**Instructions note:** `kb/work/ingestion-and-deep-search/instructions-amem-automation-quality.md`
**Documents:** A-MEM ingest, Notes Without Reasons ingest, automating-kb-learning note
**Goal:** Synthesize the automation-quality trade-off in knowledge linking across three sources
**Report:** `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md`

**What changed from Experiment 1:**
- Caller wrote a self-contained instructions note with all context frontloaded
- Sub-agent executed with clean context — no conversation history, no searching
- Multiple documents (3 inputs) instead of one
- No `/connect` step — caller pre-digested the relevant connections into the instructions

**What happened:**
- Sub-agent completed in ~73s, 23K tokens. Read instructions, read all three documents, wrote the report, saved it. No wrong turns.
- Report quality is good — addresses all questions posed, finds the key insight (retrieval vs navigability are different evaluation dimensions, not contradictory positions), and identifies the vocabulary gap (accretion-only vs accretion+curation).
- The frontloading worked: pointing to specific sections ("Extractable Value items 2, 4, and 6") and summarizing each document's relevance meant the sub-agent didn't waste tokens figuring out what mattered.

**Observations:**
- Writing the instructions note took real effort — reading the sources, deciding what to include, articulating the goal precisely. That's the caller's work, not the sub-agent's. This is the correct division of labor: judgment in the instructions, execution in the sub-agent.
- The instructions note is itself a useful artifact. Reading it tells you what the analysis is about without reading the report. It's a reusable spec — you could hand it to a different sub-agent and get a comparable report.
- No `/connect` was needed because the caller already knew the connections. The instructions note replaced what `/connect` would have discovered.
- The `directed-reading.md` procedure wasn't referenced by the instructions — the instructions were self-contained. The procedure is more like writing guidance than a runtime dependency.

**Design implications:**
- Instructions notes are the right interface for delegating analytical work to sub-agents.
- The caller's job: gather, judge, frontload. The sub-agent's job: read, synthesize, write.
- `/connect` is a caller-side tool (helps the caller discover connections to frontload), not a sub-agent-side tool.
