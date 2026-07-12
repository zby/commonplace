# Plan: rebuild the three cases from scratch, as the test of the main submission line

The submission claims that **bespoke structure is invisible from the inside**, and that Commonplace supplies a discipline making the forced/chosen boundary legible plus a rig that tests it. The three existing casebooks are the evidence. They are also a mess — built while the contract was still being invented, across a framework upgrade, with nearest-fit source types, stale lifecycle fields, and migration churn.

So the rebuild is not housekeeping. **The rebuild is the experiment**, and it is the only version of the experiment that can actually test the claim.

Written before the run and meant to be fixed before any data is seen. Protocol conventions inherited from the sibling repo's `silently-averaged-experiment`: preregistered outcome classes, blinded judging, caveats declared up front, and this document kept out of builder context until unblinding.

## Why the first build cannot test the thesis, and a rebuild can

Be honest about this in the submission, because a judge will notice it before we do.

- **The contract was co-developed with case 1.** "The contract transferred to a second and third case without amendment" sounds like a transfer result. It is not: the LHC case *shaped* the contract, so cases 2 and 3 ran against a contract already fitted to casework of that kind. The result is consistent with the thesis and equally consistent with its negation.
- **One operator, sequential builds, full memory.** Nothing rules out the transfer having been carried in the operator's head rather than in the artifact — which is exactly the failure the thesis says is invisible from the inside. We are inside.
- **The mess is confounded with the method.** Source-type gaps, the `status:` migration, the upgrade churn — a reader cannot tell which defects came from the method and which from the method being *built while in use*.

A rebuild fixes all three at once, because it inverts the crucial condition: **the contract is now fixed in advance.** It is shipped, it is the dialectical/evidential profile, and it was written before any of the three rebuild cases is touched. Every amendment the rebuild turns out to need is therefore a *finding* rather than a fitting — and every structure that survives with no amendment is a genuine transfer result rather than a restatement of how the contract was made.

## The instrument: convergence between independent builders

The thesis says you cannot tell forced structure from chosen structure from inside one project. The corresponding test is the one we have never run: **build the same case more than once, independently, and see what converges.**

- Structure that **converges** across builders who never saw each other's work is forced — by the material or by the contract.
- Structure that **diverges** was chosen, whatever its author believed while writing it.

That yields a per-structure verdict rather than a global impression. And the discipline's real job — the thing actually under test — is to have **predicted the split in advance**. A method that produces a casebook is unremarkable. A method that tells you *which parts of its output are load-bearing on the world and which are its own taste*, and is then right, is the submission.

The messy first build is a genuine second sample here, not waste. It was produced by a different process (contract-in-flight) with different knowledge, so old-vs-new agreement is informative — while being weaker than a true independent arm, since the operator lineage is shared. Treat it as a **secondary comparison**, never as the primary one.

## What is under test, stated so it can fail

Registered before the run. H3 is the submission line; H1 and H2 are the preconditions that make H3 meaningful.

- **H1 (transfer).** A fresh builder given the shipped framework, the fixed contract, and a case's sources produces a conforming casebook **without amending the contract**. Now a real test, because the contract can no longer move to meet the case.
  *Fails if:* the contract needs amendment, or the output does not conform.
- **H2 (visible invention).** Where a builder must invent structure the contract does not supply, the invention lands as a **visible local artifact** — a collection-local type, a contract addendum, a logged gap — not as silent bespoke structure smuggled into prose.
  *Fails if:* the diff between builders contains structure neither builder flagged as a choice.
- **H3 (discrimination — the submission line).** Our **sealed prediction** of which structures are forced and which are chosen matches the convergence/divergence actually observed, better than chance.
  *Fails if:* things we called forced diverge, or things we called chosen converge. Both directions are real results and both get reported.

H3 is the one that can embarrass us. That is why it is the one worth running.

## Clean-room conditions

Our own [context contamination note](../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) forbids the cheap version of this. We may **not** instruct a builder "do not copy the existing casebooks' structure" — the finding is precisely that an agent which detects a contaminant and refuses it still leaks its lean. **Exclusion, not instruction.** Concretely:

- Each builder runs in a workspace holding **the framework, the contract, and that case's sources — and nothing else**. The old casebooks are absent from the filesystem, not present-and-forbidden. This is the single most important condition in the plan and the easiest to get lazily wrong.
- Builders do not see this document, each other's output, or each other's existence. Any cover story needed to explain the workspace layout is given, as in the prior experiment.
- **Vary the model family across arms.** Same-family builders may converge because they share priors rather than because the material forces it; single-family convergence is uninterpretable (the decorrelated-checks requirement from [error correction works above chance oracles with decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md)).
- **Reuse the captured sources; rebuild everything downstream.** Re-capture is wasted spend and adds a variable we do not want. The snapshots are inputs; the ingests, notes, and structure are the output under test. *(Exception: any snapshot whose fidelity is itself in question gets re-captured — see the quote-verifier coupling below.)*
- **Log every operator intervention.** The brief asks whether the method "gracefully scales to mostly-or-entirely hands-free"; a run that needed steering must say where.

