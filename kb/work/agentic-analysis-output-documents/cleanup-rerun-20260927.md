# Cleanup regression, 2026-09-27

Execution of [the commissioned cleanup regression](./cleanup-rerun-test.md).
All three analyses validated and published at the fixed source pins, and the
bounded consumers passed. The trial does not establish preserved completeness:
two profiles drop baseline-supported classifications, and the selected scope
is narrower in Dynamic Cheatsheet and especially Mem0. No worker was stopped
by a missing type-pointer requirement. Loading still produced eight truncated
output events, and discarded exit statuses limit the Napkin trace audit.

## Fixed boundary and provenance

The trial starts at HEAD `70ce51e92be4361e8bbce73f2fcab49ca60d5d84`. Existing uncommitted work is preserved.
The parent retains startup status, baseline artifact digests, checkout origins,
source status and producer/schema hashes under
`kb/reports/cache/agentic-analysis-output-documents/cleanup-20260927/`.
The three sources are read at their fixed commits without changing worktrees.
The parent owns scheduling, the post-freeze comparison, and this report.
Fresh workers receive only current doctrine, method, source and output ownership.
They do not receive baseline analyses or workshop findings.

| System | Fixed commit | Baseline run | New run | Requested worker configuration |
|---|---|---|---|---|
| Dynamic Cheatsheet | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | `AAS-2026-09-27-dynamic-cheatsheet-03` | `AAS-2026-09-27-dynamic-cheatsheet-04` | `gpt-6-astra`, medium |
| Mem0 | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | `AAS-2026-09-27-mem0-03` | `AAS-2026-09-27-mem0-04` | `gpt-6-astra`, medium |
| Napkin | `7582d6a46f5a11995956e60a59c41a5b242109f1` | `AAS-2026-09-27-napkin-04` | `AAS-2026-09-27-napkin-05` | `gpt-6-astra`, high |

Requested model and effort match the baseline's actual configurations. Actual
new configurations will be checked in all six worker traces. The skill's
`model: opus` metadata is not the available runtime identity; the commission
explicitly requests the available baseline worker model.

## Governing file hashes

| File | SHA-256 at start | End check |
|---|---|---|
| `kb/instructions/analyse-agentic-system/SKILL.md` | `a0d4d795649445b4b4221e1c0c3187864f86ef69bd702d94551de5625dbc748b` | Identical |
| `kb/instructions/analyse-external-system-epistemic-architecture.md` | `e16916806f997b39f03395cc58d6f816c8179c6df19834dd3cb300c124978d17` | Identical |
| `kb/instructions/analyse-agentic-system/jobs/memory.md` | `2548e5d5c37106c075a6f29bfc9dcc734f76d0e2e13a97ebd4cdddbc6486db42` | Identical |
| `kb/types/agentic-system-analysis-result.md` | `644e1afdb3711c45ac7d8548dfd90a1723ecae9e95b6bbef4d236c73725590ba` | Identical |
| `kb/types/agent-memory-analysis-report.md` | `646eb26b712752e2a1477094e20f261a25a7f1f6201e3d3bd2d8f1f5a3711857` | Identical |

## Run outcomes

All three completed-run handoffs passed independently with exit 0 and empty
stderr. Publication validated each complete bundle: run state, exact result,
memory input/report and generated review. State and retained result bytes
agree. Each report has its required sections; each epistemic output carries
the six blocks in order. All three memory profiles match their specialist
profiles after declared canonical-ID mapping, and all 78 specialist quote
blocks are preserved unchanged. These checks establish bundle integrity and
structural validity, not exhaustive semantic correctness.

| System | Published exact result SHA-256 | Specialist report SHA-256 |
|---|---|---|
| dynamic-cheatsheet | `18a90d3619d9357c200ad80b41ade5b654875d9a7ca0b7b1c5203581a17ef5a4` | `39be455f397ecf0998172d975808de78a7815e12408c9117948ef64c77da55ae` |
| mem0 | `7144b0d8a19d74d7722c7986648a23b7a5977287962a863d7d0d3cdcefb89ca2` | `6812d1e3a042bb36a6fa21bb1f6eb23d29448866f3d65e6ae432d4231a55172c` |
| napkin | `548c7be0916b0d9985a139877b699736e3ac2f699a2ceb291e7e1792d525e1b0` | `64a2c3318cf344578973dc23bacd36bae167cef2fab461211e6218ad398ad0cb` |


## Trace and loading audit

The audit pairs all 241 visible tool calls with returns, parses delivered
nested shell results, scans diagnostics, and follows the material failures,
loading omissions and corrections in the raw traces. It reads completed
artifacts and compares their declared scope, records, profiles and claims.
This is targeted semantic comparison, not independent reconstruction of every
system claim. It found no agent-list call, exposed prior-analysis read or
launch/communication failure in visible tool activity. Encrypted handoff text
is not independently inspectable. Each fresh runtime also supplied the root
AGENTS.md doctrine before the worker's explicit read.

