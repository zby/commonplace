# Discriminating tests

**Status: backstage.** The conclusions these tests forced are restated without notation in the [plain account](./plain-account.md); the tests themselves stay on record here.

These tests attack the boundaries identified in the [revision-profile synthesis](./boundary-map.md). They are not additional examples for the article. Each test asks whether the current model can classify a hard case without changing the frame mid-argument; a passing test may still force the vocabulary to split.

| Test | Result | Model change |
|---|---|---|
| Gate-free direct update | Architecture-neutral membership survives, but one “governed reach” relation does not. | Separate controlled reach, improvement-warranted reach, and bounded-experiment authorization; add an update-law profile. |
| Target through split and merge | Persistent target identity fails. | Carry obligations across epochs with an explicit migration record; re-establish coverage over successor obligations and new interfaces. |
| Rotating evaluator authority | Evaluators can rotate without a permanently fixed evaluator. | Put an effective source-state authority cut `A_Δ` inside a full transition-control record `C_Δ`; keep epistemic warrant separate and stop seeking an architecture-only cure for circular evidence. |

## Test 1: a direct update can be warranted without a gate

### Frame

For a direct evidence-responsive transition, write:

`Δ: s —[e, U, K]→ s′`

- the antecedently specified objective `J` makes observation `e` improvement-relevant evidence;
- the incumbent update law `U` maps state and evidence directly to a successor;
- constraints `K` bound the mapping's target, magnitude, domain, or operating conditions.

There is no candidate standing to be rejected at this edge. Removing or replacing `e`, while holding the updater's other inputs fixed, must change what `U` computes or its output distribution. The result must then be installed in the system's behavior-determining organization, enter a live authority path, and affect a later operation for an occurrent self-improvement claim to close.

This causal test establishes membership. It does not yet establish that `U` is a good rule or that running it at the current risk is authorized.

### Three claims that the gate vocabulary had collapsed

1. **Controlled reach.** A source-state governance scheme names `U`, its write envelope, constraints, actor allocation, installation authority, activation ordering, and required monitoring or recovery. This says whether a reachable revision conforms to an antecedently authorized procedure and scope; it does not say why exercising that authority is epistemically or risk-wise justified.
2. **Improvement-warranted reach.** Evidence supports that `U`'s response is adequate for `J` over a stated domain, change class, risk threshold, and horizon. The warrant may apply to a trajectory class rather than every individual transition.
3. **Bounded-experiment reach.** Given controlled reach, an uncertain update is allowed because limits on scope, duration, magnitude, detection delay, containment, or recovery make it safe enough to try. This adds risk justification to source-state authority; it is not evidence that the update improves behavior.

`W` does not imply `C` or `E`, and `C` does not imply `W` or `E`; `E` refines `C` and does not imply `W`. A theorem can warrant a process under assumptions while the installation path is uncontrolled. Recovery can support bounded exposure without strengthening the evidence-to-objective relation.

### Case comparison

| Case | Control, warrant, and exposure | Installation and use |
|---|---|---|
| [Online projected gradient descent](../../sources/zinkevich-online-convex-programming.md) | `U` is the gradient step plus projection; the feasible set, gradient interface, and learning-rate schedule define its control envelope. The regret result warrants the process only under its convexity, boundedness, access, and cumulative-horizon assumptions. Projection supplies feasibility containment, not monotonic step-level improvement. | The next point is adopted directly. Operativity needs a later decision or gradient evaluation to use it. |
| [Homeostat](../../sources/ashby-design-for-a-brain-ultrastability.md) | Essential-variable bounds, the critical-state trigger, step mechanism, and random table control the transition. Under the ultrastability assumptions, the horizon-level claim is return to viability; no particular random successor carries successor-specific improvement warrant. | A new setting immediately governs reactions. A later violation triggers another direct transition rather than rejecting the earlier setting as a candidate. |
| [Continual Harness](../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) | Failure windows, a fixed Refiner schedule, CRUD surface, four-part harness decomposition, tools, and model judgment define `U` and its envelope. Local repair evidence is narrow; mixed results and harm for Flash-Lite defeat broad warrant. Editable scope limits some blast radius, while weak rollback and retirement evidence leave bounded-exposure authorization incomplete. | Edits enter the next step directly. A used prompt or skill can become operative; an unused skill or rarely retrieved memory shows why installation is not artifact-level operativity. |

