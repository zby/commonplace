# Commonplace

Commonplace is a theory builder for AI agent systems — a knowledge base that doesn't just store but processes, turning accumulated observations into theories with [reach](./notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md). Agents operate under [bounded context](./notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md): they can't load everything, so the knowledge they load must cover many situations, not just one.

**[Deploy-time learning](./notes/deploy-time-learning-the-missing-middle.md)** is the central theory — deployed AI systems improve through structured knowledge that accumulates in the repo alongside the code. The notes here develop that theory and apply it to the design of agent-operated knowledge bases.

This KB is itself agent-operated: a human directs the inquiry, AI agents draft, connect, and maintain the notes. The framework for building knowledge bases is documented using that framework.

## Threads worth following

**How agents learn.** [Deploy-time learning](./notes/deploy-time-learning-the-missing-middle.md) fills the gap between training and in-context learning. Two mechanisms transform accumulated knowledge: [constraining](./notes/constraining.md) narrows interpretation (conventions → structured types → deterministic code), while [distillation](./notes/distillation.md) extracts focused artifacts from larger reasoning. A third operation — [discovery](./notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — produces the high-reach theories that are accumulation's most valuable items. The [learning theory index](./notes/learning-theory-index.md) maps the full landscape.

**What makes knowledge agent-usable.** A [good agentic KB](./notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) maximizes contextual competence through three properties. Discoverable: agents find what they need without loading everything. Composable: notes chain into arguments via [explicit link semantics](./notes/links-index.md). Trustworthy: a [type ladder](./notes/types/structured-claim.md) from raw text to structured claims carries reliability signals.

**Information and bounded observers.** [Information value is observer-relative](./notes/information-value-is-observer-relative-because-extraction-requires-computation.md) — the same data can contain extractable structure for one observer and noise for another. This grounds why [distillation creates value](./notes/distillation.md) and why [reverse-compression](./notes/reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) — expanding text without adding extractable structure — is a real failure mode.

**Agent memory systems compared.** We reviewed [15 agent memory systems](./notes/related-systems/related-systems-index.md) — Mem0, Graphiti, Cognee, Letta, and more — with a [comparative analysis](./notes/related-systems/agentic-memory-systems-comparative-review.md) across six architectural dimensions. The reviews were mostly agent-produced. The key finding — that the fundamental split is who decides what to remember, not storage format — emerged from an agent traversing linked reviews and spotting patterns across them.

## Browse by topic

- [Tags](./notes/tags-index.md) — all tag indexes: foundations, architecture, evaluation, learning theory, and more
- [Notes directory](./notes/index.md) — auto-generated listing of all notes
- [Sources](./sources/index.md) — snapshotted external sources and analyses

## Use it yourself

Commonplace is open source. You can use it in two ways:

**Clone and explore.** The repo is a functioning knowledge base out of the box. Add notes alongside the existing ones, run the agent skills (`/connect`, `/validate`, `/ingest`), and build on the theory. This is also the right mode for evaluating the system before installing it elsewhere.

**Install into your own project as a theory builder for your domain.** Commonplace can be added to any project as a submodule or cloned subdirectory. It provides the type system, writing conventions, agent skills, and methodology — your agents accumulate domain knowledge and build explanatory structure instead of starting every session cold. See the [installation guide](../INSTALL.md) for setup instructions and the [installation architecture](./notes/commonplace-installation-architecture.md) for design rationale.

Both paths use the same framework. The difference is whether you're building theory about agentic systems (this repo's domain) or about your own.

For the full technical reference — directory layout, prerequisites, scripts — see the [README](../README.md).
