---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agentic system — an agent runtime, harness, orchestration framework, or agent operating layer, or any narrower system whose deployed behavior depends on model calls plus surrounding machinery."
type: types/instruction.md
user-invocable: true
argument-hint: "<system identifier> plus source input (repository reference, checkout path, snapshot/bundle, or documents)"
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
---

# Analyse an Agentic System

Analyse one external agentic system at one frozen evidence boundary. Run a mandatory runtime baseline, then run both the memory/context lens and the epistemic lens at a depth proportionate to the evidence, reconcile shared records by stable IDs, and return one bounded system synthesis.

Do not produce product rankings, generic adoption advice, a universal taxonomy or maturity ladder for agentic systems, or any claim beyond the declared evidence boundary. The agent executing this skill is the orchestrator and owns the whole run; lens workers execute inside its ownership and never establish their own boundary or publication.

## Prerequisites

- A named target system and at least one source input (repository reference, existing checkout, snapshot or document bundle, or accessible live documents).
- If no source input is reachable, stop and report the missing prerequisite; do not analyse from recollection.

## Steps

### 1. Open one run and declare the boundary

1. Accept a system identifier, the source inputs, and an optional output or staging identity. Before any analysis, allocate one run/result ID, `AAS-<YYYY-MM-DD>-<system-slug>-<nn>`, where `nn` disambiguates same-day runs against the same system. Every record belongs to that run, and the emitted result carries the ID as its canonical identity.
2. Confirm the subject is in scope: an agent runtime, harness, orchestration framework, or agent operating layer; or, as an additional route, a narrower system whose deployed behavior depends on model calls it issues **or serves**. The model call may run outside the subject's boundary: deterministic machinery driven by an external model qualifies, and so does a component that only serves a call, such as an MCP server or tool. A system centered on memory, knowledge, or context engineering is analysed by this same run; its result goes where any other result goes under step 9, not into `kb/agent-memory-systems/`, whose per-system reviews are a legacy corpus this skill does not write. If neither route matches, exit with an `out of scope` result and stop.
3. Define the reviewed boundary by function: include the components or actors whose scheduling, context selection, retained state, action execution, checking, acceptance, or authority decisions produce or constrain the behavior under review. List inclusions, exclusions, and external dependencies explicitly.
4. Name the boundary kind; it bounds what the result may conclude:
   - **whole-system** — every material loop under review sits inside the boundary; conclusions may be system-wide.
   - **subsystem-only** — the subject is one part of a larger, not fully inspected system; conclusions cannot be whole-system.
   - **complete artifact, partial loop** — the subject is a complete, independently distributed artifact, but a material loop producing the behavior under review crosses declared external dependencies (typically an MCP server, plugin, or tool whose model and host ship separately, or a loop running partly in a host platform). Conclusions may be whole-artifact but not about the behavior the crossing loop produces. List the external participants as named exclusions, each with the conclusion it prevents.
5. If no coherent system or subsystem boundary can be stated, report the run as blocked and stop.

### 2. Freeze sources once

1. Branch by source kind:
   - Repository reference: resolve an immutable revision.
   - Existing checkout: inspect without mutating by default.
   - Snapshot or document bundle: preserve its identity, version, or fingerprint.
   - Live or mixed documents, where capture is permitted: capture a dated inspectable boundary.
2. Record one analysis cutoff for the run. A dirty checkout is usable only when the exact inspected state can be identified and retained. A stable but old or partial boundary is allowed with a published limitation. If no stable inspectable boundary can be established, emit a blocker report instead.
3. Build one canonical source register with `SRC-*` IDs. Each source records kind, identity/location, revision or capture, evidence layer, inspected scope, citation anchors, and access gaps. A source whose parts carry different layers (implementation under `src/`, doctrine under `docs/`) records each layer against the scope it covers.
4. Assemble the evidence packet once, after the step-4 runtime baseline has registered its canonical records: the source register, the boundary declaration, those records, and the citation anchors relevant to each lens. Lens workers must not reacquire, refresh, or widen sources. Targeted reads inside the frozen boundary are permitted; add them centrally to the register and redo the downstream findings they affect. A correction registered while a worker is in flight is checked against that worker's return on receipt, and only findings resting on the superseded text are redone.

### 3. Fix truth conditions, definitions, and shared records

Apply these rules for the rest of the run.

#### Evidence vocabulary

