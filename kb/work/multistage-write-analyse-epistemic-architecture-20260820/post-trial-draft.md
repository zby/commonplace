---
description: Determine whether and how an external memory subsystem or agentic system produces knowledge by tracing its epistemic objects, transformations, warrant, and authority routes.
type: kb/types/instruction.md
---

# Analyse an External System's Epistemic Architecture

Use this procedure when asked whether or how an external memory subsystem or whole agentic system produces knowledge, or when asked to trace its epistemic architecture. Analyse each material route separately and return evidence-bounded findings rather than a system-wide epistemic grade. The analysis informs a review; it does not itself accept the external system's claims.

An **epistemic architecture** is the set of routes by which a system acquires or produces truth-apt content, checks it, grants or withholds reliance, retains or integrates it, and lets it affect later behavior. **Truth-apt content** is content whose truth or falsity can be stated over a named scope.

## Scope and prerequisites

Before starting, identify:

- the system and reviewed revision or version;
- the analysis question and whether the scope is a memory subsystem, a whole agentic system, or named routes;
- the inspectable sources and their identities;
- the system's knowledge-production or warrant claims, if any; and
- known evidence gaps.

For a whole-system question, inventory every **material route** within the declared boundary. A route is material when it:

- produces or changes truth-apt content;
- checks or disposes a candidate;
- grants, withholds, or changes epistemic or operational authority;
- retains or integrates a candidate for later reliance;
- directly adapts behavior or policy from evaluation; or
- is necessary to assess a consequential knowledge or warrant claim made by the system.

Include transport, storage, retrieval, formatting, freshness, and recovery plumbing only when it changes lineage or warrant, carries consequential force, or belongs to such a claim. Name omitted route classes and the conclusions their omission prevents. If exhaustive whole-system coverage is infeasible, declare the assessed and unassessed route families and do not make a system-complete conclusion.

Keep these evidence layers separate. Assign stable source IDs so later records can cite them without repeating full paths.

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

Produce these six blocks in order. Use readable Markdown tables or compact records.

### 1. Source-and-claim boundary

Use these fields:

`system | reviewed revision/version | analysis question | assessed route families | unassessed route families | implementation evidence IDs | doctrine/design evidence IDs | reported-operation evidence IDs | observed-run evidence IDs | causal-experiment evidence IDs | missing evidence -> conclusion prevented | system knowledge-production/warrant claims -> claim ID, source ID, or none found`

### 2. Epistemic-object inventory

Use one row per operative part within the material-route boundary and assign stable IDs. Split parts that differ in content, form, checks, producers or consumers, or authority paths.

`object/part id | system name and description | representational form | source/input and lineage | producer/consumer | candidate truth-apt content or none | claimed role | evidence source IDs and local anchor | gap/limit`

### 3. Authority-route ledger

Use one row per consequential check or transition and assign stable IDs. Split routes that differ in target, timing, result, or force. Record an evidenced absence without inventing an oracle.

`route id | route kind | object/candidate id | content transformation if any | transition or check target | evaluator/condition and domain | timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: consumer, channel, force, horizon | evidence source IDs and local anchor | claim IDs or mismatch | gap/limit`

Use these route kinds: `content transformation`, `check or disposition`, `retention or integration`, `operational admission, selection, or consumption`, `direct behavior/policy adaptation`, or `claimed but absent or suspended transition`. When a route changes only status, retention, admission, continuation, or use, write `content transformation: not applicable`.

### 4. Per-object lifecycle disposition

For every ampliative truth-apt candidate, key one record to its object ID and relevant route IDs. Record two axes for every phase:

- **Route availability:** `implemented`, `doctrine only`, `no route found within boundary`, or `not determinable`, with evidence.
- **Observed candidate state:** `no instance observed`, `not reached`, `phase evidenced`, `accepted`, `rejected`, `revised`, `failed`, `suspended`, `integrated`, or `not determinable`, with evidence. Use only states that apply to that phase.

Use this schema:

`candidate object ID | relevant route IDs | transformation: ampliative conjecture | observation/anomaly: availability + candidate state + evidence | conjecture: availability + candidate state + evidence | derived consequence: availability + candidate state + evidence | test/evidence: availability + candidate state + evidence | acceptance: evaluator + criterion + intended use + availability + candidate state + accepted scope | integration: retention/later-use consumer + availability + candidate state + evidence | missing phase/evidence`

For non-ampliative truth-apt content, use:

`candidate object ID | relevant route IDs | transformation | discovery lifecycle: not applicable | applicable acquisition, lineage, derivation, or update route and warrant | missing evidence/limit`

When preservation, entailment, or ampliation cannot be decided, use:

`candidate object ID | relevant route IDs | transformation: indeterminate | classifications still possible | preserved lineage | implemented checks, retention, or use | current warrant limit | evidence needed to decide preservation, entailment, or ampliation`

For an individual object with no candidate truth-apt output, write:

`No lifecycle record for <object ID>: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: <route IDs or none>.`

Only when the entire inventory contains no candidate truth-apt output, additionally write:

`No candidate lifecycle records: no candidate truth-apt output found within the source boundary.`

### 5. System-claim versus route comparison

Use one row per consequential public or design claim. State explicitly when none was found.

