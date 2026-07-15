---
description: "Ashby's ultrastable system — the cybernetic precedent for a second loop that reorganizes a system when essential variables leave viable limits, retaining by equilibrium rather than by an evaluator"
type: kb/sources/types/source-review.md
tags: [foundations, computational-model]
---

# Ashby, Design for a Brain — ultrastability

**Source:** W. Ross Ashby, *Design for a Brain: The Origin of Adaptive Behaviour*, 2nd ed. (Chapman & Hall, 1960), Chapters 7–8. Read from the full-text PDF at <https://ashby.info/Ashby%20-%20Design%20for%20a%20Brain%20-%20The%20Origin%20of%20Adaptive%20Behavior.pdf>. Ashby numbers sections as `chapter/section` (e.g. `7/7`); citations below give the section and the printed page.

**Capture note:** this is a source review, not a snapshot. The book is a copyrighted monograph and was not captured verbatim; the extraction below is authored from Chapters 7 ("The Ultrastable System," printed pp. 80–99) and 8 ("The Homeostat," printed pp. 100–121), which are the chapters that carry the ultrastability argument. Quotations are short and cited.

## Key Points

### Two loops, not one

An ultrastable system has "a motor output to the environment and *two* feedback loops" (7/5, printed p. 83). Ashby distinguishes them by role:

> The first loop … consists of the ordinary sensory input from eye, ear, joints, etc., giving the organism non-affective information about the world around it. The second feedback goes through the essential variables … it carries information about whether the essential variables are or are not driven outside the normal limits, and it acts on the parameters S. The first loop plays its part within each reaction; the second determines which reaction shall occur. (7/5–7/6, printed pp. 83–84)

The first loop is ordinary regulation, operating *within* a way of behaving. The second is slower and operates *on* the way of behaving, by changing the parameters `S` that fix which behavior the reacting part `R` produces.

### Essential variables and viability

The essential variables are those that must stay within physiological limits; Ashby draws them as "a dial with a pointer, and with two limit-marks, to emphasise that what matters about the essential variables is whether or not the value is within physiological limits" (7/3, printed p. 81). Viability is a *boundary condition*, not a graded score — the system registers in-limits or out-of-limits, and nothing finer.

### How changes are tried

`S` is realized by **step-functions**: variables that hold constant and then jump (7/13, printed p. 87). A step-mechanism has **critical states** whose occurrence makes it jump to a new value (7/18, printed p. 91).

The Homeostat makes the generator concrete, and it is the decisive detail. Its uniselector values "were deliberately randomised by taking the actual numerical values from Fisher and Yates' Table of Random Numbers" (8/2, printed p. 103). When a unit's essential variable leaves its limits, the step-functions change to three new values, and Ashby is explicit about what those values are:

> These new values have no special relation either to the previous values or to the problem in hand—they are just the values that next follow in Fisher and Yates' table. (8/3, printed p. 104)

Trial-and-error is not a second-rate method here but a *necessary* one, because the environment is a Black Box whose input–output relations can only be elicited by acting and observing the result (7/4–7/5, printed pp. 82–83).

### What causes a configuration to be retained

This is stated as a rule, and it is the sharpest thing in the chapter:

> If the trial is unsuccessful, change the way of behaving; when and only when it is successful, retain the way of behaving. (7/7, printed p. 84)

Operationally: when the essential variables are outside their limits, *no* state of `S` is equilibrial, so `S` must keep changing; when they are all within limits, *every* state of `S` is equilibrial, so `S` stays put (7/7, printed p. 84). Retention is therefore **negative and structural** — a configuration persists because nothing is left to displace it, not because anything scored it well. Ashby's veto-theorem argument concludes that the whole can only rest where both the essential variables and `S` are at equilibrium, so "if it goes to an equilibrium, the equilibrium will always be found to be an adapted one" (7/11, printed p. 86).

He further argues the second feedback is *necessary*: any system with essential variables and limits that adapts by testing behaviors "must have a second feedback formally identical (isomorphic) with that described here," for brains "living and mechanical" alike (7/8, printed p. 85).

### What Ashby does not supply

Stated plainly, because the gaps matter more than the correspondences:

- **No explicit candidate search.** There is no generator that proposes changes *targeted at the problem*. The Homeostat's new parameter values are drawn from a random-number table and bear no relation to the difficulty at hand (8/3, printed p. 104). Nothing selects *which* aspect to modify or *what kind* of change to attempt.
- **No scoring evaluator.** Nothing scores, ranks, or compares candidates. The only signal is the binary in-limits/out-of-limits state of the essential variables — a criterion that can reject (by letting the reorganization continue) but cannot rank. Read through the modern vocabulary this is the floor case of an evaluator, not a missing one; what is genuinely absent is any representation of *why* a configuration is good.
- **No self-representation.** The ultrastable system contains no model of itself. `S` is a set of parameters that get jogged, not structures the system inspects, reasons about, or acts through as a representation of its own organization. Ashby's mechanism is causal and material throughout, and this is precisely what distinguishes it from computational reflection.

