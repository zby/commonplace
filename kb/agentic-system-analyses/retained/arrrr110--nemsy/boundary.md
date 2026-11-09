---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Nemsy's shipped personal knowledge assistant, CLI and Web paths at commit 2338bab0aab96a91efb90a80249f33510b630260."
run-id: AAS-2026-11-09-nemsy-2a6b7963bf65-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "2338bab0aab96a91efb90a80249f33510b630260"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/arrrr110/nemsy
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/nemsy-aba7383c4def/related-systems/arrrr110--nemsy
  revision: "2338bab0aab96a91efb90a80249f33510b630260"
  sha256: null
---

# Nemsy boundary

## Boundary and evidence

Nemsy is in scope as a model-dependent personal knowledge system. Its intended use is to turn a user's local source documents and selected conversations into a Markdown Wiki, then use retained pages to answer later questions and propose maintenance. This run covers the whole shipped product, not just the Python agent API. The frozen repository includes its CLI driver, Web backend, browser caller, prompts, storage helpers, configuration and smoke-test definitions (SRC-1: `README.md`, `pyproject.toml`, `src/nemsy/agent.py`, `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`, `tests/test_smoke.py`).

The target class is **memory/knowledge/context-engineering system**; the boundary kind is **whole-system**. That classification follows the retained-content loop, rather than the use of “Agent” in project descriptions. Python code loads existing Wiki pages into model context, requests model-generated summaries or insights, writes them into the Wiki, and updates the index. The shipped callers initiate ingest, query, chat, save and lint; they are part of the target rather than external enclosing applications (SRC-1: `src/nemsy/agent.py`, `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/FileLibrary.tsx`, `frontend/src/views/Chat.tsx`).

Minimum source passages supporting the classification and loop:

> wiki_context = _load_wiki_context(max_files=50 if wide else 10)
> --- `src/nemsy/agent.py`

> file_path.write_text(summary_content, encoding="utf-8")
>
> _update_index(source_title, filename, f"来自 {source_title} 的摘要")
> --- `src/nemsy/agent.py`

> for f in other_files[:max_files]:
>     rel = f.relative_to(settings.vault.wiki_path)
>     content = f.read_text(encoding="utf-8")
>     context_parts.append(f"=== {rel} ===\n{content}")
> --- `src/nemsy/agent.py`

Entry-point tracing started at the three script registrations in `pyproject.toml`: `nemsy.cli:main`, `nemsy.cli:smoke` and `nemsy.cli:web`. `main` dispatches commands and defaults to the chat loop. The CLI holds conversation history and a session Wiki-context snapshot, and routes ingest/save/archive requests to agent operations. The Web command starts `src/nemsy/web.py`, whose routes also implement their own chat/query prompt construction and call the LLM wrapper directly. Browser `Chat.tsx` supplies history and explicitly requests insight saving; `FileLibrary.tsx` requests source ingestion and reads retained Wiki files. These paths must be assessed separately: inclusion does not assume CLI/Web behavioral parity (SRC-1: `pyproject.toml`, `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`, `frontend/src/views/FileLibrary.tsx`).

Included state responsibilities are source-file collection and directory `_index.md` guidance; ingest status records; model-generated source summaries, query archives and conversation insights; Wiki index and operation logs; token-use logs; later Wiki-context loading; browser file and citation consumption; model-based lint suggestions; and the shipped smoke-test assertions. Page-schema text and task prompts are product instructions, unlike the repository's developer-assistant rules (SRC-1: `src/nemsy/vault.py`, `src/nemsy/schema.py`, `src/nemsy/agent.py`, `config/_index.example.md`, `.catpaw/rules`).

### Repository coverage

Every tracked top-level file or directory is classified below. “Excluded” means deliberate functional exclusion, not unavailable evidence. Initial inspection is specified rather than implying every blob was read.

