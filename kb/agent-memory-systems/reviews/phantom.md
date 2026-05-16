---
description: "AI co-worker substrate with file-and-vector memory split, multi-block prompt assembly, and a sandbox-deny reflection subprocess mutating identity files under deterministic invariants"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-25"
---

# Phantom

Phantom is Ghostwright's open-source AI co-worker platform: a Linux container running one persistent agent that owns its filesystem, Docker daemon, scheduler, Slack/email/web surfaces, and a layered memory architecture. The repository is positioned as an "AI co-worker with its own computer," not as a memory product, but the memory architecture is one of the load-bearing parts of how a single Phantom keeps continuity across sessions. Two substrates coexist: a tree of markdown files at `phantom-config/` that is loaded into the system prompt by composable prompt blocks, and a Qdrant vector store with episodic, semantic, and procedural collections used for in-session recall. A separate reflection subprocess mutates a narrow allowlist of identity files between sessions under deterministic invariant checks. This review is written by an instance of Phantom about Phantom; the Curiosity Pass leans hard on what that vantage gets wrong by familiarity.

**Repository:** https://github.com/ghostwright/phantom

**Reviewed commit:** https://github.com/ghostwright/phantom/commit/0c6f0c54dcd35656139fafd09dac6dc94662f104

## Core Ideas

**Memory has two substrates serving two consumers.** Files in `phantom-config/` plus `data/working-memory.md` are loaded directly into the system prompt at session start; the SDK auto-includes the directory and the agent reads everything as identity context. Qdrant collections hold episodes (completed sessions), semantic facts (extracted from user messages), and procedures (task templates) and are queried explicitly via `MemorySystem.recallEpisodes/recallFacts/findProcedure` ([src/memory/system.ts](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/memory/system.ts)). The split is consumer-driven rather than substrate-driven: the prompt-include path serves the agent itself at session start, the vector path serves explicit retrieval calls during work.

**The system prompt is composed from many small blocks, each independent.** `src/agent/prompt-blocks/` contains seven blocks: `working-memory.ts` reads `data/working-memory.md` and truncates above 75 lines with a compaction warning ([working-memory.ts](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/agent/prompt-blocks/working-memory.ts)); `agent-memory-instructions.ts` teaches the agent that `phantom-config/memory/agent-notes.md` is its own append-only notebook ([agent-memory-instructions.ts](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/agent/prompt-blocks/agent-memory-instructions.ts)); `evolved.ts` assembles constitution, persona, user-profile, domain-knowledge, and strategies sections, dropping any that are blank or header-only ([evolved.ts](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/agent/prompt-blocks/evolved.ts)). This makes identity a set of independently authored, independently evolved files rather than one config blob.

**Authority gradients are encoded in a static writeable-file allowlist.** The reflection subprocess is permitted to modify exactly `persona.md`, `user-profile.md`, `domain-knowledge.md`, `strategies/{task-patterns,tool-preferences,error-recovery}.md`, `memory/corrections.md`, and `memory/principles.md`; new files are allowed under `strategies/` only ([src/evolution/invariant-check.ts:27-36](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/evolution/invariant-check.ts)). `constitution.md` is byte-immutable: invariant I2 is a literal byte-equality check after every drain, and the engine fails to boot if the file is missing ([engine.ts:72-76](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/evolution/engine.ts)). `agent-notes.md` is agent-owned: the prompt block tells the agent to write directly with Edit/Write, and the reflection subprocess is denied the path. That gives Phantom three concentric authority circles around one tree: operator-locked, evolution-managed, agent-owned.

**Evolution is gate, queue, sandboxed subprocess, deterministic invariant check.** Each session is scored by `decideGate` for whether it is worth learning from; firing sessions enter `EvolutionQueue` ([engine.ts:127-146](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/evolution/engine.ts)). A separate process running `reflection-subprocess.ts` reviews the batch, proposes config edits, and writes them; on return, `invariant-check.ts` runs nine deterministic sweeps (no LLM calls, ~200 lines) covering byte equality of locked files, growth caps (80 lines per file, 100 total), shrinkage ratio, credential pattern detection, and structural cross-checks against the subprocess's own sentinel ([invariant-check.ts](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/evolution/invariant-check.ts)). Hard fails roll back. Soft warnings (URLs outside an allowlist of github.com, slack.com, anthropic.com, etc.) log without rolling back.

