# Three-pilot citation-generation rerun

The operator commissioned this test on 2026-09-27 through
[the fixed-pin handoff](./next-pilot-test.md). It evaluates actual authoring
with the citation generator, against the [previous quotation trial](./quote-rerun-20260927.md).
All three pilots completed guarded publication and independent handoff checks.
All six authors used the generator. The audit found no quotation or range
failure in their validation/publication attempts, and all 186 final quotation
blocks match returned citations unchanged. One prepare attempt failed on
workflow identity formatting and was corrected. These observations support
reduced quotation-authoring friction in this bounded replay, with the
configuration and evidence limitations below.

## Test boundary

Producer HEAD at startup: `5057c874e36fa1c3538cd56a1bb3d3cb4a059a26`, exactly
the commissioned revision. No intervening producer change needed resolution.
The initial working changes were outside producer code and instructions.
Startup state, source origins and commit objects, source-worktree status,
inventory bytes, and 291 code/method/contract/configuration hashes are retained
in `kb/reports/cache/agentic-memory-refresh/citation-generation-rerun-20260927/`.

Each pilot receives a fresh source-only coordinator and a fresh memory
specialist. Both use `gpt-6-astra`, requested explicitly to match the previous
trial. The coordinator runs the epistemic lens locally. Only one pilot and
its specialist run at a time; workers receive current method instructions,
source identity, fixed pin and disjoint output ownership. They receive no
previous analyses, findings or failure examples. The parent owns this audit
and bounded downstream checks. No producer repair, source-worktree change,
public comparison replacement, synthesis or Git commit is commissioned.

Configuration limitation: examination of the prior six traces after the first
pilot completed found `effort: high`; the fresh session default had already
launched Dynamic Cheatsheet and Mem0 at `medium`. The model is preserved but
reasoning effort is not. Napkin explicitly requested and used `high` once the
baseline configuration was known. This is a coordinator setup error and a
comparison confound, not a producer change. Earlier workers are not rerun or
silently replaced. The cache retains `baseline-worker-configuration.json`.

| System | Source pin | Run | Completion |
|---|---|---|---|
| Dynamic Cheatsheet | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | `AAS-2026-09-27-dynamic-cheatsheet-03` | Published; independent handoff passed |
| Mem0 | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | `AAS-2026-09-27-mem0-03` | Published; independent handoff passed |
| Napkin | `7582d6a46f5a11995956e60a59c41a5b242109f1` | `AAS-2026-09-27-napkin-04` | Published; independent handoff passed |

## Counts and comparison

The result census counts identical local/retained bytes once. Specialist
blocks count separately because their authorship is a separate operation;
unchanged copies into results are not independent generator requests.

| Pilot | Coordinator requests | Specialist requests | Result quotes | Specialist quotes | Compact-review quotes | Failed quotation/range attempts |
|---|---:|---:|---:|---:|---:|---:|
| Dynamic Cheatsheet | 16 | 16 | 29 | 16 | 1 | 0 |
| Mem0 | 19 | 32 | 49 | 31 | 0 | 0 |
| Napkin | 15 | 23 | 37 | 23 | 0 | 0 |
| Total | 50 | 71 | 115 | 70 | 1 | 0 |

All 121 generator requests succeeded. Four returned two candidates each;
the others returned one citation. There were no observed rejected requests,
absent-text lookup retries, requests above ten occurrences, malformed emitted
citations, manual citation construction or altered inserted blocks. Provenance
was established for all 186 final blocks using retained generator stdout and
the inspected generation/insertion code. Mem0's one successful reselection
is counted separately from rejected requests. Unselected candidates and
unused generated excerpts were not independently source-validated by this
audit; all final inserted candidates passed the regular publication checks.

Worker acceptance denominators are 19 explicit structural validations (six
early run states, seven results and six specialist reports), four prepare
attempts, three publishes and three completed-run handoffs. All structural
validations passed; one had three ordinary link warnings. One prepare failed
with three identity-field diagnostics. The successful prepare retry, all
publishes and all handoffs passed. Quotation/range diagnostics, affected
quotation passages and repeated quotation diagnostics are all zero within
this inspected evidence. No schema rejection or validator defect was
observed. Parent checks are excluded from these worker counts.

