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
- the declared scope: memory subsystem, whole agentic system, named routes, included external actors or services, and excluded components;
- the analysis question;
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

Keep these evidence layers separate:

- **Implementation:** inspected executable behavior.
- **Doctrine/design:** declared intent or contract.
- **Reported operation:** an attributed report without inspectable run evidence.
- **Observed run:** an inspectable execution trace or artifact.
- **Causal experiment:** an observed interventional comparison plus evidence about its design. A contrast is necessary but not sufficient for causal identification. State design and confounding limits, and attribute no more finely than the actual treatment and comparison.

In standalone use, assign every source a stable ID in output 1. Map the ID to its identity or revision and evidence layer. Later records may cite the ID plus a **local anchor**: a source-local section, symbol, line, event, artifact, or other available locator. In orchestrated overlay mode below, cite the supplied canonical `SRC-*` IDs instead.

Do not upgrade one evidence layer into another. Inspect each representational form appropriately: read natural-language content, test symbolic artifacts within their declared semantics, and use available probes for distributed-parametric state. If the available probes cannot individuate truth-apt content, record the object or lifecycle phase as `not determinable`.

Apply these scope branches before continuing:

- If the task is product ranking, adoption advice, ontology design, or a general review with no knowledge-production question, stop and use a method suited to that task.
- If no inspectable source boundary or revision can be established, produce only output 1 with `insufficient evidence` and name each conclusion the missing evidence prevents.
- Treat an intentionally operational or lab-tracking purpose as a scope boundary, not as product failure. Do not prescribe natural-language claims, proposal comparison, a storage model, or a universal knowledge ontology.

## Orchestrated overlay mode

When `analyse-agentic-system` invokes this procedure with canonical source, object, route, claim, and authority records, preserve the six analytical blocks below but return them as a sparse overlay rather than a second inventory. In output 1, identify the supplied source-register boundary and cite its canonical `SRC-*` IDs without copying the register. In later outputs, use the supplied canonical IDs. For local readability, repeat at most the canonical ID, one source-native short label, and one local evidence anchor before the epistemic fields; these repetitions do not redefine the canonical record. Where a standalone output field is canonical-owned, write `see <canonical ID>` rather than copying its value. Do not copy generic identity, representational form, storage substrate, common route endpoints or progression, or claimed-operation identity.

A newly discovered object, route, claim, absence, or authority path uses an invocation-local proposal tag and supplies the full identity needed for orchestrator registration; it never mints a canonical ID. Return a targeted-read request for new source material and a correction with its evidence anchor for a defective canonical fact. When an invoking packet exists, its accepted blocks and required fields govern the return envelope; otherwise the orchestrator's linked-return contract governs. Without supplied canonical records, use the standalone stable-ID rules below.

## Required output

Produce these six blocks in order. Use readable Markdown tables or compact records.

### 1. Source-and-claim boundary

Use these fields:

`system | reviewed revision/version | declared scope and excluded components | analysis question | assessed route families | unassessed route families | source register: source ID -> identity/revision + evidence layer | missing evidence -> conclusion prevented | system knowledge-production/warrant claims -> claim ID + source ID/anchor, or none found`

### 2. Epistemic-object inventory

Use one row per operative part within the material-route boundary. Assign stable IDs in standalone use; in orchestrated overlay mode, use the supplied canonical ID or a local proposal tag. Split parts that differ in content, form, checks, producers or consumers, or authority paths.

`object/part id | system name and description | representational form | source/input and lineage | producer/consumer | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit`

### 3. Authority-route ledger

Use one row per consequential function. Assign stable IDs in standalone use; in orchestrated overlay mode, use the supplied canonical ID or a local proposal tag. Split rows when the function, target, evaluator domain, timing, result, force, epistemic license, operational consequence, consumer, channel, or horizon differs. Record an evidenced absence without inventing an evaluator.

`route id | route function | architectural status | object/candidate id | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit`

