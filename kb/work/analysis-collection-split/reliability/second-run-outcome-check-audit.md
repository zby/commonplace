# Second run under the reliability changes: stopped outcome audit

Commissioned by the operator on 2026-10-04 while the run was active. This is
an audit of the analysis workflow and its traces, compared with the
[first-run audit](./first-run-outcome-check-audit.md). It does not revise a
worker output, the method, or the retained set.

The run stopped at the last synthesis verification. The verifier found that
the synthesis said no retrieval route checks prior outputs for correctness
before inclusion. The retrieval-synthesis curator prompt does request model
assessment of effectiveness and accuracy. That request is not an independently
checked correctness gate, but it makes the blanket statement false. The
workflow had used its one synthesis correction and allowed only stopping.
The coordinator recorded a stop report at 19:10:52 UTC. No publication effect
ran and the incumbent retained set was unchanged. The human-readable run
state still says `running`; the workflow state and stop report are the
terminal evidence for this attempt.

## Evidence and limits

- Run `AAS-2026-10-04-dynamic-cheatsheet-01` in ignored worktree
  `.commonplace/worktrees/dynamic-cheatsheet-b0dc01a84b3c`, prepared at
  method commit `6f497a14e4cee76bac1a8571c23ebfec77784314`.
- Source identity and commit are the same as the prior run:
  `https://github.com/suzgunmirac/dynamic-cheatsheet` at
  `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`.
- The coordinator and all sixteen workers' turn contexts report
  `gpt-6-luna`, medium effort. Their seventeen trace paths, hashes, times,
  token totals, command-output truncation counts, the checker logs and run
  file hashes are in [the evidence file](./second-run-outcome-check-evidence.json).
  Trace reasoning and inter-agent messages are encrypted; the audit covers
  visible calls, results, delivered text and run files.
- The ignored worktree holds the run state and scratch logs. Their recorded
  paths and hashes cease to be independently useful if it is removed. This
  audit retains the decisive observations, not the full traces.
- The two runs differ in method commit and worker outputs. Even with the same
  source and reported model, one comparison cannot assign a cause to a change.

## Counts against the first run

| Measure | First run | This run |
|---|---:|---:|
| Workflow result | Published | Stopped before publication |
| Accepted job outputs | 10 | 16 |
| Worker sessions | 10 | 16 |
| Jobs requiring another handout after acceptance | 0 | 3: reconciliation, profile, synthesis |
| Substantive correction rounds | 0 | 3 |
| Acceptance refusals | 0 | 0 |
| Analyst check calls | 16 | 27 |
| Check calls with refusals | 4 | 9 |
| Wall time from opening session to result | about 21 minutes | about 47 minutes |
| Coordinator and worker tokens, including cached input | 7.6 million | 18.3 million |
| Quotations in accepted source members | 26 | 43 in the unpublished candidate |

All sixteen jobs ran their own acceptance check and passed before submission.
The nine failing check calls came from boundary (three), runtime (one), memory
(three), and epistemic (two). Across those calls the log has 36 diagnostic
lines: three source-registration, five ambiguous quotation, six quotation
not-found, four record-contract, sixteen epistemic-ledger and two job-contract
lines. Identical findings can be collapsed in a line, so these are diagnostic
lines, not a count of underlying fields. No acceptance refusal shows a worker
ignoring a failing check.

The epistemic job took about fifteen minutes and 4.5 million tokens, the
largest single contribution. Its first check reported missing ledger fields,
two invalid section headings, malformed `Part of:` lines and three missing
quotations; the worker repaired them locally. Memory had one ambiguous quote
check followed by two not-found checks before passing. The checker prevented
these draft defects from becoming acceptance retries, but the trace does not
establish whether each substitute passage supports its nearby claim as well
as the original.

## Independent reviews and why the run stopped

1. Record verification found `EPI-OBJ-provider-search` declared under Claims
   although its ID and meaning make it an operative object. Acceptance and
   set validation had passed. Reconciliation amended its classification and
   also superseded two overlapping epistemic object identities with the
   canonical memory objects. The second record verification passed. The
   misplaced heading is a typed placement defect that the code did not catch.
2. Profile verification found `synthesize` unsupported for
   `RT-RTE-retrieval-synthesis` on the curation-operations axis. A profile-only
   correction removed it and the second verification passed. This exercised
   the correction path that the first run never used.
3. First synthesis verification found that the synthesis grouped theory-builder
   conditions, criticism improving capacity, reflection, autonomy and
   self-improvement into one non-establishment claim. The synthesis correction
   stated their evidence limits separately. Second synthesis verification then
   found the blanket prior-output correctness claim, unchanged from the
   original synthesis. The source curator prompt explicitly asks for model
   evaluation of solution effectiveness and accuracy; the accepted memory
   member already distinguishes prompt guidance from a checked gate. The
   first synthesis verifier had described the implementation claims as
   agreeing with the records and missed this overstatement. The second
   verifier caught it after the one permitted correction had been spent.

This is a semantic failure past the checker's scope. The stop prevented an
overclaim from replacing the public set. It also shows that a verifier can
miss one issue while reporting another; its broad assurance that
implementation claims agreed with the records did not cover this claim.

## Latent failures found by a deeper audit

