# Graphiti 72c99440b180 amendment-effects audit

## Outcome

The three amendments were delivered, but adoption differs by operation. All 75 published quotation attributions use the new path-only form. All 16 worker validator invocations run directly, and both failures propagate and recover. Absolute paths reach all 13 analytical workers, but every worker still shortens some supplied read paths. The boundary worker also reconstructs one incorrect absolute validator argument and repairs it after an exposed failure. Absolute delivery is therefore established; reliable exact-path use is not.

The accepted result is byte-consistent and passes its frozen validator. Independent verification successfully repairs the evaluator's message-context account. The bulk raw-retention qualification survives from the previous repeat, and tied-timestamp saga coverage is better qualified. However, missing bulk provenance indexes, named-saga summary/checkpoint erasure and the server-wired instruction channel remain uncharacterized. The ordinary-ingestion context count regresses, and the verifier again alleges a citation typo that does not exist. These are result-quality findings, not demonstrated effects of the three amendments.

Preparation to publication took **71.60 minutes**, versus **65.68** for the preceding repeat. Summed analytical worker time is **74.83 minutes**, not elapsed time. Fewer semantic repair workers coexist with a long, transport-interrupted profile worker. This uncontrolled batch supports neither a causal quality improvement nor a causal speed regression.

## Commission, identity and locators

Audit date: 2026-10-11. This report follows [Audit an analysis](../audit-an-analysis.md) under the operator's narrower write authority: this file only. The coordinator owns the workshop index and cross-run synthesis. The analysis, sources, method, run state, publication and sessions remain read-only. No analysis rerun, integration, commit or delegation was performed.

```yaml
run-id: AAS-2026-10-11-graphiti-72c99440b180-01
method-commit: 48453a8110bd36bc51fbcad3e9b2b394b694f603
source-revision: 964bb11d1e7020e3cc67fab244268b0736b6c219
worker-profile:
  name: pi-sol
  harness: pi
  model: openai/gpt-6.1-sol
  launch-model: gpt-6.1-sol
  reasoning-effort: medium
reporter-profile:
  harness: pi
  model: openai/gpt-6-astra
  reasoning-effort: medium
```

Reporter settings were exposed by `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`. Other sampling/provider settings are unknown. The audited profile agrees across the publication manifest, all 13 stored `worker_model`/`worker_effort` pairs, explicit launches and embedded runtime identity reads. Null generic `model`/`effort` attempt fields are not evidence that the reported worker identity is unknown.

Locator conventions:

- `W` = `/home/zby/llm/commonplace/.commonplace/worktrees/graphiti-72c99440b180`.
- `N/` = `W/kb/agentic-system-analyses/retained/graphiti/`.
- `S/` = `W/related-systems/getzep--graphiti/`.
- `R/` = `W/kb/agentic-system-analyses/state/AAS-2026-10-11-graphiti-72c99440b180-01/`.
- `V/<hash>` = `R/state/versions/<hash>`; attempt and judgment identifiers resolve under `R/state/attempts/` and `R/state/judgments/`, with `.json` extensions.
- `T` = `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-11T15-31-16-802Z_01a12b96-f8c2-745a-b8d3-80b534c425e7.jsonl`.
- Trace anchors `L/R/m` mean one-based JSONL line, zero-based `message.details.results` index and zero-based embedded `messages` index. The timing table identifies every analytical result envelope. The diagnostic result at L7 is excluded.

Preparation record `W.preparation.json`, worktree HEAD, opening metadata and publication receipt agree on the method revision. Acquired source identity, source HEAD and receipt agree on the source revision; the new source checkout is clean. All three named amendments are ancestors of this method:

| Amendment | Exact commit | Intended operation |
|---|---|---|
| Path-only quotation attribution | `d823ef6216ee0d7d3e49bc7347d1d9e75022b926` | Resolve revision from the frozen boundary; use a path-only example; retain checked ranges or longer quotations for ambiguity |
| Direct validator invocation | `4eed3876d26e41a4d0100a50e308237facbdf78e` | Prevent trailing status printing from replacing validator failure status |
| Absolute handout paths | `b38982da28b66bdbf0ccaf987cf8f9ae0edc6882` | Normalize generated filesystem paths without changing source-relative citations |

