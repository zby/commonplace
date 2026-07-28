# Description-length optimization

## Question

What description-length contract gives Commonplace the best retrieval decisions for its context cost, now that complete generated listings are no longer on the agent read path?

The former 50–200-character warning band was not derived from a retrieval evaluation. The upper bound inherited an earlier full-index cost concern, then tightened while tag indexes were expected to carry complete membership. Tag READMEs are now selective by default, but descriptions still appear in scoped `rg` result slices and build-time listings. The old rationale weakened rather than disappeared.

## Goal

Produce an evidence-backed description-length policy that says:

- what is being optimized;
- which description consumers and artifact types the policy covers;
- whether one global numeric band is justified;
- what unit and thresholds deterministic validation should use;
- which semantic properties remain review concerns rather than length checks.

The policy must optimize the title/path-plus-description pointer as a retrieval decision surface, not description length in isolation.

## What would close this workshop

All of the following:

1. A retrieval assay compares controlled description variants across small result sets and large scoped slices.
2. The results report relevant-artifact recall, unnecessary full reads, downstream task success, and pointer-context cost.
3. A decision chooses one global band, type-specific bands, or no numeric upper bound, with an explicit result-set budget.
4. The durable decision lands in the appropriate system artifacts—an ADR if architectural, plus the type/schema, tests, authoring instructions, and command documentation affected by it.
5. Existing over-limit descriptions are migrated only if the decided policy makes them actionable warnings.

Then delete this workshop and remove its entry from `kb/work/README.md`.

## Evaluation boundary

In scope:

- Fixed note descriptions as read/skip pointers.
- The marginal information a description adds beyond its title or displayed path.
- Current agent consumers: plausible-hit triage and scoped path-plus-description listings.
- Human-facing build-time listings as a secondary consumer.
- False skips, false opens, downstream task success, scan cost, and authoring failure modes such as summary creep.
- Whether characters remain an adequate deterministic proxy for the actual token/byte budget.
- Whether artifact types with different retrieval jobs need different guidance.

Out of scope:

- Replacing `rg` with ranked or semantic search.
- Redesigning tag taxonomy or tag-README weight gates.
- Host-managed skill-description limits, which have a different always-loaded consumer and external constraints.
- Bulk-shortening descriptions before the assay determines which ones are actually defective.

## Current grounding

- The base type defines a description as a discriminating retrieval filter rather than a summary: [note type](../../types/note.md).
- The current schema warns below 50 and above 250 characters: [note-base schema](../../types/note-base.schema.yaml).
- The active navigation path uses descriptions both for five-hit triage and scoped path-plus-description slices: [navigation](../../reference/navigation.md).
- Complete generated listings moved off the agent read path in [ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md).
- Tag READMEs are selective by default and have their own document-weight contract: [tag-readme type](../../types/tag-readme.md).
- Fixed descriptions trade query-specificity for low read cost and reliable availability: [pointer design tradeoffs](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md).

## Starting evidence, not a decision

A 2026-07-27 corpus audit found that among 308 files with descriptions under `kb/notes/`:

- median length was 189 characters;
- 76 descriptions (24.7%) exceeded 200;
- the 90th percentile was 239 and the 95th was 273;
- 23 descriptions (7.5%) exceeded 250;
- 4 descriptions (1.3%) exceeded 300.

The largest tag slice, `learning-theory` at 103 notes, carried about 26,039 characters of title-plus-description payload. Capping its existing descriptions at 200 would save about 1,039 characters—roughly 4% of that payload before path/format overhead. This suggests that 200 currently cuts through ordinary descriptions while doing little to control large-slice cost.

The provisional hypothesis is that 250 may be a better soft warning than 200, while descriptions above 300 are stronger candidates for summary creep. The workshop must be able to reject that hypothesis.

## Decision after assay 1

On 2026-07-27, after reviewing assay 1, the user adopted 250 characters as the global soft upper warning. The lower warning remains 50. This is deliberately warning-level: the assay put 250 on its observed Pareto frontier but did not establish a universal optimum, and ordinary descriptions should still use the shortest wording that changes a read/skip decision.

The workshop remains open for the targeted follow-up identified by assay 1: distinguish whether same-title and same-lineage retrieval failures are better solved by description headroom, explicit artifact-role display, or type-specific guidance.

## Working files

- [measurement-plan.md](./measurement-plan.md) — proposed assay, controls, measurements, and decision rule.
- [assay-1-report.md](./assay-1-report.md) — first controlled retrieval assay, context-budget check, interpretation, and next experiment.
- [cases.json](./cases.json) and [run_assay.py](./run_assay.py) — frozen case definitions, variants, generator, evaluator driver, and scorer.
- [generated/README.md](./generated/README.md) — raw prompts/results and reproduction map for assay 1.

## Bookkeeping

Plain Markdown is sufficient. Preserve prompts, case definitions, raw results, and analysis separately so the decision can be reproduced and challenged. Further contract changes require evidence beyond assay 1 or an explicit user decision.
