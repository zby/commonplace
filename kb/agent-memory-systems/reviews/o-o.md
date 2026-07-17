---
description: "o-o review: polyglot HTML/bash living documents with embedded update contracts, source caches, changelogs, sync shell, and Claude CLI dispatch"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# o-o

o-o, from `jahala/o-o`, is a file-native living-document pattern: each `.o-o.html` file is both a browser-readable HTML article and a Bash program that can ask Claude Code to update that article in place. At the reviewed commit, the repository contains the README and example documents; the implemented system lives inside those example files as shared CSS, JavaScript, shell functions, update contracts, source caches, and changelogs.

**Repository:** https://github.com/jahala/o-o

**Reviewed commit:** [b0d5063e37b4eafdbc23c1899a31f1836168b989](https://github.com/jahala/o-o/commit/b0d5063e37b4eafdbc23c1899a31f1836168b989)

**Source directory:** `related-systems/jahala--o-o`

## Core Ideas

**The document is the application and the store.** The README's central claim is implemented literally: there is no package tree, server, database, or build system; the examples are self-contained `.o-o.html` polyglots with an HTML article above a rendering boundary and shell code below it ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). The retained artifact is therefore a single inspectable file, not a separate memory service.

**The update contract is embedded beside the content it governs.** Each article carries an `oo-contract` JSON block naming the research role, procedure, subject, scope, audience, tone, intents, required sections, source policy, budget, image policy, and output constraints ([example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). This contract is system-definition state for future update agents because the shell prompt tells the agent to read it as the complete instruction surface.

**Previous research is retained as article, manifest, source cache, and changelog.** The visible article and references are browser-facing knowledge artifacts; `oo-manifest` records title, update cadence, version, and `as_of`; `oo-source-cache` records previous sources and facts; `oo-changelog` records update history ([example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html)). The update contract instructs later agents to build on the source cache rather than restart from scratch.

**The shell is the orchestrator, not just a launcher.** Shared shell functions generate new documents, rebuild index cards and tables, update all stale documents, sync shared CSS/JS/shell blocks across siblings, edit contract fields, and dispatch Claude with a small prompt plus allowed tools ([example/index.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/index.o-o.html)). Any `index*.o-o.html` file becomes the library manager for sibling documents.

**Context efficiency is pointer-first.** The shell does not paste the whole retained document into the model prompt. It passes the file path and a compact instruction to read the contract, manifest, source cache, and changelog from disk, then asks the agent to use targeted edits ([README.md](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/README.md), [example/index.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/index.o-o.html)). This keeps initial prompt volume low, but the eventual context size and search cost are delegated to the agent's file reads and web research.

**Trust is inspectable but lightly governed.** The file keeps citations, a source cache, update dates, and changelog entries, and its browser CSP restricts external resources to inline styles/scripts and data images in the examples. There is no validator, source-span checker, contradiction policy, or test that the updated article faithfully reflects its retained sources.

## Artifact analysis

- **Storage substrate:** `files` — The central retained state is the `.o-o.html` file itself: article HTML, manifest JSON, contract JSON, source cache JSON, changelog JSON, shared JavaScript, and shared shell. Index state is another `.o-o.html` file rebuilt from sibling files, and images are embedded as data URLs rather than stored in a separate asset service ([example/anthropic-leadership.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/anthropic-leadership.o-o.html), [example/index.o-o.html](https://github.com/jahala/o-o/blob/b0d5063e37b4eafdbc23c1899a31f1836168b989/example/index.o-o.html)).
- **Representational form:** `prose` `symbolic` — Article text, references, source-cache facts, changelog summaries, and the Claude prompt are prose; JSON manifests/contracts/caches, HTML ids, stable paragraph comments, shell functions, CLI flags, freshness checks, and sync markers are symbolic. I found no vector store, embedding index, learned ranker, or model-weight artifact in the repository.
- **Lineage:** `authored` `imported` — The shared shell/JS/CSS template and update instructions are authored. Article content, citations, embedded images, source-cache entries, and fact lists are imported or derived from web sources during update runs. The code does not retain raw agent session transcripts or tool traces as the source of later behavioral artifacts, so I am not classifying it as trace-learning.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` — Articles, source caches, citations, and changelogs are knowledge artifacts for human readers and future update agents; the contract and dispatch prompt instruct the updater; filenames, index detection, required sections, update cadence, CLI flags, and sync markers route work; freshness checks and basic file-exists/marker checks validate whether to update or sync.

**Article file.** The operative object is a bundle: visible article content, citations, document metadata, update contract, prior-research cache, changelog, rendering JavaScript, and executable shell. Its strength is that the behavior-shaping state travels with the readable document. Its weakness is that one file mixes durable knowledge, runtime orchestration, UI, and write policy, so accidental broad edits can damage several authorities at once.

**Update contract.** The `oo-contract` JSON block is stronger than ordinary prose documentation because the shell prompt explicitly instructs the update agent to treat it as the instruction source. It controls the future update's subject boundary, source policy, sections, budget, image handling, and allowed mutation area.

**Source cache and changelog.** These are compact memory surfaces for future updates. They preserve previous sources and facts well enough for incremental research, but they are not provenance-complete: source-cache facts are not tied to exact article spans, source quotes, retrieval timestamps per fact, extraction prompts, or confidence states.

**Shared shell and sync markers.** The shell block is a system-definition artifact copied across sibling documents by marker replacement. The promotion path is unusual: editing any one file's shared section and running `--sync` can promote that file's shell/JS/CSS into every sibling, but there is no repository-level release gate inside o-o itself.

## Comparison with Our System

o-o and Commonplace both treat plain files as behavior-shaping memory for agents. The difference is granularity and authority. Commonplace separates notes, sources, reviews, instructions, type specs, generated indexes, validation, and review reports. o-o deliberately collapses article, memory cache, prompt contract, UI, and executable updater into one portable file.

That collapse is attractive for adoption. A single file can be opened, inspected, copied, run, scheduled, and versioned in git without a server. It is also risky for methodology knowledge: update authority is mostly delegated to an LLM with a contract and budget, while Commonplace relies on type contracts, validation, semantic review, and explicit source-grounded replacement workflows.

The closest Commonplace analogue is a workshop artifact that carries its own update prompt, source cache, and generated summary. o-o is weaker as a canonical library artifact because it lacks type-level validation and source-span lineage, but stronger as a low-friction artifact that can keep a time-sensitive report current without a separate app.

### Borrowable Ideas

**Self-contained update contract.** Commonplace could let selected workshop artifacts carry an embedded update contract naming source policy, allowed sections, budget, and mutation boundaries. Ready for temporary reports, not for canonical notes without review gates.

**Pointer-first agent dispatch.** Passing a file path plus a compact instruction keeps initial context small and lets the agent inspect only the zones it needs. Commonplace can use the same pattern for large source snapshots and review bundles.

**Sibling sync markers.** Marker-delimited shared sections are crude but effective for a family of single-file artifacts. Commonplace should not copy shell code through notes, but the marker idea could help generated report templates or standalone HTML exports.

**Inline source cache plus changelog.** A compact previous-research cache would be useful for recurring external landscape reports. It needs stronger source-fact linkage before it should influence durable methodology notes.

## Write side

**Write agency:** `manual` `automatic` — A user manually creates, opens, edits, syncs, configures, or runs a document; the shell automatically decides freshness, calls Claude, rebuilds index content, creates new files from templates, syncs shared sections, and edits contract fields. The actual research update is an agentic automatic write mediated by the embedded contract.

**Curation operations:** `evolve` — The implemented update path modifies an existing retained article, manifest, source cache, and changelog in place in light of newly gathered web information and the previous cache. Index rebuild and shared-section sync are access-structure/template maintenance rather than memory-content curation. I did not find implemented deduplication, decay, contradiction invalidation, or synthesis across multiple stored o-o documents.

The system is not trace-learning under the current review contract. It retains products of prior update work, but the durable content is sourced from web research and document state rather than distilled from session logs, tool traces, trajectories, or repeated agent rollouts.

## Read-back

**Read-back:** `pull` — The retained article, contract, source cache, and changelog re-enter the updater only when the invoked agent reads the file path it was given. The shell prompt pushes a pointer and instructions, but it does not inject stored memory content into an unrelated agent context, and the repository does not implement automatic relevance matching or always-load memory outside the chosen document.

This makes o-o a strong example of pointer-mediated context efficiency. It avoids paying prompt tokens for the whole document at launch, but it also relies on the agent to inspect the right zones, respect mutation boundaries, and decide how much prior content to load.

## Curiosity Pass

**The shell prompt is intentionally smaller than the contract.** The README says the updater gets a minimal prompt and reads the file itself; the code matches that by placing the detailed policy in `oo-contract` and only passing the file path plus high-level procedure to Claude.

**The source cache is more memory-like than the article.** The visible article is the user-facing product, but the future updater is specifically told to read previous sources and facts. That small cache is the closest thing to agent memory in the system.

**Shared code propagation is powerful and unsafe.** `--sync shell` can replace the executable updater block in sibling documents. That is convenient for a file swarm, but it turns one edited document into a distribution point for future write behavior.

**The examples contain current-affairs claims but no verification harness.** The article format encourages citations and changelogs, yet no checked-in script verifies citation resolution, source freshness, image provenance, paragraph-id preservation, or article/contract consistency.

## What to Watch

- Whether the roadmap's cron and GitHub Actions paths become checked-in workflows. That would shift o-o from manually invoked pull updates toward scheduled autonomous maintenance.
- Whether the diff-viewer roadmap becomes an implemented review gate. That would make automatic article evolution more auditable.
- Whether source-cache facts gain per-fact source ids, quote anchors, or article-span links. That would materially improve lineage.
- Whether additional agent backends are implemented beyond the `claude` case. That would test whether the file contract is portable or Claude-Code-specific.
- Whether multi-document update logic starts synthesizing across sibling `.o-o.html` files. That would change the curation classification from single-document evolution toward library-level synthesis.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: o-o stores rich document memory but relies on explicit file reads rather than automatic memory injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the `.o-o.html` file bundles knowledge, instruction, routing, validation, UI, and shell authorities in one substrate.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: article content, source caches, citations, and changelogs primarily serve as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: the update contract, shell router, freshness checks, sync markers, and dispatch prompt shape later agent behavior.
- [A functioning KB needs a workshop layer not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: o-o is closest to a self-updating workshop artifact whose value is consumed and refreshed over time.
