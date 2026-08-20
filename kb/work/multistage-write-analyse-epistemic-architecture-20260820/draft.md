---
description: Determine whether and how an external memory subsystem or agentic system produces knowledge by tracing its epistemic objects, transformations, warrant, and authority routes.
type: kb/types/instruction.md
---

# Analyse an External System's Epistemic Architecture

Use this procedure when asked whether or how an external memory subsystem or whole agentic system produces knowledge, or when asked to trace its epistemic architecture. Analyse each route separately and return evidence-bounded findings rather than a system-wide epistemic grade. The analysis informs a review; it does not itself accept the external system's claims.

An **epistemic architecture** is the set of routes by which a system acquires or produces truth-apt content, checks it, grants or withholds reliance, retains or integrates it, and lets it affect later behavior. **Truth-apt content** is content whose truth or falsity can be stated over a named scope.

## Scope and prerequisites

Before starting, identify:

- the system and reviewed revision or version;
- the analysis question and whether the scope is a memory subsystem, a whole agentic system, or named routes;
- the inspectable sources and their identities;
- the system's knowledge-production or warrant claims, if any; and
- known evidence gaps.

Keep these evidence layers separate:

- **Implementation:** inspected executable behavior.
- **Doctrine/design:** declared intent or contract.
- **Reported operation:** an attributed report without inspectable run evidence.
- **Observed run:** an inspectable execution trace or artifact.
- **Causal experiment:** an observed treatment-control contrast, with attribution limited to the actual treatment and comparison grain.

Do not upgrade one evidence layer into another. Inspect each representational form appropriately: read natural-language content, test symbolic artifacts within their declared semantics, and use available probes for distributed-parametric state. If the available probes cannot individuate truth-apt content, record the object or lifecycle phase as `not determinable`.

Apply these scope branches before continuing:

- If the task is product ranking, adoption advice, ontology design, or a general review with no knowledge-production question, stop and use a method suited to that task.
- If no inspectable source boundary or revision can be established, produce only output 1 with `insufficient evidence` and name each conclusion the missing evidence prevents.
- Treat an intentionally operational or lab-tracking purpose as a scope boundary, not as product failure. Do not prescribe natural-language claims, proposal comparison, a storage model, or a universal knowledge ontology.

## Required output

Produce these six blocks in order. Use readable Markdown tables or compact records; do not introduce a permanent controlled-token matrix.

### 1. Source-and-claim boundary

Use these fields:

`system | reviewed revision/version | analysis question | scope | implementation evidence | doctrine/design evidence | reported-operation evidence | observed-run evidence | causal-experiment evidence | missing evidence -> conclusion prevented | system knowledge-production/warrant claims -> source or none found`

### 2. Epistemic-object inventory

Use one row per operative part and assign stable IDs. Split parts that differ in content, form, checks, producers or consumers, or authority paths.

`object/part id | system name and description | representational form | source/input and lineage | producer/consumer | candidate truth-apt content or none | claimed role | evidence layer and source | gap/limit`

### 3. Authority-route ledger

Use one row per consequential check or transition and assign stable IDs. Split routes that differ in target, timing, result, or force. Record an evidenced absence without inventing an oracle.

`route id | object/candidate id | input-to-output transformation | check target | oracle/evaluator and domain | timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: consumer, channel, force, horizon | evidence layer and source | system claim versus route | gap/limit`

### 4. Per-candidate lifecycle disposition

Create a separate record for every inventory entry with candidate truth-apt output. Key each record to its object ID and all relevant route IDs.

For an ampliative candidate, use:

`candidate object ID | relevant route IDs | transformation: ampliative conjecture | observation/anomaly: state + evidence | conjecture: state + evidence | derived consequence: state + evidence | test/evidence: state + evidence | acceptance: evaluator + criterion + intended use + state + accepted scope | integration: retention/later-use consumer + state + evidence | missing phase/evidence`

Allowed phase states are `evidenced`, `absent`, `failed`, `accepted`, `rejected`, `revised`, `suspended`, and `not determinable`. Use only states supported by evidence.

For non-ampliative truth-apt content, use:

`candidate object ID | relevant route IDs | transformation | discovery lifecycle: not applicable | applicable lineage, derivation, or update route and warrant | missing evidence/limit`

If no truth-apt candidate exists, write: `No lifecycle record: no candidate truth-apt output found within the source boundary.`

### 5. System-claim versus route comparison

Use one row per consequential public or design claim. State explicitly when none was found.

`claim id | claimed operation or warrant | claim source and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support | supported conclusion | mismatch/unknown`

### 6. Bounded conclusion

Write route-level sentences, keyed to object and route IDs where applicable, that state:

- what the system retains, retrieves, reshapes, or uses;
- what it acquires and whether source warrant is preserved, degraded, or unknown;
- what it derives, from which warranted premises, and within what domain;
- what it conjectures, tests, accepts, and integrates;
- each acceptance criterion, intended use, scope, consumer, channel, and force;
- any direct behavior or policy adaptation without a truth-apt route; and
- which claims remain unsupported because implementation, run, or causal evidence is missing.

Do not give the system a single epistemic score, oracle, status, or unqualified verdict.

## Steps

1. **Fix the boundary.** Populate output 1. Assign each item its strongest available evidence layer. State each evidence gap and exactly what conclusion it prevents.

2. **Inventory objects before oracles.** Populate output 2. An **epistemic object** is the concrete typed part whose content or status a route produces, checks, accepts, or consumes. Use system-specific object names. Split a container when its parts have different content, forms, checks, producers or consumers, or authority paths. Name each target object or proposition and its domain before assessing any oracle.

