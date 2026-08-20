---
description: Workshop baseline for analysing persistent material, memory writes and maintenance, later consumption and read-back, context efficiency, activation evidence, and lifecycle controls in an agentic system.
type: kb/types/instruction.md
---

# Analyse Memory and Context Persistence

Use this procedure when the parent agentic-system analysis finds that system-, user-, project-, or run-specific material persists across invocation boundaries and a later consumer can use it to shape behavior. Analyse the persistence and consumption routes inside the parent's system boundary and reviewed revision.

This is a workshop extraction of the functioning agent-memory review contract. It does not decide whether newly produced truth-apt content is warranted knowledge; hand those routes to the epistemic lens. It also does not own checkout preparation, publication layout, comparison with Commonplace, curiosity passes, indexes, or validation.

## Definitions and boundary

- A **retained artifact** is state that persists across time and can later be consumed in a behavior-shaping path.
- An **operative part** is the content, structure, parameterization, or mechanism inside an artifact or consumption path that actually affects behavior.
- **Write side** covers every route that changes retained material.
- **Consumption** covers later use by a model, runtime, router, retriever, validator, reviewer, scheduler, human, or learning loop.
- **Read-back** is the return of material accumulated or changed through use into a later agent action, by deliberate lookup (`pull`) or unsolicited arrival (`push`). Static shipped documentation is retained system definition, not memory read-back.
- **Activation** is stronger than read-back: the supplied material changes what a consumer notices, decides, says, checks, or does.

Receive the shared system boundary, source IDs, evidence layers, runtime object/route IDs, and lens-applicability evidence from the parent. Do not establish a second revision or silently widen the inspected host boundary.

## Required output

Produce these six blocks in order.

### 1. Memory applicability and boundary

`disposition: applies/uncertain | retained scope | host/runtime boundary | candidate artifact and route IDs from parent | included persistence/consumption routes | excluded routes | source IDs | missing evidence -> conclusion prevented`

If inspection shows that only static shipped material persists and no system-, user-, project-, or run-specific material can affect a later invocation, return `does not apply within boundary` with evidence and stop. Do not create the remaining blocks merely to fill a template.

### 2. Retained-artifact inventory

Use one row per operative part. Split a container when parts differ in form, lineage, consumers, or authority paths.

`memory object id | system name/description | storage substrate | representational form | lineage and source | producer | later consumer | behavioral-authority path: consumer, channel, force, horizon | invalidation/regeneration dependency | evidence source ID/anchor | gap/limit`

Use the current stable vocabularies where they fit:

- storage substrate: `files`, `repo`, `sqlite`, `rdbms`, `vector`, `graph`, `kv`, `in-memory`, `prompt-registry`, `model-weights`, `service-object`, or a separately described substrate;
- representational form: `natural-language`, `symbolic`, `parametric`, listing each operative part rather than using `mixed`;
- lineage: `authored`, `imported`, `trace-extracted`, `other-compiled`, or a separately described evidenced lineage; and
- authority force: advice, instruction, enforcement, routing, validation, ranking, evaluation, learning input, or another described force.

Mark a value `not determinable` rather than inferring it from storage labels or product language.

### 3. Write and maintenance routes

Use one row per consequential store-changing route.

`write route id | target object id | trigger | agency: manual/automatic | source/input | operation | transformation/output | evaluator or condition | retention/replacement effect | provenance preserved/degraded/unknown | evidence source ID/anchor | gap/limit`

Classify automatic operations over already-retained material when applicable:

- `consolidate` — reductively summarize or abstract without adding a proposition absent from the inputs;
- `dedup` — detect and merge redundancy;
- `evolve` — modify an existing entry in light of new material without merging or deleting it;
- `synthesize` — produce a new entry asserting content no input stated;
- `invalidate` — supersede or mark stale while retaining history;
- `decay` — remove or down-weight by age, recency, or capacity; and
- `promote` — change tier or salience without changing content.

Creating, importing, uploading, extracting, or indexing an entry is acquisition, not automatically a curation operation. Index and embedding rebuilds are access-structure upkeep unless they change retained content or authority.

For trace-fed writes, record trace source, extraction judge, scope, timing, raw artifact, distilled artifact, and the route by which the distilled result affects later behavior. Durable trace-derived output does not by itself establish learning quality or epistemic warrant.