**Publication would also have stopped on the run ID.** This worktree allocated
`AAS-2026-10-04-dynamic-cheatsheet-01`, the same ID carried by the incumbent
retained overview. `Orchestrator.start` chooses the first free suffix in the
*local* `state/` directory. The new isolated worktree had no prior local run
state, even though it inherited the retained set from the method commit.
Publication's `_check_set` explicitly raises `replacement requires a new run
ID` when the incumbent and candidate IDs match. The synthesis stop occurred
first, so the publication check did not run and this blocker appears in no
workflow report. A same-day fresh-worktree rerun can reproduce it unless run
allocation or preflight accounts for retained and archived IDs. This is a
deterministic publication failure, not an inference about the synthesis.

**The profile has an unresolved cross-axis inconsistency.** The first run's
profile included `learning` in `behavioral_authority`; this candidate omits
it while retaining `trace_learning: "yes"`. The candidate's own rationale
says task inputs and generated outputs feed an automatic retained text update
that is supplied later. The profile type defines `learning` authority when
retained examples or experience feed an update to a durable behavior-shaping
artifact. On the supplied records, that appears to support the omitted value.
The profile verifier said all ten axes were supported and did not discuss
this cross-axis difference. The issue needs a semantic disposition before
using the candidate in the comparison matrix; a changed value is not by
itself proof that the new or old classification is correct.

Five of the ten profile axes changed against the incumbent at the same source
revision. The verifier was intentionally source-first and did not receive the
incumbent; this comparison is the audit's, not evidence it ignored a supplied
input.

| Axis | First run → candidate | Audit disposition |
|---|---|---|
| Representational form | text and parametric → adds symbolic | Structured checkpoint fields plausibly support the added value. |
| Lineage | known, including trace-extracted → partial, omitting trace-extracted | Review whether prior answer traces feeding model-written context retain this known derivation path; unknown vector provenance does not erase a separately supported path. |
| Behavioral authority | learning included → omitted | Likely inconsistency with the candidate's `trace_learning: "yes"` and the type's learning definition. |
| Write agency | automatic and manual → automatic | The type says a human-triggered automatic extraction is automatic; whether caller-supplied initial text is a separate manual write remains a scope judgment. |
| Curation operations | four known values → partial consolidation only | More conservative about unobserved model output; no defect established from the difference alone. |

The trace and state audit found no check bypass: each of the sixteen accepted
job bytes matches its recorded acceptance hash, its final local check passed,
and no worker edited its output after that check. Other tool failures remained
local to workers: epistemic made a failed shell-quoted edit and a wrong-path
source read, and profile verification made one invalid patch call, then
recovered. These attempts are absent from workflow failure counts and did not
cause the terminal stop.

## Other trace findings

- **Source-register repair loop.** The new boundary check refused the same
  row three times. The worker put the optional relative access root after the
  repository URL in the `identity/location` cell, first in parentheses and
  then after a semicolon. A change to header capitalization did nothing. The
  fourth check passed only after the access root was removed. The boundary
  contract permits an access root in the register, while code requires the
  entire identity cell to equal the canonical URL. The refusal stated the
  expected identity but neither named the row or actual conflicting cell nor
  explained that optional location text had to be removed or moved.
- **Source reading.** Five visible tool outputs were truncated: two boundary
  reads, two memory searches, and one profile combined member read. Boundary
  and profile followed with narrower reads of key files; the complete match
  set of the broad memory searches was not restored. A negative finding based
  only on those search outputs would not be demonstrated.
- **Record verifier independence.** Both record-verification sessions read the
  accepted members and listed the frozen source tree, but neither read a source
  file's contents. `verify-1` called `sonnet_eval.py` and helper evaluators
  disconnected without a direct source read of its own. Runtime and epistemic
  workers did read `sonnet_eval.py` without truncation, and the epistemic
  member recorded the disconnected utility, so the first run's unsupported
  *team-wide inspection* claim did not recur. Independent source rechecking
  by the verifier remains unobserved.
- **Coordinator command results.** All sixteen `step` calls and the other
  three workflow command calls printed both output and exit code. The
  first-run audit found that exit status had been discarded in all command
  calls. The coordinator used the worktree-local executable and working
  directory throughout this run.
- **Run-state visibility.** After the workflow stop report, `workflow-state`
  records `stopped` and the block says `Permitted: stop`, while `run-state.md`
  still says `running`. A reader of only the run-state file would miss the
  terminal result. No publication `prepare` or `publish` effect is present.

## Previous published defects and current disposition

| First-run defect | This run's candidate |
|---|---|
| Repository slug used as system name | Run and drafts use `Dynamic Cheatsheet`. |
| Machine-local path in public Source register | Boundary register uses the canonical URL and commit, with no worktree path. |
| Unsupported claim that `sonnet_eval.py` was inspected | Runtime and epistemic traces show complete reads; record verifiers relied on members and tree listings. |

These are candidate observations. The stopped run produced no new public
overview, so it did not repair the incumbent's published defects. The
incumbent still validates with zero failures and warnings. Replacement,
archiving and public link following remain untested.

## Assessment

The analyst-local checker again removed mechanical acceptance retries. It
also exposed a new source-register instruction/check mismatch and several
quote and ledger repairs before handout. The independent semantic gates did
work: they found three issues and refused publication on the unresolved one.
Compared with the first run, this attempt used more than twice the time and
tokens and yielded no published set. The evidence does not show that the
checker caused the semantic defects or that its passing result certified
content quality.

Before another comparable run, the strongest narrow repairs to evaluate are
run-ID allocation against retained sets, the profile's learning classification,
the source-register check's treatment and message for an allowed access root,
typed section placement for epistemic object declarations, and why the first
synthesis verifier missed a claim the second caught. A larger correction
budget could allow another synthesis edit, but would not remove the cause of
the overclaim, the missed first review, or the publication collision. The
worktree and traces should be retained until those decisions are made.
