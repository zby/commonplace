---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agentic system — an agent runtime, harness, orchestration framework, or agent operating layer, or any narrower system whose deployed behavior depends on model calls plus surrounding machinery."
type: kb/types/instruction.md
user-invocable: true
argument-hint: "<system identifier> plus source input (repository reference, checkout path, snapshot/bundle, or documents)"
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
---

# Analyse an Agentic System

Analyse one external agentic system at one frozen evidence boundary. Run a mandatory runtime baseline, then run both the memory/context lens and the epistemic lens at a depth proportionate to what the evidence supports, reconcile shared records by stable IDs, and return one bounded system synthesis. The consumer is an analysing agent or maintainer; the channel is explicit invocation or trigger-matched skill loading; the force is a prescriptive analysis and result-writing policy.

Do not produce product rankings, generic adoption advice, a universal taxonomy or maturity ladder for agentic systems, or any claim beyond the declared evidence boundary. This skill owns the whole run: source preparation, lens scoping, lens execution, reconciliation, the logical result, verification, and reporting. The agent executing this skill is the orchestrator referred to below; lens workers execute inside its ownership and never establish their own boundary or publication.

## Prerequisites

- A named target system and at least one source input (repository reference, existing checkout, snapshot or document bundle, or accessible live documents).
- If no source input is reachable at all, stop immediately and report the missing prerequisite; do not analyse from recollection.

## Steps

### 1. Open one run and declare the boundary

1. Accept a system identifier, the source inputs, and an optional output or staging identity. Allocate one run/result ID before any analysis, in the form `AAS-<YYYY-MM-DD>-<system-slug>-<nn>`, where `nn` disambiguates runs against the same system on the same date. Every record the run produces belongs to that run, and the emitted result carries the ID as its canonical identity.
2. Confirm the subject is in scope. In scope are agent runtimes, harnesses, orchestration frameworks, and agent operating layers; separately, so is any narrower system whose deployed behavior depends on model calls it issues **or serves**. The model-call test admits narrower systems — it does not restrict the named kinds. Under either route, a system stays in scope when the model call it depends on runs outside its own boundary: deterministic machinery driven by a model that lives elsewhere qualifies, and so does a component that only serves a call it never issues, such as an MCP server or tool. If the subject matches neither route, exit early with an `out of scope` result and stop.
3. Define the reviewed boundary by function: include the components or actors whose scheduling, context selection, retained state, action execution, checking, acceptance, or authority decisions produce or constrain the behavior under review. List inclusions, exclusions, and external dependencies explicitly.
4. Name the boundary kind. Three are available, and the choice bounds what the result may conclude:
   - **whole-system** — every material loop under review sits inside the boundary; conclusions may be system-wide.
   - **subsystem-only** — the subject is one part of a larger system that is not fully inspected; conclusions cannot be whole-system.
   - **complete artifact, partial loop** — the subject is a complete, independently distributed artifact, but a material loop producing the behavior under review crosses declared external dependencies. This is the ordinary shape for an MCP server, plugin, or tool whose model and host ship separately, and for a system whose advertised loop runs partly in a host platform outside the checkout. Conclusions may be whole-artifact; they may not describe the behavior the crossing loop produces. List the external participants as named exclusions, each with the conclusion it prevents.
5. If no coherent system or subsystem boundary can be stated, treat the run as blocked: report the blocker and stop.

### 2. Freeze sources once

1. Branch by source kind:
   - Repository reference: resolve an immutable revision.
   - Existing checkout: inspect it without mutating it by default.
   - Supplied snapshot or document bundle: preserve its identity, version, or fingerprint.
   - Live or mixed documents, where capture is permitted: capture a dated inspectable boundary.
