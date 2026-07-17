---
description: "Use-shaping strips lineage from the artifact by design, so the dependency record must live somewhere else — and reach whoever edits a source at the moment of editing; where it lives (source footers, a link database) is a design choice judged against that requirement"
type: kb/types/note.md
traits: [title-as-claim]
tags: [links]
---

# Artifacts produced from sources need lineage recorded at the source

Use-shaping produces an artifact for one consumer: an instruction guides an agent, a skill body runs a workflow, a checklist enforces a policy, a paper presents an argument. The shaping strips lineage by design — the consumer needs the artifact's content, not the reasoning that produced it. The executor is only one kind of consumer, but it is the most demanding and the most common: for a reader who must act on the artifact unassisted, inline provenance dilutes focus and adds [indirection cost](./indirection-is-costly-in-llm-instructions.md) — which is why the default for use-shaped artifacts is no source backlinks at all, not just for instructions. A well-shaped artifact is deliberately silent about where it came from.

But the artifact stays dependent on its sources — whether its content is worked out from them or generalizes beyond them. Sources keep evolving — a methodology claim is revised, a design decision reversed — and each source edit silently puts every downstream artifact at risk. Without a dependency record, a source change names nothing: there is no worklist for staleness review, and the drift is discovered only when a stale artifact misleads someone.

So the dependency record must exist — somewhere other than the artifact, whose focus is the point. The requirement any tracking design must satisfy comes from the asymmetry of the two lineage queries. The forward query — *what depends on what I just changed?* — must reach the editor **at edit time**, because its job is to interrupt: an answer the editor has to go looking for is an answer they will not look for. The reverse query — *what informed this artifact?* — is a deliberate, rare investigation that can afford a search. Whatever the design, the stored record must serve the path that has to interrupt; search can serve the path that can wait.

## Where the record lives is a design choice

Judged against that requirement:

- **Source-side records** — a lineage pointer (`Derived into:` / `Abstracted into:`) in each source — satisfy the interrupt requirement with zero machinery: the pointer is in the file the editor already has open. The cost is lineage scattered across sources, with no global view.
- **A dedicated lineage-link database** holds the whole graph in one place, serving global queries (all downstream artifacts of a subtree, orphans, coverage) and scaling past what footers can carry — but it satisfies the interrupt requirement only if some edit-time surface consults it: a hook, a validator, an editor integration. A record without that surface is lineage nobody sees at the moment that matters.
- **Artifact-side records** — the artifact listing its sources in metadata hidden from its consumer — serve the reverse query cheaply and can be indexed into a forward view, but unindexed they fail the interrupt requirement outright, and they put provenance maintenance back on the artifact the shaping was keeping clean.

The designs compose: source-side pointers as the human-visible interrupt, derived into a database for global queries — at which point the database is itself a derived copy that must be [checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

## Two audiences, one direction of flow

| | Use-shaped artifact | Lineage record |
|---|---|---|
| **Reader** | The consumer the artifact was shaped for (most demandingly: an executor) | Maintainer changing the knowledge |
| **Carries** | Content only — focus is the point | Forward pointers from each source to its downstream artifacts |
| **Staleness signal** | None it could act on | Fires at edit time, where change originates |

Staleness detection flows in the direction of change: source changes → the editor sees the downstream targets → reviews them. What that review *is* depends on the lineage regime: a derived artifact (content worked out from the source) is stale until re-derived and compared; an abstracted rule (content exceeding its instances) is re-opened for support rather than invalidated. Where the derivation is mechanical, [the check is free and the regime flips to enforce-or-omit](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

This KB's design choice is source-side records — the `Derived into:` / `Abstracted into:` footer sections with `rg` as the reverse query — with the two labels' semantics documented in [link-vocabulary.md](../reference/link-vocabulary.md). At repo scale the zero-machinery option wins; a link database becomes worth its surface when global queries or cross-repo lineage appear.

---

Relevant Notes:

- [skills derive from methodology](./skills-derive-from-methodology-through-distillation.md) — grounds: the source-to-procedure relationship that produces artifacts needing lineage
- [link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: forward lineage pointers provide the dependency edges that use-shaped artifacts deliberately omit
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — grounds: why the artifact side must stay lineage-free
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — grounds: use-shaping is a form of frontloading; tracked lineage preserves the dependency structure the frontloaded artifact no longer shows
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: the deterministic special case — when the derivation is mechanical the staleness check is free, and managed review flips to enforce-or-omit
- [link-vocabulary.md](../reference/link-vocabulary.md) — evidence: the shipped source-side lineage-footer convention, this KB's design choice within the space

Derived into:

- [link-vocabulary.md](../reference/link-vocabulary.md) — the lineage-footer convention and its two-regime semantics
