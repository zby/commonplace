---
description: "o-o review: polyglot HTML/bash living documents with embedded research contracts, source caches, freshness gates, index management, and Claude-only update dispatch"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# o-o

o-o is Jahala's file-native living-document system: each `.o-o.html` file is both a browser-readable article and a bash-executable updater. The file stores article content, manifest metadata, an embedded update contract, a source cache, a changelog, shared CSS/JS, and the shell runtime that can dispatch an LLM research agent to edit the document in place. It is less a memory database than a self-contained knowledge artifact with local system-definition machinery wrapped around it.

**Repository:** https://github.com/jahala/o-o

**Reviewed commit:** [b0d5063e37b4eafdbc23c1899a31f1836168b989](https://github.com/jahala/o-o/commit/b0d5063e37b4eafdbc23c1899a31f1836168b989)

**Last checked:** 2026-05-16

## Core Ideas

**The file format is the system boundary.** The README describes every `.o-o.html` file as a polyglot: browser users see the article, table of contents, citations, images, manifest-backed version badge, and client-side index/search behavior; bash skips the HTML through a heredoc and runs the shell block at the bottom ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/ai-model-landscape.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/ai-model-landscape.o-o.html)). The storage substrate is the HTML file itself. Article prose, citations, embedded images, source-cache facts, and changelog entries are knowledge artifacts when consumed as evidence or reference. The contract JSON, manifest update cadence, shell functions, shared CSS/JS markers, and CLI prompts become system-definition artifacts because they configure, route, constrain, or execute future updates.

**The update contract is embedded beside the content it governs.** Each article carries an `oo-contract` JSON block with role, procedure, identity, research intents, required sections, source policy, budget, image policy, and output constraints. The default procedure tells the agent to read the whole file, use the manifest `as_of` date, build on `oo-source-cache`, search the web, rewrite only the `<article>` and machine-readable metadata, preserve stable paragraph IDs, cite sources, and append the changelog ([example/ai-model-landscape.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/ai-model-landscape.o-o.html)). That contract has direct behavioral authority over the updater, but the authority is prompt-mediated rather than validated by a parser or schema.

**Source cache and changelog are local lineage aids, not raw trace memory.** Below `window.stop()`, article files embed `oo-source-cache` and `oo-changelog` JSON blocks. The source cache records prior URLs, titles, tiers, access dates, and extracted fact strings; the changelog records versioned summaries of update work ([example/ai-model-landscape.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/ai-model-landscape.o-o.html)). These blocks separate raw web-source evidence from article content, but they are still ordinary JSON inside the same file. They support continuity and audit at article level; they do not preserve full fetched pages, tool traces, model outputs, confidence scores, or source-to-paragraph provenance.

**The shell runtime is copied into every document.** `generate_oo_file` builds new documents by copying CSS, JavaScript, and shell sections from the current file, then writing a stub article plus manifest, contract, source cache, and changelog. `sync_section` propagates marked CSS, JS, shell, or all shared sections to sibling `.o-o.html` files and can inject a local `oo.css` customization block during CSS sync ([example/ai-model-landscape.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/ai-model-landscape.o-o.html)). This makes every document self-hosting and portable, but shared-code propagation is whole-section replacement with marker matching, not package versioning.

**Freshness gating prevents accidental spending.** The manifest stores `update_every_days`, `version`, and `as_of`; `check_freshness` parses those fields with portable shell tools and skips update dispatch while the document is still inside its freshness window unless `--force` is supplied ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/ai-model-landscape.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/ai-model-landscape.o-o.html)). Index files reuse the same logic to decide which sibling documents should be updated by `--update-all`. Freshness is a coarse scheduling gate over the article's last update date, not evidence-level invalidation.

