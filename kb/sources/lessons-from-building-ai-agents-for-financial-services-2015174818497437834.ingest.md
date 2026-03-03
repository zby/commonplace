---
source_snapshot: lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md
ingested: 2026-03-03
type: practitioner-report
domains: [agent-architecture, context-engineering, skills-as-product, filesystem-first]
---

# Ingest: Lessons from Building AI Agents for Financial Services

Source: [lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md](./lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md)
Captured: 2026-03-03
From: https://x.com/nicbstme/status/2015174818497437834

## Classification

Type: **practitioner-report** -- The author built Fintool, an AI agent product for professional investors, over two years and describes the architectural decisions, infrastructure choices, and lessons learned from production deployment. Includes specific technical details (S3 sync architecture, Temporal workflows, sandbox design, evaluation methodology) grounded in real operational experience.

Domains: agent-architecture, context-engineering, skills-as-product, filesystem-first

Author: @nicbstme, founder/builder of Fintool -- an AI agent for financial services used by professional investors. Two years of production experience in a domain with zero tolerance for errors. Mentions direct collaboration with Anthropic's Claude Code team (Thariq). Credible practitioner with production stakes.

## Summary

A comprehensive practitioner report covering 11 architectural lessons from building Fintool, an AI agent for professional investors. The central thesis is that "the model is not the product -- the experience around the model is the product." Key architectural bets include: mandatory sandboxing for code execution, filesystem-first data architecture (S3 as source of truth with PostgreSQL as derived index), markdown-based skills as the primary product surface, and a conviction that models will eventually absorb basic scaffolding (the "model will eat your scaffolding" thesis). The author explicitly adopted Claude Code's filesystem-first approach, retired their RAG pipeline in favor of agentic search, and built a skill system with copy-on-write shadowing (private > shared > public priority). The report also covers Temporal for long-running task reliability, real-time streaming with delta updates, and domain-specific evaluation with ~2,000 test cases.

## Connections Found

Discovery via semantic search against the commonplace index identified six strong connections:

1. **[files-not-database](../notes/files-not-database.md)** (exemplifies at production scale): Fintool's S3-first architecture is a production-grade version of the same claim -- files as source of truth, derived indexes (PostgreSQL) for fast queries. The pattern is identical: "S3 is the source of truth. A Lambda function syncs changes to PostgreSQL for fast queries." Their user memories and watchlists live as markdown/YAML files in S3. The claw note argues files beat databases for agent KBs; Fintool demonstrates this at commercial scale with 11-nines durability, versioning, and human-readable debugging.

2. **[bitter-lesson-boundary](../notes/bitter-lesson-boundary.md)** (directly instantiates the softening prediction): The "model will eat your scaffolding" section is an explicit practitioner articulation of the bitter lesson applied to agent infrastructure. The author predicts basic skills will become one-liners in two years as models improve -- this is exactly the softening trajectory the bitter lesson boundary note describes. He even describes the practical response: "write skills, delete them when they become unnecessary, build new ones for harder problems." This maps onto the crystallise-for-current-leverage-not-permanence heuristic.

3. **[Agent Skills for Context Engineering](../notes/related-systems/agent-skills-for-context-engineering.md)** (shares architectural patterns, provides production evidence): Fintool's skill architecture independently converges with the Agent Skills framework -- markdown files with YAML frontmatter, progressive disclosure (discover metadata first, load full content on use), and the claim that "the model wants to fetch skills." Their SQL discovery pattern (lazy loading, access control, shadowing logic) is a production implementation of the same progressive disclosure principle. The Agent Skills note identifies "hosted agent infrastructure (sandboxing, warm pools, pre-built images)" as an area where that framework goes deeper than ours -- Fintool provides the production detail.

4. **[Koylanai Personal Brain OS](./koylanai-personal-brain-os.ingest.md)** (parallel practitioner, different domain): Both reports independently arrive at filesystem-as-knowledge-base, markdown-as-universal-format, and skills-as-product. Koylanai builds a personal productivity system; Fintool builds a commercial financial product. The convergence across domains strengthens the signal that these architectural patterns are durable. Key difference: Fintool adds a production layer (S3 + Lambda sync + PostgreSQL) that Koylanai's Git-only approach doesn't need at personal scale.

