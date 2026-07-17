---
description: "Source-dependent artifacts need lineage signals when an upstream change may render those artifacts stale, regardless of where the lineage record is stored"
type: kb/types/note.md
traits: [title-as-claim]
tags: [links]
---

# Source changes should surface downstream review targets, while reverse lineage can remain searchable

Use-shaping produces an artifact for a particular consumer: an instruction guides an agent, a skill body runs a workflow, a checklist enforces a policy, a paper presents an argument. What belongs in the shaped artifact depends on that consumer. When the consumer's task does not include inspecting provenance, source links can dilute focus, so placement policy may keep maintenance lineage out of consumer-visible content. In LLM instructions in particular, pointers the executor must resolve add [indirection cost](./indirection-is-costly-in-llm-instructions.md). Papers, legal analyses, audit records, and evidence-backed recommendations are boundary cases when citations are part of the consumer's warrant: use-shaping then preserves that provenance, while the artifact still needs maintenance lineage.

Whether or not provenance is visible to the consumer, the artifact stays dependent on its sources — whether its content is worked out from them or generalizes beyond them. A maintained source may be edited; an immutable or externally owned source may publish a successor that the workflow detects or adopts. Either event can put downstream artifacts at risk. Without a dependency record, an upstream change names no downstream worklist, making staleness review easier to miss.

The dependency record must therefore exist, but it need not be stored at the source or outside the artifact's hidden metadata. It only needs to stay out of consumer-visible content when the consumer does not need it. This note proposes an interruption-first criterion for workflows that cannot rely on maintainers to run a separate search: the lineage view should surface downstream targets when the workflow recognizes an upstream change. For locally controlled sources, that moment is edit time. For external or versioned sources, it is when a new version is detected or adopted.

The criterion follows from the asymmetry of two lineage queries. The forward query — *what depends on what just changed?* — should reach the maintainer as part of the change workflow because a separate lookup makes downstream review easier to miss. The reverse query — *what informed this artifact?* — is usually a deliberate investigation that can afford a search. A suitable design serves the path that should interrupt and may leave search to the path that can wait.

## Where the record lives is a design choice

Under that criterion:

- **Source-side records**
  - **Benefit:** For locally editable sources, a lineage pointer (`Derived into:` / `Abstracted into:`) is visible in the file the editor already has open, without a separate lookup integration.
  - **Limitation:** Lineage is scattered across sources and provides no global view by itself.
- **A dedicated lineage-link database**
  - **Capability:** The whole graph can serve global queries (all downstream artifacts of a subtree, artifacts with no relevant lineage links, coverage) and scale past what footers can carry.
  - **Requirement:** A change-handling surface must consult it, such as a hook, validator, editor integration, or external-source update workflow. Without that surface, the record does not interrupt the maintainer.
- **Artifact-side records**
  - **Capability:** Source metadata hidden from the consumer serves the reverse query cheaply and can be indexed into a forward view.
  - **Requirement:** Without a forward index and change-handling surface, the metadata does not produce the interruption-first signal.
  - **Cost:** Provenance maintenance remains attached to the artifact, even though the metadata stays outside consumer-visible content.

The designs compose: source-side pointers as the human-visible interrupt, derived into a database for global queries — at which point the database is itself a derived copy that must be [checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

Under the interruption-first model, the consumer-facing artifact carries the content needed for use while a lineage view gives maintainers downstream targets when the workflow recognizes an upstream change. What the subsequent review *is* depends on the lineage regime: a derived artifact (content worked out from the source) is stale until re-derived and compared; an abstracted rule (content exceeding its instances) is re-opened for support rather than invalidated. Where the derivation is mechanical, [the check is free and the regime flips to enforce-or-omit](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

This KB's design choice is source-side records — the `Derived into:` / `Abstracted into:` footer sections with the ripgrep (`rg`) text-search command serving reverse queries — with the two labels' semantics documented in [link-vocabulary.md](../reference/link-vocabulary.md). For this repository, source-side pointers avoid an additional change-time integration. A lineage database becomes worth integrating when global queries or cross-repo lineage justify that surface.

---

Relevant Notes:

- [Skills derive from methodology](./skills-derive-from-methodology-through-distillation.md) — grounds: the source-to-procedure relationship that produces artifacts needing lineage
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: forward lineage pointers provide the dependency edges that use-shaped artifacts deliberately omit
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — grounds: producing an LLM instruction from already-known source material can frontload selection and derivation; tracked lineage preserves the dependency the instruction no longer shows

Derived into:

- [link-vocabulary.md](../reference/link-vocabulary.md) — the lineage-footer convention and its two-regime semantics
