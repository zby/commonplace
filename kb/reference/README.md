# Reference

Reference documentation for the Commonplace system — how to operate it and how it works.

This collection answers two kinds of question:

- **How do I...?** — operational how-tos for the common workflows your agent runs on your behalf: writing, ingesting, connecting, validating, reviewing, and so on.
- **How does this work?** — the shipped architecture, type system, control-plane conventions, authoring procedures, and the decision record behind major design choices.

Use this collection when the question is specifically about the shipped Commonplace system. For transferable claims and theory about knowledge-base methodology, see [kb/notes/](../notes/). For authoring conventions, each collection has a [COLLECTION.md](./COLLECTION.md) at its root.

## Mental model

You do not operate the KB directly. You instruct an agent, and the agent operates the KB for you.

The agent reads the shipped skills (`.claude/skills/cp-skill-*/SKILL.md` or `.agents/skills/cp-skill-*/SKILL.md`), reads the target collection's `COLLECTION.md`, and writes output under `kb/`.

The practical consequence: ask for outcomes, not internal procedures. "Write a note about X" is better than "read the write skill and then ...". The skill is the agent's concern; the outcome is yours.

This guide assumes you have a running agent session (Claude Code, Codex, etc.) with Commonplace's skills in its discovery path. If `commonplace-init` has run and `.claude/skills/` or `.agents/skills/` exists, you're ready.

## How to

Most operations are things you ask the agent to do. Each entry below shows what the operation is for, how to phrase the request, what the agent does, and the practical limits.

### Add a note

*What it's for.* Capture an insight, decision, or observation as a structured artifact in the KB.

*How to ask.*

- "Write a note arguing that rate limits should be applied per-tenant rather than per-endpoint. Connect it to existing notes on rate limiting."
- "I just realized our retry logic is swallowing errors. Write that up."
- "Capture the decision we just made about moving auth to a sidecar."

*What happens.* The agent searches the KB for related notes, picks a type, reads the writing conventions, drafts the file under `kb/notes/`, and connects it to related notes and indexes.

*What you get.* A new markdown file under `kb/notes/` with frontmatter, a claim-shaped title, and inbound and outbound links to related notes.

*Limitations.* The agent's sense of "what's worth a note" depends on the `## KB Goals and Scope` section in `AGENTS.md`. The out-of-scope list is load-bearing; without it, scope creeps.

### Ingest a source

*What it's for.* Pull an external source (URL, PDF, GitHub issue, tweet) into the KB as a snapshot plus an analysis.

*How to ask.*

- "Ingest https://example.com/some-article and connect it to our notes on context engineering."
- "Read this PDF and ingest the key claims."
- "Ingest the README at github.com/org/project as a related system."

*What happens.* The agent snapshots the source into `kb/sources/`, reads the snapshot, classifies it, finds related notes, and writes an analysis report. In this repo, agent-memory-system reviews use the local `write-agent-memory-system-review` skill so checkout setup, delegated drafting, semantic QA, and validation stay together.

*What you get.* A snapshot under `kb/sources/` and an ingest report named `<slug>.ingest.md` with summary, claims, and links into `kb/notes/`.

*Limitations.* Paywalled or JavaScript-heavy pages can snapshot incompletely. Classification into "related system" versus "source" is sometimes a judgment call.

### Search and navigate

*What it's for.* Find notes relevant to a question without reading the whole KB.

*How to ask.*

- "Find notes about how we decided to validate schemas."
- "What do we have on retry backoff strategies?"
- "Is there anything in the KB about the tradeoff between X and Y?"

*What happens.* The agent combines frontmatter search, curated tag READMEs, scoped ripgrep listings and body search, and link following. It filters by descriptions first, then loads only the notes that look relevant.

*What you get.* A short list of notes with justifications, usually followed by a synthesised answer that cites them inline.

*Limitations.* Search quality depends heavily on frontmatter descriptions, tag coverage, and the query terms an agent chooses. Vocabulary-mismatched concepts need synonym searches and link traversal rather than an external semantic-search daemon.

For the full read path and scaling direction, see [navigation.md](./navigation.md).

### Connect an existing note

*What it's for.* Discover relationships between a note and the rest of the KB, and wire them up.

*How to ask.*

- "Connect `kb/notes/my-new-note.md` to related notes."
- "I just wrote a note on X. Find what it should link to."

*What happens.* The agent reads the source collection's `COLLECTION.md` for its per-destination outbound rules, prospects each authorised destination (curated indexes, scoped `rg` description listings, body search, link-following), applies the articulation test, labels candidates from the destination's authorised set, and writes a connection report. The skill never edits notes — the report is the entire deliverable.

