---
description: "Schmidhuber formalizes curiosity as compression progress, offering a bounded account of creative search rather than evidence that creative LLM outputs imply intrinsic motivation."
source: https://arxiv.org/abs/0812.4360
captured: "2026-09-18"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 6f78be61ad4eb9e4ebce37adc98616805bec21e096c66807948573dee2e85720
ingested: "2026-09-18"
occasion: "what compression progress contributes to an account of creativity, and how far that account applies to current LLMs."
type: ingest-report
domains: [intrinsic-motivation, creativity, learning-theory]
learning_claims: true
---

# Ingest: Driven by Compression Progress

## Classification

A theoretical scientific paper with an implementable reinforcement-learning framework, a retrospective account of earlier implementations, and illustrative arguments about human cognition. Jürgen Schmidhuber writes as the originator of the artificial-curiosity research program he surveys. The retained text is arXiv v2, revised 15 April 2009; its historical implementation claims are author-reported, not independently reproduced here.

## Summary

Schmidhuber proposes that curiosity and essential aspects of creativity arise from seeking experiences that improve a bounded observer's ability to compress its history. The framework stores observations and actions, improves a predictor or compressor, measures old and new compressors on the same history, and rewards a controller for actions that yield improvement. It distinguishes already understood regularity, which offers little remaining progress, from persistent noise, which offers little learnable structure. Creative activity can connect familiar patterns through a previously unnoticed regularity, making their joint description simpler for an observer. The paper supplies a precise objective and possible learning machinery; its extension to art, science, jokes, and subjective beauty is chiefly a theoretical interpretation supported by illustrations and references to earlier studies, with further human experiments proposed.

## Quotes

- **Source extract (verbatim):** What’s beautiful is not necessarily interesting. A beautiful thing is interesting only as long as it is new, that is, as long as the algorithmic regularity that makes it simple has not yet been fully assimilated by the adaptive observer who is still learning to compress the data better.
  - **Source location:** Section 2.4, Subjective Interestingness as First Derivative of Subjective Beauty: The Steepness of the Learning Curve (arXiv:0812.4360v2)
- **Source extract (verbatim):** A visionbased agent that always stays in the dark will experience an extremely compressible, soon totally predictable history of unchanging visual inputs. In front of a screen full of white noise conveying a lot of information and “novelty” and “surprise” in the traditional sense of Boltzmann and Shannon [102], however, it will experience highly unpredictable and fundamentally incompressible data. In both cases the data is boring [72, 88] as it does not allow for further compression progress. Therefore we reject the traditional notion of surprise.
  - **Source location:** Section 2.6, True Novelty & Surprise vs Traditional Information Theory (arXiv:0812.4360v2)
- **Source extract (verbatim):** In absence of external reward, or when there is no known way to further increase the expected external reward, our controller essentially tries to maximize true novelty or interestingness, the first derivative of subjective beauty or compressibility, the steepness of the learning curve. It will do its best to select action sequences expected to create observations yielding maximal expected future compression progress, given the limitations of both the compressor and the compressor improvement algorithm.
  - **Source location:** Section 2.7, Attention / Curiosity / Active Experimentation (arXiv:0812.4360v2)
- **Source extract (verbatim):** The previous sections only discussed measures of compressor performance, but not of performance improvement, which is the essential issue in our curiosity-oriented context. To repeat the point made above: The important thing are the improvements of the compressor, not its compression performance per se.
  - **Source location:** Appendix A.5, Measures of Compressor Progress / Learning Progress (arXiv:0812.4360v2)
- **Source extract (verbatim):** Note that both the old and the new compressor have to be tested on the same data, namely, the history so far.
  - **Source location:** Appendix A.5, Measures of Compressor Progress / Learning Progress, following equation (5) (arXiv:0812.4360v2)

## Connections Found

For the creativity question, the paper is a formal anchor for the pattern-learning component of [observer-relative information value](../notes/information-value-is-observer-relative.md): an object's interestingness depends on what a particular learner can newly understand, not on novelty alone. Its distinct contribution is the change in coding performance, rather than merely the amount of accessible structure. This does not establish goal-relative usefulness in general.

The controller is a concrete comparison for [allocating search before decisive evaluation](../notes/open-ended-improvement-allocates-search-before-evaluation.md). It chooses experiences using expected learning progress and receives measured progress later. That separation helps distinguish a proposed motive for creative exploration from evidence that the resulting creation is useful. The paper also supports the need to state [which objective defines improvement](../notes/self-improvement-is-relative-to-a-declared-objective.md): intrinsic compression reward and external task reward are explicitly separate, and their helpful alignment is assumed rather than guaranteed.

## Learning Claims (our opinion)

