---
type: types/note.md
description: MerchantBench ReAct baseline combines action feedback and optional persistent
  notes, with context trimming and source/default limits
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-merchantbench-01
source-identity: https://github.com/KhanCold/merchantbench
reviewed-revision: f44ce969aeccfd65d1eef6afe50f69868e510946
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-merchantbench-01/result.md
analysis-result-sha256: 615a4b3b68f419eb12331d03f36166f166e384ace782fc2743ab7e180b74215b
---

# MerchantBench: ReAct and optional persistent notes

This analysis covers the reference ReAct baseline, its SDK and consumed server admission, observation, memory and trace interfaces. It excludes other agents, simulator market algorithms, private data, evaluation launchers and provider internals. Findings are static and code-grounded at the pinned commit; no benchmark or model was run.

The runtime receives a simulated store observation, asks its configured model for tool calls, submits them to the environment and feeds results into later model invocations. No-call responses and exhausted hop budgets force end_of_step. HTTP410 or a configured operating horizon ends the client. The environment supplies feedback and an outcome metric, while this loop implements no independent oracle for the best business action. [Baseline loop](https://github.com/KhanCold/merchantbench/blob/f44ce969aeccfd65d1eef6afe50f69868e510946/agent/baselines/react_160k_compact_30k.py#L564-L796).

Its 160k-to-30k context maintenance is approximate recent-history trimming. When the write tool is exposed, a reminder invites the model to preserve important details first; trimming follows any HTTP-successful action, including a failed memory write returned as a tool result. With the tool denied, history is trimmed before inference. A single large last message can exceed the nominal history budget, and model tools/system overhead is separate. [Maintenance code](https://github.com/KhanCold/merchantbench/blob/f44ce969aeccfd65d1eef6afe50f69868e510946/agent/baselines/react_160k_compact_30k.py#L483-L562), [trim helper](https://github.com/KhanCold/merchantbench/blob/f44ce969aeccfd65d1eef6afe50f69868e510946/agent/baselines/react_160k_compact_30k.py#L103-L120).

The pinned default enables read_memory_doc and write_memory_doc: their denylist entries are commented out, contrary to the agent README. The optional path lets a model derive run-local Markdown strategy or follow-up notes and request them after raw history has disappeared. It affords per-task online trace learning, without guaranteeing a write, recall or benefit. The current document is overwritten under a 256KiB cap, then history is appended; these are separate file operations. Only current content has the supported read tool. [Default configuration](https://github.com/KhanCold/merchantbench/blob/f44ce969aeccfd65d1eef6afe50f69868e510946/env/scenarios/default.yaml#L190-L199), [scratchpad implementation](https://github.com/KhanCold/merchantbench/blob/f44ce969aeccfd65d1eef6afe50f69868e510946/env/tools/tools.py#L2161-L2227).

Server controls check step freshness when a header is supplied, scenario permissions, argument shape, hook state and quota. The supplied SDK sends the step header. Mutating-call identities/fingerprints support bounded replay control; sequential batch execution and later trace persistence do not establish an atomic whole-turn transaction. Authentication is configuration-dependent. Local stale-step recovery slices history using an old length, which can be weakened by intervening trimming; it does not undo environment effects. [Admission path](https://github.com/KhanCold/merchantbench/blob/f44ce969aeccfd65d1eef6afe50f69868e510946/env/web/routes_agent.py#L1020-L1135), [optional authentication](https://github.com/KhanCold/merchantbench/blob/f44ce969aeccfd65d1eef6afe50f69868e510946/env/web/auth.py#L70-L95).

The strongest supported contribution is a model-action-feedback loop with optional reusable notes and inspectable protocol controls. Prompt-size and failure-state feedback support narrow reflection on runtime state. Conjectural learning and self-improvement remain uninspected: writable strategy text and simulator feedback do not establish criticism of an operative theory with improved future capacity. The [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-merchantbench-01/result.md) retains quotes, branch-specific memory comparison and epistemic limits. Controlled note-recall interventions and fault/replay traces would strengthen separate conclusions.
