---
description: "Sentry's shared skills repo with a skill-writer meta-skill that codifies the skill creation process itself — source-driven synthesis with depth gates, labeled iteration, description-as-trigger optimization, and the Agent Skills cross-tool spec"
type: note
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: 2026-03-13
---

# getsentry/skills

Sentry's open-source repository of agent skills, maintained by David Cramer (@zeeg, Sentry CTO). The repo's central artifact is the **skill-writer** — a meta-skill that codifies the entire skill creation lifecycle: source collection, synthesis with depth gates, authoring, description optimization, evaluation, and registration. Skills follow the [Agent Skills](https://agentskills.io) specification, a cross-tool standard adopted by 30+ agent products (Claude Code, Cursor, Copilot, Gemini CLI, etc.).

**Repository:** https://github.com/getsentry/skills

## Core Ideas

**The skill-writer is the interesting artifact, not the skills it produces.** The repo contains ~20 skills (security review, commit formatting, PR iteration, etc.), but the methodologically significant contribution is the process for creating them. The skill-writer packages the skill creation workflow as a 7-step pipeline with 12 reference documents covering synthesis, iteration, authoring, evaluation, and validation paths. Each path is loaded conditionally — you only read the reference you need for the current step.

**Source breadth is the primary quality lever, not prompt engineering.** The synthesis path requires exhaustive source collection before authoring can begin: domain documentation, upstream implementations, existing in-repo skills, repo conventions, and (critically) real-world failure cases and false-positive patterns. The skill-writer explicitly states: "keep collecting until retrieval passes no longer add meaningful new guidance." The Warden security skill (which found 8 real IDOR vulnerabilities in Sentry's codebase that pen testing missed) was built by feeding OWASP cheat sheets, Sentry's own security patches, and commit history — trustworthy, domain-specific source material rather than generic prompting. The accuracy came from input selection, not output tuning.

**Depth gates prevent shallow skills.** Before authoring begins, the synthesis path enforces hard gates: no missing high-impact coverage dimensions, coverage expansion passes completed, stopping rationale explicit, and for authoring skills, transformed example artifacts (happy-path, secure/robust variant, anti-pattern + corrected version) must exist. If any gate fails, synthesis is declared incomplete and authoring cannot proceed. This is the most mechanistically interesting pattern — it's a structural quality floor that doesn't depend on LLM judgment at the gate itself.

**Labeled iteration with holdout sets.** The iteration path (for improving existing skills from outcomes) captures examples labeled by kind (`true-positive`, `false-positive`, `fix`, `regression`, `edge-case`) and evidence origin (`human-verified`, `mixed`, `synthetic`), evaluates against working and holdout sets, and carries concrete behavior deltas into authoring. This is the deploy-time refinement loop with enough structure to be reproducible rather than ad-hoc.

**Description-as-trigger optimization.** Skill descriptions aren't for humans — they're routing mechanisms. The description optimization path builds should-trigger and should-not-trigger query sets, evaluates the current description against both, and iteratively edits to improve precision/recall. This treats skill discovery as an information retrieval problem with measurable quality.

**Progressive disclosure via conditional reference loading.** Skills use a three-tier loading model: metadata (name + description, always loaded) → SKILL.md body (loaded on activation) → reference files (loaded on demand via decision tables). The security-review skill demonstrates this well: SKILL.md has a table mapping code types to which reference files to load (`API endpoints → authorization.md, injection.md`; `Frontend → xss.md, csrf.md`), so the agent loads only the relevant domain knowledge for the current review. This keeps base context small while making deep knowledge available.

**Skill classes with required dimensions.** Skills are classified into types (`workflow-process`, `integration-documentation`, `security-review`, `skill-authoring`, `generic`), each with specific required coverage dimensions and artifact requirements. An `integration-documentation` skill must produce `api-surface.md`, `common-use-cases.md` (≥6 cases), and `troubleshooting-workarounds.md` (≥8 entries). This is type-driven quality — the class determines what counts as complete.

## Comparison with Our System

| Dimension | getsentry/skills | Commonplace |
|-----------|-----------------|-------------|
| Skill creation process | Codified as a meta-skill with depth gates, source provenance, evaluation | Ad-hoc; WRITING.md has a checklist but no structured synthesis pipeline |
| Source tracking | SOURCES.md with trust tiers, confidence, usage constraints, changelog | Ingestion tracks sources but doesn't carry provenance into skill creation |
| Quality floor | Hard depth gates: synthesis must pass before authoring begins | Soft: checklist in WRITING.md, /validate after writing |
| Progressive disclosure | Decision tables route to specific references by detected context | Same principle (instruction-specificity-should-match-loading-frequency), less explicit conditional loading |
| Iteration method | Labeled examples with holdout sets, provenance, evidence origin | Deploy-time learning as a concept, no structured iteration protocol |
| Skill discovery | Description optimization with should/shouldn't trigger sets | Skill descriptions exist but aren't systematically optimized |
| Cross-tool portability | Agent Skills spec, works across 30+ tools | Claude Code only |
| Grounding theory | Empirical/operational — patterns from production use | Programming theory + learning theory |

The key divergence: **getsentry/skills codifies the skill creation process; we theorize about it.** Our notes on distillation, methodology enforcement, and spec mining describe the patterns that the skill-writer implements. We have the theory that skills should mature through an instruction → skill → script trajectory; they have a working meta-skill that enforces quality at each step. This is the typical gap between explanatory knowledge and operational knowledge — we can explain why their approach works, but they have the working machinery.

The depth gates pattern is where getsentry/skills adds something our theory doesn't capture well. Our maturation trajectory describes *when* to move down the enforcement gradient (when the agent consistently proposes the same correct step), but doesn't address *quality floors for creation* — ensuring a skill has sufficient coverage before it's written at all. The depth gate is a pre-authoring quality check, not a post-authoring enforcement mechanism.

## Borrowable Ideas

**Depth gates for skill creation** — Before writing a skill, require explicit coverage evidence: what sources were consulted, what dimensions are covered vs. partial vs. missing, and a stopping rationale for why further collection is low-yield. This could integrate into our `/ingest` workflow: before the ingest report is finalized, check that key coverage dimensions are addressed. *Ready to borrow now* — doesn't require new infrastructure, just a checklist extension.

**SOURCES.md with trust tiers and provenance** — Track source material with trust tier (canonical, secondary, untrusted), confidence level, contribution notes, and usage constraints. Our ingestion already captures sources but doesn't classify trust or carry provenance through to skill artifacts. *Ready to borrow* — extend the ingest report format.

**Conditional reference loading via decision tables** — Instead of loading all references, use tables that map detected context to specific files. Our skills could benefit: `/validate` could load different check sets based on note type; `/ingest` could load different classification guidance based on source type. *Ready to borrow* — our skills already support this pattern structurally.

**Should-trigger / should-not-trigger description testing** — For each skill description, define test queries that should and shouldn't activate it, then optimize. This is a concrete quality measure we could apply to our skill descriptions. *Needs a use case first* — requires enough skills to make discovery errors a real problem.

**Labeled iteration protocol** — When improving a skill from outcomes, capture labeled examples (positive/negative/fix/regression/edge-case) with evidence origin and provenance, evaluate against holdout sets, and carry deltas into the next version. This turns ad-hoc refinement into reproducible iteration. *Needs adaptation* — our KB doesn't have the same kind of repeated execution that generates labeled examples at scale.

## Curiosity Pass

**The skill-writer is large — does it actually work as intended?** The meta-skill has SKILL.md (73 lines) + 12 reference files + 3 example case studies + a validation script. That's substantial context to load and follow. The design principles document says "if a senior engineer would skip reading it, the agent doesn't need it either" — but would a senior engineer read all 12 reference files? The progressive disclosure design (only load the path you need) mitigates this, but it depends on the agent correctly identifying which paths to follow. Failure mode: the agent loads SKILL.md, skims the step table, and goes straight to authoring without running synthesis depth gates — exactly the shallow skill creation the gates are designed to prevent.

**Depth gates claim structural enforcement, but are they really structural?** The gates are written in natural language: "no missing high-impact coverage dimensions," "stopping rationale is explicit." These are instructions to an LLM, not machine-checkable assertions. The `quick_validate.py` script exists but only checks structural properties (frontmatter format, directory naming), not coverage depth. So the depth gates are at the *skill* level on the [enforcement gradient](../methodology-enforcement-is-constraining.md), not at the hook or script level — they depend on the LLM's judgment about whether coverage is sufficient. This means they prevent obviously shallow skills but can't prevent confidently shallow skills (where the LLM believes coverage is adequate but it isn't).

**The security-review skill is the strongest artifact in the repo.** It demonstrates the full pattern: OWASP-sourced domain knowledge → progressive disclosure via decision tables → false-positive controls built from real counterexamples → confidence-calibrated reporting. The explicit "do not flag" section (framework-mitigated patterns, server-controlled values) is as important as the "always flag" section — it shows that the synthesis process generates negative constraints, not just positive ones. This is the claim that source material selection matters more than prompt engineering, made concrete.

**The Agent Skills spec is a convergence signal worth tracking.** Thirty-plus tools independently adopting the same skill format (SKILL.md with frontmatter + references/ + scripts/) is strong evidence that the progressive disclosure architecture is durable. Our note on [instruction specificity matching loading frequency](../instruction-specificity-should-match-loading-frequency.md) predicted this shape; the spec is empirical confirmation from the ecosystem.

**Source breadth vs. our distillation model.** The skill-writer's emphasis on source *breadth* (keep collecting until retrieval passes no longer add new guidance) is interestingly different from our distillation model's emphasis on *compression* (extract operational procedures from broader reasoning). These aren't contradictory — you need breadth before you can compress — but our distillation notes focus on the compression step and underemphasize the input gathering that makes good compression possible. The extractable-value section of the ingestion report noted this: "the 'what to extract' question depends heavily on 'what to feed in.'"

## What to Watch

- **Does the skill-writer improve itself?** The iteration path should apply to the skill-writer itself — it's classified as `skill-authoring` class. Watch for whether subsequent versions of the meta-skill show evidence of self-application (labeled examples from skill creation outcomes feeding back into the skill-writer's own instructions).
- **Depth gate codification.** The current depth gates are LLM-interpreted instructions. If Sentry moves any of them to machine-checkable validation (extending `quick_validate.py` with coverage analysis), that would be a concrete example of the [maturation trajectory](../methodology-enforcement-is-constraining.md) completing for a skill creation process.
- **Agent Skills spec evolution.** As the spec matures across 30+ tools, watch for whether it develops a formal evaluation/testing protocol (currently absent from the spec). The evaluation-path reference in the skill-writer is Sentry-internal, not part of the cross-tool standard.
- **Distribution model validation.** Sentry vendors (copies) skills into repos rather than treating them as runtime dependencies. This is a bet on customization over standardization. Watch whether other adopters do the same or develop a package-manager model with versioned dependencies.

---

Relevant Notes:

- [methodology enforcement is constraining](../methodology-enforcement-is-constraining.md) — the skill-writer is methodology enforcement codified as a skill: the maturation trajectory in action, with the creation process itself at skill level (deterministic trigger, LLM-interpreted response) and depth gates that aspire to but haven't yet reached the script level
- [spec mining as codification](../spec-mining-as-codification.md) — the synthesis path (collect source material, identify patterns, extract into a skill, re-run with constraints) is the spec mining workflow applied to domain knowledge rather than system behavior
- [instruction specificity should match loading frequency](../instruction-specificity-should-match-loading-frequency.md) — the Agent Skills spec's three-tier loading model (metadata always → SKILL.md on activation → references on demand) is a cross-ecosystem implementation of this principle
- [deploy-time learning: the missing middle](../deploy-time-learning-the-missing-middle.md) — the iteration path (labeled examples → holdout evaluation → behavior deltas → re-authoring) is deploy-time learning with enough structure to be reproducible
- [inspectable substrate, not supervision](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — "skills are just files in a repo" makes the synthesized knowledge diffable, versionable, and collaboratively refinable
- [Agent Skills for Context Engineering](./agent-skills-for-context-engineering.md) — earlier review of a skills-based context engineering library; getsentry/skills is a production implementation where that review covered a reference/teaching library
