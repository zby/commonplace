---
description: Escalate from files to a relational store only when churning state lands on an ownerless many-to-many edge; high churn alone, or a static many-to-many relation alone, stays in files
type: kb/types/note.md
traits: [title-as-claim]
tags: [architecture]
status: current
---

# Churning state on a many-to-many edge is where files yield to a database

[Files beat a database](./files-not-database.md) for authored, agent-navigated knowledge, but that argument has a boundary, and the boundary has a precise structural shape. A files-first system should escalate a subsystem to a relational store when, and only when, **mutable state that churns lives on the edge of a many-to-many relation**. That single condition predicts the exception; high churn alone does not, and a many-to-many relation alone does not.

## Why an ownerless edge is the thing files cannot hold

Files are good at **trees**. Every fact has one natural owner artifact, and frontmatter points one direction outward from that owner. A tree of files can express a one-to-many fan (one source, many derivations) and a **star** (many inputs converging on one owned event) without strain, because in both shapes each fact still has a home file.

A **many-to-many edge has no home file**. When entities on both sides are many — a note reviewed against many gates, a gate applied to many notes — the state that belongs to the *pair* belongs to neither file:

- store it in the left node's frontmatter, and the right node's identity is duplicated across every left node, and a change on the right cannot find its dependents without scanning every left file;
- store it in the right node's frontmatter, and the symmetric failure appears;
- the state genuinely belongs to the relationship, which is exactly what a relational store represents and a tree of files does not.

The only file-based escape is to denormalize — copy the edge state into one side and accept the duplication and the sync obligation — or to rebuild a relational index over the files, which is a database with weaker consistency. Either way the structure, not the volume, is what defeats files.

## Both qualifiers carry weight

The claim is a conjunction of two non-trivial conditions. Dropping either one collapses it back into files — and dropping both is just the ordinary files-first baseline, where every fact has an owner and nothing churns on an edge.

- **Churn without a many-to-many edge → regenerate, don't store.** A connect report or a generated index churns constantly, but each is a *tree* rebuilt from current inputs; nothing queries per-edge state, so you regenerate or [validate against the source](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) rather than maintain a store. Churn is a red herring on its own.
- **A many-to-many edge without churn → links.** A `compares-with` relation among sources is genuinely many-to-many, but its edge state is *static* — authored once, essentially one bit — so an authored link carries it. A link is written-once and read by traversal; that is all a static edge needs. Topology alone is a red herring too.

What forces the store is the *combination*: edges with no owner file **and** state on those edges that mutates often enough that authored links cannot keep up and a selector — the component that scans for stale pairs — must check freshness from both endpoints. That is the regime where a written-once link fails and a tree-of-files duplicates without bound.

## The witness, and the next candidate

Commonplace has exactly one subsystem in this regime: the review store. Its relation is `note × gate × model`, and the edge is the `(note, gate)` review pair. The edge state — reviewed SHAs, decision, acceptance, freshness — churns on every sweep (each pass that re-reviews affected pairs). Staleness is then checked from both endpoints: a gate change invalidates its note-dependents, a note change its gate-dependents. Most of the properties that looked like independent reasons for the database follow from this one structure — the composite key is just the edge's identity, and bidirectional staleness is the two-endpoint dependency. (Two others, model partition and partial-run success, are genuinely independent — a third relation dimension and a batch-execution detail — but neither is what forced the store.) This is the scoped exception [the files-first argument already anticipated](./files-not-database.md) but did not name structurally.

The predicate also says where the *next* database would be earned, from structure alone rather than from a vague sense of scale. Compiled views and cues are the candidate: a cue built from many notes where each note feeds many cues is a many-to-many mesh, and if cue freshness becomes automatic and swept per `(cue, source-note)` edge, that edge state starts churning and crosses the boundary. Until generation is automatic and swept, a cue is still a star — one compiled view recording its source hashes — and stays in files. The test is the same in both directions, and it has two parts of equal weight: the relation's shape, and whether its edge state churns — never how much data there is.

## Scope

This is a claim about the **storage substrate** for a subsystem's lineage and operational state, one [axis of artifact analysis](./axes-of-artifact-analysis.md) — not about where readable content lives. Review *prose* stays in git-backed markdown even though review *edge-state* moves to SQLite; the content's home and the edge-state's home are decided separately. The claim assumes a files-first default whose costs (versioning, browsing, zero infrastructure) are worth keeping; it identifies the minimal structural condition that overrides that default for one subsystem without overturning it for the system.

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — extends: names the structural boundary that note's "a subsystem can outgrow files" exception leaves implicit
- [axes of artifact analysis](./axes-of-artifact-analysis.md) — see-also: this is a claim on the storage-substrate axis, decided independently of representational form
- [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — see-also: the disposition for the churn-without-mesh case (regenerate or validate, never store)
- [review system architecture](../reference/review-architecture.md) — evidence: the sole current witness — `note × gate × model` edge state in SQLite while review prose stays in files
