# Workflow five-run batch audit

Audit date: 2026-10-12. Commission: [the sequential batch](../workflow-batch.md) and [Audit an analysis](../audit-an-analysis.md), narrowed to this report only. This was one continuous, non-delegated audit. GBrain is the separately checked pilot, not a sixth case. The five remaining targets are on hold.

## Outcome

**Retain the five bounded workflow accounts. Do not treat their publication or this audit as an exhaustive correctness certificate.** Each account follows one source-supported connected procedure. The useful contribution is the connection between ownership, selection, effects and terminal communication—not evidence that the target actually executed successfully. None of the five warrants deployed compliance, factual quality or causal benefit.

Two qualifications matter to subsequent decisions:

- Graphiti still lacks several previously identified non-workflow qualifications: named-saga ingestion can reset summary state, bulk episode-to-edge lookup is incomplete, and server-supplied MCP instructions are a separate channel from the Cursor document. Its selected notebook workflow remains supported.
- Instinctual Memory completed despite an epistemic worker's explicit `problem`. The worker misreported its own shortened validator path as the supplied command. Existing primary output allowed engine closure without preserving that problem. Subsequent checks and independently checked publication bytes pass, but “Stops: None” does not communicate this worker-level failure. Status handling needs operator adjudication before relying on completion as proof that every worker obligation was satisfied.

Direct validator failures continue to be exposed rather than masked. Semantic review repairs consequential findings, and transport interruptions recover. Correctly supplied absolute paths still do not ensure exact reuse. These are observations across these runs, not causal effects of the workflow lens or grounds for silently editing the method.

## Identities and evidence boundary

`reporter-profile`: pi / `openai/gpt-6.1-sol` / medium. Reporter session: `01a12f4e-fbd2-770f-aa7a-57a2fbba5d3a`. This is distinct from the audited profile. All five coordinators and all 67 analytical worker envelopes expose `openai/gpt-6.1-sol` / medium; the prepared profile is `pi-sol`. Model identity is a harness-exposed identifier, not a weights digest.

Worktrees are under `/home/zby/llm/commonplace/.commonplace/worktrees/`. Their names are `<system>-workflow-<token>`. Each run lives in its worktree at `kb/agentic-system-analyses/state/<run-id>/`; `R` below means that run directory. The integrated sets are under `kb/agentic-system-analyses/retained/<system>/` in origin. Source paths below are relative to the corresponding frozen source checkout, not origin.

| System | run-id | method-commit | source-revision |
|---|---|---|---|
| Graphiti | `AAS-2026-10-12-graphiti-1d535ca565a4-01` | `682d5e7e6fa87af0f60d6a8a35266c41cb0e2913` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| Napkin | `AAS-2026-10-12-napkin-2b85bef38252-01` | `69199c6ec09fa32b13f1bbc61d844f768cc4d7d4` | `7582d6a46f5a11995956e60a59c41a5b242109f1` |
| Letta Code | `AAS-2026-10-12-letta-code-be76afeab9b7-01` | `83cb44a89bfb56f17efb1a141ec77eaf2f859a2d` | `271f119dcf37d58649a18e6c733386b3c710a456` |
| Dynamic Cheatsheet | `AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01` | `bb155f68660d0c7294f410e3aea4816ae3c6e2b1` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` |
| Instinctual Memory | `AAS-2026-10-12-instinctual-memory-af48437aa60c-01` | `86006bf574c274b715667386ae2e3a1793538db1` | `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` |

Source identities/access roots: Graphiti `https://github.com/getzep/graphiti`, `related-systems/getzep--graphiti`; Napkin `https://github.com/Michaelliv/napkin`, `related-systems/Michaelliv--napkin`; Letta Code `https://github.com/letta-ai/letta-code`, `related-systems/letta-ai--letta-code`; Dynamic Cheatsheet `https://github.com/suzgunmirac/dynamic-cheatsheet`, `related-systems/suzgunmirac--dynamic-cheatsheet`; Instinctual Memory `https://github.com/jasonkneen/instinctual-memory`, `related-systems/jasonkneen--instinctual-memory`.

Preparation records, opening provenance and publication evidence fix the method identities; later result-integration commits are not new method identities. A scoped Git diff between the first and fifth method commits over analysis instructions/types, engine and root instructions found no changes. This does not assert whole-repository identity.

### Coverage

I read all five complete accepted workflow accounts and all five syntheses. I followed each selected workflow's consequential transitions through frozen code or complete shipped instructions. I checked selected runtime, memory, epistemic, reconciliation and verification findings where they could change workflow interpretation, prior-audit dispositions or acceptance. I inspected historical refusal findings and their repair chains, rather than treating the final “none” blocker sections as evidence that no repair occurred.