Nine visible nonzero shell returns comprise six expected absent-report polls
and three recovered failures: Mem0 quote ambiguity, Mem0's placeholder-check
false positive, and Napkin's unquoted evidence key. No failed final acceptance
check remains. All three runs required one specialist correction round; none
required a new worker or run ID. Some command sequences expose only their last
status; Napkin additionally has 21 output-only deliveries. Successful quote
subprocess stderr is sometimes discarded. These are audit limitations and
failures to retain diagnostics, not proof of zero intermediate issues.

## Comparison with the baseline

Comparison began only after the corresponding new result and public candidate
were frozen and published; none of it was supplied to analysis workers.
Counts below measure record granularity, not completeness. Detailed findings
follow for each system. Baseline run directories and retained bytes remain
unchanged. Every profile axis is compared in the tables at the end; order
within a value set is ignored.

## Downstream checks

The existing `scripts/build_systems_matrix.py`, `scripts/render_systems_table.py`
and `scripts/analyze_matrix.py` all returned 0 with empty stderr, using only:

```text
--review kb/agentic-systems/reviews/dynamic-cheatsheet.md
--review kb/agentic-systems/reviews/mem0.md
--review kb/agentic-systems/reviews/napkin.md
```

Matrix and table outputs are in the fresh trial cache; statistics stdout is
`statistics.txt`. All three rows are code-grounded. Independent checks match
each row's new run ID, retained-result digest and review digest; the table
contains those same identities/digests. All six statistics input digests match
the consumed review/result bytes. No old result was substituted. Consumer
success does not catch the semantic profile omissions recorded below.

| Cache output | SHA-256 |
|---|---|
| `matrix.csv` | `8b240037fb1fe8faec09c68a224b289952a4a9e54bab81516526a0c920b65a04` |
| `table.md` | `10eabd12c0a8a72d61f5bafbf2ad9a477744e6d37e7b8c32fc8335e977f10194` |
| `statistics.txt` | `51f4081dc11d118527a5239ee4687fd7cbcd412b93ba3638d228209865b928b8` |

The public comparison corpus was not rebuilt and is stale relative to the new
reviews. Legacy memory tables and previous landscape synthesis remain
historical. No transfer scan or larger corpus refresh was started.

## Acceptance answers and limits

1. **Did a worker meet a gap?** No missing type field, dangling method pointer
   or unavailable requirement stopped a worker in the inspected evidence.
   Correctable authoring, classification and loading problems occurred.
   The lost classifications still have requirements in the loaded contracts;
   they are not evidence of deleted rules. Encrypted messages prevent a claim
   about every off-band question.
2. **Did every produced document validate and publish?** Yes for all three
   skill-owned completed bundles; their independent handoffs pass. Reports
   remain local provenance and exact results/public reviews were published.
   Workshop/cache Markdown validation is recorded below. Validation did not
   detect the semantic omissions.
3. **Did completeness hold against the baseline?** Not fully. Dynamic
   Cheatsheet drops other-compiled lineage despite retaining its witness;
   Napkin drops the separate afforded promotion into always-loaded context.
   Napkin also loses the alternate Base item creation path. Scope narrowing
   removes additional baseline coverage, especially Mem0's server/plugins.
   Other changes add evidence or refine distinctions. The trial cannot
   attribute these stochastic choices and omissions specifically to cleanup.
4. **Did loading/truncation change?** Eight truncated output events in 241
   returns, versus 17 in 178 returns for the immediate baseline. The earlier
   reliability audit recorded 12 truncated deliveries across 11 output events
   in 222 returns. Main types/lenses still required bounded rereads. Fewer
   truncated events do not establish lower total effort or complete recovery;
   all three specialist corrections and the missing-status gaps remain.

The five governing files have identical start/end hashes. Producer/schema and
consumer-script hashes, three source worktree statuses and prior run-file
hashes are also unchanged. HEAD advanced from the startup value to
`e53525467cf8c243cc6bff280c01b1bf4e12fde4` through six concurrent commits outside
this trial, affecting eleven other files. They concern link vocabulary,
collection relation guidance, reference links and another workshop; their
identities and paths are retained in `end.json`. None changed the five files,
producer code or source pins. This trial made no Git commit. The parent first
used an overly strict unchanged-HEAD assertion; it failed, then the parent
inspected and recorded the concurrent changes instead of concealing them.

Parent read deliveries also occasionally truncated; narrower reads recovered
the passages used for findings. Parent calls are excluded from worker effort
counts. Three stochastic runs, different analytical scopes, new source
selections, concurrent repository work and incomplete diagnostic visibility
prevent a general causal claim about cleanup. The trial neither repairs the
method nor starts partition design, an extra rerun, public comparison rebuild
or the remaining corpus refresh.

## Dynamic Cheatsheet: completed comparison

The new run published and the parent independently passed
`commonplace-agentic-analysis-handoff` (exit 0, empty stderr). The report has
all eight required sections, and its fourteen-axis profile is identical to
the result after the five declared proposal-ID mappings. The epistemic
section carries the six blocks in order. It uses `implemented` as an
architectural status and treats candidate transformations as indeterminate;
no architectural or candidate state was translated into a conclusion status
in the inspected section.

