---
description: "Nested Learning recasts architectures and optimizers as nested associative memories, but Hope's broad gains vary local components within a fixed weight-only decomposition"
source: https://arxiv.org/abs/2512.24695
captured: "2026-07-31"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: f34b33a3121a97592f5beea36f23dc5eec16872ec46670bf83119a7b68228324
ingested: "2026-07-31"
type: kb/sources/types/ingest-report.md
domains: [continual-learning, learning-theory, optimization, agent-memory]
---

# Ingest: Nested Learning

## Classification

A NeurIPS 2025 paper, captured from its arXiv version, combining a unifying mathematical account with new architectures, optimizers, benchmark comparisons, and ablations.
Author: Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, and Vahab Mirrokni, with Google and Columbia affiliations. Publication and technical detail are strong credibility signals, but several central precursor systems and baselines share authorship with this paper, and no independent reproduction is recorded here.

## Summary

Nested Learning (NL) represents a trained model not as an architecture plus a separate optimizer, but as an interconnected system of optimization problems, each with its own context flow and update frequency. On this account, neural layers, recurrent states, momentum, backpropagation, and preconditioning are all associative memories that compress tokens, gradients, or local error signals at different levels; in-context learning is adaptation within any such context, and pre-training is simply the slowest, largest-context instance. The paper derives Delta Gradient Descent and more expressive momentum variants, then combines a self-referential Titans module with a Continuum Memory System (CMS) to produce Hope, whose MLP memories update at different frequencies. Hope is evaluated across continual classification and translation, long-context retrieval, language modeling, common-sense reasoning, recall, formal languages, and component ablations; a multi-timescale M3 optimizer is also tested on vision and language-model training. The strongest KB contribution is the coupled-system view: architecture generates the gradient context that the optimizer compresses, while update cadence determines persistence inside distributed-parametric state. The results support Hope as one compound design, but do not establish NL's universal decomposition or make its retained memories inspectable commitments.

## Claims

No claims have been grounded yet.

## Connections Found

Interpretation of the experiments **rests-on** [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). Hope varies DGD, momentum, weight decay, CMS presence, inner projections, level count, and update frequency, but its nested-associative-memory framing, MLP memory units, knowledge-transfer topology, objectives, and distributed-parametric substrate remain outside the learner's effective update space. The results therefore show that the compound configuration works across the tested settings; they do not validate that fixed decomposition as the generally correct learning space.

Hope **is-evidence-for** [Continual learning requires governing behaviour-changing writes, not just storing content](../notes/continual-learning-requires-governing-behaviour-changing-writes.md) and [Only explicit retention is currently durable, writable, and addressable at once](../notes/only-explicit-retention-is-durable-writable-and-addressable.md). It makes behavior-changing weights, recurrent memories, and optimizer states writable at several timescales, yet individual retained commitments remain readable only through behavioral probes. It **compares-with** [Treat continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md): more update frequencies enrich the distributed-parametric branch without creating interaction with natural-language or symbolic learning loops.

The closest source comparison is [Language Models Need Sleep](./language-models-need-sleep-self-modify-consolidate-memories.ingest.md), from overlapping authors. Nested Learning develops online multi-frequency updating; Sleep later adds offline upward distillation and dreaming. [Continual Learning in Token Space](./continual-learning-in-token-space.ingest.md) supplies the representational counterpoint of editable natural-language retention, while [Transformers Learn In-Context by Gradient Descent](./transformers-learn-in-context-by-gradient-descent.ingest.md) supplies a narrower construction and controlled regression evidence for one optimizer-like in-context mechanism. Together they bound NL's broader claim that all such adaptation is nested optimization.

## Extractable Value

1. **Optimizer state is part of the retained learning state.** Treating momentum and preconditioners as memories foregrounds an operational fact: discarding optimizer state when continual training resumes discards compressed information about the gradient history and loss landscape, even when model weights are preserved. This deserves evaluation as a retention decision rather than routine training cleanup. [experiment]

