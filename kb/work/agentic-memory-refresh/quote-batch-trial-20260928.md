# Quote-batch specialist trial — 2026-09-28

## Main question: did failed tool use require recovery?

The operator clarified that this experiment tests **intermediate failures and recovery**, including wrong tool calls that fail before the agent adjusts. A clean final report is insufficient evidence. The initial summary overemphasized final citation correctness. The parent re-audited the retained tool traces after this clarification; the findings below count unsuccessful attempts even when later work succeeded.

**No quote-tool misuse followed by repair was observed.** There was no malformed quote invocation, failed selection lookup, candidate-shape exception, hand-formatted citation repair, or quotation/YAML validation failure. This finding comes from the invocation and result traces, not merely from final validation. However, the overall execution was not free of failed attempts: **five oversized read deliveries were truncated and followed by narrower reads**.

| Specialist | Quote-tool misuse failures followed by repair | Other failed attempts and adjustments | Quote calls needing a choice |
|---|---:|---|---|
| Dynamic Cheatsheet | 0 observed | Two oversized combined reads truncated; bounded reads followed | One exit-2 batch: one ambiguous selection |
| Mem0 | 0 observed | One oversized combined contract read and one broad grep truncated; narrower reads followed | One exit-2 batch: six ambiguous selections |
| Napkin | 0 observed | One broad discovery grep truncated; bounded reads followed | None |

The five truncations are tool-use failures to deliver the requested evidence in full, even though the shell commands returned success. Dynamic Cheatsheet's returns 3 and 5, Mem0's returns 3 and 9, and Napkin's return 13 locate these events in each saved `*-tools.json`; subsequent read calls document the adjustment. They must not disappear from the experiment because the worker eventually obtained enough source text.

The two exit-2 quotation responses also remain in the attempt ledger. Dynamic Cheatsheet's second batch returned two `curator` candidates; Mem0's batch returned candidates for six keys. Both workers selected emitted occurrences unchanged. Neither first tried to parse the candidate result as a single citation and crashed. These were expected ambiguity responses, not malformed calls or failed handling. Dynamic Cheatsheet's Python wrapper returned outer exit 0 while printing the inner generator exit 2 and stderr: inspecting only top-level statuses would miss it.

The parent recursively inspected nested shell results and scanned delivered output for invocation errors and exceptions, then checked the generator wrappers and follow-up calls. `failure-recovery-reaudit.json` preserves the supplementary scan. It found no additional visible failure diagnostic. Some shell chains do not propagate every subordinate status, and truncated deliveries cannot prove the absence of diagnostics in omitted spans. Therefore zero observed quote-tool misuse is a bounded finding, not proof of zero hidden failures throughout execution.

### Final artifacts, as a separate check

All 66 final quote blocks match generated citations unchanged and resolve against their frozen source commits. All three first full report validations passed without quotation or YAML errors. Dynamic Cheatsheet handled one multiple-occurrence selection, Mem0 handled six, and Napkin encountered none. All three adopted batch generation, a secondary finding.

Every citation **used** in each report entered unchanged. Not every candidate emitted entered a report: Dynamic Cheatsheet left five earlier selections and one alternative unused; Mem0 left seven alternatives unused. Napkin used all 24 distinct generated citations. Three stochastic runs do not establish a general error rate. Napkin did not exercise the multiple-occurrence case, and none exercised an error-status payload.

## Commission and execution boundary

The operator commissioned the [quote-batch trial](./quote-batch-trial.md) to test whether three fresh memory specialists discover batch quotation generation through the current instruction, and whether quotation authoring errors recur. This record covers specialist reports only. No exact result, public review or publication is produced; the prepared run states remain `running`. No Git commit is authorized or made.

The parent scheduled the specialists serially with `fork_turns="none"`. Each handoff contained only the fresh source-only commission, instruction path, run ID, frozen input path, report destination and permitted source access root. The runtime supplied repository doctrine. The parent did not mention the batch flag, this experiment or earlier findings to a worker. The copied inputs contain source-checkable provisional records as commissioned; they are not empty source packets. Prior reports were read only by the parent for the comparison below. No worker read a prior analysis or called agent listings in the inspected traces.

The parent began at Commonplace HEAD `cb6f796df25381f4f78f20b9cd6b889e4b9d8da3`. `commonplace-quote --help` exposed `--selections`, all source origins matched the run states, and all three frozen commit objects existed. Each prepared input was confirmed equal to its baseline input with only the run ID replaced. Source worktrees were left alone, including their preexisting staged deletions.

