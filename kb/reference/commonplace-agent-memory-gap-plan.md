---
description: "Plan for closing Commonplace's current agent-memory gaps: session traces, candidates, cue activation, behavioral evaluation, lifecycle, source alignment, import, ranking, and authority"
type: kb/types/note.md
tags: []
---

# Commonplace agent memory gap plan

This page turns the gaps in [Agent memory coverage](./agent-memory-coverage.md) into a Commonplace-specific implementation plan. It does not describe how to build a generic agent memory system from scratch. Commonplace already has the baseline: file-backed authored memory, collection and type contracts, generated indexes, validation, semantic review, source snapshots, workshops, instructions, skills, and always-loaded control-plane routing.

The plan focuses on what is missing from that baseline: session-trace capture, candidate queues, situation-triggered activation, behavioral evaluation, lifecycle scheduling, compiled-view source alignment, import/reingest maturity, ranking and quality signals, and authority for automatic memory operations.

## Baseline to preserve

Do not spend roadmap effort rebuilding areas that already work:

- Direct-authored memory through notes, reference docs, ADRs, instructions, skills, source ingests, workshops, validators, and indexes.
- Artifact contracts through `COLLECTION.md`, path-valued `type:` pointers, type specs, schemas, and validation.
- Discoverability through titles, descriptions, tags, directory indexes, generated indexes, key-index pointers, `rg`, file paths, and skill metadata.
- Composability through claim titles, link prose, collection-owned link labels, definitions, and indexes.
- Trust for authored artifacts through deterministic validation, semantic review gates, and review-state provenance.
- Storage role separation for authored markdown, generated indexes, operational reports, and SQLite review state.
- Always-loaded and on-invoke activation through `AGENTS.md`, skills, instructions, and explicit file reads.

## Gap closure sequence

### 1. Define authority for automatic memory operations

Gap: authority for automatic extraction, promotion, activation, and retirement is not fully specified.

First, make the authority model explicit because later automation depends on it. Define who or what may create candidate observations, promote candidates into durable notes or instructions, activate cues in agent context, enforce behavior through scripts or guards, and retire or relax stale memory.

Done when Commonplace has a small authority table for memory transitions, including automatic, reviewed-agent, human, and deterministic-check authority levels.

### 2. Build a candidate memory queue

Gap: there is no mature candidate queue that scores future value against maintenance cost.

Create a lightweight candidate surface between `kb/log.md`, raw traces, workshops, and durable library artifacts. It should support candidate status, source pointer, signal type, scope, confidence, consequence, recurrence, suggested destination, review state, and retirement/merge decisions.

Done when agents can record a correction, silent failure, repeated procedure, preference, or possible discovery without pretending it is already durable knowledge.

### 3. Add lifecycle scheduling for candidates and durable memory

Gap: retirement, supersession, relaxation, recurrence tracking, and scheduled lifecycle work are incomplete.

After candidates exist, add maintenance operations that read lifecycle state and act on it. The first pass should support duplicate merge, supersession, rejection, promotion, retirement, and relaxation from rigid checks back to prose guidance.

Done when a candidate or durable artifact can be triaged as promote, merge, keep, reject, retire, supersede, or relax, and when stale candidate queues cannot silently become a second untrusted library.

### 4. Specify compiled behavior-view source alignment

Gap: compiled behavior-facing views need stronger source-of-truth and regeneration rules.

Before adding many behavior-facing render targets, define how generated `AGENTS.md` excerpts, assistant rules, skills, checklists, cue indexes, guards, and prompt fragments point back to authoritative sources. Each compiled view should carry source path, source version or hash, generator, target surface, generation time, direct-edit policy, stale detection, and rollback/regeneration rules.

Done when behavior-facing generated views are treated as rebuildable compiled outputs rather than independent policy.

### 5. Capture eligible session traces with retention and redaction

Gap: broad session-trace capture, redaction, retention, and replay are not shipped as a memory substrate.

Add trace capture only after eligibility policy is clear. The capture substrate should preserve enough evidence for audit, extraction, debugging, and later re-abstraction without making raw history default context. Start with text-heavy sessions: prompts, model outputs, tool calls, command outputs, approvals, errors, produced artifacts, and final diffs. Add redaction and access rules before model-based extraction.