Use one functional kind per row: `content transformation`, `check/evidence production`, `disposition/acceptance`, `retention`, `lifecycle integration`, `operational admission/selection/consumption`, `behavior/policy adaptation`, `lineage/freshness/recovery`, or `other — describe`. If one implementation performs several functions, use linked rows. Never merge checking with disposition or retention with lifecycle integration.

Record **architectural status** independently of function:

- `implemented` — inspected implementation supports the route;
- `observed, implementation uninspected` — run evidence shows the route operated, but its implementation was not inspected;
- `doctrine only` — a route is declared, but no implementation or observed route was found within the recorded search boundary;
- `no route found within boundary` — neither inspected implementation, observed operation, nor doctrine establishes the route within the recorded search boundary; or
- `not determinable` — the available evidence cannot distinguish these states.

Record activation conditions separately; an implemented route may be conditional or inactive in the inspected configuration.

For `content/update relation`, use one of:

- `truth-apt transformation: acquisition/import`, `non-ampliative reshaping`, `entailed derivation`, `ampliative conjecture`, or `indeterminate`;
- `non-truth-apt policy/content update: <description>`; or
- `no content change`.

### 4. Per-object lifecycle disposition

For every ampliative truth-apt candidate, key one record to its object ID and relevant route IDs. For each phase, record the route's architectural status separately from the observed candidate state and cite the evidence layer through its source ID.

Use these **observed candidate states**:

- `no instance observed` — no candidate artifact or trace is available within the evidence boundary;
- `not reached` — an observed candidate exists and evidence shows that it did not reach this phase;
- `phase evidenced` — an observed candidate traversed this phase;
- `accepted`, `rejected`, `revised`, `failed`, `suspended`, or `integrated` — an observed disposition supports that specific state; or
- `not determinable` — candidate evidence exists but does not determine the state.

Implementation or doctrine alone cannot establish an observed candidate state. Use `suspended` only for an observed candidate deliberately held pending, not for a disabled implementation route.

Example: observed-run evidence contains a persisted claim artifact `OBJ-7`, while implementation evidence contains conjecture, test, and acceptance routes `RTE-3` through `RTE-5`, but no provenance or trace links that artifact to any route. The artifact establishes that a candidate instance is available; it does not establish that any particular production phase ran. Record each route's architectural status as `implemented`. Record the observed candidate state for conjecture, test/evidence, and acceptance as `not determinable`, not `phase evidenced` or `accepted`. Upgrade one phase only from candidate-linked evidence of that phase. If neither a candidate artifact nor a candidate-linked trace exists, use `no instance observed`.

Use this schema:

`candidate object ID | relevant route IDs | transformation: ampliative conjecture | observation/anomaly: route IDs + architectural status + observed candidate state + evidence | conjecture: route IDs + architectural status + observed candidate state + evidence | derived consequence: route IDs + architectural status + observed candidate state + evidence | test/evidence: route IDs + architectural status + observed candidate state + evidence | acceptance: route IDs + evaluator + criterion + intended use + architectural status + observed candidate state + accepted scope + evidence | lifecycle integration: route IDs + post-acceptance change/consumer + architectural status + observed candidate state + evidence | missing phase/evidence`

Lifecycle **integration** occurs only after acceptance, when the accepted claim is connected to evidence or changes organization or use. Retention or operational use before acceptance is not lifecycle integration; keep it in separate ledger rows. If an observed candidate was retained or used without acceptance, mark lifecycle integration `not reached`. If no candidate instance was observed, use `no instance observed`.

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

`claim id | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown`

### 6. Bounded conclusion

State only findings that change the answer to the analysis question. Group homogeneous object or route IDs when their warrant and force are the same. Cover:

- what the system retains, retrieves, reshapes, or uses;
- what it acquires and whether source warrant is preserved, degraded, or unknown;
- what it derives, from which warranted premises, and within what domain;
- what it conjectures, tests, accepts, and integrates;
- each material acceptance criterion, intended use, scope, operational authority, and behavioral-authority path;
- any direct behavior or policy adaptation without a truth-apt route; and
- which claims remain unsupported because implementation, run, or causal evidence is missing.

