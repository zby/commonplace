---
source_snapshot: koylanai-personal-brain-os.md
ingested: 2026-03-09
type: practitioner-report
domains: [context-engineering, agent-architecture, knowledge-management, file-based-systems]
---

# Ingest: The File System Is the New Database: How I Built a Personal OS for AI Agents

Source: [koylanai-personal-brain-os.md](./koylanai-personal-brain-os.md)
Captured: 2026-02-22
From: https://x.com/koylanai/status/2025286163641118915

## Classification

Type: **practitioner-report** -- A first-person account of a system the author says he built and used. It includes concrete claimed file counts, schema decisions, and performance anecdotes, but all of the evidence comes through the author's own writeup rather than direct inspection.

Domains: context-engineering, agent-architecture, knowledge-management, file-based-systems

Author: Muratcan Koylan (@koylanai), Context Engineer at Sully.ai and author of the Agent Skills project. This makes the piece worth reading as practitioner testimony, but it remains self-reported evidence from an X article rather than a directly inspectable system artifact.

## Summary

Koylan reports building "Personal Brain OS," a Git-repository-based personal operating system comprising, by his account, 80+ files in Markdown, YAML, and JSONL that provide persistent context to AI coding assistants. The core idea he presents is "progressive disclosure" -- a three-level loading system (routing file, module instructions, data files) intended to give the model only task-relevant context. He also describes 11 isolated modules, append-only episodic memory logs, Anthropic-style agent skills, and automation chains for weekly reviews and content pipelines. The useful value here is not a verified system design but a compact practitioner narrative arguing that append-only formats, scoped modules, and structured voice constraints improved his own setup.

## Connections Found

The `/connect` discovery run found 9 new connections beyond the 6 already established in the KB. The source touches context efficiency theory, loading strategy, scoping, memory architecture, and writing-style constraint theory. Those connections are useful as hypothesis links, but they should be read through the source's evidence class: an authorial report, not an inspected implementation.

**Already established (6 connections linked from existing KB notes):**
- [files-not-database](../notes/files-not-database.md) -- exemplifies the files-over-database choice at 80+ file scale with format-function rationale
- [storing-llm-outputs-is-constraining](../notes/storing-llm-outputs-is-constraining.md) -- exemplifies append-only as safety mechanism (3-month data loss incident)
- [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) -- exemplifies all four action-oriented knowledge types without theoretical framing
- [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md) -- exemplifies graduated artifact loading across the verifiability gradient
- [constraining](../notes/constraining.md) -- exemplifies learning through versioned artifact accumulation
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) -- exemplifies Git-versioned files as inspectable substrate

