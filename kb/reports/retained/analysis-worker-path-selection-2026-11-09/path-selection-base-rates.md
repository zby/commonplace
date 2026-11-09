---
type: types/note.md
description: "Measured path-selection base rates in 16 Commonplace analysis runs, including successful inferred paths, missing-path recovery and shell failures hidden by successful exit status."
---

# Analysis worker path-selection base rates — 2026-11-09

## Result and retention purpose

Retain bounded source-path speculation in Commonplace analysis work. The observed successful inferred paths substantially outnumbered misses. This observation does not establish an optimal guessing policy or justify requiring discovery before every read. The more consequential risks were successive wrong guesses for the same operation, overlooked partial failures, and inspection skipped by an interrupted batch.

This dated report supports the operation of selecting and evaluating source-navigation guidance for `analyse-agentic-system`. The operator commissioned missing-path diagnosis and explicitly asked for successful guesses to establish base rates. The operator then requested retention of the analysis. This is an observation of Commonplace's own workers, not a characterization of the external systems, a final-output correctness audit, or an adopted instruction change.

## Inputs and observation boundary

The review covered 16 completed analysis runs: four reruns of Cortexes, Curated Thoughts, KHMS Memory and Project Wiki, followed by 12 newly selected systems from saved Karpathy gist comment pages. The new systems were Verbatim Citation Gate, Qiju, OmniMemory, SQLite Graph Memory, Post-Graph RAG, MDCP, Eva Brain, LLM Repo Wiki, Citadel, PM LLM Wiki, Team AI Workflows and SIGN.

The selected evidence comprised **197 role streams and 16 advisory-auditor streams**, all Pi JSON event streams. Their recorded activity extended from **2026-11-08T20:52:00.972Z to 2026-11-09T02:25:35.337Z**. Counts include correction and verification invocations, not just initial analysts. Only 120 of the 213 streams contributed concrete-file targets to the census.

The producing analysis configuration was `pi-sol` / `gpt-6.1-sol`, medium effort, with two concurrent analyses and three role-worker slots per analysis. The four reruns used method commit `1d70490506788fd638b76261169d6d2408cbc034`; the 12 new runs used `b4f3eb5ff47846da2c77940152815918f9573e75`. These are different method pins. The prior campaign check found no intervening differences in analysis code, headless execution or analysis instructions. This report does not estimate an effect of either revision.

The reviewing model was `gpt-6.1-sol` in Pi, coordinator session `01a1b743-1bd3-7316-84a6-af495096cc3e`. The review followed [hidden-failure review](../../../instructions/review-recent-logs-for-hidden-failures.md) and [design-pressure diagnosis](../../../instructions/review-design-pressure-behind-recurring-errors.md). The initial failure leads came from `src/commonplace/lib/agentic_analysis/tool_failures.py`, using `scan(path, 'pi-json')`; the base-rate census separately inspected successful calls. No workers, target programs or failed commands were replayed for this diagnosis.

The preceding hidden-failure review matched role inventories to launch directories and recorded hashes, with no missing selected traces or scanner input issues. For this census, every source checkout HEAD matched its acquired frozen revision: **16 checked, no mismatches**. Exact run, method, source and stream identities are retained in the [run inventory](./records/runs.json), [trace inventory](./records/traces.json) and [source bindings](./records/source-bindings.json).

## Method and counting rules

The unit is a **concrete file target selection**, not a failed tool call or a unit of wasted work. A target is available when its exact path names a tracked file at the registered source revision and agrees with the inspected filesystem. Availability does not establish relevance, a complete read, or claim support. An existing file whose requested offset exceeds EOF still has a correct file path.

The census extracted source paths from `read` tool arguments and literal absolute operands of simple shell inspection commands: `rg`, `grep`, `cat`, `nl`, `head`, `tail`, `wc`, `ls` and `find`. It expanded literal comma-separated braces, but did not execute shell commands, resolve variables or evaluate Python/JavaScript. Repeated operands within one shell invocation counted once. Nested tool events supplied resolved arguments; their outer event envelopes were not counted again.

The primary denominator counts the **first selection of a file within each worker or auditor invocation**, across both read and shell targets. Later selections remain in a supplementary denominator. File identity is source-relative within that invocation, not global across roles or systems.

