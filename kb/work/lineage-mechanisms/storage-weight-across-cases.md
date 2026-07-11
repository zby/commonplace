# Storage weight across derivation cases

The extracted note [`many-to-many-edge-state-is-where-files-yield-to-a-database`](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) should be the basis for this investigation. It gives the clearest storage predicate found so far: plain files yield when **churning state lands on an ownerless many-to-many edge**. "Yield" here means the system needs relational structure keyed by the edge. That can start as a filesystem-backed relation — one edge file per composite key — and become a real database when volume, churn, keyed lookup, and consistency make the hand-built relation too weak. Review lineage is the current witness (see [review-lineage-storage-case.md](../src-architecture-alternatives/review-lineage-storage-case.md)). Relocation is not the reason — we barely use it and could live without it. The reason is high-churn, keyed, mutable current-state with a fast selector over relation edges.

This document asks the next question: which future automatic dependency-maintenance mechanisms will cross the same boundary? It compares review against every other derivation case Commonplace already runs, scores them on the drivers that actually set storage weight, and names the cases to watch as automation grows. The default remains files, but any sufficiently complex automatic dependency maintainer should be checked for churning many-to-many edge state before assuming frontmatter or ordinary links will hold.

## The root driver: churning state on a many-to-many edge

Review forces relational edge-state because its lineage state lives on the **edges of a many-to-many relation**. In the simplified witness, notes × criteria is enough: a note is assayed against many criteria, a criterion applies to many notes, and the acceptance/freshness state belongs to the pair rather than either file. Schema v6 persists this directly as `criterion_path`; verdict gates, conformance dependencies, and report-kind critique all occupy that axis. The current implementation also partitions edge state by model and persists each pair's `result_kind`.

The model dimension is important, but it is not what proves the file/database boundary. It adds a partition to the current review relation. It is not saved in the note or gate files; it is part of review lineage state. That is the right placement for review freshness because a model-conditioned review judgment belongs to the derivation edge. The same principle does not imply "never put model in frontmatter": retained one-shot derivatives may need producer-model metadata directly in their typed frontmatter, while canonical notes revised many times should record model involvement on edit events, not as stable note metadata. See [model-provenance.md](./model-provenance.md).

That is the whole problem. Files are good at **trees** — each fact has one natural owner artifact, and frontmatter points one direction from that owner. A many-to-many **edge has no natural file to live in**:

- put pair state in the note's frontmatter → gate identity is duplicated across every note, and a gate change cannot find its dependents without scanning all notes;
- put it in the gate's frontmatter → the symmetric problem;
- the state genuinely belongs to the relationship, which is exactly what a relational store represents and what a tree of files does not.

Much of what the [storage case](../src-architecture-alternatives/review-lineage-storage-case.md) listed as a separate requirement follows from this structure:

| review requirement | really just… |
|---|---|
| composite key `(note_path, criterion_path)` | the edge identity of a many-to-many relation; the criterion path identifies the assay contract |
| bidirectional staleness (`note-changed` OR `criterion-changed`) | either endpoint invalidates the edge |
| model partitioning | an implementation dimension layered onto the edge |
| all-or-nothing job finalization | one transaction advances a complete requested subset of edges or none |
| swept keyed current-state selector | traversing the relation both ways (gate→notes, note→gates) |

So the keyed selector I flagged earlier is the *symptom*; the *cause* is churning state on a many-to-many edge. Readable prose, run provenance, and append-only events are all satisfiable in files. The hard part is **edge-state with no node-owner, mutated often, queried from both sides**. A directory of edge files can represent that relation, but it is already a filesystem-backed relational store; the real question is when that handmade store loses to SQLite.

**One refinement.** Many-to-many *topology* alone does not force a store. `compares-with` among sources is also a many-to-many relation, but its edge state is **static** — authored once, essentially one bit — so a link handles it fine. What tips review over is that its edges carry **mutable, churning state** (SHAs, decisions, acceptances, refreshes). The predicate is therefore:

> **Static edges → links. Dynamic, churning edge-state with no natural node-owner → relational structure; real DB when the filesystem version stops carrying the operational load.**

Trees and stars (one input artifact, or many inputs converging on one owned event) stay in files. Only a churning many-to-many mesh escalates. The practical lesson for future automation is strong but not absolute: once dependency maintenance becomes automatic enough that it sweeps freshness, acceptance, or update state over a mesh of artifacts, it should first be modeled as edge-state; then we decide whether edge files, generated indexes, or a real database are the right weight.

