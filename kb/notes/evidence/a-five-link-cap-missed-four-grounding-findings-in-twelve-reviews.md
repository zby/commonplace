---
description: "A paired Commonplace assay found five capped-versus-uncapped grounding outcome divergences; one reproduced as reviewer noise, while four appeared only after fuller reading reached 6–16 linked artifacts"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [evaluation, kb-maintenance]
---

# A five-link cap missed four grounding findings in twelve reviews

A 2026-08-25 Commonplace assay compared `semantic/grounding-alignment`
reviews of the same twelve notes under the production five-link instruction and
an otherwise identical uncapped criterion. Five outcomes diverged. One warning
also appeared when the capped criterion was repeated on that note after reading
all three available artifacts, so it is attributable to reviewer sensitivity
rather than the cap. The other four divergences appeared only under fuller
reading: two WARN and two FAIL results after opening 6, 11, 14, or 16 distinct
linked artifacts.

This is bounded evidence that the five-link instruction could hide material
grounding findings in this review setting. It is not an estimate of the
probability that any grounding review is wrong.

## Method

The sample reused twelve source-citing notes selected from a frozen 68-note
population by bivariate coverage of available artifact count and whole-file
bytes. Offers ranged from 3 to 23 distinct linked artifacts and from 21,599 to
322,097 bytes. Every capped baseline was PASS after an earlier repair pass.

Both arms used the `codex` partition, concrete worker `gpt-5.4`, effort `high`,
one note per job, and one fresh isolated worker context per job. The uncapped
criterion differed from the production criterion only in its identifier, name,
and replacement of the five-link sentence with an instruction to read all
material bearing on cited claims. Each uncapped job used the same target-note
snapshot as its capped baseline. Five capped reviews were then repeated to
measure outcome disagreement under an unchanged criterion.

## Paired outcomes

`Opened` is the number of distinct pre-resolved artifacts reported in review
consumption telemetry. The capped job is the current PASS at the experiment's
freeze, before the repeat arm replaced some baselines.

| Note | Capped job | Capped outcome, opened | Uncapped job | Uncapped outcome, opened/available | Reading |
|---|---:|---|---:|---|---|
| `automating-kb-learning-is-an-open-problem` | 8202 | PASS, 5 | 8220 | PASS, 22/22 | outcome agreement |
| `axes-of-artifact-analysis` | 8203 | PASS, 5 | 8221 | PASS, 20/23 | outcome agreement |
| `checked-outcome-licenses-episode-retention-not-abstraction` | 8204 | PASS, 5 | 8222 | PASS, 10/10 | outcome agreement |
| `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | 8205 | PASS, 5 | 8223 | FAIL, 14/14 | missing retained support for two HyperAgents details |
| `context-contamination-operates-below-an-agents-compliance-reasoning` | 8214 | PASS, 5 | 8224 | PASS, 8/8 | outcome agreement |
| `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | 8207 | PASS, 3 | 8225 | WARN, 3/3 | repeated under the capped criterion; reviewer sensitivity |
| `diagnostic-richness-constrains-outer-loop-learning-quality` | 8208 | PASS, 5 | 8226 | WARN, 6/6 | ingest analysis described as evidence beyond retained Quotes |
| `files-defer-centralized-schema-commitment-until-invariants-stabilize` | 8219 | PASS, 5 | 8227 | PASS, 11/11 | outcome agreement |
| `llm-generation-relaxes-goals-where-human-writing-stalls` | 8210 | PASS, 4 | 8228 | PASS, 4/7 | outcome agreement |
| `theory-mediated-learning-may-improve-sample-efficiency-under-shifts` | 8216 | PASS, 5 | 8229 | PASS, 21/21 | outcome agreement |
| `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | 8217 | PASS, 5 | 8230 | WARN, 11/11 | two target-side transfers not marked as hypotheses |
| `treat-continual-learning-as-representational-form-coevolution` | 8218 | PASS, 5 | 8231 | FAIL, 16/16 | broader mechanism attributed to a link that disclaims it |

The uncapped arm returned 7 PASS, 3 WARN, and 2 FAIL. Its consumed whole-file
bytes by job were 322,097; 254,004; 81,152; 132,615; 84,622; 21,599;
195,965; 107,915; 39,497; 203,329; 135,466; and 168,153. Ten workers read every
offered artifact. The other two stopped after 20 of 23 and 4 of 7. Median
consumption was 11 artifacts; the largest was 22.

## Capped-repeat baseline

| Note | Original capped job, outcome/opened | Repeat job, outcome/opened | Outcome agreement |
|---|---|---|---|
| `automating-kb-learning-is-an-open-problem` | 8202, PASS/5 | 8232, PASS/5 | yes |
| `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric` | 8205, PASS/5 | 8233, PASS/6 | yes |
| `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | 8207, PASS/3 | 8234, WARN/3 | no |
| `files-defer-centralized-schema-commitment-until-invariants-stabilize` | 8219, PASS/5 | 8235, PASS/5 | yes |
| `llm-generation-relaxes-goals-where-human-writing-stalls` | 8210, PASS/4 | 8236, PASS/5 | yes |