2. Record one analysis cutoff for the whole run. A dirty checkout is usable only when the exact inspected state can be identified and retained. A stable but old or partial boundary is allowed with an explicit published limitation. If no stable inspectable boundary can be established, emit a blocker report instead of a substantive analysis.
3. Build one canonical source register with `SRC-*` IDs. For each source record: kind, identity/location, revision or capture, evidence layer, inspected scope, citation anchors, and access gaps. A source whose parts carry different layers — a checkout with implementation under `src/` and doctrine under `docs/` — records each layer against the inspected scope it covers instead of flattening the whole source to one layer.
4. Freeze the sources here; finalize the evidence packet after step 4. The packet carries canonical records, and the runtime baseline is what mints them, so complete steps 2.1–2.3 and the step-3 rules, run the step-4 runtime baseline, then assemble the packet once. The packet comprises the source register, the boundary declaration, the canonical records registered by the runtime baseline, and the citation anchors relevant to each lens; anything beyond it is a targeted read under this step's rule. Lens workers must not reacquire, refresh, or widen sources. Targeted reads inside the frozen boundary are permitted, but they are added centrally to the register and they invalidate affected downstream findings, which must be redone. The packet is amendable as corrections arrive: a correction registered while a worker is in flight is checked against that worker's return on receipt, and only findings that rested on the superseded text are redone.

### 3. Fix truth conditions, definitions, and shared records

Apply these rules for the rest of the run; they keep every lens using the same words and the same objects.

#### Evidence vocabulary

- Overall tier: the analysis is `code-grounded` only when the material loops recorded in the step-4 runtime baseline rest on inspected implementation material; otherwise it is `doc-grounded`. The tier is relative to the declared boundary — judge it over the loops the boundary includes. A loop the boundary declares an external dependency neither raises nor lowers the tier, but record it as a limitation naming the conclusion it prevents, typically any claim about the behavior that loop produces. Report one tier; do not split it into parts. Mixed inspection gaps stay claim-local limitations; they do not change the tier silently.
- Per-source evidence layers: `implementation`, `doctrine/design`, `reported operation`, `observed run`, `causal experiment`.
- Conclusion statuses (use exactly these):
  - `absent` — not found within the named, recorded search boundary;
  - `inapplicable` — the stated trigger conditions are false inside that boundary; this is a finding about the system under review, never a reason to skip a lens;
  - `uninspected` — the evidence needed to decide was unavailable or not inspected;
  - `claimed` — doctrine or reported operation asserts it;
  - `afforded` — inspected code affords it, without proving deployment;
  - `observed` — a run exhibits it, without proving cause;
  - `causally supported` — intervention or comparison plus design evidence supports the attribution.
- These statuses are this instruction's namespace, and no value in it collides with the epistemic procedure invoked at step 7. That procedure carries its own vocabulary, in which `implemented` is an *architectural* status contrasting with `doctrine only`; this instruction says `afforded` for the neighbouring idea, so the two can never be silently merged. Record each vocabulary in its own terms.
- Every negative or uncertain result names the inspected boundary and the exact conclusion it prevents.
- Never upgrade: context presence to activation, implementation to observed operation, observation to causality, or operational continuation to warrant.

#### Definitions

- **Memory read-back**: material accumulated or changed through use returns to a later invocation or action. Static shipped material (documentation, tool specifications, installed skills) and ordinary current-run state are retained state, not read-back. The exclusion is per instance, not per kind: where the system itself rewrites such material using material accumulated through use, the rewritten instance is read-back and the as-shipped instance remains retained state; keep the two apart. "Current run" is the consuming agent's invocation boundary, not the host process's lifetime: material that survives from one consumer invocation to the next is read-back even when a long-lived process holds it in memory, and even when only a derived value — a count, a label set, a summary — returns rather than the content itself. Read-back is therefore easy to trigger: where it turns out to be degenerate, that is itself the finding and belongs in a brief memory lens output.
- **Activation**: evidence that delivered material changed behavior, not merely that it entered context.
- **Truth-apt**: capable of truth or falsity. A material epistemic route produces or changes truth-apt content, checks or disposes such a candidate, changes its authority, retains or integrates it for later reliance, or is required to assess a consequential knowledge or warrant claim. Operational curation labels name what a mechanism does to retained material; they do not establish semantic transformation or warrant.
- **Behavioral authority**: one consumption path, recorded in four parts — consumer (who or what receives the material), channel (how it reaches them), force (what it obliges, permits, or merely suggests), and horizon (the span over which the path keeps that force). These four definitions are complete as given; apply them without opening any other document. Example record: `{consumer: spawned lens workers; channel: injected system prompt; force: binding instruction; horizon: the single run that spawned them}`. **Epistemic authority** licenses content and scope; **operational authority** permits or blocks behavior. Keep all three separate; never collapse them into one authority label.

