# Judge-facing casebook tour — curated pointers to the effective regions

The brief asks entrants to include *"curated pointers to particularly effective regions of worked examples."* This is that document: a short guided path through the three demonstration casebooks, aimed at a judge on a clock who will spend minutes, not hours. It answers, per case: **where to look, what to look at, and what that region demonstrates about the protocol.**

Read it top to bottom in about ten minutes, or jump to the case you want to stress-test.

> **Authoring note — paths to fill.** The casebooks live in the sibling `epistack-casebooks` repo, not in this framework repo. The concrete file paths below are marked `‹path›` and must be filled in against that repo before submission. The *structure, framing, and claims* of the tour are complete; only the links are placeholders. Fill each `‹path›` with the real artifact, and each `‹N›` with the real count from a clean `commonplace-validate` / `commonplace-verify-quotes` run.

---

## How to read a casebook in five minutes

Before the cases, the orientation that makes any of them navigable:

1. **Start at the case root** (`‹kb/covid/notes/README.md›`, etc.). It holds the question, scope, the sub-questions, and pointers into the map. It does **not** hold a verdict — by design (see the assessment-layer document). If you want "the answer," the casebook is telling you honestly that the answer is a downstream judgment, not a stored field.
2. **Follow the labelled links.** Every link says *why* to follow it: `grounds` (check the basis), `contradicts` (a disagreement to resolve), `contrasts` (similar-but-not-identical), `correlated-with` (evidence that isn't independent). The labels are the navigation.
3. **Trust the quotations.** Every `verbatim` quote passed `commonplace-verify-quotes` against its retained snapshot. You can re-run the checker to confirm (see `demo.md`).
4. **Check what's stale.** `commonplace-review-target-selector` will tell you which judgments are fresh and which the sources have moved out from under. Nothing here claims to be settled just because it was written.

The three cases were chosen by the competition for *different challenge profiles*, and the tour is organized to show the one protocol meeting three different shapes of difficulty.

---

## Case 1 — COVID origins: parallel evidence that must not collapse

**The difficulty:** two smart people reached opposite conclusions over 15 hours; two judges ruled decisively for zoonosis; six Bayesian analyses of *the same evidence* spanned 23 orders of magnitude. The hard part is not finding evidence — it is keeping two parallel evidential structures, a contradicting institutional layer, and heavily reused underlying data from silently blending into one mush.

### Region 1A — The two parallel evidential lines *(the structure win)*
- **Look at:** `‹kb/covid/notes/zoonosis-map.md›` and `‹kb/covid/notes/lab-leak-map.md›`, and the root that links both.
- **What it demonstrates:** the two cases are held as *distinct sub-question maps*, not merged into a single pro/con list. Each line's claims `grounds`-link to their own evidence. A reader can walk one case to its foundations without the other case's framing leaking in. This is the protocol's non-flattening rule at case scale.

### Region 1B — The split institutional layer *(local extension without universalizing)*
- **Look at:** `‹kb/covid/notes/institutional-positions.md›` and COVID's `‹kb/covid/notes/COLLECTION.md›`.
- **What it demonstrates:** COVID needs a *split* institutional layer because three official bodies (e.g. an intelligence assessment, a WHO report, agency statements) contradict one another. That structure is declared in COVID's local `COLLECTION.md` — it is **not** a framework universal. LHC, with one safety review, does not have it. Same protocol, different local contract. Point of comparison: open LHC's contract next to this one and see the divergence.

### Region 1C — The correlated-evidence cluster *(the assessment win)*
- **Look at:** `‹kb/covid/notes/independence-clusters.md›` (or the generated provenance matrix region).
- **What it demonstrates:** the Andersen/Worobey/Pekar author overlap *and* the analyses reusing the same Huanan-market metagenomic dataset are shown as a **computed cluster** over provenance facts — not a prose aside a reader has to notice. This is the direct answer to *"flag correlated evidence being treated as independent,"* and it is why the 23-orders-of-magnitude spread is legible: apparently independent analyses shared inputs and decompositions.

### Region 1D — Quote verification under adversarial density *(the referential win)*
- **Look at:** run `commonplace-verify-quotes ‹kb/covid/›` (‹N› quotations, ‹N› pass).
- **What it demonstrates:** the Wilf–Miller debate is quotation-dense and contested; every `verbatim` claim resolves exactly against its snapshot. Break one and re-run to watch it fail.

### The reader question this case makes easier
*"Which pieces of the zoonosis case are evidentially independent, and which lean on the same dataset or author cluster?"* — answered by Region 1C in one look, where before it required reading six analyses and noticing their shared inputs yourself.

---

## Case 2 — LHC black holes: a settled case whose weakest link stays visible

**The difficulty:** this one is (we hope) closed and uncontested — which makes the challenge *probing the argument for its dependencies and its most speculative points* without the drama of live disagreement to guide you. The risk is a casebook that just says "settled" and hides the joints.

### Region 2A — The single load-bearing dependency chain *(the structure win)*
- **Look at:** `‹kb/lhc/notes/safety-case.md›` and follow the `grounds` chain.
- **What it demonstrates:** the whole safety argument funnels through the **cosmic-ray argument** as one load-bearing dependency. The dependency chain is traversable: you can walk from "the LHC is safe" down to the single argument nearly everything rests on. That funnel *is* the crux, made structural (assessment-layer §3).

### Region 2B — The speculative joints, kept on the map *(the honesty win)*
- **Look at:** `‹kb/lhc/notes/speculative-joints.md›` and the Ord–Hillerbrand–Sandberg critique node `‹kb/lhc/notes/out-of-model-critique.md›`.
- **What it demonstrates:** the most speculative assumptions (Hawking-radiation reliance, exotic stable-remnant scenarios) are linked one hop from the crux, and the standing *out-of-model-error* critique is attached as a `grounds`-level objection **to the very node it threatens** — not buried in a global caveat. This is the calibration-under-out-of-model-error discipline made concrete: the risk lives beside the argument it undercuts.

### The reader question this case makes easier
*"What single assumption, if it failed, would most reopen this closed case?"* — answered by walking the densest `grounds` dependency in Region 2A to the speculative joint in 2B. A "settled" verdict hides this; the casebook keeps it one click away.

---

## Case 3 — Eggs: competing syntheses that are all true, under different scopes

**The difficulty:** mundane, vague, open-ended — and representative of most everyday questions. "Are eggs good?" has *multiple correct answers* depending on population, outcome, and dose. The failure mode is averaging them into a single mush ("eggs are fine in moderation") that answers no one's actual question.

### Region 3A — Stratified competing syntheses *(the non-flattening win)*
- **Look at:** `‹kb/eggs/notes/synthesis-by-population.md›` and the `contrasts`-linked stratum notes.
- **What it demonstrates:** findings are held stratified by population (general vs. diabetic), outcome (CVD vs. all-cause mortality), and exposure (consumption level), linked by `contrasts` — *similar but not identical* claims kept distinct rather than collapsed. "Eggs raise risk" and "eggs are neutral" are **both** shown, each scoped to where it holds. This is the brief's "similar but not identical claims" desideratum, worked.

### Region 3B — The funding-correlation cluster *(the assessment win)*
- **Look at:** `‹kb/eggs/notes/funding-clusters.md›`.
- **What it demonstrates:** industry-funded studies cluster by funder (Barnard-2019-style flags) as a **provenance** fact — computable, attributed, not a rhetorical accusation. Correlated evidence again, in a third different form from COVID's shared-dataset entanglement and LHC's shared-argument dependency.

### Region 3C — Typed absence as a worklist *(the gap-surfacing win)*
- **Look at:** the blank axes in `‹kb/eggs/notes/synthesis-by-population.md›`'s coverage.
- **What it demonstrates:** where a stratum has *no* assessed evidence, the cell is blank (`not assessed`) — distinct from `none` (assessed, verified absent). The blanks are a collection worklist: "here is the sub-population no study covered," which is *what to gather next*, not a false "no effect."

### The reader question this case makes easier
*"For my sub-population and outcome, which findings apply, and is the disagreement about the evidence or about the scope?"* — answered by Region 3A: the disagreement is almost entirely about scope, and the stratified structure shows it directly instead of averaging it away.

---

## The one-protocol payoff — read this last

The three cases were built with the **same** pipeline (`capture → analyze → connect → structure → verify → review`), the **same** deterministic checkers, and the **same** review machinery. What differs is entirely in the case-local contracts and the substance:

| | correlated evidence takes the form of… | the crux is… | the flattening risk is… |
|---|---|---|---|
| **COVID** | shared dataset + author overlap | which evidential line the market data supports | blending two parallel cases |
| **LHC** | one shared load-bearing argument | the cosmic-ray dependency | declaring "settled" and hiding joints |
| **Eggs** | shared funder | which scope a finding applies to | averaging population-specific findings |

One correlated-evidence instrument, computing over uniform provenance, surfaces all three *different* entanglements. That is the generalization claim in miniature — **the connective tissue is shared; the substance stays local** — and it is visible by reading one region from each case.

For the deepest single artifact, spend your last two minutes on **COVID Region 1C**: the correlated-evidence cluster is where the 23-orders-of-magnitude puzzle from the brief's own COVID framing becomes legible in a single view.
