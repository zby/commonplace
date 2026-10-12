# AgentFly pre-integration audit

## Disposition

**Integrate with recorded limits.** No consequential missing qualification or coverage regression was established in this bounded inspection. The central case-reuse and separately trained retriever account is useful. The publication already withholds demonstrated improvement, autonomous retraining/deployment, exact checkpoint provenance and complete tool-side-file inventory. The known side-file inventory defect is explicitly carried into the public synthesis; this audit does not repair it.

No audit blocker remains. The parent still owns integration's exact publication checks and origin readiness. This is clearance for integration, not integration itself.

## Identity and inspection boundary

- Audit date: 2026-10-12.
- Auditor: fresh independent `openai/gpt-6.1-sol`, medium thinking, Pi; session `01a131a5-1ea4-7605-a03a-ede02b2be653`. No analytical worker was launched or given historical/audit findings.
- Run: `kb/agentic-system-analyses/state/AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/agentfly-bbfc9fb2d5c7`; command directory `.venv/bin`.
- Method: `0b37f22ae1a989fe806c754fea1fe8c1c8e36c63`, independently confirmed as worktree HEAD.
- Source: `https://github.com/Agent-on-the-Fly/AgentFly`, commit `42fbbcac63dd58ed6856c0761357345a58e4f032`; independently confirmed HEAD and clean status at `related-systems/Agent-on-the-Fly--AgentFly` in the worktree.
- Publication: worktree `kb/agentic-system-analyses/retained/agentfly/`, starting at `overview.md`.
- Historical lead: origin [AgentFly review](../../../agent-memory-systems/reviews/AgentFly.md), checked 2026-06-04 at the **same source commit**. It is a memory-focused account, not an independent warrant for its claims or an expectation that the new whole-runtime account repeat Commonplace borrowing advice.

Approach: read the overview, synthesis, boundary, reconciliation, memory profile and report/profile verifications; compare historical mechanisms and qualifications; inspect selected frozen producer/consumer branches; inspect attempts, judgments, publication journal and nested validation traces. Stop short of a second whole-source analysis. All locators below are relative to the prepared worktree unless explicitly identified as origin or external session storage.

## Consequential findings

### 1. Core historical coverage survives, with stronger qualifications

The publication preserves the serial planner–executor runtime, two compact case-bank schemas, positive/negative examples, rich results separate from served plans, query-conditioned ranking, automatic benchmark writes/reloads and offline retriever training. Its synthesis distinguishes trained retrieval weights from unchanged planner/executor LLM weights and guidance delivery from demonstrated dependence or improvement.

A consequential correction to the historical borrowing claim is visible: training labels are **whole-answer correctness copied to each retrieved case**, not independently judged case usefulness. I checked `client/parametric_memory_cbr.py:499–521,530–590`: one `is_correct` value feeds every retrieved-case pair; result persistence precedes pair/case writes; restart reads question identity; the subsequent call reloads the bank. The public synthesis explains the label proxy, absent judge-reason read-back and nontransactional retry suppression. `memory/train_memory_retriever.py:230–253` splits pair rows using labels, not question groups, consistent with its leakage qualification.

Evidence: `synthesis.md`, sections “From completed work to later guidance” and “From outcome pairs to numerical ranking”; records `MEM-OBJ-training-data`, `MEM-OBJ-query-record`, `RT-RTE-case-admission`, `RT-RTE-retriever-training`.

### 2. Automation and withdrawal limits are public, not audit-only

The separate trainer is not an automatically scheduled live weight refresh. Bank reload must not be mistaken for checkpoint reload. `client/parametric_memory_cbr.py:337–345` also leaves a loaded pool unchanged if the bank file disappears; parse failure clears it. These qualifications are present in reconciliation and synthesis. README's checked continual-learning TODO and named `retrain.sh` do not establish shipped scheduling. No stronger historical automation claim needs preservation.

Evidence: `reconciliation.md`, “Training configuration” and “Withdrawal and recovery”; `synthesis.md`, corresponding mechanism paragraphs and limitation rows; source `README.md:349,392,399` and the driver branches above.

### 3. Known side-file defect warrants a recorded limit, not a hold

The accepted memory inventory's cache-location description is too coarse and omits an XLS-to-XLSX side file. Frozen source confirms DOCX/Chunkr basename outputs in the working directory, PPTX images based on the source stem, cache-based unzip output and sibling XLSX conversion. The report verifier identifies this defect and the synthesis repeats it in both prose and its limitations table. Readers are expressly prevented from deriving complete location, withdrawal or cleanup comparisons. It does not change compact case reuse or establish automatic document ingestion into the case bank.

