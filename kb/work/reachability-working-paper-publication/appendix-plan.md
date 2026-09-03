# Reachability working-paper appendix plan

## Package shape

The target is one short working paper with three short appendices and two
separately paginated supplements:

```text
Main paper
Appendix A — Definitions and system boundary (short, paper adaptation)
Appendix B — Program theory and Naur (compressed adaptation)
Appendix C — Witness protocol (paper-native, canonical)
References
Supplement D — Nearest existing constructions (versioned)
Supplement E — Transition reachability and seed descent (versioned)
```

The appendices stay short so that the paper does not read as an export of the
knowledge base. The supplements carry the long material. Each supplement is
released with the same paper version, source tag, and revision date; an
independently mutable web page is not an adequate substitute.

## Appendix A — Definitions and system boundary

### Required content

- software house;
- automated software house;
- external user and internal production role;
- declared product scope and operating horizon;
- natural-language, symbolic, and distributed-parametric state;
- program theory as a capacity, whether written down or reconstructed from records;
- learning by the house rather than ordinary product-state continuity;
- admissible input histories, realized history, and selection process;
- adequate state;
- practical reachability;
- hitting probability and continuation reliability.

### Vocabulary

The paper uses the main article's vocabulary as simplified on 2026-09-03: the
house, internal role, notes and code, budget, declared horizon, learning step,
and plain glosses for eligible, witness, and the explicit-theory hypothesis.
Defined KB terms keep their names: software house, internal production role
(the definition's term for internal role), natural-language, symbolic, and
distributed-parametric state. Carrier-neutral survives only as the glossed
label for the broad obligations in the comparison article; the paper body says
that the obligations do not fix which form carries the theory.

### Mode

Paper adaptation, kept short. The source definitions are broader library
artifacts; the appendix should select only the meanings used by this paper and
make their relations explicit in one place.

### Gap

The live KB does not yet contain settled standalone definitions of practical
reachability, adequate state, hitting probability, or continuation reliability.
The workshop formulates them in Appendix A. They are specific to this paper and
are not promoted to standalone definition notes.

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
6. Possession is tested over many changes through theory-guided search, delayed
   contradiction, recovery, successor acquisition, and causal interventions.

### Mode

Compressed paper adaptation. The appendix carries the two distinctions the paper
depends on and no more:

- B1 formal execution versus explicitly formulated criteria;
- B2 what the compiler case rules out versus what it leaves open;
- B3 the bearer test's predictions, only as far as Appendix C uses them.

All three cite Naur's primary text directly. The full notes remain live links;
the paper cannot make the ingest report its only source record.

## Appendix C — Constructive-witness protocols

### Broad protocol

Start from the current seven-condition protocol in the nearest-constructions
supplement and complete:

- declaration, in advance, of the demand and consequence process;
- model, auxiliary parametric state, seed, and update machinery freeze;
- hidden-future-demand and no-post-hoc-removal rules;
- allowed user evidence versus internal production decisions;
- unstated-implication and withholding/replacement interventions;
- delayed contradiction and successor acquisition;
- learning in both forms, notes and code, across the sequence;
- retries, abstentions, timeouts, rollbacks, rescues, and human-intervention
  accounting;
- evidence for usable hitting probability;
- evidence for continuation reliability across the declared horizon.

### Explicit-theory mechanism protocol

Add the stronger intervention and baseline conditions:

- synthesize and retain a rationale-bearing artifact that can be found and revised on its own;
- load it at the decisions where unstated implications matter;
- revise or retire it when later evidence defeats it;
- compare against raw records and direct artifact search with model, source
  evidence, demand sequence, and inference budget held fixed;
- distinguish a mediation trace from a load-bearing causal effect.

### Mode

Paper-native and canonical. This appendix is the one full statement of the
witness conditions in the package. The main paper's four obligations are its
summary and point to it. Supplement D's protocol section becomes a pointer to
this appendix instead of a restatement, so the conditions exist in one place and
cannot drift across the package. The appendix does not inherit its meaning from
a changing comparison article.

## Supplement D — Nearest existing constructions

### Required content

- evidence-basis vocabulary;
- software-house boundary separated from automated continuation;
- fixed-parametric-state criterion;
- software learning and note learning;
- program-theory acquisition and successor acquisition;
- the nineteen-row comparison or its final reviewed successor;
- concise reading of the strongest neighboring clusters;
- the missing-conjunction result.

### Mode

Versioned supplement, separately paginated and released with the paper. Its
protocol section points to Appendix C rather than restating the conditions.

### Gap

Before freeze, recheck every row affected by the stronger fixed-parametric-state
criterion and preserve the exact source or commit behind code-inspected
placements. The table is evidence about reviewed records, not a ranking or a
claim that no unreviewed construction exists.

## Supplement E — Transition reachability and seed descent

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

Versioned supplement: an exact snapshot of the corrected article. The
correction (PR #179) merged on main as commit 465de048. Shorten it only when no
load-bearing distinction is lost, and then call it an adaptation.

## References

The paper should carry a conventional reference list and source locations for
material claims. At minimum:

- Peter Naur, *Programming as Theory Building*;
- Jürgen Schmidhuber, *Gödel Machines: Fully Self-Referential Optimal Universal
  Self-Improvers* or the exact cited edition/title;
- primary sources for every construction whose reported result bears load in
  Supplement D;
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
- The freeze is one annotated git tag on the source commit. Every appendix and
  supplement cites that tag.
- Exact snapshots are generated from the tagged source and not hand-edited in
  staging.
- Paper adaptations are reviewed against every source they claim to preserve.
- No released paper is regenerated automatically when a live source changes.
- No `TODO`, unresolved placeholder, mutable workshop link, or link into
  `kb/work/` may remain in the public paper package.
