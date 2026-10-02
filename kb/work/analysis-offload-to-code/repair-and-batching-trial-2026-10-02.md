# Amendment and input batching trial

Commissioned on 2026-10-02 after the Luna and Sol trace comparison. The operator
approved amendment retries, input batch hints, fresh worker contexts, early
synthesis link checking, and a controlled Luna medium/Sol medium comparison.

## Method changes

- A refused output with unchanged inputs is preserved and named in its next
  handout. The worker amends failures and dependent findings, preserving the
  remaining analysis and records. Changed inputs require a fresh attempt.
- Python adds file groups to the invocation, using a 6 KiB byte budget. The
  original files and dependencies remain intact. Oversized files get their
  own entry and a bounded-range hint. No packets or summaries are created.
- Every analysis handout specifies `fork_turns=none`.
- Synthesis acceptance uses the same link-boundary check as retained members,
  before synthesis verification.

## Trial protocol

Both new whole-system runs use `https://github.com/jasonkneen/instinctual-memory`
at source commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`, the same committed
method revision, and the analyse-agentic-system skill. The existing clean
checkout remains read-only. No target execution or provider calls are permitted.

The parent follows the code-scheduled loop for both runs and passes each prompt
unchanged to fresh workers. All workers of the Luna run use `gpt-6-luna`,
`medium`; all workers of the Sol run use `gpt-6.1-sol`, `medium`.

The supplied review destinations are
`kb/agentic-systems/reviews/instinctual-memory-luna-repair.md` and
`kb/agentic-systems/reviews/instinctual-memory-sol-repair.md`. The current
published review and the previous retained sets are left unchanged.

After both runs stop, inspect validation, retained hashes and quotations,
worker launch settings, truncation and recovery, amendment behavior if reached,
and substantive coverage. Compare the profile selectors and trace sources,
runtime component inventories, and the source's two known polarity risks with
the previous runs. Report internal repaired errors separately from defects
that remain in accepted results. Record the run IDs and trace evidence here.

## Results

Both runs completed and published under method commit
`a7d04e9bbf113dc448de19d07740cc90347b4961`. Luna produced a shorter analysis
with more correction rounds and an explicitly unresolved profile conflict.
Sol produced broader source checks and no truncated tool deliveries. Neither
analysis found every known semantic defect in the source.

| Measure | Luna medium | Sol medium |
|---|---|---|
| Run | `AAS-2026-10-02-instinctual-memory-01` | `AAS-2026-10-02-instinctual-memory-02` |
| Published disposition | complete | complete |
| Completed jobs / handouts | 12 / 12 | 8 / 8 |
| Analytical memory returns | 1 | 0 |
| Further reconciliation after verification | 1 | 0 |
| Deterministic refusals / preserved outputs | 0 / 0 | 0 / 0 |
| Words across five retained members | 12,027 | 19,612 |
| Verified quotations | 26 | 41 |
| Worker tool deliveries with truncation | 21 | 0 |
| Worker calls returning only command stdout | 36 | 0 |
| Tool deliveries with nonzero exit or script failure | 10 | 2 |
| Sum of completed worker durations | 40.8 minutes | 48.8 minutes |
| Opening to publication | 47.5 minutes | 54.9 minutes |

The retained sets are [Luna](../../agentic-systems/reports/retained/AAS-2026-10-02-instinctual-memory-01/ARTIFACT.yaml)
and [Sol](../../agentic-systems/reports/retained/AAS-2026-10-02-instinctual-memory-02/ARTIFACT.yaml).
Both manifests and all ten members pass deterministic validation with no
warnings. Every member digest matches its manifest, and every retained copy
matches the run output. All 67 quotations pass the frozen-source anchor check.
The source checkout remains clean at the requested revision. The incumbent
review digest remains
`fcd1d1c2bd332423165387d64e4f91f07321b030ac844c06393f9c8a417b0eb2`.

Wall times include parent scheduling, a shared three-worker capacity and
pauses between rounds. Sol's specialist pair waited for capacity; both runs
also waited for the parent after workers finished. These times are not an
isolated model speed benchmark. One pair cannot establish a general model
ranking or isolate the contribution of each of the four method changes.

### What the fixes exercised

All handouts carried `fork_turns=none`, and all launches applied it. The first
session metadata and turn contexts identify twelve completed Luna workers as
`gpt-6-luna`/`medium` and eight completed Sol workers as
`gpt-6.1-sol`/`medium`. Their traces contain the repository instructions and
one new task, without the earlier review conversation. Task payloads are
encrypted in the worker traces, so the trace audit does not independently
verify byte-for-byte prompt delivery. The parent supplied the generated
handouts; one transcription error is recorded below.

Every handout included the file-group hints. Sol used bounded reads and
returned full command results; its workers had no truncated deliveries.
Luna still combined multiple batches into single reads. Some workers narrowed
and retried those reads; some left holes. In particular, `memory1` combined
four instruction/type files, lost 536 tokens in the middle, and continued at
line 241 instead of recovering the omitted contract text. `reconcile2` twice
combined reports into oversized reads and wrote its result without another
read of the lost passages. `verify1` narrowed its epistemic reads three times
but still received truncation. The final `verify2` loaded the full epistemic
member without truncation. The hints are useful guidance, but this Luna run
does not establish reliable compliance with them.

Neither run reached the new deterministic amendment handout or rejected an
escaping synthesis link. Those paths have regression coverage, not live
worker coverage in this pair. The regression tests retain a complete report
while correcting its quotation, keep the preserved baseline immutable, and
exclude that baseline after an input change. They also reject escaping links
before launching synthesis verification. Luna's separate analytical memory
return copied and amended its prior report rather than rebuilding it; this
is evidence about that existing return path, not the new deterministic retry.

Implementation checks passed: 1,236 tests in the full suite, Ruff, diff
whitespace checking, and validation of the edited instructions and protocol.

### Repaired internal errors

Both boundary workers tried `commonplace-quote` before code had frozen the
run's source. The helper correctly refused. The boundary workers continued
with source paths and no retained quotation blocks. This is a workflow/tool
lifecycle mismatch, not a bad quotation accepted at publication.

Luna's other failed deliveries were one search of a nonexistent source path,
two quote selections whose proposed text did not occur in the source, two
failed patch applications, two validation failures and two Python syntax
errors, counting the boundary refusal as the tenth failed delivery. The
memory search included `src/writeback.rs`. The runtime and epistemic quote
selections were corrected before report submission. Memory validation
rejected a pending validation label and unresolved profile records; epistemic
validation rejected an 18-cell row where 17 were required. Subsequent edits
resolved both. The final verifier repaired its failed quote-check script.
None of these produced a deterministic workflow refusal because the workers
repaired their outputs before handing them back.

Sol's second failed delivery searched nonexistent `src/erase.rs` and
`src/writeback.rs`; its final account anchors erasure and writeback in their
actual source files. No target execution, provider call, installation, or
source refresh was observed in either run's public tool calls.

There were also parent errors. The parent initially guessed a Luna verifier
prompt path when code had named a memory return; it then read and launched
the actual named job. Later, one Sol verifier launch contained a typo in a
batch path. It was interrupted before any tool call, and a fresh worker
received the correct generated prompt. This extra interrupted worker is
excluded from completed-job and duration totals. These are protocol
deviations; they were not workflow or worker failures.

### Findings that survived publication

Both runtime reports retain all three model components: the configurable
chat-completion extractor, remote JEV relevance judge and local Laya
cross-encoder. The earlier Luna medium quote retry had lost all three.
Neither report equates available machinery with observed provider calls or
host benefit. Both memory profiles now name the fixed `pref_user` identifier,
session logs and event streams, and all seven supported authority values.

Luna's memory return repaired an omitted `dedup` value using tidy's removal
of already-retained duplicates. Its verifier then found another omission:
generated project instructions are in scope, but the lineage profile omits
`other-compiled`. With the memory return exhausted, reconciliation and the
overview carry an unresolved conflict. The machine-readable profile still
claims `assessment: known`. A consumer of that profile alone would read a
completeness claim that the other members expressly reject. Publication is
allowed by the current contract, but this profile must not be treated as a
complete lineage classification. Luna also omits the conditional expiry
behavior that Sol records from `Fact::is_eligible` as `decay`; Luna's claim
that no decay route was found is too strong for this source boundary.

Sol retains four lineage values and conditional decay, with ordinary writes
leaving expiry unset. It checks the source predicates separately for lexical
retrieval, startup preference reads and exported guidance, and reconciliation
corrects the runtime's broader filtering claims. Its profile additionally
calls startup availability gating `coarse`; Luna limits its push signals to
identifier and lexical selection. The source has both an active-fact count
gate and a targeted `pref_user` read, so these should be assessed separately
when using either profile in comparisons. Luna marks trace-source coverage
partial because custom note adapters leave origins open; Sol marks it known
for the inspected conversational and calendar/voice routes.

Sol's epistemic report identifies deduplication's removal of negation and
modality, which prevents lexical overlap from establishing semantic
equivalence. Luna omits that defect. Both omit the preference extractor's
loss of a qualifier: `src/consolidate.rs` matches `please always`, `please
never`, or `please don't` in a noncapturing group, then persists only the
remaining capture as `User requested: ...`. A negative request can therefore
become a positive retained instruction. The Sol verifier actually read this
function but did not report the defect. This miss cannot be explained only
by truncated access.

