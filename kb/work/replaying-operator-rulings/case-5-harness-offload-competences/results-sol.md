# Case 5: either extra input separated harness work from model judgment in both Sol drafts

2026-11-24. Two fresh drafts per condition. In all six drafts given architecture notes, a component-attribution rule, or both, the writer left mechanical work to the harness and narrowed the model's role accordingly. Neither baseline draft made the full distinction. Explicitly calling the split a hypothesis varied between repeats.

| Condition | Drafts: offloading / hypothesis | Full offloading (agreed) | Explicit hypothesis (agreed) |
|---|---|---:|---:|
| C — baseline | d03: P/W; d07: M/U or P/U | 0/2 | 1/2 |
| R — two architecture notes | d04: H/W; d06: H/U | 2/2 | 1/2 |
| A — component-attribution rule | d01: H/U; d05: H/U | 2/2 | 0/2 |
| RA — both | d02: H/U; d08: H/U | 2/2 | 0/2 |

H = full separation, P = partial, M = missed; W = explicitly hypothetical, U = unqualified. The two blind scorers agreed on 15 of 16 dimension grades. Both saw d07 give replay execution to the harness while leaving update availability and provenance to the model. Scorer 1 graded this a miss; scorer 2 gave partial credit. Neither counted it as full separation.

The rule alone worked twice without the two notes; the notes alone worked twice without the rule. That supports trying either intervention, not preferring one or diagnosing the original live miss. Only d04 met both targets. The common collection rule yielded an explicit hypothesis in 2/8 drafts; neither extra input explicitly prompted one. Two repeats can show a difference, not estimate its frequency reliably.

## Run and evidence

Operator-requested variant of the [frozen design](./design.md): `openai/gpt-6.2-sol` at medium effort through Pi instead of Opus through Claude, two writers per condition instead of three. The original predictions were for three Opus drafts per condition. The commission, packet assembly, randomized anonymous IDs, and rubric were unchanged except for the scorer's ID count. Each call started in an empty directory with tools, MCP, extensions, skills, context files and session persistence disabled. Two fresh Sol scorers each received all eight drafts in independently shuffled order. All ten calls completed without retries.

KB inputs pinned to `785ffc64a`; the reconstructed article came from the case materials. SHA-256 of the assembled base packet: `f778808f5632b4d183259e5fc0183d4f3d68104011d006765dcfbf62d15bd3d0`; of the retrieval supplement: `6027bf98011ddb968be9dc46850b55c0a100367c14d42b9c44350e2d4ac53e06`.

[Retained drafts](./positive-evidence/) are the seven with an agreed H or W. Baseline d03 is evidence for W only. The disputed d07 had neither agreed target hit and is not retained.
