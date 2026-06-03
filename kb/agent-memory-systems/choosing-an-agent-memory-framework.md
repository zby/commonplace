---
description: "Chooser-oriented guide to the reviewed agent-memory landscape, using matrix-backed axes to match systems by activation model, substrate, learning, and governance needs."
type: kb/types/note.md
traits: [has-comparison]
tags: [agent-memory]
status: current
---

# Choosing an agent memory framework starts with activation, not storage

The comparison matrix now has enough coverage to support a practical chooser lens. Across the code-reviewed systems, five fields are filled and varied enough to trust as first-pass filters: storage substrate, representational form, trace-derived status, read-back direction, and engineered push activation. The most useful first question is not "files or database?" but **how remembered material reaches the next action**.

Storage still matters, but it is a second-order constraint. A file-first system can be pull-only, coarse always-load, or engineered push. A database-backed system can be a deliberate lookup surface or an automatic prompt injector. The activation path decides whether the agent must remember to look, whether memory arrives generically, or whether the system selects relevant memory before the next action.

## The Three Chooser Questions

**1. Does memory need to arrive without agent initiative?** If not, prefer pull-first systems. Pull-only systems are easier to audit because memory enters action through explicit search, read, or restore calls. They fit workflows where the agent can be instructed to inspect memory at known moments, and where false negatives are acceptable.

If memory must arrive automatically, distinguish coarse push from instance-targeted push. Coarse push includes always-loaded profile blocks, recent notes, checkpoint state, or model weights. It is useful when the memory is small, globally relevant, or defines a persona or standing context. Instance-targeted push is the harder and more valuable case: the system selects memory for this user message, file, tool action, agent id, project, or task frame.

**2. Is the pushed memory selected by an identifier or inferred from content?** Identifier selection keys on a symbol the current instance already carries: project id, session id, path, type, tag, tool name, task id, report scope, agent id. It is deterministic and inspectable, but cannot anticipate an instance before the identifier exists. Inferred selection keys on the content itself: lexical match, embedding similarity, or LLM judgment. It can respond to an unstructured current message, but precision, recall, and context dilution become runtime questions rather than code-inspectable guarantees.

**3. Who will maintain the memory over time?** Trace-derived systems now dominate the reviewed set. That is a throughput advantage, not automatically a quality guarantee. Choose trace-derived systems when accumulation volume matters; choose authored or curated systems when lineage, reviewability, and deliberate promotion matter more than automatic capture.

## What The Mature Matrix Fields Say

The matrix is not yet a full product table. Most candidate columns remain empty by design. The stable columns still give a useful landscape:

- **Storage substrate:** files remain the largest group, but database and vector/graph systems are common enough that filesystem-first is no longer a landscape-wide convergence.
- **Representational form:** mixed artifacts dominate. Agent memory systems rarely use only prose, only symbols, or only model weights; they usually combine prose memories, metadata, embeddings, prompts, code, and indexes.
- **Trace-derived learning:** trace-derived systems are the majority, so the central question is no longer whether systems learn from traces but what authority the derived artifact gets.
- **Read-back direction:** both-direction systems are the largest group, followed by pull-only and push-only. Most serious frameworks expose explicit lookup while also wiring some automatic context path.
- **Push engineering:** engineered push is common. The important split is not push/no-push alone, but whether the push is coarse, identifier-targeted, or inferred from content.

## Matching System Shape To Use Case

**Choose pull-first, inspectable memory** when the agent works in a repo, terminal, or editor and can explicitly search or read memory as part of a known workflow. This favors systems whose value is durable storage, source visibility, and deliberate lookup rather than automatic context injection.

**Choose coarse push** when the remembered material is compact and globally relevant: profile state, recent working context, checkpoint summaries, active project state, or a learned model checkpoint. Coarse push is not useless; it is just not instance selection. It should stay bounded, because every action pays its context cost.

**Choose identifier-targeted push** when the workflow naturally emits stable symbols before action: project id, file path, tool name, task id, report definition, session id, agent id, or configured scope. This is the sweet spot for deterministic context engineering. It gives automatic activation without asking a semantic ranker to infer the situation from scratch.

**Choose inferred push** when the current user message or task text is the only reliable signal. CrewAI-style current-message retrieval and REM-style current-input retrieval are examples of this shape. They are better described as semantic push than symbolic anticipation: the system selects memory because it infers relevance from content, not because it had a prior instance identifier.

**Choose trace-derived systems** when memory volume would overwhelm manual capture. Then inspect the promotion path: does the trace become a note, fact, profile, rule, skill, validator, checkpoint, or model weight? The same source trace can become weak advisory context or high-authority system behavior.

**Choose curated file-first systems** when governance, review, diffability, and hand-edited structure matter. They are weaker at high-volume automatic capture but stronger when the retained artifact must be inspected, discussed, versioned, and retired.

**Choose database/vector/graph systems** when scale, multi-tenant access, temporal queries, relationship traversal, or low-latency semantic retrieval matter more than plain-file inspectability. The trade is operational complexity and reduced transparency of the exact memory object that shaped the next action.

## What Belongs In The README

The collection README should not become a giant comparison table. It should point readers to three entry points:

- the comparative review for the deeper theory of agency, link structure, curation, and temporal model;
- this chooser guide for first-pass system selection;
- the generated matrix for current counts and sortable backing data.

The README should also name the read-back distinction explicitly. The review framework treats shipped static documentation as baseline context, not memory read-back. That matters for readers choosing systems: a framework that auto-loads skills or manuals is not the same as one that retrieves retained memory for the current instance.

## Open Questions

- Should `read_back_targeting` and `read_back_signal` become extractable matrix fields now that the prose retrofit is complete?
- Should coarse engineered push and instance-targeted push both keep using `push-activation`, or should the tag split once the targeting field is extractable?
- Which chooser dimensions are still missing from the matrix: governance, access control, temporal model, deployment surface, or curation operations?

---

Relevant Notes:

- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) - compares-with: deeper architectural comparison whose agency-model thesis complements this chooser lens
- [trace-derived-learning-techniques-in-related-systems](./trace-derived-learning-techniques-in-related-systems.md) - see-also: focused survey of the trace-derived systems that now dominate the matrix
