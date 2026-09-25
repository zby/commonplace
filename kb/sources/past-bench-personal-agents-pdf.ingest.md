---
description: "PAST-Bench separates fresh-session persistence gains from pathway evidence; its Hermes interventions offer bounded tests for memory activation, correction, and evaluation."
type: types/ingest-report.md
source: https://arxiv.org/abs/2608.04003
captured: "2026-09-17"
ingested: "2026-09-17"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: be69e16a6c57538ad713f987791b0b4926521ab17c3d0467f536a0761c35b14d
domains: [agent-memory, evaluation, deploy-time-learning]
learning_claims: true
---

# Ingest: PAST-Bench — retained experience in personal agents

## Classification

Scientific paper by Shuhan Xue, Zixin Ding, Yichen Shen, and colleagues, captured from arXiv v1 (2608.04003v1). It introduces a benchmark, reports controlled evaluations, and tests diagnosis-driven runtime interventions. The authors also develop the evaluated Hermes+ extension. Author signal therefore combines experimental detail with an interest in the proposed benchmark and system; this ingest does not establish peer-review status or independent replication.

## Summary

[PAST-Bench](https://arxiv.org/abs/2608.04003) tests whether retained state improves later tasks across 26 synthetic scenarios and 204 episodes covering memory, procedural reuse, information gathering, and updates. Episodes start in fresh sessions; matched evaluations keep the model, runtime configuration, prompt, tools, and grader fixed while allowing or denying access to retained state. Task gains are reported separately from a mechanism-evidence score based on artifacts, retrieval events, and correctness signals. Seven models benefit within the tested Hermes configuration, but framework and capability results vary. Five interventions in Hermes's existing memory, skill, and history interfaces form Hermes+: planning consultation, current-binding rendering, skill routing, retrieval gating, and closeout persistence. With MiniMax-M2.7 fixed, the full treatment improves the mean Update persistence gap from +0.12 to +0.24, while procedural performance falls and the Overall gap change from +0.13 to +0.15 is smaller than run-to-run variation. The contribution is a diagnostic evaluation method and bounded intervention evidence, not a demonstrated general improvement to persistent agents or a comparison establishing the best memory decomposition.

## Quotes

No source quotes have been retained yet.

## Connections Found

The strongest connection is evidence for [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md). PAST-Bench supplies a concrete fresh-session, persistence-on/off comparison alongside pathway diagnostics. Hermes and nanobot have the same reported Overall gap (+0.13) but different mechanism scores (0.64 and 0.57). This supports keeping downstream effects and observed persistence pathways separate. The mechanism score partly incorporates task correctness, however, and is not an independent test that particular memory content caused a decision.

The paper is also a case for [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): the broad persistence toggle, isolated Hermes+ additions, focused full-minus-one tests, and cross-model transfers answer different questions. Detailed pathway traces cannot make a bundle-level intervention identify an individual artifact's causal contribution.

Its failure diagnosis supports [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). Plans can be formed without consulting available state, and actions can precede retrieval. Preseeded information-gathering tasks isolate timely consultation from acquisition; a recorded read alone still does not establish that the content changed the action.

The paper also gives bounded evidence for [Activate Behavior-Changing Memory Before The Mistake](../notes/agent-memory-requirements/activate-behavior-changing-memory.md) and [Retire, Redact, Supersede, And Relax Memory](../notes/agent-memory-requirements/retire-redact-supersede-relax.md). In the tested Hermes substrate, pre-answer retrieval gating improves Information Gathering, while rendering valid bindings and persisting corrections address stale-state failures. These are tests of runtime changes around existing interfaces. They do not establish that typed bindings or the memory/skill/history split are preferable to alternative representations, and the lifecycle evidence concerns correction and expiry rather than redaction or policy relaxation.

## Learning Claims (our opinion)

The source calls its mechanism online self-evolution: experience changes later behavior through persistent artifacts without retraining the model. Earlier sessions expose facts, procedures, and corrections; later sessions can consume memory records, skills, or session history through the runtime's existing tools. The learning object is external state. The base model and the runtime's available persistence interfaces remain fixed within each matched comparison. Information Gathering is a distinct case: relevant state is preseeded, so it tests consultation rather than acquisition from prior experience.

Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the agents' memory records and skills are stated content (condition 1). Persistence-on/off comparisons show that retained state changes later tasks, but the mechanism score does not establish that particular content caused a decision, so condition 2 holds at the level of retained state, not item by item. Retained state is taken up in fresh sessions on later tasks (condition 4). Criticism (condition 3) is unestablished and decides the verdict. Remembering a preference or applying a saved procedure is retention and use. Updating a procedure after an error would be criticism if the error counts against what the procedure says, but the paper does not separate such updates from others. Replacing an obsolete fact after an authoritative correction does not alone establish it. The benchmark groups these changes under self-evolution, so its aggregate score measures neither builder membership nor learning by criticism. The persistence gaps are a learning claim, improved later performance from retained state, but they are not attributed to criticism.

There are also two learners to distinguish. Agents write and revise persistent state during task families; the researchers inspect failures and engineer Hermes+'s five runtime changes. The latter is not evidence that agents improved their own learning machinery; with the researchers inside the declared boundary, the paper shows one round of such revision, not a continuing process. Consistent with [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the single-component tests compare choices inside the supplied Hermes loop, while alternative persistence partitions remain untested. The reported interference between memory rendering and skill creation makes that boundary consequential: a locally useful mechanism can divert writes from the procedural artifact later tasks need. The source strengthens the case for testing retention, consultation, and outcome separately; it does not require counting every persistent update as the work of a theory builder.

## Extractable Value

- **Matched later-task controls [quick-win].** Enrich the effects requirement with fresh-session persistence-on/off evaluation. Cold-start scores measure initial competence and headroom; they are not the matched no-persistence baseline. Keep prompts, tools, limits, and context policy fixed within each pair, and report absolute performance alongside the persistence gap. Include distractor, stale-state, and wrong-mechanism controls to test alternatives to useful reuse.
- **Layered attribution [experiment].** Combine retained-state removal with artifact and retrieval traces, then perturb a specific candidate artifact when content dependence matters. PAST-Bench implements the first two layers; it explicitly leaves deletion, replacement, and corruption tests as stronger future attribution methods. Its mechanism score should remain a diagnostic signal.
- **Interventions can compete for the same retained experience [deep-dive].** Within Hermes, the full five-mechanism treatment improves Update but reduces Procedural persistence-on performance from 0.55 to 0.38. A focused full-minus-one diagnostic finds better procedural skill creation and reuse after removing E2 memory rendering. This motivates checking where experience is written when combining memory and skill policies; the focused result is not a full-benchmark estimate or proof that typed memory generally harms procedural learning.
- **Supersession needs later-session testing [experiment].** Correction and exception-expiry families supply a reusable test shape: expose old state, provide an authoritative revision, clear the session, and check both use of the new value and suppression of the old one. The Hermes interventions offer candidate implementations within its existing substrate, not a validated prescription for Commonplace.

## Limitations (our opinion)

The scenarios are synthetic and family-isolated. Prompts, graders, and expected artifacts were generated in the same process and then checked by authors, so success may reflect conformance to that constructed task and pathway contract rather than broad personal-agent learning competence. The scenarios do not test months of mixed experience, interference across families, or the upkeep costs of a growing KB. Open-ended scoring uses a fixed MiniMax-M2.7 judge; a blinded 48-sample author audit reports 68.8% judge–human agreement within 0.25 points. That is useful calibration, but it leaves material grading uncertainty and does not test sensitivity to alternative judges.

Mechanism evidence is partly a proxy and partly outcome-derived. Artifact quality uses keyword hits and entry-count changes; recall accuracy and update correctness incorporate content correctness; retention horizon uses near/far task-score ratios. These components cannot establish content-specific causal necessity. Expected substrate and event contracts can also undervalue a semantically valid alternative path. The paper acknowledges that limitation and proposes stronger counterfactual tests.

Hermes+'s aggregate advantage is uncertain: three-run Overall gaps are 0.13 ± 0.04 for Hermes and 0.15 ± 0.06 for Hermes+, and Update variability also increases. Overall persistence-on performance remains 0.66 in both. A larger on/off gap can result from lower persistence-off performance, so the gap alone cannot establish a better deployed agent. Cross-model transfer is uneven. In the MiniMax comparison, tokens per episode rise from 12,615 to 31,859 (approximately 2.5 times), while wall time rises from 70.5 to 77.4 seconds. A larger persistence gap alone does not establish that the runtime change is worth its cost.

The isolated interventions vary runtime mechanisms within Hermes v2026.4.16; they do not compare alternative storage decompositions. Framework comparisons bundle native differences in context handling, loops, and limits despite holding the model fixed. ZeroClaw denotes its Python companion rather than its Rust executable, and Agent-Zero receives a longer timeout. These results characterize the tested adapters and configurations, not current products generally. No implementation code was inspected or executed for this ingest; all experimental outcomes and mechanism descriptions remain paper-reported.

## Recommended Next Action

Update [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) with PAST-Bench's matched fresh-session persistence control, preserving the distinction between observed pathway evidence and content-specific causal dependence.