Before each selection, the classification searched the launch prompt and earlier delivered top-level tool results for:

1. the exact source-relative or absolute path;
2. otherwise, the literal filename;
3. otherwise, neither spelling.

Outputs from earlier nested operations in the same still-running codemode batch were not treated as earlier model-visible results. Missing-path diagnostic lines were excluded from the accumulated output used for positive naming evidence. A path mentioned elsewhere could still be classified as previously named; that classification does not attest that the earlier mention was valid.

This is an observable proxy for guessing, not a measurement of intent. Imports, directory conventions and other clues can license constructing a path without spelling out its filename. A filename match can also be incidental or fail to identify its directory uniquely. No private reasoning was used to classify intent.

Existing directory operands were outside the concrete-file denominator. MDCP's nonexistent `skills/mdcp/scripts` operand was manually classified as a directory-discovery root and also excluded. Wildcard probes were counted separately against the pinned file inventories, with matching confined to path components. Programmatically constructed Python paths were outside the automated file census; selected failed Python inspections were examined as incidents. Shell operands are requested targets: conditional shell execution can skip a later operand.

The captured [census script](./records/census-script.py), [target records](./records/file-targets.csv), [summary](./records/summary.json), [exclusions](./records/exclusions.json) and [wildcard records](./records/glob-availability.json) preserve these distinctions. The script is an exact capture of the one-shot analysis, not a supported command; its original local inputs are not included in full.

## Measurements

### First file selections within each invocation

| Earlier visible naming evidence | Existing file | Missing file | Total | Availability rate |
|---|---:|---:|---:|---:|
| Exact path previously appeared | 1,884 | 1 | 1,885 | 99.95% |
| Exact path had not appeared, but its filename had | 77 | 0 | 77 | 100% |
| Neither exact path nor filename had appeared | 43 | 14 | 57 | 75.4% |
| **Total** | **2,004** | **15** | **2,019** | **99.26%** |

An interim classification combined the latter two categories: **120 existing files out of 134 selections**, or 89.6%. Separating the 77 filename-cued choices gives the more informative **43/57** observation for less explicitly cued selections. Neither number is a general model guessing-success rate.

### Supplementary denominators

| Selection class, including repeats | Existing file | Missing file | Total | Availability rate |
|---|---:|---:|---:|---:|
| Read-tool file targets | 2,489 | 2 | 2,491 | 99.92% |
| Extracted shell file targets | 772 | 13 | 785 | 98.34% |
| **All extracted concrete-file targets** | **3,261** | **15** | **3,276** | **99.54%** |

Separately, **38 of 40 wildcard probes matched tracked files**. The unmatched patterns were KHMS Memory's `tools/*update*` and `tools/khms_code*`. An unmatched naming probe is not itself evidence that the intended system operation is absent.

The 14 misses without an earlier exact-path or filename mention were concentrated in four systems: **Curated Thoughts 7, Citadel 5, Cortexes 1 and LLM Repo Wiki 1**. These are target selections, not independent experiments. Repeated roles, repository layout and task difficulty confound comparisons.

## Successful inferred paths and mixed batches

Successful path construction is part of the evidence, not merely a denominator added to failed calls. The retained [representative sequences](./records/representative-sequences.json) identify original trace lines and preserve selected arguments and results without private reasoning bodies.

| Observed selection | Original stream locator | Result and interpretation |
|---|---|---|
| Cortexes `cortex-vec/src/cortex_vec/eval/score.py`, `corpus.py`, `adapters.py` | Epistemic launch `a4f03feba5e34a67892808903a8a2d5b`; read starts 1293, 1297 and 1688 | The reads succeeded without earlier literal filename mentions. This does not rule out import or naming clues. |
| Curated Thoughts `src-tauri/src/db/heal.rs` | Memory launch `80bd07cc8fe1473ab0b540db6a417f15`; search 1181–1186 | The search returned the healing functions while another operand, `db/prune.rs`, failed. |
| Citadel `kb/agent_workflows.py` and `kb/conflicts.py` | Epistemic launch `1f4b0c86a5d14fdfbc823799529e4caa`; search 2807–2811 | Both paths returned useful source matches while `kb/conflict_detection.py` failed. |
| Qiju `src/qiju/config/allowlist.json` | Runtime launch `210ee3cec66b46f9ae3553c1c5ae9187`; prior cue at result 1190, read 1592–1594 | The worker constructed the path after seeing a package-resource expression containing `config/allowlist.json`. This is evidence-guided construction, not a wholly uncued choice. |

