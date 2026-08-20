# Claim skeleton: analyse an external system's epistemic architecture

Structural plan only. Disposition IDs point to `claim-disposition.md`; the fresh writer may phrase them but must not add commitments.

## Fixed purpose and assertion controls

Purpose: instruct an agent analysing an external memory subsystem or whole agentic system to identify epistemic objects and routes, separate generation from warrant and later use, and return evidence-bounded route findings rather than a system-wide grade.

Fixed route-level decision:

- import = acquired, not produced;
- entailed output = derived warranted content only from warranted premises through a warranted derivation in its declared domain;
- non-entailed truth-apt output = produced accepted ampliative claim only after an evidence-consuming acceptance transition names criterion, intended use, and scope;
- retention, retrieval, reshaping, direct adaptation, operational use, or candidate generation alone does not qualify;
- acceptance supplies the architectural warrant boundary; integration remains a separate finding.

Scope/confidence: fixed authoring rules for inspected routes, not universal empirical claims or philosophical truth. Basis: B12, C1-C6, C20, D6. Evidence-layer limits, indeterminate findings, and scoped negatives are fixed by A4-A8 and C12-C19.

## Artifact order

Use exactly:

1. Frontmatter.
2. Imperative H1 plus short opening.
3. `## Scope and prerequisites`.
4. `## Required output`.
5. `## Steps`.
6. `## Misuse guards`.
7. `## Verify`.

Do not add rationale, history, case studies, related work, or a summary.

### Frontmatter, title, and opening

- Only `description` and `type`.
- Description intent: trigger on a request to determine whether/how an external memory subsystem or agentic system produces knowledge, or to trace its epistemic architecture; do not advertise general product review.
- `type: kb/types/instruction.md`.
- H1: `Analyse an External System's Epistemic Architecture`.
- Opening job: state the trigger, both system scopes, route-level output, and that the analysis informs a review but does not accept external claims.
- Define here:
  - **epistemic architecture**: routes that acquire or produce truth-apt content, check it, grant or withhold reliance, retain or integrate it, and let it affect later behavior;
  - **truth-apt content**: content whose truth or falsity can be stated over a named scope.

Basis: A1-A3, A13, B1, B3.

### `## Scope and prerequisites`

Job: fix the analysis and evidence boundary.

Require system, revision/version, question, subsystem/whole-system/named-route scope, inspectable source identity, system knowledge-production claims if any, and known gaps.

Define evidence layers here: **implementation** (inspected executable behavior), **doctrine/design** (declared intent or contract), **reported operation** (attributed report without run evidence), **observed run** (inspectable execution trace/artifact), and **causal experiment** (observed treatment-control contrast, with attribution limited to its grain). Do not upgrade one layer into another.

Require form-appropriate inspection: read natural language, test symbolic artifacts inside their semantics, and probe distributed-parametric state. If available probes cannot individuate truth-apt content, require `not determinable`.

Scope exits:

1. Product ranking, adoption advice, ontology design, or a general review with no knowledge-production question -> stop and use the task-appropriate method.
2. No inspectable source boundary or revision -> return only output 1 with `insufficient evidence` and the conclusions prevented.
3. Do not prescribe natural-language claims, proposal comparison, a storage model, or a universal ontology. Treat intentionally operational scope as scope, not product failure.

Basis: A4-A8, A11-A12.

### `## Required output`

Job: specify six blocks, in this order, as readable Markdown tables or compact records. Do not introduce a permanent controlled-token matrix.

1. **Source-and-claim boundary**

   `system | reviewed revision/version | analysis question | scope | implementation evidence | doctrine/design evidence | reported-operation evidence | observed-run evidence | causal-experiment evidence | missing evidence -> conclusion prevented | system knowledge-production/warrant claims -> source or none found`

2. **Epistemic-object inventory** — one row per operative part; stable IDs; split parts with different content, form, checks, producers/consumers, or authority paths.

   `object/part id | system name and description | representational form | source/input and lineage | producer/consumer | candidate truth-apt content or none | claimed role | evidence layer and source | gap/limit`