Local audit evidence is under `kb/reports/cache/agentic-memory-refresh/quote-batch-20260928/`: `startup.json`, `baselines.json`, each worker's copied full trace and trace metadata, tool events, generated payloads, citation comparisons, audit, and independent verification output. This workshop record retains the findings; the ignored cache is not a durable library dependency. The original session paths and hashes identify the inspected traces below. Word counts split the complete Markdown, including frontmatter, on whitespace; quote counts count complete quote-anchored blocks.

## Dynamic Cheatsheet

Worker `/root/quote_dynamic` used `gpt-6-astra`, medium effort, as confirmed by its trace. The report itself records model `unknown`; the parent does not overwrite that report field. Run: `AAS-2026-09-28-dynamic-cheatsheet-quote-trial-01`. Frozen source: `https://github.com/suzgunmirac/dynamic-cheatsheet`, commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`.

The worker read `commonplace-quote --help` before generation, but did not read the command reference. It made two batch generation calls and no single-selection calls:

| Call | Selections | Distinct source files | Exit | Outcome |
|---|---:|---:|---:|---|
| First | 16 | 4 | 0 | Sixteen unique citations |
| Second | 7 | 6 | 2 | Six unique citations; `curator` has two candidates |

The second call's stderr was `1 of 7 selections need attention: curator (candidates)`. The candidates cover `dynamic_cheatsheet/language_model.py:423-425` and `:631-633`. The worker chose the first, cumulative occurrence unchanged and described hybrid behavior separately. There was no lookup error or generator exit 1. Several first-call selections were replaced by shorter, more relevant selections, not repaired after failed matching. First-call `curator`, `extract`, `budget`, `save` and `hybrid` citations did not enter the report; neither did the second curator candidate. Of 24 emitted citation variants, 18 entered unchanged. Every final quote block matches an emitted citation byte-for-byte apart from its terminal newline.

Batch adoption removed the per-quote generator loop, but Python wrapping remains: two `subprocess.run` calls build/save keyed JSON and explicitly print return code, stderr and stdout. The report assembler handles `citation` or chooses `occurrences[0]`. That handled this run's candidate response; it does not contain a separate error-status branch. This is a limit of the wrapper, not an observed failure. Selection line ranges were used to obtain source text; attribution ranges came from the generator.

The first full report validation passed cleanly with 18 well-formed anchors, and the final validation did too. JSON frontmatter avoided bare-YAML-key ambiguity. No edited or handwritten final citation, quotation error, or YAML error reached validation. Independent parent validation passed; frozen-source verification resolved **18 citations, zero failures**. The report has 4,883 words versus baseline 5,451, and 18 quotes versus 20.

There were two outer output truncations during early contract/source loading. Later bounded source reads recovered needed code, but the trace does not justify claiming complete initial contract delivery. Neither generator output nor validation output was truncated. Some source pipelines and semicolon/newline chains do not propagate every subordinate command status; generator status and stderr were explicitly retained. Progress-message text is encrypted in the stored trace, while successful delivery returns are visible. These limits do not hide the quotation outcomes above.

## Mem0

Worker `/root/quote_mem0` used `gpt-6-astra`, medium effort. Run: `AAS-2026-09-28-mem0-quote-trial-01`. Frozen source: `https://github.com/mem0ai/mem0`, commit `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`.

The worker read `commonplace-quote --help` before generation, but did not read the command reference. One direct batch invocation carried **24 selections across seven source files**, exited **2**, and reported six candidate keys: `extract`, `payload`, `entities`, `links`, `expire`, and `cleanup`. The other 18 keys resolved uniquely. There were no single-selection calls, lookup errors or generator exit 1.

| Candidate key | Emitted line ranges in `mem0/memory/main.py` | Chosen unchanged |
|---|---|---|
| `extract` | 950–955; 2633–2638 | 950–955 |
| `payload` | 1032–1034; 2711–2713 | 1032–1034 |
| `entities` | 1166–1167; 2847–2848 | 1166–1167 |
| `links` | 1187–1190; 2867–2870 | 1187–1190 |
| `expire` | 1684–1685; 3371–3372 | 1684–1685 |
| `cleanup` | 665–667; 2347–2349; 2363–2365 | 665–667 |