Both reports correctly separate source-quote occurrence and operational
admission from truth or entailment. Luna nevertheless describes specialist
agreement as independent convergence in its reconciliation, despite shared
runtime findings and the same frozen source. Sol explicitly describes such
agreement as shared-input corroboration. Fresh contexts remove inherited
conversation; they do not create independent evidence.

Compared with the previous Luna medium run, this run preserves the component
inventory and improves selector/source classification, but it takes more
rounds and still has unresolved reading gaps. All three earlier Sol runs
found both polarity risks; this Sol run finds only one. Those earlier runs
used another method revision, so this is a coverage comparison, not an
attribution of the difference to a particular fix. The previous Sol audit
is [retained here](three-run-audit-2026-10-01.md).

### Follow-up candidates

Keep the four implemented changes. The remaining candidates are:

- Make a quoted text mismatch a bounded amendment exercise in a separate
  copied test state, to observe the new retry with a real Luna worker.
- Align boundary quotation instructions with the source-freezing lifecycle,
  so workers do not invoke an unavailable helper.
- Make an unresolved comparison-axis conflict visible to profile consumers;
  adding generic retry rounds would not resolve the representation problem.
- Check concrete deterministic transformations against their input/output
  meanings during source review. More quotation checking would not catch
  either polarity defect.
