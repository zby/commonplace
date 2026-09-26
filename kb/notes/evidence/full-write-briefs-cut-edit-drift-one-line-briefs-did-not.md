---
description: "Pre-registered pilot, 95 edit runs on 10 KB documents: a full retained write brief cut dropped commission items by about two thirds, a brief rebuilt from the commissioned document did nearly as well, and a one-line brief matched no brief"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [evaluation, document-system]
---

# Full write briefs cut edit drift; one-line briefs did not

In one pre-registered pilot, writers editing a KB document under pressure dropped far fewer of its commissioned requirements when they were given the document's full write brief. A brief rebuilt afterwards from the commissioned document and its backlinks did nearly as well. A one-sentence brief did no better than no brief. The pilot tested the [per-artifact write-brief proposal](../../reference/proposals/per-artifact-write-briefs.md) on 2026-09-26. Its protocol was frozen at commit `05f3c44a` before any run, and the results were recorded at `1d76442f`.

## What was tested

Ten existing documents each had a commission written before their final draft: a brief from a multistage writing run or a workshop framing. The set was five notes whose titles state their claim, two instructions, two articles and one synthesis note. Each commission was cut to the items that bind the document rather than the original run, then split into checkable items (378 in total). Each item was labelled *recoverable* if the document, its backlinks, and its type and collection contracts would warn a careful editor to keep it, and *non-recoverable* otherwise.

Every edit started from the version the commissioned write produced, not today's version. Each writer ran `cp-skill-write` in edit mode on a copy. It received one pressure request that invited drift without naming the items at risk, for example "cut to 60%", "rewrite for a newcomer" or "add a compact comparison table". There were four arms:

- A: no brief;
- B: the original commission;
- C: a brief rebuilt by a separate agent from the commissioned document and its backlinks only, to the same length;
- D: one sentence of at most 250 characters condensed from the original.

Each target ran twice per arm (80 pressure runs), plus 15 override runs whose request legitimately changed one named item. Two scorers checked every item blind to arm. They agreed on 98.9% of 3,591 item scores, and a third scorer settled the rest.

## Results

Items broken in the pressure runs, per arm. The two runs that stopped with a question instead of an edit are excluded; see Limits.

| Arm | Non-recoverable items | Recoverable items | Must-keep and exclusion items |
|---|---|---|---|
| A — no brief | 14 / 78 | 10 / 572 | 19 / 481 |
| B — original brief | 5 / 80 | 2 / 618 | 7 / 516 |
| C — rebuilt brief | 6 / 78 | 9 / 572 | 10 / 481 |
| D — one-line brief | 13 / 80 | 11 / 618 | 20 / 516 |

Against the frozen predictions:

- **A brief helps most where the document gives no warning.** Survived. B broke 9 fewer non-recoverable items than A. The gap in violation rate was 11.7 points on non-recoverable items and 1.4 points on recoverable ones.
- **Titles that state the claim reduce the brief's value.** No support. The mean per-target gap was 0.104 for the five claim-titled notes and 0.107 for the rest.
- **A brief rebuilt from the finished document does worse.** Refuted. C broke one more non-recoverable item than B, and the refutation line was one.
- **A brief does not silently over-constrain.** Survived. All 15 override runs made the requested change and said which commissioned item they amended.
- **A one-line brief keeps the claim but loses the boundaries.** Refuted in the "adds nothing" direction. D matched A on every group of items. Both arms already kept the governing claim and reader update almost without fail (2 breaks in about 90).

## Inference

For preserving a commission through a later edit, what mattered in this pilot was an explicit, complete statement of what the document must keep and must exclude. That statement did not have to be recorded before drafting. A reader-level summary did not help, because writers already recover the claim from a claim-bearing document. What they drop are the boundaries, and one sentence cannot carry those.

The limit on the rebuilt-brief result is its starting point. The rebuilt briefs were inferred from documents that still realized their commission. An observational trace of the same ten documents found something different about the state they are in today. Of the 350 commissioned items the commissioned versions realized, 83 (24%) had since been weakened or removed. 36 of those losses had no record, or 19 if one never-promoted rewrite is set aside. A brief rebuilt from a document that has already drifted would encode the drift. So the evidence supports rebuilding a brief while the document is still faithful. It does not support rebuilding one later.

## Limits

- **Size.** Ten targets and two replicates. The verdicts rest on differences of a few items.
- **Model family.** Writers, brief rebuilders and scorers were all Claude Opus models.
- **Brief quality.** The original briefs were careful, operator-directed commissions and are not typical.
- **Pre-registration conflict.** The protocol both called a writer's question "a valid outcome" and counted any run that did not complete its request as a full failure. A rule fixed before unblinding counted the two question runs, one in arm A and one in arm C, as breaking every item. Under that rule the rebuilt-brief and one-line conjectures survive, because each question run on a 61-item document adds about 50 violations. The operator chose the exclusion reading as primary after unblinding. The verdicts on those two conjectures therefore rest on that choice.
- **Undelivered content.** No arm reliably restored commissioned content the original write never delivered: 2–5 additions in 38 opportunities per arm.

---

Relevant Notes:

- [Per-artifact write briefs](../../reference/proposals/per-artifact-write-briefs.md) — see-also: the proposal whose conjectures this pilot tested; its options and delivery routes
- [Warranted reader update is the objective of substantive writing](../warranted-reader-update-is-the-objective-of-substantive-writing.md) — grounds: the reader update is one of the commission item kinds this pilot separated from boundaries
- [Knowledge storage does not imply contextual activation](../knowledge-storage-does-not-imply-contextual-activation.md) — extends: a brief changed edits only when delivered into the writer's context; this pilot measures how much, and which kind of content, that delivery preserved