**Index files are library managers.** Any filename beginning with `index` gets a different command role. With no action it rebuilds the card grid and table by scanning sibling `.o-o.html` files, extracting manifest fields, file size, first article paragraph, and stale/fresh status. It also exposes `--new` to create and immediately populate a new article, and `--update-all` to run stale siblings ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/index.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/index.o-o.html)). The index is a generated view and management surface over colocated living documents; it is not the canonical store.

**Backend abstraction exists in flags but not yet in implementation breadth.** The CLI accepts `--agent NAME` and `--model NAME`, and `dispatch_update` switches on the agent name, but the only implemented backend is `claude`. It checks for the `claude` command and invokes `claude -p` with allowed tools `Bash,Read,Edit,WebSearch,WebFetch`, a budget from the contract, and an optional model override ([example/ai-model-landscape.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/ai-model-landscape.o-o.html)). The README's backend language should therefore be read as a CLI affordance with one concrete dispatcher at this commit ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md)).

**Quality control is instruction-shaped.** The checked-in examples include large, current-affairs articles, source lists, fact caches, and changelogs, but the repository has no tests, package manifest, schema validation, source verifier, citation checker, or CI workflow beyond funding metadata ([example](https://github.com/jahala/o-o/tree/b0d5063e37b4eafdbc23c1899a31f1836168b989/example), [.github](https://github.com/jahala/o-o/tree/b0d5063e37b4eafdbc23c1899a31f1836168b989/.github)). The system leans on the update contract, Claude Code's editing behavior, browser rendering, and human inspection. That is coherent for lightweight living documents, but weak for high-stakes or adversarial knowledge maintenance.

## Comparison with Our System

| Dimension | o-o | Commonplace |
|---|---|---|
| Canonical substrate | One polyglot `.o-o.html` file per document | Git-tracked `kb/` collections with typed markdown artifacts |
| Primary retained content | HTML article, manifest, source cache, changelog | Notes, reviews, sources, instructions, indexes, reports |
| System-definition surfaces | Embedded contract JSON, shell functions, manifest cadence, CLI prompt, index commands | Type specs, collection rules, validation scripts, skills, review gates, generated indexes |
| Update model | Prompted web refresh by Claude Code editing the same file | Human/agent edits with validation, review, indexing, and explicit artifact lifecycles |
| Lineage | Source-cache URLs/facts and changelog summaries in the same file | Source snapshots, frontmatter, links, generated reports, git history, review state |
| Activation | Run `bash file.o-o.html`; index can create or update siblings | Agent navigation, `rg`, skills, validators, curated/generated indexes |
| Trace-derived learning | Not supported as a code-grounded finding; scheduled web refresh is not trace distillation | Treated as a separate reviewed mechanism requiring source traces and durable behavior-shaping outputs |

The strongest alignment is the file-first adoption stance. o-o keeps the article, metadata, update instructions, and runtime in an inspectable artifact that works without a server, database, build step, Python package, or Node toolchain. Commonplace similarly prefers retained artifacts that agents and humans can inspect with ordinary repo tools.

The main divergence is artifact separation. o-o deliberately collapses storage substrate, content, source cache, update contract, UI, and shell runtime into one portable file. Commonplace splits those surfaces across notes, sources, type specs, scripts, reports, and generated indexes so authority and lifecycle can differ by artifact type. o-o's monolith reduces installation cost; commonplace's separation makes review, validation, replacement, and partial retirement easier.

o-o is also more aggressive about self-updating content. A document can carry a budget, decide whether it is stale, launch a web-enabled agent, and ask that agent to change the article and metadata in place. Commonplace has stronger conventions for source snapshots and validation, but it does not make every note executable or self-refreshing.

The quality tradeoff is clear. o-o's instructions tell the agent to preserve structure and update specific zones, but there is no deterministic check that citations are current, that cached facts still support paragraphs, that source tiers are meaningful, or that shell/HTML edits preserved the polyglot contract. Commonplace would treat those as validation and review problems before granting strong behavioral authority.

## Borrowable Ideas

**Embed update intent with the artifact.** Ready to borrow in weaker form. Commonplace notes should not become executable bash documents by default, but high-churn source briefs could carry a compact refresh contract: subject, scope, source policy, freshness window, and update budget.

**Separate visible content from machine-readable continuity state.** Ready to borrow. o-o's article/source-cache/changelog split is useful even though it lives in one file. Commonplace already has source snapshots and review reports; a lightweight per-artifact freshness summary could help agents decide whether to refresh before relying on a note.

**Use freshness gates before expensive research.** Ready as an operational pattern. `update_every_days` is crude, but it prevents accidental spend and makes staleness visible. Commonplace could use similar gates for source snapshots, volatile market/product reviews, or recurring landscape notes.

**Make generated indexes actionable.** Ready to borrow selectively. o-o's index is not just navigation; it can create new documents and update stale siblings. Commonplace indexes should remain generated or curated according to their contracts, but adjacent commands can use index metadata to drive scoped maintenance actions.

**Treat shared-code propagation as a warning, not a model.** Needs stronger governance before borrowing. Marker-based `--sync all` is effective for a directory of portable documents, but commonplace should prefer package code, skills, or generated templates when behavior must be reviewed and versioned across many artifacts.

**Keep backend flags honest.** Ready as a review heuristic. o-o exposes a backend abstraction but implements only `claude`. Commonplace reviews should continue distinguishing interface shape from implemented backend breadth.

## Curiosity Pass

**The system is a living document tool more than an agent memory system.** It stores knowledge and source continuity in a way that can change future reading and future updates, but it does not provide retrieval across arbitrary memories, promotion workflows, or learned policies.

**The self-contained file is both the best idea and the main risk.** Portability is excellent: one file can render, update, clone its template, and propagate shared code. The cost is that a malformed edit can damage content, metadata, UI, and runtime together.

**The source cache is a memory aid, not an evidence archive.** It helps the next updater avoid starting from scratch, but cached URL/title/fact strings are too thin to replace retained source snapshots when factual fidelity matters.

**`window.stop()` is a practical but subtle boundary.** Browser users do not see the machine zone, while the agent is told to read it. That is a clever dual-surface design, but it relies on agents respecting hidden instructions and on browsers/tools handling the document consistently.

**The examples show ambitious current-affairs use cases.** Several example articles make time-sensitive claims about AI models, companies, politics, and markets. Those domains are exactly where freshness, source verification, and hallucination controls matter most, so the absence of deterministic checks is not incidental.

**Trace-derived status is not supported.** o-o preserves changelogs and source-cache facts from prior update runs, but the qualifying loop for trace-derived learning is absent. It refreshes web-grounded article content on a schedule; it does not mine agent session traces, tool trajectories, or feedback logs into durable rules, skills, validators, rankers, or other behavior-shaping artifacts.

## What to Watch

- Whether additional backends beyond `claude` are implemented, and whether backend-specific tool permissions and cost controls remain explicit.
- Whether source caches gain source snapshots, per-paragraph support links, confidence, or invalidation metadata.
- Whether the project adds validation for JSON zones, citation references, image size constraints, freshness fields, and polyglot shell integrity.
- Whether GitHub Actions or cron support moves from roadmap to implementation, making unattended updates and commit/PR workflows reviewable.
- Whether shared CSS/JS/shell sync gains version markers, compatibility checks, or rollback guidance.
- Whether index files evolve into multi-directory libraries or remain sibling-directory managers.

---

Relevant Notes:

- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: o-o article content, source-cache entries, and changelog summaries are consumed as evidence, context, or reference.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: update contracts, shell dispatch, freshness gates, index commands, and shared runtime sections configure or route future behavior.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - defined-in: o-o is useful because different zones in one file carry different force over future readers and updater agents.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: o-o activates knowledge by making the file executable, but activation is update-oriented rather than retrieval-oriented.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts: o-o scheduled web refresh does not qualify as trace-derived learning without a trace-to-durable-behavior artifact loop.
