---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "browzy.ai's terminal knowledge system and library at frozen Git revision 56c253042041ee2f483a5e9b824174d746891cf4."
run-id: AAS-2026-10-15-browzy-ai-0a823a13a7b6-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "56c253042041ee2f483a5e9b824174d746891cf4"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/VihariKanukollu/browzy.ai
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-browzy-ai/related-systems/VihariKanukollu--browzy.ai
  revision: 56c253042041ee2f483a5e9b824174d746891cf4
  sha256: null
---

# browzy.ai boundary

## Boundary and evidence

The target is the repository's personal knowledge system, including its terminal application and importable engine. Its intended use is to ingest user-selected material, compile retained wiki articles, and answer questions from those articles. It qualifies as a **memory/knowledge/context-engineering system**, rather than only a model API client: the shipped code owns source admission, article persistence, indexing, later retrieval and model-conditioned answering (SRC-1, `src/core/ingest/index.ts`, `src/core/compile/compiler.ts`, `src/core/retrieval/contextBuilder.ts`, `src/core/query/engine.ts`).

The boundary is **whole-system** at the source level. It includes the CLI drivers, prompts, customization file mechanism, maintenance paths, demo state producer and evaluators, not just exported library classes. The package's executable is the Ink/Commander entry; the library is a separate shipped surface (SRC-1, `package.json`, `src/cli/entry.tsx`, `src/index.ts`).

> "bin": {
>     "browzy": "dist/cli/entry.js"
>   },
> --- `package.json`

Tracing that entry reaches `BrowzyApp` when no arguments are supplied and the registered ingest, compile, query, lint, status, search and init commands otherwise. The older Commander/readline entry explicitly identifies itself as unused; its presence is not evidence that normal users run the old REPL (SRC-1, `src/cli/entry.tsx`, `src/cli/index.ts`).

### Functional loop included

- **Produce and admit:** ingestion dispatches web, PDF, image and text processors, updates the raw manifest and source database, and invalidates the query cache. The application offers source previews and compilation guidance, bulk compilation, topic-search ingestion and optional clipboard capture. These callers are part of browzy, not an excluded host (SRC-1, `src/core/ingest/index.ts`, `src/cli/app.tsx`).
- **Retain and maintain:** compilation reads the raw manifest and existing articles, makes model calls for nontrivial sources, parses article markers, persists Markdown and search records, and updates backlinks and the wiki index. Short sources have a template path without a model call. Health checks, refresh/re-ingestion, rebuild requests and user schema controls remain inside the boundary; their labels do not establish that their intended effects always succeed (SRC-1, `src/core/compile/compiler.ts`, `src/core/storage/filesystem.ts`, `src/core/lint/linter.ts`, `src/cli/app.tsx`).
- **Reload and consume:** context construction searches SQLite, reloads article files and falls back to the wiki index before ranking and context assembly. The library query path calls the model itself; the terminal application calls `prepare` and then streams through the provider. Both paths are included, so library capabilities are not automatically attributed to the terminal caller (SRC-1, `src/core/retrieval/contextBuilder.ts`, `src/core/query/engine.ts`, `src/cli/app.tsx`).
- **Retain interaction-derived material:** the application saves sessions and metadata, reloads a prior session for digest generation, attempts to persist a digest as a wiki article, and invokes an insight crystallizer after multi-article answers. The crystallizer writes to `drafts`, not directly to `wiki`. This establishes separate code paths, not successful promotion or later retrieval of drafts (SRC-1, `src/cli/hooks/useSession.ts`, `src/cli/app.tsx`, `src/core/query/crystallizer.ts`).
- **Direct behavior and evaluate:** shipped compiler/query/linter/digest/crystallizer prompts and the user schema mechanism are included alongside retrieval and security test sources. Prompt instructions establish intended behavior, not compliance; tests are inspected source, not observed test results (SRC-1, `src/core/prompts.ts`, `src/core/schema.ts`, `tests/e2e/retrieval-quality.test.ts`, `src/core/__tests__/filesystem.test.ts`).

Minimum implementation passages supporting the retained-state loop:

> this.fs.writeArticle(article.slug, article.frontmatter, article.content);
> --- `src/core/compile/compiler.ts:123-123`

> const results = this.db.search(query, 20);
>       for (const r of results) {
>         if (!slugs.has(r.slug)) {
>           slugs.add(r.slug);
>           const article = this.fs.readArticle(r.slug);
>           if (article) articles.push(article);
>         }
>       }
> --- `src/core/retrieval/contextBuilder.ts`

> session.saveSession();
>     session.saveSessionMeta(stats);
> --- `src/cli/app.tsx`

> // Write to drafts/ directory (NOT wiki/)
>   const draftsDir = join(dataDir, 'drafts');
> --- `src/core/query/crystallizer.ts`

### Repository coverage

The tracked root tree was enumerated at the frozen commit. “Included” fixes functional scope; it does not claim a line-by-line audit. Available material not yet inspected remains distinguishable from unavailable evidence and is eligible for later inspection at this same pin.

