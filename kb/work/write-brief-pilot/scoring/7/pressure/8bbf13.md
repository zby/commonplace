---
description: Determine whether and how an external memory subsystem or agentic system produces knowledge by tracing its epistemic objects, transformations, warrant, and authority routes.
type: types/instruction.md
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

Assign every source a stable ID in output 1. Map the ID to its identity or revision and evidence layer. Later records cite the ID plus a **local anchor**: a source-local section, symbol, line, event, artifact, or other available locator.

Do not upgrade one evidence layer into another. Inspect each representational form appropriately: read natural-language content, test symbolic artifacts within their declared semantics, and use available probes for distributed-parametric state. If the available probes cannot individuate truth-apt content, record the object or lifecycle phase as `not determinable`.

Apply these scope branches before continuing:

- If the task is product ranking, adoption advice, ontology design, or a general review with no knowledge-production question, stop and use a method suited to that task.
- If no inspectable source boundary or revision can be established, produce only output 1 with `insufficient evidence` and name each conclusion the missing evidence prevents.
- Treat an intentionally operational or lab-tracking purpose as a scope boundary, not as product failure. Do not prescribe natural-language claims, proposal comparison, a storage model, or a universal knowledge ontology.

## Required output

Produce these six blocks in order. Use readable Markdown tables or compact records, except for output 3, which has a fixed table format.

Use these ID forms in every block, because other reviews and invoking workflows compare records by ID:

- `SRC-n` for sources, `CLM-n` for system claims, `OBJ-n` for objects, and `RTE-n` for routes. Number each series in order of first record. Never reuse or renumber an ID.
- Write every ID in full and separate several with commas: `OBJ-1, OBJ-2`, never `OBJ-1/2` or a range.
- Cite evidence as `SRC-n <local anchor>`; separate several citations with semicolons.
- If an invoking workflow supplies canonical IDs, use them unchanged and give new records IDs in the same form.

### 1. Source-and-claim boundary

Use these fields:

`system | reviewed revision/version | declared scope and excluded components | analysis question | assessed route families | unassessed route families | source register: source ID -> identity/revision + evidence layer | missing evidence -> conclusion prevented | system knowledge-production/warrant claims -> claim ID + source ID/anchor, or none found`

### 2. Epistemic-object inventory

Use one row per operative part within the material-route boundary and assign stable IDs. Split parts that differ in content, form, checks, producers or consumers, or authority paths.

`object/part id | system name and description | representational form | source/input and lineage | producer/consumer | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit`

### 3. Authority-route ledger

Use one row per consequential function. Split rows when the function, target, evaluator domain, timing, result, force, epistemic license, operational consequence, consumer, channel, or horizon differs. Record an evidenced absence without inventing an evaluator.

The ledger format is fixed so that ledgers from different reviews line up column by column. Write one Markdown table with exactly these columns, in this order and with these headers:

`route id | object id | route function | architectural status | activation condition | timing | content/update relation | check target | evaluator and domain | result | force | epistemic authority | operational authority | consumer | channel | horizon | evidence | claim IDs | mismatch | gap/limit`

Fill the cells by these rules:

- Put one value in each cell. Do not add, drop, rename, or merge columns; put any further detail in `gap/limit`.
- Never leave a cell blank. Write `none` for an absence evidenced within the boundary, `not determinable` when the evidence cannot decide, and `not applicable` when the column does not apply to the row's function, such as `evaluator and domain` on a retention row.
- Where a column below lists values, use one of them verbatim. Use `other — <description>` only when none fits.
- Order rows by object ID, then by route function in the order listed below, then by route ID.

Column values:

- `route function`: `content transformation`, `check/evidence production`, `disposition/acceptance`, `retention`, `lifecycle integration`, `operational admission/selection/consumption`, `behavior/policy adaptation`, or `lineage/freshness/recovery`. If one implementation performs several functions, give each function its own row and cite the same evidence. Never merge checking with disposition or retention with lifecycle integration.
- `architectural status`: one of the five statuses defined below.
- `activation condition`: `always`, `when <condition>`, or `inactive in inspected configuration`.
- `timing`: `on write`, `on read`, `per turn`, `scheduled: <schedule>`, `on demand`, or `on event: <event>`.
- `content/update relation`: one of the values defined below.
- `check target`: the object, proposition, or class and its domain that the route assesses or changes.
- `result`: `possible: <values>` when only implementation or doctrine shows the result set; `observed: <values>` when run evidence shows it.
- `force`: `enforcing`, `permissive`, `ranking`, `advisory`, or `none`. Write `none` for a recorded result that no consequential consumer reads.
- `epistemic authority`: `none`, or `<content licensed for reliance> within <scope>`.
- `operational authority`: `none`, or `permits: <behavior>`, `blocks: <behavior>`, or `changes: <behavior>`.
- `consumer`, `channel`, `horizon`: the behavioral-authority path, with `force` above as its fourth part. For `horizon` use `single call`, `session`, `until revised or deleted`, or `fixed period: <period>`.
- `evidence`: `SRC-n <local anchor>` citations.
- `claim IDs`: `CLM-n` IDs this row bears on, or `none`.
- `mismatch`: `none`, or `<claim ID>: <what the claim asserts that this row does not support>`.

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