| Top-level path | Classification and role | Initial inspection and limits |
|---|---|---|
| `.catpaw/` | Excluded from product operation: development-assistant rules and release-documentation skill. | Read `.catpaw/rules` and `.catpaw/skills/update-docs-after-release/SKILL.md`. These govern development, not Wiki-time maintenance; no conclusion about the effectiveness of AI-assisted development follows. |
| `.env.example` | Included: credential setup template. | Read completely; no real user credentials supplied. |
| `.gitignore` | Included: identifies ignored local runtime data and environment files. | Read completely; ignoring `.nemsy/` does not supply its contents or establish actual runtime behavior. |
| `README.md` | Included: product intent and user-facing operation instructions. | Read completely as doctrine/design, not evidence that examples succeeded. |
| `config/` | Included: runtime settings and source-directory guidance template. | Read `config/settings.toml` and `config/_index.example.md`; traced their consumers in `src/nemsy/config.py`, `src/nemsy/vault.py` and `src/nemsy/agent.py`. |
| `design/` | Excluded from claims of shipped operation: `MVP.md`, `MVP-ability.md`, `MVP-animation.md`, `MVP-frontend.md` and illustration, QR-code and screenshot assets. | Tree inspected; document bodies and images not inspected. This deliberate exclusion prevents conclusions about the detailed roadmap, proposed capabilities or screenshot-demonstrated operation. Product intent here uses the README and shipped prompts instead. |
| `frontend/` | Included: shipped browser caller and static distribution. | Read `src/main.tsx`, `src/App.tsx`, all four `src/views/` components, `src/components/MessageContent.tsx`, `src/hooks/useSSE.ts`, `src/api/client.ts`, `package.json` and `vite.config.ts`. Searched `dist/assets/index-DRPQqkgx.js` for API endpoint references; traced static mounting in `src/nemsy/web.py`. CSS, icons/images, lockfile, TypeScript/ESLint settings, frontend README and remaining HTML/build details are available but not inspected in detail. No pixel-level UI, source/bundle equivalence or build-reproducibility conclusion is established. |
| `pyproject.toml` | Included: package dependencies, optional Web dependencies, script entry points and test configuration. | Read completely; dependency implementations remain external. |
| `src/` | Included: product implementation, storage and model-call paths. | Read `src/nemsy/agent.py`, `cli.py`, `web.py`, `vault.py`, `llm.py`, `config.py` and `schema.py`; package `__init__.py` located in the tree but not inspected. Traced retention, context reload, caller admission, prompts, lint and accounting. |
| `tests/` | Included: shipped evaluation definitions. | Read `tests/test_smoke.py` and `tests/README.md`; `tests/__init__.py` located but not inspected. Tests cover basic ingest, query and query archive, and require a real API. Not executed; definitions are not passing results. |

The revision is **2338bab0aab96a91efb90a80249f33510b630260**, with applicability cutoff **2026-11-09**. The acquired checkout's HEAD matched that revision and its short Git status was empty when inspected. The overall evidence tier is **code-grounded**: implementation and declared intent are available, but this run supplies no target execution or causal experiment.

External dependencies are the model service reached through the Anthropic SDK, Python/Web/browser libraries, the host filesystem, and user-supplied documents and directory guidance. The configured service is DeepSeek's Anthropic-compatible endpoint; model-service internals and provider-side caching are outside this repository boundary. Obsidian is an optional environment for viewing the Markdown, not a prerequisite established by the product instructions (SRC-1: `config/settings.toml`, `src/nemsy/llm.py`, `pyproject.toml`, `README.md`).

No user Vault, `.nemsy` runtime records, live service responses or test execution results were supplied. These unavailable operational inputs prevent conclusions about a real collection's quality, model compliance, effective cache hits, successful deployment, measured costs or long-term knowledge improvement. They do not prevent source analysis of the shipped retention-and-consumption paths. Dependency implementations and future revisions are excluded; the run cannot establish provider guarantees, SDK internals or behavior after the pinned commit. Available but initially uninspected files in this same commit remain available to later source inspection under SRC-1; they are not access gaps.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/arrrr110/nemsy` | 2338bab0aab96a91efb90a80249f33510b630260 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/nemsy-aba7383c4def/related-systems/arrrr110--nemsy`. Implementation: package/script declarations; agent, CLI, Web, Vault, LLM, config and schema modules; browser entry, views, API client, SSE hook and reference renderer; smoke-test definitions; bounded distribution endpoint search. Doctrine/design: README, configuration and guidance template, task prompts and schema text. Developer rules inspected only to establish exclusion. Full initial coverage and non-inspection distinctions appear above. | Implementation: [entry points](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/pyproject.toml), [agent and prompts](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/src/nemsy/agent.py), [CLI caller](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/src/nemsy/cli.py), [Web caller](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/src/nemsy/web.py), [storage](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/src/nemsy/vault.py), [browser archive caller](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/frontend/src/views/Chat.tsx), [tests](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/tests/test_smoke.py). Doctrine/design: [README](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/README.md), [directory guidance](https://github.com/arrrr110/nemsy/blob/2338bab0aab96a91efb90a80249f33510b630260/config/_index.example.md). | No checkout access gap identified. No supplied observed run or causal experiment; test code and prompt constraints do not establish successful execution or model obedience. External service behavior and user-local retained state are unavailable; no empirical effectiveness, provider guarantee or deployed-state conclusion. |
