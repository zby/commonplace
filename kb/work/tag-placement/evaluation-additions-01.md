# Evaluation additions, first chunk

## Scope and decision

On 2026-09-27 the operator requested the next chunk. This pass reads the first
ten open addition entries, in stable queue order, that propose evaluation.
All ten meet the unchanged head: they substantively explain what a check,
judge, comparison, or experiment can establish. ADD-041 also proposes
type-system, which is checked and accepted in the same pass.

This is a placement decision, not an endorsement or fresh factual review of
the notes' claims. Existing uncertainty, historical statements, and TODOs
remain unchanged. No note body or tag head changes.

## Accepted entries

| Entry | Note | Reason |
| --- | --- | --- |
| ADD-001 | [A better-factory claim compares operative states under an antecedent assessment relation](../../notes/a-better-factory-claim-compares-operative-states.md) | The note fixes the comparison states, antecedent assessment relation, non-regression scope, and evaluator role needed for a better-factory claim, and separates passing that comparison from attribution of learning. |
| ADD-003 | [A claim without external assessment carries three obligations](../../notes/a-claim-without-external-assessment-carries-three-obligations.md) | The note specifies external falsifiers, independently assessed performance, and the support needed for a proposed use. It explicitly distinguishes outcome measurement from causal attribution and internal approval. |
| ADD-010 | [A proximate target is checked for achievement, not for warrant](../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) | The note separates checking a proximate target's achievement from testing whether that target serves the improvement objective. It explains the independent outcome evidence needed to test the linking claim. |
| ADD-020 | [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) | The note separates rendering a draft from judging it, explains the role and competence limits of adversarial checks, and states what would refute the claim that the loop reconstructs the writing filter. |
| ADD-023 | [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) | The behavioral-faithfulness section requires WITH/WITHOUT comparisons, perturbations, or trace audits to establish that activated memory changes action. Delivery alone is explicitly insufficient. |
| ADD-025 | [Evaluate Memory By Effects, Not By Existence](../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) | The note separates retrieval, activation, behavioral uptake, and final outcome, then maps those distinctions to tests and causal limits. Its evaluation subject is the intended effect of memory, not merely its existence. |
| ADD-037 | [An accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) | Human acceptance warrants the local edit, while a mined rule needs separate evidence of generalization. The note develops coupled-edit attribution, overfitting, independent confirmation, and rollback. |
| ADD-040 | [Automated synthesis is missing good oracles](../../notes/automated-synthesis-is-missing-good-oracles.md) | The note compares extraction and synthesis oracles and separates fidelity, novelty, and validity. It identifies what current candidate-generation evidence leaves unevaluated and proposes testable alternatives. |
| ADD-041 | [Automated tests for text](../../notes/automated-tests-for-text.md) | Accept evaluation for the deterministic, rubric, and corpus-testing pyramid and the distinction between testing a generator and its output. Also accept type-system: document type and trait contracts explicitly determine the required checks; document-system is already present as its parent. |
| ADD-044 | [Candidacy evidence licenses escalation to assessment, not acceptance](../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) | The worked idealization and source-grounding cases distinguish evidence that justifies assessment cost from evidence that warrants a verdict. The note directly analyzes what each check may establish. |

## Parent checks and accounting

The proximate-target note (ADD-010) addresses the objectives and evaluation
that govern self-improvement. Its self-improving-systems assignment remains
supported; add learning-theory and close PG-016. The candidacy-evidence note
(ADD-044) distinguishes pursuit, testing, and acceptance of conjectures.
Its discovery assignment remains supported; add learning-theory and close
PG-039. Automated tests for text already carries document-system, the parent
of its new type-system tag.

This pass adds thirteen assignments across ten notes: ten evaluation, one
type-system, and two learning-theory parents. It removes none. The evaluation
head is selective, so these additions do not require ten new curated entries.
Existing complete parent heads continue to route through the supported children.

The workshop now records 59 accepted addition entries, three duplicate removal
closures, and 144 open additions. All 68 original placement findings remain
resolved. PC-07 has 26 resolved and 103 open parent-gap entries. Original
reviewer words and frozen baseline hashes remain unchanged.

