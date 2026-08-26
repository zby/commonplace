# Fifth episode: the pass works as critique and fails as repair

**Note:** `kb/notes/naur-equates-machine-execution-with-formulated-criteria.md` (born as `irreducibility-to-rules-bounds-text-alone-not-text-plus-interpreter.md`; two relocations since).
**Passes:** `20260826T115728Z-a18058` on v0, `20260826T140020Z-7c9e` on v3. Both `keep (reframe)`.
**Evidence:** all six versions, both packets, and the critique/friction/premise reports are retained in [`fifth-episode-record/`](./fifth-episode-record/README.md). This file is the analysis; that directory is the record.
**Operator's reading at the time:** "I can see how the full improvement pass works as the critique — but it does not yet work at fixing it."

## The shape

Two cycles in one day, each with the same three moves:

1. An author writes a claim that overreaches its warrant in a specific way.
2. The pass finds the overreach — correctly, with counterexamples that hold.
3. The pass repairs by retreating to the nearest claim no gate can touch, records the contribution as *preserved* or *strengthened*, and the operator has to re-derive the intended claim from the objections.

| | Cycle 1 | Cycle 2 |
|---|---|---|
| Overreach | v0 generalized to all "irreducibility" arguments and asserted Naur's human premise was *assumed*, reading five retained quotes | v3 said a trained interpreter "falls outside Naur's partition" — but an LLM is formal symbol manipulation on a computer, which is Naur's machine pole |
| Critique that held | premise GLOBAL defeat (halting-decider counterexample); `grounding-alignment` FAIL (source-wide claim from a quote subset) | premise LOCAL defeat (an induced decision tree is learned yet an explicit rule set); friction UNSUPPORTED on the learning-implies-outside-rules joint; unsourced 1985 motive; "only personal advice repaired" not in the extracts |
| Repair the pass chose | *Naur's retained passages do not establish a human-only theory bearer* — true, and a claim about what the KB had retained | *Naur's rule-inexpressibility argument does not by itself bind program theory to humans* — true, and a bare logical point with a three-level taxonomy whose third level the closing gates found unused |
| Closing self-assessment | contribution *preserved* | contribution *strengthened* |
| What actually fixed it | operator: "argue about the full article"; full snapshot read; four grounding runs → the bridge is a premise (machine execution = formulated criteria) | operator: "at the time, execution by machine meant formal interpretation"; the bridge was *accurate for its day*, and trained recognizers *separated* execution from formulated criteria rather than falling outside anything |

Both repairs are of the kind the [cohort result](./genre-drift-cohort-result.md) found in 15 of 16 title changes: survival bought with a negation and a condition ("do not establish", "does not by itself") while the claim's kind is kept. Neither is analytic — the [narrowing note](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md)'s refuter test passes for both — so the existing guards did not fire, and should not have. The failure is elsewhere.

## Why the repair side fails

The pass's repair operations are all subtractive. Reading step 7 against what happened:

- **Motivation is not an input.** The warranted contribution must be derived "only from the artifact, repository and collection contracts, retained reports, explicit user direction, and retained intent supplied for this pass", and retained intent counts only when a block identifies its source, subject, scope, and role. Nothing supplies such a block, so the brief is reconstructed from the incumbent text — the text whose claim the gates just defeated. A reframe then measures itself against a brief built from the defeated text, and the closing cycle measures the final text against the *reframed* update. There is no reference point outside the pass, which is how *strengthened* got recorded for a claim the operator rejected on sight.
- **Evidence cannot be extended.** `grounding-alignment` judges against the ingest's retained quotes as fixed evidence; `cp-skill-ground` sits outside the pass. When a note's claim exceeds its grounding, the in-pass options are to cut the claim or bound it by the grounding. In cycle 1 the essay sat in `kb/sources/.snapshots/` the whole time; the pass's repair was to write "retained passages" into the title.
- **The reconciliation rule prefers subtraction.** Compression's bias wins ties; critique's additions are kept only when they make the claim defensible against the strongest attack; and "defensible" is measured by the gates. The repair that made v5 better than v0 — find the premise the objections were pointing at, state it, and ground it — adds a claim, and no rule in step 7 licenses adding one.

Put together: the pass can say *what is wrong* with a claim and cannot say *what the claim was for*. The second is what repair needs.

## The Naur reading of the episode

The note under repair is about Naur, and the episode is a Naur case. His compiler successors, group B, had the full program text, annotated sources, extensive design discussion, and personal advice, and still proposed changes the original authors saw instantly as patches — behaviourally adequate, "framed entirely" outside the design's theory. The pass is group B. It has the note's text, every report, the collection contracts, and the gates, and its repairs are patches: they satisfy the checks and are not framed within the note's theory, because the theory — what the note is for, which premise its argument turns on — was never in the artifacts it was given. Group A caught the patches on review; here the operator did. Naur's conclusion was that transfer needs contact with the theory-holder. The two operator interventions that fixed the note were exactly that: one sentence each, supplying the theory the repair needed.

That reading also says what the pass is good at. Critique does not require the theory: a counterexample to a universal, a source-wide claim without source-wide grounding, a learned system misplaced outside the machine pole — these are all visible from the text and the gates, and the pass found every one. The asymmetry is Naur's: verifying that a change breaks a structure is possible from the artifacts; making a change that extends the structure is not.

## Candidate consequences

None adopted; each is one witness deep, and this episode is a single note.

1. **Separate the critique from the repair as a disposition.** *Adopted 2026-08-26 as ADR 080: `revise` is a pending hand-back; the pass never changes a claim.* When the defeats hit the argument's bridge rather than its scope — the pass has no vocabulary for this yet — stop after step 7 with a pending disposition (`return-to-author` alongside `delete`/`merge`/`rehome`), handing back the objections and the packet. The pass already stops for dispositions it cannot execute; this would make "cannot repair without the theory" one of them. Cheapest change; matches the operator's assessment directly.
2. **Give the warranted-contribution brief a reference point that survives reframe.** A retained intent record the pass can read — the workshop framing file, a commit body, or a note-side field — so the closing comparison is against what the note was for, not against the reframed update. Step 7's "retained intent" channel exists on paper; nothing feeds it.
3. **Route a `grounding-alignment` FAIL to grounding before reframe** when the source is snapshot-pinned. Changes the "steps 1–7 only write reports" invariant only if a Quotes-section append counts as report-side; it edits the ingest, not the note.
4. **Evidence-scope test.** A repair whose new qualifier names the evidence set ("retained passages", "by itself", "in the sampled runs") rather than a property of the subject is bounding the claim by the KB's retention. Check whether the evidence can be extended before accepting it. Companion to the refuter and citer tests, which this episode passed while still drifting.

## What this adds to the earlier episodes

Episodes one to four are about *how* a defeated claim gets narrowed and which narrowings are honest. This one is about who can do the repair at all. The earlier guards ask whether a repair kept content; they cannot ask whether it kept the point, because the point is not in the inputs. The operator's sentence — critique works, fixing does not — is the same asymmetry Naur drew between reading a program and extending it, and the fix that worked here was Naur's: contact with the theory-holder.
