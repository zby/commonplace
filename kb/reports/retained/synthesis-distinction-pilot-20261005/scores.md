# Scores for the synthesis distinction feasibility check

Scored on 2026-10-05 against the frozen records and source, using the
[predeclared guide](./protocol/scoring.md).
Writer drafts were first read as A and B; the mapping was revealed after
initial target scoring. A was control and B was treatment. Reviewer responses
exposed the condition and were not blind. Each linked output is the exact
retained response, not a revised synthesis.

## Claim adjudication

The target distinction is between **a curator prompt asking a model to assess
solution effectiveness and accuracy** and **an independent correctness check
before the resulting text is used**. The frozen `records/runtime.md`,
`RT-RTE-retrieval-synthesis`, describes retrieved pairs being passed to a
curator, with no expected-answer filter or pre-inclusion oracle. The frozen
`source/prompts/curator_prompt_for_dc_retrieval_synthesis.txt`, lines 35–39,
explicitly says “Evaluate the Solution’s Effectiveness” and asks whether the
strategy was optimal or could improve; line 85 prioritizes accuracy. The
source `language_model.py` sends that prompt and extracts tagged text without
independent validation; `run_benchmark.py` scores answers downstream. These
files are pinned in the [frozen bundle](./protocol/frozen-input.json).
The prompt's request is evidence of an instruction, not proof that the model
assessed correctly. Direct retrieval has no curator and needs a separate
description.

| Main pipeline | Writer target fidelity | Reviewer response | Material coverage |
|---|---|---|---|
| Control | **Omitted.** [Draft](./attempts/v2/r1-control-write/output.md) says retrieval ranks pairs by cosine and “does not select on answer correctness,” then describes downstream benchmark scoring. It never describes retrieval-synthesis curator assessment versus independent validation. | [Review](./attempts/v2/r1-control-review/output.md) returned `none` and did not flag the omission. No target contradiction exists to count as false acceptance. | Omitted required separate discussion of theory-builder conditions 1–4, criticism improving future capacity, reflection, autonomy, self-improvement and scenario-relative assessment. |
| Treatment | **Omitted.** [Draft](./attempts/v2/r1-treatment-write/output.md) says other routes can “synthesize selected examples into prompt text,” but places “The prompt requests correctness assessment” in its cumulative-mode paragraph. It does not state the retrieval-synthesis prompt's assessment request or lack of independent validation. | [Review](./attempts/v2/r1-treatment-review/output.md) did not flag the target omission; it raised a separate parser blocker assessed below. | The same overview-contract topics are absent. Extra paragraphs on execution tools do not replace them. |

The frozen `method/overview.md` lines 74–90 require the bounded synthesis to
state those theory, criticism, reflection, autonomy, self-improvement and
scenario-relative findings separately where supported. The supplied records
support bounded negative findings, as the historical fixed draft demonstrates.
Both main reviewers called coverage adequate despite these omissions. Neither
draft preserves the intended contribution merely by avoiding the historical
overclaim.

The treatment main reviewer blocked the sentence “The parser accepts text
marked with `<cheatsheet>` and otherwise retains the old text,” arguing it
implies a closing marker is required. The frozen `extractor.py` lines 77–86
requires an opening marker and accepts the remainder if no closing marker
appears. The writer named only the opening marker, so its sentence is
consistent with the implementation; the asserted implication is unsupported.
This is scored as a **non-target false objection**, though spelling out the
missing-closing-marker case would make the description clearer. The control
main review had no blocker. No other supported non-target error was found in
this bounded score; this is not an exhaustive audit of every claim.

## Fixed-draft diagnostic

The original case contains the blanket sentence “None checks prior outputs
for correctness before inclusion.” The qualified case replaces only that
sentence with a route-specific distinction. Both retain the rest of the
historical draft unchanged. Exact candidate bytes are in the packets under
[`attempts/v2/`](./attempts/v2/).

