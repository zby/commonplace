---
description: First empirical study of AI context files across 466 OSS projects — provides naturalistic data on content categories, five writing styles as constraint strategies, add-then-modify evolution pattern, and 50% stagnation rate that grounds and challenges KB constraining theory
source_snapshot: context-engineering-ai-agents-oss.md
ingested: 2026-03-09
type: scientific-paper
domains: [context-engineering, agentic-systems, open-source, software-artifacts]
---

# Ingest: Context Engineering for AI Agents in Open-Source Software

Source: context-engineering-ai-agents-oss.md
Captured: 2026-03-02
From: https://arxiv.org/pdf/2510.21413

## Classification

Type: scientific-paper — Peer-reviewed MSR 2026 paper with structured methodology (mining 10,000 GitHub repos, qualitative coding of 155 AGENTS.md files, commit-level evolution analysis of 169 commits), three formal research questions, and replication package.

Domains: context-engineering, agentic-systems, open-source, software-artifacts

Author: Mohsenimofidi, Galster, Treude, Baltes — mixed SE/MSR team. Treude and Baltes are established mining software repositories researchers; Galster has a software architecture background. The combination gives credibility on both the empirical methodology and the software engineering framing.

## Summary

This paper presents the first systematic empirical study of AI context files (AGENTS.md, CLAUDE.md, copilot-instructions.md, GEMINI.md) across 466 open-source projects drawn from a curated sample of 10,000 GitHub repositories. Adoption is still early (5% of sampled repos). The authors find no established content structure, but recurring categories emerge: conventions (50 repos), contribution guidelines (48), architecture/structure (47), and build commands (40) are most common. They identify five writing styles — descriptive, prescriptive, prohibitive, explanatory, and conditional — reflecting experimentation with how to communicate expectations to AI agents. Commit-level analysis of the 10 most actively maintained AGENTS.md files (169 commits) shows evolution dominated by adding and modifying instructions, with rare section removal. Fifty percent of all AGENTS.md files were never changed after creation. The paper argues that AI context files are "maintained software artifacts" and that OSS repositories are natural laboratories for studying real-world context engineering.

## Connections Found

The `/connect` run (2026-03-09) found 4 existing links and 9 new connections. This source sits squarely in the KB's core territory — it provides empirical grounding for multiple theoretical claims.

