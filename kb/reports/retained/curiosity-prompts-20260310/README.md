# Curiosity prompts experiment — March 10, 2026

This set preserves the completed Decapod prompt comparison used by the
[agent-curiosity and structural-coherence investigation](../../../work/agent-curiosity-and-structural-coherence/README.md)
to select and interpret later prompt experiments. Its report also records
the episode discussed in [prompt ablation converts human insight to deployable
framing](../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md).

## Evidence

- [Experiment report](./captures/experiment-report.md) — method, target finding, twelve-run result table, interpretation, and proposed review prompt.
- [Prompt specification](./captures/prompts.md) — the six tested framings.
- [Reconstructed input](./captures/decapod-original.md) — the report supplied before the mechanistic objection was investigated.
- Saved investigation outputs: [curiosity](./captures/decapod-investigation-1.md), [cost/benefit](./captures/decapod-investigation-prompt2.md), [implementation check](./captures/decapod-implementation-check.md), [claims audit](./captures/decapod-claims-audit.md), and [source audit](./captures/decapod-source-audit.md).

## Interpretation limits

The report describes six prompts tested twice each. It records the target
finding in both cost/benefit trials and a broader, variable set of findings
from curiosity prompts. Two trials per framing do not establish stable
activation rates or a general ranking of prompts. The report's stronger
reliability language is preserved as historical interpretation.

The set contains five saved investigation documents, not twelve separately
identified run outputs. It does not provide a complete run-to-output map,
model versions, or a pinned Decapod source revision. The prompts name the
local checkout used at the time; that path does not reproduce its historical
state. The result table also gives different numerical treatment to entries
labelled Partial across prompt rows. Preserve those reported values as-is;
do not infer an unstated scoring rule or silently recompute them.

## Retention

Keep the captures unchanged for comparison with later experiments. Their
embedded recommendations and old type declarations are captured data, not
current procedures or live library claims. The validation-ignore marker
separates them from collection validation. Corrections or new interpretations
belong outside the captures. This is a completed experiment record, not an
active research plan.
