---
description: Document-to-simulation stack with Neo4j graph extraction, cross-platform agent rounds, sliding-window compaction, and ReACT reporting; strongest nearby reference for graph-backed simulation loops
type: agent-memory-system-review
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-03-31"
---

# MiroShark

MiroShark is a Python/Vue system for turning an uploaded document into a simulated public-reaction environment. It builds a Neo4j knowledge graph from the document, generates agent personas from graph entities, runs Twitter/Reddit/Polymarket simulations over those personas, tracks heuristic belief drift across rounds, and then uses a ReACT-style report agent to analyze what happened. Built by Aaron Elijah Mars on top of earlier MiroFish work and CAMEL/OASIS components, it is closer to a document-conditioned swarm simulator than to a durable knowledge base, but several of its mechanisms are relevant to commonplace because they show how graph extraction, prompt shaping, and context compaction can be combined into an inspectable agent loop.

**Repository:** https://github.com/aaronjmars/MiroShark

## Core Ideas

**The uploaded document is compiled into a simulation graph, not stored as a source artifact.** The backend generates an ontology from the document and simulation requirement, chunks the text, runs LLM-guided NER/relation extraction, embeds entity summaries and relation facts, then writes the result into Neo4j with vector and fulltext indexes. The important move is not "knowledge graph" in the abstract but using the graph as the intermediate representation that every later stage depends on: persona generation, search, and report writing all query the graph rather than the raw document.

**Persona generation is a layered retrieval-and-synthesis step over graph entities.** Agent profiles are built from graph attributes, connected edges, hybrid search over the graph, related nodes, and optional LLM-powered web enrichment when the entity is notable or graph context is thin. The result is a simulation persona format for Twitter, Reddit, and Polymarket rather than a reusable knowledge object. MiroShark is therefore strongest not at preserving source truth, but at converting extracted context into platform-specific actor prompts.

**Cross-platform simulation is treated as a shared-state system, not three isolated sandboxes.** Twitter, Reddit, and Polymarket run concurrently, but they exchange information through explicit bridges: market prices are injected into social prompts, social sentiment is injected into trader prompts, and a sliding-window `RoundMemory` keeps compacted history plus full recent detail across platforms. This is a real mechanism, not just a product story. The repo has concrete code for bridge state, round compaction, and cross-platform prompt injection.

**Belief dynamics are kept in symbolic state outside the LLM rather than inferred from chat transcripts alone.** Each agent gets a `BeliefState` with topic positions, confidence, trust, and exposure history. Updates are heuristic: trust shifts with likes/follows/mutes, novelty amplifies first-seen arguments, and confidence reacts to social reinforcement. This makes the "opinion drift" claim inspectable and cheap, even if it is still a simplified model of real belief change.

**Reporting is a retrieval workflow over simulation traces, not just a post-hoc summary prompt.** The report agent plans an outline, calls graph-retrieval tools, reads simulation outputs, and logs detailed tool/LLM actions to `agent_log.jsonl`. That makes the report path more auditable than the usual "ask the model what happened" pattern. The report can still hallucinate or over-interpret, but the mechanism at least exposes what evidence surfaces were available.

## Comparison with Our System

| Dimension | MiroShark | Commonplace |
|---|---|---|
| Primary goal | Simulate public reaction to a source document across social/market channels | Build durable knowledge for agent navigation, reasoning, and maintenance |
| Core substrate | Neo4j graph + embeddings + per-platform SQLite simulation state | Markdown files in git with explicit links, types, and descriptions |
| Knowledge unit | Extracted entity/relation graph plus generated personas and action traces | Authored note with retrieval-oriented description and explicit relationship semantics |
| Main transformation | Raw document -> ontology -> graph -> personas -> simulated traces -> report | Raw insights/sources -> notes -> links/indexes/instructions/skills |
| Temporal state | Stronger runtime temporality: rounds, belief drift, compacted histories, market-price feedback | Stronger durable curation: stable notes, indexes, validation, link semantics |
| Retrieval style | Hybrid graph search plus task-specific report tools | Progressive disclosure via routing files, indexes, `rg`, and note descriptions |
| Validation/governance | Narrow deterministic checks around config/schema cleaning; most semantic quality delegated to prompts and heuristics | Explicit writing rules, structural validation, link semantics, and review gates |
| Human inspectability | Medium: inspectable code and outputs, but primary state lives in databases and generated traces | High: source of truth is readable markdown under version control |

The systems overlap only at the edge. MiroShark is useful to commonplace mainly as a reference for how a graph-backed, long-running agent environment can stay somewhat inspectable. It is not solving the same problem. Its "knowledge" is an execution substrate for simulation, not a curated library meant to survive beyond the current scenario.

Where MiroShark is stronger is runtime state management. Commonplace does not have an equivalent to cross-platform round memory, explicit belief-state evolution, or a built-in mechanism for keeping simulation-time signals in sync across concurrent environments. Where commonplace is stronger is epistemic discipline. We distinguish source, note, instruction, and review artifacts; we make links articulate relationships; and we validate structure deliberately. MiroShark mostly transforms a document into a useful simulation scaffold, then trusts the scaffold.

The deepest divergence is the representation contract. Commonplace tries to preserve and sharpen propositions so they can be revisited, re-linked, and maintained over time. MiroShark converts propositions into actor context and behavioral dynamics. That makes it a poor direct template for a KB, but a good nearby example of graph-backed context engineering for scenario execution.

## Borrowable Ideas

**Sliding-window history with mixed resolutions.** `RoundMemory` keeps ancient rounds as batched summaries, the previous round in full, and the current round as partial live state. That is a clean pattern for long-running agent workflows where some recent detail matters but the full trace does not fit. In commonplace this could become a workshop artifact or compaction helper for extended operations. *Needs a concrete workshop use case first.*