Evidence: `report-verification.md#limits`; `synthesis.md#limitations`, “Side-file locations and inventory are too coarse”; `server/documents_tool.py:156–158,180–182,238–243`; `server/excel_tool.py:41–48`.

### 4. Comparison-value changes are explained rather than lost mechanisms

Unlike the historical review, the new profile classifies requested case retrieval and fulfilled delivery as pull; startup/reload supply is a separate push operation. It does not count full retained tool traces as learning inputs merely because result files contain them. Its rationale also separates case advice, ranking parameters, training inputs and restart enforcement. These changes have explicit consumer-level explanations; they do not erase example delivery or numerical updates. The current type's request/delivery rule supports the pull distinction. Historical vocabulary is not a reason to retain old comparison values.

Evidence: `memory-profile.md#comparison-rationale`; `profile-verification.md#verification`; method `kb/agentic-system-analyses/types/agentic-system-memory-profile.md:171–180`.

## Operational checks

All 33 stored attempts are completed with empty `problem` fields. All stored judgments inspected report accepted outcomes and empty findings. The publication effect journal is completed. Independently computed hashes of all 13 retained files exactly equal `effects/publish.json`'s `new` map; all 12 Markdown members are byte-identical to the run artifact. The sole artifact-tree difference is `ARTIFACT.yaml`: publication adds member hashes and the worker identity, rather than changing analytical content. Model attempts record Sol/medium; publication records `pi-sol`.

Publication success was not used to infer worker preflight compliance. Nested traces are retained inside origin coordinator-session storage:

`/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T18-52-06-274Z_01a13175-3102-76ed-b2e9-63d6c88be8db.jsonl`

Locate message `d9377b88`, then `message.details.jobs[0].result` (the completed AgentFly coordinator). The following zero-based nested message positions pair actual `commonplace-run validate-output` calls with their returned results in the **same worker**. All final results say “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Calls use this worktree's command directory and the matching run/attempt prompt path.

| Coordinator message / result | Attempt | Worker call → result positions |
|---|---|---|
| 15 / 0 | 000003-boundary | 56 → 57 |
| 19 / 0 | 000005-runtime | 49 → 50 |
| 23 / 0 | 000007-memory | 61 → 62; 65 → 66 |
| 23 / 1 | 000008-epistemic | 49 → 50 |
| 23 / 2 | 000009-workflow | 34 → 35 |
| 27 / 0 | 000019-reconciliation | 47 → 48 |
| 31 / 0 | 000022-report-verification | 96 → 97 |
| 37 / 0 | 000024-memory-profile | 52 → 53 |
| 41 / 0 | 000026-profile-verification | 59 → 60 |
| 45 / 0 | 000028-synthesis | 63 → 64 |
| 49 / 0 | 000030-synthesis-verification | 55 → 56 failed; 59 → 60 passed |

The synthesis-verification preflight failure was deterministic citation-label syntax: four links used short labels instead of record IDs. The later pass discharges that local check; it is not a semantic objection, hidden failed engine attempt or validation-path failure. Exact calls are `call_EGoSOWXqt5RgV10UOtUoVksm` and `call_SPfe393ga5UXydrID0VQkuF6` (match each full tool-call identifier to its result in the nested messages). No recurrence of the prior nonexistent-artifact validation-path problem was established.

## Coverage limits and follow-up

This audit did not execute AgentFly, reproduce benchmarks, inspect checkpoint contents, authenticate corpora, audit every tool transformation or independently reverify every runtime/epistemic record. Source checking concentrated on consequential learning/automation/recovery claims and the published side-file defect. Nested trace checking establishes the listed validation calls/results and profile settings, not compliance with every source-read, isolation or semantic worker obligation. Stored acceptance remains deterministic/engine evidence, not universal certification.

The public synthesis already carries the material evidence limits, including absent execution/causal comparisons and incomplete acquisition/payload assessment. A future path-by-path side-file analysis is needed before complete cleanup/location comparisons; linked training/deployment and intervention evidence is needed before automation or improvement claims can be strengthened. Neither is an integration unblock requirement for the current qualified publication.

## Report validation

Ran in origin with bare `commonplace-validate kb/work/agentic-system-reruns/audits/rolling-05-agentfly.md`: **VALIDATION SUCCESS**. One text file analysed; zero failures and zero warnings.
