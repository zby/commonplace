---
description: "Practitioner report on a PM skill that forces solution ideas back into problem statements, useful as a process-structure example for agent skills"
source_snapshot: "kb/sources/problem-first-skill-inverts-solution-jumps-2063186118409929161.md"
ingested: "2026-06-17"
type: kb/sources/types/ingest-report.md
domains: [skills, process-structure, product-management]
---

# Ingest: /problem-first: a simple skill to invert bad ideas

Source: [problem-first-skill-inverts-solution-jumps-2063186118409929161.md](problem-first-skill-inverts-solution-jumps-2063186118409929161.md)
Captured: 2026-06-17T09:08:07.099475+00:00
From: https://x.com/nurijanian/status/2063186118409929161

## Classification

Type: practitioner-report -- the author reports a product-management workflow they use as an AI skill, including an anecdotal run over roughly 50 ideas and a productized placement inside PM OS.
Domains: skills, process-structure, product-management
Author: @nurijanian presents as a PM practitioner and PM OS vendor; the source has firsthand workflow detail, but also promotional bias.

## Summary

The post describes `problem-first`, a product-management skill that treats a proposed solution as a compressed signal of an unarticulated problem, then expands it into underlying problem statements, assumption challenges, alternative framings, validation tests, and a stakeholder message. The author argues that this works better than telling a team to stop and restart discovery because existing roadmaps carry political momentum. The same skill can run in reverse for idea triage: feed an idea in, extract the problem it is supposed to solve, and discard ideas with no evidence status. For Commonplace, the useful part is not PM doctrine itself but the example of a lightweight AI skill whose value comes from forcing skipped reasoning moves under time pressure.

## Connections Found

The companion connect report, [problem-first-skill-inverts-solution-jumps-2063186118409929161.connect.md](../reports/connect/sources/problem-first-skill-inverts-solution-jumps-2063186118409929161.connect.md), found four strong connections. The source is evidence for [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md) because the skill's reported value comes from mandatory reasoning sections, especially assumption challenges, alternative framings, and a draft message. It also supports [Skills are instructions plus routing and execution policy](../notes/skills-are-instructions-plus-routing-and-execution-policy.md), [Skills derive from methodology through distillation](../notes/skills-derive-from-methodology.md), and [Methodology enforcement is constraining](../notes/methodology-enforcement-is-constraining.md) by showing a domain reasoning practice packaged as a user-invoked skill that makes a protocol run consistently. Weaker matches to typed callables, instruction testing, frontloading, and agent-memory-system coverage were rejected as too indirect.

## Extractable Value

1. **Practitioner example for process structure outside code/math benchmarks** -- Existing process-structure evidence in the KB leans on reasoning papers and coding-agent ingests; this source adds a product-judgment example where explicit sections change what reasoning happens, not merely what the output looks like. [quick-win]
2. **Skill value framed as anti-skipping under pressure** -- The post names the mechanism in operational terms: humans can do the work, but under time pressure they skip the sections that prevent premature commitment. That sharpens the KB's skill discussion from "procedures are reusable" to "procedures preserve high-friction reasoning steps when the operator is tempted to omit them." [quick-win]
3. **Domain-practice-to-skill distillation example** -- `problem-first` appears to distill PM discovery practice directly into a skill without an intermediate theory note. That is useful for the caveat in [Skills derive from methodology through distillation](../notes/skills-derive-from-methodology.md), which already distinguishes methodology-sourced skills from artifact- or domain-sourced skills. [quick-win]
4. **Idea triage as bottleneck selection, not idea generation** -- The reverse use case claims that the constraint is triage capacity: deciding which ideas have real problems underneath. For Commonplace, this is a transferable warning about agent skill design: automate the scarce judgment step rather than the most visible production step. [experiment]
5. **Promotional skill-system signal, not system evidence** -- PM OS is mentioned as a broader skill operating layer over company context files across Claude Code, Cowork, and Cursor, but the source does not expose implementation details. It is useful as a reference for market convergence around skill packaging, not as evidence for agent-memory architecture. [just-a-reference]

## Limitations (our opinion)

This is a single promotional practitioner report, not a controlled evaluation. The claim that 90% of roughly 50 ideas died at evidence status is useful as anecdote, but it does not establish that the skill improves product outcomes or that the eight-section template is the causal factor. The post also does not show the actual prompt, outputs, failure cases, or how company context is loaded, so it should not be treated as evidence for PM OS architecture or memory design. Its best use is narrow: a concrete example that process structure can preserve reasoning steps that people predictably skip.

## Recommended Next Action

Update [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md) with a short practitioner-example paragraph citing this source: `problem-first` shows process structure helping outside benchmarked code/math tasks by forcing assumption challenges, alternative framings, and stakeholder messaging before a team commits to a solution-shaped roadmap item.
