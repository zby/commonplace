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

*What it's for.* Analyse one URL-backed external source while keeping its reading copy local.

*How to ask.*

- "Ingest https://example.com/some-article and connect it to our notes on context engineering."
- "Read this PDF and ingest the key claims."
- "Ingest the README at github.com/org/project as a related system."

*What happens.* The agent snapshots the source into ignored `kb/sources/.snapshots/`, reads it, finds related notes, and writes a tracked analysis whose frontmatter carries the durable URL, capture provenance, genre, and exact snapshot checksum. In this repo, agent-memory-system reviews use the local `write-agent-memory-system-review` skill so checkout setup, delegated drafting, semantic QA, and validation stay together.

*What you get.* A local snapshot under `kb/sources/.snapshots/` and a tracked ingest report at `kb/sources/<slug>.ingest.md` with summary, claims, and links into `kb/notes/`.

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

### Convert text to a note

*What it's for.* Promote a rough capture to a more structured form as understanding matures.

*How to ask.*

- "Convert `kb/notes/scratch.md` from text to a note."

*What happens.* The agent adds valid note frontmatter: a semantic `description`, `type: kb/types/note.md`, and empty `traits` and `tags`, while leaving `user-verified` absent. It does not edit the body. When the filename does not match the title, it renames the file within its collection and repairs backlinks.

*What you get.* The same captured content as a structurally valid, unverified note, possibly under a title-aligned filename with its inbound links updated.

*Limitations.* Only text → note is implemented. Demotion and note → specialised-type conversion are future directions. Conversion supplies structure and retrieval metadata; it does not improve the body or create rigor.

### Revise a note

*What it's for.* Improve the prose of an existing note without changing its claims.

*How to ask.*

- "Revise `kb/notes/foo.md` for flow and clarity. Don't change what it argues."
- "This note feels redundant in the middle section. Tighten it."

*What happens.* The agent makes a revision pass, writes the result to a numbered copy, and asks you to compare before applying.

*What you get.* A revised version for review and, after approval, an updated original.

*Limitations.* Iterative revision can drift semantically over many passes. Keep passes short and verify that the claims survived.

### Validate the KB

*What it's for.* Check mechanically decidable artifact properties—well-formed frontmatter, required fields, resolvable links, and valid type-specific structure—and explicit repository invariants for collection landings and site redirects. This is deterministic and does not call an LLM.

*How to ask.*

- "Validate `kb/notes/foo.md`."
- "Run validation across the whole KB and report any failures."
- "Check the collection landings and published redirects."
- Or run `commonplace-validate kb/notes/foo.md`.

*What happens.* Artifact targets check schemas, links, filename constraints, and type-specific structural requirements. The `landings` target requires a non-colliding `README.md` for every collection directly under `kb/`; `redirects` checks `properdocs.yml` against the live published tree.

*What you get.* A pass/fail report per target with `FAIL`, `WARN`, and `INFO` lines. Artifact findings are labelled `[base]`, `[type: <name>]`, or `[schema]`; repository findings are labelled `[repository]`. See the [validation contract](./validation-contract.md) for what each source can express.

*Limitations.* Validation judges mechanically decidable properties only. Vacuous descriptions or weak claims are review problems, not validator problems.

### Review notes

*What it's for.* Run snapshot-anchored assays against notes: closed-ended gates return decisions, while open-ended assays such as critique retain current reports.

*How to ask.*

- "Review `kb/notes/foo.md` with the prose bundle."
- "Run the semantic review sweep over anything I've changed recently."
- "Ack the trivial changes in the review queue."

*What happens.* The review system stores state in SQLite, selects target `(note, criterion)` pairs, creates result-kind-homogeneous queued jobs, delegates each prompt to a worker, and advances the freshness baseline only after all pairs in the job finalize successfully.

*What you get.* Per-gate `PASS` / `WARN` / `FAIL` / `ERROR` decisions or open-ended reports, plus current freshness state pinned to the note and criterion bytes.

*Limitations.* The review UX is still agent-driven. Gate selection depends on note traits, worker delegation is owned by the current harness, and the selector/create/finalize command sequence is more operator-facing than a finished end-user CLI.

See [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md) for how to use the review system and [review-architecture.md](./review-architecture.md) for how it is built; [FIX-SYSTEM.md](../instructions/FIX-SYSTEM.md) covers the complementary fix system.

### Direct CLI commands

Most operations go through the agent, but a few CLI commands are reasonable to run directly:

| Command | Purpose |
|---|---|
| `commonplace-validate <target>` | Validate an artifact or collection, global type specs, collection landings, or the published redirect map |
| `commonplace-guard-full-pass-report <report>` | Refuse a full-pass transition unless every packet capture still matches its live artifact |
| `commonplace-relocate-note <note> --to <dest> [--apply]` | Move or rename a note with link rewrites and ProperDocs redirect; dry-run by default |
| `commonplace-github-snapshot <url>` | Snapshot a GitHub issue or PR into local `kb/sources/.snapshots/` |
| `commonplace-x-snapshot <url>` | Snapshot a Twitter/X post into local `kb/sources/.snapshots/` |

`commonplace-relocate-note` dry-runs by default. Pass `--apply` to write changes.

For the full CLI surface, see [commands.md](./commands.md).

## Reference

Look up how the shipped system is put together: its architecture, type system, always-loaded context, authoring procedures, and decision history.

### Architecture and packaging

For exact implementation behavior, inspect `src/commonplace/` in this checkout.
From an installed project, `commonplace-source` locates the package that
supplies the running commands. The documents below retain architecture,
invariants, and orientation that the implementation does not cheaply recover.

- [architecture.md](./architecture.md) — installed project layout (library under `kb/commonplace/`, user collections at top level), packaged runtime, promoted skills, and path invariance across source and ship
- [scenario-architecture.md](./scenario-architecture.md) — scenario-derived architecture: the library/user split under `kb/commonplace/`, package-provided commands, and measurable scenario decomposition
- [storage-architecture.md](./storage-architecture.md) — markdown as source of truth, derived indexes, and SQLite as a scoped exception for review state
- [documentation-site.md](./documentation-site.md) — how the ProperDocs site renders `kb/`: the README-vs-index rule, the nav-generation hook, and the full inventory of reader landing pages
- [navigation.md](./navigation.md) — how agents move through the KB using control-plane pointers, `rg`, titles/descriptions, indexes, links, connect reports, and future search layers
- [control-plane-goals.md](./control-plane-goals.md) — how Commonplace ships KB goals in always-loaded context via `AGENTS.md`
- [instruction-generation.md](./instruction-generation.md) — build-time instruction generation flow and `commonplace-init`
- [review-architecture.md](./review-architecture.md) — review dispatch ownership, canonical state versus derived artifacts, all-or-nothing finalization, and the freshness hash boundary (the build-side companion to [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md))
- [freshness-architecture.md](./freshness-architecture.md) — the general freshness substrate: commonplace store, file-text versioning, target baselines, transitions, global status, and the review adapter

### Type system and collection model

- [collections-and-types.md](./collections-and-types.md) — how collection and type contracts compose, how path-valued type pointers resolve, common examples, and where global and collection-local type specs live
- [link-vocabulary.md](./link-vocabulary.md) — linking approach and label catalogue: collection-owned outbound rules, reader-need labels, articulation tests, connect reports, and guidance for `COLLECTION.md` authors
- [collection-prototypes.md](./collection-prototypes.md) — optional creation-time contracts that may be copied into a new collection; the resulting `COLLECTION.md` is independently owned and receives no prototype updates
- [collections-never-own-frontmatter-semantics.md](./collections-never-own-frontmatter-semantics.md) — why the collection/type split is asymmetric: a type spec owns frontmatter semantics, `COLLECTION.md` owns only text-level features
- [Answerability](./definitions/answerability.md) — Commonplace's stipulated admission boundary: what an artifact answers to, the property it asserts, and the discrepancy that triggers correction
- [Collection and text contract](./definitions/collection.md) — canonical definitions of the collection boundary and its complete local authoring declaration

### Authoring and operator procedures

Imperative how-to procedures live in [kb/instructions/](../instructions/) rather than this collection, but they are part of the shipped surface:

- Each collection's `COLLECTION.md` — collection-specific writing conventions, quality goals, and placement rules
- [README-REVIEW-SYSTEM.md](./README-REVIEW-SYSTEM.md) — how to use the review system: concepts, freshness, the batch workflow, and command surface (the how-it-is-built companion is [review-architecture.md](./review-architecture.md))
- [FIX-SYSTEM.md](../instructions/FIX-SYSTEM.md) — current fix-system workflow
- [full-improvement-pass-closure.md](./full-improvement-pass-closure.md) — how the full-improvement workflow reassays final note bytes, routes residual findings, and stops without claiming convergence
- [harness-sub-agent-model-selection-regression.md](./harness-sub-agent-model-selection-regression.md) — the July harness regression that mis-attributed review executions, the August partial restoration of bounded-fork model overrides, and why a requested model is still not execution provenance

