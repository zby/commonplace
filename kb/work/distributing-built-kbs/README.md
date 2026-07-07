# Workshop: Distributing KBs built on commonplace

## Question

If someone builds a commonplace KB holding the knowledge needed for a particular problem, what is the most hassle-free way to distribute it to the people and agents who need that knowledge?

This is the **downstream** distribution problem — getting a *domain* KB to its consumers. It is distinct from, and orthogonal to [ADR-021](../../reference/adr/021-ship-library-content-under-kb-commonplace.md), which solved the *upstream* problem: how Commonplace ships its own methodology library into a project, now live as `kb/commonplace/`. The mechanisms rhyme, but the consumer and the payload differ.

## The core reframe: consumer path ≠ author path

This reframe underpins both parts below. A commonplace KB bundles two things that ship together today but have very different distribution needs:

- **The knowledge** — plain markdown in `kb/notes|reference|instructions`, their `COLLECTION.md`s, `kb/types/`, and the committed `dir-index.md` / curated indexes. Static text.
- **The authoring/maintenance machinery** — the `llm-commonplace` package, the `cp-skill-*` family (write / connect / validate / ingest / revise), and the review system (SQLite). Tools for *building* a KB.

A consumer solving a problem only needs to **read and navigate**. Per [navigation.md](../../reference/navigation.md), navigation is a progressive-disclosure stack: control-plane file → `rg` → committed indexes → descriptions → links. None of that requires the Python package or the skills. The minimal consumption runtime is **an agent + `ripgrep` + `git`**. This rests on the "files, not database" principle: authored markdown is the source of truth and indexes are rebuildable navigation artifacts ([storage-architecture](../../reference/storage-architecture.md)), so distribution inherits portability for free.

---

# Part 1 — The current situation: what you can do today

With nothing added to commonplace, a built KB is already distributable, because it is just markdown in git.

## What a consumer needs at read time

An agent + `ripgrep` + `git`. No `llm-commonplace` install, no skills, no daemon — **provided the indexes are committed**. The committed `dir-index.md` / curated indexes plus descriptions and authored links are the whole navigation surface. This is the decisive property: ship pre-built indexes and the reader needs nothing else.

## Modes that work now

1. **Standalone git repo — "clone and point" (lowest hassle).** The KB is its own repo; the consumer runs `git clone`, points their agent at the directory, and starts. Updates are `git pull`. This is the README's "Direct use" mode. Best when there is a dedicated agent or person whose job *is* that problem.

2. **Embedded via plain git — submodule, subtree, or copy.** When the knowledge must live inside another project, ordinary git already supports it: add the KB as a submodule (version-pinnable, some init friction), a subtree (no submodule friction, messier history), or a plain copy. No commonplace feature is required to *place* the tree. **Limitation today:** the consuming project's skills won't treat the embedded KB as a known library root — skill-root resolution presence-checks `kb/commonplace/` specifically (per ADR-021), not an arbitrary `kb/<domain>/`. So a manually embedded domain KB is readable by `rg` and links but is not first-class to the `cp-skill-*` family.

3. **Release tarball (`git archive`).** A versioned snapshot the consumer downloads, unzips, and points at. No history weight, no submodule friction. Works today with stock git.

## Rough edges you hit doing this manually today

Everything above works, but preparing a *clean* bundle is currently a manual checklist:

