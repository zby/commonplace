---
description: "Thalo review: plain-text knowledge language with schemas, validation, LSP tooling, query/actualize workflows, and synthesis PR automation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# Thalo

> Replaced 2026-06-05. See [Thalo](./thalo.md) for the current review.

Thalo, from `rejot-dev/thalo`, is a plain-text language and TypeScript toolchain for structured personal knowledge. At the reviewed commit it includes a Tree-sitter grammar, core parser and workspace model, validation rules, CLI, LSP, VS Code extension, Prettier plugin, Git merge driver, GitHub Action for syntheses, and an agent-facing skill. The system is closer to a file-native typed knowledge format than to a runtime memory database: retained knowledge stays in `.thalo` files or fenced `thalo` blocks in Markdown, while tools parse, validate, query, format, and actualize those files.

**Repository:** https://github.com/rejot-dev/thalo

**Reviewed commit:** [cdb9aae983e6bc0b75eff1606bc99b088c3aebff](https://github.com/rejot-dev/thalo/commit/cdb9aae983e6bc0b75eff1606bc99b088c3aebff)

**Last checked:** 2026-06-02

## Core Ideas

**The central artifact is a typed text entry, not a memory row.** A Thalo entry carries a timestamp, directive, entity, title, optional link id, tags, metadata, and sectioned content. `define-entity` and `alter-entity` entries define the local schema; ordinary `create` and `update` entries are checked against those schemas. The repo ships default entities for journal, opinion, reference, lore, and self, but the code treats entity shape as user-defined text, not as a fixed app database model ([README.md](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/README.md), [apps/thalo-cli/src/commands/init.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/thalo-cli/src/commands/init.ts), [packages/thalo/src/schema/registry.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/schema/registry.ts)).

**A compiler-style pipeline gives knowledge files hard feedback.** The parser supports pure `.thalo` files and fenced `thalo` blocks in Markdown, then the semantic analyzer builds link indexes and schema entries. The checker runs syntax diagnostics plus semantic rules for unknown entities, required fields, field types, required sections, unresolved links, duplicate links, schema evolution errors, timestamp/order issues, synthesis definitions, and actualization entries ([packages/thalo/src/parser.shared.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/parser.shared.ts), [packages/thalo/src/semantic/analyzer.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/semantic/analyzer.ts), [packages/thalo/src/checker/check.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/checker/check.ts), [packages/thalo/src/checker/rules/rules.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/checker/rules/rules.ts)). This is the main trust mechanism: an agent can write text, but it gets deterministic feedback from a language toolchain.

**Context efficiency is query and delta based.** `thalo query` filters entries by entity, tag, link, metadata equality, optional checkpoint, and optional limit; raw source text is only included for the raw output path. `thalo actualize` finds `define-synthesis` entries, resolves their source queries, uses git or timestamp checkpoints to select changed matching entries, and prints the synthesis prompt plus only the changed raw entries ([packages/thalo/src/commands/query.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/commands/query.ts), [packages/thalo/src/services/query.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/query.ts), [packages/thalo/src/commands/actualize.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/commands/actualize.ts), [packages/thalo/src/services/change-tracker/git-tracker.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/change-tracker/git-tracker.ts)). There is no token budget, embedding reranker, or progressive disclosure layer; the bounded unit is the user's query plus checkpoint discipline.

**Syntheses are prompt-bearing queries with explicit checkpoints.** A `define-synthesis` stores source queries and a `# Prompt` section. An `actualize-synthesis` entry points back to that synthesis and records a checkpoint. Actualization does not call a model inside the core CLI; it emits the prompt, matching changed entries, and instructions for the caller to update the surrounding Markdown and append the checkpoint entry ([packages/thalo/src/services/synthesis.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/synthesis.ts), [apps/thalo-cli/src/commands/actualize.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/thalo-cli/src/commands/actualize.ts)). This is intentionally low-authority: Thalo selects and packages context, while the user or host command owns generation.

**The GitHub Action turns actualization into an activation workflow.** `thalo-action` loads the workspace, runs `runActualize()`, filters syntheses with pending entries, passes each pending synthesis as JSON on stdin to a user-supplied command, commits any resulting file changes, and creates or updates a PR ([packages/thalo-action/src/action.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-action/src/action.ts), [packages/thalo-action/action.yml](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-action/action.yml), [packages/thalo-action/README.md](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-action/README.md)). The action is the strongest read-back path because selected knowledge enters a later synthesis command without a human manually copying query output.

**Adoption is editor and git native.** The LSP loads `.thalo` and Markdown files, keeps a workspace model, publishes diagnostics, and provides definition, references, hover, completion, and semantic tokens. The VS Code extension starts `thalo lsp` and delegates formatting to the CLI; the merge driver parses three versions and merges entries by identity instead of relying only on text hunks ([packages/thalo-lsp/src/server.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-lsp/src/server.ts), [packages/thalo-vscode/src/mod.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-vscode/src/mod.ts), [packages/thalo/src/merge/driver.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/merge/driver.ts), [apps/thalo-cli/src/commands/setup-merge-driver.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/thalo-cli/src/commands/setup-merge-driver.ts)).

## Artifact analysis

- **Storage substrate:** `files` — `.thalo` files and Markdown files with fenced `thalo` blocks, normally in git
- **Representational form:** `prose` `symbolic` — entry bodies and synthesis prompts are prose; timestamps, directives, entity names, metadata fields, links, tags, sections, synthesis source queries, checker rules, and actualize checkpoints are symbolic
- **Lineage:** `authored` `imported` — entries, schemas, syntheses, checker rules, and tool surfaces are authored by humans, agents, or package maintainers; scripts and external synthesis commands can import or generate corpus content, but this review does not find trace-derived learning
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — instance entries are knowledge; synthesis prompts and skills instruct; checker/LSP/action workflows enforce and validate; queries, links, indexes, actualization payloads, and workspace services route retained entries into consumers

**Thalo knowledge documents.** Storage substrate: `.thalo` files and Markdown files with fenced `thalo` blocks, normally in git. Representational form: mixed prose and symbolic structure. Entry bodies are prose; timestamps, directives, entity names, metadata fields, links, tags, sections, synthesis source queries, and actualize checkpoints are symbolic. Lineage: authored by humans or agents, imported by scripts, or generated by an external synthesis command; the code does not require source citations or trace provenance. Behavioral authority: instance entries are knowledge artifacts when queried, read, or passed into syntheses; schema entries, synthesis entries, and actualize entries also have system-definition authority because they define validation, selection, prompt assembly, and checkpoint behavior.

**Schemas and validation rules.** Storage substrate: user-authored `define-entity` / `alter-entity` entries plus checker source code. Representational form: symbolic types, section contracts, rule declarations, and diagnostic emitters, with prose descriptions attached to fields and sections. Lineage: schemas are authored inside the knowledge base and resolved by timestamp-ordered definitions and alterations; validation rules are authored package code. Behavioral authority: system-definition artifacts with enforcement authority in `thalo check`, LSP diagnostics, GitHub workflows, and any agent workflow that treats diagnostics as a gate.

**Semantic model, link index, and workspace services.** Storage substrate: in-memory `Workspace`, `SemanticModel`, schema registry, link index, and source maps rebuilt from files. Representational form: symbolic ASTs, maps, indexes, and file/position records. Lineage: derived from current source text and parser version; changing files, grammar, parser, or semantic analyzer invalidates them. Behavioral authority: navigation, lookup, references, query execution, hover, completion, and diagnostics. These derived artifacts do not preserve independent truth; they are compiled views of the text corpus.

**Actualization outputs and action payloads.** Storage substrate: CLI stdout, action stdin JSON, generated file changes, PR branches, commits, and `actualize-synthesis` checkpoint entries. Representational form: prose prompts plus symbolic JSON, checkpoint markers, source query strings, entry metadata, and raw entry text. Lineage: derived from synthesis definitions, matching source entries, git/timestamp change trackers, and an external generation command. Behavioral authority: activation and routing authority for the synthesis command; generated synthesis prose becomes a knowledge artifact only after the command writes it and the PR is reviewed or merged.

**Editor, formatter, skill, and merge tooling.** Storage substrate: LSP server code, VS Code extension code, Prettier printer, CLI commands, Git merge-driver config, and `skills/thalo/SKILL.md`. Representational form: symbolic executable code plus prose instructions. Lineage: authored toolchain surfaces around the same language. Behavioral authority: system-definition artifacts for authoring ergonomics, formatting, conflict resolution, and agent guidance. The skill is particularly close to an always-loaded local operating guide, but in this repo it ships as a file rather than as an automatic runtime injector.

Promotion path: Thalo has a strong promotion path from free-form notes into typed entries, schema-checked fields, queryable syntheses, and PR-reviewed generated output. It does not implement promotion from trace-mined observations into stronger instructions, validators, or skills.

## Comparison with Our System

| Dimension | Thalo | Commonplace |
|---|---|---|
| Primary purpose | Plain-text language and tools for structured personal knowledge | Agent-operated methodology KB and framework |
| Canonical retained unit | Timestamped typed entry in `.thalo` or Markdown fence | Typed Markdown artifact under a collection contract |
| Type surface | User-defined entity schemas inside the corpus | Type-spec docs plus JSON Schema and collection contracts |
| Validation | Language checker rules and LSP diagnostics | `commonplace-validate`, type schemas, link checks, semantic review gates |
| Read-back | CLI query, actualize, scripting API, LSP, GitHub Action | `rg`, indexes, links, skills, validation/review commands, loaded instructions |
| Generated synthesis | Query-plus-prompt actualization, optional PR automation | Workshop/review/source artifacts with explicit promotion discipline |

Thalo and Commonplace share the strongest design instinct: keep knowledge in normal text files and make the surrounding tooling precise enough that agents can get feedback. Thalo pushes further toward programming-language ergonomics: Tree-sitter grammar, AST, semantic model, LSP, formatter, merge driver, and a dedicated query language. Commonplace pushes further toward knowledge governance: collection-local contracts, cross-note link vocabulary, source snapshots, replacement archives, review gates, and artifact status.

The most important divergence is where schema lives. Thalo lets users define domain entities inside the knowledge corpus itself, so schema evolution is part of the same plain-text history as entries. Commonplace defines artifact types outside each artifact as type-spec docs and schemas. Thalo's approach is more locally customizable; Commonplace's approach is better for cross-collection methodology where the type system itself is a shared operating contract.

**Read-back:** `both` — Ordinary Thalo use is pull through `query`, LSP navigation, scripting APIs, and manual `actualize`; `thalo-action` adds engineered push activation by detecting pending syntheses from changed entries, passing the selected source entries and prompt to a user command before generation, and opening a PR

### Borrowable Ideas

**A real grammar for knowledge fragments.** Needs a concrete use case before adoption. Commonplace should not replace Markdown with a custom language broadly, but small fenced grammars for high-value substructures could make validation and editor help much stronger than prose conventions.

**Entity schemas authored inside the corpus.** Worth borrowing selectively. Commonplace's type specs are already file-native, but Thalo shows how domain-local schemas can live beside the entries they constrain. This could help workshop-specific structured logs or project-local source inventories.

**Actualization as query plus checkpoint plus prompt.** Ready as a pattern. Commonplace review sweeps and recurring synthesis tasks could benefit from explicit checkpoint records that say which source artifact revision a generated output covers.

**Language-server feedback for KB artifacts.** Needs product investment, not immediate implementation. Thalo's LSP demonstrates the upside of diagnostics, definitions, references, and completions at edit time. Commonplace currently gets this feedback later through commands and agent review.

**Semantic merge for structured knowledge entries.** Needs a structured-entry surface first. Commonplace relies on Git text merge, which is adequate for Markdown notes but weak for append-heavy structured logs. If Commonplace adds dense event or trace files, Thalo's entry-identity merge model becomes relevant.

**Keep generation out of the core language runtime.** Ready now. Thalo's core actualize command packages context but leaves model invocation to the caller. Commonplace should preserve the same boundary for generated notes and reviews: deterministic selection first, generation second, review/promotion third.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Read-back placement

**Read-back:** `both` — Thalo uses both pull and push over retained memory. Pull paths include `thalo query`, scripting API queries, LSP definition/reference/navigation, manual `thalo actualize`, and direct reading of text files. Push exists through `thalo-action`: a repository event or workflow run invokes actualization, selects pending syntheses, and feeds accumulated Thalo entries plus the synthesis prompt into a user command before that command generates or updates content.

**Read-back signal:** `identifier` — the engineered push path selects synthesis definitions, source entries, checkpoints, changed files, tags, links, entity names, metadata fields, and entry identities through assigned symbolic identifiers rather than lexical, embedding, or LLM relevance.

**Faithfulness tested:** `no` — the review finds tests for parsing, checking, queries, actualization, LSP behavior, formatting, and merge behavior, but no with/without read-back behavioral ablation for downstream synthesis quality.

**Targeting and signal.** Pull triggers are user or agent queries, link/tag navigation, editor cursor position, or a manually chosen synthesis link. The engineered push trigger is the GitHub workflow/action run, usually after changes to `.thalo` or Markdown files. Its targeting is `instance`: `runActualize()` narrows to selected synthesis link ids when provided, finds each synthesis definition, then selects entries for that synthesis's declared source queries and checkpoint. The signal is `identifier`: entity names, tags, link ids, metadata fields, synthesis link ids, git or timestamp checkpoints, changed-file detection, entry identity comparison, and query matching are all assigned symbolic fields rather than embedding, keyword, or LLM relevance judgments.

**Injection point.** `thalo-action` supplies the synthesis JSON before the user command runs, so the selected memory can shape the generated output. CLI query and manual actualize also happen before the caller's next action, but the caller intentionally requested them.

**Selection, scope, and complexity.** Query scope is entity plus `where` conditions over tags, links, and metadata; CLI query can apply a result limit. Actualize adds per-synthesis source queries, optional target link filtering, and checkpoint-based deltas. Complexity is bounded by raw matching entries and the synthesis prompt. There is no token budget, semantic compression, or multi-hop retrieval plan, so large matching deltas can still overfill a downstream LLM context; actual context dilution is not verified from code.

**Authority at consumption.** Query results are advisory knowledge artifacts. LSP diagnostics and checker results are stronger system-definition artifacts when the workflow treats errors as blocking. Action payloads have activation authority over a synthesis command, but the generated result should remain reviewable because Thalo itself does not verify model faithfulness; effective authority over the downstream command is host-policy-dependent and not verified from code.

**Faithfulness.** The code tests parsing, checking, queries, actualization, LSP behavior, formatting, and merge behavior in package tests, but I did not find a with/without read-back behavioral ablation proving that syntheses improve downstream decisions. The `push-activation` tag is for the engineered activation path, not for measured generation quality.

**Other consumers.** Human users consume files, diagnostics, query output, LSP features, formatted documents, merge results, generated PRs, and docs. Agents consume the `skills/thalo` instructions, CLI output, scripting APIs, action JSON, and the same file corpus.

## Curiosity Pass

**Thalo is a knowledge language first and an agent memory system second.** Its agent-memory relevance comes from text durability, schema feedback, queryable entries, and activation tooling. It does not try to be a runtime episodic memory layer.

**The "just enough structure" claim is backed by unusually serious language infrastructure.** Tree-sitter, AST extraction, semantic models, LSP, Prettier, merge driver, and 30-ish checker rules are a lot of machinery around a small syntax. That is the point: the format stays plain-text while the tooling acts like a compiler.

**Actualization is deliberately incomplete.** It does not decide what the synthesis should say. It selects changed entries and emits a prompt plus instructions. That makes it less magical and easier to govern than systems that silently rewrite memory.

**Git history is used as a change oracle, not as trace-derived learning.** The git tracker detects which matching entries changed since a checkpoint; it does not mine commits, tool logs, sessions, or agent trajectories into durable rules or skills. This review therefore does not mark Thalo `trace-derived`.

**The action has a sharp safety tradeoff.** It is useful that generated synthesis updates arrive as PRs. It is also notable that the action commits whatever the user command changed after running `git add .`, so repository workflows need path scoping and review discipline around the command.

## What to Watch

- Whether actualization gains token budgets, chunking, or progressive disclosure for large changed-entry sets; that would make Thalo's context-efficiency story stronger.
- Whether generated syntheses gain built-in citation or source-span requirements; that would raise trust without making model generation part of the core runtime.
- Whether the GitHub Action narrows staging to changed synthesis files instead of `git add .`; that would reduce accidental authority spillover from user commands.
- Whether entity schema evolution gets compatibility checks; that would make long-lived `.thalo` corpora safer as user-defined schemas change.
- Whether agent workflows start using `skills/thalo` plus `thalo check` as an enforced loop; that would make Thalo a stronger example of agent-facing typed memory rather than just human-friendly tooling.

## Bottom Line

Thalo is a strong example of codifying personal knowledge into a small language with compiler-grade feedback. Its best lesson for Commonplace is not the syntax itself, but the design posture: make structured knowledge editable as text, then add deterministic parser, schema, query, LSP, merge, and actualization surfaces so agents get fast feedback before generated knowledge is promoted. It warrants `push-activation` for the synthesis action, but not `trace-derived` at this commit.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Thalo needs separate treatment for entries, schemas, indexes, checker rules, action payloads, LSP surfaces, and generated syntheses.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Thalo's stored entries affect behavior only through query, actualize, LSP, action, or direct reading paths.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: entity schemas, checker rules, query semantics, actualization checkpoints, action workflows, and skills constrain future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: instance entries, generated syntheses, query output, and source references mostly serve as evidence or context.
- [Readable artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) - exemplifies: Thalo keeps knowledge and policy-like structure readable, reviewable, and versionable rather than moving them into opaque weights.
- [Underspecification and indeterminism complicate programming for LLMs](../../notes/underspecification-and-indeterminism-complicate-programming-for.md) - exemplifies: Thalo applies programming-language feedback, validation, and typing practices to knowledge artifacts intended for human and LLM collaboration.
