# ReasoningBank exact-publication audit

## Decision

**integrate with recorded limits**. No consequential defect was established in the selected checks. The public synthesis already distinguishes ordinary advice supply from demonstrated reliance or improvement, and exposes broken scaling and unresolved standalone invocation. These qualifications materially improve on the historical account. This is an audit recommendation, not integration authority or certification of every worker obligation.

## Identity and authority

- Exact run: `AAS-2026-10-14-reasoning-bank-f0bedcab086c-01`.
- Auditor: independent project worker, `openai/gpt-6.1-sol`, medium; runtime `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`; session `01a13e84-cdfa-7614-b621-42ade516d21f`.
- Worktree W: `/home/zby/llm/commonplace/.commonplace/worktrees/reasoning-bank-f0bedcab086c`.
- Method: `a568c6dc489ad546374536b642c3889ce23149a8`; independently checked W HEAD equals this revision.
- Command prefix: `W/.venv/bin` (W expands to the absolute path above).
- Frozen source S: `W/related-systems/google-research--reasoning-bank`, identity `https://github.com/google-research/reasoning-bank`, revision `ed80611788292ea739f1effd31f16c53823b8a0d`. Independent HEAD/status checks found that revision and no source changes. Used Git's `--no-optional-locks` for status.
- Publication P: `W/kb/agentic-system-analyses/retained/reasoning-bank`.
- Run state R: `W/kb/agentic-system-analyses/state/AAS-2026-10-14-reasoning-bank-f0bedcab086c-01`.
- Read the complete commission, audit procedure, earlier substantive commission, root instructions, work collection contract and workshop README. Sole authored output is this report. No delegation, acquisition, source expansion, engine mutation, integration or Git mutation was performed.

Independently SHA-256 checked **all 13 files** against this run's exact JSON inventory row: `ARTIFACT.yaml`, `boundary.md`, `epistemic.md`, `memory-profile.md`, `memory.md`, `overview.md`, `profile-verification.md`, `reconciliation.md`, `report-verification.md`, `runtime.md`, `synthesis-verification.md`, `synthesis.md`, `workflow.md`. All matched; directory enumeration found exactly those files. The assembled manifest hash is `968919ebbaaf768d4532cd3c33ac27a86352864da6c2df340aa09c074e558092`, distinct from the inventory's working declaration hash. `R/state/attempts/000043-publish.json` records completed publication with that assembled manifest pin. W status showed the untracked retained publication, not a clean integrated checkout. No origin incumbent was supplied; this audit does not authorize replacement of another publication.

## Bounded method and historical boundary

Read the historical lead `kb/agent-memory-systems/reviews/reasoning-bank.md` completely. It declares the same repository URL and revision but a different local source path and an earlier review date. That declaration is a coverage lead, not independently established equivalence of its former checkout or an endorsement of its claims.

Selected discrepancies were: whether top-1 retrieval actually ensures useful advice, whether memory-aware scaling really combines distinct trajectories, and whether internal verification corrected the standalone-induction implementation overclaim. Read public overview, synthesis, boundary and report verification; searched the corrected epistemic record. Independently inspected the frozen selector, web runner selection block, coding driver, coding system-message construction, scaling driver/inductor/client definitions and standalone induction script. No target code or provider was executed. This is not a second complete analysis or exhaustive rereading of every report/adapter.

## Consequential findings

### 1. Retrieval coverage is preserved, with a necessary stronger qualification

Historical core/read-back sections describe top-1 prior-query selection, all selected memory items, query-cache growth and system-message injection. P's synthesis, “A new task receives selected prior advice,” retains these mechanisms and explicitly says an unmatched top ID yields no advice rather than falling back to lower-ranked IDs. It also separates record count from item/token budgets and ranking from truth or success filtering.

Independent evidence: S `WebArena/memory_management.py`, `screening` loads the prior cache, appends the current query, then ranks the old snapshot. `select_memory` truncates ordered IDs before joining each to the first matching bank row. S `WebArena/run.py`, memory-enabled portion of `main`, calls `select_memory(n=1)` and joins all `memory_items` into the overwritten delivery file. S coding `run/extra/swebench.py`, `process_instance`, similarly selects one row and joins all items. Coding `agents/default.py`, `DefaultAgent.run`, appends that string to the system message with relevance discretion. Thus delivery is wired, not proof of model use. The overview description and opening synthesis already say operation/transfer/improvement are unobserved. No consequential historical coverage loss was found in this check.

### 2. Scaling is a corrected historical overstatement, not a regression

The historical “Memory-aware scaling” paragraph says repeated trials provide better evidence and synthesized memories; its curiosity section notices inverted reward labels. The new synthesis instead states that working distinct-trajectory comparison is not established, naming repeated final-directory input, missing model forwarding, uninstantiated client and incompatible tuple payload. It also correctly distinguishes the inverted local status variable from an explicit generator label.

Independent evidence: S `WebArena/pipeline_scaling.py`, `main`, launches `results_i` trials but passes only the final `results_{i}` to induction, without `--model`. S `WebArena/induce_scaling.py`, `main`, repeatedly assigns the same `args.result_dir`, assembles query/steps without status, sets `client = CLIENT_DICT[args.model]` and calls its instance method without construction. S `WebArena/utils/clients.py` maps model names to classes and ordinary chat methods return `(response, completion)` tuples. S web runner expects string blocks for joining. The selected public warning is source-supported; the audit does not need a runtime failure demonstration to reject treating this as established working synergy.

### 3. Coding feedback is not correctness or advice acceptance