The scoped diff from the previous repeat's method to this method changes only `jobs-engine/follow-worker-rules.md`, `jobs-engine/prompt-section.md` and `src/commonplace/artifactrun/handouts.py` among analysis-method, `src`, root `AGENTS.md`, lockfile and package-metadata paths. Tests and other repository documents are outside that statement. All 13 embedded workers actually read the new quotation wording and direct-validation wording; their presence is not inferred merely from HEAD.

### Same-source comparators

| Alias | run-id | method-commit | Profile |
|---|---|---|---|
| P | `AAS-2026-10-11-graphiti-4896fccada9e-01` | `0275b8abb307039d0bc975b5699e5b86fe6ca1d5` | pi-sol / Pi / `openai/gpt-6.1-sol` / medium |
| A | `AAS-2026-10-10-graphiti-5833fd846841-01` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | Same |
| B | `AAS-2026-10-10-graphiti-85a21a06d35c-01` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | Same |

All four source HEADs were independently checked as `964bb11d1e7020e3cc67fab244268b0736b6c219`. Comparator worktrees use their run token under the same worktree parent. Their method HEADs and preparation records were independently checked. Older null requested-source fields do not override the acquired source revision.

The [previous repeat audit](./graphiti-4896fccada9e-repeat-analysis-and-trace-audit.md) supplies the detailed P/A/B comparison and earlier trace counts. The [A audit](./graphiti-analysis-and-trace-audit.md) and [B audit](./graphiti-85a21a06d35c-analysis-and-trace-audit.md) supply additional historical findings. Historical trace totals below are attributed to those audits, not presented as a fresh exhaustive reread. New worker traces, focused new-result source checks and local publication bytes were independently examined here. The frozen verification and set contracts govern this audit; the later workflow-lens completeness contract was not applied.

## Amendment opportunities, adoption and recovery

### T1 — Path-only quotations adopted; ambiguity still needs repair

Every published `> ---` attribution consists solely of one backticked source path: **75/75**, distributed as boundary 4, runtime 24, memory 24, epistemic 22 and report verification 1. Other members contain none. These are attribution occurrences, not independent claims or trials. The four initial analyst/boundary primary writes already contain **68/68** path-only attributions: L21/R0/m83, L25/R0/m63, L29/R0/m67 and L29/R1/m52. Later edits add quotations and the verifier supplies its own. Thus final normalization is not being mistaken for first-pass adoption.

There is **one quotation-validation failure**, at L29/R0/m70. The one-line `EntityEdge.get_by_uuid(driver, uuid)` passage occurs in both deletion and retrieval in `S/mcp_server/src/graphiti_mcp_server.py` (source lines 718 and 783). The validator gives both candidate contexts. At m71 the memory worker adds the retrieval-specific preceding comment, preserving path-only attribution and the finding; m74 passes. No claim is narrowed or withdrawn. This is successful ambiguity detection and repair, not a revision-attribution failure.

P had two quotation-validation failures, both missing-revision attribution repairs, in 24 validation invocations; N has zero such failures in 16 invocations. Those denominators count commands, not quotations checked independently. P's run needed different numbers of attempts and checks. The observation is compatible with the amendment's intended mechanism, but does not establish a comparative failure rate or causal benefit. Path-only identity does not guarantee a unique passage or semantic support; the remaining ambiguity illustrates that distinction.

### T2 — Direct validators preserve both observed failures

All **16/16** validator calls are separate direct commands without a trailing status printer or pipeline. Fourteen pass; two fail and then pass on correction:

| Trace | Failure | Recovery |
|---|---|---|
| L21/R0/m85–86 | Boundary validator uses the invented artifact directory `/home/zby/llm/commonplace/.commonplace/worktrees/graphiti-72c99440b180-01/artifact`; exit 2 is exposed | m87 uses the supplied `R/artifact` path; m88 passes |
| L29/R0/m69–70 | Ambiguous quotation; exit 1 is exposed | m71 lengthens the quotation; m73–74 passes |

