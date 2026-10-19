---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Siftly's shipped bookmark knowledge system, web application and agent-facing CLI at commit b25daa45b858f4be096b5c368671c34db4407d8e."
run-id: AAS-2026-10-18-siftly-b81c94cf0f77-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: b25daa45b858f4be096b5c368671c34db4407d8e
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/ViperrCrypto/Siftly
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-siftly-retry-1/related-systems/ViperrCrypto--Siftly
  revision: b25daa45b858f4be096b5c368671c34db4407d8e
  sha256: null
---

# Siftly boundary

## Boundary and evidence

Siftly is in scope as a **memory/knowledge/context-engineering system**: it imports Twitter/X bookmarks and likes, retains their content and model-generated metadata in SQLite, and reloads that retained content for browsing, search, visualization, export and a JSON CLI usable by agents. It is not classified as an enclosing general-purpose agent runtime. Its shipped application owns the knowledge-management loop and issues model requests for vision, semantic tagging, categorization, category suggestions and search reranking. Evidence: SRC-1, `prisma/schema.prisma`, `app/api/import/route.ts`, `app/api/categorize/route.ts`, `app/api/search/ai/route.ts`, `lib/category-suggester.ts`, `cli/siftly.ts`.

The intended use is a self-hosted personal bookmark knowledge base. The target's declared purpose and retained-state contract are explicit (SRC-1):

> Siftly turns your Twitter/X bookmarks into a **searchable, categorized, visual knowledge base** — running entirely on your machine. No cloud, no subscriptions, no browser extensions required. Everything stays local except the AI API calls you configure.
> --- `README.md`

> semanticTags    String?   // JSON array of AI-generated searchable tags
> entities        String?   // JSON: {hashtags[], urls[], mentions[], tools[], tweetType}
> enrichedAt      DateTime? // when AI enrichment last ran — drives incremental processing
> enrichmentMeta  String?   // JSON: {sentiment, people[], companies[]} from batch enrichment
> --- `prisma/schema.prisma`

The README passage is declared intent, not proof of network isolation. The frozen code also includes X API access, media and link-preview retrieval, and optional Cloudflare tunnel setup. These shipped integrations remain inside the functional account; the remote services' implementations do not (SRC-1, `lib/twitter-api.ts`, `app/api/import/x-oauth/fetch/route.ts`, `app/api/media/route.ts`, `app/api/link-preview/route.ts`, `scripts/setup-tunnel.sh`, `start.sh`).

### Functional coverage

The boundary is **whole-system**, not just the AI helper library. It includes the Next.js application and its browser-side import drivers, HTTP routes, model adapters and CLI bridges, SQLite state and FTS index maintenance, category maintenance, export writers, direct database CLI and shipped setup/maintenance instructions. The agent-facing CLI is a same-repository consumer, not an excluded host application. `package.json` ships it as the `siftly` npm script; `cli/siftly.ts` reads the same database and calls `ftsSearch`. The import UI also belongs to the target: its upload flow advances to a categorization step that starts or attaches to the server pipeline. This matters because the file-import endpoint itself persists data but does not start categorization (SRC-1, `package.json`, `cli/siftly.ts`, `app/import/page.tsx`, `app/api/import/route.ts`).

Minimum implementation passages establishing production, maintenance and later consumption of retained state (SRC-1):

> const res = await fetch('/api/import', { method: 'POST', body: formData })
> --- `app/import/page.tsx`

> const results = await categorizeBatch(batch, client, categoryDescriptions, allSlugs)
> await writeCategoryResults(results)
> --- `app/api/categorize/route.ts`

> if (!shouldAbort()) {
>   await rebuildFts().catch((err) => console.error('FTS rebuild error:', err))
> }
> --- `app/api/categorize/route.ts`

> const ftsIds = await ftsSearch(keywords)
> --- `cli/siftly.ts`

Search also reloads semantic tags, entities, media tags and category assignments before composing the reranking prompt. Obsidian export reloads bookmarks with media and categories, writes notes, and writes category and author indexes. These are material consumption paths, not evidence that an external agent or Obsidian installation successfully used the output (SRC-1, `app/api/search/ai/route.ts`, `lib/obsidian-exporter.ts`).

The following table covers every top-level tracked entry from the frozen Git tree. All rows refer to SRC-1. “Included” describes functional scope, not a claim that every line was audited. Full reads and bounded excerpts established the central loop; bounded source searches established additional route callers and integration paths. Entries marked inventory-only were available but not substantively inspected; they are not access gaps.

