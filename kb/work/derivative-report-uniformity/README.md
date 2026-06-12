# Workshop: Uniformity for source-derived reports

## Goal

Make the three "derivative" report artifacts — reviews, connect reports, and critiques — share one shape where it pays to, while keeping the rigor proportional to what each field is actually used for. Each derives from **one main source artifact** (a note/reference/etc.), all live under `kb/reports/`, all are gitignored and regenerable. Today they diverge in metadata format, directory layout, and source-referencing for no principled reason.

## Question

Should the three source-derived reports converge on (1) one metadata convention (frontmatter), (2) one directory structure, and (3) a shared but light validation/staleness story? And where exactly should strictness fall?

## Current state (as of 2026-06-09)

| aspect | reviews | connect reports | critique |
|---|---|---|---|
| metadata | HTML comment `<!-- REVIEW-METADATA … -->` | YAML frontmatter (`type:`, `source:`, …) | prose header (`**Note:** …`, `**Central commitment:** …`) |
| directory | `kb/reports/reviews/<collection>__<slug>/<gate>.<model>.md` | `kb/reports/connect/<collection>/<artifact>.connect.md` | `kb/reports/critique/<artifact>.critique.md` |
| source ref | `note-path` in comment block | `source` in frontmatter | `**Note:**` in prose header |
| gitignored | yes (README tracked) | yes | yes (README tracked) |
| cardinality | one source → **many** files (gate × model) | one source → one file | one source → one file |

Connect is the only one that already uses frontmatter, and it already has a type-spec + schema under `kb/reports/types/` (`connect-report.md` + `connect-report.schema.yaml`).

## Corrections established during discussion

Two early assumptions were wrong and are worth recording so we don't relitigate:

1. **Reviews are NOT a render of SQLite.** The flow is: `render_bundle_prompt` builds a prompt → an agent generates one bundle (possibly many gates) → `review_protocol_parser` splits it → `run_review_bundle` writes per-gate `.md` files (`encode_stage_filename`, `write_bundle_artifacts`) with the metadata block injected via `inject_review_metadata`. SQLite (`review_db`) is a **parallel ledger** of runs/acceptances/provenance — it keeps a copy of the markdown, but the on-disk per-gate file is the primary generated artifact, not a derived view. This *strengthens* the frontmatter case: the file is first-class, so validatable frontmatter is more appropriate than a bespoke HTML comment, not less.

2. **Bundling is a transparency-and-efficiency mechanism, not a semantic input.** Bundling N gates into one prompt is meant to behave as if each gate ran solo, batched only for efficiency. Full transparency is impossible (neighbors leak through shared context/attention), but the *intent* is that bundle composition is non-semantic.

## Decisions / calibration reached

### 1. Frontmatter everywhere

Drop the HTML-comment block (reviews) and the prose header (critique); standardize on YAML frontmatter, which connect already uses. Shared core: `type`, `source`, `source_has_frontmatter`, a timestamp; plus kind-specific fields. Critique's "central commitment" stays a body heading, not a frontmatter field (it's a sentence). The review exporter owns the frontmatter (`review_metadata.py`'s parse/render moves from comment-block to frontmatter).

Safe to do: `kb/reports/` is **not** a collection (no `COLLECTION.md`) and is gitignored, so the library validator and index generators skip it (`project_paths.py` — "support directories such as kb/reports/ are ignored"). No collision with library frontmatter validation.

### 2. Unified directory structure

One convention: `kb/reports/<kind>/<collection>/<artifact-slug>…`

- connect: `kb/reports/connect/notes/<slug>.connect.md` *(unchanged — it's the model)*
- critique: `kb/reports/critique/notes/<slug>.critique.md` *(add the missing `<collection>/` level)*
- reviews: `kb/reports/reviews/notes/<slug>/<gate>.<model>.md` *(real `notes/<slug>/` nesting instead of `notes__slug` flattening)*

The extra `<slug>/` level for reviews is a **principled** difference, not an inconsistency: reviews are one-source→many-files (gate × model) while the others are one-source→one-file. All three share the `kb/reports/<kind>/<collection>/<artifact>…` prefix.

### 3. Fuzzy validation — strictness follows behavioral authority

We can afford fuzzy rules in the derivatives. Strictness belongs only on fields a machine consumes to make a decision; everything a human/agent merely reads stays loose convention. This is the KB's own `codification` principle: constrain + assign consequences only where something downstream binds on the value.

- Collapse "type-spec + schema per kind + validation profile" into **one thin lint**: frontmatter parses, `source` set and the file exists; for reviews only, the automation provenance fields present and well-formed. Warnings, not gates, for the rest. No per-kind JSON schema enforced as a hard contract.
- Do **not** make `kb/reports/` a collection (would pull reports into orphan/seedling/backlink graph checks that are meaningless for them). Reports are a different validation class — same frontmatter machinery, different (light) profile.

### 4. Fuzzy stale detection — record exactly, decide loosely, sweep deliberately

Stale detection is a **heuristic trigger** for "consider regenerating," not a correctness invariant. Errors are cheap both ways (missed-stale caught by next sweep; needless regen costs only tokens), and there's an agent/human in the loop. So:

- **Drop the `gate-fingerprint → prompt-fingerprint` upgrade** that was proposed (a solo-equivalent assembled-prompt hash). It's not worth building under fuzzy staleness. Keep `gate-fingerprint` as the coarse gate-text hash.
- **Recording stays exact** (cheap facts: note sha, gate-fingerprint, model — the honest audit trail). **The staleness decision stays coarse** (compare note-sha + gate-fingerprint; ignore protocol-scaffolding drift; ignore bundle neighbors).
- **Protocol/scaffolding changes** are handled by a deliberate "invalidate all" sweep, not per-review auto-staleness — re-coupling staleness to the bundle/protocol would kill the efficiency win.
- Bundle-neighbor leakage is treated like model nondeterminism (temperature): known, accepted, un-fingerprinted.

## Net plan

1. Frontmatter unification (reviews: rewrite `review_metadata.py` parse/render comment→frontmatter, update parser/injector, migrate existing files; critique: prose-header→frontmatter; connect: already done).
2. Directory-structure unification (critique adds `<collection>/`; reviews switch `__`-flattening to real `<collection>/<slug>/` nesting — code change in the review path + a migration).
3. One thin reports lint (format + source-exists; strict only on review provenance).
4. Staleness stays coarse; drop the prompt-fingerprint upgrade.

The reviews half is the only code-heavy piece (metadata module rewrite + path scheme + migration). Critique/connect are convention edits.

## What would close this workshop

- A short methodology note on **stale detection as a coarse heuristic trigger** (record exactly, decide loosely, sweep deliberately; bundling is a transparency/efficiency mechanism with accepted leakage). This is the load-bearing rationale that makes the schema/fingerprint choices non-arbitrary.
- The unified report frontmatter + directory convention codified where report producers can see it (likely `kb/reports/README.md` + the per-kind producers: review system, `cp-skill-connect`, the critique instruction).
- Reviews migration landed (metadata module + path scheme + existing-file migration).

## Open questions

- Exact shared-core frontmatter field names (`source` vs `note`; timestamp field name) — align on connect's existing names where possible.
- Whether the thin reports lint is a new `commonplace-*` entry point or a `--reports` mode on existing validation.
- Whether to keep `gate-fingerprint` as-is or rename it now that we've decided not to broaden its scope (cosmetic).
