---
description: "Bare autonomy is free, but warranted evaluation autonomy reaches only the candidates an oracle can assess with the required confidence"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, evaluation]
---

# Warranted autonomy is bounded by oracle reach

Autonomy — how much of an improvement pathway runs without a person — is a separate gradient over a [self-improving system](./definitions/self-improving-system.md). This note concerns the pathway shape that has a gate: the [proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md), where candidates are evaluated and can fail to be adopted. Bare autonomy is free: hand the gate to a model with a rubric and no human runs it. More autonomy strengthens that attribution, but it is not automatically a better design. What is bounded is **warranted autonomy** — a loop that runs unattended and can still be trusted with what it accepts.

Warranted evaluation autonomy reaches only the candidates the available oracle can assess with the required confidence, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). Outside that reach, unattended evaluation remains possible but unwarranted.

## Strength and strictness are different

Oracle strength concerns how reliably a check discriminates relative to the objective and what its result establishes. **Strictness** concerns how much evidence the gate demands before accepting. Increasing strictness under a fixed oracle usually narrows acceptance: uncertain candidates are rejected or deferred so the remaining acceptances carry more assurance.

Strengthening discrimination can instead expand warranted reach. A better verifier may reject bad candidates the old one passed while also accepting good candidates the old one could not distinguish from bad ones. Test suites, proofs, model judges, and human judgment therefore do not form nested acceptance sets; they establish different things over overlapping domains.

The [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) is the limiting case of assurance obtained through strict acceptance: a rewrite runs only when the machine proves that switching helps under its formalization. It gains warranted total autonomy within that proof surface and cannot reach improvements it cannot prove. The cost follows from its proof requirement, not from a general law that stronger oracles always accept less.

[Commonplace](../reference/commonplace-as-a-reflective-system.md) composes several oracles: tests and validators for structural constraints, human judgment for criteria that are not adequately automated. It could hand the latter gates to a model tomorrow and become more autonomous without becoming more warranted. Expanding warranted autonomy requires improving the relevant oracle's discrimination or narrowing the gate to cases it can establish.

The useful questions are therefore both *how autonomous is the loop?* and *which of that autonomy is warranted by its oracles?*

## Oracle hardening moves the boundary

Oracle hardening can move a gate from unwarranted to warranted autonomy: a rubric becomes a validator, a heuristic becomes a test, or an unmeasured property becomes observable. The [oracle-strength spectrum](./oracle-strength-spectrum.md) describes different verification surfaces, not a total order over their acceptance rates.

Hardening may expand warranted reach by resolving cases the old oracle could not discriminate. Where criteria still outrun the oracle, the system must retain a human evaluator, narrow the unattended gate, or accept unwarranted autonomy.

## Scope

- The claim concerns **evaluation** autonomy, so it is scoped to proposal-selection pathways — a direct evidence-driven update has no gate to hand over, and its trustworthiness is a question about the objective and the update rule instead. Search has a different failure surface, [since false-positive generation faces evaluation before retention](./false-positive-generation-is-filtered-before-retention.md).
- Bare autonomy means nobody is required at the gate. Warranted autonomy additionally claims that the unattended gate is reliable enough for its use.
- Warrant is objective-, risk-, and threshold-relative. No oracle is warranted for every decision merely because it is mechanical.
- Several oracles may govern different parts of one acceptance decision; their combined reach need not equal the union of what each accepts independently.

---

Relevant Notes:

- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: verification bounds unattended evaluation that remains trustworthy
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the loop whose evaluation function the oracle governs
- [Self-improving system](./definitions/self-improving-system.md) — extends: distinguishes bare autonomy from warranted autonomy
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — extends: why unattended evaluation has the more consequential false-positive failure
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: warranted autonomy bounded by a proof requirement
- [Oracle-strength spectrum](./oracle-strength-spectrum.md) — extends: grades the verification surfaces that determine oracle reach
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: a pathway-mixed system whose autonomy profile aligns with heterogeneous oracle reach
