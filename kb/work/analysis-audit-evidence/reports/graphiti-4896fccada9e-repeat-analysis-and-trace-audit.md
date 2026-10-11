# Graphiti 4896fccada9e repeat analysis and trace audit

## Outcome

The new publication is byte-consistent and materially improves the raw-retention account, but it is not uniformly better than either prior run. Independent verification caught the bulk raw-content suppression error and forced correction. Missing bulk provenance indexes and named-saga summary/checkpoint erasure remain omitted. Equal-timestamp saga loss is weakened to uncertainty despite a static counterexample. The server-wired instruction channel and optional response cache are still missing.

The revised omission account is operative, not merely boilerplate: it identifies questions, traces alternate paths, routes corrections and preserves a bounded provider finding. Its stopping explanation is useful but does not establish that selection was sufficient or that the method caused the improvement. Publication took **65.68 minutes**, versus **40.33** and **38.64** for the two prior runs. More repair work, different inspection choices and unmeasured service latency confound that comparison.

All 15 new analytical workers were covered by a failure-oriented trace audit. Successful outer results concealed four inner failures; three other shell failures propagated normally. Two quotation-validation failures and three model transport errors recovered. Three semantic refusals produced corrected runtime, memory and epistemic reports. No remaining execution blocker or publication-byte mismatch was found. This does not certify the retained claims that this audit challenges.

## Commission, identities and evidence locators

Audit date: 2026-10-11. This is the operator-commissioned targeted comparison under [Audit an analysis](../audit-an-analysis.md), not a new characterization or exhaustive Graphiti review. The supplied commission overrides the workshop's normal index-update step: only this report is written; README and other reports remain unchanged.