- Overall tier: `code-grounded` only when the material loops inside the boundary in the step-4 runtime baseline rest on inspected implementation material; otherwise `doc-grounded`. A loop crossing a declared external dependency does not affect the tier; record it as a limitation naming the conclusion it prevents. Report one tier; mixed inspection gaps stay claim-local limitations.
- Per-source evidence layers: `implementation`, `doctrine/design`, `reported operation`, `observed run`, `causal experiment`.
- Conclusion statuses (use exactly these):
  - `absent` — not found within the named, recorded search boundary;
  - `inapplicable` — the stated trigger conditions are false inside that boundary; a finding about the system, never a reason to skip a lens;
  - `uninspected` — the evidence needed to decide was unavailable or not inspected;
  - `claimed` — doctrine or reported operation asserts it;
  - `afforded` — inspected code affords it, without proving deployment;
  - `observed` — a run exhibits it, without proving cause;
  - `causally supported` — intervention or comparison plus design evidence supports the attribution.
- The epistemic procedure invoked at step 7 has its own vocabulary, in which `implemented` is an architectural status contrasting with `doctrine only`. It is not a conclusion status here; record each vocabulary in its own terms and never merge `implemented` with `afforded`.
- Every negative or uncertain result names the inspected boundary and the exact conclusion it prevents.
- Never upgrade context presence to activation, implementation to observed operation, observation to causality, or operational continuation to warrant.

#### Definitions

Apply these four definitions as given, without opening any other document.

- **Memory read-back**: material accumulated or changed through use returns to a later invocation or action. Static shipped material (documentation, tool specifications, installed skills) and ordinary current-run state are retained state, not read-back; but where the system rewrites such material from use, the rewritten instance is read-back. "Current run" is the consuming agent's invocation, not the host process's lifetime: material surviving from one consumer invocation to the next is read-back even when a long-lived process holds it, and even when only a derived value (a count, a label set, a summary) returns. Degenerate read-back is itself the finding for a brief memory lens output.
- **Activation**: evidence that delivered material changed behavior, not merely that it entered context.
- **Truth-apt**: capable of truth or falsity. A material epistemic route produces or changes truth-apt content, checks or disposes such a candidate, changes its authority, retains or integrates it for later reliance, or is required to assess a consequential knowledge or warrant claim. Operational curation labels do not establish semantic transformation or warrant.
- **Behavioral authority**: one consumption path, recorded as consumer (who or what receives the material), channel (how it reaches them), force (what it obliges, permits, or merely suggests), and horizon (the span over which the path keeps that force). Example: `{consumer: spawned lens workers; channel: injected system prompt; force: binding instruction; horizon: the single run that spawned them}`. **Epistemic authority** licenses content and scope; **operational authority** permits or blocks behavior. Keep all three separate; never collapse them into one authority label.

#### Canonical records and ownership

| Canonical record | Owner | Lens rule |
|---|---|---|
| `SRC-*` source | Orchestrator | Lenses cite; never replace boundary or evidence layer |
| `CMP-*` component, `OBJ-*` operative object | Orchestrator/runtime owns generic identity, form, substrate | Lenses extend by ID |
| `RTE-*` control/context/state/action route | Runtime owns common endpoints and progression | Memory and epistemic lenses annotate, or register one new route centrally |
| `CLM-*` claim | Orchestrator namespace | Epistemic lens owns truth, scope, and warrant fields |
| `ABS-*` evidenced absence | Orchestrator | Lenses return absences with their recorded search boundary for central registration; cite by ID |
| `BAP-*` behavioral-authority path | Orchestrator | Lenses reference; epistemic and operational authority remain lens-owned |

A record's **generic identity** is its identity, representational form, and storage substrate. No lens may rename or re-inventory a registered object or route.

Only the orchestrator allocates canonical IDs. A lens proposing a new record tags it lens-locally (`MEM-1`, `EPI-2`), cites that tag in its return, and states the record's identity (file path, table name, route endpoints). The orchestrator rewrites the tag to a canonical ID, records the mapping, and merges proposals whose identity is already registered. Proposal tags never appear in the emitted result and are not the parallel ID namespace step 7 forbids.

Register an `ABS-*` record for a finding whose status is `absent`, carrying the recorded search boundary and the conclusion the absence prevents or supports — and only when it bounds a conclusion someone would otherwise draw. An `uninspected` gap is a limitation, not an absence, and gets no `ABS-*` ID.

A lens that finds a registered record defective — false, misclassified by its own stated criterion, or accurate but misleading at its stated scope — returns the correction with its evidence anchor. The orchestrator amends the record, preserves the superseded value, and reruns only the work that relied on it; a lens whose findings already rest on the corrected facts does not repeat its work.

A material finding *about* a registered record — such as an output asserting something false, or a lineage break between two records — registers as an **amendment** to that record, with its evidence anchor and any superseded value, cited through that record's ID. Never discard a material return for lack of a namespace, or inflate one into a new record.

#### Worker topology

