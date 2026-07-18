# A generalized schema over artifact / version / head / edge

Second pass. [freshness-schema-as-starting-skeleton.md](./freshness-schema-as-starting-skeleton.md) found that Gaps 1 (content versioning), 3 (links as edges), and 7 (proposal-selection) are the same pattern — versioned content, a current pointer, accepted-input edges — applied past review pairs. This file drafts one schema on that pattern and tries to fit every artifact class from the gap survey through it, to see where it actually breaks rather than assert that it doesn't.

DDL below borrows the house style from [artifact-freshness-and-referential-checks/database-design.md](../artifact-freshness-and-referential-checks/database-design.md) (`CHECK` constraints, canonical JSON keys, explicit delete behavior) because that file is the closest real precedent, not because this schema is implementation-grade. It isn't — this is a design sketch for a hypothetical system, not a plan gated for a real M1.

## The core triple

```sql
CREATE TABLE artifacts (
    artifact_id INTEGER PRIMARY KEY,
    artifact_kind TEXT NOT NULL CHECK (length(artifact_kind) > 0),
    -- 'content' | 'type' | 'collection' | 'workshop-item' | ...  (open, not enumerated here)
    created_at TEXT NOT NULL
);

CREATE TABLE content_versions (
    version_id INTEGER PRIMARY KEY,
    artifact_id INTEGER NOT NULL REFERENCES artifacts(artifact_id),
    parent_version_id INTEGER REFERENCES content_versions(version_id),
    path TEXT NOT NULL CHECK (length(path) > 0),
    content_text TEXT NOT NULL,
    content_sha256 TEXT NOT NULL CHECK (length(content_sha256) = 64),
    state TEXT NOT NULL CHECK (state IN ('candidate', 'accepted', 'superseded', 'rejected')),
    authored_by TEXT NOT NULL,   -- agent/model id or human identity, uninterpreted
    authored_at TEXT NOT NULL
);

CREATE TABLE artifact_heads (
    artifact_id INTEGER PRIMARY KEY REFERENCES artifacts(artifact_id),
    current_version_id INTEGER NOT NULL REFERENCES content_versions(version_id),
    revision INTEGER NOT NULL CHECK (revision >= 1),
    updated_at TEXT NOT NULL
);
```

`artifacts` is the stable identity — answers "review-lineage-storage-case.md's open question directly: path is an attribute of a version, not the key. `content_versions` is append-only and gets a row on *every* edit, closing Gap 1's write-time-versioning hole: `artifact_snapshots` in the shipped store only gets a row when something accepts an input, which is a cache of *some* versions, not history of all of them. `parent_version_id` gives a DAG for branching (Gap 1's "worth being honest this is git's commit graph, minus git" — it is, deliberately, because nothing here removes that cost, only relocates it). `artifact_heads` is `freshness_baselines` generalized past review-pairs: one current pointer per identity, monotonic revision for optimistic concurrency, exactly the shape that already shipped.

`state` on `content_versions` is where Gap 7's candidate/evaluation/retention triad lands: a `candidate` row is a proposed version nobody promoted; promotion is `artifact_heads.current_version_id` moving to point at it and the row flipping to `accepted`; a candidate that loses evaluation flips to `rejected` and is simply never pointed at, no revert needed. This is `commonplace-as-a-reflective-system.md`'s three-row pattern (candidate framing, evaluation, retention) with retention as a pointer swap instead of a separate concept. Evaluation itself is not in this table — see edges, below, which is where review-pair-shaped evidence already lives and stays.

## Edges: one table, freshness as an opt-in layer

```sql
CREATE TABLE edges (
    edge_id INTEGER PRIMARY KEY,
    source_artifact_id INTEGER NOT NULL REFERENCES artifacts(artifact_id),
    target_artifact_id INTEGER NOT NULL REFERENCES artifacts(artifact_id),
    edge_label TEXT NOT NULL CHECK (length(edge_label) > 0),
    -- 'extends' | 'contradicts' | 'defined-in' | 'tag' | 'type-of' | 'collection-member' | 'blocks' | ...
    created_at TEXT NOT NULL,
    UNIQUE (source_artifact_id, target_artifact_id, edge_label)
);
```

Every authored link, every tag membership, every `type:` pointer, every collection membership, every workshop `blocks`/`depends-on` relation is a row here — Gap 3's forced consequence of having no authored-prose tier to fall back on. Gap 5's workshop dependency edges fold into this table too; a `workshop_items` table turns out not to earn its keep as a separate concept, only as `artifacts.artifact_kind = 'workshop-item'` plus a `state` column analogous to `content_versions.state` but with its own transition enum.

Most rows here are read far more than invalidated. Freshness tracking is **not** a column on `edges` — it's the existing generic mechanism (`freshness_baselines` / `freshness_inputs`, unmodified) opting in via `target_kind`:

```json
{"target_kind": "edge-validity", "target_key_json": "{\"edge_id\": 4821}"}
```

An edge with no registered `edge-validity` target is simply trusted until something notices otherwise — Gap 3's "cheap edges get no freshness tracking at all" resolution. An edge whose endpoints churn enough to justify eager invalidation (the review `(note, criterion)` case, generalized) gets a target registered the same way a review pair does today. This is the graded-maintenance answer `many-to-many-edge-state-is-where-files-yield-to-a-database.md` leaves as an open question — the schema doesn't resolve *which* edges deserve it, but it means that decision is a per-edge-class policy choice, not a schema fork.

## Types, as content with a bootstrap seam

A type spec is `artifact_kind = 'type'`, versioned through `content_versions` exactly like a note. The `type-of` edge (`edges` table, `edge_label = 'type-of'`) replaces `type:` frontmatter's path pointer. This is Gap 2's registry, and it satisfies Gap 6's reflective-system self-representation criterion only if a validator reads `content_versions` rows where `artifact_kind = 'type'` live and rejects `type-of`-linked content that violates them — the causal connection has to run through code that queries these tables, not just their existence.

That validator itself has to be written against *some* fixed shape, and that shape cannot be a row in `content_versions` without regress — something has to check the checker. The honest placement, following `reflective-system.md`'s explicit allowance for "an unrepresented or unmodifiable kernel": the *table schema above* (the DDL, `artifact_kind` enumeration, `edge_label` vocabulary as code-level constants or a fixed bootstrap table) is the kernel, structurally identical to Commonplace's own fixed JSON-Schema bootstrap validator for `kb/types/*.md`. A DB-native design doesn't remove this seam; it relocates it from "a bootstrap `.py` validator reading `.md` files" to "a bootstrap `.py` validator reading DB rows." Worth naming because it means Gap 6 does not get *harder* under DB-native storage, only equally hard in a different place — a finding worth carrying forward rather than assuming a database making everything relational also makes the type system self-hosting.

## What doesn't fit the pattern

- **Gap 4 (browsing/agent access)** stays outside this schema entirely — no table addresses "a human can look at this with zero setup" or "an agent can `grep` it." That's confirmed, not just repeated: nothing drafted above changes the interface cost `files-not-database.md` names. A DB-native design pays it regardless of how clean the relational model underneath is.
- **Diffing** is not stored — `content_versions` stores full text per version (deliberately, matching `artifact_snapshots`'s existing choice: cheap to compute a diff on read from two full-text rows, expensive and fragile to store diffs and replay them). This means storage grows with edit count × content size, uncosted here — a real implementation would need to decide whether that's acceptable at Commonplace's current note count and edit frequency, or whether some versions need to be dropped/compacted, which reopens a git-gc-shaped problem this schema currently ignores.
- **Rename tracking** is only as good as whoever writes the next `content_versions.path` value consistently referencing the same `artifact_id` — the schema makes stable identity *possible*, it doesn't make rename detection automatic. Something (an agent, a move-tool) still has to know it's moving artifact 4821 rather than creating a new one and deleting an old one; this is the same problem `relocation.py`'s 703 lines solve today for path-keyed identity, moved rather than removed.

## Open questions carried forward

- Does `content_versions.state` cleanly cover collection-level content too (Gap 2's `collection-text` digest), or does a materialized collection membership query need its own versioned artifact row per digest, distinct from any single member's version?
- What retires a `content_versions` row — is there ever deletion, or does everything superseded stay forever (git's answer, effectively, since git never forgets either)? This schema currently assumes the latter and doesn't budget for it.
- The `edge-validity` target_kind reuses `freshness_baselines`/`freshness_inputs` unmodified in sketch form above — worth actually writing the input-role mapping (what plays the role `artifact_freshness_and_referential_checks` gives to `note`/`criterion`) before treating this as settled rather than plausible.

---

Relevant Notes:

- [freshness-schema-as-starting-skeleton.md](./freshness-schema-as-starting-skeleton.md) — the seven-gap survey this schema is drafted against
- [artifact-freshness-and-referential-checks/database-design.md](../artifact-freshness-and-referential-checks/database-design.md) — DDL style and the shipped `target_kind`/`target_key_json` genericity this schema extends past review pairs
- [review-lineage-storage-case.md](../src-architecture-alternatives/review-lineage-storage-case.md) — the stable-id-vs-path question this schema answers by making path a `content_versions` attribute, not artifact identity
- [many-to-many-edge-state-is-where-files-yield-to-a-database.md](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — the graded-tracking question `edge-validity`-as-opt-in answers structurally, without deciding which edges qualify
