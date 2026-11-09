---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "expo-llm-wiki workflow: LongMemEval conversation replay, retained-memory answering, judgment and report delivery."
run-id: AAS-2026-11-08-expo-llm-wiki-54f1fc1a0310-01
reviewed-boundary: "09c90258560a6b1664038d642b5d25d9de0c4d3d"
---

# expo-llm-wiki workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped LongMemEval benchmark: request a selected question set, replay its conversations into memory, reopen the retained database, retrieve facts, generate an answer, judge it against a supplied reference, and deliver a report. It was selected because it connects memory production to a later model consumer and an explicit result, rather than joining unrelated API capabilities. It is a bounded evaluation workflow, not an autonomous general-purpose agent runtime or the deployed application's approval system. The baseline is [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer); this member deepens its ingestion and judgment handoffs and extends the trace to CLI delivery. SRC-1, `packages/benchmarks/src/longmemeval/run.ts`, `packages/benchmarks/src/longmemeval/ingest.ts`, `packages/benchmarks/src/cli.ts`.

Additional inspected SRC-1 implementation coverage comprises the full `packages/benchmarks/src/longmemeval/run.ts`, `packages/benchmarks/src/longmemeval/ingest.ts`, and `packages/benchmarks/src/longmemeval/judge.ts`, plus `packages/benchmarks/src/cli.ts`'s `runLongMemEvalCommand`. These are code evidence at the boundary's frozen commit, not execution traces. No target code or evaluation was run; no stored benchmark results were adopted. Consequently the account establishes wired handoffs, not successful execution, accurate judgment or improved answers.

### Request, replay and retained-state handoff

