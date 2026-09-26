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

Analyse one external agentic system at one frozen evidence boundary: run a mandatory runtime baseline, run both the memory/context lens and the epistemic lens at the depth the evidence supports, reconcile shared records by stable IDs, and return one bounded system synthesis.

Do not produce product rankings, generic adoption advice, a universal taxonomy or maturity ladder for agentic systems, or any claim beyond the declared evidence boundary. The agent executing this skill is the orchestrator: it owns source preparation, lens scoping and execution, reconciliation, the logical result, verification, and reporting. Lens workers run inside its ownership and never establish their own boundary or publication.

## Prerequisites

- A named target system and at least one reachable source input (repository reference, existing checkout, snapshot or document bundle, or accessible live documents). If none is reachable, stop and report the missing prerequisite; do not analyse from recollection.

## Steps

### 1. Open one run and declare the boundary

1. Accept a system identifier, the source inputs, and an optional output or staging identity. Before any analysis, allocate one run/result ID, `AAS-<YYYY-MM-DD>-<system-slug>-<nn>`, where `nn` disambiguates same-day runs against one system. Every record belongs to that run, and the emitted result carries the ID as its canonical identity.
2. Confirm scope. In scope are agent runtimes, harnesses, orchestration frameworks, and agent operating layers; separately, any narrower system whose deployed behavior depends on model calls it issues **or serves** (this test admits narrower systems; it does not restrict the named kinds). Under either route the model may run outside the system's boundary: deterministic machinery driven by an external model qualifies, as does a component that only serves a call, such as an MCP server or tool. Otherwise emit an `out of scope` result and stop.
3. Define the reviewed boundary by function: include the components or actors whose scheduling, context selection, retained state, action execution, checking, acceptance, or authority decisions produce or constrain the behavior under review. List inclusions, exclusions, and external dependencies explicitly.
4. Name the boundary kind; it bounds what the result may conclude:
   - **whole-system** — every material loop under review sits inside the boundary; conclusions may be system-wide.
   - **subsystem-only** — the subject is one part of a larger, not fully inspected system; conclusions cannot be whole-system.
   - **complete artifact, partial loop** — a complete, independently distributed artifact whose material loop crosses declared external dependencies, as with an MCP server, plugin, or tool whose model and host ship separately, or a loop running partly in a host platform outside the checkout. Conclusions may be whole-artifact but may not describe the crossing loop's behavior. List each external participant as a named exclusion with the conclusion it prevents.
5. If no coherent system or subsystem boundary can be stated, report the blocker and stop.

### 2. Freeze sources once

1. Branch by source kind:
   - Repository reference: resolve an immutable revision.
   - Existing checkout: inspect it without mutating it by default.
   - Supplied snapshot or document bundle: preserve its identity, version, or fingerprint.
   - Live or mixed documents, where capture is permitted: capture a dated inspectable boundary.
2. Record one analysis cutoff for the run. A dirty checkout is usable only when the exact inspected state can be identified and retained. A stable but old or partial boundary is allowed with an explicit published limitation. If no stable inspectable boundary can be established, emit a blocker report instead of an analysis.
3. Build one canonical source register with `SRC-*` IDs, each recording kind, identity/location, revision or capture, evidence layer, inspected scope, citation anchors, and access gaps. Record mixed layers per scope (implementation under `src/`, doctrine under `docs/`).
4. Assemble the evidence packet once, after the step-4 runtime baseline mints its canonical records: source register, boundary declaration, those records, and the citation anchors relevant to each lens. Lens workers must not reacquire, refresh, or widen sources. Targeted reads inside the frozen boundary are permitted: add them to the register centrally and redo the downstream findings they affect. Check a correction registered while a worker is in flight against its return on receipt, and redo only findings that rested on the superseded text.

### 3. Fix truth conditions, definitions, and shared records

#### Evidence vocabulary

- Overall tier: `code-grounded` only when the in-boundary material loops of the step-4 runtime baseline rest on inspected implementation material; otherwise `doc-grounded`. A loop declared an external dependency does not affect the tier; record it as a limitation naming the conclusion it prevents. Report one tier. Mixed inspection gaps stay claim-local limitations and do not change the tier.
- Per-source evidence layers: `implementation`, `doctrine/design`, `reported operation`, `observed run`, `causal experiment`.
- Conclusion statuses (use exactly these):
  - `absent` — not found within the named, recorded search boundary;
  - `inapplicable` — the stated trigger conditions are false inside that boundary; a finding about the system, never a reason to skip a lens;
  - `uninspected` — the evidence needed to decide was unavailable or not inspected;
  - `claimed` — doctrine or reported operation asserts it;
  - `afforded` — inspected code affords it, without proving deployment;
  - `observed` — a run exhibits it, without proving cause;
  - `causally supported` — intervention or comparison plus design evidence supports the attribution.