Trace coverage is a failure-oriented structured scan of every available analytical worker envelope, matched calls/results, validator commands and embedded assistant errors, with focused expansion of consequential episodes. It is not a line-by-line semantic assessment of every source read, output paragraph or mandatory-read continuation. The trace counts below cover 67 new workers; the old comparison uses focused old artifact/trace checks and explicitly attributed prior audit totals, not 45 fully reread old workers.

The evidence route is expressly commissioned frozen-source inspection. No target, test, example, provider or benchmark was executed. No agents were launched, engine advanced, sources edited, evidence cleaned, outputs integrated or commits made. One-shot standard-library calculations were used; no reusable audit tooling was implemented. The parent owns navigation and any later session-tools workshop.

## Per-system findings

### W1 — Graphiti: connected conversation, tool and memory boundaries

The [workflow](../../../agentic-system-analyses/retained/graphiti/workflow.md) selects the shipped LangGraph shoe-sales notebook, not an imagined MCP host episode. `examples/langgraph-agent/agent.ipynb`, especially `chatbot`, shoe-search tool, tools-to-agent edge and widget callback, supports request → five-fact context → model → optional ten-fact shoe tool → subsequent model → response display. Ingestion is scheduled asynchronously after every successful model response, including tool-call responses. The latest state message can be a tool result. Its unconditional user-name prefix does not authenticate human origin.

The account adds a useful relationship: user-facing completion and graph-memory completion are different events. It also makes recirculation explicit: retrieved facts can return through a tool and enter a later episode. Framework `MemorySaver` checkpoint state is not Graphiti graph state. External framework behavior, model compliance and completed asynchronous persistence remain unobserved.

The workflow specialist contradicted the initial human/model-only origin account. Reconciliation retained the conflict; report verification routed corrections to runtime, memory and epistemic. The accepted records and synthesis now agree with the notebook. This is a concrete safeguard success: workflow inspection changed consequential source-origin claims outside its own member. Historical judgment `000023-apply-report-verification` and workers at T/L183/c36, c40, c44 and c52 preserve the repair chain. Verification also repaired memory's renewed overgeneralization of raw suppression from single to bulk ingestion. The final bulk qualification is supported by `graphiti_core/graphiti.py` and the unchanged-content serializer in `graphiti_core/utils/bulk_utils.py`.

**Remaining local limits, independently checked:**

1. Named-saga ingestion still threatens the inputs of the positive recurring-summary account. `_get_or_create_saga`, `graphiti.py:485–540`, hydrates existing identity/pointers but not summary or watermarks. `SagaNode`, `nodes.py:907–940`, defaults those fields to empty/null and passes them to save. Ordinary ingestion saves that object at `graphiti.py:1047–1090`; bulk saves it at `1821–1826`. `models/nodes/node_db_queries.py:352–373` replaces those properties. A summarize → named ingestion → summarize sequence can therefore reset the brief/cursor in the inspected save path. Fully hydrated supplied objects and custom operations implementations differ. This is a static countercase, not an observed loss incident. Accepted `MEM-RTE-saga-summary` explains bounded incremental summarization but not this intervening reset. Carry a local correction/qualification candidate forward; do not erase the supported notebook workflow.
2. Bulk episode-to-edge lookup remains incompletely characterized. The ordinary helper assigns `ep.entity_edges` at `graphiti.py:1031`; bulk does not use that helper for the final episode update. Newly created episodes retain the empty default list. `get_nodes_and_edges_by_episode`, `2009–2021`, reads that list to load facts; `remove_episode` uses it for edge-cleanup selection. The earlier amendment audit supplies the detailed serializer/default-query chain. The new set qualifies episode attribution fallback, but does not explain this distinct missing reverse index. Withhold complete episode-based fact lookup/withdrawal comparisons.
3. `mcp_server/src/graphiti_mcp_server.py:136–181` supplies `GRAPHITI_MCP_INSTRUCTIONS` directly to `MCPServer`, correctly naming `search_memory_facts`. The accepted behavioral-authority account concentrates on `mcp_server/docs/cursor_rules.md` and its different tool name. Server wiring does not establish host presentation or compliance; it does establish a second shipped instruction channel. Withhold a complete instruction-delivery inventory.

Other old findings, including ordinary-ingestion context-count accuracy and detailed backend/recipe behavior, were not exhaustively rechecked. The old verifier's false citation-typo allegation is not repeated in the new accepted verification narrative; that is not evidence about every new criticism.

### W2 — Napkin: procedure ownership, persistence and post-write checks

The [workflow](../../../agentic-system-analyses/retained/napkin/workflow.md) follows the complete packaged `skills/distill/SKILL.md`: assess session material → KEEP/SKIP → search existing notes → merge or create → repair links → report. The external agent owns selection, semantics and command sequencing; CLI/core code owns file effects. The separate timer/separate-model design in `docs/distill.md` is not silently attached to that packaged procedure.

