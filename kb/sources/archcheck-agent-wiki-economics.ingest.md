---
description: "Archcheck reports cheaper agent lookups with one cross-file map, but not 28 mirror pages; the small A/B study bounds substitution benefits without establishing lifecycle break-even."
source: https://github.com/blurman-ai/archcheck/blob/master/docs/research/agent_wiki_economics.md
captured: "2026-11-09"
capture: github-raw-markdown
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: c3350fd5a80cf1ca762d998ffd178120fb64113734f76ec5126568fdc8084339
ingested: "2026-11-09"
type: types/ingest-report.md
domains: [agent-wiki-economics, repository-maps, marginal-token-cost, staleness-lint]
---

# Ingest: When does an agent wiki pay for itself?

## Classification

A repository-local engineering report with small A/B measurements, transcript observations, and a revised documentation design, rather than a scientific paper or a benchmark of the OpenWiki package.
Author: the write-up is hosted in blurman-ai's archcheck repository and describes the project's own implementation and trials. Its credibility signal is the stated isolation, audit, and ground-truth procedure; the underlying transcripts and code were not independently inspected for this ingest.

## Summary

Archcheck tested whether derived repository documentation reduced coding-agent lookup costs. A 28-page wiki did not improve on code search: agents either read both wiki and code, or consumed wiki pages larger than the small source files they replaced. The replacement was one directly routed map aggregating facts across files, consumed without query-time source verification and maintained with source-change lint. In this bundled design, four lookups cost a reported 13.8k marginal tokens versus 27.3k for code search, with four versus ten tool calls and all answers correct; a five-part reconnaissance probe cost 7.2k versus 16.5k, with one versus twelve calls and both arms correct. Each cell used one fresh Sonnet agent. The report motivates cross-file aggregation and separate freshness work, but does not isolate their individual effects or measure construction-and-maintenance break-even. Code inspection remained necessary for modifications and exposed a missing detail in the map.

## Quotes

> **Trial 1 — wiki with "verify against code" discipline: no effect.** Same tool
> calls (10 vs 10), same tokens. Transcripts showed why: on half the questions the
> agent read the wiki page *and then opened the source anyway*, because every page
> says "derived — never trust over code". A cache you must re-verify on every read
> saves nothing. Either the wiki is trusted at query time (with freshness maintained
> separately), or it should not exist.
> --- `kb/sources/.snapshots/archcheck-agent-wiki-economics.md` @ `sha256:c3350fd5a80cf1ca762d998ffd178120fb64113734f76ec5126568fdc8084339`

> **Measurement error found and fixed.** Raw per-agent token counts looked flat
> across arms. Two null agents (one doing nothing, one making two trivial calls)
> showed why: a do-nothing agent already costs 24.3k tokens (system prompt, tools,
> project context), and each tool call adds ~0.7k. Raw totals were ~80% constant.
> All numbers below are marginal (total − 24.3k).
> --- `kb/sources/.snapshots/archcheck-agent-wiki-economics.md` @ `sha256:c3350fd5a80cf1ca762d998ffd178120fb64113734f76ec5126568fdc8084339`

> Deleted 27 of 28 pages. Kept a single dense map (`docs/openwiki/index.md`,
> ~130 lines) containing only facts that no single repo file states: a routing
> table to authoritative docs, exit codes, the gate policy across all three modes
> (including the deliberate check-vs-`--diff` divergence), a full rule registry
> (id, exact message, threshold, impl, test, fixture — 18 rows, literals
> grep-verified), and the subsystem matrix. Entry is zero-hop: `AGENTS.md` /
> `CLAUDE.md` point straight at it. The lint and `last_checked_commit` stay as the
> freshness loop, so the map can be trusted at query time.
> --- `kb/sources/.snapshots/archcheck-agent-wiki-economics.md` @ `sha256:c3350fd5a80cf1ca762d998ffd178120fb64113734f76ec5126568fdc8084339`