- Evaluate a stronger read hint with an actual byte limit for each range
  before adding another workflow stage. The current hints do not prevent a
  worker from recombining their groups.

These candidates were not implemented during the frozen trial.

## Trace evidence

Parent trace: `01a0f246-b583-7c12-b320-070107d40be8`. Worker trace IDs below
refer to the first session metadata under
`/home/zby/.codex/sessions/2026/10/02/`. Truncation counts include inner and
outer tool limits, count affected deliveries once, and exclude parent audit
reads. Failure counts inspect exit status and script failures, not mere
mentions of errors in source text. No encrypted reasoning or task payloads
were decoded or retained as evidence.

| Worker | Trace ID | Truncated deliveries |
|---|---|---:|
| Luna boundary | `01a0fb1f-8483-7183-a82e-5d9e591c01da` | 1 |
| Luna runtime | `01a0fb21-87f8-7f72-a785-211f758507c0` | 2 |
| Luna epistemic | `01a0fb26-2b33-7e93-9b11-6d0b843cd955` | 5 |
| Luna memory 0 | `01a0fb26-92b3-7221-be7d-a2ddab56d66d` | 1 |
| Luna reconcile 0 | `01a0fb2f-a745-7ea1-a56a-f36cef6c2b87` | 0 |
| Luna memory 1 | `01a0fb32-f4c6-7702-9401-65caf3a196a3` | 4 |
| Luna reconcile 1 | `01a0fb35-bc50-7993-afdb-2743304ac50c` | 3 |
| Luna verify 1 | `01a0fb38-a8c7-77e3-a59a-ff6f08a2c5bf` | 3 |
| Luna reconcile 2 | `01a0fb3e-52bb-76b2-a2e6-a5e1c8137543` | 2 |
| Luna verify 2 | `01a0fb44-3cf8-7292-9bed-343f1e9e090b` | 0 |
| Luna synthesis | `01a0fb47-2963-7d41-8662-a92f66ff68cf` | 0 |
| Luna synthesis verification | `01a0fb49-976e-7ef0-b0d8-a8b06d79fd07` | 0 |
| Sol boundary | `01a0fb1f-db92-75f0-9c8c-bf2488d29d50` | 0 |
| Sol runtime | `01a0fb24-06d3-78b0-b031-94cac370c3ab` | 0 |
| Sol epistemic | `01a0fb2e-1169-7062-a10d-434f9f730b2c` | 0 |
| Sol memory 0 | `01a0fb2e-7439-7370-9600-8239f82d1655` | 0 |
| Sol reconcile 0 | `01a0fb37-cf2c-7bb0-9c1f-4610f79e9089` | 0 |
| Sol verify 0 | `01a0fb43-6eae-7c51-a808-00a0480582aa` | 0 |
| Sol synthesis | `01a0fb4a-61e3-7b03-8e6d-d18bcd070a30` | 0 |
| Sol synthesis verification | `01a0fb4e-d220-7ba3-9ee4-e8acd7911612` | 0 |

