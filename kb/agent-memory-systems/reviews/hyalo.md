---
description: Rust CLI for Obsidian-compatible markdown vaults with single-pass scanning, ephemeral MessagePack indexes, mutation-safe link operations, and one-command Claude bootstrap
type: agent-memory-system-review
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-05"
---

# Hyalo

Hyalo is a Rust CLI for operating on Obsidian-compatible markdown collections without a running app. It treats a markdown vault as a queryable and mutable filesystem substrate: frontmatter, tags, tasks, sections, links, and backlinks become CLI-visible structures; bulk metadata mutations and link repairs become first-class commands; and agent integration is packaged as a repo-local bootstrap step rather than as a hosted service. The repo includes its own `hyalo-knowledgebase/` with a decision log, backlog, iteration notes, and dogfooding reports, so the tool is being developed against a live markdown corpus rather than only against synthetic fixtures.

**Repository:** https://github.com/ractive/hyalo
**Status:** Active Rust workspace (`0.8.0` in `Cargo.toml`), recent commit on 2026-04-03, substantial e2e test coverage

## Core Ideas

**Markdown vault as operational substrate, not app state.** The project pitch and decision log make the boundary explicit: no vault registry, no daemon, no database-backed control plane, just `--dir` pointing at a directory of `.md` files plus an optional `.hyalo.toml`. The mechanism is real, not rhetorical. `hyalo` does not virtualize the vault behind a service layer; it reads and rewrites the same files the user and other tools can inspect directly.

**Single-pass structural scanning with an explicitly ephemeral derived index.** `scanner/mod.rs` implements multi-visitor file scanning, and `index.rs` turns that into `IndexEntry` records containing properties, tags, sections, tasks, and links. For repeated query loops, `SnapshotIndex` serializes the scanned state to a MessagePack `.hyalo-index`, validates the header against vault settings, patches entries after mutations, and writes snapshots atomically via a temp file rename. This is a clean operational acceleration layer below the source files, not a replacement for them.

**Structural mutation is a first-class capability.** Hyalo is not just a query shell. It offers bulk property/tag updates, task toggling, file moves with planned link rewrites, and `links fix` with a four-stage repair pipeline (case-insensitive exact match, extension mismatch, unique stem match, fuzzy Jaro-Winkler). The implementation pays attention to failure containment: atomic writes, path-within-vault checks, dry-run modes, and explicit handling of site-prefix-based absolute links for docs sites.

**Agent-facing control-plane artifacts are part of the product.** `init --claude` writes `.hyalo.toml`, installs two Claude skills, installs a path-scoped rule, and upserts a managed hint block into `.claude/CLAUDE.md`. The tool output itself also carries policy: a consistent JSON envelope plus optional drill-down hints generated from the current query context, and saved `views` persisted into `.hyalo.toml` for recurring query shapes. Hyalo is therefore not only a file tool; it is a repo-local routing layer for future agent behavior.

**Dogfooding lives in a workshop, not in the CLI's knowledge model.** The checked-in `hyalo-knowledgebase/` shows a disciplined working method: decision records, backlog items, iterations, and dogfooding reports feed the roadmap. That matters because it grounds the product choices in observed use, but the mechanism stays outside the CLI proper. Hyalo helps maintain a workshop; it does not itself provide a theory of promotion from workshop artifacts into a curated semantic library.

## Comparison with Our System

| Dimension | Hyalo | Commonplace |
|---|---|---|
| Primary object | Operational CLI over an existing markdown vault | Knowledge methodology plus KB structure for writing, connecting, validating, and reviewing notes |
| Structure commitment | Frontmatter, tags, sections, tasks, links, views, and snapshot indexes | Note types, claim titles, discriminative descriptions, semantic link phrases, indexes, review bundles |
| Progressive disclosure | Tool-level: hints, saved views, optional snapshot index, section-aware reads | Document-level and control-plane-level: AGENTS routing, note descriptions, curated indexes, semantic links |
| Mutation model | Strong: bulk metadata edits, task mutation, link repair, path-safe move tooling | Lighter: mostly deliberate note authoring with validation and review after the fact |
| Governance | Parser limits, path sandboxing, atomic writes, tests, dogfooding | Structural validation, semantic review, note templates, explicit maturity and linking rules |
| Human/agent coexistence | Very strong for existing Obsidian-style vaults | Very strong for curated KB work, but with more methodology overhead and less drop-in compatibility |

Hyalo is closer to [Napkin](./napkin.md) than to [Thalo](./thalo.md). Like Napkin, it adapts a real markdown vault for agent use instead of inventing a new knowledge language. But it goes further into mutation safety, repo-local agent bootstrap, and bulk operational maintenance than Napkin does. Compared with commonplace, Hyalo is strongest exactly where we are intentionally thinner: operational ergonomics over a broad markdown corpus, not semantic curation of knowledge artifacts.