## Relevance to the KB

Ashby is the cybernetic **precedent** for the claim that [an improvement loop requires search, evaluation, and operative retention](../notes/an-improvement-loop-requires-search-evaluation-and-operative-retention.md) — an adaptive system that changes its own organization when ordinary regulation fails, with a second loop distinct from the first. The two-loop structure is exactly the distinction between operating a system and modifying it. The Homeostat is a real instance of the loop, not a defective one, and because the mechanism holds no self-representation it establishes that **reflection is not a premise of the decomposition**: the three functions are exhibited without it.

But the mapping onto the modern vocabulary is an **interpretation**, and it marks the *floor* rather than the archetype. Read through that vocabulary, ultrastability occupies the minimal corner of the design space: search is a random draw, evaluation is a one-bit viability test, and retention is equilibrium — the absence of a force to change further. Ashby did not decompose adaptation into generator and oracle, and translating him as though he had would credit him with distinctions he explicitly did without.

Two things follow, and the second is the load-bearing one. Ultrastability shows how *little* machinery adaptation requires, and thereby what the extra machinery of a search-and-evaluate architecture is actually buying. And it shows what a **self-representation** buys, which is the line between this and a *reflective* [self-improving system](../notes/definitions/self-improving-system.md). On the broad definition the Homeostat is itself a self-improving system — the loop runs on its own organization against a viability standard that can reject, with no human anywhere — occupying the category's minimal, non-reflective, fully autonomous corner. The Homeostat genuinely retains — the surviving configuration persists and steers later behavior, which is what makes the retention operative — but what it retains is an opaque parameter setting rather than a representation. Nothing in the mechanism can read that setting, say why it was good, criticize it, or carry it to the next problem, so the loop runs indefinitely and nothing compounds. Ashby is the clean demonstration that adaptation can retain without accumulating, and that [routing the loop through a self-representation is what makes retention addressable](../notes/reflection-buys-addressability-not-compounding.md).

The gap is most instructive at retention. Ashby's retention criterion is *negative* — a configuration survives because it stops the reorganization, not because an evaluator endorsed it. That is a real alternative to oracle-gated retention, and it is worth holding next to the [oracle-strength spectrum](../notes/oracle-strength-spectrum.md), which grades evaluators but does not contemplate one that can only reject, never rank. It also contrasts instructively with the [Gödel machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md), the opposite extreme: retention licensed only by proof. Ashby retains anything that stops hurting; Schmidhuber retains only what is proved to help. Both are change loops; they differ almost entirely in the acceptance gate.

Finally, Ashby is a clean **negative case** for [reflective system](../notes/definitions/reflective-system.md). The ultrastable system adapts, modifies its own organization, and is causally coupled to its own viability — and it is still not reflective, because it has no self-representation. It is the sharpest available demonstration that adaptation does not imply reflection, and that the definition's causal-connection-through-a-representation requirement is doing real work rather than restating "the system affects itself."

## Open Questions

- Whether Ashby's negative retention criterion (persist because nothing displaces you) has a useful analogue in artifact-based systems, where retention is usually positive and authored.
- Whether the random generator is essential to ultrastability or merely the simplest sufficient one — Ashby argues the second feedback is necessary (7/8), but makes no such claim about how trials are generated.

---

Relevant Notes:

- [An improvement loop requires search, evaluation, and operative retention](../notes/an-improvement-loop-requires-search-evaluation-and-operative-retention.md) — evidence: an improvement loop with no self-representation, establishing that reflection is not a premise of the decomposition, and marking the floor of each function
- [Self-improving system](../notes/definitions/self-improving-system.md) — exemplifies: the floor of the category — a minimal, non-reflective, autonomous occupant whose every function takes its weakest viable form
- [Reflection buys addressability, not compounding](../notes/reflection-buys-addressability-not-compounding.md) — evidence: a loop that retains without a self-representation, so what is kept is a setting rather than knowledge and nothing accumulates
- [Reflective system](../notes/definitions/reflective-system.md) — evidence: a negative case — an adaptive, self-modifying system that is not reflective, because it has no self-representation
- [Gödel machines are a proof-governed case of reflective self-modification](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) — compares-with: the opposite extreme of the acceptance gate, retention by proof rather than by equilibrium
- [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) — evidence: a rejection-only evaluator below the spectrum's weakest grade
- [Conant and Ashby, Every Good Regulator of a System Must Be a Model of That System](./conant-ashby-every-good-regulator-1970.ingest.md) — compares-with: Ashby's later, stronger claim that regulation requires a model, which the ultrastable system itself does not satisfy
</content>