Interrupted Sol verifier: `01a0fb42-9dac-7b82-8ad0-065faa842b69`, zero tool
calls and no submitted output.

## Luna xhigh follow-up

The operator requested one Luna xhigh run to check whether more effort improved
reading and analysis under the same repaired method. Run
`AAS-2026-10-02-instinctual-memory-03` used the same frozen source commit,
fresh contexts, and `gpt-6-luna`/`xhigh` for every worker. Its method pin was
`6f0240b789fc367369ac695b8e803cdf1b92320f`: the only change from the medium
trials' pin was this research report. Code, worker instructions and types were
identical. The new destination was
`kb/agentic-systems/reviews/instinctual-memory-luna-xhigh-repair.md`.

The run stopped before synthesis or publication. The final verifier found
unlabelled implementation/operation statuses in MEM-RTE-1 and MEM-RTE-2,
including the unsupported conclusion-status value `unobserved`. The workflow
had exhausted its reconciliation correction pass and permitted only stopping.
The driver recorded a stop rather than changing outputs or releasing the
block. No new review or retained set was created.

| Measure | Luna medium | Sol medium | Luna xhigh |
|---|---:|---:|---:|
| Published | yes | yes | no |
| Accepted jobs / handouts | 12 / 12 | 8 / 8 | 10 / 11 |
| Analytical memory returns | 1 | 0 | 1 |
| Further reconciliation after verification | 1 | 0 | 1 |
| Deterministic refusals / preserved outputs | 0 / 0 | 0 / 0 | 1 / 1 |
| Matching quotation blocks | 26 | 41 | 82 |
| Worker deliveries with truncation | 21 | 0 | 10 |
| Calls returning only command stdout | 36 | 0 | 92 |
| Deliveries exposing nonzero exits or script failures | 10 | 2 | 19 |
| Sum of completed worker durations, minutes | 40.8 | 48.8 | 147.3 |
| Opening to publication or final block, minutes | 47.5 | 54.9 | 139.2 |

The xhigh totals include eleven completed workers: the refused runtime worker
and its amendment worker both count. An interrupted, incorrectly transcribed
verifier handoff is excluded. Unlike the paired medium trials, xhigh had no
competing analysis run. Durations still include parent gaps and the parallel
specialist pair, so worker sums and elapsed times measure different things.
The xhigh quotation count covers three specialist reports; it is not evidence
that they are more accurate. There is no overview to compare.

### Amendment behavior

