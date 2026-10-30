---
description: "Nostalgebraist reports persistent coding-agent blunders and weak prioritization despite rising capabilities, motivating scrutiny of supervision costs, correction retention, and benchmark blind spots."
source: https://www.lesswrong.com/posts/Gsj36znHDKAihs9qG/nostalgebraist-s-shortform?commentId=5gxpoDRpAoLzKcfa7
captured: "2026-10-30"
capture: lesswrong-embedded-json-html
capture_scope: excerpt
genre: practitioner-report
snapshot_sha256: 912b32f81520bf70339afd492e509bafe66ed240ef9953cf2cbb4c0772c9c716
ingested: "2026-10-30"
type: types/ingest-report.md
learning_claims: true
domains: [coding-agent-judgment, supervision-cost, benchmark-blind-spots, correction-retention]
---

# Ingest: Nostalgebraist on coding-agent mistakes and benchmark gaps

## Classification

A first-person account of coding-agent use, with a conceptual footnote about evaluation incentives. Its main evidence is the author's reported experience, not a controlled benchmark or longitudinal study. Author: nostalgebraist, a pseudonymous practitioner describing direct use and checking session logs; the capture does not establish an independently audited usage history.

## Summary

Nostalgebraist reports that coding agents have become useful through speed and broad knowledge while continuing to make basic mistakes and pursue low-value directions. Examples include an allegedly unnecessary concurrency limit reducing throughput eightfold and expecting identical unseeded inference outputs at temperature 1. Close supervision reportedly makes the collaboration work, but repeatedly supplying judgment and priorities leaves the author unsure how to use increasingly autonomous agents. The author also objects that successive agents do not accumulate the practical lessons a human trainee would retain. A quoted Anthropic account supplies a secondhand parallel about indiscriminate demands on human attention. The footnote conjectures that optimization absorbs easily formalized evaluation gaps, leaving important deficiencies harder to articulate; it argues against dismissing those deficiencies merely because measured performance improves. The source supplies concrete complaints and a hypothesis about evaluation, not evidence that judgment has stagnated across a controlled sequence of models.

## Quotes

No source quotes have been retained yet.

## Connections Found

This is a bounded practitioner illustration of [Unattended work needs the functions that interaction supplied](../theory/unattended-work-needs-the-functions-that-interaction-supplied.md): human steering supplies correction and decisions about which directions deserve further work. It makes the dependency vivid without testing the note's inventory or proving that a particular replacement would work. The source's no-accumulation claim also compares with [Retained system-definition artifacts enable persistent deployment-time adaptation](../theory/retained-artifacts-enable-persistent-deployment-time-adaptation.md). That note identifies an external retention path the source does not examine. This comparison limits a claim about agents in general; it does not show that retaining instructions would cure the author's prioritization failures.

## Learning Claims (our opinion)

The source contrasts human trainees' accumulated practical know-how with repeated corrections to successive agents. It describes no implemented learning mechanism. Its implied requirement is that criticism should change later choices, not merely elicit agreement during the current exchange. Under the [theory-builder definition](../theory/definitions/theory-builder.md), localized content is visible in the reported false statements and explicit proposals; consumption is suggested by choices that guide execution, though no trace establishes how a particular statement caused a choice. Content-directed criticism is directly reported as the operator challenging mistakes and low-value work. Iteration is less secure: supervised work reportedly succeeds, but agreement alone does not establish that a correction shapes the next round. Across fresh agent interactions, the author reports recurrence rather than retained improvement. These observations do not establish absence of learning within a run or across an augmented human–agent system.

Our interpretation is a missing or ineffective retention-and-consumption path, not proof of an intrinsic inability to learn without weight updates. The retained-artifact account offers a possible system-level response, but the source supplies neither a retention intervention nor later-task measurements of improved capacity. Likewise, the benchmark footnote describes optimization against expressible evaluations without specifying training histories, available signals, or the effective update space. Under [Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), it remains open whether practical judgment is excluded by the evaluation setup, weakly rewarded, or simply not yet learned. No comparison identifies a fixed representational omission or tests alternative decompositions.

## Extractable Value

1. **Identify what repeated steering supplies.** The reported mistakes and low-value tangents provide concrete cases for separating correction from prioritization and stopping before removing the operator. This adds practitioner illustration to the existing unattended-work account, not a new inventory or population estimate. [quick-win]
2. **Test whether a correction survives the session.** Repeated explanations to successive agents motivate checking whether a retained, evaluated rule changes later task choices and reduces operator intervention. The external-retention path already exists in the KB's account; this source supplies a failure case to investigate, not evidence of the remedy's effectiveness. [experiment]
3. **Keep hard-to-name evaluation failures open to criticism.** The footnote offers a reason not to equate improving benchmark scores with resolved practical deficiencies. Retain it as a conjectural evaluation warning: it neither identifies the training cause of these mistakes nor warrants rejecting benchmarks generally. [just-a-reference]

## Limitations (our opinion)

The examples lack executable traces, task samples, model and harness controls, and measured intervention costs. The eightfold throughput loss is the author's report, not a reproduced result. Task difficulty, ambition, and workflow may have changed alongside models, so persistent frustration does not establish a flat capability trend or negative net productivity. The author explicitly raises alternative explanations, including task mismatch and personal standards. The embedded Anthropic quotation was not independently checked and cannot serve here as independent corroboration.

The benchmark argument does not show which evaluations were optimized or why the remaining mistakes occurred. Poor generation, poor detection, missing context, harness choices, and weak retention remain competing explanations. The trainee and childcare analogies describe the experience but do not explain its mechanism. As the unattended-work note emphasizes, identifying a human dependency does not validate its replacement.

The capture contains the complete linked top-level comment and footnote but excludes replies and other shortform entries. It therefore cannot establish whether later discussion supplied counterexamples, clarified the setup, or revised the author's claims.

## Recommended Next Action

Review `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md` for adding this source as a bounded practitioner illustration of operator-supplied correction and prioritization, without treating it as evidence of model-wide stagnation.
