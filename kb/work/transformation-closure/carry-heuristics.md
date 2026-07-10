# Carry heuristics: deciding which transformations don't break which assessments

The optimization problem behind closure: rerunning every assessment after every transformation is always sound but expensive, and rerun-and-fix loops may not converge at all (fixing coherence adds connective tissue, which breaks compression, which cuts, which breaks coherence). Carrying evidence forward (ack) is cheap but is itself a judgment that can be wrong. The machinery this workshop is looking for is the layer that decides *when carrying is safe* — an optimization over an always-available sound fallback, never a replacement for it.

## Structural facts the heuristic must respect

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

**5. The compatibility matrix should be learned, not designed.** Because rerun is sound, the cheapest path to the heuristic is empirical: for a while, rerun everything after every pass and log which checks actually flipped after which edit kinds. The (edit-kind × check-kind) matrix falls out of the logs; hand-written heuristics come after the data, as compression of it. Until then the default is rerun, and the heuristic must fail toward rerun wherever uncertain — a wrong carry is a silent false acceptance, a wasted rerun is only cost.

## Consequences for the workshop's cases

- Case 1 (full-pass closure) doubles as the instrumentation vehicle: the closure step should initially always rerun and record whether the verdict flipped, tagged with a rough edit-kind classification of the S0→S2 diff. That log is the raw material for the matrix.
- The typed-footprint idea suggests a fourth candidate case: write the step-9 flow pass as a declared-footprint transformation and audit its footprint over a few real runs — the first test of constraint-plus-audit as a cheaper alternative to diff-judging.
- The direction/monotonicity predictor (fact 1) is the strongest candidate for an eventually extractable note — but only after the flip log confirms or corrects it.