```yaml
run-id: AAS-2026-10-11-graphiti-4896fccada9e-01
method-commit: 0275b8abb307039d0bc975b5699e5b86fe6ca1d5
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

The reporter identity comes from this audit runtime's `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`, not from the audited profile. The audited identity agrees across opening metadata, manifest, explicit launches, worker environment reads and all 15 stored model-attempt identity fields.

| Set | run-id | method-commit | source-revision |
|---|---|---|---|
| N, new | `AAS-2026-10-11-graphiti-4896fccada9e-01` | `0275b8abb307039d0bc975b5699e5b86fe6ca1d5` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| A, prior | `AAS-2026-10-10-graphiti-5833fd846841-01` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |
| B, prior | `AAS-2026-10-10-graphiti-85a21a06d35c-01` | `6ff7c828e94dd66abdf5af00c89db6420bc6a1ad` | `964bb11d1e7020e3cc67fab244268b0736b6c219` |

All three use pi-sol / Pi / `openai/gpt-6.1-sol` / medium. Worktrees are under `/home/zby/llm/commonplace/.commonplace/worktrees/graphiti-<token>/`, using the tokens in the run IDs. Within each worktree:

- `N/`, `A/` or `B/` denotes `kb/agentic-system-analyses/retained/graphiti/` in that set.
- `S/` denotes N's `related-systems/getzep--graphiti/`; the three source HEADs match and all three source working trees were clean at audit time.
- `R/` denotes N's `kb/agentic-system-analyses/state/AAS-2026-10-11-graphiti-4896fccada9e-01/`.
- `V/<hash>` denotes `R/state/versions/<hash>`. Attempt and judgment names below resolve under `R/state/attempts/` and `R/state/judgments/` respectively, with `.json` extensions.

Preparation `commit`, worktree HEAD, opening `inputs-commit`, overview and publication receipt agree on each method identity. The older openings/receipts have `source-revision: null` because no requested pin was supplied; their acquire records, boundary source revisions and source HEADs establish the actual revision. Do not substitute that null request field for the acquired source identity.

A Git comparison from the old method to the new one shows only three changed analysis-method files: `jobs-engine/follow-worker-rules.md`, `jobs-engine/verify-reports.md` and `types/agentic-system-verification.md`. No analysis engine, plan, schema, lockfile or root AGENTS change appeared in the inspected comparison. Tracked method/code paths were clean. The changed verifier instruction is actually pinned in attempts `000017` and `000031`, not just present in HEAD.

Original sessions, all under `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/`:

- N: `2026-10-11T11-25-10-443Z_01a12ab5-a7aa-745a-b8d3-80b050b39d2c.jsonl`.
- A: `2026-10-10T22-06-52-156Z_01a127da-c8fb-70fc-aae4-d7e968a723ad.jsonl`.
- B: `2026-10-10T22-09-14-881Z_01a127dc-f680-711e-8a12-57e725ff77d1.jsonl`.

N's original commission is at session line 5; publication-producing advance returns at line 72, inspect at 74 and final response at 75. Worker messages survive handout cleanup inside `message.details.results[R].messages[m]`. Trace anchors below use **one-based JSONL lines L**, **zero-based result R** and **zero-based message m**. A's prior report instead uses zero-based parent record numbers; add one to those P anchors when comparing.

The [A audit](./graphiti-analysis-and-trace-audit.md), [B audit](./graphiti-85a21a06d35c-analysis-and-trace-audit.md) and [coverage-policy comparison](../../analysis-lenses/coverage-policy-comparison.md) supplied hypotheses. The comparisons below return to retained wording and frozen source. Older trace incidents not re-investigated here remain attributed to those audits; all new analytical workers and the timing/publication measurements were independently inspected.

## Source-backed comparison

### C1 — Retained correction: bulk raw-content retention

N fixes a consequential error shared by both earlier accounts. `N/memory.md:37,55–57,346` and `N/synthesis.md:18` now explicitly distinguish ordinary blanking from successful bulk retention. This is not merely a warning that an early bulk write can survive later failure.

Source chain: `S/graphiti_core/graphiti.py:1027–1042` blanks ordinary episode content when `store_raw_episode_content` is false. Bulk constructs new episodes with caller content at `1679–1692`, saves them at `1695–1703`, and saves the same episode list again at `1763–1773`, without the blanking helper. `S/graphiti_core/utils/bulk_utils.py:160–163` serializes the episode fields; `S/graphiti_core/models/nodes/node_db_queries.py:102–109` stores content and the navigation list. Existing UUIDs are a distinct case: bulk reloads their retained content.

A's `memory.md:248,252` and B's `memory.md:37,270` do not preserve the successful-path bypass; B's synthesis already scopes ordinary suppression but still foregrounds only the intermediate bulk write. N's first memory candidate explicitly generalized blanking to both routes. The first verifier rejected that statement, and the corrected wording reached synthesis. This is a successful correction, not an error-free first pass or evidence that Graphiti itself changed.

### C2 — High-impact omission persists: bulk provenance index

N's correction stops one line too early conceptually: the same ordinary helper both clears content and populates `ep.entity_edges`. Newly constructed `EpisodicNode` objects default this list to empty (`S/graphiti_core/nodes.py:325–328`). Bulk does not assign it. The bulk persistence chain above stores that empty list even when resolved facts are saved.

Consumers depend on it: `get_nodes_and_edges_by_episode` loads fact UUIDs from `episode.entity_edges` (`graphiti.py:2009–2021`); `remove_episode` uses the same list before its first-support test (`2164–2176`). Thus newly bulk-created facts can exist but be absent from episode-based fact retrieval and explicit edge-cleanup selection. Node deletion can remove incident edges; this is not a claim that every bulk-created edge survives deletion. Facts between surviving shared entities supply the consequential remaining case.

`N/memory.md`'s `MEM-OBJ-graph-metadata`, `MEM-RTE-explicit-read` and `MEM-RTE-memory-withdrawal` name the fields/consumers but do not connect the missing producer assignment. `N/report-verification.md:28,36,38` accepts attribution/consumer/cleanup accounts without this condition. A and B also omit it; their audits' corresponding finding is independently supported. This is a persistent material omission, not a new regression relative to their retained outputs. General warnings against complete provenance do not explain why this particular advertised lookup can return no facts.

### C3 — High-impact omission persists: named-saga hydration followed by save

`S/graphiti_core/graphiti.py:516–533` loads an existing saga by name using identity and episode pointers, but not summary or summary watermarks. `SagaNode` supplies empty/null defaults (`nodes.py:907–916`). Ordinary ingestion subsequently saves that object (`graphiti.py:1087–1091`); bulk does likewise (`1821–1826`). The fallback save supplies these fields (`nodes.py:929–940`), and the inspected save query replaces them (`models/nodes/node_db_queries.py:368–373`).

Consequently, a summarize → named-saga ingestion → summarize sequence can erase the prior summary/checkpoints and restart incremental selection. This is conditional static reasoning for the inspected hydration/save/query chain, not a backend-wide executed loss test. Passing an already hydrated saga object, or repeated summarization without intervening named ingestion, is different. Custom operations-interface behavior was not exhaustively checked.

All three retained accounts describe recurrence without this intervening-write condition. In N the affected records are `MEM-OBJ-saga-node`, `MEM-RTE-saga-summary`, `EPI-RTE-saga-summary` and `synthesis.md:32`. The verifier read the complete summarization body, but that does not cover the alternate producer that resets its inputs. This independently confirms A-audit G1; it is not a finding already retained in A itself.

### C4 — Units corrected; whole-episode watermark countercase weakened

N correctly distinguishes 100,000 **characters** of initial episode packing from the assembled prompt's 128-KiB UTF-8 control (`memory.md:187`, `report-verification.md:34`). Source `graphiti.py:130–181` uses `len(content)` and character slicing, then separately measures bytes; `725–750` checks the constructed prompt. This preserves A's correct account and corrects B's `memory.md:135` unit error.

But N's `memory.md:188` says deferred later episodes remain eligible, while `190,365` leave equal-time backlog coverage unresolved. A's `memory.md:157,312` explicitly explains the strict-comparison countercase. N therefore regresses relative to A and retains B's weaker treatment.

A concrete static case is 21 nonempty, sufficiently short new episodes in one successful bulk call and saga. Bulk assigns one `now` to every new episode (`graphiti.py:1664–1691`). Summarization fetches at most 20 (`635–641`); the fallback query next requires `created_at > since` (`645–666`); the watermark advances to the maximum selected creation time (`782–786`). The unselected sibling has the same time and fails the next comparison. This needs neither oversized input nor an accidental clock collision. Subsequent named ingestion can reset the watermark through C3, so the claim is about this incremental sequence, not permanent inaccessibility through every possible intervention.

The supported narrower statement is that deferred episodes with creation times strictly above the saved watermark remain eligible. N retains the separate truncated-tail countercase and one-episode shrink-without-recheck condition; neither substitutes for whole-episode omission. A general no-losslessness disclaimer does not make the unqualified eligibility sentence true.

### C5 — Instruction-channel omission, not universal tool-name failure

N's `RT-BAP-memory-rules` and `synthesis.md:44` cover externally supplied Cursor rules, uninspected host delivery/compliance, and `search_facts` versus implemented `search_memory_facts`. That mismatch is real for `S/mcp_server/docs/cursor_rules.md:6` and the tool at `mcp_server/src/graphiti_mcp_server.py:616`.

There is also a separate wired channel: `GRAPHITI_MCP_INSTRUCTIONS` at `graphiti_mcp_server.py:136–175` is passed directly to `MCPServer(..., instructions=...)` at `177–181`. It names `search_memory_facts` correctly. N, like both prior retained accounts, does not characterize this channel. Its synthesis's broad reference to “the instructions” risks extending the Cursor limitation to all instruction delivery. Preserve server wiring while withholding actual host presentation and agent compliance; do not upgrade it to exercised behavioral control. The omitted text is not identical to Cursor's stronger procedural policy.

### C6 — Optional cache lost relative to A, unchanged relative to B

A's `MEM-OBJ-llm-cache` / `MEM-RTE-cache-reuse` and synthesis cover optional SQLite/JSON response retention. N and B lack that account. Source `S/graphiti_core/llm_client/client.py:75–92,253–281` gates creation and reuse behind a default-false cache option; a hit returns retained response data instead of a new inference. `llm_client/cache.py:27–61` supplies SQLite persistence and JSON loading/storing.

This is an omitted alternative memory mechanism, not a false claim that no cache exists. It reduces comparison breadth relative to A. It is not evidence that every provider route uses caching: overriding transports and the direct reranker need separate inspection. The revised stopping account never names caching as a considered-and-deferred question, so its omission cannot be credited as a demonstrated effort-saving choice.

### C7 — Attribute consumer retained, update distinctions narrowed

N's `MEM-OBJ-entity-text` and `MEM-RTE-summary-update` retain attributes as inputs to batch summary context. `memory-profile.md:173–184,225–236` distinguishes interpreted values from symbolic labels/keys. This avoids treating every attribute consumer as wholly unknown, a weakness highlighted in A's audit.

B is more precise: `memory.md:99–116` identifies prior attributes entering extraction as well as summary prompts, node overlay, edge replacement and conditional clearing. Source supports that distinction: `node_operations.py:1046–1074` supplies prior attributes to extraction and overlays results; `1191–1216` builds summary context; `edge_operations.py:1040–1072` supplies existing edge attributes then replaces or clears them under the stated schema condition. N preserves a positive consumer but omits this update-policy contrast. Its explicitly coarse per-part ledger is a defensible narrowing, not a fabricated absence. N is not a full replacement for B's detailed comparison value.

### C8 — Other consequential findings

- **Ordinary context count:** N `memory.md:292` and `synthesis.md:16` preserve B's distinction: ordinary admission requests ten, standalone helper defaults to three. A blurred them. Source: `graphiti.py:1431–1442`, `search/search_utils.py:64`.
- **Shared-support deletion:** N `memory.md:265` and `synthesis.md:34` explicitly retain that removing the first supporting episode can select a multiply supported fact for deletion. This preserves A's clear consequence and is clearer than B's predicate-only emphasis. Source: `graphiti.py:2173–2175`. C2 occurs before that predicate and remains missing.
- **Evaluator repair:** N's corrected `RT-RTE-graph-evaluation` and synthesis retain the first-character/remainder defect and prompt/schema polarity conflict, already present in the older analyses. Source: `tests/evals/eval_e2e_graph_building.py:41–68,155–178`; `prompts/eval.py:42–45,136–137`. Separate graph-result inputs can still contain text. The correction narrows history-grounded and consistently directed scoring, not the existence of comparison or baseline reload.
- **Search-budget interference:** A-audit G4 remains source-supported and omitted from N. `graphiti.py:1945–1948` mutates a shared recipe; `search/search.py:145–170` can await embedding before reading its limit. This permits concurrent budget interference; no incident was observed. It was an audit finding, not a retained A advantage.
- **Temporal-filter expressivity and parameter reuse:** A-audit G5 remains supported by `mcp_server/src/utils/type_config.py:139–202` (date comparisons, no null predicate) and `search/search_filters.py:167–226` (parameter keys use inner index only across outer OR groups). N withholds universal expiry suppression but does not retain these specific limitations. This is additional omitted detail, not contradiction of its deliberately partial filter account.
- **Nonexistent citation typo:** A-audit G8 concerns A's verifier falsely alleging a `dedupe_helpers.py` typo. N does not carry that allegation. No corresponding new citation defect was established; this is not evidence of an explicit repair in N.

The broad implementation-versus-observation boundary survives in all three: retained memory can reach later model requests, but source inspection does not demonstrate truth, losslessness, deployment success or improved performance. Notebook wiring, queue behavior and every provider/backend variant were not independently re-audited exhaustively here.

## Was the revised omission policy operative?

Yes, locally; sufficiency and causal benefit remain unproven.

The first verifier's retained output is `V/522510f81f22e99d8a45fd3fd24843ccce41f9cf7ee3f79a2aef28c0ac7276ba`. Its “Consequential omission searches and stopping decision” names alternate admission controls, delivery/evidence loss and evaluator successor installation. Its bulk search produced a memory blocker rather than merely appending an uncertainty disclaimer. Its GLiNER2/Gemini inspection identified a confidence-thresholded alternate extractor and retained a scoped inventory limit instead of either declaring uniform OpenAI operation or demanding exhaustive expansion. The final verifier repeats the questions and dispositions at `N/report-verification.md:52–74`.

These descriptions correspond to source reads in L38 and L54. They are useful for understanding why a concrete claim changed and why a bounded provider account survived. The initial memory analyst had already raised malformed evaluator history (L28/R0); reconciliation preserved that conflict (L32), and verification routed it to the owners. That repair is evidence for existing independent review, not uniquely for the new omission language.

The stopping rationale is less discriminating than the question selection. It lists broad remaining provider/backend/example inventories and withheld conclusions, but gives no concrete marginal-effort comparison and no reason to choose those questions over bulk navigation completeness, saga hydration/save, cache reuse or server instructions. C2–C5 show important remaining conditions inside already central mechanisms. It is therefore neither empty boilerplate nor proof that no further consequential question existed. The revised policy can be followed while question selection still misses a material condition.

Disposition: retain this as one repeat-run observation. Do not infer a detection rate, smallest useful question set, net savings, or a causal method benefit. No general method change is adopted here. A separately authorized correction decision should address C2–C5 before relying on this set for retention, cleanup, recurrence or instruction-delivery decisions.

## Trace audit

### T1 — Semantic correction chain succeeded

1. Initial runtime `53d3eaf1…` and memory `f4663716…` passed structural checks. Memory's first output identified runtime's malformed evaluator context; reconciliation retained the conflict.
2. Verifier `000017` issued three owner-specific blockers: runtime evaluator context, dependent epistemic evaluation wording, and memory's bulk blanking claim. `000018-apply-report-verification-1/2/3` refuse the corresponding versions. These are three judgments within one run, not independent trials.
3. Runtime retry `000019` (L42) copied its supplied predecessor and repaired the evaluator route; it also retained the prompt/schema polarity conflict. Memory `000021` and epistemic `000022` (L46/R0,R1) corrected their own outputs and supplied answers. They ran in parallel only after runtime completed.
4. Reconciliation `000028` (L50) disposed the former conflict. Verifier `000031` (L54) reread the corrected reports and source. Judgments `000032-apply-report-verification-0` through `-4` accepted verification and the four report relationships. Profile and synthesis verification then passed without further semantic retries.

There are 42 stored attempts: 15 model and 27 code jobs; historical judgments total 28 accepted and 3 refused. Final inspect (L74) has empty `failed-attempts` and `refusals`, but that is not an error-free history. The completed producer attempts mean outputs were returned; earlier candidates still required correction. Historical stale acceptances are visible separately.

### T2 — Four masked failures and three propagated failures

| Trace result | What failed | Status and recovery |
|---|---|---|
| L20/R0/m51, boundary | Citation attribution omitted the frozen revision | Validator exit 1 propagated. Parser read and attribution edit at m54–59; m61 passes. |
| L24/R0/m47, runtime | Search operand `llm_client/llm_helpers.py` does not exist | A following semicolon-separated search succeeded, so printed `exit=0` and outer success concealed the failed operand. The actual runtime was already read at m18; m53 searched for `generate_prompt_response`. No supported absence inference follows from the guessed path. |
| L24/R0/m67, runtime | Citation validation failed | Printed `exit=1`, but final `printf` left the tool successful. m70–73 inspected parser and added revisions; m75 passes. |
| L28/R0/m26, memory | Search operand `maintenance/saga_operations.py` does not exist | `rg ... | head -180` had no `pipefail`; `head` and final `printf` hid the upstream failure and printed zero. m27–29 directly read the actual saga selector/body in `graphiti.py`. |
| L28/R1/m26, epistemic | Same missing saga-operations path | Exit 2 propagated and stopped an `&&` chain. m27 reran the skipped MCP/README searches. |
| L28/R1/m28, epistemic | Guessed `namespaces/saga.py` does not exist | Exit 2 propagated; trailing evaluator directory listing was skipped. m29–30 enumerated actual saga/evaluator files; m38–39 read the real saga body. |
| L38/R0/m84, first verifier | Guessed `eval_episode_mentions.py` and `eval_node_extraction.py` do not exist | Printed `exit=2`, outer success from `printf`. Actual evaluator functions were enumerated earlier in the same command, and the real evaluator/CLI had been read. No retry of these guessed paths was found. Retained wording limits successor absence to the inspected path and leaves other evaluators unresolved; do not call this a successful broad evaluator search. |

Seven commands contain demonstrated failures; four are masked. Twenty-four worker validation invocations produced 22 passes and two failures, both repaired. These counts are command-level, not counts of warnings or broken citations.

Other status weaknesses remain even where no failure was observed: semicolon chains expose only their final command, and the epistemic file-filter pipeline at L28/R1/m29 lacks `pipefail`. Boundary's bounded pipeline at L20/R0/m33 explicitly captures `PIPESTATUS[0]` and treats SIGPIPE 141 as expected; it preserves the upstream status deliberately, though it still does not use the prescribed `set -o pipefail`. This is not equivalent to the memory pipeline's unexamined zero.

### T3 — Three model transport errors recovered inside successful workers

- L54/R0/m91: “OpenAI Responses stream ended before a terminal response event” during a partial proposed verification write. There is no corresponding successful tool result for that partial call. m92–93 writes the complete report; m95 and m97 validate it.
- L66/R0/m33: HTTP 503 connection failure. m34–35 resumes the next epistemic input range.
- L66/R0/m46: another premature stream termination. m47–48 continues the required profile-verification read; m60–61 writes synthesis; m63 and m65 pass validation.

All 15 result envelopes report exit code zero, empty stderr and final `stop`. The report-verifier retry and synthesis envelopes also retain an `errorMessage`, so even their top-level metadata is not wholly clean. Completion and publication hashes show recovery of final outputs, not absence of transport friction or proof that retry latency was zero.

### T4 — Reading, authority and coordination

No actual outer delivery truncation marker or missing substantive mandatory-input range was found in the 15 embedded transcripts. Supplied inputs were continued in their printed batches. Some final-line continuation notices correspond only to the empty segment after a trailing newline: for example the original runtime has 343 content lines but a split-on-newline count of 344. That is not missing prose. Deliberately bounded source reads and `head` searches are not evidence of complete source inspection; the latter's status defect is T2.

A suspected relative-path violation did not survive coordinator adjudication. The actual prompts at L24/R0/m3 and L42/R0/m3 supply worktree-relative artifact, output, identity and predecessor paths. The cited writes, edits and predecessor copy at L24/R0/m60–74 and L42/R0/m31–38 use those supplied paths. Thus these examples establish a mismatch between the worker rule's absolute-path wording and handout delivery, not workers replacing supplied absolute paths. No misrouting was demonstrated. Static source path discovery, scratch profile generation and predecessor copying stayed within assigned authority. The profile generator at L58/R0/m49–52 writes the assigned profile; it is not Graphiti execution.

Observed calls showed no worker delegation, prior-analysis/audit reads, session-log reads, source modification, engine-state editing, target execution, dependency installation, Git staging or commits. This is a trace-bounded negative, not proof about unlogged activity. All writes/copies were to assigned outputs, answers, identities or allowed scratch. Both specialist pairs completed before the coordinator advanced; no coordinator prose repair was observed.

The coordinator read worker profiles before start (L10–12), used the prepared directory, and loaded publication instructions at L33–34, well before publication at L71–72. This avoids B's late-prerequisite problem. Workers received minimal fresh-session handoffs with explicit model/effort. The original commission at L5 forbade prior analyses/audits; the inspected calls did not expose them.

## Timing and comparison limits

Durations below are independently calculated from embedded worker-message timestamps: first to last message for each analytical attempt. They include that worker's waiting/recovery, not just inference time. They exclude diagnostic, coordinator and audit work. Wall time runs from preparation record `prepared-at` to the return of the publication-producing advance, not session-file creation or final-response completion.

| New attempt | Trace | Messages | Worker minutes |
|---|---|---:|---:|
| 000003 boundary | L20/R0 | 63 | 4.06 |
| 000005 runtime | L24/R0 | 77 | 7.37 |
| 000007 memory | L28/R0 | 85 | 7.99 |
| 000008 epistemic | L28/R1 | 55 | 5.86 |
| 000014 reconciliation | L32/R0 | 43 | 2.90 |
| 000017 report verification | L38/R0 | 107 | 6.29 |
| 000019 runtime correction | L42/R0 | 41 | 1.97 |
| 000021 memory correction | L46/R0 | 50 | 2.48 |
| 000022 epistemic correction | L46/R1 | 51 | 2.81 |
| 000028 reconciliation | L50/R0 | 51 | 3.26 |
| 000031 report verification | L54/R0 | 99 | 6.20 |
| 000033 memory profile | L58/R0 | 58 | 6.04 |
| 000035 profile verification | L62/R0 | 58 | 3.49 |
| 000037 synthesis | L66/R0 | 67 | 4.67 |
| 000039 synthesis verification | L70/R0 | 58 | 3.25 |

Totals: 963 embedded messages and 552 tool results: 434 reads, 74 Bash, 37 writes and 7 edits. A partial unexecuted transport-interrupted write proposal is not counted as a successful tool result.

| Set | Analytical attempts | Preparation → publication UTC | Wall minutes | Summed worker minutes | Union of worker intervals | Parallel overlap removed |
|---|---:|---|---:|---:|---:|---:|
| N | 15 | Oct 11 11:36:26.813 → 12:42:07.417 | 65.68 | 68.63 | 60.29 | 8.34 |
| A | 12 | Oct 10 22:09:23.990 → 22:49:43.992 | 40.33 | 41.62 | 36.62 | 4.99 |
| B | 10 | Oct 10 22:10:12.782 → 22:48:51.001 | 38.64 | 39.96 | 35.30 | 4.66 |

N's initial and correction memory/epistemic pairs overlap. A and B each overlap their initial pair. Summing workers would double-count those intervals as elapsed time. Preparation/engine/coordinator gaps account for the difference between interval union and publication wall time. N's final response is later, at 12:43:44.594; its earlier session-file creation at 11:25:10 is not task start.

N's five additional repair-chain workers (`000019`, `000021`, `000022`, `000028`, `000031`) total **16.72 worker-minutes**, or **14.24 minutes** after their overlap is removed, before coordinator gaps. A's profile correction/reverification totals **4.42 worker-minutes**; B has no model retry. N's two report-verifier attempts total **12.48 minutes**, versus **3.85** for A and **4.21** for B. N's first verifier alone is 6.29 minutes, so the latency increase is not solely the second verification.

The source and worker profile are matched, but these are not controlled experiments. A and B also ran nearly simultaneously with each other; provider load and cross-run contention were not measured. Inspection breadth, output size, candidate mistakes, repair scopes and transport failures differ. The revised prose may influence selection, but neither slower elapsed time nor one newly caught defect identifies its causal effect. No independent token invoice or cost comparison was established here.

## Independent publication-byte checks

Read-only Python SHA-256 checks covered all three sets, without invoking the engine or taking its state lock:

- Exactly 12 retained files per set; the complete path/hash mapping matches `effects/publish.json`'s `new` mapping, with no missing, extra or changed files.
- Each publication receipt's `members` mapping matches that journal and the actual bytes.
- All 11 Markdown hashes match their retained manifest, publish-attempt pins, stored version bytes and working `artifact/` members. The manifest itself matches its publish pin and stored version.
- All stored version files hash to their filenames: **91 N**, **81 A**, **75 B**.
- Journals record completed publication into an absent destination, with no predecessor archive. This audit found no integration evidence and performed no integration.

| Set | Independently computed retained `ARTIFACT.yaml` SHA-256 |
|---|---|
| N | `6bc7138483846655623b7ba5cc697d0a314810f58891d45ef58b0bfa5b5919d8` |
| A | `0a98343d230587a4482d8758fcb24ec505596fec11d0bdec69c66dff8c9afdef` |
| B | `eca2bfafdcd3cc11be49a87dfe6fba9b486f461d50bd9e5d9563714ef2d3978c` |

N's publication receipt is `V/dc2c6d524440672b8be815fc3d493b8ebb79e816f9bb5c07c31553bf7c3f48b8`, produced by `000042-publish`; its corrected report verification is `9f72da90b57a2018d75079cec5139b93ee4f2fa2fa53409c28c64742a2f98496`. The working `artifact/ARTIFACT.yaml` is not the assembled publication manifest; that expected stub difference is not corruption.

These checks establish local byte consistency, not external authenticity, integration authorization, exhaustive coverage-witness replay or semantic truth. No analysis engine command was run during this audit. No Graphiti service, code, test, model or network request was executed.

## Disposition and report validation

Retain the raw-retention correction and successful owner-controlled repair as positive evidence. Retain the masked shell failures, transport recovery and persistent source omissions alongside them. Do not replace either prior analysis wholesale on the assumption that the newer method guarantees better coverage. For downstream use, C2–C5 require specific qualifications; C6–C7 explain lost comparison breadth rather than absent features.

This report leaves frozen analyses, sources, state, sessions, method, README and other agents' disjoint reports unchanged. It grants no correction, rerun, integration, commit, delegation or disposal authority. Report-only deterministic validation passed with exit code 0: `commonplace-validate kb/work/analysis-audit-evidence/reports/graphiti-4896fccada9e-repeat-analysis-and-trace-audit.md`. Output: **VALIDATION SUCCESS**; one text file analysed; zero failures and zero warnings. This checks this report, not the audited analyses' semantics.
