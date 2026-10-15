# Synthadoc exact-publication audit

## Decision

**Integrate with recorded limits.** No consequential defect was established in the bounded discrepancies checked. The public synthesis already distinguishes implementation from operation, session-summary storage from delivery, optional checks from factual guarantees, and trace-fed writes from measured improvement. This is an audit recommendation, not integration or certification of exhaustive worker compliance.

## Identity and authority

- Exact run: `AAS-2026-10-15-synthadoc-a3cae9152fff-01`.
- Auditor: independent project worker; runtime states `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`; session `01a13eb9-0a85-72fb-b799-6e06db20f97c`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/synthadoc-a3cae9152fff` (abbreviated `WT` below).
- Preparation: `WT.preparation.json`, inventory status `ready`; token `a3cae9152fff`.
- Method and independently checked worktree HEAD: `a568c6dc489ad546374536b642c3889ce23149a8`.
- Source: `https://github.com/axoviq-ai/synthadoc`; `WT/related-systems/axoviq-ai--synthadoc` (abbreviated `SRC`); independently checked HEAD `b80d9388a3013e8051baf2854c7250942c46e91a`. `GIT_OPTIONAL_LOCKS=0 git status --short` there returned no changes.
- Publication: `WT/kb/agentic-system-analyses/retained/synthadoc` (abbreviated `PUB`). No origin incumbent is recorded in the assigned inventory row.
- Trace: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/synthadoc.output` (abbreviated `TRACE`).

Read the complete commission, audit procedure, earlier substantive commission, repository instructions, work collection contract and workshop framing, plus this exact inventory row. No delegation, acquisition, target execution, run advancement/recovery, shared bookkeeping or publication edits were performed. Only this report was authored.

## Method and byte identity

Used a discrepancy-led comparison rather than a second analysis: read the historical review and public overview/synthesis, selected memory routes, and frozen code for the consequential differences below. Read selected actual nested worker call/result pairs and publication records. Historical material was used only by this auditor, not passed to analytical workers.

Recomputed SHA-256 for **all 13 actual publication files** and compared the complete filename set and each hash with the assigned inventory map. All matched. The completed `effects/publish.json` records this exact run/source and identical `new` map; `state/attempts/000033-publish.json` is completed and pins the assembled manifest and published member versions. In particular:

- assembled `ARTIFACT.yaml`: `4621d6a86efe5b5f54d6d8c74e8143b85e62bba7c0b03852988d4647b00e4fa1`;
- `overview.md`: `074011fdde5d4d6918e252c432f384169432b17bde3187096c69fcfb269c07a2`;
- `synthesis.md`: `1b38b997f1c7b133c2aebb4af9406cf9cb4d060b6eeab423c17201020ee70dd4`.

The working type declaration is not the assembled manifest; the inventory separately records its hash as `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322`. I did not substitute it for the publication.

## Consequential comparison

Historical lead: `kb/agent-memory-systems/reviews/synthadoc.md`, last checked 2026-06-05, reviewed commit `a77bdaeace7b3a461837936090624462690ee4ed`. This is a different revision from the frozen run. I did not acquire or inspect that old checkout, assert source equivalence, or establish when features changed.

1. **Session memory now has a concrete read-back route, but not summary-fed answering.** The historical review says stored sessions do not feed prior messages into answers. Current `SRC/synthadoc/integration/http_server.py:1400-1519` loads messages, selects the last `turns * 2`, stores overflow summaries, and passes only `_history` to `orch.query_stream`; summary values control regeneration/notice rather than become history. Query-agent searches locate subsequent history trimming and prompt construction. `PUB/memory.md`, `MEM-RTE-session-context`, and the public synthesis's “Later questions” section preserve this distinction and also disclose language-based eviction and history-free cached answers. The historical negative is not a current-coverage requirement. No loss or hidden long-conversation recall guarantee was established.

2. **Trace-fed compilation is supported, not generalized experience learning.** The historical review did not identify a durable trace-distillation loop. Current `SRC/synthadoc/skills/session/scripts/main.py:20-226` registers JSONL extraction, filters roles, sidechains and tool/thinking/image blocks, applies minimum word counts, and returns rendered turns as extracted content. `MEM-RTE-session-ingest` explicitly specializes ordinary source ingest rather than claim a separate verified-experience pipeline. The public synthesis says imported turns can feed durable wiki writes while withholding improved capacity, measured benefit, verified operational experience and automatic ingestion of every interaction. This is a useful current addition, not a contradiction resolved by assuming historical truth. Audit inspection verified the extractor; it did not independently retrace every ordinary ingest consumer edge.

3. **The old “warnings, not gates” account is no longer an adequate universal description.** `SRC/synthadoc/agents/lint_agent.py:824-938` partitions fresh/cached content, applies an optional positive-threshold gate to fresh pages, demotes eligible active/stale pages, and separately blocks automatic resolution at the threshold. Cached pages report retained warnings without reapplying demotion. The public synthesis's checks section carries both the optional restriction and cached-page limitation. No unconditional human-review or correctness guarantee is inferred.

4. **Citation support checking is more than structural validation, but remains fallible and potentially stale.** `SRC/synthadoc/agents/citation_faithfulness_agent.py:160-245` constructs claim/source-line comparisons, invokes a provider and emits skipped verdicts on provider/parse/missing-index failures. `faithfulness_cache.py:32-48,76-134` keys freshness to ingestion timestamps, restricts stale selection to active pages and can retain empty-result entries. The public synthesis distinguishes semantic support assessment from source truth, whole-page acceptance and automatic demotion/rewriting, and names timestamp rather than exact-content freshness. The historical review's structural-versus-semantic concern is not silently lost.

The public overview's description withholds factual acceptance and successful self-improvement; its deterministic-validation section expressly denies semantic certification. The synthesis expands those qualifications and already carries selective workflow/client coverage, external-executor boundaries, non-global withdrawal/restoration, initialization gaps and absence of adopted target execution/causal evidence. I did not independently certify every such route.

## Selected operational evidence

Parsed completed `tool_execution_end` nested `result.details.results[].messages`, matching each assistant `toolCall.id` to a `toolResult.toolCallId` **within that worker**. Stream updates and repeated transcript snapshots were not counted as extra actions.

- `TRACE` JSONL line **1756**, worker task `000007-memory`: executed reads `call_b81nuAgrRHffvkD0JvKuXoY6` and `call_Nz9jvJDO8d15OOF2RrHjEKWr` returned session extractor lines 1–190 and 191–230 successfully. This is actual source-reading evidence for the trace-filter finding, not merely an asserted citation.
- Same worker/result: `call_qKgG2J0WDIBpbieyL5oVaSPp` ran `commonplace-run validate-output` and failed with an ambiguous quotation occurring twice in `http_server.py`. `call_gGnXsB6NFCfn9hfzXDTm7Nxx` successfully changed attribution to `http_server.py:794-795`; `call_07Cf2zF3WxxhDMWwBY7kYSv0` reran validation and returned “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This was deterministic repair, not semantic refusal.
- `TRACE` line **1756**, separate worker `000008-epistemic`: `call_6pxfj6Vf2GozI44PZTizSZXx` likewise failed ambiguous-quotation validation; `call_unxiyP44H7SbbVYtGm5977xg` supplied range `792-794`; after further report edits, `call_yG8pB5xsxNkIo3W7uc7tl070` returned the same qualified content-check pass. A failed `wc` lookup for nonexistent `synthadoc/core/retraction.py` preceded successful investigation of `core/retract.py`; it is not evidence of source unavailability.
- `TRACE` line **2508**, worker `000022-report-verification`: `call_nd3tr0QSSKhoLYpNnu3yJSN9` successfully read its complete invocation; `call_VJ7RYDqJYNLOJ5XmbSAHMJsH` read `http_server.py:1400-1574` successfully. `call_LTI74S4pNC9uDul5a3NmaJns` returned source searches for faithfulness keys, exports, consumer and context budgeting. `call_9Uao7HNQrtv9AmD6OYTSwUln` wrote verification; `call_DRrB76iQ4Wd2X4TvLGCHuO41` returned the qualified content-check pass. These support performed verification work, not exhaustive fulfillment.

Call IDs above use their unique pre-`|fc_` portion; the full IDs remain in those exact trace records. The selected evidence did not establish semantic refusals or consequential scope violations. It does not establish their absence elsewhere.

Direct audit read of `WT/kb/agentic-system-analyses/state/AAS-2026-10-15-synthadoc-a3cae9152fff-01/state/handouts/000022-report-verification/prompt.md` failed: `ENOENT: no such file or directory, access` at that absolute path. I recovered the complete historical invocation-read result from the same worker in `TRACE:2508`; I did not recreate the handout or infer its current presence. This limits direct filesystem replay, not the observed historical call/result pair. Engine acceptance alone was not used to resolve this gap.

## Validation and remaining limits

Commands were called from `WT`, each with recorded prefix:

```text
PATH="/home/zby/llm/commonplace/.commonplace/worktrees/synthadoc-a3cae9152fff/.venv/bin:$PATH" commonplace-validate kb/agentic-system-analyses/retained/synthadoc
PATH="/home/zby/llm/commonplace/.commonplace/worktrees/synthadoc-a3cae9152fff/.venv/bin:$PATH" commonplace-validate --full kb/agentic-system-analyses/retained/synthadoc
```

Both exited 0. Summary: `VALIDATION SUCCESS`, one directory artifact analysed, zero text files, **0 failures and 0 warnings**. Full output checks all twelve Markdown members, schemas, quotes, source register, references and set relations; `Overall: PASS (clean)`, `WARN`, `FAIL` and `INFO` all `(none)`. No source-unavailable notice appeared. This is deterministic validation, not independent semantic quote certification.

From the same `WT` cwd and PATH prefix, ran `commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-15-synthadoc-a3cae9152fff-01.md`. Exit 0: `VALIDATION SUCCESS`; files analysed 1, text files 1, **0 failures and 0 warnings**; no notices were emitted.

This audit is selective: no target commands/tests/provider runs, old-revision inspection, complete worker-obligation replay or exhaustive public-claim check. No further source expansion is needed for the bounded recommendation. Integration requires parent review and a fresh byte-map check preserving the exact publication and its existing public limits. If those qualifications are removed or source/publication identity changes, re-audit before integration. Claims of successful factual maintenance, causal benefit or exercised self-improvement would require separately authorized provenance-linked runs and controlled comparisons; this audit does not unblock those stronger claims.
