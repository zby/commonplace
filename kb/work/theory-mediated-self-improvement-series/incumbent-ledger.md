# Incumbent claim ledger

This ledger prevents a rejected document from becoming the implicit outline of
its successor. It records claims, not paragraphs. Old prose can be considered
only after the claim it expresses has a disposition.

## Status vocabulary

| Status | Meaning |
|---|---|
| Accepted baseline | The cited completed pass accepted the article body as a starting point; later revision remains possible. |
| Candidate | The review left a bounded contribution available, but the workshop has not accepted successor wording. |
| Narrow | The mechanism may survive only after the defeated scope, modality, or category is removed. |
| Defeated as stated | The review supplied a counterexample or evidential failure that binds the reconstruction. The old sentence may not return. |
| Omit | The claim does no necessary job or cannot be warranted. |
| Promoted | An accepted successor contains exact replacement wording and evidence; the destination is recorded here. |

Moving a claim requires five fields: source claim ID, exact successor wording,
destination, warrant, and affected-citer disposition. Copying a paragraph
without that record is not a move.

## Source register

| Source | Review identity | Document status |
|---|---|---|
| accepted/what-bound-naurs-theory-to-programmers.md | closing-ready pass 20260827T152910Z-b7e42d; accepted capture SHA-256 3161c1db34e27a5f5bd7afc23778df073d5a58e0f45734e95667c2adffd9679d | Accepted baseline |
| accepted/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md | closing-ready pass 20260827T153208Z-9f4bd8; accepted capture SHA-256 73ce96a40f41a87dafb2367e2d05d602df7309f6f264aa79a2b5e41f833f4807 | Accepted baseline |
| rejected-drafts/theory-building-inside-the-system.txt | pass 20260827T163241Z-16d5d1; source SHA-256 50fee4cceeb34cef266d97a2f6f2a160e66916089442a75144b3bdc28bfafa80 | Quarantined after closing hand-back |
| rejected-drafts/when-systems-learn-theories-about-themselves.txt | pass 20260827T163237Z-7ed60b; source SHA-256 7a9f74838feb920aa6dd8be4229f526c8479582c6465cf8fab21f61064fd8180 | Quarantined after revise |
| rejected-drafts/moving-revision-decisions-into-the-automatic-system.txt | pass 20260827T163335Z-8e9d5e; source SHA-256 eeb3c69d8f54d969d1cb92ace504a49873fd56bbee9c260d26d3bce0dc95a64a | Quarantined after revise |
| rejected-drafts/continual-learning-outside-the-weights.txt | pass 20260827T163425Z-2082a8; source SHA-256 36f8896c25bb1122997e56a24e05195e722d4fc4e3b2e42721e4337c4c0b8255 | Quarantined after revise |

## Operator-supplied claims added after review

| ID | Claim | Current status | Required evidence or distinction |
|---|---|---|---|
| O1 | Commonplace already works as a human–agent theory-building tool. | Candidate; author direction | Evaluate the composite's ability to form, criticize, retain, retrieve, apply, and revise theories. Do not infer independent computational possession. |
| O2 | The same substrate can expand to other LLM-wiki functions. | Candidate program claim | Name each operation and its consumer, success test, and human cut; do not infer completeness from a catalogue. |
| O3 | Increasing warranted automation can make the theory-building and LLM-wiki tool more useful before closure. | Candidate causal claim | Compare task quality, reach, latency, intervention, repeatability, correction cost, and warrant. Automation alone is not the outcome. |
| O4 | Computational closure matters only around a system powerful enough for consequential work; trivial closed systems must be mapped and excluded from the target. | Candidate framing and evaluation requirement | Declare the challenge distribution and capability floor; compare closure, operational capability, effective revision reach, evaluator adequacy, continuity, outcome evidence, and supplied capability. |
| O5 | Any programming-tool change that increases accepted software outcomes for fixed total human programming effort, or preserves those outcomes with less effort, is real progress toward the broad goal. Better performance inside a fixed automation envelope also counts on capability or yield. | Candidate progress relation; author direction | Hold task class and acceptance threshold fixed; count configuration, review, recovery, and repair; compare output quality, reliability, coverage, latency, and resource cost; record quality or warrant losses rather than hiding them. |
| O6 | A bounded mechanism can make real progress and still reach an automation ceiling; the ceiling limits that method rather than invalidating the responsibility already transferred or later performance improvements inside its envelope. | Candidate architectural framing; author direction | Name the residual responsibility transferred, the conditions of transfer, the work outside the method's envelope, and any composition needed to continue. Separate envelope expansion from performance inside the envelope. Do not infer convergence from either local improvement. |
| O7 | Performance at least as good as a competent remote programmer is a strong capability benchmark, not the definition of all useful progress or the final upper limit. | Candidate comparator; author direction | Declare the challenge distribution; hold brief, repository, digital tools, permissions, and feedback constant; separate client direction from programming decisions; compare outcome quality and reliability independently from time and resource cost. |

## Theory-building draft claims

