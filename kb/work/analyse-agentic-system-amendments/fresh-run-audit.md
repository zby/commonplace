# Fresh-run audit: Dynamic Cheatsheet

Commissioned by the operator on 2026-10-03: wait an hour, repeat hourly until
the run finishes, then inspect results and traces for errors, including
recovered failures, explain their causes, and assess the adopted improvements.

The run published successfully, but successful completion concealed several
recovered errors. The amendments worked as acceptance checks. They did not
prevent workers from making record-format errors, and the new range detector
also produced a false positive. The most consequential remaining concern is
the boundary: the report calls a selected API implementation a whole system
while excluding shipped prompts and the benchmark driver that would inform
its memory and epistemic findings. Keep this workshop open for a bounded
follow-up decision.

## Evidence and limits

- Run: `AAS-2026-10-02-dynamic-cheatsheet-01`.
- Source commit: `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`.
- Method commit: `77a8e0d9dbb89f8661211f121dcc7077f7448154`, including
  `4807abb47` and the minimal pre-run adoption changes.
- First hourly check: 2026-10-02 23:08:56 UTC, still running at `verify-1`.
  Second check: 2026-10-03 00:09:09 UTC, complete.
- The parent trace reports `done` at approximately 23:28 UTC on October 2
  (01:28 local time on October 3). Acquisition began around 21:59 UTC.
- Inspected the parent and all 13 worker sessions: 10 logical jobs, with
  three additional workers repairing refused verification outputs. Their
  file names, hashes, line numbers and diagnostic excerpts are retained in
  [trace evidence](./fresh-run-trace-evidence.md).
- Inspected the boundary, both reconciliation and verification rounds,
  preserved refused outputs, synthesis, final members, published review,
  workflow state, scratch selections, relevant validators and source files.

This is a post-run audit, not a continuation of the driver. No `step` was
issued. The expanded source inspection below is audit evidence; it does not
retroactively enlarge the run's frozen Source register. Cross-agent message
bodies are encrypted in the local traces, so their exact instructions cannot
be assessed. The inventory covers observed errors in the available traces,
not a guarantee that every semantic error has been found. Parent development
work before the skill invocation is excluded from run error counts.

## Completed-result checks

Fresh `commonplace-validate --json` checks passed with zero failures and
warnings for the retained set, generated review and run-state document.
All six output files, including the manifest, equal their retained copies
byte for byte. The final set has 16 runtime declarations, two memory
declarations and 12 epistemic declarations, plus the two source-register
IDs. Local record syntax checks pass, and set validation resolves the
cross-member references and checks retained quotations against the source.
Every inspected code-span source path exists in the pinned checkout.

The amendment index occurs once, inside Source register, and names
`EPI-OBJ-2`, `EPI-OBJ-3`, `EPI-OBJ-4` and `EPI-OBJ-8`. Member identity fields
match the run and source commit. The final verification reports no blocker.
These checks certify the recorded structural and quotation contracts; they
do not certify source coverage or every interpretation of the source.

## Error inventory and root causes

### 1. Source acquisition hit restricted networking

The first workflow step failed to clone GitHub because DNS resolution was
blocked. The parent reran the step with network escalation and acquisition
succeeded. This consumed one workflow environment block, before any analyst
job. It did not consume an analyst retry. The cause was the launch environment,
not the source repository or amended method. Start the next Codex session
with outbound networking enabled when source acquisition requires it.

The parent also found the required commands missing before opening the run.
At the operator's instruction it reinstalled the editable user-level tool
and checked command discovery. This was installation drift: checkout changes
alone do not install newly added entry points. The repair succeeded before
the run started. Evidence: parent lines 140–200, 216 and 231.

The post-install `uv tool list` inspection also failed because the sandbox
could not create a temporary file under `/home/zby/.cache/uv/`. Command
discovery and the subsequent workflow start succeeded independently, so
this did not block the run. It is a separate filesystem permission error,
not another network failure. Evidence: parent line 200.

### 2. Three verification jobs consumed their one retry on ID ranges

`verify-0`, `verify-1` and `verify-synthesis` each submitted a report containing
prohibited record ranges. The workflow preserved and refused each first
output, and a fresh worker expanded the IDs. The retained retry prompts
list nine, seven and four range diagnostics respectively. These are 20
reported occurrences across three failed submissions, not 20 independent
worker failures. The accepted reports preserve the substantive findings.

The range check therefore caught real contract violations, including shorthand
such as `RT-OBJ-1–4` whose endpoints need no expansion by the checker. The
workers had read the rule, but reverted to compact range prose when writing
verification summaries. The first workers did not run the same syntax check
on their verification text before finishing. Analyst members could use
`commonplace-validate`; these section-only verification outputs rely on the
workflow's acceptance path. The result is a late discovery of a predictable
format error and three additional model invocations.

