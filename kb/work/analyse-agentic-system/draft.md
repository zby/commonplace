---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agentic system — an agent runtime, harness, orchestration framework, agent operating layer, or a narrower system whose deployed behavior depends on model calls plus surrounding machinery."
type: kb/types/instruction.md
---

# Analyse an Agentic System

Analyse one external agentic system at one frozen evidence boundary. Run a mandatory runtime baseline, then apply the memory/context lens and the epistemic lens only where each is applicable, reconcile shared records by stable IDs, and return one bounded system synthesis. The consumer is an analysing agent or maintainer; the channel is explicit invocation or trigger-matched skill loading; the force is a prescriptive analysis and result-writing policy.

Do not produce product rankings, generic adoption advice, a universal taxonomy or maturity ladder for agentic systems, or any claim beyond the declared evidence boundary. This skill owns the whole run: source preparation, applicability decisions, lens execution, reconciliation, the logical result, verification, and reporting. Lens workers execute inside that ownership; they never establish their own boundary or publication.

## Prerequisites

- A named target system and at least one source input (repository reference, existing checkout, snapshot or document bundle, or accessible live documents).
- If no source input is reachable at all, stop immediately and report the missing prerequisite; do not analyse from recollection.

## Steps

### 1. Open one run and declare the boundary

1. Accept a system identifier, the source inputs, and an optional output or staging identity. Allocate one run/result ID before any analysis; every later record cites it.
2. Confirm the subject is in scope: an agent runtime, harness, orchestration framework, agent operating layer, or a narrower system whose deployed behavior depends on model calls plus surrounding machinery. If not, exit early with an `out of scope` result and stop.
3. Define the reviewed boundary by function: include the components or actors whose scheduling, context selection, retained state, action execution, checking, acceptance, or authority decisions produce or constrain the behavior under review. List inclusions, exclusions, and external dependencies explicitly.
4. A subsystem-only boundary is permitted but must be named as such; it cannot support whole-system conclusions.
5. If no coherent system or subsystem boundary can be stated, treat the run as blocked: report the blocker and stop.

### 2. Freeze sources once

1. Branch by source kind:
   - Repository reference: resolve an immutable revision.
   - Existing checkout: inspect it without mutating it by default.
   - Supplied snapshot or document bundle: preserve its identity, version, or fingerprint.
   - Live or mixed documents, where capture is permitted: capture a dated inspectable boundary.
2. Record one analysis cutoff for the whole run. A dirty checkout is usable only when the exact inspected state can be identified and retained. A stable but old or partial boundary is allowed with an explicit published limitation. If no stable inspectable boundary can be established, emit a blocker report instead of a substantive analysis.
3. Build one canonical source register with `SRC-*` IDs. For each source record: kind, identity/location, revision or capture, evidence layer, inspected scope, citation anchors, and access gaps.
4. Prepare the evidence packet once. Lens workers must not reacquire, refresh, or widen sources. Targeted reads inside the frozen boundary are permitted, but they are added centrally to the register and they invalidate affected downstream findings, which must be redone.

### 3. Fix truth conditions, definitions, and shared records

Apply these rules for the rest of the run; they keep every lens using the same words and the same objects.

#### Evidence vocabulary

- Overall tier: the analysis is `code-grounded` only when implementation material was inspected to the depth of the central runtime account; otherwise it is `doc-grounded`. Mixed inspection gaps stay claim-local limitations; they do not change the tier silently.
- Per-source evidence layers: `implementation`, `doctrine/design`, `reported operation`, `observed run`, `causal experiment`.
- Conclusion statuses (use exactly these):
  - `absent` — not found inside a named, sufficiently inspected boundary;
  - `inapplicable` — the stated trigger conditions are false inside that boundary;
  - `uninspected` — the evidence needed to decide was unavailable or not inspected;
  - `claimed` — doctrine or reported operation asserts it;
  - `implemented` — inspected code affords it, without proving deployment;
  - `observed` — a run exhibits it, without proving cause;
  - `causally supported` — intervention or comparison plus design evidence supports the attribution.
- Every negative or uncertain result names the inspected boundary and the exact conclusion it prevents.
- Never upgrade: context presence to activation, implementation to observed operation, observation to causality, or operational continuation to warrant.

#### Definitions

- **Memory read-back**: material accumulated or changed through use returns to a later invocation or action. Static shipped material (documentation, tool specifications, installed skills) and ordinary current-run state are retained state, not read-back.
- **Activation**: evidence that delivered material changed behavior, not merely that it entered context.
- **Truth-apt**: capable of truth or falsity. A material epistemic route produces or changes truth-apt content, checks or disposes such a candidate, changes its authority, retains or integrates it for later reliance, or is required to assess a consequential knowledge or warrant claim. Operational curation labels name what a mechanism does to retained material; they do not establish semantic transformation or warrant.
- **Behavioral authority**: one consumption path's consumer, channel, force, and horizon. **Epistemic authority** licenses content and scope; **operational authority** permits or blocks behavior. Keep all three separate; never collapse them into one authority label.