Frozen `src/core/crud.ts`, `src/core/links.ts`, `src/utils/files.ts` and `src/commands/links.ts` support the consequential limits. Link checks follow persistence and are diagnostics, not admission vetoes, semantic verification or rollback. Loose/shallowest matching and fragment stripping do not establish an unambiguous heading-level target. The literal skill create example supplies a folder-shaped path where core expects the complete filename, and copying a template does not populate it with distilled content. The accepted workflow, verification and synthesis retain that delivery mismatch rather than claiming successful literal execution.

This adds connected ownership and failure ordering, although the previous synthesis already described distillation and caller-owned overview → search → read. It is not discovery of an entirely new capability. No observed host compliance, factual admission or later retrieval benefit follows.

The accepted memory report now declares `MEM-RTE-background-distill` as separate-model/extension doctrine and preserves unknown timer/cursor/injection implementation. This is clearer than the old underclassification. It still does not warrant a deployed automatic push route. Profile verification at c48 routes the missing permanent-unlink `decay` classification; c52 repairs and c56 verifies. This is a successful comparison-field safeguard, not target execution or evidence of time-based decay.

Disposition: retain the bounded workflow and its create-example limit; no new material workflow correction identified in this sample. Formula, renderer, tokenizer and external injection inventories remain partial.

### W3 — Letta Code: launch is not child acceptance or caller delivery

The [workflow](../../../agentic-system-analyses/retained/letta-code/workflow.md) selects local non-memory Task delegation in bidirectional headless mode. `src/tools/impl/task.ts` establishes identity/fork admission, background startup, launch receipt and completion conversion. `src/agent/subagents/manager.ts` establishes captured result/error handling and fallback parsing. `src/headless.ts` and `src/queue/turn-queue-runtime.ts` establish queued synthetic-user notification and later parent input.

The useful connected distinction is launch receipt → child protocol completion → bounded notification → parent continuation → delivered answer. A child exit is not a factual/product acceptance decision. Notification delivery is conditional on the selected host mode and queue progression; it is not universal unsolicited delivery. Child unrestricted mode plus inherited disallows does not establish universal delegated permissions or isolation.

The workflow's “one narrower automatic recovery” paragraph describes one-time truncated-stream respawn. The manager also has provider-unsupported and lost-stdout recovery branches. Treat that paragraph as a selected recovery example, not a complete retry inventory. The exact quote ambiguity detected during drafting concerned three separate retry sites; the repaired range correctly selects the intended site. I do not classify the positive selected recovery mechanism as false. Avoid extracting “only one recovery mechanism” from it.

Previous Task launch descriptions already had context, receipt and recovery fields. The new value is the source-connected notification/continuation/terminal-delivery account. The verifier explicitly retains incomplete characterization of the separate Workflow tool and initialization/reorganization doctrine; synthesis carries those limits. Those are not repaired by adding a Task workflow. A source spot check of `src/hooks/executor.ts:437–455` confirms BLOCK stops processing while ERROR records feedback and continues; the new epistemic hook account is not a substitute for every old hook disposition detail.

Disposition: retain the selected account; qualify recovery-inventory extraction and withhold cross-tool permission/recovery completeness. No new material selected-workflow correction identified.

### W4 — Dynamic Cheatsheet: update precedes scoring

The [workflow](../../../agentic-system-analyses/retained/dynamic-cheatsheet/workflow.md) connects the cumulative benchmark driver to generation, optional local code execution, curator output, reference replacement, answer scoring and checkpoint/resume. `run_benchmark.py`, the cumulative branch in `dynamic_cheatsheet/language_model.py`, `utils/extractor.py`, `utils/execute_code.py` and `prompts/curator_prompt_for_dc_cumulative.txt` support this ordering.

The central useful distinction is that scoring does not admit or veto the cheatsheet update: the curator acts before objective scoring. A generated reference may shape a later answer without being certified by the current answer's score. The shipped cumulative curator prompt is optional configuration, not the default behavior: without the supplied prompt path the template is `(empty)`. Code execution is an effect boundary, not a semantic proof about all generated advice. Recursive attempts and execution results do not establish successful benchmark operation at this pin.

The accepted synthesis retains reference-admission, execution and scoring distinctions rather than equating score retention with a production improvement gate. Source inspection supports the selected cumulative mode, not every dataset/mode/provider/resume permutation. No live accuracy, cumulative benefit or isolation claim was checked.

Disposition: retain this particularly useful connected account. Its utility comes from exposing temporal ordering and differing decision criteria, not adding a runtime capability inventory. No same-source previous amendment-effects case exists in this commission.

### W5 — Instinctual Memory: review is not an immutable approved candidate

