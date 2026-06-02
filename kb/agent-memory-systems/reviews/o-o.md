---
description: "o-o review: self-contained HTML/bash living documents with embedded update contracts, source caches, changelogs, and Claude-driven web refresh"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# o-o

o-o, from Jahala's `jahala/o-o` repository, is a living-document format rather than a general memory service: each `.o-o.html` file is both a browser-readable HTML article and a bash executable that can invoke Claude Code to refresh the article from the web. At the reviewed commit, the repository contains the README and example polyglot documents; the operational code lives inside the documents themselves.

**Repository:** https://github.com/jahala/o-o

**Reviewed commit:** [b0d5063e37b4eafdbc23c1899a31f1836168b989](https://github.com/jahala/o-o/commit/b0d5063e37b4eafdbc23c1899a31f1836168b989)

**Last checked:** 2026-06-02

## Core Ideas

**The document is the app.** Each example file starts as a bash script, hides its HTML body behind a heredoc, renders as a normal article in the browser, then resumes shell execution after the `OO_HTML` terminator when run with `bash` ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). The storage substrate, UI, update policy, source history, and update command are bundled into one portable file.

**The update contract is embedded beside the article.** A JSON script block named `oo-contract` gives the research agent its role, procedure, identity, research intents, required sections, source policy, budget, image policy, and output rules ([example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). The shell dispatcher does not expand the whole contract into the prompt; it passes a short instruction telling Claude to read the file and follow that embedded contract.

**Context efficiency comes from indirection into local file reading.** The README states the agent "never receives the whole file as prompt context" and instead reads the document itself, while `dispatch_update()` sends a compact prompt containing the file path, structural boundaries, allowed edit targets, image instructions, tool allowlist, and budget ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). This reduces initial prompt volume, but complexity is still pushed onto the agent's file-reading and section-editing discipline.

