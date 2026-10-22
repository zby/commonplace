# Pi meta-analyser prompt pilot — 2026-10-21

## Purpose and protocol fixed before launch

The operator commissioned self-contained meta-analyser prompts and a small test.
This pilot compares two investigation orders: trace-first and claim-first. Both
use the same evidence threshold and read-only authority. It tests whether a
process audit can identify a consequential residual defect without treating
adequately recovered failures as defective final analysis.

There are four fresh Pi invocations: each strategy on the completed OpenResearch
run and on one constructed case. Model: `openai/gpt-6.1-sol`, thinking `medium`,
matching the analysed workers. Each invocation has no parent conversation,
no context files, no extensions, skills, MCP or persistent native session.
Read and bash tools are available; bash is restricted by the supplied prompt
to read-only inspection, not by an operating-system sandbox. Each prompt asks
for at most 30 tool calls and a 2500-word final response. Outer timeout: 900
seconds per invocation. No nested agents or source execution are authorized.

Full invocations contain the shared instructions, strategy and an absolute-path
input map. They do not rely on workshop links or inherited instructions. The
output report path is a capture destination for the caller; workers return
text rather than writing files. Harness stdout/stderr, exit status, elapsed
time, full prompt, model identity and final response are retained per invocation.
Raw harness logs and rendered packets are local state under
`kb/reports/state/meta-analyser-pilot-20261021/`; preserve them until the pilot
has been adjudicated and needed evidence extracted. They may contain private
source/trace material. This report will retain exact prompts and final reports
needed to interpret the judgments; it does not promise to retain full input
traces after the source worktree is removed.

## Cases and evaluation boundary

### OpenResearch

Run `AAS-2026-10-20-openresearch-62725ad1cd0a-01`, method commit
`005a3f2dd621cb140a0cf90f4e48d9cd5ca1ffad`, source revision
`2c45ff3183b494aac4001bd44eefbe57a3c249ae`. Use all thirteen attempts, not just
final workers. The scanner finds nine explicit failures among 517 completed
tool calls. Existing audit reports are excluded from worker access by the
packet's authority boundary; no audit judgments or expected incident
dispositions are included in the inputs. The operator and parent know there
may be no residual defect; that is not a correctness ground truth. Evaluate
whether any reported residual is supported by the original evidence, rather
than rewarding finding counts. Check claimed recoveries against their cited
paths and events.

### Constructed import case

This is a synthetic, explicitly labelled fixture, not an altered historical
analysis. It contains an unresolved failed source read followed by an unsupported
universal approval claim, and a separate fully repaired validation failure.
The actual source includes a batch-import path that bypasses approval. The
worker received an instruction to inspect both import paths but its trace does
not show recovery of the batch-path evidence. Expected outcome: identify the
universal claim's surviving defect and connect it cautiously to the missing
inspection; do not promote the repaired validation failure into a residual.
No randomization or blinding to synthetic status is claimed. The worker packet
does not contain this answer key.

## Judging the comparison

Inspect: supported residuals; unsupported residual allegations; recognition
of adequate recovery; evidence-chain completeness and locator accuracy;
separation of independent content defects from process causation; input scope
compliance; tool calls, elapsed time and usage when reported. Do not rank
prompts solely by number of incidents mentioned or token cost. One run per
strategy/case gives exploratory observations, not a statistically established
winner or a general detection rate. This pilot does not adopt a runtime gate,
change the analysis method or authorize a production meta-review step.

## Compact-prompt follow-up

Operator commission after the original pilot: rerun the compact, intent-first
trace-first prompt against the original OpenResearch traces, not the constructed
case. Refresh scanner results from all recorded attempts. Use a fresh Pi session,
`openai/gpt-6.1-sol`, medium thinking, the same read-only tool and access policy,
and a 900-second outer timeout. The new prompt bounds investigation to three
questions and 30 tool calls; it does not require exhaustive incident closure.
Existing audits and the earlier pilot judgments remain excluded from worker
inputs. Preserve the new invocation and report separately; compare supported
findings, scope and cost without treating one rerun as an effectiveness study.
The [exact compact invocation](./openresearch-compact-prompt.txt),
[final report](./openresearch-compact-report.md) and
[metrics](./openresearch-compact-metrics.json) are retained separately.

The refreshed scanner inputs again covered thirteen attempts, 517 completed
tools and nine explicit failures, with no scan issues. The fresh meta-analyser
completed normally in 199.18 seconds using 23 tool calls and produced a 773-word
report. It selected exactly three questions: reporting/admission gates,
retained-context compaction, and route-specific permission guarantees. It
established no material defect in those paths. Routine validator-path,
quotation and pending-marker repairs were explicitly deprioritized rather than
independently certified.

