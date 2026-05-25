# Workshop: Distributing KBs built on commonplace

## Question

If someone builds a commonplace KB holding the knowledge needed for a particular problem, what is the most hassle-free way to distribute it to the people and agents who need that knowledge?

This is the **downstream** distribution problem — getting a *domain* KB to its consumers. It is distinct from, and orthogonal to, the [shipping-model workshop](../shipping-model/README.md), which solved the *upstream* problem: how commonplace ships its own methodology library into a project (decided in [ADR-021](../../reference/adr/021-ship-library-content-under-kb-commonplace.md), now live as `kb/commonplace/`). The mechanisms rhyme, but the consumer and the payload differ.

## The core reframe: consumer path ≠ author path

A commonplace KB bundles two things that ship together today but have very different distribution needs:

- **The knowledge** — plain markdown in `kb/notes|reference|instructions`, their `COLLECTION.md`s, `kb/types/`, and the committed `dir-index.md` / curated indexes. Static text.
- **The authoring/maintenance machinery** — the `llm-commonplace` package, the `cp-skill-*` family (write / connect / validate / ingest / revise), and the review system (SQLite). Tools for *building* a KB.

A consumer solving a problem only needs to **read and navigate**. Per [navigation.md](../../reference/navigation.md), navigation is a progressive-disclosure stack: control-plane file → `rg` → committed indexes → descriptions → links. None of that requires the Python package or the skills. The minimal consumption runtime is **an agent + `ripgrep` + `git`**.

This is the lever:

> **The single biggest hassle-reduction move is to commit fresh indexes at release time and keep the consumer off the package entirely.** The moment navigation depends on running `commonplace-refresh-indexes`, the install step and a runtime dependency come back — to deliver what is fundamentally static text. Pre-build the indexes, ship them, and the consumer needs nothing but an agent with ripgrep.

This rests on the "files, not database" design principle: authored knowledge is file-backed and indexes are rebuildable navigation artifacts, not the source of truth ([storage-architecture](../../reference/storage-architecture.md)). Distribution inherits that property for free.

## Distribution modes, ordered by hassle

### 1. Standalone git repo — "clone and point" (default, lowest hassle)

The KB is its own repository with a consumption-oriented control-plane file at the root. The consumer runs `git clone`, points their agent at the directory, and starts. Updates are `git pull`. This is essentially the README's "Direct use" mode and is the most hassle-free when there is a dedicated agent or person whose job *is* that problem.

- **Pro:** zero install, free versioning, diffable, offline-capable; the control-plane file travels with the content.
- **Con:** it is a separate checkout — if the knowledge must live *inside* another project, you need mode 2.

### 2. Embedded read-only namespace inside a consuming project (`kb/<domain>/`)

When the knowledge must live *inside* another project, this is the **exact problem ADR-021 already solved** for commonplace's own library: a namespace directory, a `.commonplace`-style marker, presence-check skill-root resolution, and a drift check on re-run. A domain KB is just another instance of "ship a read-only library into a consuming tree," so that machinery generalizes from `kb/commonplace/` to `kb/<domain>/`.

Delivery options for the embedded tree:

| Mechanism | Re-sync | Tradeoff |
|---|---|---|
| Git submodule | `git pull` in submodule; version-pinnable | Submodule UX friction; consumers must init it |
| Git subtree | Re-pull subtree | No submodule friction; messier history |
| Plain copy + marker | Re-copy / re-run an export | Simplest; weakest version story |

### 3. Release tarball (`git archive` of the consumption subset)

For pinned or offline consumers: a release artifact they download, unzip, and point at. Versioned, no git-history weight, no submodule friction. Good for "give me exactly v3 of the payments-KB and never move."

### Avoid for pure knowledge: the pip-package + init path

Packaging the content into `_data/` and shipping an `init`-style installer is what commonplace does for its *methodology* library — justified because it ships executable tooling. For a read-only **domain** KB it drags in packaging, an install step, and a runtime dependency to deliver static text. Only justify it if the KB ships its own *executable* tooling (custom validators, generators, or skills) alongside the knowledge.

