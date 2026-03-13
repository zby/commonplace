# The knowledge layer for AI agents

Your agents start every session cold. No memory of last week's decisions. No awareness of what your team already knows. They repeat themselves and produce shallow work because the context is empty.

RAG doesn't fix this. Retrieval gives you recall, not reasoning. An agent that pulls a paragraph about your architecture can't chain it with a design decision from last month to reach a useful conclusion.

**Commonplace is a framework for building knowledge bases that AI agents can use** — structured knowledge they can navigate, compose into arguments, and rely on.

---

## How it works

**Plain markdown files in git.** No database, no platform dependency. Your knowledge lives in files you own and version-control.

**Discoverable.** Claim-as-title headings, retrieval-oriented descriptions, and tag indexes let agents find what they need without loading everything. An agent decides "not this one" from metadata alone.

**Composable.** Notes link to each other with explicit relationship semantics — extends, grounds, contradicts, enables. Agents chain reasoning across notes, not just retrieve isolated facts.

**Trustworthy.** A progression from raw text to structured claims means each artifact carries a reliability signal. Agents know what's load-bearing and what's speculative.

**Gets better with use.** Each note you add creates new paths agents can follow. Decisions get grounded in prior work instead of re-derived from scratch.

---

## See it in action: agent memory systems reviewed

We used Commonplace to review 15 agent memory systems — Mem0, Graphiti, Cognee, Letta, Hindsight, ClawVault, and more — with a comparative analysis across six architectural dimensions.

**These reviews were mostly agent-produced** with minimal human steering. The comparative synthesis — including the finding that the fundamental split isn't storage format but *who decides what to remember* — came from an agent traversing linked reviews and spotting patterns across them.

This is what your agents could produce about *your* domain.

[Read the comparative review →](../../notes/related-systems/agentic-memory-systems-comparative-review.md)
[Browse all system reviews →](../../notes/related-systems/related-systems-index.md)

---

## What you get

- **A methodology** — writing conventions, type system, and linking discipline that make knowledge agent-navigable
- **Agent skills** — `/ingest`, `/connect`, `/validate`, `/convert` — operations that agents run to build and maintain the KB
- **A working example** — the Commonplace repo is itself a knowledge base documenting the methodology, so you can see how it works before committing

## Who this is for

Teams and individuals already using AI agents daily. You've noticed that agents forget, repeat themselves, and miss context that you've already worked through. You want that to stop.

**This is early-stage software for early adopters.** The methodology is solid, the tooling works, the rough edges are real. For now, Commonplace runs as agent skills inside agentic coding CLIs like Claude Code or Codex — no standalone app yet.

[Get started →](https://github.com/zby/commonplace)
