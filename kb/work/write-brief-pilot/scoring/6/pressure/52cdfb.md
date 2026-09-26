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

Analyse one external agentic system at one frozen evidence boundary: run a mandatory runtime baseline, run both the memory/context and epistemic lenses at a depth proportionate to the evidence, reconcile shared records by stable IDs, and return one bounded system synthesis. The consumer is an analysing agent or maintainer; the channel is explicit invocation or trigger-matched skill loading; the force is a prescriptive analysis and result-writing policy.

Do not produce product rankings, generic adoption advice, a universal taxonomy or maturity ladder for agentic systems, or any claim beyond the declared evidence boundary. This skill owns the whole run: source preparation, lens scoping, lens execution, reconciliation, the logical result, verification, and reporting. The agent executing this skill is the orchestrator; lens workers execute inside its ownership and never establish their own boundary or publication.

A system that is mainly a memory system is analysed here like any other, and its result goes where step 9 sends every result, not into `kb/agent-memory-systems/`: memory is one lens of this analysis, and that collection holds legacy memory reviews.

## Prerequisites

- A named target system and at least one source input (repository reference, existing checkout, snapshot or document bundle, or accessible live documents).
- If no source input is reachable, stop and report the missing prerequisite; do not analyse from recollection.

## Steps

### 1. Open one run and declare the boundary

1. Accept a system identifier, the source inputs, and an optional output or staging identity. Before any analysis, allocate one run/result ID `AAS-<YYYY-MM-DD>-<system-slug>-<nn>`, where `nn` disambiguates same-day runs against the same system. Every record belongs to that run, and the emitted result carries the ID as its canonical identity.
2. Confirm scope: agent runtimes, harnesses, orchestration frameworks, and agent operating layers, plus any narrower system whose deployed behavior depends on model calls it issues **or serves** (this test admits narrower systems; it does not restrict the named kinds). The model call may run outside the boundary: deterministic machinery driven by a model elsewhere qualifies, as does a component that only serves a call, such as an MCP server or tool. Otherwise exit with an `out of scope` result.
3. Define the boundary by function: the components or actors whose scheduling, context selection, retained state, action execution, checking, acceptance, or authority decisions produce or constrain the behavior under review. List inclusions, exclusions, and external dependencies.
4. Name the boundary kind; it bounds what the result may conclude:
   - **whole-system** — every material loop under review is inside the boundary; conclusions may be system-wide.
   - **subsystem-only** — the subject is one part of a larger, not fully inspected system; conclusions cannot be whole-system.
   - **complete artifact, partial loop** — a complete, independently distributed artifact whose material loop crosses declared external dependencies (typically an MCP server, plugin, or tool whose model and host ship separately, or a loop running partly in a host platform outside the checkout). Conclusions may be whole-artifact but not about the behavior the crossing loop produces. List each external participant as a named exclusion with the conclusion it prevents.
5. If no coherent system or subsystem boundary can be stated, report the blocker and stop.

### 2. Freeze sources once

1. By source kind: resolve an immutable revision for a repository; inspect an existing checkout without mutating it by default; preserve a supplied snapshot's or bundle's identity, version, or fingerprint; capture a dated inspectable boundary for live or mixed documents where capture is permitted.
2. Record one analysis cutoff for the run. A dirty checkout is usable only when the exact inspected state can be identified and retained. A stable but old or partial boundary is allowed with an explicit published limitation. If no stable inspectable boundary can be established, emit a blocker report instead of an analysis.
3. Build one canonical source register with `SRC-*` IDs, recording for each source: kind, identity/location, revision or capture, evidence layer, inspected scope, citation anchors, and access gaps. A source whose parts carry different layers (implementation under `src/`, doctrine under `docs/`) records each layer against the scope it covers.
4. Assemble the evidence packet once, after the step-4 runtime baseline mints the canonical records: source register, boundary declaration, those canonical records, and the citation anchors relevant to each lens. Lens workers must not reacquire, refresh, or widen sources. Targeted reads inside the frozen boundary are permitted; add them centrally to the register and redo the downstream findings they affect. A correction registered while a worker is in flight is checked against that worker's return, and only findings resting on the superseded text are redone.

