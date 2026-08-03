# Revision profiles and moving boundaries

**Status: backstage.** Per operator constraint (2026-08-03), the article-facing synthesis is the [plain account](./plain-account.md), which must stand without this file's notation. This file is the formal bookkeeping behind it — kept for precision work inside the workshop, promoted only if a real consumer needs a record the prose cannot carry.

This is a formal working synthesis, not a proposed definition. Its purpose is to make visible which distinctions are stable enough to use and which boundaries still move when the system boundary, target granularity, update pathway, or evidential horizon changes.

## Working scope and claim unit

In this workshop, **self-revision** means that a pathway determines and installs a change to the bounded system's own behavior-determining organization. The term alone does not imply reflection, evidence-responsiveness, operativity, warrant, or a favorable outcome. A **reflective revision** is the narrower case mediated through a causally connected self-representation; an evidence-responsive operative revision may satisfy the self-improving-system definition.

“This system can revise itself” is still underspecified. The smallest safe reportable unit currently available is a versioned, indexed revision claim:

`(mode, boundary, source state/epoch, objective, assessment context, target aspect, granularity, pathway, change class, horizon)`

- **Mode** distinguishes a dispositional claim that a pathway can perform a class of revisions from an occurrent claim about a realized transition.
- **System boundary** says which actors and machinery count as internal. A human-inclusive workflow and its computational subsystem can receive different classifications.
- **Source state or epoch** fixes the pathway and authority arrangement being assessed. Revision may change the profile that applies to the next transition.
- **Objective** says relative to what later behavior is being called better. It is required when improvement or improvement warrant is claimed; a purely structural self-revision report records that no improvement objective is asserted. An incumbent objective can license its successor relative to the incumbent; claiming that a terminal objective itself became better under a different normative index requires a comparison level outside that pair. Neither case makes one objective artifact permanently immutable.
- **Assessment context** states the operating or evidence domain and the assurance required for the target's risk. The same evaluator can warrant one domain and fail another.
- **Target aspect and granularity** say what is changing. A file can be writable while one semantic commitment smeared across files is not addressable; a model can be immutable internally while its binding is replaceable.
- **Pathway** says how this change is determined and installed. One standing system can compose proposal selection, direct installation, runtime enforcement, and later direct state updates.
- **Change class** bounds the deltas being claimed: for example, selecting a binding, configuring an interface, modifying internals, or revising a named semantic target. Supporting profiles separately record reflective-coverage operations (observation, selection, configuration, modification) and semantic-addressability operations (retrieval, interpretation, criticism, revision, rescoping, transfer). Neither profile forms a ladder, and observation alone is not a revision.
- **Horizon** says how much of the causal path is evidenced: adoption, first exercise, downstream outcome, leverage on a later revision, or eventual retirement. Adoption can close only a partial-path report; an occurrent operative-revision claim must extend through subsequent exercise and causal effect.

Changing one coordinate starts a new claim. A system-level description is a collection of these claims, not a scalar maturity score. *Commitment* remains useful for semantically addressable content, but it is not yet a demonstrated universal unit across prose, code, schemas, system topology, and weights.

## Three maps

The original kernel account mixed three maps that need different evidence. Coordinates scope a claim; target and pathway profiles describe properties; derived relations report determination reach, installation reach, procedural control, improvement warrant, bounded-experiment authorization, operativity, and recovery; coverage aggregates those relations over a declared inventory. Only independently variable profile properties qualify as candidate axes.

### 1. Target-affordance and reach map

This map describes what a named target makes available to a named pathway. Some entries are target properties and others are target–pathway relations; neither should be mistaken for governance:

| Field | Question | What it does not establish |
|---|---|---|
| Representational form | Is the operative part natural-language, symbolic, distributed-parametric, or mixed, and how is its content localized? | Storage guarantees, behavioral authority, evaluator adequacy, or revision reach. |
| Substrate-supplied guarantees | Which schema, query, integrity, or transaction guarantees surround the target? | Representational form or semantic correctness. These guarantees must be reported separately rather than as one “database” value. |
| Reflective coverage | Which target aspects have a causally connected self-representation available to processes inside the boundary, and with which coverage-operation profile? | Semantic addressability for every operation, or update reach. Reflection is required only for a reflective-revision claim, not for all self-improvement. |
| Addressability profile | Can the pathway retrieve, interpret, criticize, revise, rescope, or transfer the target as an object? | Authority to install a revision or evidence that it would improve behavior. |
| Raw change authority | What state can processes inside the boundary physically write, replace, or rebind? | That the pathway can identify or formulate the needed change. |
| Determination reach | Which target deltas can the pathway actually formulate or determine under admissible inputs and evidence? | That a determined result can enter the bounded system's organization. |
| Installation reach | Which determined results can actually become changes to the bounded system's behavior-determining organization? | Evidence-responsiveness, a live behavioral-authority path, or subsequent exercise. |
| Effective revision reach | For which indexed claims do determination and installation reach both hold? | Warrant, operativity, or a favorable outcome. It is a derived intersection, not another intrinsic target axis. |
| Revision closure | Which operative parts, mappings, derivatives, interfaces, and checks must change or be revalidated together for the revision to remain coherent? | That a smaller closure is always safer or better; atomic bundles can preserve invariants and apparently local changes can have broad effects. |

These properties affect inspection, intervention, coordination cost, and blast radius. They do not establish that a change is good. A natural-language instruction can be tested through deterministic downstream behavior; symbolic code can require semantic review; a formal proof can be rigorous about a formalization that misses the external objective.

### 2. Revision-governance map

This map describes the governance profile of a named pathway and the transition-specific records needed when it is exercised:

| Field | Question | What it does not establish |
|---|---|---|
| Evidence-responsive update architecture | Does evidence directly determine the update, or does a reject-capable process select among proposals? Which composed subpath is being classified? | The quality of its evidence or whether the change became operative. Blind or unconditional self-revision is outside this improvement-pathway contrast. |
| Determination or update-law profile | What mapping turns state, evidence, and other inputs into a delta or candidate class, with what constraints, stochasticity, scope, and assumptions? | That the rule's evidence response is adequate for the objective. Direct paths especially need this field; an evaluator profile is not a substitute. |
| Evidence-assessment or evaluator profile | When assessment is separable, which criterion and evidence channel shape the direct update or proposal verdict, over what domain, with what discrimination, independence, timing, cost, and uncertainty? | That the relation is adequate for this target, objective, and risk. A direct update need not contain a distinct evaluator. |
| Source-state governance scheme `Σ_t` | Which roles, grant scopes, decision rules, installation paths, activation ordering, and monitoring or recovery requirements govern the change class at this epoch? | That a particular transition conformed to the scheme or was epistemically or risk-wise justified. |
| Transition control record `C_Δ` | Did this transition conform to the applicable update law, grant scope, actor allocation, installation and activation order, and required monitoring or recovery? | Improvement warrant or bounded-risk justification. `A_Δ` is one required subrecord, not the whole conformance trace. |
| Transition authority cut `A_Δ` | Did every live installation path cross source-authorized controls whose relevant authority and scope predated the delta, could not be bypassed or changed before activation, and were causally necessary? | Full conformance to `Σ_t`, or more than exclusion of wholly successor-conferred authority. A rubber stamp can pass this test. |
| Improvement warrant `W_Δ` | Why is the evidence-to-update or evidence-to-verdict relation adequate for this objective, domain, change class, risk, and horizon, without assuming the contested successor is already trustworthy? | Installation, later uptake, or permission to run an uncertain experiment merely because its downside is bounded. |
| Bounded-exposure authorization `E_Δ` | Given a source-authorized, conforming path, why may an uncertain transition run under this scope, duration, magnitude, detection, containment, and recovery envelope? | That the update is an improvement. It adds a risk basis for exposure to `C_Δ`; it does not replace control provenance or conformance. |
| Authority-path entry | Through which consumer, channel, and force did the installed change enter a live behavioral-authority path capable of reaching later behavior? | That any subsequent operation actually depended on the change. |
| Subsequent exercise | Which later operation causally depended on the installed change over the declared horizon? | That the resulting behavior was better, or that the change will influence another revision. Together with authority-path entry, this establishes operativity. |
| Recovery profile | Can harm be detected, attributed, localized, rolled back, or repaired, and at what delay and cost? | Correct original acceptance. Recovery can help authorize bounded exposure by limiting downside; it does not supply evidence that the change is an improvement. |

