# Three-system rerun and trace audit, 2026-09-27

The operator requested: “then rerun the three analyses and again check the
traces,” after authorizing the reliability commit. The repairs and earlier
bounded acceptance are committed as `2d5a9d9a`. This record owns scheduling,
validated completion and the new trace audit within the refresh workshop.

All three reruns completed and replaced their public reviews. Independent
handoff verification and the three-system matrix, table and statistics checks
passed. Across six worker sessions and 222 matched tool outputs, the audit
found three recovered command/check failures, twelve truncated read deliveries,
and one Python escape warning. No unresolved operational failure was found.
This supports bounded acceptance of the repairs, not an error-free workflow.

## Boundary

Hold the three existing source revisions fixed to exercise the repaired method
against the same source inputs. Each analysis has a fresh coordinator and a
fresh mandatory memory specialist. Neither receives old analyses, audit
findings, classifications or comparison outputs. The parent audits traces
without forwarding previous findings into analysis contexts. Run one coordinator
and its specialist at a time; use completion events and owned output paths,
never agent listings, for status.

| System | Frozen repository revision | New run | Status |
|---|---|---|---|
| Dynamic Cheatsheet | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | `AAS-2026-09-27-dynamic-cheatsheet-01` | complete; handoff and traces checked |
| Mem0 | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | `AAS-2026-09-27-mem0-01` | complete; handoff and traces checked |
| Napkin | `7582d6a46f5a11995956e60a59c41a5b242109f1` | `AAS-2026-09-27-napkin-02` | complete; handoff and traces checked |

The run owns its normal skill-managed local state, exact retained result and
guarded public-review replacement. Sources, historical retained results,
producer code and instructions stay unchanged. The parent owns this record and
inventory updates after checked completion. The already authorized commit does
not include these subsequent reruns.

## Acceptance and audit

Require each completed-run handoff to verify independently. Then inspect the
coordinator and specialist traces for nonzero checks, tracebacks masked by later
success, output truncation, coordination failures and unreturned calls. Follow
material failures through their recovery and final checks. Separate expected
negative probes and unavailable-yet report paths from operational defects.
Record remaining uncertainty; do not treat final success as proof of an
error-free path. Prior-analysis exposure requires a new clean run, not reuse of
its analytical draft.

The new analyses supersede their public reviews. Earlier comparison/synthesis
snapshots remain historical; any bounded consumer check must use the same three
explicit new reviews. Full-corpus refresh and a new public landscape remain
outside this replay. All three inventory entries were already complete, so
this rerun does not reduce the remaining 159-artifact count.

## Results

### Dynamic Cheatsheet

Published and independently verified with `commonplace-agentic-analysis-handoff`.
Result SHA-256: `9351ed7cec03d03b6da8e66a0c1ac8a6358c382a4f14bb9e8511a82c25963298`.
Memory report SHA-256: `aa49de3cde70ec6de5fb8f1607aef992160a03cab9b5d5496edc9bba4f3aef12`.
The result passed 77 source checks; the specialist passed 52. Both passed
structural validation on the first attempt. Prepare, publish and handoff passed.

The two completed traces contain 66 tool outputs (43 coordinator, 23 specialist),
all matched to calls, with no unreturned calls. No nonzero command/check,
traceback, communication failure or agent listing was found. This was not a
truncation-free run: seven read deliveries were truncated across six tool-output
records. Bounded rereads cover the omitted instruction/type/definition, prompt,
wrapper and schema spans. Explicit selected prefixes in JSON exploration are
bounded source selection, not a failed complete-read claim.

Trace provenance under `/home/zby/.codex/sessions/2026/09/27/`:

- Coordinator `rollout-2026-09-27T10-29-22-01a0e1fb-ad27-7452-83d9-409c66940d65.jsonl`:
  truncated outputs at lines 16, 28 and 182 (the last contains two truncated
  reads); bounded recovery calls at 18, 32/40 and 186.
- Specialist `rollout-2026-09-27T10-31-40-01a0e1fd-c62a-7813-807c-2185b0ddd8e6.jsonl`:
  truncated outputs at 19, 71 and 111; recovery calls at 29, 75 and 115. The
  last omission was in the wrapper/schema read, not the accompanying JSON
  sample extraction. The final report discloses each recovery and its limits.