Of the **14 outer calls containing a concrete-file miss in the extracted census, 13 also accessed or requested existing source files**. Across all 19 inspected missing-path outer calls, the extracted operands included 47 existing concrete-file targets and 15 missing ones; the remaining failures involved wildcard probes, directory roots or a Python-constructed path. Some shell targets could be conditional, so this is not a count of 47 successful reads. Treating every whole failing batch as wasted work would nevertheless overstate the observed cost.

## Missing paths, recovery and hidden status

The expanded inspection identified **19 outer calls containing missing-path incidents**, compared with 17 in the preceding scanner-led review. The [missing-call index](./records/missing-call-index.json) preserves every call's original arguments and locators. These counts do not assert that every miss was a malfunction: a probe can deliberately test a candidate location, and advisory auditors can revisit a previously failed path.

Representative recoveries were:

| Missed location | Subsequent inspection | Original locator |
|---|---|---|
| Cortexes `raw_reclaim.py` | Directory listing, then `reclaim.py` and related reads | Memory launch `ae3b947009764537a13f7695a59d9835`: failed result 1472; listing start 1536; read batch 1682 |
| Curated Thoughts guessed review and migration paths | Broader symbol search, then `db/proposals_review.rs` and `db/connection.rs` | Runtime launch `576fd0efec264258acc80a28718d78af`: failed search 2741–2746; discovery 2886; read batch 3065 |
| Curated Thoughts `src-tauri/src/okf/import.rs` | Tracked-tree lookup and `drafts_api.rs` search, followed by `db/drafts.rs`, `drafts_api.rs` and `okf/mod.rs` reads | Report-verification launch `a2bb3d63f0e04081ac8d350e4cd2d26a`: failure 4048; discovery 4226; read batch 4343 |
| Citadel `kb/improvement_scope.py` | Located and read `kb/improvement_policy.py`; resumed the interrupted inspection | Epistemic launch `1f4b0c86a5d14fdfbc823799529e4caa`: failure 2360; discovery 2578; read batch 2696 |
| Citadel `kb/agent_payloads.py`, then `kb/agent_response.py` | Read MCP imports, located `kb/search_format.py`, and inspected its compaction functions | Memory launch `5edd921a7f164ba2868fdeaf4a331930`: failures at 1953 and 2255; import read 2319; discovery 2502; reads 2570 and 2635 |
| LLM Repo Wiki `src/app/api/chat/route.ts` | Located the wiki-scoped route and inspected chat persistence | Advisory-audit launch `6dd8e0f62fb645a4a1998368536fd383`: failure 1862; discovery 2080; inspections 2237, 2553 and 2798 |

Citadel's successive payload-module guesses are the clearest avoidable-cost example. Both searches sought the same compaction machinery. The later import read supplied the correct module. Following the import or searching for the function after the first miss could have avoided the second wrong filename. That is a local diagnosis, not evidence that discovery-first is cheaper for every file.

A failed read can also stop a sequential batch before later inspection runs. The Citadel improvement-policy failure stopped three subsequent reads and a search/revision check; the continuation resumed equivalent inspection. Curated Thoughts' missing hook path stopped a subsequent search, which the continuation repeated. Recovery matters separately from the initial path choice.

### Two calls missed by the earlier scanner

1. **Citadel memory, launch `5edd921a7f164ba2868fdeaf4a331930`, lines 2251–2255.** The search of nonexistent `kb/agent_response.py` failed, but a later semicolon-separated search succeeded. The shell result had `exit_code: 0` and `isError: false` despite its missing-path diagnostic. The worker subsequently inspected `search_format.py`.
2. **Curated Thoughts advisory audit, launch `c5d82798344c496e9feb9a4fbb734219`, lines 1745–1749.** A search included nonexistent `db/wiki.rs`, but later Python inspection succeeded, again leaving `exit_code: 0` and `isError: false`. The same call found relevant functions in `lib.rs`; focused reads followed at 1930.