The direct-call denominator covers every Bash tool call containing the validator executable in the 13 analytical envelopes. “Direct” concerns shell composition, not argument correctness: the first boundary command is direct but not literally the supplied command. Both nonzero validator results have `isError: true`. **Zero of two failed validators is masked.** P's runtime validator failure was masked by its trailing `printf`; P's boundary failure propagated. The new run demonstrates status preservation under actual failure, not just successful commands with safer syntax.

Across **54 Bash tool results**, five return nonzero: the two validators above, two missing-source-path searches below, and one exploratory `rg` no-match. None is an established masked failure. “Masked” here requires evidence that an inner command failed while its encompassing shell result reported success. A pipeline with unavailable upstream status is classified as risky, not counted as a demonstrated hidden failure.

### T3 — Absolute delivery succeeds; exact-path use does not

All **13/13** rendered prompts supply absolute filesystem paths. There are **282** absolute-valued assignment lines across them, plus 13 absolute instruction paths after `Follow`. These counts include repeated slots across attempts; they are not unique files. Prompt bodies are at m3 in each analytical envelope. No relative filesystem slot was found; non-filesystem values such as role, identity and source-relative citation paths are excluded.

Yet **13/13 workers** use relative reads for at least one supplied path. A tighter operation denominator is **236 relative reads out of 238 read calls whose resolved target exactly matches a filesystem assignment or the `Follow` instruction in that worker's prompt**. Repeated ranged reads count separately. Initial reads of the prompt itself and source exploration paths are excluded from this denominator. Relative targets are resolved against the launch cwd, W. Only two matched reads, in the second report verifier, remain absolute. Examples: L21/R0/m4 and m6; L25/R0/m4–14; L51/R0/m4–44; L67/R0/m4–46.

This is now a demonstrated rule deviation: the absolute strings were delivered. It is not the previous audit's adjudicated mistake of faulting workers for using paths that the old handout itself supplied relatively. The relative reads resolved inside the correct worktree; no read misrouting was established. The malformed boundary validator argument is a separate, actual reconstruction error despite absolute delivery, exposed and repaired as T2 describes.

Mutation behavior is stronger: **33 successful write results, four edit results and one predecessor copy** all target assigned absolute output/identity paths. The copy is L43/R0/m32; the subsequent patch is m34. One additional proposed profile write is transport-interrupted and has no tool result; it is excluded from successful-write counts. No output misrouting or unauthorized source/state mutation was demonstrated. Delivering absolute paths fixes the handout/rule mismatch but does not itself enforce literal path reuse.

### T4 — Non-validation shell risk persists without a proven masked failure

- **Missing guessed saga module, twice:** L29/R0/m37–38 and L29/R1/m30–31 search nonexistent `graphiti_core/utils/maintenance/saga_operations.py`. Both exit 2 and propagate. Memory searches actual symbols at m39–40 and reads the selector in `graphiti.py` at m41. Epistemic enumerates saga/dedup/text paths at m32–33 and later reads the actual saga/summary bodies at m56. These are discovery mistakes with recovery, not evidence that saga machinery is absent.
- **Exploratory no-match:** L21/R0/m37–38 searches a captured Bash log for a filename prefix that is absent; exit 1 is exposed. m39–40 finds the notebook section by its printed line/content shape. This is one nonzero command, not a broken source read or validator incident.
- **Risky wrappers:** memory's `rg | head -180` at L29/R0/m25, its `tail` pipelines at m27 and m56, and epistemic's pipeline plus semicolon chain at L29/R1/m32 lack `pipefail`. Several identity/source-check commands also use semicolons. No visible missing operand or other decisive inner failure accompanies their successful results. Upstream SIGPIPE/status cannot be reconstructed from the printed zero, so these are neither proven successes of every constituent command nor counted masked failures. The validator-specific amendment was adopted without curing general shell-status discipline.
- **Actual delivery truncation:** boundary's broad source search at L21/R0/m29–30 produces a 50-KB truncation marker and a saved log. The worker reruns narrower searches at m31 and m33, reads the log at m35 and m41/m43/m45, and retains bounded source coverage. This is recovery work, not evidence that the original delivered result was complete. This audit does not certify every line of every broad exploratory result as recovered.