#### Canonical records and ownership

| Canonical record | Owner | Lens rule |
|---|---|---|
| `SRC-*` source | Orchestrator | Lenses cite; never replace boundary or evidence layer |
| `CMP-*` component, `OBJ-*` operative object | Orchestrator/runtime owns generic identity, form, substrate | Lenses extend by ID |
| `RTE-*` control/context/state/action route | Runtime owns common endpoints and progression | Memory and epistemic lenses annotate, or register one new route centrally |
| `CLM-*` claim | Orchestrator namespace | Epistemic lens owns truth, scope, and warrant fields |
| `ABS-*` evidenced absence | Orchestrator | Lenses return absences with their recorded search boundary for central registration; cite by ID |
| `BAP-*` behavioral-authority path | Orchestrator | Lenses reference; epistemic and operational authority remain lens-owned |

A record's **generic identity** is what the thing is and what it is made of — its identity, its representational form, and its storage substrate — independent of any lens's annotations. No lens may rename or independently re-inventory a registered object or route. Any new material record returns to the orchestrator for one canonical ID.

Only the orchestrator allocates canonical IDs. A lens needing a new record proposes it under a lens-local tag — `MEM-1`, `EPI-2`, unique only inside that lens — and cites it that way throughout its own return. Each proposal states the record's identity — file path, table name, route endpoints — so the orchestrator can rewrite it to a canonical ID on registration, record the mapping, and merge any proposal whose identity is already registered rather than issuing a second ID for it. Workers never mint a canonical ID: lenses running in parallel cannot see each other's numbering, so unguarded minting collides two different objects on one ID. A proposal tag is not a parallel ID namespace in the sense step 7 forbids — it is discarded at registration and never appears in the emitted result.

Register an evidenced absence as an `ABS-*` record: a finding whose status is `absent`, carrying the named, recorded search boundary that was searched and the conclusion the absence prevents or supports. An `uninspected` gap is not an absence — it stays a limitation and gets no `ABS-*` ID. Register an absence only when it bounds a conclusion someone would otherwise draw; an absence that prevents nothing has no reason to exist, and for any system infinitely many things are absent.

A lens that finds a registered record defective returns the correction with its evidence anchor instead of re-inventorying. A record is defective when it is false, when it is misclassified by the very criterion the record states, or when it is accurate as far as it goes but misleading at the scope it is stated — not only when it is outright wrong. The orchestrator amends the canonical record, preserves the superseded value, and reruns only the work that relied on it. This correction branch is distinct from the targeted-read invalidation in step 2.4: a lens that already derived its findings from the corrected source facts does not repeat its own work.

A material lens return that fits none of the record kinds — a finding *about* a registered record rather than a new component, object, route, claim, absence, or authority path, such as an output asserting something false or a lineage break between two registered records — registers as an **amendment** to the record it attaches to. An amendment carries its evidence anchor and any superseded value, and is cited through the ID of the record it annotates. Never discard a material return for lack of a namespace, and never inflate one into a new record to give it somewhere to live.

#### Worker topology

These rules govern both lenses (steps 6 and 7). Prefer fresh worker contexts that consume only the prepared evidence packet, the frozen read-only boundary, and any method document this instruction directs them to execute. If fresh workers are unavailable, execute the lens sequentially in the current context against the same registers. If neither path can run a lens, stop with an explicit capacity or dependency blocker — never record the lens as unnecessary, never let a thin scoping record stand in for an unrun lens, and never widen the evidence boundary to compensate.

If a worker terminates after producing output, its written artifact is authoritative over its own self-report and over any harness failure notice. Verify the artifact against the record set that lens was required to return; accept it when complete and redo only what is missing or unverifiable. A failure notice alone is not grounds for redoing work already written.

### 4. Run the runtime baseline (always)