- **Indexes must be regenerated before release.** If content changed, the author runs `commonplace-refresh-indexes` (the package) so committed indexes are fresh. Authors have the package, so this is fine — but it is a manual step, easy to forget, and a stale index silently degrades the consumer's navigation.
- **Sources need hand-trimming.** `kb/sources/` raw captures are often the bulk of a problem KB and may be copyrighted. Today you manually omit them and fix `../sources/...` links to external URLs (ADR 021 already locked this decision as a rule for Commonplace's own shipped library, but nothing applies it for arbitrary domain KBs).
- **No consumer control-plane exists.** Only the authoring-heavy `AGENTS.md` ships (skills, review, fix, write conventions). To hand a consumer a clean entry point you trim it by hand down to Goals → Key indexes → Navigation conventions.
- **Author-only trees travel unless excluded.** `kb/work/`, `kb/tasks/`, the review SQLite state, and `.venv/` are all author-side and add weight/noise unless you exclude them yourself.
- **No single export command.** The above is a checklist a human runs each release, not one reproducible command.

Net: **distribution works today, but "hassle-free" requires manual discipline** — refresh indexes, strip sources and author trees, trim a consumer control-plane, then clone/submodule/tar.

---

# Part 2 — Brainstorm: what we could add to make it easier

Each item below removes one of the manual rough edges. Ordered roughly by leverage.

## A. A `commonplace-bundle` export command (highest leverage)

One command that produces a consumption bundle, turning the Part 1 checklist into a reproducible build. Sketch:

1. **Select** the consumption subset: `kb/notes`, `kb/reference`, `kb/instructions`, their `COLLECTION.md`s, `kb/types`. Exclude `sources`, `work`, `tasks`, reports, review state, `.venv`.
2. **Rewrite** `../sources/...` links to their external URLs (reuse ADR 021's source-link migration rule).
3. **Regenerate** all indexes fresh so the bundle is navigable without the package.
4. **Swap in** the consumer control-plane file (item B).
5. **Emit** as a standalone repo layout (mode 1), an embeddable `kb/<domain>/` tree with a marker (mode 2), or a tarball (mode 3) — same subset, three packagings.

This shares most of its logic with the `commonplace-ship-preview` tool ADR 021 deferred; building one likely gets the other cheaply.

## B. A consumer control-plane template

A stripped `AGENTS.md` variant that foregrounds Goals → Key indexes → Navigation conventions and drops the authoring workflow (skills, review, fix, write conventions). This is what makes a cold-start consumer agent productive in a single read. `commonplace-init` could grow a `--consumer` control-plane template, or the bundle command could emit it.

## C. Generalize the read-only namespace beyond `kb/commonplace/`

Today ADR-021's read-only-library machinery — namespace directory, `.commonplace` marker, presence-check skill-root resolution, drift check — is hardwired to Commonplace's *own* library. Generalizing it so any embedded domain KB at `kb/<domain>/` is recognized as a read-only library root would make mode 2 first-class: the consuming project's skills would scan the embedded KB as link targets and load its `COLLECTION.md` register. The ADR 021 design space already gestured at this ("scales to multi-source libraries") and left it as an open question. This is the difference between "an agent can grep the embedded KB" and "the embedded KB is a known, navigable library in the project."

## D. Versioning / re-sync metadata

A version tag + manifest in the bundle (generalizing the `.commonplace` marker) so a consumer can tell which release they have and re-sync cleanly. Pairs with mode 2: a submodule pinned to a release tag, or a copy whose marker records the source version, both enable "update to the latest payments-KB" without guesswork.

## E. (Conditional) a stronger search layer for large bundles

If distributed KBs grow past the size where `rg` + indexes stay scannable, [navigation.md](../../reference/navigation.md) already anticipates ranked lexical (BM25) and later semantic/hybrid search. Only worth adding when a distributed KB is large enough that flat lexical search gets noisy — not needed for the small problem-scoped KBs this workshop is mostly about.

## Recommendation

**Today:** default to mode 1 (standalone repo, clone-and-point); use mode 2 (embed via submodule/subtree/copy) when it must live inside a consuming project; tarball for pinned/offline. In all cases the decisive lever is shipping **pre-built indexes + a hand-trimmed consumer control-plane** so the reader never needs the package or the skills.

**To add, in priority order:** (A) the `commonplace-bundle` export command, (B) the consumer control-plane template, then (C) the generalized read-only namespace for first-class embedding. (A) and (B) remove most of the manual hassle; (C) makes embedded domain KBs first-class to the skill family.

## What would close this workshop

- A decision on whether to build `commonplace-bundle` (and whether it merges with `ship-preview`).
- A specification of the consumer control-plane template.
- A decision on whether to generalize the ADR-021 read-only namespace to arbitrary `kb/<domain>/` libraries.
- Promotable durable conclusions: a note on "distributing a KB for consumption is a strictly lighter problem than installing it for authoring," and a reference doc on the bundle format.

## Grounding

- [ADR-021: ship library content under kb/commonplace/](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) — grounds: the read-only-namespace mechanism Part 2 item C would generalize.
- [ADR 021 shipped-content namespacing design space](../../reference/adr/021-shipping-model-design-space.md) — derived-from: the upstream option inventory behind the namespace, marker, drift-check, and source-link decisions reused here.
- [Navigation](../../reference/navigation.md) — grounds: the consumer only needs control-plane + rg + indexes + descriptions + links; also the source for the item-E search-layer roadmap.
- [Storage architecture](../../reference/storage-architecture.md) — grounds: authored markdown is the source of truth; indexes are rebuildable, so the bundle can ship them pre-built.
- [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable.md) — rationale: why a clean consumer boundary preserves trust in the shipped knowledge.
