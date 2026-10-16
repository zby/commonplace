# LLM-WIKI-MCP — independent single-publication follow-up audit

## Decision

**Integrate with recorded limits.** No consequential publication defect was established in this bounded audit. The necessary qualifications are already in the public synthesis, not supplied only by this report. In particular, compressed history is not automatically delivered by final agentic ask; prompt budgets and replay provenance are path-specific; metrics can retain separate answer copies; and instruction-surface coverage remains incomplete. This recommendation concerns the exact publication below. It does not authorize integration, replacement of an incumbent, or recovery.

The earlier `AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01.md` remains unchanged as incomplete group-audit evidence. This separate report completes the substantive review for this case; it does not retroactively turn that group session into a completed semantic audit.

## Identity and authority

- Run: `AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01`.
- Actual auditor: Pi, provider `openai`, model `gpt-6.1-sol`, reasoning `medium`; session `01a146f2-3d1f-71b1-9648-907f7256ec39`. Independent of the producing analysis and earlier group session. No delegation.
- Intake: `kb/work/agentic-system-reruns/publication-audit-current-intake.json`, freshly hashed SHA-256 `29c5a94a2c926f9c8b895cf5a5f50b0157461fa2a8aff39779131d14ab6d530e`.
- W: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-llm-wiki-mcp`.
- P: `W/kb/agentic-system-analyses/retained/llm-wiki-mcp`.
- R: `W/kb/agentic-system-analyses/state/AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01`.
- S: `W/related-systems/Electro-resonance--LLM-WIKI-MCP`.
- Source identity: `https://github.com/Electro-resonance/LLM-WIKI-MCP`; source HEAD freshly checked as `25efb7631082fa3732723fee08e24d39b43311fa`.
- Method/prepared worktree HEAD: `989a702d695f78f4c329a29144878377a6e04f7b`.
- Fully read commission, audit procedure, workshop README, work collection and text contracts. This report is frontmatter-free workshop text. The single-case commission controls write scope.

## Fresh exact-byte binding

Recursive enumeration and SHA-256 hashing found exactly the intake's 13 publication files, with no extra or missing files. The complete current map equals both intake `published-sha256` and completed own `R/effects/publish.json:new`. Its compact sorted path/hash JSON digest is `1bb9c7aea4f9ccb1829a90f2feb8ad8dba710356a439c27587f4af0f3e66202d` (UTF-8, sorted keys, separators `(',', ':')`, no trailing newline).

Freshly parsed `P/ARTIFACT.yaml` equals intake's assembled-manifest record. Every one of its 12 member hashes matches current bytes; the manifest itself hashes to `e6fbcf39cf40a3a57ce404c6754ef7659245be9a7fce5e5ddef28d3a1b2d4766`. Completed attempt `000045-publish` pins that manifest. The current receipt version `d480ae101fc7ab4a47297b311ccac46a3d49506b6be2399f46d2aa219657460d` was hashed, parsed and compared to intake; its member map equals the recursive map and its destination/run/source/method agree. This is an own publication, not an inherited retained directory.

Fresh hashes also equal intake for:

| Input | SHA-256 |
| --- | --- |
| `R/run.json` | `5c10206ff1ecaea2c9bea05f9f6f4e5dffb47a89782bb0490dec5bdc2ba3a399` |
| `W.preparation.json` | `5c5a4d1cc482a63eabf0400ccb9a72132a08ef777174b066772258dd4b8c4a90` |
| `R/effects/publish.json` | `c92671991ef654bc62f3d0c78bef7a2919ac2d27af0eeba8ecfb2f8d98f1bbcc` |
| `R/state/attempts/000045-publish.json` | `b8a2ab532ee3ba3f628f5652dbbefba313e4defd0a489d64cdd88f1f979e31e9` |
| Opening metadata version | `a193d4e8923ad3a006386a1251923f2860fb96a3dc98e8db621cbe31450dcc75` |

