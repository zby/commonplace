# Workshop: Epistemic Architectures

## Goal

Compare the epistemic architectures of six research systems — how claims, evidence, warrant, and explanation route through each system's acceptance machinery, and what its operative oracle actually discriminates. The six cases:

- **Commonplace** — this KB: natural-language artifacts, declared quality goals, verdict/report review pairs, freshness baselines.
- **Eigenius** — typed kernel substrate: certificates, epistemic grades, path-specific commit gates, optional Lean proof checking; pinned authority in the [code-grounded review](../../agentic-systems/eigenius.md).
- **ScienceFlow** — long-horizon research-agent harness: evaluator-gated Stage acceptance, anchor selection, folded memory; pinned authority in the [code-grounded ingest](../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md).
- **AI Research OS** — skill-driven personal research wiki: immutable sources, LLM-maintained synthesis pages, deterministic indexes, structural lint, no reject-capable acceptance step; pinned authority in the [code-grounded review](../../agent-memory-systems/reviews/ai-research-os-workshop.md).
- **The ontology draft** — a private research-ontology design for an artifact-focused AI lab (v0.2, examined 2026-08-19): measurement-only acceptance over versioned objects, with explanation represented but unscored. Kept anonymous in all committed text until the authors approve naming; the source document is not ingested.
- **ARC skill** — prediction-gated game-solving harness: pre-action admission, post-action consequence grading, event evidence, prose notes, executable replay, provenance-bound plans, and halt-on-surprise execution. Its [code-grounded reading](./arc-skill-reading.md) is pinned to ARC commit `dba53c3`.

"Epistemic architecture" deliberately names the comparison plane, not a class of systems: every system has one, possibly degenerate, so "system X's epistemic architecture lacks a claim object" is a sayable finding. Whether a given system's machinery is genuinely epistemic is an output of the comparison, not a membership condition.

The selection angle that seeded this workshop is [weakly discriminated qualities tend to be underselected](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md); the lineage angle was already run for two of the systems in the [lineage-mechanisms](../lineage-mechanisms/README.md) workshop and is not this workshop's job.

## Threads

- [four-system-baseline.md](./four-system-baseline.md) — the opening position from the 2026-08-19 analysis: per-system operative-oracle readings, the four-way spectrum of where explanation sits relative to the oracle, the route-level asymmetry variant, and the response taxonomy (exile / grade-cap / declare-and-audit)
- [ai-research-os-reading.md](./ai-research-os-reading.md) — the fifth case: retention without an acceptance gate, selection moving to read-time as a candidate scope extension of the conjecture, the mark-and-expose response, and the participation × containment 2×2 that reframes the taxonomy
- [arc-skill-reading.md](./arc-skill-reading.md) — the sixth case: an authority-route ledger separating target, oracle, timing, force, epistemic authority, and operational authority; the system-level participation × containment 2×2 fails unchanged
- [Analyse an External System's Epistemic Architecture](../../instructions/analyse-external-system-epistemic-architecture.md) — promoted workshop result: a collection-neutral review procedure that inventories epistemic objects, separates truth-apt transformations from non-truth-apt adaptations, and traces checking, acceptance, integration, and behavioral force per material route
- **Response taxonomy (failed unchanged)** — the fifth case's participation × containment 2×2 cannot assign ARC one system-level cell. Participation and containment remain useful only as route-qualified questions; no unchanged taxonomy note should be promoted.
- **Route-level oracle asymmetry (open, candidate addition)** — asymmetry between commit routes into the accepted population, not just between qualities; Eigenius is the original witness. ARC strengthens the need to type each route's target and force, but is not positive evidence for explanatory-quality underselection.
- **Behavioral-authority fold (open handoff)** — a later run may add ARC as a bounded worked case to the [behavioral-authority decomposition proposal](../../reference/proposals/revise-behavioral-authority-decomposition.md). ARC warrants no new standalone theory note.
- [operator-response.md](./operator-response.md) — the draft's author responded (2026-08-19, corrected 2026-08-20): the draft is intended for publication, and the stated intent is lab tooling à la Neptune.ai, not theory production — reframing exile as deliberate scoping (the operator concurs that lab tooling is right to be evidence-heavy) while leaving the drift prediction and the tracking-vs-knowledge-production tension open
- **Attribution of the ontology draft (open, external)** — the author intends to publish the draft; once it is public, snapshot and ingest it and restore the anonymized references here and in the weakly-discriminated note to full citations. Until then everything stays anonymous.

## What closes this workshop

1. The durable claims extracted: the failed system-level response taxonomy either replaced by a route-qualified comparison or explicitly dropped; the route-level variant either added to the weakly-discriminated note with its warranted evidence edges or rejected with a reason.
2. The comparison itself consumed: anything worth keeping lands in library notes or an article; the workshop's tables are not promoted as-is, workshops being sinks.
3. The attribution question answered or parked with the contact.
4. The ARC worked-case fold into the behavioral-authority proposal either completed in a separate run or explicitly parked.

## Evaluation boundary

Evidence grades differ by system and the comparison must not flatten them: Eigenius and ScienceFlow claims rest on pinned code-grounded reviews; ontology-draft claims describe an unpublished design, not a running system — no loop has run, so all selection effects there are predicted by construction; Commonplace claims about itself can cite operational episodes (the Popperian-maintenance record) but are this installation's behavior, not the framework's in general. ARC's architecture claims are pinned to inspected code; its campaign quantities remain repository-reported because no run directories or component ablation were supplied.

## Bookkeeping

Plain markdown, workshop register. Started 2026-08-19 from the conversation that analyzed the ontology draft against Commonplace, added the designed-in example to the weakly-discriminated note, and re-read the Eigenius and ScienceFlow analyses through the selection angle. ARC was added on 2026-08-20 as the sixth case; it failed the system-level 2×2 unchanged and moved the working comparison to authority routes. The route-level method was promoted on 2026-08-20 as a reusable instruction after cold applications to ARC and held-out GBrain; the workshop remains open for its separate explanatory-underselection and attribution threads.