## The confound that would flatter us

Convergence between builders could come from the **contract dictating the structure** rather than the material forcing it. That is a real finding — the contract is doing work — but it is *not* the thesis, and it is easy to mistake for it.

So one case gets an extra arm with a **minimal contract**: sources plus a bare instruction to map the dispute, no dialectical/evidential profile. If minimal-contract builders converge on the same joints, the structure is material-forced. If they scatter, the convergence in the main arms is contract-induced. Only one of those is the story we currently plan to tell, and we should find out which before a judge does.

## Preregistered predictions

Sealed now, so they cannot be revised into correctness later.

1. **Converges (forced by the material):** the root position-map note; the identification of the central contested joint(s); the gap register; attribution of positions to named parties; zero bare file-level links surviving contact with writing.
2. **Diverges (chosen):** note granularity and file boundaries; section ordering; which link labels get used; whether the institutional/meta layer earns its own note; title phrasing.
3. **Contract amendments needed: zero** for the three-part citation convention. This is the sharpest H1 prediction and the one most likely to be wrong.
4. **The known-messy spots do not recur:** with `genre` now one open field (ADR 045) and the global `status:` field gone (ADR 044), the nearest-fit source-typing and lifecycle churn that fouled the first build should simply not happen. If they recur, the framework fixes did not fix them.
5. **Quote-verifier mismatch rate on fresh prose lands near the 24/88 baseline** — naive `verbatim` marking fails at a *stable, author-independent* rate, not because one author was sloppy.
6. **Case-shape prediction:** the LHC rebuild converges hardest (one dependency chain), eggs next, **COVID diverges most** (two parallel evidential structures plus a split institutional layer admit more than one defensible carve-up). If COVID converges as tightly as LHC, our "differently-shaped on purpose" framing is weaker than we think.

Prediction 1 versus 2 **is** H3. Scoring them is the experiment.

## Measurement, decided in advance

- **Contract amendments required** — counted, each classified forced vs chosen *before* reconciliation against the sealed list.
- **Structural convergence** — a blind judge, given the independent casebooks under neutral names, knowing neither the hypothesis nor that conditions exist, lists structures common to all and structures unique to each. H3 then scores by mechanical comparison against the sealed list.
- **Quote-verifier run** on every output — deterministic, no judgment, comparable to the 24/88 baseline. This couples the two workshop builds: ship the verifier before the rebuild lands so the rebuild is checked, not hand-trusted.
- **Steering log** — every operator intervention.
- **Old-vs-new delta** — what the clean build drops, keeps, or adds relative to the messy one. Secondary, and reported as such.

## Scope, against six days

This is now the workshop's most expensive item and its most important. Tiered so it can be cut without becoming worthless:

- **Minimum viable (do this or nothing): one case, two independent builders, different model families, fixed contract.** Scores H1, H2, H3. Use **COVID** — prediction 6 says it is where divergence should be largest, so it is the case with the most power to falsify, and it is the case the first build left thinnest.
- **+2 cases** (LHC, eggs) if budget allows, giving the cross-case transfer claim its evidence and testing prediction 6.
- **+1 minimal-contract arm** to separate material-forced from contract-induced convergence. If cut, say so plainly in the submission rather than letting the ambiguity ride.
- **Cut first:** additional builders per arm. n=2 is thin and we will say so, exactly as the drift experiment did.

If the schedule forces a choice between running this and polishing the write-up, **run this**.

## What we report either way

- **Convergence matches prediction** → the discipline discriminates forced from chosen, with the contract fixed in advance and builders blind to each other. That is the submission, with evidence.
- **Convergence does not match prediction** → we falsified our own headline claim, on our own rig, and say so. The brief names "a critique with counterexamples of an otherwise promising approach" as an entry shape in its own right, and an entrant who reports this is more credible than one who never looked.

The failure mode to guard against is neither. It is **running the experiment and then narrating around the result** — precisely the drift our own contamination finding says we would be blind to. Hence the sealed predictions, the blind judge, and this document staying out of builder context.

## What closes it

Predictions sealed, contract frozen, builders run clean-room, judge unblinded, H1–H3 scored against the sealed list, result written into the submission whichever way it fell. Then the durable finding promotes to `kb/notes/` and this file dies with the workshop.