The three retry workers ran for about 3 minutes 37 seconds, 3 minutes 29
seconds and 3 minutes 36 seconds: roughly 10 minutes 42 seconds of additional
worker wall time. This is a timing observation, not a measurement of all
avoidable cost. Evidence: the three retry prompts and preserved outputs
under the run's `workflow-state/jobs/` directories; trace inventory.

### 3. Analysts repaired several errors before the workflow saw them

Six failing validation invocations are visible across runtime, memory and
epistemic work. Runtime's summary and full checks inspect the same defective
draft; do not count them as separate draft regressions.

| Worker | Observed defect | Cause and recovery |
|---|---|---|
| Runtime | Four schema diagnostics: wrong runtime and record-kind order, missing `## Annotations`, missing `### Behavioral-authority paths`. | The draft omitted required headings and put behavioral-authority content outside its canonical kind heading. The type already supplied the template. The worker read the schema, repaired the structure and passed validation. |
| Memory | Two bulleted `- Part of: RT-OBJ-2` fields. | The worker applied its usual list-field formatting to a field with an explicit unindented grammar. The new checker rejected both; removing the bullets repaired them. |
| Memory | `report-status: complete` with `Validation: pending.`; persisted through the first repair. | The completion checklist contradicted the declared status. The worker changed the text and then ran a passing check. The eventual claim is supported by the later successful validation, although its wording was written before that successful check. |
| Epistemic | Five genuine range diagnostics in its initial draft, still present after its first attempted replacement. | The repair searched for unbackticked phrases while the draft separately backticked endpoints. Exact string replacement missed those phrases; the next validation caught them again. |
| Epistemic | Nine invalid route-function values, such as `content transformation: answer generation`. | The worker appended descriptive suffixes to a controlled-value field. The validator requires the exact value; removing the suffixes repaired it. This was lexical contract noncompliance, not a source finding. |

Evidence: runtime lines 262 and 270; memory lines 346, 350, 360 and 364;
epistemic lines 355, 359 and 369. None of these defects reached workflow
acceptance as an unresolved analyst error. Their absence from final job
failure counters does not mean the first drafts were correct.

### 4. The new range detector misclassified an ordinary relation

The epistemic draft also received this sixth initial range diagnostic:

```text
record references: ranges are not expanded: EPI-OBJ-8` to `RT-OBJ-1; list every full ID
```

The phrase describes a relation between different records. It is not an
enumerated interval. The `_RANGE` expression accepts two full IDs joined by
`to` without distinguishing their namespaces or the surrounding sentence.
The worker removed the second endpoint from that sentence to clear the
diagnostic. The declared relation remained and was later assessed by
verification, so no resulting lost declaration is demonstrated.

A read-only reproduction using the shipped checker confirms the defect:

```python
record_reference_errors('The inventory compares `EPI-OBJ-8` to `RT-OBJ-1`.')
```

This reports a range. Evidence: epistemic lines 355 and 359;
`src/commonplace/lib/agentic_records.py`, `_RANGE`.

The adoption needs a bounded correction that distinguishes interval syntax
from ordinary relation prose, with regression cases for both. Expanding
the test surface from headings to sentences containing valid IDs is justified
by this run. This is a new checker error, not a reason to withdraw range
checking entirely.

### 5. A syntactically valid containment claim was semantically wrong

The epistemic analyst declared `EPI-OBJ-8` (the proposed extracted response
segment) as `Part of: RT-OBJ-1` (the current or returned cumulative sheet).
The first reconciler accepted it and reported no unresolved conflict.
Verification correctly distinguished a proposal before admission from the
sheet after admission and raised a blocker. The second reconciliation added
an amendment replacing containment with a distinct-identity comparison.
The second verification accepted that repair.

The cause was identity conflation across an admission transition: a candidate
that can replace an object is not thereby a material part of that object.
Structural checks cannot determine this from well-formed IDs. The adopted
semantic verification rule performed useful work here, and reconciliation
repaired the finding while preserving the immutable analyst member. The
original `Part of:` line remains in epistemic.md by design; readers must
apply the reconciliation amendment. Evidence: `verification-0.md`,
`reconcile-1.md`, `verification-1.md` in the run directory.

### 6. Quotation preparation had escaping and exact-match errors

The epistemic worker hand-authored malformed selections JSON. The quotation
helper rejected it with `Expecting ',' delimiter: line 9 column 299`.
Its first repair called `json.load` on the same invalid document, so it
failed before it could remove the defective last selection. The worker
rewrote the JSON and continued. These are two failed commands from one
malformed-input episode. Evidence: epistemic lines 200, 211 and 214.