3. **Authority-route ledger** — one row per consequential check or transition; stable IDs; split different targets, timing, results, or force; include evidenced absence without inventing an oracle.

   `route id | object/candidate id | input-to-output transformation | check target | oracle/evaluator and domain | timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: consumer, channel, force, horizon | evidence layer and source | system claim versus route | gap/limit`

4. **Per-candidate lifecycle disposition** — a separate record for every object inventory entry with candidate truth-apt output; key to object ID and all relevant route IDs.

   Ampliative record:

   `candidate object ID | relevant route IDs | transformation: ampliative conjecture | observation/anomaly: state + evidence | conjecture: state + evidence | derived consequence: state + evidence | test/evidence: state + evidence | acceptance: evaluator + criterion + intended use + state + accepted scope | integration: retention/later-use consumer + state + evidence | missing phase/evidence`

   Allowed phase states: `evidenced`, `absent`, `failed`, `accepted`, `rejected`, `revised`, `suspended`, `not determinable`. Use only states supported by evidence.

   Non-ampliative truth-apt record:

   `candidate object ID | relevant route IDs | transformation | discovery lifecycle: not applicable | applicable lineage, derivation, or update route and warrant | missing evidence/limit`

   If no truth-apt candidate exists: `No lifecycle record: no candidate truth-apt output found within the source boundary.`

5. **System-claim versus route comparison** — one row per consequential public/design claim; state explicitly when none was found.

   `claim id | claimed operation or warrant | claim source and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support | supported conclusion | mismatch/unknown`

6. **Bounded conclusion** — route-level sentences, keyed where applicable, covering:
   - retained/retrieved/reshaped/used;
   - acquired and source warrant preserved/degraded/unknown;
   - derived, warranted premises, and domain;
   - conjectured, tested, accepted, and integrated;
   - acceptance criterion, intended use, scope, consumer, channel, and force;
   - direct behavior/policy adaptation without a truth-apt route;
   - claims unsupported by missing implementation, run, or causal evidence.

   Prohibit a system-wide epistemic score, oracle, status, or unqualified verdict.

Basis: C4, C9-C12, D1-D8.

### `## Steps`

Job: populate the six outputs in dependency order. Use numbered imperatives; do not repeat their schemas.

1. **Fix the boundary.** Populate output 1. Assign each item its strongest available evidence layer. State each gap and exactly what it prevents.

2. **Inventory objects before oracles.** Populate output 2. Define **epistemic object** here as the concrete typed part whose content or status a route produces, checks, accepts, or consumes. Split heterogeneous containers; allow system-specific object names. [B2-B5]

3. **Apply the early branch.**
   - Only storage/retrieval/serving/direct use and no knowledge-production claim -> output one ledger row for the evidenced transition (or explicit `no relevant route found`), no relevant check/epistemic authority within the boundary, any operational force, the no-candidate lifecycle statement, an explicit no-claim comparison, and a bounded negative; then stop.
   - Knowledge-production claim but no implemented route -> ensure the claimed object has an inventory ID, output an absence row keyed to it, claim comparison, claimed-candidate phases as `absent` or `not determinable`, mismatch, and bounded conclusion; then stop.
   - Otherwise continue. Never turn a scoped absence into “no informal or unobserved route exists.” [A9-A10, C12]

4. **Classify each input-to-output edge.** Define and decide in order:
   - external content enters -> **acquisition/import**; source warrant preserved/degraded/unknown;
   - truth-apt content is only reordered, indexed, grouped, reformatted, deduplicated, or compressed -> **non-ampliative reshaping**;
   - new proposition follows from inputs -> **entailed derivation**; warrant requires warranted premises and a checked interpretation/formal domain;
   - truth-apt proposition does not follow from inputs -> **ampliative conjecture**; novelty, fluency, and plausibility establish only generation;
   - behavior changes via reward/error/gradient/viability with no truth-apt object -> **direct behavior/policy adaptation**;
   - preservation or entailment cannot be established -> **indeterminate** plus missing evidence.
   Split sequential transformations. [B6-B11]