Record counts (baseline → new): SRC 1 → 4, CMP 2 → 2, OBJ 11 → 6,
RTE 10 → 7, CLM 3 → 5, ABS 1 → 1, BAP 4 → 4. Quote anchors 29 → 31;
limitation rows 6 → 6; whitespace-separated words 10,614 → 12,593.
The source increase separates implementation, doctrine, historical observation
and reported operation. The new historical evidence is the first two pinned
AIME result rows: target-inconsistent guidance is retained and appears in the
next prompt. Its producing revision remains unknown; the result does not
upgrade current implementation to observed deployment or claim causal effect.

The smaller object/route inventory partly groups existing coverage: current
question/target, prompt guidance, local feedback and checkpoint details now
sit on routes rather than separate objects, while full-history and retrieval
share a selection route. The retrieval-synthesis sheet is split as its own
object. Two baseline findings are outside the new scope: the separate
provider-client chat/history route (baseline RTE-10 and OBJ-11), including
manual `set_history`, and the opaque native-container memory surface (baseline
OBJ-6/RTE-3). The new runtime still describes provider execution dispatch,
but not its memory profile. These are stochastic boundary choices under the
unchanged method, not evidence that the cleanup removed their requirement.
They prevent a claim of equal breadth. Unchanged component/absence/authority
counts do not mean identical record boundaries: generator and curator advisory
paths are split where the baseline instead separated static-template force.
The additional claim records split curator promises and a faithfulness limit.

The baseline's mostly partial profile becomes mostly known under the narrower
scope. Service-object storage, authored lineage and manual writing disappear
with the excluded routes. Natural-language and symbolic existence become
observed from historical content, with current-production provenance limits.
Curation keeps wired evolve, but changes synthesize/dedup/promote from afforded
to claimed and removes consolidate. The new explanation uses the controlled
semantic definitions: replacement does not establish novel claims, successful
deduplication, count-based priority, or reduction without new claims. These
are source-bounded changes in judgment, not established losses of instruction.

There is also a substantive profile omission. Baseline `other-compiled`
lineage covered mechanically formatted prior pairs. New RTE-3 still says
that source pairs and returned context strings persist in benchmark JSONL,
but its known lineage set contains only imported and trace-extracted. The
parent checked the pinned `dynamic_cheatsheet/language_model.py` full-history
branch (460–501) and `run_benchmark.py` persistence (272–280, 303–315):
formatted prior pairs become `final_cheatsheet`, are recorded, and are saved.
This is not explained by the stated scope narrowing. The finding survives
in prose but is missing from the normalized profile; structural validation
and publication did not detect it. Completeness therefore does not fully hold
for this pilot. This audit records the defect without altering the frozen
analysis or starting an uncommissioned fourth analysis. The cleaned result
type still says “Lineage covers their derivation paths” in Memory comparison
fields, and step 7 requires “scope agreement with the canonical records.”
Both remain available and were loaded. This is an integration/classification
omission, not an observed gap where a type pointer lacks its requirement.

One specialist correction round revised the synthesis basis, the strongest
symbolic-content witness, absence-search detail and row-two delivery anchors.
The integrated per-value evidence preserves the corrected specialist profile.
All observed validation/publication commands passed. The coordinator's one
nonzero command was an expected `test -f` poll before the report existed,
not a failed analysis check.

The coordinator trace has 53 matched tool calls/returns; the specialist has
20. Neither has an unreturned call. Actual model/effort is gpt-6-astra/medium
in both, matching the baseline. Their trace paths, hashes, complete visible
deliveries and byte counts are retained in `dynamic-coordinator-audit.json`
and `dynamic-specialist-audit.json` in the trial cache. Two deliveries were
truncated: coordinator trace line 14 and specialist line 24. The coordinator
recovered the missing skill prefix in output line 20; the specialist reread
source spans in output 35. All result-type sections and the epistemic
instruction arrived before coordinator source findings. The specialist
received Memory comparison fields, Status fields and Source register in
output 24, whose omission was later source code, and Canonical identity in
output 72. Neither worker visibly loaded the command reference; CLI help and
the instruction's command forms supplied the operational syntax. No request
for missing instruction content, invented controlled value or dangling type
pointer was observed. The first combined coordinator read also omitted part
of AGENTS.md, but trace message 6 independently supplies the full repository
doctrine through the runtime, so that omission is not a doctrine-loading gap.

Successful quote subprocesses checked return status but captured and discarded
stderr. Their possible successful-command warnings are inaccessible to this
audit. Inter-agent message arguments are encrypted in the raw traces; the
result's Reconciliation and specialist report preserve the substantive
correction, but this is not a complete plaintext message audit.

## Mem0: completed comparison

The new run published; the parent's independent handoff passed with exit 0
and empty stderr. The specialist report has all eight required sections.
The integrated fourteen-axis profile is identical after the thirteen declared
proposal mappings. The epistemic section contains all six blocks in order,
uses implemented/doctrine-only architectural states, and keeps indeterminate
transformations separate from candidate observation. No translation into
conclusion-status values was observed in this section.

