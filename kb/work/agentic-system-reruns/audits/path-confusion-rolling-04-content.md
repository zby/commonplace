# Rolling 04 path-confusion content check

## Disposition

**All four affected drafts are reasonable partial analyses on the decisive claims checked. None is a completed publication.** The validation-path mistakes did not expose a substantive contradiction in these selected source comparisons. AgentFly runtime remains only a historical candidate from a failed worker. AHE memory, epistemic and workflow are installed members, but their run stopped at failed report verification. AHE's operational-authority inventory is incomplete: its exported shell binding can deny selected commands, independently of its advisory risk middleware.

| Affected draft | Bounded content disposition | Completion and remaining limit |
|---|---|---|
| AgentFly `000005-runtime` | Reasonable historical partial draft. Planner/executor control, shell effects, case admission and separate retriever training are coherently qualified. | Not installed or accepted as runtime completion. No downstream memory/epistemic/workflow account or publication. Deployment, learning and isolation remain unobserved. |
| AHE `000007-memory` | Reasonable installed partial draft. It separates retained files from delivered context, named-memory doctrine from inspected loading, and placeholders from semantic summaries. | External memory loading and full-trace bridging remain unresolved. Exported task-level authority coverage is partial. |
| AHE `000008-epistemic` | Reasonable installed partial draft, with an explicit inventory limit. Its deterministic comparisons do not license causal attribution or automatic rollback. | The shell guard is missing from the ledger. Do not use this as a complete account of exported task-level admission. |
| AHE `000009-workflow` | Reasonable installed partial draft of the ordinary improvement loop. Evaluation-before-edit, normal-return persistence and delayed successor evaluation are supported. | This is deliberately not the best-of-N workflow or an exhaustive exported coding-tool account. Failure and final-generation qualifications must remain. |

These are independent bounded judgments, not adoption of engine judgments or the failed verifier. Passing deterministic content checks establish neither source truth nor analytical completeness. No recovery, target execution, integration, delegation or commit was performed. Only this report is written and validated.

## Evidence identity and exact locators

The [execution check](rolling-04-execution-check.md) and [rolling record](../rolling-04.md) supply the current parent trace. Define:

```text
B = /home/zby/llm/commonplace/.commonplace/worktrees
F = B/agentfly-987dd174e8a2
H = B/agentic-harness-engineering-49c4f24b03c3
RF = F/kb/agentic-system-analyses/state/AAS-2026-10-12-agentfly-987dd174e8a2-01
RH = H/kb/agentic-system-analyses/state/AAS-2026-10-12-agentic-harness-engineering-49c4f24b03c3-01
SF = F/related-systems/Agent-on-the-Fly--AgentFly
SH = H/related-systems/china-qijizhifeng--agentic-harness-engineering
T = /home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T17-28-24-482Z_01a13128-90a2-76ed-b2e9-63d20e80199a.jsonl
```

Source HEADs were independently read: SF is
`42fbbcac63dd58ed6856c0761357345a58e4f032`; SH is
`8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`. Both `git status --short` results were empty. All source locators below are relative to these frozen roots, not current upstream branches.

T line numbers are one-based; nested message indexes are zero-based. C is `message.details.jobs[0].result` at the specified line; W is `C.messages[index].details.results[worker index]`. Tool arguments live in the named tool-call content block, not necessarily `content[0]`.

