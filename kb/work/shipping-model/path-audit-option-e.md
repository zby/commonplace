# Path audit: does Option E work?

A pattern-level audit of every hardcoded `kb/{notes,reference,instructions,types,...}/` path in shipped content, with an Option-E compatibility assessment per pattern. Written to replace the earlier "~85 references" undercount and to answer whether Option E (`kb/commonplace/{notes,reference,instructions}/`) can ship as-is using relative paths, or what exactly needs translation.

## Scope

Scanned all of `kb/notes/`, `kb/reference/`, `kb/instructions/`. Not yet scanned: `AGENTS.md.template`, `.envrc.template`, `kb/sources/types/`, `kb/reports/types/`, `kb/types/`.

## Raw counts

| Collection | References to `kb/{notes,reference,instructions,types,...}/` | Files |
|---|---|---|
| `kb/instructions/` | 204 | 67 |
| `kb/notes/` | 266 | 192 |
| `kb/reference/` | 243 | 39 |
| **Total** | **713** | **298** |

Additional frontmatter count: **300** `type: kb/...` entries across the three collections (these point at type-spec docs, not at other content).

## Reference pattern classes

Each reference falls into one of six patterns. The E-compatibility answer is different for each.

### Pattern A — Generic descriptive references in prose

**Example.** `COLLECTION.md`: "Scan `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/sources/`, and `kb/instructions/` for link targets." Or `README.md`: "Use `kb/notes/` for transferable claims and theory."

**What they are.** Prose mentions of collection names for human readers. The path is a label, not a click target. In a user's install, the sentence "Use `kb/notes/` for transferable claims" refers to *the user's* `kb/notes/`, and that is the intended reading.

**Option E result.** ✅ Work as-is. No translation. The label resolves semantically to whatever `kb/notes/` means in the reader's context (in our repo: our collection; in a user install: the user's collection).

**Estimated share.** Dominant in `COLLECTION.md`, `README.md`, and the higher-level instructions. Probably 40–60% of the 713.

### Pattern B — Frontmatter `type:` pointers

**Example.** `type: kb/types/note.md`, `type: kb/notes/types/structured-claim.md`, `type: kb/reference/types/adr.md`.

**What they are.** Tool-interpreted absolute-from-root paths used by the type resolver. 300 such entries across notes/reference/instructions. Split into two sub-patterns with different E-compatibility.

#### B1 — Shared global types (`kb/types/...`)

Types that live at the top-level shared `kb/types/` directory. All three collections (notes, reference, instructions) reference these — e.g. `type: kb/types/note.md`, `type: kb/types/index.md`.

**Option E result.** ✅ Work as-is **if** `kb/types/` stays at shared top level. Both our repo and a user's install have `kb/types/` at the same path. No nesting under `kb/commonplace/`.

If instead `kb/types/` were nested under `kb/commonplace/types/`, these references would need translation — so the decision is to **keep `kb/types/` at top level and shared**, which matches current `init_project.py` behavior.

#### B2 — Collection-local types (`kb/notes/types/...`, `kb/reference/types/...`)

Types that live inside a specific collection — e.g. `type: kb/notes/types/structured-claim.md`, `type: kb/reference/types/adr.md`. These carry scope information (a `structured-claim` is for notes; an `adr` is for reference). Rationale for keeping types local: [kb/notes/directory-scoped-types-are-cheaper-than-global-types.md](../../notes/directory-scoped-types-are-cheaper-than-global-types.md).

**Option E result.** ❌ Break under E without intervention. A note at `kb/commonplace/notes/foo.md` with frontmatter `type: kb/notes/types/structured-claim.md` points at the user's (empty) `kb/notes/types/structured-claim.md`, not at the library's `kb/commonplace/notes/types/structured-claim.md`.

**Resolution options:**

| Option | Mechanism | Pro | Con |
|---|---|---|---|
| B2a. Ship-time translation | Rewrite `type: kb/notes/types/` → `type: kb/commonplace/notes/types/` during packaging | Simple; contained in build tooling | Frontmatter diverges between source and ship — **dropped**, B2b is cheap enough |
| **B2b. File-relative frontmatter** ✅ | Rewrite to file-relative paths, same convention as markdown links: `type: ../types/structured-claim.md` for a note in a subdirectory, `type: ./types/structured-claim.md` for a note at the collection root | **Invariant under E** — same string works in source and ship; generalizes to any future collection-local resource; resolver change confirmed small (~1–2h) | Requires type resolver extension (confirmed feasible); different notes have different prefixes depending on their depth |
| B2c. Type-resolver two-root fallback | Resolver tries user path first, falls back to library | No frontmatter changes | Magic resolution; fragile; hides the real problem |
| B2d. Flatten to shared `kb/types/` | Move collection-local types to top-level | Fewest paths to worry about | Contradicts existing theory on directory-scoped types — **rejected** |
| B2e. Hybrid | Common types shared; collection-specific types local; ship-time translate only the locals | Minimizes translation | Two classes of types; decision matrix per type |