`claim id | claimed operation or warrant | claim source and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support | supported conclusion | mismatch/unknown`

### 6. Bounded conclusion

State only findings that change the answer to the analysis question. Group homogeneous object or route IDs when their warrant and force are the same. Cover:

- what the system retains, retrieves, reshapes, or uses;
- what it acquires and whether source warrant is preserved, degraded, or unknown;
- what it derives, from which warranted premises, and within what domain;
- what it conjectures, tests, accepts, and integrates;
- each material acceptance criterion, intended use, scope, consumer, channel, and force;
- any direct behavior or policy adaptation without a truth-apt route; and
- which claims remain unsupported because implementation, run, or causal evidence is missing.

Do not give the system a single epistemic score, oracle, status, or unqualified verdict.

## Steps

1. **Fix the boundary.** Populate output 1. Assign each source an evidence layer and stable ID. State every gap and exactly what conclusion it prevents.

2. **Inventory material objects before oracles.** Populate output 2. An **epistemic object** is the concrete typed part whose content or status a route produces, checks, accepts, or consumes. Apply the material-route rule, name omitted route families, use system-specific object names, and split heterogeneous containers. Name each target object or proposition and its domain before assessing any oracle.

3. **Apply the early branch.**

   - If the inventory shows only storage, retrieval, serving, or direct use, with no relevant transformation and no knowledge-production claim, add one ledger row for the evidenced transition or an explicit `no relevant route found`. Record no relevant check or epistemic authority within the boundary, any operational force, the global no-candidate statement, an explicit no-claim comparison, and a bounded negative conclusion. Then stop.
   - If the system makes a knowledge-production claim but no implemented route was found, give the claimed object an inventory ID. Add an absence row keyed to it, compare the claim with the absent route, mark each lifecycle route as `no route found within boundary` and each candidate state as the evidence permits, and write the mismatch and bounded conclusion. Then stop.
   - Otherwise, continue. Never expand a scoped absence into a claim that no informal or unobserved route exists.

4. **Classify content edges and direct adaptations.** Apply these rules to every content-producing or content-changing edge, in order, and split sequential transformations into separate edges:

   - External content enters the system -> **acquisition/import**; record source warrant as preserved, degraded, or unknown.
   - Truth-apt content is only reordered, indexed, grouped, reformatted, deduplicated, or compressed -> **non-ampliative reshaping**.
   - A new proposition follows from its inputs -> **entailed derivation**; carry warrant only from warranted premises through a checked interpretation or formal domain.
   - A truth-apt proposition does not follow from its inputs -> **ampliative conjecture**; novelty, fluency, and plausibility establish candidate generation only.
   - Semantic preservation or entailment cannot be established -> **indeterminate**; state the remaining classifications and evidence needed.

   When behavior changes through reward, error, gradient, or viability without an evidenced truth-apt object, use route kind **direct behavior/policy adaptation** and write `content transformation: not applicable`. For any other consequential route that does not change content, choose its route kind, write the same, and still analyse its target, condition, force, authorities, consumer, and horizon.

5. **Build the authority-route ledger.** Populate output 3. A **check target** is the object, proposition, or class and domain being assessed; name it before the evaluator. An **oracle/evaluator** is the human, model, program, environment, proof, measurement, or hybrid procedure that judges that target. An **operative result** is consumed to change admission, rejection, revision, acceptance, retention, integration, rollback, use, ranking, or continuation. **Epistemic authority** is the content and scope licensed for reliance. **Operational authority** is the later behavior permitted through a named consumer, channel, force, and horizon. A recorded result with no consequential consumer has no implemented force. Use separate rows when targets, timing, results, or force differ.

6. **Dispose every object.** Populate output 4. The **discovery lifecycle** comprises observation or anomaly, conjecture, consequence derivation, test or evidence, acceptance, and integration. Apply it only after ampliation is established. **Acceptance** is a recorded, evidence-consuming decision against a named criterion for an intended use and scope. Record integration and its consumer separately. Never use implementation evidence alone to mark an observed candidate accepted, rejected, revised, failed, or integrated. Use `no instance observed` when a route exists but no run artifact shows a candidate traversing it. Use the indeterminate, non-ampliative, per-object no-candidate, and global no-candidate branches exactly as specified.

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

- The source, claim, and material-route boundary is complete; assessed and unassessed route families, evidence layers, and prevented conclusions are explicit.
- Every operative part inside that boundary has an ID, and heterogeneous parts are split.
- Every content-changing edge is classified or bounded as indeterminate; every consequential non-content transition has a route kind and `content transformation: not applicable`.
- Every material check or transition has a route row with target before evaluator, timing, result, force, separate authorities, evidence, and limit.
- Every truth-apt object has the applicable ampliative, non-ampliative, or indeterminate disposition; every other object has the per-object no-candidate line.
- Every ampliative phase separates route availability from observed candidate state, and implementation evidence alone never establishes an observed disposition.
- Every consequential system claim is compared across evidence layers without upgrading them.
- Every negative or unknown is scoped; no license exceeds its target, contrast, domain, horizon, or route.
- The conclusion includes only decision-relevant findings, uses route-level verbs, and gives no system-wide epistemic grade.
- The analysis informs review but does not accept the system's claims.