The CLI receives argument flags, environment endpoints, dataset, sample IDs and an embed callback. It intersects sample IDs with the supplied dataset and optionally caps question count. A dry run returns an estimate before endpoint resolution; a live run resolves answer/judge endpoints, prints an estimate, and requires `--yes` before invoking the runner. This is an operator spending decision, not approval of individual extracted facts or answers. Code, rather than a model planner, owns progression. The runner uses a default four-worker promise pool; each question gets its own pipeline, while usage instrumentation is shared. The ingestion provider uses the answer endpoint but is metered under `other`; answer and judge calls have separate accounting roles. SRC-1, `packages/benchmarks/src/cli.ts`, `packages/benchmarks/src/longmemeval/run.ts`; [WF-RTE-report-delivery](#wf-rte-report-delivery).

For each question, ingestion supplies the engine with an entity (`lme-user`), provider, embedder, strategy configuration and events reconstructed from dated conversation sessions. Session indices are sorted by parsed date; every turn becomes an observation with a role-prefixed summary. The original session date is supplied as `occurred_at` only when the database supports that column. This is replay of supplied evidence, not an online conversation. The model-dependent extraction/admission mechanisms remain those in [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian) and [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian).

The replay-to-read boundary is a file path, not a transfer of the ingestion model's conversation. A completion sentinel controls reuse. Auto replay waits for librarian/heal inactivity after each turn and forces a final librarian pass when event count exceeds checkpoint. Deferred replay invokes pending maintenance up to 200 times, rejecting exhaustion before writing the sentinel. These checks establish the driver's acceptance rule, not that every conversation fact was extracted correctly or that all model failures surface as failed ingestion. The legacy configuration branch supplies threshold 20 but does not forward the requested maintenance flag; a legacy/deferred flag combination therefore does not itself establish actually deferred writes. SRC-1, `packages/benchmarks/src/longmemeval/ingest.ts`; [WF-RTE-replay-cache](#wf-rte-replay-cache).

### Retrieval, answer and verification

After ingestion returns, `runOneQuestion` opens the database anew and sets up `WikiMemory` with the supplied embedder and a no-op text generator. It requests at most ten candidate facts and forwards a truthy read budget when configured; zero is omitted by this driver, independently of core's zero-budget behavior. It formats the bundle with tasks and events excluded. Thus answer generation receives selected, formatted memory, not the original haystack or complete stored state. See [RT-RTE-memory-read](runtime.md#rt-rte-memory-read) for core retrieval limits. SRC-1, `packages/benchmarks/src/longmemeval/run.ts`.

The answer prompt carries the question date, formatted memory (or `(empty)`), and question. Its system instruction asks the model to use memory, say it does not know when memory lacks the answer, and be concise. These are model instructions, not enforced answer properties. SRC-1, `packages/benchmarks/src/longmemeval/judge.ts`.

> `Current date: ${q.question_date}\n\nMemory:\n${memoryContext || '(empty)'}\n\nQuestion: ${q.question}`;
> --- `packages/benchmarks/src/longmemeval/judge.ts`

A separate judge invocation receives a question-type-specific template populated with the question, dataset reference answer (or preference rubric), and generated response. It does not receive the retrieved memory context in this builder. The reference is an answer oracle supplied by the dataset object, not truth inferred solely from judge agreement. Template policy permits off-by-one temporal answers, accepts updated answers even with earlier information, and uses a personalized-response rubric for preference questions. The model proposes a yes/no judgment; code records any trimmed, lowercased reply beginning with `yes` as correct and all other strings as incorrect. This tolerates more than a strict yes/no response and does not independently validate the judge's reasoning. SRC-1, `packages/benchmarks/src/longmemeval/judge.ts`.

> const values: Record<string, string> = { question: q.question, answer: q.answer, response };
> --- `packages/benchmarks/src/longmemeval/judge.ts`

> return text.trim().toLowerCase().startsWith('yes');
> --- `packages/benchmarks/src/longmemeval/judge.ts`

### Rejection, recovery and delivery

A negative judgment is a recorded evaluation outcome, not a request to revise the answer or edit memory. The inspected `runOneQuestion` sequence has one answer call followed by one judge call and no repair loop. It closes the read database in `finally`. The promise pool propagates a question rejection, so aggregate report construction is not reached on that rejected invocation; `Promise.all` rejection is not cancellation of other in-flight work. Recovery from thrown failures belongs to a later caller rerun. Ingestion can reuse a complete cache or rebuild a readable incomplete cache, but an exception while probing a corrupt/missing-schema cache propagates rather than automatically entering the rebuild branch. SRC-1, `packages/benchmarks/src/longmemeval/run.ts`, `packages/benchmarks/src/longmemeval/ingest.ts`.

On success the runner aggregates correctness, context-size estimates, timing percentiles, usage and cached-ingestion count. Although its internal per-question result includes raw answer and judge text, its public `questions` projection retains only ID, type, correctness and context-token estimate. Consequently the delivered report is not a full transcript suitable for independently rejudging every answer. SRC-1, `packages/benchmarks/src/longmemeval/run.ts`.

> const questions = records.map((r) => ({
>     id: r.id,
>     type: r.type,
>     correct: r.correct,
>     contextTokens: r.contextTokens,
>   }));
> --- `packages/benchmarks/src/longmemeval/run.ts`

The CLI calls `writeFileAtomic` with the serialized report, then prints the path and a summary and returns exit code zero. This is the shipped delivery boundary; the helper's atomicity internals and filesystem durability are not assessed here. The report's generation neither installs new production instructions nor feeds judge corrections back into retained facts. SRC-1, `packages/benchmarks/src/cli.ts`; [WF-RTE-report-delivery](#wf-rte-report-delivery).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-replay-cache
Label: Conversation replay and cache acceptance

Part of: [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

This is the cache-preparation portion of the supplied benchmark route, not a second declaration of its answer/judge sequence. Code owns progression from a supplied question's haystack to a file-backed SQLite memory database. The caller supplies evidence and flags; core model calls propose extracted knowledge under the admission policies cited above. Replay itself uses no expected-answer oracle. Its completion decision checks engine state, not semantic truth; there is no per-fact human veto. The cache stores symbolic event/checkpoint/sentinel data and natural-language retained knowledge, with embeddings when provided. SRC-1, `packages/benchmarks/src/longmemeval/ingest.ts`.

- Immediate return: database path, cache-hit boolean and ingestion elapsed time after closing the handle, or a thrown error.
- Later read-back: a complete database is reused on later invocations; the answer pipeline reopens it and retrieves selected facts.
- Delegated visibility: core receives dated role-prefixed observation events and provider callbacks, not the dataset reference answer through this ingestion entry.
- Selection predicate: path includes engine version, strategy, maintenance mode and question ID; read budget is intentionally excluded. Existing sentinel value `1` bypasses replay; otherwise a readable incomplete cache is removed and rebuilt.
- Invalidation or expiry: incomplete main/WAL/SHM files are removed before rebuilding; no dataset-content digest or provider-model identity is checked by this cache key. A complete sentinel is not evidence of freshness under changed data or endpoints.
- Activation or effect: admission persists replay-derived memory; auto waits and deferred bounded pumping precede the completion marker. Unsupported deferred APIs, idle timeout or exhausted deferred rounds throw rather than deliberately accepting unfinished work.
- Evidence limits: source implementation only; quiescence and sentinel are not semantic verification. A failing initial cache probe is not caught for rebuilding. Legacy configuration does not forward the maintenance flag, limiting interpretation of legacy/deferred mode.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guidance and rollback: the driver chooses core strategy/configuration; it does not formulate a new theory or learn from verdicts. The proposed retained content comes from replayed turns through core extraction. Failed builds can leave partial files for a later successful probe/rebuild, rather than transactionally rolling back the entire question replay.

> if (row?.value === '1') {
>         return { dbFile, cached: true, ingestMs: 0 };
>       }
> --- `packages/benchmarks/src/longmemeval/ingest.ts`

> if (!quiesced) {
>         throw new Error(`deferred maintenance did not quiesce within ${DEFERRED_MAX_ITERATIONS} rounds for "${q.question_id}"`);
>       }
> --- `packages/benchmarks/src/longmemeval/ingest.ts`

#### WF-RTE-report-delivery
Label: Spend authorization and report delivery

Distinct from [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer): this is the outer command's spending gate and file/console delivery, not its per-question retrieval/answer/judge computation. The CLI owns selection of supplied sample questions, endpoint resolution, runner invocation and report writing. The operator supplies the spend flag, not an expected answer or per-answer approval. The operating mode is a bounded benchmark request; the report is a symbolic JSON projection on the filesystem and a human-readable console summary. SRC-1, `packages/benchmarks/src/cli.ts`.

- Immediate return: exit code zero after successful report write and summary; absent spend approval returns one, and inspected endpoint/input failures return two.
- Later read-back: report JSON is retained for external consumption; this command does not reload it into core memory or use it to revise answers.
- Delegated visibility: runner receives selected questions, flags, cache location, engine version, answer/judge endpoints, embedder and optional concurrency/seed; writer receives serialized aggregate report.
- Selection predicate: supplied sample IDs intersect supplied dataset, optional question cap; `--yes` gates spending, and dry-run branches before endpoint resolution.
- Invalidation or expiry: caller may choose an output path, otherwise a timestamped default is used; no report expiry or automatic semantic invalidation is established by this command.
- Activation or effect: calls the runner then writes its report, announces path and prints summary. This is delivery, not evidence that measured accuracy reflects deployment performance.
- Evidence limits: inspected command branch, not helper internals or live I/O; runner rejection prevents reaching the report-write statement. Spend approval is not content approval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!yes) {
>     stdout('Re-run with --yes to spend these tokens.\n');
>     return { exitCode: 1 };
>   }
> --- `packages/benchmarks/src/cli.ts:328-331`

> writeFileAtomic(reportFile, JSON.stringify(report, null, 2));
> --- `packages/benchmarks/src/cli.ts:349-349`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

Workflow-specific verification: dataset field `q.answer` supplies the reference/rubric; `q.question_type` selects judgment policy. The answer model proposes the answer, the judge model proposes its assessment, and the prefix parser decides the recorded boolean. No human adjudication or answer-repair step occurs in this inspected sequence. The oracle checks are evaluative, not gates on core knowledge admission. The account above retains the newly inspected judgment and output-projection evidence. The final aggregate omits raw answers/judgments despite their presence in internal per-question results. The outer file-delivery route is separately declared because the supplied record ends at the question result.
