# Withheld-instruction review

An experiment for the [separation plan](./separate-analysis-types-from-instructions.md)'s
evidence of completion: can an independent checker recover a job output's
acceptance criteria from the type and contracts alone, without the job
instruction that produced it? The plan names this as a possible means; it is
not a model trial of the analysis method, and it changes nothing.

## Question

Given one accepted analyst report, the type it declares, and the shared
contracts the job loaded, does a reviewer who has never seen the job
instruction or the worker rules state the same acceptance criteria that the
instruction and the code enforce, and judge the report against them? A
criterion the reviewer cannot recover is one that still lives only in the
generation procedure.

## Subject

The epistemic report of run `AAS-2026-10-06-dynamic-cheatsheet-67d9770093c6-01`
(method `8a76fe4b9`, source revision `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`
per the run's `boundary.md`), third version. It went through two correction
rounds and passed the third record verification, which found no blockers. It is
the most-corrected accepted output we have, so a reviewer that finds defects
the verifier missed is informative too.

All files are under the run's worktree, from the repository root:

```
W = .commonplace/worktrees/dynamic-cheatsheet-67d9770093c6
R = $W/kb/agentic-system-analyses/state/AAS-2026-10-06-dynamic-cheatsheet-67d9770093c6-01
```

The worktree's types and contracts are byte-identical to `main`'s at the time
of writing (2026-10-06), so the reviewer reads the worktree's copies and the
experiment is self-contained.

## Given to the reviewer

| Role | Path |
|---|---|
| Report under review | `$R/epistemic-report-2.md` (17.8 KB) |
| Its type | `$W/kb/agentic-system-analyses/types/agentic-system-epistemic-report.md` and `.schema.yaml` |
| Record contract | `$W/kb/agentic-system-analyses/instructions/agentic-analysis-records.md` |
| Source contract | `$W/kb/agentic-system-analyses/instructions/agentic-analysis-sources.md` |
| Collection contract | `$W/kb/agentic-system-analyses/COLLECTION.md` |
| Boundary and Source register | `$R/boundary.md` |
| Runtime report the epistemic report cites | `$R/runtime-report-0.md` |
| Frozen source | `$W/related-systems/suzgunmirac--dynamic-cheatsheet/` (read-only) |
| Form for the verdict | `$W/kb/agentic-system-analyses/types/agentic-system-verification.md` |

These are exactly the files the epistemic job loads, minus the two withheld
below, plus the verification type so the verdict has a form.

## Withheld

Nothing under `$W/kb/agentic-system-analyses/instructions/analyse-agentic-system/`:
the job instructions (`jobs/epistemic.md`, `jobs/verify.md`, the others), the
worker rules and the skill. Also withheld: the run's earlier report versions,
request packets, answers, changes files and verifications, and the memory and
reconciliation members. The reviewer judges one report from its contracts.

## What the reviewer produces

One file in the main checkout,
`kb/work/analyse-agentic-system-amendments/withheld-instruction-review-result-<model>.md`,
with:

1. Its model identifier and reasoning-effort setting, as the harness reports them.
2. **Recovered criteria.** The acceptance criteria it derives for this report
   from the given files alone, each with the file and passage it rests on,
   split into deterministic (a program could check it) and semantic.
3. **Verdict.** A judgment of the report against those criteria, in the
   verification type's form: a `## Verification` account and a `## Blockers`
   list that is `none` or one entry per defect with full IDs, passage, what is
   wrong and the evidence.
4. **Gaps.** Judgments it could not make because no given file states a
   criterion for them, and anything in the report whose purpose it could not
   tell from the contracts.

## Scoring, done afterwards by the coordinator

Compare the recovered criteria with the operative set below. Each operative
criterion is recovered, partly recovered, or missed; each missed one is
misplaced unless it is procedure. Compare the verdict with
`$R/verification-2.md` (no blockers) and `$R/verification-1.md` (the last
blocker the analyst answered): a blocker the reviewer raises on a passage the
verifier accepted is read against the source before it counts for either side.

Operative criteria for an epistemic report, with where each lives now:

| Criterion | Deterministic? | Lives in |
|---|---|---|
| Frontmatter identity: `type`, `description`, `run-id`, `reviewed-boundary` match the run | yes (schema, `identity_refusals`) | epistemic type |
| Declares only `EPI-` records; keeps supplied `RT-` and `SRC-` IDs unchanged | yes (`pass_refusals`) | record contract 16–45 |
| Every cited ID resolves: own declarations, runtime records, Source register | yes (`set_record_errors`) | record contract |
| Quotations are blockquotes with `> ---` attribution and occur once in the frozen source | yes (`verify_quote_anchors`) | source contract 62–88 |
| Prose anchors cite paths without line ranges | yes (type rule) | source contract |
| Numbered `SRC-*` ranges are not written | yes | record contract |
| Ledger rows well formed; route function, architectural status and content/update relation take controlled values | yes (`epistemic_ledger_errors`) | epistemic type 130–195 |
| `Part of:` well formed, names one declared parent, not itself | yes | record contract 69–93 |
| Required blocks present in order; empty-ledger form when nothing is material | yes (schema) | epistemic type |
| Materiality: which routes belong in scope | semantic | epistemic type 36–46 |
| Checking order for content/update relations; ampliative needs non-entailment evidence | semantic | epistemic type 184–186 |
| Evidence layer stated per finding; design claims not promoted to implementation | semantic | source contract 45–58 |
| Supported positives kept beside unresolved included parts; no bundled negative; faithful uncertainty acceptable | semantic | record contract 188–235 |
| Theory-builder conditions, learning, reflection, autonomy, self-improvement assessed independently | semantic | record contract 253–320; epistemic type 95–103 |
| Comparison with supplied records before declaring; `Part of:` only for a part of exactly one supplied record | semantic | record contract 69–87 |
| Coverage table and explicit unassessed limits retained | semantic | epistemic type |
| Bounded conclusion holds only findings that change the answer | semantic | epistemic type 193 |

Procedure that the instruction carries and the reviewer is not expected to
recover: trace CLI dispatch, hooks and registered tools against the runtime
account; name target and domain before judging an evaluator; trace a concrete
input through a deterministic transformation. If the reviewer states one of
these as a criterion anyway, note it; it is not a miss either way.

## Record of runs

| Date | Model / effort | Result file | Recovered / partial / missed | Verdict vs verification-2 |
|---|---|---|---|---|
| | | | | |