Counts (baseline → new): SRC 1 → 3, CMP 4 → 5, OBJ 7 → 9,
RTE 12 → 8, CLM 4 → 3, ABS 1 → 1, BAP 6 → 3; quotes 49 → 34;
limitation rows 8 → 6; words 11,806 → 14,862. Source rows now separate
implementation, doctrine and reported operation. The extra component records
the persistence/dependency assembly, not an additional independent model.
Object count includes a superseded aggregate retained to preserve canonical
identity; raw and extracted payloads, recent messages, mutation history,
access structures, procedural summaries and transient vision text are split.
Fewer records or quotes therefore do not directly measure reduced coverage.

Coverage is nevertheless materially narrower. The baseline covers the Python
library, HTTP service and representative shared host integrations, with
partially inspected alternatives. The new result explicitly chooses
`subsystem-only`: synchronous Python OSS Memory. It excludes AsyncMemory,
server, CLI, JS, hosted/platform and external runtime implementations. Missing
baseline findings include server authentication versus caller identity,
administrative configuration replacement and persistence limits, generated
instruction proposals, deployment/package drift, hook trace capture and staged
spooling, first-prompt coding-agent supply, requested MCP recall, and the proxy
completion injection route with incompatible calls. The baseline's bounded
absence of a graph route is replaced by the narrower ADD-only absence finding.
These are deliberate boundary/selection differences permitted by the current
skill; the trial did not freeze functional scope alongside the source pin.
There is no evidence that the cleanup removed a requirement for those fields,
but equal breadth against the baseline is not established.

Within the synchronous subsystem, the new result gives more explicit treatment
to distinct raw/extracted payloads, vision preprocessing and incomplete
withdrawal: public search expiration does not establish exclusion from direct
get or internal extraction context. The ADD-only implementation versus the
add docstring, procedural summaries, entity ranking and the distinction between
storage admission and factual acceptance remain. These are source-supported
retentions and refinements. The six new limitation rows emphasize static
operation, optional providers, opaque semantics and withdrawal; the baseline's
server configuration, deployment and isolation limitations disappear with
those excluded routes.

Profile changes follow the narrower scope: files/service-object storage,
event-stream trace source, per-project learning scope and staged timing are
lost with plugin/hosted routes. Automatic/manual writing and pull/push become
known within the API boundary; manual writing, authored lineage and external
pull use afforded rather than wired witnesses. The positive trace-learning
classification becomes known from one wired existential trace-to-consumer
chain; this does not strengthen activation or learning-as-improved-capacity.
Curation values remain dedup/evolve/invalidate/decay, with their per-value
bases preserved. Faithfulness changes from uninspected to not-determinable:
neither run inspected an intervention establishing dependence on recall.
That is a difference in uncertainty classification, not new execution evidence.

One specialist correction round split the raw/extracted aggregate without
reassigning its canonical ID and expanded source-path anchors. Its profile
and evidence were integrated without change after mapping. No missing method
pointer or invented controlled value was reported or found in the inspected
material.

The coordinator trace has 55 matched calls/returns; the specialist has 27.
Both actual configurations are gpt-6-astra/medium, matching the baseline.
Neither has an unreturned call. Two deliveries were truncated: coordinator
output 14 (combined doctrine/skill) and specialist output 19 (report type,
result type and ancillary reads). The coordinator recovered the skill prefix
in output 20 and reread later steps in 170. Its result type and epistemic
instruction arrived in outputs 30/36/42 before source findings. The specialist
initially received Memory comparison and Canonical identity, recovered Source
register in output 24, and recovered the remaining Status fields in output
149, after the first report draft. Thus all four sections were received before
the final report, but not all before initial analysis. The late read followed
the coordinator's source-path correction request. The type pointer had the
content; oversized loading had omitted it. Neither worker visibly read the
command reference; both used available command forms/help.

There were two recovered command failures, separately from two expected
missing-report polls. Specialist output 103 rejected a quote-generator response
containing two valid occurrences (sync and async expiry code), although the
quote command itself returned 0. Output 110 selects the emitted synchronous
occurrence unchanged, then the report validates. Coordinator output 352 fails
a broad placeholder assertion after writing the integrated draft: the pattern
also matches the quoted source identifier `MEMORY_SYSTEM`. Output 361 checks
actual whole-line placeholders and validates; later exact-result validation,
prepare, publish and handoff pass. This is a checker false positive, not an
unresolved placeholder. The follow-up shell combines a negative grep and
validation with a semicolon, so only the final command's status is exposed;
the audit treats the grep's expected no-match separately, not as a second
independent passing command.

As for Dynamic Cheatsheet, successful quote subprocess stderr is not retained
by the wrappers, and raw inter-agent message text is encrypted. The two
`mem0-*-audit.json` cache files retain visible deliveries, nested statuses,
trace identities and byte counts. No unresolved visible execution failure
was found; that claim does not cover inaccessible stderr or messages.

## Napkin: completed comparison

