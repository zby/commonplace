---
description: "Apache Maka's separate history, local-memory and atomic-extraction routes, with their consumers and evidence limits"
type: kb/types/note.md
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-05-apache-maka-01
source-identity: https://github.com/apache/maka
reviewed-revision: ece69ab3e7a1629a6073831005711d8aa7160ca4
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-01/result.md
analysis-result-sha256: fcd16d145d4ee6730eedab994478c8a320fd98f79123dd2df145c3cb6b8d3c18
traits: [has-external-sources, has-implementation]
tags: [agent-memory, context-engineering, evaluation, tool-loop]
---

# Apache Maka

Maka is an enclosing agent runtime whose Host owns the inspected execution
path while model context is projected from retained execution events. Its
built-in memory has distinct write and later-read routes: local Markdown memory
is injected into prompts, conversation checkpoints replace covered history,
and atomic SQLite MemoryItems are written without an inspected production
recall consumer.

This is a code-grounded analysis of [commit
ece69ab3e7a1629a6073831005711d8aa7160ca4](https://github.com/apache/maka/tree/ece69ab3e7a1629a6073831005711d8aa7160ca4),
inspected on 2026-09-05. The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-01/result.md)
retains the canonical records, scoped comparison fields and limitations.
No target run or intervention was performed; implemented wiring does not
establish successful operation, activation or benefit.

## Execution and effect boundaries

The ordinary route is client request → Host admission → AgentRun and
RuntimeKernel → provider step → local tool settlement or final output →
durable events and terminal state. Host checks session/turn identity against
existing admission. The adapter issues one provider step; the runtime owns
continuation and refreshes its history projection. Before local tool effects,
the backend requires readable current-run events. These are implementation
findings in RTE-1/RTE-2, supported by [root admission](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/root-turn-coordinator.ts#L1462-L1510),
[provider dispatch](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/model-adapter.ts#L281-L339)
and [local tool continuation](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/ai-sdk-backend.ts#L2815-L2878).

Graph supervisor wakes and scheduled agent work enter hosted execution, but
provider-owned tools and scheduled native notifications have separate effect
owners. Local ToolRuntime checks therefore do not establish universal control
over external effects. Recovery closes unfinished runs from retained evidence;
continuation requires an authoritative safety check. These are bounded
protocols, with no inspected crash experiment or deployed isolation result
(RTE-3 through RTE-6): [provider activity](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/ai-sdk-backend.ts#L2506-L2557),
[graph admission](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/agent-graph-execution-coordinator.ts#L74-L143),
[scheduled effects](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/scheduled-task-coordinator.ts#L560-L605)
and [continuation safety](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/runtime-kernel.ts#L1475-L1486).

## Three memory routes

| Material | Write and maintenance | Later consumer and limit |
|---|---|---|
| Local MEMORY.md/PENDING.md | User operations, proposal approval/rejection, status changes and revision-checked bundle writes | Active, session-visible entries pass policy/privacy gates and enter the prompt as untrusted lower-priority context; activation unmeasured |
| Atomic SQLite MemoryItems | Models transform eligible user text; citation/policy checks and canonicalization judgments gate durable writes with event provenance | Storage key/ID lookup is available, but no production task-model caller was found in the inspected composition |
| RuntimeEvents and compaction checkpoints | Events are retained; text compaction produces and structurally checks summaries; provider compaction can retain opaque state | Coverage-matched history/checkpoint replay changes later context; text faithfulness and opaque representation remain unmeasured |

The first two routes must not be joined into a single extraction-to-prompt
loop. [Local prompt composition](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime-host/src/server/interactive-run-composer.ts#L588-L624)
reads the file bundle (RTE-8), while [atomic commitment](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/memory-extraction.ts#L1019-L1139)
writes structured items (RTE-9 through RTE-11). ABS-1 records the bounded
production call search behind the missing-recall finding; an external embedder
could still call the storage API.

Text checkpointing is an implemented online, session-bounded transformation of
accumulated traces for later task continuation. It does not demonstrate
cross-task learning from atomic items or improved outcomes. [Checkpoint
variants](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/history-compact-checkpoint.ts#L87-L138)
include encrypted provider content, so the comparison leaves the complete
representational and distilled-form classifications unresolved. See
RTE-12/RTE-13 and [coverage-matched replay](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/ai-sdk-backend.ts#L1890-L1916).

## What the checks authorize

Atomic extraction checks citation membership and uses a separate model
judgment of support. These checks do not establish the truth of user assertions
or observed rewrite fidelity. Local human approval authorizes inclusion;
summary checks authorize a structurally eligible checkpoint. Neither is an
inspected semantic-faithfulness test (RTE-7/RTE-10/RTE-12).

Goal evaluation is a separate, tool-free call using the session model and recent
conversation. Its flags can settle or continue a goal, and its reason steers
later work. The parser coerces values to booleans, so accepted JSON alone does
not establish strict flag types. Task reminders are advisory and cannot veto
an already-terminal judge result. This is operational control, with no
independent environmental verification established (RTE-14/RTE-15): [goal
parser](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/goal-evaluator.ts#L122-L173)
and [settlement](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/runtime/src/goal-continuation.ts#L699-L741).

The eval framework separately acquires verifier results and chooses the
earliest attempt excluding infrastructure failures and indeterminate outcomes,
including scored task failures. That licenses a selected benchmark outcome,
not a claim that memory caused an improvement (RTE-16): [result
selection](https://github.com/apache/maka/blob/ece69ab3e7a1629a6073831005711d8aa7160ca4/packages/eval/src/result.ts#L87-L94).
The inspected benchmark report is attributed operation; its raw traces and
verifier output were not available to this pass.

## Scope

The whole-system target is assessed through selected material routes. The
comparison covers built-in conversational history/checkpoints, local memory and
atomic items with their access bookkeeping. Mutable skills and goal state are
adjacent control/instruction material. Offloaded tool artifacts, arbitrary
project files, external skills/extensions, peer meshes, image-context and
research features are outside the comparison or not traced end to end.

A wired atomic recall consumer, paired source/summary evidence, stricter goal
admission, inspected deployment boundaries or retained recall interventions
would change specific conclusions. No product ranking, measured benefit or
system-wide epistemic grade follows from this source inspection.
