# Evaluation additions, fourth chunk

## Scope and decision

On 2026-09-27 the operator requested continued work. Six open evaluation
suggestions remain in stable queue order. All six qualify under the existing
head. The two proposed warranted-autonomy assignments and one proposed
claims-and-grounding assignment also qualify under their respective heads.

This completes the evaluation suggestions in the retained queue, not an
exhaustive missing-tag audit. Placement does not certify the truth of the
notes or reopen their source grounding. Note bodies, inclusion rules, original
reviewer words, and frozen baselines are unchanged. Three curated links keep
the two affected complete heads consistent with their new members.

## Accepted entries

| Entry | Note | Reason |
| --- | --- | --- |
| ADD-173 | [The augmentation-automation boundary is discrimination not accuracy](../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) | Accept evaluation and warranted-autonomy: the note distinguishes aggregate accuracy from per-instance discrimination and uses that distinction to judge when verification can replace human output review. |
| ADD-175 | [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) | Accept evaluation and warranted-autonomy: the note compares hard, soft, and missing verification, asks which automated decisions can replace manual checking, and identifies error tolerance and oracle quality as limits on that argument. |
| ADD-182 | [Theory warrant should be tracked at the finest granularity evidence licenses](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) | Accept evaluation and claims-and-grounding: the note distinguishes what interventions, comparisons, proof, and joint tests warrant, then requires support to remain attached to the specific claim, bundle, and scope the evidence identifies. |
| ADD-196 | [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) | Accept evaluation: the note separates evidence that a decomposition worked locally from tests of transfer, and requires interventions on the stated rationale or varied-context checks to examine the broader claim. |
| ADD-197 | [The verifiability gradient](../../notes/verifiability-gradient.md) | Accept evaluation: the verifiability grades distinguish shape checks, statistical output tests, and deterministic checks, including cases where passing a check fails to establish quality. |
| ADD-202 | [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) | Accept evaluation: the note specifies before-and-after evidence for preferential transfer, contrasts it with cross-sectional observations, and proposes a separate test of the effect on remaining human judgment. |

## Parent checks and accounting

Three original learning-theory gaps close after checking the supporting tags:

- PG-114 / ADD-173: output-error discrimination, external verification, and
  confidence-based escalation substantively concern llm-reliability.
- PG-115 / ADD-175: constructing and applying checks to prevent unreliable
  automated output substantively concerns llm-reliability.
- PG-124 / ADD-202: the note explains conditions and evidence for transferring
  decisions from humans to computation, directly fitting warranted-autonomy
  and its existing self-improving-systems parent.

The two new warranted-autonomy assignments on ADD-173 and ADD-175 also require
self-improving-systems; that parent explicitly includes the child area's
actor-allocation question without asserting that every automated system
improves itself. ADD-182 gains kb-maintenance as the parent of
claims-and-grounding: its evidence-relative bookkeeping governs how retained
claims stay supportable. These three parent additions are outside PC-07's
frozen learning-theory inventory.

This pass adds fifteen assignments across six notes: six evaluation, two
warranted-autonomy, one claims-and-grounding, three learning-theory, two
self-improving-systems, and one kb-maintenance. No assignments are removed.
The warranted-autonomy head gains two curated entries and claims-and-grounding
one, preserving their completeness marks. Parent completeness continues to
route through those children.

The workshop now records 85 accepted addition entries, three duplicate removal
closures, and 118 open additions. All 68 original placement findings remain
resolved. PC-07 has 35 resolved and 94 open parent-gap entries.

## Verification

`commonplace-validate` passed on all fourteen changed files and the tags
collection: zero failures and zero warnings. Separate checks confirmed fifteen
added assignments, no removals, six unchanged note bodies, seven unchanged
inclusion rules, queue counts, and all thirteen recorded final hashes. No
evaluation suggestion remains open in the retained queue. `git diff --check`
passed.
These are direct semantic judgments, not new independent assays. Changes
remain uncommitted.

## Checked versions

SHA-256 hashes identify the six note inputs and seven heads used. Only
warranted-autonomy and claims-and-grounding change, through curated entries.

| Artifact | Before | After |
| --- | --- | --- |
| `kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md` | `550f09291fd3fa222327ad7388d39dbe1969f686c53f856da501befa1f8e0f31` | `972f026788c0ab3961e3bcdd40f2bcef7ff3075220cfe297c89bc29526b506e1` |
| `kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | `411e81ffacadea8e4c38886b246225af554e1dd29db661b9bff25e5e162a9f26` | `a9774760f7a119a64d5094fd1e74557a85a788f785e7a5ed458e71c22711591b` |
| `kb/notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md` | `b31e26526271b45fafb6ef540324ad4c280c5c69eb75659eca10d5537500b0c4` | `c9b4229a636a1931c30c48e337e1352f3c83b08ec3510ee2a1345410aa0ba8ff` |
| `kb/notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` | `f23b5da628802517fa58c7bfe48d135c11e237d7620f78ca10059283e9fd4dcb` | `d4352605ee784b57052cf68660fe8e1f8786648050e0c0f0c1fb3daa22213cb1` |
| `kb/notes/verifiability-gradient.md` | `38f8c0634b3a8397a74cb7fd9088ea71475d9777c9b50fb8f3d1146a75b67761` | `c6a9e1e0cc72507f1d4b21d48246c8b6b7b6109c3ad5f58608fb3c542e3dd115` |
| `kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md` | `2104612302ee521666729dfc62d0098d0c8a5fee48e7921136fea4e978d61361` | `6eb0303bc748fd7394fc1ad00207f424137d1997a43cb794e4a0fbe7d99d0bd6` |
| `kb/tags/evaluation-README.md` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` |
| `kb/tags/warranted-autonomy-README.md` | `78b46df20e0dcdf40f468f6441484a4739abbfd31f1baf77bf7488cbb3d6a888` | `4a693f29f636c359df3fae3e2855d44c155243058955a792607929b80239021b` |
| `kb/tags/claims-and-grounding-README.md` | `d4b54e3f483d056bfda3e2e40f308597fb29061297b32562a653b3c2d4af0822` | `4bba94a1166cb4d6d683c58def867090547ab8a01367ab6b2da7c122ea2915bd` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/self-improving-systems-README.md` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` | `22dbb0008ce2d7d556c2f1927ecf30378e227eb2c11b8c53a1164be49b5143fe` |
| `kb/tags/llm-reliability-README.md` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
| `kb/tags/kb-maintenance-README.md` | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` |
