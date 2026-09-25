---
description: "X thread on ICLR's reported ~47k submissions and NeurIPS's AI-detector desk rejections; a field case of an automated gate acted on before its discrimination was measured"
source: https://x.com/jonathanschloss/status/2101135922666365032
captured: "2026-09-19T21:41:10.541414+00:00"
capture: xdk
genre: conceptual-essay
snapshot_sha256: 1733aac10bd4571e7c6fdb4a23c881d2c979d969983bf2d86eb9d988f62292d8
status_id: 2101135922666365032
conversation_id: 2101135922666365032
post_count: 2
ingested: "2026-09-19"
type: ingest-report
domains: [evaluation, llm-reliability, scholarly-review]
---

# Ingest: Thread by @jonathanschloss on ICLR volume and AI-detector review

## Classification

Two posts by one author advancing one position: submission volume will force AI screening on large conferences, and the NeurIPS screen already shows what that costs. The author reports no work of his own and runs no study; every figure is relayed from blogs he does not name. That makes this a framing argument resting on secondhand numbers rather than a practitioner report. The second post is a remark about the thread's reach, so `conversation-thread` does not fit either — there is no multi-party discussion — and both genres carry the same limitations lens.
Author: `@jonathanschloss` is not otherwise represented in this KB, and the capture carries no affiliation, role, or link to his own work. The credibility signal is therefore entirely borrowed from the unnamed blogs behind the figures.

## Summary

The thread reports that ICLR's 2026 abstract submissions are approaching 50,000 (one figure seen: 47,647) against 19,525 valid submissions the year before, and asks whether the human review layer survives a jump of that size. Its argument runs through NeurIPS as a warning: by the author's account NeurIPS screened 969 submissions with an AI detector, 42.7% initially landed in the 90–100% AI-generated band and 273 papers scored 100%, and re-running the same tool on the same papers with a narrower text window dropped that band to 12.7%. He reports 178 desk rejections with no appeal, 123 authors ordered to produce version histories, and a rejected author who ran the track chairs' own recent papers through the same detector and got 24–69%. The thread closes with advice to keep drafts and version history and to be specific in AI-use attestations. Read it for the structure of the case — a provenance judgment automated into an irreversible decision while its error rate went unmeasured — not for the numbers, which are relayed and uncheckable from the capture.

## Quotes

- **Source extract (verbatim):** Yes, probably a lot of AI papers. And yes, it'll probably need AI review at that scale. But @NeurIPSConf just ran into this exact wall, and the results were... interesting.
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 2
- **Source extract (verbatim):** Based on some blogs that have come out, NeurIPS screened all 969 submissions through an AI detector. Out of those, 42.7% of submissions initially scored in the 90-100% AI-generated range, and 273 papers hit a full 100%.
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 3
- **Source extract (verbatim):** Resultantly, 178 papers were desk-rejected with no appeal and 123 were told to produce version histories or also be desk-rejected.
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 4
- **Source extract (verbatim):** There are reports that people's submission numbers are getting real close to 50k. The one that I saw plainly stated was 47647.
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 6
- **Source extract (verbatim):** Compared to last year, there were 19,525 valid submissions to ICLR, with 779 desk rejected and 5,042 withdrawn. This left 13,763 papers that needed a decision.
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 7
- **Source extract (verbatim):** To do this, ICLR organized 76,139 reviews from 18,054 reviewers.
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 8
- **Source extract (verbatim):** At ~50k submissions, ICLR is definitely going to have to use some AI review processes, but can the human-review layer scale as well, or is it something that may end up getting dropped?
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 10
- **Source extract (verbatim):** This is speculation at this point, and is based solely on the abstract submissions so far, but the final paper deadline is Sept 25th, and it will sure be interesting how this all plays out.
  - **Source location:** Post 1 of the thread (status 2101135922666365032, 2026-09-19T02:26:55Z), paragraph 11

## Connections Found

This source's role is a field case: an outside institution instantiating failure modes the KB has so far argued from designed systems and its own review machinery. It is evidence for [the augmentation-automation boundary is discrimination not accuracy](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), because the detector was placed on the automation side — desk rejection, no appeal, no human adjudication — where per-instance discrimination is what the decision needs; and for [error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), whose TPR > FPR viability condition was never established before deployment, so the only reading of the false-positive side came from a rejected author's ad-hoc probe afterwards. The same reversal makes it a case for [evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md): the generalized judge ran first and comprehension of its behaviour arrived last.

The thread also carries both sides of [review automation should target verifiable subroles before reviewer identity](../notes/verifiable-subroles-before-reviewer-identity.md) in one paragraph — ICLR's hallucinated-reference check is a narrow subrole with a checkable surface that kept at least three humans in front of any desk rejection, while the AI-provenance screen is a role-level authority judgment with no comparable surface. It supplies the missing institutional instance for two notes whose relevant claims are currently unevidenced: the closing caveat of [cheap generation breaks text volume as an effort signal](../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md), which withholds exactly the licence NeurIPS took, and both halves of [history has one chance to become checkable](../notes/history-has-one-chance-to-become-checkable.md) — 123 authors asked after production for a record convertible only at production time, and a stylistic-leakage verdict that moved 70% on one parameter. ICLR's 18,054 reviewers and 76,139 reviews against a reported 2.5x volume jump give [maintenance capacity must match harmful-artifact inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) a numbered instance outside Commonplace's own operations, and illustrate its proxy caveat from the other side: the response substituted a cheap detector for capacity and generated a new repair queue of appeals and version-history demands.

