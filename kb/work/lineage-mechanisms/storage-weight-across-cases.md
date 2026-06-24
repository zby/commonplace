# Storage weight across derivation cases

The extracted note [`many-to-many-edge-state-is-where-files-yield-to-a-database`](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) should be the basis for this investigation. It gives the storage predicate: files yield when **churning state lands on an ownerless many-to-many edge**. Review lineage is the current witness (see [review-lineage-storage-case.md](./review-lineage-storage-case.md)). Relocation is not the reason — we barely use it and could live without it. The reason is high-churn, keyed, mutable current-state with a fast selector over relation edges.

This document asks the next question: which future automatic dependency-maintenance mechanisms will cross the same boundary? It compares review against every other derivation case Commonplace already runs, scores them on the drivers that actually set storage weight, and names the cases to watch as automation grows. The default remains files, but any sufficiently complex automatic dependency maintainer should be assumed suspect until its relation shape is checked for churning many-to-many edge state.

## The root driver: churning state on a many-to-many edge

Review forces a database because its lineage state lives on the **edges of a many-to-many relation**: notes × gates × models. A note is reviewed against many gates; a gate applies to many notes; each model partitions the result. The acceptance/freshness state belongs to the *pair*, and a pair belongs to neither file.

That is the whole problem. Files are good at **trees** — each fact has one natural owner artifact, and frontmatter points one direction from that owner. A many-to-many **edge has no natural file to live in**:

- put pair state in the note's frontmatter → gate identity is duplicated across every note, and a gate change cannot find its dependents without scanning all notes;
- put it in the gate's frontmatter → the symmetric problem;
- the state genuinely belongs to the relationship, which is exactly what a relational store represents and what a tree of files does not.

Everything the [storage case](./review-lineage-storage-case.md) listed as a separate requirement falls out of this one structure:

| review requirement | really just… |
|---|---|
| composite key `(note, gate, model)` | the edge identity of a 3-way relation |
| bidirectional staleness (`note-changed` OR `gate-changed`) | either endpoint invalidates the edge |
| model partitioning | the third dimension of the relation |
| partial run success | one run touches a subset of edges |
| swept keyed current-state selector | traversing the relation both ways (gate→notes, note→gates) |

So the keyed selector I flagged earlier is the *symptom*; the *cause* is churning state on a many-to-many edge. Readable prose, run provenance, and append-only events are all satisfiable in files — what is not is **edge-state with no node-owner, mutated often, queried from both sides.**

**One refinement.** Many-to-many *topology* alone does not force a store. `compares-with` among sources is also a many-to-many relation, but its edge state is **static** — authored once, essentially one bit — so a link handles it fine. What tips review over is that its edges carry **mutable, churning state** (SHAs, decisions, acceptances, refreshes). The predicate is therefore:

> **Static edges → links. Dynamic, churning edge-state with no natural node-owner → relational store.**

Trees and stars (one input artifact, or many inputs converging on one owned event) stay in files. Only a churning many-to-many mesh escalates. The practical lesson for future automation is strong: once dependency maintenance becomes automatic enough that it sweeps freshness, acceptance, or update state over a mesh of artifacts, it will probably need a database or a database-equivalent generated index.

## Scoring every case

Each case scored on the two things that matter: the **lineage structure** (tree / star / many-to-many mesh) and whether the **edge state churns**. "Weight" is the lightest storage that preserves the case's lineage needs.

| case | lineage structure | edge state | where content lives | required weight |
|---|---|---|---|---|
| **Review** | many-to-many mesh `note × gate × model` | **churning** | markdown report files | **operational DB** |
| Source snapshot | leaf (no derivation yet) | — | the file (immutable) | frontmatter / none |
| Ingest report | tree (one snapshot → one ingest) | static | the `.ingest.md` file | frontmatter pointer |
| Agent-memory-system review | tree (one repo → one review) | static, on-demand check | the review note | frontmatter + on-demand check |
| Connect report | tree (one artifact → one report) | disposable | gitignored candidate | none (disposable) |
| Critique / friction report | tree (one note → one report) | disposable | gitignored candidate | none (disposable) |
| Generated index | tree (frontmatter → listing) | recomputable | build output / curated head | validator-checked, no state |
| Ad-hoc distillation | star (many inputs → one packet) | static | workshop / prompt file | frontmatter on promotion |
| Merge-back event | star (many inputs → one owned event) | append-once | the canonical artifact | shared append-only ledger |
| `compares-with` among sources | many-to-many mesh | **static** | authored links | links (no store) |

The shape is stark. **Review is the only current row in the database tier**, and the table shows exactly why: it is the only current case that is *both* a many-to-many mesh *and* has churning edge state. The same table should guide further investigations; it is not evidence that review will remain unique. Three patterns cover the present non-review cases:

- **Trees and stars stay in files.** Ingests, source reviews, connect/critique reports, ad-hoc distillations, and merge-back all have a natural owner artifact for each fact — the derived file, or the event's target. Frontmatter pointers (or one shared ledger for the owned merge-back event) express them directly. No edge is orphaned.
- **Churn without a mesh → regenerate, don't store.** Connect reports and generated indexes change constantly, but each is a tree rebuilt from current inputs; nothing queries per-edge state. Generated indexes get a deterministic validator instead ([`a-derived-copy-of-recomputable-truth-must-be-checked-or-absent`](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)).
- **Mesh without churn → links.** `compares-with` is genuinely many-to-many, but its edge state is static, so authored links carry it. It never needs a store.

