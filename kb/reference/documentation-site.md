---
description: How the MkDocs site renders kb/ — the README-vs-index rule, the nav-generation hook, and the full inventory of reader landing pages (GitHub repo page, site home, per-collection landings) that positioning copy must keep consistent
type: kb/types/note.md
tags: []
---

# Documentation site

The KB renders to a static MkDocs site (`mkdocs.yml`, `docs_dir: kb`), published to GitHub Pages by `.github/workflows/pages.yml`. This doc covers how pages and the nav are produced, and — the load-bearing part for anyone doing positioning or site work — the full set of reader **landing pages**, which is larger than it looks and easy to update incompletely.

## The README-vs-index rule

MkDocs (1.6.1) renders a directory's main page from either `index.md` or `README.md`:

- A file named `README.md` is treated as the directory index — it builds to `index.html` and is served at the directory URL. **So a directory with only a `README.md` renders that file as its main page.** Every `kb/<collection>/README.md` is therefore the rendered landing page for its collection.
- If a directory contains **both** `index.md` and `README.md`, they collide on the same output path; `index.md` wins, `README.md` is dropped from the build, and MkDocs logs a warning.

This is why `kb/README.md` does **not** appear on the site: `kb/index.md` shadows it. `kb/README.md` survives only as a source-tree routing aid for agents reading the repo directly; if it ever needs to render, it must be renamed or merged into `kb/index.md`.

## Nav generation

The nav is generated, not hand-listed. `src/commonplace/docs/mkdocs_hooks.py:on_config` walks the directories directly under `docs_dir` and adds a top-nav entry for each one that contains a `README.md`, pointing at that README. `Home` (fixed to `index.md`) leads the list; external `Recent Changes` and `GitHub` links bracket the end. Adding a collection to the nav means giving its directory a `README.md`; nothing in `mkdocs.yml` lists collections.

`mkdocs.yml` also carries a `redirect_maps` block (preserves external URLs across note renames; written by `commonplace-relocate-note`) and `exclude_docs` (keeps `reports/**` and a few workshop fixtures out of the build). Per-collection `dir-index.md` and per-tag listing pages are generated at build time only (ADR 025), covered in [storage-architecture.md](./storage-architecture.md).

## Landing-page inventory

A reader can enter through any of these. They are distinct files with distinct jobs — positioning or identity copy changed in one is **not** changed in the others, which is the failure mode to guard against.

| Page | File | Role | On the site? |
|---|---|---|---|
| GitHub repo page | `/README.md` | Tool face: install, commands, layout, license. Outside `docs_dir`, so GitHub-only. | No (GitHub repo view) |
| Site home | `kb/index.md` | Content face: the rendered site's front door — positioning lede, theory threads, browse. Shadows `kb/README.md`. | Yes (`Home`) |
| Source routing doc | `kb/README.md` | Filesystem-contract routing for agents reading the source tree. Shadowed by `kb/index.md`. | No (dropped from build) |
| Collection landings | `kb/<collection>/README.md` (notes, reference, instructions, agent-memory-systems, agentic-systems, sources, work) | Each collection's curated head and nav target; renders as the collection's main page. | Yes (one nav entry each) |

The root `README.md` (tool face) and `kb/index.md` (content face) are kept as separate files deliberately: they serve different jobs, and `docs_dir: kb` puts the root README outside the docs tree, so a single shared homepage would require moving `docs_dir` or a symlink. Both should open with the same positioning lede and then diverge by job; the shared lede is short enough to sync by hand.

## See also

- [storage-architecture.md](./storage-architecture.md) — the build-time derived indexes and the MkDocs site as a derived surface over authored markdown
- [navigation.md](./navigation.md) — how agents (not human site readers) move through the KB via `rg`, indexes, and links
- [lib-modules.md](./lib-modules.md) — internal API of `commonplace.lib`; the nav/index hooks live in `commonplace.docs.mkdocs_hooks`