**Keep dynamic state symbolic when the update rule is inspectable.** MiroShark does not ask the LLM to remember each agent's stance implicitly; it stores trust, confidence, and exposure in explicit state and injects only the current summary. That separation is strong. When we have small state machines in commonplace, we should prefer explicit symbolic state over conversational drift. *Ready to borrow now as a design principle.*

**Shared-state bridges between concurrent contexts.** The `MarketMediaBridge` is a practical example of synchronizing partially independent agent loops without collapsing them into one giant prompt. A comparable commonplace pattern would be workshop components that publish compact state summaries to each other rather than sharing raw histories. *Needs a concrete multi-loop use case first.*

**Detailed report/action logs for post-hoc audit.** The report agent writes fine-grained JSONL logs of planning, tool calls, tool results, and section generation. For commonplace, similar logging around high-stakes maintenance or mutation workflows would make after-action review much easier. *Ready to borrow now where we already have multi-step automated workflows.*

**Derived graph layers can be valuable when they are clearly secondary.** MiroShark's graph is not a good primary knowledge substrate for us, but it is a strong example of a derived layer optimized for a specific operation. If commonplace ever needs scenario analysis, contradiction tracing, or neighborhood expansion over a subset of notes, a temporary or rebuildable graph view could earn its keep without replacing files. *Needs a use case first.*

## Curiosity Pass

**The graph step genuinely transforms the source, but only toward simulation-readiness.** The property claimed is richer grounding than prompting directly from the raw document. Mechanistically that is true: ontology generation, extraction, embedding, and indexing produce a new representation with different affordances. The simpler alternative would be "just chunk the document and retrieve passages." MiroShark's graph wins when the task really is actor generation plus relationship-aware reporting. It would be overkill for ordinary source analysis or KB curation.

**The persona layer is partly transformation and partly relocation.** The property claimed is realistic, richly grounded agents. Some of that is real transformation: graph facts and web-enrichment bullets are synthesized into platform-specific personas. But much of the value still comes from relocating source facts into prompt-shaped biographies. Even if this mechanism works perfectly, its ceiling is bounded by the extraction quality upstream. Weak ontology or NER output yields weak personas with more fluent prose, not deeper truth.

**The cross-platform bridge is the strongest mechanism in the repo.** The property is coupled dynamics rather than isolated toy simulations. The mechanism is concrete: shared market snapshots, shared sentiment summaries, and round-memory injection. The simpler alternative would be three separate simulations plus a summarizer that merges outputs afterward. MiroShark's design is better because interaction happens during execution, not only in analysis.

**Belief tracking is useful precisely because it is heuristic and bounded.** The property claimed is interpretable opinion drift. The mechanism does not infer beliefs from first principles; it applies visible update rules over stances, confidence, novelty, and trust. That is a good trade if the goal is controllable simulation rather than cognitive realism. The simpler alternative is no explicit belief model at all. MiroShark's version meaningfully improves traceability, but even perfect execution can only support lightweight directional judgments like convergence, polarization, or trust shifts.

**The repo's "universal" framing outruns some local assumptions.** The README calls MiroShark a universal engine, but several defaults are narrower than that slogan suggests. Time heuristics are explicitly framed around a China/Beijing daily schedule in `simulation_config_generator.py`; the Claude Code path still requires a separate LLM for CAMEL-driven simulation rounds; and web enrichment treats the LLM as a knowledge base unless a search-capable model is configured. None of these are fatal flaws, but they matter because they show the universal claim is mostly about provider flexibility, not about culture-free simulation dynamics or fully self-contained runtime design.

**Validation remains infrastructural rather than epistemic.** The property claimed is better simulation quality from structured extraction and retrieval. The mechanism includes config validation, ontology post-processing, NER cleanup rules, Neo4j schema creation, and test scripts for pipeline paths. That is real engineering. But the system has little governance around whether the extracted graph is actually faithful, whether personas misrepresent the source, or whether the report overclaims. The simpler alternative is a looser prototype with no checks at all, and MiroShark is clearly better than that. The ceiling, though, is a trustworthy simulator scaffold, not a trustworthy knowledge base.

## What to Watch

- Does the graph become a more durable first-class artifact, or remain a transient intermediate representation whose quality is judged only indirectly through simulation output?
- Do the hardcoded time/activity assumptions evolve beyond the current China-centered defaults into scenario-specific or locale-aware behavior?
- Does the report agent gain stronger evidence discipline, such as explicit provenance linking from report claims back to simulation events and graph facts?
- Does the belief model stay heuristic and inspectable, or drift toward more opaque prompt-only "memory" that is harder to reason about?
- Does the repo add stronger evaluation for extraction fidelity and simulation realism, or continue to rely mainly on end-to-end demos and pipeline scripts?

---

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — contrasts: MiroShark shows a legitimate database-backed design, but for a simulation substrate rather than a curated KB source of truth
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: MiroShark's round compaction, partial-history injection, and cross-platform summaries are all explicit responses to context pressure
- [LLM-mediated schedulers are a degraded variant of the clean model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — extends: MiroShark partially recovers the clean model by externalizing belief state, bridge state, and compacted history into code-managed structures
- [Inspectable substrate, not supervision, defeats the blackbox problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — parallels: the simulator remains reviewable because belief updates, bridge logic, and report tooling live in inspectable code rather than hidden prompt state
- [Quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md) — contrasts: MiroShark has structural and pipeline checks, but lacks the richer epistemic evaluation layer a durable KB would need
- [OpenSage](./OpenSage.md) — compares: both systems use Neo4j-backed agent environments, but OpenSage is an agent framework while MiroShark is a document-conditioned simulation pipeline
