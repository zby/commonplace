---
description: "Sentry co-founder's practitioner report on synthesizing Claude Code skills from domain-specific source material (commit history, security patches, OWASP docs) — found 8 real IDORs missed by professional pen testing"
source_snapshot: skill-synthesis-materializing-knowledge-as-skills-2032179291031806408.md
ingested: 2026-03-13
type: practitioner-report
domains: [skill-synthesis, security-automation, deploy-time-learning, context-engineering]
---

# Ingest: Skill Synthesis — Materializing Knowledge as Skills

Source: skill-synthesis-materializing-knowledge-as-skills-2032179291031806408.md
Captured: 2026-03-13
From: https://x.com/zeeg/status/2032179291031806408 + https://cra.mr/skill-synthesis

## Classification

Type: **practitioner-report** — David Cramer describes a specific system he built (Warden), the process he used to build it (skill synthesis via Claude Code), the iterations he went through, and measurable results (17 candidates, 8 validated vulnerabilities). This is experience reporting, not conceptual argument.

Domains: skill-synthesis, security-automation, deploy-time-learning, context-engineering

Author: David Cramer (@zeeg), co-founder and CTO of Sentry. Long track record building developer tools at scale. His experience is with a large, mature, professionally pen-tested codebase — not a toy project. High credibility for "what works in a production codebase" claims.

## Summary

Cramer describes discovering IDOR (Insecure Direct Object Reference) vulnerabilities in Sentry and building an automated detector called Warden using Claude Code's skill system. The core technique — which he calls "skill synthesis" — feeds trustworthy domain-specific source material (OWASP cheat sheets, Sentry's own security patches, internal documentation, commit history) into Claude Code to produce a specialized security-scanning skill. After two refinement iterations to reduce false positives, Warden found 17 potential vulnerabilities, 8 of which were validated as real — some undetected for years despite professional penetration testing and code review. Cramer has packaged the workflow into a reusable skill-writer (`npx skills add getsentry/skills --skill skill-writer`) and describes it as "working really well for materializing knowledge as skills."

## Connections Found

The `/connect` discovery found 6 strong connections, all in the **exemplifies** relationship. This source is a clean practitioner demonstration of several theoretical claims already in the KB:

1. **[skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md)** — exemplifies, and *extends*. Cramer's process is distillation: domain knowledge (the mixture) is compressed into an operational skill (the distillate), with the source material retained for other uses. Critically, the source material here is external domain knowledge (OWASP, commit history), not internal methodology — directly demonstrating the note's own caveat that "not all skills are distilled from methodology."

2. **[deploy-time-learning-the-missing-middle](../notes/deploy-time-learning-the-missing-middle.md)** — exemplifies. The two-iteration refinement loop is deploy-time learning in action. "Skills are just files in a repo" is the deploy-time learning thesis in practitioner language. The skill is a durable, inspectable, versioned repo artifact.

3. **[spec-mining-as-codification](../notes/spec-mining-as-codification.md)** — exemplifies. Mining commit history and past security patches for IDOR patterns, then encoding them as a detection skill, maps directly to the spec mining workflow: observe behavior, identify regularities, extract rules, re-run with constraints.

4. **[inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md)** — exemplifies. The skill file is diffable, versionable, collaboratively refinable. The `npx skills add` distribution model treats skills as inspectable artifacts.

5. **[constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md)** — exemplifies. Iterative refinement through false positive analysis is constraining during deployment per Simon's definition.

6. **[distillation](../notes/distillation.md)** — exemplifies. Multiple distillations from the same material are possible (Cramer plans performance prediction next), the distillate cannot reconstruct the source, and the source persists.

One synthesis opportunity flagged: skills distilled from external domain knowledge have different staleness and maintenance properties than skills distilled from co-maintained internal methodology. When the source is OWASP guides or commit history, you need different mechanisms to detect when the skill has drifted from its source.

## Extractable Value

