---
description: Three-take Auto Research field report where optimization only worked after manual error analysis, failure taxonomy design, and judge calibration across the Three Gulfs.
source: https://x.com/nurijanian/status/2035257434365976671
captured: "2026-03-21T19:45:41.107797+00:00"
capture: xdk
genre: practitioner-report
snapshot_sha256: 1dc1ef267ff8461036b2be14622da1d06ace013cca0ef2db896a9658cb6521aa
status_id: 2035257434365976671
conversation_id: 2035257434365976671
post_count: 1
ingested: "2026-03-21"
type: kb/sources/types/ingest-report.md
domains: [evals, verification, skill-optimization]
---

# Ingest: Improving AI Skills with autoresearch & evals-skills

## Classification
First-person report of three concrete implementation attempts, what changed between attempts, and what failed before success improved.
Author: Nurijanian is reporting direct hands-on iteration with Auto Research and eval tooling; useful for workflow signals, but not a controlled or generalized benchmark.

## Summary
The source argues that automated skill optimization only works after manual comprehension and specification work are done. Across three iterations, the author found that letting tooling auto-generate inputs and judges produced superficially higher scores but worse real behavior, because the objective was ungrounded in observed failure. Improvement came only after manually reading outputs, building a failure taxonomy (open coding -> axial coding), writing judges from that taxonomy, and calibrating judges on a small hand-scored set before rerunning optimization. The "Three Gulfs" framing (comprehension, specification, generalization) is the core contribution: the optimization loop addresses generalization, but only after human work closes comprehension and specification.

## Quotes

- **Source extract (verbatim):** The scores were up shortly. It all looked great until I looked at what's changed. Unfortunately, the skills were far from improved. The problem wasn’t the tool. Auto Research did exactly what it was designed to do: run a systematic optimization loop against whatever criteria you give it. The issue was the criteria. They were machine-generated with no model of what real failure looked like, no grounding in actual observed behavior. So the loop ran hundreds of experiments and got very good at satisfying those criteria. The skill got better at the wrong things.
  - **Source location:** Post body, “Take one” account
- **Source extract (verbatim):** The Gulf of Comprehension is the gap between what you think your system does and what it actually does. What failure actually looks like in the outputs, which cases break, in which ways, for which reasons. It’s the first gulf because, as far as I can tell, it has to be closed before anything else can work. No automation can close it. Only reading closes it. The Gulf of Specification is the gap between what you want your system to do and what your judges actually measure. This seems to be the direct consequence of skipping comprehension. If you haven’t seen real failure, I don’t think you can write a judge that measures what matters. In takes one and two, my judges were measuring something they imagined. Optimizing against that was optimizing against a fantasy. The Gulf of Generalization is the gap between how the system performs on your test inputs and how it performs on inputs it’s never seen. This is the gulf that Auto Research’s optimization loop actually addresses. But only if the first two are already closed.
  - **Source location:** Post body, “Take three” and “Three Gulfs” discussion
- **Source extract (verbatim):** Open coding. Run your skill on a set of diverse inputs and read every output. Don’t categorize yet. Just write freeform notes on what’s wrong. Which outputs are too generic. Which miss constraints the input spelled out. Which are off in a way you can feel but couldn’t have predicted. This is where you build intuition about failure that no tool can build for you. Axial coding. Take those freeform notes and group them into a coherent failure taxonomy: a small set of distinct, binary failure categories. “Too abstract,” “missed enterprise constraints,” “wrong level of specificity.” These become the thing your judges should actually measure. Write judges grounded in the taxonomy, written against what you saw. Validate the judges. Build a mini golden dataset: manually score fifteen to twenty outputs per criterion before trusting any judge to run autonomously. This is how you calibrate the Gulf of Specification: you check whether the judge agrees with your own labels on cases you’ve already reasoned about. Then you run Auto Research, and only then.
  - **Source location:** Post body, error-analysis procedure
- **Source extract (verbatim):** For take three, I ran this sequence on the skill I’d been trying to improve. I varied the inputs. Then I read everything it output. I coded failures (freeform in chat, which is not right), and the LLM grouped them, built the taxonomy, wrote judges against it, and I validated them manually on fifteen outputs. Then the loop ran.
  - **Source location:** Post body, “For take three” account

## Connections Found
`/connect` found strong links to [spec-mining-as-codification](../notes/spec-mining-as-codification.md) (**exemplifies**), [specification-strategy-should-follow-where-understanding-lives](../notes/specification-strategy-should-follow-where-understanding-lives.md) (**exemplifies**), and [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) (**exemplifies**). It also connects to [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) (**extends**) and [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) (**exemplifies**) through the judge-calibration step. The key fit is that this source adds practitioner evidence for a phase-gated view of automation: objective construction remains human-gated before loop automation becomes useful.

## Extractable Value
1. [quick-win] Add a phase gate to evaluation workflows: require explicit completion of comprehension -> specification -> generalization before running optimization loops; this has high reach because it explains why optimization can improve the wrong target.
2. [experiment] Treat judge creation as spec mining: mine criteria from observed failures, then calibrate on a hand-labeled mini set before trusting autonomous runs; high reach because it operationalizes verifier construction rather than tool-specific tuning.
3. [quick-win] Introduce a "manual read quota" (for example, read and annotate N outputs before each judge revision) as a hard precondition; high reach because it directly protects against fantasy objectives across domains.
4. [experiment] Keep tuple-based synthetic input generation, but only after failure-taxonomy grounding; medium reach because coverage improvements transfer broadly, while the exact tuple schema is context-bound.
5. [just-a-reference] Use this source as external evidence for the oracle bottleneck argument in automation notes; low-to-medium reach because it is a single-team observational report.

## Limitations (our opinion)
This is a sample-of-one practitioner narrative, not a controlled study. Multiple variables changed at once between takes (course study, manual reading, taxonomy quality, judge design, calibration), so causal attribution to any single change is weak. Reported score/quality improvements are not paired with rigorous held-out evaluation, so the Gulf of Generalization claim is asserted more than demonstrated. The strongest claim ("no automation can close comprehension") may be directionally right but is not hard-to-vary yet: a simpler account is that spending focused attention on outputs improved the objective, regardless of specific framework terminology. This is consistent with [specification-strategy-should-follow-where-understanding-lives](../notes/specification-strategy-should-follow-where-understanding-lives.md): understanding may emerge through observation, but the source does not test whether alternate workflows could surface that understanding with less manual effort. Context factors (skill type, model choice, judge implementation details, budget) are also underspecified, limiting transfer confidence.

## Recommended Next Action
Write a note titled "Evaluation automation is phase-gated by comprehension" connecting to [spec-mining-as-codification](../notes/spec-mining-as-codification.md) and [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — it would argue that optimization loops should be blocked until failure-taxonomy and judge-calibration gates are met.
