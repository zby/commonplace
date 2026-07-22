# Literature-offload analysis — what the five new ingests let us delegate

The five sources named in [external-delegation-assessment](./external-delegation-assessment.md) §5 are now snapshotted and ingested: [Bainbridge 1983](../../sources/ironies-of-automation.ingest.md), [Kephart & Chess 2003](../../sources/the-vision-of-autonomic-computing.ingest.md), and the three Moen/Norman PDSA papers ([Evolution of the PDCA Cycle](../../sources/evolution-of-the-pdca-cycle.ingest.md), [Foundation and History of the PDSA Cycle](../../sources/foundation-and-history-of-the-pdsa-cycle.ingest.md), [Circling Back](../../sources/circling-back-clearing-up-myths-about-the-deming-cycle.ingest.md)). This document answers the follow-up question: with these in hand, how much of the cluster's local analysis can be offloaded to the literature, and how much local text can actually be cut?

**Verdict up front: almost none of the existing text, and that is a finding, not a failure.** All five ingests independently reached the same conclusion about their source's role — "casebook notes already exist; this source's role is corroborating evidence / origin citation," in each report's own words. The cluster's notes contain very little rederived established theory to shed, because they were written under the conservative-extension stance ([external-theory evaluation](./external-theory-evaluation.md) §0) that keeps inherited content cited rather than restated. The real offload is **prospective**: the digest phase can now delegate change-process procedure to PDSA and runtime-loop engineering to MAPE-K by citation, because the citable snapshots finally exist. What the ingests buy the existing notes is robustness (origin citations, second-tradition corroboration), which is worth a handful of added lines, not subtracted ones.

## 1. Note-by-note disposition

### 1.1 [Increasing computational autonomy relocates human effort](../../notes/increasing-computational-autonomy-relocates-human-effort.md) — repoint, do not cut

The one place the cluster cited an external theory without the adapter discipline (delegation assessment, cleanup item 5) is now fixed at the source side: Bainbridge is snapshotted and ingested. The remaining edit is mechanical — repoint the bare DOI link to the local snapshot.

No text reduction beyond that. The note's Bainbridge content is already a single sentence ("automation transforms rather than removes the operator's role, leaving the residue that could not be automated"); the local kernel — the elastic-backlog mechanism, the constant-hours observation, the measure-per-human-judgment program — is not in Bainbridge and cannot be delegated to him. The note is already the "short hypothesis grounded in Bainbridge" the delegation proposal asked for.

### 1.2 [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — add one source; the real reduction candidate is different

Bainbridge's monitoring irony ("the human monitor has been given an impossible task" — checking in real time a system installed because it outperforms the human) is historically prior, independent support for the note's convergence claim. Worth roughly two added lines as a fifth source.

This note is, however, the cluster's one genuine *structural* reduction candidate — just not via these five sources. Its bulk is in-body exposition of external sources (Tam, Amodei, Rabanser, MAKER, in-toto) that are cited by external URL rather than held as snapshot+ingest pairs. Applying the same discipline there — snapshot, ingest, compress each in-note exposition to claim-plus-citation — would shed a substantial fraction of the note's length and is the pattern this offload exercise validates. Flagged as a candidate follow-up, out of scope for this pass.

### 1.3 [A proposal-selection loop requires search, evaluation, and operative retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — origin citation only

The delegation assessment's fact-check ("little to trim; the note contains no engineering decomposition to delegate") is confirmed by the Kephart & Chess ingest: the paper supplies no membership test, argues by analogy, and is valuable precisely as the *origin* of the reference-model tradition the note already cites through Weyns and Petrovska. The edit is one added line — cite the origin beside the derivatives in the "What the decomposition claims" section. The boundary-case analysis (Homeostat, Zinkevich, Gödel machine) is the distinctive kernel and stays.

Optional, cheap: the PDCA "act = standardize if satisfactory, back to plan if unsatisfactory" fork is a fourth independent tradition converging on the reject-capable-evaluation requirement. If added at all, it should be one clause with a citation, not a paragraph — the convergence detail lives in the ingest reports.

### 1.4 [Discovery lifecycle](../../notes/definitions/discovery-lifecycle.md) — evidence links; the definition stays stipulative

All three PDSA ingests converge on the same recommendation: the definition's conjecture–consequence–test core currently rests on the Peirce SEP entry alone, and the Deming lineage is a second, applied, non-philosophical tradition landing on the same loop (Shewhart's own specification–production–inspection ↔ hypothesis–experiment–test mapping; the 1991 Moen/Nolan/Provost prediction-in-Plan, observation-vs-prediction-in-Study revision). Add one evidence link — [Foundation and History](../../sources/foundation-and-history-of-the-pdsa-cycle.md) is the strongest single anchor — and cite the siblings from there rather than adding three links.

