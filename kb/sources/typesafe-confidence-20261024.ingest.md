---
description: "TypeSafe documents confidence as a distribution statistic and risk-based routing signal, not validated correctness or evidence of Jev/Basal equivalence."
source: https://docs.typesafe.ai/confidence
captured: "2026-10-24"
capture: trafilatura
capture_scope: partial-source
genre: official-statement
snapshot_sha256: a6058cdbe823de1bc3804d4f3b26b71b710a0959a522d9fd3425f109802a4c1c
ingested: "2026-10-24"
occasion: "Investigate Jev and Basal model strengths, weaknesses and suitable bounded KB uses before future Commonplace use; no model selection or deployment is commissioned."
type: types/ingest-report.md
domains: [typed-decisions, uncertainty, model-evaluation]
---

# Ingest: TypeSafe confidence documentation

## Classification

Official product documentation explaining intended answer semantics and recommended application behavior. It contains no empirical evaluation of confidence calibration, error discrimination or workflow outcomes.

Author: TypeSafe, the provider describing its own interface. This is a direct source for intended semantics, not independent evidence of reliability.

## Summary

TypeSafe describes `confidence` as a deterministic summary of the probability distribution returned with Choice and Score answers, on a scale from 0 to 1. Choice confidence uses the winning probability relative to an even split; Score confidence also considers distance between ordered levels. Noul returns a yes probability without a separate confidence field. The documentation exposes the underlying distributions, suggests alternative summaries, and recommends high-, medium- and low-confidence response paths with thresholds chosen for task performance and action risk. This makes uncertainty available to application policy but does not demonstrate that the statistic predicts correctness. The capture omits rendered mathematical expressions and example distributions, so it supports these qualitative distinctions, not exact formulas or numerical verification.

## Quotes

> `confidence` is a statistic computed from the probability distribution the answer already gives you. TypeSafe computes it for you and returns it on every Choice and Score answer, so the common case needs no extra work on your side.
> --- `kb/sources/.snapshots/typesafe-confidence-20261024.md` @ `sha256:a6058cdbe823de1bc3804d4f3b26b71b710a0959a522d9fd3425f109802a4c1c`

> A confidence threshold is not one number. Different actions within the same system should be gated at different levels depending on the consequences of getting it wrong.
> The correct threshold values depend on your domain and the performance of the model for your use case. Start with conservative thresholds, test with your own data, and adjust as you observe results.
> --- `kb/sources/.snapshots/typesafe-confidence-20261024.md` @ `sha256:a6058cdbe823de1bc3804d4f3b26b71b710a0959a522d9fd3425f109802a4c1c`

## Connections Found

For the Jev/Basal investigation, this source supplies an interface-level distinction rather than evidence for choosing a model. The [Basal model-card ingest](./basal-2-0-max-20261024.ingest.md) records producer-reported fitted calibration and accepted-case error/coverage. TypeSafe instead documents a default distribution summary and advises local threshold testing. These are distinct operations: defining a statistic does not fit or validate an acceptance policy. Shared primitive names do not establish shared models, formulas, calibration or interchangeable interfaces.

The pinned historical [mem review](../agentic-systems/reviews-archive/instinctual-memory.md) places Jev in optional requested retrieval ranking. That is a different job from using typed-answer uncertainty to choose whether to proceed or defer. Neither that review nor this page establishes Jev's probability semantics, its relationship to TypeSafe, or relative quality against Basal.

The source is also a concrete comparison for [Generation confidence does not by itself certify soundness](../theory/generation-confidence-does-not-by-itself-certify-soundness.md). The note concerns next-token generation probability; TypeSafe describes a typed-answer distribution statistic. Their shared issue is the need to establish a relationship to correctness separately, not identical readout mechanics. The documentation illustrates the distinction but does not empirically test the note's claim.

## Extractable Value

1. **Separate score jobs before comparing Jev and Basal.** Record whether a score ranks retrieval relevance, summarizes answer uncertainty, or supports a validated selective-acceptance policy. This source adds the distribution-summary case to the existing Jev placement and Basal calibration records; it does not connect their implementations. [quick-win]
2. **Keep future KB use advisory until locally evaluated.** Review-priority suggestions or proposed document routes with explicit deferral are plausible bounded uses of the documented interface. Retaining full distributions would permit later comparison of the default confidence, top probability and runner-up separation. No Commonplace benefit is demonstrated, and exact-statistic comparisons require a new capture preserving the missing mathematics. [experiment]
3. **Treat escalation as a separate application decision.** The page distinguishes confirmation, information gathering, human routing and fallback rather than making every threshold failure equivalent. A future evaluation should specify the response as well as measure errors and coverage; the provider's high-confidence automation example is not permission to accept notes or certify source truth automatically. [quick-win]

## Limitations (our opinion)

The partial-source capture loses rendered formulas, operands and example distributions. It cannot establish exact calculations, verify the numerical examples, or support a compatible implementation. No formula has been reconstructed from background knowledge or another artifact. A new observation preserving the expressions would be needed for those uses; the retained bytes should not be repaired in place.

The documentation explains a statistic, not observed calibration or discrimination. A concentrated distribution can still select the wrong answer. Its language about honest uncertainty is an intended interpretation, not evidence of privileged access to correctness. The common 0–1 range does not establish equivalent error rates across question types, option sets or tasks. The page itself advises conservative thresholds and testing on the user's data; its Noul starting thresholds are suggestions, not certified operating points.

No model identity, training procedure, implementation inspection, benchmark execution or end-to-end recovery result is supplied here. Threshold advice does not test whether caller-defined options cover a KB task, whether ordered levels preserve the relevant distinctions, or whether deferral actually reaches an effective reviewer. The source therefore supports an investigation vocabulary and candidate response patterns, not model selection, comparative performance conclusions or deployment.

## Recommended Next Action

Draft a source-grounded Jev/Basal comparison brief separating retrieval relevance, distribution confidence and calibrated acceptance, with explicit unknowns for each and review-priority suggestions as a bounded KB use to investigate rather than deploy.
