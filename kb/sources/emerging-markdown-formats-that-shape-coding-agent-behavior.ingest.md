---
description: "Practitioner taxonomy separating standing rules, task procedures, reviewed plans, domain context, and machine-local memory in agent-ready repositories"
source: https://generativeprogrammer.com/p/emerging-markdown-formats-that-shape
captured: "2026-08-03"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: fadeacc09687cc0e898e54a8821f72fa50650c88970e6a5aa87e525a711880e9
ingested: "2026-08-03"
type: kb/sources/types/ingest-report.md
domains: [agent-instructions, context-engineering, document-systems, agent-memory]
---

# Ingest: Emerging Markdown Formats That Shape Coding Agent Behavior

## Classification

A practitioner synthesis that organizes current agent-facing Markdown conventions and proposes a unifying “metacode” frame, without a study, implementation evaluation, or formal argument that the formats improve outcomes.
Author: Bilgin Ibryam. The essay cites first-party specifications and product documentation for the formats it inventories, which supports point-in-time factual orientation; the cross-format taxonomy and “intent compiler” conclusion remain the author's synthesis.

## Summary

The essay argues that an agent-ready repository should hold not only implementation but also the project knowledge an agent needs to change that implementation correctly. It separates five roles: standing repository rules in `AGENTS.md` and vendor-native equivalents; repeatable procedures in `SKILL.md`; reviewable requirements, plans, and tasks in versioned planning files; specialized domain context in files such as `ARCHITECTURE.md`, `DESIGN.md`, `AUTH.md`, and `REVIEW.md`; and agent-written, machine-local memory that should be promoted into shared artifacts only after human review. It recommends the smallest reliably discoverable set, one canonical source with thin vendor-specific bridges, and scoped, reviewed, current files. Its broad conclusion is that this Markdown “metacode” lets an agent compile human intent into source code.

## Connections Found

The source is best treated as a dated practitioner map over distinctions the KB already explains more precisely. Its standing-file, on-demand-skill, and local-memory inventory corroborates [Always-loaded context mechanisms in agent harnesses](../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), while its one-canonical-file plus thin-bridge advice is a practical instance of [Keep Lineage And Compiled Views From Drifting](../notes/agent-memory-requirements/keep-compiled-views-aligned.md). The local observation → human review → shared rule, skill, ADR, or domain document path supplies a concrete example for [Promote Only When Future Value Exceeds Maintenance Cost](../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md), but the KB adds the missing validity, authority, lineage, maintenance, and activation gates. [Context Engineering for AI Agents in Open-Source Software](./context-engineering-ai-agents-oss.ingest.md) is the empirical breadth companion for context-file adoption and evolution; [Harness Engineering](./harness-engineering-leveraging-codex-agent-first-world.ingest.md) is the stronger production example of a short agent-facing map pointing to deeper repository sources; and [The What & When of Self-Evolving Agents](./the-what-and-when-of-self-evolving-agents.ingest.md) separates substrate from persistence horizon where this essay groups both under “metacode.”

## Extractable Value

1. **A usable role taxonomy for agent-facing repository documents** -- Separating standing context, task-invoked procedure, reviewed plan, domain-specific context, and tentative local memory is a compact routing aid. It is less precise than the KB's authority and lifecycle axes, but it is easy to explain and immediately useful when deciding where new project knowledge belongs. [quick-win]

2. **A concrete promotion path from private observation to shared behavioral authority** -- The essay proposes that an agent first records a tentative machine-local observation, then a human reviews it when recurrence or shared impact makes it relevant, and only then promotes it into a rule, skill, ADR, or domain document. This operationalizes the candidate-versus-durable distinction, provided recurrence is treated as a trigger for review rather than as proof. [quick-win]

3. **Canonical source plus thin compatibility bridges** -- The advice to choose one canonical file and keep vendor-native files as thin bridges is a portable source-of-truth rule for multi-harness repositories. The higher-reach version needs explicit derivation, regeneration, and freshness checks so a “thin bridge” does not silently become an independent policy. [quick-win]

4. **Authorship and sharing are independent of repository association** -- Claude's auto memory is associated with a repository but normally machine-local and agent-written, whereas project instruction files are shared and human-governed. This is a clean example of why storage location, author, sharing scope, and authority must be recorded separately. [just-a-reference]

5. **Versioned planning files make design reviewable without making it permanent knowledge** -- Moving requirements, plans, and tasks out of chat creates inspectable handoff artifacts, but their lifecycle remains work-in-flight. Comparing the essay's single “metacode” layer with [A functioning knowledge base needs a workshop layer, not just a library](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) sharpens the distinction between reviewability and durability. [deep-dive]

6. **A point-in-time maturity map of agent Markdown conventions** -- The essay distinguishes cross-tool standards, vendor conventions, long-standing human documentation, and experimental domain files. This is useful orientation for August 2026, but its product support and popularity claims should be rechecked before operational use. [just-a-reference]

## Limitations (our opinion)

The essay catalogs formats and plausible roles but does not test whether agents discover them, load the right one, follow it, or improve task outcomes. A file being present and nominally supported is therefore not evidence that it shapes behavior. [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) supplies the missing boundary: discoverability, context presence, and behavior change are separate claims.

“Metacode” is also broader than the mechanism warrants. The category combines knowledge artifacts, behavior-shaping system-definition artifacts, temporary plans, specifications, and private memory because they share a file format and repository-adjacent use. But Markdown and placement do not determine behavioral authority; a document becomes operative only through a named loading, routing, validation, or execution path. Likewise, calling the agent an “intent compiler” hides interpretation and verification: natural-language intent is underspecified, and generated source is not proven faithful merely because both inputs and outputs are versioned.

The proposed memory-promotion loop is directionally sound but underspecified. Recurrence or impact can trigger review, yet it does not verify a diagnosis, establish a generalization boundary, resolve conflicting observations, or justify the maintenance cost of a standing rule. [Trace-extracted memory earns authority per operation, not at capture](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) is the stronger model for those steps. Finally, the ecosystem examples and support claims are a dated selection from a fast-moving field; the essay offers neither a systematic sampling method nor evidence that the chosen formats are representative.

## Recommended Next Action

Update [Promote Only When Future Value Exceeds Maintenance Cost](../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) with this snapshot as `evidenced-by`, using the local-observation → human-review → shared rule/skill/ADR example while stating that recurrence triggers evaluation rather than granting validity or authority.
