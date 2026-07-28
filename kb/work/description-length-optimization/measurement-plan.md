# Description-length measurement plan

## Decision to support

Determine the shortest description allowance at which retrieval performance stops materially improving, subject to a context budget for large candidate slices.

The experiment should distinguish three possible outcomes:

1. One global warning band works across Commonplace artifact types.
2. Different retrieval jobs justify type-specific guidance or limits.
3. A numeric upper bound is the wrong control; semantic review plus result-set budgeting should replace it.

## Unit of evaluation

Evaluate the pointer the consumer actually sees:

- H1 title plus description in generated listings;
- path plus description in current scoped `rg` output.

Description quality is marginal to that first component. A description that is redundant after a strong claim title should score poorly even when it is informative in isolation.

## Case selection

Build a stratified set of 40–60 artifacts covering at least:

- theoretical notes with claim titles;
- definitions;
- ADRs and reference documents;
- instructions whose descriptions act as retrieval wires;
- source snapshots or ingest reports if they remain under the shared contract.

Within each type, include short, median, 200–250-character, and over-300-character incumbents. Favor real cases with plausible neighboring artifacts, because random distractors make discrimination artificially easy.

For each target, record a realistic retrieval task or query and the relevant-artifact judgment before producing variants.

## Controlled variants

Produce truthful variants under maximum allowances of approximately:

- 120 characters;
- 160 characters;
- 200 characters;
- 250 characters;
- 300 characters.

These are ceilings, not target lengths. Do not pad a description to consume its allowance. Do not use raw truncation: it confounds length with grammatical damage and omitted sentence endings. Each variant should independently preserve the strongest available mechanism, scope, contrast, or implication.

Have a reviewer reject variants that introduce false claims or change the artifact's scope. Keep rejected variants out of the retrieval comparison rather than treating their failures as evidence against the length band.

## Retrieval conditions

Test at three scales:

| Condition | Candidate set | Question answered |
|---|---:|---|
| Plausible-hit triage | 5 | Can the pointer identify the right artifact among close neighbors? |
| Noisy search | 20–30 | Does extra description detail still help when scanning becomes substantial? |
| Large scoped slice | 75–100 | Does the added information survive attention and justify its aggregate context cost? |

Randomize candidate order and description variant. Run enough repetitions to separate stable effects from sampling noise for the models that actually operate the KB.

The evaluator should select which artifacts to open, with abstention allowed. For a subset of cases, continue into the full task so pointer selection can be connected to downstream success rather than judged only by file choice.

## Measurements

Per trial:

- whether every relevant artifact was selected;
- number of irrelevant artifacts selected;
- abstention or missed-target result;
- confidence, if the runner exposes it consistently;
- pointer characters, bytes, and model-token count;
- full-body tokens subsequently loaded;
- downstream task success for end-to-end cases;
- wall time and inference cost where available.

Aggregate by length allowance, candidate-set size, artifact type, and title strength. Report at least:

- relevant-artifact recall;
- precision or irrelevant-open rate;
- false-skip rate;
- total pointer plus body tokens consumed;
- end-to-end success rate;
- variance across runs and models.

False skips and false opens should not be assigned equal cost automatically. Missing the artifact that carries the needed constraint can be more damaging than opening one extra short note; the final weighting must be stated explicitly.

## Context-budget check

The retrieval assay finds where information value plateaus. A separate calculation checks whether that plateau fits the large-slice budget:

```text
available description tokens per result
  = (pointer-context budget / p95 candidate count)
    - title-or-path and formatting overhead
```

Use a declared pointer-context budget and the observed 95th-percentile candidate count. Do not derive a per-description cap from tag-README document size: curated README weight and query-result weight are different consumers.

If the accuracy plateau exceeds the slice budget, test scope reduction or ranking before compressing every description. The result may show that candidate-set control dominates per-item length.

## Decision rule

1. Plot retrieval quality and total context cost against allowance.
2. Identify the Pareto frontier; discard allowances that cost more without improving retrieval.
3. Choose the shortest allowance whose false-skip and downstream-success results are not materially worse than longer variants.
4. Verify that its p95 large-slice cost fits the declared budget.
5. Split by artifact type only when the measured curves or consumer paths differ materially—not merely because their current length distributions differ.

The decision must state the practical effect of uncertainty. A soft warning can use a less certain threshold than a hard validity rule; absent strong evidence, length should remain warning-level.

## Required durable outputs

Depending on the result, update the relevant subset of:

- `kb/types/note-base.schema.yaml` and schema fixtures;
- validator tests;
- `kb/types/note.md` and any type-specific description contracts;
- `kb/instructions/cp-skill-write/SKILL.md`;
- `kb/instructions/cp-skill-convert/SKILL.md`;
- `kb/instructions/fix-warnings/fix-descriptions.md`;
- `kb/reference/commands.md` and navigation documentation;
- an ADR recording the consumer, budget, evidence, and chosen enforcement level.

Only after those contracts agree should existing descriptions be swept for newly actionable warnings.
