---
description: "Aaron Defazio argues that cheaper AI-assisted theory work can move auto-research from experiment search toward predictive models, while problem choice remains human work"
source: https://x.com/aaron_defazio/status/2084779496549548323
captured: "2026-08-18T07:36:59.980126+00:00"
capture: xdk
genre: conceptual-essay
snapshot_sha256: eb66910a34e9f06aefeb2baeb258e9794f9e8f7111a6ebd122ba4efd9dda6b16
status_id: 2084779496549548323
conversation_id: 2084779496549548323
post_count: 1
ingested: "2026-08-18"
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, theory-mediated-learning, auto-research, automation-boundary]
---

# Ingest: A new Era Of Theory-Driven AI Research

## Classification

An X article that advances a thesis through argument, forecasts, and one first-person anecdote rather than a reported study.
Author: Aaron Defazio writes as a researcher with long-running AI-theory problems and reports direct use of a coding agent, but the captured profile supplies no institutional affiliation or independent credibility signal.

## Summary

Defazio argues that frontier coding agents have made mathematical theory development fast enough to lead AI experimentation instead of rationalizing results after the fact. Predictive theory, in his account, should forecast training quantities, select hyperparameters, and eventually guide algorithms, architectures, and losses; this becomes more valuable as agent thinking gets cheaper relative to running training experiments. He says researchers should therefore spend more effort selecting problems, setting quantifiable goals, and moving rapidly between ideas and evidence, while agents automate technical derivation. The article's strongest support is a personal report that an unspecified coding agent made “major progress” within an hour on each of several theory problems he had considered for years.

## Claims

No claims have been grounded yet.

## Connections Found

The source is a current practitioner articulation of the discriminator in [first-principles reasoning selects for explanatory-reach over adaptive fit](../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md): a theory that can explain successful and unsuccessful alternatives equally well has not constrained a prediction. Its proposed payoff compares with [theory-mediated learning may improve sample efficiency under structured shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md), but shifts from reuse after distribution change to using explicit theory before expensive experiments. The recommended rapid alternation among brainstorming, consequences, and evidence is a compressed practitioner version of the [discovery lifecycle](../notes/definitions/discovery-lifecycle.md), with acceptance and integration left implicit.

The source also qualifies [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). It argues that mathematical derivation and theory production are moving into automation while problem selection and impact judgment remain with the researcher, so “research” must be decomposed before its automation boundary can be located. This is the useful contrast with [When code is free, research is all that matters](./when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md): the essays disagree about how much research work is becoming cheap but agree that choosing worthwhile goals remains scarce.

## Extractable Value

1. **Predictive constraint separates theory from retrospective fit.** The article gives the KB a concise practitioner test: if an explanation works just as well for approaches that fail, it has not earned the predictive force required to guide design. This corroborates the existing explanatory-reach test without adding a new theoretical category. [quick-win]

2. **Theory-generation cost and experiment cost may be crossing.** The novel operational conjecture is not merely that agents can do mathematics, but that fast symbolic work may make deriving and comparing predictions cheaper than running another training experiment. If measured, this would change the optimal allocation between reasoning and empirical search in auto-research loops. [experiment]

3. **Automation boundaries cut through research workflows.** The essay separates problem selection, theory construction, experiment execution, and impact judgment instead of treating research as one weak-oracle task. That decomposition refines the existing verification-boundary discussion even if the author's capability forecast is wrong. [quick-win]

4. **A research loop should alternate rather than hand off once.** Defazio rejects both experiment-only search and a long theory-first pipeline tested only at the end. His proposed rapid back-and-forth is a context-bound practitioner restatement of consequence derivation and testing in the discovery lifecycle. [just-a-reference]

5. **The current evidence is a signal for evaluation design, not a capability result.** “Major progress” on every selected problem is striking enough to motivate a controlled before/after study with blinded expert assessment, preserved traces, task sampling, and time-matched human or tool baselines. Until those exist, the anecdote identifies what to test rather than what has been established. [experiment]

## Limitations (our opinion)

The central capability claim rests on one uncontrolled personal intervention. The reported learner could condition on author-selected, long-considered problems and whatever histories, prompts, files, or iterative feedback the unspecified coding agent received. It could compose whatever mathematical, coding, search, and checking operations that harness exposed. The capture does not show which mappings its model and tools could express. Problem selection, representation, prompting, model and tool choice, the meaning of “major progress,” and the absence of a time-matched baseline all remained fixed outside the effective update space. Under [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the anecdote can support usefulness within that setup; it cannot validate those fixed choices or the theory-first decomposition as a whole.

Nor does the intervention establish the article's main outcome: no prospective prediction, experiment avoided, hyperparameter selected, or new algorithm validated is reported. A simpler account is that the agent accelerated algebra, proof search, coding, or exposition on problems whose structure and promising directions the author had already supplied. That would still be useful, but it is weaker than showing that agents now produce theories with predictive power.

As a conceptual essay, the article also leaves its forecasts unargued. It supplies no data for the claimed divergence between intelligence-per-watt and training speed, no failure criterion for the asserted tipping point, and no account of how valid or impactful theory will be selected from increased output. The claim that impactful work will remain apparent may underestimate the same weak-oracle problem the article assigns to human research taste. The author's direct experience is relevant evidence for a newly possible workflow, but self-assessment, selected problems, and an advocacy interest in theory-driven research limit generalization.

## Recommended Next Action

Review [the boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) for a narrow update that cites this snapshot as practitioner evidence that the boundary cuts within research -- automating mathematical theory work before problem selection or impact judgment -- while preserving the source's anecdotal evidence limit.
