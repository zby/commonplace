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