The new run published and the parent independently passed its handoff (exit 0,
empty stderr). All eight specialist report sections and all six epistemic
blocks are present. The profile is identical after the eleven declared
proposal mappings, and all 35 specialist quote blocks occur unchanged in the
result. The explicit generalization lifecycle uses architectural values such
as doctrine only and not determinable independently of the observed candidate
state no instance observed. Neither field is translated into a conclusion
status; instructions and link checks do not become observed acceptance.

Counts (baseline → new): SRC 1 → 3, CMP 3 → 2, OBJ 10 → 13,
RTE 10 → 13, CLM 2 → 3, ABS 0 → 2, BAP 5 → 4; quotes 37 → 43;
limitation rows 6 → 7; words 10,668 → 14,770. Source rows separate code,
doctrine and reports. The component inventory groups external model roles
rather than separately counting the skill interpreter/package; it adds the
search dependency's boundary explicitly. The object total includes one
superseded auxiliary aggregate and splits canvas, bookmarks, persisted base
views and transient SQLite rows. Link diagnostics and inferred generalization
receive separate objects. Answering and scoring split, and documented pinned
supply, link checking and auxiliary mutations receive distinct routes. The
additional claim and absences qualify design labels, the missing extension
and absent retained dependence evidence. Behavioral paths are grouped
differently, with no separate tend/template authority path. These are record
and inspection choices rather than changes in source.

The overall whole-system responsibility remains similar, but the new memory
scope includes benchmark imports and a documented host pinned-context
convention that the baseline excluded. This adds imported lineage and afforded
push/coarse supply. The host remains outside implementation evidence; no wired
push is asserted. Pull changes from afforded named external use to a wired
CLI/SDK requested-return witness. Permanent deletion now supplies wired decay,
explicitly meaning forgetting rather than age-based decay. These are
source-supported scope/judgment changes, not new source behavior.

Timing changes from afforded online/offline to afforded staged for the same
skill's current-session, requested and session-end triggers. The new account
calls extraction a separate review/write stage; it does not observe a new
scheduler. This is a stochastic categorization difference under these
instructions, not new execution evidence resolving the timing taxonomy.
Storage, form, behavioral authority, write agency, trace-learning, trace
source, learning horizon and distilled form keep their value sets (order
changes do not count as differences). Faithfulness remains not-determinable.

Two baseline findings are missing or weakened. First, baseline RTE-9 records
`createBaseItem` writing directly without the ordinary create-file collision
guard. The parent rechecked pinned `src/core/bases.ts` (77–93): it calls
writeFileSync directly. The new RTE-12 covers requested Base queries but does
not retain that mutation alternative; its createFile guarantee is correctly
scoped to that primitive, yet the alternate-path finding is lost. The current
skill still says in step 4.2, “Enumerate materially equivalent alternate paths
before judging a guarantee.” No pointer gap explains this omission. Editable
templates/folder descriptions and their variable-substitution contrast are
also no longer separately retained as accumulated memory; static scaffold
content is treated as configuration. That is a narrower analytical treatment
than baseline OBJ-8, not a change to the type contract.

Second, the new known curation set omits promote. Its rationale excludes the
design-only access-count promotion mechanism, but baseline promote was a
different witness: distill moves fundamental project findings into NAPKIN.md.
The new result itself retains that source quote on RTE-3 and includes the
always-loaded convention on RTE-11. The parent reread the pinned distill skill,
including its Step 5 direction to update the always-loaded context note. The
current result type defines promote as raising tier or salience. Excluding
access-count promotion therefore does not dispose the separate afforded
salience-raising route already within this profile's scope. This is a second
baseline-supported classification missing from a claimed complete profile.
It survives in prose but is lost to normalized consumers. The report records
it without changing the frozen result or expanding the trial. The existing
contract still supplies the requirement, so the omission cannot be attributed
to a removed cleanup rule.

One specialist correction round split auxiliary objects and added their
mutation route; the same specialist retained ownership and input bytes.
Before that round, its initial validator caught an unquoted YAML yes key in
the trace-learning evidence map (output 151). Output 159 quotes the key and
passes; later corrected-report validations pass too. This is an authoring
error against the loaded rule “quote `"yes"` and `"no"` in YAML so they
remain strings,” not a missing type field. All final acceptance commands and
the independent handoff passed. Three coordinator nonzero commands were
expected missing-report polls, not analysis failures.

The coordinator has 61 matched calls/returns and the specialist 25; none are
unreturned. Both actual configurations are gpt-6-astra/high, matching the
baseline. Four output events were truncated: coordinator 15, specialist
20, 40 and 48. Coordinator output 25 recovers the missing skill prefix;
outputs 31/36/42 deliver the result type and epistemic instruction before
source findings. Specialist output 28 recovers the four required result-type
sections before source analysis. Output 48 rereads tend and 53 recovers selected
overview/search/CRUD spans; later 61/70 provide bounded benchmark reads.
The broad grep listing truncated in output 48 was not fully redelivered, so
this audit does not assert recovery of every omitted discovery line. Neither
worker visibly loaded the command reference; help and supplied command forms
were used. No missing method pointer or invented controlled value was observed.