| Top-level tracked path | Classification and material paths | Initial inspection and limits |
|---|---|---|
| `README.md` | Included: declared use, commands, architecture and configuration. | Read; doctrine/design only. Marketing examples are not execution traces. |
| `package.json` | Included: library entry, executable, build/test scripts and dependency declarations. | Read; supports shipped entry tracing, not installed-package equivalence. |
| `src/` — application surfaces | Included: `src/index.ts`, `src/core/index.ts`, `src/cli/entry.tsx`, `src/cli/app.tsx`, `src/cli/commands/`, `src/cli/hooks/useSession.ts`; legacy `src/cli/index.ts` and `src/cli/repl.ts`. | Read entry points, session hook, compile command and material application ranges covering admission, answering, persistence, maintenance and later digest consumption; searched other commands and legacy REPL. Other command bodies, onboarding, key store, history/autocomplete hooks and rendering helpers are available but not fully inspected. No external-host exclusion applies to these shipped callers. |
| `src/` — state engine | Included: `src/core/ingest/`, `src/core/compile/`, `src/core/storage/`, `src/core/query/`, `src/core/retrieval/`, `src/core/wiki/`, `src/core/discovery/`, `src/core/lint/`, `src/core/analytics/`, plus config, schema, prompts, activity log, types, sanitation and utilities. | Read ingestion dispatch, compiler, query engine, crystallizer, filesystem store, linter, schema and material context-builder, SQLite, provider and prompt ranges; searched config, discovery and wiki responsibilities and their application consumers. Processor internals, ranking/cache/compactor internals, migrations, analytics and utility bodies are available but not fully inspected. These are included follow-up evidence, not access gaps or proof of their advertised guarantees. |
| `src/` — demo and tests | Included: `src/core/demo/seed.ts`, `src/demo/articles/`, `src/core/__tests__/`; `src/types.d.ts` supplies declarations. | Seeder read: it loads bundled articles, populates SQLite, writes wiki files/index and a marker. Demo article bodies, declarations and most unit-test bodies not yet inspected; test names searched. Demo contents are not independent evidence of system quality. |
| `tests/` | Included: `tests/e2e/retrieval-quality.test.ts` and `tests/fixtures/articles/`. | Read fixture-loading/setup and initial retrieval assertions; searched suite headings for ranking, stemming, tokens, migration, cache, chunking, BM25 and latency. Remaining assertions and fixture bodies not yet inspected. No test execution or measured quality conclusion. |
| `tsconfig.json` | Included: source-to-dist compilation boundary. | Read; identifies `src/**/*` compilation, Node16 modules and declaration output. No build performed. |
| `.npmignore` | Included: package-content exclusions. | Read; source and tests are excluded from npm packaging. This analysis concerns the Git artifact, not a captured npm tarball. |
| `package-lock.json` | Included as dependency-resolution metadata. | Tree-listed, contents not yet inspected. Does not supply dependency implementation or installed-environment evidence. |
| `.gitignore` | Deliberately excluded from behavioral analysis: Git housekeeping. | Tree-listed, not read. No conclusion about completeness of a developer's ignored local state. |
| `LICENSE` | Deliberately excluded from behavioral analysis: legal terms. | Tree-listed, not read. No legal/license assessment. |

### Frozen evidence and external boundary

The sole frozen source is SRC-1 at commit `56c253042041ee2f483a5e9b824174d746891cf4`, applicable through the run cutoff **2026-10-15**. The acquired checkout's HEAD matched that commit and its status was clean. This is **code-grounded** analysis with documentation as attributed design evidence. No target process, examples, tests or provider calls were executed.

External dependencies include model services selected through the Claude, OpenAI, OpenRouter and Ollama provider adapter, web/search destinations, local user inputs and customization, and npm dependencies including SQLite bindings, SDKs, Ink and document parsers (SRC-1, `src/core/llm/provider.ts`, `src/cli/app.tsx`, `package.json`). The repository's adapter and integration code is included; service implementations, model weights, live pages, dependency repositories and arbitrary consuming applications are excluded. These exclusions prevent conclusions about provider reliability, model accuracy, live search quality, third-party implementation guarantees or behavior of an unspecified host.

No user knowledge directory, real session corpus, deployed environment, run trace, npm distribution capture or causal experiment was supplied. These are unavailable evidence, not uninspected repository files. Consequently the boundary supports source-level control/data-flow analysis and attributed intent, not observed persistence success, answer quality, security effectiveness, latency, cost or compounding knowledge quality. Obsidian compatibility in the README remains a declared integration claim, not inspected Obsidian operation (SRC-1, `README.md`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/VihariKanukollu/browzy.ai` | 56c253042041ee2f483a5e9b824174d746891cf4 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-browzy-ai/related-systems/VihariKanukollu--browzy.ai`. Implementation: tracked tree, package/TS configuration, entry and library exports, CLI consumers, session retention/reload, ingestion dispatcher, compiler, query engine, context assembly, filesystem, SQLite setup/indexing, crystallizer, linter, demo seeder, provider selection, schema handling and selected test setup/assertions. Doctrine/design: README and compiler, contradiction, conversation, output, digest, crystallizer and schema-aware prompt sections. Ranged reads and remaining available material are identified in coverage above. | Implementation: [package](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/package.json), [CLI caller](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/app.tsx), [compiler](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/compile/compiler.ts), [retrieval](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/retrieval/contextBuilder.ts), [sessions](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/cli/hooks/useSession.ts), [evaluator](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/tests/e2e/retrieval-quality.test.ts). Doctrine/design: [README](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/README.md), [prompts](https://github.com/VihariKanukollu/browzy.ai/blob/56c253042041ee2f483a5e9b824174d746891cf4/src/core/prompts.ts). | No repository access gap encountered. Implementation lacks supplied execution evidence: no observed success, benchmarks or security validation. Doctrine/design cannot establish prompt compliance or advertised quality. External services and dependency implementations are outside the frozen source. |
