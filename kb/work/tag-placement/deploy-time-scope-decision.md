# Deployment learning includes responses

## Operator decision

On 2026-09-26 the operator settled the scope question: “for deply time I would allow the responses to be covered”. The tag therefore includes both what deployed use reveals and how people or systems respond. This supersedes the old opening's explicit exclusion of response machinery.

## Placement rule

An artifact qualifies when it substantively addresses what operating software reveals beyond initial design and testing, or a response to that experience: diagnosing requirements, making changes, evaluating and retaining lessons, or maintaining the knowledge needed for later modification. The response may be human, computational, or mixed. A generalized mechanism or limit of learning from use can qualify without a separate narrative of surprising user needs. Generic improvement alone remains insufficient.

Overlap is intentional. Continued learning through retained changes outside weights may qualify for both deploy-time-learning and continual-learning. Self-improvement used to respond to deployed experience may qualify for both deploy-time-learning and self-improving-systems. Neither neighboring tag automatically implies deployment relevance.

The deploy-time-learning opening and description now state this rule. Neighbor descriptions in continual-learning, self-improving-systems, learning-theory, and the tag hub now reflect it. No note tags or arguments were changed in this pass.

## Assignment dispositions

All eleven original mismatch proposals for this tag are resolved by retaining the assignment under the revised scope. The reasons below come from reading the live notes, not from their curated links alone.

### TP-006 — retaining lessons from experience

[Abstract an experience into a lesson only when you can state where the lesson stops](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md).

The opening makes the episode-to-lesson decision its subject; the success/failure comparison and boundary test govern how an agent responds to experience without installing an overgeneral rule.

### TP-007 — responding to new requirements

[Ad hoc prompts extend the system without schema changes](../../notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md).

The body explains how prompts absorb requirements that no longer fit the existing deterministic base, then how recurring responses mature into reusable skills. The KB collections case is a worked response to a need encountered in use.

### TP-020 — deployment-time adaptation

[Constraining during deployment is continuous learning](../../notes/constraining-during-deployment-is-continuous-learning.md).

The note explicitly explains adaptation to new data, tasks, and shifts during deployment through prompts, schemas, tests, and code. It belongs under both deploy-time-learning and continual-learning.

### TP-032 — diagnosing and revising failed requirements

[Exact implementation does not validate a requirement against its objective](../../notes/exact-implementation-does-not-validate-a-requirement.md).

The body distinguishes local conformance from whether a requirement serves its objective, then prescribes retracting failed requirement–objective claims, rescoping surviving use, and relaxing hardened links when operation exposes poor fit. This is a generalized response mechanism, not merely a deployment example.

### TP-044 — knowledge needed for later maintenance