### T5 — One transport error and one semantic refusal recover

The memory-profile worker at L55/R0/m49 reports `OpenAI Responses stream ended before a terminal response event` during a proposed write. No corresponding successful tool result exists. m50–51 writes the complete profile, and m52–53 validates it. The worker envelope retains `errorMessage` while ending with exit code zero and `stop`. All 13 envelopes end successfully; that does not erase the embedded failure.

There are **37 engine attempts: 13 model and 24 code**. Historical judgments comprise **25 accepted and one refused**. The refused runtime candidate had passed its structural check. First report verification (`000017`, L37) confirms the specialists' evaluator objection and routes a runtime blocker. Runtime correction (`000019`, L43) patches its supplied predecessor and answers the blocker. Reconciliation (`000023`, L47) and fresh report verification (`000026`, L51) complete the repair chain. The three extra model workers cost 11.00 summed minutes. The accepted source-mechanism findings agree, although specialist correction-history wording remains stale and is explicitly carried as a limit.

No observed tool call launches a nested worker, reads prior analyses/audits, modifies Graphiti or coordinator-owned run state, executes Graphiti/tests/providers, installs dependencies, stages or commits. This is a negative finding over logged calls, not proof about unlogged activity. The coordinator loads publication instructions at L38–39, before publication at L68–69; both specialists return before the next advance. No coordinator prose repair was observed.

## Focused audit of the accepted result

These are static source checks against S, not executed Graphiti counterexamples. The retained synthesis is broadly useful for architecture and evidence limits. It distinguishes implementation wiring from exercised behavior, graph persistence from truth, queued acknowledgement from completed admission, and file-based evaluation from successor installation. The following qualifications matter before relying on it for specific retention, cleanup, recurrence or instruction-delivery decisions.

### C1 — Bulk raw-retention correction survives; provenance defect remains omitted

`N/memory.md:38,260–272` and `N/synthesis.md`, “From submission to retained graph state,” correctly retain successful bulk bypass of individual raw-content blanking. Unlike P, the memory worker has this in its first candidate; no bulk-retention semantic retry was needed. A and B did not preserve the successful-path bypass with this clarity.

Source: ordinary `_process_episode_data` sets `ep.entity_edges` and conditionally blanks content at `S/graphiti_core/graphiti.py:1027–1042`. Bulk constructs fresh episodes with caller content at `1679–1692`, saves them at `1695–1703`, then saves those episodes again at `1763–1773`. Existing UUIDs are a different case because they reload existing episodes.

The same missing helper also means new bulk episodes retain the empty default `entity_edges` list (`S/graphiti_core/nodes.py:325–328`). A source-wide assignment search finds the operative assignment only in the ordinary helper. Bulk serializes episode fields (`utils/bulk_utils.py:160–163`); the inspected default persistence query stores the empty list (`models/nodes/node_db_queries.py:102–109`). Episode-based fact retrieval consumes that list (`graphiti.py:2009–2021`), as does explicit edge-cleanup selection (`2164–2176`). Newly bulk-created facts can therefore exist without appearing in that lookup or cleanup selection. Deleting nodes can still remove incident edges; facts between surviving shared entities are the consequential remaining case.

N's `MEM-OBJ-graph-metadata` quotes the ordinary assignment but does not connect the absent bulk assignment to the consumer. The verifier's additional `get_episode_entities` formatter inspection does not resolve this upstream condition. This independently reconfirms P-audit C2 and A-audit G3. A general partial-provenance disclaimer does not explain why an advertised episode lookup can return no facts.

### C2 — Named-saga ingestion can erase prior summary/checkpoints

N's `MEM-OBJ-saga-summary`, `MEM-OBJ-saga-watermarks`, `MEM-RTE-saga-summary` and synthesis explain recurrence but omit the intervening producer that can reset its inputs. This repeats P-audit C3 and A-audit G1.

