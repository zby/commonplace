# Methodological leads: from live incidents to controlled trials

Initial map, 2026-11-14. This is a reading agenda, not a completed literature review. The two retained sources below were checked through their ingest Quotes sections. The additional titles are bibliographic search leads from prior knowledge; their texts and bibliographic details have not been verified in this workshop. They supply no established support for the design yet.

## Targeted consultation, not a prerequisite survey

The general architecture separates affordable live observability from comprehensive capture in controlled investigation. It applies to deterministic systems with changing environments as well as stochastic operations. Incident reproduction and test-fixture construction are additional methodological search areas, not claims of novelty or sources already reviewed here.

The next deliverable is a concrete workflow/provenance design and pilot protocol. Consult this map for specific unresolved questions rather than completing every reading before design begins. Freshness is one consumer of provenance, alongside debugging and experimental reconstruction.

## Organizing research direction

The operator endorsed this lead on 2026-11-14:

> Experimental design for measurement and repair comparison; statistical debugging for failure localization; testing-oracle research for deciding what the measurements mean.

For evaluation where execution remains variable, use experimental design for stochastic simulation as the primary methodological lead, with statistical debugging for diagnosis and testing-oracle research for evaluation validity. Investigate independent replications, task-level comparisons, controlled factors, uncertainty and stopping rules. Investigate how failure-associated trace features become causal hypotheses rather than being mistaken for causes. Investigate how evaluator error can masquerade as procedure bias.

Additional reading leads, not yet inspected: Averill Law's *Simulation Modeling and Analysis*, software testing's oracle-problem literature, and metamorphic testing. For metamorphic testing, ask whether an operation has defensible expected relationships between outputs under controlled input changes when its complete correct output is hard to specify.

Every literature finding should feed a KB design question, principally at the workflow or provenance boundary: what to retain, what to reset, what to compare, when to rerun, and what a result can claim. Repeated trials on one fixture and repeated trials across representative tasks answer different questions. Do not optimize for identical outputs when multiple outputs are acceptable.

## Evidence already retained in the KB

### Repeated agent execution against fixed tasks

[Many AI analysts, one dataset](../../sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.ingest.md) reports 4,946 autonomous analysis runs in a design crossing datasets, models and analyst personas. Its retained source extracts explicitly describe fixed dataset–hypothesis tasks, within-condition distributions and transcript-level auditing. This establishes a relevant experimental precedent for studying distributions of agent behavior, not evidence that the proposed Commonplace maintenance architecture works.

Investigate how its scaffold resets trials, how it distinguishes analytical choices from violations, and what audit uncertainty remains. The transfer question is whether a KB operation can similarly have a fixed task environment while retaining freedom to choose its tool trajectory. Do not transfer the paper's reported compliance rate to Commonplace.

### Fixed sampling settings do not fix every source of variance

[Defeating Nondeterminism in LLM Inference](../../sources/defeating-nondeterminism-in-llm-inference.ingest.md) reports 80 distinct completions in 1,000 temperature-zero trials in one setup, and identical completions after enabling batch-invariant kernels. Its retained extracts identify server-load-dependent batch size as a source of numerical variation.

This is a boundary condition for the proposed experiment: a fixed KB and nominal model configuration do not establish that remaining variation is sampling alone. Record the serving limits without making provider-level determinism a prerequisite for useful local experiments. The report does not establish correctness from repeatability or test complete agent workflows.

## Literature leads to verify

| Area and candidate reading | Question for this workshop | Transfer limit to investigate |
|---|---|---|
| Statistical debugging: Liblit et al., *Bug Isolation via Remote Program Sampling*; *Scalable Statistical Bug Isolation* | Can observations from ordinary runs identify failure-associated conditions that become controlled fixtures? | Correlation across traces need not identify a cause; agent traces and semantic outcomes differ from program predicates. |
| Flaky tests: Luo et al., *An Empirical Analysis of Flaky Tests* | How should repeated tests distinguish intermittent failures, environmental causes and unreliable test judgments? | Variation is often unwanted in conventional tests but expected in an LLM's valid outputs. |
| Statistical model checking: Younes and Simmons, *Probabilistic Verification of Discrete Event Systems Using Acceptance Sampling* | Can bounded repeated runs support a stated failure-probability decision and stopping rule? | Independence, a stable generating process and a reliable observable property may not hold. |
| Randomized algorithm evaluation: Arcuri and Briand, *A Practical Guide for Using Statistical Tests to Assess Randomized Algorithms in Software Engineering* | How should incumbent and repair be compared across repeated runs and multiple fixtures? | Statistical significance on selected diagnostic cases does not establish useful effect size or generalization. |
| ML evaluation variability: Henderson et al., *Deep Reinforcement Learning That Matters*; Agarwal et al., *Deep Reinforcement Learning at the Edge of the Statistical Precipice* | Which aggregation and uncertainty practices prevent a few favorable runs from deciding adoption? | Training-run variability is not identical to inference-time agent trajectory variability. |
| Failure reduction: Zeller and Hildebrandt, *Simplifying and Isolating Failure-Inducing Input* | Once a fixture exposes a failure, can irrelevant context be removed without losing the failure mode? | A stochastic pass/fail predicate may make ordinary reduction unstable; repeated checks and an unresolved outcome may be needed. |
| Simulation experiment design and output analysis | How are warm starts, independent replications, transient state and precision-based stopping handled? | Hosted models may drift and expose no controllable random stream; do not assume textbook simulation conditions. |

These are complementary questions, not competing names for the whole proposal. Prioritize sources that change a concrete capture, trial or inference decision; a broad survey is not itself the goal.

## Quantitative question worth retaining

If independent trials have a fixed probability p of exposing a specified failure, the probability of seeing it at least once in n trials is:

`1 - (1 - p)^n`

This elementary model makes the operator's recurrence intuition testable, but does not guarantee discovery. For example, p = 0.1 gives about a 95.8% chance of at least one failure in 30 trials. Unknown p, dependent trials, a changing model endpoint or a fixture that removes a necessary condition defeat that interpretation. The formula concerns observing a specified failure, not correctly diagnosing it.

Separate three activities:

1. Search for a configuration that exposes the failure.
2. Estimate the failure frequency at that configuration using a declared sampling/stopping plan.
3. Test whether a repair improves outcomes there and on independently selected cases.

Selecting a fixture because it failed and then reporting its frequency as representative production prevalence would conflate these activities. Continuing until a failure appears is useful diagnosis, but is not by itself a valid fixed-sample estimate of a production failure rate.

## Existing Commonplace work to reuse

[LLM debugging diagnosis](../../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md) already warns that failure frequency does not decide whether the instruction is inadequate or the model violated it. The new contribution sought here is an operational bridge from permissive maintenance to controlled investigation, including Git and non-Git state, not a replacement for that diagnosis.

Next research should retain, per inspected source: the exact supported proposition, experimental assumptions, proposed Commonplace use, counterexample or limitation, and whether it changes the workshop design. Do not promote the unverified leads into citations merely because their titles fit.