- These statuses share no value with the epistemic procedure invoked at step 7. There, `implemented` is an *architectural* status contrasting with `doctrine only`; this instruction says `afforded` for the neighbouring idea. Record each vocabulary in its own terms and never merge them.
- Every negative or uncertain result names the inspected boundary and the exact conclusion it prevents.
- Never upgrade context presence to activation, implementation to observed operation, observation to causality, or operational continuation to warrant.

#### Definitions

- **Memory read-back**: material accumulated or changed through use returns to a later invocation or action. Static shipped material (documentation, tool specifications, installed skills) and ordinary current-run state are retained state, not read-back — per instance: a copy the system rewrites from use is read-back, while the as-shipped copy stays retained state. "Current run" means the consuming agent's invocation, not the host process's lifetime: material surviving to the next consumer invocation is read-back even when a long-lived process holds it, and even when only a derived value (a count, a label set, a summary) returns. Degenerate read-back is itself the finding, recorded in a brief memory lens output.
- **Activation**: evidence that delivered material changed behavior, not merely that it entered context.
- **Truth-apt**: capable of truth or falsity. A material epistemic route produces or changes truth-apt content, checks or disposes such a candidate, changes its authority, retains or integrates it for later reliance, or is required to assess a consequential knowledge or warrant claim. Operational curation labels name what a mechanism does to retained material; they do not establish semantic transformation or warrant.
- **Behavioral authority**: one consumption path, recorded as consumer (who or what receives the material), channel (how it reaches them), force (what it obliges, permits, or merely suggests), and horizon (the span over which the path keeps that force). Example: `{consumer: spawned lens workers; channel: injected system prompt; force: binding instruction; horizon: the single run that spawned them}`. **Epistemic authority** licenses content and scope; **operational authority** permits or blocks behavior. Keep all three separate. These definitions are complete as given; apply them without opening any other document.

#### Canonical records and ownership

| Canonical record | Owner | Lens rule |
|---|---|---|
| `SRC-*` source | Orchestrator | Lenses cite; never replace boundary or evidence layer |
| `CMP-*` component, `OBJ-*` operative object | Orchestrator/runtime owns generic identity, form, substrate | Lenses extend by ID |
| `RTE-*` control/context/state/action route | Runtime owns common endpoints and progression | Memory and epistemic lenses annotate, or register one new route centrally |
| `CLM-*` claim | Orchestrator namespace | Epistemic lens owns truth, scope, and warrant fields |
| `ABS-*` evidenced absence | Orchestrator | Lenses return absences with their recorded search boundary for central registration; cite by ID |
| `BAP-*` behavioral-authority path | Orchestrator | Lenses reference; epistemic and operational authority remain lens-owned |

A record's **generic identity** is its identity, representational form, and storage substrate, independent of lens annotations. No lens may rename or re-inventory a registered object or route.

Only the orchestrator allocates canonical IDs; parallel workers cannot see each other's numbering. A lens proposes a new record under a lens-local tag (`MEM-1`, `EPI-2`), cites that tag throughout its return, and states the record's identity — file path, table name, route endpoints. The orchestrator rewrites the tag to a canonical ID, records the mapping, and merges any proposal whose identity is already registered. Proposal tags never appear in the result and are not the parallel ID namespace step 7 forbids.

Register an evidenced absence as an `ABS-*` record: status `absent`, with the recorded search boundary and the conclusion the absence prevents or supports. Register one only when it bounds a conclusion someone would otherwise draw. An `uninspected` gap is not an absence; it stays a limitation with no `ABS-*` ID.

A lens that finds a registered record defective — false, misclassified by its own stated criterion, or misleading at its stated scope — returns the correction with its evidence anchor instead of re-inventorying. The orchestrator amends the record, preserves the superseded value, and reruns only work that relied on it; a lens whose findings already used the corrected facts does not repeat its work.

A material finding *about* a registered record — an output asserting something false, a lineage break between two records — registers as an **amendment** to that record, with its evidence anchor and any superseded value, cited through that record's ID. Never discard a material return for lack of a namespace, and never inflate one into a new record.

#### Worker topology

For both lenses (steps 6 and 7), prefer fresh worker contexts that consume only the evidence packet, the frozen read-only boundary, and any method document this instruction directs them to execute. If fresh workers are unavailable, run the lens sequentially in the current context against the same registers. If neither can run a lens, stop with an explicit capacity or dependency blocker — never record the lens as unnecessary, never let a thin scoping record stand in for an unrun lens, and never widen the evidence boundary to compensate.