The rows across both maps do not form a ladder. A read-only self-model can have reflective coverage, behavioral authority, and later exercise without revision reach. Online gradient descent can have effective and operative direct revision without an explicit self-representation or rejection event. Opaque checkpoints can support rollback without semantic addressability. Even a closed, evidence-responsive operative pathway establishes improvement-directed change rather than a favorable outcome; outcome evidence is a further claim.

The pathway profile is indexed to a source state or epoch. `Σ_t` is the dispositional scheme for a claimed change class. For an occurrent claim, a transition record `Δ: s → s′` separately records evidence dependence in determination, installation into behavior-determining organization, and—when the corresponding claim is made—`C_Δ`, `W_Δ`, or `E_Δ`, followed by entry into a live authority path and later exercise. `C_Δ` records conformance to `Σ_t` and contains `A_Δ` as its authority-cut subrecord. `E_Δ` adds the risk justification for exercising that controlled path under uncertainty; `W_Δ` independently bears on improvement. One controlled or warranted episode lower-bounds the corresponding reach only for the demonstrated delta or justified change class; it does not cover every delta the pathway can produce.

### 3. Coverage-accounting map

The most that can currently be stated cleanly is declared-model coverage. Its accounting unit is not a bare target. Let `i` be an inventory obligation naming the boundary, source state or epoch, objective, assessment context, target aspect, granularity, and change class. Coverage is normally dispositional; an occurrent claim adds a transition and horizon separately.

- `I`: the declared inventory of obligations `i`;
- `D(p,i,m_D)`: pathway `p` has determination reach for `i`, with evidence annotation `m_D`;
- `L(p,i,m_L)`: pathway `p` has installation reach for `i`, with its own annotation `m_L`;
- `R(p,i)`: effective revision reach — supported `D` and `L` claims both hold for that path and obligation;
- `C(p,i,m_C)`: **controlled reach** — in addition to `R`, an effective source-state `Σ_t` governs authority provenance, scope, installation, activation, and required monitoring or recovery for the change class, with evidence annotation `m_C`;
- `W(p,i,h,m_W)`: **improvement-warranted reach** — in addition to `R`, the evidence response is adequately connected to the objective for obligation `i` over horizon `h`, with its own annotation `m_W`;
- `E(p,i,h,m_E)`: **bounded-experiment reach** — in addition to `C`, source-authorized uncertain transitions in the class have adequate risk grounds for exposure within a stated envelope, with annotation `m_E`;
- `X(i)`: a declared exclusion from revision;
- `F(i)`: a warranted effective freeze — `X(i)` plus evidence that the obligation remains outside all in-scope effective revision paths over the assessment frame;
- `U`: consequential behavior-determining organization absent from `I`.

Each `m_*` independently records whether its claim is declared, theoretically possible, demonstrated, or routinely exercised; determination reach, installation reach, control, improvement warrant, and exposure authorization need not have the same evidential standing. **Declared controlled coverage** requires both that every established `R` path–obligation pair has a corresponding `C` claim whose evidence meets the assessment context, and that every `i` in `I` has at least one such controlled path or a warranted effective freeze. `W` and `E` are then reported separately: `E` refines `C` with a risk justification, but neither implies `W`; process-level `W` need not warrant every step. For an occurrent claim, `O(p,i,h,m_O)` additionally records authority-path entry and subsequent exercise over horizon `h` with its own evidence annotation.

The per-obligation relations are projections, not a composition rule for a multi-obligation transition. Let `Cl(Δ)` be the revision closure: every before- or after-state obligation, changed interface, and interaction whose coherence or exposure is affected by `Δ`. `C_Δ`, `W_Δ`, and `E_Δ` are joint records over `Cl(Δ)`; their projections can support `C(p,i,…)`, `W(p,i,…)`, and `E(p,i,…)`, but conjoining the per-`i` claims does not establish the joint record. Any new interaction obligation discovered while constructing `Cl(Δ)` must enter the successor inventory.

The useful residuals are explicit: `R` without `C` is effective but uncontrolled reach; `C` without `W` is controlled but not improvement-warranted; `E` without `W` is authorized experimentation, not an improvement claim; an `i` with neither a controlled path nor `F(i)` is a known unresolved coverage gap; `X` without `F` is a declared exclusion not yet shown to be protected and warranted. But `U` is not an enumerable set available to the system: an audit can discover an omitted aspect and thereby refute completeness, while failure to discover one does not prove `U` empty.

