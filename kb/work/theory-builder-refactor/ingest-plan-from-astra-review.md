# Ingest plan from the Astra review

> **Status:** Workshop record, 2026-09-15. On this date the operator supplied
> a literature review produced by an external research assistant (Astra) of
> the workshop's reframing, and asked for an independent judgement and a list
> of papers to ingest. At that point none of the recommended sources had a
> snapshot or ingest in `kb/sources/`. The descriptions below preserve that
> review's unverified source claims as questions to check, not findings.
> Judgements are the session's own. The table now links the completed ingests.
> The 2026-09-17 [main-path review](./implementation-review.md) records which
> proposals the current drafts apply and which questions remain open.

## Verdict

The review's central move is right and should be adopted: the research
target is a broader and more reliable realization of an identifiable
historical program, not a category defined to exclude every earlier system.
Its four-part foundation (problem-solving methods for the ontology,
introspective multistrategy learning for the reflective mechanism, automated
science for the inquiry loop, belief maintenance plus adaptive evaluation for
retention and warrant) is a better base than classical theory refinement
alone, and the KB currently holds none of it. The main risk is scope: the
knowledge-engineering literature carries a designer-centric ontology whose
reuse assumption is the opposite of the conjecture, so the import should be
its distinctions and its record of what people still had to do, not its
process.

Three of the review's recommendations coincide with findings already in this
workshop, which raises confidence in both:

- Its request to remove the Gödel-machine exclusions and the closure claims
  from the definitions matches the [comparison file's](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
  own caution and the [special case's](../../notes/definitions/externally-tested-theory-builder.md#what-remains-for-the-general-case)
  finding that the closure worry is relative to the evidence interface.
- Its "connect theory revision to inquiry and observed consequences before
  adding more general definitions" is the evidence-interface point from the
  other side. The special case describes a passive interface, where bug
  reports arrive; the automated-science component adds an active one, where
  the builder chooses what to observe. The interface parameter should carry
  that distinction.
- Its diagnosis that the earlier theory-status draft mixed revisability,
  partial support, consumption permission, evaluator reliability, and
  objective preservation matches the README's
  [retention-policy review row](./README.md#definition-review-dispositions).
  The 2026-09-17 vocabulary change separates the borrowed term from the
  [policy draft](../../notes/a-claim-without-external-assessment-carries-three-obligations.md); substantive policy review remains.

## Judgements by section

**1. Introspective multistrategy learning.** Agreed that this is the closest
predecessor and the first ingest. Its loop (performance failure, explanation
of the reasoning failure, learning goal, constructed learning strategy) is
the operative form of what the [reflective definition](../../notes/definitions/reflective-theory-builder.md)
states abstractly: external work as a test of the machinery. Two things to
check on ingest matter more than the loop itself. First, the reported
ablation, that removing explicit learning goals impaired learning and that
arbitrary algorithm ordering could do worse than not learning, is the kind
of retained-content intervention the training article proposes, and would
be the earliest evidence that readable methodological content does causal
work. Second, Meta-AQUA assembled strategies from a supplied algorithm
library. By the workshop's [extension clause](../../notes/definitions/theory-builder.md#extension),
activating a retained component is not extension, so Meta-AQUA extends
nothing. That is either a correct verdict or a sign the clause is too
strict; it is a cheap test case for the extension review row.

**EURISKO and Lenat–Brown.** Agreed as the historical stress test. The
Lenat–Brown claim, that modifying a representation is productive in one
setting and unproductive in another, gives the conjecture the mechanism it
lacks for "why now": a language-model interpreter may reduce the
representation engineering that bounded earlier systems. That is testable as
a comparison of representation-engineering effort, and it is a stronger
statement than any in the current goal. One hypothesis to check on ingest:
EURISKO's reported successes were in areas with an external objective (the
Traveller fleet tournament) and its reported failure was learning new
heuristics, where a heuristic's worth is judged internally. If the record
supports that reading, it is a historical instance of the evidence-interface
finding. Caveat for the ingest: EURISKO's behaviour is known from Lenat's
reports, not from inspectable code, and the comparison supplement's
separation of code-inspected from reported evidence applies.

**2. Problem-solving methods.** Partly agreed. The distinctions are worth
importing now, because they turn "doctrine edits per new area" into three
countable kinds of change: domain knowledge acquired, a mapping constructed so
an existing method operates in the area, and a method created or changed. The
KB's own [system-definition artifact](../../notes/definitions/system-definition-artifact.md)
and [actionable methodology](../../notes/definitions/actionable-methodology.md)
definitions already sit near the task and inference layers, so the import is
a refinement rather than a new ontology. The competence-theory construction
paper is the priority: its three stages (competence specification,
conceptual refinement introducing vocabulary and assumptions, operational
specification) decompose what the [semantic-work record](../../reference/proposals/resource-bounded-ideal-interpreter.md)
currently asks the ideal interpreter to cover, and would let the interpreter
shrink to a faithful-interpretation contract. Not agreed: importing
CommonKADS's development process or its library assumption. The research
problem, stated in this vocabulary, is that the builder must do the
method-construction work these frameworks assign to designers.

**3. Automated science.** Agreed, and it is the most consequential gap for
Commonplace itself. The [interface investigation](../theory-refinement-interface/theory-refinement-interface.md)
already reports that the routine review loop compares text against reviewer
criteria and that empirical comparison does not pass through the same
machinery. The theorist, experimentalist, and experiment-runner separation
names the missing role: deciding which observation, intervention, or
computation would discriminate between current alternatives. The obligation
to state what uncertainty an inquiry addresses and what its outcome would
establish transfers directly to workshop practice.

**4. Belief maintenance and adaptive evaluation.** Agreed on all points,
with one ranking change: the adaptive data analysis result is the most
important of the four, not the last. The earlier clause, now a question in the
[retention-policy draft](../../notes/a-claim-without-external-assessment-carries-three-obligations.md), that warranted revisions chain, and the review system's reuse of the same
criteria and evaluators across revisions, are the adaptivity problem
exactly. Warrant for a revision sequence has to be established under an
evaluation protocol; a succession of local approvals does not supply it. On
belief bases: a finite collection of retained notes and commitments is a
belief base, not a deductively closed belief state, so Hansson's account is
the right starting abstraction and the original AGM paper is a citation
rather than a working tool. On assumption-based truth maintenance: the
[Commonplace store](../../reference/freshness-architecture.md) already tracks
dependencies at the file level; the import would be dependency tracking at
the claim and assumption level, which is also what corrects the draft's
per-claim atomism, since evidence can support a conjunction without
identifying which conjunct to revise.

**5. Bounded extension.** Agreed that the artifact-diff criterion should go;
the README already records its inconsistency with learning in weights. The
review's replacement measure, whether retaining a change makes later theory
building more capable or cheaper, is already the research question stated in
the [theory-builder draft](../../notes/definitions/theory-builder.md#extension). The change is to
make it the definition of extension rather than a question asked about
diff-defined extensions. Bounded optimality supplies the framing; DreamCoder
is already ingested twice and needs no new work.

**6. Contemporary alternatives.** Agreed that "no methodology" is a misnamed
rival. The right control is the same interpreter under a generic instruction
("investigate the problem and invent whatever methods are needed"), which
separates the interpreter's competence from the retained methodology's
contribution. GEPA is cited in eight existing ingests without a dedicated
one; ADAS has none; the Darwin Gödel Machine is ingested. The review's
warning stands: some of these systems' retained natural-language reflections
may already qualify as theories under a broad definition, so the difference
must be shown in what the content does across areas and over long sequences.

**7. The conjecture.** Agreed on all three changes, recorded here as
proposals for the operator rather than applied:

- Split the conjecture into a sufficiency hypothesis (the methodology
  acquires what successive areas need without fresh human methodological
  design) and a comparative hypothesis (retaining and revising it beats
  alternatives at comparable total cost). Partial results then stay
  informative.
- Demote the doctrine-edit count from the conjecture's empirical content to
  one diagnostic, conditioned on demonstrated competence, completion,
  reliability, and resource use, and recording substantive authorship. The
  zero-edit generic instruction is a decisive counterexample to the count as
  it stands.
- Remove the Gödel-machine exclusions and the objective-closure claims from
  the definitions, and stop the autonomy draft from settling by stipulation
  whether an operational objective change needs a person.

## Papers to ingest

Priority 1 is needed before the definitions review; 2 before the conjecture
is restated; 3 supports closing condition 3 and the experiment design. Each
row names the question the ingest must answer for this workshop, which is
what the ingest report should lead with. Access notes are for the snapshot
step; where the canonical source is a book, a paper surrogate is named.

| # | Source | Question the ingest must answer | Lands in | Ingest status |
|---|---|---|---|---|
| 1 | Cox, M. T. and Ram, A. (1999). Introspective multistrategy learning: on the construction of learning strategies. *Artificial Intelligence* 112. | What the failure-to-strategy loop requires of the self-representation; what the learning-goal ablation showed and under what conditions; whether the strategy library is fixed or extensible. | Reflective definition; extension review row; retained-content intervention design. | [Complete](../../sources/introspective-multistrategy-learning.ingest.md) |
| 1 | Lenat, D. B. and Brown, J. S. (1984). Why AM and EURISKO appear to work. *Artificial Intelligence* 23. | The representation-productivity claim in its own terms; why learning new heuristics was harder than adding heuristics as a subject; what people intervened to do. | Goal ("why now" mechanism); evidence-interface hypothesis. | [Complete](../../sources/why-am-and-eurisko-appear-to-work.ingest.md) |
| 1 | Lenat, D. B. (1983). EURISKO: a program that learns new heuristics and domain concepts. *Artificial Intelligence* 21. | Which areas had an external objective and which did not; the reported self-modification failures and credit-assignment pathologies; the human interventions and their consequences. | Boundary cases in all definitions; special-case file. | [Complete](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md) |
| 1 | Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., and Roth, A. (2015). Generalization in adaptive data analysis and holdout reuse. *NeurIPS 2015* (arXiv 1506.02629). | Why a sequence of evaluations that each guides the next revision invalidates ordinary generalization arguments; what protocols restore it; what this implies for reusing review criteria across revisions. | Retention-policy obligation 3; review-system design; warrant of revision sequences. | [Complete](../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md) |
| 2 | Wielinga, B., Akkermans, H., and Schreiber, G. (1998). A competence theory approach to problem-solving method construction. *International Journal of Human-Computer Studies* 49. | The three construction stages and the commitments each exposes; which stages the framework leaves to the designer. | Semantic-work record; ideal-interpreter scope row; "specify first" route. | [Complete](../../sources/competence-theory-problem-solving-method-construction.ingest.md) |
| 2 | Studer, R., Benjamins, V. R., and Fensel, D. (1998). Knowledge engineering: principles and methods. *Data & Knowledge Engineering* 25. Surrogate for the CommonKADS book. | The domain, inference, and task knowledge layers; the problem-solving method as a reusable unit and its applicability assumptions; the reuse assumption's dependence on human construction. | Doctrine-edit measure (three kinds of change); actionable-methodology definition. | [Complete](../../sources/knowledge-engineering-principles-and-methods.ingest.md) |
| 2 | Fensel, D., Benjamins, V. R., Motta, E., and Wielinga, B. (1999). UPML: a framework for knowledge system reuse. *IJCAI 1999*. Surrogate for "The component model of UPML in a nutshell". | Tasks, methods, domain models, ontologies, adapters; what bridges and refiners make explicit; how far configuration was automated. | Doctrine-edit measure; extension as adapter versus method change. | [Complete](../../sources/upml-framework-for-knowledge-system-reuse.ingest.md) |
| 2 | Musslick, S. et al. (2024). AutoRA: automated research assistant for closed-loop empirical research. *Journal of Open Source Software* 9(104). | The theorist, experimentalist, and runner roles and their shared state; what users supply; what the framework does not invent. | Evidence interface (active versus passive); interface investigation gap; builder roles. | [Complete](../../sources/autora-automated-research-assistant.ingest.md) |
| 2 | Agrawal, L. A. et al. (2025). GEPA: reflective prompt evolution can outperform reinforcement learning. arXiv 2507.19457. | What the natural-language reflection retains and whether it functions as a theory under the workshop's definition; what the comparison with scalar-reward search established. | Rival hypothesis; generic-instruction control design. | [Complete](../../sources/gepa-reflective-prompt-evolution.ingest.md) |
| 2 | Hu, S., Lu, C., and Clune, J. (2024). Automated design of agentic systems. arXiv 2408.08435 (ICLR 2025). | How the meta-agent's archive is consumed; whether discovered agents transfer across domains; where people intervene. | Extension by procedure acquisition; contemporary comparison set. | [Complete](../../sources/automated-design-of-agentic-systems.ingest.md) |
| 3 | Hansson, S. O. (1992). In defense of base contraction. *Synthese* 91(3):239–245 ([publisher record](https://link.springer.com/article/10.1007/BF00413568)). | The belief-base versus belief-state distinction and its advantages for repeated change; what a base needs to record. | Theory-retention policy; closing condition 3. | [Complete](../../sources/in-defense-of-base-contraction.ingest.md) |
| 3 | Alchourrón, C. E., Gärdenfors, P., and Makinson, D. (1985). On the logic of theory change: partial meet contraction and revision functions. *Journal of Symbolic Logic* 50. | The postulates as a citation for what contraction and revision are; explicitly what they do not supply (discovery, empirical reliability). | Closing condition 3, citation only. | [Complete](../../sources/logic-of-theory-change-partial-meet-contraction.ingest.md) |
| 3 | de Kleer, J. (1986). An assumption-based TMS. *Artificial Intelligence* 28. | Maintaining conclusions relative to assumption sets and recording dependencies; what it does not establish. | Claim-level dependency record; per-claim warrant atomism. | [Complete](../../sources/an-assumption-based-tms.ingest.md) |
| 3 | Russell, S. J. and Subramanian, D. (1995). Provably bounded-optimal agents. *JAIR* 2. | Evaluating a program relative to architecture and environment rather than an ideal reasoner; which classes the results cover. | Resource-bounded framing; interpreter fidelity and coverage. | [Complete](../../sources/provably-bounded-optimal-agents.ingest.md) |
| 3 | A formal learning theory survey (candidate: the Stanford Encyclopedia of Philosophy entry "Formal learning theory"). | Convergence guarantees versus current warrant, the distinction the README's source checks require. | Closing condition 3. | [Complete](../../sources/formal-learning-theory.ingest.md) |

Already ingested and not repeated: EITHER
([ingest](../../sources/theory-refinement-analytical-empirical-methods.ingest.md)),
FORTE ([ingest](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md)),
the Mooney–Shavlik recap
([ingest](../../sources/recap-early-work-theory-knowledge-refinement.ingest.md)),
DreamCoder (two ingests), the Darwin Gödel Machine, and the Gödel machine
paper.

## Ingest execution — 2026-09-17

All fifteen sources have full-text ingests, drafted by fresh Sol
agents after source capture and connection discovery. The table links each
report. All three priority groups are complete; the definitions review is
the next workshop step. Each report records its
row's question as its occasion and recommends one follow-up action.

**Hansson capture:** The operator supplied the full seven-page PDF after
the web download attempts returned access pages. Its identity and complete
page range, 239–245, were verified before capture. The
[publisher record](https://link.springer.com/article/10.1007/BF00413568)
identifies it as *Synthese* 91(3):239–245, not *Philosophical Studies* 65;
the table's citation is corrected. The full-text access blocker is resolved.

**Versions and validation:** Lenat–Brown uses the full 26-page 1984 journal
article, not its shorter 1983 conference predecessor. GEPA uses arXiv v2
(2026-02-14), ADAS v2 (2025-03-02), and the adaptive-data-analysis paper v2
(2015-09-25). All ingest reports pass validation without failures or warnings;
checks also verify source checksums, capture metadata, the exact occasion,
and the required Quotes section. The snapshots have no validation failures.
Three preserve capture warnings: one apparent link in Dwork's extracted
text, five apparent links in ADAS's extracted code, and 27 warnings in the
SEP capture (relative web links and its capture-time genre).

## Additional seed-learning sources — 2026-09-17

After a search for better definitions of seed improvers, the operator asked
to ingest these two papers and add them to this workshop. They supplement
the fifteen-source Astra list. Both full-text ingests were drafted by fresh
Sol workers; their reports and snapshots passed validation with no failures
or warnings. Neither ingest has a task-specific occasion. The questions
below route their use in the workshop; they do not alter the ingest analyses
or settle the proposed definitions.

| Source and completed ingest | Question for the definitions review | Lands in |
|---|---|---|
| Thórisson (2020), [Seed-Programmed Autonomous General Learning (snapshot required)](../../sources/seed-programmed-autonomous-general-learning.ingest.md) | Which initial knowledge, observables, drives, and learning operations does the seed supply? How does the requirement for overlap between novel phenomena and existing knowledge limit the claim of autonomous generality? What supports cumulative knowledge revision, and what would additionally establish extension of the learning machinery? | Seed in the theory-builder definition; cross-area methodology conjecture; evidence-interface and extension review. |
| Nivel et al. (2013), [Bounded Recursive Self-Improvement (snapshot required)](../../sources/bounded-recursive-self-improvement.ingest.md) | Which executable models can AERA learn or replace, and which architectural and motivational parts remain protected? What do the dialogue experiments establish about later behavior, and what remains untested about improvement of the learning process itself? | Reflective and autonomous boundary cases; extension review; comparison with Gödel-machine rewrite governance. |

The ingests identify a useful predecessor for learning from a supplied seed,
but bound its demonstrated achievements to model acquisition and use inside
a designer-supplied architecture. Use that distinction when assessing the
workshop's stronger claim that its methodology can acquire and revise the
machinery new areas require. Neither ingest establishes sustained recursive
compounding or the workshop's comparative reliability claim.

## Order of work

1. Ingest the four priority-1 sources. They decide whether the reflective
   mechanism has a developed predecessor, whether the "why now" mechanism can
   be stated, and what warrants a sequence under retention-policy obligation 3.
2. Run the definitions review in the README with those ingests in hand,
   applying the review's three conjecture proposals if the operator accepts
   them.
3. Ingest the priority-2 sources before restating the conjecture, so the
   doctrine-edit measure is stated in the three-kinds-of-change vocabulary
   and the rivals are named against GEPA, ADAS, and the DGM.
4. Priority 3 as closing condition 3 requires.
