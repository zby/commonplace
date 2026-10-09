# Dynamic Cheatsheet Sol/Luna audit — 2026-10-06

## Finding and purpose

The newest stopped Sol run tracks several memory mechanisms more faithfully than the newest published Luna run. Its stop identifies real profile defects; publication status does not rank analytical correctness. The latest Luna run is faster than the previous Luna run, but loses several supported classifications and introduces scope inconsistencies. Neither comparison establishes a causal effect of model or method.

The operator commissioned this retrospective comparison and then requested its retention in this workshop. It informs evaluation of the analysis method, not revision of the external-system analyses. The audit read existing run outputs, pinned implementation, workflow state and harness traces. It did not execute the target system, open analysis runs, recover stopped runs or modify retained sets. Two independent workers reviewed parts of the comparison; the coordinator checked model identities and timestamps and corrected the baseline comparison through direct rereading.

This report supersedes the conversational comparison. That comparison initially mixed findings from the retained incumbent with the selected October 5 baseline. In particular, it incorrectly credited that Luna baseline with pull/push separation and incorrectly described it as overclaiming semantic curation. Both inspected Luna profiles are pull-only and both leave semantic curation undetermined. The tables below use the actual run outputs, not an inherited retained set in a stopped worktree.

## Runs and evidence boundary

All four runs pin source revision `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`. Source changes therefore do not explain their differences.

| Label | Exact run ID | Method commit | Recorded model | Harness / reasoning | Endpoint |
|---|---|---|---|---|---|
| Older Sol | `AAS-2026-10-04-dynamic-cheatsheet-01` in worktree `4d912688cb3b` | `49725e9aa` | `gpt-6.1-sol` | Codex / low | Analysis verification passed; publication blocked |
| Older Luna | `AAS-2026-10-05-dynamic-cheatsheet-39e1e27ebdc0-01` | `b95a2bb79` | `gpt-6-luna` | Pi / medium | Complete |
| Latest Luna | `AAS-2026-10-06-dynamic-cheatsheet-947b5c8445a4-01` | `8a76fe4b9` | `gpt-6-luna` | Pi / medium | Complete |
| Latest Sol | `AAS-2026-10-06-dynamic-cheatsheet-67d9770093c6-01` | `8a76fe4b9` | `gpt-6-sol` | Codex / low | Stopped at profile verification |

The older Luna run is the nearest earlier completed run, not the immediate preceding attempt. The October 5 attempt `fabd993043b5` stopped and is not the baseline here.

Older Sol's run-state still says `running`. Its workflow block and coordinator trace establish a publication failure: `ValueError: replacement requires a new run ID`. It reused an ID already present in the retained set. This is a publication-identity defect, not a rejected analytical finding. Its output is an unpublished comparison input.

### Model identity evidence

The Luna coordinator messages record `gpt-6-luna`. Pi's subagent-result metadata independently records `openai/gpt-6-luna` in all 15 older-run and 14 latest-run worker results. Those counts include launch diagnostics and retries; they are not counts of distinct accepted jobs. Both sessions record medium reasoning.

Codex turn-context records identify `gpt-6.1-sol` and low reasoning in the older coordinator and its 12 child sessions. The latest coordinator and its 16 child sessions record `gpt-6-sol` and low reasoning. The latest session's startup-instruction provenance says `gpt-6-astra`; this is not its active turn model. The audit uses the turn-context model and effort fields, not the startup provenance or a model inferred from a run's prose.

These are recorded identifiers. The audit does not infer provider-side model equivalence between `gpt-6-sol` and `gpt-6.1-sol`.

## Latest Sol versus latest Luna

Both runs use method `8a76fe4b9`, but their model, harness and reasoning setting differ.

| Mechanism or classification | Latest Sol | Latest Luna |
|---|---|---|
| Requested checkpoint read versus automatic later prompt supply | Correctly separates pull from push | Calls all included reads pull and push signals inapplicable |
| Local execution feedback reused through full generator output | Correctly identifies conditional tool-trace input for cumulative/hybrid updates | Says no tool-trace input is established for the update |
| Previous synthesis sheet supplied to the next synthesis curator | Explicit in the memory account | General synthesis description does not preserve this later-consumer path in its detailed inventory |
| Ranking authority | Misattributes embedding ranking to prior outputs; verifier rejects it | Similar misattribution accepted by verification |
| Semantic curation | Withholds operations not established by semantic comparison | Also appropriately withholds them |
| Improved capacity | Not established | Not established |