5. **Build the route ledger.** Populate output 3. Define here: **check target** (object/proposition/class and domain, named before oracle); **oracle/evaluator** (human, model, program, environment, proof, measurement, or hybrid procedure judging that target); **operative result** (result consumed to change admission, rejection, revision, acceptance, retention, integration, rollback, use, ranking, or continuation); **epistemic authority** (content and scope licensed for reliance); **operational authority** (later behavior permitted through consumer, channel, force, horizon). A recorded result without a consequential consumer has no implemented force. [C8-C12, C20]

6. **Dispose every candidate.** Populate output 4. Define **discovery lifecycle** here: observation/anomaly, conjecture, consequence derivation, test/evidence, acceptance, integration. Apply only to ampliative candidates. Define **acceptance** as a recorded evidence-consuming decision against a named criterion for an intended use and scope. Record integration and its consumer separately. [C2-C6]

7. **Bound each check's licenses.** For every ledger row, state what the result warrants, permits, and does not establish. Keep separate: outcome/process/explanation; reconstructed route/producing route; consequence fit/mechanism and transfer; formal validity/source truth and encoding fidelity; applicability/endorsement; continuation/warrant; bundle success/component effect. Attribute component effect only to an independently varied component and actual contrast. [C13-C19]

8. **Compare claims with routes.** Populate output 5 across doctrine, implementation, observed-run, and causal evidence. Record deliberately operational scope without treating it as failure; still expose broader claim/route mismatch. [A11, D5]

9. **Conclude by route.** Populate output 6 using the fixed decision at the top. Do not turn acceptance into infallibility, integration into acceptance, or one route's result into a system label. [B12, C20, D6]

### `## Misuse guards`

Job: one compact prohibition list, without rationale or examples.

- No knowledge-production inference from storage, retrieval, injection, later use, behavioral influence, novelty, fluency, or plausibility alone. [E1, E3]
- No acceptance inference from retention, labels, grades, reports, freshness, or unconsumed results. [E2]
- No transfer from an outcome pass to process, explanation, replay safety, transfer, or component effect. [E4, E6]
- No transfer from proof/formal validity to source truth, encoding fidelity, omitted premises, or outside-domain claims. [E5]
- No system-wide oracle, status, or authority for heterogeneous routes. [E7]
- No upgrade from doctrine/purpose to implementation; no product-failure judgment from operational scope. [E8]
- No required natural-language claims, proposal loop, Commonplace storage, or universal ontology. [E9]

### `## Verify`

Job: completion checks only.

- Boundary complete; evidence layers and prevented conclusions explicit.
- Every operative part has an ID; heterogeneous parts split.
- Every transformation classified or evidence-bounded as indeterminate.
- Every consequential check/transition has a route row with target before oracle, timing, result, force, separate authorities, evidence, and limit.
- Every candidate truth-apt object has its own object/route-keyed lifecycle record, including not-applicable records.
- Every ampliative record separates generation, test, acceptance, and integration and names missing phases.
- Every consequential system claim is compared across evidence layers without upgrading them.
- Every negative/unknown is scoped; no license exceeds its target, contrast, domain, horizon, or route.
- Conclusion uses route-level verbs and no system-wide epistemic grade.
- Analysis informs review but does not accept the system's claims. [D7, A13]

## Omit or defer

- Omit all case narratives, discarded matrices/labels, system-specific mechanics, product rankings, the explanatory-quality conjecture, Commonplace review internals, and existing memory-review gap rationale. [F1-F8]
- Omit a universal parametric probe or proposal loop. [F13-F14]
- Defer permanent controlled vocabulary, companion note, skill promotion, and memory-review integration. [F7, F9, F12]
- ARC and held-out GBrain trials occur only after `draft.md`; do not name them in the instruction or make them executor steps. [F10-F11]

No blocking marker remains. A new material commitment must return to claim disposition instead of entering the draft.