1. Treat scheduling, context assembly, and external state/action as causal responsibilities, not mandatory module boundaries; one facility may span more than one.
2. For each material loop, record: trigger/input, next-step owner, decision policy and its form, context selection and framing, state reads and writes, action executor and boundary, persistence, coordination and return, retry/cancellation/recovery, and output. Link every record by canonical IDs and cite its evidence. Register the `CMP-*`, `OBJ-*`, and `RTE-*` records this baseline discovers as you go: these are the canonical records the step-2.4 packet carries. A loop is material under the same test step 4.4 applies to other surfaces: include it when it alters the analysis question, a control path, evidence strength, or a lens result. For a loop crossing a declared external dependency, record what the in-boundary artifact contributes to each field, mark the remainder as owned by the named external participant, and do not infer that participant's policy; append the limitation naming the conclusions the crossing prevents.
3. Keep the anti-conflation rules: a filesystem is not a scheduler; retaining material is not selecting it into context; a tool schema present in context is not tool execution.
4. Inspect permissions, governance, observability, providers, user interface, packaging, performance, and other surfaces only when they materially alter the analysis question, a control path, evidence strength, or a lens result — and state that materiality when you include one. Do not turn this inventory into a universal taxonomy, fixed template, maturity ladder, ranking, or adoption advice. This prohibition governs the conditional surface inventory, not the mandatory loop record in 4.2.

### 5. Scope the two lenses

Both lenses always run. This step does not decide *whether* — it decides *how deep*, and it is where the trigger evidence is named before any lens worker sees it.

For each lens (memory/context; epistemic), emit one scoping record: `{lens, trigger evidence IDs, inspected boundary, the routes and objects that evidence points the lens at, warranted depth, rationale}`.

- Warranted depth follows the evidence. Rich trigger evidence warrants a full pass; thin or degenerate evidence warrants a brief one. Thin evidence never warrants skipping a lens, and a brief pass is a result, not an omission.
- **The floor for a brief output.** However degenerate the case, a lens output states what was inventoried, what was found, and what conclusions the thinness prevents. Brevity never licenses dropping the prevented-conclusion pairing. A complete brief finding looks like "retention is total, retrieval of content is nil; branch labels are the only accumulated caller-authored text that returns" — short, specific, and bounded.
- **`uncertain` is not a scoping value and not an exit.** Evidence you cannot resolve becomes an explicit evidence limitation *inside* the lens output, paired with the conclusion it prevents. Never let it end a lens: an exit that means "we could not tell" reads to every later reader as "there is nothing there."
- An absent lens section or file must never carry meaning implicitly. Every run emits both scoping records and both lens outputs.

**Memory/context evidence.** Look for a path by which material accumulated or changed through use can affect a later invocation or action, in code, documentation, or observation. Static shipped material, ordinary current-run state, and retained material with no later delivery path are not such paths — where these are all you find, scope the lens brief rather than absent, and say so. A merely claimed path is trigger evidence; the lens output preserves whether the path is `claimed`, `afforded`, or `observed`.

**Epistemic evidence.** Look for a material route that handles truth-apt content, and for any consequential knowledge-production or warrant claim the system makes — including where the eventual finding is failure or absence. Successful knowledge production is never a prerequisite for running the lens.

**Direct-adaptation exception.** Evaluated direct behavior or policy adaptation with no truth-apt object and no knowledge or warrant claim is not an epistemic object. The exception scopes what the epistemic lens treats as its objects; it does not decide whether the lens runs. Such a route stays in the runtime account, and the scoping record names it for the orchestrator. Hand it to the invoked epistemic procedure tagged **classify-only**: that procedure classifies every content-changing edge it meets and carries a class for exactly these routes, so withholding one would leave a silent hole in its ledger. Classify-only means the route is recorded in its content/update classification and is *not* analysed for warrant, transformation, or acceptance. If the lens concludes the route is in fact truth-apt, that comes back as a correction under step 3's correction branch — never as a silent expansion of the lens's own scope.

### 6. Run the embedded memory/context lens

Analyse accumulated-from-use mechanisms; this is not a memory-review publication workflow. Work at the depth the step-5 scoping record warrants: the items below are the full pass, and a brief pass covers the same ground proportionately rather than skipping items silently.