The original runtime report used `### Shared records` instead of the required
second-level heading and omitted `### Claims`. Code refused it and preserved
the complete output in the runtime job's `kept/1-runtime.md`. The next handout
named that immutable baseline and asked for amendment.

The fresh worker read the baseline in two ranges, copied it, fixed the two
headings and validated the result. It finished in about 77 seconds. Both
versions contain the same nineteen declared records, including all three
model components. All nonblank, nonheading lines are identical. Word counts
are 5,267 before and 5,269 after. The preserved file's SHA-256 is
`b2579f82b4ad1690a5d5bdf2a93297cc0f3b752478a1d546d5683ebb62d2e20b`.
This exercises the new deterministic amendment path with a real worker and
shows no loss of analysis. It repairs headings, not a quotation mismatch.

### Reading and hidden failures

Reading improved relative to Luna medium, but literal batch compliance was
still uneven. Boundary, runtime and memory-correction workers combined
separate prescribed groups. Most other workers read files separately or in
ranges. Only one of the ten truncated deliveries was an initial prescribed
input load: memory0 printed boundary and the entire runtime report in one
call, even though its Python output inserted range headings. Printing ranges
inside one large result did not bound the delivery.

That load lost the middle of runtime line 109 through part of line 236.
The worker reread lines 151–225 and 226–300, leaving the omitted part of
109–150 unrecovered in its input reads. Source exploration may independently
cover some of those findings; this is an input-reading gap, not proof that
every corresponding claim is wrong. No instruction/type load was truncated.

The other nine truncations were three broad source searches/reads, three
quotation-helper result dumps and three status searches in the first
verifier. Workers narrowed several reads or summarized stored helper JSON.
The first verifier eventually printed route IDs instead of complete long
status paragraphs. Epistemic's broad source search lost about 35,000 tokens;
it then used narrower searches and direct function reads. Fewer truncated
deliveries do not mean every lost passage was recovered.

The nineteen deliveries exposing failed exits or script failures include
three ordinary nonzero results: a diff showing the intended amendment and
two searches with no matches. The remaining visible errors include two
pre-freeze quotation-helper refusals, quotation-selection and parsing errors,
a failed shell brace expansion, JavaScript/Python errors, a failed text
replacement, and two validators rejecting `Validation: pending`. Workers
repaired these before submission. A quote dump also visibly reported a
mismatch while its caller suppressed exit metadata; the worker repaired it
and checked the stored results. With 92 stdout-only calls, the exit-based
count is not a complete census of command failures.

The final verifier initially treated the helper's successful `citation`
status as unresolved. It corrected that check, confirmed all 82 selections,
and compared generated citation blocks against report blocks. Both verifiers
did substantive source reads as well as checking quotations and references.
No target execution, provider call, installation or source refresh was
observed in the public tool calls. The source checkout remained clean, and
the incumbent review retained its previously recorded digest.

There was a parent deviation: the first verify1 launch incorrectly replaced
one instruction path in the batch list with a task-input path. It was
interrupted before any tool call. A fresh worker received the correct prompt.
As in the medium audit, encrypted task payloads prevent independent
byte-for-byte verification from worker traces; no encrypted content was
decoded. All completed workers' turn contexts confirm Luna xhigh, with one
repository-instruction message and no inherited review conversation.

### Final blockers and substantive coverage

All four available typed reports pass deterministic validation without
warnings. All 82 quotation blocks pass frozen-source verification. These
checks do not enforce the prose status-field contract or establish semantic
accuracy.

The first verifier found unsupported `unobserved` conclusion-status values
throughout runtime and epistemic, plus abbreviated record ranges in
reconciliation. Reconcile2 amended those findings. The second verifier then
found the same status problem in the two memory routes. The first verifier
had read those memory passages without truncation but omitted them from its
blocker list. The final defect was not caused by inaccessible input; the
review failed to enumerate all instances before consuming the correction
pass. The intended uncertainty about operation was reasonable; its controlled
representation was invalid.