| Draft | Parent / worker locator | Exact reviewed content |
|---|---|---|
| AgentFly runtime | T line 103, message ID `3cc72151`; W = C.messages[20].details.results[0] | W.messages[64] writes `outputs/report.md`; result 65 confirms it. Message 66 edits the checkpoint quote; result 67 confirms it. This supersedes the visibly unfinished write at message 63. Checks are 68/69 (wrong artifact) and 70/71 (supplied artifact, pass). |
| AHE memory | T line 107, message ID `e96ba865`; W = C.messages[24].details.results[0] | Installed `RH/artifact/memory.md`, identical by SHA-256 to attempt output version below. Quote repair is W.messages[81]; checks 75/76, 79/80 and 83/84. |
| AHE epistemic | Same T line/ID; W = C.messages[24].details.results[1] | Installed `RH/artifact/epistemic.md`, identical to attempt output version. Message 58 splits the static-check ledger domains; checks 54/55, 56/57 and 60/61. |
| AHE workflow | Same T line/ID; W = C.messages[24].details.results[2] | Installed `RH/artifact/workflow.md`, identical to attempt output version. Write is message 38; checks 43/44 and 45/46. |
| Failed AHE verifier finding | Same T line/ID; W = C.messages[32].details.results[0] | W.messages[128] writes `outputs/verification.md`, including the shell-guard omission and its limit. Check 130/131 passed, but `000022-report-verification` failed and is not an accepted verification. |

Immutable AHE attempt records are `RH/state/attempts/<attempt>.json`; their `outputs.report` values name `RH/state/versions/<hash>`. Installed file hashes match:

```text
000007-memory:
8ae7410559cef9a29d29d40b55e5a17e8a08a173f85f2326e3b335f2d860eedf
000008-epistemic:
bb4749e6dcf36df676d39169fcff874d9befb68c3b6583c40f8c69ec27f18fd4
000009-workflow:
7d0278aa9260d6a4a72a04b9c0c5041e20717d609bb72c5e4dbc4f338b305670
```

`RF/state/attempts/000005-runtime.json` is failed and has no recorded outputs. `RF/artifact` contains boundary only. No AgentFly version file is asserted. Applying the confirmed message-66 edit to the message-64 content in memory gives SHA-256 `595489b2efff956feb7d5bbca33d3f5a2eb02797ebe4bab6bccdb6002d40891f`. This is a trace-derived content identity, not an installed version or a recreated candidate file. Missing handouts were not reconstructed on disk or revalidated.

## AgentFly runtime: decisive source comparisons

**The central control account is supported.** SF `client/agent.py:203-257` resets query history, calls the planner without tool schemas, accepts `FINAL ANSWER:`, parses a plan, executes tasks serially, and gives raw tool outputs to task-local executor messages. Nonempty executor content ends the task before tool-call dispatch; only the resulting task summary enters shared planner history. The inner `while True` has no iteration counter. The report correctly confines the outer cycle bound and does not promise whole-query termination. The CLI's final-answer label and startup-before-cleanup qualification also match `client/agent.py:276-298`.

**Shell capability is not confused with isolation.** SF `server/code_agent.py:628-653` selects the subprocess wrapper with confirmation false. `server/interpreters/subprocess_interpreter.py:171-218` chooses an explicit executable for non-Python code, copies the environment, starts it with workspace cwd and `shell=False`, and kills the launched process after timeout. Calling Bash explicitly still grants shell semantics. The draft correctly treats cwd, disabled confirmation and process timeout as different from deployment containment or a total agent budget. This is an implementation account, not proof of safe operation.

**Admission can be partial, and training is separate.** SF `client/parametric_memory_cbr.py:535-592` reads recorded questions for restart skipping, appends result JSONL before training/case writes, reloads case files after successful admission, and continues after exceptions. `:495-496` maps judge exceptions to an incorrect judgment. SF `memory/train_memory_retriever.py:280-327` implements gradient updates, optional metric-improving best checkpoints and an unconditional last checkpoint. These support the report's distinction between retained case guidance and separately trained numerical retriever state. Result-file restart skipping can indeed outlive failed later writes; the route is not a transaction. Nothing in these comparisons establishes deployed retraining, activated new weights or improved planner performance.

The checked claims are substantial enough to call this a reasonable draft, not just valid Markdown. This check did not independently audit every declared model/tool adapter, local streaming branch, retrieval detail or alternate interpreter. In particular, it does not certify the historical candidate's coverage claims or complete required reading.

## AHE memory: meaningful retention and delivery distinctions

