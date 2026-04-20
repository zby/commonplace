---
description: Shell-first TribleSpace agent runtime with branch-separated cognition/archive/memory, chat-log importers, and budget-adaptive temporal memory built from an append-only event graph
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-05"
---

# Playground

Playground is a Rust agent runtime built around a TribleSpace pile rather than a markdown repository. Its central loop is intentionally small: model output becomes a shell command request, an executor writes the command result back into the graph, and the next prompt is assembled from that recorded history. Around that loop it adds a growing set of "faculties" for memory, archive import, wiki fragments, relations, diagnostics, Teams, and web search. The repo's rhetoric frames this as a persistent digital being, but the implemented mechanism is more concrete and more interesting: an append-only, queryable event store that projects past execution and imported conversation traces into the next model context.

**Repository:** https://github.com/triblespace/playground

## Core Ideas

**Shell-first causality is the system's hard constraint.** Playground treats the shell as the model's physical world. The main loop stores a sequence of thought, model request, model result, command request, and command result entities, and the prompt tells the model to emit exactly one raw shell command per turn. This is a real constraint, not just framing language: the loop is built so every observation is command output and every next action is another command.

**One append-only pile holds several distinct branches of experience.** The repo keeps cognition, memory, archive, config, wiki, and other faculties in the same TribleSpace substrate but under separate schemas and branch identities. That gives it a single auditable store without collapsing all artifacts into one least-common-denominator record type. The result is closer to an event-sourced operating substrate than to a note collection.

**Long-term context is projected as synthetic memory turns, not retrieved piecemeal by the model.** Memory chunks carry summaries, time intervals, child edges, and optional provenance to exec results or imported archive messages. At prompt-build time, Playground selects root chunks, drops old roots if needed, then adaptively splits the widest parents whose children fit the remaining budget. The selected chunks are rendered as synthetic `memory <range>` shell turns, followed by a fixed breath boundary and then recent raw command turns.

**Archive import is a real normalization pipeline with raw provenance preserved.** Separate importers for ChatGPT, Codex, Copilot, Gemini, and Claude Code ingest source-specific exports, store the raw source tree, then project them into a unified archive message graph with stable identities, authors, attachments, reply edges, source-format metadata, and conversation groupings. This is not learning by itself, but it creates a durable substrate for later trace mining.

**The repo currently implements simpler memory mechanics than some docs suggest.** The active memory architecture and code center on explicit chunk creation, temporal ranges, and read-time adaptive splitting. Historical docs and parts of the README still mention lenses, compaction requests, and automation paths more aggressively than the current `memory` faculty implements. The important mechanism today is selective summarization plus prompt assembly, not an autonomous multi-lens memory compiler.

## Comparison with Our System

Playground overlaps with commonplace on one axis and diverges on another. Both systems care about persistent knowledge under bounded context, provenance, and agent-facing inspectability. But commonplace is a library-first knowledge base made of human-readable notes linked by explicit semantics, while Playground is a runtime-first operating substrate made of typed events, summaries, and tool faculties inside one append-only graph.

| Dimension | Playground | Commonplace |
|---|---|---|
| Primary substrate | TribleSpace pile with typed event/entity schemas | Markdown notes and instructions in git |
| Main unit of knowledge | Events, memory chunks, wiki versions, faculty artifacts | Notes, instructions, ADRs, tasks, workshop artifacts |
| Context delivery | Preassembled prompt: memory cover -> breath -> recent moment turns | Progressive disclosure: descriptions first, full notes on demand |
| Retrieval model | Query and projection over one append-only graph | Search, links, and explicit reader choice |
| Trace ingestion | Built-in importers for external chat logs plus native exec history | Manual/source-driven capture, snapshots, workshop artifacts |
| Validation/governance | Strong audit trail and diagnostics, weak semantic structure | Stronger semantic structure and deterministic note validation |
| Integration surface | Faculties, exec worker, model worker, VM-backed shell | Instructions, skills, scripts, repo workflows |

**Where Playground is stronger.** It has a more explicit runtime substrate than commonplace. Every turn, request, result, rationale, and imported chat message can live in one auditable graph with stable provenance edges. The shell-first causality rule is also genuinely constraining in a useful way: it keeps the model's world grounded in concrete effects rather than abstract tool call narratives. The memory cover builder is another real contribution. It does not just dump old summaries into context; it chooses a budget-fitting antichain of time ranges and refines the widest summaries first.

**Where commonplace is stronger.** Our artifacts are more composable as knowledge. Playground's memory chunks are temporal summaries addressed by range, not stable conceptual units connected by explicit semantic relationships. Its wiki faculty adds versioned fragments and links, but the center of gravity is still event history plus runtime projection. Commonplace makes relationship semantics first-class, which matters when knowledge needs to travel across tasks and survive beyond one agent runtime. Playground is better at preserving lived traces; commonplace is better at turning ideas into reusable arguments and procedures.

