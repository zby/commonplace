---
description: "Large-scale Claude Code plugin study finds shifted commit semantics and maintenance coupling between scripts and runtime instructions."
source: https://arxiv.org/abs/2608.28497
captured: "2026-09-03"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 4409153d9f9d6f56327b6940c165751a3d9814094ee9352d216738f2b1e881d3
ingested: "2026-09-03"
type: kb/sources/types/ingest-report.md
domains: [agent-plugins, software-maintenance, instruction-artifacts, empirical-software-engineering]
---

# Ingest: Maintenance and Co-evolution of Claude Code Agent Plugins

## Classification

An arXiv v1 scientific paper that combines repository mining, statistical tests, manual open coding, and LLM-assisted classification to characterize one young software ecosystem. Its empirical base covers 1,926 public GitHub repositories, 8,351 locally resolvable plugins, and 77,773 plugin-touching commits, with narrower samples for commit and pull-request classification.
Author: Ahmed Hereiz, Yingzhe Lyu, Hao Li, Bram Adams, and Ahmed E. Hassan are affiliated with Queen's University's Software Analysis and Intelligence Lab. The paper exposes its collection method, prompts, agreement measures, sensitivity checks, and a public replication-package URL, which makes the reported analysis inspectable even though this ingest did not independently reproduce it.

## Summary

The paper provides a first large-scale maintenance baseline for public Claude Code plugin marketplaces through March 2026. It finds rapid early growth, a 61.3% concentration in software-engineering plugins, and a development history dominated by feature, fix, and chore commits. Its strongest result for Commonplace is that AI-facing Markdown is not ordinary documentation: commits labeled `docs`, `style`, `perf`, or `refactor` often change runtime instructions, and scripts within `skills/` co-change with Markdown above chance. Manual review classifies 78% of 64 sampled Script–Markdown co-changes as functionally coupled through interface, internal-logic, value/version, or repository-structure changes. The study is useful as population evidence for a mixed natural-language and symbolic maintenance problem, but it does not measure whether synchronized changes improve agent behavior or whether unsynchronized changes cause failures.

## Quotes

No source quotes have been retained yet.

## Connections Found

This paper is a population-level empirical anchor for treating AI-facing Markdown as a [system-definition artifact](../notes/definitions/system-definition-artifact.md): its runtime consumption path, rather than its file extension, determines that an edit can change behavior. It supplies repository-scale maintenance evidence for the natural-language and symbolic pairing in [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), without establishing that note's broader optimization claims. Compared with [Context Engineering for AI Agents in Open-Source Software](./context-engineering-ai-agents-oss.ingest.md), it directly studies code–instruction co-change inside plugins; compared with [Harness-IF](./harness-if-instruction-following-across-instruction-surfaces.ingest.md), it measures how behavior-shaping instruction surfaces are maintained rather than whether those instructions affect agent behavior. The stale instruction/runtime mismatches documented for [Fractal](../agentic-systems/fractal.md) and [beads-rust](../agentic-systems/beads-rust.md) are concrete comparison cases, but this paper does not connect its aggregate co-change patterns to observed failures.

## Extractable Value

1. **Classify agent-facing text by runtime role, not by extension or commit label** -- The reclassification study shows that Markdown edits labeled as documentation can add or correct behavior when the agent reads the file at runtime. This is population evidence for applying the system-definition distinction during review and maintenance. [quick-win]

2. **Treat Script–Markdown consistency as a bounded mixed-form maintenance problem** -- Above-chance co-change within `skills/` and the four observed coupling mechanisms operationalize one part of the readable-artifact loop: script interfaces, behavior, identifiers, and paths can each require matching instruction changes. [deep-dive]

3. **Use the coupling taxonomy as a candidate audit surface** -- Interface changes, internal-logic changes, value/version synchronization, and repository restructuring define four concrete checks that an instruction-aware pull-request reviewer could test. The paper proposes consistency tooling but does not evaluate such a reviewer, so this remains an experiment target. [experiment]

4. **Adjust raw co-change rates for artifact prevalence before inferring coupling** -- Skills co-change with other component types in 43.2% to 56.6% of relevant pull requests, yet their lift remains below one because skills are common. Only the Agents–Commands pair exceeds chance at the component level. This distinction is a reusable warning for maintenance analyses. [quick-win]

5. **Revalidate software taxonomies when the primary behavioral artifact changes form** -- Conventional commit labels preserve ambiguous developer intent across instruction edits, and classifiers based on ordinary source-code repositories can misstate the work performed. Diff role and runtime authority are necessary classification inputs. [quick-win]

6. **Keep the marketplace figures as a dated Claude Code baseline** -- The 8.8-fold six-month commit growth, 61.3% software-engineering share, 34.4% multi-component share, and 34.9% detected Claude co-authorship describe an early, platform-specific observation rather than a stable agent-plugin ecosystem law. [just-a-reference]

## Limitations (our opinion)

The fixed decomposition limits what the classifier results establish. The plugin classifier can condition on names and descriptions; the commit classifier can use messages, file roles, and change metadata or sampled diffs; and the coupling classifier receives Script–Markdown diffs. Their available operation is to assign one response from the supplied functional, Conventional Commit, or coupling labels. Their hypothesis classes therefore express mappings only into those taxonomies and rubrics. Repository discovery, the public-GitHub and star filters, Claude Code's component schema, the file-role partition, the commit and pull-request units, the modification-only co-change filter, the sampled strata, and the label vocabularies all remain fixed outside those mappings. Agreement with human labels supports classification inside this design; it does not show that the fixed categories are complete or preferable, as [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). The 5-, 10-, and 25-star sensitivity analysis varies only the star threshold and cannot validate the other fixed choices.

The co-change analysis is observational. An above-chance association can show recurring coordinated maintenance, but it cannot establish that every paired edit was required, that a missing paired edit produced a defect, or that the script change caused the Markdown change. The study selects pull requests in which both files changed and therefore does not estimate the prevalence of changes that should have been synchronized but were not. It also evaluates no downstream agent behavior, so the claim that stale instructions cause silent defects remains plausible mechanism rather than measured outcome.

The findings are bounded to a rapidly growing Claude Code ecosystem collected in April 2026. Private, deleted, low-star, external-source, and non-GitHub plugins are excluded; the median repository age is only 80 days; and later marketplace structure may differ. The manual samples are modest, the reported inter-rater and classifier agreement leaves ambiguous cases, and LLM classifications can be prompt- and model-sensitive. Authorship trailers and related heuristics miss uncredited agent use, so the reported Claude co-authorship rate is a lower-bound-style detection count rather than a complete measure of AI involvement.

## Recommended Next Action

Write a note titled "Maintain agent-facing text by runtime role, not file extension" that synthesizes this population evidence with the context-file evolution study and the Fractal and beads-rust drift cases, while keeping its empirical scope limited to Claude Code plugins until the pattern is replicated elsewhere.