| Measure | Previous quotation trial | Citation-generation trial |
|---|---:|---:|
| Result / specialist / compact-review final blocks | 113 / 86 / 2 | 115 / 70 / 1 |
| Failed attempts with quotation or range diagnostics | 5 | 0 |
| Ambiguous quote-block diagnostics | 8 | 0 |
| Altered quote-block diagnostics | 1 | 0 |
| Out-of-bounds citation occurrences | 8 | 0 |
| Bare-URL attribution diagnostics | 6 | 0 |
| Copied-image-link diagnostics | 1 | 0 |
| New final publications passing their completion checks | 3 / 3 | 3 / 3 |

The previous categories overlap within attempts. Its five failures were
separate source-check operations; that operation no longer exists. The new
zero counts refer to the same defect categories wherever they reached
structural validation or publication, not to zero calls of a removed command.
Final block counts are coverage denominators, not the number of draft blocks
submitted across retries. The current four successful multiple-occurrence
selections are not ambiguous-block failures.

## Dynamic Cheatsheet evidence

Both workers loaded the citation instructions and each generated 16 citations
in one checked batch. Every invocation returned zero; neither batch needed
occurrence selection or a lookup retry. The batch code captured stdout and
stderr, rejected nonzero exits, and stored the returned citations in JSON.
The audit retained those JSON bytes and matched every final quotation block
against them, without reconstructing citations or rerunning source matching.
Successful generator stderr was captured but not printed by these batch
wrappers; the audit can establish successful exits and retained stdout, but
cannot establish that successful calls emitted no stderr. Failed-call stderr
would have been surfaced by the inspected wrapper code.
All 29 result blocks, 16 specialist blocks and one compact-review block match
a returned citation unchanged. The local and identical retained result count
once. Specialist quotations copied into the result retain those same bytes.

No quotation or range diagnostic reached structural validation or publication.
The first result validation passed with three warnings for relative links to
Commonplace definitions; the author corrected their paths, removed a repeated
quote and validated cleanly. These were not quotation failures. Prepare,
publish and both coordinator and independent parent handoffs passed.

Coordinator trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T18-08-09-01a0e39f-b3af-7860-8e51-17ed6cf1c327.jsonl`.
Generation call/result: lines 122/125; initial validation: 214/217; correction
and clean validation: 221/225; prepare: 229/233; publish and handoff: 239/243.
Specialist trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T18-09-49-01a0e3a1-3c5f-73b3-adda-03af0eed41a9.jsonl`.
Generation: 77/80; clean validations: 86/90 and 96/102.

The two traces have 44 matched call/return pairs, no unreturned calls and no
observed delegation failure. Actual trace models are `gpt-6-astra`, reasoning
effort `medium`. Five output events carry truncation markers: coordinator
14, 19 and 132; specialist 23 and 29. Subsequent bounded reads include source
spans and selected contracts, but this audit does not establish
that every omitted instruction byte was reloaded. The citation instructions
themselves are visible in the delivered outputs. Inter-agent message payloads
are encrypted; their full plaintext is outside the audit.

## Mem0 evidence

The specialist made 32 successful generator requests: 28 in its initial
batch, three additional selections, then a replacement of the proxy excerpt
with the more relevant call site. The replacement was an author selection
change after successful generation, not a rejected lookup. Four retained
requests returned two candidates each (`persist`, `rank`, `expire`, `boost`);
the report selected one occurrence from each. All 31 final report quotation
blocks match returned citation strings unchanged, including these four
disambiguated selections. This exercises candidate selection, which the
Dynamic Cheatsheet requests did not need.

Specialist trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T18-36-51-01a0e3b9-f9e8-7331-aaf9-57ad30abc85f.jsonl`.
Generation calls: 96, 150 and 162. Both structural validations passed cleanly
(outputs 183 and 199). No quotation failure or schema rejection was observed.
The search command returning 1 at output 64 ends in a `git grep` for graph
code with no match; it is a search result, not a quotation failure.
Successful generator stderr is not exposed by the batch wrapper.

The coordinator generated 19 citations in four checked batches (9, 6, 3 and
1 requests); all returned zero. Its wrappers printed both stdout and stderr.
All 49 final result quotations match returned citations unchanged, including
31 copied from the specialist. The compact review has no quotation blocks.
No request was rejected and none exceeded ten occurrences.

Coordinator trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T18-35-17-01a0e3b8-8d54-76b3-8192-dd2cd4e25fdf.jsonl`.
Generation calls: 132, 200, 247 and 291. Structural result validations passed
at outputs 355 and 363. The first prepare failed at 373 with three workflow
identity diagnostics: the run-state path, generated-review path and memory
report identity had trailing punctuation around code spans. The coordinator
removed that punctuation, rebound the result hash and passed validation and
prepare at 382. Publish and handoff passed at 390; the parent independently
repeated the handoff successfully. These are three identity-field diagnostics
in one failed prepare, not quotation/range failures or generator defects.

