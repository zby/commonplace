---
description: "Reproducing a record's content does not transfer its authority. Replacement requires a governed artifact with stable identity, integrity, contestability, and attribution; mutable records also require currentness and addressable revision."
type: kb/types/note.md
traits: [title-as-claim]
tags: [agent-memory, foundations]
---

# Parametric reproduction alone cannot replace an authoritative record

The debate over whether models can absorb a record often conflates two events. *Reproduction* occurs when a model trained on the record can state its content unaided. *Substitution* occurs when the original is retired and a replacement becomes authoritative. Reproduction alone does not accomplish substitution: copying content does not transfer the source's institutional status.

A parametric artifact can become authoritative, but only through a separate act of governance and only if the artifact and its interface supply the guarantees that the retired record provided. Successful substitution therefore requires:

- **Stable identity and citation** — a consumer must be able to identify, quote, link to, and audit the operative object. A checkpoint hash, fixed inference specification, recorded query, and signed response can satisfy this requirement; an unversioned recalled statement cannot.
- **Authenticity and integrity** — a consumer must be able to verify that the identified object is genuine and unaltered. Reproducing a signature-shaped string is not the same as furnishing a verifiable signature or equivalent integrity evidence.
- **Contestability** — a challenge must attach to a specific authoritative object and enter a governed appeal or amendment process. A versioned model service can participate in such a process; bare recall cannot.
- **Attribution** — the authoritative object must identify who adopted the record, under what mandate, and what it supersedes. A model can reproduce those provenance claims, but reproduction does not authenticate their relationship to the adopting authority.
- **Currentness**, for mutable records — the authority must say what is operative *now*. Parametric state can meet this requirement only if its governed update cycle keeps pace with deployment. This is the persistence condition analyzed in [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md).
- **Addressable revision or supersession**, for mutable records — a change must target a defined commitment and preserve its scope, lineage, and validation envelope. Explicit records provide direct handles today; modular adapters and model-editing techniques can qualify only when their edits are comparably scoped, attributable, and regression-checked. This is the current representational advantage described by [only explicit retention is durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md), not a claim that numerical state can never acquire those properties.

These guarantees belong to a governed artifact or service; they are not intrinsic to natural-language text. The durable role of a retention layer is therefore to preserve authority, not exclusive possession of information. A separate informational defense applies only before a commitment is recorded: no reader, regardless of capability, can regenerate its unentailed resolution from pre-decision sources, because [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md). That defense ends once the record enters a training stream.

Consider a repository-specific adapter retrained after every accepted decision, while signed decision records remain the objects used for training, appeal, and revision. The adapter is a derivative cache: reproducing those records accurately does not retire them. If governance instead designates a signed checkpoint and deterministic query protocol as canonical, and its release, appeal, and revision processes supply the guarantees above, then authority has transferred. The checkpoint service has become the authoritative record; content reproduction alone did not make it one.

## What this licenses

This distinction licenses a routing rule, not a survival forecast. Stable, repeated, authority-free content is a candidate for weights—or for deletion once models reproduce it reliably. Authority-bearing content belongs in an artifact whose representation and governance provide the required identity, integrity, contestability, and attribution; mutable content also requires currentness and addressable change. In present systems, those requirements usually favor explicit records, while a parametric projection can reduce retrieval costs without inheriting authority. The same distinction explains why [system-definition artifacts](./definitions/system-definition-artifact.md)—artifacts the system consumes with binding force—survive even when a model can reproduce the facts behind their constraints.

## Scope

- The central claim covers both mutable and immutable authority-bearing records. Mutability adds currentness and change-management requirements; an immutable authority-bearing decision still requires stable identity, authenticity, and attribution.
- An immutable, authority-free exposition—a tutorial or general mechanism writeup—can be absorbed once its content can be reproduced reliably and activated when needed. This is the genuinely absorbable case.
- Parametric reproduction still has value. A model that encodes the record layer may navigate it better and require less of it to be quoted into context. The claim is only that reproduction does not itself confer authority.
- A governed parametric artifact can become the authoritative record. That is a transfer of authority backed by versioning, integrity, appeal, and revision guarantees, not an automatic consequence of learning the old record's content.

---

Relevant Notes:

- [Only explicit retention is durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: the property comparison behind the substitution costs
- [Retained artifact](./definitions/retained-artifact.md) — defined-in: the umbrella term for the records a retention layer holds
- [Keep lineage and compiled views from drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — extends: turns the derivative-cache distinction into source-version, regeneration, staleness, and authority rules
- [Agent-R](../agent-memory-systems/reviews/agent-r.md) — evidenced-by: an iterative self-training framework whose checkpoint-level learning lacks per-lesson provenance, targeted recall, and invalidation at consumption
- [KBLaM](../agent-memory-systems/reviews/KBLaM.md) — evidenced-by: a knowledge-augmented language-model system that retains readable KB records beside parametric projections and identifies missing invalidation and source-to-weight lineage
- [ROME: Locating and Editing Factual Associations in GPT](../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md) — evidenced-by: demonstrates narrow parametric edits while leaving applicability scope, criticizable rationale, lineage, and invalidation outside the edit
- [Exo](../agentic-systems/exo.md) — evidenced-by: a self-modifying agent harness that protects canonical state, lifecycle, and the record of prior attempts beneath a rewritable executor
- [We should take text optimization more seriously](../sources/we-should-take-text-optimization-more-seriously.ingest.md) — evidenced-by: argues the same routing — stable repeated information toward weights, volatile and auditable information in text
- [Claude Workstream Kit and Fable agent scaffolding](../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) — abstracted-from: a source about a Claude Code project add-on and Fable model class where stronger models allowed checklists and compliance scripts to be deleted while authority constraints and cited-evidence gates remained