The [workflow](../../../agentic-system-analyses/retained/instinctual-memory/workflow.md) selects `/mem tidy`: host readiness → preview → user keep choices → apply → publication → communication. The complete `skills/mem/SKILL.md`, `src/tidy.rs`, `src/cli.rs` and `src/repo.rs` support its instruction-versus-code distinction. Host review/compliance is requested, not demonstrated.

Apply recomputes candidates instead of loading an immutable reviewed preview. Keep IDs veto selected findings but do not bind a human to the exact candidate that is eventually published. Model-error, duplicate-only/degraded and no-change branches are distinct. Candidate structural validation and Git compare-and-swap protect particular publication/concurrency properties, not semantic user approval. Successful publication does not prove tidy judgment quality.

Report verification at c34 detected two runtime overclaims: evidence matching discards normalized fragments shorter than eight characters, and local backfill reports completion without an explicit final flush whose errors propagate. Runtime c40, reconciliation c44 and fresh verifier c48 repair these claims. The final verification explains both dispositions and retains a partial sibling/reranker candidate-pool inventory. This is a supported semantic repair chain; this audit concentrated source inspection on tidy and publication, rather than independently reproducing every consolidation/acquisition deduction.

Disposition: retain the selected workflow; independently source-supported review/apply mismatch is correctly disclosed. Separately escalate the run-status episode below. It is not a source defect in Instinctual Memory.

## Trace definitions and reproducible locators

`T` is `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T15-31-10-091Z_01a12b96-de8a-711e-8a12-57ef261a7126.jsonl`.

Locators `T/L<n>/c<n>/r<n>/m<n>` use a one-based JSONL line and zero-based nested message/result/message indices. Coordinator results are `rows[L-1]["message"]["details"]["results"][0]`; a worker is `coordinator["messages"][c]["details"]["results"][r]`; an event is worker `messages[m]`. Locate by run ID/task as well as these current line numbers. Coordinator-only events omit `r/m` and refer directly to its `messages[c]`.

- An analytical worker is a nested result whose task launches an engine handout; diagnostic tasks are excluded. Repeated/correction workers count separately, not as independent systems.
- An emitted call is a `toolCall` block keyed by its ID. An executed/logged result requires a matching `toolResult.toolCallId`. A proposal without a result is not certified executed; transport failure is not proof it had no external effect.
- A validator invocation is a matched Bash call containing `commonplace-validate`. A direct invocation contains none of `;`, `|`, `&&` or newline. Failure means the matched result reports `isError`; printed command status/content identifies its nature.
- A transport error is an assistant message with `stopReason == "error"` and provider/error text. It is distinct from tool failures and from the outer envelope's exit code.
- Worker duration is maximum minus minimum numeric embedded message timestamp, in minutes. It includes wait/recovery, excludes launch/return overhead and is neither CPU time nor wall time.

| System / T line | Workers | Emitted calls | Matched results | Direct validators | Failed validators: path / content | Transport-error messages |
|---|---:|---:|---:|---:|---:|---:|
| Graphiti / 183 | 18 | 741 | 740 | 28 | 6 / 2 | 1 |
| Napkin / 189 | 13 | 566 | 565 | 17 | 3 / 0 | 1 |
| Letta Code / 195 | 11 | 510 | 510 | 20 | 4 / 4 | 0 |
| Dynamic Cheatsheet / 201 | 11 | 386 | 386 | 15 | 2 / 1 | 0 |
| Instinctual Memory / 207 | 14 | 591 | 584 | 18 | 4 / 0 | 2 |
| Total | 67 | 2794 | 2785 | 98 | 19 / 7 | 4 |

All 98 matched worker validators are direct. All 26 failures propagate. “Content” counts failing invocations, not individual diagnostics: Letta includes quotation ambiguity, a record-link label and duplicate profile records. The 19 bad-path invocations affect 19 workers across five systems. They are not evidence of 19 malformed supplied handouts. Correct full command delivery is visible in sampled prompt results; the Instinctual episode below demonstrates the distinction exactly.

This scan includes 287 matched Bash results: Graphiti 79, Napkin 43, Letta Code 79, Dynamic Cheatsheet 39, Instinctual Memory 47. Nonzero results include discovery/no-match probes; those are not automatically acceptance defects. I did not certify constituent statuses in every compound exploratory shell command or assign a zero masked-failure count to uninspected inner commands. The strongest status result is the validator-specific one above.

### O1 — Path reconstruction persists; quotation checks do useful narrower work

Graphiti bad-artifact results are c26/r0/m81, c26/r1/m56, c36/r0/m116, c56/r0/m54, c68/r0/m66 and c72/r0/m66. They invent a worktree-like `…graphiti-workflow-1d535ca565a4-01/artifact` instead of using `R/artifact`. Memory's subsequent c26/r0/m83 exposes an out-of-source range plus ambiguity; epistemic c26/r1/m80 exposes ambiguity. These are different stages of failure, not masked passes.

