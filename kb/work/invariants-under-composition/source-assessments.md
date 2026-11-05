# Source assessments

Primary-source reading and proposed transfers are recorded separately. URLs are reading locators, not tracked ingests; library promotion requires the normal source workflow.

## Abadi and Lamport: Conjoining Specifications (1995)

Read: [primary paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/Conjoining-Specifications.pdf), §§1–2.2 (brainstormer), circularity discussion §4.3.1 (parent). Reusable component guarantees depend on environment assumptions; naively circular promise matching is not generally a sound rule. Temporal conditions distinguish preserving a property from eventual progress and prevent later assumption failure from excusing earlier guarantee failure.

Role: ask who establishes an assumption at the time it is needed. Transfer: review evidence about captured bytes does not alone authorize a later baseline transition. We have not applied or verified the paper's formal composition theorem for Commonplace.

The [authors' 1993 retrospective](https://www.microsoft.com/en-us/research/publication/composing-specifications/) identifies the 1995 treatment as superseding its earlier approach. Do not make the older implication-only account the workshop's proof rule.

## Hayes, Jones and Colvin: Laws and semantics for rely-guarantee refinement (2014)

Brainstormer read abstract, §5 opening and Laws 5.1–5.2, §8 opening and Lemma 8.1 in the [full author report](https://eprints.ncl.ac.uk/fulltext.aspx?pub_id=205931&url=205931/30C3C5FD-22C9-4A30-BF20-C0302564FAA6.pdf), located through [Newcastle's record](https://eprints.ncl.ac.uk/205931). Rely conditions constrain environment steps; component guarantees must respect the other components' relies. Shared-variable evaluation needs an account of intervening changes.

Role: expose the interval between checking a condition and using it. The publication trace is our constructed transfer; no formal rely/guarantee proof of Commonplace is claimed. Keep the test, not a parallel vocabulary.

## Ames et al.: Control Barrier Function Based Quadratic Programs (2017)

Brainstormer read abstract, introduction through §I.B, and §II opening through equations (1)–(5), pp. 1–3 of the [author manuscript](https://arxiv.org/pdf/1609.06408). Distinguishes stabilization objectives from preservation of an admissible set by forward invariance.

Role: discriminate stability from the particular requirement's preservation. Our affine counterexample is independently constructed and calculated; no continuous-control barrier theorem is applied to prompts.

## Jiang, Teel and Praly: Small-gain theorem for ISS systems and applications (1994)

Read by brainstormer: notation pp. 96–97; Definition 2.2, Remark 1 p. 98; equations (13)–(17), Theorem 2.1, Remark 2 pp. 99–100; Corollary 2.2 p. 101 in the [primary paper](https://web.ece.ucsb.edu/~teel/ECE236/jiang-teel-praly-1994). Parent checked the abstract. Results concern specified dynamic interconnections and gain conditions, not generic weak coupling.

Disposition: parked. A future transfer must supply states, time semantics, gains and assumptions, then connect its bound to the requirement. No current KB case needs this machinery. Chaos/catastrophe leads remain unassessed; do not describe ordinary threshold crossing as either phenomenon.

## Reynolds: Separation Logic (2002)

Brainstormer read abstract/introduction and frame-rule discussion with soundness argument, PDF pp. 6–7 of the [author paper](https://www.cs.cmu.edu/~jcr/seplogic.pdf). Separation of storage, plus the variable-modification condition, matters to preservation; syntactically different names can alias the same storage.

Role: inspect mutation routes before treating a dependency boundary as independent. The renderer example is our transfer. We do not use the frame rule as a theorem about natural-language clauses or claim that a Markdown graph establishes disjoint state.

## Clarkson and Schneider: Hyperproperties (2010)

Brainstormer read abstract/introduction opening, §2 information-flow discussion around equations 2.4–2.6 (printed pp. 1163–1164), §3 opening (pp. 1167–1168), and §4 paired-execution discussion (pp. 1169–1171) in the [author paper](https://www.cs.cornell.edu/fbs/publications/Hyperproperties.pdf). Requirements about sets of executions cannot in general be reduced to checks on each trace independently; observational determinism compares public observations across suitable initial states.

Role: require a comparison across runs for the held-out confidential-bit case. The report-ordering pipeline is our construction. Keep the observation obligation, not a general hyperproperty calculus or a claim of confidentiality for stochastic LLMs.

## Parked leads and their admission tests

- Small-gain machinery: reopen only with a specific feedback problem, defined states, units/time semantics and justified gain bounds, plus a link from those bounds to the requirement.
- [Lorenz, Deterministic Nonperiodic Flow](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2) and [Zeeman, Catastrophe Theory](https://imechanica.egr.uh.edu/sites/default/files/1976%20zeeman%20catastrophe%20theory.pdf): original unassessed leads. Reopen only if sensitive dependence or bifurcation explains a worked case that the simpler arguments do not. Ordinary threshold crossing is insufficient.
- [Benveniste et al., Contracts for System Design](https://research-explorer.ista.ac.at/record/5677): unassessed lead. Reopen for a concrete compatibility or replacement obligation not resolved by the current examples. No broad survey is required by this workshop.

The role of the dynamics reading is a limit on inference, not a proposed implementation. The term hyperproperty stays in this reading record; the main account asks directly which runs and observations must be compared.