No reduction: the definition is stipulative and already minimal. The gain is that its core is now corroborated by independent convergence rather than one source, which is exactly what conservative extension predicts corroboration should look like.

### 1.5 [An accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) and [first-principles reasoning selects for explanatory reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — optional one-line corroborations

Moen/Nolan/Provost's "not enough to determine that a change resulted in improvement during a particular test... predict whether a change will result in improvement under the different conditions you will face in the future" is near-verbatim, decades-old, unrelated-field corroboration of both notes' central claims. Each is a one-line evidence addition, best made when the notes are next revised for other reasons. Neither note has text to cut — both are already tight.

### 1.6 Review-system vocabulary (gate vs. critique) — no action

The Check→Study renaming (Deming: "check" as pass/fail compliance vs. "study" as compare-observation-to-prediction learning) maps cleanly onto the review system's verdict/report result kinds. That is a pleasing historical echo, not an offload: the reference docs describe the shipped system and delegate nothing by gaining the citation. Available as framing if the concepts section is ever revised.

## 2. The prospective offload — where the reduction actually lands

The texts that shrink are the ones **not yet written**. The delegation assessment's negative commitment (§3b step 1: audit dispositions and the digest must not create local guidance duplicating what PDSA/MAPE-K supply) was adopted with a gap — nothing citable to point at. That gap is now closed:

- **Change-testing procedure → PDSA.** When a phase-1 audit disposition or the future digest wants trial/observation/adoption procedure, it cites the snapshots: the three improvement questions ("What are we trying to accomplish? How will we know a change is an improvement? What changes can we make?") and prediction-before-test are established, citable, and need no local restatement. Local text states only the Commonplace delta: the operativity test, the reflective/addressability profile, the warrant boundary.
- **Staged autonomy granting → Kephart & Chess.** Their adoption ladder (collect → advise → act on low-level decisions → act on higher-level ones) is citable framing for any future guidance about how much autonomy to grant an agent loop, instead of deriving a local ladder. Their goal-specification warning (autonomy magnifies goal-error consequences) is likewise available to the warranted-autonomy guidance surface.
- **Host binding stays worked-case-first.** Nothing here changes §3b step 3: no PDSA adapter until one real repository change runs through a PDSA overlay; no MAPE-K binding while no computational runtime pathway exists.

## 3. Temptations dispositioned — recommendations that would grow text

Three ingest recommendations cut against the reduction direction. Under the maintainer's direction and the quality bar, dispositions:

1. **Bainbridge C/D/E note** (skill atrophy from disuse, vigilance limits, the training-investment paradox — genuinely uncovered by any note, per the ingest's search). *Park as a recorded gap.* The transfer to agent-operated KBs (humans who only review automated output lose the skill the review depends on) is real and would change oversight-allocation decisions, so it clears the quality bar — but it is new analysis, not offload, and nothing in the current workshop consumes it. Write it if and when phase-1 audit dispositions need the claim; the ingest's Extractable Value section preserves the material until then.
2. **PDSA-convergence synthesis note** (two ingests recommend a note stating that Peircean philosophy and Deming-lineage quality improvement independently converge on the predict-then-test loop). *Do not write.* The convergence is fully recorded across the three ingest reports and becomes citable through the discovery-lifecycle evidence link (§1.4); a standalone synthesis note would restate what the sources now carry — the exact pattern this exercise exists to stop.
3. **Reverse-edge sweeps** (each ingest lists two or three candidate reverse edges). *Take only the strongest per source*, per each ingest's own recommendation; the rest wait for the next natural revision of the target notes.

## 4. Summary of concrete edits recommended

Small, mechanical, all confirmed against current note text:

| Edit | Target | Direction |
|---|---|---|
| Repoint Bainbridge DOI → local snapshot | autonomy-relocation note | hygiene, ±0 lines |
| Add Bainbridge as fifth convergent source | verification-boundary note | +2 lines |
| Add Kephart & Chess origin citation beside Weyns/Petrovska | proposal-selection loop note | +1 line |
| Add evidence link to PDSA history snapshot | discovery-lifecycle definition | +1 line |
| Optional one-line corroborations | accepted-edit note; first-principles note | +1 line each, deferred |

Net effect on existing library text: a few lines added, none removed. The reduction the maintainer's direction buys is concentrated in text not yet written (§2) plus one structural follow-up outside these five sources (§1.2). The five ingests' unanimous "corroboration, not replacement" reading is itself the strongest evidence yet that the cluster's conservative-extension discipline is working as designed.

---

Links:

- [External-delegation assessment](./external-delegation-assessment.md) — extends: executes and closes that document's §5 snapshot+ingest work items and answers its follow-up question
- [External-theory evaluation](./external-theory-evaluation.md) — depends-on: the conservative-extension criterion this analysis applies
- [Workshop README](./README.md) — depends-on: the sequencing this analysis feeds (audit dispositions may now cite the ingested hosts)
