# GBrain workflow-lens pilot check

## Recommendation

**Proceed: retain the pilot and proceed with the ten sequential workflow-enabled analyses.** The selected workflow is connected, useful and supported by the frozen implementation. It adds task submission, authority handoff, recovery ownership and result delivery to the runtime baseline. It does not fabricate a successful task or mistake queue completion for semantic success. Independent source checks found no material accepted-claim correction in this sample.

This is a recommendation to the parent, not integration or batch execution. One successful pilot does not establish consistent quality across ten systems or isolate the workflow lens's effect. The existing profile limitation and recovered worker errors should remain visible. Neither requires holding this pilot under the existing contracts.

## Provenance and scope

| Key | Value |
|---|---|
| run-id | `AAS-2026-10-11-gbrain-9de8e3c225d3-01` |
| method-commit | `8213c5f06ea86ec6c13dd3bedff6a66c6b0bd3ad` |
| source-revision | `da434385572e0dc0d825649179aabed4107d6e60` |
| source-identity | `https://github.com/garrytan/gbrain` |
| audit-date | `2026-10-12` UTC |
| reporter-profile | pi; provider `openai`; model `gpt-6.1-sol` (`openai/gpt-6.1-sol`); reasoning effort `medium`, from this reporter's `PI_*` environment |
| reporter-session | `01a12d81-93b7-719d-b066-af634bf8f982` |
| audited-worker-profile | `pi-sol`; pi; launch model `gpt-6.1-sol`; reported model `openai/gpt-6.1-sol`; effort `medium` |
| worktree | `/home/zby/llm/commonplace/.commonplace/worktrees/gbrain-9de8e3c225d3` |
| command-path | Worktree `.venv/bin`, invoked with that worktree as cwd |
| frozen-plan-sha256 | `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd` |
| workflow-sha256 | `b96fb69a2d2cf9a08e7f6bb52020ec7436a3fa92aa402b6567be49f351113722` |
| published-manifest-sha256 | `fd3deedf9ec21974e7fe3ec47b4675ca91684c95e5a3c8a73d1a7e12fbb03b7d` |

The sibling `gbrain-9de8e3c225d3.preparation.json`, opening metadata version `aca97aaba1dd01175b4f6ef890d10786234e154a6e23e77aab9492edbc19fdbb`, overview and Git HEAD agree on the method revision. The boundary and independently checked source HEAD agree on the source revision; source `git status --short` was empty. The opening's requested source revision is null: acquisition selected the frozen revision above. That null is not the evidence boundary.

Locators below use:

- **P**: worktree `kb/agentic-system-analyses/retained/gbrain/`.
- **R**: worktree `kb/agentic-system-analyses/state/AAS-2026-10-11-gbrain-9de8e3c225d3-01/`.
- **S**: worktree `related-systems/garrytan--gbrain/`, at the source revision above.
- **T**: `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T15-31-10-091Z_01a12b96-de8a-711e-8a12-57ef261a7126.jsonl`, line 159. Its embedded coordinator is `message.details.results[0]`. `C30/R2/m65` means coordinator message index 30, embedded result index 2, worker message index 65; all message/result indices are zero-based. The SHA-256 of the complete line 159 bytes, including its newline, is `c4257c59fb7df5178839bb6907f51dc9db2f07f28e4e22a801de8062ceb82384`.

I read P/workflow.md completely, together with runtime, boundary, overview, reconciliation, report-verification, profile-verification, synthesis and synthesis-verification. I inspected memory's replay annotation and related coverage statements, not the complete memory, epistemic or 1,413-line profile. Source spot-checks concentrated on consequential delegation, gateway selection, persistence/replay, pending-write handling, retry disposition, completion and polling. These are static implementation checks. No target execution, provider calls or recovery experiment occurred.

The [audit commission](../audit-an-analysis.md), [workshop framing](../README.md), work collection contract, frozen analysis collection contract, workflow type, set type and shared-record contract govern this check. Source and outputs remained read-only. The only authored artifact is this report; README ownership remains with the parent.

## Substantive findings

### F1 — The workflow adds end-to-end understanding