A distinct observability failure remains: 21 coordinator deliveries print
shell output alone and omit at least one exit status (trace outputs 25, 31,
36, 42, 61, 69, 139, 148, 158, 166, 200, 236, 285, 290, 333, 338, 343,
368, 410, 416 and 431). The skill's Failure rule says to “retain status and
stderr as well as stdout.” The .output field carries combined visible output,
but cannot establish the discarded status. Final result validation, prepare,
publish and handoff do retain successful statuses; the independent handoff
also passes. Earlier missing statuses remain audit gaps, not inferred zeros.
Some successful quote subprocess stderr and encrypted message contents remain
inaccessible as in the earlier pilots. No method file was repaired during
the trial.

## Effort beside the earlier trials

Each cell reports tool-return events, not model turns or individual shell
subcommands. The reliability audit's truncation column retains both units
because one event contained two truncated reads. Reconciliation counts mean
substantive specialist correction rounds, separate from deterministic repairs.

| System | Immediate baseline returns / truncated events | New returns / truncated events | Reliability returns / truncated deliveries (events) |
|---|---|---|---|
| Dynamic Cheatsheet | 44 / 5 | 73 / 2 | 66 / 7 (6) |
| Mem0 | 80 / 7 | 82 / 2 | 77 / 3 (3) |
| Napkin | 54 / 5 | 86 / 4 | 79 / 2 (2) |
| Total | 178 / 17 | 241 / 8 | 222 / 12 (11) |

The immediate baseline recorded two recovered Mem0 failures (assembly and
prepare), with report-existence/empty-search probes separately excluded. The
reliability audit recorded three recovered failures and one Python escape
warning. This trial records three recovered failures and no additional
visible runtime-warning diagnostic, within the visibility limits above.
All three new pilots have one specialist correction round; the reliability
audit explicitly recorded one Napkin request to expand absence searches.
Thus lower truncation coexists with more calls and reconciliation. Baseline
source/record scopes and output sizes differ, so these are measured costs,
not an isolated estimate of the cleanup's effect.

## Trace identities

All six raw files are under `/home/zby/.codex/sessions/2026/09/27/`.
The cache's `trace-index.json` retains absolute paths, hashes, configurations,
matched calls, diagnostic lines and audit gaps. The adjacent per-worker
`*-audit.json` and `*-audit.txt` retain the complete visible tool deliveries.
Models and effort match their immediate baseline configurations exactly.

| Worker | Trace filename | SHA-256 | Actual configuration |
|---|---|---|---|
| dynamic-coordinator | `rollout-2026-09-27T22-13-32-01a0e480-5cdf-7b23-a0aa-269568a5b302.jsonl` | `02711e8e278768be24646ebdca9cc28922a6833b23de286769bd0a38537cd2b5` | gpt-6-astra, medium |
| dynamic-specialist | `rollout-2026-09-27T22-15-30-01a0e482-2709-7081-9cf3-f997fcf16a9d.jsonl` | `ccf1a806578fd85577d10ca88a7ce75813be11ed7652bd56c17693982ef8844d` | gpt-6-astra, medium |
| mem0-coordinator | `rollout-2026-09-27T22-30-14-01a0e48f-a667-7393-8d88-3ce42b80c6c6.jsonl` | `39406be9eebcf227aaa42449a89b6b0beb2ad6a1d318514332eef9d5856d26d6` | gpt-6-astra, medium |
| mem0-specialist | `rollout-2026-09-27T22-32-11-01a0e491-6fa3-7880-87db-35a6c362e503.jsonl` | `554d61816caddc05efc6d4a762f44a1c738730b565bea790d683bb48548ea98f` | gpt-6-astra, medium |
| napkin-coordinator | `rollout-2026-09-27T22-48-49-01a0e4a0-aa31-7d00-967f-3519a969c7d0.jsonl` | `c81cdd22d6377f49925e7f2a4649ee9b5865ec62aad286346b54961592a17ea4` | gpt-6-astra, high |
| napkin-specialist | `rollout-2026-09-27T22-50-00-01a0e4a1-bdfb-7f73-b12f-8ecf57b29b21.jsonl` | `7f49e4685e02bc9b9fab887d7db66af2187a33c988a115bc681150d6a3e56b0a` | gpt-6-astra, high |

## Instruction delivery bytes and order

The following table records each relevant **delivery**, including wrapper
framing and co-loaded files; it does not pretend to apportion bytes among
files in a batch. Line numbers address the worker's raw trace output events.
The cache's `loading-deliveries.json` retains exact commands/ranges and nested
output byte counts where available. Discovery listings and hash-only mentions
are not counted as instruction loads. The main skill, result type and
specialist report type are distinct files despite similar names.

