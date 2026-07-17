---
description: "Thalo review: structured plain-text knowledge language with schemas, validation, git-aware synthesis actualization, LSP tooling, and PR automation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
---

# Thalo

Thalo, from `rejot-dev/thalo`, is a structured plain-text format and toolchain for personal knowledge bases. At the reviewed commit it provides a Tree-sitter grammar, TypeScript parser/model/checker library, CLI, LSP, VS Code extension, Prettier plugin, semantic merge driver, GitHub Action, and a bundled agent skill. Its memory model is "files in git with typed entries, links, tags, and syntheses," not an autonomous long-term-memory service.

**Repository:** https://github.com/rejot-dev/thalo

**Reviewed commit:** [cdb9aae983e6bc0b75eff1606bc99b088c3aebff](https://github.com/rejot-dev/thalo/commit/cdb9aae983e6bc0b75eff1606bc99b088c3aebff)

**Last checked:** 2026-06-05

## Core Ideas

**Thalo turns personal notes into typed plain-text records.** The README frames Thalo as "just enough" structure for tools and AI while remaining readable, editable, and version-controlled by humans; entries carry timestamps, directives, entity names, titles, optional stable `^links`, `#tags`, typed metadata, and section bodies ([README.md](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/README.md), [packages/grammar/grammar.js](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/grammar/grammar.js)).

**The central feedback loop is validation, not hidden retrieval.** `thalo check` loads `.thalo` and Markdown files into a workspace, collects syntax errors, builds a workspace index, and runs rule visitors for entity existence, required fields and sections, field types, duplicate links, unresolved links, synthesis shape, actualization checkpoints, and related constraints ([packages/thalo/src/checker/check.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/checker/check.ts), [packages/thalo/src/checker/rules/rules.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/checker/rules/rules.ts), [apps/thalo-cli/src/commands/check.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/thalo-cli/src/commands/check.ts)). This gives agents a tight authoring loop: write plain text, validate it, fix diagnostics.

**Context efficiency comes from symbolic selection and incremental change tracking.** Thalo does not embed everything by default. Queries filter by entity, field equality, tags, and links; `actualize` finds synthesis definitions, applies their source queries, and emits only entries changed since the last checkpoint ([packages/thalo/src/services/query.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/query.ts), [packages/thalo/src/services/synthesis.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/synthesis.ts), [packages/thalo/src/commands/actualize.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/commands/actualize.ts)). The Git tracker detects in-place edits and renames by comparing parsed entries across commits; the timestamp fallback only detects newer entries ([packages/thalo/src/services/change-tracker/git-tracker.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/change-tracker/git-tracker.ts), [packages/thalo/src/services/change-tracker/timestamp-tracker.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/change-tracker/timestamp-tracker.ts)).

**Syntheses are prompt packages, not built-in model calls.** A `define-synthesis` entry stores source queries plus a prompt. The CLI prints the prompt, raw changed source entries, and instructions for appending an `actualize-synthesis` checkpoint; it does not generate or insert the synthesized prose itself ([apps/thalo-cli/src/commands/actualize.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/thalo-cli/src/commands/actualize.ts)). The GitHub Action adds automation by passing that synthesis JSON to a user-supplied command, committing whatever that command changes, and opening or updating a PR ([packages/thalo-action/src/action.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-action/src/action.ts), [packages/thalo-action/README.md](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-action/README.md)).

**Adoption is editor/git-native.** The LSP scans `.thalo` and Markdown files, keeps a workspace model, publishes diagnostics, and provides hover, completion, definition, references, and semantic tokens ([packages/thalo-lsp/src/server.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-lsp/src/server.ts)). The merge driver parses base/ours/theirs as Thalo ASTs and merges by entry identity before emitting conflicts ([packages/thalo/src/merge/driver.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/merge/driver.ts)). The bundled skill tells agents how to create entries, define entities, validate, format, and actualize Thalo projects ([skills/thalo/SKILL.md](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/skills/thalo/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `files` — The behavior-shaping memory is stored as `.thalo` files and Thalo blocks in Markdown, typically under git. Runtime workspace indexes, LSP state, and parsed ASTs are in-memory access structures; checkpoints are recorded back into `actualize-synthesis` entries rather than a database ([packages/thalo/src/vfs/loader.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/vfs/loader.ts), [apps/docs/content/docs/change-tracking.mdx](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/docs/content/docs/change-tracking.mdx)).
- **Representational form:** `prose` `symbolic` — Entry bodies, prompts, descriptions, and generated synthesis text are prose; directives, timestamps, entity schemas, metadata types, links, tags, queries, checkpoints, diagnostics, rule configs, ASTs, and merge identities are symbolic. I did not find retained embeddings, vector stores, model weights, or adapter state in this revision.
- **Lineage:** `authored` `imported` — Users and agents author schema entries, knowledge entries, syntheses, and actualization markers. Imported material can be captured as reference entries, Markdown Thalo blocks, starter templates, or source entries passed into syntheses. I did not find qualifying trace-extracted durable memory from agent session logs, tool traces, trajectories, or event streams.
- **Behavioral authority:** `knowledge` `instruction` `validation` `routing` `ranking` — Entries and synthesis outputs serve as knowledge artifacts; entity definitions, the bundled skill, synthesis prompts, and actualization instructions guide agents; checker rules and diagnostics validate; links, tags, queries, LSP navigation, workspace indexes, and merge identity route readers and tools; query order, limits, changed-entry selection, and GitHub Action pending-synthesis selection rank or prioritize what gets surfaced.

**Thalo entries and schemas.** `define-entity` and `alter-entity` records create the local type surface; `create` and `update` instance entries carry the actual knowledge. The `Workspace` parses documents, maintains schema and link indexes, tracks entity and link dependencies, and reports affected files when edits change schemas or links ([packages/thalo/src/model/workspace.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/model/workspace.ts)).

**Synthesis definitions and actualization markers.** A `define-synthesis` artifact combines source queries with a prompt; an `actualize-synthesis` artifact records a checkpoint such as `git:<commit>` or `ts:<timestamp>`. These artifacts shape later generation by deciding which changed entries are included and what prompt accompanies them ([packages/thalo/src/services/synthesis.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/services/synthesis.ts), [apps/docs/content/docs/change-tracking.mdx](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/apps/docs/content/docs/change-tracking.mdx)).

**Tool indexes and diagnostics.** The checker's workspace index, the LSP's loaded workspace, and the merge driver's entry matching are derived access structures. They do not add new knowledge claims, but they strongly affect authoring feedback, navigation, conflict resolution, and CI outcomes ([packages/thalo/src/checker/workspace-index.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/checker/workspace-index.ts), [packages/thalo-lsp/src/server.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo-lsp/src/server.ts), [packages/thalo/src/merge/driver.ts](https://github.com/rejot-dev/thalo/blob/cdb9aae983e6bc0b75eff1606bc99b088c3aebff/packages/thalo/src/merge/driver.ts)).

**Promotion path.** Thalo's implemented promotion path is loose but useful: unstructured thoughts or external references can become typed entries; typed entries can become query-selected synthesis inputs; a user or external command can write synthesized prose and add a checkpoint; validation and PR review can then harden the result. The system does not itself promote prose advice into enforced validators except when a human or agent authors a schema or rule.

## Comparison with Our System

Thalo and Commonplace share the repo-native premise: durable knowledge should stay inspectable as text, versionable by git, and checkable by deterministic tooling. Both systems favor explicit types, validation, links, and agent-readable authoring instructions over opaque hosted memory.

The main difference is where the governance lives. Commonplace has collection contracts, type specs, validation over Markdown artifacts, generated indexes, review workflows, and an explicit artifact-authority vocabulary. Thalo provides a lower-level personal knowledge language and toolchain: users define their own entity schemas, then use CLI/LSP/checker feedback to keep entries valid. Commonplace's semantics are collection-specific and methodology-specific; Thalo's semantics are user-defined and format-level.

Thalo is more general as an embedded substrate. It can parse Thalo blocks inside Markdown, expose a TypeScript API and VFS, run in browser or Node contexts, and provide LSP/editor services. Commonplace is more opinionated about knowledge-base practice: note types, links, review gates, source grounding, and indexes already encode a methodology.

The synthesis mechanism is close to Commonplace review workflows but weaker in authority by default. Thalo can select changed source entries and package them with a prompt; a user command or agent must perform the synthesis and write the result. Commonplace review artifacts usually retain stronger provenance and validation around generated claims.

### Borrowable Ideas

**Embedded typed blocks in Markdown.** Commonplace could borrow a "typed block" surface for small structured records inside ordinary notes, while keeping collection-level Markdown as the durable artifact. Useful only with a concrete recurring record shape.

**Git-aware synthesis checkpoints.** Thalo's `actualize-synthesis` checkpoint is a compact way to ask, "What changed since this synthesis last ran?" A Commonplace analogue could track source-note deltas for generated indexes, surveys, or cross-system comparisons. Ready for generated analyses that have clear source queries.

**Semantic merge driver by artifact identity.** Thalo's entry-level merge approach is a strong fit for append-heavy structured text. Commonplace could use the idea for future machine-generated structured sections, but ordinary Markdown notes are too free-form for this to be ready broadly.

**Agent-facing skill plus validators as adoption package.** Thalo ships a concise skill that tells agents how to edit the format and run validation. Commonplace already has skills, but Thalo's format-specific references are a good reminder to bundle examples and local syntax in the skill itself.

**Do not borrow unrestricted action writes.** The GitHub Action intentionally runs a caller-supplied command and commits all resulting changes. That is powerful for user-owned repos, but Commonplace review automation should keep narrower path ownership and stronger source-grounding checks.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents manually author entries, schemas, syntheses, checkpoints, and synthesis outputs through text editors, CLI workflows, LSP-assisted editing, scripts, and PR review. Automatic write paths exist for initialization, formatting, VFS writes with revision checks, merge-driver output, checker/LSP diagnostics, changed-entry packaging, and the GitHub Action that invokes a user command, commits its resulting file changes, and opens or updates a PR.

**Curation operations:** `none` — The automatic paths I found are acquisition/orchestration, validation, formatting, conflict handling, prompt packaging, and PR automation. I did not find built-in code that automatically consolidates, deduplicates, evolves, synthesizes, invalidates, decays, or promotes memory already in the Thalo store under the review vocabulary; synthesis content is produced by a user or external command, not by Thalo's core algorithm.

The strongest write-side operation is `actualize`: it finds changed source entries for a synthesis and emits raw entry text plus instructions for adding a checkpoint. The CLI leaves the final write to the operator; the GitHub Action delegates generation to a configured command and then commits whatever changed. That makes the automated authority procedural rather than epistemic: Thalo can decide which inputs are pending, but it does not judge whether the generated synthesis is faithful.

## Read-back

**Read-back:** `pull` — Retained Thalo knowledge re-enters future work through explicit query, actualization, LSP navigation, checker diagnostics, scripting API calls, editor actions, GitHub Action runs, or an agent deliberately reading the files. I did not find a deployed path that pushes retained memory into an agent invocation without such an explicit read or workflow trigger.

`thalo query` and the API execute symbolic filters over the workspace; `thalo actualize` pulls changed entries for declared synthesis sources; the LSP serves hover/completion/definition/reference data when the editor asks; the GitHub Action runs on repository events but still passes selected synthesis JSON to an explicitly configured command. From the receiving model's perspective, Thalo's stored memory is not automatically injected unless the host command chooses to put the JSON or files into that model call.

Selection is bounded by entity type, field equality, tag, link, source query, target synthesis link id, changed-entry checkpoint, file extension discovery, ignore rules for hidden directories and `node_modules`, CLI limits, and LSP workspace folders. There is no built-in semantic recall, vector similarity, or runtime budget planner beyond symbolic filtering and incremental change selection. Effective use of retrieved entries by downstream LLMs is not faithfulness-tested by Thalo itself.

Other consumers include human authors, editors, CI jobs, GitHub PR reviewers, custom scripts through the TypeScript API, and any external LLM command wired into the synthesis action.

## Curiosity Pass

**The language is closer to plain-text accounting than to RAG.** Thalo's design strength is that entries are structured enough for tools to validate and select, while still being ordinary text. That makes it easy for agents to write, but it also means recall depends on authored symbols rather than learned similarity.

**"Synthesized understanding" is intentionally outside the core.** The README's synthesis story sounds like a memory system producing higher-level understanding, but the inspected code mostly packages deltas and prompts. The actual synthesis oracle is user-chosen.

**The format can represent trace-extracted memories, but Thalo does not create them by itself.** A user could define `conversation-message`, `conversation-summary`, or similar entities and import agent logs into Thalo. That would be a Thalo-backed trace-learning workflow, not evidence that this repository implements one.

**The strongest trust affordance is validation plus git history.** Thalo does not prove claims true, but it makes malformed structure, missing links, invalid fields, and changed synthesis inputs visible. That is a practical trust layer for agent-authored knowledge.

## What to Watch

- Whether `actualize` or the GitHub Action gains built-in faithfulness checks for generated synthesis content; that would move it from prompt packaging toward validated knowledge production.
- Whether Thalo adds a standing retrieval layer beyond symbolic queries, such as lexical search, embeddings, or budgets; that would change the read-back comparison with Commonplace.
- Whether action-generated PRs get per-claim provenance or source spans instead of only listing included entries; that would make synthesis review more auditable.
- Whether custom validation rules become first-class project artifacts rather than scripts around the core checker; that would strengthen promotion from prose convention to system-definition enforcement.
- Whether agent trace entities become part of the default templates or examples; that would create a clearer trace-learning use case, but only if paired with durable extraction and distillation code.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: Thalo stores structured knowledge, but read-back is pull-only in the inspected implementation.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Thalo separates file substrate, prose/symbolic forms, authored/imported lineage, and validation/routing/knowledge authorities.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: entity definitions, checker rules, synthesis prompts, action configuration, and merge rules can shape later behavior with stronger force than ordinary entries.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Thalo entries and synthesis outputs mainly act as retained evidence, reference, and advice.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Thalo's main context mechanism is symbolic selection plus changed-entry packaging under bounded human or CI workflows.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - compares: Thalo frontloads schema validation, link indexing, and changed-entry selection before a downstream LLM sees synthesis inputs.
