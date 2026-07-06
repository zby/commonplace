---
description: "OpenWiki review: agent-generated repository wiki with Git-scoped updates, root AGENTS/CLAUDE pointers, and no wiki retrieval index"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-07-06"
---

# OpenWiki

OpenWiki, from `langchain-ai/openwiki`, is a TypeScript CLI that runs a DeepAgents documentation agent against the current repository, writes or refreshes an `openwiki/` documentation tree, and prompts the agent to add a standardized pointer to that tree in top-level `AGENTS.md` and/or `CLAUDE.md`. At the reviewed commit it is a documentation-generation and maintenance loop, not a retrieval engine over the generated wiki: future context efficiency comes from a small generated doc map, Git-scoped update prompts, no-op detection, and coding-agent instruction pointers rather than from search, embeddings, or a context compiler ([README.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/README.md), [src/agent/prompt.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/prompt.ts), [src/agent/index.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/index.ts)).

**Repository:** https://github.com/langchain-ai/openwiki

**Reviewed commit:** [23428de0cc0b1b6d3e5d09be413e92a5d6ee451f](https://github.com/langchain-ai/openwiki/commit/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f)

**Last checked:** 2026-07-06

## Core Ideas

**The generated wiki is a repository-local memory artifact.** The CLI creates initial documentation in `openwiki/` and refreshes it on update runs; the agent prompt requires `openwiki/quickstart.md` as the entrypoint, a small set of section pages, links between pages, and source references useful to humans and future coding agents ([README.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/README.md), [src/agent/prompt.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/prompt.ts), [openwiki/quickstart.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/openwiki/quickstart.md)). The wiki is maintained as ordinary Markdown files in the target repo, so inspection, review, and rollback are Git-shaped.

**Root agent files are the activation hook.** The README says OpenWiki appends prompting to `AGENTS.md` and/or `CLAUDE.md`; the system prompt implements this by requiring a fixed "OpenWiki" section that points future agents to `openwiki/quickstart.md` and says to read it before following deeper links ([README.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/README.md), [src/agent/prompt.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/prompt.ts), [AGENTS.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/AGENTS.md)). The hook is prompt-driven rather than a deterministic post-processing step, but it is a real design claim: generated docs should be discoverable by later coding agents without the user remembering to mention them.

**Git evidence scopes update work.** For init and update runs, the host process builds a prompt context from `git status --short`, current `HEAD`, recent commits or commits since the last recorded update, and `git diff --name-status HEAD` ([src/agent/utils.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/utils.ts), [openwiki/architecture/overview.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/openwiki/architecture/overview.md)). Successful init/update runs write `openwiki/.last-update.json` only when the wiki content snapshot changed, and update runs can skip entirely when `HEAD` and the meaningful worktree state have not changed since the last run ([src/agent/index.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/index.ts), [src/agent/utils.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/utils.ts), [test/update-noop.test.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/test/update-noop.test.ts)).

**Context efficiency is prompt- and artifact-shaped, not retrieval-shaped.** OpenWiki constrains volume and complexity by telling the documentation agent not to exhaustively read every file, to avoid root `**/*` globs, to prefer targeted discovery, to use at most eight initial pages unless justified, to avoid thin pages, and to keep update edits surgical with a soft diff budget ([src/agent/prompt.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/prompt.ts)). The DeepAgents backend is rooted at the target repo, runs in virtual mode, caps tool output at 100,000 bytes, and has a 120 second timeout, which bounds source exploration but does not rank wiki content for later agents ([src/agent/index.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/index.ts)). Future agents get a map and links, not an automatic top-k context pack.

**Operational state is local and mostly symbolic.** Credentials and model/provider choices live in `~/.openwiki/.env`; a SQLite checkpointer lives at `~/.openwiki/openwiki.sqlite`; update metadata lives under the target repo's `openwiki/`; and the scheduled workflow example installs the package, runs `openwiki --update --print`, and opens a PR scoped to `openwiki/` ([src/env.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/env.ts), [src/credentials.tsx](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/credentials.tsx), [src/agent/index.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/index.ts), [examples/openwiki-update.yml](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/examples/openwiki-update.yml)). Optional LangSmith tracing records runs externally, but I did not find code that distills traces into durable lessons, rules, rankings, or model artifacts.

## Artifact analysis

- **Storage substrate:** `repo` `files` `sqlite` `service-object` - The main retained artifacts are files in the target repository: `openwiki/*.md`, `openwiki/.last-update.json`, and top-level `AGENTS.md`/`CLAUDE.md` sections. Local configuration is another file store under `~/.openwiki/.env`; DeepAgents checkpoints use SQLite under `~/.openwiki/openwiki.sqlite`. Optional LangSmith traces are external service-held diagnostics, not OpenWiki's project memory substrate ([README.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/README.md), [src/constants.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/constants.ts), [src/env.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/env.ts), [src/agent/index.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/index.ts)).
- **Representational form:** `prose` `symbolic` - Wiki pages, root agent instructions, generated source maps, and prompts are prose interpreted by future agents and humans. CLI options, env keys, provider config, update JSON, Git summaries, content hashes, parser checks, and checkpointer records are symbolic. The inspected code uses external model APIs but stores no embeddings, adapters, or model weights ([src/commands.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/commands.ts), [src/constants.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/constants.ts), [src/agent/prompt.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/prompt.ts)).
- **Lineage:** `authored` `imported` `trace-extracted` - The package code, prompt, CLI parser, provider tables, docs, and tests are authored. Generated wiki pages are imported/derived views over repository files, existing docs, and Git evidence. Update metadata and the optional checkpoint/tracing surfaces are extracted from runs, but they are used for continuity, update scoping, and diagnostics rather than distilled into learned policy ([src/agent/utils.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/utils.ts), [src/agent/types.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/types.ts), [openwiki/agent/workflow.md](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/openwiki/agent/workflow.md)).
- **Behavioral authority:** `knowledge` `instruction` `routing` `enforcement` `validation` - Generated wiki pages are knowledge artifacts; root agent-file sections and the OpenWiki system prompt instruct future behavior; `quickstart.md`, links, source maps, update metadata, and Git summaries route attention; the prompt's repository-root and secret-handling rules plus no-op update skipping enforce operational boundaries; CLI/model/base-URL validation and content-snapshot checks validate run eligibility and metadata writes ([src/agent/prompt.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/prompt.ts), [src/commands.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/commands.ts), [src/constants.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/constants.ts), [src/agent/utils.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/utils.ts)).

**Generated wiki pages.** The durable content surface is Markdown under `openwiki/`: a quickstart plus section pages sized for a future agent to navigate. The prompt gives these pages advisory/context authority, not validator authority; there is no schema or deterministic checker for page claims.

**Root agent-instruction sections.** The standardized `AGENTS.md`/`CLAUDE.md` block is the strongest behavior-shaping artifact OpenWiki creates outside `openwiki/`. Its authority depends on a later host coding agent actually loading those root files, but when loaded it is instruction plus routing: read quickstart first, then follow links.

**Update metadata and Git summaries.** `.last-update.json` is a small symbolic memory of the previous successful run. OpenWiki reads it to scope the next update prompt and to skip no-op updates; it is not user-facing knowledge, but it changes whether and how the documentation agent runs.

**Prompts and CLI/runtime code.** The OpenWiki system prompt is a high-authority prose system-definition artifact: it controls repository boundaries, file-writing scope, page count, source discovery, subagent use, root instruction-file edits, and update discipline. The CLI/parser/provider/env code is symbolic system definition around that prompt.

**Checkpoints and traces.** The SQLite checkpointer and optional LangSmith tracing can preserve run traces, with LangSmith living outside the repo as a service diagnostic surface. The code does not expose a stable cross-run memory policy that promotes those traces into wiki edits, rules, validators, embeddings, or model updates. I therefore treat them as diagnostic/continuity surfaces, not trace-derived learning.

**Promotion path.** OpenWiki's implemented path is repository source and Git evidence -> generated wiki pages -> root agent-file pointer -> future human/agent pull from the wiki. Update runs can revise the wiki from newer source changes, but there is no implemented promotion from a generated claim into a typed, validated, higher-authority artifact.

## Comparison with Our System

OpenWiki and Commonplace share the belief that future agents need an explicit map. Both use repository files, root instruction files, and Markdown links to make local context easier to navigate. OpenWiki is much more productized around generating that map: one CLI collects Git evidence, runs an agent, writes docs, stores update metadata, and can be scheduled through GitHub Actions.

The main divergence is authority. Commonplace treats collection contracts, type specs, validation, review gates, link vocabulary, and curated indexes as the system. OpenWiki treats the generated wiki as helpful documentation and relies on the generation prompt for shape and quality. That makes OpenWiki easier to adopt in an arbitrary repo, but weaker as an agent memory system: it has few typed artifacts, no claim-level provenance, no link semantics, and no deterministic validation of generated page content.

OpenWiki's update loop is the piece most directly relevant to Commonplace. It uses prior update metadata and Git evidence to keep maintenance scoped, then avoids timestamp churn when no wiki content changed. Commonplace already has richer artifact governance; OpenWiki is a useful reminder that update scoping and no-op detection are themselves context-engineering surfaces.

### Borrowable Ideas

**Git-scoped documentation update prompts.** Ready now. Commonplace commands that refresh generated docs or indexes could include the exact changed-path and recent-commit window that justifies the edit, instead of asking an agent to rediscover the scope inside the same call.

**Content snapshots to suppress metadata churn.** Ready now. OpenWiki's "write update metadata only when content changed" pattern is a cheap guard against scheduled-workflow noise.

**Standard root instruction pointer.** Ready with constraints. Commonplace already uses root instructions, but OpenWiki's fixed "start here" block is a clean install-time affordance for repositories that vend a KB or generated docs to future agents.

**Small generated quickstart as a context router.** Ready for consuming projects, not for Commonplace's own library artifacts. A generated map can be useful as onboarding context if it is clearly lower authority than typed notes and validators.

**Do not borrow prompt-only governance as sufficient quality control.** Commonplace should borrow the update-scoping mechanics, not the idea that an LLM prompt alone can make generated knowledge trustworthy.

## Write side

**Write agency:** `manual` `automatic` - Humans invoke the CLI, choose providers/models, send chat or init/update messages, and can edit generated docs directly. The OpenWiki agent automatically writes and updates `openwiki/`, inserts or refreshes top-level `AGENTS.md`/`CLAUDE.md` sections, writes a temporary plan during documentation runs, deletes that plan before completion, records update metadata when content changed, and can be scheduled to open update PRs ([src/commands.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/commands.ts), [src/agent/prompt.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/prompt.ts), [src/agent/index.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/src/agent/index.ts), [examples/openwiki-update.yml](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/examples/openwiki-update.yml)).

**Curation operations:** `evolve` - The automatic update path can modify existing wiki pages and root agent-instruction sections in light of newer repository state. Source-to-wiki generation is acquisition, not curation; content hashing, Git summaries, credentials, and SQLite checkpoints are access/runtime upkeep, not curation over stored memory. The prompt asks the agent to avoid duplicate/thin pages and keep updates surgical, but I did not find deterministic code that performs deduplication, decay, invalidation, or promotion over wiki entries.

## Read-back

**Read-back:** `both` - Generated wiki memory can be pulled explicitly by humans, future agents, or OpenWiki chat/update runs that inspect `openwiki/`; it is also pushed indirectly when OpenWiki's standardized `AGENTS.md`/`CLAUDE.md` section is loaded by a host coding agent, and directly into OpenWiki update runs when `.last-update.json` and Git change summaries are inserted into the update prompt.

**Read-back signal:** `coarse` `identifier` - The root instruction pointer is coarse project-level recall, while `.last-update.json`, `openwiki/quickstart.md`, command mode, repository path, and linked page paths are identifier-based signals. I found no lexical, embedding, or LLM-judgment retrieval layer over the generated wiki.

**Faithfulness tested:** `no` - The test suite checks update no-op behavior, and the code validates CLI/model/base-URL inputs, but I did not find an ablation or audit showing that future agents actually read the pushed OpenWiki pointer or use generated wiki pages faithfully ([test/update-noop.test.ts](https://github.com/langchain-ai/openwiki/blob/23428de0cc0b1b6d3e5d09be413e92a5d6ee451f/test/update-noop.test.ts)).

**Direction edge cases.** The root `AGENTS.md`/`CLAUDE.md` section is push only when the downstream coding-agent harness loads those files; OpenWiki creates the hook but does not itself own every future host's context assembly. The generated wiki pages are mostly pull: the agent or human must follow the quickstart and links. Update metadata is push inside OpenWiki's own update command because the host process injects it into the prompt.

**Selection, scope, and complexity.** OpenWiki does not provide top-k retrieval, token budgeting over wiki pages, vector search, or claim-level snippets. Its context strategy is to keep the retained wiki small and navigable, to frontload a quickstart and source-map structure, to scope update prompts with Git evidence, and to tell the model not to exhaustively inspect the repository. That manages complexity by constraining the generated artifact and the update task, not by ranking memory at read time.

**Authority at consumption.** Generated wiki pages are advisory context. Root agent-file sections are soft instructions and route future agents toward the wiki. `.last-update.json` has stronger operational authority inside OpenWiki because it can scope or skip update runs. None of these paths hard-gate future coding behavior against the wiki's claims.

**Other consumers.** Humans use the interactive Ink CLI, `--print` output, generated Markdown, local credential diagnostics, and scheduled PRs. The documentation agent consumes Git summaries, current docs, and prompts. Future coding agents consume the root pointer and wiki pages if their harness loads or retrieves them.

## Curiosity Pass

**OpenWiki is a doc-maintenance loop more than a memory backend.** It stores useful agent-facing documentation, but it does not expose search, MCP tools, embeddings, a graph, schema validation, or a context compiler over that documentation.

**The strongest context move is update scoping.** The most concrete context-engineering mechanism is not the generated wiki itself; it is the host-side assembly of Git evidence and last-update metadata so an update run starts with a bounded change window.

**Prompt-level governance carries a lot of weight.** Repository boundaries, no secret reads, page-count discipline, subagent discipline, and root instruction-file edits are prompt rules interpreted by the DeepAgents model. The code wraps the model, but it does not independently verify the generated wiki's fidelity.

**The SQLite checkpointer looks stronger than the memory policy around it.** The checkpointer persists thread state, but thread ids include a per-run/session component, so I did not find a stable cross-session replay path that makes prior conversations a durable project memory.

**Generated AGENTS/CLAUDE sections are powerful but host-dependent.** The idea is good: put a pointer where future agents already look. Its effect depends on the downstream agent harness actually loading those files and treating the pointer as action-relevant.

## What to Watch

- Whether OpenWiki adds a retrieval or context-compiler surface over `openwiki/`. That would change read-back from map-based pull/coarse push to ranked or inferred context assembly.
- Whether generated pages gain schemas, provenance requirements, or validation. That would move OpenWiki closer to a typed KB rather than generated docs.
- Whether the AGENTS/CLAUDE insertion becomes deterministic host code instead of prompt-only agent behavior. That would make the activation hook easier to verify.
- Whether checkpoints or LangSmith traces are later distilled into docs, rules, rankings, or model updates. That would create a real trace-derived learning path.
- Whether scheduled update PRs run documentation-specific checks before opening. That would upgrade update quality from prompt discipline to enforceable governance.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: OpenWiki's wiki pages, root instruction sections, update metadata, prompts, and checkpointer differ by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - classifies: generated wiki pages help only when future agents pull them or receive the coarse root pointer.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: generated wiki pages mostly serve as evidence, reference, context, and advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: OpenWiki's prompt, CLI parser, update metadata, and root agent-file block shape future behavior.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds: OpenWiki manages context by creating a small map and scoping update runs rather than loading all source into future agents.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - relates: OpenWiki frontloads repository discovery into a quickstart/wiki so later agents can start from a precomputed map.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: OpenWiki's later recall depends on available symbols such as `AGENTS.md`, `CLAUDE.md`, `openwiki/quickstart.md`, linked paths, and Git metadata.