Opening metadata was parsed and compared to intake: exact run, source identity and method commit agree. Its null requested source revision is not a missing acquired revision: the acquired source record and published boundary explicitly select the source HEAD above. Preparation records exclude uncommitted origin changes. Tracked status checks in W and S returned no changes; this does not certify ignored/untracked state or original acquisition behavior. Manifest producer identity reports Pi/Sol medium. Neither that report nor completed engine state certifies every worker obligation.

## Historical comparison and material challenges

Fully read the sole historical lead, `kb/agent-memory-systems/reviews/LLM-WIKI-MCP.md`, and current boundary, overview, synthesis, workflow and all three public verification reports. Read supporting memory objects and selected profile units; this was not a line-by-line re-verification of every record or all 1,019 profile lines. Historical owner and commit exactly match this frozen source. Differences below therefore require implementation explanations, not an upstream revision explanation. Historical assessment is a lead, not authority over current findings.

### 1. Compressed memory: narrower consumption claim is supported

The historical account says future ask prompts include recent/compressed history, suggesting a single integrated loop. The new synthesis separates final agentic prompt construction from the recursive-context archive reader. Directly inspected `S/src/llm_wiki_mcp/context_api.py:495–619`: compaction loads at most 500 live rows, appends shortened older answers to the archive, rewrites recent live rows, and `release_recursive_context_with_memory` reads both archive and recent history. Inspected final context-pack/ask bodies at `4210–4503`: the pack reads recent live history, and its tool-evidence whitelist does not include recursive-context output. This supports the narrower current account; archive exposure to an explicit host is not automatic final-model consumption. The current `MEM-OBJ-ask-history-compressed` and synthesis retain the positive archive reader, so this is a correction, not loss of the memory mechanism.

### 2. “AI” notes: deterministic production is not model generation

The historical review describes generated summaries/terms/link suggestions and an iterative sidecar layer. Direct source `context_api.py:1064–1110` builds a fixed template from page/old-note terms and candidate links; there is no inference request in that producer. The adjacent search implementation joins note text into scoring and can prefer it for snippets. Current `MEM-OBJ-notes` and synthesis preserve retrieval influence and old-note feedback while removing the misleading inference implication. Later overrides are a real review risk in this file; the final ask and planner definitions were checked, not assumed from early matches.

### 3. Budget/debug claims: current qualifications are necessary and public

The historical debug-pack proposal is broader than actual replay visibility. Final pack code at `4210–4295` has a separately trimmed recent-history section and a history-tool JSON branch capped at 6000 characters before source/whole-pack trimming. Final ask at `4343–4477` may obtain a second-pass answer while retaining the first prompt in recording and return. Thus the recent-history budget is not an all-history cap and the exposed first pack is not a complete replay of the answer-producing request. Current synthesis explicitly carries both limits; workflow describes delivery separately from provider status and persistence. This is improved qualification rather than a coverage regression.

### 4. Retention, local-first safety and planner ownership

Historical privacy and broad read/write safety concerns remain materially represented. The current synthesis says history controls do not govern every retained answer copy, and MCP registry membership does not establish host authorization. Independently inspected the metrics writer/loader at `context_api.py:625–694` and final ask metadata/recording at `4447–4460`: metadata can carry provider answer/raw-response copies separately from live history. This supports `MEM-OBJ-runtime-traces`, not a universal forgetting guarantee.

At `context_api.py:3275–3292`, the final planner calls `release_plan_tools_base` under a caught exception; a definition/reference search found no binding for that name. Fallback planning is therefore supported, rather than the richer early planner being the active contract. Final ask preselects search/capabilities/history and performs the orchestration itself. The public account correctly avoids model-selected tool or autonomous-worker claims.

The historical maintenance, provenance, FTS, separate callers and trace-continuity themes remain present in current records/synthesis. Historical recommendations to Commonplace are not mandatory system characterization and their omission is not a defect. The newer partial profile does not claim the old review's broad complete-value inventory. No source-supported contradiction requiring a new hold emerged from these selected challenges.

## Completed-run trace check

