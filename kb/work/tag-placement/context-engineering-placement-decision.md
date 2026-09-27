# Context-engineering placement: loading versus evidence and control

## Boundary applied

On 2026-09-26 this pass checked the nine remaining context-engineering
findings against the unchanged head: how knowledge reaches or is managed
within a bounded LLM context. It also checked the associated llm-reliability
finding on the cheap-generation note. All ten assignments are removed.

A substantive secondary loading argument can qualify. A context-window
premise, an intended application, a footer link, or the general reuse of
retained material does not by itself supply that argument. The two capture
notes develop fidelity and rationale preservation; the scheduler notes develop
control ownership. Their existing content fits other heads without broadening
context-engineering. Note bodies are unchanged.

## Assignment decisions

| Finding | Note | Disposition and reason |
| --- | --- | --- |
| TP-001 | [A citation cannot assert more fidelity than its capture preserved](../../notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) | The finite context window motivates lossy capture, but the developed mechanism governs citation fidelity and recapture, not knowledge loading. Replace context-engineering with claims-and-grounding and its kb-maintenance parent. |
| TP-005 | [A retained instruction preserves what testing selected](../../notes/a-retained-instruction-preserves-what-testing-selected.md) | Testing selects a candidate procedure and retention makes the evaluated choice reusable outside weights. Replace context-engineering with improvement-loop and continual-learning, plus self-improving-systems and learning-theory. No loading mechanism is developed. |
| TP-015 | [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) | Prompt rewrites are one proposed benchmark. The experiment concerns judge discrimination, variance, bias, and correction of selection errors, so keep evaluation and llm-reliability, remove context-engineering, and add the learning-theory parent. |
| TP-016 | [Cheap generation breaks text volume as an effort signal](../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) | Text volume is assessed as a triage signal for reviewer effort. This develops neither bounded-context operations nor an LLM deviation or correction mechanism. Replace context-engineering and llm-reliability with evaluation. |
| TP-017 | [Cheap generation breaks text volume as an effort signal](../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) | The note expressly separates its triage signal from evidence that an output is false or incorrect. Remove llm-reliability along with context-engineering; evaluation covers what the signal establishes. |
| TP-022 | [Cross-task transition policy remains scheduling behind a tool interface](../../notes/cross-task-transition-policy-remains-scheduling-behind-tools.md) | The substantive mechanism locates transition authority and interceptable control boundaries. Keep computational-model and add architecture; scheduling independently steerable goals does not by itself establish a bounded-context question. |
| TP-042 | [Mixed epistemic status must be preserved below the document level](../../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md) | The note preserves separate warrant for observations, deductions, and compatible explanations inside a document. Replace context-engineering with document-system and claims-and-grounding, plus kb-maintenance; keep evaluation. |
| TP-055 | [Stateful tools recover control by becoming hidden schedulers](../../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) | The argument relocates scheduler state and control behind a tool boundary. Context overflow is only a named limit delegated to another note. Keep computational-model, replace context-engineering with architecture, and move its curated entry to the architecture head. |
| TP-056 | [Bottom-up structure inference needs capture at the decision surface, not the state](../../notes/structure-inference-needs-capture-at-the-decision-surface.md) | The capture point determines which rationale-bearing structure can later be inferred. This explains memory ingress, not activation or loading into bounded calls. Remove context-engineering; retain agent-memory and learning-theory. |
| TP-066 | [Warranted reader update is the objective of substantive writing](../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) | The workflow searches for a warranted contribution and judges its value relative to the reader. Co-presence is one ingredient, not a developed loading mechanism. Replace context-engineering with document-system; retain learning-theory and discovery. |

## Additions and parent relations

Five queued addition entries are accepted in full: ADD-002, ADD-012,
ADD-046, ADD-126, and ADD-201. Their individual dispositions state the
fit to each head. The two scheduler notes also receive architecture under
its already revised general scope: both explain control boundaries and their
consequences. Neither develops a Commonplace-specific arrangement, so neither
receives commonplace-architecture.

This pass removes ten assignments and adds fourteen across nine notes.
Four new child assignments carry their required parents: the citation and
mixed-status notes gain kb-maintenance through claims-and-grounding; the
retained-instruction note gains self-improving-systems and learning-theory
through improvement-loop and continual-learning. PG-037 adds learning-theory
to the pairwise-judge experiment after checking its llm-reliability mechanism:
variance, position bias, and noisy selection are tested as output-correction
problems. PG-040 closes by removing the unsupported llm-reliability assignment,
so it does not acquire a learning-theory parent. The original parent inventory
and its hashes remain historical inputs. Fourteen entries are now resolved,
leaving 115 open.

The claims-and-grounding, improvement-loop, and continual-learning heads gain
links needed by their completeness marks. The stateful-tools entry moves from
context-engineering to architecture. Its former context-engineering entry
overstated the note's treatment of context control. Architecture also links the transition
policy note. No tag inclusion rule changes in this pass.

## Verification

Semantic decisions are this agent's direct rereading of the notes and live
heads, not fresh independent assays. `commonplace-validate` passed on all
21 changed files in this pass and on the tags collection: zero failures and
zero warnings. The tag check includes the heads' completeness marks.
A separate check confirmed ten removals and fourteen additions, unchanged
bodies for all nine notes, 60 resolved and eight open assignment findings,
25 accepted additions plus one duplicate closure and 180 open entries, and
14 resolved and 115 open parent gaps. `git diff --check` passed.
All work remains uncommitted.