## Verification

`commonplace-validate` passed on all sixteen changed files and on the tags
collection: zero failures and zero warnings. Separate checks confirmed thirteen
additions, no removals, ten unchanged note bodies, six unchanged heads, all
queue counts, and all sixteen recorded final hashes. `git diff --check` passed.
These are direct semantic judgments, not new independent assays. Changes
remain uncommitted.

## Checked versions

SHA-256 hashes identify the ten note inputs and the six heads read for this
pass. Unchanged hashes record the heads, whose scopes were applied as written.

| Artifact | Before | After |
| --- | --- | --- |
| `kb/notes/a-better-factory-claim-compares-operative-states.md` | `fee44e85e300871969d4f5f663a140dcdc7fe28cbf440139c200695721187ccd` | `347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc` |
| `kb/notes/a-claim-without-external-assessment-carries-three-obligations.md` | `91ff51e4f24621fab693e353863e89912ae0ea6e4ee63fc5e9cc5f1986e28522` | `42701287945fdf8926164b2c529775858a48bf2c7cdd8f8aebaa1732ed68d9b8` |
| `kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md` | `5fe81dc4aadb63a6db583250bbaec3c55a3c66ae05de0f648cbf588f23793626` | `6051519acd7c29c8f4e324d82a992f68a074f375d1554f33c86de81a87b6e55c` |
| `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` | `44b8c0625fed66dd3fdb6f84aa0e7685d0990b7999db1965c9493a678a711c61` | `8b06470125f563ea1ffa8472ed8ef3d7c5b7e5d6c7e140332225e7404aef4213` |
| `kb/notes/agent-memory-requirements/activate-behavior-changing-memory.md` | `61b4a1300b17f00967afcb7816c005982e780205266b2c8b0591c0f60ac5d596` | `34ba57291e89ed23d5d799dd3e3233cc30f0b7a428a77b7d818383e60865ef8e` |
| `kb/notes/agent-memory-requirements/evaluate-memory-by-effects.md` | `2b2f2ae5fa087350b792950e9cc90c4dde5af17495a06c626e5f23fea1a89d6f` | `7c252df3e42a4278f0ef4aa35e482eefa81fac726ec78e39943f70fefb243045` |
| `kb/notes/an-accepted-edit-verifies-the-change-not-the-rule.md` | `b612bcc948d8bb072d1befea9efa4580f3e8ae88f15d15683f1e2056f1390287` | `965f85f341b333a39bca436041c3a3e01a36563901c2f704bc90265ba4a490fb` |
| `kb/notes/automated-synthesis-is-missing-good-oracles.md` | `abdd9b20c205731070d8ebd57c0cdaf119b10598e76d87a266ad0f49fed89d63` | `2e4fb32c7d5cde9be44c44e3fa1cd36449c88b95382d1d436f1bd21ed6416e8e` |
| `kb/notes/automated-tests-for-text.md` | `56b67349c428d69d0142e866a9c14ed98944c5df511425f9f886409e2e618952` | `1ac631b245a0d6388e5e4a488a6c41169e8a4d85a571ff55d4817961502899d7` |
| `kb/notes/candidacy-evidence-licenses-escalation-not-acceptance.md` | `f704f3372bb8154505c78e710e4f0d1a52a50b7367738a17a9d1ac43009c7c3c` | `1a9bed037d05ab83516b54aa6314e97b8e3c1569a06d93894a1ff42ae749566a` |
| `kb/tags/evaluation-README.md` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` |
| `kb/tags/type-system-README.md` | `684298973c1787bb2740278e2cf7b1cfd33cf6ac264cb20b76e7e562c97beb03` | `684298973c1787bb2740278e2cf7b1cfd33cf6ac264cb20b76e7e562c97beb03` |
| `kb/tags/document-system-README.md` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` |
| `kb/tags/self-improving-systems-README.md` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/discovery-README.md` | `3bba07121cedd3c664aff434dc42ea2b5e46c8590152194bab942b145a58f881` | `3bba07121cedd3c664aff434dc42ea2b5e46c8590152194bab942b145a58f881` |