### The repository as a worked case

Commonplace runs on its own methodology, so this collection also documents *this repository* as an operating instance — what it has been observed to do, under which declared boundary, and what that does and does not establish. These describe the case, not the surface a consuming project installs.

- [commonplace-declared-frame.md](./commonplace-declared-frame.md) — the declared boundary all the assessments below are made under: what is inside, what is outside, and how to cite or depart from it
- [commonplace-as-a-reflective-system.md](../notes/evidence/commonplace-as-a-reflective-system.md) — classifies the repository as a human-inclusive reflective self-improving system and locates which functions in one observed pathway are human, joint, or computational
- [commonplace-as-an-instrument.md](./commonplace-as-an-instrument.md) — what the KB application is *for* in the design program: the composition test, two worked provenance instances, and the transfer evidence the repository does not have
- [design-rationale-management.md](./design-rationale-management.md) — how workshops, proposals, ADRs, contracts, and validators distribute design rationale, and the end-to-end continuity the shipped contracts do not enforce
- [tag-readme-trace-observed-causal-connection.md](../notes/evidence/tag-readme-trace-observed-causal-connection.md) — the ADR-026 change traced commit by commit as one observed instance of causal connection in both directions
- [tag-readme-trace-as-self-improving-loop.md](./tag-readme-trace-as-self-improving-loop.md) — the same trace mapped onto search, evaluation, and retention, showing which half of each step runs in code
- [where-change-candidates-come-from-in-commonplace.md](./where-change-candidates-come-from-in-commonplace.md) — how problem-noticing and candidate-drafting happen beyond a maintainer's own judgment
- [agent-memory-coverage.md](./agent-memory-coverage.md) — how the shipped surfaces realize agent-memory requirements, and where they currently fall short
- [commonplace-agent-memory-gap-plan.md](./commonplace-agent-memory-gap-plan.md) — the plan for closing those gaps: session traces, candidates, cue activation, behavioral evaluation, lifecycle, import, ranking, and authority

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
- [ADR-017: COLLECTION.md is the register convention boundary](./adr/017-collection-md-is-the-register-convention-boundary.md) — why collection files became the boundary for the then-current register conventions while types stayed structural
- [ADR-068: collection contracts stop enumerating available types](./adr/068-collection-contracts-stop-enumerating-available-types.md) — global-plus-owned-local type eligibility, the `kb/work/` exception, and filesystem-backed type discovery
- [ADR-070: notes bind choices; reference records selections and state](./adr/070-notes-bind-choices-reference-records-selections-and-state.md) — the intended-contribution and choice-binding test that separates transferable theory from Commonplace's selected and resulting state
- [ADR-071: text contract is part of the collection definition](./adr/071-text-contract-is-part-of-the-collection-definition.md) — why collection and text-contract vocabulary have one reference owner while each local `COLLECTION.md` remains the binding surface
- [ADR-019: collection-owned link vocabulary with per-destination outbound rules](./adr/019-collection-owned-link-vocabulary.md) — why each `COLLECTION.md` owns outbound rules per local destination collection, and why the connect/write skills read it directly instead of a compiled topology
- [ADR-059: external is a reserved outbound destination](./adr/059-external-is-a-reserved-outbound-destination.md) — extends collection-owned authorization to external targets without making the open web a connect-search surface
- [ADR-060: rationale becomes rests-on](./adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-reclassified.md) — applies source-as-subject grammar to design dependencies, reclassifies off-pattern grounds, and gives the global type surface a collection contract
- [ADR-020: theoretical-default link vocabulary additions](./adr/020-theoretical-default-contrasts-mechanism.md) — the `contrasts` and `mechanism` labels and the directional-asymmetry principle under the historical theoretical-default grouping
- [ADR-035: review jobs finalize all-or-nothing with derived artifacts](./adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — established all-or-nothing finalization and derived artifact paths
- [ADR-043: review state separates completion, outcomes, and freshness baselines](./adr/043-review-state-separates-completion-outcomes-and-freshness-baselines.md) — current review vocabulary, schema-v7 state model, and v5 preservation decision

## Collection boundary

- Use `kb/notes/` for beliefs about the design space whose particular system choices are bound.
- Use `kb/reference/` for Commonplace's selections and the current or historical state they produced.
- Use `kb/instructions/` for imperative procedures and operator-facing process details.

Keep these docs self-contained within the shipped surface. A consuming project should be able to read `kb/reference/` without needing links back to the Commonplace source repository or methodology library.