Napkin bad-artifact results: c28/r0/m94, c52/r0/m58, c56/r0/m65. Letta Code: c23/r0/m99, c28/r0/m73, c33/r0/m56, c37/r0/m132; the reconciliation error misroutes the candidate rather than only the artifact. Letta content failures: c23/r0/m91, c29/r0/m53, c33/r0/m52 and c41/r0/m51. Dynamic Cheatsheet: bad artifacts c27/r1/m66 and c27/r2/m44; runtime ambiguity c23/r0/m53. Instinctual: c22/r0/m71, c26/r0/m79, c26/r1/m49 and c40/r0/m45.

Quotation occurrence/range checks catch ambiguity even when attribution formatting is valid. They do not check truth, correct passage interpretation, omitted mechanisms or runtime success. Graphiti and Letta ambiguity repair demonstrates useful enforcement without establishing semantic completeness. Relative spellings that resolve to the assigned file are a separate issue from these nonexistent targets; this audit does not count all relative paths as misrouting.

### O2 — A false problem explanation becomes an unretained status event

At T/L207/c26/r1/m3 the delivered epistemic prompt contains the correct full `R/artifact` binding **and the correct literal validator command**. At m48–49 the worker instead executes the shortened nonexistent artifact path. At m50–51 it successfully writes `problem.md`, claiming the mandated command was run exactly and differed from the artifact variable. That explanation is false: the discrepancy was introduced by the worker. At m52 it returns exactly `problem` despite already writing a primary candidate, empty answers and identity.

Coordinator c27 submits `--completed 000008-epistemic` along with the other specialists. c28 advances successfully to reconciliation. Frozen `src/commonplace/artifactrun/engine.py:381–451`, `_close`, reads a problem but uses it to fail a completed result only if the primary output is missing. With primary output/identity present it commits outputs and removes the handout directory. `R/state/attempts/000008-epistemic.json` is completed, with report hash `1493b381668e863dbf61332894c563db54712d1fd0a25ffc07954c1cabbc8f08`; it contains no problem disposition. The trace is therefore the surviving evidence of this problem text. Later deterministic/semantic checks proceed and publication succeeds. The coordinator's final response says “Stops: None.”

The driver says completion means the worker finished, not that its output was accepted, and forbids coordinator substantive judgment of outputs/problem reports. That constrains the coordinator's options; it does not make the worker's inability explanation correct or preserve its problem in engine state. Do not call this a knowingly forced engine stop: no stop was emitted. Do not call it a successful recovery of the worker's mandatory validation: that worker never passed it. The exact established issue is the mismatch between an explicit problem signal, finished-worker submission and primary-output-based closure, compounded by inaccurate self-reporting and deletion of problem evidence. This merits separate status-contract adjudication, not an automatic rerun or frozen edit.

The old Letta Code amendment audit had already identified an inaccurate “mandated command” explanation after worker path shortening, but that worker repaired and passed. This new episode is a consequential recurrence of the explanation error with a different disposition. Correct final bytes and frozen validation limit its accepted-result impact; they do not erase it.

### O3 — Recovered provider errors are not unexecuted work or failed runs

Graphiti T/L183/c26/r1/m76 and Napkin T/L189/c24/r0/m62 contain “OpenAI Responses stream ended before a terminal response event.” Their proposed edit/write has no corresponding result; later calls resume the work. Instinctual T/L207/c34/r0/m35 has the same transport error attached to seven proposed reads without results; subsequent reads recover the inputs. Its profile worker c52/r0/m39 records a 503 upstream disconnect/reset error and later continues.

Thus nine emitted calls lack matched results: one Graphiti edit, one Napkin write and seven Instinctual reads. They explain the emitted/result difference, not nine independently failed jobs. All 67 outer analytical envelopes return exit 0, including the worker returning `problem`. Envelope success alone conceals both transport recovery and the status distinction in O2. No inference-time/service-wait decomposition or external exactly-once guarantee is available.

## Cost and comparison with the previous three analyses

### New timing boundary

Wall duration below is preparation `prepared-at` in the sibling `<worktree>.preparation.json` to the final publication-producing advance result: T lines 183/c78, 189/c66, 195/c55, 201/c53 and 207/c66. Ignore earlier c5 `publishable` text from setup. This common boundary excludes parent inspection/integration, this audit and later final-response/inspect overhead. The outer coordinator tool duration includes additional setup/reporting and is shown separately.

