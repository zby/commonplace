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

Where a defeat was a transfer past a source's shared mechanism, the
[match register](./match-register.md) records the row (S2, C3, R2) and the
reconstruction must re-derive the claim from that mechanism or drop it.

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
| O8 | Warranted transfer out of the human cut is adversely selective: the residual human decisions are harder to warrant per decision, so envelopes do not stack toward closure and the human-work list is a residue, not a capacity claim. | Candidate mechanism; library note `kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md` (2026-08-28) | Hold boundary, objective, horizon, and workload fixed; classify each residual decision by the reason it resisted transfer; keep distinct from the elastic-backlog relocation mechanism; do not infer prevalence from the conditional. |
| O9 | Scoped closure and the remote-programmer benchmark meet at the evaluator: both are decided by whether the system can warrant its own hardest decisions, and the benchmark's client cut is a declared export of demand choice and acceptance. | Candidate framing; author direction (2026-08-28) | Name the exported decisions; show that captured evaluator, viability-only gate, and boundary export all sit at the verification row; keep closure and capability as separate coordinates that share one deciding point. |
| O10 | The program's theory is an operational instrument in the KB: classifying a path's residual human decisions by reason and routing each class to a mechanism is a theory-building wiki function, and its use on Commonplace's own transfers supplies a mediation trace. | Candidate; author direction (2026-08-28); earned by recorded use | One recorded application on a Commonplace path with classification, chosen transfer, and outcome; cite it from the bootstrap article. Tool-usefulness and traceability only; not closure. |
| O12 | At the coherent-modification decision, holding the theory is equivalent to warrant under conditions: bearer tests passed with test 3 as track record under exposure; refuting exposures not authored by the candidate; outcomes read back and recorded; exposure density matched to stakes, with decorrelated criticism as the decisive check where exposure is sparse; a plural or decorrelated coherence check; recognized abstention routed to exposure or a peer. The human holder is the standard, and human self-judgment works because dense cheap feedback, a group of holders, and knowing-when-unsure come free; science is the sparse-exposure regime that institutionalizes the substitutes. | Candidate; operator direction (2026-08-28) | Show the four conditions for a named composite and path; reread captured-evaluator cases as non-holder self-assessment or holder-without-exposure; test over a horizon of later demands, not per-task acceptance. |
| O11 | Read as a build plan, the classification orders what to build next for an LLM wiki, an LLM coding agent, or an LLM agent generally, because the theory is stated over decisions rather than tasks. | Candidate program claim; author direction (2026-08-28) | Separate the plan's ordering from any power claim; a power gain is a conjecture tested by matched comparison, not derived from the plan's shape. |

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

## Retained source grounding (carried from the earlier workshop)

Quote counts as recorded when the earlier workshop closed its outline; verify
against the ingest before relying on a count.

| Source | Role in the series | Quotes retained |
|---|---|---|
| Naur, *Programming as Theory Building* | hook, both halves, three tests | 19 |
| Popper, *A Realist View of Logic, Physics, and History* | what a theory is; consumption as criticism | 8 (no "World 3" label in this text) |
| Argyris, *Organizational Learning and MIS* | espoused/theory-in-use; single/double loop; self-sealing | 9 (OCR artifacts preserved; "changes" governing variables is our reading) |
| Craik, *Hypothesis on the Nature of Thought* | why a model pays | none — `(snapshot required)` marker |
| Ashby, *Design for a Brain* | theory-free contrast | see ingest |
| Sutton and Javed | weights-side counterpoint | 7 |
| Memento-Skills | acceptance-mechanism cell in the Bitter Lesson article | 2 (test gate; rollback steps) |

## Transfer record

When a claim moves, append a row here:

| Source IDs | Disposition | Exact successor claim | Destination | Warrant | Citer updates |
|---|---|---|---|---|---|
| O8; T5; R6 | Promoted to library note | Each residue class needs a different mechanism, so a self-improving architecture must be mixed | `kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md` | Argued from library notes only; validated 2026-08-28; no source grounding consumed | Reciprocal footer links added to cited notes; articles not yet reconciled |
| O7; O9 | Promoted to library note | A benchmark that holds the client fixed exports the least-warrantable decisions by design | `kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md` | Argued from library notes only; validated 2026-08-28; no source grounding consumed | Reciprocal footer links added to cited notes; articles not yet reconciled |
| S2; S3; S4 | Folded 2026-08-28 into an existing note | A theory-mediated loop closes only by causal co-indexing, not by co-occurrence inside one boundary | `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md` § The attribution needs one co-indexed path | Compressed from the satellite note; argued from library notes only | Inbound links repointed or dropped |
| O5; O6 | Promoted to library note | A method's ceiling bounds the method, not the transfer it already made | `kb/notes/a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md` | Argued from library notes only; validated 2026-08-28; no source grounding consumed | Reciprocal footer links added to cited notes; articles not yet reconciled |
| O3; O11 | Promoted to library note | Tool usefulness, computational autonomy, warrant, and system power are separate dimensions | `kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md` | Argued from library notes only; validated 2026-08-28; no source grounding consumed | Reciprocal footer links added to cited notes; articles not yet reconciled |
| S4; O10; T2 | Promoted to library note | Citing retained theory at the decision point is a mediation trace (necessary for a record-based mediation claim, not sufficient) | `kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md` | Argued from library notes only; validated 2026-08-28; no source grounding consumed | Reciprocal footer links added to cited notes; articles not yet reconciled |
| O5; T3 | Folded 2026-08-28 into an existing note | Programming-tool progress is a partial order on accepted outcomes per total human effort, not a scalar | `kb/notes/increasing-computational-autonomy-relocates-human-effort.md` § What to measure instead | Compressed from the satellite note; argued from library notes only | Inbound links repointed or dropped |
| C4; C1 | Folded 2026-08-28 into an existing note | Explicit artifacts buy addressability, not credit assignment, coherence, retrieval, or admission | `kb/notes/reflection-buys-addressability.md` § What addressability does not buy | Compressed from the satellite note; argued from library notes only | Inbound links repointed or dropped |
| O3; T6 | Retired 2026-08-28 as trivial | Removing a human judgment can degrade the judgments that remain — kept as one sentence plus its defeater in the parent note | `kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md` (Consequences for closure) | Parent note | Inbound footer links removed |