**Already linked** (4 notes + 2 indexes):
- [writing-styles-are-strategies-for-managing-underspecification](../notes/writing-styles-are-strategies-for-managing-underspecification.md) — grounds: the paper is the primary source; note was derived from the paper's five-style taxonomy
- [human-llm-differences-are-load-bearing](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — validates: paper explicitly contrasts README-for-humans vs context-file-for-agents at empirical scale
- [tags](../notes/tags-index.md) — validates: listed in Reference material; provides empirical grounding for context-loading categories
- [learning-theory](../notes/learning-theory-index.md) — validates: listed in Reference material; commit-level evolution confirms continuous learning through versioned artifacts

**New connections identified** (9):
1. [methodology-enforcement-is-constraining](../notes/methodology-enforcement-is-constraining.md) — **validates**: RQ3 evolution data (Add 78, Modify 59, Remove 23, Remove section 2) confirms the maturation trajectory from underspecified guidance to refined instructions. The rsyslog commit removing a stylecheck instruction is a concrete constraining exemplar.
2. [deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md) — **validates**: the paper's conclusion that AI context files are "maintained software artifacts" that are "versioned, reviewed, quality-assured, and tested" is the deploy-time learning thesis stated as an empirical finding.
3. [constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md) — **validates**: 169 annotated commits showing add-then-modify dominance is continuous learning through versioned artifacts in the wild. The 50% stagnation finding (77/155 never changed) is an interesting counterpoint — half of all context files lack a maintenance practice that would enable continuous learning.
4. [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) — **exemplifies**: the five writing styles are empirically observed strategies for managing the interpretation space the note theorizes. Prescriptive narrows maximally, descriptive leaves interpretation wide, conditional partitions the space.
5. [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **validates**: average AGENTS.md is 142 lines (SD=231), Copilot instructions 310 lines — teams are experimenting with what fits in the attention budget.
6. [agents-md-should-be-organized-as-a-control-plane](../notes/agents-md-should-be-organized-as-a-control-plane.md) — **validates**: Table 1 categories show the unstructured landscape without a normative model — "no established content structure yet."
7. [instruction-specificity-should-match-loading-frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — **validates**: practitioners independently arrive at the slim-router pattern; the 14 content categories map onto what should be routed to, not embedded in, always-loaded context.
8. [programming-practices-apply-to-prompting](../notes/programming-practices-apply-to-prompting.md) — **validates**: version control, code review, and testing applied to context files at scale across 466 projects.
9. [legal-drafting-solves-the-same-problem-as-context-engineering](../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) — **complements**: the five writing styles are an independent taxonomy that overlaps with the legal constraint strategies (defined terms, enumeration, canons of interpretation).

**Source-to-source**: [harness-engineering-leveraging-codex-agent-first-world](../sources/harness-engineering-leveraging-codex-agent-first-world.md) complements as depth vs breadth on the same phenomenon — one practitioner team's deliberate approach alongside the empirical survey of 466 projects.

**Synthesis opportunities** flagged by /connect:
1. Context file evolution follows a growth-then-refinement pattern with a stagnation risk — combining the paper's 50% stagnation data with the methodology-enforcement maturation trajectory creates a testable prediction.
2. The five writing styles plus loading tier form a 2D design space for context file instructions — the writing-styles note maps styles to autonomy, instruction-specificity-should-match-loading-frequency maps content to loading frequency; combining them makes the design space explicit.

## Extractable Value

1. **The 50% stagnation finding as a challenge to constraining theory.** 77 of 155 AGENTS.md files were never changed. This is not just "early adoption" — it suggests many teams create context files without a feedback loop that would enable constraining. The KB's constraining model assumes iterative refinement occurs; this data shows it often doesn't. Worth investigating what distinguishes evolving from stagnant files. [deep-dive]

2. **Evolution pattern quantified: growth dominates pruning.** Add (78) and Modify (59) dwarf Remove (23) and Remove-section (2). Context files grow and refine but rarely shrink. This challenges any assumption that constraining naturally prunes instructions and suggests active pruning is a discipline, not an emergent behavior. The methodology-enforcement note should acknowledge this empirical asymmetry. [quick-win]

3. **Co-evolution of source code and context files as a research direction.** The paper flags this as an open question, analogous to code-comment co-evolution. Our KB has no note on this yet. When instructions and implementation drift apart, agent behavior degrades — this is a concrete failure mode for deploy-time learning systems. [experiment]

4. **Content category frequency as evidence for control-plane prioritization.** Table 1's ranked categories (conventions 50, contribution guidelines 48, architecture 47, build commands 40) are empirical evidence for what practitioners prioritize. The agents-md-control-plane note's three-layer model (invariants, routing, escalation) could be validated or refined against this frequency data. [just-a-reference]

5. **Tool-language correlations as a signal.** C# strongly favors Copilot, TypeScript favors Claude Code. This is a weak signal but suggests tool-specific ecosystems may develop different context engineering practices. [just-a-reference]

## Limitations (our opinion)

**What was not tested:**

- **No measurement of agent behavior.** The paper studies what developers *write* in context files, not whether those instructions actually change agent output quality. The entire study is on the input side — there is no dependent variable measuring effectiveness. The authors acknowledge this as future work, but it means the paper cannot tell us whether any particular content category or writing style actually works.

- **Selection bias toward active, popular projects.** The 10,000-repo sample uses a ranking that balances popularity and maturity, which excludes small/new projects and over-represents well-maintained ones. The 5% adoption rate may be higher in this elite sample than in the general population — or lower than in cutting-edge teams not yet captured by the sampling window (October 2025). The paper acknowledges this.

- **No analysis of multi-file context strategies.** The paper treats each context file as an independent artifact. It does not study how AGENTS.md interacts with CLAUDE.md or copilot-instructions.md within the same repo. The 25 repos with both AGENTS.md and CLAUDE.md are noted but not analyzed for content overlap or complementarity. This matters because the KB's [instruction-specificity-should-match-loading-frequency](../notes/instruction-specificity-should-match-loading-frequency.md) note argues for a multi-tier loading architecture — the paper provides no data on whether practitioners already do this.

- **Evolution analysis limited to 10 files.** The commit-level analysis (169 commits) covers only the 10 most actively maintained AGENTS.md files — the top 6% by commit count. These are self-selected outliers. The add-then-modify pattern may not generalize to the 50% of files that were never changed or the 23% changed only once. The stagnation finding is actually the more interesting data point, but the paper treats it as a limitation rather than analyzing it.

- **Writing style analysis limited to convention sections.** The five writing styles were identified from only the 50 "Conventions" sections, not from the full content of all files. Other content categories (architecture, build commands, test strategy) may exhibit different style distributions — for example, build commands are inherently prescriptive, so the style variation may be an artifact of the section type chosen for analysis.

- **No comparison to README effectiveness literature.** The paper draws the README/context-file parallel but does not engage with the substantial literature on README quality and its effects on project adoption and contribution. This is a missed opportunity to ground the AI context file phenomenon in known patterns of documentation effectiveness.

## Recommended Next Action

Write a note titled "Context files that do not evolve cannot constrain" connecting to [methodology-enforcement-is-constraining](../notes/methodology-enforcement-is-constraining.md) and [constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md). It would argue that the paper's 50% stagnation finding reveals a gap in the constraining model: the model assumes iterative refinement occurs, but half of context files are write-once artifacts that never enter the maturation trajectory. This creates a testable prediction (projects with evolving context files should show better agent performance than stagnant ones) and a design implication (context engineering tooling should include feedback loops that surface when instructions drift from actual agent behavior — analogous to dead-code detection for instructions).
