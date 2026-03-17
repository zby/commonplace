---
description: Obsidian-vault CLI with NAPKIN.md pinned context, TF-IDF overviews, agent-shaped search defaults, and pi-based auto-distill — clearest reference for adapting Obsidian into an agent memory interface
type: note
traits: [has-comparison, has-implementation]
tags: [related-systems]
status: current
last-checked: 2026-03-17
---

# Napkin

Napkin is a TypeScript/Bun CLI for Obsidian-compatible markdown vaults. It treats a local vault as an agent memory system with a progressive-disclosure command ladder: `NAPKIN.md` as pinned context, `napkin overview` as a vault map, `napkin search` as ranked partial retrieval, and `napkin read` as full resolution. The repo is currently hosted at `the-shift-dev/napkin`, but package metadata and some docs still point at `Michaelliv/napkin`, which suggests the project is in the middle of a stewardship or transfer transition rather than at a fully stable packaging boundary.

**Repository:** https://github.com/the-shift-dev/napkin

## Core Ideas

**Obsidian compatibility is the adoption strategy.** Napkin does not ask users to migrate into a new knowledge substrate. It creates a `.napkin/` vault inside a project, stores plain markdown, syncs config into `.obsidian/`, and operates directly on files. The bet is that agent memory adoption gets easier if the same notes remain inspectable to humans in familiar Obsidian tooling.

**Progressive disclosure is implemented as a real command ladder, not just a design slogan.** The four levels are explicit in the code and docs: `NAPKIN.md` for pinned context, `overview` for folder summaries, `search` for ranked snippets, and `read` for full content. The overview extracts weighted TF-IDF keywords per folder from headings, filenames, frontmatter titles, and body text. Search indexes basename plus content with MiniSearch, then boosts results with backlink counts and recency.

**The CLI is tuned for model psychology rather than human preferences.** Napkin hides search scores by default because models anchor on numbers, defaults snippets to zero surrounding lines because every token costs context, and prints hint lines telling the agent the cheapest next step. This is one of the clearest examples in the surveyed systems of treating tool output formatting itself as part of the context-engineering problem.

**It uses Obsidian's higher-level affordances as an agent query layer.** Napkin does not stop at CRUD over notes. It reads tags, tasks, bookmarks, canvas files, and `.base` files. The Bases support is especially notable: it parses `.base` YAML, builds an in-memory SQLite table from markdown files and frontmatter, and translates Obsidian-style formulas into Jexl. That gives agents a structured query surface without changing the underlying file substrate.

**LLM-dependent automation is kept outside the core CLI.** The core tool is intentionally LLM-free. Automatic context injection and conversation distillation live in `pi` extensions. The distill extension forks the current session, spawns a separate `pi` subprocess with a distillation prompt, and tells that subprocess to use `napkin` commands plus vault templates to create or append notes. This is a clean architectural boundary: file operations stay deterministic, model judgment stays optional and external.

## Comparison with Our System

| Dimension | Napkin | Commonplace |
|---|---|---|
| Primary substrate | Real markdown files in a `.napkin/` vault, designed to stay Obsidian-compatible | Real markdown files in a repo-first KB, designed for explicit agent authorship and git review |
| Always-loaded context | `NAPKIN.md`, plus optional `pi` extension that injects overview into the session | `AGENTS.md`/`CLAUDE.md` routing layer plus skill descriptions |
| Progressive disclosure | Hard-coded tool ladder: `NAPKIN.md` -> `overview` -> `search` -> `read` | Routing + descriptions + indexes + search; the ladder is distributed across conventions rather than one CLI |
| Search strategy | MiniSearch over basename/content with backlink-count and recency boosts; snippets tuned for agents | `rg` + descriptions + indexes + explicit link phrases |
| Link model | Obsidian wikilinks and backlinks; links are navigational but semantically thin | Standard markdown links with explicit relationship semantics |
| Knowledge structure | Template-defined folder shapes, frontmatter, tasks, tags, Bases views | Typed notes (`note`, `structured-claim`, `adr`, `index`, `related-system`) with methodology around when each shape is warranted |
| Human/agent coexistence | Very strong: same vault is comfortable for Obsidian users and agents | Strong for agents and maintainers, but less optimized for drop-in use with mainstream note-taking tooling |
| Learning theory | Mostly operational and ergonomic; no explicit theory of distillation, promotion, or codification | Explicit theory of context engineering, distillation, constraining, and codification |

The systems are closer in spirit than in interface. Both are local-first, file-based, and skeptical of vector-heavy memory stacks. The difference is where each system commits its structure. Napkin commits more into tooling ergonomics: command ladders, output defaults, template scaffolds, Obsidian compatibility. Commonplace commits more into the documents themselves: typed note forms, description quality, link semantics, and theory-driven distinctions between distillation and codification.

Napkin is strongest where we are still comparatively thin: agent-shaped UX on top of a general markdown substrate. We are stronger where Napkin stays loose: explicit semantic links, type-driven curation, and a theory for when a pattern should remain prose versus harden into stronger forms.

## Borrowable Ideas

**Hide ranking scores in agent-facing search by default.** Napkin's score-hiding choice is small but well-argued: the ranker can use scores without letting the model over-trust them. This is ready to borrow now anywhere we expose ranked retrieval or candidate lists to an agent.

**Treat hint text as control flow, not as help text.** Napkin's `HINT:` footer lines explicitly tell the agent the next cheapest action after `overview` or `search`. We already rely on progressive disclosure conceptually; this is a concrete way to encode the workflow directly into tool output. Ready to borrow now.