5. **[llm-context-is-a-homoiconic-medium](../notes/llm-context-is-a-homoiconic-medium.md)** (exemplifies without naming): Skills, memories, and watchlists are all "just files" -- the same markdown that serves as content also serves as agent instructions. The copy-on-write skill shadowing system (private > shared > public) works because skills are just text files, not compiled code. The author doesn't use the term homoiconicity, but describes the property exactly: "Skills tell the agent how to do things. Memories tell it what the user cares about. Both are just files."

6. **[skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md)** (provides a counter-example worth examining): Fintool's skills are written by analysts and customers, not distilled from a methodology KB. Their DCF skill encodes a portfolio manager's 500-valuation methodology directly into markdown. This is distillation from human expertise, not from written methodology notes. The claw's claim that skills derive from methodology through distillation may be specific to methodology-about-methodology -- in a product context, skills distill from practitioner knowledge.

## Extractable Value

1. **S3-first with derived PostgreSQL index as production-grade files-not-database.** Their architecture (writes to S3, Lambda sync to PostgreSQL, reads from DB for lists / S3 for freshness) is a concrete, battle-tested implementation of the files-as-source-of-truth pattern. Could inform how we think about scaling the claw's file-based architecture beyond grep. [just-a-reference]

2. **Copy-on-write skill shadowing (private > shared > public priority).** A concrete mechanism for user customization of skills without forking. When a user drops their own `SKILL.md` at the same path, it wins. This is a pattern we don't have -- our skills are not overridable per-installation. [experiment]

3. **"The model will eat your scaffolding" as a design principle.** Explicitly designing skills for obsolescence -- markdown over code because it's easier to update and delete. The practical corollary: send detailed feedback to AI labs documenting exactly what scaffolding you built and why, so the next model generation can absorb it. This reframes the bitter lesson from a theoretical observation to a design methodology. [quick-win]

4. **SQL discovery for skill metadata instead of filesystem mounting.** Loading skill names/descriptions at query time, full content only on activation. Prevents token waste from mounting all skills. Their argument: lazy loading, access control at query time, shadowing logic, and metadata-driven filtering are all easier in SQL than filesystem mounts. [just-a-reference]

5. **Domain-specific evaluation as non-optional infrastructure.** ~2,000 test cases across ticker disambiguation, fiscal period normalization, numeric precision, and adversarial grounding (injecting fake numbers to test hallucination resistance). PR blocked if eval score drops >5%. The adversarial grounding pattern (plant false data alongside real data, verify correct citation) is a concrete, replicable evaluation technique. [experiment]

6. **User memories as injectable markdown files.** A `/private/memories/UserMemories.md` file that users edit directly, injected as context on every conversation. "I focus on small-cap value stocks" or "Always compare to industry median, not mean." Simple, powerful, no schema needed. This is user-facing stabilisation -- the user constrains the agent's interpretation space by writing preferences in the same medium the agent reads. [quick-win]

7. **Fiscal period normalization as a "calculator" domain.** Their fiscal calendar database for 10,000+ companies -- normalizing "Q1 2024" to absolute date ranges per company -- is a clean example of a calculator-regime problem inside an otherwise vision-feature domain. The spec IS the problem (Apple's fiscal Q1 = Oct-Dec), so it crystallises cleanly. Useful as a concrete example for the bitter lesson boundary. [just-a-reference]

## Recommended Next Action

Write a note titled "Skill shadowing enables per-user customization without forking" connecting to [skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md) and [ad-hoc-prompts-extend-the-system-without-schema-changes](../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md) -- it would argue that a copy-on-write priority chain (private > shared > public) for skills is the mechanism that bridges the gap between "skills distilled from methodology" and "skills authored by domain experts," and that it works precisely because skills are files in a homoiconic medium where override is just file shadowing.