### Verdict

The direct path needs no evaluator component, adoption veto, or candidate object. Its missing profile field was the **update law**: mapping, stochasticity, constraints, scope, and assumptions. The [proposal-selection loop](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) remains the right vocabulary only when a verdict can block, discard, roll back, or deny continued retention by an operation distinct from producing the next update.

The important moving boundary is horizon. Online gradient descent and the Homeostat can have process- or trajectory-level warrant without a claim that each step improves the objective. Continual Harness can have standing permission to edit and direct installation while lacking broad evidence that the rule improves every target class. A revision profile must therefore attach warrant and exposure authorization to their own change class and horizon.

## Test 2: targets persist by lineage, not identity

### Frame

[ADR 018](../../reference/adr/018-types-are-path-references-to-instruction-docs.md) changed Commonplace's type-contract architecture in one whole-KB migration. The target is the architecture, not one renamed file. Compare the source epoch immediately before the migration with the installed result.

```text
Before: artifact + enum + collection
          ├─ skill-side lookup → template + instructions
          └─ validator lookup → conventionally named schema

After:  new write → COLLECTION type menu → type-spec path
        typed artifact → type-spec doc → explicit schema pointer
```

### Lineage reconstruction

| Before obligation or role | After obligation or role | Disposition |
|---|---|---|
| Bare type name plus collection scope carries identity | Resolved type-spec path carries identity | transformed |
| `{type}.template.md` body skeleton | Template aspect of the type-spec body | merged physically |
| `{type}.instructions.md` authoring guidance | Guidance aspect of the same type-spec body | merged physically |
| Inline default-note template plus canonical note materials | One `kb/types/note.md` contract | duplicate retired; content reconciled |
| Conventionally discovered sibling schema | Separate schema named by an explicit `schema:` pointer | role carried; interface changed |
| Lookup duplicated in skill prose and Python | Collection selection, stored binding, and validator dereference | responsibility split and reallocated |
| Implicit filesystem inventory | Curated `COLLECTION.md` type offerings | introduced selection surface |
| No contract governing type specs | Root `type-spec.md` plus its schema | introduced meta-contract |
| Enum fallback and retired sidecar roles | No successor | retired |

The migration changes all three provisional decomposition dimensions: role inventory, allocation, and topology/interface. It also shows why file identity is the wrong carrier. Template and guidance merged physically while remaining separately criticizable semantic aspects. “Type resolution” split into selection, binding, and dereference even though users may still describe it with one phrase.

### Coverage transport

Let `I₀` and `I₁` be the inventory obligations at the two epochs. Architectural revision needs a migration record:

`M_Δ = (Λ_Δ, New_Δ, Retired_Δ)`

`Λ_Δ` is a labelled many-to-many relation from `I₀` to `I₁`: fan-out and fan-in express splits and merges, while labels distinguish carried from transformed contributions. `New_Δ` records introduced obligations, and `Retired_Δ` records obligations with no successor plus a retirement rationale and evidence. Coverage transports only under explicit rules:

1. every old obligation has successors or a justified retirement;
2. every new obligation has predecessors or an introduced marker;
3. a split requires fresh coverage for every child;
4. a merge creates coherence and interface obligations not implied by coverage of its inputs;
5. every changed producer–consumer edge is revalidated;
6. the migration record transports correspondence only; every derived coverage claim—determination, installation, effective reach, control, warrant, bounded exposure, operativity, or freeze—needs its own evidence-transport rule or reassessment.

ADR 018 did unusually well at declared migration closure: it inventoried live type values, sidecars, writers, readers, skills, schema constants, and fixtures; migrated them atomically; and rejected a compatibility period. That supports source-checkout coverage at the migration horizon. It does not establish unrestricted inheritance. Template-to-schema consistency was explicitly deferred, and [ADR 021](../../reference/adr/021-ship-library-content-under-kb-commonplace.md)'s installed-library boundary later exposed non-portable repository-relative local-type pointers. [ADR 048](../../reference/adr/048-imperative-type-rules-dispatch-by-canonical-path.md) added a later obligation around canonical path identity. Those are epoch and boundary changes, not proof that one flat inventory was always incomplete.

### Verdict