P/workflow.md selects an OAuth client's gateway-enabled subagent task and explains why: that branch connects delegation, tool effects, durable recovery and polling. Its progression is task submission → selected tools and prompt → model/tool rounds → worker settlement → owner polling. The task, job ID, owner-client identity and delegation snapshot connect those stages. They are not unrelated capabilities joined by analogy.

Relative to P/runtime.md's `RT-RTE-subagent-loop`, the workflow adds two genuinely different routes: `WF-RTE-agent-submission` and `WF-RTE-agent-delivery`. It annotates the existing execution route rather than redeclaring it. The useful increment is where responsibility changes: the client requests work; software admits authority; the model proposes tool calls; handlers execute; the worker decides retry and completion; the queue fences settlement; the client requests the retained result. This lets a reader distinguish an accepted task, an accepted write, a settled tool outcome, a completed job and a delivered answer.

The account describes machinery capable of multiple rounds, not an invented example in which the model actually used several tools. It explicitly allows a no-tool final response and makes no successful-execution claim. That is appropriate under the frozen workflow type's selective, source-supported requirement.

### F2 — Delegation and handoff are supported, with the branch condition preserved

Independent checks:

| Claim checked | Frozen source anchor | Assessment |
|---|---|---|
| Task submission requires a client identity and agent scope, validates the request and retains owner/grant state | S/src/core/ops/jobs.ts:339–492, especially 363–425 and queue add at 445–447 | Supported. The returned ID admits queued work, not a result. The job-data literal does not set `require_writes` or oneshot mode. |
| Gateway selection is conditional rather than automatically true for every submitted job | S/src/core/minions/handlers/subagent.ts:443–461, 574–591 | Supported. Executable selection uses configuration or the supported OpenRouter family. Workflow correctly qualifies the nearby submission comment's stronger assertion. |
| The model receives selected definitions and guidance, not the entire registry | S/src/core/minions/handlers/subagent.ts:469–493, 1185–1191, 1298–1314 | Supported. Selected guarded tools build the prompt and gateway definitions; the task supplies fresh user input or recovered history. |
| Submitted permission is a ceiling intersected with live grants | S/src/core/minions/delegated-policy.ts:123–164; complete delegated-tools.ts, especially 17–31 | Supported. Tool, prefix, source, scope, budget and concurrency intersections can narrow execution. Each guarded call refreshes the effective grant. |

The selected submission cannot opt into the handler's oneshot branch through its inspected job-data construction. This supports tracing the gateway-loop branch without silently incorporating a different mode. The analysis does not establish deployed grant values, human task authorship, provider compliance or universal isolation. Those qualifications remain beside the claims.

### F3 — Replay, pending writes and retries have bounded owners

S/src/core/ai/gateway.ts:4074–4220 confirms assistant persistence before dispatch, pending-row callback before registered execution, outcome settlement and tool-result persistence before the next model turn. S/src/core/minions/handlers/subagent.ts:1383–1471 confirms this caller supplies the callbacks and reads the canonical execution UUID from SQL `RETURNING`. Generic optional callbacks do not become a gateway-wide durability guarantee.

The actual resume path also matters. S/src/core/minions/handlers/subagent.ts:1214–1270 and 1553–1704 confirms prior transcript loading, dangling-result reconciliation, completed/failed outcome reuse, refusal of pending non-idempotent work and terminal-text early return. I checked that path, not only the generic gateway's similarly named replay branches. A non-idempotent pending refusal throws an ordinary Error in the inspected code; the account does not incorrectly promise immediate dead-lettering for that specific condition. The worker may retry until attempts are exhausted without safely repeating the tool.

Complete S/src/core/minions/tool-write-identity.ts and subagent.ts:1195–1209, 1449–1456 support stable write request identity, same-request waiting/replay and escape of a pending-write failure without settling its execution as failed. This is not universal exactly-once execution. Request identity generation also respects an already supplied request ID; the account need not imply every input gets a replacement identity.

S/src/core/minions/worker.ts:1571–1768 supports infrastructure-abort handling, lease-pressure release without attempt burn, delayed backoff and unrecoverable/exhausted dead disposition. The account is selective: configuration, deferred-job, shutdown and fleet paths are not exhaustively explained. Its full-fleet/reaper limitation prevents treating the abbreviated retry paragraph as an inventory of every error class. No exercised recovery is established.