A worker's written artifact outranks its self-report and any harness failure notice. Verify it against the records that lens must return; accept it when complete and redo only what is missing or unverifiable.

### 4. Run the runtime baseline (always)

1. Treat scheduling, context assembly, and external state/action as causal responsibilities, not mandatory module boundaries; one facility may span several.
2. For each material loop (material under the step-4.4 test), record: trigger/input, next-step owner, decision policy and its form, context selection and framing, state reads and writes, action executor and boundary, persistence, coordination and return, retry/cancellation/recovery, and output. Link records by canonical IDs, cite evidence, and register the `CMP-*`, `OBJ-*`, and `RTE-*` records you discover for the step-2.4 packet. For a loop crossing a declared external dependency, record the in-boundary artifact's contribution to each field, mark the remainder as owned by the named external participant without inferring its policy, and add the limitation naming the conclusions the crossing prevents.
3. Keep the anti-conflation rules: a filesystem is not a scheduler; retaining material is not selecting it into context; a tool schema present in context is not tool execution.
4. Inspect permissions, governance, observability, providers, user interface, packaging, performance, and other surfaces only when they materially alter the analysis question, a control path, evidence strength, or a lens result, and state that materiality. Do not turn this conditional inventory (unlike the mandatory 4.2 record) into a universal taxonomy, fixed template, maturity ladder, ranking, or adoption advice.

### 5. Scope the two lenses

Both lenses always run. This step decides *how deep*, and names the trigger evidence before any lens worker sees it.

For each lens (memory/context; epistemic), emit one scoping record: `{lens, trigger evidence IDs, inspected boundary, the routes and objects that evidence points the lens at, warranted depth, rationale}`.

- Rich trigger evidence warrants a full pass; thin or degenerate evidence warrants a brief one, which is a result, never a skipped lens.
- **Brief-output floor.** Every lens output states what was inventoried, what was found, and what conclusions the thinness prevents, e.g. "retention is total, retrieval of content is nil; branch labels are the only accumulated caller-authored text that returns."
- **`uncertain` is neither a scoping value nor an exit.** Unresolvable evidence becomes a limitation *inside* the lens output, paired with the conclusion it prevents.
- An absent section or file never carries meaning.

**Memory/context evidence.** Look, in code, documentation, or observation, for a path by which material accumulated or changed through use can affect a later invocation or action. Static shipped material, ordinary current-run state, and retained material with no later delivery path do not count; where they are all you find, scope the lens brief and say so. A merely claimed path is trigger evidence; the output preserves whether it is `claimed`, `afforded`, or `observed`.

**Epistemic evidence.** Look for a material route that handles truth-apt content, and for any consequential knowledge-production or warrant claim the system makes — including where the finding will be failure or absence. Successful knowledge production is never a prerequisite for the lens.

**Direct-adaptation exception.** Evaluated direct behavior or policy adaptation with no truth-apt object and no knowledge or warrant claim is not an epistemic object; the lens still runs. Keep such a route in the runtime account, name it in the scoping record, and hand it to the epistemic procedure tagged **classify-only**: recorded in its content/update classification, *not* analysed for warrant, transformation, or acceptance. If the lens finds the route truth-apt, that returns as a step-3 correction, never a silent scope expansion.

### 6. Run the embedded memory/context lens

Analyse accumulated-from-use mechanisms; this is not a memory-review publication workflow. The items below are the full pass; a brief pass covers them proportionately, skipping none silently.

