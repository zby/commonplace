---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "nao workflow account: CLI analytics test, model answer extraction, bounded SQL repair and delivered comparison report."
run-id: AAS-2026-10-14-nao-f9d36a4b7276-01
reviewed-boundary: "0085625a8fd22e4f404b6a3971d153f6b6699479"
---

# nao workflow report

## Workflow account

### Selection and evidence boundary

This account follows a CLI analytics test with reference SQL, from submitted test case to saved comparison report. It was selected because one connected shipped path exposes model work, a second model handoff, executable rejection, bounded repair and deterministic completion criteria. It elaborates [RT-RTE-test-answer](runtime.md#rt-rte-test-answer), not a new workflow identity. It does not imply that ordinary chat uses this verification gate.

The evidence is implementation and prompt text from SRC-1 at the revision in [the boundary](boundary.md). No test, agent, model or warehouse was run. The account establishes wiring, not successful delivery or evaluation validity. Added inspection covers `apps/backend/src/routes/test.ts`, `apps/backend/src/services/test-agent-verification.ts`, `apps/backend/src/services/duckdb.service.ts` (query-result execution and safety-check ranges), `cli/nao_core/commands/test/client.py` and `cli/nao_core/commands/test/assertions.py`, plus targeted ranges of the previously inspected test service, agent generate path and CLI runner. DuckDB parser internals, the complete SQL-safety helper chain and warehouse behavior were not audited; no isolation invariant follows.

### 1. The test author supplies the task and reference

The CLI client sends the test prompt, provider/model selection, optional reference SQL and database identity to `/api/test/run`. Tool assertions stay on the CLI side. The backend route applies its authentication hook, requires a project and calls `runTest` using the request's user/project. This is not evidence that every web-chat role policy applies to the test route. SRC-1: `cli/nao_core/commands/test/client.py`, `apps/backend/src/routes/test.ts`.

The author supplies the reference SQL, not expected prose for a model judge. Only after the analytics run does the server execute that SQL to obtain expected rows and column names:

> const { data: expectedData, columns: expectedColumns } = await executeQuery(
> { sql_query: sql, database_id: databaseId },
> toolContext,
> );
> --- `apps/backend/src/routes/test.ts`

Thus the reference outcome depends on the author's SQL, current warehouse contents and the reference query's access context. This is a comparison oracle, not proof that the reference captures the user's intent. The two warehouse queries are not shown to share an atomic data snapshot. SRC-1: `apps/backend/src/routes/test.ts`.

### 2. nao delegates analytics to its enclosing agent

`runTest` builds a temporary chat identity containing the user prompt and principal, creates the normal agent manager and calls its nonstreaming `generate` method. The model chooses analytics tools and composes the response under the runtime's supplied instructions and grants. nao's tool implementations dispatch effects; external providers and databases remain separate dependencies. See [RT-RTE-web-chat](runtime.md#rt-rte-web-chat) for the common model/tool division and [RT-OBJ-tool-context](runtime.md#rt-obj-tool-context) for the principal and result accumulator. This test is not necessarily a task-subagent invocation.

The generate result carries text, response messages, step-level tool calls/results, usage, cost, duration and the accumulated query-result map. Its `finally` calls `_finish`; unlike the streaming chat route, this path does not use the settled-message persistence callback. A temporary chat structure is not a delivered chat transcript. SRC-1: `apps/backend/src/services/test-agent.service.ts`, `apps/backend/src/services/agent.ts`.

### 3. A separate model translates the answer into executable extraction

With reference SQL present, the server passes the original question, analytics response messages, expected column names and collected query results to `runVerification`. The second call uses `generateText` with a schema containing nullable SQL. It is a sequential model call, not an independent critic with a fresh expected-answer oracle. The model-selection argument is reused, so separate responsibilities need not mean different model identities. See [RT-CMP-verification-model](runtime.md#rt-cmp-verification-model).

The prompt builder delivers the question, response messages and a table inventory containing query IDs, row counts and column names. It does not serialize all stored rows or send expected row values in this builder. Actual rows are loaded later for SQL execution. SRC-1: `apps/backend/src/services/test-agent-verification.ts`, `apps/backend/src/services/test-agent.service.ts`.

> Rules:
> - Only read from the tables above, the warehouse is not reachable anymore.
> - Return exactly these columns, with these names: ${columns.join(', ')}
> - Read the values from the tables, never retype them as literals.
> - Apply the same filters, aggregations and ordering as the answer you gave.
> - Set sql to null if these tables cannot answer the question.
> --- `apps/backend/src/services/test-agent-verification.ts`

These instructions request faithful extraction; they do not establish it. In particular, a valid query can still misrepresent the prose answer. The eventual comparison judges extracted rows, not the complete truth or presentation quality of the answer.

### 4. Code rejects execution failures and returns one repair opportunity

`runSqlOverQueryResults` creates an in-memory DuckDB instance, checks the proposed SQL against a read-only/table-allowlist policy, loads the result tables, disables external access and executes the query. Its `finally` closes the connection/instance and removes its temporary workspace. These are adapter enforcement points, not proof that all possible unsafe SQL is rejected. SRC-1: `apps/backend/src/services/duckdb.service.ts`.

> await assertSafeQueryResultsSql(connection, sql, [...queryResults.keys()]);
> --- `apps/backend/src/services/duckdb.service.ts`

An execution or safety-check error is caught by `runVerification`. Code appends the failed SQL as an assistant message and the error-bearing repair request as a user message, then calls the model again. The two-attempt cap in [RT-RTE-test-answer](runtime.md#rt-rte-test-answer) means one correction opportunity, not an unbounded repair loop.

> That query failed with: ${error}
>
> Return a corrected DuckDB query, or set sql to null if the tables cannot answer the question.
> --- `apps/backend/src/services/test-agent.service.ts`

The recovery owner is split: code decides whether execution failed and whether another attempt remains; the model proposes corrected SQL. The repair is of the extraction query, not a rerun of analytics or revision of the reference. No fetched query results produces an immediate error result. Null SQL terminates with an inability-to-answer result. After two failed executions, the service returns null data with the last SQL/error. Errors from model generation itself are outside this execution catch and reach the route's error response. SRC-1: `apps/backend/src/services/test-agent.service.ts`, `apps/backend/src/routes/test.ts`.

### 5. The CLI accepts or rejects the result and delivers the report

The backend returns answer text, extracted tool calls, run metadata and verification payload including expected rows. HTTP errors become client exceptions and failed CLI test results. The client has one authentication retry after a 401 if reauthentication succeeds; this is distinct from SQL repair and does not demonstrate general retry safety. SRC-1: `apps/backend/src/routes/test.ts`, `cli/nao_core/commands/test/client.py`, `cli/nao_core/commands/test/runner.py`.

For a verification payload, CLI code checks asserted tool names, minimum counts and optionally recursive argument subsets. It separately compares extracted and reference rows: missing columns and unequal row counts reject; numeric normalization, configurable rounding/tolerances and sorting affect equality. Row order is deliberately ignored. Both empty datasets pass. The combined condition is retained in [RT-RTE-test-answer](runtime.md#rt-rte-test-answer). A recorded tool call does not prove its external effect succeeded. SRC-1: `cli/nao_core/commands/test/assertions.py`, `cli/nao_core/commands/test/runner.py`.

A data mismatch does not trigger another model repair in this runner. It becomes a failed report with comparison details. The tool-assertions-only branch can pass without data verification. The final fallback also returns a passed result labelled `no verification`; therefore a CLI pass outside the reference-SQL workflow must not be read as demonstrated answer correctness:

> passed=True,
> message="no verification",
> --- `cli/nao_core/commands/test/runner.py`

Delivery here is a returned per-run result, followed by CLI aggregation, timestamped JSON under the project's test outputs directory and printed summaries. The batch exits with status 1 if any collected result is failed. These are source-defined completion effects, not observed artifacts from this analysis. Saved details include answer text, actual/expected data, tool calls and reference/extraction SQL where available. Retention does not establish that a later agent consumes the report or that a failed test automatically blocks deployment. SRC-1: `cli/nao_core/commands/test/runner.py`.

> output_file = save_results(results, project_path / TESTS_FOLDER / "outputs")
> --- `cli/nao_core/commands/test/runner.py`

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-test-answer](runtime.md#rt-rte-test-answer)

Workflow selection: reference-SQL CLI test, selected for its connected analytics → extraction → executable check → comparison → report chain.

Handoff contract: the test author supplies question and reference SQL; the backend supplies principal and agent runtime; the extractor receives question, response messages, expected column names and result-table descriptions, not expected row values in its prompt builder. The CLI receives the reference and extracted rows for deterministic comparison.

Verification boundary: successful SQL execution accepts an extraction query for comparison, not the analytics answer as true. CLI data equality and tool-call assertions decide the reported test verdict. The no-verification fallback can report passed without this answer check.

Recovery and delivery: execution rejection can prompt one SQL repair; final comparison rejection records failure without an analytics retry. The CLI saves the collected run results and emits batch failure status. Neither a saved report nor an exit status establishes deployment admission or later model learning. Supporting implementation passages and their limits are retained in the workflow account rather than duplicating the runtime record's identity and evidence.
