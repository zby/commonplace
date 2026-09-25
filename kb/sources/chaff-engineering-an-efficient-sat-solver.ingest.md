---
description: "Chaff (DAC 2001): watched-literal propagation and the VSIDS decision heuristic, which ranks two-valued SAT variables by decayed conflict-clause counts, not remaining options"
source: https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 8c2c3c97737fede2530b5e29195f66f55b676ee80e18d1824306cd63fd8e57cd
ingested: "2026-09-24"
occasion: "How do SAT solvers choose which decision to make next when the candidates cannot be ranked by how many options each has left? (For a KB note on solving low-degree-of-freedom subproblems first.)"
type: types/ingest-report.md
domains: [sat-solving, search-heuristics, variable-ordering, search-control]
learning_claims: true
---

# Ingest: Chaff: Engineering an Efficient SAT Solver

## Classification

This is a conference paper (DAC 2001) describing a new algorithm implementation and reporting benchmark comparisons, so it is a scientific paper. Author: Moskewicz, Madigan, Zhao, Zhang, and Malik (Berkeley, MIT, Princeton). Chaff and its VSIDS heuristic became the template for later conflict-driven SAT solvers. The authors built the solver they evaluate, and all timings are their own runs; the paper is primary evidence for the mechanisms and the reported results, not an independent replication.

## Summary

Chaff is a complete Davis-Putnam backtracking SAT solver with GRASP-style conflict analysis and learned conflict clauses. The paper attributes its speedups to engineering of the basic loop, not to "sophisticated learning strategies". Its two main contributions are a propagation scheme and a decision heuristic. The propagation scheme watches two literals per clause, so a clause is visited only when it may have become unit, and backtracking needs no watch updates. The decision heuristic, VSIDS, keeps one counter per literal. The counter is incremented whenever a clause containing that literal is added, and all counters are periodically divided by a constant. Each decision picks the unassigned literal with the highest counter. Because learned conflict clauses dominate the clause database on hard instances, VSIDS in effect favours literals from recent conflicts, and it costs little because counters change only when clauses are added. The paper argues that decision or conflict counts are misleading metrics for comparing heuristics, and that total runtime is the only fair one. It also describes scheduled lazy deletion of learned clauses and restarts that keep learned clauses and decision statistics. Reported results are whole-solver comparisons against GRASP and SATO: comparable on easy DIMACS classes, and about one to two orders of magnitude faster on hard microprocessor-verification suites. The paper gives no benchmark table that isolates VSIDS or the propagation scheme; the benchmark results come from the whole engineered solver in one conflict-learning design.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, Chaff is the anchor source for the SAT side of variable ordering. In SAT, every unassigned variable has exactly two values, so "fewest remaining options" cannot separate decision candidates. Chaff's answer has two parts. A variable with only one admissible value is not a decision at all: the unit clause rule forces it during propagation, before the next decision. Among the remaining candidates, VSIDS ranks literals by recent involvement in conflict clauses, not by domain size or static clause structure. The paper also names the static alternatives it tested and beat on its benchmarks (RAND, DLIS and its variants, BOHM, MOMs, JW-OS, JE-TS), but it gives no per-heuristic numbers.

For the general KB, Chaff is a technical basis for the "Conflict-directed backtracking, learned constraints, and restarts" and "Restart schedules" sections of [Cost-sensitive formalisms for tentative theory search](../notes/cost-sensitive-formalisms-for-tentative-theory-search.md). That note marks those sections as needing source grounding. Chaff confirms that restarts clear assignments while keeping learned clauses and decision statistics. It also shows that clause deletion together with restarts can cost completeness, which Chaff recovers by growing the relevance bound or the restart period. It does not describe backjumping, so it should not be cited for that part of the note.