> Lookup questions (4, marginal tokens, sums; correctness 4/4 in every arm):
>
> | arm | tool calls | tokens | wall-clock |
> |---|---|---|---|
> | grep the code | 10 | 27.3k | 93.7s |
> | 28-page wiki, verify | 10 | 27.6k | 92.3s |
> | 28-page wiki, trust | 10 | 29.8k | 60.2s |
> | **one-page map, trust** | **4** | **13.8k** | **31.4s** |
> --- `kb/sources/.snapshots/archcheck-agent-wiki-economics.md` @ `sha256:c3350fd5a80cf1ca762d998ffd178120fb64113734f76ec5126568fdc8084339`

> n = 1 agent per cell; one model (Sonnet); wall-clock is noisy. The four lookup
> questions predate the map's design, but the map was shaped by the same experiment
> that then re-measured it — the #168-style recon probe was added as a check against
> that bias. Absolute savings per question are small (a few thousand tokens); the
> relative numbers are what scale.
> --- `kb/sources/.snapshots/archcheck-agent-wiki-economics.md` @ `sha256:c3350fd5a80cf1ca762d998ffd178120fb64113734f76ec5126568fdc8084339`

## Connections Found

The source is bounded supporting evidence for [LLM recompute cost shifts the store-vs-recompute balance](../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md): materialization lost when it added expensive reads, while a directly routed cross-file map consumed without source rechecking reduced reported query costs. That bundled comparison illustrates the substitution boundary, not a general victory for persistent caches or a comparison against on-demand symbolic derivation. It also supplies a concrete case for [An insufficient summary precedes the source rather than replacing it](../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md): verify-arm transcripts reportedly showed wiki reads followed by code reads on half the questions. This supports counting displaced work rather than page production; it does not show that verification always erases savings or that the trusted map met every task's reliability requirement.

## Extractable Value

1. **A losing-and-winning materialization case.** The 28-page wiki failed even when code reads were forbidden; the directly routed, cross-file map then reduced reported lookup costs. This adds an external example to the existing recompute ledger: compare the actual question-answering routes, not the existence or size of a documentation corpus. Aggregation, entry routing, and reliance changed together, so the result supports the tested bundle rather than a universal compression threshold. [quick-win]
2. **Separate use-phase overhead from investment costs.** Null agents revealed a reported 24.3k-token baseline, around 80% of raw totals. Subtracting that baseline exposed incremental differences, but neither marginal tokens nor query latency prices authoring, refresh work, or actual billing/cache behavior. A reusable evaluation should report baseline and incremental costs alongside a separate lifecycle ledger. [experiment]
3. **Freshness signals create review work without proving truth.** Eight wiki pages were flagged on the same day after cited files changed, including unrelated changes. This illustrates the maintenance burden of file-granularity dependencies. The lint checks paths and source changes, not every claim's correctness; the reconnaissance probe itself exposed an omitted rule-id attribution detail. These observations are useful when evaluating whether a map can be relied on for orientation rather than modification. [just-a-reference]

## Limitations (our opinion)

There is one agent per cell, one model, four lookup questions, and one additional probe. No repeat-run dispersion is reported, and wall-clock measurements are noisy. The map was shaped during the experiment that evaluated it; the added probe reduces but does not remove concern about task-specific tailoring. All reported answers were correct, yet the deeper code-search probe found a gap in the map. Equal scores on these questions therefore do not establish equal reliability across future work.

The winning arm bundles page consolidation, cross-file aggregation, direct entry, and permission to rely on the map. The trust-only 28-page arm tests removal of code reads within that representation; its null result does not independently identify the cause of the one-page gain. The proposed multiplicative savings formula is a design hypothesis, not an identified law. Source-change lint likewise cannot establish semantic correctness merely because no dependency changed.

Despite the title's investment question, the write-up does not quantify construction tokens or ongoing maintenance effort, estimate reuse volume, or calculate a break-even horizon. Its results concern query costs in a small, greppable repository, not total wiki economics or large heterogeneous corpora. Claims about what external wiki advocates promise are the author's interpretation and were not independently checked here.

## Recommended Next Action

Add this bounded external case to the evidence discussion in [LLM recompute cost shifts the store-vs-recompute balance](../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md), preserving the bundled intervention, one-agent-per-cell design, and unpriced lifecycle costs.
