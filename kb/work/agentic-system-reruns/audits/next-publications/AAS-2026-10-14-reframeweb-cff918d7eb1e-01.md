# ReframeWeb exact-publication audit

## Decision

**Integrate with recorded limits.** No consequential defect was established in this bounded discrepancy-led audit. The new account's differences from the historical review are supported by the inspected current implementation, not by assuming revision equivalence. Necessary qualifications already appear in the public synthesis: implementation is not observed operation or benefit; guidance review lacks independent interaction evidence; workspace input coverage is incomplete; and different memory/publication routes have different admission gates.

This is an audit recommendation, not integration or exhaustive method-compliance certification. Parent review and a fresh byte-map check remain required. No present semantic unblock condition is imposed. Stronger operation, improvement or exhaustive comparison claims require the evidence specified below.

## Identity and authority

- Exact run: `AAS-2026-10-14-reframeweb-cff918d7eb1e-01`.
- Auditor: independent Pi worker, `openai/gpt-6.1-sol`, medium reasoning (actual `PI_MODEL` and `PI_REASONING_LEVEL` checked).
- Prepared worktree (`W`): `/home/zby/llm/commonplace/.commonplace/worktrees/reframeweb-cff918d7eb1e`.
- Recorded command prefix: `W/.venv/bin` (expanded in executed commands).
- Method: `a568c6dc489ad546374536b642c3889ce23149a8`; worktree HEAD independently matches.
- Source identity: `https://github.com/jubjub727/ReframeWeb`.
- Frozen source (`S`): `W/related-systems/jubjub727--ReframeWeb`, HEAD `318987dcde9a016f8e3db819ed9a73abf6b3ad81`; independent Git status was clean.
- Publication (`P`): `W/kb/agentic-system-analyses/retained/reframeweb`.
- Run evidence (`R`): `W/kb/agentic-system-analyses/state/AAS-2026-10-14-reframeweb-cff918d7eb1e-01`.
- Historical lead: `kb/agent-memory-systems/reviews/ReframeWeb.md`, reviewed commit `5b8726b39da4ad01f03bb67294b286b4652cb0f1`, checked 2026-07-07. That account covers the memory subsystem and consuming flow, not the new whole-runtime scope. I did not acquire or reconstruct its old checkout, assert equivalent source bytes, or import its findings as truth. There is no origin incumbent in the commissioned row.

Read the complete commission, audit procedure, earlier substantive commission, repository instructions, work collection contract, workshop framing and exact-run inventory JSON. Read the frozen analysis skill for method context. Only this report was written; no agents were launched, sources acquired, engine commands advanced, publications edited or integration/Git mutations performed. Git status used `--no-optional-locks`.

## Byte identity

Independently enumerated all regular files beneath P and calculated SHA-256. The actual complete map has **13 files**, exactly equal to the commissioned row's `published-sha256` map, with no extra or missing files. Read `R/effects/publish.json`: completed effect, exact run/source identity, expected destination absent, no old/archive publication, same destination and new-file map.

Key identity anchors:

| File | SHA-256 |
| --- | --- |
| `ARTIFACT.yaml` | `df8889d4c4a8060f280c62fbc9bd99266b89faf4ba8a7bc2481fd3750b29075a` |
| `overview.md` | `25c2b351dea96c3638deef84dea8b3fc5878e7d8d6cb26428728c1c59217dd8f` |
| `synthesis.md` | `45c7adcfaaf2eb48ffbeaae6a86b22b232656489d5ee929e49a6b84fc569fc8e` |
| `memory-profile.md` | `20c71636316e1f49af3b087f12a3094ec1376425c50705475e5a30ae98733b22` |

The assembled manifest is not the engine's type-only working declaration. The full 13-entry comparison, not only these selected anchors, underlies this finding. Worktree status showed only the untracked retained `reframeweb/` publication; source status was clean.

## Discrepancy-led substantive checks

### 1. Historically unwired guidance now has a producer, admission and consumer

The historical account describes five example pools without a production writer. The new synthesis describes optional candidate staging, review, persisted guidance and later prompt reloads. This difference changes the system's adaptation characterization, so I checked it directly.

