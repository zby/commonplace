---
description: "ADR 021 appendix enumerating shipped-content namespace options, read-only conventions, path translation, skill-root resolution, and collection scaffolding"
type: kb/types/note.md
tags: []
status: current
---

# ADR 021 appendix: shipped-content namespacing design space

Design-space appendix for [ADR 021](./021-ship-library-content-under-kb-commonplace.md). It enumerates the axes that led to shipping Commonplace library content under `kb/commonplace/`.

## Axis 1: Namespacing shape

| Option | Shape | Pro | Con |
|---|---|---|---|
| A. No change | `kb/notes/`, `kb/reference/`, `kb/instructions/` shipped verbatim | Zero churn | User/library collision; no isolation; current state |
| B. Marker file, same paths | Same paths as A, plus `.commonplace` marker at each shipped root | Minimal churn; provenance queryable | Doesn't solve collision; users still share our namespace |
| C. File-level prefix | `cp-distillation-is-transformation.md` etc., still in `kb/notes/` | Visible provenance; no directory changes | Rewrites every internal link once; filename noise; doesn't isolate COLLECTION.md or types |
| D. Directory prefix per collection | `kb/cp-notes/`, `kb/cp-reference/`, `kb/cp-instructions/` | Preserves flat collection structure; peer-siblings with user collections; shorter paths | Six top-level dirs; weaker isolation signal than a boundary directory |
| E. Single namespace directory | `kb/commonplace/{notes,reference,instructions}/` | One boundary to reason about; natural home for a `.commonplace` marker; scales to future additions | Deeper paths in shipped content |
| F. Separate vault | `kb-commonplace/` alongside `kb/` | Strongest isolation | Two vault roots; most skill/config rework |

**Decision (2026-04-23): Option E — `kb/commonplace/{notes,reference,instructions,agent-memory-systems}/`.** Reversed from the earlier D lean after the path audit ([ADR 021 path audit](./021-shipping-model-path-audit-option-e.md)) showed E has strictly lower translation burden than D: sibling-relative links (`../notes/...`, `../reference/...`) are invariant under E's nested-namespace wrapping, but would all need rewriting to `../cp-notes/...` etc. under D. E preserves more existing links intact and the namespace directory gives a single boundary to reason about for read-only enforcement.

## Axis 2: Read-only convention

| Option | Mechanism | Pro | Con |
|---|---|---|---|
| R1. Convention only | README at `kb/commonplace/` says "don't edit" | Zero enforcement cost | Easy to violate |
| R2. Marker file | `.commonplace` at shipped root; `commonplace-init` checks it before overwrite | Detects modification; enables clean re-sync | User must understand the marker |
| R3. Checksum manifest | `kb/commonplace/.manifest` with file hashes; init detects drift | Exact drift detection | Manifest maintenance cost; noisy on intentional local edits |
| R4. File permissions | Chmod readonly at scaffold time | OS-level enforcement | Bad UX on grep/search; cross-platform fragility; doesn't survive git |
| R5. Git submodule | `kb/commonplace/` is a submodule pinned to a commonplace release | Strongest isolation; versioned; re-sync is `git pull` in submodule | Submodule UX friction; requires users to handle submodule init |

**Decision (2026-04-23): R2 — marker file.** A `.commonplace` marker at `kb/commonplace/` root. `commonplace-init` writes it on fresh install; on subsequent runs, init checks that the shipped tree matches the marker's recorded version before overwriting. If modifications are detected, init refuses to overwrite and prints a diff summary asking the user to confirm. No filesystem permissions, no git submodule — users who want stronger isolation can add that later.

## Axis 3: Path translation at ship time

Our source paths reference `kb/notes/...`, `kb/reference/...`, `kb/instructions/...`. In a user's install, shipped content lives at `kb/cp-notes/...` (Option D) or `kb/commonplace/notes/...` (Option E). Not every reference needs translation, though — the 85-reference raw count splits into two populations with very different translation needs:

**Category 1: generic "the collection you're operating on" references.** Instructions that describe collection-generic behavior: "documents live in a `kb/` collection such as `kb/notes/`", "determine the source collection from the path (`kb/notes/...` → `notes`)", "read `kb/<collection>/COLLECTION.md`". In a user install, these resolve correctly to the user's own collections. **No translation needed** — this is precisely the dogfooding win from authoring in the user's working position. Probably the majority of the 85 references.

**Category 2: references to specific shipped artifacts.** A specific ADR number (`kb/reference/adr/010-review-state...`), a specific shipped instruction file (`kb/instructions/run-review-batches.md`), shipped infrastructure (`kb/instructions/review-gates/{lens}/...`). These point at files that live at the shipped path post-install. **These do need translation.**

The exact Category-1 / Category-2 split requires an audit of the 85 references. First-sample readings suggest Category 1 dominates, which significantly reduces the translation burden compared to the earlier "rewrite everything" framing.

| Option | Mechanism | Pro | Con |
|---|---|---|---|
| T1. Rewrite at ship time | Package step translates `kb/notes/` → `kb/commonplace/notes/` in all shipped text | Source stays user-shaped; ship is mechanical | Translation step is code that can break; source-vs-ship divergence is a correctness gap |
| T2. Rewrite paths in source | Our own instructions reference `kb/commonplace/notes/...` — but we don't have that directory in our repo | Source = ship | Our own links are broken in our repo |
| T3. Path variables | Instructions reference `<cp-root>/notes/...`; skills resolve at runtime | Source = ship; no text rewriting | Every skill must understand the variable; tools like grep and "click to open file" break |
| T4. Symlink in source | Our repo has `kb/commonplace` symlinked to `kb/` — source paths resolve through the symlink | Source = ship | Symlinks on Windows; doubles grep hits; fragile |
| T5. Dogfooding mirror | Our repo maintains `kb/commonplace/` as a duplicate-for-testing | Lets us test shipped instructions in our tree | Maintenance cost; contradicts user's "dogfood as a user" framing |

**Decision (2026-04-23): T1, scoped narrowly.** Translation step exists but is small. Concrete translation operations:

- Rewrite Pattern E (long-relative `../kb/...`) and Pattern F (absolute URL `[...](kb/...)`) links to Pattern D (sibling-relative `../notes/...`, etc.) — one-time pass across shipped content.
- Migrate B2 frontmatter (28 pointers) from absolute to file-relative (`./types/...` or `../types/...`) — one-time pass.
- Update `AGENTS.md.template`'s three specific library references to `kb/commonplace/...`.
- Move shipped trees under `kb/commonplace/` in `SCAFFOLD_TREES`.

Accept: cosmetic drift in Pattern C (code-formatted prose paths like "`kb/instructions/run-review-batches.md`" — small population, rewrite display text at ship time if it becomes a support issue).

## Axis 4: Skill root resolution

Skills today assume a single root (the project root) and look under `kb/notes/`, `kb/reference/`, `kb/instructions/` relative to it. Post-shipping, they need to know about two collection roots.

| Option | Mechanism | Pro | Con |
|---|---|---|---|
| K1. Hardcoded fallback | Each skill checks the library path if target missing in user path | No config | Scattered logic across skills; brittle |
| K2. Config file | `kb/.commonplace-config.yaml` names library roots | Centralized; explicit | New config surface; must be maintained |
| K3. Env variable | `$COMMONPLACE_LIBRARY_ROOT` | Runtime configurable | Silent if unset |
| K4a. Presence check on single dir | Always look for `kb/commonplace/` alongside user collections; if present, library root. Else single-root. | No config; zero-setup | Directory-name lock-in for the namespace |
| K4b. Prefix-glob convention | Library collections are `kb/cp-*/`; user collections are `kb/*/` minus prefix matches. Glob at skill init. | No config; no central dir | Prefix lock-in; every skill needs the glob logic |

**Decision (2026-04-23): K4a.** Skills look for `kb/commonplace/` alongside user collections. If present, it's the library root — skills include it when scanning for link targets, loading type specs, etc. If absent, single-root mode. No config file. Follows from Axis-1 Option E.

## Axis 5: COLLECTION.md duplication

