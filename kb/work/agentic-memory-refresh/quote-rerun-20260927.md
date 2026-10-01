# Three-pilot quote-verification rerun, 2026-09-27

All three pilots completed and published. The current checker accepts all 199
quote blocks in their exact results and specialist reports, plus two in their
generated reviews. The earlier published pilot artifacts had twelve ambiguous
blocks among 179 when the migration applied the stronger rule. No quotation
matching failure remains in the new publications under the current checker.

Authoring is still error-prone. Five source-check attempts failed before
correction, reporting eight ambiguous quote blocks, one altered quote block,
eight out-of-bounds source citation occurrences and six bare-URL attributions.
There was also one copied-image-link error and one comparison-schema failure.
This demonstrates successful rejection and recovery, not fewer drafting errors
or an error-free workflow. Two remaining instruction/validator inconsistencies
are recorded below; producer code and instructions were not changed in this run.

The operator commissioned fresh runs of Dynamic Cheatsheet, Mem0 and Napkin
to check whether the quote-verification changes reduce quotation problems.
Execution began after the intervening fixes in commit
`4a97ad715a4dbdcc6de09dea22417d1f88fbbbdf`. Producer code and instructions had
no uncommitted edits at the start. Existing review and workshop changes were
preserved; generated reviews may be replaced only through guarded publication.

## Evaluation boundary

Hold the source pins from the [previous rerun](./reliability-rerun-20260927.md)
fixed. Each system receives a fresh source-only coordinator and mandatory fresh
memory specialist. Run one coordinator and its specialist at a time. Neither
receives previous analysis or audit findings. The parent owns this record,
inventory updates, independent completion checks and trace inspection. No
producer repair or Git commit is commissioned by this replay.

| System | Frozen source revision | New run | Status |
|---|---|---|---|
| Dynamic Cheatsheet | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | `AAS-2026-09-27-dynamic-cheatsheet-02` | complete; handoff independently checked |
| Mem0 | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | `AAS-2026-09-27-mem0-02` | complete; handoff independently checked |
| Napkin | `7582d6a46f5a11995956e60a59c41a5b242109f1` | `AAS-2026-09-27-napkin-03` | complete; handoff independently checked |

Inspect the first source checks, rejected quotations, corrections, publication
checks and final handoffs in all six worker traces. Count failed check attempts
separately from individual citation diagnostics and repeated diagnostics for
the same passage. Distinguish source-range errors, absent or altered quote
text, ambiguous occurrences, attribution/parser errors and checker defects.
Final success does not erase failures earlier in a run. Truncation and other
operational problems are reported separately.

## Comparison baseline

The previous six-session rerun reported two recovered source-check failures:
one Mem0 coordinator range beyond EOF and one Napkin specialist range beyond
EOF. Dynamic Cheatsheet had no failed source check. That checker did not yet
enforce all the current matching rules.

The later [quote migration](../../reports/retained/quote-verification-migration/README.md)
found additional defects in those published artifacts. Its
[citation repair record](../../reports/retained/quote-verification-migration/analysis-repairs.json)
contains four Dynamic Cheatsheet result citations and eight Mem0 citations
(five result, three specialist) requiring disambiguation, with no Napkin
citations. These twelve citation occurrences are distinct from the two earlier
failed check attempts. The current pilot tests both authoring friction and
whether invalid quotations survive publication under the stronger checker.

The migration's [initial sweep](../../reports/retained/quote-verification-migration/analysis-sweep.json)
gives these denominators, counting the exact result once rather than counting
its identical local and retained copies twice:

| Previous pilot | Result quote blocks | Specialist quote blocks | Ambiguous blocks after publication |
|---|---:|---:|---:|
| Dynamic Cheatsheet | 29 | 16 | 4 |
| Mem0 | 41 | 21 | 8 |
| Napkin | 44 | 28 | 0 |
| Total | 114 | 65 | 12 |

The same systems and revisions make this a bounded comparison. Different
generated passages, analysis scope and stochastic execution prevent treating
three runs as a controlled estimate of an error-rate change. Matching proves
source occurrence, uniqueness and range containment; semantic support remains
a separate responsibility.

## Completion and audit

All three completed-run handoffs independently validate. The following counts
come from the shared parser on the final bytes and the six worker traces.
Source checks, publication and completed-run verification establish source
matching; the census itself only counts parsed blocks.

