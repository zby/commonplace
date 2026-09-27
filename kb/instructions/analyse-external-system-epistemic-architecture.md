---
description: Invoked by analyse-agentic-system in every run to trace the analysed system's epistemic routes over the run's canonical records and fill the result's Epistemic lens section as a sparse overlay.
type: types/instruction.md
---

# Analyse an External System's Epistemic Architecture

Goal: an evidence-bounded, route-by-route account of whether and how the analysed system acquires or produces truth-apt content, checks it, grants or withholds reliance on it, retains or integrates it, and lets it affect later behavior, with no system-wide epistemic grade.

`analyse-agentic-system` invokes this procedure in every run, locally or in a worker with the same frozen boundary, after the runtime baseline has produced the canonical `SRC-*`, `OBJ-*`, `RTE-*`, `CLM-*`, `ABS-*` and `BAP-*` records and the epistemic scoping record. The output is the result's `### Epistemic lens` section. The [result type](../types/agentic-system-analysis-result.md#lens-outputs) fixes its six blocks, their fields, the controlled values and the terms they use; read that contract first. This instruction says how to fill it. The analysis informs a review; it does not itself accept the external system's claims.

## Overlay rules

- Annotate canonical IDs; do not build a second inventory. Before the epistemic fields, repeat at most the canonical ID, one source-native short label and one local evidence anchor. Write `see <canonical ID>` for a field the canonical record owns. Do not copy generic identity, representational form, storage substrate, common route endpoints or progression, or claimed-operation identity.
- A newly discovered object, route, claim, absence or authority path takes an invocation-local proposal tag and supplies the full identity the coordinator needs to register it; never mint a canonical ID. Return a targeted-read request for new source material, and a correction with its evidence anchor for a defective canonical fact.
- Retain minimum verbatim code or prose for load-bearing findings as quote blocks under the result type's [Source register](../types/agentic-system-analysis-result.md#source-register) contract, generated with [`commonplace-quote`](../reference/commands.md#commonplace-quote) and inserted unchanged. Write every canonical ID or local proposal tag in full in every list, as the type's [Canonical identity](../types/agentic-system-analysis-result.md#canonical-identity) rules require.
- Keep the evidence layers separate and never upgrade one into another. Inspect each representational form appropriately: read natural-language content, test symbolic artifacts within their declared semantics, and use available probes for distributed-parametric state. If the available probes cannot individuate truth-apt content, record the object or lifecycle phase as `not determinable`.
- Treat an intentionally operational or lab-tracking purpose as a scope boundary, not as product failure. Do not prescribe natural-language claims, proposal comparison, a storage model, or a universal knowledge ontology.
- If exhaustive whole-system coverage is infeasible, declare the assessed and unassessed route families and make no system-complete conclusion. Name omitted route classes and the conclusions their omission prevents.

## Steps

1. **Fix the boundary.** Fill block 1 from the scoping record and the Source register: declared scope and exclusions, the analysis question, assessed and unassessed route families, every evidence gap with the conclusion it prevents, and the system's knowledge-production or warrant claims by `CLM-*` ID.

2. **Inventory material objects before evaluators.** Fill block 2 for every operative part inside the material-route boundary the type defines. Use system-specific object names and split heterogeneous containers under proposal tags. Name each target object or proposition and its domain before assessing any evaluator.

3. **Apply the early branch.**

   - If the inventory shows only storage, retrieval, serving, or direct use, with no relevant transformation and no knowledge-production claim, add a ledger row for each material evidenced function or an explicit `no relevant route found`, record no relevant check or epistemic authority within the boundary together with any operational and behavioral authority, write the global no-candidate statement, an explicit no-claim comparison, and a bounded negative conclusion. The lens output is then complete.
   - If the system makes a knowledge-production claim but no implemented or observed route supporting it was found, inventory the claimed object and first classify its claimed transformation. If the claim evidence establishes ampliation, use the lifecycle record: declared phases `doctrine only`, unclaimed phases as the scoped evidence permits, every unobserved candidate phase `no instance observed`. Otherwise use the non-ampliative or indeterminate disposition. Add ledger rows for the claimed functions and compare the claim with the absent supporting implementation or operation. Continue with any remaining implemented or observed routes; never let this branch discard them.
   - Otherwise continue. Never expand a scoped absence into a claim that no informal or unobserved route exists.

4. **Classify content edges and direct adaptations.** Give every truth-apt content-producing or content-changing edge one content/update relation from the type's list, testing the values in the order listed and splitting sequential transformations into separate edges. Record source warrant for an acquisition as preserved, degraded, or unknown. Carry warrant into an entailed derivation only from warranted premises through a checked interpretation or formal domain. Novelty, fluency, and plausibility establish candidate generation only. When preservation or entailment cannot be established, state the classifications still possible and the evidence needed. Describe a behavior or policy adaptation with no evidenced truth-apt object as a non-truth-apt update; do not force it into the truth-apt classes. For a consequential route with no content update, write `no content change` and still analyse its function, target, condition, force, authorities, consumer, and horizon.

5. **Build the authority-route ledger.** Fill block 3. Name the check target before the evaluator. Record architectural status independently of function, and activation conditions separately: an implemented route may be conditional or inactive in the inspected configuration. Record an evidenced absence without inventing an evaluator. Use linked rows where one implementation performs several functions. A recorded result with no consequential consumer has no implemented force.

6. **Dispose every object.** Fill block 4. Apply the discovery lifecycle only after ampliation is established, and record each phase's architectural status separately from its observed candidate state, citing the evidence layer through its source ID. Implementation or doctrine alone never establishes an observed candidate state; upgrade a phase only from candidate-linked evidence of that phase. If a persisted candidate artifact exists but no provenance or trace links it to the implemented routes, the artifact establishes only that a candidate instance is available: record those phases `not determinable`, not `phase evidenced` or `accepted`. Record post-acceptance integration separately from retention and pre-acceptance use.

7. **Bound each check's licenses.** For every ledger row, state what the result warrants, what it permits or changes operationally, how it becomes behaviorally consequential, and what it does not establish. Keep separate:

   - outcome from producing process, explanation, replay safety, transfer, and component effect;
   - a valid reconstructed route from evidence that it produced the observed outcome;
   - consequence fit from warrant for the proposed mechanism and its transfer boundary;
   - formal validity from source truth, encoding fidelity, omitted premises, and claims outside the formal domain;
   - applicability or freshness from endorsement;
   - operational continuation from epistemic warrant; and
   - bundle success from the effect of an individual component.

   Attribute a component effect only when the observed comparison independently varied that component, and only at the grain of the actual contrast. State why the design does or does not license a causal interpretation.

8. **Compare claims with routes.** Fill block 5, comparing each claim across doctrine/design, implementation, observed-run, and causal evidence. Record a deliberately operational scope without treating it as failure, but still expose any mismatch between that scope and a broader knowledge-production claim.

9. **Conclude by route.** Fill block 6. Report imported content as acquired, not produced. Report an entailed output as derived warranted content only when its premises and derivation are warranted within the declared domain. Report a non-entailed truth-apt output as a produced accepted ampliative claim only when an evidence-consuming acceptance transition names its criterion, intended use, and scope. Retention, retrieval, reshaping, direct adaptation, operational use, or candidate generation alone does not qualify as knowledge production. Report acceptance and post-acceptance integration separately. Do not turn acceptance into infallibility, integration into acceptance, or one route's result into a system label.

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

- Every operative part inside the boundary is annotated or proposed, and heterogeneous parts are split.
- Every truth-apt content edge is classified or bounded as indeterminate; every non-truth-apt update is described without forcing it into that taxonomy; every route with no content update says so.
- Every ampliative phase separates architectural status from observed candidate state, and implementation or doctrine alone never establishes an observed disposition.
- Every negative or unknown is scoped; no license exceeds its target, contrast, domain, horizon, or route.
- The conclusion includes only decision-relevant findings, uses route-level verbs, and gives no system-wide epistemic grade.
