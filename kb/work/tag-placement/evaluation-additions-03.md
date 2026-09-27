# Evaluation additions, third chunk

## Scope and decision

On 2026-09-27 the operator requested the next chunk. This pass reads the next
ten open evaluation suggestions in stable queue order. All ten qualify under
the existing head. Four suggested neighboring assignments also qualify:
warranted-autonomy on oracle accumulation, and constraining on oracle strength,
process versus output structure, and technical constraints on KB objectives.

This is a metadata placement decision, not a new assessment of the notes'
truth or source grounding. Note bodies, inclusion rules, original reviewer
words, and frozen baselines are unchanged. One curated link is added to keep
the warranted-autonomy head complete.

## Accepted entries

| Entry | Note | Reason |
| --- | --- | --- |
| ADD-122 | [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) | Accept evaluation: the note explains how noisy, delayed, composite, and misaligned outcome signals limit feedback-trained policy updates, and what a controlled comparison would need to isolate oracle quality. |
| ADD-134 | [Open-ended improvement must allocate search before decisive evaluation is available](../../notes/open-ended-improvement-allocates-search-before-evaluation.md) | Accept evaluation: the note separates provisional branch evidence from criterion-relative adoption evidence and explains why even a proof gate cannot evaluate branches search never reaches. |
| ADD-137 | [Oracle accumulation improves selection for later candidates in its maintained domain](../../notes/oracle-accumulation-improves-the-selection-environment.md) | Accept evaluation and warranted-autonomy: regression coverage is distinguished from evidence that a check discriminates beyond its originating case; held-out incidents, fault injection, adversarial cases, calibration, and monitoring condition expansion of warranted evaluation autonomy. |
| ADD-138 | [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) | Accept evaluation and constraining: the oracle spectrum distinguishes what checks can establish, while schema validation and mined deterministic rules explicitly replace softer interpretations with enforceable criteria. |
| ADD-143 | [Process structure and output structure are independent levers](../../notes/process-structure-and-output-structure-are-independent-levers.md) | Accept evaluation and constraining: the note explains how result-form and process constraints narrow different interpretation spaces and identifies experimental contrasts and ablation limits needed to separate their effects. |
| ADD-147 | [Quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md) | Accept evaluation: the note develops candidate structural and LLM-based quality signals, their calibration, independence, and Goodhart limits, and before/after checks on KB mutations. |
| ADD-149 | [Reliability dimensions map to oracle-hardening stages](../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) | Accept evaluation: the note maps reliability dimensions to distinct verification questions and contrasts aggregate calibration with per-instance discrimination. |
| ADD-156 | [Selecting an LLM output fixes a result, not its interpretation](../../notes/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) | Accept evaluation: generator tests and selected-artifact tests have different targets and license different inferences; the note states the discrimination, time, and cost conditions for artifact filtering. |
| ADD-167 | [Structured-prompt gains do not establish training-distribution selection](../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) | Accept evaluation: matched heading-only, process-only, combined, and unstructured prompts are proposed to distinguish causal explanations, with task accuracy measured separately from format compliance. |
| ADD-172 | [Technical constraints turn KB objective-function choice from philosophy into engineering](../../notes/technical-constraints-make-kb-objective-choice-engineering.md) | Accept evaluation and constraining: the note compares evidence and oracles for reference descriptions, instructions, and theory, and develops codification as a change from natural-language interpretation to formal checks. |

## Parent checks and accounting

Three original learning-theory gaps close after checking the supporting tags:

- PG-091 / ADD-134: allocating search before decisive acceptance directly
  concerns improvement-loop and its self-improving-systems parent. Both were
  already present; learning-theory was missing.
- PG-092 / ADD-138: oracle manufacture, amplification, and monitoring concern
  machinery for detecting and correcting LLM output deviations, fitting
  llm-reliability. The newly added constraining tag also requires learning-theory.
- PG-102 / ADD-149: consistency, robustness, predictability, and bounded failure
  concern detection and correction of unreliable agent output, fitting
  llm-reliability.

Four more parent assignments are required outside that frozen inventory:
learning-theory for the new constraining assignments on ADD-143 and ADD-172,
and document-system for the existing type-system assignments on ADD-143 and
ADD-167. Both type-system assignments fit its explicit coverage of the effects
of prescribing document structure: the former separates process and result
requirements, and the latter tests proposed explanations of structured-prompt
gains. These are document-structure cases, so they do not require settling the
broader document-system versus architecture boundary.

ADD-137 already carries self-improving-systems and learning-theory, the parents
of its new warranted-autonomy assignment. ADD-122 and ADD-156 already carry
the parents of their existing children. Evaluation itself does not require a
learning-theory parent assignment.

This pass adds twenty-one assignments across ten notes: ten evaluation, three
constraining, one warranted-autonomy, five learning-theory, and two
document-system. No assignments are removed. The warranted-autonomy head gains
one curated entry to preserve its completeness mark; the other heads are
unchanged.