The public synthesis says saved prediction delivery precedes judging and induction, errors can still become predictions, restart can skip incomplete admission, and the judge's substring parser admits `unsuccessful` as success. S `third_party/src/minisweagent/run/extra/swebench.py` directly supports the ordering and parser: `save_traj`, `update_preds_file`, transcript filtering, `llm_judge_status`, then unconditional generated-item append using the selected success/failure prompt. Existing prediction keys are skipped by `main`. This is a useful correction to reading the historical outcome-gated induction description as validated learning. The public text already states no external SWE-Bench test outcome is supplied to that judge and no semantic gate validates generated advice.

### 4. The standalone-induction objection was actually processed

The first report verification raised a semantic blocker, not a deterministic schema failure. `R/state/judgments/000023-apply-report-verification-1.json` objects that `EPI-RTE-legacy-induction` was labelled `wired` despite an unestablished import/launch contract. Attempt `000024-epistemic` records a refusal pin against the previous epistemic version, then corrected report hash `a01983eae2e10d21bcf809df7613ba223fd6884cd43980fa3ae280e46384f060`, matching the accepted/public file.

The current epistemic record uses `afforded`, an intended immediate return and unresolved launch context; final report verification discharges the blocker. Independent reading of S standalone `third_party/src/minisweagent/memory/induce_memory.py` confirms differently rooted `memory.memory_management` and `instruction` imports. This supports retaining uncertainty, not universal impossibility. Public synthesis names the unresolved invocation and unestablished destination consumer; no audit-only repair is needed.

## Selected actual worker evidence

Trace T: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-14/reasoning-bank.output`. Locators below are physical JSONL line numbers, `result.details.results[0].messages` indexes (zero-based), and tool-call IDs. I used final `tool_execution_end` subagent results, not duplicate streaming updates, and matched assistant calls to tool results within the same worker.

- T line **2403**, first report verifier: messages **108 → 109**, call `call_JU01yFuRj1GY64Na775xegBJ|fc_0387bb6c0a520482016acfe8df614487d2902de5349aa84209`, wrote the verification and received successful write result. Its supplied content SHA-256 equals retained version `e4ee8ded9048de939a3e066f34da32f101026946a35db9c10a6d041462cda494`, the blocker-bearing verification consumed by attempt 23.
- T line **2710**, correction worker: **36 → 37**, call `call_xIMfOkdS6qruQqZh3RwetT2O|fc_06c4170756ece7f5016acfe978de5c87d2a5076a7c7dd8f29c`, reads the standalone source and receives code, not an unavailable-source notice. **44 → 45**, call `call_XpMSLTXPdHGuMlB4KtXW6RB8|fc_06c4170756ece7f5016acfe986ead487d2abcddbb1ce9edbd3`, edits its owned report with a result confirming eight replacements. **46 → 47** writes correction answers successfully; content hash matches attempt 24's `ad40e659e1dbef79305c1256a25f4f3d0204bfa258cdbc54c5c91c9b65a9dbc8`.
- T line **3392**, final report verifier: **75 → 76**, call `call_Jmlc8kUhrhVziAAETxGkBFxK|fc_05b15f6d0522f9fc016acfeb033ba887d2954c61443ea48132`, independently reads that source successfully; adjacent calls/results read dispatch and package metadata. **67 → 68–70** actually reads scaling inductor, driver and clients. **120 → 121**, call `call_gLNJcQWPdhYsZRKCeTFtGX0A|fc_05b15f6d0522f9fc016acfeb58c93487d2b22b3e7b89ad7107`, successfully writes final verification; content hash matches published `61edbd38964e2a7bfbef9ced9e00fea342dda1a273f70cb6fb25c4a3f73dd202`. **122 → 123** executes `commonplace-run validate-output` and receives: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.”

All listed pairs have `isError=false`; selected nested workers report Sol/medium and exit 0. These establish performed source inspection, correction and checking, not exhaustive worker compliance. No consequential scope violation was established in this sample; I did not inventory every action across every worker. The named handout directory is no longer present locally (`ls` returned “No such file or directory”); retained versions/attempts and the nested final trace preserve the selected evidence. I did not reconstruct it or invoke recovery.

## Validation and remaining limits

From W, used exactly the recorded prefix:

```text
W/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/reasoning-bank
W/.venv/bin/commonplace-validate --full kb/agentic-system-analyses/retained/reasoning-bank
```

Both exited 0. Summary: `VALIDATION SUCCESS`, files analysed 1 (the directory artifact), text files 0, 0 failures, 0 warnings. Full output checks all twelve Markdown members plus directory schema/member-role relations; `WARN`, `FAIL`, `INFO` are each `(none)`, overall `PASS (clean)`. No source-unavailable notice occurred. Deterministic success does not certify quotations or semantic completeness.

From W, report validation used `W/.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-14-reasoning-bank-f0bedcab086c-01.md`. It exited 0: `VALIDATION SUCCESS`, files analysed 1, text files 1, 0 failures and 0 warnings; no notices were emitted. No publication was patched. No tests, experiments, live environments or extra sources were used. Generated advice content, actual downstream reliance, causal improvement, provider/environment reproducibility, all-entry-point equivalence and exhaustive operational compliance remain unverified. The public synthesis already makes these limits visible.

No semantic unblock is required for this recommendation. Parent should recheck the exact byte map and review the report before authorized integration. A changed publication needs renewed review. Stronger scaling/standalone/benefit claims would require separately authorized invocation evidence, corrected contracts or causal comparisons as appropriate; they must not be inferred from publication acceptance. Broader graph discovery is outside this audit; any later `cp-skill-connect` work requires separate scope.
