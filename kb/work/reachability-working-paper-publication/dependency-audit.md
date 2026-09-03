# Reachability working-paper dependency audit

## Test

Read the candidate paper as if its hyperlinks were unavailable. For each
linked artifact, ask whether a technically competent critic needs its contents
to understand or assess a central definition, premise, derivation, protocol,
qualification, or evidence claim.

- **Package** means the necessary content must appear in the main body or a
  versioned appendix.
- **Summarize and link** means the body carries the load-bearing result and the
  live artifact supplies fuller derivation or later development.
- **Live link only** means the paper remains assessable without the artifact.
- **Primary reference** means the paper should cite the external source
  conventionally; the Commonplace ingest remains optional provenance.

The current dispositions are staging decisions, not publication approval.

## Current `source_notes` cohort

| Source | Role in the paper | Initial disposition | Reason / required paper content |
|---|---|---|---|
| `kb/notes/definitions/software-house.md` | load-bearing definition and boundary | package in Appendix A | the paper's target and distinction between automated and people-in-internal-roles cannot be judged without the complete persistent producer, external-user, internal-role, scope, and horizon boundaries |
| `kb/notes/definitions/representational-form.md` | load-bearing fixed/mutable-state distinction | package in Appendix A | the conjecture depends on distributed-parametric state staying fixed while natural-language and symbolic state can learn; only the needed form carve should be adapted |
| `kb/notes/program-theory-sustains-search-under-delayed-feedback.md` | load-bearing bearer argument and causal test | summarize in body; adapt in Appendix B and C | the paper must carry theory-guided search, delayed contradiction, recovery, and withholding or wrong-theory interventions without requiring a click |
| `kb/notes/naur-equates-machine-execution-with-formulated-criteria.md` | load-bearing reopening of Naur's human-only conclusion | package in Appendix B, snapshot or adaptation | the paper's theoretical possibility claim depends on separating formal execution from explicitly formulated criteria |
| `kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md` | material evidence boundary | package in Appendix B, snapshot candidate | the paper must preserve both sides: ordinary extensive documentation failed, while newer representation and consumption paths were not tested |
| `kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md` | mechanism premise for admission and credit assignment | summarize and link | the main body already states the required selection, validation, authorization, and coordination; the general continual-learning ontology need not be copied wholesale |
| `kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md` | material scaling qualification | summarize and link; keep fuller treatment outside this paper | the reachability paper needs the outgrowth condition and failure implication, while the dedicated Bitter Lesson paper owns the full argument |
| `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md` | conceptual defense of learned localized state | summarize and link | the body must state production method versus representational form; the quadrant analysis and broader literature remain separate |
| `kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md` | stronger payoff and explicit-theory experiment | live link only after the body states the bounded hypothesis | sample efficiency is not required for the reachability conjecture; only the optional prediction and its costs belong in the paper |
| `kb/notes/opacity-is-a-scale-threshold.md` | caveat to legibility | live link only after one body sentence | the paper already disclaims transparency; the full opacity argument is not needed to assess reachability |
| `kb/notes/axes-of-artifact-analysis.md` | implementation and comparison ontology | summarize and link or omit from frozen package | useful for the research program's machinery map, but not necessary if the paper directly defines the mutable surfaces and causal consumption requirement |
| `kb/notes/code-complements-weight-prompt-with-symbolic-operations.md` | implementation rationale for symbolic state | live link only | the main paper's core claim does not depend on the full weight–prompt versus runtime derivation |
| `kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` | implementation rationale for symbolic bookkeeping | live link only | a useful design argument, not a necessary premise of existential reachability |
| `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | formal comparison | summarize in body and Appendix E; cite primary source | the paper needs the proof-gated contrast and its limits, not the complete note's wider comparison portfolio |
| `kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md` | optional extension | live link only | the main paper explicitly does not depend on this separate conjecture |
| `kb/sources/programming-as-theory-building.ingest.md` | source analysis and quote locations | primary reference; provenance link optional | Appendix B and the paper bibliography should cite Naur directly with page or section locations |
| `kb/sources/goedel-machines-schmidhuber.ingest.md` | source analysis and quote locations | primary reference; provenance link optional | Appendix E and the paper bibliography should cite Schmidhuber directly rather than relying on the ingest as the scholarly endpoint |

## Article and supplement dependencies outside `source_notes`

| Source | Role | Initial disposition | Remaining decision |
|---|---|---|---|
| `kb/articles/nearest-existing-constructions-to-a-reachability-witness.md` | evidence map and full protocols | package as Appendix D or versioned supplement; protocol core becomes Appendix C | decide whether one-document length remains manageable and freeze every system placement against its evidence basis |
| `kb/articles/reachability-as-closure-under-the-seed-gate.md` | transition-reachability derivation | package as Appendix E; correction merged as 465de048 | confirm the corrected successor-relation treatment and settle probability evidence in Appendix C |
| `kb/articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md` | separate companion argument | cite as separate live or versioned paper, not appendix | decide whether it is promoted alongside the reachability paper or remains a draft dependency with the main paper carrying its own minimal qualification |
| `kb/articles/the-decisions-that-stay-human-and-what-would-move-them.md` | separate boundary and transfer argument | optional companion link | the reachability paper already carries the internal-role boundary needed for its claim |

## Main-body completeness checklist

The main body, without following links, must let a reader state:

1. the exact fixed-parametric-state reachability conjecture and its declared
   scope, horizon, input process, and budget;
2. what a software house and an automated software house include and exclude;
3. why open-ended coherent modification is argued to require a
   program theory as a capacity;
4. why Naur's human-only inference and documentation evidence do not settle the
   current computational question in advance;
5. how fixed models, natural-language state, and symbolic state divide the
   work;
6. what counts as learning by the house rather than ordinary product
   continuity;
7. the four witness obligations and that they do not fix which form carries
   the theory;
8. why explicit retained theory is a stronger mechanism hypothesis with raw
   records or direct artifact search as baselines;
9. what the nearest-constructions review establishes and what it does not;
10. why practical usefulness, automated continuation, and scaling in the way the
    Bitter Lesson favours remain separate achievements.

## Appendix-closure rule

An appendix may link to a live note for later developments without importing
that note's full dependency graph. The appendix must carry every proposition
needed for its own paper function. Links from a frozen appendix to optional
examples, supporting derivations, or newer evidence remain navigation, not
historical authority.

A dependency is not discharged merely because the paper lists it in
`source_notes`. Discharge requires the main body or frozen appendix to state the
needed content at the scope and confidence the paper uses.
