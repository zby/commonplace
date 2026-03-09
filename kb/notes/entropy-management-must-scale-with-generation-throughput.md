---
description: In agent-maintained systems, cleanup throughput must match generation throughput — agents replicate existing patterns including bad ones, so without proportional maintenance, quality degrades as a function of output volume
type: note
traits: [has-external-sources]
areas: [kb-design]
status: seedling
---

# Entropy management must scale with generation throughput

When agents produce artifacts (code, notes, links), they replicate existing patterns — including bad ones. A codebase with inconsistent naming conventions gets more inconsistent. A KB with vague link semantics gets more vague links. The replication is not random; agents amplify whatever patterns are most visible in context, which means entropy compounds with volume.

This creates a scaling requirement: cleanup throughput must be proportional to generation throughput. If it isn't, quality degrades as a function of output volume, not as a function of time.

## Evidence

OpenAI's Codex team found this empirically at 1M LOC scale. Early on, engineers spent 20% of their time on "AI slop cleanup" — manual Friday sessions fixing drift. The fix was not working harder but matching throughput: background cleanup agents that continuously scan for pattern violations and open small refactoring PRs, most auto-merged. "Garbage collection for code quality" — a continuous process, not a periodic chore. The transition from manual Fridays to automated cleanup is [spec mining](./spec-mining-as-crystallisation.md) completing: observe drift patterns, extract standards, crystallise into automated enforcement. ([Harness Engineering](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md))

The [stagnation finding](./methodology-enforcement-is-stabilisation.md) from the context engineering study reinforces this from the negative direction: 50% of AGENTS.md files were never changed after creation. These are systems where maintenance throughput is zero — and instructions accumulate without pruning.

## Implications for this KB

The KB already has the pieces — [maintenance operations](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) (what to clean), [external triggering](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md) (when to trigger), [staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) (how to detect). What it lacks is the scaling commitment: as note production increases (especially if [boiling cauldron mutations](./automating-kb-learning-is-an-open-problem.md) are automated), the maintenance operations must run at matching frequency. Orphan detection, connection quality checks, and staleness sweeps need to become continuous, not periodic.

The pruning asymmetry makes this urgent: even in actively maintained systems, additions outnumber removals 6:1. Without deliberate pruning discipline, the KB grows noisier with every note added — and noisy links cause [credibility erosion](./quality-signals-for-kb-evaluation.md) that degrades the entire navigation infrastructure.

---

Relevant Notes:

- [methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) — connects: the stagnation evidence (50% write-once, 6:1 add-to-remove ratio) is what happens when maintenance throughput is zero
- [spec mining as crystallisation](./spec-mining-as-crystallisation.md) — mechanism: the transition from manual cleanup to automated enforcement is spec mining applied to maintenance — observe drift, extract pattern, crystallise into check
- [maintenance operations catalogue](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — operationalizes: the catalogue lists what needs scaling; this note argues it must scale proportionally with generation
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — constrains: if boiling cauldron mutations are automated, maintenance must be automated at matching throughput or quality degrades
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — detects: the credibility erosion failure mode is what happens when entropy management falls behind generation
- [Harness Engineering](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — primary evidence: 1M LOC agent-generated codebase where background cleanup agents maintain quality at generation-matching throughput

Topics:

- [kb-design](./kb-design.md)
