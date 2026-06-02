---
description: "Voiden review: offline Git-native API workspace with .void files, extension skills, search, imports, and pull-only agent affordances"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# Voiden

Voiden, from VoidenHQ, is an offline, Git-native API workspace for building, testing, documenting, and collaborating on API requests in plain-text `.void` files. At the reviewed commit, its agent-memory relevance is not an autonomous memory loop; it is a file-native context substrate for API work, with readable workspace files, importers, stitch execution, extension-provided skill text for Claude/Codex, and ordinary search/git surfaces that agents can use.

**Repository:** https://github.com/VoidenHQ/voiden

**Reviewed commit:** [c0776cb399ab452dc942b606c7b34f80b95c4412](https://github.com/VoidenHQ/voiden/commit/c0776cb399ab452dc942b606c7b34f80b95c4412)

**Last checked:** 2026-06-02

## Core Ideas

**The central memory unit is a `.void` file, not a database row.** Voiden files combine YAML frontmatter, Markdown documentation, and fenced `void` YAML blocks that serialize request, response, scripting, assertion, and protocol-specific editor nodes. The README presents this as "pure text" API work, while the app serializer/parser turns ProseMirror/Tiptap nodes into YAML-backed Markdown and back ([README.md](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/README.md), [markdownConverter.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/ui/src/core/editors/voiden/markdownConverter.ts)).

**Requests are composed from reusable structured blocks.** REST, GraphQL, sockets, scripting, assertions, faker, auth, OpenAPI import, Postman import, and stitch runner functionality live as core extensions registered over a shared editor/request pipeline ([WORKSPACES.md](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/docs/architecture/WORKSPACES.md), [OVERVIEW.md](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/docs/architecture/OVERVIEW.md), [core-extensions/src/plugins.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/plugins.ts)). The retained artifact is still text, but the operative parts are symbolic node types, attrs, UIDs, sections, variables, and plugin schemas.

**Agent adoption is implemented as static skill composition.** Settings expose Claude and Codex skill toggles, startup recomposes enabled extension `skill.md` files, and the installer writes a single `SKILL.md` into `~/.claude/skills/voiden` or `~/.codex/skills/voiden` ([settings.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/settings.ts), [skillsComposer.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/skillsComposer.ts), [skillsInstaller.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/skillsInstaller.ts)). The base skill teaches agents the `.void` file format and workflows rather than providing a live retrieval API ([base.skill.md](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/skills/base.skill.md)).

**Context efficiency is file-native and pull-oriented.** The file tree avoids eager recursion, skips heavy directories, caps concurrent I/O, and decorates git state from caches; file search uses ripgrep when possible, skips `.git` and `.voiden`, caps result volume, and extracts readable text from Markdown plus `void` YAML blocks ([fileSystem.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/fileSystem.ts), [files.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/ipc/files.ts), [search.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/ipc/search.ts)). This controls discovery cost and context volume, but an agent still has to pull files, search results, or skill text deliberately.

**Imports are source-to-file conversion, not learning from agent traces.** Postman and OpenAPI converters parse external API specifications or collections and generate native `.void` blocks/files ([postman converter](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/postman-import/utils/converter.ts), [OpenAPI converter](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/openapi-import/utils/converter.ts)). That gives Voiden a derived artifact path, but the source signal is imported API material, not session logs or repeated agent trajectories.

**Execution traces are operational records.** The REST history adapter captures request/response state and can export it back to `.void`; the stitch runner executes matched `.void` files, expands linked files/blocks, records section results, and persists recent run history under `.voiden/stitch-runner/` ([historyAdapter.tsx](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/voiden-rest-api/historyAdapter.tsx), [stitchEngine.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/voiden-stitch/lib/stitchEngine.ts), [stitchHistory.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/core-extensions/src/voiden-stitch/lib/stitchHistory.ts)). I did not find code that distills those traces into durable agent rules, skills, or ranked memory.

## Artifact analysis

- **Storage substrate:** `files` — Ordinary project files, intended to be edited, searched, diffed, and committed with Git
- **Representational form:** `mixed` — Mixed Markdown prose, YAML frontmatter, symbolic `void` block nodes, UIDs, attrs, tables, links, variables, and script/assertion blocks

**`.void` workspace files.** Storage substrate: ordinary project files, intended to be edited, searched, diffed, and committed with Git. Representational form: mixed Markdown prose, YAML frontmatter, symbolic `void` block nodes, UIDs, attrs, tables, links, variables, and script/assertion blocks. Lineage: authored in the editor, created from sample projects, imported from Postman/OpenAPI, exported from history, or edited by humans/agents; parser/serializer and plugin node schemas determine how file changes regenerate editor state. Behavioral authority: knowledge artifacts as API documentation and examples; system-definition artifacts when request blocks, environment references, scripts, assertions, and stitch config drive request execution.

**Project metadata, environments, and runtime variables.** Storage substrate: `.voiden/.voiden-projects`, `.voiden/env-public.yaml`, `.voiden/env-private.yaml`, profile-specific env YAML files, legacy `.env*` files, and `.voiden/.process.env.json` ([projectUtils.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/projectUtils.ts), [env.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/env.ts), [variables.ts](https://github.com/VoidenHQ/voiden/blob/c0776cb399ab452dc942b606c7b34f80b95c4412/apps/electron/src/main/variables.ts)). Representational form: symbolic JSON/YAML/key-value state. Lineage: authored or runtime-written configuration, with public/private split and profile inheritance. Behavioral authority: routing/configuration authority over which project, env profile, and variables requests consume; not memory advice by itself.

**Extension manifests, plugin code, and skill files.** Storage substrate: repository extension modules, installed community extension directories, copied packaged skill resources, and user-installed Claude/Codex skill directories. Representational form: symbolic manifests and TypeScript plugin registrations plus prose skill instructions. Lineage: authored by Voiden or extension authors, then composed from enabled extensions at runtime. Behavioral authority: system-definition artifacts: plugin code registers editor nodes, slash commands, request hooks, response sections, and skill text; composed skills instruct agents how to create and edit `.void` files.

**Search, file-tree, git, and CLI surfaces.** Storage substrate: mostly transient app state and subprocess output over the project filesystem. Representational form: symbolic IPC payloads, file paths, git status maps, search snippets, and readable extracted text. Lineage: derived views over current workspace files and git state. Behavioral authority: routing/ranking/advisory authority for what humans or agents inspect next; search results remain knowledge artifacts until a caller loads and applies them.

**Request history and stitch results.** Storage substrate: in-memory stores during execution plus persisted stitch history JSON under `.voiden/stitch-runner/`; REST history entries are plugin-captured request/response records in the app's history surface. Representational form: structured JSON with request metadata, response metadata, assertions, body snippets, durations, status, and errors. Lineage: generated from actual request executions and batch runs. Behavioral authority: audit/evidence artifacts for humans or agents; they can be exported or inspected, but code does not promote them into future instructions.

Promotion path: Voiden has practical conversion paths from imported API specs, captured history, and structured blocks into editable `.void` files. It does not implement a governance path from execution traces to durable agent instructions; the strongest authority promotion is manual or tool-mediated editing of a `.void` file or extension skill.

## Comparison with Our System

| Dimension | Voiden | Commonplace |
|---|---|---|
| Primary purpose | Offline API workspace and executable API documentation | Agent-operated methodology KB |
| Canonical retained artifact | `.void` files plus `.voiden/` project/config/history state | Typed Markdown notes, instructions, reviews, ADRs, sources, indexes, reports |
| Storage substrate | Local filesystem, project repo, Electron user data, optional extension installs | Git repository files plus generated indexes and validation/review reports |
| Representational form | Mixed Markdown, YAML, symbolic editor/request nodes, scripts, plugin manifests | Mostly prose/frontmatter plus schemas, scripts, links, validators, and reports |
| Activation | Human/agent pull through files, search, CLI, editor, git, and installed skills | Agent pull through `rg`, indexes, links, skills, instructions, validation, and review gates |
| Governance | Git diffs, app schemas, request/assertion execution, extension boundaries | Collection contracts, type specs, link rules, validation, review gates, replacement archives |

Voiden and Commonplace share the strongest file-first instinct: important work should remain inspectable, diffable, greppable, and editable by agents without a proprietary workspace. Voiden is more productized for API execution: it owns the editor, protocols, variables, scripts, auth, history, imports, and desktop workflow. Commonplace is stronger on knowledge governance: every durable artifact has a collection contract, type contract, review status, link semantics, and validation surface.

The biggest divergence is authority. In Voiden, symbolic request blocks have execution authority, but documentation and skill text are only as authoritative as the host agent makes them. In Commonplace, the KB is explicitly designed around behavior-shaping retained artifacts, so instructions, validators, reviews, notes, and indexes are classified by authority and lifecycle.

**Read-back:** `pull` — Voiden stores and exposes readable workspace artifacts, search results, git status, history, and static installed skills, but I did not find a code-grounded relevance-gated pre-action push path that injects selected project memory into an agent context

### Borrowable Ideas

**Treat domain files as executable documentation.** Ready now as a design pressure. Commonplace already has typed Markdown, but Voiden's `.void` format is a good example of keeping prose, structured blocks, scripts, assertions, and examples in one file that remains useful to both humans and tools.

**Generate agent skills from enabled capabilities.** Ready with care. Voiden composes a skill from the base format guide plus enabled extension skills. A Commonplace analogue would generate scoped agent guidance from enabled collection/tools state, while keeping the generated skill visibly derived and validateable.

**Keep import conversion as an explicit lineage boundary.** Ready now. Voiden's Postman/OpenAPI converters make source-to-native conversion visible. Commonplace should continue treating imported material, snapshots, and converted notes as distinct lineage stages rather than pretending conversion is authorship.

**Use readable extraction for custom block files.** Useful if Commonplace grows richer embedded block formats. Voiden's search path extracts human-readable text from Markdown and YAML blocks before matching. Commonplace can borrow that pattern for future mixed-format artifacts without making the embedded structure opaque to `rg`-style workflows.

**Do not borrow execution history as automatic learning.** Voiden's histories are useful evidence, but they do not become better rules by being stored. Commonplace should keep any trace-to-instruction promotion behind explicit review and source grounding.

## Curiosity Pass

**The interesting memory design is not AI-specific.** Voiden is agent-friendly because the workspace is local, textual, and structured, not because it has an LLM memory engine.

**The `.voiden/` directory carries mixed authority.** Project metadata, env files, runtime variables, and stitch history live near the project, but they have different visibility and governance properties; public env YAML can be versioned while private/runtime state should not be treated as shared knowledge.

**Skill installation is powerful but static.** A composed Voiden skill can teach an agent the format and available extension blocks, but it does not by itself select the right project file or verify that generated `.void` files still execute.

**Search extraction is a quiet adoption advantage.** Custom block formats often become hard for generic tools to inspect. Voiden partly avoids that by extracting readable text from `void` YAML blocks for search.

**Trace-derived learning does not apply under the current rule.** Request history and stitch history are traces in an operational sense, but the inspected code does not derive durable agent-facing memories, rules, skills, or rankers from them.

## What to Watch

- Whether Voiden adds an MCP or agent API that can search, open, and edit project `.void` files with scoped retrieval rather than only installing static skills.
- Whether execution history gains summarization or failure-pattern extraction, which would move Voiden toward trace-derived learning and require provenance/review treatment.
- Whether composed skills become project-specific and include current workspace metadata; that would change read-back from static format instruction toward context activation.
- Whether `.void` schemas gain stronger validation outside the editor, making files easier for agents to generate safely in headless workflows.
- Whether public/private `.voiden/` state rules remain clear as more runtime artifacts are persisted near the repo.

## Bottom Line

Voiden is a strong file-native API workspace and a useful adjacent example for agent-operated knowledge systems, but it is not a trace-derived memory system at the reviewed commit. Its durable value is the `.void` artifact model: prose plus executable structured blocks in local files, supported by imports, search, git, and composed agent skills. Commonplace should borrow the file-native executable-documentation pattern and generated skill composition, while preserving stricter review gates before traces or generated artifacts gain behavioral authority.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Voiden stores readable workspace artifacts, but agents must still pull them through files, search, CLI/editor actions, or static skills.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: `.void` files, env state, extension manifests, skills, search results, and run histories carry different substrate, form, lineage, and authority.
- [Context engineering](../../notes/definitions/context-engineering.md) - relates: Voiden is a domain-specific context substrate whose efficiency comes from file search, lazy loading, readable extraction, and block structure.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: API docs, examples, search snippets, and execution histories advise later work as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: request blocks, extension manifests, scripts, assertions, environment routing, and composed skills configure future behavior.