One of five repeated outcomes disagreed. It was the same three-artifact note
that warned under the uncapped criterion, and both warning reviews read every
available artifact. That case therefore explains one of the five raw arm
divergences without invoking the cap. The capped repeat of the fourteen-artifact
compounding note again returned PASS, even after opening six artifacts, while
the full fourteen-artifact read returned FAIL.

## What this establishes

The four remaining divergences are aligned with the intervention: they require
6–16 artifacts, all beyond the old cap, and include two material failures. A
cap of 16 distinct artifacts covers every divergent case in this sample and
also matches the p90 offered artifact count measured over the larger 337-target
availability population. The three uncapped tail cases offering 21–23 artifacts
all returned PASS, so this sample supplies no divergent tail fixture that would
justify split-pass review machinery now.

The assay does not identify a general attention price. Artifact count and bytes
remain confounded with each note's evidence need, and the uncapped workers'
natural stopping points do not reveal an exchange rate between another artifact
and more bytes within one artifact.

## Production recertification at sixteen

After the production criterion adopted the sixteen-artifact budget, all 68
notes in the frozen source-citing population were reviewed under the `codex`
partition by fresh isolated `gpt-5.4` workers at high effort. The initial pass
returned 57 PASS, 9 WARN, and 2 FAIL outcomes. Eleven bounded target repairs
resolved those findings. One follow-up warning incorrectly said that a retained
table header was absent; moving that existing exact quote directly above its
rows made the route easier to audit, and a fresh review passed. The final
current baselines are 68 PASS, and the stale selector returns no target for the
frozen population.

All 68 current reviews have complete consumption telemetry. Offers ranged from
3 to 25 distinct artifacts, with p50 11 and p90 18. Reported consumption ranged
from 2 to 16, with p50 9 and p90 13; 58 reviews opened more than the former
five-artifact ceiling. Thirty reviews opened every offered artifact. Of the 38
that opened fewer, 37 reported sufficiency and one reported budget. The sole
remaining budget stop inspected 13 of 21 offered artifacts and named two
unchecked internal argument routes; it did not leave a source route carrying
the note's empirical claims undisclosed.

Whole-file availability totalled 7,890,452 bytes across the population, while
the reported opened paths charged 6,290,366 bytes. Median and p90 consumption
were 89,928 and 144,007 bytes. These are provenance measurements, not model
usage or an attention-price estimate.

The production run therefore exercises the chosen ceiling beyond the paired
sample: ten notes offered more than sixteen artifacts, two reviewers consumed
exactly sixteen, and no final result exposed a material source-grounding
divergence above the ceiling. That observation does not prove the tail safe,
but it supplies no trigger for the deferred split-pass machinery.

## Scope

The sample is selected rather than random, small, and limited to one criterion,
one model partition, and one concrete model. The repeat arm covers five notes,
not all twelve, so the four-case attribution is mechanism-aligned evidence rather
than a formal causal estimate. Because every capped baseline was PASS, the assay
could not observe the opposite transition in which partial reading produces a
false WARN or FAIL that fuller joint support clears.

Review freshness pins the target note and criterion, not linked files. Target
note snapshots matched across arms, and offered byte totals matched on every
divergent row, but exact linked-file bytes were not independently pinned. The
result supports raising this criterion's count cap and measuring the new tail;
it does not support exporting sixteen to other gates or treating it as a stable
capacity of future models.

---

Relevant Notes:

- [Review architecture](../../reference/review-architecture.md) — see-also: documents the two-file freshness boundary that pins the paired note and criterion while leaving linked reading context outside review identity
