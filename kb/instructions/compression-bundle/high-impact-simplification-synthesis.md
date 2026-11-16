---
description: "Synthesize a compression review into at most three high-level simplifications that materially improve the artifact but still require authorial judgment"
type: types/instruction.md
depth: 4
---

# Synthesize high-impact simplification opportunities

Read the complete artifact and the individual compression findings. Report only opportunities likely to materially improve a reader's understanding of the central claim, conceptual structure, or argumentative flow. Do not edit the artifact.

An opportunity qualifies when its benefit would be large but its implementation requires broader judgment. Typical cases include surfacing a buried thesis, making the role of a load-bearing paragraph explicit, combining several local findings into one deletion or fold, or reorganizing an explanation whose current sequence hides the argument. Exclude local wording improvements, cosmetic changes, minor compression, and alternatives that are merely different.

The synthesis may combine several gate findings or identify a global reorganization visible only after reading the artifact as a whole. Ground every opportunity in the artifact or the gate findings; do not invent a stronger thesis for the artifact to serve.

Distinguish a buried contribution from an undetermined one. A contribution supported by the artifact can be surfaced or given a clearer role. If the artifact does not select among materially different theses, audiences, or purposes, report the missing choice under `Preserve or decide`; do not choose one merely to make the prose cohere. This isolated synthesis receives no retained-intent input, so do not import the choice from the topic, a bare writing prompt, or ambient conversation. The calling workflow may later resolve it from explicit user direction or a separate memory input. A [bare writing prompt does not determine its intended contribution](../../theory/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md).

If the simplification depends on choosing among materially different meanings, conceptual roles, evidence claims, or substantive conclusions, name that unresolved choice as a prerequisite. Do not resolve it as a compression edit. Semantic gates or the author must settle it first.

Return zero to three opportunities. For each one, give:

- the location and smallest useful quotation or section range;
- the important reader problem;
- the direction a revision could take;
- the compression findings it combines, if any; and
- the meanings, implications, or structural choices the author must resolve or preserve.

Do not present a rewrite as settled. A short candidate formulation may illustrate the opportunity, but label it as one possible resolution. Keep fact-checking, claim evaluation, and general completeness review outside this synthesis unless they are necessary to explain why the simplification cannot safely proceed.

## Running it alone

The [compression bundle](../run-compression-bundle-on-note.md) applies this synthesis after its four checks, under the bundle's own output contract. The inputs and output below apply when the synthesis runs alone.

### Inputs

The compression findings are explicit input files, one per check, such as the four check results under `kb/reports/state/review/results/<note-path>/`. Run the synthesis alone:

```bash
commonplace-review run gates NOTE --criteria compression-synthesis \
  --input core-claim-obscured=PATH --input branch-bloat=PATH \
  --input detail-overhang=PATH --input marginal-value-redundancy=PATH
```

Use only the supplied findings. Do not run a check, and do not look for other findings. The run keeps its result as a retained observation and writes no current result, because no freshness hash covers the supplied findings.

### Output

The caller names the output file. Write only that file; mutate nothing else. The output is a [review result](../../types/review-result.md) fragment with `outcome: report` and no `attack-outcome`. Each opportunity is one finding, zero to three in all. Give it `scope: passage` with its smallest useful quotation, or `scope: document` with no quotes for a section range or a cross-cutting change. Its `reason` states the reader problem and the direction.

```markdown
---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["<smallest useful quotation>"]
    reason: "<reader problem>; <direction a revision could take>"
outcome: report
---

# Simplification synthesis: <note title>

## Opportunities

### 1. <short opportunity name>

- Location: <heading and quotation or section range>
- Combines: <the compression findings, or "cross-cutting">
- Preserve or decide: <meanings, implications or structural choices the author must resolve or preserve>
```

Write `None` under `## Opportunities` when no opportunity clears the threshold.