For both lenses (steps 6 and 7), prefer fresh worker contexts that consume only the evidence packet, the frozen read-only boundary, and any method document this instruction directs them to execute. Otherwise run the lens sequentially in the current context against the same registers. If neither can run a lens, stop with an explicit capacity or dependency blocker — never record the lens as unnecessary, let a thin scoping record stand in for it, or widen the evidence boundary to compensate.

If a worker terminates after producing output, its written artifact is authoritative over its self-report and any harness failure notice. Verify the artifact against the records that lens must return and redo only what is missing or unverifiable.

### 4. Run the runtime baseline (always)

1. Treat scheduling, context assembly, and external state/action as causal responsibilities, not mandatory module boundaries; one facility may span more than one.
2. For each material loop, record: trigger/input, next-step owner, decision policy and its form, context selection and framing, state reads and writes, action executor and boundary, persistence, coordination and return, retry/cancellation/recovery, and output, linked by canonical IDs with evidence. Register the `CMP-*`, `OBJ-*`, and `RTE-*` records you discover. A loop is material when it alters the analysis question, a control path, evidence strength, or a lens result. For a loop crossing a declared external dependency, record what the in-boundary artifact contributes to each field, mark the remainder as owned by the named external participant without inferring its policy, and add the limitation naming the conclusions the crossing prevents.
3. A filesystem is not a scheduler; retaining material is not selecting it into context; a tool schema present in context is not tool execution.
4. Inspect permissions, governance, observability, providers, user interface, packaging, performance, and other surfaces only when they meet the same materiality test, and state that materiality when you include one. Do not turn this conditional inventory into a universal taxonomy, fixed template, maturity ladder, ranking, or adoption advice; the prohibition does not apply to the mandatory loop record in 4.2.

### 5. Scope the two lenses

Both lenses always run; this step decides depth and names the trigger evidence before any lens worker sees it.

For each lens (memory/context; epistemic), emit one scoping record: `{lens, trigger evidence IDs, inspected boundary, the routes and objects that evidence points the lens at, warranted depth, rationale}`.

- Rich trigger evidence warrants a full pass; thin or degenerate evidence warrants a brief one, never a skipped lens.
- **Brief-output floor.** However degenerate the case, a lens output states what was inventoried, what was found, and what conclusions the thinness prevents. Example: "retention is total, retrieval of content is nil; branch labels are the only accumulated caller-authored text that returns."
- **`uncertain` is not a scoping value and not an exit.** Unresolvable evidence becomes an explicit limitation inside the lens output, paired with the conclusion it prevents.
- Every run emits both scoping records and both lens outputs; an absent section or file never carries meaning.

**Memory/context evidence.** Look, in code, documentation, or observation, for a path by which material accumulated or changed through use can affect a later invocation or action. Where you find only static shipped material, ordinary current-run state, or retained material with no later delivery path, scope the lens brief and say so. A merely claimed path is trigger evidence; the lens output preserves whether it is `claimed`, `afforded`, or `observed`.

**Epistemic evidence.** Look for a material route that handles truth-apt content, and for any consequential knowledge-production or warrant claim the system makes, including where the eventual finding is failure or absence.

**Direct-adaptation exception.** Evaluated direct behavior or policy adaptation with no truth-apt object and no knowledge or warrant claim is not an epistemic object. The route stays in the runtime account, and the scoping record names it. Hand it to the epistemic procedure tagged **classify-only**: recorded in its content/update classification, not analysed for warrant, transformation, or acceptance. If the lens concludes the route is truth-apt after all, that returns as a correction under step 3's correction rule, never as a silent expansion of the lens's scope.

### 6. Run the embedded memory/context lens

Analyse accumulated-from-use mechanisms; this is not a memory-review publication workflow. The items below are the full pass; a brief pass covers the same ground proportionately rather than skipping items silently.

