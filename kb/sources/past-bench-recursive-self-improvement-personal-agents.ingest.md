---
description: "PAST-Bench tests retained-state benefits across fresh sessions, separating task gains from pathway evidence and exposing model-dependent limits of Hermes+ runtime interventions."
source: https://arxiv.org/html/2608.04003v1
captured: "2026-09-17"
capture: trafilatura
capture_scope: partial-source
genre: scientific-paper
snapshot_sha256: bbb2ba854ff8aa355e7d435765d7db4d64582ea1a9717700a3934c68feff176d
ingested: "2026-09-17"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, agent-evaluation, deploy-time-learning]
learning_claims: true
---

# Ingest: PAST-Bench — retained experience across fresh sessions

## Classification

Scientific paper: Shuhan Xue and eight coauthors introduce a benchmark, compare model–framework configurations, and test runtime interventions through ablations. This is their arXiv v1 report, dated 2026-08-04. The authors construct both the evaluation and Hermes+, the proposed improved runtime; reported outcomes are their experimental evidence, not an independent replication.

## Summary

[PAST-Bench](https://arxiv.org/html/2608.04003v1) evaluates whether retained experience improves later executable tasks across 26 synthetic task families and 204 episodes. Each episode starts in a fresh session. Matched evaluation pairs permit or deny access to retained state while holding the model, runtime, prompt, tools, and context policy fixed. Task scores and persistence-on/off gaps are reported separately from trace-based evidence of the expected persistence pathway. Four capabilities distinguish stable fact reuse, ordered procedural reuse, retrieval of preseeded information, and correction of outdated state. Across seven models and four personal-agent frameworks, the authors report uneven benefits rather than a universal persistence advantage. Their researcher-designed Hermes+ adds planning consultation, typed memory rendering, skill management, a retrieval gate, and synchronous correction writeback within Hermes's existing persistence surfaces. With MiniMax-M2.7, the retained table reports the same overall persistence-on score, 0.66, for Hermes and Hermes+, with gaps of +0.13 and +0.15; the paper says this difference is smaller than run-to-run variation. Update is the clearest reported improvement, but procedural reuse and some model pairings regress. These comparisons test particular runtime changes within a supplied persistence architecture, not autonomous improvement of the agent's learning mechanism or superiority of that architecture.

## Quotes

No source quotes have been retained yet.

## Connections Found

The strongest role is empirical support and a concrete testing method for [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md). PAST-Bench separates later-task outcomes from retained-state access and expected-path traces. Its matched comparison is within a model–runtime configuration; it does not isolate the semantic contribution of an individual artifact. This makes it a useful case for [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): the broad persistence toggle, isolated Hermes+ additions, focused full-minus-one tests, and cross-model transfers answer different questions.

The diagnosis also supports [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). The authors describe plans formed without consulting available state and actions taken before retrieval. Preseeded information-gathering tasks specifically separate successful storage from timely consultation. Trace evidence locates these failures without establishing semantic uptake merely from a recorded read.

Update families provide bounded evidence for the supersession and expiry requirements in [Retire, Redact, Supersede, And Relax Memory](../notes/agent-memory-requirements/retire-redact-supersede-relax.md). Typed validity rendering and correction writeback make the next session's active state part of the test. The reported Update improvement belongs to the tested Hermes configuration; it does not establish redaction, historical point-in-time recall, or a general lifecycle solution.

## Learning Claims (our opinion)

The source calls its target *online self-evolution*: experience changes future behavior through persistent artifacts without retraining the base model. The agent receives user facts, task experience, procedures, or authoritative corrections and can retain them through memory, skills, profiles, and session history. Later sessions must retrieve and apply the relevant state. Information-gathering families are a special case: their evidence is preseeded, so they test consultation rather than learning to retain it. The matched persistence-off baseline is the same later task without access to retained state, not the earlier cold episode.

In Commonplace terms, ordinary fact lookup and procedure reuse apply retained knowledge. An authoritative replacement of a value demonstrates state revision when it governs the later response; it does not by itself demonstrate [theory refinement](../notes/definitions/theory-refinement.md). Failure-to-rule, latent-rule induction, and procedure-patching families are closer candidates for constructing or revising explicit rules. Establishing theory refinement would require following a criticizable rule through evidence, localized revision, and later use. Aggregate task gains and expected-path telemetry do not establish that chain for every successful family. The paper strengthens our account of evaluation across retention, activation, and outcome without requiring these operations to share one learning classification.

The distinction in [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) matters at two levels. During online adaptation, the supplied runtime determines available persistence interfaces and the agent updates content through them; the experiment does not ask it to redesign those interfaces. In the Hermes+ study, researchers vary five runtime mechanisms while retaining the underlying Hermes substrate, tasks, model, and grader for the intervention comparison. This tests particular choices of representation and access policy, but leaves alternative substrate decompositions untested. The focused procedural diagnosis, where removing typed memory rendering improves skill creation and reuse, is evidence that these supplied mechanisms can interact adversely. It is not evidence that every separation of declarative and procedural memory is mistaken.

Hermes+ therefore demonstrates researcher-led diagnosis and redesign, while the benchmark evaluates agents' subsequent retained-state use. The paper explicitly leaves stronger recursive improvement of storage, retrieval, verification, and update mechanisms to future work. Our learning judgment should preserve that boundary rather than infer reflective theory refinement from the title or from persistence alone.

## Extractable Value

1. **A reusable fresh-session evaluation protocol.** Match later episodes with and without access to retained state, distinguish cold calibration from the matched baseline, and report outcome and pathway evidence separately. Add distractor, stale-state, and wrong-mechanism controls so mere replay is not sufficient. This operationalizes the existing effects-based requirement within a fixed model–runtime pair; individual-artifact attribution still needs a finer intervention. [quick-win]

2. **Separate retention, consultation, and supersession tests.** Preseeded references test whether consultation occurs before action; correction and expiry families test what remains authoritative in the next session. These are distinct failure opportunities that a successful retrieval question can miss. The transferable contribution is the test design, while the observed intervention effects remain conditional on Hermes's interfaces and the synthetic families. [experiment]

3. **Test component interactions before adopting a persistence bundle.** Single additions and full-minus-one tests answer different questions. The focused procedural diagnosis reports more reliable task-specific skill creation and reading when typed memory rendering is removed. This supports checking which persistence surface receives and supplies a procedure; it does not identify a generally superior memory architecture. [experiment]

4. **Keep benefit, cost, and uncertainty together.** In the MiniMax-M2.7 comparison, Hermes+ preserves the 0.66 persistence-on overall score while changing the reported gap from +0.13 to +0.15, below run-to-run variation. Tokens per episode rise from 12,615 to 31,859 and wall time from 70.5 to 77.4 seconds. Within this configuration, a larger persistence gap alone is insufficient evidence that the revised runtime is a worthwhile improvement. [just-a-reference]

## Limitations (our opinion)

**The capture is partial.** The retained HTML extraction preserves prose, appendices, and some tables, but loses mathematical notation, many numeric cells, and figure contents. It supports the protocol, qualitative findings, and intact Appendix D numbers used here. It cannot establish the exact scoring equations, recover missing effect sizes or uncertainty, or independently inspect the illustrated traces. No implementation was inspected or executed for this ingest; none of the reported outcomes was reproduced.

**Pathway evidence is weaker than artifact-level causality.** Mech, the paper's mechanism-evidence score, compares traces with expected artifact types, keyword patterns, counts, retrieval signals, and correctness measures. It can reward a visible expected pathway without proving that a particular artifact's content changed the answer. It can also penalize a semantically valid alternative pathway. The authors acknowledge both limits and propose deletion, replacement, and corruption interventions as future work. As the [experimental-contrast note](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) explains, detailed telemetry cannot make a bundle-level toggle identify a finer cause.

**Scope and evaluation share a constructed setting.** All families are synthetic and isolated. Prompts, graders, and expected artifacts were generated in the same process and then checked by authors. This makes conformance to the constructed task and pathway contract a simpler account than broad personal-agent learning competence. Longer horizons, cross-family interference, real-user interactions, and autonomous mechanism revision remain untested. A blinded 48-sample judge audit reports agreement within 0.25 of the human mean on 68.8% of samples; the study does not vary the judge model or prompt.

**Framework comparisons do not isolate architecture.** Adapters preserve native loops and context-management policies, so absolute scores include bundled system differences. Agent-Zero receives a 1,200-second budget versus 300 seconds for Hermes; the ZeroClaw result uses its Python companion rather than the Rust executable. Hermes+ is built on Hermes v2026.4.16. These are versioned experimental configurations, not general rankings of current products. Similarly, the small, variable overall Hermes+ gap and mixed transfer across models do not establish a stable overall improvement or justify all five mechanisms together.

## Recommended Next Action

Update [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) with a bounded PAST-Bench example of matched fresh-session evaluation, preserving the distinction between retained-state benefit, expected-path evidence, and individual-artifact causal uptake.
