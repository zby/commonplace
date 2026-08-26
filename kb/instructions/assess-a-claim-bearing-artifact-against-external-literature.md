---
description: "Use when explicitly asked whether external literature duplicates or subsumes a claim-bearing KB artifact, or should change its keep, rewrite, thin, merge, retire, or cohort status"
type: kb/types/instruction.md
---

# Assess a claim-bearing artifact against external literature

Decide the artifact's smallest faithful disposition from direct source evidence without mistaking topical similarity, model recall, or backlink count for a verdict.

Use this procedure only for an explicit retrospective literature-disposition question. Ordinary writing, a named-source grounding check, and a general request to improve an artifact do not trigger it. This procedure does not certify novelty: a bounded search that finds no source means only that no candidate was found within the recorded boundary.

Run the procedure inside `cp-skill-write-multistage`. Use that workflow's workshop for the records below and its reconstruction, audit, source-dependency guard, promotion, and validation stages for any live edit.

## Steps

1. **Fix the assessment boundary.** Record the target, the alleged externally established subject, the intended consumer, and a finite source-candidacy boundary. Prefer a user-supplied corpus or source. Otherwise record the exact queries, venues, dates, or result limit used to look for the strongest plausible host. Ask the user only when materially different reasonable boundaries could change the requested disposition.

2. **Inventory the live claims before selecting sources.** Divide the target into claim regions at the finest grain at which a consumer could rely on one commitment without importing another. Include the title claim, load-bearing premises, mechanisms, scope boundaries, and operational consequences. For each alleged literature overlap, first decide whether the target actually makes that claim. If it does not, record `cohort removal` and do not edit the artifact merely to fit the assessment premise.

   Use bilateral isolation only when the user explicitly requests an independence control, a prior comparison is challenged because one side may have shaped the representation of the other, or the task is a prospective evaluation of the comparison method. When it applies, add `target-claim-inventory.md`, `source-reconstruction.md`, and `isolated-comparison.md` to the multistage workshop checklist. Launch a fresh target worker now to write `target-claim-inventory.md` from the target and its contracts without seeing the source, source reconstruction, or prior comparison. Do not make bilateral isolation the default from the existing single bounded case; it changed verdicts but did not isolate which procedural difference caused the change.

3. **Nominate sources against exact claims.** For each in-scope claim region, record the proposition a source would need to establish, contradict, or bound. A user-named source, model recall, search result, citation graph, or topical resemblance may nominate a reading assignment; none supplies verdict evidence. Admit a source to the assessment only when a direct tracked `kb/sources/*.ingest.md` identifies it. If no ingest exists, report the exact source or URL for a separate `cp-skill-ingest` run. Do not change the target from a snippet, paraphrase, or remembered source.

4. **Ground each admitted source use.** Read the ingest's complete `## Quotes` section and judge only what those retained extracts establish. If they are insufficient, invoke `cp-skill-ground` with `Target: <ingest path>` and `Claim needed: <source-side proposition>`, then follow its result. Use a pinned snapshot only when that skill returns `snapshot required`. Record the source-established unit and its limits separately from any Commonplace transfer, synthesis, application, counterexample, or boundary.

   When bilateral isolation applies, launch a separate fresh source worker after grounding. Have it write `source-reconstruction.md` from the admitted source evidence and source-side question without seeing target prose, the target inventory, or a prior comparison. Then launch a third worker with only the two frozen outputs, the intended consumer, and the assessment question. Have it write `isolated-comparison.md`, testing both charitable over-attribution and false narrowing. It marks missing information instead of opening either live input. Use that comparison as the source-versus-target input to the remaining steps.

5. **Build a claim-region disposition table.** Give every live claim region one row with:

   - the incumbent claim and scope;
   - the direct source evidence and exactly what it licenses;
   - the target-local remainder, if any;
   - the intended consumer's warranted inference or action;
   - the strongest existing local artifact that could carry the remainder;
   - the smallest faithful replacement path; and
   - the provisional disposition.

   Keep source-established and target-local units separate. Evidence for one claim, conjunction, or scope does not spread across the document.

6. **Try to eliminate the incumbent.** Construct the strongest replacement from the admitted source plus existing local artifacts. A replacement is faithful only when it gives the intended consumer the same warranted inference or operation over the same scope. Keep a local remainder only when it changes that use and cannot be recovered from the replacement path. A verbal difference, domain renaming, ungrounded transfer, or subject narrowed until the predicate is true does not earn a separate artifact.

7. **Inspect inbound uses semantically.** Find tracked inbound links with one backlinks query. Classify each as `imports affected claim`, `imports another claim`, or `incidental`. Use the first class to test whether the proposed replacement preserves real imports. Use total link count only to estimate rewiring work; it neither warrants the incumbent nor measures the inherited claim's blast radius. No inbound links do not by themselves justify retirement.

8. **Choose the outcome from the rows, without an outcome prior.** Use these meanings:

   - `cohort removal` — the target does not make the claim that admitted it to the assessment; leave the artifact unchanged and correct the cohort record;
   - `keep` — an independent contribution survives the replacement test and the incumbent already states and supports it accurately;
   - `rewrite` — an independent contribution survives, but its wording, scope, attribution, evidence, or separation from source-established material must change;
   - `thin` — source-restating regions can be removed while a smaller independent, citable contribution remains;
   - `merge` — an existing local artifact can carry the surviving contribution with a cheaper faithful path;
   - `retire` — direct sources and existing local artifacts replace every warranted use, leaving no independent contribution.

   A mixed target may receive different region-level outcomes, but the final artifact action must preserve one coherent contribution or type-appropriate purpose. For a merge that changes another artifact, use the multistage workflow's user-decision gate. For retirement, read and follow [Retire an artifact](./retire-artifact.md), including its approval stop after the inbound inventory. Keep relocations pure when an outcome changes only the artifact's address.

9. **Execute and verify.** Record the final disposition, evidence paths, search boundary, unresolved coverage, and inbound classifications in the workshop. Use the remaining multistage steps for an authorized rewrite, thin, or merge. Validate every changed artifact. A keep or cohort removal produces no target edit. After a changed artifact validates, suggest `cp-skill-connect` for broader graph discovery. Never report the result as proof that no prior art exists outside the recorded boundary.

## Verify

- Every admitted source was selected against an exact live claim and assessed from tracked direct evidence.
- Every claim region has a source-established unit, a local remainder, a smallest faithful replacement, and a disposition.
- The replacement test could have produced a non-keep outcome; verbal distinctness did not decide it.
- Inbound links were classified by imported claim before they affected impact or rewiring decisions.
- Candidate-generation evidence never decided overlap, novelty, or disposition.
- The result states its search boundary and does not certify global novelty.

---

Relevant Notes:

- [Candidacy evidence licenses escalation to assessment, not acceptance](../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) — rests-on: source suggestions may route reading but cannot decide disposition
- [Theory warrant should be tracked at the finest granularity evidence licenses](../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — rests-on: source support and local remainder are assessed at claim-region grain
- [A borrowed pattern transfers only as far as source and target share a mechanism](../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) — rests-on: a target-local transfer survives only over an identified shared mechanism
- [Narrowing bought to survive review is paid for in content](../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: the adversarial replacement test rejects empty remainders made defensible by narrowing
