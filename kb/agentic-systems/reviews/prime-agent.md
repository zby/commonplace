---
type: kb/types/note.md
description: "Prime Agent's persistent Python runtime, recursive child sessions, and supplemental-harness refinement, with separate admission and improvement limits"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-05-prime-agent-01
source-identity: https://github.com/PrimeIntellect-ai/prime-agent
reviewed-revision: 514633727bf26d74f39f3119c2b0e31a5ceb2a9d
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-05-prime-agent-01/result.md
analysis-result-sha256: a74d14523dee1f0588a42252c3a356e1e826c214c42b465b72dc30d1499ac305
---

# Prime Agent

Evidence basis: source code and shipped documentation at commit `514633727bf26d74f39f3119c2b0e31a5ceb2a9d`, analysed on 2026-09-05; no target execution or efficacy experiment.

Prime Agent is a coding and research runtime built around persistent Python and mutable supplemental harness state. Its Recursive Language Model interface makes tool use and child-agent work programmable from IPython. Its Continual Harness retains prompts, memories, skill descriptions and subagent specifications for later use. The inspected code supports persistent execution and context adaptation; it does not establish that an individual refinement improves performance. [Claimed work](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/README.md#L39-L52), [refinement admission](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/refinement/refinement.ts#L637-L806).

## Execution and control

A daemon supervisor routes clients to session workers. The session assembles context, calls the selected provider model, executes requested tools, and handles steering, follow-up and continuation. IPython is the default active SDK tool and can run Python, shell commands, imports and subprocesses. Tool-name and argument checks plus optional extension hooks govern admission; the worker/kernel processes run with user permissions and do not supply a security sandbox. [Session setup](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/sdk.ts#L235-L324), [loop](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/agent/src/agent-loop.ts#L305-L499), [trust boundary](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/README.md#L71-L74).

Child spawning returns a handle when work is admitted. Completion and explicit replies arrive later. Children have their own sessions and local state, while inheriting tool grants and sharing global harness access. Recursion depth is enforced at the host API, not across arbitrary Python execution. If a worker dies after a potentially effectful operation, recovery marks interrupted work and avoids replaying uncertain commands; it does not undo earlier effects. [Child admission and completion](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/agent-session.ts#L10198-L10488), [recovery](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/modes/daemon/daemon-supervisor.ts#L3170-L3248).

## Retained context

Continuity uses several stores: branch-selected JSONL history, compaction and branch summaries, supplemental harness entries, kernel snapshots and retained children. History assembly uses entry identities to select delivered material. Harness prompt assembly supplies a bounded catalog; requesting a complete entry is a separate read. Persistence therefore does not imply that the full entry reaches the model. Kernel revival restores arbitrary serialized values, so readable name manifests cannot establish every payload's form or authority. [History selection](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/session-manager.ts#L422-L529), [catalog](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/refinement/refinement.ts#L429-L519), [namespace revival](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/kernel/state-snapshot.ts#L203-L243).

Compaction summaries, branch summaries and refinement each implement automatic trace-fed production of retained guidance for later model calls. This meets the analysis's trace-learning criterion without establishing benefit. The task horizon remains uncertain across session/branch alternatives; a session can contain multiple tasks. Raw logging, namespace copying and independent skill authorship are distinct from those learning transformations. [Compaction application](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/agent-session.ts#L7393-L7474), [branch continuation](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/agent-session.ts#L11290-L11424).

## What refinement checks

The refiner proposes edits from bounded conversation and harness history. Optional automatic review decides whether to attempt refinement; structural checks then admit or reject each edit. Checks cover permitted fields, the reserved base-prompt target, entry existence and changes since planning. Recorded before/after entries support inverse edits. These checks do not test factual truth, the behavior of a referenced skill, or realized improvement. Direct Python harness writes and arbitrary executable extensions are separate admission paths. [Planner and checks](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/refinement/refinement.ts#L673-L948), [application](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/agent-session.ts#L8194-L8238).

One evidential distinction is easy to lose: the refiner's expectedOutcome is stored and later displayed as an outcome. It remains a prediction. Autonomous quality gates are a separate mechanism: the host executes configured commands and uses their exit/error/timeout results to stop or request repair. No inspected route makes those task gates an independent test of each harness refinement. [Prediction storage](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/refinement/refinement.ts#L791-L800), [gate execution](https://github.com/PrimeIntellect-ai/prime-agent/blob/514633727bf26d74f39f3119c2b0e31a5ceb2a9d/packages/coding-agent/src/core/autonomous.ts#L284-L367).

## Scope

This is a bounded whole-system code analysis, not an exhaustive inspection of every adapter, extension, UI or installer path. Remote provider internals, deployed grants, actual recalled-content dependence, measured improvement and causal effects remain uninspected. The selected checkout revision was not verified as the latest upstream commit. Candidate-linked runs and controlled comparisons would be needed to strengthen the assessment.

The [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-prime-agent-01/result.md) retains the canonical records, both lenses, comparison profile, source boundaries and limitations.
