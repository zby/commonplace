---
description: Production practitioner report on building AI agents for financial services — validates files-not-database at commercial scale (S3-first with derived PostgreSQL), documents skill shadowing as user-customization mechanism, and articulates "model eats scaffolding" as an explicit design principle with fiscal-period normalization as calculator-regime counterexample
source_snapshot: lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md
ingested: 2026-03-09
type: practitioner-report
domains: [agent-architecture, context-engineering, skills-as-product, filesystem-first]
---

# Ingest: Lessons from Building AI Agents for Financial Services

Source: [lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md](./lessons-from-building-ai-agents-for-financial-services-2015174818497437834.md)
Captured: 2026-03-03
From: https://x.com/nicbstme/status/2015174818497437834

## Classification

Type: **practitioner-report** — The author built Fintool, an AI agent product for professional investors, over two years and describes the architectural decisions, infrastructure choices, and lessons learned from production deployment. Includes specific technical details (S3 sync architecture, Temporal workflows, sandbox design, evaluation methodology) grounded in real operational experience with paying customers.

Domains: agent-architecture, context-engineering, skills-as-product, filesystem-first

Author: @nicbstme, founder/builder of Fintool — an AI agent for financial services used by professional investors. Two years of production experience in a domain with zero tolerance for errors. Mentions direct collaboration with Anthropic's Claude Code team (Thariq). Credible practitioner with production stakes.

## Summary

A comprehensive practitioner report covering 11 architectural lessons from building Fintool, an AI agent for professional investors. The central thesis is that "the model is not the product — the experience around the model is the product." Key architectural bets include: mandatory sandboxing for code execution, filesystem-first data architecture (S3 as source of truth with PostgreSQL as derived index), markdown-based skills as the primary product surface, and a conviction that models will eventually absorb basic scaffolding (the "model will eat your scaffolding" thesis). The author explicitly adopted Claude Code's filesystem-first approach, retired their RAG pipeline in favor of agentic search, and built a skill system with copy-on-write shadowing (private > shared > public priority). The report also covers Temporal for long-running task reliability, real-time streaming with delta updates, and domain-specific evaluation with ~2,000 test cases where PRs are blocked if eval score drops >5%.

## Connections Found

Discovery via `/connect` identified 8 strong and 5 moderate connections.

**Strong connections:**

1. **[files-not-database](../notes/files-not-database.md)** — exemplifies at production scale. Fintool's S3-first architecture validates the files-not-database claim at commercial scale: S3 as source of truth, Lambda-synced PostgreSQL as derived index for fast queries, user data (memories, watchlists, skills) stored as YAML/markdown files. The "derived indexes for capabilities files alone can't provide" pattern is exactly what they built. Adds 11-nines durability and real paying users to the evidence base.

2. **[bitter-lesson-boundary](../notes/bitter-lesson-boundary.md)** — exemplifies the softening prediction. "The model will eat your scaffolding" is the bitter lesson applied to agent infrastructure. The author predicts basic skills become one-liners in two years as models improve, and describes the practical response: "write skills, delete them when unnecessary, build new ones for harder problems." This maps onto the crystallise-for-current-leverage-not-permanence heuristic. Critically, fiscal period normalization (10,000+ company calendars) is a clean calculator-regime counterexample — the spec IS the problem, so models will not absorb it.

3. **[Agent Skills for Context Engineering](../notes/related-systems/agent-skills-for-context-engineering.md)** — provides production evidence for shared patterns. Fintool's skill architecture independently converges: markdown files with YAML frontmatter, progressive disclosure (discover metadata first, load full content on use), SQL discovery with lazy loading. Agent Skills identifies "hosted agent infrastructure (sandboxing, warm pools)" as an area they cover deeply; Fintool provides the production implementation detail.

4. **[llm-context-is-a-homoiconic-medium](../notes/llm-context-is-a-homoiconic-medium.md)** — exemplifies without naming. Skills, memories, and watchlists are all "just files" — the same markdown serves as both content and agent instructions. The copy-on-write skill shadowing system works because skills are text files, not compiled code. The author writes: "Skills tell the agent how to do things. Memories tell it what the user cares about. Both are just files." This is homoiconicity described as production architecture.

