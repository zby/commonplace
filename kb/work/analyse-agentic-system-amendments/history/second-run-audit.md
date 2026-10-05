# Second-run audit: Dynamic Cheatsheet

Commissioned by the operator on 2026-10-03 after completion: inspect the
results and traces, including recovered failures, explain their causes and
assess the fixes against the first run. This is an audit of the analysis
workflow, not a replacement source analysis. Published members are unchanged.

The source-coverage repair worked: the runner, shipped prompts, persistence
and evaluators are included, and verification checks the repository tree.
Verification range retries fell from three to zero. The run nevertheless
required three other scheduled retries and two substantive correction cycles.
A duplicate cheatsheet identity survived all checks. The register also
overstates the boundary worker's initial inspection. Keep the workshop open
for disposition of these findings; completion is not an error-free result.

## Evidence and limits

- Run: `AAS-2026-10-03-dynamic-cheatsheet-02`; source revision
  `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, unchanged from the first run.
- Method: `d0af3dd6d51866ff432e582cbafc5c9537875d02` in opening metadata
  and the published overview. The parent's already-loaded driver predates
  that final instruction change; pinning HEAD did not reload its context.
- The completed run state, retained set and generated review pass
  `commonplace-validate` with zero warnings or failures. Direct frozen-source
  quote checking also passes all 14 final quotations. The retained manifest
  digest is `1aa78cd07fca9f97750f6c6fac912d9477496e5f4ef00bb207e3a9f99538c4a8`.
- The set has 20 declarations: runtime 10, memory 7, epistemic 3; six
  explicit `Part of:` fields, no amendments or supersessions, and one
  unresolved evaluator-coverage conflict carried into the synthesis.
- [Trace evidence](./second-run-trace-evidence.md) inventories the parent
  and all 17 workers, including retry workers, with hashes and diagnostic
  excerpts. The parent also contains the earlier stopped same-day `-01` run;
  its events before line 78 are excluded from `-02` counts.
- This scan covers visible tool calls/results and delivered assistant text.
  Encrypted delegate handoffs are not auditable as message bodies. Missing
  exit codes limit claims about empty tool results. Negative findings below
  mean no demonstrated case in these traces, not proof of universal absence.

The new run opened at 06:26:42 UTC and published at 07:20:43 UTC, about
54 minutes. It has 14 accepted jobs and 17 worker sessions: three jobs needed
two handouts. Final failure counters are zero and histories empty because
acceptance clears them. The preserved refused outputs and traces establish
the failures below independently of those counters.

## Recovered failures and causes

### Acquisition still consumed an environment repair

The first `-02` step fetched inside the sandbox and failed DNS resolution.
The parent then escalated the workflow step itself and acquisition succeeded.
It did not repeat the standalone-fetch mistake from the stopped same-day
`-01` run. One workflow block was consumed before any analyst ran.

The new instruction to request approval before a predictable acquisition
failure was committed at 06:26:15 UTC. The parent had read the driver earlier,
at line 21; its delivered version lacks that instruction. It did not reread
the driver when opening `-02` at 06:26:42. This is a stale execution-context
case: opening metadata pins the new method, but that does not establish that
the parent consumed its latest instructions. The run therefore does not test
adherence to the new advance-approval sentence. It does show successful
recovery by escalating the right command.

No repair report for `-02` appears between the block and the escalated step,
or elsewhere in the parent trace. The driver requires that report before
advancing. The environment failure and recovery can be reconstructed from
the trace, but the repair is not recorded as a workflow event. Evidence:
parent lines 85–95; workflow `block-1.md`; driver's earlier read at line 24.

### Three jobs lost their retry on preventable output defects

| Job | Refused output | Cause and recovery |
|---|---|---|
| `memory-0` | A quote of `write_jsonl` changed the source's literal `"\n"` to `"\\n"`. | The helper had supplied the correct citation, but the draft's nested string/patch encoding altered it. Local validation checked well-formed attribution, not the frozen passage; workflow acceptance caught the mismatch. The retry regenerated the literal passage and repaired the report. Its first scratch reconstruction also overescaped the newline, then was corrected before helper use. |
| `reconcile-1` | `MEM-OBJ-1 through MEM-OBJ-3`. | A range appeared in the axis-by-axis summary despite the shared full-ID rule. The reconciliation checker refused it; the retry listed all IDs. |
| `synthesize` | `MEM-OBJ-1–MEM-OBJ-3`. | The synthesizer compressed a record list into interval notation. Acceptance refused it; the retry expanded the list. |

The three retry workers took approximately 2:15, 2:38 and 1:57, totaling
about 6:50 of extra worker wall time. This measures those invocations only.
All four verification jobs had one handout. The conspicuous range guidance
was read in each verifier's trace and coincides with no verification range
retry. The range problem moved to other consumers; it did not disappear.

The quote refusal reproduces against the preserved first memory output; all
final quotes pass. A passing standalone member check did not establish
source correspondence, so those two validation claims must remain distinct.

### Analysts repaired malformed drafts within their sessions

Three failing validation invocations are visible before job completion:

| Worker | Defect | Recovery and cause |
|---|---|---|
| Epistemic | `SRC-1`–`SRC-3`, plus two ledger route functions containing semicolon-separated combinations of controlled values. | Expanded source IDs and selected one permitted function per row. This repeats the first run's tendency to compress references and embellish controlled-value fields. |
| Memory | Missing frontmatter closing delimiter. | Inserted `---`. The draft could not be parsed far enough to check its body until this was fixed. |
| Memory | Six malformed part fields and `report-status: complete` with `Validation: pending`. | Removed bullets and separated identity prose from `Part of:` lines; replaced the pending claim and validated successfully. The first repair had itself introduced bulleted part fields, so it did not resolve the exact grammar. |

These are three failed invocations, not eleven independent worker failures
or scheduled retries. Later checks passed. Part-field enforcement worked;
the authoring instruction still did not prevent the formatting habit.

Two additional tool mistakes recovered: runtime wrote a quote selection to
an absolute path with duplicated `llm/commonplace` segments, then used the
supplied scratch path; epistemic called the quote helper with an uncreated
`/tmp/dc-epi-selection.txt`, then created its assigned scratch inputs. The
failed call also disregarded the rule to keep selections in supplied scratch.
No new malformed JSON, JavaScript syntax error, or invented retained source
path is demonstrated in this run. Empty patch results are not failures.

### Semantic checks caused useful correction cycles

The first reconciliation returned two memory-profile support errors: the
file-storage evidence note named embedding CSVs but omitted their object ID,
and the synthesis value cited the append-all route rather than the synthesis
route. The returning memory analyst corrected them. This exercises the return
path that the first run did not reach; it does not exercise a missing-part
declaration or split-supersession branch. No new IDs were needed.

The first record verifier found `dynamic_cheatsheet/utils/sonnet_eval.py`
outside the epistemic coverage account. The registered repository allowed it
to inspect that file without boundary expansion. The after-blockers
reconciliation added an anchored unresolved conflict, and final verification
accepted the bounded limitation. Audit inspection confirms a standalone
checker with self-tests, a commented import in `evaluation.py`, and no
identified shipped benchmark/notebook caller. The conflict does not establish
that the helper runs. It preserves an evaluator-completeness limit instead
of inventing a route or rewriting the immutable epistemic member.

The first synthesis verifier also blocked a missing independent
self-improvement assessment. The synthesis described improvement as
unobserved but did not state that property separately as required. The next
synthesis added the evidence-bounded conclusion and passed verification.
These are substantive corrections, distinct from the three refused outputs.

## Failures that survived publication

### Duplicate cheatsheet identity escaped reconciliation and verification

`RT-OBJ-1` and `MEM-OBJ-1` both identify the runner's `cheatsheet` /
`final_cheatsheet` string, with process storage during a run and JSONL storage
between runs. Both cite the same updater and adoption flow. The memory record
says “new operative part of RT-OBJ-1” but specifies no distinct material part
and carries no `Part of:` field. Its identity comparison distinguishes the
cheatsheet from the prior-example corpus, rather than from the supplied
cheatsheet record it duplicates.

The memory member separately annotates `RT-OBJ-1`, so a reuse path already
exists. None of the three reconciliations supersedes `MEM-OBJ-1`, records a
conflict about it, or supplies evidence for distinct identity. Both record
verifiers list it among valid declarations while checking the other six part
relations. Structural checks cannot infer this semantic duplication.

The root cause is a comparison against the wrong referent: “different from
the corpus” passed as justification for “different from the cheatsheet.”
Verification examined declared part fields but missed the unsupported part
claim in identity prose. The candidate-versus-admitted sentence did not
address this failure, and this run contains no corresponding candidate/sheet
containment test. Identity repair is the highest-value new finding. Preserve
the frozen set; any correction needs the method's explicit amendment path
or a later commissioned analysis, not an audit edit to its members.

### The register overstates initial inspection

The register correctly permits the whole pinned repository. However, `SRC-2`
says notebooks were inspected, and `SRC-3` says results, figures, data and
embeddings were inspected. The boundary worker's complete command trace
lists those files but reads README, the runner, core code, prompts and utility
code. It contains no notebook-content or dataset/result-content read. Later
verification searches notebook text, but this cannot establish the boundary
worker's claimed initial inspection retroactively.

This is a residual register-fidelity defect, not the old file-access allowlist
regression: later workers may inspect the files and the important memory loop
is now covered. Separate registration, role classification and actual
inspection when reporting coverage. A file's presence or an inferred role
cannot support the statement that its contents were inspected.

### Tool-result and truncation discipline remain weak

Every worker session contains calls delivering only `r.output`, despite the
required complete-result pattern. Some switch to complete objects later.
This hides structured exit status and inner truncation metadata. Visible
stderr exposed the two bad paths, but no exit status survived those calls.

Five delivered results show truncation: one boundary source read and four
searches across memory and verification. The boundary's combined core-code
and prompt read lost a middle span and was not reread before classification.
Later analysts inspected the core, so this does not prove a final unsupported
route. Search truncations were followed by narrower source reads or targeted
queries, but their full match sets were not restored. Do not treat those
searches as exhaustive coverage evidence. The supplied bounded member reads
otherwise show no delivered truncation in this scan.

## Did the fixes work?

| Fix | Evidence in `-02` | Judgment |
|---|---|---|
| Repository registration rather than a path allowlist | Additional evaluator file inspected without expansion; initial paths expressly nonexclusive. | Worked. Initial-inspection claims still need fidelity. |
| Whole-system coverage tied to tree and responsibilities | All 13 top-level tracked paths classified; shipped prompts, driver, persistence/reload and evaluators named and traced. | Main regression repaired. The final helper conflict bounds evaluator completeness. |
| Remove ordinary `to` false positives | No refusal of relation prose; direct checker reproduction returns no errors. | Parser correction confirmed; no live false-positive case observed. |
| Range guidance in verification jobs | All four verifiers read it; zero verification syntax retries versus three previously. | Positive live evidence. Reconciliation and synthesis still produced ranges. |
| Candidate-versus-admitted containment sentence | No matching candidate/sheet record interaction. | Not exercised; no prevention claim warranted. |
| Part grammar and immutable corrections | Six malformed fields repaired; six final fields resolve; returned profile corrections preserved. | Enforcement and return path worked. Duplicate cheatsheet identity survived. |
| Run/member identities, heading order and amendment index | Correct IDs, clean set checks, accepted returned reconciliation; no amendments to index. | Happy paths passed; index placement not exercised here. |
| Acquisition approval guidance | Right command escalated after a DNS block; new sentence absent from parent's loaded driver. | Redundant fetch avoided, but advance-approval behavior not tested. Repair reporting still omitted. |
| Recovery-history proposal | Zero final failure counters still conceal recovered failures. | Need remains demonstrated; no storage implementation was adopted. |

## Next decisions

Prioritize the demonstrated duplicate-identity omission and truthful inspection
claims. A bounded refinement should require comparison with the closest
supplied referent, including part claims in prose, and distinguish registered
files from inspected passages. Extend the verification-output reminder to
reconciliation and synthesis; retain the existing refusal mechanism. Quote
repairs should preserve helper output literally and distinguish formatting
validation from frozen-source matching.

Before another run, reload changed orchestration instructions and apply the
network approval guidance to acquisition itself; retain its repair event if
one occurs. No fresh run or method/storage change is authorized by this audit.
The former live closure conditions—no range false positive, no verification
range retry and shipped prompts registered—were met, but the new retained
identity error needs disposition before workshop closure. Deferred audit
items 8–16 remain deferred as a group; these concrete findings do not justify
implementing that entire list or adopting a new identity-pass stage.

## Operator disposition (2026-10-03)

After reviewing this audit, the operator accepted the result as good enough
and requested retaining it unchanged. The findings and recommendations above
remain evidence, not an adopted repair plan. Revisit the demonstrated errors
if they recur in later runs; no immediate method fix or repeat run is
commissioned. Retain the published set, review and audit for that comparison.