- `S/agent-host/baml_src/ns_voice_turn/task_flow.baml`, lines 364–375: request completion builds review context, calls `ReviewMemories`, and invokes `write_candidate_memories` only for selected candidates.
- `S/agent-host/baml_src/ns_voice_turn/memory_review_flow.baml`: review passes purpose, candidates and stored memories to the model.
- `S/agent-host/baml_src/ns_memory/ns_internal/candidate_review_flow.baml`: only nonempty groups enter review; kept IDs are intersected with supplied candidates; results are assigned to the five destinations.
- `S/agent-host/src/reframe_agent_host/agent_flow/candidate_memory_writeback.py`: those destinations create title/description `ContextMemory` records. The writer does not establish preference initialization or retained observation provenance.
- `S/agent-host/src/reframe_agent_host/agent_flow/memory_contexts.py`: the five guidance collections and preferences have automatic search/load adapters, without numerical caps in these adapters.

This supports the new wired-path account. It does not establish good lessons, reliable review, observed adaptation, or improved capacity. Those qualifications are explicit in `P/synthesis.md`, “What survives and how it changes later work,” its independent assessment, and its limitations table. The overview description also distinguishes supported paths from demonstrated correctness/improvement. No audit-only caveat is needed to repair these claims.

### 2. Historical recency/suppression language must not be carried forward as truth

The old review calls read stamping an anti-repetition mechanism that suppresses a memory after surfacing. The inspected current query instead accepts `read_at = NONE OR read_at >= read_after` alongside created/updated cutoffs. Stamping a read to now does not by itself establish suppression on the next turn. Current `graph_retrieval_query_sessions.py`, lines 1–85, also requires positive hints and performs tag/substring/exact-string matching. I did not establish the complete historical implementation or why the old prose says otherwise.

The new synthesis correctly speaks of time thresholds and read marking before relevance selection, not proven anti-repetition or actual executor consumption. It separately distinguishes unfiltered guidance/preference loading from graph search, and gives Store-project search its separate 32-result cap. This is a useful correction of comparison framing rather than an omission to restore. No memory-benefit experiment was run.

### 3. Workspace projection omission is already public and bounded

The retained report verifier identified automatic live saved-panel input projection outside the task-link/relevance routes. I independently read `S/agent-host/src/reframe_agent_host/workspace/panel_manifest.py`: it selects nonclosed saved panels, resolves project entries, extracts filesystem-memory IDs, and writes a checked project manifest. This is not evidence that the route ran successfully.

The synthesis explicitly names automatic projection of eligible live saved-panel projects and its files/generated instructions, links the report-verification limit, and carries a dedicated limitation row. Therefore this known local inventory omission does not silently support an exhaustive two-selector comparison. Expanding all workspace consumers would be substantial reanalysis and was not undertaken.

## Actual worker evidence and revisions

