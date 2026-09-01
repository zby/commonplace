---
description: "Sentry co-founder's practitioner report on synthesizing Claude Code skills from domain-specific source material (commit history, security patches, OWASP docs) — found 8 real IDORs missed by professional pen testing"
source: https://x.com/zeeg/status/2032179291031806408
captured: "2026-03-13T00:00:00+00:00"
capture: webfetch
genre: practitioner-report
snapshot_sha256: b9d7263006deec0be4b866e232e0c5cc8ce3c00f59323cd9721cbde3a640c706
status_id: 2032179291031806408
linked_url: https://cra.mr/skill-synthesis
ingested: "2026-03-13"
type: kb/sources/types/ingest-report.md
domains: [skill-synthesis, security-automation, deploy-time-learning, context-engineering]
---

# Ingest: Skill Synthesis — Materializing Knowledge as Skills

## Classification

David Cramer describes a specific system he built (Warden), the process he used to build it (skill synthesis via Claude Code), the iterations he went through, and measurable results (17 candidates, 8 validated vulnerabilities). This is experience reporting, not conceptual argument.

Author: David Cramer (@zeeg), co-founder and CTO of Sentry. Long track record building developer tools at scale. His experience is with a large, mature, professionally pen-tested codebase — not a toy project. High credibility for "what works in a production codebase" claims.

## Summary

Cramer describes discovering IDOR (Insecure Direct Object Reference) vulnerabilities in Sentry and building an automated detector called Warden using Claude Code's skill system. The core technique — which he calls "skill synthesis" — feeds trustworthy domain-specific source material (OWASP cheat sheets, Sentry's own security patches, internal documentation, commit history) into Claude Code to produce a specialized security-scanning skill. After two refinement iterations to reduce false positives, Warden found 17 potential vulnerabilities, 8 of which were validated as real — some undetected for years despite professional penetration testing and code review. Cramer has packaged the workflow into a reusable skill-writer (`npx skills add getsentry/skills --skill skill-writer`) and describes it as "working really well for materializing knowledge as skills."

## Quotes

No source quotes have been retained yet.

## Connections Found

The `/connect` discovery found 6 strong connections, all in the **exemplifies** relationship. This source is a clean practitioner demonstration of several theoretical claims already in the KB:

1. **[Skills derive from methodology](../notes/skills-derive-from-methodology.md)** — qualifies. Cramer's skills are abstracted from external domain artifacts (OWASP guidance and commit history), not worked out from retained methodology. The resulting rules generalize beyond the artifacts that prompted them, so they enter the discovery lifecycle as conjectures and earn authority through testing. The process skips theory-building and goes straight from domain artifacts to operational instructions. Without a theory layer, the skill has no reasoned basis for adapting when it encounters cases the source material did not cover.

2. **[deploy-time-learning-the-missing-middle](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md)** — exemplifies. The two-iteration refinement loop is deploy-time learning in action. "Skills are just files in a repo" is the deploy-time learning thesis in practitioner language. The skill is a durable, inspectable, versioned repo artifact.

3. **[spec-mining-as-codification](../notes/spec-mining-as-codification.md)** — exemplifies. Mining commit history and past security patches for IDOR patterns, then encoding them as a detection skill, maps directly to the spec mining workflow: observe behavior, identify regularities, extract rules, re-run with constraints.

4. **[inspectable-artifact-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md)** — exemplifies. The skill file is diffable, versionable, collaboratively refinable. The `npx skills add` distribution model treats skills as inspectable artifacts.

5. **[constraining-during-deployment-is-continuous-learning](../notes/constraining-during-deployment-is-continuous-learning.md)** — exemplifies. Iterative refinement through false positive analysis is constraining during deployment per Simon's definition.

6. **[Both narrowed and use-shaped artifacts trade generality for reliability, speed, and cost](../notes/constraining-and-extraction-both-trade-generality-for-reliability.md)** — exemplifies. The same material can be reshaped for different consumers (Cramer plans performance prediction next), the resulting skill cannot reconstruct the source, and the source persists.