**New connections found (9):**
1. [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **exemplifies (anecdotally)**: the author frames the whole architecture as a response to context efficiency, citing claimed volume effects like a 1,200-line voice-guide degradation threshold and 40% token savings from module splitting.
2. [context-loading-strategy](../notes/context-loading-strategy.md) -- **exemplifies (by self-report)**: the described three-level loading hierarchy matches the routing -> module -> data pattern already present in the KB.
3. [agent-statelessness-makes-routing-architectural-not-learned](../notes/agent-statelessness-makes-routing-architectural-not-learned.md) -- **exemplifies (if the description is accurate)**: the reported instruction hierarchy (CLAUDE.md -> AGENT.md -> module files) is a practitioner version of routing as fixed architecture.
4. [agents-md-should-be-organized-as-a-control-plane](../notes/agents-md-should-be-organized-as-a-control-plane.md) -- **exemplifies (by described structure)**: the source presents repo-level onboarding, a decision-table layer, and module-local constraints as separate control surfaces.
5. [llm-context-is-composed-without-scoping](../notes/llm-context-is-composed-without-scoping.md) -- **exemplifies (anecdotally)**: the reported module isolation and "never sees network data during a content task" language is a compact practitioner statement of the scoping problem.
6. [directory-scoped-types-are-cheaper-than-global-types](../notes/directory-scoped-types-are-cheaper-than-global-types.md) -- **exemplifies (suggestively)**: the source treats module boundaries as loading decisions with local instruction files, which points in the same direction as the note's economic argument.
7. [three-space-agent-memory-maps-to-tulving-taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) -- **exemplifies (suggestively)**: the author's described split between research/content, values/decisions/failures, and operational task state resembles the semantic / episodic / procedural separation.
8. [writing-styles-are-strategies-for-managing-underspecification](../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- **exemplifies (anecdotally)**: the reported voice system uses numeric scales, banned-word lists, and editing passes as structured style constraints.
9. [agent-skills-for-context-engineering](../notes/related-systems/agent-skills-for-context-engineering.md) -- **extends**: same author. The article can be read as implementation-side anecdotal evidence adjacent to the Agent Skills methodology, but not as a deeply observed system review.

**Synthesis opportunities flagged by /connect:**
- Practitioner convergence on three-level progressive disclosure as a universal pattern (Koylanai, Ars Contexta, ClawVault, commonplace all arrive at routing -> domain -> data independently)
- Module boundaries simultaneously serve scoping, loading, and type boundary functions (unifies llm-context-is-composed-without-scoping, directory-scoped-types, and this source)

## Extractable Value

1. **Context efficiency as design-time architectural driver, not runtime optimization.** The source offers anecdotal practitioner support for the theory note, including claimed 40% token savings from module splitting and a reported voice-guide degradation threshold around 1,200 lines. These data points are worth citing as practitioner testimony, not as verified benchmark results. [quick-win]

2. **Module isolation as practical scoping for LLMs.** "The model never sees network data during a content task" is a compact practitioner formulation of the scoping problem described in llm-context-is-composed-without-scoping. The reported waste from merged modules is useful as anecdotal evidence that flat-context composition has operational cost. [quick-win]

3. **Three-space memory emerging without theory.** The source's described memory split (knowledge/self/operations) loosely maps onto Tulving's taxonomy. This is useful as convergence evidence, but only at the level of reported design narrative. [quick-win]

4. **Four-system convergence on three-level progressive disclosure.** If Koylanai's account is taken at face value, it joins Ars Contexta, ClawVault, and commonplace in arriving at a three-level loading architecture. That makes it useful as a convergence signal, but weaker than systems we have inspected more directly. [deep-dive]

5. **Module boundaries unify scoping, loading, and type functions.** Three KB notes approach the same insight from different angles (scoping theory, type economics, practitioner module isolation). This source is better used as a suggestive practitioner anecdote than as the empirical anchor for that synthesis. [deep-dive]

6. **Voice encoding as structured constraints vs. prose descriptions.** The reported numeric scales and banned-word lists provide a compact practitioner example of prescriptive and prohibitive style strategies. [just-a-reference]

7. **Claim-strength audit needed before reuse.** Because this source is dense with potentially useful claims but thin in evidence, the immediate value is auditing downstream notes to ensure they cite it as anecdotal practitioner evidence rather than as a deeply verified system reference. [quick-win]

## Limitations (our opinion)

- **Self-report only.** We have a snapshot of an X article, not the repository, file tree, prompts, or logs of the underlying system. Every architectural detail in this report is filtered through the author's own description.
- **Sample size of one.** Even if the reported numbers are accurate, they come from one person's workflow, tools, and evaluation criteria. Transfer to other domains or teams is untested.
- **Metrics are not independently checkable.** Claims like 40% token reduction, 1,200-line degradation, and the 3-month data-loss incident are plausible and useful, but they are not backed here by artifacts we can inspect.
- **Author credibility does not remove observability limits.** The author may be a credible practitioner, but credibility only raises the prior that the report is worth reading; it does not turn the article into the equivalent of a scientific report or repo review.

## Recommended Next Action

File as reference and downgrade downstream claim strength where needed. Keep using this source as anecdotal practitioner evidence for scoped loading, append-only logs, and structured voice constraints, but do not promote it into a full related-system review unless we obtain direct repo/docs coverage or another higher-signal primary source.
