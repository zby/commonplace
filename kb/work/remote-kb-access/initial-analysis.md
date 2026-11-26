# Initial analysis: accessing Commonplace via GitHub or the rendered HTML site

Captured 2026-11-26 from inspecting [README.md](../../../README.md), [kb/index.md](../../index.md), [kb/README.md](../../README.md), [properdocs.yml](../../../properdocs.yml), [properdocs_hooks.py](../../../src/commonplace/docs/properdocs_hooks.py), [site_links.py](../../../src/commonplace/docs/site_links.py), and collection landings. Candidate changes below are options to evaluate, not adopted commitments.

## 1. Structural diagnosis

Commonplace's discovery model ([ADR 025](../../reference/adr/025-complete-generated-indexes-are-build-time-only.md), [ADR 140](../../reference/adr/140-tag-heads-are-selective.md)) rests on two local access paths: curated heads plus scoped `rg` over frontmatter for agents, and ProperDocs build-time listings plus browser find for humans. When accessed remotely without cloning or installing — the mode advertised in [README.md](../../../README.md#consult-the-research-with-your-agent) — those assumptions break for both consumers.

A recursive count of Markdown files under `kb/` (excluding `kb/sources/.snapshots/` and `kb/workflow-state/data/`, measured 2026-11-26) shows **6,243** files:

- **Core readable KB (~520 files):** `theory/` (464), `tags/` (35), `articles/` (13), `notes/` (7)
- **System and procedures (~410 files):** `reference/` (265), `instructions/` (126), `types/` (21)
- **Bulk, in-flight, or historical (~5,300 files):** `agentic-system-analyses/` (2,977), `work/` (1,090), `sources/` (631), `reports/` (272), `agent-memory-systems/` (175), `agentic-systems/` (156), plus `tasks/` (5), `workflow-state/` (2), `messages/` (1), and top-level `index.md`, `README.md`, `log.md`

Both the GitHub repository and the rendered site expose the ~5,300 bulk, in-flight, or historical pages alongside the ~520 core pages, while offering no remote equivalent of `rg` over `description:` frontmatter.

## 2. External agents (web fetch or GitHub without cloning)

1. **Build-time `llms.txt` at site root (`https://zby.github.io/commonplace/llms.txt`).**
   - Currently absent. A compact (~2–5 KB) machine-oriented entry file could name:
     - which collections carry transferable doctrine (`theory/`, `articles/`, `agentic-systems/comparisons/`) vs. Commonplace-specific contracts (`reference/`, `instructions/`) vs. exploratory or historical material (`work/`, `agent-memory-systems/`);
     - where the topic index and metadata catalogs live;
     - how to fetch raw Markdown instead of HTML, and when to prefer `git clone --depth 1` plus `rg` if the agent has a shell.
2. **Compact build-time metadata catalog for core collections.**
   - ProperDocs's stock `search/search_index.json` is client-side JS and indexes full page bodies across thousands of pages, making it oversized and noisy for remote agent fetches.
   - Emitting a slim build-time catalog (for example `catalog/theory.tsv` or `.json` with `path`, `title`, `description`, `tags`, `type`, `user-verified` for `theory/`, `articles/`, `tags/`, `reference/`, and `agentic-systems/`) would total roughly 100 KB for `theory/` and restore `ADR 025`'s selective `title + description` triage over HTTP.
3. **Clean Markdown access from the rendered site.**
   - Fetching rendered HTML pages pulls navigation chrome, sidebars, and Giscus script markup into bounded agent context. Emitting raw `.md` companions at build time — or explicitly documenting the `raw.githubusercontent.com/zby/commonplace/main/kb/...` path mapping in `llms.txt` and `README.md` — reduces fetch overhead and preserves YAML frontmatter.
4. **Keep rendered tag heads lightweight while keeping full membership one click away.**
   - [properdocs_hooks.py](../../../src/commonplace/docs/properdocs_hooks.py) appends the full `## Tagged artifacts by collection` listing directly onto each `tags/<tag>-README.html`. For tags with over 100 members, a web-fetching agent opening the curated head pays linear context cost on the entire generated tail. Splitting the generated listing onto a sibling page (linked from the head) preserves lightweight head reads for agents while keeping complete membership accessible to human browsers.