| Worker | Output line | Delivered text bytes | Governing content received or recovered | Truncated |
|---|---:|---:|---|---|
| dynamic-coordinator | 14 | 40,154 | Main skill + doctrine batch; missing skill prefix | Yes |
| dynamic-coordinator | 20 | 10,288 | Main skill 1–165 recovery | No |
| dynamic-coordinator | 25 | 34,820 | Run-state type; result type 1–210; collections | No |
| dynamic-coordinator | 32 | 39,958 | Result type 211–440; memory and epistemic instructions | No |
| dynamic-coordinator | 38 | 8,214 | Result type 441–597; source identity operations | No |
| dynamic-coordinator | 115 | 13,341 | Memory report type; note type; selected source | No |
| dynamic-specialist | 14 | 38,972 | Memory instruction; doctrine and input | No |
| dynamic-specialist | 19 | 23,103 | Memory report type; collection and discovery | No |
| dynamic-specialist | 24 | 40,154 | Result type 43–178, 197–290; omission in source code | Yes |
| dynamic-specialist | 72 | 10,149 | Result type 179–197, 290–325; selected source | No |
| mem0-coordinator | 14 | 40,154 | Main skill + doctrine batch; missing skill prefix | Yes |
| mem0-coordinator | 20 | 9,285 | Main skill 1–145 recovery | No |
| mem0-coordinator | 30 | 33,090 | Run-state type; result type 1–195; collections | No |
| mem0-coordinator | 36 | 38,631 | Result type 196–410; memory and epistemic instructions | No |
| mem0-coordinator | 42 | 17,676 | Result type 411–597; memory report type | No |
| mem0-coordinator | 170 | 23,509 | Main skill 145–385; result schema | No |
| mem0-specialist | 14 | 38,859 | Memory instruction; doctrine and input | No |
| mem0-specialist | 19 | 40,154 | Report/result types and ancillary content; type middle omitted | Yes |
| mem0-specialist | 24 | 23,864 | Result type 225–335; report schema; source discovery | No |
| mem0-specialist | 149 | 4,224 | Result type 190–216 recovery; source and identity checks | No |
| napkin-coordinator | 15 | 40,153 | Main skill + doctrine batch; missing skill prefix | Yes |
| napkin-coordinator | 25 | 9,336 | Main skill 1–155 recovery | No |
| napkin-coordinator | 31 | 32,405 | Run-state type; result type 1–200; collections | No |
| napkin-coordinator | 36 | 22,843 | Result type 200–420 | No |
| napkin-coordinator | 42 | 25,649 | Result type 420–630; memory and epistemic instructions | No |
| napkin-coordinator | 139 | 11,013 | Memory report and note types; publication help | No |
| napkin-coordinator | 166 | 6,480 | Main skill 155–250; quote operation | No |
| napkin-coordinator | 236 | 15,356 | Main skill 245–450 | No |
| napkin-specialist | 14 | 34,207 | Memory instruction and doctrine | No |
| napkin-specialist | 20 | 40,154 | Report/result types; collection and input; type middle omitted | Yes |
| napkin-specialist | 28 | 21,397 | Result type 70–295 recovery; source discovery | No |

All coordinators received the result type and epistemic instruction before
provisional findings (step 3). Specialists received their four named sections;
Mem0's full Status fields recovery was late, before final handback rather
than initial drafting. Specialists did not load the main skill, epistemic
instruction or run-state type as separate governing reads, consistent with
their narrower task. No worker visibly loaded `kb/reference/commands.md`;
command forms/help were used. These are observed loading facts, not a claim
that the linked command reference is mandatory reading at every invocation.

## Record-count comparison

Counts are declared unique IDs, attribution lines beginning `> ---`, and data
rows in Limitations. Superseded records remain counted because they remain
canonical declarations. Words are whitespace-separated over the complete file.

| System/version | SRC | CMP | OBJ | RTE | CLM | ABS | BAP | Quotes | Limitations | Words |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dynamic-cheatsheet baseline | 1 | 2 | 11 | 10 | 3 | 1 | 4 | 29 | 6 | 10,614 |
| dynamic-cheatsheet new | 4 | 2 | 6 | 7 | 5 | 1 | 4 | 31 | 6 | 12,593 |
| mem0 baseline | 1 | 4 | 7 | 12 | 4 | 1 | 6 | 49 | 8 | 11,806 |
| mem0 new | 3 | 5 | 9 | 8 | 3 | 1 | 3 | 34 | 6 | 14,862 |
| napkin baseline | 1 | 3 | 10 | 10 | 2 | 0 | 5 | 37 | 6 | 10,668 |
| napkin new | 3 | 2 | 13 | 13 | 3 | 2 | 4 | 43 | 7 | 14,770 |

## Fourteen-axis comparison

Each cell gives the coverage assessment and value set, not its evidence grade.
Per-value grade changes are described in each system's account; complete
per-value evidence, record IDs and notes are retained in the authoritative
results and the cache's three `*-comparison.json` files. The integration check
compared those full mappings, not just the sets below.

### dynamic-cheatsheet

