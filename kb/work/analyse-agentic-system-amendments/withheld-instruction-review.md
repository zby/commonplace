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
| 2026-10-06 | `gpt-6-luna`, Pi; effort not exposed to the model (medium per the session) | [result](./withheld-instruction-review-result-gpt-6-luna.md) | 7 / 5 / 5 of 17 | No substantive defect found, agreeing with `none`; one blocker, a false positive |
| 2026-10-06 | `gpt-6-luna`, Pi, medium; subject: run `947b5c8445a4`'s `epistemic-report-0.md`, never corrected | [result](./withheld-instruction-review-result-gpt-6-luna-947b.md) | 9 / 4 / 4 of 17 | One blocker on a passage the run's verifier accepted; source-accurate and arguable, see below |

## Results: gpt-6-luna, 2026-10-06

Scored against the operative table by the coordinator (`claude-fable-5-1`).

**Recovered (7):** frontmatter identity; cited IDs resolve; ledger controlled
values; required blocks in order; evidence layer per finding without promoting
design to implementation; coverage table with unassessed limits; quotation
form (blockquote with attribution, matching the frozen source).

**Partial (5):** `EPI-` prefix stated, keeping supplied IDs unchanged only
implied; quotation uniqueness not stated; materiality named as "material
operative part" without the type's test; coverage and uncertainty rules
stated as "no unsupported negatives or completeness" without the no-bundled-
negative rule; bounded conclusion as "within evidence" without "only findings
that change the answer".

**Missed (5):** prose anchors carry no ranges; numbered `SRC-*` ranges refused;
`Part of:` form and semantics; comparison with supplied records before
declaring; theory-builder, learning, reflection, autonomy and self-improvement
assessed independently (the reviewer's Gaps section says no criterion requires
them; the record contract's Theory account does, conditionally).

**Misplaced criteria: none.** Every missed criterion is stated in a file the
reviewer was given (record contract sections Identity and grammar, Record
fields, Theory account; epistemic type checking order). The misses are recall
failures on the record contract's relational rules, not criteria that live
only in the job instruction. This is the plan's test, and it passes for this
report.

**Verdict.** The reviewer checked the load-bearing quotations and code claims
in the frozen source and found no substantive defect, agreeing with
`verification-2.md`. Its one blocker, that anchors such as `run_benchmark.py`
and `README.md` lack a full commit-relative path, is a false positive: the
source contract's anchor rule says "A basename denotes a repository-root file",
and both are root files; the report has no bare `language_model.py` or
`extractor.py` anchors (checked by search) and its attributions use full paths.
The reviewer quoted the rule without that sentence. Three of the report's
earlier defects (the `Part of:` containment, the misassigned ledger row) were
already corrected in this version, so the review could not show whether it
would have caught them.

**Side finding.** Pi does not expose the reasoning-effort setting to the model.
The manifest's `effort` therefore has to come from the operator at `start`,
which is how the skill now asks for it; a worker cannot report it.

## Results: gpt-6-luna on the uncorrected report, 2026-10-06

Second subject: the `947b5c8445a4` run's epistemic report, accepted at its
first verification with no blockers. Same reviewer model and conditions.

**Recovered (9):** identity and blocks in order; `EPI-` declarations with full,
unique, resolving IDs; quotation form, anchors and minimum verbatim support;
evidence layers per finding and the interpretation rules; ledger controlled
values; the content/update checking order with indeterminate requiring the
remaining alternatives (missed by the first review); coverage table with
assessed and unassessed limits; bounded conclusion limited to findings
relevant to the question; route fields including conditional fields.

**Partial (4):** materiality (named, not tested); uncertainty rules as "bound
authority to target, domain, consumer, horizon" without the no-bundled-
negative rule; keeping supplied IDs unchanged (implied); independence of
theory-builder and related properties (not named).

**Missed (4):** prose anchors without ranges; numbered `SRC-*` ranges refused;
`Part of:` form and semantics; comparison with supplied records before
declaring. All four are stated in the record contract. Misplaced criteria:
none, as before.

**Verdict.** The reviewer found one blocker where the run's verifier found
none: `EPI-RTE-extract` classifies answer and cheatsheet extraction as
`truth-apt transformation: non-ampliative reshaping` on the strength of a
one-tag example, while `extract_answer` in the frozen
`dynamic_cheatsheet/utils/extractor.py` also has `FINAL ANSWER` and
code-fence branches that select substrings. The source reading is accurate
(checked). Whether substring selection counts as reshaping or leaves the
relation indeterminate under the type's first-established-test rule is a
judgment; the objection is defensible, not a false positive, and the run's
verifier did not raise it. One of two reviews therefore found a plausible
defect the in-run verification let through.

**Across the two reviews:** 14 of 17 operative criteria were recovered or
partly recovered by at least one review; `Part of:`, the comparison with
supplied records and the `SRC-*` range rule were missed by both, and all
three are relational rules in the record contract that neither report
exercised. Pi reported the effort setting in the second run (medium) and not
in the first.

**Limits.** Two reviews by one model of two reports from one system. The recall gaps
cluster on relations between records, which this report happened not to
exercise (it declares no `Part of:` and makes no theory-builder claim), so a
reviewer may simply not have looked for rules it had no occasion to apply.