#### Canonical records and ownership

| Canonical record | Owner | Lens rule |
|---|---|---|
| `SRC-*` source | Orchestrator | Lenses cite; never replace boundary or evidence layer |
| `CMP-*` component, `OBJ-*` operative object | Orchestrator/runtime owns generic identity, form, substrate | Lenses extend by ID |
| `RTE-*` control/context/state/action route | Runtime owns common endpoints and progression | Memory and epistemic lenses annotate, or register one new route centrally |
| `CLM-*` claim | Orchestrator namespace | Epistemic lens owns truth, scope, and warrant fields |
| `BAP-*` behavioral-authority path | Orchestrator | Lenses reference; epistemic and operational authority remain lens-owned |

No lens may rename or independently re-inventory a registered object or route. Any new material record returns to the orchestrator for one canonical ID.

### 4. Run the runtime baseline (always)

1. Treat scheduling, context assembly, and external state/action as causal responsibilities, not mandatory module boundaries; one facility may span more than one.
2. For each material loop, record: trigger/input, next-step owner, decision policy and its form, context selection and framing, state reads and writes, action executor and boundary, persistence, coordination and return, retry/cancellation/recovery, and output. Link every record by canonical IDs and cite its evidence.
3. Keep the anti-conflation rules: a filesystem is not a scheduler; retaining material is not selecting it into context; a tool schema present in context is not tool execution.
4. Inspect permissions, governance, observability, providers, user interface, packaging, performance, and other surfaces only when they materially alter the analysis question, a control path, evidence strength, or a lens result — and state that materiality when you include one. Do not turn this inventory into a universal taxonomy, fixed template, maturity ladder, ranking, or adoption advice.

### 5. Decide lens applicability

For each optional lens (memory/context; epistemic), emit one disposition record: `{lens, applicable|inapplicable|uncertain, trigger evidence IDs, inspected boundary, rationale, action, prevented conclusions}`.

- `applicable` — run the lens. `inapplicable` — exit that lens explicitly. `uncertain` — exit as an explicit evidence limitation, never as absence.
- A candidate trigger means `applicable`, not `uncertain`. An absent lens section or file must never carry the disposition implicitly.

**Memory/context trigger.** Applicable when code, documentation, or observation identifies a path by which material accumulated or changed through use can affect a later invocation or action. `inapplicable` requires sufficient evidence that no such path exists. Static shipped material, ordinary current-run state, and retained material with no later delivery path do not qualify as triggers. A merely claimed path still triggers the lens; the later analysis preserves whether the path is claimed, implemented, or observed.

**Epistemic trigger.** Applicable when a material route handles truth-apt content or the system makes a consequential knowledge-production or warrant claim — even when the eventual finding is failure or absence. Successful knowledge production is never a prerequisite for running the lens.

**Direct-adaptation exception.** Evaluated direct behavior or policy adaptation with no truth-apt object and no knowledge or warrant claim does not by itself trigger the epistemic lens. Keep such a route in the runtime account. If another trigger makes the epistemic lens applicable, include that route in the invoked epistemic method.

### 6. Run the embedded memory/context lens (when applicable)

Analyse accumulated-from-use mechanisms; this is not a memory-review publication workflow.