Trace `T`: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-14/reframeweb.output` (448,817,986 bytes at inventory). I streamed JSON events read-only and examined selected completed `tool_execution_end` subagent results. Locators below are **1-based outer JSONL lines**, result index, and paired nested assistant `toolCall` / `toolResult` IDs in that same worker. I did not count proposals, stream updates or repeated snapshots as performed actions.

- **Memory analyst**, T line 1812, result index 0 (`000007-memory`): `call_nc2ZC7BAfPJWx5Zp1f1p4nVy|fc_06560a5f31f70f86016ad001d3784087d295477b150068af13` read the candidate writeback implementation, with nonerror source text returned. `call_aEjJOpMSFHaIDjaUEz3DJX1n|fc_06560a5f31f70f86016ad001acf68087d2b97b58dd0884c317` read `memory_contexts.py`, also with source text returned. `call_L9n0lyzfz4ItTDZNTbr6wYKs|fc_06560a5f31f70f86016ad00215b34887d2a5c6e26c4f65fcd0` wrote the memory report and received a successful-write result. These pairs support actual source inspection/authorship, not merely an accepted publication.
- **Report verifier**, T line 2529, result index 0 (`000022-report-verification`): `call_HJcW0Fw1vv2Npxnx9SZw9abM|fc_052193d0ce9181b0016ad0042e43e487d2ad9ee2ca167b3a67` read the live-panel manifest source with nonerror contents returned. `call_fhgCSnyp5ewQLNz18gRmfGda|fc_052193d0ce9181b0016ad00472e98887d282c06010078c7821` read host-service wiring, lines 95–152, with nonerror contents returned. The successful verification write is paired at `call_Gu7NR6dD3eUUqH2K6KlU05Sc|fc_052193d0ce9181b0016ad00486679087d29d2f0f2f10344218`. The published omission is backed by actual verifier calls, not only its self-description.
- **Semantic refusal and correction**, T line 3230 (`000026-profile-verification`): successful write pair `call_4RxN6RfPcymrUdg8g5eZog3q|fc_079620bda95bf7b2016ad006ad6dd487d2a234a8fb6b5a4bc3` retained a blocker: the profile's known/wired learning-authority finding asserted retained decision observations at guidance review without adequate support. At T line 3562 (`000028-memory-profile`), paired successful edits `call_9oqVgSD59WypLUeWHEBC4tX7|fc_0716b137e841ca73016ad007657f8087d2aa6bb94c07639592` and `call_tmwvuOALKy3FX79ESMVpHmhf|fc_0716b137e841ca73016ad007750d0887d2b892a1d8ee02352d` revised the profile. Successful answer write `call_sqKUpMQsyZFoa504po39LJl2|fc_0716b137e841ca73016ad00779e9bc87d290d1f46a42e76e30` explicitly withdrew the retained-observation claim and separated graph-backed action-history summarization. Stored judgment `R/state/judgments/000029-check-memory-profile-0.json` binds the revised candidate to final profile hash `20c716…33b22`; `000031-apply-profile-verification-0.json` binds final verification `00861c…c7cc9`. The final public synthesis preserves the observation-provenance uncertainty. Publication followed a real semantic correction, not a clean first-pass semantic history.
- **Local tool failure**, T line 1812, result index 1 (`000008-epistemic`): edit pair `call_PZIx8qhiIkwrGz2umwEfORFZ|fc_0ae7c858c1f6fee8016ad002b17f7487d2a0a33752c626027e` returned `edits[2] and edits[0] overlap ... Merge them into one edit or target disjoint regions.` The next edit pair `call_k5LU6bp05BDzaLZ2nCQCubRb|fc_0ae7c858c1f6fee8016ad002c7d0d487d2b944b437c57eb46f` returned successful replacement of four blocks. This is a recovered local edit failure, not a missing result or unresolved semantic refusal.

The selected calls do not certify every worker read, complete recovery of every truncated read, invocation-residue compliance, absence of all scope violations, or every scheduled obligation. No consequential source expansion or unauthorized mutation was established in this selected sample. I did not replay target execution or treat engine acceptance as evidence of it.

## Validation and audit read errors

Executed from W, using the recorded prefix:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/reframeweb-cff918d7eb1e/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/reframeweb
/home/zby/llm/commonplace/.commonplace/worktrees/reframeweb-cff918d7eb1e/.venv/bin/commonplace-validate --full kb/agentic-system-analyses/retained/reframeweb
```

Both exited 0. Summary: `VALIDATION SUCCESS`; `Files analysed: 1`, `Text files: 0`; `0 failures across 0 subjects; 0 warnings across 0 subjects`. Full output treats the directory as one set artifact and checks all 12 Markdown members plus directory members/roles/relations. `Overall: PASS (clean)`; WARN, FAIL and INFO all `(none)`; no excluded subtrees. No source-unavailable notice appeared. Deterministic validation is not quotation/semantic certification.

Two attempted audit reads returned `ENOENT: no such file or directory, access` for `R/state/handouts/000028-memory-profile/outputs/answers.md` and `R/state/handouts/000026-profile-verification/outputs/verification.md`. I did not repair or recreate either. Their actual write contents/results were recovered from the exact nested worker trace; final content identity was checked through retained hashes/judgment version bindings. These were audit lookup failures, not publication-validation failures.

Absolute origin report validation, executed from W with the same prefix:

```text
/home/zby/llm/commonplace/.commonplace/worktrees/reframeweb-cff918d7eb1e/.venv/bin/commonplace-validate --full /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-14-reframeweb-cff918d7eb1e-01.md
```

Exited 0. Type `text`; PASS: `[base] text file: no frontmatter, no structural requirements`; WARN, FAIL and INFO all `(none)`; `Overall: PASS (clean)`. This is a plain-text structural check, not semantic acceptance.

## Limits and follow-up conditions

This audit fully read overview/synthesis, the historical review and report verification, then selectively checked current source mechanisms, memory-report passages, stored bindings and worker traces. It is not a line-by-line audit of runtime, epistemic, workflow, profile or every dependency/native leaf. The historical review's unsupported-website-memory and other old narrow claims were not exhaustively rechecked; restoring every old detail is not an acceptance requirement.

The public limits are sufficient for the inspected claims. Before claiming exercised adaptation or benefit, obtain linked candidate/review/later-decision evidence and controlled comparisons. Before exhaustive workspace-input or memory-axis comparisons, expand the explicitly incomplete route/part inventories under separate authority. Before deployed security, durability or external-model guarantees, inspect deployment/dependency-specific evidence. Those are conditions for stronger claims, not current integration blockers. If parent review finds a consequential discrepancy outside this bounded sample, hold that claim/run for separately authorized source-grounded resolution; do not silently expand this audit or patch the accepted publication.
