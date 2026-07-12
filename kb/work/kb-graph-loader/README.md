# Workshop: kb-graph-loader

## Question

Should Commonplace load the KB once into an in-memory graph/model, then let validation, generated indexes, docs hooks, and review targeting query projections of that model?

## Why this workshop exists

Several modules independently walk files, parse frontmatter, strip bodies, extract titles, and apply local filtering rules:

- [project_paths.py](../../../src/commonplace/lib/project_paths.py) owns path and collection discovery.
- [validation.py](../../../src/commonplace/lib/validation.py) defines a local `ParsedNote` and reparses documents for validation and orphan detection.
- [index_directory.py](../../../src/commonplace/lib/index_directory.py) scans directories and parses frontmatter for generated directory listings.
- [index_generated.py](../../../src/commonplace/lib/index_generated.py) scans collections for tag listings.
- [mkdocs_hooks.py](../../../src/commonplace/docs/mkdocs_hooks.py) adds build-time indexes and repeats index metadata reads.
- [review_target_selector.py](../../../src/commonplace/review/review_target_selector.py) has its own notion of reviewable notes and type-content filtering.

The repeated scans are not just a performance smell. They are a consistency risk: each caller can drift on what counts as a note, an index, a type definition, or a reviewable current artifact.

## Scope

In scope:

- a `KbNote` or `LoadedNote` aggregate with path, collection, frontmatter, body, title, links, tags, type, and status;
- one loader that respects collection boundaries, ignored files, type directories, replaced archives, and collection metadata;
- projection helpers for validation, generated indexes, docs hooks, and review targeting;
- deciding whether this model lives under `commonplace.lib.kb_graph`, `commonplace.lib.project_model`, or another small module.

Out of scope:

- persistent graph storage;
- semantic search or embeddings;
- changing file formats or frontmatter schemas;
- changing review DB acceptance state.

## Working Hypothesis

Start with a read-only, in-memory model. Do not build a general graph database. The first useful version should make current behavior easier to express:

- `load_kb(root) -> KbGraph`;
- `graph.collection_notes(collection)`;
- `graph.notes_with_tag(tag)`;
- `graph.reviewable_notes(current_only=False)`;
- `graph.link_targets(note)`;
- `graph.orphan_info()`.

Consumers can adopt it incrementally. Validation is likely the first candidate because it already has `ParsedNote`, link health, schema validation, and orphan checks in one flow.

## Risks

- Loading the entire KB might be wasteful for single-file validation unless the API supports loading a subset.
- A model that tries to own too much policy will become another god module. Keep policy-specific projections near their consumers when needed.
- Existing tests are spread across validation, index generation, docs hooks, and review targeting; migration should proceed one consumer at a time.

## First Work

1. Inventory the filtering predicates and resolve obvious duplicates such as type-definition detection.
2. Define the smallest `LoadedNote` value object that can replace `validation.ParsedNote` without touching other consumers.
3. Move validation onto the loader first, guarded by existing tests.
4. Only then evaluate index generation and review targeting adoption.

## Closure Conditions

Close when this workshop produces:

- a minimal API proposal and first implementation slice;
- or a decision that repeated scans are acceptable, with the consistency risks named and local helper extractions chosen instead.


## New evidence (2026-07-12): referential checks are an undesigned check class

Shipping the verbatim-quote check ([ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md)) made a distinction visible that this workshop should absorb, because it sharpens the loader question from "should consumers share a scan?" to "what model should they share?"

**The dividing line is not frontmatter versus body.** The schema already validates the body: `ParsedDocument.to_validation_object()` hands it `body`, `headings`, `links`, and `body_dates`, and several type schemas assert required headings. Anything about a note's own text that the parse model exposes is declarative and type-owned.

What the schema cannot express is **dereferencing** — *follow this path and look inside the artifact it names*. That yields the real class:

- **Intra-document checks** — schema-declared over the parse model. Frontmatter *and* body. Adding one is a schema edit.
- **Referential checks** — link health (does the target exist?) and verbatim-quote resolution (does this span occur in the source it cites?). Their ground truth lives in a *second* artifact, so they are hand-written imperative passes with **no shared model of a positioned element, no shared severity policy, and no owner.** Adding one is a new bespoke parser.

This is the same gap this workshop already owns, stated more precisely: **a referential check is a graph edge being resolved.** The loader is the natural home for it.

The class arrived without being designed, and it immediately produced a defect: the quote checker shipped with its own markdown parsing and no code-fence handling, so a fenced block *demonstrating* the citation convention was scanned as a live claim and reported as a false mismatch. Two checks over the same prose had disagreed about what counts as content. The immediate fix was to make fence neutralization a single shared primitive (`note_parser.blank_fenced_code_blocks`), blanking rather than deleting so offsets survive.

But the deeper problem stands, and it bears directly on the `LoadedNote` design in step 2 above:

**The shared parse is lossy for its referential consumers.** `ParsedDocument.links` is a tuple of URLs — no positions, no spans. Sufficient for link health, which needs only the *set*. Insufficient for the quote checker, which pairs quotes to citations *by proximity* and must report line numbers, so it still carries a private link regex. A `LoadedNote` that merely deduplicates the file read, without carrying **positioned** body elements (links, quotes, code spans, blockquotes), will not let the second consumer drop its parser — and the divergence will regrow.

So evaluate the minimal `LoadedNote` (step 2) against a concrete *referential* consumer, not just against `validation.ParsedNote`: can the verbatim-quote check be expressed over it **without re-parsing**? If not, the loader has unified the read but not the model, which is the cheaper half of the problem.