## Worked example

This example is invented to show the output format and the main distinctions. It does not describe a real system. It is abbreviated: a real analysis fills every field of outputs 1, 2, 4, and 5, and would also record the acquisition/import route and non-ampliative disposition for `OBJ-1`, which are omitted here.

The system is a memory plugin. After each conversation, an LLM reads the transcript and writes short "facts" about the user to a store. Each later turn retrieves the five facts most similar to the prompt and puts them in the system prompt. The README says the plugin "learns verified facts about you."

**1. Boundary.** Scope: the memory plugin; the host agent is excluded. Sources: `SRC-1` repository at commit `a1b2c3` (implementation); `SRC-2` README (doctrine/design); `SRC-3` one exported run log (observed run). Missing evidence: no causal experiment, so no conclusion about whether retrieved facts improve answers. Claims: `CLM-1` "learns verified facts about you" (`SRC-2 Features`).

**2. Objects.** `OBJ-1` transcript: natural-language input from the user. `OBJ-2` fact record: one natural-language sentence plus an embedding, produced by the extractor LLM and consumed by the retriever; candidate truth-apt content, a proposition about the user.

**3. Ledger** (all 20 columns, as required):

| route id | object id | route function | architectural status | activation condition | timing | content/update relation | check target | evaluator and domain | result | force | epistemic authority | operational authority | consumer | channel | horizon | evidence | claim IDs | mismatch | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTE-1 | OBJ-2 | content transformation | implemented | always | on event: conversation end | truth-apt transformation: ampliative conjecture | not applicable | not applicable | observed: fact written | permissive | none | permits: fact creation | store | write call | until revised or deleted | SRC-1 extract.py:extract_facts; SRC-3 event 14 | CLM-1 | none | the prompt asks for inferred preferences, so facts need not be stated in the transcript |
| RTE-2 | OBJ-2 | check/evidence production | no route found within boundary | not applicable | not applicable | no content change | OBJ-2 proposition about the user | none | none | none | none | none | none | none | not applicable | SRC-1 whole-repository search for validation or confirmation | CLM-1 | CLM-1: "verified" asserts a check that no route performs | search boundary is SRC-1 only |
| RTE-3 | OBJ-2 | retention | implemented | always | on write | no content change | not applicable | not applicable | observed: fact stored | permissive | none | permits: later retrieval | retriever | vector store | until revised or deleted | SRC-1 store.py:add; SRC-3 event 15 | none | none | none |
| RTE-4 | OBJ-2 | operational admission/selection/consumption | implemented | always | per turn | no content change | OBJ-2 relevance to current prompt | embedding similarity, top 5 | observed: 5 facts injected | advisory | none | changes: system prompt content | host agent LLM | system prompt | single call | SRC-1 retrieve.py:top_k; SRC-3 event 22 | CLM-1 | none | effect on answers not determinable without a causal experiment |

**4. Lifecycle for `OBJ-2`** (ampliative): conjecture — `RTE-1`, `implemented`, `phase evidenced` (`SRC-3 event 14`). Test/evidence — `RTE-2`, `no route found within boundary`, `not reached`. Acceptance — no route, `not reached`. Lifecycle integration — `not reached`: the fact was retained (`RTE-3`) and used (`RTE-4`) without acceptance, which is not integration.

**5. Claims.** `CLM-1`: doctrine only; no check or acceptance route (`RTE-2`); supported conclusion: the plugin stores and uses conjectured facts; mismatch: "verified".

**6. Conclusion.** The plugin generates ampliative conjectures about the user (`RTE-1`), retains them (`RTE-3`), and injects them into prompts with advisory force for a single call (`RTE-4`). No route checks or accepts a fact, so it produces candidates, not knowledge. `CLM-1` is unsupported. Whether the facts improve answers is unknown.