**Named memory is appropriately unresolved.** SH `agents/code_agent_simple/code_agent.yaml` and `experiments/evolved_harness/code_agent.yaml` explicitly select `systemprompt.md` and bind the shell tool. The complete corresponding prompts do not select LongTermMEMORY or ShortTermMEMORY. The simple caller's complete `start.py` passes date/user/work-directory context, not these file contents. The exported prompt itself carries extensive working rules. These sources support the distinction between an explicit prompt path and an unestablished named-memory injection path. They do not prove an absence in the external NexAU loader. The draft correctly leaves that possibility open rather than declaring memory inoperative.

**Configured continuation is lossy, not verified semantic memory.** SH `agents/evolve_agent/middleware/context_compaction/compact_stratigies/compact_tool_result.py`, especially `compact`, replaces old ToolResultBlock content with a fixed marker while retaining tool-use identity and error flag; other messages can remain. The YAML's `compaction_strategy` and `keep_iterations: 10` locate the configured strategy. This directly supports both memory and epistemic distinctions between preserving envelopes and preserving evidence. The optional summaries are not silently treated as the default, lossless context or proven learning.

**The debugger-overview repair selects the right mechanism.** Memory message 81 changed only the quote's citation from unrestricted `evolve.py` to `evolve.py:1648-1648`. SH `evolve.py:1600-1675` shows the containing ordinary overview writer: failure/timeout explanations become one-liners; all-pass tasks become names and a detail-file hint. The identical text at line 3665 is in the separate variant-debugger overview path. Selecting 1648 is therefore meaningful for this object's ordinary producer, not merely suppressing ambiguity by choosing an arbitrary occurrence. It does not license full-detail delivery, freshness or diagnostic truth; those remain explicitly qualified.

The independent memory check is strongest for named-memory loading, configured compaction and debugger overview delivery. It is not a complete audit of summarizer quality, trace conversion, implicit external loading or the history of the exported rules.

## AHE epistemic: comparisons do not become causal warrant

SH `evolve.py:2267-2328` computes predicted fixes and risks by membership in flipped/regressed sets, then emits labels such as EFFECTIVE. Two changes naming the same flipped task can each receive that label; no independent component intervention is required. The draft's countercase follows the source without executing it. Its conclusion that this checks declared task membership rather than component causality is reasonable.

SH `skills/agentic-harness-engineering/scripts/verify_manifest.py`, read completely, uses a different aggregate comparison: expected fixes in caller `passed`, declared risks in caller `failed`, and false-prediction rules. It needs no before-edit baseline. It writes verification metadata, not workspace rollback. The draft correctly distinguishes this standalone format from the automated driver's manifest. Its countercases about an already-passing expected fix, a declared risk that passes, and an unlisted failure follow those rules.

SH `evolve.py:4377-4390` explicitly makes attribution report-only and skips it if no prior manifest is found; `:4517-4522` proceeds from normal editor return to recording and manifest archival without a static-validation, manifest-presence or non-regression veto there. SH `:3313-3336` warns if the best variant is below baseline but still returns its index. These comparisons support the central claim: persistence and score selection do not establish factual acceptance, causal falsification or mandatory rollback. The report's wired-versus-observed and external-oracle qualifications prevent the central overclaims.

The message-58 ledger edit is not a quote repair. Splitting the agent validator from the standalone file-presence audit makes their distinct targets, consumers and force visible instead of assigning both to one source anchor. No quotation failure is recorded for this affected worker. Its remaining consequential omission is addressed below; other debugger/schema/web leaves were not independently exhaustively audited here.

## AHE workflow: ordering and generation limits

The ordinary path in SH `evolve.py:4377-4524` computes feedback, tests the target before editing, optionally obtains/reuses diagnosis, then runs the editor and persists its result. SH `run_evolve_agent` at `:3008-3074` has trace-thread cleanup in `finally`, not a local file-effect rollback if `agent.run` raises. The report's normal-return qualification is necessary and supported.