Within `kb/sources/`, it compares with [Hacker News — I'm becoming AI-blind](./hacker-news-im-becoming-ai-blind.ingest.md) on the reliability of style-based detection under consequential decisions, where that ingest records the same fragility at individual reading scale with nothing at stake; comparing them separates "detection is noisy" from "acting on noisy detection is costly." It also compares with the KB's existing scholarly-review cluster, [Beyond "Not Novel Enough"](./beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md) and [Towards automating scientific review](./towards-automating-scientific-review-google-paper-assistant.ingest.md), on the same axis those two designed pipelines address deliberately: choosing an evaluation surface the review system can be checked against before delegating to it. See also [calibrating semantic gates against labelled fixtures](../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md), for which this is a negative case end to end — a fluent per-instance verdict stream with no fixture suite, no field calibration, and an error rate discovered by an outsider.

## Extractable Value

1. **A weak oracle shifts the evidentiary burden onto the producer, and the shift only works for producers who were already recording.** NeurIPS could not verify provenance from the artifact, so it demanded version histories from 123 authors — satisfiable only by authors who had already taken the records route. Commonplace does the same thing when a grounding gate that cannot check a claim from the note requires retained quotes at write time. This coupling is stated by none of the KB's existing notes and is the highest-reach item here. [deep-dive]
2. **First institutional case where the AI-detection licence was taken.** [cheap generation breaks text volume as an effort signal](../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) closes by ruling out exactly this inference, and that caveat — the part most likely to be dropped in transfer — currently cites no instance. [quick-win]
3. **A provenance verdict that moved 70% on one settings change.** Same papers, same tool, narrower text window: 42.7% to 12.7% in the top band. Concrete evidence that a verdict stream can look decisive while its rate is a free parameter, and the negative case for [calibrating semantic gates against labelled fixtures](../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md). [quick-win]
4. **A deployed counter-case for subrole-first review automation.** One conference kept three humans in front of a narrow, checkable reference gate; the other granted role-level authority to a provenance judgment with no checkable surface, and the predicted failure followed. [verifiable subroles before reviewer identity](../notes/verifiable-subroles-before-reviewer-identity.md) argues from designed pipelines only. [quick-win]
5. **Post-hoc demand for a production record.** The 123 version-history orders are a live instance of the boundary in [history has one chance to become checkable](../notes/history-has-one-chance-to-become-checkable.md), and the author's closing advice is the records route stated as practical guidance. [quick-win]
6. **Reviewer-capacity figures against a volume jump.** 19,525 valid submissions, 76,139 reviews, 18,054 reviewers, against a reported ~47,647 abstracts, is the rate comparison in [maintenance capacity must match harmful-artifact inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) with real numbers on the human side. Usable only once the figures are sourced. [just-a-reference]
7. **The primary write-ups behind the numbers are not yet captured.** The thread's four shortened links (NeurIPS info, ICLR info, the ICLR conference page, a graph) are the evidence layer for every quantitative claim above; ingesting them would convert this from a structural case into citable data. [quick-win]

## Limitations (our opinion)

- **Every number is secondhand and unattributed.** The thread relays figures from blogs it does not name, so nothing here is independently checkable. The 969-submission figure is internally odd for a conference of NeurIPS's size and may describe one track or one screening batch rather than the whole conference. Until the primary write-ups are captured, this source supports structural claims about oracle deployment, not quantitative ones.
- **The order of events is left open and must not be inferred.** The thread does not say whether the 178 desk rejections were issued under the 42.7% reading or after the 12.7% re-run. Several readings above — notably whether authors were rejected on verdicts the chairs had already superseded — turn on that, and the ingest does not resolve it.
- **The false-positive probe is suggestive, not a measurement.** One rejected author ran an unstated number of chairs' papers through the detector. Their negative status is presumed rather than established, the sample is self-selected, and no control was held. It indicates that discrimination was unmeasured; it does not supply the rate.
- **The ICLR extrapolation is the author's own speculation.** He says so, and the figures are abstract submissions taken before the 25 September full-paper deadline. Last year 5,042 of 19,525 submissions were withdrawn and 779 desk-rejected, so an abstract count overstates the eventual decision load by an unknown margin.
- **The two conferences are contrasted as if they made comparable decisions.** A hallucinated-reference check and an AI-provenance screen differ in what can be verified at all, and that difference does more work in the comparison than the thread acknowledges — it is the reason the human layer was affordable in one case, not evidence that one conference was more careful.
- **The capture holds the thread and nothing it points at.** The four shortened links and any replies are outside the snapshot, so this ingest can establish what the author asserts and not what his cited material says.

## Recommended Next Action

Update [cheap generation breaks text volume as an effort signal](../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) to cite this ingest against its closing caveat, as the first institutional case in the KB where the licence that caveat withholds — treating surface style as grounds for dismissal — was taken and acted on without appeal. Carry the structural claim only, not the thread's figures.
