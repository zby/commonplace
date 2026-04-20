---
description: Polyglot HTML/bash living-document system where each file carries its own update contract, agent dispatch, rendering, and source cache — the file is the app, with no server, database, or build step
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-05"
---

# o-o

o-o ("looky-looky") is a self-updating living document system by jahala. Each `.o-o.html` file is a polyglot — valid HTML and valid bash. Open it in a browser to read a formatted article with TOC, citations, and embedded images. Run it with `bash` to dispatch a Claude Code agent that researches the web and edits the article in-place. No build step, no server, no database. The file is the entire application: rendering, update contract, source cache, changelog, and agent dispatch shell code all live in one artifact.

**Repository:** https://github.com/jahala/o-o

## Core Ideas

**Each file is a self-contained polyglot artifact.** The `.o-o.html` file format uses a bash heredoc (`: << 'OO_HTML'`) to hide the HTML from bash while letting browsers render it normally. The file structure has four zones: (1) browser-visible HTML/CSS/JS above `window.stop()`, (2) a JSON update contract, (3) a machine-readable zone with source cache and changelog, and (4) the shell code that parses arguments and dispatches the agent. Every file carries the complete toolset — CSS, JS, and shell code are replicated across all files and synchronized with `--sync`.

**The update contract is an embedded declarative specification.** Each document contains a JSON block (`id="oo-contract"`) that specifies the agent's identity, research intents, required sections, source policy, budget cap, and image instructions. The agent reads this contract from the file itself — the prompt tells it "read this file, find the contract, follow the instructions." This means the document controls its own update behavior: what to research, how much to spend, what sections to produce.

**Agent dispatch is minimal and deliberate.** The shell code (`dispatch_update`) constructs a short prompt that tells the agent to read the file and follow the embedded contract. It passes `--allowed-tools "Bash,Read,Edit,WebSearch,WebFetch"` and `--max-budget-usd` from the contract. The agent never receives the whole file as prompt context — it reads the file through tool use and edits it surgically. This is a clean separation: the shell handles orchestration (freshness check, flag parsing, budget extraction, agent invocation), the embedded contract handles intent, and the agent handles judgment. The CLI surface looks backend-pluggable (`--agent NAME`), but the current implementation only accepts `claude`; that abstraction is prepared for expansion, not realized yet.

**Freshness gating prevents unnecessary updates.** The manifest JSON tracks `update_every_days` and `as_of` (last update date). The shell code checks whether the document is stale before dispatching the agent. If still fresh, it exits without spending money. `--force` overrides.

**Index files manage document collections.** Any file named `index*.o-o.html` acts as a library manager: it scans sibling `.o-o.html` files, extracts manifest metadata, and rebuilds a card grid and sortable table in its own HTML. It also supports `--new` (create a new document from a template and immediately run its first update) and `--update-all` (update all stale documents). The index is rebuilt from file metadata, not from a database.

**Shared code propagation via `--sync`.** CSS, JS, and shell code are wrapped in `OO:` markers (for example `<!-- OO:CSS:START -->` / `<!-- OO:CSS:END -->`). The `--sync` command extracts the canonical section from one file and replaces the corresponding section in all sibling `.o-o.html` files. This is the system's answer to code reuse without external dependencies: every file is self-contained, but shared sections can be updated in one place and propagated.

## Comparison with Our System

| Dimension | o-o | Commonplace |
|---|---|---|
| Primary purpose | Self-updating research articles | Agent-operated knowledge base |
| Storage model | Single polyglot HTML/bash files | Markdown files in a git repo |
| Knowledge structure | Flat article collections with index | Typed notes, indexes, instructions, sources, workshops |
| Agent role | Web researcher that edits articles on a schedule | Author, reviewer, maintainer, traverser |
| Agent specification | Embedded JSON contract per document | Routing table, skills, instructions, type templates |
| Learning model | No inter-document learning; each article is independent | Cross-note linking, distillation, codification, promotion |
| Update model | Periodic web research, freshness-gated | Human-triggered or task-triggered; no scheduled auto-update |
| Validation | None — the agent's output is the final product | Deterministic validation script, semantic review gates |
| Link model | None between documents except index -> article | Explicit link semantics between notes |
| Build dependencies | Bash 3.2+ and Claude Code CLI only; `--agent` is not truly generic yet | uv, Python, git, many scripts |

The systems occupy different niches. o-o is a publishing tool: it produces readable articles that stay current. Commonplace is a knowledge system: it produces interconnected notes that support reasoning. o-o's strength is radical self-containment: one file, no infrastructure. Commonplace's strength is knowledge structure — types, links, validation, and a theory of how knowledge matures.

The most interesting contrast is in how each system specifies agent behavior. o-o embeds a declarative contract in the artifact itself: the document literally tells the agent what to research, what sections to write, and how much to spend. Commonplace distributes agent specification across routing tables, skills, instructions, and type templates. o-o's approach is more portable (the contract travels with the file), while commonplace's is more composable (the specification can reference other notes and adapt to context).

## Borrowable Ideas