The source chain supports automatic later delivery and conditional tool-feedback reuse. It does not establish actual model uptake or improved capacity. For synthesis, the carried prior sheet reaches the next curator; the next generator receives the newly synthesized sheet or retrieved-pair fallback, not necessarily the previous sheet unchanged.

### Why Sol stopped

The final verifier identifies three consequential profile defects:

1. **Ranking attribution.** Similarity ranks precomputed task-input vectors; prior outputs are attached after index selection. No cited output content determines priority. The profile excludes those static embeddings from accumulated-memory scope, so it cannot silently attribute their force to the retained outputs.
2. **Coverage uncertainty.** Unobserved model compliance is an evidence-strength limit on identified prompt paths, not a separate unresolved retained part or consumer. It does not by itself justify partial inventory coverage.
3. **Missing selector.** The push-signal inventory omits whole carried synthesis text supplied to the next synthesis curator while claiming known coverage.

See latest Sol `profile-verification-1.md:13–25`. The run-state's stop reason quotes only the first blocker. The stopped profile is not ready to publish. Its correct route account remains useful, and the final verifier's rejection is warranted.

A residual audit finding is that Sol's trace-source inventory identifies conditional tool feedback for cumulative/hybrid updates but does not separately preserve the same possible source in selected full outputs feeding synthesis (`profile-1.md:252–269`).

## Luna versus Luna

This comparison holds recorded model, harness, reasoning and source revision constant. Method differs, but one execution per method cannot establish that method caused the differences.

The profile's [classification contract](../../agentic-system-analyses/types/agentic-system-memory-profile.md) distinguishes retained parts, actual consumers, evidence strength and inventory coverage. The [theory-builder definition](../../notes/definitions/theory-builder.md) separates stated theory content, content-dependent consumption, criticism and criticism-shaped iteration. A wired prompt path is evidence of delivery, not proof of the full consumption condition.

| Area | Older Luna | Latest Luna | Comparative finding |
|---|---|---|---|
| Implementation references | Some runtime anchors name the empty `__init__.py`; other members identify or repair attribution | More consistently names `language_model.py` | Latest improves independently readable source attribution |
| Answer/update timing | Does not clearly explain that the answer precedes the last post-answer sheet update | Explicitly separates returned answer from subsequent sheet update | Latest improves timing explanation |
| Scope consistency | Excluded provider internals do not reduce included-axis coverage | Excludes them in scope, then inserts unresolved provider units into multiple axes | Older is more consistent |
| Checkpoint representation | Preserves symbolic field structure alongside text | Omits symbolic representation from profile despite its memory record | Latest loses a supported finding |
| Authority at distinct consumers | Preserves experience feeding durable guidance, vector ranking and checkpoint routing | Drops learning/routing findings and poorly scopes ranking to examples | Older preserves more useful distinctions |
| Lineage | Keeps known derivation findings beside unresolved provenance | Makes every lineage unit undetermined | Latest loses known derivation detail; older authorship labels still need caution |
| Theory-building assessment | Separates localized strategy formulation and wired delivery from unestablished criticism and criticism-shaped iteration | Broadly leaves conditions unestablished | Older gives the more discriminating assessment |
| Pull/push | Incorrect pull-only classification | Same | Shared defect, not a regression |
| Semantic curation | Undetermined: replacement does not establish semantic operation | Same restraint | Both appropriately cautious |
| Tool feedback | Underclassifies conditional reuse and says no independent tool-trace input is established | Also misses it and says no tool-trace input is established | Shared defect |
| Synthesis carry-forward | Treats synthesis mainly as per-query context, failing to preserve next-curator reuse adequately | Detailed inventory still omits that later consumer | Neither is a sound reference for this mechanism |

