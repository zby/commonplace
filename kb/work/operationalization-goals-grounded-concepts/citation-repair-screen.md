# Citation-repair screen: the checklist and explicit assumptions both reached ceiling

**Decision, 2026-11-17:** Do not scale this fixture or change the ingest, editing, or review instructions on its evidence. Both prompts yielded correct decisions with the supporting facts intact on all four cases in all three matched pairs. The pilot found no advantage for stating the action–outcome relation. It cannot establish that the prompts are equivalent on harder work.

## What ran

The operator authorized fewer than twelve Sol sessions. This screen used eight fresh `openai/gpt-6.1-sol` sessions at medium effort: one fixture author, six paragraph editors and one condition-blind scorer. The coordinator checked the fixture and key before editor dispatch and verified the scores afterward. The [larger plan](./operationalization-plan.md) did not run: this screen dropped the ordinary-instructions arm, used four cases, and tested paragraph repair from supplied evidence, not autonomous evidence acquisition, persistence after correction, or open-ended article quality.

Each editor received the same fictional records, decisions, edit permissions and 55-word limit per paragraph. For each matched pair the case order was the same. One editor got a completeness-and-consistency checklist; the other was asked what must hold for its edit to support the reader's decision. Both cues asked for a possible defeating observation. Authors could not call tools or see the key. The scorer saw anonymous outputs, source facts and the frozen key, not the prompts or allocations. It judged whether a reader could recover **both** the warranted decision and the result with its proper scope from the paragraph. It did not test whether a separate reader actually performed the task.

| Evidence condition | Required repair or retention | Checklist joint passes | Explicit relation joint passes |
|---|---|---:|---:|
| Unchanged result, failed paragraph refresh | Retain the latest 18/20 and release the identical route despite the blank preview. | 3/3 | 3/3 |
| Changed result at the same locator and the same refresh failure | Preserve Monday's 18/20 as historical, report Tuesday's 12/20, and hold the run. | 3/3 | 3/3 |
| Successful retrieval, wrong trial population | Keep the machine-printed-label result; withhold release for handwriting pending a relevant trial. | 3/3 | 3/3 |
| Missing latest report, unknown cause | Keep Monday's verified count; hold pending Tuesday's report without inventing a count or blaming a component. | 3/3 | 3/3 |

All six editors scored 4/4. All 24 paragraphs met the length cap. The scorer found no unsupported unique blame or unnecessary weakening; the coordinator agreed after reading the outputs and checking the counts. The three author sessions per arm, not twelve independent trials, are the replication units. Total author usage was 25,233 input / 941 output tokens for the checklist and 25,236 / 904 for the explicit relation. The small output difference is not a cost-effectiveness finding. All eight execution traces ended normally; editors and scorer made zero tool calls.

## What to investigate next

The packets gave authors the relevant passages, the threshold, and often an explicit warning about what the receipt did not establish. The common prompt also told them to preserve historical and current results. Both conditions could therefore succeed by reading carefully. This is a plausible ceiling explanation, not a measured cause. All explicit-relation editors included citation locators and all checklist editors omitted them; locator retention was optional, not a scored benefit. One model supplied both authors and scorer. There was no human-reader outcome, formal assessor-blinding check, or measurement of operator time.

If a further pilot is commissioned, change **the decision the agent has to make**, not just the case count. Give an ambiguous initial trace and a budget for one follow-up observation: for example, the current claim-bearing passage, the fetch receipt, or the paragraph-write log. Pair cases where different observations distinguish the live faults; include one where none can. Score the chosen observation, subsequent repair and warranted uncertainty. Do not supply a card that already explains which inference fails. Preflight the answer key before spending more author sessions.

Local run record: `kb/reports/state/requirements-workshop/pilot-01/` (ignored; includes design, packet, key, allocation, verbatim outputs and scoring). Allocation seed: `582901`. No production procedure changed.