**Embed update contracts in artifacts.** o-o's per-document JSON contract is a clean pattern: the artifact carries its own update specification. In commonplace, this could apply to notes or sources that need periodic refresh — a `refresh` frontmatter block specifying what to check, when, and at what cost. Not ready to borrow yet; we have no scheduled update use case, but the pattern is sound if one emerges.

**Freshness gating as a cost control.** The `update_every_days` + `as_of` check is simple and effective: don't spend money if the document is still fresh. If commonplace ever adds automated maintenance passes (for example periodic review sweeps), this pattern prevents runaway costs. Ready to borrow as a principle; implementation would differ.

**File-as-app via polyglot formats.** The idea that a file can be simultaneously readable (HTML in browser) and executable (bash in terminal) is clever. In commonplace, we've kept rendering and execution separate (markdown + scripts + MkDocs). The polyglot approach sacrifices separation of concerns for radical portability. Not borrowable for our architecture, but it's a useful reference for when portability matters more than modularity.

**`--sync` for shared code across self-contained files.** The marker-delimited section sync is a practical solution to the "self-contained but DRY" tension. Our instruction/skill architecture already solves this differently (shared definitions referenced, not replicated), but the marker-based sync could be useful for template-heavy workshop scaffolds where each file needs to be self-contained. Needs a use case.

## Curiosity Pass

**The polyglot format is genuinely novel but has a ceiling.** The property it produces is radical self-containment: one file, zero dependencies beyond bash and the Claude CLI. The mechanism is real — the heredoc trick actually works, and the file genuinely functions as both HTML and bash. The simpler alternative is separate HTML + shell script + JSON config. o-o's approach wins on distribution (email one file, it just works) but loses on maintainability (every file carries about 1300 lines of shell code, CSS, and JS, synchronized by string replacement). Even if the polyglot approach works perfectly, it cannot scale beyond flat document collections — there is no mechanism for cross-document knowledge structure, and the sync approach breaks down as shared code grows.

**The update contract is specification, not distillation.** The property it claims is agent control — the document tells the agent what to do. The mechanism transforms a configuration (JSON fields) into a prompt context (the agent reads the contract and follows it). This is real constraining: the contract narrows what the agent will research and produce. But the contract is static — it does not learn from previous updates. The source cache can accumulate prior extracted facts, but there is no mechanism to refine the contract based on what worked. The simpler alternative is a prompt template with variables. o-o's embedded approach is better because it travels with the file, but the contract itself does not evolve.

**Source cache accumulation is a document-local reuse loop, not a knowledge system.** The `oo-source-cache` JSON block records prior `sources` and extracted `facts`, and the contract instructs the agent to "build on prior research, do not start from scratch." That is a real lightweight distillation step inside one document's maintenance loop: prior web research becomes a smaller reusable cache for the next run. But the loop stays local to the file. There is no contradiction resolution, no cross-document synthesis, no promotion of recurring facts into a separate shared layer, and no mechanism for one article's learning to improve another. This is enough for keeping one article current, but it is not a broader learning system.

**The index file is a genuine derived artifact, not just a listing.** The `rebuild_index` function scans sibling files, extracts metadata via grep, formats cards and tables, and writes the result back into the index file's own HTML. This is a real derivation step: structured metadata extracted from source files, transformed into a browsable index. The simpler alternative is a static list maintained by hand. o-o's approach correctly treats the index as derived state that should be regenerated from source data.

**The backend abstraction is thinner than the CLI suggests.** The property implied by `--agent NAME` is backend flexibility. The implemented mechanism is narrower: the dispatcher has one concrete branch, `claude`, and any other value errors out. The simpler alternative is to hardcode Claude and omit the flag entirely. Keeping the flag is reasonable if more backends are imminent, but today it is interface preallocation rather than a delivered capability.

## What to Watch

- Does o-o gain cross-document linking or any form of inter-article knowledge structure, or does it remain a flat collection of independent articles?
- Does the update contract evolve to include feedback from previous runs (for example "this search intent consistently returns low-quality results, deprioritize it")?
- Does the `--sync` mechanism hold up as the shared code grows, or does it become a maintenance burden that pushes toward external shared files?
- Does `--agent` become a real backend abstraction, or remain a Claude-only interface surface?
- Does the system add verification or quality gates (factual accuracy checks, source credibility scoring), or does it remain trust-the-agent?
- Does the roadmap item for GitHub Actions auto-update materialize, creating a fully autonomous document maintenance pipeline?

---

Relevant Notes:

- [Constraining](../../notes/definitions/constraining.md) — exemplifies: the embedded update contract constrains agent behavior by narrowing research scope, budget, and output structure — a deployment-time constraining mechanism
- [Files, not database](../../notes/files-not-database.md) — converges: o-o takes filesystem-first design to an extreme by collapsing renderer, updater, cache, and article into one readable file
- [Inspectable substrate, not supervision, defeats the blackbox problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — foundation: o-o keeps everything in one readable file — contract, source cache, changelog, article — making the agent's inputs and outputs fully inspectable
- [Ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) — contrasts: o-o avoids ephemeral computation by persisting source cache and changelog in the file itself, but the accumulation is raw rather than synthesized
- [Distillation](../../notes/definitions/distillation.md) — contrasts: o-o does lightweight document-local distillation into `sources` and `facts`, but it stops short of reusable cross-document knowledge artifacts