1. Inventory retained operative parts, splitting bundled artifacts whenever content, form, producer/consumer, checks, or authority path differs. For each part record: storage substrate; representational form (natural-language, symbolic, distributed-parametric, or mixed); persistence; lineage; producer and consumer; invalidation/regeneration conditions; and any promotion path toward a more binding form (note to schema or code) or stronger consumption force (suggestion to binding instruction).
2. Separate the write side from read-back. Record whether write agency is manual, automatic, or both; separate acquisition and index maintenance from curation; where applicable, identify consolidation, deduplication, evolution, synthesis, invalidation, decay, and promotion; where relevant, distinguish raw traces from distilled retained artifacts.
3. Annotate the runtime-owned context route with: read-back direction (pull, push, or both, from the receiving agent's perspective), selection signal, targeting, selection scope and budget, delivery and consumption point, and any behavioral-faithfulness test. Post-turn capture or consolidation is write-side maintenance, not a second read-back point.
4. Record context presence, deployed wiring, activation, and causal effect as separate findings with separate evidence.
5. Reference `BAP-*` records for authority; authority-family labels never substitute for consumer, channel, force, and horizon. Keep lineage and curation labels independent of epistemic transformation, acceptance, and warrant — a `consolidate` or `import` label never establishes semantic preservation.
6. Omit: checkout, archive, and publication mechanics; Commonplace comparison; borrowable ideas; curiosity passes; watch items; collection routing.

### 7. Invoke the epistemic procedure

1. Every run invokes the procedure in `kb/instructions/analyse-external-system-epistemic-architecture.md` inside this run's boundary. Do not copy or restate its object-inventory, route-ledger, transformation, lifecycle, claim-comparison, or authority method.
2. Pass it: a bounded epistemic subquestion, the run and system boundary, the frozen revision, the `SRC-*` register and evidence packet, the existing canonical records, the step-5 scoping record with its trigger evidence, and any classify-only routes. The scoping record governs only depth — a full route ledger, or bounding and confirming a thin finding; the wrapper rules hold at either depth.
3. Enforce the wrapper rules: no source reacquisition, boundary widening, revision change, silent evidence upgrade, parallel ID namespace, independent publication decision, or system-wide epistemic grade. Keep its architectural `implemented` and this run's conclusion statuses under their own names; a return may carry both.
4. Require linked returns: material objects, routes, and claims by canonical ID; transformation class and route function; architectural status and observed candidate state; checking, acceptance, and retention/integration findings; the three authority records kept separate; and missing evidence paired with the conclusions it prevents. An early branch's required substitutes (the no-candidate statement and explicit no-claim comparison) satisfy this. New records and targeted-evidence requests return to the orchestrator for registration, and affected work is rerun.

### 8. Reconcile and synthesize

1. Merge duplicate objects and routes by canonical ID. Preserve anchored evidence conflicts as conflicts; never resolve one by picking the strongest-sounding status.
2. Keep ownership: runtime owns complete control and context routes; the memory lens annotates read-back and activation; the epistemic lens annotates transformation, checking, warrant, acceptance, integration, and its two authorities.
3. Check every shared route for one revision and consistent sources, endpoints, objects, and `BAP-*` references. Memory curation labels cannot determine epistemic transformation; behavioral influence cannot imply epistemic or operational authority.
4. Write the synthesis around the deployed system's progression — scheduling, context, state and action, memory return and truth-apt and warrant routes where applicable, governing controls — not as concatenated lens reports. Preserve capability-versus-deployment and evidence-layer limits; mention a lens's thinness only where it bounds conclusions; assign no system-wide epistemic grade.

### 9. Emit the logical result

The physical form (one file, a package, or a structured response) is open; the logical result is not.

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

- Give the result one canonical identity, with IDs resolvable across all physical parts. A package may distribute records across files, and a record may be a resolvable pointer, provided each record has one canonical location.
- Reading order is not writing order: judge record 2's tier after step 4, then present it up front.
- Publish only into an authorized target whose existing contract can represent the result; otherwise retain the logical result under the run's staging identity and report a publication blocker. Do not improvise a collection contract and do not reuse the agent-memory review schema.
- A system that is mainly a memory system follows the same rule: `kb/agent-memory-systems/` is a legacy review corpus that takes no new results, so do not publish there.
- Publishable limitations (each naming scope and prevented conclusion): doc-only evidence, inaccessible components, no observed run, no causal experiment, trigger evidence too thin to resolve, conflicting evidence. Publication blockers: missing logical records, ID collisions, unsupported material claims, failed applicable validation, no authorized target contract.

### 10. Verify and report

1. Check the result against the semantic checklist under **Verify** below.
2. Run the deterministic validation the chosen existing target contract requires; until a dedicated result contract exists, use applicable generic validation plus the semantic checklist. When no authorized target contract applies, record `no deterministic validation applicable` with the checklist result; that is complete verification. Do not change schemas or parsers, or adopt an unrelated contract, to manufacture a validation path.
3. Report: result identity and location, boundary/revision/tier, both scoping records and the depth each lens ran at, limitations, and any blockers.

## Verify

- One run/result ID, one declared boundary, one frozen revision or capture, and one source register that every record cites; source anchors present; IDs unique and resolving.
- Every conclusion status is one of the seven step-3 values, none is `implemented`, and none was upgraded.
- Runtime coverage is complete. Both scoping records and both lens outputs exist explicitly, each output meeting the brief-output floor.
- Every thin, negative, or unresolved finding names its inspected boundary and prevented conclusion. Shared-route ownership is respected.
- Each distinction holds: retention is not read-back; context presence is not activation; implementation is not deployment; observation is not causality; curation is not warrant; use is not acceptance; behavioral authority is not epistemic or operational authority.
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