Do not give the system a single epistemic score, oracle, status, or unqualified verdict.

## Steps

1. **Fix the boundary.** Populate output 1. Record the declared system boundary and exclusions. Assign each source an evidence layer and stable ID. State every gap and exactly what conclusion it prevents.

2. **Inventory material objects before evaluators.** Populate output 2. An **epistemic object** is the concrete typed part whose content or status a route produces, checks, accepts, or consumes. Apply the material-route rule, name omitted route families, use system-specific object names, and split heterogeneous containers. Name each target object or proposition and its domain before assessing any evaluator.

3. **Apply the early branch.**

   - If the inventory shows only storage, retrieval, serving, or direct use, with no relevant transformation and no knowledge-production claim, add a ledger row for each material evidenced function or an explicit `no relevant route found`. Record no relevant check or epistemic authority within the boundary, any operational and behavioral authority, the global no-candidate statement, an explicit no-claim comparison, and a bounded negative conclusion. Then stop.
   - If the system makes a knowledge-production claim but no implemented or observed route supporting that claim was found, inventory the claimed object and first classify its claimed transformation. If ampliation is established by the claim evidence, use the lifecycle schema: mark declared phases `doctrine only`, unclaimed phases as the scoped evidence permits, and every unobserved candidate phase `no instance observed`. If ampliation is not established, use the non-ampliative or indeterminate disposition instead. Add ledger rows for the claimed functions and compare the claim with the absent supporting implementation or operation. If this disposes every material route in the declared boundary, write the bounded conclusion and stop. Otherwise continue at step 4 with the remaining implemented or observed routes; never let this claim branch discard them.
   - Otherwise, continue. Never expand a scoped absence into a claim that no informal or unobserved route exists.

4. **Classify content edges and direct adaptations.** Apply these rules to every truth-apt content-producing or content-changing edge, in order, and split sequential transformations into separate edges:

   - External content enters the system -> **acquisition/import**; record source warrant as preserved, degraded, or unknown.
   - Truth-apt content is only reordered, indexed, grouped, reformatted, deduplicated, or compressed -> **non-ampliative reshaping**.
   - A new proposition follows from its inputs -> **entailed derivation**; carry warrant only from warranted premises through a checked interpretation or formal domain.
   - A truth-apt proposition does not follow from its inputs -> **ampliative conjecture**; novelty, fluency, and plausibility establish candidate generation only.
   - Semantic preservation or entailment cannot be established -> **indeterminate**; state the remaining classifications and evidence needed.

   For a behavior or policy adaptation with no evidenced truth-apt object, describe any changed non-truth-apt policy/content and do not force it into the truth-apt transformation classes. For a consequential route with no content update, write `no content change` and still analyse its function, target, condition, force, authorities, consumer, and horizon.

5. **Build the authority-route ledger.** Populate output 3. A **check target** is the object, proposition, or class and domain being assessed; name it before the evaluator. An **oracle/evaluator** is the human, model, program, environment, proof, measurement, or hybrid procedure that judges that target. An **operative result** is consumed to change admission, rejection, revision, acceptance, retention, integration, rollback, use, ranking, or continuation. **Epistemic authority** is the content and scope licensed for reliance. **Operational authority** is the behavior a result permits, blocks, or changes before another check. A **behavioral-authority path** is the consumer, channel, force, and horizon through which an artifact or result affects behavior; its force may be advisory, ranking, permissive, or enforcing. A recorded result with no consequential consumer has no implemented force. Use separate linked rows as required by the ledger's split rule.

6. **Dispose every object.** Populate output 4. The **discovery lifecycle** comprises observation or anomaly, conjecture, consequence derivation, test or evidence, acceptance, and integration. Apply it only after ampliation is established. **Acceptance** is a recorded, evidence-consuming decision against a named criterion for an intended use and scope. Record post-acceptance integration separately from retention and pre-acceptance use. Apply the architectural-status and observed-candidate-state rules exactly. Use the indeterminate, non-ampliative, per-object no-candidate, and global no-candidate branches where specified.

