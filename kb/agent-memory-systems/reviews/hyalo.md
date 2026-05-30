---
description: "Hyalo review: Rust CLI control plane for markdown/Obsidian vaults with scanning, indexes, link repair, saved views, hints, schemas, and Claude skills"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# Hyalo

Hyalo is Ractive's Rust CLI for operating on markdown knowledgebases and Obsidian-compatible vaults. It does not create a separate memory service; it makes existing markdown, frontmatter, tags, links, tasks, schemas, and config files queryable and safely mutable from a terminal or agent loop. The interesting design is the control plane around plain files: live scanning and optional snapshot indexes for retrieval, guarded mutation commands for frontmatter and moves, saved views and hints for repeatable navigation, and `hyalo init --claude` artifacts that instruct Claude Code to use Hyalo instead of raw file tools.

**Repository:** https://github.com/ractive/hyalo

**Reviewed commit:** [567a2399120f64f084ef17dc5ba7ed4cc106c466](https://github.com/ractive/hyalo/commit/567a2399120f64f084ef17dc5ba7ed4cc106c466)

**Last checked:** 2026-05-16

## Core Ideas

**Plain markdown remains the canonical store.** The README frames Hyalo as a tool for folders of `.md` files with YAML frontmatter, `[[wikilinks]]`, markdown links, tags, and tasks, explicitly saying it works with the user's existing structure rather than defining a new one ([README.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/README.md)). The storage substrate for knowledge artifacts is therefore the vault directory itself. The `.hyalo.toml` file adds configuration, saved views, schemas, rule settings, and agent integration state; those are system-definition artifacts because the CLI and generated agent instructions consume them with configuration, validation, and routing force ([views.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/views.rs), [types.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/types.rs)).

**Scanning is a shared parser pipeline, not per-command grep.** `ScannedIndex::build` takes discovered markdown files and runs frontmatter, tag, outline, task, link, and optional BM25-token visitors into stable `IndexEntry` objects ([index.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-core/src/index.rs)). The scanner validates and caps frontmatter, skips oversized files, uses SIMD newline splitting, and lets visitors opt out of body reads when only metadata is needed ([scanner/mod.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-core/src/scanner/mod.rs)). This gives Hyalo a symbolic, inspectable representation of the vault without moving source of truth away from markdown.

**The snapshot index is an explicit derived cache.** `hyalo create-index` builds `<dir>/.hyalo-index` as a MessagePack snapshot containing entries, the link graph, and a persisted BM25 inverted index when tokenization is enabled ([create_index.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/create_index.rs)). Snapshot loading rejects unsafe paths, oversized graphs, bad BM25 doc ids, and incompatible schemas, then falls back to live scanning rather than trusting a bad cache ([index.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-core/src/index.rs)). Mutations with `--index` patch affected index entries and link-graph state in place, but the README and skill template still treat the index as a session cache to create, use, and drop; the canonical artifacts remain markdown plus config ([README.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/README.md), [skill-hyalo.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/templates/skill-hyalo.md)).

**Retrieval combines filters, BM25, graph fields, views, and jq.** `find` runs metadata filters over pre-scanned entries, then performs BM25 scoring only for matching candidates when a body query is present; it can include links, backlinks, tasks, sections, typed properties, title-derived fields, orphan/dead-end checks, and broken-link signals ([find/mod.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/find/mod.rs)). Saved views serialize `FindFilters` into `.hyalo.toml` and can be recalled or extended by later commands ([views.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/views.rs)). The output pipeline wraps command JSON in a consistent envelope, adds drill-down hints, and lets `--jq` operate on that envelope, making Hyalo suitable for both humans and scripted agent loops ([output_pipeline.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/output_pipeline.rs)).

**Mutation commands encode vault invariants.** Frontmatter mutation commands patch in-memory snapshot entries after writes ([mutation.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/mutation.rs)). `hyalo mv` plans the file move plus inbound and outbound link rewrites, skips non-vault targets, preserves fragments, handles case-insensitive and short-form wikilinks, and checks mtimes before writing ([mv.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/mv.rs), [link_rewrite.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-core/src/link_rewrite.rs)). `links fix` separates detection from repair, using case, extension, shortest-path, and fuzzy strategies before applying rewrite plans ([link_fix.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-core/src/link_fix.rs)). These commands are system-definition surfaces because they enforce how agents may change durable vault artifacts.

**Validation is both schema-driven and markdown-aware.** `hyalo lint` validates frontmatter against `.hyalo.toml` schemas, warns on missing `type`/`tags` and undeclared properties, can promote some warnings under `--strict`, and can auto-fix defaults, enum typos, dates, and inferred types ([lint.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/lint.rs)). The separate `hyalo-mdlint` crate supplies markdown body rules, while the local knowledgebase docs explain schema merging, property types, lint output, and fix modes ([schema-and-lint.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/hyalo-knowledgebase/docs/schema-and-lint.md), [hyalo-mdlint](https://github.com/ractive/hyalo/tree/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-mdlint)). This makes schema and lint config a stronger behavior-shaping layer than ordinary notes: it can block or repair invalid metadata before agents rely on it.

**Agent bootstrap artifacts are first-class generated instructions.** `hyalo init --claude` writes `.hyalo.toml`, two Claude skills, a scoped rule, and a managed `CLAUDE.md` section; `deinit` removes them ([init.rs](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/src/commands/init.rs)). The generated `hyalo` skill tells Claude to use the CLI for structured markdown operations, and the `hyalo-tidy` skill defines a five-phase consolidation workflow that creates an index, saves recurring views, checks git and optional Claude memory signal, runs lint/link/orphan/status queries, applies conservative fixes, then reports a dashboard ([skill-hyalo.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/templates/skill-hyalo.md), [skill-hyalo-tidy.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/templates/skill-hyalo-tidy.md), [rule-knowledgebase.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/crates/hyalo-cli/templates/rule-knowledgebase.md)). These generated files are system-definition artifacts with direct instruction authority over later agent behavior.

**The project dogfoods Hyalo on its own workshop layer.** The repository contains `hyalo-knowledgebase/` with iteration plans, backlog items, dogfood reports, research, docs, and a promotion plan; `CLAUDE.md` instructs agents to use Hyalo for that directory and records iteration-file rules ([CLAUDE.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/CLAUDE.md), [hyalo-knowledgebase](https://github.com/ractive/hyalo/tree/567a2399120f64f084ef17dc5ba7ed4cc106c466/hyalo-knowledgebase)). Dogfood reports record concrete CLI runs and discovered issues, and iteration notes link fixes back into implementation work ([dogfood-v0150-iter132.md](https://github.com/ractive/hyalo/blob/567a2399120f64f084ef17dc5ba7ed4cc106c466/hyalo-knowledgebase/dogfood-results/dogfood-v0150-iter132.md)). That is evidence of an operational workshop practice, but it is not an implemented trace-to-memory learning loop.

## Comparison with Our System

| Dimension | Hyalo | Commonplace |
|---|---|---|
| Primary substrate | Existing markdown/Obsidian vault plus `.hyalo.toml` | Git-tracked KB collections with type specs, indexes, reviews, instructions, and commands |
| Retrieval surface | `hyalo find`, BM25, filters, saved views, hints, jq, optional snapshot index | `rg`, authored indexes, generated indexes, note descriptions, semantic links, skills |
| Mutation surface | CLI commands for frontmatter, tags, tasks, moves, link repair, auto-linking | File edits plus `commonplace-*` commands for validation, indexing, note operations, and review workflows |
| Source of truth | Markdown files and config; `.hyalo-index` is derived cache | Markdown files and schemas; generated indexes and reports are derived |
| Agent bootstrap | Generated Claude skills/rules and managed `CLAUDE.md` section | Repo-level `AGENTS.md`, installed `cp-skill-*` workflows, type specs, commands |
| Validation authority | `.hyalo.toml` schemas, lint rules, markdown lint, strict/fix modes | Type specs, schemas, `commonplace-validate`, review and fix systems |
| Learning loop | Manual/dogfood workshop feedback into iterations and code changes | Manual/agent review workflows with curated promotion into notes, instructions, code, schemas |
| Trace-derived status | Not supported by implementation | Studied in reviews; core KB is curated artifact workflow |

Hyalo and commonplace share the same core bias: durable memory should stay in inspectable files, and agents should operate through structured, repeatable tools instead of ad hoc raw edits. Hyalo pushes harder on the CLI as a universal control plane over arbitrary markdown vaults. Commonplace pushes harder on collection-local contracts, semantic link vocabulary, type specs, and methodology as the substance of the KB.

The most important architectural split in Hyalo is clean: source markdown and `.hyalo.toml` are canonical; `.hyalo-index` is a derived runtime cache; command output and hints are tool surfaces; generated skills/rules are behavior-shaping control-plane artifacts. That split matches commonplace's source-vs-generated discipline, but Hyalo packages it for existing vaults rather than a single methodology repo.

Hyalo is weaker as an agent-memory system in the narrow sense because it does not implement automatic distillation, evaluation of retained memories by downstream task effects, or promotion from traces into durable rules. Its learning happens through human/agent dogfooding artifacts and ordinary software iteration. That is still valuable: it shows how much agent memory infrastructure can be achieved by constraining how agents search, mutate, validate, and maintain ordinary markdown.

**Read-back:** both — agents query vaults through Hyalo commands, while generated Claude rules and managed instructions can steer later sessions without a query.

## Borrowable Ideas

**A reusable markdown-vault control plane.** Ready to borrow as a design reference, not necessarily as code. Commonplace already has domain-specific commands; Hyalo shows what a generic frontmatter/link/task/schema CLI looks like when tuned for agent use.

**Session-scoped binary snapshot indexes.** Worth borrowing if commonplace starts running many repeated structural queries over the same large source or workshop corpus. The key discipline is the one Hyalo keeps: the index accelerates reads and can be patched during a session, but it is never the canonical artifact.

**Saved views as named operational queries.** Ready now for review and maintenance workflows. Hyalo's views turn repeated filter sets into config-backed names, which makes agent procedures less brittle than copy-pasting long query strings.

**Hints as an output-level navigation contract.** Ready to borrow for `commonplace-*` commands. Hyalo generates concrete next commands from command results, so the tool itself teaches progressive disclosure and follow-up action.

**Generated agent bootstrap bundles.** Useful if commonplace wants a promoted install story for consuming projects. `init --claude` writes skills, rules, and a managed instruction section idempotently; the analogue would be a commonplace project bootstrap that installs commands, skills, and scoped instructions without requiring users to hand-copy agent guidance.

**Move/link repair as a mutation primitive.** Ready to borrow conceptually. Commonplace already cares about link integrity, but Hyalo's `mv` and `links fix` make link preservation the default mutation path rather than a validation afterthought.

## Curiosity Pass

Hyalo's best memory-system contribution is not storage novelty. It is operational authority over a familiar substrate. A future agent behaves differently because the generated skill says "use Hyalo," the CLI prevents unsafe moves, the schema/lint layer constrains metadata, and saved views/hints steer navigation.

The snapshot index is easy to overstate. It contains rich derived state, including a link graph and BM25 index, but the implementation treats it as disposable and validates it defensively. That makes it a runtime surface, not a memory store.

The dogfood corpus is a real workshop layer. Iteration files, backlog notes, and dogfood reports are knowledge artifacts when read as evidence, and they become system-definition artifacts only when promoted into code, CLI behavior, schema, rules, or generated skills. The repository shows that promotion socially and operationally, but does not automate it from traces.

The generated `hyalo-tidy` skill is stronger than a command reference because it encodes an operational procedure: orient, index, gather signal, detect issues, consolidate, and report. That is a behavior-shaping artifact even though it is prose.

Trace-derived status is not supported. Hyalo can inspect optional Claude memory files during tidy, and the project has dogfood reports from agent-assisted work, but there is no implemented loop that consumes agent traces or conversations and distills them into durable notes, rules, schemas, prompts, or learned state.

## What to Watch

- Whether Hyalo adds a first-class trace/session ingestion path that turns agent runs into durable vault artifacts.
- Whether `hyalo-tidy` remains generated prose or gains a command-backed planner that records actions, evidence, and promotion decisions.
- Whether saved views grow lifecycle metadata, owners, or validation so they can be governed as stronger system-definition artifacts.
- Whether the snapshot index gets stronger source fingerprints or content hashes for long-lived automation sessions.
- Whether generic Hyalo schemas become expressive enough to model commonplace-style collection contracts and semantic link rules.

## Bottom Line

Hyalo is an operational CLI and agent control plane for markdown knowledgebases. It turns plain vault files into a structured, validated, queryable, and safely mutable memory substrate without replacing the files. For commonplace, the strongest lessons are the explicit source-vs-cache boundary, agent-facing mutation primitives, saved operational views, output hints, and generated bootstrap artifacts that carry real behavioral authority.

Relevant Notes:

- [Napkin](./napkin.md) - compares-with: both target agent operation over markdown vaults, but Hyalo emphasizes mutation/link/schema control while Napkin emphasizes progressive retrieval and distillation.
- [The wikiwiki principle: lowest-friction capture, then progressive refinement in place](../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) - exemplifies: Hyalo keeps capture and refinement in the user's existing markdown vault.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: vault markdown and dogfood notes advise later agents until promoted into stronger surfaces.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: `.hyalo.toml`, schemas, lint rules, generated skills, rules, and managed instructions bind later agent/tool behavior.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Hyalo cleanly separates storage substrate, representational form, lineage, and behavioral authority across markdown, config, indexes, CLI outputs, and generated agent artifacts.
