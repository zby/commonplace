---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM Project Wiki's shipped bootstrap and maintenance prompt at commit 1fdfba9129a46afd18aa68a83f12d6716ab694c6."
run-id: AAS-2026-10-14-llm-project-wiki-c6c664168f3e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "1fdfba9129a46afd18aa68a83f12d6716ab694c6"
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  identity: https://github.com/akash-r34/llm-project-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-project-wiki-c6c664168f3e/related-systems/akash-r34--llm-project-wiki
  revision: "1fdfba9129a46afd18aa68a83f12d6716ab694c6"
  sha256: null
---

# LLM Project Wiki boundary

## Boundary and evidence

The target is the complete shipped prompt package for creating, maintaining and consulting a project-specific Obsidian wiki through Claude Code. Its intended use is to give later model sessions a persistent project reference instead of repeatedly reading raw code. It is in scope as a memory/knowledge/context-engineering system: its bootstrap, interpretation of sources, wiki writing and later lookup depend on the host model following instructions (SRC-1, `README.md`, `SETUP_PROMPT.md`).

> A Claude Code prompt that bootstraps a **self-maintaining Obsidian knowledge base** for any software project, and wires it as the primary reference for all future LLM work on that project.
> --- `README.md`

The boundary is **whole-system** for this shipped prompt package, not for a generated project installation or the enclosing Claude Code runtime. The tracked tree contains only `README.md` and `SETUP_PROMPT.md`; both were inspected completely at commit `1fdfba9129a46afd18aa68a83f12d6716ab694c6`. The applicability cutoff is 2026-10-14. Evidence is **doc-grounded**: the repository supplies instructions and embedded code examples, not a materialized vault, executable maintenance package or inspectable run trace (SRC-1, `README.md`, `SETUP_PROMPT.md`).

### Shipped-path coverage

| Top-level tracked path | Coverage | Role and material scope | Limit or conclusion prevented |
|---|---|---|---|
| `README.md` | Included; completely inspected | Usage entry point; new-project and existing-vault invocation; ongoing sync and ingest instructions; declared wiki-first consumption flow; attributed example output and supported-stack claims. | Example page counts and claimed capabilities are reported operation or declared intent, not demonstrated outcomes. |
| `SETUP_PROMPT.md` | Included; completely inspected | Step 0 branches between bootstrap and existing-vault audit. Phases 0–3 specify project inspection, persistent vault layers, schema, templates, index, log, health dashboard, source sync and diff-based ingest. Phase 4 specifies later callers through project instruction files, status commands and phase-completion commands. Phases 5–6 specify tracking, manuals, logging and self-audit. The gap heuristic, quality bar and Phase G specify coverage, link/schema checks, source refresh, protocol repair and audit logging. | These are instructions for model-mediated generation and maintenance. They do not establish that generated scripts, commands or future host sessions actually satisfy them. |

Functional inclusions cover the entire declared knowledge loop: producing wiki pages from project sources; retaining sources, compiled pages and activity records; selecting pages through the index; marking pages stale after code edits; updating pages through sync and diff-based ingest; resolving logged gaps; and auditing an existing vault. The specified generated callers and support files are part of the design being analyzed, even though their concrete project-specific realizations are not shipped here (SRC-1, `SETUP_PROMPT.md`).

> The governing document. A future LLM maintaining this wiki must read it first. It must define:
> --- `SETUP_PROMPT.md`

> 4. Read changed source → read wiki page → update only changed sections → bump `updated:`
> 5. Check `log.md` for open `[gap]` entries and resolve them
> 6. Create new wiki pages for any new entities introduced by the changed sources
> 7. Append ingest entry to `log.md`
> --- `SETUP_PROMPT.md`

> 1. Open `<vault path>/index.md` — use the Semantic Lookup table to navigate
> 2. Read the relevant `Wiki/` page(s) — they contain full code excerpts and cross-references
> 3. **Only if the wiki is insufficient:** fall back to existing memory files
> 4. **Only for a targeted edit:** open the actual source file
> --- `SETUP_PROMPT.md`

External dependencies are Claude Code's model, filesystem and command execution capabilities; optional Gemini instruction-file integration; the consuming project's source, memory, rules and Git history; shell utilities including rsync, grep and Git; and Obsidian with Dataview and Templater for the specified vault interface. The prompt describes these dependencies but does not ship their implementations (SRC-1, `README.md`, `SETUP_PROMPT.md`).

The enclosing host runtime is deliberately excluded: this evidence cannot establish its instruction loading, slash-command execution, context limits, scheduling or enforcement of wiki-first behavior. Consuming project code and generated vault artifacts are unavailable in this source set: the analysis cannot establish actual entity coverage, freshness, retrieval accuracy, generated-script correctness or successful persistence and reload across sessions. Dataview, Templater, Obsidian and Gemini implementations are excluded: their rendering, plugin compatibility and instruction-following behavior cannot be inferred from the prompt. The linked Karpathy gist is not part of the frozen source and was not inspected; attribution in the README does not support independent conclusions about that external proposal. No target execution or experiment was performed; effectiveness and causal improvement remain unestablished. These limits do not remove any shipped path from the prompt-package boundary (SRC-1, `README.md`, `SETUP_PROMPT.md`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/akash-r34/llm-project-wiki` | 1fdfba9129a46afd18aa68a83f12d6716ab694c6 | doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-project-wiki-c6c664168f3e/related-systems/akash-r34--llm-project-wiki`. Verified HEAD and enumerated all tracked paths. Doctrine/design: complete `README.md` and `SETUP_PROMPT.md`, including embedded sync/audit examples and all bootstrap, maintenance, consumption and repair instructions. Reported operation: README's example project and page-count account. | Doctrine/design: [README](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md), [setup prompt](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md). Reported operation: the README's “What the Wiki Contains” section at the same pinned anchor. | All tracked files inspected; no uninspected material shipped path. No concrete generated installation, host implementation, execution trace, evaluator results or causal experiment is supplied. Instructions support declared operation, not verified enforcement or effectiveness; reported counts do not establish a reproducible run. |
