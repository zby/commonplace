# Score the frozen synthesis distinction trial

Coordinator/scorer only. Do not put this file, historical reviews or expected
answers in worker packets. Judge support from frozen records and source,
not by matching favored wording. No results have been recorded yet.

## Evidence behind the target

The target is the collapse of model-requested assessment into no assessment,
or the reverse collapse of requested assessment into verified correctness.
Inspect these frozen paths, available inside `frozen-input.json`:

- `records/runtime.md`, `RT-RTE-retrieval-synthesis`: curator model selection,
  prompt-guided admission, no independent answer oracle and no operation trace.
- `source/prompts/curator_prompt_for_dc_retrieval_synthesis.txt`: the section
  “Evaluate the Solution’s Effectiveness” and direction to prioritize accuracy.
- `source/dynamic_cheatsheet/language_model.py` and `source/run_benchmark.py`:
  distinguish retrieved pairs entering the curator from synthesized text
  reaching the generator, and locate downstream benchmark evaluation.
- `records/runtime.md`, `RT-RTE-direct-retrieval`: no curator call and selection
  by cosine top-k; distinguish this route from retrieval-synthesis.

Do not say the runtime record itself contains the explicit accuracy wording.
Do not treat similarity ranking as correctness assessment, a curator prompt
as proof it assessed correctly, or later benchmark scoring as a pre-inclusion
gate. The original sentence is overbroad across routes and leaves “inclusion”
ambiguous. A defensible rewrite can narrow the stage rather than use the
example wording. Check its actual scope.

## Main pipeline measures

Score each first-round synthesis independently of its reviewer verdict:

| Field | Values and interpretation |
|---|---|
| Target fidelity | preserved: mechanism and assurance limit are both accurate; contradicted: absence or verified-success overclaim; omitted: distinction removed rather than expressed; ambiguous: wording does not resolve the distinction |
| Target evidence | exact output passage plus record/source locator supporting the judgment |
| Review catch | explicit target blocker; mentioned without blocker; missed; no target error present |
| False acceptance | reviewer says `none` while scorer finds a target contradiction; other unsupported claims counted separately |
| Coverage | supplied overview requirements retained; material omissions enumerated with exact passages/requirements |
| Other errors | each supported non-target error or false reviewer objection, separately adjudicated |
| Evidence use | record-only; source inspected (name files); unavailable from trace |
| Process | format failure, problem report, budget exhaustion, contamination or infrastructure error; none |
| Cost | wall seconds; input, cached input and output tokens if supplied; call count |

Main comparison: first-draft distinction fidelity in the one planned pipeline
per arm, with incomplete jobs shown rather than silently excluded. Report
whether each reviewer explicitly blocks a target defect or falsely accepts
one. There is no corrected or final synthesis in this check.
Do not call omitted discussion a preservation success. A shorter output that
evades the issue may reduce target contradictions while failing the intended
contribution. Judge whether omission also violates the overview contract.

Reviewer detection in the main pipelines is conditional on a target defect
actually appearing. Its denominator may differ by arm; this is why the fixed
review diagnostic exists. A treatment reviewer seeing a better draft cannot
demonstrate better detection on its own.

## Fixed-draft expected judgments

| Case | Target sentence disposition | What counts as success |
|---|---|---|
| original | Unsupported blanket absence | Explicit blocker identifies the retrieval-synthesis qualification and requested-versus-validated distinction |
| qualified | Supported mechanism plus assurance limit | No objection claiming the assessment is absent or independently validated; reasonable requests about citation precision scored separately |
| bounded-absence (outside this check) | Supported absence on direct retrieval only | Does not reject the claim merely because another route has a curator |
| implicit-overclaim (outside this check) | Same blanket absence without the original wording | Explicit blocker preserves the same distinction; a vocabulary-only detector is insufficient |

For each response record target verdict (blocker / discussion only / accepted
or unmentioned), evidence accuracy, unsupported objections, and non-target
findings. A whole-document `none` is not required for either supported control.
For this check, report the original-case catch and qualified-case false
objection separately for each arm. Each case has one response per arm; do not
turn those two responses into a reliability rate. The other two candidate
cases remain unrun.

## Decision rule and stopping

Attempt the eight-call schedule subject to the documented stop conditions;
report calls that could not run. Do not add cases, corrections or repetitions
after viewing a near miss. Do not adopt based only on the target disappearing
or a reviewer producing more text. A promising feasibility signal requires
the treatment writer to preserve the distinction and the treatment reviewer
to catch the known original defect without falsely objecting to the qualified
case or losing material coverage. Show trade-offs instead of collapsing them
into one score. Ties, few reproduced errors or mixed effects remain
inconclusive. Any reliability claim needs a separately specified trial.

The operator adjudicates disputed source support before the conclusion is
used for method adoption. Changing either treatment paragraph after trials
begin creates a new version; preserve all old prompts, outputs and scores.