Each collection has a `COLLECTION.md` (register, title conventions, link vocabulary, types). Post-shipping there are six possible ones:

- `kb/notes/COLLECTION.md` (user's own)
- `kb/reference/COLLECTION.md` (user's own)
- `kb/instructions/COLLECTION.md` (user's own)
- `kb/commonplace/notes/COLLECTION.md` (shipped)
- `kb/commonplace/reference/COLLECTION.md` (shipped)
- `kb/commonplace/instructions/COLLECTION.md` (shipped)

User collections need their own because the register may differ. Shipped collections need theirs because skills that *read* shipped content (e.g. `cp-skill-connect` as a link-target scan) need the register to interpret candidates correctly.

| Option | Scaffolding behavior | Pro | Con |
|---|---|---|---|
| C1. No scaffold | User's `kb/notes/` has no COLLECTION.md; user writes from scratch | Clean start; no implied register | User has no starting template; write skills fail-fast until authored |
| C2. Minimal template | `commonplace-init` scaffolds a minimal COLLECTION.md with placeholders for register choice | Discoverable; guides the user | Encodes choices we may want the user to make consciously |
| C3. Copy shipped | Scaffold copies `kb/commonplace/notes/COLLECTION.md` to `kb/notes/COLLECTION.md` as a default | Immediate working state | User inherits our register by accident; strong default that's hard to notice |

**Decision (2026-04-23): C2 — minimal template.** `commonplace-init` scaffolds a minimal `COLLECTION.md` into each user collection (`kb/notes/`, `kb/reference/`, `kb/instructions/`) with explicit register prompts ("theoretical / descriptive / prescriptive — pick one") and placeholder sections. User fills in title conventions, outbound link rules, and type offerings. Shipped `kb/commonplace/*/COLLECTION.md` remain authoritative for the library itself.

## Axis 6: Source-vs-ship divergence cost

If our repo keeps `kb/notes/` and users receive `kb/commonplace/notes/`, there are paths where divergence matters:

- **Testing shipped instructions in our repo.** We can't simply run a shipped skill in our repo and expect it to find `kb/commonplace/notes/COLLECTION.md` because we don't have that directory.
- **Documentation embedded in shipped artifacts.** An instruction that says "see `kb/notes/COLLECTION.md` for register rules" must be translated to `kb/commonplace/notes/COLLECTION.md` at ship time.
- **Link stability.** Internal links within the shipped tree (note-to-note) stay relative and survive unchanged. Cross-collection links within shipped content need translation.

Mitigations:

- `commonplace-ship-preview` that packages the tree into a temp dir with translations applied, so shipped instructions can be tested against a realistic user tree
- A linting rule in the build pipeline: no hardcoded `kb/notes/` in shipped instructions — they must go through the translation step
- A manifest of translation rules checked into the repo so the translation logic is auditable

Current working hypothesis: accept the divergence; add `commonplace-ship-preview` as a validation tool. The translation rules are simple enough to be mechanical; the source-path convention in our repo stays user-shaped.

## Prefix (Option D) vs. namespace directory (Option E): deep comparison

This is the central open question. The two options have similar implementation cost and the same translation burden; the difference is structural positioning and the affordances it creates. Captured here so the argument survives the chat that produced it.

### Arguments for the `cp-` prefix (Option D)

- **Preserves flat collection structure.** `kb/` stays "a directory of collections" rather than gaining a nested grouping layer. The user's `kb/notes/` and the shipped `kb/cp-notes/` are structural peers at the same depth.
- **Copy-as-example is frictionless.** A user comparing conventions opens `kb/cp-notes/COLLECTION.md` right next to their own — same depth, side-by-side. This matters because shipped collections *are* the best worked examples of each register (theoretical, descriptive, prescriptive) we have.
- **Shorter shipped paths.** `kb/cp-notes/definitions/x.md` vs. `kb/commonplace/notes/definitions/x.md` — one fewer segment in the references that do need translation (Category 2 — specific shipped artifacts; see Axis 3).
- **Scales to multi-source libraries.** If a third party publishes `foo-commonplace`, their collections ship as `kb/foo-notes/`, `kb/foo-reference/`. No convention to renegotiate. The namespace-directory approach (Option E) implicitly claims `kb/commonplace/` as "the library root" — harder to extend without a second-level namespace convention (`kb/commonplace/foo/...`?).
- **Simpler skill root resolution.** `glob("kb/cp-*/")` identifies the library; everything else is user. Same depth for both, name pattern only.
- **No artificial grouping layer.** With Option E, `kb/commonplace/` contains collections but is not itself a collection. That introduces a new category of directory ("a collection-of-collections") that the KB otherwise doesn't have.

### Arguments against the `cp-` prefix (Option D)

- **No single boundary to operate on.** "Re-sync the library," "what's shipped?", "remove the library" — all of these refer to a globbed pattern (`kb/cp-*`) rather than one directory. Option E gives a single filesystem object to reason about.
- **Weaker isolation signal.** A filename convention is easier to violate than a directory boundary. A user is more likely to hand-edit `kb/cp-notes/foo.md` ("it's just in my kb") than `kb/commonplace/notes/foo.md` (where every path announces "not yours").
- **"Examples to copy" cuts both ways.** The same proximity that makes the library easy to learn from invites in-place editing — the exact failure mode we want to prevent. Option E makes "copy out before modifying" more structurally obvious.
- **Marker-file placement gets awkward.** With Option D there is no single "library root" to put a `.commonplace` marker at; either three markers (one per prefixed collection) or a top-level `kb/.commonplace-manifest` listing prefix patterns. Option E has an obvious single marker location.
- **Top-level dir count doubles.** User sees `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/cp-notes/`, `kb/cp-reference/`, `kb/cp-instructions/` — six instead of three or four. `ls kb/` gets busier.
- **Prefix lock-in.** The `cp-` prefix becomes part of the skill/instruction contract. Changing it later means rewriting everything that resolves library roots. (Option E has the same cost for `kb/commonplace/` → anything else.)

### What's the same in both options

- **Translation burden.** Both benefit from the dogfooding win: Category-1 "generic collection" references resolve correctly to the user's collection without translation. Both need translation for Category-2 specific-shipped-artifact references. The scope is the same for both options.
- **Source-vs-ship divergence.** In either case, our repo works with `kb/notes/` and the user sees `kb/cp-notes/` or `kb/commonplace/notes/`. The `commonplace-ship-preview` mitigation applies to both.
- **`COLLECTION.md` duplication.** Both options put shipped and user `COLLECTION.md` files in distinct locations (the prefix or namespace-dir handles the isolation).
- **Read-only convention enforcement.** Both rely on convention + a marker + an init-time drift check. Neither uses filesystem permissions.
- **Type copy-to-extend workflow.** Users copy types from the shipped collection into their own `types/` directory, in either layout.

### Framing the tension

- Option D optimizes for **"collections are collections; origin is metadata."** Flat, symmetric, easy to learn from by comparison.
- Option E optimizes for **"shipped content is a bounded thing with a clear edge."** Explicit boundary, single operational unit, stronger provenance signal.

Both are defensible. The choice is about what we want the user's first impression of `ls kb/` to convey — "here are a bunch of collections, yours and ours" vs. "here are your collections and, over there, the library."

### Final disposition: Option E

After the path audit ([ADR 021 path audit](./021-shipping-model-path-audit-option-e.md)), the initial lean toward D reversed. Reason: **E has strictly lower translation cost.**

- Sibling-relative links (`../notes/...`, `../reference/...`, `../agent-memory-systems/...`) are invariant under E's wrapping because `kb/commonplace/{notes,reference,...}` preserves the sibling relationship. Under D, every one of those links would need `../notes/` → `../cp-notes/`.
- File-relative type pointers (B2b, 28 sites) work invariantly under E with one type-resolver extension.
- Global type pointers (B1, 270 sites) stay absolute `kb/types/...` and work under both options.
- The namespace directory gives a single boundary for the `.commonplace` marker and read-only convention.

The abstract argument for D (flat collection structure, examples-as-peers) didn't survive contact with the concrete path-invariance math. E ships cheaper and stays cleaner.