The worker inspected the ambiguous outputs, then selected the first occurrence for each, corresponding to the synchronous implementation it had inspected. It did not lengthen or drop any selection. Of 31 emitted variants, 24 entered unchanged; seven alternatives were unused. All final blocks match generator citations exactly apart from terminal newlines.

The shell invocation redirected generator stdout to `/tmp/mem0-quotes.json`, with exit status and stderr visible in the trace. The parent copied that output and the selection list after completion; the trace shows no later rewrite of the generated payload. Python builds selections and assembles the report, but there is no per-selection generator subprocess loop. Its assembler handles a citation or `occurrences[0]`, with the same unexercised missing error-status branch as Dynamic Cheatsheet.

First full validation passed cleanly with 24 well-formed anchors. The worker then added an afforded `tool-traces` value and changed the `trace_source` assessment before a second clean validation; this was an analytical edit, not a quotation/YAML repair. Frontmatter was serialized as JSON. No quotation or YAML error reached validation. Parent validation passed and frozen-source verification resolved **24 citations, zero failures**. The report has 7,075 words versus baseline 8,622, and 24 quotes versus 23.

One outer contract read and one nested discovery grep were truncated; bounded contract/code reads followed. Generator and validation results were complete. Source pipelines did not independently propagate Git status. Interagent message contents are encrypted in the trace, but their delivery succeeded. No prior-analysis exposure, publication or out-of-scope mutation was observed.

## Napkin

Worker `/root/quote_napkin` used `gpt-6-astra`, high effort. Run: `AAS-2026-09-28-napkin-quote-trial-01`. Frozen source: `https://github.com/Michaelliv/napkin.git`, commit `7582d6a46f5a11995956e60a59c41a5b242109f1`.

The worker read `commonplace-quote --help` before generation, but did not read the command reference. It made two batch calls, each with the **same 24 selections across 14 files**, and no single-selection calls. Both returned exit 0; every selection was unique. The first complete JSON payload was delivered in the trace. The second call repeated generation inside a `subprocess.check_output` report assembler. Its successful continuation, absence of an exception and completed report establish exit 0; stderr inherited the shell capture and showed no diagnostic. It did not print that second payload. The selection file was unchanged between calls and deleted at completion; its contents are reconstructable from the retained creation command.

All 24 distinct generated citations entered the report unchanged; no candidate was omitted or selected, and no error-status response occurred. The assembler asserts that every keyed status is `citation`. That worked for this run; it does not demonstrate recovery from candidates or errors. There is no per-quote generator loop. Its `rstrip()` removed only terminal whitespace after the attribution: the actual final blocks match the first generated payload byte-for-byte apart from the terminal newline.

The first full validation passed cleanly with 24 anchors. The worker subsequently clarified status-label wording and revalidated; those edits did not repair quotations or YAML. Frontmatter was serialized as JSON. Independent parent validation passed and frozen-source verification resolved **24 citations, zero failures**. The report has 4,505 words versus baseline 7,703, and 24 quotes versus 35.

One discovery grep delivery was truncated; bounded blob reads followed. Quote generation and validation results were not truncated. Fourteen later source reads retained full nested shell results, all exit 0; they were not stdout-only results. Some early command chains lack individual failure propagation, while the later source loop enables `pipefail`. Progress-message contents are encrypted in the trace with successful delivery responses. No prior-analysis exposure or unauthorized mutation was observed.

## Comparison context

These differences describe independently authored reports, not effects causally attributable to batching. Baselines are the specialist reports named in the commission: Dynamic Cheatsheet `AAS-2026-09-27-dynamic-cheatsheet-04`, Mem0 `AAS-2026-09-27-mem0-04`, and Napkin `AAS-2026-09-27-napkin-05`. All source pins and commissioned input content are fixed. Values below preserve each report's order; a reordered set alone is not a classification change. Per-value evidence and rationale remain in the saved report/comparison payloads; this table reproduces the requested assessments and values, not an independent adjudication of their correctness.

| Specialist | Baseline words | Trial words | Baseline quotes | Trial quotes |
|---|---:|---:|---:|---:|
| Dynamic Cheatsheet | 5,451 | 4,883 | 20 | 18 |
| Mem0 | 8,622 | 7,075 | 23 | 24 |
| Napkin | 7,703 | 4,505 | 35 | 24 |

### Dynamic Cheatsheet — fourteen axes