Use *governed* only as a natural-language umbrella after specifying which of `C`, `W`, and `E` is meant. Declared controlled coverage is defensible; absolute “complete self-revision” remains unauditable.

### Coverage across epochs requires a migration record

Architectural revision can change `I` itself. There is no general identity relation from a before-target to an after-target: one role can split across several successors, several artifacts can merge while retaining separately criticizable aspects, and new interfaces create obligations with no predecessor. Use an explicit migration record between epoch inventories:

`M_Δ = (Λ_Δ, New_Δ, Retired_Δ)`

`Λ_Δ` is a labelled many-to-many relation from before-obligations to after-obligations; its fan-out and fan-in express splits and merges, while labels distinguish carried from transformed contributions. `New_Δ` holds introduced obligations with provenance, and `Retired_Δ` holds obligations with no successor plus a retirement rationale and evidence. Each before obligation needs an outgoing lineage edge or justified retirement; each after obligation needs an incoming edge or introduced marker. Splits require fresh coverage for every child. Merges create new coherence and interface obligations not implied by coverage of their inputs. Changed producer–consumer edges must be revalidated.

`M_Δ` transports correspondence only. Determination reach, installation reach, effective reach, control, warrant, bounded-exposure authorization, operativity, and effective freeze each require their own evidence-transport rule or reassessment at the successor epoch. The [path-valued type-contract test](./discriminating-tests.md#test-2-targets-persist-by-lineage-not-identity) establishes this need; what remains moving is how to anchor lineage nodes, derive merge-created obligations, justify retirement, and decide when evidence can cross an epoch or boundary without replay.

## Why one kernel is insufficient

The first model used *kernel* for too many boundaries:

1. permanent exclusions outside the system or target boundary;
2. targets that are currently unreachable or deferred;
3. declared, warranted, effectively protected exclusions (`F`);
4. consequential but unrepresented organization (`U`);
5. the source-state governance scheme and authority cut for a particular transition.

These structures behave differently. In particular, the last is not necessarily permanent. `Σ_t` is the versioned source-state scheme of roles, grant scopes, decision rules, installation paths, and activation ordering. For transition `Δ`, `A_Δ` is the authority-cut subrecord inside `C_Δ`: every live path that can install or activate the contested delta must cross controls whose relevant authority and scope predate the delta, which the delta cannot mutate or bypass before activation, and whose operation is counterfactually necessary. `A_Δ` is an episode record, not another coverage class; the source controls whose operation it records may themselves be among the targets of the transition.

This cut is necessary and sufficient only for excluding wholly successor-conferred authority relative to the declared installation paths. It does not establish epistemic independence or warrant: a causally necessary incumbent can rubber-stamp a successor, share its errors, or apply a candidate-authored criterion whose probative force presupposes the candidate. Those failures belong in `W_Δ`, which must state non-circular grounds and adequacy for the objective, assessment context, and full revision closure.

A properly warranted incumbent evaluator can therefore govern its replacement before that replacement becomes authoritative. Later, the successor can participate in governing another change to the former evaluator. The versioned authority graph can remain acyclic while evaluator components rotate; no evaluator need be permanent, although an unchanged `Σ_t` would still be fixed machinery. The Gödel machine is the limiting formal case: incumbent axioms and utility license a successor program that may include replacements for them, while reserved hardware remains outside the software transition boundary.

For now, do not use bare *kernel* as the workshop's central object. If the term survives, it must name one of the structures above relative to a declared inventory, granularity, boundary, and horizon. Kernel shrinkage is meaningful only within a stable comparison frame and only when a warranted exclusion moves into controlled reach with whatever improvement warrant or bounded-exposure authorization the assessment context requires.

## Direct and proposal-selected pathways

The general model must not import a gate from proposal selection. The following contrast classifies evidence-responsive revision edges. A blind or unconditional rewrite has a direct transition shape but is not a direct self-improvement pathway, because no improvement evidence shapes it.

- In **proposal selection**, a proposed or already actualized change can be blocked, discarded, rolled back, or denied continued retention by a verdict that is distinct from producing the next variation.
- In a **direct update**, evidence determines the successor at the classified edge with no rejectable candidate and no selection, rollback, or continued-retention decision distinct from producing the next update. Improvement warrant rests on the update rule's evidence relation, scope constraints, and domain justification. Monitoring, containment, and recovery can separately justify bounded exposure by limiting downside; an outer rollback gate would be a composed proposal-selected pathway rather than part of the direct edge.
- In a **composed system**, design selection, batch installation, runtime enforcement, and later state updates may use either architecture independently. The architecture label therefore attaches to the named pathway and granularity, not the whole system.

The improvement objective is a semantic comparison basis. A final adoption veto is subtype-specific machinery, not a universal licensing floor.

## Audit of the proposed design space

The earlier axis list combined target properties, pathway properties, and safeguards. The current dispositions are:

| Candidate | Disposition | Boundary status |
|---|---|---|
| Representational form | **Keep.** It changes the default direct inspection route and content-localization profile. It does not determine evaluator regime or assurance strength. | Stable enough to use. |
| Substrate discipline | **Decompose.** Schema enforcement, query algebra, transactions, and integrity constraints are independent guarantees that files or databases can supply in different combinations. | Components known; decomposition still moving. |
| Consumption path / executor | **Replace with behavioral authority**: consumer, channel, and force. Keep the target's consumer distinct from the update evaluator. | Distinction stable. |
| Addressability / granularity | **Split.** Addressability is an operation profile over a represented target; granularity is a coordinate of the claim. Mechanical location is not semantic addressability. | Split stable; anchoring obligation-lineage nodes remains moving. |
| Provenance / history | **Split.** Artifact lineage supports attribution, invalidation, and regeneration; obligation lineage maps revision targets across epochs; version history supports comparison and bisection; recovery supports restoration or compensation. | Distinctions usable; lineage transport and effective recovery remain pathway-specific. |
| Locality / coupling | **Recast as revision closure or dependency topology.** It is change-relative and can reverse between migration time and steady state. | Moving and not yet established as one axis. |
| Update law / evaluator | **Split by architecture.** Direct paths need the mapping, constraints, stochasticity, scope, and assumptions of `U`; proposal paths additionally need evaluator criterion, domain, discrimination, independence or correlated error, timing, cost, and uncertainty. | Need for both profiles is stable; their minimal shared vocabulary is open. |
| Determination, installation, and effective revision reach | **Add as derived relations**, not target-position axes. Effective revision reach is the intersection of the first two for an indexed claim. | Split stable; measurement and modality moving. |
| Controlled / improvement-warranted / bounded-experiment reach | **Keep as three derived relations.** Control and improvement warrant do not imply one another; bounded-experiment reach refines control with a risk justification but does not imply improvement warrant. | Split stable; operational thresholds remain context-relative. |
| Update architecture | **Add as a pathway coordinate.** Direct and proposal-selected paths have different warrant structures. | Stable. |
| Actor allocation, authorization, and installation | **Add as pathway topology.** Who determines, authorizes, installs, monitors, vetoes, or reverses is distinct from who consumes the target later. | Moving. |
| Recovery | **Keep outside improvement evidence.** It changes containment, exposure authorization, and correction cost, not the truth of the original improvement claim. | Distinction stable; contribution to bounded-experiment authorization moving. |

An axis earns membership only if it asks one stable property question; varying it while holding the claim coordinates and other factors sufficiently fixed changes a feasible operation, evidential claim, installation guarantee, or containment capability; its effect is not already derivable from another axis; and coherent cross-combinations demonstrate some independence. Artifact names, correlated bundles, and maturity scores fail this test. Composite properties should remain profiles rather than being scalarized.

## Three senses of decomposition change

The cases exposed three useful provisional senses of *decomposition change*. They are comparison dimensions, not yet an exhaustive or mutually exclusive partition:

1. **Role inventory** — which functions or artifact roles exist;
2. **allocation or realization** — which actor or component performs a function;
3. **topology or interface** — how functions are separated, connected, and authorized.

The tag-README episode changed verification allocation from agent judgment to validator enforcement, but did not add an artifact role. The reports layer and proposal lifecycle changed the role inventory. Path-valued types and the general freshness store also changed interfaces or subsystem boundaries. These can all be architectural revisions at the appropriate granularity without being the same kind of decomposition change.

One revision can span several senses, and the classification is granularity-sensitive. Moving one file may be an ordinary edit while changing the collection role that governs a family of files is architectural. A before/after account at the claimed layer — role inventory, allocation map, or topology/interface — plus an obligation-lineage mapping is therefore required before claiming that decomposition itself changed.

## What the current cases actually separate

| Case | What it supports | Boundary that moves |
|---|---|---|
| Tag-README completeness mark | Controlled human-inclusive revision of verification allocation, followed by deterministic enforcement and later use. | Computational subsystem versus human-inclusive system; artifact-role versus functional-allocation granularity; design adoption versus runtime enforcement pathway. |
| Reports layer and proposal lifecycle | Economical examples of new artifact roles and later use. | Creating proposal-selection machinery does not prove that the episode creating it was itself proposal-selected. An ADR alone records a decision; migrated and later-consumed artifacts establish use. |
| Darwin Gödel Machine | Broad code mutation can reach decomposition changes while target diagnosis and parts of the improvement machinery remain fixed. | Admission is viability-gated, while benchmark quality affects reproductive selection only over later generations; parent, archive, population, and controller yield different boundaries. |
| Gödel machine | A theoretical construction for broad, proof-governed, decision-relative software revision. | Syntactic write scope can be broad while provably reachable change is almost empty; incumbent authority machinery can license successors without constituting a permanent component kernel, while adequacy still depends on the formal premises. |

These cases diagnose the dimensions; they do not jointly establish a universal catalogue or a complete practical system.

## Boundary status

### Stable enough to use

- target affordances, pathway governance, and coverage accounting are different maps;
- representational form and evaluator regime are distinct;
- reflective coverage, addressability, determination reach, installation reach, procedural control, improvement warrant, bounded-experiment authorization, authority-path entry, subsequent exercise, and recovery are distinct;
- direct and proposal-selected evidence-responsive update paths need different governance accounts;
- an obligation-migration record, rather than persistent artifact identity, is required across inventory-changing revisions;
- `Σ_t`, transition conformance `C_Δ`, its authority-cut subrecord `A_Δ`, epistemic warrant `W_Δ`, and exposure authorization `E_Δ` are different records;
- pathway architecture and decomposition claims are indexed by target and granularity;
- recovery does not strengthen the evidence that originally supported a revision.

### Moving

- how to anchor obligation-lineage nodes through splits, merges, and redistributed responsibility, and how each coverage relation transports evidence;
- operational evidence thresholds for `C`, `W`, and `E`, especially in direct updates and at trajectory horizons;
- the recording form for `Σ_t`, `C_Δ`, `A_Δ`, and the full set of live installation paths;
- evaluator profiles and the relation between domain, independence, cost, and target risk;
- revision closure and how to compare coordination burden across a migration and steady-state use;
- the exact boundary among role-inventory, allocation, interface, and subsystem changes;
- how much recovery and containment suffices to authorize a bounded experiment for a given risk.

### Unknown or currently unauditable

- whether *commitment* can be individuated consistently across representational forms;
- whether particular target positions impose contingent upper bounds on attainable evidence, beyond the settled claim that position alone establishes no general acceptance-quality ceiling;
- whether the design-space catalogue can ever be complete;
- whether an empty unrepresented remainder can be evidenced;
- whether cross-system coverage or kernel comparisons survive different inventories and granularities;
- how epistemic non-circularity can be tested when candidate-produced evidence is informative but may presuppose the candidate's disputed adequacy.

## Next discriminating tests

The first three tests are recorded in [Discriminating tests](./discriminating-tests.md). The next useful tests should attack what they left moving:

1. apply `C`, `W`, and `E` together to one unlike pathway to test whether the three-relation split is sufficient rather than case-fitted;
2. distinguish declared, theoretically possible, demonstrated, and routinely effective reach for the same target and pathway;
3. test whether revision closure predicts a real coordination or recovery difference after the other claim coordinates are held fixed;
4. reconstruct one justified retirement and one boundary change to test when obligation-lineage evidence can be transported without replay;
5. test epistemic non-circularity on candidate-produced evidence that is useful but partially dependent on the candidate.
