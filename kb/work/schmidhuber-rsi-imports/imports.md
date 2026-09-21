# Five candidate imports

These are design and experimental questions within the
[adopted RSI research direction](./README.md#position-within-the-rsi-program).
Starting with interpreted methodology and selectively codifying parts is our
development path; the five mechanisms below remain candidates to assess.
The source papers do not
test natural-language KB methodology. Their algorithms and evidence are
summarized in the ingests linked below; source-dependent promotion needs
grounding through retained quotes or the required snapshot citation.

## 1. Learn the improvement procedure

**Source mechanism.** In [self-modifying policies](../../sources/reinforcement-learning-self-modifying-policies.ingest.md),
the policy generates modifications to itself. Earlier modifications can
therefore alter how subsequent modifications are generated.

**Candidate import.** Treat procedures for diagnosis, investigation, test
construction, and revision as learning products. A natural-language procedure
can be interpreted by the same model that uses it to revise another procedure.
Distinguish an improved task skill from an improved method for improving skills.

**Existing coverage and remaining question.** The
[reflective-builder account](../../notes/definitions/reflective-theory-builder.md)
already admits machinery revision. The added research focus is a concrete
dependency: does a learned procedure make later improvement work more
productive? A rewritten skill and successful task output do not alone answer
that question. The [first experiment](./first-experiment.md) tests this import
together with the next one.

## 2. Reuse knowledge to direct search

**Source mechanism.** [OOPS](../../sources/optimal-ordered-problem-solver.ingest.md)
can use the contents of an earlier program to change later instruction
probabilities. The earlier program need not execute its original solution to
help discover a new one. Its reported transfer is bounded by the supplied
language, curriculum, and initial bias.

**Candidate import.** Retained explanations and criticism can influence which
hypothesis, repair, or test the agent pursues. A lesson about stale applicability
conditions could redirect an investigation away from rewriting correct content.
This is a proposed semantic counterpart, not an implementation of OOPS.

**Existing coverage and remaining question.**
[Natural-language project state may specialize search heuristics](../../notes/natural-language-project-state-specializes-search-heuristics.md)
already states the conjecture. OOPS supplies a specific predecessor and a
useful contrast. Test changed branch choices and their consequences; retrieval,
citation, or a persuasive explanation without changed search is insufficient.

## 3. Preserve a route beyond inherited methodology

**Source mechanism.** OOPS divides search effort between extending an earlier
solution and fresh program beginnings. Its exact allocation and guarantees
belong to its formal construction.

**Candidate import.** When a retained methodological commitment may be
misdirecting work, compare a bounded alternative developed without that
commitment. Keep task requirements and relevant evidence available. Do not
interpret this as removing standing authorization or safety constraints.

**Existing coverage and remaining question.**
[Search allocation precedes decisive evaluation](../../notes/open-ended-improvement-allocates-search-before-evaluation.md)
explains why a strong acceptance check cannot rescue an alternative never
considered. Determine when an alternative starting point produces useful
variation and when it merely repeats discarded work. Do not copy OOPS's
half-budget allocation into an LLM workflow without evidence.

## 4. Evaluate later consequences and reconsider retention

**Source mechanism.** The [success-story algorithm](../../sources/shifting-inductive-bias-success-story-algorithm.ingest.md)
assesses earlier modifications through later reward history and can restore
saved policy components when continued retention fails its criterion.

**Candidate import.** Distinguish immediate quality from later usefulness.
A diagnostic distinction may initially cost effort but enable later repairs;
an instruction that passed review may repeatedly misdirect subsequent work.
Assess continued use against those consequences, including the time needed
for a benefit to become observable.

**Existing coverage and remaining question.** The
[compounding measurement note](../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md)
already requires later outcomes and a consumption path. SSA adds a concrete
account of delayed credit and revocable retention. Choose an observable horizon
and defensible outcome comparison before proposing a KB retention rule.
Historical survival does not establish causation; restoring a file cannot undo
decisions or environmental effects produced while it was active.

## 5. Account for the cost of learning

**Source mechanism.** SSA includes elapsed learning time in reward-rate
accounting; OOPS includes verification costs in its search accounting.

**Candidate import.** Count diagnosis, reading, candidate generation, review,
maintenance, and operator judgment when assessing an improvement procedure.
Compare total cost at comparable outcome quality, and quality under matched
budgets. Keep unlike costs visible rather than forcing them into an arbitrary
single score.

**Existing coverage and remaining question.** The
[current retention research](../../notes/commonplace-studies-conjectural-learning-through-retained-theories.md)
and compounding protocol already include these costs. Import the papers as
mechanistic precedents and sharpen a concrete accounting practice only where
current experiments omit consequential work. A new ledger is not itself an
improvement.

## Additional comparison source

The [RSI retrospective](../../sources/recursive-self-improvement-since-1987.ingest.md)
maps the wider research program. The
[Gödel-machine comparison](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
distinguishes proof-authorized switching from empirical retention. Use it to
bound claims about assurance; it does not prescribe a proof gate for this work.