| Axis | Baseline assessment; values | Trial assessment; values |
|---|---|---|
| `storage_substrate` | known; files, in-memory | known; files, in-memory |
| `representational_form` | known; natural-language, symbolic | known; natural-language, symbolic |
| `lineage` | known; imported, trace-extracted | known; imported, trace-extracted |
| `behavioral_authority` | known; knowledge, ranking | known; knowledge, ranking |
| `write_agency` | known; automatic | known; automatic |
| `curation_operations` | known; evolve, synthesize, dedup, promote | partial; evolve, consolidate, dedup, synthesize, promote |
| `read_back_direction` | known; push | known; push |
| `read_back_signal` | known; coarse, inferred-embedding, inferred-judgment | known; coarse, inferred-embedding, inferred-judgment |
| `trace_learning` | known; yes | known; yes |
| `trace_source` | known; trajectories, tool-traces | known; trajectories, tool-traces |
| `learning_scope` | known; per-task, cross-task | known; cross-task, per-task |
| `learning_timing` | known; online | known; online |
| `distilled_form` | known; natural-language, symbolic | known; natural-language, symbolic |
| `faithfulness_tested` | not-determinable; ∅ | not-determinable; ∅ |

### Mem0 — fourteen axes

| Axis | Baseline assessment; values | Trial assessment; values |
|---|---|---|
| `storage_substrate` | partial; vector, sqlite | partial; vector, sqlite |
| `representational_form` | partial; natural-language, symbolic | partial; natural-language, symbolic |
| `lineage` | partial; trace-extracted, imported, authored, other-compiled | known; authored, imported, trace-extracted, other-compiled |
| `behavioral_authority` | partial; knowledge, ranking | partial; knowledge, ranking, routing |
| `write_agency` | known; automatic, manual | known; automatic, manual |
| `curation_operations` | partial; dedup, evolve, invalidate, decay | partial; dedup, evolve, invalidate, decay |
| `read_back_direction` | known; pull, push | known; pull, push |
| `read_back_signal` | partial; identifier, inferred-embedding | known; identifier, inferred-embedding |
| `trace_learning` | known; yes | known; yes |
| `trace_source` | partial; session-logs, trajectories, tool-traces | partial; session-logs, trajectories, tool-traces |
| `learning_scope` | partial; per-task, cross-task | partial; cross-task, per-task |
| `learning_timing` | partial; online | partial; online |
| `distilled_form` | partial; natural-language, symbolic | known; natural-language |
| `faithfulness_tested` | not-determinable; ∅ | uninspected; ∅ |

### Napkin — fourteen axes

| Axis | Baseline assessment; values | Trial assessment; values |
|---|---|---|
| `storage_substrate` | known; files, in-memory, sqlite | known; files, in-memory |
| `representational_form` | known; natural-language, symbolic | known; natural-language, symbolic |
| `lineage` | known; authored, imported, other-compiled, trace-extracted | known; authored, imported, other-compiled, trace-extracted |
| `behavioral_authority` | known; knowledge, instruction, ranking, routing | known; knowledge, instruction, ranking, routing |
| `write_agency` | known; automatic, manual | known; automatic, manual |
| `curation_operations` | known; consolidate, dedup, evolve, invalidate, decay, synthesize | known; evolve, invalidate, decay, dedup, consolidate, synthesize |
| `read_back_direction` | known; pull, push | known; pull, push |
| `read_back_signal` | known; coarse | known; coarse |
| `trace_learning` | known; yes | known; yes |
| `trace_source` | known; session-logs | known; session-logs |
| `learning_scope` | known; cross-task, per-project | known; cross-task, per-project |
| `learning_timing` | known; staged | known; online |
| `distilled_form` | known; natural-language, symbolic | known; natural-language |
| `faithfulness_tested` | not-determinable; ∅ | not-determinable; ∅ |

## Provenance and preservation

The original session traces were copied byte-for-byte into the local audit cache after each worker ended. The parent inspected all tool calls and returns, including nested shell results, reported statuses and stderr. Source text containing words such as “error” was not counted as a command failure. The cache preserves full delivered output, including truncation notices; it cannot recover bytes that were never delivered. The observed quotation calls, candidate responses, report construction and validation were sufficient for the primary finding above.

Each specialist also ran `commonplace-quote --help` once before its first generation call. Mem0's help command returned exit 0 directly. Dynamic Cheatsheet and Napkin delivered complete help but combined it with later reads, so the final shell status alone does not separately prove the help subprocess status. None read the command reference. Across the trial there were five batch generation calls (95 selection attempts, including Napkin's duplicate 24), zero single-selection generation calls, two exit-2 candidate responses and no observed generator exit-1 failures.