### Mem0

Published and independently verified with `commonplace-agentic-analysis-handoff`.
Result SHA-256: `4d56119cce3674e2aac27b52818df46a534167961a0370b4b7d5a1a549d8d9d4`.
Memory report SHA-256: `bdb9f70a41135a412a99b1e6c99a32c02d4f179ce7596518d4a0779636c4a768`.
Final result passed 92 source checks; specialist passed 50. Structural
validation, prepare, guarded publication and handoff passed.

The two completed traces contain 77 tool outputs (54 coordinator, 23 specialist),
all matched to calls, with no unreturned calls or agent listings. Two coordinator
commands failed and were recovered:

- A discovery `wc` returned exit 1 for the guessed nonexistent
  `kb/types/agent-memory-report.md`. The worker followed the memory instruction's
  link to the correct type. This was a file-discovery error, not a schema failure.
- Early `verify-sources` returned exit 1 for
  `mem0/utils/entity_extraction.py:751-776`, beyond the 772-line pinned blob.
  The worker reread the full function, corrected the citation to 751–758 and
  passed the next source check. The audit independently reread that function:
  the corrected span supports the attached empty-result fallback when the model
  loader returns no pipeline. This is support checking, not blind EOF clamping.

The coordinator had three truncated instruction/ontology deliveries. Its first
ontology recovery was itself truncated; a further bounded read supplied the
missing support. The specialist had no failed checks, truncation or communication
failures. Its intentionally bounded discovery listing was followed by a full
scoped listing, so it did not assert discovery coverage from a shortened prefix.
No masked failure was found in the recorded diagnostics. Publication was not
attempted before correcting the source error.

Trace provenance under `/home/zby/.codex/sessions/2026/09/27/`:

- Coordinator `rollout-2026-09-27T10-44-37-01a0e209-a3e9-78b0-8ec2-804c895add73.jsonl`:
  truncation outputs 18/167/180 and recovery calls 20/27/176/184; discovery
  failure output 30; source rejection output 201 and reread/correction call 205.
- Specialist `rollout-2026-09-27T10-46-07-01a0e20b-0309-7433-be8c-12c3bf02a9d7.jsonl`:
  23 outputs; all checks and final identity verification succeeded.

The parent audit's first attempted function read was itself truncated because
its output budget was too small. It then read the pinned 751–772 range in full
before checking the claim. Parent audit commands are outside the worker-output
counts above.

### Napkin

Published and independently verified with `commonplace-agentic-analysis-handoff`.
Result SHA-256: `c73351449c9a391e615839fa2aebb44b24894ed34a671e9778d625fbb410f4d1`.
Memory report SHA-256: `06c160664d3154705ca033d2875e420aef9b7af0ddeaecef8855f4d4666fa3dc`.
Final result passed 142 source checks; specialist passed 90. Structural
validation, prepare, guarded publication and handoff passed without cleanup warnings.

The two completed traces contain 79 tool outputs (53 coordinator, 26 specialist),
all matched to calls, with no unreturned calls, agent listings or communication
failures. The specialist's first source check rejected `README.md:405-411`
because the pinned file has 387 lines. A bounded reread located the pi-napkin
integration at 366–372; the specialist also corrected four other README anchors
against that read. The corrected integration citation supports the report's
explicit distinction between documented external integration and inspected
implementation. The parent checked the cited source span and attached claim.

During integration, the coordinator requested exact evidence-search operations
for two absence records. The specialist repeated and recorded those searches;
the substantive findings did not change. Two `git grep` probes returned 1 with
empty stdout and stderr, explicitly recorded as no matches rather than hidden
failures. The Python wrapper emitted `SyntaxWarning: invalid escape sequence` for
`\(` in its regex string. The command and matching metric search still completed;
this was a warning, not a failed search. A raw string would avoid the warning.

Two coordinator instruction/definition deliveries were truncated. Bounded
rereads recovered the omitted main-instruction, theory-builder and reflective
definition spans before use. The specialist had no read truncation. Canonical
integration separated structured memory objects while preserving the report's
qualifications and partial assessments.

