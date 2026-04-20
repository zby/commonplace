---
gate_id: prose/confidence-miscalibration
name: Confidence miscalibration
description: 'Speculative frameworks are presented as established, or well-grounded findings are presented with unnecessary tentativeness.'
type: kb/types/instruction.md
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

Speculative frameworks are presented as established, or well-grounded findings are presented with unnecessary tentativeness.

## Test

For each framework, taxonomy, or causal model in the note, ask whether it is sourced or the note's own construction. If it is the note's own move, its wording should propose rather than assert. Report all miscalibrated instances.

Language like `requires`, `consists of`, or `the stages are` asserts. Language like `a plausible decomposition` or `one way to model this` proposes.

Focus on cases where the note makes quantitative or empirical-sounding claims without evidence. Qualitative analytical frameworks (e.g., a taxonomy that decomposes a concept into types) are the note's own analytical moves — hedging words like "at least" or "one useful way" are sufficient. Do not flag qualitative decompositions as miscalibrated merely because they are the note's own construction.
