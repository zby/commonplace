# Commonplace — the theory of LLM wikis, running as one

Your agents start every session cold. No memory of last week's decisions. No awareness of what your team already knows. They repeat themselves and produce shallow work because the context is empty.

Andrej Karpathy [sketched the fix](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): give agents a persistent, linked markdown layer they maintain themselves — an **LLM wiki**. The idea caught on. The hard part is everything after the idea: how agents find the right note without loading everything, how a thousand notes stay coherent as they grow, and how an agent knows which of them to trust.

**Commonplace is a framework for building LLM wikis** — typed, linked, review-gated markdown that AI agents write, navigate, and maintain.

And it is **self-hosting**: the theory of how to make LLM wikis work is itself an LLM wiki. The methodology is executed here, not just described — agents follow it to maintain the very repository the theory lives in. The skills agents use to write and validate notes are themselves artifacts in the wiki, maintained the same way. Reading the repo is watching it run.

---

## Not another memory service

Most agent-memory products are services: a database between your agent and its knowledge, background processes deciding what gets remembered, ranking code deciding what gets retrieved. Powerful — and a second runtime you have to trust.

Commonplace takes the opposite bet. **No second runtime.** Plain markdown in git; your agent harness is the engine. Agents write knowledge deliberately, every write passes validation and review, and every change to what your agents believe is a diff you can read, question, and revert. Where memory services optimize recall of everything that happened, an LLM wiki built with Commonplace optimizes trust in what it claims.

## How it works

**Plain markdown files in git.** No database, no platform dependency. Your knowledge lives in files you own and version-control.

**Discoverable.** Claim-as-title headings, retrieval-oriented descriptions, and curated indexes let agents find what they need without loading everything. An agent decides "not this one" from metadata alone.

**Composable.** Notes link to each other with explicit relationship semantics — extends, grounds, contradicts, enables. Agents chain reasoning across notes, not just retrieve isolated facts.

**Trustworthy.** A progression from raw capture to structured claims means each artifact carries a reliability signal, and writes pass typed validation before they land. Agents know what's load-bearing and what's speculative.

**Gets better with use.** Each note you add creates new paths agents can follow. Decisions get grounded in prior work instead of re-derived from scratch.

---

## See it in action: agent memory systems reviewed

We used Commonplace to review 148 agent memory systems — Mem0, Graphiti, Cognee, Letta, Hindsight, GBrain, and more — with a comparative analysis across shared architectural axes.

**These reviews were mostly agent-produced** with minimal human steering. The comparative synthesis — including the finding that the fundamental split isn't storage format but *who decides what to remember* — came from an agent traversing linked reviews and spotting patterns across them. The wiki produced its own market analysis; that is the self-hosting loop doing useful work.

This is what your agents could produce about *your* domain.

[Read the comparative review →](../../agent-memory-systems/agentic-memory-systems-comparative-review.md)
[Browse all system reviews →](../../agent-memory-systems/README.md)

---

## What you get

- **A methodology** — writing conventions, type system, and linking discipline that make knowledge agent-navigable, developed and tested on itself
- **Agent skills** — `/write`, `/ingest`, `/connect`, `/validate` — operations that agents run to build and maintain the wiki
- **A working example** — the Commonplace repo is the methodology running as a wiki, so you can see exactly how it works before committing

## Who this is for

Teams and individuals already using AI agents daily. You've noticed that agents forget, repeat themselves, and miss context that you've already worked through. You want a knowledge layer you can audit, not another service to trust.

**This is early-stage software for early adopters.** The methodology is solid, the tooling works, the rough edges are real. Commonplace runs as agent skills inside agentic coding CLIs like Claude Code or Codex — your harness is the engine; there is no app.

[Get started →](https://github.com/zby/commonplace)