`S/graphiti_core/graphiti.py:516–533` hydrates an existing named saga with identity and episode pointers, but no summary or watermarks. `SagaNode` defaults them to empty/null (`nodes.py:907–916`). Ordinary ingestion saves the partially hydrated object (`graphiti.py:1087–1091`); bulk does too (`1821–1826`). The fallback save passes summary/watermarks (`nodes.py:929–940`), and the inspected query replaces them (`models/nodes/node_db_queries.py:352–373`). A summarize → named-saga ingestion → summarize sequence can therefore discard the prior brief and restart incremental selection. Passing a fully hydrated saga object or repeatedly summarizing without this intervening named ingestion differs. Custom operations-interface implementations were not exhaustively audited, and no live loss incident is asserted.

### C3 — Tied-timestamp qualification improves; not an observed loss claim

N avoids P's unqualified assertion that deferred later episodes remain eligible. `N/memory.md:155,191–192` says they **can** remain eligible and names strict-timestamp limits; `report-verification.md`, Limits, explicitly says selection can omit tied-timestamp backlog. Synthesis carries that restriction. The character-versus-byte distinction also survives: 100,000 characters of initial packing, then 128-KiB assembled UTF-8 control.

A concrete static witness remains 21 nonempty, sufficiently short episodes created by one bulk call into a saga. The call assigns one `now` (`S/graphiti_core/graphiti.py:1664–1691`); the summary fetch cap is 20 (`137,635–641`); the fallback next query requires `created_at > since` (`645–666`); and the saved watermark is the selected maximum (`782–786`). An unselected equal-time sibling fails the next comparison. C2 may reset that watermark after later named ingestion, so this is not permanent inaccessibility under every intervention. N does not spell out the bulk-created tie witness as clearly as A, but its qualified emitted finding is defensible and stronger than P's uncertainty-only treatment.

### C4 — Server instruction channel still missing; cache omission is explicitly bounded

N's `RT-BAP-memory-procedures` and synthesis retain the Cursor document's `search_facts` mismatch and unknown host adoption. They do not characterize the separate `GRAPHITI_MCP_INSTRUCTIONS` string wired into `MCPServer(..., instructions=...)` at `S/mcp_server/src/graphiti_mcp_server.py:136–181`. That string correctly names `search_memory_facts`. Server wiring does not prove host presentation or agent compliance; it does refute treating the Cursor document as the only shipped instruction channel. This is P-audit C5/A-audit G6, still unresolved, not a new tool-name failure.

The optional response cache remains absent from the positive memory inventory, unlike A. N now explicitly lists caches among unaudited alternatives (`memory.md:34`), which is more honest than implying a complete inventory. Source `graphiti_core/llm_client/client.py:75–92,253–281` shows default-false enablement and cache-hit return before inference; `llm_client/cache.py:27–61` shows SQLite/JSON retention. This is a bounded lost comparison opportunity, not a false absence claim or proof of cache use through every provider override.

### C5 — Ordinary-ingestion count regresses to the helper default

`N/memory.md:249–252`, under the ordinary-ingestion annotation, says previous context defaults to three episodes and quotes `EPISODE_WINDOW_LEN = 3`. The helper default is real, but the ordinary caller overrides it: `S/graphiti_core/graphiti.py:1431–1442` passes `last_n=RELEVANT_SCHEMA_LIMIT`, and `search/search_utils.py:64` sets that value to ten. Explicit UUIDs are a separate branch.

P and B distinguish ten for ordinary ingestion from three for standalone default retrieval; A had this same conflation. N's core-ideas wording about the fallback alone is less specific, but the route annotation makes the wrong ordinary-ingestion implication. This is a local correction recommendation, not a reason to discard the supported architecture.

### C6 — Verifier's nonexistent citation typo recurs

`N/report-verification.md`, “Checks and disposal,” alleges an exact-reuse ledger locator `dedupe_helpers.py` and dismisses it as editorial. The actual ledger at `N/epistemic.md:155` already names `dedup_helpers.py`; so do its declaration at 534 and quotation at 550. The original specialist write at **L29/R1/m52** already contains the correct path in all three places. Neither later epistemic edit introduces or repairs the alleged typo. This is a false verifier observation, not publication drift or an unresolved citation failure.