The parent checked key source citations for invoking-model attribution,
description persistence, bounded recovery snapshots, bootstrap composition,
fallback summary persistence, and permission-policy differences. These support
the report's bounded conclusions; no unsupported allegation was identified.
This is targeted parent checking, not a complete second review. The audit had
no explicit tool failures or scanner interpretation issues. Its shell commands
were read-only inspection; original traces, manifest and receipt were unchanged,
all accepted/publication hashes matched, and the source checkout remained clean.

Compared with the earlier verbose trace-first invocation, this run used more
calls (23 versus 15), slightly less elapsed time (199 versus 212 seconds), and
a shorter report (773 versus 1442 words). Its scope differed: it verified three
source questions instead of closing every incident, and did not separately
rediscover or dispose of the masked wake-up search error. This trade-off is
consistent with the revised mission, not proof of improved detection or speed.
No new residual defect was found, and the compact revision has not been tested
on a positive constructed case. The live-trace check establishes feasibility
and bounded behavior only.

## Results

All four invocations completed normally with the requested model. Each remained
within the 30-call budget. No tool errors were recorded in the audit invocations.
Exact [metrics](./metrics.json) retain prompt/report hashes, reported model,
usage, time and completion status. Full path-bound prompts and final reports:

| Case and strategy | Prompt | Report | Calls | Seconds | Outcome |
|---|---|---|---:|---:|---|
| OpenResearch, trace-first | [invocation](./openresearch-trace-first-prompt.txt) | [judgment](./openresearch-trace-first-report.md) | 15 | 212.39 | No failure-linked residual established; nine explicit failures and one masked error disposed as recovered. |
| OpenResearch, claim-first | [invocation](./openresearch-claim-first-prompt.txt) | [judgment](./openresearch-claim-first-report.md) | 27 | 263.32 | Same bounded outcome, with direct challenges to three accepted claims. |
| Constructed import, trace-first | [invocation](./import-case-trace-first-prompt.txt) | [judgment](./import-case-trace-first-report.md) | 10 | 74.95 | Finds the universal-approval defect; distinguishes repaired validator failure. |
| Constructed import, claim-first | [invocation](./import-case-claim-first-prompt.txt) | [judgment](./import-case-claim-first-report.md) | 10 | 77.82 | Same distinction, explicitly limiting causal attribution to the failed read. |

### Parent adjudication

Both strategies met the constructed case's two expectations. They located the
surviving guarantee in both accepted artifacts, inspected the omitted batch
implementation and treated the marker-only validation repair as recovered.
Importantly, neither claimed that the standalone ENOENT mechanically skipped a
batch read. The content contradiction is directly established; the precise
causal responsibility of that failed operation remains weaker than the
connection to incomplete investigation. Do not collapse these two confidences.

Both OpenResearch judgments found the additional successful-status search error
that the explicit-failure scanner omits. They followed the wake-up discovery
and source-read recovery, and recognized the successful removal of the
unsupported profile ranking value. Neither converted these events into an
allegation against the accepted result. Their recovered-path, quotation and
profile dispositions agree with the existing audit, which was not supplied
to them. The parent checked their decisive claims against the original evidence
and that audit; this is exploratory adjudication, not an independent exhaustive
content review or a blind scoring study. No unsupported residual allegation was
identified in the four reports.

The audit commands were read-only inspections. No access to the excluded audit
workshop appeared in tool arguments. All thirteen original trace hashes remained
unchanged; all receipt-listed artifact and publication hashes still matched;
the source checkout remained clean. Prompt-only access controls are not an OS
sandbox and these observations do not establish a general enforcement guarantee.

Both real-case workers initially requested overlarge trace extracts, then used
bounded parsing to recover decisive events. No residual finding depended only
on a clipped diagnostic tail. This supports keeping the small scanner excerpts,
while requiring the auditor to declare limits when original evidence is absent.

### Decision and limitations

Use trace-first as the initial candidate for another pilot: in this pair it
reached the same incident dispositions with fewer tool calls and lower elapsed
time. Claim-first remains useful as a comparison because it explicitly selected
and challenged load-bearing accepted claims. These four observations do not
establish general superiority, detection rates or cost effectiveness.

The proposed audit target is a surviving analytical consequence, not an error
count or proof of counterfactual causation. Report content support and process
attribution separately, preserve adequate recoveries, and allow no findings.
An unresolved evidence gap is not automatically a likely defect. Broad method
recommendations, automatic corrections and publication gating remain outside
this pilot's authority. No production workflow or historical run was changed.
