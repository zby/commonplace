# Trace audit of the parameterized Luna trials

- **Recorded:** 2026-09-30, at the operator's request to look for hidden failures and other issues after the two trials passed their validators.
- **Scope:** memory and epistemic trials on copied inputs from `AAS-2026-09-30-instinctual-memory-02`, at method commit `4e4f4013`; observable commands, delivered tool outputs, worker messages, and resulting reports. This is not a complete fact check of either report.
- **Result:** both final submitted reports still pass structural and quotation checks. Their execution was not clean: command failures were recovered, required reads were truncated without complete recovery, and substantive omissions and contract violations survived validation.

## Evidence and method

The local rollout directory is `/home/zby/.codex/sessions/2026/09/30/`.
Line numbers below refer to the original JSONL files, not an extracted rendering.

| Analyst | Rollout filename | Calls / outputs | Truncated outputs, JSONL lines |
|---|---|---|---|
| Memory | `rollout-2026-09-30T15-13-17-01a0f272-adfe-7511-b7a7-6f74cc549194.jsonl` | 13 / 13 | 16, 23, 30 |
| Epistemic | `rollout-2026-09-30T15-13-47-01a0f273-25de-7662-9b00-1685f1aa7957.jsonl` | 12 / 12 | 18, 46, 53 |

Both turn contexts identify `gpt-6-luna` and the real repository root as
working directory. Scanning all 25 command/output pairs covered error and
truncation markers, command sequencing, file reads and writes, validation,
and quotation generation. Failed deliveries and report findings were then
inspected in detail. Missing spans in concatenated file reads were located
by matching the text immediately before and after the truncation marker
against the unchanged input files.

The temporary root is `/tmp/commonplace-parameterized-luna-yrskqzv5`.
It now contains readable extracts `trace-1.txt` and `trace-2.txt`,
`trace-audit-metadata.json` with rollout hashes and read gaps, and
`epistemic-ledger-render.html` for the rendering check below. The original
rollouts are not copied into the repository. Task contents and the parent's
spawn-message arguments are encrypted in these local rollouts, so this audit
cannot compare delivered task bytes with saved prompt bytes.

## Findings

### 1. Required reads remained incomplete

Both workers requested large combined reads and continued after explicit
truncation warnings. A larger nested `exec_command.max_output_tokens` did
not remove the outer `functions.exec` delivery limit.

| Delivery | Missing content | Later recovery |
|---|---|---|
| Memory, line 16 | Overview type lines 143–290 and memory type lines 1–136 | Memory type was delivered in full at line 23; overview was never reread. |
| Memory, line 23 | Supplied runtime lines 110–142, including its central route records | No reread of that runtime span. Later source excerpts cover some mechanisms, but do not recover the supplied records. |
| Memory, line 30 | Broad source search, 8,511 tokens omitted | Some narrowed source reads followed; no complete search or coverage receipt. |
| Epistemic, line 18 | Overview type lines 195–290 and epistemic type lines 1–131 | Epistemic type was reread fully at line 39; overview was never reread. |
| Epistemic, lines 46 and 53 | Source search and its subsequent narrowed source read | The narrowed read still omitted 340 tokens in `check_llm_fact`; no complete reread. A later generated quote recovers only its selected evidence-match passage. |

The workers therefore did not fully load the overview contract. Memory
also never fully received the runtime input. This violates the shared rule
that truncated output is not evidence and must be narrowed and reread.
Merely putting every dependency under `read-first` did not ensure delivery.

### 2. The tool wrapper concealed failed inner commands

Every analyst call forwarded only `r.output`; none retained the nested
command's `exit_code`. The outer wrapper consequently said `Script completed`
even when the command output contained failures.

Memory's selection-file Python at call line 64 failed with an unterminated
string literal. The following quote command ran anyway because the commands
were separated by a newline rather than `&&`; it failed because
`selections.json` did not exist. Both errors are visible at line 67.
The worker repaired the script and generated all five quotations at lines
71–74. No failed citation remained in its final report.

Memory's first report failed validation with **15 failures** at line 92:
all comparison axes encoded per-value evidence as lists rather than keyed
objects. The worker read the schema, converted those lists to maps, and
obtained a clean validation at line 106. That repair recovered the
structural result. It does not make the earlier execution successful.

The earlier record's “first attempt” means the first final submission to
the parent validator, not the first draft or command attempt. There was no
parent-requested retry; memory performed these repairs internally.

### 3. Memory's retained validation result is stale

The memory report ends with `Validation: pending.` despite the clean
validation at trace line 106. The repair changed its frontmatter but left
the check record untouched. Its type requires retaining the deterministic
validation result under Limitations and checks. The validator accepts this
contradiction because the section's presence is checked, not its meaning.