The test rejects persistent target identity by artifact path or row equality. A semantic role or behavior obligation can have lineage across a split or merge, but its coverage does not automatically follow. The remaining open problem is not whether lineage is required; it is how to anchor its nodes, derive merge-created coherence obligations, justify retirement, and decide which evidence can cross an epoch or boundary without replay.

## Test 3: rotating evaluators need an authority cut and a warrant trace

### Frame

Use three versions:

```text
s₀: evaluator A₀ is authoritative
  Δ₁: A₀ governs activation of evaluator B₁
s₁: B₁ is authoritative
  Δ₂: B₁ governs activation of evaluator A₂
s₂: A₂ is authoritative
```

The component names appear cyclic, but the versioned authority graph `A₀ → B₁ → A₂` is acyclic. No evaluator component must remain permanently fixed. The analysis needs four records:

- `Σ_t`: the source-state governance scheme—roles, grant scopes, decision rule, installation paths, and activation ordering;
- `C_Δ`: the full transition-control trace showing conformance to `Σ_t`;
- `A_Δ`: the authority-cut subrecord within `C_Δ`;
- `W_Δ`: the epistemic warrant trace for the improvement claim.

### The narrow authority test

For the declared complete set of live installation paths, `A_Δ` is an effective **authority cut** when:

1. every path capable of installing or activating the contested delta crosses source-authorized controls;
2. the relevant authority and scope predate the delta;
3. the delta cannot mutate or bypass the controls before activation;
4. those controls are counterfactually necessary—without them, the transition cannot acquire authority.

This is necessary and sufficient only for excluding **wholly successor-conferred authority** within the declared path set. It works for proposal selection, where withholding approval blocks or rolls back, and for a direct path, where a source-authorized update law itself determines the successor. It catches decorative evaluators and hidden bypasses without imposing a universal veto, but it does not by itself show conformance to the rest of `Σ_t`; that belongs in `C_Δ`.

### Why the cut is not warrant

All of these can pass the narrow authority test and still fail:

- A is a required rubber stamp with no discrimination.
- A and B share correlated errors or collude.
- A runs a candidate-authored rubric whose probative force already presupposes that B is trustworthy.
- A authorizes only evaluator addition, while B later uses that provenance to claim replacement authority outside the original scope.
- `Δ₁` activates a new scheme `Σ₁` and then uses `Σ₁` to justify its own activation rather than having `Σ₀` cover the full revision closure.
- B later treats approval under successor objective `O₁` as proof that replacing terminal objective `O₀` was better. At most, `O₀` can license the transition relative to `O₀`; a stronger normative comparison needs an outside level.

These are epistemic or scope failures, not missing topology. `W_Δ` must separately state an antecedent objective, grounds whose probative force does not assume the contested successor's correctness, coverage of the full revision closure, and evaluator or update-rule adequacy for the assessment domain and risk.

### Verdict

Evaluator rotation is coherent. Within `C_Δ`, `A_Δ` should be a versioned source-state authority-cut subrecord recording `Σ` version, provenance, scope, causal necessity, bypass resistance, and activation order. It rules out wholly successor-conferred authority, not substantive circularity or bad judgment. There is no architecture-only sufficient condition for warrant; non-circular probative grounds and domain adequacy belong in `W_Δ`.

The open question therefore narrows. The workshop should stop looking for a stronger topology that somehow guarantees sound self-evaluation. The remaining problem is how to test epistemic non-circularity and adequacy in the assessment context, while allowing the components that realize `Σ` to change under a later source-state scheme.

## Consequences for the working model

1. Retire one formal `G` relation. Report **controlled reach** `C`, **improvement-warranted reach** `W`, and **bounded-experiment reach** `E` separately; use *governed* only as an umbrella when all relevant readings are spelled out.
2. Add an update-law profile for direct paths. An evaluator profile is insufficiently general.
3. Treat `Σ_t` as a dispositional source-state scheme, `C_Δ` as its occurrent conformance trace, and `A_Δ` as the authority-cut subrecord. Do not make one record do all three jobs.
4. Add an obligation-migration record `M_Δ` whenever an architectural change alters the inventory. Lineage edges, introduced roles, retirements, and changed interfaces trigger fresh coverage work.
5. Keep improvement warrant and exposure authorization distinct. Recovery can make an experiment acceptable to run without making its result an improvement.

These results are ready to update the boundary synthesis. Promotion to durable notes should wait until the revised notation survives one application outside these three tests.