7. **Bound each check's licenses.** For every ledger row, state what the result warrants, what it permits or changes operationally, how it becomes behaviorally consequential, and what it does not establish. Keep separate:

   - outcome from producing process, explanation, replay safety, transfer, and component effect;
   - a valid reconstructed route from evidence that it produced the observed outcome;
   - consequence fit from warrant for the proposed mechanism and its transfer boundary;
   - formal validity from source truth, encoding fidelity, omitted premises, and claims outside the formal domain;
   - applicability or freshness from endorsement;
   - operational continuation from epistemic warrant; and
   - bundle success from the effect of an individual component.

   Attribute a component effect only when the observed comparison independently varied that component, and only at the grain of the actual contrast. State why the design does or does not license a causal interpretation.

8. **Compare claims with routes.** Populate output 5. Compare each claim across doctrine/design, implementation, observed-run, and causal evidence. Record a deliberately operational scope without treating it as failure, but still expose any mismatch between that scope and a broader knowledge-production claim.

9. **Conclude by route.** Populate output 6. Report imported content as acquired, not produced. Report an entailed output as derived warranted content only when its premises and derivation are warranted within the declared domain. Report a non-entailed truth-apt output as a produced accepted ampliative claim only when an evidence-consuming acceptance transition names its criterion, intended use, and scope. Retention, retrieval, reshaping, direct adaptation, operational use, or candidate generation alone does not qualify as knowledge production. Report acceptance and post-acceptance integration separately. Do not turn acceptance into infallibility, integration into acceptance, or one route's result into a system label.

## Misuse guards

- Do not infer knowledge production from storage, retrieval, injection, later use, behavioral influence, novelty, fluency, or plausibility alone.
- Do not infer acceptance from retention, labels, grades, reports, freshness, or unconsumed results.
- Do not call retention or pre-acceptance use lifecycle integration.
- Do not transfer an outcome pass to the producing process, explanation, replay safety, transfer, or component effect.
- Do not transfer proof or formal validity to source truth, encoding fidelity, omitted premises, or claims outside the checked domain.
- Do not assign one evaluator, status, or authority to heterogeneous routes.
- Do not upgrade doctrine or purpose to implementation, or treat intentionally operational scope as product failure.
- Do not require natural-language claims, a proposal loop, Commonplace storage, or a universal ontology.

## Verify

- The source, claim, declared-scope, and material-route boundary is complete; included/excluded components, assessed/unassessed route families, source-ID register, evidence layers, and prevented conclusions are explicit.
- Every operative part inside that boundary has an ID, and heterogeneous parts are split.
- Every route has one function and a separate architectural status; checks/dispositions and retention/lifecycle integration are not merged.
- Every truth-apt content edge is classified or bounded as indeterminate; every non-truth-apt update is described without forcing it into that taxonomy; every route with no content update says so.
- Every material function has a route row with target before evaluator, activation/timing, result, force, epistemic authority, operational authority, behavioral-authority path, evidence, claim IDs, mismatch marker, and limit.
- Every truth-apt object has the applicable ampliative, non-ampliative, or indeterminate disposition; every other object has the per-object no-candidate line.
- Every ampliative phase separates architectural status from observed candidate state, and implementation or doctrine alone never establishes an observed disposition.
- Lifecycle integration is post-acceptance; retention and pre-acceptance use remain separate ledger functions.
- Every consequential system claim is compared across evidence layers without upgrading them, and every causal conclusion states its design limits.
- Every negative or unknown is scoped; no license exceeds its target, contrast, domain, horizon, or route.
- The conclusion includes only decision-relevant findings, uses route-level verbs, and gives no system-wide epistemic grade.
- The analysis informs review but does not accept the system's claims.