Conflict clauses give [A failure explanation becomes search control only when it changes a later branch decision](../notes/failure-explanation-changes-later-branch-decisions.md) a formal, sound instance. A retained explanation of a failed branch changes later branches through two channels: propagation prunes assignments, and VSIDS raises decision priority. The VSIDS evaluation argument supports [A search controller is tested by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md), with one qualification the note does not state: the controller's own computation must be charged in the comparison. Restarts that keep learned clauses fit [Accumulation counts dependence through the retained result](../notes/accumulation-counts-dependence-through-the-retained-result.md) as a symbolic, within-run case. Their horizon is one solver run on one instance.

Chaff compares with [Shifting inductive bias with the Success-Story Algorithm](./shifting-inductive-bias-success-story-algorithm.ingest.md) and [Optimal Ordered Problem Solver](./optimal-ordered-problem-solver.ingest.md) on how a retained search product biases later search. SSA revises search bias by rolling changes back. VSIDS never rejects an update; old bias fades through periodic division. OOPS transfers frozen code across tasks, while Chaff's learning stays within one instance.

## Learning Claims (our opinion)

On its own terms, Chaff adapts within one run through two retained products. Learned conflict clauses, inherited from GRASP, record assignment combinations that led to conflict, and propagation then prevents them. VSIDS counters are numeric statistics over literals in added clauses, and periodic division makes them favour recent conflicts. Restarts discard the assignment and decision stack but keep both products, so the next trajectory is computed from them. The authors frame their speedup as engineering, not learning. That framing concerns their contributions (cheap propagation, cheap decisions); the design still depends on learned clauses, since VSIDS counters are mostly driven by them on hard instances.