The systems therefore fit together more naturally than they compete. Hyalo could sit underneath a filesystem-first KB as an operational and control-plane substrate for querying, mutating, and routing work over markdown. Commonplace adds what Hyalo does not try to provide: a theory of note shape, link meaning, knowledge maturation, and review discipline. Hyalo makes markdown collections easier to operate on and easier for agents to navigate procedurally. Commonplace tries to make them better places to think.

## Borrowable Ideas

**One-command agent bootstrap.** `hyalo init --claude` turns a repo into an agent-aware markdown workspace by installing config, skills, rules, and a managed always-loaded hint. For commonplace, this suggests a packaging move: a single setup command that installs our router hints and targeted skills into a repo or workshop. Ready to borrow as a distribution pattern, not as-is content.

**Deterministic drill-down hints in tool output.** Hyalo's hints are concrete next commands, not prose documentation. That would transfer well to our validation and maintenance scripts: a `/validate` or review command that emits the next cheapest follow-up action would lower navigation cost immediately. Ready to borrow now.

**Ephemeral patch-through indexes for bursty maintenance loops.** The snapshot index is attractive precisely because it is scoped as temporary. For commonplace, a throwaway index over note metadata, link graph, and task state could speed review sweeps, maintenance audits, or workshop triage, as long as it is kept clearly below the source-of-truth layer. Needs a concrete use case first.

**Saved views as local query macros.** Persisting recurring query shapes into `.hyalo.toml` is a lightweight alternative to baking every maintenance slice into a new script. For commonplace, this could be useful for recurring review selections or workshop slices. Needs a use case first.

## Curiosity Pass

**"Safe move rewrites all wikilinks" is broader than the implementation.** The README and skill template say `mv` rewrites all wikilinks, but `link_rewrite.rs` and the e2e tests intentionally leave bare wikilinks like `[[b]]` untouched. That is a coherent design for directory moves where the basename stays stable, but it means the safety property depends on conventions and future shortest-path resolution rather than on universal rewrite coverage. The mechanism is narrower than the headline.

**The snapshot index is useful because it is disposable, not because it is authoritative.** The property is speed for repeated queries. The mechanism genuinely transforms a vault scan into a structured operational cache. But the dogfooding report already records an index-versus-disk orphan discrepancy, which is exactly the failure mode of an authoritative derived map drifting from source truth. This is a strong confirmation of our [stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) warning: the index should stay explicitly short-lived.

**`init --claude` is control-plane codification, not learning.** It installs files that shape future agent behavior. That is useful, and it is a real mechanism. But it does not learn from traces or improve from observed outcomes; it writes routing policy into repo-local scaffolding. The benefit is packaging and discipline, not adaptation.

**Hints are one of the genuinely strongest ideas here because they alter the agent's action surface directly.** The simpler alternative is a help page or README section. Hyalo instead computes next-step commands from the actual result set and places them in the output channel the model is already consuming. That is a small mechanism with disproportionate leverage for agent usability.

## What to Watch

- Whether the bare-wikilink rename gap gets fixed, or the docs get narrowed to match the actual safety envelope
- Whether snapshot-index correctness catches up fully to the performance story, especially for link-graph-derived metrics like orphans
- Whether the Claude-specific bootstrap becomes a broader pattern for repo-local agent/tool integration across harnesses
- Whether Hyalo stays an operational layer under markdown vaults or starts to grow note-quality, semantic-governance, or promotion logic

---

Relevant Notes:

- [files-not-database](../../notes/files-not-database.md) — convergence: Hyalo is a strong filesystem-first operational tool, keeping the primary substrate in readable files rather than shifting knowledge work into a service boundary
- [Instruction specificity should match loading frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — exemplifies: `init --claude` installs a slim always-loaded hint plus on-demand skill bodies, rhyming with our loading hierarchy even though the repo-local bootstrap is a narrower mechanism
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: Hyalo implements tool-level guidance and pointer-like affordances through hints, views, and section-aware reads instead of relying mainly on document-level pointers
- [Stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) — warns: Hyalo's dogfooding report shows exactly why a derived index must remain visibly temporary and subordinate to source files
- [Deterministic validation should be a script](../../notes/deterministic-validation-should-be-a-script.md) — contrasts: Hyalo has strong parser and write-path safeguards, but it does not provide a content-quality validation layer analogous to our review and validation stack
- [A functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — sharpens: the bundled `hyalo-knowledgebase/` is a real workshop, but Hyalo itself does not yet provide the library-side promotion model
- [Napkin](./napkin.md) — sibling: both adapt Obsidian-compatible vaults for agents, but Hyalo goes further into mutation safety and repo-local agent bootstrap while Napkin goes further into retrieval ergonomics