| System | Prepared-at UTC | Publication result UTC | Wall min | Sum worker min | Outer coordinator min | Reported worker / coordinator cost |
|---|---|---|---:|---:|---:|---:|
| Graphiti | 00:35:22.325056 | 01:47:15.323 | 71.88 | 76.94 | 74.34 | 6.971 / 0.326 |
| Napkin | 01:50:24.552681 | 02:48:39.428 | 58.25 | 65.49 | 60.48 | 4.823 / 0.263 |
| Letta Code | 02:51:17.780618 | 03:51:39.856 | 60.37 | 69.95 | 62.37 | 5.003 / 0.236 |
| Dynamic Cheatsheet | 03:54:32.068379 | 04:42:04.822 | 47.55 | 53.38 | 49.48 | 3.738 / 0.233 |
| Instinctual Memory | 04:44:31.844165 | 05:49:46.708 | 65.25 | 69.06 | 67.65 | 5.265 / 0.275 |

Costs sum exposed assistant `usage.cost.total` separately for analytical workers and coordinator messages; they exclude diagnostic, parent and auditor usage. They are harness-reported estimates, not a billing invoice. Summed worker durations include internal specialist overlap; the five runs themselves are sequential. Neither costs nor spans isolate repair, reasoning, tool latency or provider wait.

For reproduction and cost localization, the following lists every analytical worker as `coordinator-message/result: attempt-role, minutes`; correction roles reuse the role name but have distinct attempts.

- Graphiti: c18/r0 boundary 3.12; c22/r0 runtime 6.43; c26/r0 memory 7.09; c26/r1 epistemic 11.47; c26/r2 workflow 2.23; c30/r0 reconciliation 2.78; c36/r0 report verification 6.00; c40/r0 runtime correction 2.24; c44/r0 memory correction 2.70; c44/r1 epistemic correction 2.03; c48/r0 reconciliation 3.15; c52/r0 report verification 5.26; c56/r0 profile 6.01; c60/r0 profile verification 3.51; c64/r0 profile correction 2.60; c68/r0 profile verification 3.12; c72/r0 synthesis 4.11; c76/r0 synthesis verification 3.09.
- Napkin: c20/r0 boundary 3.90; c24/r0 runtime 8.68; c28/r0 memory 8.63; c29/r0 epistemic 9.09; c30/r0 workflow 3.62; c36/r0 reconciliation 3.07; c40/r0 report verification 5.73; c44/r0 profile 6.09; c48/r0 profile verification 3.22; c52/r0 profile correction 2.50; c56/r0 profile verification 3.72; c60/r0 synthesis 4.03; c64/r0 synthesis verification 3.22.
- Letta Code: c19/r0 boundary 4.47; c23/r0 runtime 9.50; c27/r0 memory 10.52; c28/r0 epistemic 10.74; c29/r0 workflow 3.65; c33/r0 reconciliation 4.23; c37/r0 report verification 9.12; c41/r0 profile 6.33; c45/r0 profile verification 3.51; c49/r0 synthesis 4.79; c53/r0 synthesis verification 3.09.
- Dynamic Cheatsheet: c19/r0 boundary 3.75; c23/r0 runtime 6.76; c27/r0 memory 6.82; c27/r1 epistemic 9.82; c27/r2 workflow 3.12; c31/r0 reconciliation 3.01; c35/r0 report verification 5.19; c39/r0 profile 4.63; c43/r0 profile verification 3.22; c47/r0 synthesis 4.11; c51/r0 synthesis verification 2.95.
- Instinctual Memory: c18/r0 boundary 3.23; c22/r0 runtime 7.86; c26/r0 memory 8.58; c26/r1 epistemic 6.99; c26/r2 workflow 2.67; c30/r0 reconciliation 3.30; c34/r0 report verification 7.92; c40/r0 runtime correction 2.26; c44/r0 reconciliation 3.29; c48/r0 report verification 5.75; c52/r0 profile 5.81; c56/r0 profile verification 3.51; c60/r0 synthesis 4.50; c64/r0 synthesis verification 3.40.

Rounding individual spans can differ from the rounded aggregate. Workflow workers total about 15.29 summed minutes, but this is not the marginal cost of adding workflow: other workers read/use it, and repairs change later work. Graphiti has 18 model attempts versus the 11-worker no-semantic-refusal paths in Letta Code and Dynamic Cheatsheet. Napkin adds profile repair/reverification; Instinctual adds runtime repair/reconciliation/reverification. Verification benefit and expense are both visible; no optimal reviewer count follows.

### Historical comparison boundary

The preceding same-source sets are `AAS-2026-10-11-graphiti-72c99440b180-01`, `AAS-2026-10-11-napkin-28752ba411ea-01` and `AAS-2026-10-11-letta-code-9d060e7dab7e-01`. All used `method-commit: 48453a8110bd36bc51fbcad3e9b2b394b694f603`, the same source revisions as their new counterparts, and Sol/medium. Worktrees are named `<system>-<old-token>`. I independently checked their journal/retained byte agreement and frozen validators. I did not apply the later workflow contract to them.