## Checked versions

SHA-256 hashes identify the inputs read and the resulting library artifacts.
Unchanged head hashes match in both columns. The original review findings and
placement baseline are not rewritten.

| Artifact | Before | After |
| --- | --- | --- |
| `kb/notes/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md` | `064c640124256f189ca1f64028439ef3d615f5617ad4c216a46243c5306fc5c3` | `ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16` |
| `kb/notes/a-retained-instruction-preserves-what-testing-selected.md` | `2f3b6eef189ba01a8b25e8f66a09bf16ae237c22c4b671f9010a8a4d6fbe84f1` | `6c18f336984e7e181143d6325cf6ba1b38c77ea83054c6902a46d3e3a94d0d39` |
| `kb/notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md` | `2e10078b6a12e2123700611890457eaf9f2c04490ed14d06749f62614e12b4d6` | `7febe6370ed21a2ab8745c9a19fb5b6e2f2dceeb6d76fbe3c27eece174cd28b6` |
| `kb/notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md` | `39507af50238bb6a5259ed5037d6a836516146aa680742acc7900720cf7319bb` | `c3f6a80d1b9d919143cbe0a4a200e55eef24c22352e086c00c8ae2e026d16973` |
| `kb/notes/cross-task-transition-policy-remains-scheduling-behind-tools.md` | `f8047a2a344379f22a57e73c521350f620204240908b53099eb6f538c3b9db1c` | `502a65c444cd4fd409a4a7865de7548de370ae354f2444aefd335bbface2f595` |
| `kb/notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md` | `8b4e5cc9614e380cc9c3878a4cbff82b5a748061d6337d5a924af13508375e2d` | `719ab7c3d962bac4294e78000f6c5c442641c9538d830a373705d23572d5c792` |
| `kb/notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md` | `6e14b839c2505d65d3790f248b65342fb62da92503b2283b592a29586c16ce58` | `ca3320376738e880526b867e5af12b15411698e54364fa5549bfad2d46a74a1e` |
| `kb/notes/structure-inference-needs-capture-at-the-decision-surface.md` | `5c60017063428e04d40a0c330db74bb8c0f5c0dfce05b43eefe3d31fd52d41c2` | `c5d747d42002ee12655cf8e065032c1b7ddc7c61ef570eea4ff1481e306f9a13` |
| `kb/notes/warranted-reader-update-is-the-objective-of-substantive-writing.md` | `5294f05cb58888536a9f51c1a8b29d5e9a0040aed2f8c5370716654bc67d4662` | `566aa3a816a5a098dc85dcb8e878d57980d2e37da25999d8dcbacbb005067104` |
| `kb/tags/context-engineering-README.md` | `fa3e8c4eedfc0e222b21c5137986a296815ed881012447e8a2132460cc2d9955` | `93b4389c239ba680c7d1fbe134715b41e635e1ca81836613c89e4b5f08052b14` |
| `kb/tags/claims-and-grounding-README.md` | `3a0be768095c55597fa2a1ed9ba4dc6e03d6a49454c15fe3251d5e8152f3a628` | `ac38d660c86df0c689f3eb06aafc75a18ae02c6c278c72739425841882ec3178` |
| `kb/tags/kb-maintenance-README.md` | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` | `01a93c13dded3a6e13f65199ea21cc8062d18fe091cee0c9471b8903368c9157` |
| `kb/tags/improvement-loop-README.md` | `ea2f7ea2282c6caf80527cff91387552c4dc0e7d2406bc215052cbaaa45b35a5` | `4947fc0c72e5d67bfd787ee6717bf8b907f0f717016c3f5495f4b350a97cd560` |
| `kb/tags/continual-learning-README.md` | `bb5bca21428ca9b033ff8ae951f4582725941836a27b3d4806c33ab17738b62d` | `95d3647a7d89af31ea894166874767a0038b8b1eace4c0433d3d5a1f37fdcda9` |
| `kb/tags/self-improving-systems-README.md` | `81bb084cc147d4c7e4df574f2d339c30da1c58205b772b5bc7a8eb81da13e718` | `81bb084cc147d4c7e4df574f2d339c30da1c58205b772b5bc7a8eb81da13e718` |
| `kb/tags/learning-theory-README.md` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` | `3effa98ce3c2d9db6a1aaf30769a3b179f994691a90e8222318e5f115305b5cf` |
| `kb/tags/evaluation-README.md` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` | `1268a09409705248434d19441ad1d3cc49b387e7b0ed39b76a4057c0cd31e669` |
| `kb/tags/llm-reliability-README.md` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` | `b66bc38d119eab7dcf51d2e795e736467a0933c24807bb856a21aded79763da5` |
| `kb/tags/architecture-README.md` | `bec434d109605ed794509aaa9e07286cb9f51265844501cb0560e3eb54024561` | `1f710c930f124ebc41f5b6159a97a6284b7881ec85ccbd7cb755fc251cbd0764` |
| `kb/tags/document-system-README.md` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` | `5d0f5de7f082fedfe8be6038f71e2f1386e008ae77feca5906e14c354b45d1da` |