A later `openai_limit` selection did not occur verbatim in the frozen
source. The attempted correction overescaped newlines: it wrote literal
`\n` into both the selection and the end of the JSON file. The worker then
switched to a literal text file and successfully obtained the quotation.
The final report's quotation passes source checking, but the abandoned
`scratch/epistemic/search-selections.json` is still invalid JSON:
`Extra data: line 22 column 2`. The analysis recovered; that intermediate
file did not. Evidence: epistemic lines 287, 298, 308, 312 and 317;
the audit's direct parse of the surviving scratch file.

The memory worker received two `candidates` responses for the same passage
appearing twice. It ultimately selected an occurrence and retained valid
quotes. These are expected ambiguity responses, not tool defects or evidence
of invented quotations. Evidence: memory lines 220 and 292. Likewise,
`rg` returning exit 1 for the synthesizer's no-range search is an expected
no-match result, not a failure to run the search.

### 7. Supplied paths and tool-call syntax were mistyped

| Worker | Failure | Root cause and outcome |
|---|---|---|
| `verify-0` | A type read omitted `kb/agentic-systems/`. | Reconstructed path instead of copying the supplied path; the next read used the correct path. |
| `verify-0` | Tried to read `related-systems/suzgunmirac--dynamic-cheatsheet/not-a-path.md`. | A fabricated or placeholder source path. The read failed and supplied no evidence. No later retained citation uses it. The trace does not establish why that placeholder was chosen. |
| `verify-1` | Two reads duplicated `llm/commonplace/` inside the absolute epistemic path. | Repeated path transcription error; subsequent reads corrected it. |
| Synthesizer | Process creation failed with `No such file or directory`. | `workdir` was `home/zby/llm/commonplace`, missing its leading slash; the next call repaired it. |
| Synthesis verifier | `SyntaxError: missing ) after argument list`. | The JavaScript wrapper ended with incomplete `text(r.output`; the next call closed the expression and read the file. |

Evidence: the corresponding trace excerpts. These recovered tool failures
did not change source identity or cause a missing-output retry.

### 8. Truncation recovery and exit-status retention were incomplete

The `verify-1` repair worker received a truncated epistemic read, then split
it into smaller reads that covered the missing material. Recovery worked.
The synthesis-verification repair worker received a truncated read of lines
50–54, reread only lines 50–51, then advanced to line 55. The tail of the
search-route row was not fully recovered by a later bounded read in that
worker's trace. This violates the supplied recovery rule; it does not
demonstrate an incorrect public conclusion. The original synthesis verifier
had read the same material, but the fresh repair worker did not inherit its
context. Evidence: `verify_1_retry` lines 207–234 and
`verify_synthesis_retry` lines 185–206.

Every worker session includes calls that return only `r.output`, despite
the explicit common rule to return the complete command result. Some
workers later switched to whole objects or added an exit-status line.
The two failed `sed` calls in `verify-0`, for example, exposed stderr but
discarded the structured exit code. The causes are tool-wrapper habits
and path transcription; the current instruction supplies the right pattern
but does not ensure it is followed. This weakens detection of empty output,
inner truncation and partial failures. Do not treat the lack of an exposed
exit code as proof that a command succeeded.

### 9. The completion state hides recovered failure history

All final job `failures` values are zero, and their `history` lists are
empty. `engine.accept` explicitly resets those fields on successful
acceptance. Hand-out counts and preserved refused outputs retain the three
verification retries, so those are recoverable; self-validation failures
and tool repairs require the session traces. The state is suitable for
current scheduling, but insufficient as an error-history summary.

The parent also resumed after the network block by escalating `step`,
without a `commonplace-workflow report ... repair` command visible in the
trace. The driver requires recording the repair before the next step.
The block record survives, but the repair action is explained only by the
session trace. This is an operator-loop reporting omission, not a failure
of acquisition after the escalation. Do not infer a repair event from a
commentary message. Cross-agent messages cannot be audited further because
their contents are encrypted in this log representation.

## Remaining result concern: source coverage

The boundary permits five files: README and four implementation files.
It classifies the run as `whole-system`, but explicitly excludes CLI
implementation and omits the repository's supplied prompts. Later analysts
correctly stayed within that register and carried the resulting unknowns
into the synthesis. Their scope compliance does not settle whether the
boundary represents the requested system adequately.

Audit inspection at the same source commit finds:

- `prompts/generator_prompt.txt`,
  `prompts/curator_prompt_for_dc_cumulative.txt`, and
  `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` are shipped files.
  The cumulative curator instruction asks the model to assess the answer's
  correctness before updating the sheet and describes preservation,
  refinement, redundancy removal and reusable lessons. These instructions
  do not prove the model complies, but they are available design evidence
  for curation and proposed criticism, rather than an inaccessible external
  template.