5. **[skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md)** — provides a counter-example. Fintool's skills are written by analysts and customers, not distilled from a methodology KB. A portfolio manager with 500 DCF valuations encodes their methodology directly in markdown. This is distillation from human expertise — a different pathway than the methodology-to-skill distillation the KB note describes. In product contexts, practitioner-authored skills may be the dominant mode.

6. **[deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md)** — exemplifies the full verifiability gradient. Fintool demonstrates multiple grades in production: restructured prompts (skills as markdown), eval-driven development (~2,000 test cases, PR blocked on regression), and deterministic modules (fiscal period normalization, parsing pipeline with quality scoring). The "model eats scaffolding" thesis maps onto the stabilise/soften cycle.

7. **[context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md)** — validates from production. "Context is the product" echoes the note's central claim. Fintool's entire data normalization pipeline exists because context quality determines agent quality. Their SQL skill discovery (lazy loading, metadata-driven filtering) is progressive disclosure driven by context budget constraints. "Bad chunks = bad answers" is context engineering applied to retrieval.

8. **[oracle-strength-spectrum](../notes/oracle-strength-spectrum.md)** — exemplifies oracle hardening at scale. ~2,000 test cases manufacturing hard oracles (ticker disambiguation, fiscal period normalization, numeric precision), adversarial grounding tests (planting false data to verify hallucination resistance) amplifying oracle strength, production monitoring detecting drift. Tables below 90% confidence get flagged — quality scoring as soft oracle. PR blocked if eval drops >5% — a hard oracle gate on deployment.

**Moderate connections:**

9. **[inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md)** — exemplifies inspectable substrate choice. "YAML files are human-readable. You can debug with `cat`" is the inspectable substrate argument applied to production agent architecture.

10. **[three-space-agent-memory-maps-to-tulving-taxonomy](../notes/three-space-agent-memory-maps-to-tulving-taxonomy.md)** — partially exemplifies knowledge/self separation. Fintool separates knowledge (financial data), self/preferences (UserMemories.md), and procedural (skills). The separation is implicit in their S3 mount points (public/shared/private) rather than theorized.

11. **[Koylanai Personal Brain OS](./koylanai-personal-brain-os.ingest.md)** — parallel practitioner in a different domain. Both independently arrive at filesystem-as-knowledge-base, markdown-as-universal-format, and skills-as-product. Convergence across personal productivity and commercial finance strengthens the signal that these patterns are durable.

12. **[related-systems-index](../notes/related-systems/related-systems-index.md)** — provides additional convergence evidence. The index already documents convergence on filesystem-first and progressive disclosure across independent systems; Fintool adds commercial production-scale evidence from a zero-error-tolerance domain.

**Synthesis opportunities flagged by /connect:**

- **Production-scale convergence on filesystem-first**: Three independent sources (Fintool, Koylanai, systems in related-systems-index) converge on filesystem-as-source-of-truth with derived indexes across personal/commercial/research contexts.
- **Oracle hardening in practice**: Fintool's evaluation infrastructure is a concrete production implementation of the manufacture/amplify/monitor pipeline from oracle-strength-spectrum — enough practitioner evidence may exist to write a note about how oracle hardening works in deployed systems versus the theoretical framework.

## Extractable Value

1. **Copy-on-write skill shadowing (private > shared > public priority).** A concrete mechanism for user customization of skills without forking. When a user drops their own `SKILL.md` at the same path, it wins. This is a pattern we don't have — our skills are not overridable per-installation. [experiment]

2. **"The model will eat your scaffolding" as explicit design principle.** Designing skills for obsolescence — markdown over code because it's easier to update and delete. The practical corollary: send detailed feedback to AI labs documenting exactly what scaffolding you built and why, so the next model generation can absorb it. Reframes the bitter lesson from observation to design methodology. [quick-win]

