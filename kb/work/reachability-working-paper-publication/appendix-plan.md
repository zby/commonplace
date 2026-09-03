# Reachability working-paper appendix plan

## Package shape

The default target is one working paper with paper-native appendices:

```text
Main paper
Appendix A — Definitions and system boundary
Appendix B — Program theory and the technology-relative reading of Naur
Appendix C — Constructive-witness protocols
Appendix D — Nearest existing constructions
Appendix E — Transition reachability and seed descent
References
```

Appendix D may instead become a separately paginated supplement if the complete
comparison makes the paper unwieldy. That supplement must be released with the
same paper version, source commit, and revision date; an independently mutable
web page is not an adequate substitute.

## Appendix A — Definitions and system boundary

### Required content

- software house;
- automated software house;
- external user and internal production role;
- declared product scope and operating horizon;
- natural-language, symbolic, and distributed-parametric state;
- program-theory function;
- learning by the house rather than ordinary product-state continuity;
- admissible input histories, realized history, and selection process;
- adequate state;
- practical reachability;
- hitting probability and continuation reliability.

### Mode

Paper adaptation. The source definitions are broader library artifacts; the
appendix should select only the meanings used by this paper and make their
relations explicit in one place.

### Gap

The live KB does not yet contain settled standalone definitions of practical
reachability, adequate state, hitting probability, or continuation reliability.
The workshop should formulate them in Appendix A and then decide which deserve
promotion back into atomic notes.

## Appendix B — Program theory and Naur

### Required argument

1. Naur's functional tests connect software to the activity it supports,
   justify its organization, and assimilate new demands coherently.
2. Extensive ordinary documentation failed to transfer enough of this capacity
   in the compiler case.
3. That case tested one historically bounded representation and consumption
   path; more prose of the same kind is not the answer, but linked rationale,
   indexing, retrieval, context assembly, and decision-point activation remain
   empirical alternatives.
4. Naur's human-only conclusion also relied on identifying machine judgment with
   execution of explicitly formulated criteria.
5. Trained recognizers and LLM interpretation reopen the bearer question without
   proving that current systems pass it.
6. Possession is tested longitudinally through theory-guided search, delayed
   contradiction, recovery, successor acquisition, and causal interventions.

### Mode

Provisional combination:

- B1 machine-execution bridge — exact snapshot unless compression materially
  improves the paper;
- B2 compiler-transfer bound — exact snapshot candidate;
- B3 longitudinal bearer test — paper adaptation from the longer note.

All three need direct citation to Naur's primary text. A snapshot may preserve
internal source links, but the paper cannot make the ingest report its only
source record.

## Appendix C — Constructive-witness protocols

### Carrier-neutral protocol

Start from the current seven-condition protocol in the nearest-constructions
supplement and complete:

- prospective declaration of the demand and consequence process;
- model, auxiliary parametric state, seed, and update machinery freeze;
- hidden-future-demand and no-post-hoc-removal rules;
- allowed user evidence versus internal production decisions;
- unstated-implication and withholding/replacement interventions;
- delayed contradiction and successor acquisition;
- learning in both localized forms across the sequence;
- retries, abstentions, timeouts, rollbacks, rescues, and human-intervention
  accounting;
- evidence for usable hitting probability;
- evidence for continuation reliability across the autonomous horizon.

### Explicit-theory mechanism protocol

Add the stronger intervention and baseline conditions:

- synthesize and retain an addressable rationale-bearing artifact;
- load it at the decisions where unstated implications matter;
- revise or retire it when later evidence defeats it;
- compare against raw records and direct artifact search with model, source
  evidence, demand sequence, and inference budget held fixed;
- distinguish a mediation trace from a load-bearing causal effect.

### Mode

Paper-native. This appendix defines what the paper asks future constructions to
demonstrate; it should not inherit its meaning from a changing comparison
article.

## Appendix D — Nearest existing constructions

### Required content

- evidence-basis vocabulary;
- software-house topology separated from automated continuation;
- fixed-parametric-state criterion;
- software learning and note learning;
- program-theory acquisition and successor acquisition;
- the nineteen-row comparison or its final reviewed successor;
- concise reading of the strongest neighboring clusters;
- the missing-conjunction result.

### Mode

Paper adaptation from the current supplement, or a versioned supplement released
as part of the same package.

### Gap

Before freeze, recheck every row affected by the stronger fixed-parametric-state
criterion and preserve the exact source or commit behind code-inspected
placements. The table is evidence about reviewed records, not a ranking or a
claim that no unreviewed construction exists.

## Appendix E — Transition reachability and seed descent

### Required content

- complete mutable state and pinned parameters;
- state-dependent successor relation covering gated and direct updates;
- transition closure from the seed over declared input histories;
- self-revision admitted by predecessor machinery;
- exogenous human transitions distinguished from warrant;
- Gödel-machine proof-gated transition relation versus fallible empirical
  relation;
- machine-state reachability distinguished from deductive closure of theorems;
- existential claim distinguished from nondeterminism;
- admissible histories, realized history, and distribution distinguished;
- hitting probability and continuation reliability;
- seed-exclusion and negligible-mass failure modes.

### Mode

Paper adaptation or exact snapshot of the corrected supplement after PR #179 is
reviewed. The appendix should be shorter than the supplement only when no
load-bearing distinction is lost.

## References

The paper should carry a conventional reference list and source locations for
material claims. At minimum:

- Peter Naur, *Programming as Theory Building*;
- Jürgen Schmidhuber, *Gödel Machines: Fully Self-Referential Optimal Universal
  Self-Improvers* or the exact cited edition/title;
- primary sources for every construction whose reported result bears load in
  Appendix D;
- Richard Sutton, *The Bitter Lesson*, for the narrow production-method claim.

Repository notes and ingests may appear as reproducibility and provenance links,
but external readers should be able to identify and inspect the primary sources
without traversing Commonplace.

## Assembly rules

- The paper body points first to the frozen appendix, not directly to the live
  note, when the appendix carries a load-bearing argument.
- Each appendix links onward to the live note or article and states that the live
  version may have changed.
- Live notes should eventually link back to the paper version and appendix that
  froze or adapted them.
- Exact snapshots are generated from the declared source commit and not
  hand-edited in staging.
- Paper adaptations are reviewed against every source they claim to preserve.
- No released paper is regenerated automatically when a live source changes.
- No `TODO`, unresolved placeholder, mutable workshop link, or link into
  `kb/work/` may remain in the public paper package.