The one cross-cutting case is **merge-back**: when an automatic report drives an edit to a canonical artifact, the update event needs to be auditable across *all* artifact classes ([automatic-derivation-rules.md](./automatic-derivation-rules.md) §Merge-Back). It has no keyed selector and low churn, so it does not want a database — but it does want one durable, append-only, queryable-enough surface shared by every class. That is the heaviest thing the non-review world needs, and it is much lighter than SQLite.

## The layered mechanism: one vocabulary, three weights

The universal part is **not** a universal store. It is a single lineage-event vocabulary that can be *materialized at three weights*, with an escalation rule that keeps the default cheap. Every case uses the same fields; cases differ only in where those fields are written.

**Shared event vocabulary** (the universal core — same for every case):

- artifact path + version/hash;
- role (source, derived view, generated index, canonical, archival — from [`axes-of-artifact-analysis`](../../notes/axes-of-artifact-analysis.md));
- source dependencies + their versions/revisions;
- derivation event kind (capture, distill, generate, merge-back, ack, retire);
- freshness rule (what source change invalidates this, and whether refresh is regenerate, re-distill, or review).

**Three storage weights:**

| weight | carrier | when | cases |
|---|---|---|---|
| **1. In-artifact** (default) | frontmatter pointers + prose | lineage is low-churn and read on demand | snapshots, ingests, source reviews, ad-hoc distillations, promoted notes |
| **2. Shared ledger** | one git-tracked append-only `JSONL`/event file | events must be auditable across classes but have no keyed selector | merge-back / promotion / retirement events |
| **3. Operational store** | SQLite (or a generated index over a ledger) | a keyed selector runs repeatedly over high-churn mutable current-state on many-to-many edges | review now; future swept cue/source, compiled-view/source, or dependency-maintenance meshes |

**Escalation rule:** start at weight 1. Add weight 2 only for events that must survive and be audited independently of the artifact's own file. Escalate to weight 3 when an artifact class develops **churning state on a many-to-many edge** — when lineage state stops having a natural owner file and starts living on the relationship, mutating often, queried from both sides (the [ADR 010](../../reference/adr/) transition). Tree/star structures and static meshes do not earn a store by structure alone; complex automatic dependency maintenance often will, because its job is usually to maintain fresh edge state across a mesh.

The first class to watch is **compiled views / cues**. A cue compiled from many notes, where each note feeds many cues, is a many-to-many mesh — and if cue freshness becomes automatic and swept (per `(cue, source-note)` edge), its edge state would start churning. That is the next case that could earn weight 3. Until cue generation is automatic and swept, its lineage is still a star (one compiled view, recorded source hashes) and stays at weight 1.

Other likely investigations:

- **source-to-derived refresh queues** once one source can invalidate many derived notes and each derived note depends on many sources;
- **merge-back acceptance state** if report-driven edits become swept per `(artifact, producer)` or `(artifact, source)` pair rather than rare commit events;
- **agent-memory-system review freshness** if many external repositories feed many comparison artifacts and upstream revisions are checked automatically;
- **cue activation / retirement** if triggers, sources, targets, and observed outcomes form a changing mesh.

This is the "not too heavy" answer concretely: **we do not build an artifact-lineage database before a second mesh earns it, but we should expect complex automatic dependency maintenance to earn one.** We define the event vocabulary once, let frontmatter carry it by default, add at most one shared append-only ledger for merge-back audit, and leave review's SQLite as the current specialization that earned escalation. The same vocabulary flows through all three weights, so a class that later grows a selector can be promoted from frontmatter → ledger → store without redefining what a lineage event *is*.

## Why this beats both extremes

- **Beats "DB for everything"**: only one case has the churn×selector profile that pays for an index. Putting ingests or source reviews in a database adds a store, a schema, and a sync obligation to lineage that a frontmatter pointer already serves — pure overhead.
- **Beats "files for everything"**: the [storage case](./review-lineage-storage-case.md) showed the all-files port of review just rebuilds a database with weaker consistency. The layered model concedes that one tier honestly instead of pretending files cover it, while still keeping every *other* case in files.
- **Keeps the universal property that matters**: the thing that generalizes is the *event vocabulary and the escalation rule*, not the storage engine. That is what lets automatic derivation expand across classes without each class inventing its own lineage shape.

## Open questions for closure

- **Does the shared ledger (weight 2) get built now, or stay deferred?** Merge-back is the only thing that wants it, and merge-back volume is still low. It may be enough to record merge-back in commit messages until volume forces a ledger — i.e. weight 2 might start as a git-log convention and only become a file when queried.
- **Should the weight-3 store, when a *second* class needs it, be a generic artifact-lineage DB or a second purpose-built store?** The extracted theory note says the substrate will likely be relational; it does not decide whether one shared schema should serve all automatic dependency meshes.
- **Where does the agent-memory-system-review "stale vs upstream HEAD" check (◐) sit** — frontmatter pin + on-demand `ls-remote`, or does a handful of external repos justify a tiny refresh ledger? Likely on-demand until the count grows.
- **How should this workshop use the extracted theory note now that it exists?** Treat it as the basis for the next investigation pass: enumerate future automatic dependency-maintenance mechanisms, map their relation shape, and decide which ones are just files/ledgers and which ones practically require a DB.
