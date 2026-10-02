# Batch 01 rerun trace audit — 2026-09-28

## Result

The trace audit confirms zero failed analysis validations, zero failed prepares
and three successful publications in [batch 01's rerun](./batch-01-rerun-2026-09-28.md).
It also finds six recovered worker command errors, three of them hidden behind
an outer exit status of zero, and 17 worker output deliveries containing
truncation. Final success therefore does not establish clean execution.

The strongest improvement is to deliver the runtime record contract directly
to memory specialists. Their entry instruction names the memory and overview
contracts, but their routes are later judged against fuller runtime fields.
Two specialists guessed a wrong contract filename; Basic Memory's specialist
never loaded the runtime type and needed a substantive correction after its
report had passed validation. Failure propagation and read budgeting are the
other priorities. Existing instructions already address both, so merely adding
more prohibitions is unlikely to solve them.

No method or validator was changed. This is an execution audit and an
instruction-improvement proposal, not a fresh source analysis or a finding that
the published conclusions are false.

## Audit boundary and evidence

The operator requested this audit while the batch was running. Inspection
started only after batch commit `2d50ef6d`. All six worker traces were available
through their final completion, including specialist correction turns. The
batch coordinator trace is cut immediately after that commit's tool result,
at 21:49:44.907 UTC. This avoids a self-extending audit boundary.

I scanned all 476 tool-output envelopes and their associated calls, including
nested shell results, nonzero exits, stderr/traceback text inside successful
outputs, truncation markers, source-access commands, publication checks and
mechanical finalization. Suspicious events were inspected with their recovery
calls and current contracts. This is not an independent semantic reanalysis of
every source claim. Local inter-agent message bodies are encrypted in the raw
traces; completion messages visible in the parent conversation, typed reports,
and the readable tool actions supply the correction evidence. No decryption
or hidden reasoning is needed for these findings.

Raw traces remain under `/home/zby/.codex/sessions/2026/09/28/`. The identifiers
below locate them. Event locators are physical JSONL line numbers, not model
source citations. A regenerable local extraction of tool calls/results and a
manifest lives under
`kb/reports/cache/agentic-memory-refresh/batch-01-rerun-2026-09-28/trace-audit/`.
No raw trace is required to read the findings retained here.

| Label | Agent | Trace filename | Audited lines |
|---|---|---|---:|
| C | batch coordinator | `rollout-2026-09-28T22-29-37-01a0e9b5-714f-7050-b96b-1ddefff8eb56.jsonl` | 1126 |
| A | Agent-S coordinator | `rollout-2026-09-28T22-30-34-01a0e9b6-4ed9-7b10-991b-d46f63946d64.jsonl` | 546 |
| AM | Agent-S specialist | `rollout-2026-09-28T22-32-40-01a0e9b8-3b7f-7ac3-85bb-a10f5ec1e4ea.jsonl` | 248 |
| M | MemoryOS coordinator | `rollout-2026-09-28T22-56-15-01a0e9cd-d2d0-7a11-aafd-d24a8413889b.jsonl` | 487 |
| MM | MemoryOS specialist | `rollout-2026-09-28T22-58-31-01a0e9cf-e84e-7c92-b030-9f74d02bc515.jsonl` | 245 |
| B | Basic Memory coordinator | `rollout-2026-09-28T23-19-12-01a0e9e2-d545-7913-8caf-a1532df1dc03.jsonl` | 564 |
| BM | Basic Memory specialist | `rollout-2026-09-28T23-21-19-01a0e9e4-c5cd-7ae3-b855-a19795ddae34.jsonl` | 332 |

All seven `turn_context` records identify `gpt-6-astra`, medium. The full
worktree `AGENTS.md` text occurs byte-for-byte in every worker's initial user
context at line 6. Truncated explicit rereads did not mean missing doctrine.
This narrows the earlier Agent-S self-report: incomplete rereading is confirmed,
but complete doctrine was already supplied by the runtime.

## Recovered errors, including zero-status failures

| Trace event | First diagnostic | Recovery and consequence |
|---|---|---|
| AM 35 | `rg: kb/types/agentic-system-analysis-runtime.md: ... No such file or directory` | Exit 2. Continued discovery; correct runtime fields read at call 47. |
| AM 43 | `cat: kb/types/agent-runtime-analysis-report.md: No such file or directory` | Exit 1. Same recovery. Two guesses for one needed contract. |
| MM 25 | `rg: kb/types/agentic-system-analysis-runtime.md: ... No such file or directory` | Exit 2. Scoped file discovery at call 29 and correct contract at call 34. |
| MM 160 | `ValueError: substring not found` | **Outer exit 0.** Python excerpt assembly failed on CRLF/LF matching; shell continued to hashing and validation of the old report. Call 164 changed Git decoding to `text=True`, rebuilt excerpts, then validated successfully. |
| B 142 | `fatal: path 'src/basic_memory/mcp/tools/posix.py' does not exist` | **Outer exit 0.** `git show ... | sed ...` lacked `pipefail`; sed succeeded. Scoped lookup and call 155 read actual `posix_tools.py` with `pipefail`. |
| BM 99 | `fatal: path 'src/basic_memory/models/note_content.py' does not exist` | **Outer exit 0.** Python printed stderr and continued the source-read loop. Calls 110/117 located and read `models/knowledge.py`. |

The three zero-status cases explain why a grep for nonzero tool exits would
under-count recovered errors. The MemoryOS example is more consequential than
a failed navigation query: a later validator passed bytes that the failed
preceding command had not updated. The agent noticed and repaired it; the
validation itself did not prove the intended edit ran.

No failed `commonplace-quote` call was found. Agent-S's ambiguous lookup returned
candidate occurrences with exit 0; selecting the contextual occurrence is normal
operation, not a lookup failure. No failed prepare was hidden behind later
publication, and all three publish calls succeeded on their first attempt.

The batch coordinator also had five nonzero setup/diagnostic executions: the
existing branch collision, checking the absent worktree path, and three bare
`python3` help calls without the installed package. It safely fast-forwarded the
unused ancestor branch, created the worktree, and used `uv run python`.
Two other `rg` exit-1 results were no-match searches, not execution errors.
All three real downstream acceptance commands exited 0.

## Truncation and instruction loading

Count one affected tool-output delivery once, even if both inner shell and
outer orchestration layers report truncation. There were 17 worker deliveries
and two batch-coordinator deliveries before the audit:

| Agent | Truncated deliveries | Trace output lines |
|---|---:|---|
| Agent-S coordinator | 3 | 14, 152, 327 |
| Agent-S specialist | 4 | 23, 43, 58, 207 |
| MemoryOS coordinator | 2 | 14, 96 |
| MemoryOS specialist | 1 | 14 |
| Basic Memory coordinator | 4 | 14, 60, 250, 467 |
| Basic Memory specialist | 3 | 25, 43, 50 |
| Batch coordinator | 2 | 69, 443 |

All three coordinators began with an oversized combined AGENTS/skill read.
Command-level budgets of 16,000–24,000 tokens did not enlarge the outer
`functions.exec` delivery budget. All reread skill material, but MemoryOS and
Basic Memory did not fully repeat the omitted AGENTS portion. That content was
already in the initial context. Agent-S reread AGENTS in full late in the run.
Its specialist did not recover every omitted overview-contract span.

Source and report truncations were followed by narrower inspection: MemoryOS
reread the Playground file; Basic Memory split hook/integration reads and report
sections; Agent-S split the parent report read and later inspected selected S2
source passages. Broad discovery output was not always reconstructed in full.
The audit verifies those recovery actions, not complete semantic coverage of
every omitted discovery line. Publication's source-quote checks prove occurrence,
not that an author inspected every relevant surrounding mechanism.

During this audit, several initial extraction summaries were themselves capped;
the affected findings were re-extracted by trace/event with bounded output.
Those are outside the batch counts and reinforce the same budgeting lesson.

## Corrections and contract delivery

Specialist correction turns remain Agent-S 1, MemoryOS 2, Basic Memory 2.
Agent-S's later accounting-only follow-up is not a report correction.

- Agent-S separated query from response and raw traces from captions, choices
  and scores. This is an analytical distinction, not a formatting failure.
- MemoryOS removed operational retry chronology, then expanded an abbreviated
  record-ID range so exact-token mapping would not leave local identifiers.
- Basic Memory split heterogeneous objects, completed route read-back fields,
  regularized kind headings/IDs and supplied a separate schema-check route.
  A second turn removed a retry-history sentence. Initial validation had
  accepted the omissions and abbreviated representation.

The specialist [instruction](../../instructions/analyse-agent-memory.md) says
“Read that contract” for the memory type and overview conventions. The
[memory type](../../types/agent-memory-analysis-report.md#shared-records)
gives a short route field list. The fuller read-back, delegation, expiry,
activation, admission and theory requirements are in the
[runtime type](../../types/agentic-system-runtime-report.md#shared-records),
which the specialist entry path does not directly name. Basic Memory's specialist
never opened that file in its tool trace. This is a contract-delivery gap, with
additional execution failures where agents guessed filenames instead of following
links. It is not evidence that adding one link would have prevented every
analytical correction.

The report type's “Limitations and checks” asks for the deterministic validation
result, while the specialist instruction says “Record corrections ... inside the
report.” The parent skill prohibits retry logs. Semantic corrections and a final
validation result belong in the report; operational attempt history belongs in
final communication and this batch audit. Two workers needed cleanup because
that distinction was not stable in execution.

I independently reconstructed each final memory member from its local report:
exact-token mapping, merged-heading conversion, provenance hash and appended
Amendments reproduce all three members, with no substantive parent rewrite.
Agent-S maps 26 proposals, MemoryOS 19, Basic Memory 34. Eight total merged
records exercised the new annotation rule. **No proposal was rejected**, so the
rejected-proposal finalization rule was not exercised by this batch.

## Scope and independence

The confirmed unauthorized scratch write is AM call 11:
`cat AGENTS.md >/tmp/agent-s-memory-agents-read`. The worker later deleted it at
call 178. It contained doctrine, not source analysis, and no remaining public
artifact depends on it; deletion does not retroactively authorize the write.
The handoff required all writes within the assigned worktree. A read redirected
to a file also does not deliver its content to the model.

No worker agent-listing call, prior-review read, source-worktree evidence read,
method edit or worker commit was found in the callable traces. Source inspection
used the frozen commits; fetching updated Git objects was authorized. All
specialists were fresh workers. Off-band message encryption limits raw-message
inspection, so this is a positive statement about the visible access/action
record, not proof about inaccessible communication contents.

## Proposed instruction changes, in priority order

1. **Name every required record contract at specialist entry.** Link the runtime
   type's shared-record and route fields directly from the specialist instruction,
   and state that the memory type's short list supplements those fields. Provide
   the six exact kind headings and require explicit complete ID tokens. Keep one
   authoritative field definition rather than copying conflicting versions.
2. **Provide a fail-fast command pattern.** The rule already says “later validation
   or hashing cannot clear an earlier failure.” Show dependency chains using `&&`,
   `set -o pipefail`, and Python `check=True`. If a discovery loop intentionally
   continues, return a failure summary/nonzero aggregate and resolve every needed
   missing path before treating the read as complete. Never validate as evidence
   of an edit unless that edit's command succeeded.
3. **Budget the outer delivery, not just shell calls.** Read one contract at a time
   and bound the sum of parallel source reads below the wrapper limit. Use scoped
   trees and selected source spans. Raising `max_output_tokens` only on the nested
   shell call does not fix wrapper truncation. When a required contract is cut,
   recover its omitted span before drafting; do not infer delivery from exit 0.
4. **Separate report content from execution accounting explicitly.** Say that
   substantive corrections, limitations, identity checks and the final validation
   result remain in the report; failed attempts and recovery chronology go in the
   completion message for the batch coordinator. This addresses both observed
   retry-prose cleanup turns without dropping the required final check result.
5. **Keep structural and semantic acceptance separate.** A clean validator does
   not check that every route field is meaningfully answered or every object has
   one consumer/authority profile. Have the specialist compare each proposed route
   against the authoritative fields before handoff. Treat deterministic heading
   and identifier-range checks as candidates for the method owner, not repairs
   authorized by this batch.
6. **Make runtime-provided doctrine and model identity explicit in the handoff.**
   All six workers already received the full doctrine; mandatory repeated reads
   created cost and truncation without filling a knowledge gap. Where runtime
   delivery is verifiable, say so. Supply actual model/effort metadata from the
   coordinator when available; otherwise retain `unknown`. The skill's `opus`
   metadata did not describe the model that ran here.
7. **Allow bounded scratch selections inside the run and nowhere else.** Define
   `memory-report.md` as the sole analytical handoff, while expressly permitting
   temporary quote-selection files inside its run. Forbid redirecting instruction
   reads to scratch as a substitute for consuming them. MemoryOS and Basic Memory
   inputs already clarified scratch selection scope; Agent-S's did not.

These are proposals for a subsequent method change. The three published sets
remain unchanged, full-corpus comparisons remain stale, and prior landscape
synthesis remains historical. The rerun did not re-exercise rejected-proposal
handling or establish error-free source coverage.