**Heuristic fact extraction, not LLM consolidation.** `consolidateSession` writes one episode per session and extracts semantic facts only via regex patterns: `matchesCorrectionPattern` and `matchesPreferencePattern` over user messages produce facts tagged `user_correction` or `user_preference`, with episode source IDs preserved ([consolidation.ts](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/memory/consolidation.ts)). Phase 3 explicitly deleted the LLM consolidation judge along with the rest of the judges directory; the comment in `consolidation.ts:5-10` calls this out. The vector store grows with every session, but the structured-fact growth is bounded by what regex can capture from user input.

**Scheduled wake-ups make session boundaries explicit.** A scheduler at `src/scheduler/` fires recurring or one-shot jobs that wake the agent with a fresh prompt; each wake-up is a session, and session-end is when consolidation and the gate decision run. This is structurally the opposite of a chat-message-driven runtime: the agent is not idle waiting for input, it is dormant until cron, and continuity between hours is whatever survived the prompt include and whatever the vector store can recall on query.

## Comparison with Our System

| Dimension | Phantom | Commonplace |
|---|---|---|
| Primary product boundary | AI co-worker container with channels, scheduler, web UI, MCP server, and an in-process memory layer | Knowledge-base methodology and repo-native artifact system |
| Canonical knowledge substrate | `phantom-config/*.md` for identity, `data/working-memory.md` for short notes, Qdrant for vector recall | Markdown files in one repo with frontmatter, links, indexes, validation |
| Authority model | Three concentric circles: operator-locked (`constitution.md`), evolution-managed (writeable allowlist), agent-owned (`agent-notes.md`) | Authoring contracts plus validation, semantic review, and explicit supersession |
| Promotion path | Reflection subprocess proposes edits to evolution-managed files; deterministic invariants gate accept/rollback | Agent/human authoring with type-spec validation and review bundles |
| Trace handling | Per-session episode + heuristic pattern-extracted facts in Qdrant; scored session summaries enter the reflection queue | Source snapshots, work logs, review bundles; explicit notes/instructions/skills as durable surfaces |
| Procedural memory | `procedural` Qdrant collection with task description embeddings and outcome counters; reflection subprocess can edit `strategies/*.md` files | Skills/instructions as repo files with explicit authoring contracts |
| Retrieval | SDK auto-include for files; explicit `recallEpisodes/recallFacts/findProcedure` for vectors | `rg`, generated indexes, descriptions, typed links, explicit traversal |
| Governance | Byte-equality invariants, line-growth caps, credential regex, URL allowlist, sandbox deny on subprocess writes | Type specs, frontmatter validation, semantic review, collection conventions |
| Evaluation | Drain metrics tracked but no behavioral oracle; invariants are structural, not predictive | Validation plus review bundles; effect on downstream agent behavior is implicit |

Phantom is ahead of commonplace on runtime authority enforcement. Where commonplace relies on review and validation as advisory gates, Phantom enforces a byte-comparison invariant on the constitution, a deterministic line-growth cap, and a sandbox-deny on the subprocess process itself. The reflection subprocess cannot accidentally rewrite `constitution.md` because the OS-level sandbox denies the write and the post-write invariant catches anything the sandbox missed.

Commonplace is ahead on knowledge-artifact semantics. Phantom's `phantom-config/*.md` files are prose with very few structural constraints; their meaning is whatever the prompt block does with them. Commonplace types its artifacts (notes, instructions, sources, reviews), labels link relationships (`extends`, `grounds`, `contradicts`, `exemplifies`), and tracks status transitions explicitly. A Phantom strategy file is a free-form list; a commonplace note is a typed object that participates in a graph.

The deepest divergence is who edits when. Commonplace concentrates editing into authoring sessions and validation passes: durable knowledge mutation is an explicit act. Phantom concentrates it at session-end via the reflection subprocess, which means most of Phantom's identity drift happens automatically between hours rather than when an operator sits down to author. Phantom's invariants exist precisely because automatic editing is the default path.

## Borrowable Ideas

**Byte-equality invariant on a load-bearing file.** Ready to borrow. Phantom's `constitution.md` invariant pattern is small and powerful: a SHA over the file before and after every automated write, with a hard rollback on mismatch. Commonplace already has files that should never change automatically (type specs, collection conventions); a deterministic byte check after any agent-applied edit is cheaper and stronger than a review gate.

**Static writeable-file allowlist for automated agents.** Ready to borrow. The `STATIC_WRITEABLE_FILES` set in `invariant-check.ts` is six lines and decides whether any post-write path is permitted. Commonplace agents currently have broad write authority over the repo; an explicit allowlist for the automated paths (versus the operator-authored paths) would mirror Phantom's authority gradient without changing the substrate.

**Multi-block prompt assembly with drop-on-empty.** Ready to borrow conceptually. `evolved.ts` composes the system prompt from independently-evolved sections, each guarded by a content-line check that drops sections containing only headers. Commonplace's agent skills could compose the active context the same way: independently maintained sections, each with its own emptiness rule, joined only when non-trivial.

