---
type: kb/types/note.md
description: "Apache Maka's hosted execution, durable continuation, separate memory acquisition and evaluation authority at a pinned source boundary"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-05-apache-maka-06
source-identity: https://github.com/apache/maka
reviewed-revision: "02f97c16d76e644d5b565889701958293ff7b5fb"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-06/result.md
analysis-result-sha256: "9752e8525ec9e76d03dbac0934726cecf97263b2a6f092ea5ae413c769db42b4"
---

# Apache Maka

Evidence basis: source code and source documentation at commit `02f97c16d76e644d5b565889701958293ff7b5fb`, inspected on 2026-09-05. No target execution or behavioral experiment was performed.

Apache Maka (Incubating) is an enclosing agent runtime organized around hosted execution and a retained event log. Clients submit work to Runtime Host; RuntimeKernel and AgentRun own the turn, the model-step loop selects subsequent calls, and ToolRuntime settles client-executed effects. Agent Graph admits dependent child activations through revision-bound claims. Eval separately executes experiment cells, imports verifier scores and selects authoritative attempt results. This is a whole-system ownership account with bounded feature coverage, not an exhaustive proof of every client or deployment path. See the [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-apache-maka-06/result.md) for canonical records and retained verbatim evidence.

## Execution and recovery

The ordinary loop assembles context and the active tool subset, calls the configured provider, settles returned tool calls and continues while step budget and stop conditions permit. Its terminal message records what the runtime returned; it does not establish task success. Model identity resolves through connection/model configuration. Exact provider weights and operational parameter changes remain uninspected. RTE-1 and CMP-2: [model-step loop](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/ai-sdk-turn.ts), [model resolution](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/model-adapter.ts).

Durability has distinct enforcement points. Where a durable commit sink is configured, tool preparation is committed before invocation; an outcome-write failure can still follow an external effect, with compensation only best effort. Ordinary nonterminal events can fail open, while steering and selected terminal/interaction boundaries require durable writes. Replay planning blocks indeterminate effects, including model-hidden nested calls. These are source-level protocols, not observed crash guarantees or exactly-once arbitrary effects. RTE-2, RTE-3 and CLM-1: [tool settlement](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/tool-runtime.ts), [event persistence](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/agent-run.ts), [replay planning](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/runtime-resume.ts).

Graph readiness is computed from stored state; dispatch then checks the expected schedule revision. Supervisor notifications are an observation channel rather than a per-dispatch approval gate. RTE-4: [schedule reconciliation](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/stream-graph-schedule-reconcile.ts).

## Memory and context

Maka's retained-context mechanisms have different consumers:

- Earlier inline session invocations are automatically projected into later context. Portable compaction creates a durable continuation summary; provider-native compaction retains encrypted state that later requests consume directly. Both checkpoint branches establish automatic trace-fed write, retention and later consumption. Trace learning is therefore **wired**, without establishing improvement. Opaque native content prevents a complete representation/distilled-form classification, and session identity does not establish the aggregate task horizon. RTE-8, RTE-9, RTE-10: [checkpoint forms and replay](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/history-compact-checkpoint.ts).
- Active manual Markdown memory enters eligible main-session prompts as explicitly untrusted context. Automatic extraction instead proposes and canonicalizes assertions from cited user events into a separate SQLite store. The bounded in-tree call-site search established no later semantic recall consumer for those SQLite items; a saved receipt is not evidence of future recall. RTE-11, RTE-12 and ABS-1: [manual-memory composition](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime-host/src/server/interactive-run-composer.ts), [extraction](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/memory-extraction.ts).
- Acquired skills have a shared turn inventory, deterministic catalog ranking and requested instruction reads. Archived tool results and child outputs also have explicit requested-read routes. Automatic identity/coarse selection and model-requested pull coexist; lexical search answering a request is not automatic relevance-based push. RTE-13, RTE-14, RTE-15, RTE-16: [skill context](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/skills-context.ts), [archive read](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/runtime/src/archive-read-tool.ts).

## Evidence and authority

Memory admission, checkpoint compatibility, tool permission and graph readiness have operational force. They do not automatically warrant the truth of an answer. Extraction combines model semantic guidance with code-level provenance/quote/shape checks; quote containment does not prove entailment. Compaction coverage checks likewise do not establish semantic fidelity.

Eval provides a different, bounded check: it imports the configured verifier's score and selects the earliest reusable substantive attempt, rather than the highest score. Verifier validity, expected-answer access and reported benchmark outcomes were not inspected, so this run establishes evaluation machinery without a performance or causal advantage. RTE-5, RTE-6 and CLM-3: [evaluation runner](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/eval/src/runner.ts), [result selection](https://github.com/apache/maka/blob/02f97c16d76e644d5b565889701958293ff7b5fb/packages/eval/src/result.ts).

## Scope

Provider internals, remote peer transport, every platform sandbox and individual tool, deep-research/goal/bot workflows, release machinery and third-party session import routes were not exhaustively inspected. Operator-facing recap was checked and excluded from model-learning scope. No recalled-content dependence test was observed. These limits prevent universal isolation, faithfulness, task-success and causal claims. Candidate-linked runs, boundary fault tests, provider semantics and recalled-content interventions would strengthen or change this assessment.