SH `run_post_evolve` at `:3999-4010` returns when disabled or without datasets; the main caller invokes it after the loop at `:4598-4600`. Combined with evaluation preceding each ordinary edit, this supports the report's most consequential generation distinction: exhaustion after a final edit can retain an unevaluated successor. A last input score cannot certify that successor. Likewise, normal recording is not certified improvement or guaranteed selection of the best-ever workspace.

No quote repair was needed after workflow's artifact-path restoration. Its ordinary-workflow scope is explicit; the shell guard does not turn improvement-plane admission into a non-regression gate. This check did not retrace every timeout, resume or debugger branch, and does not certify a successful experiment.

## Quote repairs and the validator distinction

AgentFly message 66 replaced a short best-checkpoint quote with an expanded step-validation passage. SF `memory/train_memory_retriever.py:301-309` includes the step metric print, AUC/F1 selection and conditional save; the similar epoch-end branch at `:311-320` lacks that step print. The repair uniquely identifies a real metric-selection context and supports the claim. It was proactive, before the path-error call, not a repair of a recorded quotation failure. Removing the narrow range did not remove source grounding because the additional context disambiguates the occurrence.

AHE memory's repaired range selects an actual ordinary overview producer, as checked above. It narrows occurrence support without broadening the supported claim. AHE epistemic and workflow had path errors but no recorded quote failure. Thus it would be misleading to describe all four affected workers as having repaired bad quotations.

The parent execution check records supplied-path passes for each affected worker. This audit did not repeat historical role validation or treat those passes as claim support. It checked source meaning separately. Neither quote uniqueness nor restored artifact paths certify coverage, factual inference or publication.

## Shell-tool omission: independently supported coverage limit

The failed verifier's message-128 finding is a lead, not an accepted verdict. Direct inspection independently confirms the omitted mechanism in SH `experiments/evolved_harness/tools/shell_tools/run_shell_command.py`:

- `:350-405` collects protected-file/root and Git-metadata reasons, distinguishes hard reasons from overrideable reasons, and returns `POST_SUCCESS_STATE_GUARD` with exit code 90 when blocking.
- `:408-447` activates protection after a zero-exit command with a description matching `FINAL_CHECK_RE`, using extracted targets and non-temp cwd.
- `:517-523` returns a guard block before the foreground/background execution branches. The foreground completion path calls activation at `:626-633`.
- The exported `code_agent.yaml:20-24` binds `tools.shell_tools:run_shell_command`; this is not merely an unregistered helper.

This is heuristic task-level command admission, not authenticated evaluator success, human approval, durable learned experience or improvement-plane successor acceptance. It is nevertheless stronger than advisory middleware: recognized later commands can be denied before execution. The epistemic ledger inventories risk reminders but not this guard. Memory describes those reminders as current-invocation advice; workflow confines its account to the ordinary improvement loop. Those local statements need not be false for the broader inventory to be incomplete.

Consequently, retain the failed verifier's omission as an independently supported coverage limit. Do not generalize the risk middleware's advisory force to the entire exported shell binding, and withhold a complete comparison of exported task-level admission mechanisms. This does not accept its `Blockers: none`, certify its purported all-record review, install its candidate or discharge failed report verification.

## Gaps and report check

No selected comparison found a consequential source contradiction requiring rejection of these partial drafts. That is a bounded result, not an exhaustive omission search. Source implementation remains separate from actual diagnosis quality, tool execution, oracle reliability, memory activation, summary fidelity, fixed deployed weights, successful self-change or improved capacity. The external runtime/service boundaries and absent observed experiments remain material gaps.

AgentFly has no installed runtime or later analytical members. AHE has installed analytical members but failed verification and no publication. The original stopping conditions remain unchanged; this report neither recovers nor certifies completion.

Executed `commonplace-validate kb/work/agentic-system-reruns/audits/path-confusion-rolling-04-content.md`: `VALIDATION SUCCESS`; one text file analysed, zero failures and zero warnings. Validation is restricted to this workshop report. Broader graph discovery via `cp-skill-connect` is optional later work, outside this commission.