In Commonplace terms this is adaptation of search control through operative retained results, and it is not a [theory builder](../notes/definitions/theory-builder.md). A conflict clause is stated in formal language (condition 1) and guides propagation through what it says (condition 2). VSIDS counters fail condition 1: no counter says anything. Criticism (condition 3) decides the verdict. A conflict clause is a sound consequence of the formula, so the solver never attempts to refute it; deletion removes it for memory reasons, not because it was found wrong. This is the [fixed-theory exclusion](../notes/definitions/theory-builder.md#exclusions). Iteration (condition 4) is not separately decided: clauses survive restarts and shape the next trajectory, which is persistence across the rounds of one run, but they are derived consequences, not results of criticism of a stated theory. The whole-solver speedups are the paper's improvement claim; they are not attributed to the learned clauses or counters. The case is useful as a contrast: it shows retained failure explanations steering search when those explanations are guaranteed correct, which is the condition fallible natural-language explanations lack.

Under [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), VSIDS adapts only a priority ordering over literals of a fixed CNF encoding. The encoding, the literal as the unit of ranking, the argmax decision rule, the increment and decay constants, and GRASP-style conflict analysis are all fixed outside the adaptive part. The reported gains support that this configuration worked on the tested suites. They do not compare alternative encodings or decision units, and they do not isolate the adaptive counters from the rest of the solver.

## Extractable Value

1. **SAT decision order when domain size cannot discriminate** -- Every unassigned SAT variable has two values, so the "fewest options first" rule has nothing to rank. Chaff separates the degenerate case from the ranking case. Forced (single-option) variables are assigned by unit propagation before any decision. The remaining two-option candidates are ranked by VSIDS, using decayed counts of their appearances in added (mostly learned conflict) clauses. For a note on solving low-degree-of-freedom subproblems first, this gives a precise example of what replaces domain-size ordering: eager propagation of zero-freedom choices plus an adaptive conflict-activity signal. The signal is our reading of what "constrained" means here; the paper itself describes VSIDS only as "attempting to satisfy recent conflict clauses". The benefit is shown only within Chaff's conflict-learning design. [quick-win]
2. **Static-structure heuristics lost to a cheap adaptive one on these benchmarks** -- The paper reports testing RAND, DLIS (literal most frequent in unresolved clauses) and its variants, BOHM, MOMs, JW-OS, and JE-TS before designing VSIDS, and claims an order-of-magnitude gain on the hardest problems with no loss on simpler ones. This is a data point that clause-count ordering (a structural proxy for how constrained a literal is) did worse than conflict-driven ordering in this solver. No per-heuristic table is given, so it cannot be treated as a controlled comparison. [just-a-reference]
3. **Charge controller overhead when comparing search heuristics** -- Chaff argues that decision and conflict counts mislead because decisions trigger unequal propagation work and heuristics carry unequal computation cost. Only runtime counts. VSIDS won partly by being cheap (about 10% of runtime on hard instances). This adds an overhead qualification to the search-controller evaluation note. [quick-win]
4. **Grounding for restarts and learned-constraint retention** -- Restarts keep learned clauses and decision statistics, unlike GRASP's; clause deletion is scheduled at adoption by a relevance bound; and completeness is recovered by growing the restart period or relevance bound. These ground the restart and learned-constraint sections of the cost-sensitive formalisms note, except its backjumping sentence. [quick-win]
5. **Retirement scheduled at adoption** -- Each learned clause gets its deletion condition when it is added. This is a counter-design to cheap adoption with weak retirement, but it is one formal-domain case and learned clauses have no downstream consumers to coordinate. It is worth a log entry, not a note. [just-a-reference]

## Limitations (our opinion)

The benchmark tables compare whole solvers. Chaff differs from GRASP and SATO in propagation, decision heuristic, clause deletion, and restarts at once, so the tables do not attribute the speedup to VSIDS or to watched literals. The VSIDS claim ("an order of magnitude" on the hardest problems) is stated without its own table, the rival heuristics are named without numbers, and the paper admits that one benchmark class (pret) needed a decision-strategy parameter change. The authors say their strategy is better "for the range of problems on which we tested our solver", which is mostly hardware-verification instances; the result may not transfer to random or other structured SAT families. GRASP comparisons on some suites rely on configurations the authors could not reproduce.

A simpler account of VSIDS's advantage is that its main benefit is low overhead, not better ordering. The paper's own emphasis on overhead leaves this open, since it reports no decision-count comparison alongside runtime. For the occasion, the paper never discusses domain size or the fail-first principle. The link between VSIDS and "most constrained first" is our interpretation, not the authors' claim. VSIDS also depends on conflict clauses being added, so it does not carry over to solvers or search processes without clause learning.

The pdftotext capture damages part of the VSIDS section: several lines in the paragraph on decision-count metrics are garbled, and the Table 2 layout is scrambled. Claims here about that paragraph rest on the readable portions, and this report does not rely on individual Table 2 cells. Conflict analysis is deferred to GRASP and not described, and the paper has no section 6.

## Recommended Next Action

When writing the planned note on solving low-degree-of-freedom subproblems first, add a SAT paragraph citing this ingest: forced single-option assignments are handled by unit propagation before any decision, and the remaining two-valued choices are ranked by VSIDS conflict activity rather than option count. State that the paper gives no ablation isolating VSIDS, and that reading VSIDS as a "most constrained first" signal is the note's interpretation.

---

Relevant Notes:

- [Original paper](https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf) — derived-from: primary description of watched-literal propagation, VSIDS, clause deletion, restarts, and benchmark results
- [Cost-sensitive formalisms for tentative theory search](../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) — is-evidence-for: restarts keep learned clauses and statistics; deletion versus completeness trade-off
- [A failure explanation becomes search control only when it changes a later branch decision](../notes/failure-explanation-changes-later-branch-decisions.md) — is-evidence-for: conflict clauses change later branches through propagation and decision priority
- [A search controller is tested by what it brings to stronger evaluation](../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — is-evidence-for: heuristics compared by runtime, with controller overhead charged
- [Accumulation counts dependence through the retained result](../notes/accumulation-counts-dependence-through-the-retained-result.md) — is-evidence-for: learned clauses across restarts as a symbolic within-run accumulation case
- [Shifting inductive bias with the Success-Story Algorithm](./shifting-inductive-bias-success-story-algorithm.ingest.md) — compares-with: rejection-based versus decay-based revision of search bias
- [Optimal Ordered Problem Solver](./optimal-ordered-problem-solver.ingest.md) — compares-with: how a retained search product biases later search, cross-task versus within-instance
