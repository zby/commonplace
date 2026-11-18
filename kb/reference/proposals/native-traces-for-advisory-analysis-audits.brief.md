---
type: types/write-brief.md
description: "Commission for the native-trace audit proposal: preserve the migration option without deciding whether advisory audits are worth keeping."
---

# Brief: Native traces for advisory analysis audits

## Intent

Let a future operator recover the native-trace migration option and its costs without treating this discussion as approval to implement it.

## Must keep

- Separate the value of advisory audits from their trace-storage mechanism. The operator is unsure whether audits have value and has deferred that decision.
- Preserve materially different options, including keeping the current mechanism and disabling audits, without selecting one.
- Keep session ownership, evidence retention and missing-trace behavior visible; avoiding duplicate stdout must not silently weaken audit evidence.

## Must exclude

- A commission to run experiments, migrate trace lookup or remove audits.
- Claims that audit value has been demonstrated or disproved.

## Reserved decisions

- Whether to keep advisory audits, investigate their value, or change their trace source remains with the operator.