| Axis | Baseline assessment and values | New assessment and values |
|---|---|---|
| `storage_substrate` | partial; `files`, `in-memory`, `service-object` | known; `files`, `in-memory` |
| `representational_form` | partial; `natural-language`, `symbolic` | known; `natural-language`, `symbolic` |
| `lineage` | partial; `imported`, `other-compiled`, `trace-extracted`, `authored` | known; `imported`, `trace-extracted` |
| `behavioral_authority` | partial; `knowledge`, `ranking` | known; `knowledge`, `ranking` |
| `write_agency` | partial; `automatic`, `manual` | known; `automatic` |
| `curation_operations` | partial; `evolve`, `consolidate`, `dedup`, `synthesize`, `promote` | known; `evolve`, `synthesize`, `dedup`, `promote` |
| `read_back_direction` | partial; `push` | known; `push` |
| `read_back_signal` | partial; `coarse`, `inferred-embedding`, `inferred-judgment` | known; `coarse`, `inferred-embedding`, `inferred-judgment` |
| `trace_learning` | known; `yes` | known; `yes` |
| `trace_source` | partial; `trajectories`, `tool-traces` | known; `trajectories`, `tool-traces` |
| `learning_scope` | partial; `per-task`, `cross-task` | known; `per-task`, `cross-task` |
| `learning_timing` | partial; `online` | known; `online` |
| `distilled_form` | partial; `natural-language`, `symbolic` | known; `natural-language`, `symbolic` |
| `faithfulness_tested` | not-determinable; ∅ | not-determinable; ∅ |

### mem0

| Axis | Baseline assessment and values | New assessment and values |
|---|---|---|
| `storage_substrate` | partial; `vector`, `sqlite`, `files`, `service-object` | partial; `vector`, `sqlite` |
| `representational_form` | partial; `natural-language`, `symbolic` | partial; `natural-language`, `symbolic` |
| `lineage` | partial; `authored`, `imported`, `trace-extracted`, `other-compiled` | partial; `trace-extracted`, `imported`, `authored`, `other-compiled` |
| `behavioral_authority` | partial; `knowledge`, `ranking` | partial; `knowledge`, `ranking` |
| `write_agency` | partial; `automatic`, `manual` | known; `automatic`, `manual` |
| `curation_operations` | partial; `dedup`, `evolve`, `invalidate`, `decay` | partial; `dedup`, `evolve`, `invalidate`, `decay` |
| `read_back_direction` | partial; `pull`, `push` | known; `pull`, `push` |
| `read_back_signal` | partial; `identifier`, `inferred-embedding` | partial; `identifier`, `inferred-embedding` |
| `trace_learning` | partial; `yes` | known; `yes` |
| `trace_source` | partial; `session-logs`, `event-streams`, `tool-traces`, `trajectories` | partial; `session-logs`, `trajectories`, `tool-traces` |
| `learning_scope` | partial; `per-project`, `cross-task`, `per-task` | partial; `per-task`, `cross-task` |
| `learning_timing` | partial; `online`, `staged` | partial; `online` |
| `distilled_form` | partial; `natural-language`, `symbolic` | partial; `natural-language`, `symbolic` |
| `faithfulness_tested` | uninspected; ∅ | not-determinable; ∅ |

### napkin

| Axis | Baseline assessment and values | New assessment and values |
|---|---|---|
| `storage_substrate` | known; `files`, `in-memory`, `sqlite` | known; `files`, `in-memory`, `sqlite` |
| `representational_form` | known; `natural-language`, `symbolic` | known; `natural-language`, `symbolic` |
| `lineage` | known; `authored`, `other-compiled`, `trace-extracted` | known; `authored`, `imported`, `other-compiled`, `trace-extracted` |
| `behavioral_authority` | known; `knowledge`, `instruction`, `ranking`, `routing` | known; `knowledge`, `instruction`, `ranking`, `routing` |
| `write_agency` | known; `manual`, `automatic` | known; `automatic`, `manual` |
| `curation_operations` | known; `consolidate`, `dedup`, `evolve`, `invalidate`, `synthesize`, `promote` | known; `consolidate`, `dedup`, `evolve`, `invalidate`, `decay`, `synthesize` |
| `read_back_direction` | known; `pull` | known; `pull`, `push` |
| `read_back_signal` | inapplicable; ∅ | known; `coarse` |
| `trace_learning` | known; `yes` | known; `yes` |
| `trace_source` | known; `session-logs` | known; `session-logs` |
| `learning_scope` | known; `per-project`, `cross-task` | known; `cross-task`, `per-project` |
| `learning_timing` | known; `online`, `offline` | known; `staged` |
| `distilled_form` | known; `natural-language`, `symbolic` | known; `natural-language`, `symbolic` |
| `faithfulness_tested` | not-determinable; ∅ | not-determinable; ∅ |

## Final validation and retained evidence

Final explicit workshop README, this report and bounded table validation
passed cleanly: each returned 0, with no warnings/failures and empty stderr.
The command records are in `final-validation.json` in the cache. Exact-result bundle validation
and the three independent handoffs are recorded separately. No pytest run is
required for these Markdown/data-only outputs. The cache contains startup/end
identities, producer hashes, source/baseline preservation checks, trace audits,
profile/count comparisons, integration checks and downstream commands/hashes.
The substantive findings and limitations are retained in this report so that
removing regenerable cache files does not erase the trial's conclusions.
