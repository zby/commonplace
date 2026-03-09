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

Type: **practitioner-report** -- The author built a specific system (Personal Brain OS), used it daily, and describes what worked, what failed, and what he'd do differently. Includes concrete file counts, schema decisions, and measured outcomes (e.g., 40% token reduction from module splitting).

Domains: context-engineering, agent-architecture, knowledge-management, file-based-systems

Author: Muratcan Koylan (@koylanai), Context Engineer at Sully.ai (healthcare AI). His open-source Agent Skills work has 8,000+ GitHub stars and is cited in academic research alongside Anthropic. Previously built multi-agent systems handling 10,000+ weekly interactions at 99Ravens AI. Credible practitioner with production experience in the exact domain he's writing about.

## Summary

Koylanai describes "Personal Brain OS," a Git-repository-based personal operating system comprising 80+ files in Markdown, YAML, and JSONL that provide persistent context to AI coding assistants (Cursor, Claude Code). The core architectural insight is "progressive disclosure" -- a three-level loading system (routing file, module instructions, data files) that gives the model exactly what it needs per task and nothing more, avoiding attention budget waste. The system includes 11 isolated modules, an episodic memory system (experiences, decisions, failures as append-only JSONL), a skill system built on the Anthropic Agent Skills standard (auto-loading reference skills vs. manually invoked task skills), and automation chains for weekly reviews and content pipelines. The most important lessons: append-only formats are a safety mechanism (not just a convention), module boundaries are loading decisions that directly affect token efficiency, and voice/style is best encoded as structured data (numeric scales, banned word lists) rather than prose descriptions.

## Connections Found

The `/connect` discovery run found 9 new connections beyond the 6 already established in the KB. The source is one of the most densely connected practitioner reports in the sources collection, touching context efficiency theory, loading strategy, scoping, memory architecture, and writing-style constraint theory.

**Already established (6 connections linked from existing KB notes):**
- [files-not-database](../notes/files-not-database.md) -- exemplifies the files-over-database choice at 80+ file scale with format-function rationale
- [storing-llm-outputs-is-stabilization](../notes/storing-llm-outputs-is-stabilization.md) -- exemplifies append-only as safety mechanism (3-month data loss incident)
- [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) -- exemplifies all four action-oriented knowledge types without theoretical framing
- [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md) -- exemplifies graduated artifact loading across the verifiability gradient
- [stabilisation](../notes/stabilisation.md) -- exemplifies learning through versioned artifact accumulation
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) -- exemplifies Git-versioned files as inspectable substrate

