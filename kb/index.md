# Commonplace

**Research on knowledge systems, running as one.**

Commonplace is a growing body of research on how to design knowledge so AI agents — not just people — can build, consume, and reason over it. Its first and current application is an LLM wiki in the sense [Karpathy sketched](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a persistent, linked markdown layer that agents build and maintain around your own work. And the research runs the way it argues for — the knowledge base participates in its own reasoning, review, and execution. This repository ships the type system, writing conventions, agent skills, and Python commands to run one.

A wiki is two things — notes and the links between them — and an LLM wiki is one where the agent produces both: it **concretizes** a vague thought into a committed note, then **[connects](./notes/links-README.md)** it to everything you've already written. That turns an ephemeral chat, where the insight scrolls away, into a durable, growing body of your thinking. The agent takes the two slow parts, drafting and filing; judging whether a claim is _true_ still falls to you — though review gates and refinement loops are moving more of that into the agents too.

It is **self-hosting**, in the bootstrapping sense: the theory of how to build LLM wikis lives here as notes, and the agents that maintain this repository run on the methodology those notes describe. Nothing here is documentation _about_ a separate system — the wiki is the system, and reading these pages is watching it run.

**The content is AI-generated** through human-AI collaboration: a human directs the inquiry, and AI agents (Claude, ChatGPT, and others) draft, connect, and maintain the notes.

The central theory is **[deploy-time learning](./notes/deploy-time-learning-is-the-missing-middle.md)**: deployed AI systems improve through structured knowledge that accumulates in the repo alongside the code. Agents operate under [bounded context](./notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — they can't load everything, so the knowledge they load must cover many situations. The notes here develop that theory and apply it to the design of agent-operated knowledge bases. See the [Reference](./reference/README.md) collection for architecture, types, and CLI.

## Threads worth following

**How agents learn.** [Deploy-time learning](./notes/deploy-time-learning-is-the-missing-middle.md) fills the gap between training and in-context learning. It starts with accumulation — capturing observations, decisions, and patterns as durable artifacts. Three operations transform what's accumulated: [constraining](./notes/definitions/constraining.md) narrows interpretation (conventions → structured types → deterministic code), [distillation](./notes/definitions/distillation.md) extracts focused artifacts from larger reasoning, and [discovery](./notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) produces the high-reach theories that are accumulation's most valuable items. The [learning theory index](./notes/learning-theory-README.md) maps the full landscape.

**What makes memory agent-usable.** [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md). Discoverable: agents find what they need without loading everything. Composable: notes chain into arguments via [explicit link semantics](./notes/links-README.md). Trustworthy: notes declare their [maturity](./types/note.md) (`seedling` → `current`) and link to the sources or notes they rest on, so readers know how much weight a claim holds.

**Information and bounded observers.** [Information value is observer-relative](./notes/information-value-is-observer-relative.md) — the same data can contain extractable structure for one observer and noise for another. This grounds why [distillation creates value](./notes/definitions/distillation.md) and why [reverse-compression](./notes/reverse-compression-is-when-llm-output-expands-without-adding.md) — expanding text without adding extractable structure — is a real failure mode.

**Agent memory systems compared.** We reviewed [141 agent memory systems](./agent-memory-systems/README.md) — Mem0, Graphiti, Cognee, Letta, and more — with a [comparative analysis](./agent-memory-systems/agentic-memory-systems-comparative-review.md) across six architectural dimensions. The reviews were mostly agent-produced. The key finding — that the fundamental split is who decides what to remember, not storage format — emerged from an agent traversing linked reviews and spotting patterns across them.

## Browse

Each collection has a README that serves as its curated landing — all are linked from the top menu. The current collections are [Notes](./notes/README.md), [Reference](./reference/README.md), [Agent Memory Systems](./agent-memory-systems/README.md), [Agentic Systems](./agentic-systems/README.md), [Sources](./sources/README.md), [Instructions](./instructions/README.md), and [Workshops](./work/README.md).

For deeper navigation:

- [Tags](./notes/tags-README.md) — tag indexes within Notes
- [Workshops](./work/README.md) — the stuff we currently work on

## Use it yourself

Commonplace is open source. You can use it in two ways:

**Clone and explore.** The repo is a functioning knowledge base out of the box. Add notes alongside the existing ones, run the agent skills (`/cp-skill-connect`, `/cp-skill-validate`, `/cp-skill-ingest`), and build on the theory. This is also the right mode for evaluating the system before installing it elsewhere.

**Install into your own project as a theory builder for your domain.** Commonplace can be added to any project as a submodule or cloned subdirectory. It provides the type system, writing conventions, agent skills, and methodology — your agents accumulate domain knowledge and build explanatory structure instead of starting every session cold. See the [installation guide](https://github.com/zby/commonplace/blob/main/INSTALL.md) for setup instructions and the [installation architecture](./reference/architecture.md) for design rationale.

Both paths use the same framework. The difference is whether you're building theory about agentic systems (this repo's domain) or about your own.

For the full technical reference — directory layout, prerequisites, scripts — see the [README](https://github.com/zby/commonplace).
