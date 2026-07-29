# Automation-boundary retrospective: how this theory was found

The generator theory in this workshop was produced by a human–agent process worth examining with the same discipline as the experiments themselves: linking is core technology in this KB, so the search was reflective — the system theorizing about its own connective tissue — and the episode is a worked case of a **theory search with explanatory reach as the goal**. This file separates what the process record shows from interpretation, and asks what could be automated versus what still required human input.

## The arc (established record)

1. A cross-collection audit found contradictions among linking contracts, shared vocabulary, and procedures (the [consistency workshop](../linking-contract-consistency/README.md)'s trigger).
2. Reconciliation ran through four label reviews (evidence, rationale, grounds, mechanism). Each adjudication needed principles that did not exist; the mechanism review made that unavoidable, and this workshop opened.
3. The maintainer identified the missing piece: the inherited Ars Contexta theory justified *having* typed links but was not **generative** — it could not produce the vocabulary appropriate to a given collection, a limitation known since the vocabulary failed for the reference collection (repaired by ADR 019).
4. The brainstorm produced competing models and the seed-then-harvest generator sketch; six experiments (three retrodiction variants, an A/B, two corpus checks plus a control) tested it in one day, recorded in the [retrodiction run](./generator-retrodiction-run.md).

The episode maps onto the [discovery lifecycle](../../notes/definitions/discovery-lifecycle.md) almost stage for stage: observe (contradictions, migration data) → conjecture (competing models) → derive consequences (retrodiction predictions) → test (variants, A/B, corpus checks, discrimination control) → accept/integrate (still pending: the handoffs in the run file's Next section).

## Division of labor observed

**Done by agents, effectively automatically** (the maintainer's inputs were one-line "run it" messages, each selecting an item the agent had already proposed):

- synthesizing ~700 classified edges and four ADRs into the repeated observations;
- generating the competing models and the generator sketch;
- designing and executing every experiment: blind protocols, deterministic leak checks, control arms, scoring rubrics, k-sampling;
- **self-refutation**: the A/B killed the agent's own revision-consequence hypothesis; the portfolio finding corrected the agent's own "three tries, three families" narrative — error-correction inside the loop needed no human push;
- forward prediction (the three gap candidates) and the discrimination control that validated the forward mode.

**Required the human**, on the evidence of this session:

- the original noticing that contradictions pointed at a missing theory rather than at more reconciliation;
- **supplying the load-bearing historical fact** — that the Ars Contexta inheritance was central and non-generative — and its emphasis, via one corrective message after the first brainstorm draft underweighted it;
- adoption authority, deliberately withheld throughout: no label registered, no contract changed;
- pacing and stopping.

The asymmetry is stark: the agent's contributions were voluminous and fast; the human's were two or three sentences — but the sentences were ones no agent produced.

## The central puzzle: why agents did not discover the inheritance's role

The maintainer's question: linking is core technology here, the Ars Contexta inheritance is its origin story — why did the agents not surface its crucial role themselves?

**Layer 1 — a capture gap, now verified.** The durable corpus does not contain the fact. ADR 009 records the adoption; ADR 019 records the repair (collection-owned vocabularies) and even concedes in passing that new collections must design vocabularies by hand; `linking-theory.md` asks only an open question about the borrowed types. Nowhere does any artifact state the claim itself: *the inherited theory is not generative; attempts to derive per-collection vocabularies from it failed.* A search for generativity language across those documents returns nothing. The failed derivation attempt — the event that defines this workshop's problem statement — was never an ADR (no decision), never a note (nobody wrote the claim), never a log entry. It survived only in the maintainer's episodic memory, entering the corpus for the first time as a grounding bullet the maintainer dictated into the [brainstorm brief](./brainstorm-formal-link-theory.md). **The KB records decisions and repairs; it does not record failed theory searches — and failed theory searches are exactly the problem statements of future ones.**

**Layer 2 — a valuation gap, not a retrieval gap.** Even with the fact in context (the brief's bullet), the first brainstorm draft cited it, built one conclusion around the missing process, and still treated it as one grounding observation among ten rather than as the central explanandum. The brief presented its grounding as a flat list, and flat lists erase importance gradients; the agent weighted what was dense, recent, quantitative, and locally verifiable (the 700-edge migration record) over what was sparse, old, narrative, and counterfactual (a failure that left no artifact). Recognizing the inheritance as a *completed natural experiment with a readable result* — adopted universally, worked where endpoints were propositions, broke where they were not — requires assembling significance across ADR 009, ADR 019, and an absent artifact. Nothing in the corpus or the procedure prompted that historian's move.

**Capability was not the limit.** One corrective sentence from the maintainer ("the rules we inherited... we could not create a generator out of it") produced, within a single turn, the full diagnosis — the propositional vocabulary's hidden endpoint-kind parameter — and the two-stage generator that the experiments then validated. The agent could do everything except decide, unprompted, that this was the thing to explain.

## A reflexive symmetry

The experiments concluded: *the seed generates the semantic skeleton; authorization is selection, and selection belongs to the corpus record and the humans who own it.* The meta-process that produced the theory has the same shape: **agents generated the models, experiments, corrections, and candidate conclusions; the human supplied significance and holds adoption.** The boundary the theory located inside link vocabularies — generated semantics versus selected authorization — recurses onto the theory-building process itself. A second reflexive loop: the normalized footer grammar (protected by brainstorm conclusion 2) is what made the migration data enumerable, which is what gave the agents anything to theorize from — the KB's self-correction capacity was not just claimed in this workshop but exercised by it.

## Candidate remedies (generated, not adopted)

1. **Record framework failures as first-class claims.** When work repairs *around* an inherited framework (as ADR 019 did), the framework's limitation should be captured as a claim-note at that moment — "X is not generative for Y" — not left implicit in the repair. This is a capture rule; it would have put the load-bearing fact within `rg`'s reach years before this workshop. Route: a note plus possibly one line in ADR-writing guidance.
2. **Rank grounding by explanatory demand.** Brainstorm briefs/procedures could require, before modeling: *rank the grounding observations by "which is the biggest unexplained fact?", and address the top-ranked first.* The inheritance story (worked for one collection, failed for another, no generator derivable) plausibly tops such a ranking. This is an automatable salience repair for the flat-list problem. Route: an addition to whatever brainstorm instruction gets promoted from this workshop.
3. **Treat maintainer memory as an un-ingested source.** At workshop opening, elicit explicitly: *what did we already try that failed, and where is that recorded?* Anything answered from memory rather than from an artifact is a capture debt to pay before theorizing. Route: workshop-opening checklist.
4. **What stays human, for now:** deciding which unexplained fact the project should care about (goal-level significance), adoption/authorization, and stopping. The efficient design this episode demonstrates is not "automate the human away" but the comparative-advantage split: agents generate broadly and self-correct cheaply; the human spends a few sentences of rare, high-leverage steering — provided the capture rules above stop those sentences from being the only place critical history lives.

## Status

Analysis of one episode; the remedies are candidates for the workshop's closure outputs, alongside the theory itself. The promotion-worthy claims flagged here — failed theory searches are systematically under-captured; agent theory-building fails on valuation before it fails on retrieval or capability; the generate/select boundary recurses from the object theory onto the process that built it — should be tested against at least one more episode before any becomes a note.