### 3. Fix truth conditions, definitions, and shared records

These rules hold for the rest of the run so every lens uses the same words and objects.

#### Evidence vocabulary

- Overall tier: one value, `code-grounded` only when the material in-boundary loops of the step-4 runtime baseline rest on inspected implementation material, otherwise `doc-grounded`. A loop declared an external dependency does not affect the tier; record it as a limitation naming the conclusion it prevents. Mixed inspection gaps stay claim-local limitations.
- Per-source evidence layers: `implementation`, `doctrine/design`, `reported operation`, `observed run`, `causal experiment`.
- Conclusion statuses (use exactly these):
  - `absent` — not found within the named, recorded search boundary;
  - `inapplicable` — the stated trigger conditions are false inside that boundary; a finding about the system, never a reason to skip a lens;
  - `uninspected` — the evidence needed to decide was unavailable or not inspected;
  - `claimed` — doctrine or reported operation asserts it;
  - `afforded` — inspected code affords it, without proving deployment;
  - `observed` — a run exhibits it, without proving cause;
  - `causally supported` — intervention or comparison plus design evidence supports the attribution.
- The step-7 epistemic procedure has its own vocabulary, where `implemented` is an architectural status contrasting with `doctrine only`; this instruction says `afforded` for the neighbouring idea. The sets share no value; record each in its own terms.
- Every negative or uncertain result names the inspected boundary and the exact conclusion it prevents.
- Never upgrade context presence to activation, implementation to observed operation, observation to causality, or operational continuation to warrant.

#### Definitions

These definitions are complete as given; apply them without opening any other document.

- **Memory read-back**: material accumulated or changed through use returns to a later invocation or action. Static shipped material (documentation, tool specifications, installed skills) and ordinary current-run state are retained state, not read-back. The exclusion is per instance: if the system rewrites such material from use, the rewritten instance is read-back. "Current run" means the consuming agent's invocation, not the host process's lifetime: material surviving to the next consumer invocation is read-back even when held in a long-lived process's memory, and even when only a derived value (a count, label set, or summary) returns. Degenerate read-back is itself a finding for a brief memory lens output.
- **Activation**: evidence that delivered material changed behavior, not merely that it entered context.
- **Truth-apt**: capable of truth or falsity. A material epistemic route produces or changes truth-apt content, checks or disposes such a candidate, changes its authority, retains or integrates it for later reliance, or is required to assess a consequential knowledge or warrant claim. Operational curation labels name what a mechanism does to retained material; they do not establish semantic transformation or warrant.
- **Behavioral authority**: one consumption path in four parts — consumer (who or what receives the material), channel (how it reaches them), force (what it obliges, permits, or merely suggests), and horizon (the span over which the path keeps that force). Example: `{consumer: spawned lens workers; channel: injected system prompt; force: binding instruction; horizon: the single run that spawned them}`. **Epistemic authority** licenses content and scope; **operational authority** permits or blocks behavior. Keep all three separate.

#### Canonical records and ownership

| Canonical record | Owner | Lens rule |
|---|---|---|
| `SRC-*` source | Orchestrator | Lenses cite; never replace boundary or evidence layer |
| `CMP-*` component, `OBJ-*` operative object | Orchestrator/runtime owns generic identity, form, substrate | Lenses extend by ID |
| `RTE-*` control/context/state/action route | Runtime owns common endpoints and progression | Memory and epistemic lenses annotate, or register one new route centrally |
| `CLM-*` claim | Orchestrator namespace | Epistemic lens owns truth, scope, and warrant fields |
| `ABS-*` evidenced absence | Orchestrator | Lenses return absences with their recorded search boundary for central registration; cite by ID |
| `BAP-*` behavioral-authority path | Orchestrator | Lenses reference; epistemic and operational authority remain lens-owned |

**Generic identity** is a record's identity, representational form, and storage substrate, independent of lens annotations. No lens may rename or re-inventory a registered object or route.