The workshop now records 79 accepted addition entries, three duplicate removal
closures, and 124 open additions. All 68 original placement findings remain
resolved. PC-07 has 32 resolved and 97 open parent-gap entries. Its frozen
inventory does not expand to count the four other parent additions in this pass.

## Verification

`commonplace-validate` passed on all seventeen changed files and the tags
collection: zero failures and zero warnings. Separate checks confirmed
twenty-one added assignments, no removals, ten unchanged note bodies, eight
unchanged heads, queue counts, and all nineteen recorded final hashes. The
remaining head change adds only the new curated member. `git diff --check`
passed.
These are direct semantic judgments, not new independent assays. Changes
remain uncommitted.

## Checked versions

SHA-256 hashes identify the ten note inputs and nine heads used. Only the
warranted-autonomy head changes, by adding its new member to the curated list.

| Artifact | Before | After |
| --- | --- | --- |
| `kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md` | `425af4870ae2a25d29abf3cf80abfd13b469fe3744b2d0c26ab3ebbfc6820e82` | `5c0c2925678d0fd01c47ae7bf1ffab71f240eb37d71aeec1a0b9ee2b0e6e58fb` |
| `kb/notes/open-ended-improvement-allocates-search-before-evaluation.md` | `5b4ef3b7bc8ea2f281980203510411e94b90cfb2a2aeaf2999f433977d168cfa` | `24f8c766cbce308a5e4a4a57c83e5472ce76379804c71f89161c0dcab16ce2e9` |
| `kb/notes/oracle-accumulation-improves-the-selection-environment.md` | `3eb74f15b68a64eae1c427f82561d1301c4248f9d483a8d61c054c723d31416f` | `9dc55a1de80408aa449ce646d9dbf61cfb8072c65599c3efb336ee1c6dd67fab` |
| `kb/notes/oracle-strength-spectrum.md` | `89cc6024636ca6935c869599dae57a975ac687263792a5b76f18107dfffe669a` | `46ec73902f1248162566b78a68c2ff6b8dcf079275ab727dde87ca5fc62afc9f` |
| `kb/notes/process-structure-and-output-structure-are-independent-levers.md` | `5b4731161351b4600d7bf82a534148220ac9bea41ea6c678cf7b48964dee15d9` | `334bc3aae0466f49fc1280743ee03eed53f7662f5f9b56c07dc3622851148e4c` |
| `kb/notes/quality-signals-for-kb-evaluation.md` | `ed15deacdd40055d13ee0f315c64e85b025f8a9a4344dedf4fb49bf3754b387c` | `9a3e58eed969cbd53d8770c50e59f745b6c4e5d73b3fd9d9e1ae3eda2862ed42` |
| `kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md` | `6df096fbb550b782a4edf5b4d5f705e9fab7876550810ccfa646341052fff5ef` | `0b384c736f716c416ffe3b8e2c4a610216ec0c8ed572ea394a347544a8061075` |
| `kb/notes/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md` | `c8b7ddb34fc2f198cfdb245922e8ebb2616b699a1b4ea0a2743fcb3f5c42f60d` | `1217d877a6399427f6a263a95ef5b40c720c55868ca8b83abb17e083abb0b859` |
| `kb/notes/structured-prompt-gains-do-not-establish-distribution-selection.md` | `76b2c7e8c25489dd0aec8393b5b68fbe0166e4495deefa6656e2b35236ce3291` | `a4c48c73b889483ef80cd5631ebab7012a03782754378881d9786d88f4119939` |
| `kb/notes/technical-constraints-make-kb-objective-choice-engineering.md` | `13520c0bae8be4df6d42baf2d8bed78d950d394c4f264ed7135e3585e8f678b5` | `0e213aa80d3c00c71f507c15a0aeec7bf25d33a65cc00baced41189ab2c114a8` |
| `kb/tags/evaluation-README.md` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` |
| `kb/tags/warranted-autonomy-README.md` | `b7c7590800aa6bf9996ecd60ecffb8e9e322902bc85912001193e96486cf12db` | `78b46df20e0dcdf40f468f6441484a4739abbfd31f1baf77bf7488cbb3d6a888` |
| `kb/tags/constraining-README.md` | `70c60b9b0b6607144d278ef47998a8fded1381089a4e7e95b04014d1583a232e` | `70c60b9b0b6607144d278ef47998a8fded1381089a4e7e95b04014d1583a232e` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/self-improving-systems-README.md` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` |
| `kb/tags/llm-reliability-README.md` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
| `kb/tags/improvement-loop-README.md` | `d52cb75a943a852508c0d6d52e024ae68870608916209a3225510dda44f63f1f` | `d52cb75a943a852508c0d6d52e024ae68870608916209a3225510dda44f63f1f` |
| `kb/tags/type-system-README.md` | `684298973c1787bb2740278e2cf7b1cfd33cf6ac264cb20b76e7e562c97beb03` | `684298973c1787bb2740278e2cf7b1cfd33cf6ac264cb20b76e7e562c97beb03` |
| `kb/tags/document-system-README.md` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` |
