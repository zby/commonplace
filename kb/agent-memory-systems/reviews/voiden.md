---
description: "Voiden review: offline Git-native API workspace with .void Markdown/request files, linked blocks, request history, extension skills, and local execution"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
---

# Voiden

Voiden, from `VoidenHQ/voiden`, is an offline Electron API workspace that stores API requests, documentation, reusable request blocks, imported collections, scripts, assertions, and batch runners in local text artifacts. It is agent-adjacent rather than an autonomous memory runtime: the inspected code makes API-work context diffable, greppable, executable, importable, and available to Claude/Codex through generated skills, but it does not automatically learn future behavior from agent traces.

**Repository:** https://github.com/VoidenHQ/voiden

**Reviewed commit:** [c0776cb399ab452dc942b606c7b34f80b95c4412](https://github.com/VoidenHQ/voiden/commit/c0776cb399ab452dc942b606c7b34f80b95c4412)

**Last checked:** 2026-06-05

## Core Ideas

**The canonical workspace artifact is a `.void` file, not a hosted collection object.** The README presents Voiden as an offline, Git-native API workspace whose `.void` files combine Markdown, frontmatter, and executable `void` request blocks ([README.md](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/README.md)). The serializer emits YAML frontmatter plus fenced `void` blocks from ProseMirror nodes, while the parser strips frontmatter, parses YAML block payloads back into typed editor nodes, and falls back to code blocks when a block type is unknown ([apps/ui/src/core/editors/voiden/markdownConverter.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/editors/voiden/markdownConverter.ts)).

**Voiden uses symbolic composition for context efficiency.** A request file can import a block or whole file by UID/path, so shared auth, headers, bodies, request sections, and documentation do not have to be duplicated across every request. Linked block previews are cached for the UI, but request execution calls `expandLinkedBlocksInDoc(..., { forceRefresh: true })` and linked-file expansion so the runnable request is assembled from current disk contents ([apps/ui/src/core/editors/voiden/extensions/BlockLink.tsx](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/editors/voiden/extensions/BlockLink.tsx), [apps/ui/src/core/editors/voiden/utils/expandLinkedBlocks.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/editors/voiden/utils/expandLinkedBlocks.ts), [apps/ui/src/core/request-engine/requestOrchestrator.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/request-engine/requestOrchestrator.ts)).

**The request engine is a plugin pipeline over retained blocks.** Core execution builds a request through registered plugin handlers, runs hybrid pipeline stages for preprocessing, compilation, environment replacement, auth, sending, response extraction, and postprocessing, then lets response handlers consume the result ([docs/architecture/OVERVIEW.md](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/docs/architecture/OVERVIEW.md), [apps/ui/src/core/request-engine/sendRequestHybrid.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/request-engine/sendRequestHybrid.ts)). The `.void` document is therefore both documentation and an executable symbolic specification.

**Imports are transformations into the native retained form.** Postman and OpenAPI importers parse external collection/spec data and write native `.void` files with generated request blocks, folder structure, request bodies, headers, query params, auth, and documentation ([core-extensions/src/postman-import/utils/converter.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/postman-import/utils/converter.ts), [core-extensions/src/openapi-import/utils/converter.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/openapi-import/utils/converter.ts)). The import result is inspectable and editable, but import lineage is mostly implicit in the generated files rather than maintained as a provenance graph.

**Request/response history is stored, but not distilled into learned behavior.** When history is enabled, post-processing hooks capture request and response state, file attachments, timings, status, and plugin-owned metadata into per-file JSON under `.voiden/history`, prune by retention days, and keep the directory ignored by Git ([apps/ui/src/core/history/pipelineHooks.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/history/pipelineHooks.ts), [apps/ui/src/core/history/historyManager.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/history/historyManager.ts)). I did not find code that turns those traces into durable rules, skills, embeddings, route entries, or edited `.void` files.

**Agent adoption is through generated skills and plain files.** The Electron app composes a base `.void` skill plus enabled extension `skill.md` files, then installs the result into `~/.claude/skills/voiden/SKILL.md` and/or `~/.codex/skills/voiden/SKILL.md` when the user enables those targets ([apps/electron/src/main/skillsComposer.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/skillsComposer.ts), [apps/electron/src/main/skillsInstaller.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/skillsInstaller.ts), [apps/electron/skills/base.skill.md](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/skills/base.skill.md)). That is a practical bridge from editor-native API context to agent-editable files, not a relevance engine.

## Artifact analysis

- **Storage substrate:** `files` `repo` — The central retained artifacts are `.void` files, generated/imported `.void` folders, `.voiden/history/*.json`, user settings/state JSON, installed skill Markdown, extension manifests, and optional Git repositories around the project; no database, vector store, graph store, or model-weight store is required by the reviewed implementation ([apps/electron/src/main/voiden.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/voiden.ts), [apps/electron/src/main/persistState.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/persistState.ts), [apps/electron/src/main/settings.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/settings.ts), [apps/electron/src/main/git.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/git.ts)).
- **Representational form:** `prose` `symbolic` — Markdown docs, request notes, extension readmes, generated skills, and response/history text are prose; YAML block payloads, node types, UIDs, manifests, settings, environment variables, request pipeline hooks, assertions, scripts, stitch configs, history JSON, and Git status are symbolic. I did not find retained embeddings or learned parameters in this revision.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author `.void` files, scripts, assertions, settings, and skills; Postman/OpenAPI collections and protocol/schema files can be imported into native blocks; request/response history is trace-extracted from executions, though it remains stored as evidence rather than distilled learning.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Markdown docs, examples, history entries, and responses serve as knowledge; installed Claude/Codex skills and script blocks instruct agents or the runtime; extension manifests, block ownership, linked-block references, section splitting, and pipeline handlers route work; assertions, auth/env handling, request cancellation, attachment hashing, schema parsing, and Git/project checks validate or enforce selected behavior.

**`.void` request documents.** The operative artifact is a hybrid Markdown/YAML document: prose carries API documentation and intent, while fenced `void` blocks carry executable node structure. The app can parse, render, modify, execute, and serialize those blocks, so the symbolic fields have direct operational consequences.

**Linked blocks and linked files.** `linkedBlock` and `linkedFile` nodes store references to source block UIDs and source file paths; the UI can preview them, and request execution expands them from disk with `forceRefresh`. Their authority is routing and composition: they decide which authored source material becomes part of the runnable request without duplicating it.

**Extension manifests and skills.** Core extensions declare block ownership, slash commands, pipeline hooks, response panels, history builders, and optional `skill.md` guidance. Voiden composes enabled extension skills into an installed external-agent instruction file, which gives the agent enough file-format and block-contract knowledge to create or edit `.void` files.

**History files.** Request/response history JSON records execution traces with retention pruning and attachment-change checks. It is useful as evidence, debugging context, and replay/export material, but I did not find a path that automatically rewrites future requests, updates skills, or promotes traces into a higher-authority memory artifact.

**Promotion path.** Voiden can promote imported Postman/OpenAPI material into native `.void` files, and users can manually turn history findings into edited requests, docs, assertions, or scripts. The implemented automatic path stops at acquisition, formatting, history capture, and execution; promotion into more authoritative artifacts is manual.

## Comparison with Our System

Voiden and Commonplace share the strongest design instinct: keep behavior-shaping knowledge in ordinary files that humans, agents, Git, and search tools can inspect. Commonplace does this for methodology and review artifacts; Voiden does it for API workspaces. Both benefit from plain text, local editability, Git diffs, and agent-readable conventions.

The divergence is register and authority. Commonplace is a knowledge-base method with explicit collection contracts, type specs, validation, and review gates. Voiden is an API IDE: its typed blocks execute requests, run scripts and assertions, compose shared request parts, and store response history. Its symbolic form is more executable than most Commonplace notes, but its governance over knowledge claims is lighter.

Voiden's linked-block model is close to a code-oriented include system. Commonplace links are usually navigational and evidential: they help agents decide what to read. Voiden links are operational: they assemble the request payload that will actually be sent. That is stronger authority and therefore needs freshness guarantees; Voiden handles this with execution-time disk refresh instead of relying on the UI preview cache.

The agent surface is narrower than a memory system but useful. Voiden does not push workspace knowledge into an agent conversation by relevance matching; it makes a project legible to agents by installing a skill and preserving the workspace as greppable files. Commonplace already uses a similar skill/type-contract layer, but for KB operations rather than API execution.

### Borrowable Ideas

**Executable Markdown blocks with stable UIDs.** Commonplace could borrow this only for artifacts that need formal sub-block execution or reuse. For ordinary notes it would add too much structure; for review bundles, generated prompts, or test cases it may be useful.

**Execution-time linked-content refresh.** Ready now as a pattern. If Commonplace ever uses transcluded fragments or reusable prompt blocks, the consumer should re-read the source at execution time rather than trusting a preview cache.

**Skill composition from enabled modules.** Voiden composes a base skill plus extension skill files. Commonplace could use the same pattern for optional KB capabilities, but only where the enabled/disabled module state is a real configuration surface.

**History as local evidence, not automatic learning.** Voiden's request history is a good restraint model: capture traces cheaply, make them inspectable, and do not pretend they have improved the system until something promotes them into a reviewed artifact.

**Git-native application workspaces.** Voiden shows that domain tools can expose operational state as ordinary project files rather than app-private collections. Commonplace should keep favoring file-backed knowledge unless a concrete workflow needs a service store.

## Write side

**Write agency:** `manual` `automatic` — Users, agents, import flows, extension installers, scripts, and the desktop app can create or edit `.void` files, settings, installed skills, extension state, and request artifacts. Automatic writes include frontmatter generation, import conversion, autosave/state persistence, history capture, retention pruning, `.gitignore` updates for `.voiden/history`, and skill recomposition after extension/skill settings change.

**Curation operations:** `none` — The automatic paths I found are acquisition, serialization, execution-log capture, retention pruning, cache invalidation, and generated-instruction composition. I did not find automatic consolidation, deduplication, evolution, synthesis, invalidation, decay, or promotion of memory already in the store under the review vocabulary.

History capture is trace extraction, but not trace-learning under the current review contract. The stored traces are request/response evidence, and the code provides UI/history consumption plus retention controls. It does not distill those traces into future prompt instructions, validators, route policies, embeddings, or edited workspace artifacts.

## Read-back

**Read-back:** `pull` — Retained workspace memory reaches agents or users through deliberate file opening, CLI path opening, editor rendering, search, linked-block expansion during an explicit request run, history/sidebar inspection, or external agent use of the installed Voiden skill; I did not find a deployed path that pushes project memory into an agent invocation by relevance, identifier match, or always-load policy.

Linked blocks can feel like push inside the editor because imported content appears in the current document, but the trigger is an authored link in the file and a user/editor/request action. That is pull/composition through a symbolic reference, not unsolicited memory activation.

The installed Claude/Codex skill is the closest edge case. It can make Voiden file-format instructions available to an external agent runtime, but the skill is composed from baseline app/extension guidance and user-enabled extension state. It does not read the user's project history or select project memories for a future action.

Selection is bounded by file paths, project roots, active tabs, block UIDs, section separators, enabled extensions, request sections, history retention settings, and explicit import references. Quality of later agent behavior from the installed skill is not tested in the inspected code; I found structural code for skill composition and installation, not behavioral ablations proving that agents create better `.void` files.

Other consumers include the desktop user, the Electron renderer, request pipeline hooks, extension plugins, history sidebars, Git UI, terminal/CLI opener, script/assertion runners, and external Claude/Codex agents after the user installs the skill.

## Curiosity Pass

**Voiden is more interesting as a context substrate than as a memory learner.** It makes API context durable, executable, and agent-editable. That is valuable even without automatic relevance matching or trace learning.

**The strongest memory mechanism is the linked-block include model.** A shared auth/header/body block can alter many future requests without duplicating content. That is a high-authority retained artifact because it changes execution, not just display.

**History is intentionally app-local.** `.voiden/history` is kept out of Git, which is right for transient execution traces and sensitive responses. It also means the most trace-like artifacts are weaker as collaborative long-term memory unless manually promoted.

**Extension skills are a clean agent bridge.** Voiden does not ask agents to infer the file format from examples every time. It prepackages the operational contract into a skill, which is exactly the kind of context frontloading that makes plain files agent-usable.

**Lineage is the main weak point.** Imported Postman/OpenAPI data becomes native `.void` files, but the review did not find durable provenance tying each generated block back to the source operation/schema. That limits invalidation and regeneration.

## What to Watch

- Whether history gains a reviewed promotion path into assertions, docs, scripts, or reusable request blocks; that would turn request traces from evidence into trace-learning.
- Whether imported OpenAPI/Postman artifacts retain source pointers and regeneration metadata at the block level; that would make invalidation and re-import safer.
- Whether installed skills start including project-specific summaries or workspace indexes; that would change read-back from baseline instruction availability toward project memory push.
- Whether extension manifests become enforceable capability contracts rather than descriptive metadata; that would raise plugin governance closer to Commonplace type validation.
- Whether linked-block sync adds version pins or conflict detection for shared blocks; without that, a high-authority shared block can silently change many request executions.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Voiden's `.void` files, linked blocks, history JSON, extension manifests, and installed skills differ by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Voiden stores request knowledge and traces, but project memory read-back is pull/composition rather than automatic push.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `.void` request blocks, scripts, assertions, extension manifests, pipeline hooks, and installed skills can define or constrain future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Markdown docs, examples, responses, and request history serve as evidence or reference until promoted into executable blocks or instructions.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - parallels: Voiden composes installable agent skills so agents do not rediscover the `.void` format from scratch.