**Trace-derived placement.** Playground clearly belongs in the broader trace-derived set, but as a weaker artifact-learning case than ACE, ExpeL, or ClawVault. Here "weaker" means the promotion boundary is still mostly explicit curation over a rich trace substrate, rather than automated extraction with lifecycle mutation. In this note, "artifact-learning" means traces are promoted into durable, queryable artifacts that can shape later context, even if the promotion step is explicit or human-gated. Semi-automated systems sit between those extremes: stronger than Playground's mostly manual chunk promotion, weaker than loops that automatically extract and maintain rules or playbooks. Playground imports and normalizes agent/session traces, and it can promote specific time ranges into durable memory chunks. But the reviewed repo does not implement a strong automatic extraction loop that continuously learns rules or policies from those traces.

## Borrowable Ideas

**A stable memory/moment seam for cache-aware prompting.** Ready with prerequisite. The fixed breath boundary plus one-turn delay when the memory cover changes is a concrete runtime trick, not just a prompt flourish. If we ever run a persistent shell loop around commonplace, this is an immediately borrowable pattern for keeping the stable prefix cacheable.

**Unified trace normalization with source-specific importers and shared projection.** Needs a use case first. The archive importers keep raw provenance while mapping different export formats into one queryable message graph. That is a strong pattern for any future commonplace trace-ingestion layer, but it only pays off once we truly need cross-source conversational trace analysis.

**Budget-adaptive refinement of coarse summaries.** Needs a use case first. The memory cover algorithm does something specific and useful: it starts with coarse roots and spends remaining budget on splitting the widest parents. That is a stronger mechanism than "include summaries until full." It could matter for workshop compaction or long source-review histories if we decide to project temporal summaries into agent context.

**Reason notes as a separate first-class event stream.** Ready now in some workflows. The `reason` faculty records rationale without forcing it into the main command channel. Commonplace already distinguishes between durable notes and transient workshop traces; this suggests a cleaner shape for lightweight rationale capture tied to specific actions.

## Curiosity Pass

The repo's most important distinction is between rhetoric and mechanism. The system prompt talks about identity, embodiment, and a digital being with memory. The code that matters is narrower: a model worker sends provider requests, an exec worker runs commands, a memory branch stores summaries, and prompt assembly projects those artifacts into the next turn. The anthropomorphic layer may be useful as agent guidance, but it is not the architectural contribution.

**Shell-first causality.**
1. *Property claimed:* grounded, reproducible action.
2. *Transform or relocate?* Genuine constraint. The model's freeform text is reduced to one command line and the world answers through command output.
3. *Simpler alternative:* generic tool calls with arbitrary JSON arguments. That would still ground actions, but it would lose the strong "same medium for every act" discipline.
4. *Ceiling:* this can only ground what the shell can safely mediate. It does not solve planning quality or semantic correctness by itself.

**Append-only graph with branch-separated schemas.**
1. *Property claimed:* auditability plus heterogeneity without schema collapse.
2. *Transform or relocate?* Mostly relocation and normalization. It moves many artifact types into one substrate with explicit tags and edges.
3. *Simpler alternative:* separate SQLite tables or plain files per subsystem.
4. *Ceiling:* a better substrate does not automatically produce better knowledge. Without stronger curation rules, the graph can become an excellent log of mediocre memory.

**Budget-adaptive memory cover.**
1. *Property claimed:* preserve long-term context under a bounded window.
2. *Transform or relocate?* Genuine transformation at prompt-build time. The system chooses an antichain of summaries and refines it by splitting parents into children where budget permits.
3. *Simpler alternative:* truncate oldest summaries until the prompt fits.
4. *Ceiling:* the selection logic can only work with summaries that already exist. If chunk creation is sparse or low quality, adaptive splitting just rearranges thin material.

**Archive import pipeline.**
1. *Property claimed:* make heterogeneous external traces queryable in one model.
2. *Transform or relocate?* Both. It preserves raw source trees, but it also transforms vendor-specific exports into a common message graph with stable conversation/message identities.
3. *Simpler alternative:* keep raw JSON and search it ad hoc.
4. *Ceiling:* normalized traces are still traces. They only become learning if another loop distills them into durable, decision-shaping artifacts.

The main thing this pass updates is the memory story. README examples still gesture toward richer automation, but the implemented current system is more conservative and therefore easier to trust: explicit chunking, explicit provenance, adaptive read-time selection. That narrower mechanism is still interesting. It just means Playground is best read as an event substrate with curated temporal memory, not as an already-solved autonomous memory compiler.

## What to Watch

- Whether the repo resolves the current documentation drift by either reviving automated memory-build paths or removing the lens/compaction residue from user-facing docs
- Whether the wiki and memory branches converge into a stronger long-term knowledge lifecycle, or remain separate facilities sharing only a substrate
- Whether archive import grows into explicit trace-to-rule or trace-to-playbook promotion, which would make Playground a much stronger trace-derived learning reference
- Whether the shell-first loop remains the center of gravity as more communication faculties accumulate, or gets diluted into a generic agent platform

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — comparison frame: this review uses that note's ingestion/promotion axes to place Playground as a trace-normalization and manual-summary case
- [files-not-database](../../notes/files-not-database.md) — contrast lens: Playground gets many of the inspectability benefits we want from files, but it reaches them through a typed append-only graph rather than a human-readable repository
- [agents-navigate-by-deciding-what-to-read-next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) — contrast lens: Playground preassembles memory and moment into one prompt, while commonplace makes the reader decide what to load next
- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — analogy: Playground's trace substrate is strong, but its memory promotion still looks more like weak-oracle curation than hard-verified learning