Only the orchestrator allocates canonical IDs, since parallel workers' numbering would collide. A lens needing a new record proposes it under a lens-local tag (`MEM-1`, `EPI-2`), cites it that way, and states its identity (file path, table name, route endpoints). The orchestrator maps the tag to a canonical ID, records the mapping, and merges proposals whose identity is already registered. Tags are discarded at registration, never appear in the result, and are not the parallel ID namespace step 7 forbids.

Register an evidenced absence as an `ABS-*` record: status `absent`, the recorded search boundary, and the conclusion the absence prevents or supports. An `uninspected` gap is a limitation, not an absence, and gets no `ABS-*` ID. Register an absence only when it bounds a conclusion someone would otherwise draw.

A lens that finds a registered record defective — false, misclassified by its own criterion, or misleading at its stated scope — returns the correction with its evidence anchor instead of re-inventorying. The orchestrator amends the record, preserves the superseded value, and reruns only work that relied on it; unlike step 2.4, a lens whose findings already rest on the corrected facts does not repeat its work.

A material return about a registered record rather than a new one (such as an output asserting something false, or a lineage break between two records) registers as an **amendment** to that record, with its evidence anchor and any superseded value, cited through that record's ID. Never discard a material return for lack of a namespace or inflate it into a new record.

#### Worker topology

For both lenses (steps 6 and 7), prefer fresh workers that consume only the evidence packet, the frozen read-only boundary, and any method document this instruction names; otherwise run the lens sequentially in the current context against the same registers. If neither can run, stop with a capacity or dependency blocker: never record the lens as unnecessary, let a thin scoping record stand in for it, or widen the evidence boundary.

A worker's written artifact is authoritative over its self-report and any harness failure notice. Verify it against the records that lens must return; redo only what is missing or unverifiable.

### 4. Run the runtime baseline (always)

1. Treat scheduling, context assembly, and external state/action as causal responsibilities, not mandatory module boundaries; one facility may span several.
2. For each material loop, record: trigger/input, next-step owner, decision policy and its form, context selection and framing, state reads and writes, action executor and boundary, persistence, coordination and return, retry/cancellation/recovery, and output. Link by canonical IDs, cite evidence, and register the `CMP-*`, `OBJ-*`, and `RTE-*` records you discover for the step-2.4 packet. A loop is material when it alters the analysis question, a control path, evidence strength, or a lens result. For a loop crossing a declared external dependency, record the in-boundary contribution to each field, mark the rest as owned by the named external participant without inferring its policy, and add the limitation naming what the crossing prevents.
3. A filesystem is not a scheduler; retaining material is not selecting it into context; a tool schema in context is not tool execution.
4. Inspect permissions, governance, observability, providers, user interface, packaging, performance, and other surfaces only when they meet the same materiality test, and state that materiality when you include one. Do not turn this conditional inventory into a taxonomy, fixed template, maturity ladder, ranking, or adoption advice; the prohibition does not apply to the mandatory loop record in 4.2.

### 5. Scope the two lenses

Both lenses always run; this step decides depth and names trigger evidence before any worker sees it. For each lens (memory/context; epistemic), emit one scoping record: `{lens, trigger evidence IDs, inspected boundary, the routes and objects that evidence points the lens at, warranted depth, rationale}`.

- Rich trigger evidence warrants a full pass; thin or degenerate evidence a brief one, which is a result, never a skip.
- **Brief-output floor.** A lens output always states what was inventoried, what was found, and what conclusions the thinness prevents. Example: "retention is total, retrieval of content is nil; branch labels are the only accumulated caller-authored text that returns."
- **`uncertain` is not a scoping value or an exit.** Unresolvable evidence becomes an explicit limitation inside the lens output, paired with the conclusion it prevents.
- Every run emits both scoping records and both lens outputs; an absent section or file never carries meaning.