*What you get.* A report at `kb/reports/connect/<collection>/<note-name>.connect.md` (gitignored) listing candidate outbound edges, bidirectional candidates, reverse-edge candidates (notes that should link *to* this target under their own COLLECTION.md rules), off-authorisation candidates (articulated but outside the authorised label set), index memberships, synthesis opportunities, and a discovery trace. Review the candidates and apply the ones worth keeping — connect never mutates the source, so applying the suggestions is a separate step.

*Limitations.* Relationship labels are judgment calls and sometimes need correction. Connection is often underdone at write time, so running connect explicitly on new notes is a reasonable habit.

### Convert between types

*What it's for.* Promote a rough capture to a more structured form as understanding matures.

*How to ask.*

- "Convert `kb/notes/scratch.md` from text to a note."
- "This note has enough argument behind it now. Promote it to a structured-claim."

*What happens.* The agent adds frontmatter, renames the file to match the title where needed, or adds required structural sections such as Evidence and Reasoning.

*What you get.* The same note at a higher point on the type ladder, with the required structure filled in or drafted from the existing prose.

*Limitations.* Demotion is not supported, and converting weak content into a stronger type does not create rigor by itself.

### Revise a note

*What it's for.* Improve the prose of an existing note without changing its claims.

*How to ask.*

- "Revise `kb/notes/foo.md` for flow and clarity. Don't change what it argues."
- "This note feels redundant in the middle section. Tighten it."

*What happens.* The agent makes a revision pass, writes the result to a numbered copy, and asks you to compare before applying.

*What you get.* A revised version for review and, after approval, an updated original.

*Limitations.* Iterative revision can drift semantically over many passes. Keep passes short and verify that the claims survived.

### Validate the KB

*What it's for.* Check that notes have well-formed frontmatter, required fields, resolvable links, and valid type-specific structure. This is deterministic and does not call an LLM.

*How to ask.*

- "Validate `kb/notes/foo.md`."
- "Run validation across the whole KB and report any failures."
- Or run `commonplace-validate kb/notes/foo.md`.

*What happens.* The validator checks schemas, links, filename constraints, and type-specific structural requirements.

*What you get.* A pass/fail report per note with `FAIL`, `WARN`, and `INFO` lines.

*Limitations.* Validation is structural only. Vacuous descriptions or weak claims are review problems, not validator problems.

### Review notes

*What it's for.* Run semantic-quality gates against notes and either accept or fix what the gates flag.

*How to ask.*

- "Review `kb/notes/foo.md` with the prose bundle."
- "Run the semantic review sweep over anything I've changed recently."
- "Ack the trivial changes in the review queue."

*What happens.* The review system stores state in SQLite, selects target `(note, gate)` pairs, creates queued review jobs, delegates each prompt to a worker, and advances acceptance only after all pairs in the job finalize successfully.

*What you get.* Per-gate `PASS` / `WARN` / `FAIL` decisions with rationale text, plus current freshness state.

*Limitations.* The review UX is still agent-driven. Gate selection depends on note traits, worker delegation is owned by the current harness, and the selector/create/finalize command sequence is more operator-facing than a finished end-user CLI.

See [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md) for how to use the review system and [review-architecture.md](./review-architecture.md) for how it is built; [FIX-SYSTEM.md](../instructions/FIX-SYSTEM.md) covers the complementary fix system.

### Direct CLI commands

Most operations go through the agent, but a few CLI commands are reasonable to run directly:

| Command | Purpose |
|---|---|
| `commonplace-validate <path>` | Run the deterministic validator on a note or directory |
| `commonplace-relocate-note <note> --to <dest> [--apply]` | Move or rename a note with link rewrites and mkdocs redirect; dry-run by default |
| `commonplace-github-snapshot <url>` | Snapshot a GitHub issue, PR, or repo README into `kb/sources/` |
| `commonplace-x-snapshot <url>` | Snapshot a Twitter/X post into `kb/sources/` |

`commonplace-relocate-note` dry-runs by default. Pass `--apply` to write changes.

For the full CLI surface, see [commands.md](./commands.md).

## Reference

Look up how the shipped system is put together: its architecture, type system, always-loaded context, authoring procedures, and decision history.

### Architecture and packaging

- [architecture.md](./architecture.md) — installed project layout (library under `kb/commonplace/`, user collections at top level), packaged runtime, promoted skills, and path invariance across source and ship
- [scenario-architecture.md](./scenario-architecture.md) — scenario-derived architecture: the library/user split under `kb/commonplace/`, package-provided commands, and measurable scenario decomposition
- [storage-architecture.md](./storage-architecture.md) — markdown as source of truth, derived indexes, and SQLite as a scoped exception for review state
- [documentation-site.md](./documentation-site.md) — how the MkDocs site renders `kb/`: the README-vs-index rule, the nav-generation hook, and the full inventory of reader landing pages
- [navigation.md](./navigation.md) — how agents move through the KB using control-plane pointers, `rg`, titles/descriptions, indexes, links, connect reports, and future search layers
- [control-plane-goals.md](./control-plane-goals.md) — how Commonplace ships KB goals in always-loaded context via `AGENTS.md`
- [instruction-generation.md](./instruction-generation.md) — build-time instruction generation flow and `commonplace-init`
- [review-architecture.md](./review-architecture.md) — how the review subsystem is built: package layout, storage schema, canonical-state-vs-derived-output, freshness mechanism, module map, and invariants (the build-side companion to [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md))
- [lib-modules.md](./lib-modules.md) — internal API reference for `commonplace.lib` modules