A-audit G8 established the same mechanism in A, including an auditor initially accepting the false allegation. P did not carry it. This recurrence strengthens the local warning to check criticism against the artifact; it establishes neither prior-analysis exposure nor a causal defect in the three amendments. The inspected new calls show no such exposure. The error is low impact because no substantive finding is altered, but the verification narrative itself is wrong.

### C7 — Successful evaluator repair retains explicit editorial limits

The accepted runtime's `RT-RTE-graph-evaluation` correctly says the builder appends individual message strings and the comparator takes `episodes[0]` and `episodes[1:]` (`S/tests/evals/eval_e2e_graph_building.py:41–68,155–178`). The code does not deliver a full current/prior-message sequence. The prompt/schema polarity conflict and non-strict pairing also survive in the accepted findings. Candidate persistence and baseline reload remain real operations; no validated improvement result follows.

Memory and epistemic still describe their character-slicing findings as corrections to the current runtime. Reconciliation identifies the stale attributions; final verification explicitly accepts them as limits because the source-mechanism findings now agree. Synthesis carries both limits. That is a supported publication tradeoff under the historical verification contract, not an unnoticed unresolved semantic disagreement. Reconciliation's claim that no correction answers were supplied is separately dismissed by the verifier, which actually reads the runtime answer.

Other P-audit findings about shared search-recipe mutation, temporal-filter expressivity/parameter reuse and detailed node-versus-edge attribute update policy were not independently re-audited here. They must not be counted as corrected merely because this report prioritizes other checks. No exhaustive memory-profile reclassification, notebook execution, provider/backend parity audit or source-output truth test was attempted.

## Timing and cost boundaries

Worker duration is first-to-last embedded message timestamp, including waiting/recovery. It excludes coordinator, diagnostic and audit work. Wall time is preparation `prepared-at` to the publication-producing advance result at T/L69, not session creation, final response or inspect completion.

| Attempt | Trace envelope | Messages | Worker minutes |
|---|---|---:|---:|
| 000003 boundary | L21/R0 | 90 | 6.37 |
| 000005 runtime | L25/R0 | 70 | 7.23 |
| 000007 memory | L29/R0 | 76 | 8.53 |
| 000008 epistemic | L29/R1 | 67 | 9.86 |
| 000014 reconciliation | L33/R0 | 47 | 3.55 |
| 000017 report verification | L37/R0 | 110 | 6.50 |
| 000019 runtime correction | L43/R0 | 42 | 2.08 |
| 000023 reconciliation | L47/R0 | 49 | 3.22 |
| 000026 report verification | L51/R0 | 94 | 5.70 |
| 000028 memory profile | L55/R0 | 55 | 11.40 |
| 000030 profile verification | L59/R0 | 58 | 3.08 |
| 000032 synthesis | L63/R0 | 62 | 4.06 |
| 000034 synthesis verification | L67/R0 | 59 | 3.25 |

Totals use unrounded timestamps: **879 messages; 519 tool results** comprising 428 reads, 54 Bash results, 33 writes and four edits. The interrupted proposed write is not a successful result.

| Set | Analytical attempts | Preparation → publication UTC | Wall minutes | Summed worker minutes | Union of worker intervals |
|---|---:|---|---:|---:|---:|
| N | 13 | Oct 11 15:33:12.589 → 16:44:48.624 | 71.60 | 74.83 | 66.30 |
| P | 15 | Oct 11 11:36:26.813 → 12:42:07.417 | 65.68 | 68.63 | 60.29 |
| A | 12 | Oct 10 22:09:23.990 → 22:49:43.992 | 40.33 | 41.62 | 36.62 |
| B | 10 | Oct 10 22:10:12.782 → 22:48:51.001 | 38.64 | 39.96 | 35.30 |

N removes 8.53 minutes of specialist overlap when converting summed duration to interval union. Preparation, coordinator and engine gaps account for another 5.30 minutes of wall time. The final response is at 16:46:17.053, later than publication. Historical duration calculations are retained from the previous audit; preparation timestamps were rechecked here.