[Naur's compiler case tests one historically bounded documentation-and-consumption system](../../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).

The compiler case concerns a successor group attempting extensions and failing to preserve structure; the argument compares retained rationale and consumption pathways that could support coherent modification across later demands. It evaluates a response capability without requiring the note to describe the original user surprise.

### TP-050 — retaining evaluated adaptation

[Retained system-definition artifacts enable persistent deployment-time adaptation](../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).

The note explains how deployment experience drives proposed artifact changes, evaluation selects them, and retention changes later behavior. Human proposal or approval is allowed. The mechanism is now explicitly within the tag.

### TP-052 — limits and renewal of deployment responses

[Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md).

The argument examines when deployment-specific scaffolding should disappear and when new task demands call for new external structure. Its substantive subject is whether that adaptation response remains useful as models and assigned difficulty change.

### TP-057 — interpreting feedback from use

[System use provides evidence of theory fit and causal usefulness, not independent warrant](../../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).

The body explains what live-system consequences warrant and when failures justify rescoping or removing a claim. Those limits govern how a system learns from use; a separate account of a surprising user encounter is no longer required.

### TP-059 — selecting revisions through use

[System use is an initial selection environment when theory fit lacks a fixed oracle](../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md).

The argument makes consequential use an initial selection environment for theory candidates and explains correction, delayed consequences, and the danger of self-confirming feedback. That is a substantive learning response to operating experience.

### TP-063 — choosing what a deployed response can change

[The deployed system, not the model alone, is the unit of learning](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).

The note identifies the deployed system as the evaluation boundary and describes prompt revisions, validators, and other evidence-responsive updates. It explains why responding only through model weights leaves relevant causes fixed.

### TP-065 — bounding what successful use licenses

[Use tests a decomposition locally; retained rationale is what makes transfer testable](../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md).

The body explains why running a design only supports local sufficiency and what rationale must be retained to test transfer under new demands. It governs what can safely be learned and reused from operating experience rather than merely discussing decomposition.

## Membership and evidence boundary

The current membership contains twelve notes. The eleventh-mismatch count is not the full scope: the previously accepted [changing-requirements note](../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) also remains a fit. It explicitly separates world change from late-discovered interpretation errors and explains the different responses, including shorter feedback cycles and constraining.

The revised scope admits response mechanisms while retaining the old phenomenon route, so the change does not invalidate that accepted member. Suggested additions remain separate work; this pass does not certify that every eligible note already carries the tag.

The original reviews and frozen baseline remain unchanged. Their verdicts describe the old criterion. These workshop dispositions apply the operator's revised scope and do not pretend that a fresh independent review has passed.

## Verification

`commonplace-validate tags` and explicit validation of the edited workshop
files and index completed with zero failures and zero warnings. A membership
check across the five participating collections found twelve tagged notes.
The issue list contains all eleven deployment dispositions and now totals
30 resolved assignment findings and 38 open. `git diff --check` passed.

## Input versions

SHA-256 of the live notes and resulting tag heads considered in this decision. Earlier parent-membership input hashes remain a record of that earlier pass.

| Input | SHA-256 |
| --- | --- |
| `kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | `ec24b365273a158cf51bc13003d65e314d68ee4424c6fe7736fa07babc418d2b` |
| `kb/notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md` | `a8fc9be0f3053b0a686cd0e6c81993d71341a645cdc8ae9cef6a5ea9da81f9a7` |
| `kb/notes/constraining-during-deployment-is-continuous-learning.md` | `ccdf37978ef45d25ee5ac908fd17d44cb27a39355f2f351a01cb74b6bb09fba3` |
| `kb/notes/exact-implementation-does-not-validate-a-requirement.md` | `0b1ca481ded77c87f11860c4738d9b627123b29654920eb1c6be3cd31d156b23` |
| `kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md` | `88398cbb94c93b192ec514db9d02030441af9669d48dd02e0c539d1c6c817174` |
| `kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md` | `fb5cb1833e576e10fa4247e2bb30482ccd87423b861c58d63d91d8b1ab7dc460` |
| `kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md` | `8ce34030fcfa51e9caac633b9109a937ef2a1b7286b92a2ed17d9bff44bc845e` |
| `kb/notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md` | `646ba7beaeab12313568789c1a08490d29e11c10f15915b293d3b74d5c03770b` |
| `kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md` | `f409f86e1dabbb72e46c24450630451d0bbf2b5dcb7dd34549c86f9f0398bba0` |
| `kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md` | `0e7142f4208f8e41319ebe64ef847d40b01d6325f2d4b02bfe8da8edbedfa20c` |
| `kb/notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` | `f23b5da628802517fa58c7bfe48d135c11e237d7620f78ca10059283e9fd4dcb` |
| `kb/notes/changing-requirements-conflate-genuine-change-with-disambiguation.md` | `4a7fc5461fa4a1900a60a5c855fb577eb131afd8f6397455ff206bfe3aad7339` |
| `kb/tags/deploy-time-learning-README.md` | `aaf1c80d74ce43c34c389773e8d6f362460d7e4939f102839bf4399d53437ee1` |
| `kb/tags/continual-learning-README.md` | `bb5bca21428ca9b033ff8ae951f4582725941836a27b3d4806c33ab17738b62d` |
| `kb/tags/self-improving-systems-README.md` | `81bb084cc147d4c7e4df574f2d339c30da1c58205b772b5bc7a8eb81da13e718` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/README.md` | `b0b7b4905367a5284a52e060c48ca0c6c84582696d741170b012ed993df3ab46` |