3. **Adversarial grounding as evaluation technique.** Injecting fake numbers into context alongside real data, then verifying the model cites the real source. 50 test cases specifically for hallucination resistance. A concrete, replicable evaluation pattern that directly hardens the oracle. [experiment]

4. **User memories as injectable markdown files.** A `/private/memories/UserMemories.md` that users edit directly, injected as context on every conversation. "I focus on small-cap value stocks." Simple, powerful, no schema needed. This is user-facing stabilisation — the user constrains the agent's interpretation space by writing preferences in the same medium the agent reads. [quick-win]

5. **SQL discovery for skill metadata instead of filesystem mounting.** Loading skill names/descriptions at query time, full content only on activation. Prevents token waste from mounting all skills. Implements progressive disclosure at the infrastructure level. [just-a-reference]

6. **Fiscal period normalization as a clean calculator-regime example.** 10,000+ company fiscal calendars where "Q1 2024" means different absolute date ranges per company. The spec IS the problem, making it a clean example of the calculator regime inside an otherwise vision-feature domain. Useful as a concrete example for the bitter lesson boundary note. [just-a-reference]

7. **S3-first with derived PostgreSQL index as production-grade files-not-database.** Writes to S3, Lambda sync to PostgreSQL, reads from DB for lists / S3 for freshness. Two Lambda functions: real-time SNS-triggered sync plus 3-hour reconciliation sweep. Battle-tested implementation of the files-as-source-of-truth pattern with durability and audit trail guarantees. [just-a-reference]

## Limitations (our opinion)

**Survivorship bias.** The author reports what worked at Fintool. Failed experiments, abandoned architectures, and approaches that didn't scale are invisible. The S3-first bet is presented as obvious in retrospect, but the author acknowledges "people thought we were crazy" when they retired their embedding pipeline — the failed alternative paths aren't described.

**Sample size of one.** Fintool serves professional investors — a niche with extreme accuracy requirements, high user sophistication, and willingness to pay premium pricing. Patterns that work here (paranoid evaluation, 2,000 test cases, domain-specific fiscal calendars) may not transfer to domains with different error tolerances or cost structures. The author generalizes ("every chat application needs a sandbox") without acknowledging this.

**Context-specific infrastructure.** The S3 + Lambda + PostgreSQL architecture makes sense at Fintool's scale and within AWS. The "S3 beats databases" claim is actually "S3 beats databases for Fintool's specific access patterns" (mostly writes of user-generated files, with list queries as the main read pattern). Workloads with complex relational queries, transactions, or real-time consistency requirements might not fit this pattern.

**No independent evaluation.** The ~2,000 test cases and eval-driven development process are self-reported. We don't see the test cases, the failure modes they miss, or how the 5% regression threshold was chosen. The adversarial grounding tests sound robust but 50 test cases is a small adversarial set for a system making financial recommendations.

**Skills-as-product claim is underdeveloped.** The author claims non-engineers write skills and customers write their own, but provides only one simplified DCF example. How many customer-authored skills exist in practice? How often do they break? What happens when a customer's skill contradicts financial best practices? The copy-on-write mechanism is elegant in theory; adoption and quality data are missing.

**The "model eats scaffolding" prediction is unfalsifiable as stated.** "In two years, most basic skills will be one-liners" — there's no definition of "basic" that would let you evaluate this prediction. The [bitter-lesson-boundary](../notes/bitter-lesson-boundary.md) note provides the theoretical framework for identifying WHICH scaffolding gets eaten (vision-feature regime) versus which persists (calculator regime), but the author conflates the two.

## Recommended Next Action

Write a note titled "Skill shadowing enables per-user customization without forking" connecting to [skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md) and [ad-hoc-prompts-extend-the-system-without-schema-changes](../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md) — it would argue that a copy-on-write priority chain (private > shared > public) for skills is the mechanism that bridges the gap between "skills distilled from methodology" and "skills authored by domain experts," and that it works precisely because skills are files in a homoiconic medium where override is just file shadowing. This is the one genuinely new architectural pattern in the source that we don't yet have a note for.