| Pilot | Result quotes | Specialist quotes | Failed source-check attempts | Quote ambiguities | Altered quote blocks | Out-of-bounds citation occurrences | Bare-URL attribution errors |
|---|---:|---:|---:|---:|---:|---:|---:|
| Dynamic Cheatsheet | 29 | 31 | 2 | 1 | 0 | 0 | 6 |
| Mem0 | 40 | 24 | 2 | 7 | 0 | 5 | 0 |
| Napkin | 44 | 31 | 1 | 0 | 1 | 3 | 0 |
| Total | 113 | 86 | 5 | 8 | 1 | 8 | 6 |

All listed diagnostics were resolved before publication. The eight range
diagnostics include two occurrences of the same Napkin range; they are not
eight distinct source spans. The six bare-URL errors arose in one command.
The copied-image-link failure occurred in that same Dynamic Cheatsheet check.
Mem0's separate comparison-schema rejection is outside the source-check count.
The compact Mem0 review contains two additional verified quote blocks; the
other two compact reviews contain none.

### Dynamic Cheatsheet

The specialist's first source check rejected one quotation appearing 32 times
in `results/AIME_2025/gpt-4o_DynamicCheatsheet_Cumulative.jsonl`. It extended
the excerpt with the `final_cheatsheet` field and pinned it to row 1. The next
check passed. It also tightened two notebook quotations during the same edit.
This is a caught authoring ambiguity, not evidence of a checker defect.

Specialist trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T15-39-02-01a0e317-309d-70b3-9169-2f6f4a73fe66.jsonl`.
Command-completion records: first source rejection at line 92, correction call
at line 104, passing verification at line 111. A later structural and source
check also passed after a report edit (line 126).

The coordinator's first result check rejected six bare-URL attributions and
one relative image link copied inside a quote. It wrapped the URLs in Markdown
links and removed the image line from the selected excerpt. The next source
check passed; a further check after finalizing the result also passed. Prepare,
publish and independently repeated handoff all succeeded.

The six URL diagnostics expose a remaining contract inconsistency. The
[producer skill](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md) and
[result type](../../types/agentic-system-analysis-result.md) say a full-commit
GitHub blob URL is sufficient. `quote_matching._attributed_citation` accepts
that URL, but `validation.validate_quote_citations` additionally requires a
Markdown link or code span. Its “names no source” diagnostic therefore rejects
a URL the shared parser has already resolved. Wrapping the URLs is an available
author-side repair; aligning the documented form and structural check remains
method work. This replay leaves both unchanged.

Coordinator trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T15-36-59-01a0e315-4fce-7b71-8c14-09e9af772ceb.jsonl`.
Rejection: line 324; correction call: 331; passing checks: 334 and 342.
The two traces contain 69 matched tool outputs (48 coordinator, 21 specialist),
with no unreturned calls or delegation failures. Six truncation markers occur
across four tool outputs: coordinator 14, 58 and 105 (three markers), specialist
18. Bounded source rereads followed at coordinator calls 62 and 117; method
and definition rereads appear at 20, 25 and 109. This was not a truncation-free
run; the audit does not claim every omitted instruction byte was reloaded.

The coordinator also returned a substantive scope question to the specialist:
temporary local execution context should not independently supply the
accumulated-memory read-back classification. The specialist amended the report
and reran source verification. This was semantic reconciliation, separate from
the quotation repairs.

Final result SHA-256:
`fe61854d8a9074abc2c1d2c9c4dad3eec781417384967f708b61d027c6825078`.
Final specialist report SHA-256:
`b5bb6019e509596e7746d0e588bfe72783ebdc7daa2d836083022ecbd487e603`.

### Mem0

The specialist's first structural check rejected an evidence map that did not
cover exactly the declared comparison values. After that repair, its first
source check rejected seven ambiguous quotations (one repeated four times,
six repeated twice) and three source citation ranges beyond EOF. It located
the quote occurrences and added ranges; it corrected the source citation
endpoints from 1075 to 1062 in `mem0/configs/prompts.py`, 190 to 173 in
`mem0/reranker/llm_reranker.py`, and 150 to 139 in `mem0/utils/scoring.py`.
The next source check passed.