**Decision: B2b confirmed.** File-relative frontmatter is the right target — same convention as existing markdown links, so notes use one consistent path style for both references and type pointers. Invariant under namespace wrapping in E.

**Type resolver capability check (2026-04-23).** Current resolver in [`src/commonplace/lib/type_resolver.py`](../../../src/commonplace/lib/type_resolver.py) explicitly rejects file-relative paths at `_validate_repo_relative_kb_path` (lines 55-62):

- Rejects absolute paths
- Requires values to start with `kb/`
- Rejects any `..` segments

To enable B2b, relax this function to accept both forms:

- Values starting with `./` or `../` → resolve against `file_path.parent`
- Values starting with `kb/` → resolve against `workspace_root` (current behavior)
- In both cases, preserve the existing "must resolve under `kb/`" boundary check (line 67) — already handles both cases correctly via `.resolve().relative_to(boundary)`.

**Scope:** ~30 lines in `type_resolver.py`, plus tests in `test/commonplace/lib/test_type_resolver.py`. `resolve_type(file_path, ...)` already receives `file_path`; threading it into `validate_type_path` is trivial. No caller changes needed in `validation.py` or `validate_notes.py`. Estimated 1–2 hours including test coverage.

**Helpful precedent:** the resolver already resolves JSON-schema `$ref` links file-relative (line 165: `(resolved.parent / ref).resolve()`), so the pattern is already established in the codebase.

**B2a dropped.** With B2b this cheap, ship-time translation adds no value.

**B2d (flatten global) rejected.** Contradicts [directory-scoped-types-are-cheaper-than-global-types](../../notes/directory-scoped-types-are-cheaper-than-global-types.md).

**Important caveat for the B1/B2 split.** Only B2 (collection-local types) can use file-relative paths. B1 (global `kb/types/`) must stay as absolute-from-root paths (`type: kb/types/note.md`). Reason: file-relative from `kb/notes/foo.md` to `kb/types/note.md` is `../types/note.md` — works in source. But in ship, the file is at `kb/commonplace/notes/foo.md` while the global types are at `kb/types/note.md` (shared, not under commonplace), so the relative path would need to be `../../types/note.md` — different depth. Absolute-from-root `kb/types/note.md` stays invariant under E because `kb/types/` stays at top level.

The clean split: **B1 absolute, B2 file-relative.** Both invariant under E.

**Exact split (audited 2026-04-23):**

| Type value | Count | Category |
|---|---|---|
| `kb/types/note.md` | 177 | B1 |
| `kb/types/instruction.md` | 63 | B1 |
| `kb/types/index.md` | 21 | B1 |
| `kb/types/definition.md` | 6 | B1 |
| `kb/types/type-spec.md` | 3 | B1 |
| `kb/reference/types/adr.md` | 20 (frontmatter) | B2 |
| `kb/notes/types/structured-claim.md` | 4 (frontmatter, shipped) | B2 |
| `kb/sources/types/snapshot.md` | 1 | B2 (in sources — not shipped) |
| `kb/sources/types/ingest-report.md` | 1 | B2 (in sources — not shipped) |
| **Total** | **296 frontmatter** | **B1: 270 / B2 (shipped): 24** |

**Migration status (2026-04-23): COMPLETE.** All 24 B2 frontmatter pointers in shipped content rewritten:

- `kb/reference/adr/*.md` (20 files) → `type: ../types/adr.md`
- `kb/notes/*.md` (4 files) → `type: ./types/structured-claim.md`

Workshop files using `structured-claim` (2 in `kb/work/agent-complexity-theory/`) skipped — not shipped; leaving them absolute avoids awkward cross-collection relative paths in working content.