Xhigh retains the three model components, four lineage values, all seven
authority values, fixed-identifier preference selection, both supported trace
sources, and the distinction between shared-input agreement and independent
evidence. Its memory return explicitly includes the shipped Rust publication
API and marks seven affected axes partial because caller inputs are unknown.
This resolves its scope conflict rather than leaving a contradictory `known`
profile, as Luna medium did. Reconciliation also merges the separately
declared memory and epistemic tidy routes and corrects direct-write provenance
and writeback filtering.

Several semantic gaps remain:

- The curation profile omits `decay` and denies any built-in decay path,
  although its own OBJ-3 annotation quotes the elapsed `expires_at` and
  `valid_to` eligibility checks. Those checks conditionally withdraw later
  lexical retrieval; ordinary writers leaving the fields unset limits their
  routine use, not the existence of that mechanism. Sol medium records it.
- Neither specialist nor verifier reports either known polarity defect:
  the preference regex drops `always`/`never`/`don't` before persisting the
  instruction, and duplicate comparison removes negation/modality words.
  Sol medium found the latter; Luna medium found neither. The xhigh
  epistemic worker received the complete preference extractor in a direct,
  untruncated read. That miss cannot be attributed to truncated access.
- The epistemic report correctly separates excerpt occurrence from semantic
  support but presents candidate entailment as indeterminate without checking
  the transparent rule transformation for a concrete counterexample.
  “Please never send reminders” maps to “User requested: send reminders”
  under the inspected regex and formatter. This is a static inference from
  the implementation, not an executed target test or observed stored fact.

These findings support a limited conclusion: more Luna effort improved input
reading and some coverage, but did not establish reliable completion or
semantic defect detection. The failure that stopped publication is a format
contract problem; it does not establish an absolute reasoning limit.

### Difficulty frontier as an engineering stopping rule

The operator proposed recognizing when a task is near the model's capability
limit and waiting for better models instead of continually expanding the
workflow. Treat that frontier as relative to a fixed task, model, effort and
acceptable failure rate. These three runs do not locate an absolute LLM limit:
Sol medium completed the same workflow, and one run per setting cannot
establish reliability.

Keep the cheap, reusable fixes already implemented. Retain small examples of
the remaining reading, format and semantic failures for future model tests.
Do not add general retry rounds solely because this run exhausted its budget.
If addressing its final blocker, first consider simplifying the repeated
status representation or checking its controlled values at initial acceptance.
Neither requires another analytical stage. The missed source transformations
need a different assessment: raising effort alone did not reveal them here.
Deferring elaborate recovery is reasonable when its maintenance cost exceeds
the value of using the chosen model now; deferral does not certify the outputs.

### Xhigh trace evidence

| Worker | Trace ID | Truncated deliveries |
|---|---|---:|
| Boundary | `01a0fb7c-fc2f-79c1-a65a-1a15227d92ab` | 0 |
| Runtime | `01a0fb84-1966-7b32-a2cf-c9c6076d4fc7` | 4 |
| Runtime amendment | `01a0fba1-210b-72d2-b775-5af5fa64bd05` | 0 |
| Epistemic | `01a0fba3-060c-72b0-ab13-ded57b713f01` | 1 |
| Memory 0 | `01a0fba3-7f92-7fb1-b699-6e7adf1f854f` | 1 |
| Reconcile 0 | `01a0fbbf-ff9d-7e91-8a10-1299b9e76434` | 0 |
| Memory 1 | `01a0fbca-c8d7-7b12-93fe-a683211f75dd` | 0 |
| Reconcile 1 | `01a0fbd6-3268-7093-8eb7-baa2ab8b461d` | 0 |
| Verify 1 | `01a0fbdd-27d3-7741-a6ba-a9f2419aa2a1` | 3 |
| Reconcile 2 | `01a0fbea-f08f-7853-bb82-7f5076f4adc7` | 0 |
| Verify 2 | `01a0fbf1-a5b8-7c41-91ac-aebc33a2814d` | 1 |

Interrupted verify1: `01a0fbdb-fd04-7630-aa5c-22d4841be4f9`, zero tool calls.
The ignored state directory preserves the refused baseline, specialist
reports, both verifications and `workflow-state/workflow/block-1.md`. The
stopping event is recorded there. No workflow or definition changes were made
during or after this follow-up.