2. **Architecture and optimizer form a coupled learning system.** The architecture generates the optimizer's context -- gradients and local error signals -- while the optimizer determines the next architecture state. This makes “use the best architecture with the best optimizer” an under-specified composition rule and motivates testing architecture-specific optimization policies. [deep-dive]

3. **Update cadence is independent of representational form.** CMS adds a persistence spectrum within distributed-parametric memory: fast and slow weights can differ in lifespan without becoming different representational forms. This prevents “short-term” and “long-term” labels from silently implying a text store, symbolic archive, or addressable record. [quick-win]

4. **An ablation map is not an effective-update-space map.** Hope's ablations expose several local coordinates, but the learner cannot revise the level partition, transfer direction, memory class, internal objectives, or retention form. The reusable experiment-reading practice is to list both what was varied and what the design made inexpressible. [quick-win]

5. **Self-modification does not imply reflection.** Hope generates internal keys, values, gates, and updates that modify later computation, so its self-modification is substantive. Yet it cannot name, criticize, or selectively revert the commitments encoded by those changes, keeping it on the non-addressable side of reflective improvement. [quick-win]

6. **Compression makes forgetting a capacity-allocation problem, not a solved defect.** The paper explicitly concludes that CMS reduces catastrophic forgetting on tested tasks rather than solving it: finite parametric memories must discard information as new contexts arrive. This candid boundary is more reusable than the stronger “continual learner” branding. [just-a-reference]

## Limitations (our opinion)

The paper's unifying vocabulary is broader than its evidence. Defining every input-caused neural update as memory, every relevant computation as an optimization problem, and every adaptation to context as in-context learning makes many existing systems fit NL by construction. The mathematical rewrites demonstrate that the representation is possible; they do not show that it is uniquely explanatory, more predictive than competing descriptions, or the best basis for design. The neuroscience discussion motivates update timescales and uniformity but does not empirically validate the mapping from brain oscillations to frequency-ordered neural modules.

The fixed decomposition is the central experimental limitation. Hope learns contents, projections, gates, and updates within prescribed context flows, but it does not learn how many levels should exist, how they should be partitioned, which frequency schedule should apply, which direction knowledge should move, or whether retention should remain entirely parametric. Component removal and hand-selected level/frequency sweeps are informative inside that family. They cannot establish that the family admitted the distinctions, operations, or mappings needed outside the benchmark suite.

Benchmark breadth should not be confused with decomposition-level generalization. Different sections use different model scales, training budgets, fine-tuning regimes, and comparison sets. The continual-classification Hope models receive 15B tokens of additional training; the from-scratch language models receive 30B or 100B tokens; the 10M-token BABILong result depends on task fine-tuning. The paper says it uses best reported benchmark results in some comparisons and explicitly excludes Cartridges from one long-context study because computational costs differ. Those choices may be reasonable, but they leave no common resource-controlled contest among rival memory decompositions.

Several results are narrower than the headline. Hope remains below the Transformer on the short in-context recall suite, formal-language success ties other nonlinear recurrent models, and M3 is a stated proof of concept that is slower than Muon and evaluated for solution quality on one ImageNet setup. The paper tunes learning rates by model or optimizer, while many figures do not provide uncertainty estimates in the captured text. The evidence supports promising design points, not a general replacement for deep architectures or established optimizers.

Finally, NL's “memory” is distributed-parametric or optimizer state. It has durability and writability at several frequencies but no claim-level retrieval, provenance, criticism, or selective rollback. Readers working on agent memory should not import the paper's terminology as if a frequency-ordered weight block supplied the lifecycle and governance properties of an explicit retained artifact.

## Recommended Next Action

Update [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) with Hope as a worked experimental case, explicitly contrasting its varied components with the fixed level partition, transfer topology, objectives, and weight-only retention form that its broad benchmark suite does not test.
