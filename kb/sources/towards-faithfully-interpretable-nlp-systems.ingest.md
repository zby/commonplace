---
description: "Jacovi and Goldberg separate faithfulness from plausibility, expose the assumptions behind common explanation tests, and argue for graded rather than binary faithfulness"
source_snapshot: "towards-faithfully-interpretable-nlp-systems.md"
ingested: "2026-07-23"
type: kb/sources/types/ingest-report.md
domains: [interpretability, faithfulness, explanation-evaluation, oversight]
---

# Ingest: Towards Faithfully Interpretable NLP Systems

Source: [towards-faithfully-interpretable-nlp-systems.md](./towards-faithfully-interpretable-nlp-systems.md)
Captured: 2026-07-23
From: <https://aclanthology.org/2020.acl-main.386/>

## Classification

Genre: scientific-paper -- an ACL opinion/survey paper that formalizes a vocabulary for explanation quality, surveys faithfulness tests, and proposes evaluation guidelines rather than presenting a new benchmark.
Domains: interpretability, faithfulness, explanation-evaluation, oversight
Author: Alon Jacovi and Yoav Goldberg; the paper is published in ACL 2020 and the authors have direct interpretability/NLP research standing, while the paper's prescriptive claims are explicitly an opinion piece.

## Summary

Jacovi and Goldberg argue that explanation quality must separate **plausibility** (how convincing an interpretation is to people) from **faithfulness** (how accurately it reflects the model's actual reasoning process). They organize existing faithfulness tests around three assumptions--model, prediction, and linearity--and show how each yields counterexamples or stress tests. Their guidelines reject human utility or user-performance measures as faithfulness tests, reject unverified claims of inherent interpretability, and warn that gold-label evaluation pushes judgments toward what humans think the model should do. Because exact faithfulness is an unrealistically high global bar for approximate explanations, they recommend graded criteria across models/tasks and across regions of input space. This is the conceptual source for the target note's condition that an oversight-saving rationale must be faithful, not merely readable or persuasive.

## Connections Found

The paper is direct evidence for [Reflection may lower oversight cost when its rationale is faithful](../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md): it supplies the faithful/plausible distinction and the warning that utility can increase without validating the explanation's causal truth. It also gives [Reasoning production is not reasoning evaluation](../notes/reasoning-production-is-not-reasoning-evaluation.md) a non-mathematical instance of process validity being distinct from successful output, and it qualifies [Structured output is easier for humans to review](../notes/structured-output-is-easier-for-humans-to-review.md): readability helps a reviewer inspect an artifact but does not establish faithfulness. [Language Models Don't Always Say What They Think](./language-models-dont-always-say-what-they-think.md) is the empirical companion, testing this distinction with controlled input interventions.

## Extractable Value

1. **Faithfulness and plausibility are independent criteria** -- A fluent, convincing rationale can be wrong about the process that generated a decision, so the target note's faithful-rationale condition is load-bearing rather than a synonym for legibility. [quick-win]
2. **Utility is not a faithfulness oracle** -- Better user task performance or trust can reflect correlation between persuasive explanations and correct outputs without showing that the explanation tracks the model's reasoning. [quick-win]
3. **Three assumption families organize faithfulness tests** -- Model, prediction, and linearity assumptions provide a reusable diagnostic vocabulary for asking what a proposed faithfulness check actually presumes. [deep-dive]
4. **Global binary faithfulness is an unrealistic bar** -- The proposed graded view supports keeping the target note's faithful/unfaithful experimental contrast while treating faithfulness as model-, task-, and input-region-relative in later operationalization. [quick-win]
5. **Human judgment can evaluate plausibility while missing faithfulness** -- The paper's warning limits how much oversight can be automated by simply asking a person or model whether a rationale sounds right. [experiment]

## Limitations (our opinion)

This is a conceptual survey and opinion paper, not a new causal evaluation of explanation methods. Its three assumptions are organizing abstractions whose validity varies by method and domain; the paper does not settle which graded faithfulness metric should replace binary tests. The examples and terminology are rooted in 2020 NLP interpretability, so they do not directly measure current chain-of-thought systems, native retained rationales, or an overseer's behavioral-probe count. The paper's claim that human judgment cannot establish faithfulness is strongest as a warning against using plausibility alone, not as proof that every human-assisted assessment is useless.

## Recommended Next Action

Update [Reflection may lower oversight cost when its rationale is faithful](../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md) to cite this ingest where it distinguishes faithfulness from plausibility, and add the graded-faithfulness caveat without weakening the note's controlled faithful-versus-unfaithful test design.

---

Relevant Notes:

- [Reflection may lower oversight cost when its rationale is faithful](../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md) -- evidence: supplies the target distinction and oversight boundary
- [Reasoning production is not reasoning evaluation](../notes/reasoning-production-is-not-reasoning-evaluation.md) -- evidence: separates output utility from process validity
- [Structured output is easier for humans to review](../notes/structured-output-is-easier-for-humans-to-review.md) -- evidence: readability does not entail faithfulness
- [Language Models Don't Always Say What They Think](./language-models-dont-always-say-what-they-think.md) -- compares-with: controlled behavioral test of the conceptual distinction
