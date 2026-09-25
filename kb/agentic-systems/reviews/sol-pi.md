---
type: note
description: SoL-Pi wraps Pi with optional fused actions, recoverable observations, checked diagnostic excerpts
  and plan-driven native compaction
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-24-sol-pi-01
source-identity: https://github.com/NVlabs/SoL-Pi
reviewed-revision: 1559b5cb12c72da4a485bc50fe326586b216fb19
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-24-sol-pi-01/result.md
analysis-result-sha256: 328605b07b77b380803f5f23dd26ae7147b0fd9baa44755a1d88aaaa8aa51caa
---

# SoL-Pi

**Evidence basis:** source code and repository documentation at [NVlabs/SoL-Pi commit 1559b5c](https://github.com/NVlabs/SoL-Pi/tree/1559b5cb12c72da4a485bc50fe326586b216fb19), inspected 2026-09-24; no live execution or causal efficiency experiment.

SoL-Pi is an extension for Pi that packages four optional efficiency mechanisms. All are disabled by default. It owns tool wrappers, context transforms and compaction scheduling; Pi owns the main agent loop, permission envelope, model transport and native summary generation. Its README attributes the mechanisms to historical auto-research, but that research process is outside this release boundary.

Action Fusion lets a model request an edit or write followed by a shell command without an intervening model call. A per-file queue serializes this extension's operations, and two hashes around a yield detect some intervening changes. Mutation failure skips the command; command failure leaves the mutation in place. This is neither transactional rollback nor a global filesystem lock. [Implementation](https://github.com/NVlabs/SoL-Pi/blob/1559b5cb12c72da4a485bc50fe326586b216fb19/src/sol-pi/extensions/action-fusion/then-run.ts).

ObservationPack archives eligible large successful text results, keeps their first two full context sends, and then projects a handle with a bounded excerpt. `obs_recall` retrieves bounded exact slices from the current session archive. The stored history and outgoing projection are different objects: shortening one does not erase the other. Recall availability still depends on the local archive and host session contract. [Projection implementation](https://github.com/NVlabs/SoL-Pi/blob/1559b5cb12c72da4a485bc50fe326586b216fb19/src/sol-pi/extensions/observation-pack/index.ts).

The Evidence-Preserving Reducer archives eligible diagnostic logs and asks a configured model to select quotations. It checks source identity, status, schema, quotation occurrence and size before replacing the tool result with a shorter receipt. These checks establish provenance of selected text, not completeness or correct diagnostic labels. The receipt leaves diagnosis and repair with the main agent and affords raw-log readback through Bash. Handled model/validation failures preserve the original result; archive errors occur outside that fallback and depend on Pi's hook handling. [Reducer](https://github.com/NVlabs/SoL-Pi/blob/1559b5cb12c72da4a485bc50fe326586b216fb19/src/sol-pi/extensions/evidence-preserving-reducer/index.ts), [receipt checks](https://github.com/NVlabs/SoL-Pi/blob/1559b5cb12c72da4a485bc50fe326586b216fb19/src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts).

Online Context Compact retains plan status and request/context statistics. Completed plan steps can trigger a cost/window calculation, followed by native compaction after the current run settles. Success triggers a new turn with a generic instruction to rebuild the remaining plan. Plan completion is model-declared, not independently verified. Retained progress wording has no established later model reader on the custom-state route; native summary contents and replay selection remain host-owned. [Compaction control](https://github.com/NVlabs/SoL-Pi/blob/1559b5cb12c72da4a485bc50fe326586b216fb19/src/sol-pi/extensions/online-context-compact/extension.ts).

The strongest supported result is the wiring of recoverable evidence and adaptive context scheduling. Diagnostic receipts, native compaction continuation and persistent scheduling statistics meet the analysis's trace-learning criterion, without establishing improved capacity. The economic formula is an operative, inspectable prediction; runtime updates change its inputs, not its content. Criticism-driven improvement and self-improvement of the released extension remain uninspected. Narrow operational reflection is wired: prior compaction count and cache debt represent its own operations and change later scheduling. This does not establish a reflective theory builder.

Compatibility documentation reports deterministic fake-provider checks and explicitly excludes live token-savings claims. Measured savings, preserved task quality and downstream dependence on recalled evidence require additional execution evidence. The extension also supplies no sandbox: it runs with Pi's permissions.

- [Exact analysis and canonical evidence](../../reports/retained/agentic-system-analysis/AAS-2026-09-24-sol-pi-01/result.md) — see-also.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: the limited state-to-policy mapping above.
- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: why retained traces alone do not establish criticism-driven improvement.
