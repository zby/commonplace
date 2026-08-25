---
description: "Why missing comparisons, bundle-to-component attribution, and adjacent unrun treatments all overstate causal conclusions beyond an experiment's observed contrast"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, deploy-time-learning]
---

# An experiment identifies only the contrast it actually runs

When an experiment identifies a causal effect, that effect is indexed by the difference between its observed treatment and comparison conditions. It cannot support causal attribution finer than the finest unit varied independently between those conditions. Properties that always move together form one treatment bundle for that contrast.

That difference is the **experimental contrast**. The **treatment grain** is the finest causal unit varied independently. The **measurement grain** is the unit on which outcomes are recorded, such as a rule opportunity, task, trajectory, or benchmark. The **attribution grain** is the unit named as the cause in the conclusion. Detailed measurement can reveal where behavior differs, but it cannot make a bundle-level intervention identify a component-level cause.

This bound follows from the role of the condition pair. An outcome difference bears on a cause through what changed between the observed conditions. Replacing either condition changes the causal question. Naming one component inside a jointly changed bundle asks a finer question than the experiment ran. Missing comparisons, bundle-to-component attribution, and claims about adjacent unrun treatments are therefore three versions of the same error: substituting another contrast for the observed one.

## Check the contrast before naming an effect

Write the treatment and comparison conditions literally. List the causally relevant differences between them. Identify the finest unit varied independently, then compare it with the noun used as the cause in the conclusion.

This check gives three immediate limits:

- When the relevant comparison was not observed, report the outcome level under the observed condition rather than an intervention effect.
- When several components changed together, report a bundle effect rather than assigning the difference to one component.
- When a proposed treatment differs materially from every observed arm, report its effect as untested rather than borrowing the result of a nearby treatment.

An observational comparison can establish an association between exposure conditions, but the contrast alone does not supply the intervention needed for a causal reading. In either design, the claimed conclusion must not silently substitute a missing condition or a finer unit.

The same logic applies beyond ablations. [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not.md) because the object varied determines the question a result can answer. An experimental contrast makes that boundary causal: the observed condition pair fixes the possible effect, and the treatment grain fixes the finest possible attribution.

## A missing comparison leaves a level, not an instruction effect

Behavior observed while an instruction is present is an outcome level under that condition. It is not by itself the effect of supplying or using the instruction. The same behavior might arise from model priors or harness defaults.

Harness-IF makes this problem visible. Its zero-injection probes withhold a target rule and show that unprompted behavior can already align with the rule. Its aggregate-to-AP-Acc gap supports prior-alignment inflation in the benchmark score, but AP-Acc compares different rule strata. It is not a paired estimate of the effect of injecting each rule on matched opportunities ([paper](https://arxiv.org/abs/2608.11727), [local analysis](../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md)).

If an absent-instruction condition differs only by the instruction-bearing component, then the component is the treatment grain. A finer claim about semantic uptake needs a finer contrast. If omission also removes a delivery slot, changes prompt length, suppresses retrieval, or changes the opportunity to act, then the intervention remains a bundle.

The self-evolver study illustrates why named controls are not interchangeable. For raw trajectories, Empty retains formatting, Shuffle retains content tokens while disrupting order, and Irrelevant retains format and structure while replacing topical content. For condensed summaries, Empty retains formatting, Corrupt changes logical content while retaining surface form, Irrelevant substitutes unrelated content, and Filler retains surface structure with meaningless placeholders. Full ablations instead omit the experience section, and the study does not run every control on both representations ([paper](https://arxiv.org/html/2601.22436v3), [self-evolver ingest (snapshot required)](../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md)). The general conclusion is this note's transfer: a control identifies only the properties its implementation actually varies while holding others fixed.

Causal uptake is distinct from correctness or benefit. Correct behavior can occur without uptake of the named instruction. An instruction can change behavior while making the outcome worse. The contrast must therefore match the uptake claim, while utility requires its own outcome evidence.

## A bundle contrast stays at bundle grain

Memento-Skills compares its full system with a Read-Write condition that retains skill retrieval, execution, and feedback while jointly disabling failure attribution, skill rewriting, and skill discovery. For Gemini-3.1-Flash, the full system reports 66.0% test accuracy against 52.3% for Read-Write on GAIA, and 38.7% against 17.9% on HLE ([paper](https://arxiv.org/pdf/2603.18743), [local analysis](../sources/memento-skills-let-agents-design-agents.ingest.md)).

Those differences support an effect of enabling the skill-optimization pipeline as a bundle, relative to that retained baseline and within the reported setup. They do not isolate failure attribution, rewriting, discovery, or any selected skill. Route-level or task-level measurements can describe where the bundle's consequences appear, but they do not supply the missing component-level counterfactuals. This is why [memory must be evaluated by its effects rather than its existence](./agent-memory-requirements/evaluate-memory-by-effects.md): discovery, activation, uptake, and outcome remain distinct evidential links even when an aggregate result improves.

## A nearby but unrun treatment remains untested

Meta-Harness supplies the subtler case. In its text-classification ablation, the scores-only condition reached 34.6% median accuracy. The `Scores + Summary` condition had no raw-trace access and reached 34.9%; its best accuracy was 38.7%, against 41.3% for scores only. The full raw-trace condition reached 50.0% median accuracy. These are descriptive results for the reported proposer, task, and search setup, not a statistical-significance claim or a result from the paper's other experiments ([paper](https://yoonholee.com/meta-harness/paper.pdf), [local analysis](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md)).

The warranted negative reading is that this fixed, trace-replacing summary treatment did not recover the performance of raw-trace access in that setup. It does not identify summaries or abstraction as treatment classes. An artifact that retains trace access behind a derived representation changes evidence availability. Query-conditioned production changes when and for which diagnostic question the representation is made. Joint optimization changes which representations enter the search space. These are materially different treatments, and Meta-Harness did not run them; [learning inside a fixed decomposition inherits its excluded alternatives](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

The result therefore creates an experimental obligation, not a verdict about the unrun alternatives: a claim about episode-backed theory needs an arm that adds that treatment while holding episode access fixed. Sharing a motivation or plausible mechanism with the tested summary does not make it part of the observed contrast.

The full-trace advantage also supports a scoped positive interpretation: richer inspectable failure evidence helped this proposer produce better candidates in this setup. [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) develops that interpretation. Neither reading establishes that rawness is universally causal or predicts whether an unrun theory treatment would succeed.

## Scope

Running the relevant contrast is necessary, not sufficient, for causal identification. Assignment, interference, behavioral opportunity, outcome measurement, statistical resolution, and construct validity can still defeat identification. No remedy for those problems can make a result answer a different condition pair from the one observed.

Any identified effect also remains indexed by the studied tasks and population, model and harness, wording and delivery surface, opportunity structure, comparison implementation, evaluator, aggregation rule, and observation horizon. Evidence earns warrant only for the claim and scope it covers, since [theory warrant should be tracked at the finest granularity evidence licenses](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md).

Accept a causal noun only when it names the observed treatment-versus-comparison difference at no finer grain than the intervention. Otherwise report a level, a bundle effect, or an untested hypothesis.