| Top-level entry | Treatment and material paths | Role, inspection basis and limit |
|---|---|---|
| `.env.example` | Included; configuration contract | Searched provider/database settings; no real credentials or configured deployment was inspected. |
| `.github/` | Included: `.github/workflows/docker-ghcr.yml`; excluded: issue and PR templates | Workflow inventoried and searched as packaging support. Templates are collaboration material, inventory-only; no conclusion about contributor process. |
| `.gitignore` | Excluded; inventory-only | Checkout hygiene, not retained-knowledge behavior; ignored-file completeness was not assessed. |
| `CLAUDE.md` | Included; fully read | Shipped setup, schema maintenance, pipeline and agent CLI instructions; treated as target doctrine, not execution authority. |
| `CODE_OF_CONDUCT.md` | Excluded; inventory-only | Community policy; no governance assessment. |
| `CONTRIBUTING.md` | Excluded; inventory-only | Contributor procedure; no development-process assessment. Runtime maintenance instructions in `CLAUDE.md`, `README.md` and launchers remain included. |
| `LICENSE` | Excluded; inventory-only | Legal text; no licensing conclusion. |
| `README.md` | Included; fully read | Intended use, import/enrichment/search loop, architecture and maintenance instructions. Claims remain distinguishable from implementation. |
| `SECURITY.md` | Excluded; inventory-only | Security reporting policy; no disclosure-process assessment or comprehensive security audit. Executable admission controls remain included. |
| `__tests__/` | Included: `__tests__/minimax-ai-client.test.ts`, `__tests__/minimax-auth.test.ts`, `__tests__/minimax-integration.test.ts` | Adapter/auth test declarations searched; integration test fully read. These are test source, not observed executions or retrieval-quality evaluations. |
| `app/` | Included: `app/import/page.tsx`, `app/api/import/route.ts`, `app/api/import/bookmarklet/route.ts`, `app/api/import/twitter/route.ts`, live/sync and X OAuth routes under `app/api/import/`; `app/api/categorize/route.ts`, `app/api/analyze/images/route.ts`; category, bookmark, search, mindmap, export, settings and stats routes under `app/api/`; matching pages | Produces, admits, maintains and consumes retained content. Core import/pipeline/search handlers read; remaining handlers searched for persistence, model and consumer responsibilities. Browser callers searched across all TSX pages; import driver inspected in bounded excerpts. Generated Prisma client is not tracked; icons/layout/style were inventoried, not visually assessed. |
| `cli/` | Included: `cli/siftly.ts`, fully read | Direct database search/list/show/categories/stats consumer with JSON output. Includes retained metadata in detail output; does not establish an enclosing agent's behavior. |
| `components/` | Included: `components/command-palette.tsx`, `components/bookmark-card.tsx`, `components/bookmark-row.tsx`, `components/bookmark-detail-modal.tsx`, `components/nav.tsx`, `components/mindmap/`, `components/theme-toggle.tsx` | Searched UI callers: bookmark search, manual category writes, media/link previews, graph reads and progress polling. Presentation-only portions inventoried; no rendered-UI verification. |
| `docker/` | Included: `docker/Dockerfile`, `docker/docker-compose.yml`, `docker/docker-entrypoint.sh`, `docker/README.md` | Entrypoint read, build/database-volume declarations searched; deployment README inventory-only. Defines shipped production startup and persistent storage placement; no image build or deployment result. |
| `eslint.config.mjs` | Excluded; inventory-only | Lint configuration; no lint-cleanliness conclusion. |
| `lib/` | Included: `lib/parser.ts`, `lib/twitter-api.ts`, `lib/x-sync.ts`, `lib/rawjson-extractor.ts`; `lib/vision-analyzer.ts`, `lib/image-context.ts`, `lib/categorizer.ts`, `lib/category-suggester.ts`; `lib/ai-client.ts`, `lib/claude-cli-auth.ts`, `lib/claude-cli.ts`, `lib/codex-cli.ts`, `lib/openai-auth.ts`, `lib/minimax-auth.ts`, `lib/settings.ts`; `lib/db.ts`, `lib/fts.ts`, `lib/search-utils.ts`, `lib/exporter.ts`, `lib/obsidian-exporter.ts`, `lib/types.ts` | Import normalization/sync, extraction, shipped prompts, enrichment persistence, category admission, provider/CLI calls, retained-state access, retrieval and exports. Core files or relevant ranges read; additional helpers searched and traced through callers. No model quality or external CLI internals inferred. |
| `middleware.ts` | Included; fully read | Optional Basic Auth, including bookmarklet endpoint exception; application-level admission is within scope. No penetration test. |
| `next.config.ts` | Included; configuration search/inventory | Framework configuration support; no production framework-behavior validation. |
| `package-lock.json` | Included; inventory-only | Frozen dependency resolution evidence available for later inspection; third-party package implementation is not thereby frozen for analysis. |
| `package.json` | Included; fully read | Next.js and CLI entry points, test script and dependencies. |
| `postcss.config.mjs` | Excluded; inventory-only | Styling build support; no CSS build correctness conclusion. |
| `prisma.config.ts` | Included; searched | Schema/migration paths and database URL configuration. |
| `prisma/` | Included: `prisma/schema.prisma`, `prisma/migrations/20260307055559_init/migration.sql`, `prisma/migrations/20260308000000_add_source_column/migration.sql`, migration lock | Schema fully read; migration files inventoried and launcher application path traced. No migration replay or schema-history correctness conclusion. |
| `public/` | Excluded; inventory-only SVG assets | Static visual assets; no branding, accessibility or rendered-design assessment. |
| `scripts/` | Included: `scripts/setup-tunnel.sh`, searched | Optional tunnel/DNS configuration and local token persistence; remote Cloudflare control plane excluded. No tunnel reachability conclusion. |
| `start.sh` | Included; fully read | Dependency/client/database setup, optional tunnel and development-server launch. |
| `tsconfig.json` | Included; inventory-only | TypeScript/tooling support; no typecheck result. |
| `vitest.config.ts` | Included; inventory-only | Test harness configuration, not evidence of executed tests. |