Trace provenance under `/home/zby/.codex/sessions/2026/09/27/`:

- Coordinator `rollout-2026-09-27T11-01-47-01a0e219-5aac-73e0-9a1d-d65f61bcde51.jsonl`:
  truncation outputs 18/112; recovery calls 22/29/116; final source verification
  output 376, prepare 385, publication 392 and handoff 397.
- Specialist `rollout-2026-09-27T11-03-32-01a0e21a-f37c-7f41-862c-d4fb64a6b14c.jsonl`:
  source rejection 105, source reread 111, anchor correction 118, passing check
  127; amended absence searches 173, warning and explicit probe results 176,
  amendment 180 and final source-check call 185.

## Comparison-reader check

All three existing readers succeeded with only these explicit review arguments:

```text
--review kb/agentic-systems/reviews/dynamic-cheatsheet.md
--review kb/agentic-systems/reviews/mem0.md
--review kb/agentic-systems/reviews/napkin.md
```

Run `uv run python scripts/build_systems_matrix.py` and
`uv run python scripts/render_systems_table.py` with those arguments and
`--output` paths under `kb/reports/cache/agentic-memory-refresh/rerun-20260927/`.
Run `uv run python scripts/analyze_matrix.py` with the same review arguments,
capturing successful stdout as `statistics.txt`. This check produced three
code-grounded rows; each row's `analysis_run` and retained-result hash matched
the completed run. Every captured statistics input hash matched its file.
All three reviews, retained results, the generated table and the two workshop
Markdown files passed full validation cleanly. CSV validation preserved 166
rows: three complete, 159 pending and four historical predecessors.

| Regenerable output | SHA-256 |
|---|---|
| `matrix.csv` | `a6a9ac327e624bcdb359cbbac0288a28b4b8c62bd016c1921b23cedbf29d0ad4` |
| `table.md` | `e6be3c811a255b111193312d4bd749b5379624140ca6b8bf00ab4ed0348cd162` |
| `statistics.txt` | `9cc41dadbef66a1aa9f30e0636cbbf955f4f76cdd10936b0641f84ee721dce32` |

Spot checks recover automatic writing in three selected systems and push in
two, from per-value strong evidence. These are positive counts, not absence
claims about the remainder. Partial profiles and weaker evidence remain
separate. No new narrative synthesis was commissioned for this replay; previous
synthesis and comparison snapshots remain historical.

## Interpretation and limits

The six workers used `gpt-6-astra`. The producer instruction remained at SHA-256
`75f4ac90c1de0283d36f1a36c26c3478e0f74f1b31d1c0af92d4006fc093fdf8`;
the memory instruction remained at
`4c5ae2555eda3623f12c02d062dd37d1634ddc3b17d0cac48e14e0f58f580743`.
No producer code, source checkout or historical retained result was changed by
this replay. New published results remain exact frozen records.

The early checker caught two citation mistakes before publication. Serial
scheduling encountered no thread-limit failure. No quote-serialization,
communication, publication or cleanup failure was found. These observations
support the bounded repair acceptance; they do not establish reliability for
all source types or for a larger batch.

Avoidable read friction remains: every coordinator's initial whole-skill read
exceeded the orchestration output cap despite a larger nested shell budget.
Later ontology batches also overflowed. The twelve deliveries span eleven
tool-output records, and the necessary omitted passages were recovered with
bounded reads. Future operation should bound reads at the outer output budget.
The invalid Python regex escape is another small remaining execution issue.

The audit matched tool calls to returns, inspected diagnostics and followed
recoveries through final checks. It excluded source-code error strings and
explicit negative probes from actual failures. Some inter-agent message text
is encrypted in session files; this is not a full plaintext message audit or
an independent semantic review of every external-system claim. Parent audit
commands are excluded from the 222 worker-output count. Besides the recovered
Mem0 source read noted above, the parent's broad status listing and combined review diff were truncated;
subsequent reads covered task-scoped paths and the omitted diff spans. No task file was staged or committed
as part of these subsequent reruns.