1. Inventory retained operative parts, splitting bundled artifacts whenever content, form, producer/consumer, checks, or authority path differs. For each part record: storage substrate, representational form, persistence, lineage, producer and consumer, invalidation/regeneration conditions, and any promotion path toward stronger form or force.
2. Separate the write side from read-back. Record whether write agency is manual, automatic, or both; separate acquisition and index maintenance from curation; where applicable, identify consolidation, deduplication, evolution, synthesis, invalidation, decay, and promotion; where relevant, distinguish raw traces from distilled retained artifacts.
3. Annotate the runtime-owned context route with: read-back direction (pull, push, or both, from the receiving agent's perspective), selection signal, targeting, selection scope and budget, delivery and consumption point, and any behavioral-faithfulness test. Post-turn capture or consolidation is write-side maintenance, not a second read-back point.
4. Record context presence, deployed wiring, activation, and causal effect as separate findings with separate evidence.
5. Reference `BAP-*` records for authority; do not let authority-family labels substitute for consumer, channel, force, and horizon. Keep lineage and curation labels independent of epistemic transformation, acceptance, and warrant — a `consolidate` or `import` label never establishes semantic preservation.
6. Omit entirely: checkout, archive, and publication mechanics; Commonplace comparison; borrowable ideas; curiosity passes; watch items; collection routing.

### 7. Invoke the epistemic procedure conditionally (when applicable)

1. Invoke [Analyse an external system's epistemic architecture](../../instructions/analyse-external-system-epistemic-architecture.md) — invokes: run the accepted route-analysis method inside this run's boundary. Do not copy or restate its object-inventory, route-ledger, transformation, lifecycle, claim-comparison, or authority method.
2. Pass to the invocation: a bounded epistemic subquestion, the run and system boundary, the frozen revision, the `SRC-*` register and evidence packet, the existing canonical records, and the trigger evidence from step 5.
3. Enforce the wrapper rules: no source reacquisition, no boundary widening, no revision change, no silent evidence upgrade, no parallel ID namespace, no independent publication decision, no system-wide epistemic grade.
4. Require linked returns: material objects, routes, and claims by canonical ID; transformation class and route function; architectural status and episode status; checking, acceptance, and retention/integration findings; the three authority records kept separate; and missing evidence paired with the conclusions it prevents. Any new record or targeted-evidence request returns to the orchestrator for registration, and affected work is rerun.
5. Worker topology, for any applicable lens: prefer fresh worker contexts that consume only the prepared packet and the frozen read-only boundary. If fresh workers are unavailable, execute the lens sequentially in the current context against the same register. If neither path can run an applicable lens, stop with an explicit capacity or dependency blocker — never relabel the lens `inapplicable` and never widen the evidence boundary to compensate.

### 8. Reconcile and synthesize

1. Merge duplicate objects and routes by canonical ID. Preserve anchored evidence conflicts as conflicts; never resolve one by selecting the strongest-sounding status.
2. Keep ownership: runtime owns complete control and context routes; the memory lens annotates read-back and activation; the epistemic lens annotates transformation, checking, warrant, acceptance, integration, and its two authorities.
3. Check every shared route for one revision, consistent sources, endpoints, objects, and `BAP-*` references. Memory curation labels cannot determine epistemic transformation; behavioral influence cannot imply epistemic or operational authority.
4. Write the synthesis organized around the deployed system's progression — scheduling, context, state and action, memory return where applicable, truth-apt and warrant routes where applicable, and the governing controls — not as concatenated lens reports. Preserve capability-versus-deployment and evidence-layer limits inside the synthesis. Mention early exits only where they bound conclusions. Do not assign a system-wide epistemic grade.

### 9. Emit the logical result

Produce the same complete logical result whether the physical form is one file, a package, or a structured response; this instruction deliberately does not fix the physical layout, which remains under trial.

Required logical records, in order:

1. run/staging identity;
2. system boundary, revision, and overall evidence tier;
3. source register;
4. shared component/object/route/claim/authority records;
5. runtime account;
6. both lens applicability records;
7. applicable lens outputs, or their explicit early exits;
8. cross-lens reconciliation;
9. bounded synthesis;
10. limitations, each paired with the conclusion it prevents;
11. verification/blocker report.

Rules:

- Give the result one canonical identity, with IDs resolvable across all physical parts.
- Publish only into an authorized target whose existing contract can represent the result. Otherwise retain the logical result under the run's staging identity and report a publication blocker. Do not improvise a collection contract and do not reuse the agent-memory review schema.
- Publishable limitations include: doc-only evidence, inaccessible components, no observed run, no causal experiment, unresolved applicability, and conflicting evidence — each naming its scope and prevented conclusion. Publication blockers include: missing logical records, ID collisions, unsupported material claims, failed applicable validation, and no authorized target contract.

### 10. Verify and report

1. Verify: source anchors and statuses; unique, resolving IDs; one boundary and revision across all records; mandatory runtime coverage; both lens dispositions present; all applicable lens outputs present; prevented conclusions stated for every non-run; shared-route ownership respected; no forbidden evidence upgrades.
2. Check each distinction explicitly: retention is not read-back; context presence is not activation; implementation is not deployment; observation is not causality; curation is not warrant; use is not acceptance; behavioral authority is not epistemic or operational authority.
3. Run the deterministic validation required by the chosen existing target contract. Until a dedicated result contract exists, use applicable generic validation plus the semantic checklist above; do not change schemas or parsers to manufacture a validation path.
4. Report: result identity and location, boundary/revision/tier, both lens dispositions, limitations, and any blockers.

## Verify

- The run has one run/result ID, one declared boundary, one frozen revision or capture, and one source register that every lens record cites.
- Both optional-lens dispositions exist as explicit records; no disposition is implied by an absent section.
- No conclusion status was upgraded; every negative or uncertain finding names its inspected boundary and prevented conclusion.
- The synthesis is organized around the system, contains no system-wide epistemic grade, and the emitted result contains all eleven logical records or an explicit blocker report.

---

- [Agent-runtime analysis should separate scheduling, context, and state](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: the three causal runtime responsibilities behind step 4
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — rests-on: why the runtime inventory stays open rather than becoming a taxonomy
- [Runtime structure determines governance control surfaces](../../notes/runtime-structure-determines-governance-control-surfaces.md) — rests-on: why governance surfaces are conditional, crosscutting inspections
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — rests-on: why memory is a lens inside system analysis, not a peer category
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: the retention/read-back/presence/activation distinctions in steps 3, 5, and 6
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — rests-on: the consumer/channel/force path definition behind `BAP-*` records