### Trace identities

- dynamic: original `/home/zby/.codex/sessions/2026/09/28/rollout-2026-09-28T08-52-22-01a0e6c9-3b56-7a63-bd69-5167dc17e46a.jsonl`; copied `dynamic-trace.jsonl`; SHA-256 `6dac536ccce27030df4041efed99f0db1fffaaf0e33d4d521d103af4a507b161`; gpt-6-astra, medium.
- mem0: original `/home/zby/.codex/sessions/2026/09/28/rollout-2026-09-28T08-59-21-01a0e6cf-a095-7d61-9c21-6bf40a179d54.jsonl`; copied `mem0-trace.jsonl`; SHA-256 `8ab3ee325e4ef8d1ee94444fc96973c60e2dd4d28795c672e5001f476042717f`; gpt-6-astra, medium.
- napkin: original `/home/zby/.codex/sessions/2026/09/28/rollout-2026-09-28T09-08-19-01a0e6d7-d3c6-7871-a6f8-d1addd7ac87f.jsonl`; copied `napkin-trace.jsonl`; SHA-256 `db3b4a1e3665f092dcbb39e4c7ac9610343d8be168716c3c832d9fb5c057773c`; gpt-6-astra, high.

### Input, method and output identities

| Artifact | SHA-256 |
|---|---|
| `kb/instructions/analyse-agent-memory.md` | `7fad98f7ef579e82729c556bdfe9f8b0d0061887d64932db71bf2dabf73c273f` |
| `src/commonplace/cli/quote.py` | `908394ebf6c1e27475e658785b4b4cd5c516ee05171f5087d0a93544b8a181a3` |
| `src/commonplace/lib/quote_generation.py` | `e499ceb5e9c0a551aa42de1b3c1b84cf5804ea67402f12720dc21c261c39ae12` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-dynamic-cheatsheet-quote-trial-01/memory-input.md` | `e1b8ac079ee6b055d43e8bf3ba08d9577e89071c8b8f07cf3104e7abc229d203` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-dynamic-cheatsheet-quote-trial-01/run-state.md` | `c0dfe58d0c4e6388df16e826e74b6dd0562d48b20be776d35df5231263786ef8` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-mem0-quote-trial-01/memory-input.md` | `4bd7b0d79e8c14adb3f09b57f8ce09c454820449c65d474945cb81cfac603057` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-mem0-quote-trial-01/run-state.md` | `93e1912ba415a2d8b53c5aeaadd23d298563213e8cbe9878a07ea921f91213b2` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-napkin-quote-trial-01/memory-input.md` | `dcb9a670a82af5eb574479a205ad25fc3936e31216aabe3794d0ab7dc9b4d907` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-napkin-quote-trial-01/run-state.md` | `2ff42f493ef68c85ab341e80be17bf7cae30408d5e210c136876b34948fcbf38` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-dynamic-cheatsheet-quote-trial-01/memory-report.md` | `161c006c64f67f900d5670066cfce2f638b1ae9056c751d696369b13cb7a35ae` |
| Baseline `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-04/memory-report.md` | `39be455f397ecf0998172d975808de78a7815e12408c9117948ef64c77da55ae` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-mem0-quote-trial-01/memory-report.md` | `3d6ecb512c5838b9fb72655ba87c053a1a2e1dcf59068e865a63e2bf47c4d62d` |
| Baseline `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-04/memory-report.md` | `6812d1e3a042bb36a6fa21bb1f6eb23d29448866f3d65e6ae432d4231a55172c` |
| `kb/reports/state/agentic-system-analysis/AAS-2026-09-28-napkin-quote-trial-01/memory-report.md` | `9227d8eac00a09d51996814c1d2c375920b3b983d87f71c2bb74e28846229a41` |
| Baseline `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-napkin-05/memory-report.md` | `64a2c3318cf344578973dc23bacd36bae167cef2fab461211e6218ad398ad0cb` |

At completion, HEAD remained `cb6f796df25381f4f78f20b9cd6b889e4b9d8da3`. Method, generator source, all prepared inputs, all run states and all baseline reports retained their startup hashes. All source worktree status snapshots were unchanged. The parent kept the three specialist reports and left their run states `running`; it did not complete or publish a run, produce an exact result, change the method/generator, or commit. Final report/README validation is recorded in the local cache.