## Steps

1. **Fix the boundary.** Populate output 1. Record the declared system boundary and exclusions. Assign each source an evidence layer and stable ID. State every gap and exactly what conclusion it prevents.

2. **Inventory material objects before evaluators.** Populate output 2. An **epistemic object** is the concrete typed part whose content or status a route produces, checks, accepts, or consumes. Apply the material-route rule, name omitted route families, use system-specific object names, and split heterogeneous containers. Name each target object or proposition and its domain before assessing any evaluator.

3. **Apply the early branch.**

   - If the inventory shows only storage, retrieval, serving, or direct use, with no relevant transformation and no knowledge-production claim, add a ledger row for each material evidenced function or an explicit `no relevant route found`. Record no relevant check or epistemic authority within the boundary, any operational and behavioral authority, the global no-candidate statement, an explicit no-claim comparison, and a bounded negative conclusion. Then stop.
   - If the system makes a knowledge-production claim but no implemented or observed route was found, inventory the claimed object and first classify its claimed transformation. If ampliation is established by the claim evidence, use the lifecycle schema: mark declared phases `doctrine only`, unclaimed phases as the scoped evidence permits, and every unobserved candidate phase `no instance observed`. If ampliation is not established, use the non-ampliative or indeterminate disposition instead. Add ledger rows for claimed functions, compare the claims with the absent implementation/operation, and write a bounded conclusion. Then stop.
   - Otherwise, continue. Never expand a scoped absence into a claim that no informal or unobserved route exists.

4. **Classify content edges and direct adaptations.** Apply these rules to every truth-apt content-producing or content-changing edge, in order, and split sequential transformations into separate edges:

   - External content enters the system -> **acquisition/import**; record source warrant as preserved, degraded, or unknown.
   - Truth-apt content is only reordered, indexed, grouped, reformatted, deduplicated, or compressed -> **non-ampliative reshaping**.
   - A new proposition follows from its inputs -> **entailed derivation**; carry warrant only from warranted premises through a checked interpretation or formal domain.
   - A truth-apt proposition does not follow from its inputs -> **ampliative conjecture**; novelty, fluency, and plausibility establish candidate generation only.
   - Semantic preservation or entailment cannot be established -> **indeterminate**; state the remaining classifications and evidence needed.

   For a behavior or policy adaptation with no evidenced truth-apt object, describe any changed non-truth-apt policy/content and do not force it into the truth-apt transformation classes. For a consequential route with no content update, write `no content change` and still analyse its function, target, condition, force, authorities, consumer, and horizon.

5. **Build the authority-route ledger.** Populate output 3. A **check target** is the object, proposition, or class and domain being assessed; name it before the evaluator. An **oracle/evaluator** is the human, model, program, environment, proof, measurement, or hybrid procedure that judges that target. An **operative result** is consumed to change admission, rejection, revision, acceptance, retention, integration, rollback, use, ranking, or continuation. **Epistemic authority** is the content and scope licensed for reliance. **Operational authority** is the behavior a result permits, blocks, or changes before another check. A **behavioral-authority path** is the consumer, channel, force, and horizon through which an artifact or result affects behavior; its force may be advisory, ranking, permissive, or enforcing. A recorded result with no consequential consumer has no implemented force. Use separate rows as required by the ledger's split rule, and follow the ledger's fixed columns, cell rules, and values.

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
- IDs follow the `SRC-n`, `CLM-n`, `OBJ-n`, `RTE-n` forms or the invoking workflow's canonical IDs. The ledger has exactly the fixed columns in order, no blank cells, one value per cell, listed values used verbatim, and the fixed row order.
- Every truth-apt object has the applicable ampliative, non-ampliative, or indeterminate disposition; every other object has the per-object no-candidate line.
- Every ampliative phase separates architectural status from observed candidate state, and implementation or doctrine alone never establishes an observed disposition.
- Lifecycle integration is post-acceptance; retention and pre-acceptance use remain separate ledger functions.
- Every consequential system claim is compared across evidence layers without upgrading them, and every causal conclusion states its design limits.
- Every negative or unknown is scoped; no license exceeds its target, contrast, domain, horizon, or route.
- The conclusion includes only decision-relevant findings, uses route-level verbs, and gives no system-wide epistemic grade.
- The analysis informs review but does not accept the system's claims.