5. **Strengthen the consultation protocol and signpost `AGENTS.md`.**
   - [README.md](../../../README.md#consult-the-research-with-your-agent) currently offers one example prompt and four bullets, including *"Browse ongoing investigations (`./kb/work/`)"* without warning that `work/` holds 1,090 exploratory or unadopted files.
   - A short consultation guide could provide problem-to-collection routing, evidence-weighting guidance (`theory/` vs. `reference/` vs. `agentic-system-analyses/` vs. `work/`), and copy-pasteable prompts.
   - A two-line pointer at the top of [AGENTS.md](../../../AGENTS.md) can route read-only consulting agents away from the 14 KB of maintainer rules when they clone or inspect the repository.

## 3. Human readers on `https://zby.github.io/commonplace/`

1. **Improve search and top-level navigation signal-to-noise.**
   - **Search:** [properdocs.yml](../../../properdocs.yml) uses the stock `search` plugin with no collection weighting or faceting. Searches for terms like "memory" or "review" mix core `theory/` and `articles/` with 2,977 analysis sub-files, 1,090 `work/` drafts, 631 `sources/` ingests, 175 frozen `agent-memory-systems/` files, and potentially `reports/` (which is omitted from nav via `UNPUBLISHED_COLLECTIONS` but not listed in `exclude_docs`). Scoping default search exclusions or switching to a static faceted search index (such as Pagefind) would separate durable reading from bulk appendix material.
   - **Top nav:** `on_config` in [properdocs_hooks.py](../../../src/commonplace/docs/properdocs_hooks.py) generates 11 flat top-level items in alphabetical order (`Home`, `Tags`, `Agentic Systems`, `Articles`, `Instructions`, `Notes`, `Reference`, `Sources`, `Theory`, `Work`, `GitHub`). Grouping into reader tiers — core reading (`Tags`, `Articles`, `Theory`, `Agentic Systems`), system docs (`Reference`, `Instructions`, `Notes`), and appendix (`Sources`, `Work`) — would make collection roles visible immediately.
2. **Render build-time backlinks ("Referenced by") on each page.**
   - Already designed in [backlink-surfacing.md](../../reference/proposals/backlink-surfacing.md) based on [inbound and outbound links serve asymmetric reader needs](../../theory/inbound-and-outbound-links-serve-asymmetric-reader-needs.md). Because `contradicts`, `contrasts`, and `extends` links are often one-sided, build-time inbound links give web readers visibility into extensions and counterexamples without committing generated footers.
3. **Add link hover previews from frontmatter `description`.**
   - Every note already carries a validated 50–250 character `description`. Exposing that description on internal links (for example via `site_links.py` attributes or a small tooltip asset) applies [agents navigate by deciding what to read next](../../theory/agents-navigate-by-deciding-what-to-read-next.md) to human web reading by supplying information scent before a click.
4. **Upgrade page framing, authority banners, and GitHub source links.**
   - Replace raw type paths (`**Type:** types/note.md`) rendered by `on_page_markdown` in [properdocs_hooks.py](../../../src/commonplace/docs/properdocs_hooks.py) with readable labels, and surface `description` as a subtitle and HTML `<meta name="description">`.
   - Render explicit collection banners on `kb/work/` (exploratory, not adopted doctrine) and `kb/agent-memory-systems/` (historical and frozen) so visitors arriving via search or deep links know the page's status.
   - Configure `repo_url` or inject per-page **"View source on GitHub"** and **"Open an issue"** links so readers can inspect history or contest a claim directly.
5. **Add problem-oriented entry paths alongside the tag index.**
   - [kb/tags/README.md](../../tags/README.md) organizes 35 tags by Commonplace's own conceptual vocabulary (*Constraining*, *Artifact analysis*, *Method-guided action*). Pairing it with 4–5 task-oriented reading tracks on [kb/index.md](../../index.md) (such as designing agent memory, preventing prompt/instruction drift, building a project LLM wiki, and reading the continual-learning research) lowers entry friction for newcomers.

## 4. GitHub repository browsing (`github.com/zby/commonplace`)

1. **Fix build-time-only links that 404 on GitHub.**
   - [kb/agentic-systems/README.md](../../agentic-systems/README.md) links to `../agentic-system-analyses/current-analyses.md`, which is materialized only in ProperDocs memory (not present on disk) and returns 404 when clicked on GitHub. Audit other links to build-time-only pages (`systems.md`, `dir-index.md`) for the same failure.
2. **Make [kb/README.md](../../README.md) navigable on GitHub.**
   - GitHub renders `kb/README.md` whenever someone opens `kb/`, whereas ProperDocs shadows it with `kb/index.md`. Currently `kb/README.md` lists collection paths in backticks with no clickable links and does not point to [kb/index.md](../../index.md), [kb/tags/README.md](../../tags/README.md), or the rendered site.
3. **Bridge selective tag heads on GitHub to full membership.**
   - Because `kb/tags/*-README.md` heads are selective ([ADR 140](../../reference/adr/140-tag-heads-are-selective.md)) and lack build-time tails on GitHub, [kb/tags/README.md](../../tags/README.md) can document how a remote GitHub reader enumerates a tag (either on the rendered site or via GitHub code search).

## 5. Suggested first empirical step

Before investing in larger ProperDocs changes, run a bounded diagnostic test: give a fresh external agent access **only** to `https://zby.github.io/commonplace/` and `https://github.com/zby/commonplace` (no local clone), run the consultation prompt from [README.md](../../../README.md#consult-the-research-with-your-agent) against a real target repository, and record where the agent stalls, burns context on HTML or tag tails, misses relevant theory, or misinterprets `kb/work/` as settled doctrine. Use those observed failure modes to prioritize which fixes to implement first.
