# Workshop: Epistemic Architectures

## Goal

Compare the epistemic architectures of four research systems — how claims, evidence, warrant, and explanation route through each system's acceptance machinery, and what its operative oracle actually discriminates. The four cases:

- **Commonplace** — this KB: natural-language artifacts, declared quality goals, verdict/report review pairs, freshness baselines.
- **Eigenius** — typed kernel substrate: certificates, epistemic grades, path-specific commit gates, optional Lean proof checking; pinned authority in the [code-grounded review](../../agentic-systems/eigenius.md).
- **ScienceFlow** — long-horizon research-agent harness: evaluator-gated Stage acceptance, anchor selection, folded memory; pinned authority in the [code-grounded ingest](../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md).
- **The ontology draft** — a private research-ontology design for an artifact-focused AI lab (v0.2, examined 2026-08-19): measurement-only acceptance over versioned objects, with explanation represented but unscored. Kept anonymous in all committed text until the authors approve naming; the source document is not ingested.

"Epistemic architecture" deliberately names the comparison plane, not a class of systems: every system has one, possibly degenerate, so "system X's epistemic architecture lacks a claim object" is a sayable finding. Whether a given system's machinery is genuinely epistemic is an output of the comparison, not a membership condition.

The selection angle that seeded this workshop is [weakly discriminated qualities tend to be underselected](../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md); the lineage angle was already run for two of the systems in the [lineage-mechanisms](../lineage-mechanisms/README.md) workshop and is not this workshop's job.

## Threads

- [four-system-baseline.md](./four-system-baseline.md) — the opening position from the 2026-08-19 analysis: per-system operative-oracle readings, the four-way spectrum of where explanation sits relative to the oracle, the route-level asymmetry variant, and the response taxonomy (exile / grade-cap / declare-and-audit)
- **Response taxonomy (open, candidate note)** — three observed responses to the form-vs-explanation oracle asymmetry. Log-entry-grade until the mechanism is worked out and a further system either fits or breaks the taxonomy.
- **Route-level oracle asymmetry (open, candidate addition)** — asymmetry between commit routes into the accepted population, not just between qualities; Eigenius is the witness. Candidate one-sentence extension to the weakly-discriminated note plus `evidenced-by` edges for Eigenius and ScienceFlow.
- **Attribution of the ontology draft (open, external)** — ask the draft's authors whether it may be named and ingested; if yes, the anonymized references here and in the weakly-discriminated note can be restored to full citations, and the comparison becomes a shareable artifact for that conversation.

## What closes this workshop

1. The durable claims extracted: the response taxonomy either promoted to a note or recorded as a log entry and dropped; the route-level variant either added to the weakly-discriminated note with its evidence edges or rejected with a reason.
2. The comparison itself consumed: anything worth keeping lands in library notes or an article; the workshop's tables are not promoted as-is, workshops being sinks.
3. The attribution question answered or parked with the contact.

## Evaluation boundary

Evidence grades differ by system and the comparison must not flatten them: Eigenius and ScienceFlow claims rest on pinned code-grounded reviews; ontology-draft claims describe an unpublished design, not a running system — no loop has run, so all selection effects there are predicted by construction; Commonplace claims about itself can cite operational episodes (the Popperian-maintenance record) but are this installation's behavior, not the framework's in general.

## Bookkeeping

Plain markdown, workshop register. Started 2026-08-19 from the conversation that analyzed the ontology draft against Commonplace, added the designed-in example to the weakly-discriminated note, and re-read the Eigenius and ScienceFlow analyses through the selection angle.