**Memory/context evidence.** Look in code, documentation, or observation for a path by which material accumulated or changed through use can affect a later invocation or action. If you find only static shipped material, current-run state, or retained material with no later delivery path, scope the lens brief and say so. A claimed path is trigger evidence; the output preserves whether it is `claimed`, `afforded`, or `observed`.

**Epistemic evidence.** Look for a material route that handles truth-apt content and for any consequential knowledge-production or warrant claim the system makes, including where the eventual finding is failure or absence. Successful knowledge production is never a prerequisite.

**Direct-adaptation exception.** Evaluated direct behavior or policy adaptation with no truth-apt object and no knowledge or warrant claim is not an epistemic object, though the lens still runs. The route stays in the runtime account; the scoping record names it and hands it to the epistemic procedure tagged **classify-only**: recorded in its content/update classification, not analysed for warrant, transformation, or acceptance. If the lens finds the route truth-apt, that returns as a step-3 correction, never a silent scope expansion.

### 6. Run the embedded memory/context lens

Analyse accumulated-from-use mechanisms; this is not a memory-review publication workflow. Below is the full pass; a brief pass covers the same ground proportionately, skipping nothing silently.

1. Inventory retained operative parts, splitting bundled artifacts wherever content, form, producer/consumer, checks, or authority path differs. Per part: storage substrate; representational form (natural-language, symbolic such as code or schema, distributed-parametric such as model weights, or mixed); persistence; lineage; producer and consumer; invalidation/regeneration conditions; and any promotion path toward a more binding form (note to schema or code) or stronger force (suggestion to binding instruction).
2. Separate the write side from read-back: write agency (manual, automatic, or both); acquisition and index maintenance apart from curation; where applicable, consolidation, deduplication, evolution, synthesis, invalidation, decay, and promotion; raw traces apart from distilled artifacts.
3. Annotate the runtime-owned context route with: read-back direction (pull, push, or both, from the receiving agent's perspective), selection signal, targeting, selection scope and budget, delivery and consumption point, and any behavioral-faithfulness test. Post-turn capture or consolidation is write-side maintenance, not a second read-back point.
4. Record context presence, deployed wiring, activation, and causal effect as separate findings with separate evidence.
5. Reference `BAP-*` records for authority instead of authority-family labels. Keep lineage and curation labels independent of epistemic transformation, acceptance, and warrant: a `consolidate` or `import` label never establishes semantic preservation.
6. Omit checkout, archive, and publication mechanics; Commonplace comparison; borrowable ideas; curiosity passes; watch items; collection routing.

### 7. Invoke the epistemic procedure

1. In every run, invoke `kb/instructions/analyse-external-system-epistemic-architecture.md` to run its route-analysis method inside this run's boundary; do not restate its method.
2. Pass: a bounded epistemic subquestion, the run and system boundary, the frozen revision, the `SRC-*` register and evidence packet, the canonical records, the step-5 scoping record with its trigger evidence, and any classify-only routes. The scoping record governs only depth (full route ledger, or bounding a thin finding); the wrapper rules hold at either depth.
3. Wrapper rules: no source reacquisition, boundary widening, revision change, silent evidence upgrade, parallel ID namespace, independent publication decision, or system-wide epistemic grade. Record its architectural `implemented` under that name and this run's conclusion statuses under theirs; a return that needs both carries both.
4. Require linked returns: material objects, routes, and claims by canonical ID; transformation class and route function; architectural status and observed candidate state; checking, acceptance, and retention/integration findings; the three authority records kept separate; and missing evidence paired with the conclusions it prevents. Where the procedure takes one of its early branches, that branch's substitutes (the no-candidate statement and the explicit no-claim comparison) satisfy this requirement. New records and targeted-evidence requests return to the orchestrator for registration, and affected work is rerun.

### 8. Reconcile and synthesize

1. Merge duplicate objects and routes by canonical ID. Preserve anchored evidence conflicts as conflicts; never resolve one by picking the strongest-sounding status.
2. Keep ownership: runtime owns complete control and context routes; the memory lens annotates read-back and activation; the epistemic lens annotates transformation, checking, warrant, acceptance, integration, and its two authorities.
3. Check every shared route for one revision, consistent sources, endpoints, objects, and `BAP-*` references. Memory curation labels cannot determine epistemic transformation; behavioral influence cannot imply epistemic or operational authority.
4. Organize the synthesis around the deployed system's progression — scheduling, context, state and action, memory return and truth-apt/warrant routes where applicable, governing controls — not concatenated lens reports. Keep capability-versus-deployment and evidence-layer limits inside it, mention lens thinness only where it bounds conclusions, and assign no system-wide epistemic grade.

### 9. Emit the logical result

Produce the same complete logical result whether the physical form is one file, a package, or a structured response; this instruction does not fix the physical layout.

Required logical records, in reading order:

1. run/staging identity;
2. system boundary, revision, and overall evidence tier;
3. source register;
4. shared component, object, route, claim, absence, and authority records, each with its amendments;
5. runtime account;
6. both lens scoping records;
7. both lens outputs;
8. cross-lens reconciliation;
9. bounded synthesis;
10. limitations, each paired with the conclusion it prevents;
11. verification/blocker report.

Rules:

- Give the result one canonical identity, with IDs resolvable across all physical parts.
- Write record 2 after step 4, since its tier is judged over the runtime baseline, but present it first.
- A package may distribute records across files, and a record may be a resolvable pointer to the part carrying it, provided each record has one canonical location and every ID resolves across all parts.
- Publish only into an authorized target whose existing contract can represent the result. Otherwise retain the logical result under the run's staging identity and report a publication blocker. Do not improvise a collection contract and do not reuse the agent-memory review schema.
- Publishable limitations (each naming scope and prevented conclusion): doc-only evidence, inaccessible components, no observed run, no causal experiment, too-thin trigger evidence, conflicting evidence. Publication blockers: missing logical records, ID collisions, unsupported material claims, failed applicable validation, no authorized target contract.

### 10. Verify and report

1. Verify: source anchors; every conclusion status is one of the seven step-3 values and none is `implemented`; IDs are unique and resolve; one boundary and revision across all records; mandatory runtime coverage; both scoping records and both lens outputs present, each output meeting the brief-output floor; prevented conclusions stated for every thin, negative, or unresolved finding; shared-route ownership respected; no forbidden evidence upgrades.
2. Check each distinction: retention is not read-back; context presence is not activation; implementation is not deployment; observation is not causality; curation is not warrant; use is not acceptance; behavioral authority is not epistemic or operational authority.
3. Run the deterministic validation the chosen target contract requires, or applicable generic validation until a dedicated result contract exists, plus the checklist above. With no authorized target contract, record `no deterministic validation applicable` with the checklist result; that completes verification. Do not change schemas or parsers, or adopt an unrelated contract, to create a validation path.
4. Report: result identity and location, boundary/revision/tier, both scoping records and the depth each lens ran at, limitations, and any blockers.

## Verify

- One run ID, boundary, frozen revision, and source register, cited by every lens record.
- Both lenses ran, with explicit scoping records and outputs meeting the brief-output floor.
- No status upgraded; every negative or uncertain finding names its boundary and prevented conclusion.
- A system-organized synthesis with no system-wide epistemic grade, and all eleven logical records or a blocker report.

---

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: the three causal runtime responsibilities behind step 4
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — rests-on: why the runtime inventory stays open rather than becoming a taxonomy
- [Runtime structure determines the control surfaces available to governance](../../notes/runtime-structure-determines-governance-control-surfaces.md) — rests-on: why governance surfaces are conditional, crosscutting inspections
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — rests-on: why memory is a lens inside system analysis, not a peer category
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: the retention/read-back/presence/activation distinctions in steps 3, 5, and 6
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — rests-on: the consumer/channel/force path definition behind `BAP-*` records
- [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — rests-on: the SKILL.md packaging of this instruction
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — rests-on: why the runtime and memory/context procedures are embedded
- [Model-resolved indirection adds interpretation work to LLM execution](../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — rests-on: the cost of invoking the epistemic instruction by path
