---
description: "Napkin review: TypeScript/Bun markdown-vault CLI and SDK with progressive disclosure, Obsidian parity, BM25 cache, pi integration docs, and benchmark-only session mining"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# Napkin

Napkin is Michaelliv's TypeScript/Bun knowledge system for agents: a local-first CLI and SDK that turns a project directory or Obsidian-style vault into progressively disclosed markdown context. Its core package is deliberately LLM-free. It stores ordinary files, builds cheap derived views for orientation and retrieval, and leaves higher-authority agent behavior to tool outputs, `NAPKIN.md`, pi integrations, and the calling agent.

**Repository:** https://github.com/Michaelliv/napkin

**Reviewed commit:** [4d939149fc64720d7566735bfc22789f8b9a9251](https://github.com/Michaelliv/napkin/commit/4d939149fc64720d7566735bfc22789f8b9a9251)

**Last checked:** 2026-05-16

## Core Ideas

**Progressive disclosure is the central memory contract.** The README and design docs define a four-level path: `NAPKIN.md` as pinned context, `napkin overview` as a vault map, `napkin search` as ranked partial retrieval, and `napkin read` as full-file access ([README.md](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/README.md), [docs/agent-memory-progressive-disclosure.md](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/docs/agent-memory-progressive-disclosure.md)). The implementation backs that shape: `getOverview` reads `NAPKIN.md`, groups markdown files by folder, extracts tags and TF-IDF-like keywords, and returns a compact map; `searchVault` builds a MiniSearch index and returns ranked snippets; `readFile` resolves a note and returns full markdown ([src/core/overview.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/overview.ts), [src/core/search.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/search.ts), [src/core/crud.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/crud.ts)).

**The storage substrate is a markdown vault, not Napkin's config directory.** Normal initialization creates `.napkin/config.json` beside `.obsidian/`, while content remains in the project root with `NAPKIN.md`, template-defined folders, note templates, daily notes, canvas files, bases, and ordinary markdown ([src/core/init.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/init.ts), [src/utils/vault.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/utils/vault.ts)). `listFiles` explicitly skips `.napkin`, `.obsidian`, `.git`, `.trash`, `.nanny`, `node_modules`, `config.json`, and `search-cache.json`, which makes the source-vs-cache boundary visible in code ([src/utils/files.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/utils/files.ts)). Vault notes are knowledge artifacts when consumed as evidence or context. `NAPKIN.md`, templates, `.base` files, and synchronized Obsidian config gain system-definition authority when they configure retrieval, note creation, views, daily-note paths, or agent startup context.

**CLI and SDK are deliberately separated.** `src/sdk.ts` exposes a `Napkin` class whose methods return typed data and throw errors, while `src/main.ts` registers Commander commands and `src/commands/*` handle parsing, process exits, and human/JSON/quiet output ([src/sdk.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/sdk.ts), [src/main.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/main.ts), [src/utils/output.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/utils/output.ts)). That split is important for agent memory: the CLI can shape agent behavior with minimal text and hints, while programmatic callers can embed the same vault operations without scraping stdout.

**Search is cached, but the cache is a derived accelerator.** `searchVault` fingerprints markdown paths and mtimes, reuses `.napkin/search-cache.json` when valid, and rebuilds the MiniSearch index plus backlink counts when the fingerprint changes ([src/core/search.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/search.ts), [src/utils/search-cache.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/utils/search-cache.ts)). The cache stores serialized index data, doc metadata, and backlink counts, not canonical note content. It is a system-definition artifact only while it ranks retrieval; lineage is a coarse mtime fingerprint, so a reviewer should treat it as disposable.

**Obsidian parity is practical, not cosmetic.** Napkin resolves files by wikilink-style basename or exact path, uses shallowest-match loose resolution for backlink scoring, parses tags, tasks, headings, links, aliases, and YAML frontmatter, synchronizes daily-note and template settings into `.obsidian/`, supports Obsidian Bases via SQL/Jexl translation, and reads/writes JSON Canvas files ([src/utils/files.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/utils/files.ts), [src/core/links.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/links.ts), [src/utils/config.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/utils/config.ts), [src/core/bases.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/bases.ts), [src/core/canvas.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/core/canvas.ts)). The design lets human-maintained Obsidian vaults become agent memory without moving them into a product database.

**Agent-facing output is part of the control surface.** The CLI hides search scores by default, emits match-only snippets unless asked for context, and prints workflow hints that tell the agent how to go deeper ([src/commands/search.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/commands/search.ts), [src/commands/overview.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/commands/overview.ts), [docs/designing-cli-for-agents.md](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/docs/designing-cli-for-agents.md)). These outputs are lightweight system-definition artifacts: they do not enforce policy, but they route the next retrieval action through instruction-shaped tool text.

**Distillation is documented as an external pi extension, not implemented in the core package.** The README points pi users to `pi-napkin` for context injection, `kb_search`/`kb_read` tools, and automatic distillation, while `docs/distill.md` describes a timer that reads conversation entries and writes template-shaped notes into the vault ([README.md](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/README.md), [docs/distill.md](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/docs/distill.md)). The checked-in repository, however, has no `.pi/extensions/napkin-context/` or `.pi/extensions/distill/` directory, and the package's CLI command table does not register a `distill` command ([src/main.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/src/main.ts), [package.json](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/package.json)). Code-grounded review should therefore treat automatic session-to-note distillation as an adjacent integration claim, not as implemented Napkin-core behavior.

**The benchmarks exercise agentic retrieval over synthetic vaults.** `bench/longmemeval-eval.ts` and `bench/locomo-eval.ts` turn conversation/session traces into temporary markdown notes, set mtimes from session dates, run `pi` with a napkin context extension, capture tool calls/results, score answers, and remove the temporary vaults afterward ([bench/longmemeval-eval.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/bench/longmemeval-eval.ts), [bench/locomo-eval.ts](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/bench/locomo-eval.ts), [bench/README.md](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/bench/README.md)). This is trace-derived evaluation machinery, not a durable user-memory feature: its per-round session notes are source fixtures for a run, not retained cross-session learning artifacts. The repo also has ordinary Bun tests and Biome lint/check scripts for implementation quality ([package.json](https://github.com/Michaelliv/napkin/blob/4d939149fc64720d7566735bfc22789f8b9a9251/package.json)).

## Comparison with Our System

| Dimension | Napkin | Commonplace |
|---|---|---|
| Primary purpose | Agent-friendly CLI/SDK for local markdown and Obsidian-compatible vaults | Methodology KB framework with typed artifacts, validation, review, and operational conventions |
| Canonical substrate | Project files: markdown, templates, `.base`, `.canvas`, `NAPKIN.md`; `.napkin/` holds config/cache | Git-tracked `kb/` collections with type specs, schemas, indexes, reviews, sources, and instructions |
| Retrieval | Progressive disclosure: pinned context, overview keywords, BM25/backlinks/recency search, read | `rg`, descriptions, generated/curated indexes, authored links, skills, review reports |
| Derived state | `search-cache.json`, overview output, graph UI data, benchmark result files | Directory indexes, generated reports, review outputs, validation state |
| Behavioral authority | Mostly advisory and routing: CLI hints, `NAPKIN.md`, templates, config, pi tool surface | Stronger artifact contracts: type specs, collection rules, validators, review gates, instructions |
| Trace-derived learning | Not in core package; external distill docs and benchmark trace loaders exist | Explicitly reviewed as a methodology axis; promotion from traces requires artifact contracts and validation |

The strongest alignment is the shared filesystem-first premise. Napkin makes the cheapest useful version of an agent memory substrate: keep the user's notes where editors and git can see them, make orientation cheap, and let the agent choose when to search or read. That is close to commonplace's belief that context engineering starts from inspectable retained artifacts rather than a hidden service object.

The main divergence is contract strength. Napkin is intentionally generic: a vault can be a personal assistant notebook, coding project, research notes, company KB, or product workspace. Its template skeletons and Obsidian conventions provide structure, but the core package does not enforce collection-specific quality bars, source lineage, review state, link labels, or promotion rules. Commonplace is narrower and heavier: type specs, collection conventions, validation, review bundles, and replacement archives give artifacts stronger behavioral authority.

Napkin's progressive disclosure is also more product-shaped. The agent learns the retrieval path from command defaults and hints: overview to search to read. Commonplace currently relies more on repo conventions, `rg`, indexes, and skill instructions. Napkin shows how much leverage a small CLI can get from agent-shaped defaults, especially hidden scores, match-only snippets, and workflow hints.

The distillation boundary is important. If the external pi distill extension writes conversation-derived notes into a Napkin vault, those distilled notes would be durable knowledge artifacts and possibly system-definition artifacts when templates or `NAPKIN.md` make them guide future behavior. But this review cannot assign that authority to Napkin core from the checked-in package alone. The implementation evidence here supports "markdown vault retrieval system with benchmark session loaders," not "shipped trace-derived learning system."

**Read-back:** pull — agents deliberately run overview, search, and read over the vault; checked-in core does not inject notes automatically.

## Borrowable Ideas

**Make progressive disclosure executable.** Commonplace already has navigation guidance, but Napkin's CLI makes the path operational: overview output points to search, search output points to read and outline. A commonplace analogue could expose task-specific `commonplace-overview`, `commonplace-search`, or bundle commands whose outputs instruct the next cheapest expansion step. Ready as a command-output design pattern.

**Hide ranking internals from default agent output.** Napkin sorts by BM25, backlinks, and recency but hides numeric scores unless `--score` is requested. If commonplace adds ranking over notes, default output should avoid false precision and show evidence snippets or discriminating metadata instead. Ready as a UI rule.

**Keep caches outside the canonical artifact set.** `search-cache.json` lives in `.napkin/`, is fingerprint-invalidated, and is skipped by file listing. Commonplace should preserve the same authority split for any future indexes, embeddings, or usage-derived ranking: canonical notes stay reviewable; volatile accelerators stay explicitly derived.

**Use Obsidian parity as an adoption bridge.** Napkin benefits from supporting wikilinks, frontmatter, daily notes, templates, Bases, Canvas, and `.obsidian/` config sync. Commonplace should not copy the whole Obsidian surface, but the general lesson is strong: reuse a mainstream human note substrate where that lowers adoption cost for agent memory.

**Treat SDK and CLI as separate consumers.** Napkin's core returns typed data while CLI wrappers shape stdout for agents. Commonplace commands could follow that split more consistently: library functions provide structured results; command output can be optimized for agent reading and next-step routing.

**Do not import benchmark trace loaders as production memory.** The LongMemEval and LoCoMo harnesses show a useful way to convert conversation sessions into per-round markdown notes for retrieval experiments. In commonplace, that pattern belongs first in a source/snapshot or workshop pipeline with explicit lineage and expiry, not directly in the library layer.

## Curiosity Pass

**Napkin is less magical than the README's memory language might suggest.** The core package has no embeddings, graph database, daemon, hidden model call, or durable learning loop. Its memory effect comes from file affordances plus a retrieval workflow that agents can follow.

**`NAPKIN.md` has high leverage but no freshness machinery.** It is loaded into overview output and scaffolded by templates, so it can guide every session. The code does not validate whether it is current, contradicted by notes, or too large. That is acceptable for a lightweight tool, but it makes `NAPKIN.md` a manually maintained system-definition artifact.

**The source/cache boundary is mostly clean, with one legacy wrinkle.** Normal vaults keep `.napkin/` as config/cache and content in the project root. Some benchmark harnesses create an embedded `.napkin` vault for temporary data because `findVault` supports legacy layouts. That does not undermine the product model, but it matters when interpreting benchmark paths.

**The docs describe more integration than the repo contains.** `CLAUDE.md` mentions `.pi/extensions/napkin-context/` and `.pi/extensions/distill/`, and the benchmark scripts expect a napkin-context extension path, but those extension directories are not present in this checkout. The actual extension implementation needs separate review before claims about pi tools, context injection, or automatic distillation are promoted.

**Obsidian compatibility creates a large behavioral surface.** Bases and Canvas support are not just import/export conveniences. They let structured views and visual boards become retained artifacts that agents can query or mutate through Napkin. That increases utility, but also increases the number of formats whose semantics need testing if Napkin becomes a governance tool.

**Benchmark evidence should be read through the harness.** The benchmark code creates per-question temporary vaults, writes session notes at useful granularity, injects a prompt/tool environment through pi, and scores with an LLM judge. It is credible retrieval-evaluation machinery, but it is not evidence that ordinary user vaults will be well-authored, well-distilled, or well-governed.

## What to Watch

- Whether `pi-napkin` or future in-repo extensions are brought into this repository, making automatic context injection and distillation reviewable as implementation rather than documentation.
- Whether a `napkin distill` command appears in core, and whether it writes durable markdown artifacts with source lineage, template contracts, review state, and invalidation rules.
- Whether `NAPKIN.md` gains size, freshness, or contradiction checks as its authority grows.
- Whether search ranking remains transparent enough to debug when backlinks, recency, cache state, and fuzzy/prefix matching interact.
- Whether Bases and Canvas support evolve into stable agent tool surfaces or remain compatibility utilities for human-maintained vaults.
- Whether benchmark results are accompanied by full run artifacts, prompt versions, extension code, and reproducible sampled datasets.

---

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Napkin's value comes from staged activation through overview, search, and read, not from merely storing markdown.
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) - exemplifies: Napkin makes `NAPKIN.md`, folder keywords, search snippets, outlines, and full files into progressively stronger pointers.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: vault notes and benchmark session notes are mostly consumed as evidence, context, or reference.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: `NAPKIN.md`, CLI hints, templates, config, cache ranking, and pi tool surfaces can instruct, route, configure, or rank future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts: Napkin core does not implement durable trace-derived extraction, while its docs and benchmarks show where such extraction would attach.