The learner has two coupled update processes. A compressor learns regularities in the action-observation-reward history; a controller learns which actions create opportunities for further compressor improvement. Appendix A.5 compares old and new compressors on identical data. Appendix A.6 freezes a history for an asynchronous comparison, so delayed reward requires the controller to assign credit to earlier actions. A.3–A.4 allow compression length alone or a measure that also charges for computation time. These choices change what progress means.

This is broader than a [theory builder](../notes/definitions/theory-builder.md) and does not require one. The framework leaves condition 1 open: a neural predictor improved by fitting satisfies its mechanism with no unit that says anything, while an explicit predictive program would be stated in a formal language. What the framework does fix fails condition 3: compression progress scores a new compressor against an old one on the same history, and that score rewards and selects without a stated reason bearing on what the compressor says. The retained history records actions, observations, and rewards, which is the input-and-outcome baseline that condition 4 excludes. An implementation that revised explicit programs through criticism of their content could be a builder; the objective does not require that operation. The source adds an explicit account of how learning can select its own future evidence; it does not supply a diagnosis procedure for repairing a KB theory.

The framework leaves the compressor class, improvement algorithm, action interface, and much of the controller design open. In any concrete implementation, those choices bound which regularities can be learned and which experiences can be produced. Progress within such a configuration does not establish the adequacy of its fixed choices, as [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains. Section 3 surveys implementations with different predictors and rewards; it is not a matched comparison that isolates the best decomposition. Section 3.2's warning about prediction-error reward is particularly useful: persistent error can attract exploration without producing improvement.

## Extractable Value

1. **Creative connections can reveal shared structure.** Sections 2.10–2.16 propose that combining familiar elements becomes interesting when a learner discovers a regularity that shortens their joint description. This gives an explanatory candidate for why some combinations teach or surprise while arbitrary juxtaposition does not. Its reach is observer-relative; it is neither a complete definition of creativity nor an empirical test of every creative practice. [quick-win]

2. **The LLM comparison needs a specified learning loop.** The paper supplies a conditional test, not evidence about current deployments. A system that only samples from a fixed predictor does not thereby implement reward for improving that predictor. Updating a predictor on supplied training data supplies one ingredient; the full mechanism additionally requires action selection responsive to measured or expected improvement. An LLM-based system could implement those functions through changing context, external memory, programs, or weights, but each proposed mapping needs an identified compressor, a before/after comparison, and a causal route from progress to later choices. An output could help its human reader discover structure without showing that its generator learned or pursued intrinsic reward. [deep-dive]

3. **Progress must be measured on a common observation set.** The old/new comparison in A.5–A.6 is a reusable design constraint for a KB experiment. Shorter notes or easier newly selected examples would not by themselves establish better compression of the same evidence. A transfer test would preserve the evaluated observations and separately check whether the resulting representation improves downstream decisions. This adds an operational measurement constraint to the existing search-allocation account. [experiment]

## Limitations (our opinion)

The broad account of human creativity is underdetermined by the evidence presented. The drawings and autobiographical examples illustrate possible regularities and rewarding discovery, but do not discriminate compression progress from alternatives such as familiarity, task mastery, or social reward. The author separates external rewards conceptually; the examples do not experimentally isolate them. Section 5 explicitly proposes controlled psychological and neurophysiological tests beyond the anecdotal evidence.

Section 3 reports earlier implementation successes, including faster acquisition of external reward, without presenting a new matched benchmark or sufficient results here to assess effect sizes and competing design choices. Several practical reward signals are approximations, including predicted predictor changes and prior/posterior divergence; they should not be treated as interchangeable empirical measures of saved description length. The theoretical optimality discussions do not establish practical efficiency for an implementable controller.

Compression improvement is an objective about an observer and its history. It does not alone establish causal truth, transfer to new situations, task usefulness, or the artistic value of an output. Section 1.3 expressly sets aside harmful curiosity. Full-history storage and repeated evaluation also carry costs that the paper identifies as subjects for further work. The captured text includes figure captions but does not preserve the rendered visual experience, limiting independent assessment of its aesthetic illustrations.

The source predates current LLM systems and tests none of them. Its applicability therefore remains a mechanism comparison: neither creative-looking generation nor apparent discovery in a conversation proves a compression-progress drive. Conversely, failure to instantiate this particular drive would not establish that a system cannot produce creative work.

## Recommended Next Action

Schedule a focused brainstorm on the LLM creativity question, using this paper to separate an output that reveals structure to its reader from a generator whose own learning progress measurably controls its subsequent search.

---

Relevant Sources:

- [Driven by Compression Progress, arXiv v2](https://arxiv.org/abs/0812.4360v2) — derived-from: formal framework, historical implementations, and proposed account of creativity