If a write creates or changes truth-apt content, pass its object and route IDs to the epistemic lens. `Synthesize` marks novelty relative to inputs, not acceptance or truth.

### 4. Consumption and read-back routes

Use one row per materially different later-use path.

`consumption route id | object id | consumer | pull/push/other consumption | trigger | selection signal | scope and budget | assembly/injection point | channel | force | horizon | observed activation/faithfulness evidence | evidence source ID/anchor | gap/limit`

For agent-context read-back:

- `pull` means the agent deliberately looks up the retained material;
- `push` means it arrives without that agent's deliberate lookup, including orchestrator or human retrieval injected into the receiving agent;
- a push signal is `coarse` when always-loaded or keyed only by a broad occasion, `identifier` when keyed by a designed identifier, or `inferred / lexical`, `inferred / embedding`, or `inferred / judgment` when relevance is computed from content;
- record the occasion that assembles the next call, not a fictitious post-action read. Capture, consolidation, re-indexing, decay, and other after-turn work are write-side routes.

For every path, distinguish the observable serving mechanism from unverified precision, recall, dilution, effective authority, or action improvement. A faithfulness claim requires the system to compare behavior with and without the material, perturb it, audit its use, or provide other evidence that the read-back changed action.

### 5. Lifecycle, trust, and context-efficiency controls

`control id | object/route IDs | provenance/source preservation | versioning/history | freshness/invalidation | conflict handling | deletion/decay | rollback/recovery | access/privacy boundary | context-volume control | context-complexity control | evidence source ID/anchor | effectiveness evidence or not tested`

Describe implemented controls and their wired consumers. Do not infer trust from inspectability, metadata from correctness, or a configured token limit from preserved relevance.

### 6. Bounded memory/context conclusion and handoffs

State only decision-relevant findings:

- what persists, in which operative forms, and with what lineage;
- who or what writes, maintains, selects, and consumes it;
- which later-use routes are pull, push, or non-context consumption;
- how selection bounds volume and complexity;
- what behavioral authority each material path has;
- whether activation or downstream improvement is tested or merely assumed;
- which lifecycle controls are implemented and wired; and
- which truth-apt transformations and knowledge claims require epistemic analysis, and which direct policy adaptations remain runtime findings or must join an independently triggered epistemic analysis.

End with:

`Epistemic handoff: object/route IDs + reason + applicability basis, or none within boundary.`

Do not call the system knowledge-producing, learning, trustworthy, or effective solely because it stores, transforms, retrieves, injects, or later consumes material.

## Steps

1. Confirm applicability at the parent's boundary and revision.
2. Inventory behavior-shaping operative parts, not every stored file or row.
3. Trace each material write from source through mutation and retention.
4. Trace each later-use path to its actual consumer and force.
5. Separate read-back availability from behavioral activation and measured outcome improvement.
6. Record lifecycle, provenance, recovery, access, and context-efficiency controls only where they are implemented or explicitly declared.
7. Hand truth-apt transformations and claims to the epistemic lens using stable IDs.
8. Conclude within the evidence layer and host boundary.

## Misuse guards

- Do not treat storage as read-back, read-back as activation, or activation as improvement.
- Do not classify static shipped documentation as accumulated memory merely because it enters every prompt.
- Do not infer deployed push from a library callback without inspecting host wiring.
- Do not call acquisition a curation operation or an index rebuild a content transformation.
- Do not call consolidation synthesis unless the output asserts content absent from its inputs.
- Do not call synthesis knowledge production without analysing warrant, acceptance, and authority routes.
- Do not attach one authority to an entire file or database when its operative parts have different consumers or force.
- Do not infer quality from code paths that only show capability, configured policy, or retention.

## Verify

- Applicability is evidenced and scoped.
- Every central retained artifact is split into operative parts where form, lineage, or authority differs.
- Write-side and later-consumption routes remain separate.
- Every authority statement names consumer, channel, force, and horizon.
- Read-back direction and targeting are judged from the receiving agent's perspective.
- Context-volume controls and context-complexity controls are both addressed.
- Activation and effectiveness claims have observed or causal evidence, or are marked untested.
- Every truth-apt transformation or warrant claim has an epistemic handoff.