The specialist had inspected those complete tails before drafting. The parent
independently reread all three corrected spans at the pinned commit: they
support the attached prompt-assembly and search/reranking mechanisms. The
three out-of-bounds diagnostics concern ordinary source citations, not quote
containment failures. Their endpoint repair alone would not prove support.

There is also residual instruction tension about these ordinary citations:
the producer skill makes Git line ranges optional navigation, while the result
type's local-anchor rule still asks for a full path and “one or more line
ranges.” Both permit quote disambiguation through a containing range. The
three failures show that optional quote locators have not eliminated ordinary
source-range mistakes; this audit does not establish that the wording tension
caused those mistakes.

Specialist trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T15-56-29-01a0e327-2a68-7c60-9d0e-c56967531d54.jsonl`.
Structural rejection: line 131; source rejection: 145; source-location search:
153; correction: 160; passing source check: 161.
Coordinator trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T15-54-34-01a0e325-68c7-72a2-b2ac-1b6efb2ba4cc.jsonl`.
Two `test -f` checks at lines 199 and 237 returned 1 while the report was not
yet available; these are availability probes, not analysis failures.

The coordinator's first result source check also rejected two ordinary citation
ranges: `mem0/configs/prompts.py:905-1069` and
`mem0/utils/entity_extraction.py:751-774`. It reread the pinned tails and
corrected the anchors to `905-944,970-1062` and `751-772`. The next check passed.
The parent reread the entity functions and checked the corrected use: they
support extraction and the empty-result fallback when the model is unavailable.
The prompt tail was already reread during the specialist audit. These checks
support the particular endpoint repairs, not a fresh semantic review of the
entire result.

Coordinator rejection: trace line 353; source reread call: 358; repair call:
365; successful verification: 367. Additional supporting quote blocks were
then added, and the final result passed 107 source checks (378). Prepare,
publish and independent handoff passed. The specialist's final report passed
63 source checks (specialist 191, independently repeated by coordinator 320).
The coordinator's progress message reported the final passing check; the full
trace reveals its earlier rejection. Audit conclusions use the trace.

The two traces contain 79 matched tool outputs (55 coordinator, 24 specialist),
with no unreturned calls or delegation failures. Seven truncation markers span
six outputs: coordinator 14, 137, 156 and 246; specialist 18 and 39 (two markers).
Coordinator bounded rereads appear at calls 20, 141, 160 and 250; source-specific
specialist reads followed its broad discovery output. Truncation remains a
separate operational limitation.

Final result SHA-256:
`7682f25dfbbe2c166a45217536f38219db73c73d0e705c22d186f77fed5c7217`.
Final specialist report SHA-256:
`0ce564fddd6e8d5131cfc5d081ff01136d097d0439ceb8ea8ed5e660823d8ff2`.

### Napkin

The specialist's first source check rejected one quote from
`bench/overview-exposure.ts`: it had omitted the leading `*` characters from
two code-comment lines. Restoring those characters made the quotation match.
The same check rejected three citation occurrences in `src/core/crud.ts`,
using two distinct ranges ending at 215 in a 198-line file. The specialist
reread the functions and corrected those citations to `134-198` or `176-198`.
The parent independently checked the file-move/delete functions and the comment
passage; the repairs preserve the attached findings.

Specialist trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T16-15-49-01a0e338-ddd6-7da2-ab3b-17f80cc42eef.jsonl`.
Rejection: line 151; pinned reread call: 156; correction call: 163; passing
source check: 165. The coordinator subsequently requested explicit searched
boundaries for two absence findings. The specialist recorded the searches,
including their no-match exit statuses, and the final report passed 90 source
checks at line 231. These two Git grep exits of 1 (217 and 218) are documented
negative-search results, not failed analysis operations.

Coordinator trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T16-14-02-01a0e337-3a1b-7a82-b55e-ce07e78e8dcc.jsonl`.
The integrated result passed its first source check at line 388 and the final
check at 397, each with 137 checks. Prepare, publish and independent handoff
passed. Three earlier `test -f` failures were report-availability probes.

The two traces contain 90 matched tool outputs (58 coordinator, 32 specialist),
with no unreturned calls or delegation failures. Five truncation markers span
five outputs: coordinator 14, 60 and 134; specialist 34 and 42. Later bounded
source reads include specialist calls 46, 51 and 60. The reports disclose
rereads, but this audit does not establish recovery of every omitted byte.