One synthesis opportunity flagged: skills abstracted from external domain artifacts have different staleness and maintenance properties from skills worked out from co-maintained methodology. When the source is OWASP guidance or commit history, different mechanisms are needed to detect when the skill has drifted from its source.

## Extractable Value

1. **Skill-from-domain-knowledge as a distinct pattern.** Cramer's skills are abstracted from domain artifacts (commit history, security patches, external standards), not derived from methodology. This is a concrete instance of the note's own caveat, with enough production detail to reason about the different authority and fallback regimes. [quick-win] — update the existing skills-derive note with this as an external `evidenced-by` link.

2. **Source material selection matters more than prompt engineering.** Cramer's key insight is that feeding the right source material (trustworthy, domain-specific) produces dramatically better skills than prompting for generic capability. The accuracy improvement comes from input selection, not output tuning. For evidence-to-rule abstraction, the "what to extract" question depends heavily on "what to feed in." [just-a-reference]

3. **Quantified false-positive reduction across iterations.** Two refinement iterations took the system from noisy to 8/17 validated (47% precision). This is rare — most practitioner reports don't quantify the improvement trajectory. Could inform thinking about expected iteration counts for deploy-time learning. [just-a-reference]

4. **Skill distribution as package management (`npx skills add`).** Skills as installable packages from a repo. This is a concrete implementation of skill portability that our KB hasn't explored. Can a skill abstracted from one organization's domain artifacts transfer to another organization? [experiment] — worth tracking but not directly actionable for our methodology.

5. **Professional pen testing missed what domain-specific LLM scanning found.** This is a strong claim about the complementarity of LLM-based detection (broad pattern matching across large codebases with org-specific context) vs. traditional security review (deep but narrow, lacking full codebase context). [just-a-reference] — interesting but tangential to our core concerns.

6. **The "skill-writer" meta-skill.** Cramer packaged the source-driven skill-synthesis process itself as a skill. Could Commonplace's ingestion and connection workflows likewise be packaged as transferable skills? [deep-dive] — the comparison requires more information about how the skill-writer actually works.

## Limitations (our opinion)

**What is not visible:**

- **Sample size of one codebase.** Warden was tested on Sentry — a large, mature Python/Django application. The 8/17 hit rate may not transfer to different architectures, languages, or security vulnerability classes beyond IDORs. Cramer acknowledges planning to expand to performance prediction, but hasn't yet demonstrated the technique outside security.

- **No comparison to simpler baselines.** Would a carefully prompted Claude Code session with the same source material but without the skill-synthesis machinery produce meaningfully worse results? The value of the skill-writer packaging vs. simply feeding the material into a long prompt is asserted, not measured.

- **Survivorship bias on the refinement process.** Cramer reports two iterations that worked. We don't see: how many source material combinations were tried and discarded, how much Cramer's own security expertise guided the iteration (would a non-security-expert get the same results?), or whether the technique has a floor below which it doesn't help.

- **The "years undetected" claim lacks context.** Eight vulnerabilities "undetected for years" despite pen testing is striking, but we don't know the severity distribution, whether they were in code paths pen testers examined, or whether the pen testing scope was comparable to the LLM scan scope (full codebase vs. targeted assessment). The [spec-mining note](../notes/spec-mining-as-codification.md) would frame this as: the LLM scan covered a broader surface than targeted pen testing, not that it was deeper on the same surface.

- **Maintenance story is absent.** "Skills are just files in a repo" addresses versioning and collaboration but not staleness. When Sentry's codebase evolves, how does Warden's skill stay current? When OWASP updates its guidance, does the skill need re-synthesis? [The two-layer execution model](../notes/theory-and-methodology-form-a-two-layer-execution-system.md) requires judgment-dependent reshaping to carry lineage and managed-staleness review, and Cramer's external sources are harder to maintain than internal methodology.

## Recommended Next Action

Done: deep related-systems review written at [getsentry/skills](../agent-memory-systems/reviews/getsentry-skills.md), focusing on the skill-writer meta-skill and source-driven skill synthesis rather than the trivial observation that skills are reshaped from source material. The review covers: source-driven synthesis with depth gates, labeled iteration, description-as-trigger optimization, the Agent Skills cross-tool spec, and borrowable patterns for our own skill creation process.
