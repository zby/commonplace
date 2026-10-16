# Graphiti 4896fccada9e incumbent-readiness supplement

## Decision

**Hold. No reason established to replace the integrated incumbent.** This is an older same-source alternative, not new corpus coverage. Existing C2–C5 correction requirements remain in force. Passing byte and structural checks does not resolve them; qualifications written here do not amend the publication.

## Identity and bounded method

- Run: `AAS-2026-10-11-graphiti-4896fccada9e-01`.
- Method/observed worktree HEAD: `0275b8abb307039d0bc975b5699e5b86fe6ca1d5`.
- Source: `https://github.com/getzep/graphiti`, frozen/observed HEAD `964bb11d1e7020e3cc67fab244268b0736b6c219`; source status clean.
- Auditor: `audit-graphiti-4896fccada9e`; Pi, `openai/gpt-6.1-sol`, medium, as exposed by runtime environment.
- `W` = `/home/zby/llm/commonplace/.commonplace/worktrees/graphiti-4896fccada9e`.
- `N` = `W/kb/agentic-system-analyses/retained/graphiti`; `R` = `W/kb/agentic-system-analyses/state/AAS-2026-10-11-graphiti-4896fccada9e-01`; `S` = `W/related-systems/getzep--graphiti`.
- Ready sibling preparation agrees on token, method, worktree and command prefix `W/.venv/bin`.

Read the binding handoff, complete audit procedure, workshop/collection contracts and both listed existing audits. Compared candidate overview/synthesis with current origin overview/synthesis/boundary and targeted runtime passages, then followed consequential source leads only in S. This supplements readiness/incumbent scope; it does not repeat the previous exhaustive worker-trace audit or apply newer workflow requirements retroactively.

Evidence leads: [repeat/trace audit](../../../analysis-audit-evidence/reports/graphiti-4896fccada9e-repeat-analysis-and-trace-audit.md), especially C2–C7 and T1–T4; [later amendment audit](../../../analysis-audit-evidence/reports/graphiti-72c99440b180-amendment-effects-audit.md). The latter audits a different run and is not candidate compliance evidence.

## Historical and incumbent boundaries

The [historical review](../../../../agent-memory-systems/reviews/graphiti.md) remains in `agent-memory-systems`; no moved review was substituted. It covers `34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6`, last checked 2026-06-04, not the candidate revision. Its graph/extraction/invalidation/retrieval/MCP account survives at greater resolution in N. Its pull-only shorthand is usefully refined by N's distinction between requested retrieval and notebook-owned context supply. Its explicit server-instruction coverage supplies a still-relevant omission lead, not current truth by inheritance.

Origin [retained/graphiti](../../../../agentic-system-analyses/retained/getzep--graphiti/overview.md) is `AAS-2026-10-12-graphiti-1d535ca565a4-01`, method `682d5e7e6fa87af0f60d6a8a35266c41cb0e2913`, at the **same source revision**, cutoff 2026-10-12. This comparison establishes no source evolution.

| Comparison | Readiness implication |
|---|---|
| Both publicly retain successful bulk raw-content bypass, asynchronous admission limits, first-support deletion, concrete later model-context supply and no demonstrated improvement. | Candidate's prior raw-retention repair is valuable but not a replacement advantage over this incumbent. |
| Incumbent adds a workflow member and a concrete notebook sequence, including tool-result feedback, unawaited admission and separate checkpoints. Candidate lacks that member under its older method. | Useful incumbent coverage, not a retroactive candidate schema failure. |
| Candidate `memory.md:188` says deferred later episodes remain eligible, while ties remain unresolved at 190/365. Incumbent synthesis explicitly carries strict-timestamp/capped-batch limits. | Candidate is weaker on a consequential recurrence condition. |
| Candidate publicly carries evaluator prompt/schema polarity conflict; incumbent synthesis instead emphasizes character slicing, pairing and default scoring. | A possible selective detail worth retaining, not evidence that wholesale replacement is better. No new evaluator audit attempted. |
| Incumbent runtime `RT-BAP-memory-instructions` still centers Cursor rules. | Incumbent is not certified defect-free by this comparison; that shared weakness does not justify replacing it with N. |

## Consequential findings and preserved blockers