1. **Skill-from-domain-knowledge as a distinct pattern.** The KB has "skills derive from methodology through distillation" but Cramer's skills derive from *domain knowledge* (commit history, security patches, external standards). This is a concrete instance of the note's own caveat, with enough production detail to reason about the differences. [quick-win] — update the existing skills-derive note with this as an external evidence link.

2. **Source material selection matters more than prompt engineering.** Cramer's key insight is that feeding the right source material (trustworthy, domain-specific) produces dramatically better skills than prompting for generic capability. The accuracy improvement comes from input selection, not output tuning. This has implications for our distillation model — the "what to extract" question depends heavily on "what to feed in." [just-a-reference] — already implied by our distillation framework but useful as a concrete data point.

3. **Quantified false-positive reduction across iterations.** Two refinement iterations took the system from noisy to 8/17 validated (47% precision). This is rare — most practitioner reports don't quantify the improvement trajectory. Could inform thinking about expected iteration counts for deploy-time learning. [just-a-reference]

4. **Skill distribution as package management (`npx skills add`).** Skills as installable packages from a repo. This is a concrete implementation of skill portability that our KB hasn't explored. How does skill distribution interact with the distillation thesis — can a skill distilled from one org's domain knowledge transfer to another? [experiment] — worth tracking but not directly actionable for our methodology.

5. **Professional pen testing missed what domain-specific LLM scanning found.** This is a strong claim about the complementarity of LLM-based detection (broad pattern matching across large codebases with org-specific context) vs. traditional security review (deep but narrow, lacking full codebase context). [just-a-reference] — interesting but tangential to our core concerns.

6. **The "skill-writer" meta-skill.** Cramer packaged the skill-creation process itself as a skill. This is meta-distillation — distilling the distillation process. Relevant to our own skill design: could commonplace's ingestion/connection workflows be packaged as transferable skills? [deep-dive] — raises interesting questions but requires more information about how the skill-writer actually works.

## Limitations (our opinion)

**What is not visible:**

- **Sample size of one codebase.** Warden was tested on Sentry — a large, mature Python/Django application. The 8/17 hit rate may not transfer to different architectures, languages, or security vulnerability classes beyond IDORs. Cramer acknowledges planning to expand to performance prediction, but hasn't yet demonstrated the technique outside security.

- **No comparison to simpler baselines.** Would a carefully prompted Claude Code session with the same source material but without the skill-synthesis machinery produce meaningfully worse results? The value of the skill-writer packaging vs. simply feeding the material into a long prompt is asserted, not measured.

- **Survivorship bias on the refinement process.** Cramer reports two iterations that worked. We don't see: how many source material combinations were tried and discarded, how much Cramer's own security expertise guided the iteration (would a non-security-expert get the same results?), or whether the technique has a floor below which it doesn't help.

- **The "years undetected" claim lacks context.** Eight vulnerabilities "undetected for years" despite pen testing is striking, but we don't know the severity distribution, whether they were in code paths pen testers examined, or whether the pen testing scope was comparable to the LLM scan scope (full codebase vs. targeted assessment). The [spec-mining note](../notes/spec-mining-as-codification.md) would frame this as: the LLM scan covered a broader surface than targeted pen testing, not that it was deeper on the same surface.

- **Maintenance story is absent.** "Skills are just files in a repo" addresses versioning and collaboration but not staleness. When Sentry's codebase evolves, how does Warden's skill stay current? When OWASP updates its guidance, does the skill need re-synthesis? The [distillation note](../notes/distillation.md) flags this: "The residue is only valuable if maintained" — and Cramer's external sources are harder to maintain than internal methodology.

## Recommended Next Action

Done: deep related-systems review written at [getsentry/skills](../notes/related-systems/getsentry-skills.md), focusing on the skill-writer meta-skill and the skill synthesis method rather than the trivial observation that skills are distilled. The review covers: source-driven synthesis with depth gates, labeled iteration, description-as-trigger optimization, the Agent Skills cross-tool spec, and borrowable patterns for our own skill creation process.