### F4 — Completion and delivery are not semantic success

S/src/core/minions/handlers/subagent.ts:1481–1508 distinguishes clean termination, output cap, turn limit, refusal and abort mapping. S/src/core/minions/handlers/subagent-persistence.ts:247–304 confirms supplemental accounting over settled `brain_put_page` rows, stricter write-required behavior and fail-open accounting reads for open jobs. Neither is independent answer-quality review.

S/src/core/minions/worker.ts:1547–1560 and queue.ts:1706–1735 confirm normal handler return leads to transactional completion requiring active status and the current lock token. Stale completion returns null. S/src/core/ops/jobs.ts:513–598 confirms owner/subagent SQL filtering, uniform foreign/missing not-found, result parsing, capped error text and waiting position.

The polling operation is classified `outputRedaction: 'retrieval'` at jobs.ts:517. Workflow explicitly stops short of exact post-redaction transport bytes and final host answer. Thus its positive delivery claim is access to the owner-filtered handler result, not proof that the entire retained payload reaches the external model unchanged. I did not exhaustively trace transport redaction; the analysis already withholds the conclusion that would require it.

### F5 — The added lens is reconciled rather than isolated

P/reconciliation.md's delegated-workflow section connects the two new routes to runtime execution and distinguishes polling from surrounding MCP dispatch. It expressly says workflow's positive retry and completion findings resolve selected runtime uncertainties, not all fleet coverage. Runtime's locally uninspected retry field is not a contradictory system-wide negative.

P/memory.md:453–455 treats resumed assistant/tool state as recovery/context memory, not learned strategies. P/report-verification.md independently addresses the connected workflow and completion question. P/synthesis.md carries the same branch, grant, receipt, replay and completion distinctions into its public account; P/synthesis-verification.md checks those connections. No material cross-member disagreement was found in these inspected surfaces.

The set retains one profile-verification limit: event/history pruning is not separately classified as a curation transformation. Synthesis explicitly carries that limit and its prevented cleanup comparison. It is not concealed by `Blockers: none`, and it does not invalidate the workflow or existing partial profile values. This audit does not independently certify every profile finding.

## Set form and publication bytes

Fresh inspection used the frozen worktree command environment:

```text
.venv/bin/commonplace-analysis inspect kb/agentic-system-analyses/state/AAS-2026-10-11-gbrain-9de8e3c225d3-01
.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/gbrain
```

Inspection reports `state: completed`, `completion: publication-job-completed`, `publishable: true`, no failed/open attempts, no exhausted jobs, no refusals and no canonical-peer drift. Historical stale acceptances are listed; they are not current peer drift or proof of a publication defect. The inspect command itself says completion and journal status are not fresh filesystem verification. Its lock file already existed before inspection; no logical state edit was performed.

The deterministic validator returned:

```text
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/gbrain
Scope: kb/agentic-system-analyses/retained/gbrain
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

The one analysed unit is the directory artifact, not a claim that only one report exists. The set has twelve Markdown members including workflow and all three verification members, plus ARTIFACT.yaml. Its frozen layout includes workflow in required complete-disposition membership, citations and report verification.

Independent local SHA-256 and exact-file-set checks, run with the frozen `.venv/bin/python3 -B`, found:

- All thirteen published filenames and hashes exactly match R/effects/publish.json's `new` map.
- All twelve Markdown member hashes match P/ARTIFACT.yaml and the named R/state/versions bytes.
- All twelve published Markdown members are byte-identical to R/artifact's corresponding working members.
- The published manifest has member pins and worker provenance. R/artifact/ARTIFACT.yaml is only the working type declaration. Consequently an initial comparison of **all thirteen** working/public files returned false solely for ARTIFACT.yaml; this is the expected assembly distinction, not a member mismatch. The published manifest itself matches the receipt hash above.
- No extra published file or missing member was found. Receipt state is completed and expected incumbent is absent.

These establish the local publication bytes at audit time. They do not perform integration, prove source correctness or certify future files against later changes.

## Bounded trace evidence and cost

I inventoried the seventeen analytical worker results in T and used their timestamps for timing. Failure/authority-oriented inspection was narrower: workflow C30/R2, accepted report verification C52/R0, accepted profile verification C68/R0 and synthesis verification C76/R0. That sample has **302 messages and 170 tool results: 139 reads, 20 shell calls and 11 writes**. It is not a complete semantic reread of every embedded source output or an all-worker trace audit.

### T1 — Workflow inspection and validation recovered visible errors

At C30/R2/m25–26, a source search used nonexistent `subagent-write-accounting.ts`; exit 2 propagated. The worker subsequently located `subagent-persistence.ts` and read the accounting code. At m65–66 its direct validator used an invented artifact path and returned exit 2. At m67–68 it retried with the real R/artifact path and passed. The accepted report-verification worker similarly reconstructed an incorrect artifact path at C52/R0/m96–97, then passed at m98–99. These are two validator-path failures plus one failed source search, not three accepted content defects.

Direct validator calls exposed both failures. Absolute delivery did not prevent argument reconstruction. This locally resembles the prior amendment batch's recorded path errors; it does not establish a new workflow-method defect or authorize another instruction. In the selected sample there is no demonstrated masked failed shell command or out-of-scope write. Risky search pipelines still occur, and uninspected workers remain unknown.

### T2 — Review adoption is visible, but complete read recovery is not certified

The workflow trace reads the handed runtime and source mechanisms, writes its identity, empty answers and report, then validates. Its R/state/attempts/000011-workflow.json pins the current runtime hash and the accepted workflow output hash above. Report verification, profile verification and synthesis verification visibly use the added workflow rather than ignoring it.

C52/R0/m72 and m76 contain truncated large search results. This bounded scan did not establish complete recovery of those outputs; it does not certify all claimed source coverage. Independent source checks in F2–F4 supply separate support for the consequential workflow transitions. A truncation alone does not demonstrate an incorrect retained claim, and this pilot recommendation is not an exhaustive process-compliance certificate.

### T3 — Timing supports feasibility, not a lens-effect estimate

Preparation call C11 to publication result C78 spans **63.44 wall minutes**, from `2026-10-11T23:21:29.159Z` to `2026-10-12T00:24:55.519Z`. Summing each analytical worker's first-to-last numeric message timestamps gives **66.91 worker minutes** across seventeen workers; the diagnostic is excluded. Memory, epistemic and workflow overlap in the initial specialist group, so the sum is not wall time.

The workflow worker contributes **3.85 worker minutes**. It finishes before the concurrent memory and epistemic workers; its duration is not simply 3.85 added wall minutes. Runtime has two author attempts, memory has a correction, reconciliation and report verification rerun, and the profile has a correction and fresh verification. Such repair/review work is inside the reported totals, not an additional cost to add to them.

For scale only, the [immediately preceding Letta Code amendment audit](letta-code-9d060e7dab7e-amendment-effects-audit.md#timing-wall-time-worker-spans-and-repairs) records 89.67 preparation-to-publication wall minutes, 90.51 worker minutes and eighteen analytical workers. That run used a different system and method without the workflow lens. This pilot is not evidence that adding workflow reduces time. There is no same-source no-workflow control here; scope, overlap, exploration and repairs prevent causal attribution or a performance trend.

## Decision boundary

Retain this pilot as evidence that the workflow lens can produce a grounded request-to-delivery account and survive the existing set checks. Proceeding with the commissioned ten sequential analyses is reasonable. Preserve standard acceptance and each system's evidence limits; this report proposes no new gate, instruction or acceptance criterion.

No hold finding is established in the inspected workflow, reconciled claims or publication bytes. What remains unknown is whole-system correctness, all-worker mutation/compliance behavior, exact final transport disclosure, exercised recovery and repeatability across other systems. Those are audit and analysis boundaries, not silently waived blockers.

## Report validation

The report is frontmatter-free workshop evidence, permitted by kb/work/COLLECTION.md. Validation is run from the frozen worktree against this report's absolute origin path, without output or scratch-report options. The command returned:

```text
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/analysis-audit-evidence/reports/gbrain-9de8e3c225d3-workflow-pilot-check.md
Scope: /home/zby/llm/commonplace/kb/work/analysis-audit-evidence/reports/gbrain-9de8e3c225d3-workflow-pilot-check.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```