1. **C2 bulk provenance omission remains a correction requirement.** The prior audit traces the missing bulk assignment of `EpisodicNode.entity_edges` into episode-based fact lookup and explicit cleanup selection. N's synthesis offers general lineage qualifications, not this route-specific condition. Preserve the prior source-chain finding; this supplement does not claim a fresh exhaustive assignment/consumer audit.
2. **C3 named-saga summary/checkpoint reset remains a correction requirement.** Fresh read of `S/graphiti_core/graphiti.py:516–533` confirms named hydration omits summary/watermarks; `nodes.py:907–940` confirms empty/null defaults and fallback save arguments. N's synthesis describes recurrence without the intervening named-ingestion reset condition. The prior audit supplies ordinary/bulk save and replacement-query links. Scope remains conditional static reasoning, not executed loss or backend-wide behavior.
3. **C4 tied-time backlog is a concrete static countercase, not merely unmeasured fidelity.** Fresh reads confirm one `now` shared by new bulk episodes (`graphiti.py:1664–1692`) and the capped selector's strict `created_at > since` (`635–666`). The prior audit completes cap-20/max-selected-watermark evidence at 137/782–786: 21 short nonempty siblings can leave one equal-time episode ineligible next time. N's general no-losslessness disclaimer does not repair `memory.md:188`; the incumbent public qualification is stronger. No target execution occurred.
4. **C5 server-wired instruction channel remains omitted/misgeneralized.** Fresh `S/mcp_server/src/graphiti_mcp_server.py:136–181` shows `GRAPHITI_MCP_INSTRUCTIONS` passed directly to `MCPServer`, correctly naming `search_memory_facts`. N synthesis says distribution is uninspected and “the instructions” have a mismatched tool name, without distinguishing this channel from Cursor's `search_facts`. Server wiring is established; host presentation and compliance are not. Historical coverage makes this a consequential regression lead, not evidence of exercised policy.

Optional response-cache coverage and node/edge attribute-update distinctions remain the prior audit's C6–C7 breadth limits. They were not independently re-audited and are not treated as absent features. Other historical findings remain attributed, not cleared or newly certified.

## Bytes and operational evidence

Read-only SHA-256 checks found exactly **12 files** in N, with the complete relative-path/hash map equal to `R/effects/publish.json:new`. Completed attempt `000042-publish` pins assembled manifest `6bc7138483846655623b7ba5cc697d0a314810f58891d45ef58b0bfa5b5919d8`. Its stored receipt `dc2c6d524440672b8be815fc3d493b8ebb79e816f9bb5c07c31553bf7c3f48b8` has the same members map. Working declaration hash `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322` is a distinct type-only stub, not publication drift. None of the 12 candidate file hashes matches its corresponding current origin file; origin has the different incumbent run ID.

Stored attempts `000017`, `000019`, `000021`, `000022`, `000031` confirm completed verifier/correction jobs, not error-free first-pass compliance. Performed-worker evidence remains the existing repeat audit's same-worker call/result inspection: 15 workers, four masked shell failures, recovered validator/transport failures, and owner-controlled semantic corrections. Those trace conclusions are **attributed, not freshly replayed**. Publication acceptance alone proves neither mandatory reads nor successful target operation. No consequential new operational question required reopening huge session streams.

## Validation, limits and unblock conditions

From W, using its exact prepared `W/.venv/bin/commonplace-validate` executable with `--json`:

- `kb/agentic-system-analyses/retained/graphiti`: exit 0, `status: success`, one set analyzed, zero failures/warnings.
- Each of its **11 Markdown members**, separately: exit 0, `status: success`, one file analyzed per call, zero failures/warnings.
- Owned origin report by absolute path: exit 0, `status: success`, one text file analyzed, zero failures/warnings.

These are frozen-method deterministic checks, not semantic certification. No target code/tests, source expansion, state-writing inspect, rerun, delegation, accepted-output edit, integration, cleanup or commit was performed. Only this report is written.

Unblock only through separately authorized correction/disposition of C2–C5, owner-controlled reverification/republication where content changes, and a fresh byte/readiness audit. Any proposed replacement also needs a concrete advantage over the current incumbent and preservation of its useful coverage. Stop here: repairing accepted artifacts or substantially reanalysing the system exceeds this commission. Existing blockers remain; keep the incumbent and count no new coverage.