### Frozen evidence and limits

The only frozen source is SRC-1: `https://github.com/ViperrCrypto/Siftly` at **b25daa45b858f4be096b5c368671c34db4407d8e**. The supplied checkout's HEAD matched that revision; source inspection was read-only. The applicability cutoff is **2026-10-18**, the supplied run date. It is not a claim that the commit was authored that day or that later revisions behave the same way. No supplementary repository, web capture, execution trace or experiment is registered.

Overall evidence is **code-grounded**. Executable source supports implementation findings; `README.md` and `CLAUDE.md` support attributed doctrine/design. Tests are inspectable code with mocked SDK responses, not observed runs. In particular (SRC-1):

> * These test end-to-end scenarios like categorization and search
> * using the MiniMaxAIClient with mocked SDK responses.
> --- `__tests__/minimax-integration.test.ts`

External dependencies are the Next.js/React and Prisma/SQLite stacks, provider SDKs and remote model endpoints, locally installed Claude/Codex CLIs and credentials, X/browser sessions and APIs, media/link hosts, optional Cloudflare infrastructure, and an optional destination Obsidian vault. Siftly's adapter code and calls are included; dependency internals, actual accounts, user databases, external host applications and remote service implementations are not frozen. The CLI bridges invoke external executables; they do not give Siftly ownership of those runtimes' internal loops (SRC-1, `package.json`, `lib/db.ts`, `lib/ai-client.ts`, `lib/claude-cli.ts`, `lib/codex-cli.ts`, `lib/openai-auth.ts`, `lib/twitter-api.ts`, `lib/obsidian-exporter.ts`, `scripts/setup-tunnel.sh`).

There was no access failure for a material shipped source path. Available but uninspected support files are identified above, not described as unavailable. The absence of frozen provider responses, deployed databases, browser sessions and runtime traces prevents conclusions about successful authentication, actual image understanding, search precision/recall, operational throughput, restart behavior in a real deployment or downstream agent task improvement. Excluding remote dependency internals prevents attributing their scheduling, tool execution, durability or safety properties to Siftly. None of these limits removes the shipped import, maintenance or consumption paths from this whole-system boundary.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ViperrCrypto/Siftly` | b25daa45b858f4be096b5c368671c34db4407d8e | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-siftly-retry-1/related-systems/ViperrCrypto--Siftly`. Implementation: tracked tree, `package.json`, `prisma/schema.prisma`, `lib/db.ts`, `lib/fts.ts`, `cli/siftly.ts`, `app/api/import/route.ts`, `app/api/categorize/route.ts`, `app/api/search/ai/route.ts`, relevant prompt/admission/persistence ranges in `lib/categorizer.ts`, `lib/vision-analyzer.ts`, `lib/category-suggester.ts`, `lib/obsidian-exporter.ts`, `app/import/page.tsx`; `lib/ai-client.ts`, `lib/x-sync.ts`, `lib/codex-cli.ts`, `middleware.ts`, launchers and `__tests__/minimax-integration.test.ts`; bounded caller and integration searches described in the coverage table. Doctrine/design: complete `README.md` and `CLAUDE.md`. Listed paths are initial inspection, not an allowlist. | Implementation: [schema](https://github.com/ViperrCrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/prisma/schema.prisma), [pipeline](https://github.com/ViperrCrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categorize/route.ts), [search](https://github.com/ViperrCrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/search/ai/route.ts), [CLI](https://github.com/ViperrCrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/cli/siftly.ts). Doctrine/design: [README](https://github.com/ViperrCrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/README.md), [shipped instructions](https://github.com/ViperrCrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/CLAUDE.md). | No material source access gap. No observed-run or causal-experiment layer: runtime success, model quality, deployment properties and downstream task benefits are unestablished. Third-party services and runtime internals are outside the frozen source; documentation claims do not establish their behavior. |