| Case and arm | Target judgment | Result |
|---|---|---|
| Original, control | [Review d1](./attempts/v2/r1-d1/output.md) returned `none` without discussing the blanket claim. | Missed known overclaim: 0 of 1 catch. |
| Original, treatment | [Review d2](./attempts/v2/r1-d2/output.md) called the blanket sentence supported from cosine or sequence selection, omitting the retrieval-synthesis curator's requested assessment. | Explicit false acceptance: 0 of 1 catch. |
| Qualified, treatment | [Review d3](./attempts/v2/r1-d3/output.md) identified the curator prompt's effectiveness/accuracy request and lack of independent validation; `none`. | Accepted supported target: 0 of 1 false target objection. |
| Qualified, control | [Review d4](./attempts/v2/r1-d4/output.md) blocked the claim that the prompt requests solution-effectiveness assessment, despite the prompt's explicit section at lines 35–39. | False target objection: 1 of 1. |

These four calls do not measure reviewer sensitivity or specificity. One
supported qualification was accepted by treatment, but the critical original
defect was not caught by either arm. The original-case treatment reviewer
inspected several source files but did not inspect the retrieval-synthesis
curator prompt; the qualified-case reviewers did inspect that prompt. This
trace difference is descriptive, not an isolated causal explanation.

## Execution and evidence use

All jobs used `gpt-6-luna` at medium effort with fresh isolated sessions,
Codex CLI 0.160.0, a 1,800-second time limit and a 1,000,000-token reported
input-plus-output ceiling. Input bytes stayed unchanged. In the table,
“source” means a command in the raw trace mentioned a path under
`inputs/source/`; it does not establish that every relevant line was read.
Tokens are cumulative reported job usage, including cached input.

| Job | Wall seconds | Input / cached / output tokens | Total | Source access in trace |
|---|---:|---:|---:|---|
| [Control writer](./attempts/v2/r1-control-write/result.json) | 34.43 | 197,834 / 155,648 / 1,183 | 199,017 | README, language model, extractor, benchmark |
| [Treatment writer](./attempts/v2/r1-treatment-write/result.json) | 52.05 | 363,929 / 314,624 / 2,228 | 366,157 | README, language model, extractor, executor, benchmark |
| [Treatment main reviewer](./attempts/v2/r1-treatment-review/result.json) | 42.96 | 210,019 / 163,840 / 1,930 | 211,949 | Record-only |
| [Control main reviewer](./attempts/v2/r1-control-review/result.json) | 38.93 | 261,265 / 213,760 / 1,660 | 262,925 | Language model, benchmark |
| [Original control reviewer](./attempts/v2/r1-d1/result.json) | 24.70 | 154,775 / 110,848 / 866 | 155,641 | Record-only |
| [Original treatment reviewer](./attempts/v2/r1-d2/result.json) | 67.39 | 327,951 / 278,016 / 3,006 | 330,957 | Multiple source files, no retrieval-synthesis curator prompt |
| [Qualified treatment reviewer](./attempts/v2/r1-d3/result.json) | 52.04 | 215,133 / 165,888 / 2,450 | 217,583 | Retrieval-synthesis curator prompt and other source files |
| [Qualified control reviewer](./attempts/v2/r1-d4/result.json) | 19.82 | 205,253 / 160,768 / 612 | 205,865 | Retrieval-synthesis curator prompt |
| **Eight calls** | **332.32** | **1,936,159 / 1,563,392 / 13,935** | **1,950,094** | — |

These are operational costs for this packet and delivery version, not a
forecast for production. The version 1 over-budget call and initial
infrastructure failure are additional attempts described in the
[execution record](./README.md). No correction rounds or extra diagnostic
cases were run. The decision rule required treatment target preservation and
an original-case catch without a qualified-case false objection or material
coverage loss. It therefore fails here. Further repetition or revised wording
would require a new decision and plan, not post-hoc extension of this pilot.
