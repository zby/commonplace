---
source_snapshot: context-engineering-ai-agents-oss.md
ingested: 2026-03-02
type: scientific-paper
domains: [context-engineering, agentic-systems, open-source, software-artifacts]
---

# Ingest: Context Engineering for AI Agents in Open-Source Software

Source: context-engineering-ai-agents-oss.md
Captured: 2026-03-02
From: https://arxiv.org/pdf/2510.21413

## Classification

Type: scientific-paper -- Peer-reviewed MSR 2026 paper with structured methodology (mining 10,000 GitHub repos), qualitative coding of content categories and writing styles, commit-level evolution analysis, and formal research questions.

Domains: context-engineering, agentic-systems, open-source, software-artifacts

Author: Mohsenimofidi, Galster, Treude, Baltes -- mixed SE/MSR team. Treude and Baltes are established mining software repositories researchers; Galster has a software architecture background. The combination gives credibility on both the empirical methodology and the software engineering framing.

## Summary

This paper presents the first systematic empirical study of AI context files (AGENTS.md, CLAUDE.md, copilot-instructions.md, GEMINI.md) across 466 open-source projects drawn from a curated sample of 10,000 GitHub repositories. Adoption is still early (5% of sampled repos). The authors find no established content structure, but recurring categories emerge: conventions, contribution guidelines, architecture/structure, and build commands are most common. They identify five writing styles for instructions -- descriptive, prescriptive, prohibitive, explanatory, and conditional -- which reflect experimentation with how to communicate expectations to AI agents. Commit-level analysis of the 10 most actively maintained AGENTS.md files (169 commits) shows that evolution is dominated by adding and modifying instructions, with rare section removal. The paper argues that AI context files are "maintained software artifacts" and that OSS repositories are natural laboratories for studying real-world context engineering.

## Connections Found

/connect discovered eight connections to existing KB notes, all strong:

1. **[context-loading-strategy](../notes/context-loading-strategy.md)** (validates) -- The paper's 14 content categories map directly onto the kinds of information CLAUDE.md loads. The five writing styles are empirical evidence for different instruction modes in always-loaded context.

2. **[methodology-enforcement-is-stabilisation](../notes/methodology-enforcement-is-stabilisation.md)** (grounds) -- The RQ3 evolution data shows context files maturing through "add instructions" then "modify instructions" -- the stabilisation trajectory observed in the wild. The rsyslog commit removing a stylecheck instruction is a concrete example of instruction pruning as practices harden.

3. **[deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md)** (validates) -- The paper's conclusion that AI context files are "maintained software artifacts" that are "versioned, reviewed, quality-assured, and tested" is the deploy-time learning thesis stated as an empirical finding.

4. **[agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md)** (exemplifies) -- The five writing styles are strategies for managing underspecification: prescriptive narrows interpretation maximally, descriptive leaves it wide, conditional encodes branching, prohibitive sets boundaries, explanatory adds warrants.

5. **[human-llm-differences-are-load-bearing](../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md)** (validates) -- The paper explicitly contrasts "README files for humans" with "AI context files for AI agents" -- the dual-audience observation at scale.

6. **[programming-practices-apply-to-prompting](../notes/programming-practices-apply-to-prompting.md)** (validates) -- Developers are applying version control, code review, and testing to context files, confirming that programming practices transfer to prompt-adjacent work.

7. **[continuous-learning-is-stabilisation-during-deployment](../notes/continuous-learning-is-stabilisation-during-deployment.md)** (validates) -- The commit-level analysis showing iterative refinement of instructions over time is continuous learning through versioned artifacts.

8. **[agent-skills-for-context-engineering](../notes/related-systems/agent-skills-for-context-engineering.md)** (complements) -- Academic empirical data on the same phenomenon that the agent-skills note addresses through practitioner design.

The source sits squarely in the knowledge base's core territory. It provides empirical grounding for multiple theoretical claims that were previously supported only by practitioner intuition.

## Extractable Value

1. **Five writing styles as an empirical taxonomy.** The descriptive/prescriptive/prohibitive/explanatory/conditional taxonomy is grounded in qualitative coding of 50 convention sections. This could sharpen our own instruction-writing guidance -- we currently don't distinguish these modes explicitly. [quick-win]

2. **Content category frequency data.** Table 1 provides a ranked list of what developers actually put in context files. Conventions (50), contribution guidelines (48), and architecture (47) dominate. This is evidence for prioritising these categories in CLAUDE.md templates. [just-a-reference]

3. **Evolution pattern: add-then-modify dominance.** "Add instruction(s)" (78) and "Modify instruction(s)" (59) dwarf "Remove instruction(s)" (23) and "Remove section(s)" (2). Context files grow and refine but rarely shrink. This challenges any assumption that stabilisation naturally prunes instructions -- it may require deliberate effort. [experiment]

4. **The 50% stagnation finding.** 77 of 155 AGENTS.md files were never changed after initial creation. Half of all context files are write-once artifacts. This is a signal that many teams create context files without a maintenance practice -- relevant to our stabilisation theory. [deep-dive]

5. **Co-evolution as a research frontier.** The paper flags co-evolution of source code and context files as an open research direction, analogous to code-comment co-evolution. This is directly relevant to how claws should handle drift between instructions and implementation. [experiment]

6. **Dual-audience confirmation at scale.** The explicit README-for-humans vs. context-file-for-agents distinction, observed across 466 projects, is the strongest empirical evidence we have for the dual-audience design principle. [just-a-reference]

7. **rsyslog anecdote as stabilisation exemplar.** "AI support: Agent shall no longer call stylecheck.sh" is a perfect concrete example for the stabilisation narrative -- an instruction removed because the underlying practice hardened. Worth citing directly. [quick-win]

## Recommended Next Action

Write a note titled "Context file writing styles are strategies for managing underspecification" connecting to [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) and [context-loading-strategy](../notes/context-loading-strategy.md). It would argue that the five empirically-observed writing styles (descriptive, prescriptive, prohibitive, explanatory, conditional) are not random stylistic variation but correspond to different strategies for narrowing the interpretation space that agents face when processing instructions. Prescriptive and prohibitive styles constrain maximally; descriptive and explanatory styles provide context that enables better judgment; conditional style encodes branching logic. This maps the empirical taxonomy onto the theoretical framework and provides actionable guidance for writing CLAUDE.md content: choose the style that matches the desired degree of agent autonomy for each instruction.
