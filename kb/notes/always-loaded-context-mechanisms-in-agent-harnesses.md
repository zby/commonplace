---
description: Survey of always-loaded context mechanisms across agent harnesses — system prompt files, capability descriptions, memory, and configuration injection — cataloguing what each carries, how write policies differ, and where the gaps are
type: note
traits: []
tags: []
status: seedling
---

# Always-loaded context mechanisms in agent harnesses

Agent harnesses inject several kinds of context before the agent sees its first user message. This note catalogues the user-facing mechanisms — the surfaces that project authors and tool developers control. Platform-injected context (safety preambles, behavioral guidelines, tool schemas) also competes for the same token budget but is not configurable and falls outside the scope of this survey.

The same structural roles appear across platforms — Claude Code, Codex, Gemini, Cursor — despite independent implementations. Whether this reflects genuine convergence or shared ancestry from early prompt-engineering practices is unclear; the [OSS study](../sources/context-engineering-ai-agents-oss.ingest.md) documents current similarity but not the history.

## System prompt files

**Platform names:** CLAUDE.md (Claude Code), AGENTS.md (Codex), GEMINI.md (Google), .cursorrules (Cursor).

Loaded every session, these files carry several distinct kinds of content:

- **Constraints** — "do this, don't do that" (git conventions, guardrails, safety boundaries)
- **Routing rules** — "when you encounter X, look here" (conditional pointers consulted when relevant)
- **Definitions** — shared vocabulary, key concepts, scope boundaries (reference material, neither imperative nor routing)
- **Domain scope** — what the project is about, what belongs and what doesn't
- **Operational recipes** — build commands, test invocations, deployment steps

What unifies these is not that they're all directives — definitions are purely informational — but that the agent needs them available before it knows what task it's working on.

The last category deserves a caveat: the [OSS study](../sources/context-engineering-ai-agents-oss.ingest.md) found build commands in 40 repos and testing instructions in 25, making operational recipes common in practice. But the [control-plane model](./agents-md-should-be-organized-as-a-control-plane.md) would route most of them to on-demand documents, reserving the system prompt file for pointers. The tension between what practitioners embed and what theory recommends is real and unresolved.

**In practice:** Lopopolo (OpenAI/Codex, 2026) maintains a 100-line AGENTS.md as "a map with pointers to deeper sources of truth" for a 1M LOC agent-generated codebase. Across open source, AGENTS.md files average 142 lines (SD=231), with 50% never updated after creation; CLAUDE.md files average 287 lines (SD=112) ([OSS study](../sources/context-engineering-ai-agents-oss.ingest.md)).

**Internal organization:** The [control-plane model](./agents-md-should-be-organized-as-a-control-plane.md) proposes three layers: invariants (safety, universal conventions), routing (where artifacts go, what to read next), and escalation boundaries (when to leave the system prompt and load deeper guidance).

## Capability descriptions

**Platform names:** skill descriptions (.claude/skills/), tool descriptions (MCP tool listings), extension metadata.

The agent sees a menu of available capabilities and decides whether to invoke one. The description must be good enough for the agent to recognize when a capability is relevant, but the detailed instructions only load when invoked. This is the key structural difference from system prompt files: capability descriptions are always *listed* but their bodies load on demand.

**What belongs here:** Task-specific workflows the agent should know about but not always execute. In this KB: `/connect`, `/validate`, `/ingest`, `/review-related-system`.

**Overlap with system prompt files:** The two surfaces sometimes point toward the same work through different mechanisms. A system prompt says "before creating notes, read WRITING.md" (routing rule). A skill description says "/connect — find connections between notes" (available capability). Both concern note-writing, but one shapes the agent's background understanding while the other offers an action to take.

## Memory

**Platform names:** MEMORY.md (Claude Code auto-memory), core memory blocks (Letta/MemGPT), reflection files (Pi Self-Learning).

Memory is always-loaded contextual state that accumulates across sessions — user preferences, project context, past decisions. It differs from system prompt files in that it is not authored once but grows and changes through use. Its main design tension is growth: memory that accumulates without curation competes for the same token budget as constraints and routing.

**The write-policy question** is the central design axis — who decides what enters memory and when:

- **Human-governed agent writes** (Claude Code): the agent writes entries, but the policy for when and what to remember is defined by human-authored instructions in the system prompt
- **Fully agent-managed** (Letta/MemGPT): the agent autonomously decides what to store, update, and delete using self-edit tools
- **External pipeline** (Pi Self-Learning): a separate process analyzes session traces and updates memory; the agent doesn't control the write policy

These represent different trust models for who curates always-loaded state. The boundaries are not sharp — users can also write memory entries directly (e.g., editing MEMORY.md by hand), making memory indistinguishable from system prompt content except by the expectation that it will also accumulate agent-written entries over time.

## Configuration injection

**Platform names:** build-time generation (commonplace install scripts), settings merge (Pi's three-level settings), environment variables.

Some always-loaded values are static within one installation but variable across installations: sibling repo paths, local tool paths, environment-specific endpoints. These are resolved before the agent sees them, either at build time or at session start.

**Mechanisms:**
- Build-time template expansion: `{{claw_root}}/notes/` → `commonplace/kb/notes/`
- Settings merge: defaults → global config → project config → session overrides
- Environment variable injection

This is [partial evaluation applied to instructions](./frontloading-spares-execution-context.md) — pre-computing static parts so the agent doesn't waste context on resolution at runtime. The inputs can be repo-committed or [installation-specific](./generate-instructions-at-build-time.md) (local paths, endpoints) — the mechanism is the same.

## Design principles

**Token budget is shared.** All four surfaces compete for the same finite context window. The [loading hierarchy](./instruction-specificity-should-match-loading-frequency.md) exists because always-loaded context must be slim — anything that can load on demand should.

**Read and write cadences both matter.** Write cadences differ: system prompt files change with project structure (weeks/months), capability descriptions with tool development (days/weeks), memory continuously, configuration rarely. Read patterns differ too: system prompt files and memory are present every session, configuration is resolved once at build/session-start, capability descriptions are scanned as a list every session but their bodies load on demand. Mixing content with mismatched cadences on the same surface creates staleness risk on the write side and wasted attention on the read side.

**The ambient/on-demand distinction is the load-bearing one.** System prompt files, memory, and resolved configuration are all ambient — present every session regardless of task. Capability descriptions are the one surface where detailed content loads on demand. This is why skill bodies can be long and procedural while system prompt files must be concise.

**Volatile project state is a gap.** Temporary declarations like "we're in a code freeze" or "the migration to v2 is in progress" don't fit cleanly on any surface. The [control-plane model](./agents-md-should-be-organized-as-a-control-plane.md) explicitly excludes volatile state from system prompt files. Memory accumulates from agent observations, not human declarations about current state. Configuration is static per installation. In practice, project state ends up in system prompt files anyway — the least bad option — but it's the content most likely to go stale.

---

Relevant Notes:

- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — foundation: the loading hierarchy that establishes why always-loaded context must be slim
- [AGENTS.md should be organized as a control plane](./agents-md-should-be-organized-as-a-control-plane.md) — extends: internal organization of the system prompt file surface
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — grounds: the partial evaluation principle behind configuration injection
- [Agent statelessness means the context engine should inject context automatically](./agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) — extends: proposes an "on reference" layer within the loading hierarchy that would dynamically inject definitions, ADRs, and indexes alongside loaded documents