Used the exact batch-16 lead, `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-16/llm-wiki-mcp.output`. Its session header identifies producer coordinator `01a13edb-6752-71dd-b6ae-701f590f8d7f`. Enumerated top-level completed call/results (36 starts and 36 ends); this is navigation evidence, not a compliance finding by count. Inspected nested message tool-call/result pairs for runtime correction `000024`, memory correction `000026`, and report verifier `000034` to test whether the repaired history/retention distinctions were supported by actual source reads rather than acceptance alone.

Concrete trace locators (JSONL line numbers):

- `3331 → 3384`, outer call `call_LhCEODPR7OYfSckJIWm7kxUA|fc_0a1f1d2cf6cfe0d0016ad0a1c9e79487d287992002dec5509b`: runtime correction. Nested `call_6EUOuJz48zhamnzgtiaPXoJC|fc_046e91d4a2117651016ad0a20a625487d2a2badd3d80d40cbb` reads the final context/history channel and has a paired result. A first validate-output failure is followed by a quote correction and a successful second validation, not a silently ignored failure.
- `3709 → 3773`, outer `call_wPbokHdg7F5BT0moabFivivR|fc_0a1f1d2cf6cfe0d0016ad0a266460487d2b8f5fac03101f60a`: memory correction. Nested `call_Lg7atR6Yyz75dlIJ9RU0W71v|fc_04334b5f671e138b016ad0a2b328f487d2aafc372d4a882626` reads metrics bodies; subsequent final-ask and history-control reads, edits and validation have paired results.
- `4491 → 4602`, outer `call_2wpuM3JcHzdPYvRpGIbpXrqE|fc_0a1f1d2cf6cfe0d0016ad0a418c53c87d284eeb25941d15546`: independent report verifier. Nested `call_KDVFfSBQj5WjG7UsMlxgmR0j|fc_0bc7c42ff7ee3d95016ad0a49c170887d29a649fbeee32e4fa` and `call_0K85anxY2gU9p4E2DLb6ytjP|fc_0bc7c42ff7ee3d95016ad0a4a564f087d2a9167f59d11226f0` read final context/ask source and have paired results. Additional paired history/metrics/source reads support a substantive source check rather than mere trust in analyst answers.

Installed attempts `000024-runtime`, `000026-memory` and `000034-report-verification` pin/output the current versions and report Sol/medium. No target execution or unauthorized effect was established in this selected trace slice. This is not exhaustive operational clearance: other nested workers, complete source-read recovery, all original actions and the separate older `outputs/llm-wiki-mcp.output` lead were not audited. That older lead was not needed to explain this exact completed publication. No unavailable trace was represented as compliant.

## Public limits and disposition boundary

The synthesis's Limitations table already withholds exhaustive schema/editable-guidance consumption, complete maintenance/evaluator coverage, observed execution and causal benefit, provider/host guarantees, universal budgeting, exact replay and all-copy withdrawal. The boundary distinguishes available-but-uninspected material from absent deployment evidence. The profile units inspected explicitly remain partial. Those limits are compatible with a useful positive implementation account.

There is no new hold and therefore no justified earliest-fault/restart assignment. The earlier unfinished audit was an audit-evidence stop, not a source-report defect or producer retry. Deep reconstruction, local correction, operational disposition and incumbent transfer are not interchangeable; none is newly required by the inspected evidence. The parent retains acceptance, current canonical transfer checks and any recovery decision.

## Deterministic validation and write boundary

Prepared executable: `W/.venv/bin/commonplace-validate`; commands run with cwd W, no output/receipt option:

1. `W/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/llm-wiki-mcp`
2. `W/.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/current-publications/AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01-followup.md`

Publication result: exit 0, `VALIDATION SUCCESS`, one set analysed, zero failures, zero warnings, no notice emitted. Report result: exit 0, `VALIDATION SUCCESS`, one text file analysed, zero failures, zero warnings, no notice emitted. These deterministic checks do not certify semantics or operational compliance.

Only this follow-up report was written. No target code/tests/services, fetching, installation, delegation, producer contact, state/source edits, active-handout inspection, reset/advance/judge, integration, staging, commit or cleanup was performed.
