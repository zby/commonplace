# Carry heuristics: deciding which transformations don't break which assessments

The optimization problem behind closure: rerunning every assessment after every transformation is always sound but expensive, and rerun-and-fix loops may not converge at all (fixing coherence adds connective tissue, which breaks compression, which cuts, which breaks coherence). Carrying evidence forward (ack) is cheap but is itself a judgment that can be wrong.

The heuristic deciding when carrying is safe does not need to be system machinery: it lives in the agent, which plans the pass — ordering, which transformations to run, which assessments to carry versus rerun. The system's job is to trust but check (see the division of labor below). The facts that follow are planning guidance the agent should respect, not a matrix to encode.

## Structural facts the agent's planning must respect

**1. Safety is per (edit-kind, check-kind) pair, with signs.** No edit kind is universally safe:

- glosses/clarifying additions preserve semantic checks almost perfectly — and are exactly what compression gates exist to catch (context cost);
- narrowing fixes preserve truth/grounding (they mostly shrink the claim) but can hurt completeness and break flow;
- deletions are safe for compression, adversarial for the grounding of remaining claims (may remove their support);
- reorderings are near-null for semantic checks, high-risk for coherence.

The organizing predictor: each check penalizes excess or deficit of some quantity; each edit kind moves that quantity in a known direction; preservation is predictable when the edit's direction is in the check's safe direction. This is why "small fix" is the wrong unit — direction matters more than size.

**2. Preservation is not compositional.** Many small revisions, each locally coherence-preserving, jointly make a note incoherent. Consequence for machinery: the carry decision must never judge the incremental diff (last edit); it must judge the cumulative diff against the last-assessed state. The review DB's accepted snapshots already provide exactly that baseline, so baseline-anchored acking is available by construction. Incremental acking drifts silently; baseline-anchored acking cannot — accumulated small edits eventually present as one large diff that no longer looks carry-safe, which is the correct behavior.

**3. Ex-ante constrained transformations beat ex-post diff classification.** Instead of a heuristic judging arbitrary diffs after the fact, type the transformations: each transformation kind declares its invalidation footprint — the check families it is allowed to affect — and closure reruns only the footprint. The declaration is enforced by constraint (the prompt/contract restricts what the transformation may do) plus occasional audit (did the copyedit actually change claims?). Step 9 of the full pass is already an informal instance: the flow-revise prompt's footprint is "flow/coherence only," currently enforced by 'do not' prose. Typing it would make the closure consequence explicit: a footprint-clean copyedit does not stale the semantic acceptance; an audit failure retroactively does.

**4. Convergence needs structure, not judgment.** Three standard moves, two already present in the full pass:

- **ordering** — content-before-form, so form fixes can't reopen content (the pass's step 8/9 design);
- **footprint-empty last transformation** — the final pass is constrained to a class that cannot break the checks being closed, so closure after it is cheap by contract;
- **stopping rule** — at most one closure cycle; residual findings route to the packet's open items rather than triggering another transformation round. Non-convergence is handled by refusing to loop, not by hoping the loop settles.

## Division of labor: heuristics in the agent, invariants in the system

The agent owns the plan and the carry judgments. The system owns the four things an agent cannot be trusted to self-supply:

1. **The baseline.** The system computes the cumulative diff against the accepted snapshot and hands it to the agent. Fact 2 is enforced mechanically, not left to agent discipline — the agent never gets to judge an incremental diff by mistake.
2. **The record.** Every carry is a version-anchored record carrying the agent's declared rationale and footprint, written when the decision happens — process history has one chance to become checkable.
3. **The check.** Sampled audits: rerun a fraction of carried assessments and compare. A flip is a caught false carry; the flip rate is the trust dial that sets the sampling rate. Start at 100% — which is indistinguishable from always-rerun — and decay as evidence accumulates. High flip rates for a check kind or transformation kind shrink trust back toward rerun for that kind.
4. **The fail-safe.** A carry that cannot be audited is not offered — same rule as marks: enforced-or-omitted. Wherever the check surface is missing, the default is rerun; a wrong carry is a silent false acceptance, a wasted rerun is only cost.

This is the checked-or-absent principle extended from deterministic recomputable values to judgment-valued caches: a carried acceptance is a cached judgment, and because recomputing a judgment is expensive and stochastic, the check is sampled rather than total, with an explicit trust dial in place of a hash comparison.

Two facts above soften under this division. The declared footprints of fact 3 stop being system-enforced contracts and become stated intent the audit verifies — a "flow-only" transformation that flips a semantic check is an audit failure, and repeat offenses shrink trust for that transformation kind. And no edit-kind taxonomy gets encoded anywhere: as models improve, the only thing that moves is the trust dial. Verification scaffolding persists while judgment scaffolding recedes (cf. the scaffolding-relaxation workshop).

## Consequences for the workshop's cases

- Case 1 (full-pass closure) becomes: the agent plans reruns and carries at the end of the pass and records rationale; the audit starts at 100% sampling, so initially every carry is also rerun and every flip is logged with a rough edit-kind classification of the S0→S2 diff. That log calibrates the trust dial — it is not training data for a system-side heuristic.
- The typed-footprint idea suggests a fourth candidate case: have the step-9 flow pass declare its footprint and audit the declaration over a few real runs — the first test of stated-intent-plus-audit as the cheaper alternative to diff-judging.
- The direction/monotonicity predictor (fact 1) is the strongest candidate for an eventually extractable note — as agent planning guidance, not system design — but only after the flip log confirms or corrects it.
- The sampled-audit-for-judgment-caches idea (trust dial over a cached judgment, versus total mechanical checking for deterministic caches) is a second extraction candidate: it extends [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) to a class of caches that note doesn't cover.