**Freshness and cost are local manifest policy.** The `oo-manifest` block carries title, update cadence, version, `as_of`, and changelog metadata; `check_freshness()` reads `update_every_days` and `as_of` with portable grep/date logic and skips updates unless the document is stale or `--force` is set ([example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). The shell also extracts `max_cost_usd` from the contract and passes it to Claude's `--max-budget-usd`.

**Source cache and changelog are living-document state, not trace learning.** The machine-readable zone contains `oo-source-cache` and `oo-changelog` blocks. The contract tells the agent to preserve prior valid sources and facts, add newly used sources, increment the manifest, and append a changelog entry after each update ([example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). These are durable research state and update history, but they are derived from web/source refresh and document edits, not from agent execution traces or trajectories.

**The index document is a lightweight library manager.** Any file named `index*.o-o.html` gets extra behavior: `--new` creates a sibling document from the current file's shared CSS/JS/shell template, `--update-all` checks sibling freshness and invokes stale documents, and no-argument execution rebuilds a card/table index by scanning sibling `.o-o.html` files ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/index.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/index.o-o.html)). Shared CSS, JS, and shell blocks are synchronized across files by marker-delimited replacement.

**The system has strong adoption affordances and weak governance.** It needs bash and Claude Code, not a server, package install, database, or build step. A user can inspect, copy, open, run, and version-control one file. The tradeoff is that many high-authority operations rely on prompt compliance and regex/perl edits inside large HTML files rather than a typed parser, validator, test suite, or review gate.

## Artifact analysis

**Visible article HTML.** Storage substrate is the `.o-o.html` file in the user's filesystem or repository. Representational form is prose HTML with citations, images, paragraph ids, and references. Lineage is LLM-edited research output derived from web sources, prior article content, the embedded contract, and prior source-cache entries. Behavioral authority is mostly knowledge-artifact authority for human readers and for the future update agent when it re-reads the article as context.

**Manifest, source cache, and changelog.** Storage substrate is JSON script blocks inside the same file. Representational form is symbolic JSON with embedded prose facts and summaries. Lineage is generated or edited during each update: manifest freshness depends on `as_of` and `update_every_days`; source cache depends on the sources the agent claims it used; changelog depends on the agent's summary of the edit. Behavioral authority is mixed: the manifest has system-definition authority for freshness, versioning, and cost-saving skip behavior; source cache and changelog are knowledge artifacts that advise later updates and human inspection.

**Update contract.** Storage substrate is the `oo-contract` JSON script block inside each document. Representational form is mixed symbolic/prose: structured identity, research arrays, source policy, budget, image limits, and natural-language procedure. Lineage is authored by the template or later CLI edits; changes to this block alter future research scope, required sections, source preferences, budget, and permitted output shape. Behavioral authority is system-definition authority when the Claude update agent reads it as instructions.

**Shell dispatcher and library-manager code.** Storage substrate is the marker-delimited shell section embedded in every document. Representational form is symbolic bash plus regex/perl/sed text manipulation. Lineage is authored shared code copied between documents by `--sync`; generated documents inherit the current shell, CSS, and JS sections from the creating index file. Behavioral authority is execution, routing, configuration, and enforcement: it parses CLI flags, decides freshness, builds prompts, passes allowed tools and budget to Claude, creates documents, updates indexes, and synchronizes shared sections.

**Browser rendering code.** Storage substrate is embedded CSS and JavaScript inside the same file. Representational form is symbolic web code. Lineage is authored shared code copied by `--sync`, with optional custom CSS injection from `oo.css`. Behavioral authority is presentation and human-navigation authority rather than agent-memory authority: it renders table of contents, search/sort, theme toggles, badges, and in-browser contract display.

**Generated index view.** Storage substrate is the index document's own HTML article section. Representational form is derived HTML table/card markup. Lineage is generated by scanning sibling `.o-o.html` files for manifest fields, excerpts, file size, and freshness. Behavioral authority is knowledge-artifact authority for browsing and system-definition authority for the library manager's stale-document update loop when `--update-all` invokes siblings.

The promotion path is narrow but important. A new topic can become a generated document stub, then a Claude-populated article, then a refreshed living document whose manifest/source cache/changelog shape future refreshes. o-o does not provide a review ladder that promotes research facts into validated rules, tests, or project instructions; authority increases mainly because the same file will keep invoking its own contract.

## Comparison with Our System

| Dimension | o-o | Commonplace |
|---|---|---|
| Primary purpose | Self-updating web/source research documents | Agent-operated methodology KB with typed artifacts and validation |
| Canonical artifact | One polyglot HTML/bash document | Markdown notes, reviews, instructions, ADRs, source snapshots, generated indexes |
| Storage substrate | User filesystem/repo, one self-contained file per subject | Git-tracked `kb/` collections with separate source, note, index, report, and tool files |
| Representational form | Mixed prose HTML, JSON contracts/state, CSS/JS, bash | Mostly Markdown prose/frontmatter plus schemas, validators, skills, generated indexes |
| Lineage | Source cache, changelog, manifest dates, copied shared sections | Citations, source snapshots, replacement archives, type contracts, validation/review outputs |
| Activation | Manual `bash file.o-o.html`, index `--update-all`, or external scheduler | Agent search/navigation, skills, collection contracts, validators, review gates |
| Governance | Prompt instructions and shell conventions; no validator/test gate | Collection contracts, type specs, validation commands, review bundles, git history |

o-o and Commonplace both choose inspectable files over an opaque memory service. The strongest overlap is the idea that retained context should travel as an artifact a future agent can read directly. Commonplace spreads that across many typed files and generated indexes; o-o compresses the article, state, instructions, renderer, and executable updater into one artifact.

The strongest divergence is modularity versus portability. o-o's single-file shape is excellent for adoption: copy a file, open it, run it. Commonplace's separated collections are heavier, but they let source snapshots, notes, instructions, schemas, validators, archives, and indexes carry different authority and validation obligations. o-o's bundling makes those obligations easy to inspect locally but hard to govern independently.

The second divergence is lineage quality. o-o has a useful source cache and changelog, but the implementation trusts the update agent to maintain them. Commonplace treats source capture, citations, validation, review, and replacement archives as separate surfaces that can be checked or regenerated outside the author's prose.

Read-back: pull - a user, index command, cron job, or other external runner invokes a document, then the update agent reads the embedded contract/cache/changelog; I did not find a code-grounded relevance-gated pre-action push path, so the `push-activation` tag is not warranted.

### Borrowable Ideas

**Make small artifacts executable where the command is obvious.** Ready as a local experiment. Commonplace should not turn notes into polyglots, but a review/report artifact could advertise its exact refresh or validation command in a machine-readable block that tooling can invoke.

**Embed a compact update contract next to living content.** Ready for selected generated reports. Commonplace source reviews and recurring surveys could carry a local refresh contract that names scope, source policy, budget, and allowed mutation zones.

**Use freshness metadata to skip expensive refreshes.** Ready now where the freshness rule is simple. o-o's `update_every_days` pattern could inform generated source snapshots or recurring external-system checks, provided Commonplace records stronger lineage and validates stale decisions.

**Keep source-cache state separate from authoritative claims.** Ready conceptually. o-o usefully preserves source lists and facts for the next update, but Commonplace should keep those as source/research state until reviewed into notes or instructions.

**Do not borrow the full polyglot artifact as the default KB unit.** The single-file app is elegant for living articles, but Commonplace benefits from separate type contracts, validators, indexes, and archives. Borrow the locality of the update contract, not the loss of modular boundaries.

## Curiosity Pass

**The most distinctive artifact is a contract-bearing document, not a memory database.** o-o stores enough state to make future refreshes cheaper and more scoped, but it does not retrieve across a corpus except through the index manager's filesystem scan.

**The prompt is intentionally short, but the agent still has a complex file to interpret.** Moving the full document out of the initial prompt saves context volume. It does not remove the complexity of reading a large mixed HTML/JSON/bash artifact and respecting mutation boundaries.

**The library manager is deterministic until it invokes Claude.** Rebuilding index cards and checking staleness are shell operations; article quality, source-cache fidelity, image choice, and changelog accuracy depend on the update agent.

**Source caches are not trace-derived learning.** They are durable memory for research refresh, but they come from web sources and prior document state. Treating them as trace-derived would blur the difference between source-refresh memory and lessons distilled from agent behavior.

**The roadmap is more autonomous than the implementation.** The README mentions cron, GitHub Actions, and PR diffs, but the checked-in code implements manual shell invocation and index-driven stale updates; unattended scheduling remains an external wrapper at this commit.

## What to Watch

- Whether o-o adds validation for contract JSON, source-cache entries, changelog shape, citation consistency, and mutation-boundary compliance.
- Whether future versions record exact source URLs, accessed dates, source tiers, and source-to-claim links consistently enough to audit refreshed articles.
- Whether the planned GitHub Actions path commits diffs with enough provenance to separate source changes, article edits, cache updates, and shared-shell sync.
- Whether shared-section sync gains versioning or conflict detection so a document can tell which shell/CSS/JS generation it is carrying.
- Whether external scheduling becomes part of the implementation and whether it remains simple stale-document invocation rather than relevance-gated push activation.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: o-o requires splitting one physical file into article, contract, manifest, source cache, changelog, renderer, shell, and generated index consumption paths.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: visible articles, source caches, changelogs, and index cards mostly advise humans or future update agents as evidence/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: update contracts, freshness metadata, shell dispatch, tool allowlists, budgets, and sync/index routines carry instruction, routing, configuration, or execution force.
- [Lineage](../../notes/definitions/lineage.md) - motivates: o-o's source caches and copied shared sections need clear invalidation because generated behavior can survive after sources or templates change.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - overlaps: o-o frontloads subject, scope, source policy, budget, and mutation rules into an embedded contract that the update agent reads at execution time.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - frames: o-o reduces initial prompt volume by making the file a readable artifact, while leaving complexity-management to document structure and prompt discipline.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: o-o stores source history and update policy, but activation still depends on manually invoking the document or an external scheduler.