### MkDocs is a human surface, not the agent path

`mkdocs.yml` already exists and renders the KB for human browsing. That is a **discovery / marketing** complement, not the agent-consumption mechanism — agents consume the markdown and indexes directly.

## What to strip from a consumption bundle

- `kb/sources/` raw captures → **cite external URLs** instead. Sources are often a problem-KB's bulk and may be copyrighted; the shipping-model workshop already locked the "convert source links to external URLs, omit raw sources" decision.
- `kb/work/`, `kb/tasks/`, the review SQLite state, `.venv/` — all author-side, none of it consumed.
- The control-plane file needs a **consumer variant**. The current `AGENTS.md` is authoring-heavy (skills, review, fix, write conventions). A consumer control-plane foregrounds Goals → Key indexes → Navigation conventions and drops the authoring workflow. This is what makes a cold-start agent productive in one read.

## The missing piece: an export command

No command today produces this consumption bundle. `commonplace-init` goes the *opposite* direction — it sets up authoring and installs the methodology library. The shipping-model workshop already flagged a `commonplace-ship-preview` as a needed mitigation; that is the same machinery pointed downstream.

Sketch of `commonplace-bundle` (name TBD):

1. **Select** the consumption subset: `kb/notes`, `kb/reference`, `kb/instructions`, their `COLLECTION.md`s, `kb/types`. Exclude `sources`, `work`, `tasks`, reports, review state, `.venv`.
2. **Rewrite** `../sources/...` links to their external URLs (reuse the shipping-model source-link migration rule).
3. **Regenerate** all indexes fresh (`commonplace-refresh-indexes`) so the bundle is navigable without the package.
4. **Swap in** the consumer control-plane file (a stripped `AGENTS.md`).
5. **Emit** either a standalone repo layout (mode 1), an embeddable `kb/<domain>/` tree with a marker (mode 2), or a tarball (mode 3) — same subset, three packagings.

Building this turns "hassle-free distribution" from a manual checklist into one command, and it shares most of its logic with the already-planned `ship-preview`.

## Recommendation

Default to **mode 1 (standalone git repo, clone-and-point)** for a problem-scoped KB consumed by an agent: it is the lowest-friction path and needs no install. Reach for **mode 2 (embedded read-only `kb/<domain>/`)** when the knowledge must live inside a consuming project, reusing the ADR-021 namespace + marker + presence-check pattern. Use **mode 3 (tarball)** for pinned/offline delivery. In all three, the decisive lever is the same: **ship pre-built indexes and a consumer control-plane so the reader never needs the `llm-commonplace` package or the authoring skills.**

## What would close this workshop

- A decision on whether to build `commonplace-bundle` (and whether it merges with `ship-preview`).
- A specification of the consumer control-plane template.
- A confirmed mode-2 mechanism (submodule vs. subtree vs. copy+marker) for embedding a domain KB.
- Promotable durable conclusions: most likely a note on "distributing a KB for consumption is a strictly lighter problem than installing it for authoring," and a reference doc on the bundle format.

## Grounding

- [Shipping-model workshop](../shipping-model/README.md) — derived-from: the upstream counterpart; its namespace, marker, drift-check, and source-link decisions are reused here.
- [ADR-021: ship library content under kb/commonplace/](../../reference/adr/021-ship-library-content-under-kb-commonplace.md) — grounds: the read-only-namespace mechanism this workshop generalizes.
- [Navigation](../../reference/navigation.md) — grounds: the consumer only needs control-plane + rg + indexes + descriptions + links; no daemon, no package.
- [Storage architecture](../../reference/storage-architecture.md) — grounds: authored markdown is the source of truth; indexes are rebuildable, so the bundle can ship them pre-built.
- [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable.md) — rationale: why a clean consumer boundary preserves trust in the shipped knowledge.