## Scoring every case

Each case scored on the two things that matter: the **lineage structure** (tree / star / many-to-many mesh) and whether the **edge state churns**. "Weight" is the lightest storage that preserves the case's lineage needs.

| case | lineage structure | edge state | where content lives | required weight |
|---|---|---|---|---|
| **Review assays, including critique** | many-to-many mesh `note × criterion`, partitioned by model | **churning** | markdown verdict/report files | **operational DB today** |
| Source snapshot | leaf (no derivation yet) | — | the file (immutable) | frontmatter / none |
| Ingest report | tree (one snapshot → one ingest) | static | the `.ingest.md` file | frontmatter pointer |
| Agent-memory-system review | tree (one repo → one review) | static, on-demand check | the review note | frontmatter + on-demand check |
| Connect report | tree (one artifact → one report) | disposable | gitignored candidate | none (disposable) |
| Friction / connect report | tree (one note → one report) | disposable | gitignored candidate | none (disposable) |
| Full-pass report packet | star (one pass → initial and closing reports) | retained while actionable, then disposable | gitignored pass directory | artifact-local / disposable |
| Generated index | tree (frontmatter → listing) | recomputable | build output / curated head | validator-checked, no state |
| Ad-hoc distillation | star (many inputs → one packet) | static | workshop / prompt file | frontmatter on promotion |
| Merge-back event | star (many inputs → one owned event) | append-once | commit + canonical artifact | commit history now; shared ledger only if queried |
| `compares-with` among sources | many-to-many mesh | **static** | authored links | links (no store) |

The shape is stark. **Review is still the only current row in the operational-DB tier**, even after critique joined it, because critique reused the existing note/criterion mesh rather than creating a second one. The closure calibration briefly tested a hand-written shared-event surface, then retired it because no real carry or continuing consumer justified retention. The same table should guide further investigations; it is not evidence that review will remain unique. Three patterns cover the present non-review cases:

- **Trees and stars stay in files.** Ingests, source reviews, connect/friction reports, ad-hoc distillations, full-pass packets, and merge-back all have a natural owner artifact for each fact — the derived file, pass, or event target. Frontmatter pointers and intentional commits express them directly at current volume. No edge is orphaned.
- **Churn without a mesh → regenerate, don't store.** Connect reports and generated indexes change constantly, but each is a tree rebuilt from current inputs; nothing queries per-edge state. Generated indexes get a deterministic validator instead ([`a-derived-copy-of-recomputable-truth-must-be-checked-or-absent`](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)).
- **Mesh without churn → links.** `compares-with` is genuinely many-to-many, but its edge state is static, so authored links carry it. It never needs a store.

The one cross-cutting case is **merge-back**: when an automatic report drives an edit to a canonical artifact, the update event may need to be auditable across artifact classes ([automatic-derivation-rules.md](./automatic-derivation-rules.md) §Merge-Back). It has no keyed selector and low churn, so it does not want a database. At current volume, an intentional commit is the durable event surface. A shared ledger is earned only when agents need to query merge-back history independently of Git and the artifact.

## The layered mechanism: one vocabulary, three weights

The universal part is **not** a universal store. It is a single lineage-event vocabulary that can be *materialized at three weights*, with an escalation rule that keeps the default cheap. Every case uses the same fields; cases differ only in where those fields are written.

**Shared event vocabulary** (the universal core — same for every case):

- artifact path + version/hash;
- role (source, derived view, generated index, canonical, archival — from [`axes-of-artifact-analysis`](../../notes/axes-of-artifact-analysis.md));
- source dependencies + their versions/revisions;
- producer metadata when a model/tool generated the derivation (model partition, runner, prompt/generator version as needed);
- derivation event kind (capture, distill, generate, merge-back, ack, retire);
- freshness rule (what source change invalidates this, and whether refresh is regenerate, re-distill, or review).

**Three storage weights:**