1. Inventory retained operative parts, splitting bundled artifacts whenever content, form, producer/consumer, checks, or authority path differs. For each part record: storage substrate; representational form — how the retained content is encoded and consumed, whether natural-language, symbolic (code, schema, grammar), distributed-parametric (model weights), or mixed; persistence; lineage; producer and consumer; invalidation/regeneration conditions; and any promotion path toward stronger form or force — movement toward a more binding representation, such as natural-language note to schema or code, or toward a stronger consumption force, such as suggestion to binding instruction.
2. Separate the write side from read-back. Record whether write agency is manual, automatic, or both; separate acquisition and index maintenance from curation; where applicable, identify consolidation, deduplication, evolution, synthesis, invalidation, decay, and promotion; where relevant, distinguish raw traces from distilled retained artifacts.
3. Annotate the runtime-owned context route with: read-back direction (pull, push, or both, from the receiving agent's perspective), selection signal, targeting, selection scope and budget, delivery and consumption point, and any behavioral-faithfulness test. Post-turn capture or consolidation is write-side maintenance, not a second read-back point.
4. Record context presence, deployed wiring, activation, and causal effect as separate findings with separate evidence.
5. Reference `BAP-*` records for authority; do not let authority-family labels substitute for consumer, channel, force, and horizon. Keep lineage and curation labels independent of epistemic transformation, acceptance, and warrant — a `consolidate` or `import` label never establishes semantic preservation.
6. Omit entirely: checkout, archive, and publication mechanics; Commonplace comparison; borrowable ideas; curiosity passes; watch items; collection routing.

### 7. Invoke the epistemic procedure

1. Invoke the procedure in `kb/instructions/analyse-external-system-epistemic-architecture.md` to run the accepted route-analysis method inside this run's boundary. Every run invokes it. Do not copy or restate its object-inventory, route-ledger, transformation, lifecycle, claim-comparison, or authority method.
2. Pass to the invocation: a bounded epistemic subquestion, the run and system boundary, the frozen revision, the `SRC-*` register and evidence packet, the existing canonical records, the step-5 scoping record with its trigger evidence, and any classify-only routes the direct-adaptation exception named. The scoping record governs the invocation's depth: it tells the invoked procedure whether it is building a full route ledger or bounding and confirming a thin finding. Depth is the only thing it governs — the wrapper rules below hold identically at either depth.
3. Enforce the wrapper rules: no source reacquisition, no boundary widening, no revision change, no silent evidence upgrade, no parallel ID namespace, no independent publication decision, no system-wide epistemic grade. Its status vocabulary stays its own: record its architectural `implemented` under that name and this run's conclusion statuses under theirs. The two sets share no value, so a return that needs both carries both.
4. Require linked returns: material objects, routes, and claims by canonical ID; transformation class and route function; architectural status and observed candidate state; checking, acceptance, and retention/integration findings; the three authority records kept separate; and missing evidence paired with the conclusions it prevents — or, where the invoked procedure takes one of its early branches, that branch's own required substitutes, the no-candidate statement and the explicit no-claim comparison, which satisfy this requirement. Any new record or targeted-evidence request returns to the orchestrator for registration, and affected work is rerun.

### 8. Reconcile and synthesize

1. Merge duplicate objects and routes by canonical ID. Preserve anchored evidence conflicts as conflicts; never resolve one by selecting the strongest-sounding status.
2. Keep ownership: runtime owns complete control and context routes; the memory lens annotates read-back and activation; the epistemic lens annotates transformation, checking, warrant, acceptance, integration, and its two authorities.
3. Check every shared route for one revision, consistent sources, endpoints, objects, and `BAP-*` references. Memory curation labels cannot determine epistemic transformation; behavioral influence cannot imply epistemic or operational authority.
4. Write the synthesis organized around the deployed system's progression — scheduling, context, state and action, memory return where applicable, truth-apt and warrant routes where applicable, and the governing controls — not as concatenated lens reports. Preserve capability-versus-deployment and evidence-layer limits inside the synthesis. Mention a lens's thinness only where it bounds conclusions. Do not assign a system-wide epistemic grade.

### 9. Emit the logical result

Produce the same complete logical result whether the physical form is one file, a package, or a structured response; this instruction deliberately does not fix the physical layout.

Required logical records, in order:

1. run/staging identity;
2. system boundary, revision, and overall evidence tier;
3. source register;
4. shared component, object, route, claim, absence, and authority records, each carrying its amendments;
5. runtime account;
6. both lens scoping records;
7. both lens outputs;
8. cross-lens reconciliation;
9. bounded synthesis;
10. limitations, each paired with the conclusion it prevents;
11. verification/blocker report.

Rules:

- Give the result one canonical identity, with IDs resolvable across all physical parts.
- The order above is the reading order, not the writing order. Record 2's evidence tier is judged over the runtime baseline that record 5 carries, so write record 2 after step 4 and present it where the reader needs it — up front, bounding everything that follows.
- The required order is logical, not physical. A package may distribute the records across files, and a record may be satisfied by a resolvable pointer to the part that carries it, provided the result names one canonical location per record and every ID resolves across all parts.
- Publish only into an authorized target whose existing contract can represent the result. Otherwise retain the logical result under the run's staging identity and report a publication blocker. Do not improvise a collection contract and do not reuse the agent-memory review schema.
- Publishable limitations include: doc-only evidence, inaccessible components, no observed run, no causal experiment, trigger evidence too thin to resolve, and conflicting evidence — each naming its scope and prevented conclusion. Publication blockers include: missing logical records, ID collisions, unsupported material claims, failed applicable validation, and no authorized target contract.

### 10. Verify and report

1. Verify: source anchors; every conclusion status is one of the seven values listed in step 3, and no record carries `implemented` as a conclusion status; unique, resolving IDs; one boundary and revision across all records; mandatory runtime coverage; both lens scoping records present; both lens outputs present, each meeting the brief-output floor; prevented conclusions stated for every thin, negative, or unresolved finding; shared-route ownership respected; no forbidden evidence upgrades.
2. Check each distinction explicitly: retention is not read-back; context presence is not activation; implementation is not deployment; observation is not causality; curation is not warrant; use is not acceptance; behavioral authority is not epistemic or operational authority.
3. Run the deterministic validation required by the chosen existing target contract. Until a dedicated result contract exists, use applicable generic validation plus the semantic checklist above. When no authorized target contract applies, no deterministic validation applies either: record `no deterministic validation applicable` alongside the semantic checklist result and treat that as a complete verification. Do not change schemas or parsers, and do not adopt an unrelated contract, to manufacture a validation path.
4. Report: result identity and location, boundary/revision/tier, both lens scoping records and the depth each lens ran at, limitations, and any blockers.

## Verify

- The run has one run/result ID, one declared boundary, one frozen revision or capture, and one source register that every lens record cites.
- Both lenses ran. Both scoping records and both lens outputs exist as explicit records; nothing is implied by an absent section, and a brief output still names what was inventoried, what was found, and what its thinness prevents.
- No conclusion status was upgraded; every negative or uncertain finding names its inspected boundary and prevented conclusion.
- The synthesis is organized around the system, contains no system-wide epistemic grade, and the emitted result contains all eleven logical records or an explicit blocker report.

---

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: the three causal runtime responsibilities behind step 4
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — rests-on: why the runtime inventory stays open rather than becoming a taxonomy
- [Runtime structure determines the control surfaces available to governance](../../notes/runtime-structure-determines-governance-control-surfaces.md) — rests-on: why governance surfaces are conditional, crosscutting inspections
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — rests-on: why memory is a lens inside system analysis, not a peer category
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: the retention/read-back/presence/activation distinctions in steps 3, 5, and 6
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — rests-on: the consumer/channel/force path definition behind `BAP-*` records
- [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — rests-on: the SKILL.md packaging that gives this instruction discovery, user invocation, and execution policy
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — rests-on: why the runtime and memory/context procedures are embedded rather than left for the executor to reassemble
- [Model-resolved indirection adds interpretation work to LLM execution](../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — rests-on: the interpretation cost weighed when embedding lenses versus invoking the epistemic instruction by path