| ID | Incumbent claim | Review-constrained disposition | Permitted next move |
|---|---|---|---|
| T1 | Theory building can be decomposed into functions and allocated across human and computational actors inside a declared boundary. | Candidate | Fix the path and decision grain, then state the functions without implying that any activity by a model is theory-guided. |
| T2 | The traced repair episode warrants criticism and proposal as computational contributions while other decision content is untraced or human. | Narrow | Preserve only the evidence-bounded allocation. Distinguish criticism of a theory claim from criticism guided by the retained program-specific theory. |
| T3 | Re-recording the allocation gives a unique or scalar measure of progress toward autonomy. | Defeated as stated | Replace with a vector or partial order that records path coverage, horizon, human cut, warrant, usefulness, and yield. |
| T4 | Retained natural-language theory becomes operative or learned state when a capable interpreter consumes it. | Candidate | Specify the causal consumption path and separate operative retention from theory possession and system-level learning. |
| T5 | Formalization moves rather than removes the theory problem. | Candidate | Name the remaining theory–model correspondence and explain how code can faithfully execute a wrong realization. |
| T6 | Moving more theory-building functions to computation makes the current tool more useful. | Not established by the rejected draft | Reconstruct through O3 with a utility-and-warrant comparison rather than autonomy as proxy. |

## Self-theories draft claims

| ID | Incumbent claim | Review-constrained disposition | Permitted next move |
|---|---|---|---|
| S1 | Theory mediation, reflection, and self-improvement are distinct properties. | Candidate at path grain | Define each over a named causal path before making a system-level attribution. |
| S2 | A system realizes their intersection whenever all three occur somewhere inside its boundary. | Defeated as stated | Require causal co-indexing; disconnected witnesses are a counterexample. |
| S3 | Membership, interpretation, and separable retention are sufficient minimum conditions for the integrated loop. | Defeated as sufficient | Add the requirement that the self-theory determines change and is revised by the result on the same path. |
| S4 | Occurrence, revision-surface, and later-episode compounding tests establish that the self-theory loop is closed. | Defeated as sufficient | Keep the generic tests and add a mediation trace or intervention over theory, change, result, and theory revision. |
| S5 | None of the examined systems demonstrates recurrent later-episode dependence through a retained improvement. | Bounded candidate | Preserve the examined-set boundary and do not turn it into a prevalence claim. |
| S6 | Commonplace is a partial realization of the integrated loop. | Narrow | Separate current tool usefulness and human-inclusive participation from evidence that one self-theory path is closed. |

## Revision-decisions draft claims

| ID | Incumbent claim | Review-constrained disposition | Permitted next move |
|---|---|---|---|
| R1 | Human-inclusive self-revision is cheap relative to moving decisions into the automatic system. | Candidate framing | Name the decision and path; do not treat human inclusion as satisfying a computational-closure claim. |
| R2 | A governed revision path needs complete addressability of every repository artifact and relation. | Defeated as stated | Replace repository-wide addressability with the representations required by the named path. |
| R3 | Admission cannot move because its authorizing inputs are absent from the system. | Candidate | Identify the missing grant, holder, scope, conditions, and binding to the operative change. |
| R4 | Model realization cannot move because it is not represented. | Defeated as stated | Split absence from an existing but untrusted trace, false declaration, weak binding, and missing verification. |
| R5 | Six audited paths establish broad readiness for revision decisions to move. | Narrow | State readiness per named path and decision; do not infer repository-wide coverage. |
| R6 | A moved decision remains automatic because its scheduler and admission machinery stay supplied. | Incomplete | Treat the scheduler, verifier, and admission machinery as later revision targets or declare them outside the scoped claim. |

## Continual-learning draft claims

| ID | Incumbent claim | Review-constrained disposition | Permitted next move |
|---|---|---|---|
| C1 | A frozen interpreter over a governed artifact layer is a candidate continual-learning substrate for expressible changes. | Candidate | State proposal, evaluation, authorization, retention, and later activation inside the declared system boundary. |
| C2 | Durable behavior change selected by the system's evidence is system-level learning even when weights do not change. | Category decision pending | Define the learning unit and distinguish system adaptation from Sutton and Javed's stronger concept-formation target. |
| C3 | New concepts are formed as named retained artifacts after weights freeze. | Defeated as stated for the computational part | Preserve only demonstrated naming, retention, application, and revision by the human–agent composite unless an autonomous witness is supplied. |
| C4 | Explicit artifacts keep the knowledge coherent and correct. | Defeated as stated | Claim addressability and inspectability only; add credit assignment, conflict handling, retrieval, evaluation, and admission where warranted. |
| C5 | Artifact-only learning should outperform weight updates on expressible structure-preserving shifts with less collateral change. | Untested prediction | Retain only as an experiment with matched baselines and an explicit interaction prediction. |
| C6 | The artifact substrate already supports broader LLM-wiki operation. | Candidate through O2 | Describe demonstrated operations without using continual learning as a blanket label. |

## Transfer record

When a claim moves, append a row here:

| Source IDs | Disposition | Exact successor claim | Destination | Warrant | Citer updates |
|---|---|---|---|---|---|
| — | — | — | — | — | — |