| weight | carrier | when | cases |
|---|---|---|---|
| **1. In-artifact** (default) | frontmatter pointers + prose | lineage is low-churn and read on demand | snapshots, ingests, source reviews, ad-hoc distillations, promoted notes |
| **2. Shared event surface** | structured commit convention first; append-only `JSONL`/ledger only when queried | events must be auditable across classes independently of the artifact file | future high-volume merge-back / promotion / retirement events |
| **3. Operational store** | edge-file directory, SQLite, or generated index over a ledger | a keyed selector runs repeatedly over high-churn mutable current-state on many-to-many edges | review now; future swept cue/source, compiled-view/source, or dependency-maintenance meshes |

**Escalation rule:** start at weight 1. Add weight 2 only for events that must survive and be audited independently of the artifact's own file and ordinary commit history. Escalate to weight 3 when an artifact class develops **churning state on a many-to-many edge** — when lineage state stops having a natural owner file and starts living on the relationship, mutating often, queried from both sides (the [ADR 010](../../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) transition). Weight 3 can begin as edge files or a generated index; a real DB wins when transactionality, lookup, and churn make the filesystem version awkward. Tree/star structures and static meshes do not earn a store by structure alone; complex automatic dependency maintenance often will, because its job is usually to maintain fresh edge state across a mesh.

The first class to watch is **compiled views / cues**. A cue compiled from many notes, where each note feeds many cues, is a many-to-many mesh — and if cue freshness becomes automatic and swept (per `(cue, source-note)` edge), its edge state would start churning. That is the next case that could earn weight 3. Until cue generation is automatic and swept, its lineage is still a star (one compiled view, recorded source hashes) and stays at weight 1.

Other likely investigations:

- **source-to-derived refresh queues** once one source can invalidate many derived notes and each derived note depends on many sources;
- **merge-back acceptance state** if report-driven edits become swept per `(artifact, producer)` or `(artifact, source)` pair rather than rare commit events;
- **agent-memory-system review freshness** if many external repositories feed many comparison artifacts and upstream revisions are checked automatically;
- **cue activation / retirement** if triggers, sources, targets, and observed outcomes form a changing mesh.
- **authored link maintenance** because every link is a latent dependency edge; rank link and edge types by disruption probability, then decide which are checked on demand and which deserve automatic stale-edge maintenance.

This is the "not too heavy" answer concretely: **we do not build an artifact-lineage database before a second mesh earns it, but we should expect complex automatic dependency maintenance to need relational structure.** We define the vocabulary once, let frontmatter and ordinary commits carry it by default, add a shared event ledger only after a real cross-class query appears, and leave review's SQLite as the current specialization that earned the real-DB version of the edge-state store. The same vocabulary flows through all three weights, so a class that later grows a selector can be promoted from artifact/commit → ledger → edge store without redefining what a lineage event *is*.

## Why this beats both extremes

- **Beats "DB for everything"**: only one case has the churn×selector profile that pays for an index. Putting ingests or source reviews in a database adds a store, a schema, and a sync obligation to lineage that a frontmatter pointer already serves — pure overhead.
- **Beats "files for everything"**: the [storage case](../src-architecture-alternatives/review-lineage-storage-case.md) showed the all-files port of review just rebuilds a database with weaker consistency. The layered model concedes that one tier honestly instead of pretending files cover it, while still keeping every *other* case in files.
- **Keeps the universal property that matters**: the thing that generalizes is the *event vocabulary and the escalation rule*, not the storage engine. That is what lets automatic derivation expand across classes without each class inventing its own lineage shape.

## Open questions for closure

- **Does the shared ledger (weight 2) get built now, or stay deferred?** Merge-back is the only thing that wants it, and merge-back volume is still low. It may be enough to record merge-back in commit messages until volume forces a ledger — i.e. weight 2 might start as a git-log convention and only become a file when queried.
- **Should the weight-3 store, when a *second* class needs it, be edge files, a generated index, a generic artifact-lineage DB, or a second purpose-built DB?** The extracted theory note says the structure is relational; it does not decide which implementation weight or whether one shared schema should serve all automatic dependency meshes.
- **Where does the agent-memory-system-review "stale vs upstream HEAD" check (◐) sit** — frontmatter pin + on-demand `ls-remote`, or does a handful of external repos justify a tiny refresh ledger? Likely on-demand until the count grows.
- **How should this workshop use the extracted theory note now that it exists?** Treat it as the basis for the next investigation pass: enumerate future automatic dependency-maintenance mechanisms, map their relation shape, rank edge churn/disruption probability, and decide which ones are ordinary files, edge-file relations, generated indexes, or real databases.