1. Inventory retained operative parts, splitting bundled artifacts whenever content, form, producer/consumer, checks, or authority path differs. For each part record: storage substrate; representational form (natural-language, symbolic, distributed-parametric, or mixed); persistence; lineage; producer and consumer; invalidation/regeneration conditions; and any promotion path toward a more binding representation (note to schema or code) or stronger force (suggestion to binding instruction).
2. Separate the write side from read-back. Record whether write agency is manual, automatic, or both; separate acquisition and index maintenance from curation; identify any consolidation, deduplication, evolution, synthesis, invalidation, decay, and promotion; distinguish raw traces from distilled retained artifacts where relevant.
3. Annotate the runtime-owned context route with: read-back direction (pull, push, or both, from the receiving agent's perspective), selection signal, targeting, selection scope and budget, delivery and consumption point, and any behavioral-faithfulness test. Post-turn capture or consolidation is write-side maintenance, not a second read-back point.
4. Record context presence, deployed wiring, activation, and causal effect as separate findings with separate evidence.
5. Reference `BAP-*` records for authority; authority-family labels do not substitute for consumer, channel, force, and horizon. Keep lineage and curation labels independent of epistemic transformation, acceptance, and warrant — a `consolidate` or `import` label never establishes semantic preservation.
6. Omit: checkout, archive, and publication mechanics; Commonplace comparison; borrowable ideas; curiosity passes; watch items; collection routing.

### 7. Invoke the epistemic procedure

1. Every run invokes the procedure in `kb/instructions/analyse-external-system-epistemic-architecture.md` inside this run's boundary. Do not copy or restate its method.
2. Pass it: a bounded epistemic subquestion, the run and system boundary, the frozen revision, the `SRC-*` register and evidence packet, the existing canonical records, the step-5 scoping record with its trigger evidence, and any classify-only routes. The scoping record governs only depth — a full route ledger or bounding and confirming a thin finding; the wrapper rules hold at either depth.
3. Wrapper rules: no source reacquisition, no boundary widening, no revision change, no silent evidence upgrade, no parallel ID namespace, no independent publication decision, no system-wide epistemic grade. Record its architectural `implemented` under that name and this run's conclusion statuses under theirs; a return that needs both carries both.
4. Require linked returns: material objects, routes, and claims by canonical ID; transformation class and route function; architectural status and observed candidate state; checking, acceptance, and retention/integration findings; the three authority records kept separate; and missing evidence paired with the conclusions it prevents. Where the procedure takes one of its early branches, that branch's substitutes — the no-candidate statement and the explicit no-claim comparison — satisfy this requirement. Any new record or targeted-evidence request returns to the orchestrator for registration, and affected work is rerun.

### 8. Reconcile and synthesize

1. Merge duplicate objects and routes by canonical ID. Preserve anchored evidence conflicts as conflicts; never resolve one by selecting the strongest-sounding status.
2. Keep ownership: runtime owns complete control and context routes; the memory lens annotates read-back and activation; the epistemic lens annotates transformation, checking, warrant, acceptance, integration, and its two authorities.
3. Check every shared route for one revision and consistent sources, endpoints, objects, and `BAP-*` references.
4. Write the synthesis around the deployed system's progression — scheduling, context, state and action, memory return where applicable, truth-apt and warrant routes where applicable, and the governing controls — not as concatenated lens reports. Preserve capability-versus-deployment and evidence-layer limits. Mention a lens's thinness only where it bounds conclusions. Do not assign a system-wide epistemic grade.

### 9. Emit the logical result

Produce the same complete logical result whether the physical form is one file, a package, or a structured response.

Required logical records, in reading order:

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
- Write record 2 after step 4, since its tier is judged over the runtime baseline, but present it up front.
- A package may distribute records across files, and a record may be a resolvable pointer to the part that carries it, provided the result names one canonical location per record.
- Publish only into an authorized target whose existing contract can represent the result. Otherwise retain the logical result under the run's staging identity and report a publication blocker. Do not improvise a collection contract and do not reuse the agent-memory review schema.
- Publishable limitations (each naming its scope and prevented conclusion) include doc-only evidence, inaccessible components, no observed run, no causal experiment, unresolvably thin trigger evidence, and conflicting evidence. Publication blockers include missing logical records, ID collisions, unsupported material claims, failed applicable validation, and no authorized target contract.

### 10. Verify and report

1. Verify: source anchors; every conclusion status is a step-3 value, never `implemented`; unique, resolving IDs; one boundary and revision; mandatory runtime coverage; both scoping records and both lens outputs present, each output meeting the brief-output floor; prevented conclusions for every thin, negative, or unresolved finding; shared-route ownership respected; no forbidden evidence upgrades.
2. Check each distinction explicitly: retention is not read-back; context presence is not activation; implementation is not deployment; observation is not causality; curation is not warrant; use is not acceptance; behavioral authority is not epistemic or operational authority.
3. Run the deterministic validation the chosen target contract requires, plus the checklist above. When no authorized target contract applies, record `no deterministic validation applicable` alongside the checklist result; that is complete verification. Do not change schemas or parsers, or adopt an unrelated contract, to manufacture a validation path.
4. Report: result identity and location, boundary/revision/tier, both lens scoping records and the depth each lens ran at, limitations, and any blockers.

## Verify

- One run/result ID, boundary, frozen revision or capture, and source register that every lens record cites.
- Both scoping records and both lens outputs exist explicitly, each output meeting the brief-output floor; no status was upgraded.
- The synthesis is organized around the system with no system-wide epistemic grade, and the result contains all eleven logical records or an explicit blocker report.

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