The [Graphiti](./graphiti-72c99440b180-amendment-effects-audit.md), [Napkin](./napkin-28752ba411ea-amendment-effects-audit.md) and [Letta Code](./letta-code-9d060e7dab7e-amendment-effects-audit.md) audits supply historical trace counts and their timing definitions. Their old worker traces reside respectively in sibling session files ending `01a12b96-f8c2-745a-b8d3-80b534c425e7`, `01a12b97-d2f5-7274-939c-cb3181407ed7` and `01a12b97-6580-74ff-ac08-71cf6ff28392`. Old episodes are located by those reports' L/R/m conventions, not the new coordinator nesting. Independently re-extracted samples were Graphiti L29/R0/m69–74 (ambiguity and distinctive-quote repair), Napkin L29/R1/m84–87 (shortened artifact and corrected pass), and Letta Code L29/R1/m59–68 (shortened artifact, false verbatim-command explanation and final pass). These samples support recurrence; the aggregate old totals remain attributed to the prior audits.

| System | Old → new workers | Old → new summed worker min | Old reported wall → new common-boundary wall min | Old → new failed direct validators |
|---|---:|---:|---:|---:|
| Graphiti | 13 → 18 | 74.83 → 76.94 | 71.60 → 71.88 | 2/16 → 8/28 |
| Napkin | 14 → 13 | 78.36 → 65.49 | 75.53 → 58.25 | 2/18 → 3/17 |
| Letta Code | 18 → 11 | 90.51 → 69.95 | 89.67 → 60.37 | 7/26 → 8/20 |

Old wall boundaries differ: Graphiti preparation record to publication, Napkin start-result to publication, Letta Code preparation call to publication. The table retains them rather than manufacturing identical measurement. Old runs overlapped across systems; the new five did not. Uncontrolled model exploration, repair scope, source-specific complexity, service recovery and earlier concurrency prevent causal attribution or speed claims for workflow.

The accepted-result comparison is mixed:

- Graphiti gains the explicit notebook transition/origin repair and keeps evaluator character-slicing and single/bulk raw-retention qualifications. It still lacks the saga reset, reverse-index and MCP instruction-channel qualifications identified previously. Rechecking old and new artifacts against the same source prevents calling these source changes or newfound target regressions.
- Napkin's old synthesis already characterized session distillation, create-example mismatch, request-owned retrieval and evaluation limits. The new workflow connects post-write diagnosis and reporting more explicitly, while the separate background-distill declaration improves doctrine classification. Profile verification still has real classification work to do.
- Letta Code's old runtime already describes Task launch, output receipt and recovery. New workflow traces notification into parent continuation. Separate Workflow and initialization inventories remain bounded; old hook/security detail is not wholly replaced by the new member. Fewer repair attempts do not prove improved accuracy.

No old analysis is rejected for lacking a workflow member. No claim is made that all old warnings were corrected, or that the new lens caused either result gains or operational failures.

## Independent publication and validation checks

For each new run I independently compared:

1. The exact retained filename → SHA-256 map with `R/effects/publish.json["new"]`, including `ARTIFACT.yaml` and 12 Markdown members.
2. All manifest member digests with retained bytes, and working artifact member bytes with their retained digests. The working manifest and published manifest have different roles; they were not incorrectly required to be byte-identical.
3. Origin's integrated retained bytes with the worktree's retained bytes.
4. Every version-store filename with its content digest, and every published file digest with a present version blob. Version counts: Graphiti 103, Napkin 87, Letta Code 81, Dynamic Cheatsheet 81, Instinctual Memory 89.
5. Publication receipt `members` with the journal's new map, `published: true`, and input method/source identities. Resolve the receipt through the completed `publish` attempt's `outputs.receipt` digest into `R/state/versions/<digest>`; for Graphiti this is attempt `000052-publish`, digest `45cc1fa95705f2ebbc8410e0fa34d8b44aec487d357a93f824a2b2d1a6365dff`.
6. Source checkout HEAD with the recorded source revision and empty `git status --porcelain`.

All comparisons passed. There is no demonstrated publication drift, missing member, hash mismatch or source mutation. These checks certify byte agreement and provenance consistency, not factual correctness, source coverage or a successful target run. The old three sets' retained bytes also agree with their publication journals at the same source revisions.

Each validator was called from its own worktree using that worktree's `.venv/bin/commonplace-validate`, with no output-file option:

```text
.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/<system>
```

The five new targets were graphiti, napkin, letta-code, dynamic-cheatsheet and instinctual-memory; the old three targets were graphiti, napkin and letta-code in their old worktrees. **All eight frozen-method checks returned exit 0, VALIDATION SUCCESS, Files analysed: 1, 0 failures and 0 warnings.** One analysed subject is the directory artifact, not one Markdown member. Later origin rules were not applied to old sets.

The origin validator is the separate check for this audit report:

```text
commonplace-validate kb/work/analysis-audit-evidence/reports/workflow-five-run-batch-audit.md
VALIDATION SUCCESS
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

It returned exit 0. No target tests or pytest suite were run: this is a Markdown evidence report, not a code change.

## Dispositions and requirements for later session-audit tools

The decision supported here is to keep using the workflow lens as a bounded connected-account requirement, while preserving local correction candidates and the status issue for explicit operator decisions. It is not an adopted method amendment or authorization to resume the held targets.

| Finding | Current disposition | What remains unknown or would change the decision |
|---|---|---|
| Five connected workflows | Retain | Pinned target runs could establish operation; outcome comparisons could test benefit. |
| Graphiti omitted state-reset/reverse-index/instruction channels | Local correction/qualification candidates | Full backend parity and runtime incidence are untested; selected notebook workflow remains valid. |
| Bad validator paths across five systems | Recurring worker error despite correct sampled delivery | Exact reuse enforcement and its cost need a separately authorized comparison, not another inferred generator defect. |
| Direct validation and quotation repair | Retain successful safeguards | Semantic interpretation and omissions require independent judgment; occurrence checks cannot replace it. |
| Semantic report/profile repairs | Preserve evidence of both detection and cost | No controlled comparison identifies an optimal review structure. |
| Instinctual explicit problem accepted and removed | Needs operator status-contract adjudication | Decide how finished-worker submission, problem persistence and worker validation obligations should interact. Final bytes passing does not settle the contract. |
| Recovered transport errors | Retain nested evidence | Outer exits do not locate effects, wait time or exactly-once behavior. |
| Sequential timing versus old concurrency | Descriptive only | Provider-load telemetry and controlled scope/profile conditions are absent. |

### Tool requirements, not an implementation backlog

A later Python session-audit workshop should make these checks reproducible without embedding new semantic verdicts in a parser. The purpose is evidence extraction for a bounded audit, not autonomous acceptance, replay or cleanup. These requirements arose from this audit; no tools are implemented or authorized here.

1. **Nested discovery and stable locators.** Search JSONL by run ID/task/tool-call ID and enumerate recursively embedded coordinator/worker results. Emit original file, one-based line and zero-based nested indices. Do not require standalone child session files or assume fixed current line numbers.
2. **Call/result accounting.** Pair by exact IDs within the proper envelope. Retain unmatched calls, result errors, transport errors and later retries separately. Return both emitted and matched counts; never count interrupted writes or reads as proven execution.
3. **Problem/status lineage.** Extract exact worker final text, `problem.md` write/result, coordinator completion/failure flags, engine closure and later judgments. Compare them without treating exit 0, `completed`, accepted content and published bytes as synonyms. Recover removed handout evidence from embedded reads/writes and version pins.
4. **Path checking against delivered bindings.** Parse supplied prompt assignments and literal commands; resolve relative paths against recorded launch cwd. Distinguish harmless spelling changes, wrong reconstructed paths and writes outside authority. Show the delivered and executed strings beside an inaccurate “as written” explanation. Do not infer a producer defect from a worker's report.
5. **Validation/status evidence.** Classify direct validators separately from wrappers; retain complete stdout/stderr/status and command locators. Treat search exit 1 and expected missing-path probes by context, not as automatic failures of accepted analysis. Flag compound-shell uncertainty rather than inventing upstream statuses.
6. **Read/truncation coverage.** Track file/range/offset reads, explicit harness truncation markers and recovery calls. Distinguish actual delivery truncation from quoted source text saying “truncated,” and advertised EOF remainders from substantive missing lines. Return unresolved coverage, not a fabricated full-read certificate.
7. **Timing and usage boundaries.** Export preparation, launch, nested message span, publication, final response and parent integration separately. Compute sums and interval unions, expose overlap and diagnostic exclusions, and label reported usage costs as estimates. Do not add repair windows already included in totals or attribute provider-error delay without telemetry.
8. **Frozen publication inspection.** Compare journal, receipt, manifest, version store, working member and integrated retained byte maps read-only. Record the exact validator executable/worktree/method and source HEAD/status. Missing evidence must remain missing rather than triggering an advance or repair.
9. **Small, resumable output.** Filter by envelope/event/category and paginate large text with explicit continuation. Return compact tables with drill-down locators, so a 50-KB truncation does not silently become audit coverage. Avoid copying encrypted reasoning signatures or huge inherited system prompts when the requested evidence is a command or status event.

Parser tests would need nested/parallel workers, same-name retry attempts, transport-interrupted calls, false success envelopes, completed outputs plus problems, disappearing handouts, path aliases, expected nonzero searches and real versus textual truncation markers. Any reusable implementation, fixture retention, broader graph connection via `cp-skill-connect`, or method change needs a separate commission. The present report leaves all evidence and parent-owned navigation unchanged.