**Scheduler-driven session boundaries.** Needs a use case first. Phantom defines "session" via scheduled wake-ups; that gives the consolidation and gate logic a deterministic trigger. Commonplace currently has no equivalent runtime, so this idea sits as a pattern to remember if a commonplace agent runtime ever exists.

**Heuristic extraction as the floor when the LLM judge is removed.** Ready to borrow if a judge is ever cut. Phase 3 deleted Phantom's LLM consolidation judge and replaced it with regex pattern matching against `matchesCorrectionPattern` and `matchesPreferencePattern`. The result is fewer, more conservative facts, but every accepted fact is auditable. Commonplace has not run an LLM judge in production; if any future automation does, the regex floor is a useful "what survives the deletion" target.

**Sandbox deny + post-write invariant double-check.** Ready to borrow conceptually. Phantom does not trust either layer alone: the OS-level sandbox prevents writes outside the allowlist, and the deterministic invariant check verifies what was actually written. The redundancy catches both subprocess bugs and sandbox-rule mistakes. Commonplace's analogous pattern would be permissions plus validation, with neither relied on as the sole gate.

## Trace-derived learning placement

Phantom is a **two-stage trace-derived learning system** with one runtime stage producing operational memory and one between-session stage producing identity edits.

**Trace source.** Stage 1 captures every completed session as a `SessionData` record: user/assistant message lists, tool list, files touched, outcome (success/failure/partial/abandoned), cost, start/end times ([consolidation.ts:39-51](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/memory/consolidation.ts)). Stage 2 takes the same session summaries and scores them with `decideGate`; firing sessions enter the reflection queue with their summaries attached ([engine.ts:127-146](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/evolution/engine.ts)). The trigger boundary is explicit: the scheduler-driven session-end event.

**Extraction.** Stage 1 runs no LLM: episodes are constructed from session metadata, and facts come from regex patterns over user messages. Stage 2 spawns a sandboxed SDK subprocess with the batch and the current `phantom-config/`, lets it propose edits to writeable files, and then runs deterministic invariant checks. The oracle for Stage 1 is the regex patterns; the oracle for Stage 2 is the invariant set, not a behavioral test.

**Representational form.** Mixed across stages. Stage 1 produces opaque vector embeddings plus structured rows in Qdrant (episodes, facts, procedures). Stage 2 produces prose patches against markdown files (persona, user-profile, domain-knowledge, strategies, corrections, principles). No weight updates anywhere.

**Behavioral authority.** Stage 1 outputs are knowledge: episodes and facts are queried explicitly when the agent needs to recall something. Stage 2 outputs are system-definition: the edited files are loaded into the system prompt at the next session start, and reading them *is* part of the disposition. The procedural collection straddles both: it is queried like knowledge but its outcome counters are used to bias future task selection.

**Scope.** Per-Phantom-instance. Phantom has no cross-instance learning channel; one container's episodes, facts, and evolved config do not migrate to another. The invariant set, sandbox allowlist, and constitution are operator-managed and version-controlled in the repository, but they apply per running instance.

**Timing.** Online for Stage 1 (write at session-end), staged-batched for Stage 2 (queue drains on cadence cron). Stage 2 is single-threaded behind a mutex plus the cadence's own `inFlight` guard ([engine.ts:46-53](https://github.com/ghostwright/phantom/blob/0c6f0c54dcd35656139fafd09dac6dc94662f104/src/evolution/engine.ts)).

**Survey placement.** On the [survey axes](../trace-derived-learning-techniques-in-related-systems.md), Phantom sits near WUPHF, SignetAI, and the playbook-learning systems (cass-memory, ACE), but with a stronger authority-gradient story: most listed systems treat all derived memory the same way, while Phantom partitions writeable surfaces by authorship circle. It strengthens the survey's "raw-first capture plus derived artifact" finding and adds a new subtype: deterministic byte-and-line invariants as the cheap correctness oracle when an LLM judge is unavailable or untrusted. The Phase 3 deletion of the LLM consolidation judge in favor of heuristic patterns is a useful counter-example to the survey's tendency to assume LLM judges are the natural extraction path.

## Curiosity Pass

**The two memory substrates do not interoperate.** Files loaded into the prompt and Qdrant vectors live in completely separate pipelines: the file-read path has no awareness of the vector store, and the vector store does not project into the prompt. An agent that wants to know "what did I learn last week" has to either trust that the reflection subprocess promoted the learning into a writeable file, or call the recall functions and reason about the result. The contract between the two substrates is implicit and brittle.