The diagnostics were visible in tool output. These calls expose a limit of exit-status-led scanning, not a demonstrated new defect in delivered reports. Full selected evidence for both is retained in the representative-sequence capture.

## Supported operating choice

The intended outcome is to inspect the controlling source without treating a missing candidate location as evidence that the mechanism is absent. The applicable worker rules required bounded reads, inspection of complete results including errors and truncation, exact supplied workflow locators, and frozen-source inspection. They did not establish a blanket prohibition on inferring internal source paths.

The observed successful constructions support retaining cheap exploratory choices. A mandatory preliminary lookup for every file would add work to successful cases; this review did not measure whether its savings on failures would outweigh that cost. Batching also saves expression and round trips, but sequential failure can suppress later work and compound shell commands can hide failure behind a successful final status.

The supported recommendation is therefore to allow plausible exploratory paths, prefer targeted discovery over another renamed guess after a miss, and account for useful partial results and skipped operations. Supplied input/output locators should remain exact; their reconstruction is not the same activity as exploring a source tree. This report proposes no new reader abstraction, validator, logging obligation or method amendment.

## Scope

- This is a dated observation of 16 selected Commonplace analysis runs, including four targeted reruns. It is not a random sample or a general estimate for agents, repositories or other harnesses. No non-Pi transcript bodies were inspected.
- Availability is not semantic relevance, completeness, correct quotation or claim warrant. A correct filename can still lead to an incomplete or irrelevant inspection.
- Earlier naming is a textual proxy. It cannot establish whether a worker guessed, inferred, remembered or deliberately probed a path. The single missing previously named path was revisited by an auditor; prior mention did not establish existence.
- The automated census is deliberately partial for shell programs. It excludes Python-constructed paths, variable resolution and most non-simple command forms. Existing directories and the explicitly identified missing directory-discovery root are not file targets. Wildcards have their own denominator.
- Recovery inspection was bounded. No new delivered-output defect was demonstrated by these path incidents, but this does not certify all reports. Curated Thoughts' accepted memory report explicitly left draft promotion and entity merge/redirect internals incompletely traced; the rerun did not establish that earlier substantive coverage gap was resolved.
- Failed attempts, repeated discovery and skipped inspections are observed extra work. Attributable time and token costs were not measured. Whole-session usage or wall time cannot be assigned to path guessing, and no cost-optimal policy follows.
- The retained records suffice to inspect the counts, classification and representative incidents from a clean checkout. Full reproduction against all event bodies requires the original local streams and pinned source checkouts. Hashes identify those bytes but do not replace missing evidence. The report grants no cleanup authority over the originals.
- This retention did not change instructions, analysis outputs, source checkouts or tooling, and did not integrate or rerun any analysis.

## Retained record guide

The `records/` directory is a capture/data subtree, excluded from site publication and recursive Markdown validation by its marker. The interpreted report remains outside that subtree.

| Record | Purpose |
|---|---|
| [Runs](./records/runs.json) | Sixteen run IDs, method pins, source revisions and original local worktree locators |
| [Traces](./records/traces.json) | 213 stream identities, sessions, roles, times, cutoffs, byte counts, stream hashes and prompt hashes; original paths are repository-relative locators |
| [File targets](./records/file-targets.csv) | 3,276 extracted target selections, with trace IDs, source-relative paths, lines, tool status and classification flags |
| [Summary](./records/summary.json) | Measured totals, strata and per-system counts |
| [Source bindings](./records/source-bindings.json) | Sixteen acquired revisions compared with observed checkout HEADs |
| [Exclusions](./records/exclusions.json) | Extractor exclusions, not a complete inventory of all unsupported source-reading programs |
| [Wildcard availability](./records/glob-availability.json) | Forty probes and their matching tracked files |
| [Missing-call index](./records/missing-call-index.json) | Nineteen incident locators and original arguments, including two scanner-missed calls |
| [Representative sequences](./records/representative-sequences.json) | Selected successful selections, failure/recovery sequences and masked failures; tool events only |
| [Census script](./records/census-script.py) | Exact one-shot extractor capture with its original local input locations |
| [Record manifest](./records/manifest.json) | SHA-256 and byte count of each retained supporting record |

Broader graph discovery was not part of this retention. `cp-skill-connect` can be commissioned separately if these results should inform other library artifacts.