### 4. The criticism route remains unexamined

Neither worker read `src/tidy.rs`. Memory encountered tidy in README,
skill text, and CLI search hits; its report mentions cleanup, duplicates,
and one-session facts. It does not trace the model judgment, retained
reason, and later extraction consumer. Epistemic contains no tidy route
and does not list it as unassessed.

At the pinned source revision `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`:

- `src/tidy.rs` lines 125–145 ask the configured model to judge session-only facts.
- The bundled skill's cleanup procedure asks the user to review the list before applying it.
- `src/tidy.rs` lines 171–202 retain the reason while retracting and suppressing selected facts.
- `src/consolidate.rs` lines 145–157 read suppression/deletion controls and pass the blocked IDs into subsequent extraction.

This is a consequential evaluation, disposition, and later-consumer route
within the frozen boundary. Its omission leaves the earlier criticism
coverage question unresolved. It does not, by itself, establish factual
truth checking or accepted knowledge production. The supplied runtime
already omits this route; these trials did not reliably correct that gap.

### 5. Record overlap and heterogeneous parts survive validation

Memory's Integration issues says it identified no duplicate MEM records.
Its own event journal overlaps runtime `OBJ-1`, its Git tree overlaps
`OBJ-2`, and its ingestion/extraction, change, hook, and writeback routes
overlap runtime `RTE-4`, `RTE-5`, `RTE-1`, and `RTE-6` respectively.
Separate prefixes do not establish separate referents. Both records may
remain declared under the overview contract, but the job requires flagging
possible duplicates with affected full IDs; this report does not do so.
The missing runtime span may have contributed, but that causal explanation
is not established by the trace.

Memory also groups fact content, indexes, controls, checkpoints, receipts,
and intents into one operative object. Epistemic recognizes this grouping
in its `OBJ-2` inventory row but assesses only fact statements. It does not
inventory separately the material control parts, and its `OBJ-3` row still
groups hook delivery and retained instruction-file writeback. The job and
type require separate inventory rows where checks, consumers, or authority
paths differ; reconciliation can retain responsibility for splitting the
supplied record IDs. Structural ID resolution does not enforce this semantic
separation.

### 6. Epistemic's ledger has vocabulary and rendering defects

The explicit-change row at report line 40 puts `truth-apt transformation`
in the route-function field. That is not an allowed route function; the
type puts transformation classification in the separate content/update
relation field.

The quotations at report lines 31–37 interrupt the ledger table. The seven
remaining pipe-separated rows at lines 39–45 have no new header and
separator. Rendering with the installed Python Markdown tables extension
produces only **two of nine** ledger rows as table rows; the other seven
are paragraphs containing literal pipes. The validator accepts the section
but does not establish that its ledger is a readable table or compact record.

### 7. Trial metadata and source-inspection claims need qualification

Copied boundary/runtime inputs retain the recorded run's ID, while each
output and run-state uses its trial ID. Memory correctly flags the runtime
identity mismatch for reconciliation. This is a trial-fixture property,
not a source failure. These inputs suffice for this isolated job test;
they would need metadata adjustment before testing full-set assembly.

Memory's inspected-evidence list includes `src/setup.rs`, but its trace
contains no direct read of that file. Some other anchors likewise rely on
the supplied runtime rather than an independent source read. The report
should distinguish supplied implementation findings from source inspection
performed by this worker; its broad wording does not.

### 8. Worker silence conflicts with inherited runtime instructions

Epistemic emits two progress messages at trace lines 14 and 67, although
worker-rules requires silence until the final output path. Its inherited
developer instructions require an initial tool-use commentary and ongoing
updates. That is a runtime/instruction conflict: the job file cannot
override the higher-priority requirement. Memory remained silent.

## Checks that still hold

No observed command reads a forbidden prior-analysis directory, another
trial's report, or workflow-state. No worker delegates, commits, publishes,
modifies the source checkout, or writes outside its assigned report and
scratch paths. Epistemic temporarily changes command working directory to
the source checkout, then runs its validation in the repository root.

The final reports, declared dependencies, and saved prompts were preserved
during this audit. The previously recorded workflow-validator passes and
seven quote-anchor passes still describe those same report bytes. These
checks establish structural acceptance and quote occurrence, not complete
reading, clean command execution, or semantic completeness.

## Follow-up boundary

This audit records failures; it does not change the method or regenerate
the reports. The next discriminating trial should require complete delivered
reads and retained inner exit statuses before judging wording changes.
The existing [review accuracy fixes](./review-accuracy-fixes.md) entry-point
inventory bears on tidy coverage. Duplicate identification, operative-part
separation, vocabulary, and retained check results need review beyond current
structural acceptance. Preserve these trial outputs as the evidence for that
follow-up rather than repairing their content after acceptance.
