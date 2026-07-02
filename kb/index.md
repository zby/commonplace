# Commonplace

**Research on knowledge systems, running as one.**

Commonplace is a growing body of research on how to build the most powerful agentic systems. The bet is simple: an LLM can consume a theory and act on it, and can even write the code that theory calls for — so an _actionable_ theory of how to build such systems is itself a way of building them. Commonplace aims to be that theory: one closed under its own recommendations, telling an agent when to reason from prose, when to freeze knowledge into durable code, and how to verify what it produces.

The theory's most actionable immediate target is an **LLM wiki** in the sense [Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked markdown layer that agents build and maintain around your own work. A wiki is two things — notes and the links between them — and an LLM wiki is one where the agent produces both: it **concretizes** a vague thought into a committed note, then **[connects](./notes/links-README.md)** it to everything you've already written. That turns an ephemeral chat, where the insight scrolls away, into a durable, growing body of your thinking. The agent takes the two slow parts, drafting and filing. Judging whether it's _true_ still falls to you — though critique passes, review gates, and refinement loops are moving more of that into the agents too.

The research is **self-hosting**, in the bootstrapping sense. It lives in this repository as notes, and the methodology those notes lay out is executed here, not just described: LLM agents follow it to maintain the very wiki the research lives in. The skills agents use to write, connect, and validate notes are themselves artifacts in the wiki, maintained the same way; the writing conventions govern the very files they are written in. Nothing here is documentation _about_ a separate system — the wiki is the system, and reading it is watching it run. The content is AI-generated through human-AI collaboration: a human directs the inquiry, and AI agents (Claude, ChatGPT, and others) draft, connect, and maintain the notes.

The core mechanism is **[deploy-time learning](./notes/deploy-time-learning-is-the-missing-middle.md)**: deployed AI systems improve through structured knowledge that accumulates in the repo alongside the code — the concrete way the theory above turns into capability. Agents operate under [bounded context](./notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — they can't load everything, so the knowledge they load must cover many situations. The notes here develop the theory and apply it to the design of agent-operated knowledge bases; start with deploy-time learning and follow the links from there.

## Threads worth following

**How agents learn.** [Deploy-time learning](./notes/deploy-time-learning-is-the-missing-middle.md) fills the gap between training and in-context learning. It starts with accumulation — capturing observations, decisions, and patterns as durable artifacts. Three operations transform what's accumulated: [constraining](./notes/definitions/constraining.md) narrows interpretation (conventions → structured types → deterministic code), [distillation](./notes/definitions/distillation.md) extracts focused artifacts from larger reasoning, and [discovery](./notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) produces the high-reach theories that are accumulation's most valuable items. The [learning theory index](./notes/learning-theory-README.md) maps the full landscape.

**What makes memory agent-usable.** [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). Discoverable: agents find what they need without loading everything. Composable: notes chain into arguments via [explicit link semantics](./notes/links-README.md). Trustworthy: notes declare their [maturity](./types/note.md) (`seedling` → `current`) and link to the sources or notes they rest on, so readers know how much weight a claim holds.

**Information and bounded observers.** [Information value is observer-relative](./notes/information-value-is-observer-relative.md) — the same data can contain extractable structure for one observer and noise for another. This grounds why [distillation creates value](./notes/definitions/distillation.md) and why [reverse-compression](./notes/reverse-compression-is-when-llm-output-expands-without-adding.md) — expanding text without adding extractable structure — is a real failure mode.

**Agent memory systems compared.** We reviewed [141 agent memory systems](./agent-memory-systems/README.md) — Mem0, Graphiti, Cognee, Letta, and more — with a [comparative analysis](./agent-memory-systems/agentic-memory-systems-comparative-review.md) across six architectural dimensions. The reviews were mostly agent-produced. The key finding — that the fundamental split is who decides what to remember, not storage format — emerged from an agent traversing linked reviews and spotting patterns across them.

## Browse

Each collection has a README that serves as its curated landing — all are linked from the top menu:

- [Notes](./notes/README.md) — the research itself; the [tag indexes](./notes/tags-README.md) give finer-grained entry points
- [Reference](./reference/README.md) — the shipped system: architecture, type system, CLI, ADRs
- [Agent Memory Systems](./agent-memory-systems/README.md) and [Agentic Systems](./agentic-systems/README.md) — reviews of external systems
- [Sources](./sources/README.md) — snapshotted external material with analysis
- [Instructions](./instructions/README.md) — procedures, skills, and review gates
- [Workshops](./work/README.md) — work currently in flight

## Use it yourself

Commonplace is open source. Clone the repo and it is a functioning knowledge base out of the box — add notes alongside the existing ones and build on the theory. Or install it into your own project as a theory builder for your domain: your agents get the same type system, conventions, and skills, and accumulate domain knowledge instead of starting every session cold. The [GitHub README](https://github.com/zby/commonplace) covers the tool side — repository layout, commands, prerequisites; [INSTALL.md](https://github.com/zby/commonplace/blob/main/INSTALL.md) covers setup, and the [installation architecture](./reference/architecture.md) gives the design rationale.