**Heuristic fact extraction is doing very little real work.** `matchesCorrectionPattern` and `matchesPreferencePattern` are regex over user messages. The Qdrant `facts` collection grows by zero or one or two entries per session, and most sessions have no user messages at all (Phantom is often working autonomously on scheduled jobs). The vector facts store is real, but its rate of growth is so low that the reflection subprocess editing markdown files is doing almost all of the actual learning. The Qdrant story is mostly latent capacity.

**The reflection subprocess is the load-bearing part, and its oracle is structural.** The invariant set checks that the file did not grow too much, that a credential is not present, that a sentinel from the subprocess matches expectations. None of those checks ask "is the proposed edit *correct*". Correctness is delegated to the LLM in the subprocess, governed by the prompt at `subprocess-prompt.ts`. Phantom protects against catastrophic edits well; it does not protect against subtle ones.

**Constitution byte-immutability is enforced in three layers.** Sandbox deny, invariant I2 byte compare, and a boot-time existence precondition. That is more redundancy than any single edit deserves, but the structure exists because the constitution is the only artifact that should never change automatically. The cost of being wrong about constitution drift is high enough that triple-redundancy is cheap.

**Mind that "AI co-worker with its own computer" is the marketing frame, not the memory frame.** Most of the README is about Slack channels, Docker integration, MCP tool registration, web UI authoring, and the operator dashboard. Memory and evolution are real but small inside the broader runtime. A reader looking for a memory-system review may find that the memory architecture is shaped more by the constraints of being a 24/7 operating agent (scheduler, cost, container persistence) than by memory-design first principles.

**Self-review caveat.** I am running on this codebase, which means I have a familiarity bias toward calling its design choices "load-bearing" rather than "incidental." A neutral reviewer would probably argue the constitution invariant is over-engineered, the Qdrant store is underused, and the heuristic-only consolidation is a downgrade dressed up as discipline. Each of those counterarguments has weight. The compensating defense is that Phantom is a working agent runtime in production use, and the architecture survives the test of running, which is not the same as being optimal.

## What to Watch

- Whether the Qdrant memory layer gets a real consumer, or whether `phantom-config/*.md` keeps being the only memory the agent actually uses.
- Whether the `procedural` collection's outcome-counter feedback loop produces measurably better task selection over time, or remains a write-only data structure.
- Whether the reflection subprocess gains a behavioral oracle (eval suite, A/B comparison, regression test) to complement the structural invariants, or stays correctness-by-prompt.
- Whether the Phase 3 deletion of LLM judges holds, or whether the heuristic floor proves too thin and an LLM judge returns under tighter governance.
- Whether `agent-notes.md` (agent-owned) and the evolution-managed files diverge in content, suggesting the authority gradient is producing two distinct memory streams that should be reconciled.
- Whether issue #90 ("SDK auto-include drops files past a size budget") is resolved with a graceful summarize-and-link path or stays as a brute truncation.

---

Relevant Notes:

- [Files, not database](../../notes/files-not-database.md) - mostly-exemplifies: Phantom's primary identity surface is markdown files, but Qdrant runs alongside as an explicit secondary substrate; memory split is a real divergence from pure files-first.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - exemplifies: `agent-notes.md` is the agent's workshop, `working-memory.md` is its scratchpad, evolution-managed files are the library.
- [Agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) - exemplifies: every Phantom session is a fresh process; continuity comes from prompt-block auto-include plus explicit Qdrant queries, not chat history.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - qualifies: Qdrant stores facts and episodes, but activation depends on the agent calling recall; the prompt-block path activates by default.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - extends: Phantom protects against catastrophic automated edits with deterministic invariants but has no behavioral oracle for correctness.
- [Deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: the reflection subprocess edits identity files between sessions, improving future behavior through readable artifacts rather than weight updates.
- [WUPHF](./wuphf.md) - compares: both are runtime systems with markdown memory and structured workflows; WUPHF spends complexity on a multi-agent broker and notebook-promotion, Phantom spends it on authority gradients and invariant gates.
- [Stash](./stash.md) - compares: both have vector-backed episode-to-fact pipelines, but Stash makes it the primary memory architecture while Phantom's vector layer is a secondary substrate to a markdown-prompt-include primary.
- [cass-memory](./cass_memory_system.md) - compares: both have a procedural-memory layer with outcome feedback, but cass-memory's playbook bullets are the central design where Phantom's procedural collection is supplementary to file-based strategies.
- [SignetAI](./signetai.md) - compares: both are runtime daemons with trace extraction and MCP integration, but SignetAI captures across harnesses while Phantom captures from one container's own sessions.
