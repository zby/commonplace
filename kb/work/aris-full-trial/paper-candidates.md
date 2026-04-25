# Paper Candidates

## Candidate 1: Bounded-Context Orchestration

Working title:

> Bounded-Context Orchestration: A Computational Model of LLM Agent Workflows

Paper type:

- theory / position paper
- possible workshop paper
- maybe later full paper if the formal model and evidence mature

Core claim:

LLM agent systems are best modeled as symbolic schedulers over bounded stochastic calls. Practical techniques such as subagents, progressive disclosure, frontloading, decomposition, and verifier stages are scheduling strategies under context constraints.

Why it is attractive:

- Existing workshop material is already paper-shaped.
- The claim is high-reach.
- It could become a strong theoretical contribution if formalized well.

Why it is risky:

- We do not want to publish the idea to GitHub too early.
- The strongest version needs careful formalization and positioning.
- ARIS may generate lots of draft surface area that should stay private.

Use ARIS for:

- private literature field map,
- idea refinement,
- adversarial review,
- paper outline and draft generation,
- claim audit before any public release.

Recommendation:

Keep as a private ARIS trial candidate, not the first public-facing output.

## Candidate 2: Practical Agent Memory Systems Review

Working title:

> Practical Agent Memory Systems: A Systematization of Substrates, Lifecycles, and Evaluation Gaps

Paper type:

- survey paper,
- systematic mapping study,
- systematization of knowledge,
- taxonomy paper.

The best label is probably **SoK / systematization of knowledge** if we emphasize code-grounded analysis and a taxonomy over practical systems. In venues that do not use "SoK", call it a **survey and taxonomy of practical agent memory systems**.

Core claim:

Existing agent-memory systems solve extraction and retrieval more concretely than they solve maintenance. Across practical implementations, the hard unsolved layer is lifecycle: contradiction, supersession, promotion, staleness, failure memory, and evaluation of what deserves to become durable memory.

Why it is attractive:

- We already have many code-grounded system reviews in `kb/agent-memory-systems/reviews/`.
- The material is less strategically sensitive than the bounded-context model.
- The paper can be empirical/descriptive without needing a new algorithm.
- It fits ARIS well because Research Wiki can track systems, claims, gaps, and contradictions.

Possible contribution shape:

1. Corpus: open-source/practitioner agent-memory systems reviewed from code and docs.
2. Taxonomy: trace source, extraction method, storage substrate, retrieval/activation, promotion target, lifecycle maintenance, evaluation oracle.
3. Finding: extraction is implemented; maintenance and evaluation are mostly missing or aspirational.
4. Design implications: memory systems should expose lifecycle state, failure memory, promotion criteria, and verifier-backed maintenance loops.

Risks:

- Need a clean inclusion criterion for systems.
- Need to avoid overclaiming from a convenience sample.
- Need to decide whether GitHub repos, product docs, and papers count together or as separate strata.
- Need to update reviews and make the corpus reproducible enough for publication.

Use ARIS for:

- building the review corpus field map,
- tracking claims and contradictions across systems,
- generating failed-taxonomy/alternative-taxonomy records,
- drafting a paper outline,
- running external review against the taxonomy.

Recommendation:

Best first full-ARIS trial.

## Candidate 3: Lifecycle Management for Agent-Operated Knowledge Bases

Working title:

> From Sources to Durable Claims: Lifecycle Management for Agent-Operated Knowledge Bases

Paper type:

- design study,
- experience report,
- systems methodology paper.

Core claim:

Agent-operated KBs need an explicit lifecycle layer between source intake and durable notes: candidates, failed ideas, active claims, experiments, gaps, promotion, retirement, and reactivation triggers.

Why it is attractive:

- It directly uses the ARIS trial as evidence.
- It connects commonplace's workshop layer with Research Wiki.
- It could become a practical methodology paper.

Risks:

- Evidence may be too self-referential unless we run enough real workflows.
- It may be better as a later paper after the ARIS trial produces data.

Recommendation:

Keep as the "lessons learned" paper after the first trial, not the first trial target.

## Suggested Parallel Trial

Run two private ARIS roots in parallel:

1. `bounded-context-paper/` as the sensitive high-upside theory candidate.
2. `agent-memory-review-paper/` as the lower-risk survey/SoK candidate.

Use the same ARIS workflow on both for a short first pass:

- initialize research wiki,
- write a brief,
- add initial sources/systems,
- generate/refine candidate paper claims,
- compare whether ARIS creates useful state or just overhead.

Then choose one for a deeper paper-writing run.
