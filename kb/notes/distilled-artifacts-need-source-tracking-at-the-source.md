---
description: "Distillation strips lineage from the artifact by design, so the dependency record must live where change happens — visible to whoever edits a source at the moment of editing, not to whoever executes the artifact"
type: kb/types/note.md
traits: [title-as-claim]
tags: [links]
status: seedling
---

# Distilled artifacts need source tracking at the source

Distillation shapes an artifact for one consumer: an instruction guides an agent, a skill body runs a workflow, a checklist enforces a policy, a paper presents an argument. The shaping strips lineage by design — the consumer needs the artifact's content, not the reasoning that produced it. The executor is only one kind of consumer, but it is the most demanding and the most common: for a reader who must act on the artifact unassisted, inline provenance dilutes focus and adds [indirection cost](./indirection-is-costly-in-llm-instructions.md) — which is why the default for distilled artifacts is no source backlinks at all, not just for instructions. A well-distilled artifact is deliberately silent about where it came from.

But distilled knowledge stays dependent on what it was distilled from. Sources keep evolving — a methodology claim is revised, a design decision reversed — and each source edit silently puts every downstream distillate at risk. Without a dependency record, a source change names nothing: there is no worklist for staleness review, and the drift is discovered only when a stale artifact misleads someone.

The resolution is not to put the lineage back into the artifact but to put it **where change happens**. The staleness signal exists to reach whoever changes a source, at the moment they change it. Lineage recorded inside the artifact is invisible then — nobody re-opens downstream artifacts while editing a source. Lineage recorded at the source is exactly where the editor already is: they see "this has been distilled into X and Y" as they edit, and the review worklist falls out of the edit itself.

The deeper reason is that the two lineage queries have asymmetric requirements. The forward query — *what depends on what I just changed?* — must be zero-hop at edit time, because its job is to **interrupt**: an answer the editor has to go looking for is an answer they will not look for. The reverse query — *what informed this artifact?* — is a deliberate, rare investigation that can afford a search. Store the pointer on the path that must interrupt; let search serve the path that can wait.

## Two audiences, one direction

| | Distilled artifact | Source |
|---|---|---|
| **Reader** | The consumer the artifact was shaped for (most demandingly: an executor) | Maintainer changing the knowledge |
| **Lineage carried** | None — focus is the point | Forward pointers to its distillates |
| **Staleness signal** | None it could act on | Fires at edit time, where change originates |

Staleness detection flows in the direction of change: source changes → the editor sees the downstream targets → reviews them. What that review *is* depends on the derivation: in the general case it is judgment (re-read and re-distill); where the derivation is mechanical, [the check is free and the regime flips to enforce-or-omit](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

The shipped encoding of this rule — the `Distilled into:` footer section and the `rg` reverse query — is documented in [link-vocabulary.md](../reference/link-vocabulary.md).

---

Relevant Notes:

- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — grounds: the distillation relationship that produces artifacts needing source tracking
- [link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: source-side forward pointers provide the dependency edges that distilled artifacts deliberately omit
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — grounds: why the artifact side must stay lineage-free
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — grounds: distillation is a form of frontloading; source-side tracking preserves the dependency structure the frontloaded artifact no longer shows
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: the deterministic special case — when the derivation is mechanical the staleness check is free, and managed review flips to enforce-or-omit
- [link-vocabulary.md](../reference/link-vocabulary.md) — evidence: the shipped `Distilled into:` convention encoding this rule

Distilled into:

- [link-vocabulary.md](../reference/link-vocabulary.md) — the `Distilled into:` footer convention