The preference is bounded: retain older Luna's better-scoped profile and condition-by-condition assessment, and latest Luna's cleaner implementation anchors and timing explanation. Neither should be the uncorrected correctness baseline.

### Shared source-checking defects

- **Malformed-tag fallback.** Missing opening `<cheatsheet>` causes fallback. Missing closing markup can still admit the remaining text. Claims that missing or invalid tags generally preserve the previous sheet are too broad.
- **Persisted scoring.** The benchmark saves input, target and generation fields before evaluation. The Boolean check updates counters and printed reporting; it is not inserted into those saved result records. Both accounts conflate computed correctness with persisted fields.
- **Delivery versus requests.** Caller orchestration does not make every later read pull. A requested restart and automatic supply to a model consumer are distinct operations.
- **Delivery versus benefit.** Both appropriately avoid causal performance claims, but withholding observed benefit should not erase an inspected delivery route or known derivation path.

## Older Sol as an additional baseline

Older Sol already records the correct pull/push distinction, conditional reuse of execution feedback including failures, and carried synthesis text reaching the next curator. These are not new mechanisms discovered by the latest method. Comparing newest Sol only with older Luna would wrongly suggest that they were method improvements.

Older Sol also keeps a stronger condition-by-condition account of theory building. It distinguishes formulated strategies, consumption, criticism and iteration without inferring actual uptake from prompt insertion. It does not misattribute vector ranking to solution-output text: its separate ranking finding is claimed curator interpretation of usage counts.

It is not a gold standard. Its wired `evolve` finding rests on whole-sheet replacement, which does not establish semantic revision of an existing entry. Its memory narrative preserves synthesis carry-forward better than its push-signal profile inventory. It also uses an older aggregate profile schema and a wider scope including direct-client history, compatibility configuration and unresolved native state. Different scope or schema coverage must not be counted as factual gains or losses without checking the underlying route.

## Elapsed runtimes

Measure elapsed wall time from the successful workflow-start invocation to the terminal `done` or block response. Include worker execution, orchestration, retries and validation. Exclude preparation and subsequent handoff/explanation. UTC timestamps below retain milliseconds; displayed durations are rounded to the nearest second.

| Run | Start UTC | Terminal response UTC | Elapsed | Accepted jobs | Endpoint |
|---|---|---|---|---:|---|
| Older Sol | 2026-10-04 21:30:20.973 | 2026-10-04 22:08:52.675 | 38m 32s | 12 | Publication block |
| Older Luna | 2026-10-05 14:19:16.738 | 2026-10-05 14:53:33.328 | 34m 17s | 12 | Published |
| Latest Luna | 2026-10-06 07:49:53.359 | 2026-10-06 08:17:34.622 | 27m 41s | 12 | Published |
| Latest Sol | 2026-10-06 07:52:27.033 | 2026-10-06 08:20:09.249 | 27m 42s | 16 | Profile-verification stop |

Accepted-job counts come from `workflow-state/state.json` entries with accepted outputs. They include correction rounds and do not imply that all substantive findings were judged correct.

Latest Luna is 395.327 seconds faster than older Luna, about 19.2% less elapsed time. Older Luna repeats runtime and epistemic attempts; latest Luna retries a verifier launch after a malformed coordinator path. Both revise the profile. These are observed execution costs, not a general model-speed ranking.

The newest Sol and Luna executions have almost identical elapsed time but different endpoints and work: Sol performs more correction/verification jobs and stops before synthesis/publication; Luna completes those final stages. Their elapsed times cannot be interpreted as equal cost per completed analysis. No cost or token comparison was performed.

## Implications for the workshop

The current [report-correction plan](./report-correction-implementation-plan.md) says no model run has exercised the implementation. The newest runs at `8a76fe4b9` now provide post-change evidence. Latest Sol includes multiple epistemic correction and re-verification rounds; latest Luna reaches publication without a record-correction round. This report establishes that the implementation was exercised, not that its propagation goals or relative efficiency have been independently verified.

The observed outcomes support three bounded conclusions:

- Publication status is an inadequate proxy for correctness. The published Luna set contains source-checkable defects that the stopped Sol run either avoids or catches.
- An evaluation needs the actual run output, exact model/effort/harness metadata and a fixed comparison question. An inherited retained set or an initial session model can misidentify the evidence.
- Same-method differences remain confounded by model, harness and effort. The Luna pair is a closer method comparison, but still lacks replication and differs in correction/retry work. Older Sol adds mechanism evidence, not a controlled model trial.

The evidence supports considering a repeated comparison with fixed source, harness, effort, publication policy and claim-level checks. This report does not authorize that trial, prescribe a new method, reopen stopped runs or authorize repairs to published profiles. Any further run or method change remains an operator decision under the workshop's authority boundary.

## Evidence locator and retention limits

The findings above are extracted here so their interpretation survives local-worktree cleanup. Full reports and raw traces remain local evidence; this report does not archive their exact bytes. Preserve them until any audit requiring those bytes has extracted its evidence or the operator disposes of it explicitly. The previous conversational mistake is retained above to prevent reuse of its incorrect baseline table.

### Run files

From the repository root, each run is under `.commonplace/worktrees/dynamic-cheatsheet-<token>/kb/agentic-system-analyses/state/<run-id>/`. Source anchors below are under that worktree's `related-systems/suzgunmirac--dynamic-cheatsheet/`.

- Older Sol: `output/memory.md:82,208,227,278–298`; `output/memory-profile.md:121–126,187–274`; `output/epistemic.md:76–78`; `workflow-state/workflow/block-1.md`.
- Older Luna: `output/memory-profile.md:54,79–92,96–172,198–256`; `output/memory.md:136–159,183–187`; `output/epistemic.md:157`; `output/runtime.md:62–80,164–169`; `output/reconciliation.md:12`.
- Latest Luna: `output/memory-profile.md:9,27–80,81–117,151–212`; `output/memory.md:28,38–43,110–116`; `output/epistemic.md:41–42,58,88–95`; `output/overview.md:63–67,93–112`.
- Latest Sol: `output/memory.md:103–104,164`; `profile-1.md:101–113,149–218,239,252–269`; `profile-verification-1.md:13–25`; `workflow-state/workflow/block-1.md`.
- Pinned implementation: `dynamic_cheatsheet/language_model.py:249–288,397–435,504–546,574,631`; `run_benchmark.py:180–189,246–309`; `dynamic_cheatsheet/utils/extractor.py:76–87`; `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:128–130`.

### Harness traces

Paths are local operator evidence, not portable KB links. Line numbers refer to the JSONL files inspected on 2026-10-06; later appends do not change the cited earlier lines.

| Run | Trace directory and filename | Identity / timing evidence |
|---|---|---|
| Older Luna | `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-05T14-17-53-672Z_01a10c6d-a108-75c2-8fc6-b0ddd65a3d57.jsonl` | Model change at line 4; worker-result metadata throughout; successful start call line 15; `done` response line 71 |
| Latest Luna | `/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-06T07-48-21-490Z_01a1102f-5b72-75c2-8fc6-b0e2f18bac6f.jsonl` | Model change at line 4; worker-result metadata throughout; successful start call line 15; `done` response line 71 |
| Older Sol | `/home/zby/.codex/sessions/2026/10/04/rollout-2026-10-04T23-29-57-01a108d2-d786-7222-836d-b538a7722976.jsonl` | Turn context line 8; command start time in line 27; publication-block completion time in line 638; child traces linked by parent thread ID `01a108d2-d786-7222-836d-b538a7722976` |
| Latest Sol | `/home/zby/.codex/sessions/2026/10/06/rollout-2026-10-06T09-50-41-01a11031-7e9b-7322-bf60-e4b3a8bd7125.jsonl` | Turn contexts lines 8 and 38; command start time in line 70; terminal-block completion time in line 470; child traces linked by parent thread ID `01a11031-7e9b-7322-bf60-e4b3a8bd7125` |

For Pi, timing uses the successful tool-call timestamp and terminal tool-result timestamp. For Codex, it uses command-event `started_at_ms` and `completed_at_ms`. Neither duration is calculated from filesystem modification times or the session's final modification time.