**New connections found (9):**
1. [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **exemplifies**: the source's entire architecture is a response to context efficiency. The attention budget / lost-in-middle discussion addresses volume (1,200-line voice guide degradation, 40% token savings from module splitting), and module isolation addresses complexity (scoped rules prevent conflicting instructions). Provides practitioner evidence for the claim that context efficiency is a design-time concern.
2. [context-loading-strategy](../notes/context-loading-strategy.md) -- **exemplifies**: implements the exact loading hierarchy. SKILL.md = routing (always loaded), module instruction files = domain context (40-100 lines each), JSONL data = task-specific (loaded on demand). "Max two hops to any information" operationalizes the loading frequency principle.
3. [agent-statelessness-makes-routing-architectural-not-learned](../notes/agent-statelessness-makes-routing-architectural-not-learned.md) -- **exemplifies**: the three-layer instruction hierarchy (CLAUDE.md -> AGENT.md -> module files) is permanent routing architecture because the agent starts cold every session. The AGENT.md decision table is exactly the prosthetic the note describes.
4. [agents-md-should-be-organized-as-a-control-plane](../notes/agents-md-should-be-organized-as-a-control-plane.md) -- **exemplifies**: CLAUDE.md = invariants/onboarding, AGENT.md with decision table = routing, module-level files = task-specific constraints. The source explicitly notes this "solves the conflicting instructions problem."
5. [llm-context-is-composed-without-scoping](../notes/llm-context-is-composed-without-scoping.md) -- **exemplifies**: 11 isolated modules implement lexical scoping in practice. "The model never sees network data during a content task." The 40% token waste from merged identity+brand modules quantifies the cost of flat-context composition.
6. [directory-scoped-types-are-cheaper-than-global-types](../notes/directory-scoped-types-are-cheaper-than-global-types.md) -- **exemplifies**: "module boundaries are loading decisions" directly validates the economic argument. Each module has its own instruction file with domain-specific behavioral constraints. The 40% token savings from splitting modules is empirical evidence.
7. [three-space-agent-memory-maps-to-tulving-taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) -- **exemplifies**: the memory module maps onto Tulving's taxonomy without theoretical awareness. Knowledge = research/content/brand (semantic). Self = values, goals, voice, decisions, failures (episodic). Operations = todos, pipeline state, weekly reviews (procedural). Demonstrates three-space separation emerging from practitioner needs.
8. [writing-styles-are-strategies-for-managing-underspecification](../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- **exemplifies**: the voice system demonstrates prescriptive style (numeric 1-10 scales on five attributes), prohibitive style (50+ tiered banned words), and conditional style (four-pass editing with branching quality gates). Practitioner case for the claim that style choice encodes autonomy allocation.
9. [agent-skills-for-context-engineering](../notes/related-systems/agent-skills-for-context-engineering.md) -- **extends**: same author. Personal Brain OS is the concrete implementation from which the Agent Skills framework was distilled. The relationship is implementation-to-methodology.

**Synthesis opportunities flagged by /connect:**
- Practitioner convergence on three-level progressive disclosure as a universal pattern (Koylanai, Ars Contexta, ClawVault, commonplace all arrive at routing -> domain -> data independently)
- Module boundaries simultaneously serve scoping, loading, and type boundary functions (unifies llm-context-is-composed-without-scoping, directory-scoped-types, and this source)

## Extractable Value

1. **Context efficiency as design-time architectural driver, not runtime optimization.** The source independently validates the theoretical position in context-efficiency-is-the-central-design-concern with concrete data: 40% token savings from module splitting, voice guide degradation from lost-in-middle at 1,200 lines. These data points are not yet cited in the theory note. [quick-win]

2. **Module isolation as practical scoping for LLMs.** "The model never sees network data during a content task" is a one-sentence practitioner formulation of the scoping problem described in llm-context-is-composed-without-scoping. The 40% waste from merging identity+brand is evidence that flat-context composition has measurable cost. Not yet cited in the theory note. [quick-win]

3. **Three-space memory emerging without theory.** The source's memory module (knowledge/self/operations) maps onto Tulving's taxonomy without the author knowing the framework. This is practitioner convergence evidence for three-space-agent-memory-maps-to-tulving-taxonomy. [quick-win]

4. **Four-system convergence on three-level progressive disclosure.** Koylanai, Ars Contexta, ClawVault, and commonplace all independently arrived at a three-level loading architecture. A synthesis note could argue this convergence is not coincidence but a consequence of bounded context -- any system under context constraints converges on routing -> domain -> data. [deep-dive]

5. **Module boundaries unify scoping, loading, and type functions.** Three KB notes approach the same insight from different angles (scoping theory, type economics, practitioner module isolation). A synthesis note could unify them with this source as the empirical anchor. [deep-dive]

6. **Voice encoding as structured constraints vs. prose descriptions.** The source's numeric scales (1-10 on five attributes) and tiered banned word lists demonstrate prescriptive and prohibitive style strategies from writing-styles-are-strategies-for-managing-underspecification. The voice system is a practitioner case study for the theory. [just-a-reference]

7. **Missing related-system review.** Given the density of connections (15 total), a dedicated related-system review note in kb/notes/related-systems/ would be warranted. It would sit alongside Agent Skills (same author) and provide the most concrete empirical data points in the related-systems collection. [experiment]

## Recommended Next Action

Write a related-system review note titled "personal-brain-os.md" in `kb/notes/related-systems/`, linking to `agent-skills-for-context-engineering.md` (same author, theory-to-implementation relationship). This source has 15 connections to existing KB notes -- more than any other practitioner report -- and provides concrete empirical data points (40% token savings, 3-month data loss, 1,200-line degradation threshold) that strengthen multiple theoretical positions. The related-system review format would capture these connections structurally and make them navigable, whereas the ingest report leaves them as unlinked observations.
