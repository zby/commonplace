---
description: Experimental run-by-hand report method that decomposes a note's central commitment into the premises it rests on and hunts a counterexample for each, routing failures as local (revise a premise) or global (the commitment fails)
type: kb/types/instruction.md
---

# Decompose a note into premises and counterexample each

Experimental, run by hand. This method tests the **nodes** of a note's argument — the premises its central commitment takes as given — not the edges between them. It assumes every stated inference is valid and asks a different question: is each premise the commitment rests on *itself* true, or does a concrete counterexample defeat it? This is the "explanation as a falsification surface" move — a commitment is only as strong as the weakest premise it silently assumes. It is **not a review-system gate or snapshot-anchored assay**: it writes no evidence or freshness-baseline state and is not wired into the review system. Write the report; do not touch the note.

Unlike [reconstruct a note's composition friction](./composition-friction-gate.md), which tests whether each *inference* holds (the edges), this tests whether each *premise* holds (the nodes). The two are complementary: an argument can have valid inferences resting on a false premise, which the friction check passes and this check catches. Run both when a commitment must be load-bearing.

Run it in a **fresh sub-agent**, a different runner than wrote the note, so the checker has no sympathy for the note's framing. Separation is what gives the check teeth: the runner that assumed a premise while writing will assume it again while reading.

The caller owns reviewer lifecycle. After the report has been written and verified, close, terminate, or release the checker with the harness lifecycle operation. The checker is a single-use context and must not receive follow-up work.

## The hard rule

Do **not** emit an overall "sound / unsound" or pass/fail verdict, and do not accept the note. The product is **routed attention**: the premises that a counterexample defeats or dents, and — for each — whether its failure is local or global. **Default to `DOUBTFUL` when uncertain.** A premise earns `HOLDS` only when an active counterexample hunt fails; do not extend it the benefit of the doubt the way fluent reading does.

## Step 1 — State the central commitment

State the note's central commitment in **one sentence**. Match its artifact kind:

- **claim** — the proposition the note asserts is true;
- **definition** — the boundary it draws and asserts is the right cut;
- **procedure** — the outcome it asserts following the steps produces.

## Step 2 — Decompose into load-bearing premises

Enumerate the premises the commitment **rests on and takes as given** — including background premises the note treats as obvious and never argues for. What counts as a premise follows the artifact kind:

- **claim** — a proposition that must be true for the claim to hold;
- **definition** — a commitment that makes this the correct boundary (that the distinguished cases differ in the way named, that the distinction is not idle, that nothing important is mis-sorted);
- **procedure** — an assumption under which the steps produce the intended outcome (about inputs, the executor, the environment, or the world).

List the premises the *argument consumes*, not every true sentence in the note. A premise the note never states but the commitment cannot survive without is the most valuable to surface.

## Step 3 — Counterexample each premise

For each premise, actively hunt a concrete **counterexample** or a specific reason it could be false — a case, input, or situation in which the premise does not hold. Record per premise:

- `HOLDS` — an active hunt found no defeater;
- `DOUBTFUL` — a plausible reason or edge case dents it (state it);
- `DEFEATED` — a concrete counterexample makes it false (state it).

Counterexample by artifact kind: for a claim, a case where the premise is false; for a definition, a case the boundary mis-sorts (over- or under-includes) or a distinction that changes nothing; for a procedure, a situation where the assumption fails and the steps misfire.

**Read each premise at its stated modality** (`kb/notes/COLLECTION.md`, "Claim modality"). A premise stated as a tendency ("usually", "most", "under conditions C") is dented or defeated only by prevalence-shaped evidence — the exceptions being common or the ordinary case going the other way — never by one instance it already concedes. A premise stated as a first-order model with adequacy commitments is attacked through those commitments — an exception its domain treats as ordinary unmarked practice, or the model losing dominance — not by conceded, accounted-for exceptions. A premise with no stated mode reads as universal, and one genuine counterexample defeats it. The modes differ in the inference form of the refuter: deductive for universal (one instance, modus tollens), inductive for statistical (a sample-based prevalence result), comparative for ideal-type (loss of dominance to the corrections or a rival, or an exception ordinary in its own domain) — hunt each premise's defeater in its mode's form.

For every non-`HOLDS` premise, also record the **counterexample shape**: `instance` (one concrete case), `prevalence` (evidence the exception is common or ordinary), or `priced-exception` (the case is marked, fenced, or charged for in its own domain). The shape is routing information for whoever repairs the note — a prevalence-shaped defeat of a universal premise points at a statistical reframe, and a priced-exception defeat points at an ideal-type candidate — not a verdict, and not this method's call to make.

## Step 4 — Route each failure local or global

For every `DOUBTFUL` or `DEFEATED` premise, classify the scope of its failure:

- **LOCAL** — the failure defeats only this premise; the central commitment can still stand on the remaining premises or be rescued by a qualification (narrow the scope, add a condition). The revision changes a premise and keeps the commitment; the qualification belongs in the note's `## Scope` (or `## Caveats`) section, where a later edit can narrow it further without touching the claim.
- **GLOBAL** — the failure propagates to the central commitment, so the commitment itself fails as stated. The revision must weaken, rescope, or retire the commitment, not just patch a premise.

A `GLOBAL` failure on a load-bearing premise is the strongest signal this method produces; surface it first.

## Output

Write to `kb/reports/cache/premise-decomposition/<note-name>.premises.md`. Mutate nothing else.

```markdown
# Premise decomposition: <note title>

**Note:** <path>
**Register:** claim | definition | procedure
**Central commitment (one sentence):** <...>

## Premises and counterexamples
1. **<premise, stated as a proposition, at its stated modality>** — <HOLDS | DOUBTFUL | DEFEATED> — <the counterexample or reason> — <LOCAL | GLOBAL if not HOLDS> — <instance | prevalence | priced-exception if not HOLDS>
2. ...

## For the human
<one line: the premise to look at first — the global defeater if any, else the load-bearing doubtful premise most worth the author's attention>
```