- `run_benchmark.py:95` loads prompt files; lines 173–187 initialize or
  reload a previous sheet; lines 253–270 call the analysed API; line 284
  assigns the next sheet. Lines 293–300 select task-specific answer
  evaluators, and lines 309–315 write outputs after examples and at the end.
  Thus a shipped caller provides persistence, reuse and answer evaluation
  wiring. This does not prove observed benefit, does not show correctness
  scores gate sheet admission, and does not validate benchmark claims.

The source files are present in the frozen checkout, not inaccessible.
The current report accurately limits claims to its selected library API,
but its whole-system label overstates that scope. Its unknown template
guidance and caller persistence are avoidable gaps for a repository-wide
analysis. Verification mostly checked consistency within the accepted
register and did not challenge this classification.

The root cause is an early allowlist selected before tracing the shipped
caller's full memory loop, followed by downstream authority that correctly
prohibits enlarging it. The boundary job inspected README and API/client
files and did not read the prompts or benchmark driver before freezing the
allowlist. A source-coverage check needs to distinguish operator exclusions,
unavailable evidence and inspectable files omitted by the analyst.

Two honest follow-ups are available: explicitly scope a new analysis to the
library API with a narrower boundary classification, or open a new run whose
register includes the shipped driver and prompts. Do not edit this frozen
set to pretend those sources were examined during the original run.

## Did the improvements work?

| Adopted change | Fresh-run evidence | Judgment |
|---|---|---|
| Mandatory `RT-` prefixes and unresolved-ID hints | All 30 declarations and final references resolve; no prefix or unresolved-target diagnostic was found in the run traces. | Positive usage evidence. The hint behavior was not exercised by a mismatch. |
| Range detection independent of resolution | Epistemic self-check and all three first verification outputs rejected ranges. | Enforcement worked; error prevention did not. One ordinary relation was falsely rejected. |
| Explicit `Part of:` grammar | Memory's two bulleted fields were caught and repaired. Eight original part fields exist across memory and epistemic members. | Exercised successfully as syntax enforcement. |
| Semantic containment verification and immutable amendments | First verifier blocked the candidate/sheet containment; second reconciliation amended it and verification accepted. | Exercised successfully after the first reconciler missed the issue. |
| Preserve valid containers and distinguish duplicate identities | `RT-OBJ-2` remains a container; memory text/vector parts remain distinct; `EPI-OBJ-4` is superseded by matching `MEM-OBJ-2`. | Positive evidence for the distinction in this set. |
| Split into already-declared parts; missing-part return or conflict | No split or memory-return round occurred. | Fresh run does not test these branches; bounded fixtures remain their evidence. |
| Explicit run ID and early member identity comparison | Prompts supply the ID; all three analyst members match; none required identity repair. | Positive happy-path evidence, no live refusal case. Regression tests carry the negative evidence. |
| Amendment index placement | One index inside Source register with the four amended IDs and source rows preserved. | Worked for this boundary order; alternate-order evidence remains the fixture. |
| Returning reconciliation reference checks and early prose-anchor checks | Both reconciliations passed; neither returned findings or contained a prohibited source range. | Live negative branches unexercised. |
| Reconciliation heading order and named instruction read first | Reconciliation used the required heading; workers read their named job instruction before dependencies. | Positive usage evidence. This did not ensure full-result tool delivery or complete truncation recovery. |

This run supports keeping the adopted checks. It does not establish that all
errors disappeared or that the new grammar costs fewer retries. The prior
scripted results and this model-run evidence answer different questions.

## Bounded next decisions

1. Correct the demonstrated `to` false positive while retaining genuine
   interval refusal. Test ordinary cross-record relation sentences and the
   actual range forms that occurred here.
2. Make the exact record-list requirement conspicuous at verification output
   time, and decide whether section-only outputs need a bounded preflight
   check usable by workers. This run justifies examining that specific
   friction; it does not authorize a general workflow expansion.
3. Add a boundary review question for shipped consumers, prompts and
   persistence paths before declaring `whole-system`. Select the honest
   follow-up scope for Dynamic Cheatsheet.
4. Decide whether durable recovery history is required outside session logs.
   Existing preserved outputs suffice for scheduled refusal evidence but
   not within-job repairs. A feature proposal should state that need before
   changing storage or workflow stages.
5. Retain a direct warning about candidate-versus-admitted identity when
   refining part guidance. The semantic checker already catches it; this
   evidence does not require automating containment meaning.

Deferred audit items 8–16 are not collectively justified by this run. All
required memory kind headings are present; no metadata-policy mismatch,
analyst-owned amendment, malformed absence status or missing cited source
path was demonstrated. Memory annotations appear in their required section.
The dotless-path gap was not exercised. Keep those items deferred unless
separate evidence or a bounded commission selects one.

Workshop closure remains pending. The run completed and produced a structurally
valid set, but new ID-format refusals and a range-check false positive were
observed. Successful recovery is evidence that the checks work, not evidence
that the fresh run contained no new errors. This audit retains the findings
for the operator's next adoption decision.