N's three repair-chain workers total **11.00 minutes**, versus P's five at **16.72** summed minutes. N's two report verifiers total **12.20**, close to P's **12.48**. The profile worker alone takes **11.40**, versus P's **6.04**, and contains the transport interruption. The trace does not separate inference, service waiting, retry backoff and tool time sufficiently to attribute that entire excess to the error. Initial boundary and specialist work also differ. These observations identify cost locations, not amendment effects. No independent billing/token invoice, controlled seed, isolated provider-load measurement or controlled rerun exists.

## Publication bytes and deterministic checks

Read-only SHA-256 inspection establishes:

- The exact 12-file path/hash mapping under N equals `R/effects/publish.json`'s `new` mapping, with no extra, missing or changed files.
- The publication receipt's `members` equals that mapping. Receipt: `V/fafb65e93c1c492172fbba23a402d071e2cb348d6dcbbd95c95764a99875489e`, produced by `000037-publish`.
- All 11 Markdown members match manifest pins and working `R/artifact` bytes; all 12 published files have matching stored version bytes and publish-attempt pins.
- All **83** stored version files hash to their filenames.
- Published `ARTIFACT.yaml` SHA-256 is `b80635dde20520eff3d5f8f3951fae702f3218068db3e48ba4fab14008266195`.
- The journal records completed publication into an absent destination, with no predecessor archive. It does not establish integration into origin.
- P, A and B's recorded publication mappings also still match their local file bytes. Their broader version-store checks are those retained in the previous audit, not newly claimed here.

From W, the frozen command `.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/graphiti --json` returned exit 0, status `success`, one set analyzed, zero failures and zero warnings. This uses the historical method, not origin's newer contracts. No engine advance or acceptance replay was run. The working manifest stub is not confused with the assembled publication manifest.

These are local integrity and form checks, not external authenticity, semantic truth or complete coverage certification. The accepted verifier's false typo allegation survives precisely because occurrence/form validation does not judge that prose claim.

## Disposition and limitations

Retain the amendments' observed operation separately from analytical quality: path-only quotations are used; direct validation exposes failures; absolute handouts are delivered but often shortened and once reconstructed incorrectly. Do not claim that all shell failures are now visible, that absolute paths prevent path errors, or that fewer missing-revision repairs establish a causal improvement.

For result use, preserve the successful bulk-retention and evaluator corrections and the stronger saga tie qualification. Request a separate correction decision for C1's missing provenance condition, C2's saga reset, C4's omitted instruction channel, C5's ingestion count and C6's false criticism. This audit neither edits frozen artifacts nor authorizes another run. Cache breadth and stale editorial history are explicitly bounded rather than silently treated as absent mechanisms or unresolved source disagreements.

No additional method change is recommended from this run alone. General shell discipline and literal path reuse remain candidates for further evidence collection; adding another instruction has unmeasured cost and no demonstrated marginal benefit here. A counterexample to the intended operational gains would be new path-only identity failures, a masked direct-validator failure, or a relative generated filesystem slot. Continued worker path shortening already counts against treating absolute delivery as sufficient behavior control.

All 13 available analytical traces were covered by call/result and failure-oriented inspection, with focused expansion of consequential episodes. This is not a fresh semantic audit of every source claim or an exhaustive proof of mandatory-read range coverage. Frozen-source source checks, rather than a new ingest or target execution, are the expressly commissioned evidence route. Missing deployment evidence and opaque provider behavior remain unknown. Older audit findings not rechecked here remain attributed findings, not independent confirmations.

Report-only validation in origin passed with exit 0: `commonplace-validate kb/work/analysis-audit-evidence/reports/graphiti-72c99440b180-amendment-effects-audit.md`. Output: **VALIDATION SUCCESS**, one text file analyzed, zero failures and zero warnings. This validates this working report, not its empirical conclusions. Graph connection discovery, if desired later, belongs to a separately authorized `cp-skill-connect` task; no additional report or graph write is made under this commission.
