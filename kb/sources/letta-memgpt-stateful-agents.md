# Letta (MemGPT): Stateful Agents with Self-Managed Memory

**Source:** https://github.com/letta-ai/letta
**Original paper:** MemGPT: Towards LLMs as Operating Systems (2023)
**Type:** Open-source agent platform (Apache 2.0), commercial platform
**Retrieved:** 2026-03-05

## Overview

Letta (formerly MemGPT) builds stateful AI agents with self-managed memory. The foundational insight from the MemGPT paper: treat the LLM's context window like RAM in an operating system, and give the agent tools to manage its own memory hierarchy. The agent decides what to remember, what to forget, and when to swap information in and out of context.

## Architecture

### Memory Hierarchy (the OS analogy)

**Core Memory (= RAM)** — always in the context window. Structured as labeled blocks:
- `human` block — facts about the user (name, preferences, relationship context)
- `persona` block — the agent's self-description and personality
- Custom blocks — developer-defined labeled sections

Each block has a `value` (text content), `limit` (character cap), `label`, `description`, and `read_only` flag. Blocks are rendered into the system prompt as XML:
```xml
<memory_blocks>
  <human>
    <description>...</description>
    <metadata>chars_current=150, chars_limit=2000</metadata>
    <value>Name: Alice. Likes hiking...</value>
  </human>
  <persona>...</persona>
</memory_blocks>
```

The agent edits core memory blocks using tools — `core_memory_append`, `core_memory_replace` — which modify the block text directly. The agent sees the current character count and limit, managing space like a program managing RAM.

**Recall Memory (= recent page cache)** — conversation history stored in a database, searchable. The agent can search its past messages.

**Archival Memory (= disk)** — persistent long-term storage. The agent can `archival_memory_insert` and `archival_memory_search` to store and retrieve information that doesn't fit in core memory.

### Context Window Management

The `ContextWindowOverview` tracks everything in the context:
- System prompt + core memory blocks + summary memory + tool definitions + message history
- Token counts for each section
- Archival and recall memory counts (shown as metadata, not full content)

When the message history grows too long, it's summarized and older messages are moved to recall memory, keeping the context window within limits.

### Git-Backed Memory (Context Repositories — new evolution)

Letta is evolving toward `git_enabled` memory where:
- Memory blocks are stored as files in a git repository
- Changes are tracked via git commits with `GitOperations` class
- The agent can read/write files in its memory filesystem
- Block labels use paths (e.g., `system/human`) with prefix stripping for display

`GitOperations` provides:
- Clone repos from object storage (GCS/S3) to temp directories
- Commit changes with structured `MemoryCommit` objects (file changes tracked)
- Push changes back to storage
- Redis-based locking for concurrent access

This is a significant architectural shift: from in-memory blocks to a filesystem-based memory model with version control.

### Agent Loop

The agent runs in a loop:
1. Assemble context (system prompt + core memory + message history + tool definitions)
2. Call LLM
3. LLM may call tools (including memory tools)
4. Execute tool calls, update state
5. Repeat until the agent produces a final response

The agent autonomously decides when to:
- Write to core memory (important facts it wants to always see)
- Archive information (important but doesn't need to be in every context)
- Search recall/archival memory (needs to find something)

### Storage

- PostgreSQL for agent state, blocks, messages
- Object storage (GCS/S3) for git-backed memory repos
- Redis for locking and caching
- External vector search (e.g., Turbopuffer) for archival memory search

### API Surface

Full REST API + Python/TypeScript SDKs:
```python
client = Letta(api_key="...")
agent = client.agents.create(
    model="openai/gpt-5.2",
    memory_blocks=[
        {"label": "human", "value": "Name: Alice"},
        {"label": "persona", "value": "I am a helpful assistant"}
    ],
    tools=["web_search"]
)
response = client.agents.messages.create(agent.id, input="Hello")
```

Also has a CLI tool (`letta-code`) that runs agents locally in the terminal.

### Multi-Agent

Supports multi-agent architectures with:
- Shared memory blocks between agents
- Agent-to-agent messaging
- Broadcast messaging for multi-agent coordination

## Key Design Decisions

1. **Agent self-manages memory** — the most distinctive feature. The agent, not external code, decides what goes in core memory, what gets archived, what gets searched. Memory management IS the agent's reasoning.
2. **OS analogy taken literally** — core memory = RAM (fast, limited), archival = disk (large, searchable), recall = page cache. Context window is the constraint that drives the architecture.
3. **Blocks as structured core memory** — not just free text, but labeled sections with character limits. The agent sees its own memory constraints and manages within them.
4. **Git-backed evolution** — moving from in-memory blocks to filesystem + version control. This adds persistence, history, and the ability to treat memory as files that agents can manipulate.
5. **Platform orientation** — Letta has evolved from a research prototype (MemGPT paper) to a full platform with REST API, SDKs, multi-agent support, and commercial hosting.

## Limitations

- The self-managing memory approach requires capable models — works best with frontier models (recommends Opus 4.5, GPT-5.2)
- Core memory blocks have fixed character limits; the agent must manage space manually
- The git-backed memory evolution is still early; adds significant infrastructure complexity
- Has become more of a platform than a focused memory system — less architecturally distinctive now
- Memory management quality depends entirely on the LLM's judgment
