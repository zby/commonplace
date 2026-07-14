---
description: "Autonomy in evaluation extends only as far as an oracle reaches, and strengthening the oracle narrows what it will accept — so autonomy is bought, and the currency is reach"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, evaluation]
---

# A stronger oracle buys autonomy and pays in reach

Autonomy — how much of a [governed adaptation loop](./governed-adaptation-requires-search-evaluation-and-retention.md) runs without a person — is what the *self* in self-improving names, and there is no reason to want less of it. It cannot be turned up at will. Automating an evaluation for which no adequate oracle exists does not produce a more self-improving system; it produces a less governed one, retaining changes nothing checked. The system does not advance within the category, it drops out of it, into plain self-modification.

So autonomy in evaluation extends exactly as far as mechanical verification reaches, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). What that framing leaves implicit is the price, and the price is the point: **a stronger oracle accepts fewer things.**

## The trade

Rank the oracles by strength and the acceptance sets nest. Proof accepts less than tests; tests accept less than judgment. That ordering is not incidental — it is what strength *means*. An oracle is strong because it refuses to certify what it cannot establish, and the same refusal that makes its acceptances trustworthy makes them rare. Buy autonomy with a stronger oracle and the loop can run unattended over a smaller space of improvements.

The [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) shows the bill in full. It adopts the strongest oracle available — accept a rewrite only under proof that it helps — and gets total autonomy with it: search, evaluation, and retention all run without a human. It pays the whole price in reach. Every improvement it cannot prove is unreachable, and most improvements worth having cannot be proved.

[Commonplace](../reference/commonplace-as-a-reflective-system.md) settles the same trade at the other end. Its oracles are tests, validators, and a maintainer's judgment; its acceptance set is correspondingly wide, and it can adopt improvements no proof system would certify. It pays in autonomy: the human is still standing at every gate where the judgment cannot be mechanized — which is exactly where the theory predicts a human must stand.

Neither is misconfigured. They are two settlements of one trade, and the position on the autonomy gradient is *downstream* of where the trade was settled. That is why the useful question about a self-improving system is never *how autonomous is it* but **what does its oracle reach, and what does that reach cost**.

## Why the trade is real and not just a budget

The obvious objection is that the trade is an artifact of not trying hard enough — build a *better* oracle, one that is both strong and broad, and the tension dissolves. Sometimes it does. Oracle-hardening is real work with real wins: a rubric that becomes a validator, a heuristic that becomes a test, a property that turns out to be checkable after all. The [oracle-strength spectrum](./oracle-strength-spectrum.md) is a description of where that work has and has not paid off.

But hardening moves the frontier; it does not remove it. At any fixed level of oracle-construction effort, the strength you take is paid for in breadth, because the improvements that resist mechanization are not a residue of laziness — they are the ones whose criteria the system cannot state. A system that could state them would have an oracle already. The trade binds wherever criteria outrun formalization, which is most places that matter, and the effect of hardening is to shift *which* improvements sit on the far side of it, not to empty that side.

## Scope

- The claim is about **evaluation** autonomy. Search autonomy is not bought the same way and is cheaper to take, [since search errors are filtered while evaluation errors are retained](./search-errors-are-filtered-evaluation-errors-are-retained.md) — a bad candidate costs effort, a bad acceptance compounds.
- Strength and reach are not a single scalar each, so the trade is a direction, not an exchange rate. Two oracles can be incomparable, accepting overlapping but non-nested sets, and a system usually runs several at once at different gates.
- Reach is measured against improvements the system could otherwise have adopted. An oracle that refuses nothing useful costs no reach — which is the case for the well-mechanized gates, and precisely why they were mechanized first.

---

Relevant Notes:

- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: the ceiling this note prices; autonomy in evaluation reaches exactly as far as verification does
- [Governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — grounds: the loop whose evaluation function is being bought
- [Self-improving system](./definitions/self-improving-system.md) — extends: supplies the price behind the definition's autonomy gradient
- [Search errors are filtered; evaluation errors are retained](./search-errors-are-filtered-evaluation-errors-are-retained.md) — extends: why evaluation is the function that must be bought and search is the one to automate first
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the strongest-oracle corner, where autonomy is total and reach is minimal
- [Oracle-strength spectrum](./oracle-strength-spectrum.md) — extends: grades the oracles this trade ranges over, and maps where hardening has paid off
- [Human-inclusive boundaries make reflection cheap](./human-inclusive-boundaries-make-reflection-cheap.md) — extends: autonomy is the discriminating gradient; this note says what it costs to move along it
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: the wide-reach, low-autonomy settlement, with the human at the gates no oracle closes
