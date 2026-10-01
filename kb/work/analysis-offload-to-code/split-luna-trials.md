# Reconciliation/synthesis split: fresh Luna trials

## Result

The method is implemented and all 1,211 Python tests pass. Both fresh
source-first Luna runs stopped at final record verification. Neither reached
synthesis or published a retained set or review. The plan's publication
acceptance criterion remains unmet. Do not infer that omitting member types
from synthesis is harmless, or that total work fell: neither trial reached
those jobs.

## Boundary and execution

Date: 2026-10-01. Method commit: `0ad34f5d`. Each worker was fresh, with
`fork_turns=none`, model `gpt-6-luna`, standard Codex tools, and the code-written
prompt as its message. The two clean local sources stayed at their pinned
revisions:

- PageIndex: `d2693d80791a86345ef78b3234834f5fe53a70a0`.
- Instinctual Memory: `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

The orchestrator interrupted its first Instinctual Memory boundary launch
because it had delivered an incorrect output path. That worker made no tool
calls. The failure was recorded with `launch-failed`; code supplied the next
prompt. This extra handout is an orchestrator error, not a method refusal.
Two speculative prompt reads also failed harmlessly before the actual named
prompt was read. Workers received no supplementary guidance.

## Scheduling observations

| Run | Reconciliation jobs | Record verification jobs | Memory reports | Distinct jobs | Handouts | Synthesis jobs |
|---|---|---|---|---:|---:|---:|
| `AAS-2026-10-01-pageindex-01` | 0, 1, 2 | 1, 2 | 0, 1 | 10 | 11 | 0 |
| `AAS-2026-10-01-instinctual-memory-01` | 0, 1, 2 | 0, 2 | 0, 1 | 10 | 13 | 0 |
| Prior local `AAS-2026-09-30-instinctual-memory-03` | 0, 1, 2 | 1, 2 | 0, 1 | 10 | 11 | Combined with reconciliation |

PageIndex returned memory findings before its first record verification;
Instinctual Memory returned them after its first verification. Both exhausted
the existing two-round correction budget. No record blocker concerned public
synthesis text. Neither run produced an overview draft. The reconciler and
record judges loaded analyst/reconciliation types and did not load the
overview type. No trial tested synthesis correction, a missing member-type
definition at synthesis, or a late record fault there. Those paths have Python
test coverage only.

Workflow refusal retries were PageIndex's final judge (a prose source anchor
had a line range), Instinctual Memory's epistemic member (an undeclared
`EPI-RTE-5`), and its first reconciliation (undeclared `RTE-10`, `RTE-11`).
These differ from the semantic correction rounds in the table.

## Record findings

PageIndex's runtime findings cited paths without the required source IDs.
The memory report's reading-workflow quote inserted a second `call` before
`get_page_content()`. Both memory workers had obtained the correct citation
from `commonplace-quote`; the added word entered while copying it into the
report. The final judge also repeated the epistemic source assignment as a
blocker even though reconciliation formally amended `RTE-3` from `SRC-3` to
`SRC-2`. That blocker overlooks amendment precedence under the shared record
contract. The other two defects remain independently evidenced.

Instinctual Memory's boundary listed three implementation anchors,
while later analysts inspected and cited further paths in the same frozen
repository. Both record judges treated the anchor list as exhaustive. The
registered scope explicitly includes the corresponding modules, and the source
contract requires a finding's path to exist at the commit without explicitly
requiring every cited path in that list. This is a stricter interpretation than
the stated rule. Reconciliation accepted it, could not edit the frozen boundary,
and retained the conflict. Its final output also omitted the exact `Unresolved conflict:`
marker and restated an earlier transformation correction without carrying its
formal `Amendment:` paragraph. These defects persisted despite code accepting
the reconciliation's headings and resolved IDs.

The Source register's anchor list and the later findings duplicate anchor
information while being authored at different times. The list's exhaustiveness
is unclear to the judges. The resulting gap is
recorded in [the source-register proposal](../../reference/proposals/source-registers-without-duplicated-path-inventories.md).
No boundary or analyst output was repaired by the parent.

## Trace audit

The 24 launch traces identify `gpt-6-luna`; one interrupted launch had no tool
calls. The other 23 workers used `exec_command` and `apply_patch` for their work;
two also sent status messages to the parent.
Inspection covered 465 literal shell commands and the patch calls. No source
execution, previous retained-analysis/review reads, nested delegation, Git
staging/commits or worker publication was found. Both source worktrees remained
clean. The local Codex trace names begin `split_pageindex_` and
`split_instinctual_`; run metadata and refused attempts remain in each ignored
run directory.

Seven of eleven PageIndex workers and five of twelve active Instinctual Memory
workers truncated their first contract read. Some recovered through smaller
reads; not every worker demonstrably recovered every omitted passage. Naming
the contract in a prompt is not proof that the worker read all its bytes.

Workers recovered from wrong-path reads, malformed quote selections, a
throwaway Python syntax error, invalid status values, duplicate declarations,
pending-validation text and a short description. These internal failures are
not included in workflow handout counts. Instinctual Memory's boundary worker
also called the quotation helper three times before code had frozen the
run's source; each call failed its running/frozen-source precondition.

Structural validation reports quotation blocks as well formed; it does not
prove that a worker retained the generated excerpt unchanged. PageIndex's
independent judge checked fourteen quotes with the helper and caught the
altered one. The set checks reported no structural failures in the judged
rounds of either run. Model verification supplied the missing evidence checks
and itself produced one amendment-precedence error.

Both runs are marked `failed` with concise reasons and validate in that state.
No handoff is produced for either. The live retained-set directory has no
members; validation of the fourteen existing reviews reports no failures or
warnings. Unrelated workshop edits were saved separately for exact restoration.

## Stop reports

PageIndex:

```text
blocked
- workflow: StopRun: the semantic verification of the last round names blockers: - Runtime `CMP-1`–`CMP-3`, `OBJ-1`, and `RTE-1`–`RTE-5`: source-dependent account and record findings cite bare paths without source IDs. Resolve by returning the runtime member with each finding tied to its registered `SRC-*` identifier and path.
  record: /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-10-01-pageindex-01/workflow-state/workflow/block-1.md
  permitted: stop and report to the operator
```

Instinctual Memory:

```text
blocked
- workflow: StopRun: the semantic verification of the last round names blockers: - Boundary and reconciliation; `SRC-2`, `RTE-1`–`RTE-9`, `CLM-1`–`CLM-3`, `MEM-RTE-1`, `MEM-OBJ-1`, `EPI-OBJ-1`, `EPI-OBJ-2`: the frozen Source register omits implementation anchors relied on by the members, and the reconciliation's statement of this conflict lacks the required `Unresolved conflict:` marker with its conflicting evidence and prevented conclusion. Resolve by updating the boundary Source register through the workflow owner and recording the remaining conflict in the required reconciliation form, or otherwise removing unsupported anchors/findings.
  record: /home/zby/llm/commonplace/kb/reports/state/agentic-system-analysis/AAS-2026-10-01-instinctual-memory-01/workflow-state/workflow/block-1.md
  permitted: stop and report to the operator
```
