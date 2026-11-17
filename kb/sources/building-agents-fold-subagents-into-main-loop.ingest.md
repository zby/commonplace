---
description: "Anthropic practitioner guidance on merging context-coupled subagents into one loop, with repeated task-level evaluations to detect regressions rather than a universal agent-count rule."
source: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
captured: "2026-10-24"
capture: trafilatura
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: b48cc4467467b986b319e8594c26946e678c18124cbba3e59da119036b8b3baa
ingested: "2026-11-17"
type: types/ingest-report.md
domains: [subagent-consolidation, progressive-disclosure, architecture-evaluation]
---

# Ingest: Building agents: When to fold subagents into your main agent loop

## Classification

A practitioner report combining enterprise deployment observations, migration advice, and promotion of an accompanying migration kit. Author: Diane Sarkis, writing on Anthropic's site and reporting experience from its Applied AI team. This provides proximity to deployment decisions, but not independent evaluation of the vendor's architectural recommendations.

## Summary

The article recommends testing whether routers, planners, and domain subagents can become skills and tools within one model's main loop. Its proposed mechanism is preserving cross-step information while loading instructions and tool definitions only when needed, rather than exchanging lossy specialist summaries. It reports that a single agent with skills frequently beat both monolithic-prompt and subagent designs in selected enterprise comparisons; one customer's single-loop runtime was roughly twice as fast. The article summarizes deployment comparisons without supplying enough detail to isolate the cause of the reported gains. The migration procedure is more reusable than the reported gains: merge context-coupled specialists one at a time, cover production chains and mandatory rules with repeated end-to-end evaluations, and inspect individual tasks that change outcome. Separate agents remain appropriate for verification, disposable parallel work, measured context degradation, and tool-selection or instruction conflicts. The proposed simplification moves planning and domain procedure into the model's loop while retaining hard limits, permissions, and validation in the harness or tools.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source supplies bounded practitioner support for [Decomposition heuristics for bounded-context scheduling](../theory/decomposition-heuristics-for-bounded-context-scheduling.md). That note weighs orchestration overhead against preserved interactions and leaves detecting the stopping point unresolved. The article contributes a practical test candidate: merge frequently co-used specialists sharing data, then compare task-level outcomes and cost. It does not validate all the note's heuristics or establish a stopping threshold. In particular, its recommendation to remove some routing code should not be equated with the note's preference for symbolic operations where exactness is available.

It also supplies a concrete warning relevant to [Operational signals that a component is a relaxing candidate](../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md): a support-agent merge reduced latency but intermittently bypassed the shipping specialist needed to obtain a delivery date. This supports testing changes in integration rather than accepting aggregate improvement. It does not show that the removed boundary was intrinsically wrong, or that mandatory process requirements can safely be discarded.

## Extractable Value

1. **A candidate test for excessive decomposition.** Start with specialists that share data or consume one another's outputs; fold one boundary into skills and tools, then compare repeated end-to-end outcomes, latency, and cost. This operationalizes the decomposition note's open stopping question without claiming a universal threshold. The source's deployment gains do not isolate boundary removal from accompanying prompt, tool, or model choices. [experiment]
2. **Task-level regression inspection as a migration gate.** Cover each production agent chain and each mandatory rule, repeat runs, and inspect tasks whose outcomes flip rather than relying only on the final score. The shipping example shows why a faster merged loop can still lose a required dependency; the reported one-in-two occurrence illustrates intermittency, not an estimated failure rate. [quick-win]
3. **Separate team ownership from execution boundaries.** Teams can own skills, tools, and their tests while a central team owns the system prompt and end-to-end quality. This is a reusable organizational alternative to assigning every team its own agent, but the article provides advice rather than a controlled comparison of ownership arrangements. Here a skill means retrievable procedural instructions, not an independently executing worker. [just-a-reference]

## Limitations (our opinion)

The enterprise comparisons lack task sets, sample sizes, model configurations, scoring details, uncertainty estimates, and full failed-migration histories. Vendor selection and unreported deployment conditions may explain part of the favorable pattern. The roughly twofold runtime improvement is one customer's observation, not a portable estimate.

The proposed comparison changes the execution boundary: specialist prompts become skills, API calls become tools, and intermediate results stay in the main context. The article does not establish which tool interfaces, prompts, budgets, models, or evaluation tasks were held fixed in the reported deployments. It therefore cannot distinguish gains from shared context, fewer model calls, better instructions, or other implementation changes. Nor does it compare all plausible alternative decompositions. Its model-generation claims and numerical tool-count guidance should remain deployment-specific advice, not general design limits.

Progressive disclosure limits what is loaded initially; it does not by itself prevent interference among instructions once loaded or guarantee that a long-running main context remains manageable. The source explicitly preserves reasons to use separate contexts, including verification and parallel work. Its closing preference for keeping a subagent only when folding scores worse must be read alongside those exceptions, permission requirements, and mandatory-rule checks—not as permission to optimize a single quality score at their expense. No implementation or migration-kit execution was examined for this report.

## Recommended Next Action

Update the open stopping-condition discussion in [Decomposition heuristics for bounded-context scheduling](../theory/decomposition-heuristics-for-bounded-context-scheduling.md) with the article's fold-one-boundary, repeated task-level comparison as an unvalidated practitioner test candidate, retaining mandatory-rule and separate-context exceptions.