### Type system and collection model

- [collections-and-types.md](./collections-and-types.md) — orientation: how collections (register conventions, per-destination outbound rules) and types (structural contracts) compose, and how the connect/write skills read each source `COLLECTION.md` directly for linking rules
- [available-types.md](./available-types.md) — catalog of shipped types: global (`text`, `note`, `instruction`, `definition`, `index`) and directory-scoped specialised types
- [type-loading.md](./type-loading.md) — how authoring skills and validation resolve a type contract through collection-scoped lookup
- [link-vocabulary.md](./link-vocabulary.md) — linking approach and label catalogue: collection-owned outbound rules, reader-need labels, articulation tests, connect reports, and guidance for `COLLECTION.md` authors
- [definitions/](./definitions/) — vocabulary terms used by the shipped system (e.g., [collection](./definitions/collection.md))

### Authoring and operator procedures

Imperative how-to procedures live in [kb/instructions/](../instructions/) rather than this collection, but they are part of the shipped surface:

- Each collection's `COLLECTION.md` — register-specific writing conventions, quality goals, and placement rules
- [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md) — how to use the review system: concepts, freshness, the batch workflow, and command surface (the how-it-is-built companion is [review-architecture.md](./review-architecture.md))
- [FIX-SYSTEM.md](../instructions/FIX-SYSTEM.md) — current fix-system workflow

### Decision history

[adr/](./adr/) contains the architecture decision records for major shipped-system choices. Notable entries:

- [ADR-021: ship library content under kb/commonplace](./adr/021-ship-library-content-under-kb-commonplace.md) — the library/user boundary, path invariance rules, and scaffold layout behind the current installed surface
- [ADR-027: package scaffold assets without source-tree symlinks](./adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — the current packaging mechanism for scaffold assets in source checkouts, sdists, and wheels
- [ADR-037: promote skills into runtime surfaces by copying](./adr/037-promote-skills-into-runtime-surfaces-by-copying.md) — why `commonplace-init` copies skill directories instead of symlinking or junctioning them
- [ADR-039: tool visibility is package-owned and git is never invoked](./adr/039-tool-visibility-is-package-owned-and-git-is-never-invoked.md) — the name-based visibility contract that replaced gitignore filtering and `git mv`
- [ADR-014: scripts as python package, one-tree model](./adr/014-scripts-as-python-package-one-tree-model.md) — the packaging and install decision ADR-021 refines
- [ADR-012: types for structure, traits for review](./adr/012-types-for-structure-traits-for-review.md) — why structural types and semantic-review traits are separate axes
- [ADR-015: standardize authored type definitions on JSON schema](./adr/015-standardize-authored-type-definitions-on-json-schema.md) — the authored type-definition format
- [ADR-016: custom types use template/instruction pairs](./adr/016-custom-types-use-template-instruction-pairs.md) — how specialised types are packaged
- [ADR-017: COLLECTION.md is the register convention boundary](./adr/017-collection-md-is-the-register-convention-boundary.md) — why collection files own register conventions while types stay structural
- [ADR-019: collection-owned link vocabulary with per-destination outbound rules](./adr/019-collection-owned-link-vocabulary.md) — why each `COLLECTION.md` owns outbound rules per destination collection, and why the connect/write skills read it directly instead of a compiled topology
- [ADR-020: theoretical-default link vocabulary additions](./adr/020-theoretical-default-contrasts-mechanism.md) — the `contrasts` and `mechanism` labels and the directional-asymmetry principle for the theoretical register
- [ADR-035: review jobs finalize all-or-nothing with derived artifacts](./adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — current review-job state model, strict parsing, derived artifact paths, and finalization-time provenance
- [ADR-036: review acceptance is current state, not append-only history](./adr/036-review-acceptance-is-current-state-not-append-only-history.md) — current acceptance rows and inline superseded-review pruning

## Collection boundary

- Use `kb/notes/` for transferable claims and theory.
- Use `kb/reference/` for shipped-system documentation, operator guidance, and decision history.
- Use `kb/instructions/` for imperative procedures and operator-facing process details.

Keep these docs self-contained within the shipped surface. A consuming project should be able to read `kb/reference/` without needing links back to the Commonplace source repository or methodology library.
