---
description: The clearest structural trigger for a files-first KB to adopt a relational store — churning state on an ownerless many-to-many edge; high churn alone, or static topology alone, stays in files
type: kb/types/note.md
traits: [title-as-claim]
tags: [architecture]
status: current
---

# Churning state on a many-to-many edge is where files yield to a database

[Files beat a database](./files-not-database.md) for authored, agent-navigated knowledge, but that argument has a boundary, and the clearest form of that boundary has a precise structural shape. The general trigger found so far: a files-first system is pushed toward a relational store when **mutable state that churns lives on the edge of a many-to-many relation**. This is the clearest structural condition the work has surfaced, not a proof that no other trigger exists. Where it holds, files lose; high churn alone does not force the move, and a many-to-many relation alone does not either.

## Why a churning ownerless edge outgrows a tree of files

Files and directories are good at **trees**. Every fact has one natural owner — a file, or a directory standing for an entity — and its metadata points one direction outward from that owner. A tree expresses a one-to-many fan (one source, many derivations) and a **star** (many inputs converging on one owned event) without strain, because each fact still has a home.

A **many-to-many edge has no home.** When both sides are many — items on the left each related to many on the right, and vice versa — the state that belongs to the *pair* belongs to neither side:

- store it with the left item, and the right item's identity is duplicated across every left item, and a change on the right cannot find its dependents without scanning every left file;
- store it with the right item, and the symmetric failure appears;
- the state genuinely belongs to the relationship, which is what a relational store represents and a plain tree of files does not.

There is a file-based escape, and it is worth naming because it is often the right call: give the relation its own directory and write one file per edge, keyed by the composite identity. But notice what that is — a relational store, hand-built on the filesystem. It keeps version history and needs no new infrastructure, and it holds up to some level of volume and churn. The claim here is not that files *cannot* represent the relation; it is that representing it forces relational structure — an index keyed by the edge — and past some level of complexity a real database carries that structure better, with the transactional consistency and fast keyed lookup a directory-of-files only weakly reconstructs. Either way, the structure, not the volume, is what pushes you off a plain tree.

## Both qualifiers carry weight

The claim is a conjunction of two non-trivial conditions. Dropping either one collapses it back into files — and dropping both is just the ordinary files-first baseline, where every fact has an owner and nothing churns on an edge.

- **Churn without a many-to-many edge → regenerate, don't store.** A connect report or a generated index changes constantly, but each is a *tree* rebuilt from current inputs; nothing queries per-edge state. So high churn by itself is no reason to reach for a store — you re-derive the artifact from its inputs instead of indexing it, and where the derivation is deterministic you [validate against the source](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rather than persist it.
- **A many-to-many edge without churn → links.** A `compares-with` relation among sources is genuinely many-to-many, yet in practice its edge state is *static* — authored once, essentially one bit — so an authored link carries it. That stillness is a fact about how the relation is used, not an intrinsic property: a system that continuously re-scored those edges would put churn on them and face the same pressure. A static edge needs only a written-once link read by traversal; topology with no churn does not force a store.

What forces the store is the *combination*: edges with no owner file **and** state on those edges that mutates often enough that authored links cannot keep up and something must repeatedly recheck which edges have gone stale. That is the regime where a written-once link fails and a tree-of-files duplicates without bound.

## A witness

Commonplace's review system is a simplified example of the regime. Take it in two dimensions: reviews relate notes and quality gates, where each note is reviewed against many gates and each gate applies to many notes — a many-to-many relation whose edge is the `(note, gate)` pair. The state on that edge — which version was reviewed, the verdict, whether it is still fresh — churns as notes and gates change, and the system must repeatedly recheck staleness from both endpoints: a gate change invalidates its note-dependents, a note change its gate-dependents. The review *prose* stays in markdown files, but that churning edge-state moved into a small relational store, because no single note file or gate file owns the pair. This is the scoped exception [the files-first argument already anticipated](./files-not-database.md) but did not name structurally.

(The real review system carries a further dimension and operational detail that this note deliberately sets aside; the two-dimensional version is enough to show the structure.)

## The boundary opens a larger question

The same predicate hints at where a store might next be earned — compiled views or cues, say, if their freshness ever becomes automatically maintained over a many-to-many mesh of sources. But that points at something larger and unsettled. *Every* authored link is a latent dependency edge: it can go stale when either endpoint changes, and a sufficiently automatic KB would want to know which links to recheck and when. The predicate here only resolves the extreme case — edges whose state churns continuously, enough to need an index. Ranking link and edge types by how likely an endpoint change is to disrupt them, and deciding which deserve automatic maintenance rather than on-demand rechecking, is the larger analysis this boundary opens.

## Scope

This is a claim on the **storage-substrate** [axis of artifact analysis](./axes-of-artifact-analysis.md): which substrate a given *kind* of state should live on. "Where it lives" is exactly that question — in a files-first KB the content lives in flat files, with version control as a layer over that substrate. The point is that one system can place different classes of state on different substrates: readable content stays in flat files even when a churning slice of operational state moves to a relational store. The note assumes a files-first default whose benefits (versioning, browsing, zero infrastructure) are worth keeping, and identifies the structural condition under which one subsystem's edge-state outgrows that default without overturning it for the system.

## Open Questions

- Is churning ownerless many-to-many edge state the *only* structural trigger for a relational store, or just the clearest one found so far?
- Every authored link is a latent dependency edge that can go stale when its source or target changes. Which link and edge types carry the highest disruption probability, and which warrant automatic maintenance rather than on-demand rechecking?
- At what level of volume and churn does a filesystem-backed relational store (a directory of edge-files keyed by composite id) stop being the practical choice, and a real database win?

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — extends: names the structural boundary that note's "a subsystem can outgrow files" exception leaves implicit
- [axes of artifact analysis](./axes-of-artifact-analysis.md) — see-also: this is a claim on the storage-substrate axis, decided independently of representational form
- [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — see-also: the disposition for the churn-without-mesh case (regenerate or validate, never store)
- [review system architecture](../reference/review-architecture.md) — evidence: the witness — a `(note, gate)` review relation whose churning edge-state lives in a relational store while review prose stays in files