Final result SHA-256:
`f4cb51d4e840f86184231a96eaa839074719cfd77764a3ed2fc2844e1c1dff93`.
Final specialist report SHA-256:
`5aa2e9572c7ca0817b482bb9588ddc68788e76009126fb5c08d814e89d30b843`.

## Downstream checks and reproducibility

The existing matrix, table and statistics scripts completed against exactly
these three generated reviews. All three rows are code-grounded. Matrix result
and review hashes and all six statistics input hashes match the new files.
Only bounded cache outputs were written; public comparison outputs and prior
landscape syntheses remain historical relative to the new runs.

The three generated reviews, three retained results, bounded table and two
workshop Markdown files pass `commonplace-validate`: nine files, zero failures
and zero warnings. The inventory preserves all 166 rows and its three current
run pointers agree with the checked publications.

Cache root: `kb/reports/cache/agentic-memory-refresh/quote-rerun-20260927/`.
The explicit review arguments are:

```text
--review kb/agentic-systems/reviews/dynamic-cheatsheet.md
--review kb/agentic-systems/reviews/mem0.md
--review kb/agentic-systems/reviews/napkin.md
```

| Output | SHA-256 |
|---|---|
| `matrix.csv` | `116f5a84168efe041cccdab840255a5d66ff115da20ca7fd11260c4261fe7b3e` |
| `table.md` | `8cbc397eaa9e1d93f8f55cd7de708f8ad96945d35808a0faa1c68025ce602d07` |
| `statistics.txt` | `151831043e233b8fa1a78f585192ec6b2c51090fbd902a5a446da0acf5f187ea` |
| `quote-census.json` | `72faa5c2d7d89759accaf195ff17e9050b0ad066ec24dc5f15328c4ecfebf4b5` |

The cache also contains `trace-index.json`, with the six trace paths, hashes,
models, call/return counts and truncation locations. The 238 tool outputs all
match calls; no unreturned call, agent-list call or delegation failure was
found. All six workers used `gpt-6-astra`, as in the previous rerun. There are
18 truncation markers across 15 tool outputs, compared with twelve markers
across eleven outputs in the earlier rerun. This trial does not show reduced
read-delivery friction.

All 106 fingerprinted Python and method/type files have identical start/end
hashes; HEAD remained `4a97ad71`. The three consumer scripts also match that
commit. No source worktree, producer code, prior retained result, public
comparison output or synthesis was changed by this replay. No staging or
commit was performed. Inventory coverage remains three completed pilots,
159 pending legacy artifacts and four historical predecessors.

Parent audit commands are excluded from worker counts. The parent's `uv`
launcher first failed under sandbox confinement and succeeded after escalation.
Two CSV spot checks used incorrect column names before the final check used
the actual headers and verified all pins. A post-completion attempt to reuse
`verify-sources` for six artifacts was rejected because that command requires
a running state; no state was changed. Completed-run handoff verification is
the supported check and rechecks the result, review and specialist sources.
Parent instruction/search deliveries also included truncation; worker-trace
claims above use bounded inspections. These are parent audit limitations and
recoveries, not failures hidden inside the six analysis sessions.

Some inter-agent messages are encrypted in the traces. The audit follows tool
calls, diagnostics, corrections and final bytes; it is not a full plaintext
message audit or an independent semantic review of every analysed-system claim.

## Decision supported by this trial

The stronger checker successfully stopped the observed quotation and locator
defects before publication. The new final artifacts have no matching failures
under that checker. The trial does not establish fewer authoring mistakes:
there were five failed source-check attempts instead of the previous two,
under a stronger contract and with independently selected passages.

Before describing the authoring workflow as repaired, align the bare-URL
attribution guidance with structural validation and reconcile the optional
range rule with the result type's local-anchor wording. Repeated passages,
literal code-comment markers and ordinary citation endpoints still need care.
These are retained follow-up findings, not implementation changes made during
this fixed-method test. This replay completes the operator's three-pilot
comparison; it does not authorize or complete the remaining corpus refresh.

The subsequently commissioned [root-cause analysis](./source-check-root-causes.md)
traces these failures back through the drafting commands and required reading
paths. It adds the specialist uniqueness-rule delivery gap and distinguishes
artifact-validation failures from failures reached by the source matcher.