Done when Commonplace can point a candidate or durable artifact back to a retained session trace or trace excerpt under explicit retention, redaction, and loading policy.

### 6. Extract strong-signal candidates from traces

Gap: automated session-trace extraction is not implemented.

Start with signal types that have visible oracles: explicit corrections, command failures, retries, fallback paths, warnings, weakened guarantees, accepted/rejected suggestions, and repeated tool sequences. Do not begin with broad discovery extraction.

Done when trace extraction can create low-authority candidates with source pointers, confidence, scope, and suggested destinations, and when those candidates enter the same queue as manually recorded observations.

### 7. Add typed situation cues for activation

Gap: there is no typed on-situation cue index; situation-triggered activation remains future work.

Define a cue artifact or generated cue index with trigger condition, lesson, source pointer, role, scope, priority, consequence weight, placement target, false-positive tolerance, and retirement criteria. Keep cues low-authority until they are reviewed or behaviorally tested.

Done when a future agent can receive a relevant warning or procedure before a known repeated mistake, without preloading all potentially relevant policy.

### 8. Measure behavioral uptake and activation quality

Gap: activation, behavioral uptake, context efficiency, source-alignment health, and promotion economics are not first-class metrics.

Add evaluation around the new cue and candidate machinery. Test whether a cue fires in plausible situations, whether it changes downstream plan/tool/artifact behavior, whether it earns context budget, and whether it becomes stale or noisy. For high-priority behavior-changing memory, use WITH/WITHOUT or perturbation-style checks where possible.

Done when Commonplace can distinguish "memory exists," "memory activated," and "memory changed behavior in the intended direction."

### 9. Improve ranking, quality signals, and connection maintenance

Gaps: ranking and quality scoring are underdeveloped; automated connection discovery is report-based, not continuously maintained.

Use the candidate queue, lifecycle state, review state, descriptions, backlinks, link labels, recurrence, and usage/evaluation results as ranking signals. Improve connection maintenance incrementally: reports can remain the first workflow, but repeated accepted connections should inform indexes, link suggestions, or review targets.

Done when future agents can prioritize current, reviewed, high-value, well-connected memory over stale, candidate, noisy, or low-confidence material.

### 10. Mature import and reingest paths

Gap: there is no mature graph-first or bulk-reingest pipeline.

Commonplace already has source snapshots, ingest reports, conversion tooling, and workshops. The next step is reingest and bulk import that preserve source boundaries, map imported material to artifact contracts, detect duplicates, track freshness, and regenerate derived views when sources change.

Done when an imported repository, document set, or legacy note set can be refreshed without turning old extracts into unauditable parallel truth.

### 11. Add retrospective episodes only where they answer real queries

Gap: retrospective episodes remain underdeveloped.

Do not build an episode layer just because memory taxonomies often include one. Add episodes for bounded efforts where future users actually ask "what happened when we tried this?" and where a narrative summary would be cheaper than replaying traces or reading a workshop.

Done when episodes have a clear consumer, source trace or workshop pointer, lifecycle state, and promotion path into durable notes, ADRs, instructions, or negative-result records.

## Ordering rule

The order follows Commonplace's current shape. It starts from the missing governance and candidate substrate, then adds trace capture, extraction, activation, evaluation, ranking, import maturity, and episodes. This preserves Commonplace's existing strength as a directly authored, quality-controlled, file-backed memory substrate while adding autonomous-learning capabilities only after their authority, lifecycle, and evaluation paths exist.

The plan should change when a gap becomes more urgent because of actual use. For example, if imported corpora become the main workload, bulk reingest can move earlier. If repeated mistakes become the main cost, cue activation and behavioral tests can move earlier. The default remains: close the gaps that let Commonplace remember safely before closing the gaps that let it remember more automatically.

---

Relevant Notes:

- [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md) — rationale: defines the memory requirements whose Commonplace gaps this plan closes
- [Agent memory coverage](./agent-memory-coverage.md) — part-of: maps those requirements onto current Commonplace implementation coverage and gaps
- [Review system architecture](./review-architecture.md) — implemented-by: shipped review state and semantic gates used for trust and promotion decisions
- [Storage](./storage-architecture.md) — implemented-by: shipped storage roles for authored markdown, generated views, reports, and review state