3. **Apply the early branch.**

   - If the inventory shows only storage, retrieval, serving, or direct use, with no relevant transformation and no knowledge-production claim, add one ledger row for the evidenced transition or an explicit `no relevant route found`. Record no relevant check or epistemic authority within the boundary, any operational force, the no-candidate lifecycle statement, an explicit no-claim comparison, and a bounded negative conclusion. Then stop.
   - If the system makes a knowledge-production claim but no implemented route was found, give the claimed object an inventory ID. Add an absence row keyed to it, compare the claim with the absent route, mark the claimed candidate's phases `absent` or `not determinable` as the evidence permits, and write the mismatch and bounded conclusion. Then stop.
   - Otherwise, continue. Never expand a scoped absence into a claim that no informal or unobserved route exists.

4. **Classify every input-to-output edge.** Apply these rules in order and split sequential transformations into separate edges:

   - When external content enters the system, classify the edge as **acquisition/import** and record source warrant as preserved, degraded, or unknown.
   - When truth-apt content is only reordered, indexed, grouped, reformatted, deduplicated, or compressed, classify the edge as **non-ampliative reshaping**.
   - When a new proposition follows from its inputs, classify the edge as **entailed derivation**. Carry warrant only from warranted premises through a checked interpretation or formal domain.
   - When a truth-apt proposition does not follow from its inputs, classify the edge as **ampliative conjecture**. Novelty, fluency, and plausibility establish candidate generation only.
   - When behavior changes through reward, error, gradient, or viability without an evidenced truth-apt object, classify the edge as **direct behavior/policy adaptation**.
   - When semantic preservation or entailment cannot be established, classify the edge as **indeterminate** and state the missing evidence.

5. **Build the authority-route ledger.** Populate output 3. A **check target** is the object, proposition, or class and domain being assessed; name it before the oracle. An **oracle/evaluator** is the human, model, program, environment, proof, measurement, or hybrid procedure that judges that target. An **operative result** is consumed to change admission, rejection, revision, acceptance, retention, integration, rollback, use, ranking, or continuation. **Epistemic authority** is the content and scope licensed for reliance. **Operational authority** is the later behavior permitted through a named consumer, channel, force, and horizon. A recorded result with no consequential consumer has no implemented force. Use separate rows when targets, timing, results, or force differ; do not merge routes merely because they share a file, model, evaluator, or task.

6. **Dispose every candidate.** Populate output 4. The **discovery lifecycle** comprises observation or anomaly, conjecture, consequence derivation, test or evidence, acceptance, and integration. Apply it only to ampliative candidates. **Acceptance** is a recorded, evidence-consuming decision against a named criterion for an intended use and scope. Record integration and its retention or later-use consumer separately. For acquisition, reshaping, entailed derivation, and direct adaptation, record that the discovery lifecycle is not applicable and identify the applicable lineage, derivation, or update route.

7. **Bound each check's licenses.** For every ledger row, state what the result warrants, what it permits operationally, and what it does not establish. Keep separate:

   - outcome from producing process, explanation, replay safety, transfer, and component effect;
   - a valid reconstructed route from evidence that it produced the observed outcome;
   - consequence fit from warrant for the proposed mechanism and its transfer boundary;
   - formal validity from source truth, encoding fidelity, omitted premises, and claims outside the formal domain;
   - applicability or freshness from endorsement;
   - operational continuation from epistemic warrant; and
   - bundle success from the effect of an individual component.

   Attribute a component effect only when the observed comparison independently varied that component, and only at the grain of the actual contrast.

8. **Compare claims with routes.** Populate output 5. Compare each claim across doctrine/design, implementation, observed-run, and causal evidence. Record a deliberately operational scope without treating it as failure, but still expose any mismatch between that scope and a broader knowledge-production claim.

9. **Conclude by route.** Populate output 6. Report imported content as acquired, not produced. Report an entailed output as derived warranted content only when its premises and derivation are warranted within the declared domain. Report a non-entailed truth-apt output as a produced accepted ampliative claim only when an evidence-consuming acceptance transition names its criterion, intended use, and scope. Retention, retrieval, reshaping, direct adaptation, operational use, or candidate generation alone does not qualify as knowledge production. Report acceptance and integration separately. Do not turn acceptance into infallibility, integration into acceptance, or one route's result into a system label.

## Misuse guards

- Do not infer knowledge production from storage, retrieval, injection, later use, behavioral influence, novelty, fluency, or plausibility alone.
- Do not infer acceptance from retention, labels, grades, reports, freshness, or unconsumed results.
- Do not transfer an outcome pass to the producing process, explanation, replay safety, transfer, or component effect.
- Do not transfer proof or formal validity to source truth, encoding fidelity, omitted premises, or claims outside the checked domain.
- Do not assign one oracle, status, or authority to heterogeneous routes.
- Do not upgrade doctrine or purpose to implementation, or treat intentionally operational scope as product failure.
- Do not require natural-language claims, a proposal loop, Commonplace storage, or a universal ontology.

## Verify

- The source and claim boundary is complete; evidence layers and prevented conclusions are explicit.
- Every operative part has an ID, and heterogeneous parts are split.
- Every transformation is classified or bounded as indeterminate by missing evidence.
- Every consequential check or transition has a route row with target before oracle, timing, result, force, separate authorities, evidence, and limit.
- Every candidate truth-apt object has its own object- and route-keyed lifecycle record, including records where the discovery lifecycle is not applicable.
- Every ampliative record separates generation, test, acceptance, and integration and names missing phases.
- Every consequential system claim is compared across evidence layers without upgrading them.
- Every negative or unknown is scoped; no license exceeds its target, contrast, domain, horizon, or route.
- The conclusion uses route-level verbs and gives no system-wide epistemic grade.
- The analysis informs review but does not accept the system's claims.