An earlier assembly script failed because a YAML date was not JSON serializable
(333); the coordinator converted date values before retrying. A report-existence
probe returned 1 at 227 while the specialist was working. Neither is a source
or schema rejection. No producer code was changed for recovery.

The two traces have 80 matched call/return pairs, no unreturned calls and no
observed delegation failure. Both actual models are `gpt-6-astra`, effort
`medium`. Seven output events contain truncation markers: coordinator 15, 59,
78 and 172; specialist 14, 24 and 43. Later bounded reads are visible, but
recovery of every omitted instruction/source byte is not established. The
citation instructions and the generator invocation/candidate-selection code
are inspectable. Full inter-agent plaintext remains an audit gap.

## Napkin evidence

The coordinator generated 15 citations in two batches (11 and 4); the
specialist generated 23 (22 plus one additional selection). All requests
returned zero and one citation each. All 37 result and 23 specialist blocks
match the retained generated strings unchanged; the compact review contains
none. The result includes the specialist's generated quotations without
alteration. No lookup, occurrence-selection, quotation, range or schema failure
was observed. Both report validations and both result validations passed
cleanly, followed by successful prepare, publish and handoff. The parent
independently repeated the handoff successfully.

Coordinator trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T18-52-54-01a0e3c8-ab78-7330-96d9-211dfa89c020.jsonl`.
Generator batches: call 128 and call 171; result validations: 259 and 267;
prepare: 275/279; publish: 285/288; handoff: 290. Two report-availability probes
returned 1 (182 and 206); neither was an acceptance failure.
Specialist trace:
`/home/zby/.codex/sessions/2026/09/27/rollout-2026-09-27T18-54-42-01a0e3ca-5050-7ac3-92df-5d2e6dd2048a.jsonl`.
Generation: 110 and 137; clean report validations: 149/153 and 162/167.

The two traces have 54 matched call/return pairs, no unreturned calls and no
observed delegation failure. Both actual models are `gpt-6-astra`, effort
`high`. Five output events carry truncation markers: coordinator 19, 97 and
158; specialist 19 and 44. Narrower reads followed the broad instruction and
source deliveries; complete recovery of every omitted byte is not established.
Coordinator generator wrappers printed stdout and stderr; the specialist
retained stdout and exposed stderr only on failure. Citation instructions
are visible in both traces.

## Audit coverage and downstream acceptance

The cache's `trace-index.json` retains all six trace paths, SHA-256 hashes,
actual models and effort, paired calls/returns, nested command exits,
nonzero diagnostics, instruction-delivery evidence and truncation locations.
There are 178 matched call/return pairs, no unreturned calls, no agent-list
calls and no observed delegation failures. Truncation affected 17 output
events, compared with 15 in the previous trial's 238 outputs. Citation
generation did not eliminate read-delivery friction. Encrypted inter-agent
messages and unprinted successful generator stderr remain audit gaps, not
evidence of zero issues in those channels.

`quote-census.json` records every final block's location, citation digest and
matching returned candidate. Generator-output captures are retained alongside
it. The audit compares returned bytes; it does not implement another source
matcher, infer semantic support from text equality, or independently review
every substantive system claim. Citation validity at publication is established
by the shipped validator and completed-run checks.

The existing matrix, table and statistics scripts ran successfully with exactly
these review arguments:

```text
--review kb/agentic-systems/reviews/dynamic-cheatsheet.md
--review kb/agentic-systems/reviews/mem0.md
--review kb/agentic-systems/reviews/napkin.md
```

All three matrix rows are code-grounded and name the commissioned new runs
and pins. Every matrix review/result hash matches current bytes; the table
contains those same six hashes, and statistics names exactly those six inputs.
`consumer-commands.json` retains commands and exit/output evidence;
`consumer-verification.json` retains the identity and hash checks.
Final scoped `commonplace-validate` checks passed for the three reviews,
three retained results, bounded table, this report and workshop README:
nine files, zero failures and zero warnings. The report was revalidated after
adding this completion record. `final-validation.json` retains command output.
Only the three commissioned inventory rows changed. The other 163 rows retain
their original bytes; all 166 rows remain. Inventory coverage remains three
completed pilots, 159 pending current artifacts and four historical
predecessors. Public comparison outputs and previous syntheses remain
historical relative to these new analyses.

Producer HEAD remained `5057c874e36fa1c3538cd56a1bb3d3cb4a059a26` at completion.
All 291 fingerprinted files have identical start/end hashes. The SHA-256 of
the sorted, compact JSON path-to-hash mapping is identical at both boundaries:
`82e9f77a1dd99788a2d6d765736c640a325703e531cb14f31c64a6815b2d91e7`.
`start.json` and `end.json` retain the full maps and working-tree status.
Source-worktree HEADs and status also match startup. No producer or instruction
repair, source-worktree change, staging or Git commit occurred.

| Cache output | SHA-256 |
|---|---|
| `matrix.csv` | `18bc3a70e907ce520c1e22d2d2fb4111a5dfdc7de4f03159b8f5f2ff2a8e55f6` |
| `table.md` | `1e69e333db813d8f10499b66c7be065cc73021a1860f4b1bdd945b019e5c727f` |
| `statistics.txt` | `6b1a3826f8e8297ca662bff566b44d6846daf1eeddb51f64da22740ef0d6fcd0` |
| `quote-census.json` | `08fce77f30a663c795418f8d95f75e1bcf338f071295bb0aec5230e4ccb33111` |
| `trace-index.json` | `01bd388a13ba58a5127d18aacc3ea05a97db5591e3504a7e022ba350bc2c431b` |

| Exact result | SHA-256 |
|---|---|
| Dynamic Cheatsheet | `7a8ebe9a5316b00937ba088177b0dd4890fff697c1bc2700342331095f967d57` |
| Mem0 | `c018cb9aad519e006e5ccb4ed7e9f457372bed5dc0c1e993046668982b7aaefa` |
| Napkin | `db2d565c46c319a1ecce235c0e12b167acc646d2567848f0170be7769a73360b` |

## Conclusions within this test

**Did authors use the generator?** Yes: all six loaded its instructions and
used it; all final quotation blocks have unchanged returned-candidate
provenance, including specialist-to-result copies.

**Did it emit valid citations?** No malformed emission was observed, and all
inserted final citations passed publication. The unselected candidates and
unused outputs were not independently checked here. The more-than-ten
occurrence rejection path was not exercised.

**Did authoring friction decrease?** Observed quotation/range failures fell
from five failed attempts to zero, across the stated final-block denominators.
Four repeated-passage selections were resolved through returned candidates
without a validation rejection. Ordinary link warnings, one assembly error,
one identity-format prepare failure and read truncation still occurred. The
different reasoning effort in four workers, stochastic source/excerpt choices,
and fewer specialist quotations prevent a controlled causal or general
error-rate claim. This trial did not measure time or cost savings.

**Did invalid quotations survive publication?** None were detected by the
regular validator and independently repeated completion checks in the three
new publications. That is bounded source-matching evidence, not a guarantee
of semantic support or a general zero-error rate.

## Parent execution limitations

The initial `python3` attempts to inspect the three consumer scripts' help
failed because that interpreter lacked the installed Commonplace package.
The prescribed `uv run python` attempts then hit the sandbox's snap confinement
error. Escalated help calls succeeded. These are parent setup failures, not
worker quotation failures. Some broad parent reads also truncated; audit
claims use targeted inspection of the raw traces and retained artifacts.
The first final-validation invocation incorrectly supplied several targets to
a single-target CLI and was rejected with exit 2 before validation. Separate
per-file invocations then passed. Two parent report-edit patches failed to
match their requested context and were reapplied against the actual text;
neither changed worker artifacts or producer behavior.