**Keep LLM automation as an extension boundary around a deterministic core.** The distill extension is the right architectural instinct even when the knowledge quality is uneven. If we add background reflection, workshop capture, or auto-promotion later, keeping that logic outside the core file-manipulation toolchain would preserve inspectability and failure isolation. Ready to borrow now as a boundary principle.

**Offer a lightweight query layer over markdown metadata.** Napkin's Bases support suggests a useful middle ground between pure grep and a database-backed KB: build a temporary queryable table from markdown plus frontmatter when a task needs structured slicing. This is not ready to borrow blindly, but it is a strong candidate once we have recurring dashboard-like queries over workshop or task artifacts.

**Use domain templates to scaffold workshop spaces, not just note folders.** Napkin's templates encode folder shapes plus starter files and templates for different work modes. We should not copy the domain taxonomy directly, but the mechanism is borrowable if we decide to make workshops more scaffolded. Needs a concrete workshop use case first.

## Curiosity Pass

**Obsidian compatibility is more interface adaptation than representation change.** The property it produces is adoption ease: humans and agents can use the same vault. Mechanistically, Napkin mostly relocates an existing Obsidian substrate behind an agent-friendly CLI rather than transforming the substrate into a new knowledge form. The simpler alternative is "just use `rg` and scripts on an Obsidian vault." Napkin's answer is that the interface defaults matter enough to justify a dedicated tool. I think that claim holds, but the value is in UX shaping, not in inventing a new storage model.

**The progressive-disclosure ladder is real, but the middle layer is only as good as the vault's metadata hygiene.** The property is context-efficient navigation. The mechanism does transform raw files into lower-resolution pointers: weighted TF-IDF folder summaries and ranked snippets. That is a real distillation step. But the docs slightly overclaim the ranking mechanics: they describe "PageRank via backlinks," while the implementation currently uses raw inbound-link counts as a booster, not graph propagation. The simpler alternative is a directory tree plus grep. Napkin's overview layer is better than that, but its ceiling is still governed by filename quality, heading quality, and backlink hygiene.

**The agent-shaped CLI defaults are the strongest genuinely novel idea in the repo.** The property is better agent behavior under context constraints. Unlike many "agent-ready" claims, these defaults are not just naming: hiding scores, defaulting to match-only snippets, and printing next-step hints all directly alter what the model sees. The simpler alternative is a human-oriented CLI plus docs. Napkin shows that defaults are load-bearing when the consumer is an LLM.

**The Bases layer is a compatibility bridge, not a foundation.** The property is structured querying over markdown. The mechanism mostly relocates markdown metadata into an in-memory SQLite table and formula engine long enough to answer a query. That is a pragmatic bridge to Obsidian's ecosystem, not a deeper knowledge model. The simpler alternative is direct grep or custom scripts for each query. Napkin's approach wins when users already have `.base` files and expect them to work, but its rebuild-the-world-per-query design probably caps out at small-to-medium vault scales.

**Distill is architecturally clean but epistemically weak.** The property is background knowledge capture without contaminating the core CLI. The mechanism is real: a timer notices changed conversation state, forks the session, and runs a separate model invocation that uses templates and `napkin` commands to write notes. But even if it works perfectly, the ceiling is limited. It can extract and route potentially useful notes; it cannot reliably judge truth, resolve contradictions, or synthesize durable concepts without stronger verification layers. It is closer to structured capture than to the fuller [distillation](../distillation.md) sense we use in this KB.

**The repo still shows transition seams.** The remote is `the-shift-dev/napkin`, but `package.json`, CLI docs, and some URLs still point to `Michaelliv/napkin`. That mismatch does not break the mechanism, but it is a maintenance signal. Systems that present themselves as memory infrastructure need tight packaging and identity boundaries, because agents will copy commands and URLs verbatim.

## What to Watch

- Does the overview/search ladder stay useful once a vault becomes messy, heterogeneous, and large, or does the TF-IDF layer degrade into generic folder keywords?
- Does distill gain stronger verification and deduplication, or remain an extraction-and-routing helper with limited epistemic strength?
- Do template-specific extractors and richer overview logic actually land, or does the current generic folder summarization remain the long-term design?
- Does the project consolidate the repo/package identity split between `the-shift-dev` and `Michaelliv`, or is the fork/transfer state still in motion months from now?

---

Relevant Notes:

- [Instruction specificity should match loading frequency](../instruction-specificity-should-match-loading-frequency.md) — foundation: Napkin's `NAPKIN.md` -> overview -> search -> read ladder is a concrete tool-level implementation of the same loading hierarchy
- [Always-loaded context has two surfaces with different affordances](../always-loaded-context-has-two-surfaces-with-different-affordances.md) — extends: Napkin's injected overview plus CLI hint text make the always-loaded/tool-output boundary especially explicit
- [Pointer design tradeoffs in progressive disclosure](../pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: Napkin supplies concrete examples of fixed pointers (overview keywords) and query-time pointers (search snippets), and shows how output defaults change their usefulness to agents
- [Distillation](../distillation.md) — contrasts: Napkin's auto-distill captures and routes structured notes, but does not yet provide the stronger synthesis and task-specific compression this note argues for
- [Inspectable substrate, not supervision, defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — foundation: Napkin keeps the substrate inspectable because even its richer querying and automation still terminate in plain files
- [OpenViking](./openviking.md) — contrasts: both systems make progressive disclosure first-class, but OpenViking virtualizes a database behind a filesystem metaphor while Napkin stays on a real markdown vault and focuses on agent-shaped CLI ergonomics
- [The wikiwiki principle: lowest-friction capture, then progressive refinement in place](../wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) — exemplifies: Napkin inherits the wiki/Obsidian assumption that capture should stay cheap and refinement should happen in the same file substrate
