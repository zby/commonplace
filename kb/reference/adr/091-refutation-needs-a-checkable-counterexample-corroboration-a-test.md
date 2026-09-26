---
description: "A universal claim is refuted by a counterexample others can check again, not by one unrepeated report; evidence corroborates only when it reports a test the claim could have failed, so the cases a claim was built from are its origin, not its support"
type: reference/types/adr.md
tags: []
status: accepted
---

# 091-Refutation needs a checkable counterexample, and corroboration needs a test

**Status:** accepted
**Date:** 2026-09-26
**Amends:** [ADR 066](./066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) (decision 1, the universal mode's refuter)

## Context

ADR 066 defined the universal mode as "one genuine counterexample refutes" and left "genuine" undefined. Read literally, one reported exception, such as a single session episode, would defeat a universal note. [Popper's §22](../../sources/popper-logic-of-scientific-discovery.ingest.md) rejects that reading: "non-reproducible single occurrences are of no significance to science", and a theory counts as falsified only when a reproducible effect contradicts it. His §18 adds that a contradiction falsifies the claim together with the conditions it was applied under, without saying which part failed.

The link vocabulary had the matching gap on the positive side. `evidenced-by` covered anything that "corroborates, qualifies, or bounds" a claim, so the case a note was generalized from could be cited as its corroboration. Appendix \*ix counts evidence toward corroboration only when it reports sincere attempts to refute the theory. The operator's aim of linking corroboration to claims needs that distinction, and it applies the same way to internal evidence (session traces, reports, ADRs) and to external sources.

## Decision

1. **Universal refuter.** A counterexample refutes a universal claim when others can check it again: a specified case whose conflict with the claim any reader can re-derive, or an observed effect shown to recur. A single unrepeated report of an exception raises a problem to test. The premise-decomposition gate grades it `DOUBTFUL`, not `DEFEATED`.
2. **Blame is named.** A refutation says whether it blames the claim or the conditions the claim was applied under.
3. **Origin is not corroboration.** Evidence corroborates a claim only when it reports a test the claim could have failed. A case or source the claim was built from is linked `abstracted-from`. An `evidenced-by` link that claims corroboration says what the claim risked and whether the evidence came after the claim or independently of how it was built. Corroboration is dated relative to the evidence accepted when it was appraised.
4. **Scoping produces a hypothesis.** When scoping a Commonplace-derived claim leaves a claim about the design space, that claim is a new universal hypothesis whose origin cases do not corroborate it. A witness names the universal prohibition it contradicts or the existence claim it verifies.

The rest of ADR 066 stands, including the statistical and ideal-type refuters, which now cite §§65–68 for the probabilistic treatment.

## Considered alternatives

**Keep "genuine" undefined and leave it to reviewer judgment.** Rejected: the gate would keep grading one anecdote as a defeat, and nothing in the contract would stop it.

**Require an observed recurrence for every refutation.** Rejected: most review counterexamples are specified cases, not observations. A specified case is already reproducible in Popper's sense, because anyone can re-derive the conflict. Demanding repeated observation would disarm the gate.

**A separate `corroborated-by` label beside `evidenced-by`.** Rejected for now: the context phrase can carry the test, and a new label would require re-sorting every existing `evidenced-by` edge before it helped any reader. It becomes worth revisiting if corroboration records need to be enumerated mechanically.

**Forces.** One-off internal episodes are becoming the main input for new notes, so their evidential role had to be fixed before they are linked at scale. The primary text is now in the KB, so the rules can be grounded in it rather than in recollection.

## Consequences

**Easier.** A session trace can be cited without deciding whether it proves anything; its link says whether it was the claim's origin or a test of it. Review cannot retire a universal note on one anecdote.

**Harder.** Authors who claim corroboration must name the test and its date. A reviewer holding one real but unrepeated failure must look for a second case or specify the conditions under which it recurs.

**Riskier.** "Others can check it again" can be used to dismiss inconvenient evidence. §20 forbids rejecting a checkable counterexample by doubting who reported it, and the `DOUBTFUL` grade keeps an unrepeated report visible rather than discarding it.

**Limits.** Existing `evidenced-by` edges are not audited. Links whose context phrase does not name a test read as qualifying or bounding, not as corroboration. Not yet exercised in a full pass.