**Additional change**: `validate_instance` in `type_resolver.py` now normalizes `instance.frontmatter.type` to the canonical `kb/...` form before running the JSON-schema validator, so `const: kb/<collection>/types/<name>.md` checks match regardless of whether the source used repo-relative or file-relative form. Test covers this at `test_validate_instance_normalizes_file_relative_type_for_const_match`.

All 24 migrated files validate clean; all 234 tests pass.

### Pattern C — Within-collection absolute references

**Example.** `REVIEW-SYSTEM.md`: "Instruction: `kb/instructions/run-review-batches.md`" — a code-formatted text reference from one file in `kb/instructions/` to another. Or inside a note, prose text like "see `kb/notes/distillation-is-transformation-not-selection.md`" (rare — notes mostly use markdown links).

**What they are.** Absolute paths as display text (code-fenced or prose), not markdown links. The path is shown to the user as-is.

**Option E result.** ⚠️ Link click-through is moot (these aren't links), but the *displayed text* becomes inaccurate. A user reading shipped `REVIEW-SYSTEM.md` sees "Instruction: `kb/instructions/run-review-batches.md`" but the file is actually at `kb/commonplace/instructions/run-review-batches.md`. Cosmetic but confusing if the user tries to grep or open by the displayed path.

**Options:** (a) rewrite display text at ship time, (b) accept cosmetic drift, (c) rewrite source to use relative references in prose ("`./run-review-batches.md`" — ugly).

**Estimated share.** Small — probably <10% of the 713. Most cross-file references use markdown links (Pattern D/E), not absolute paths as prose.

### Pattern D — Markdown links with sibling-relative paths

**Example.** `COLLECTION.md` in `kb/instructions/`: `[register](../notes/definitions/register.md)`. The URL is `../notes/definitions/register.md` — from `kb/instructions/` this resolves to `kb/notes/definitions/register.md`.

**What they are.** Actual markdown hyperlinks using relative URLs that go up one level and into a sibling collection.

**Option E result.** ✅ Work unchanged. From `kb/commonplace/instructions/` the path `../notes/definitions/register.md` resolves to `kb/commonplace/notes/definitions/register.md` — exactly what the reader wants (the shipped library's note). No translation needed.

This is the crucial pattern for E's viability: sibling-relative URLs are invariant under the `kb/commonplace/` wrapping.

**Estimated share.** Common in `kb/notes/` (notes linking to other collections' material) and `kb/reference/` (references citing notes). Hard to estimate precisely without a fuller audit, but the grep confirmed many existing links already use this pattern. Likely 20–30% of the 713.

### Pattern E — Markdown links with long-relative paths (`../kb/...`)

**Example.** `REVIEW-SYSTEM.md`: `[kb/reference/adr/010-...md](../kb/reference/adr/010-...md)` — URL goes up one level (to repo root) and back down through `kb/`.

**What they are.** Markdown links that route through the repo root instead of going sibling-to-sibling.

**Option E result.** ❌ Break under E. From `kb/commonplace/instructions/REVIEW-SYSTEM.md`, `../kb/reference/adr/...` resolves to `kb/commonplace/kb/reference/adr/...` — wrong directory, no such path. These links need rewriting to Pattern-D style (`../reference/adr/...`) to work under E.

**Estimated share.** Very low — grep found only 1 across shipped content. Not a population worth worrying about; a one-time rewrite pass fixes all of them.

### Pattern F — Markdown links with absolute paths from repo root

**Example.** `[kb/instructions/run-review-batches.md](kb/instructions/run-review-batches.md)` — URL is an absolute path from the repo root.

**What they are.** Links where the URL is treated as a repo-root-relative path (works in GitHub's renderer and some tools; doesn't work as a file-system relative path from the current file's directory).

**Option E result.** ⚠️ Depends on renderer. If the renderer treats the URL as "path from repo root," it resolves to `kb/instructions/...` — the user's own (empty) collection, not the library. Broken. If we rewrite to sibling-relative (`./run-review-batches.md` for within-collection, `../reference/...` for cross-collection), works under both source and ship.

**Estimated share.** Unclear; mixed with Pattern D. Needs a more specific grep distinguishing `[...](kb/...)` (absolute URL) from `[...](./...)` and `[...](../...)` (relative).

### Pattern G — Links in `[path](../kb/...)` or similar "absolute path as display + absolute URL"

These are Pattern E variants and Pattern F variants where the display text itself includes the absolute path. Display text is cosmetic under E (it will be wrong in ship), URL needs rewriting to sibling-relative.

## Summary table

| Pattern | Description | Share | E-compat with existing code | E-compat after rewrite |
|---|---|---|---|---|
| A | Generic prose references (`kb/notes/`) | ~50% | ✅ correct | ✅ |
| B1 | Frontmatter `type:` to shared `kb/types/` | ~15% | ✅ correct | ✅ |
| B2 | Frontmatter `type:` to collection-local types | ~15% (~100–150 sites) | ❌ breaks | ✅ after B2a (ship-time translate) or B2b (relative-path resolver) |
| C | Within-collection prose paths | <10% | ⚠️ cosmetic drift | ✅ |
| D | Sibling-relative links (`../notes/...`) | ~20% | ✅ works unchanged | ✅ |
| E | Long-relative links (`../kb/...`) | 1 site | ❌ breaks | ✅ after one-time rewrite |
| F | Absolute URL links (`[...](kb/...)`) | Unclear | ❌ if renderer uses repo-root | ✅ after rewrite |

## Does Option E work?

**Yes, with four conditions:**

1. **Shared `kb/types/` stays at top level** — do not nest it under `kb/commonplace/`. This keeps B1 frontmatter pointers invariant. Matches current `init_project.py` behavior.
2. **Collection-local types (B2) use B2b** (confirmed 2026-04-23): migrate to file-relative frontmatter (`type: ../types/...` for notes in subdirectories, `type: ./types/...` for notes at collection root — same convention as markdown links). Extend the type resolver to accept file-relative paths (~1–2h of work, precedent exists for `$ref`). Invariant across source and ship. B1 (global `kb/types/`) stays absolute because file-relative would break across the namespace boundary (shared `kb/types/` lives outside `kb/commonplace/`).
3. **Rewrite Patterns E and F to Pattern D** — convert `../kb/reference/...` and `kb/reference/...` (absolute URL) links to sibling-relative `../reference/...`. One-time mechanical rewrite, affects a small number of links (Pattern E has 1 known case; F needs a precise count but is bounded).
4. **Accept cosmetic drift in Pattern C** — prose text like "`kb/instructions/run-review-batches.md`" shown to a user reading the shipped file will be inaccurate (the file is at `kb/commonplace/instructions/...`). Either rewrite display text at ship time or live with it. Small population.

Under these conditions, Option E ships with **zero translation of Pattern-A content (the majority)**, no translation for B1 frontmatter, a bounded one-pass migration for B2 frontmatter, and a one-pass conversion of E/F → D.

## How does this affect the D-vs-E comparison?

Under **Option D** (`kb/cp-notes/`, etc.):

- Pattern A still works unchanged.
- Pattern B has the same types-placement question; same answer.
- Pattern D (sibling-relative links `../notes/...`) **breaks** because the sibling is `cp-notes/`, not `notes/`. These need to become `../cp-notes/...` in ship — a translation. The rewrite would be a repo-wide mechanical change but it's still a translation pass, and the source `../notes/...` cannot stay as-is.
- Patterns C, E, F have the same or worse issues as under E.

**Net: Option E translates less than Option D.** Specifically, E preserves the sibling-relative link pattern (D) unchanged, while D requires rewriting every `../notes/`, `../reference/`, `../instructions/` URL in the shipped tree to `../cp-notes/`, etc.

This is a meaningful reversal of the earlier "cheaper to walk back from" argument for D: once you account for sibling-relative links, **E is the cheaper option to ship**, because it preserves a larger set of existing links intact. D's simplicity was in layout; E's simplicity is in path invariance.

## Bundle scope — per-directory decisions

Every top-level entry under `kb/` classified. Four categories:

- **L (library)** — shipped under `kb/commonplace/` in the user's tree; read-only content
- **S (shared)** — shipped at the user's `kb/` top level; library and user both consume and extend
- **U (user-scaffold)** — we provide empty directories or minimal templates for the user to fill in; our content in these paths does NOT ship
- **—  (not shipped)** — excluded from the bundle entirely

| Dir | Files (tracked) | Size | Category | Where in user's tree | Notes |
|---|---|---|---|---|---|
| `kb/notes/` | 195 | 1.8M | **L** | `kb/commonplace/notes/` | Theory + methodology library |
| `kb/reference/` | 39 | 328K | **L** | `kb/commonplace/reference/` | Shipped-system docs + ADRs |
| `kb/instructions/` | 68 | 452K | **L** | `kb/commonplace/instructions/` | Methodology procedures + skills |
| `kb/agent-memory-systems/` | 108 | 1.9M | **L** | `kb/commonplace/agent-memory-systems/` | Reviews of external systems, linked from notes |
| `kb/types/` | 12 | 52K | **S** | `kb/types/` | Shared global types; users extend alongside ours. Top-level placement preserves B1 absolute-path invariance |
| `kb/sources/types/` | subset | — | **U** | `kb/sources/types/` | Type scaffolding for user's own sources (not library content) |
| `kb/reports/types/` | subset | — | **U** | `kb/reports/types/` | Type scaffolding for user's own reports |
| `kb/sources/` (content) | 194 | 4.2M | **—** | omitted | 4.2M bulk + copyright risk for captured external material. See linking principle below |
| `kb/reports/` (content) | 5 | — | **—** | user-scaffolds empty | Our 5 tracked reports are operational; user's `kb/reports/` starts empty (except types/) |
| `kb/tasks/` | 10 | 64K | **U** | `kb/tasks/{backlog,active,completed}/` empty | User gets empty task dirs; our tracked tasks don't ship |
| `kb/log.md` | 1 | 13K | **U** | `kb/log.md` empty | User gets an empty log file; our log doesn't ship |
| `kb/work/` | 201 | 2.1M | **—** | user-scaffolds empty `kb/work/` | Workshop layer is temporary by design; users create their own workshops |
| `kb/index.md` | 1 | 5K | **U** (regenerated) | `kb/index.md` regenerated | Auto-generated parent index; `commonplace-refresh-indexes` rebuilds for user's tree |

### Totals

- **Shipped under `kb/commonplace/`** (category L): ~410 files, ~4.5M
- **Shipped at shared `kb/types/`** (category S): 12 files, 52K
- **Scaffolded empty or with type definitions** (category U): ~15 files of type scaffolding, plus empty directories
- **Total bundle**: ~425 files of library + ~15 files of scaffolding ≈ **~440 files, ~4.5M**

This is roughly 1.5× the current shipped footprint (~320 files today), and still well under 10M.

### Cost of omitting `kb/sources/`

### Cost of omitting `kb/sources/`

283 markdown links across 94 files in shipped content point at `../sources/...`. Under Option E, these become dangling under `kb/commonplace/notes/` (etc.) because no `kb/commonplace/sources/` exists.

### Derived linking principle

A note's **primary citation** should be the external source (URL, DOI, paper). The local ingest/digest is a **supplementary** link for readers who want our distilled version. Reasons:

- Shipped notes stay valid without shipping sources
- Canonical attribution points at the original author, not our capture
- Readers who want to audit our reasoning go to the original
- Citation hygiene improves independently of the shipping decision

**Current pattern** (primary = local): `[Title](../sources/foo.ingest.md)`

**New pattern** (primary = external, ingest supplementary): `[Title](https://original.url) — [ingest](../sources/foo.ingest.md)` or simply `[Title](https://original.url)` if no ingest exists.

Migration: 283 links across 94 files need a rewrite pass. Each conversion requires looking up the external URL from the ingest's frontmatter. Mechanical-ish but non-trivial.

This principle is itself worth extracting as a library note — it's a general claim about KB citation practice that applies beyond the shipping model workshop.

## Open questions

- Exact Category F (absolute-URL links) count — needs a grep that distinguishes `[...](kb/...)` from `[...](./...)`.
- Template audit (2026-04-23):
  - `.envrc.template` — clean, no kb/ paths.
  - `AGENTS.md.template` — mostly Pattern A (generic references to the user's own `kb/notes/`, `kb/reference/`, `kb/instructions/`). **Three specific references to shipped content** need translation: `kb/reference/commands.md`, `kb/instructions/REVIEW-SYSTEM.md`, `kb/instructions/FIX-SYSTEM.md`. Update the template to point at `kb/commonplace/reference/commands.md`, `kb/commonplace/instructions/REVIEW-SYSTEM.md`, `kb/commonplace/instructions/FIX-SYSTEM.md` respectively.
- Sibling collections beyond `notes/reference/instructions` — `kb/agent-memory-systems/`, `kb/reports/` show up as link targets from shipped notes. Do these stay at top level (user-space) or get namespaced under `kb/commonplace/` too? Sources is decided (omit); the others still need a call.
- `kb/sources/` omission migration: can the URL be mechanically extracted from each ingest's frontmatter, or does this need a note-by-note pass?
