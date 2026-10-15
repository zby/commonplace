---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "llm-context-base's shipped knowledge-base template and instruction-driven maintenance loop at commit 6d01cba8e2c22f9ca2519c70073a05cd54378a8c."
run-id: AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "6d01cba8e2c22f9ca2519c70073a05cd54378a8c"
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  identity: https://github.com/asakin/llm-context-base
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-context-base-f63a7c0fb5f2/related-systems/asakin--llm-context-base
  revision: 6d01cba8e2c22f9ca2519c70073a05cd54378a8c
  sha256: null
---

# llm-context-base boundary

## Boundary and evidence

This run analyses llm-context-base as a template for an LLM-maintained personal knowledge base. Its intended use is to retain captures, knowledge, decisions, projects and personal context in files, then have a file-capable assistant reload, query and maintain those files. The target is a **memory/knowledge/context-engineering system**, not an enclosing agent runtime. Its model-dependent operation is prescribed by shipped prompts consumed by external AI tools. The absence of an internal model-call implementation does not remove the instruction-driven knowledge loop from scope (SRC-1, `README.md`, `PHILOSOPHY.md`, `docs/supported-tools.md`).

The target explicitly separates its substrate from the host:

> **The repo stays dumb. The intelligence lives outside it.**
> --- `PHILOSOPHY.md`

> **No runtime.** The repo doesn't run. It exists. Sophisticated behaviors — monitoring the web, creating PRs, integrating with external services — belong in the intelligence layer above.
> --- `PHILOSOPHY.md`

The **whole-system** boundary covers the shipped substrate: tool bootstrap prompts and recommended permissions; session initialization and phase-sensitive context loading; configuration and learned preferences; capture and source preservation; metadata, templates and admission/completion instructions; query and decision-precedent consumption; lint and instruction optimization; project indexes and logs; Obsidian capture settings and the clipper template; and the metadata migration utility. This is whole-system coverage of the template's material shipped responsibilities, not of the external hosts that act on them (SRC-1, `AGENTS.md`, `_config/config.md`, `_meta/instructions/general.md`, `_meta/instructions/agent-write.md`, `_meta/instructions/knowledge-query.md`, `_meta/instructions/knowledge-lint.md`, `migrate-to-yaml-frontmatter.py`).

Entry-point inspection traced all six bootstrap files to the shared configuration and general module. Those prompts belong to the target even though their consumers execute outside the repository. The generic bootstrap declares:

> Follow the Session Start Protocol defined in `_config/config.md`, then `_meta/instructions/general.md`. All instructions are there.
> --- `AGENTS.md`

The general module connects conversation output to retained state, including instructions and preferences:

> The rule: **when something new is established in conversation, update the relevant file immediately.**
> --- `_meta/instructions/general.md`

The later query path explicitly consumes retained content:

> Read the 1-3 most relevant files in full. For very large files (500+ lines), focus on the first major section.
> --- `_meta/instructions/knowledge-query.md`

Accordingly, the boundary includes both the writing and later reading instructions, rather than treating the write API or metadata format alone as the system. It includes the supplied lint and completion criteria as prescribed evaluation paths, not as demonstrated independent evaluators. The tracked tree contains no separate test suite, benchmark harness or observed agent trace; the sample records are examples, not measured operation (SRC-1, `_meta/instructions/definition-of-done.md`, `_meta/instructions/knowledge-lint.md`, `examples/example-decision-record.md`).

### Coverage of the tracked top level

All rows concern SRC-1 at the reviewed commit. “Included, inspected” denotes source-text inspection, not execution. Deliberately excluded supporting material remains available at the same commit; it is not an access gap. Empty placeholders were identified through the tracked tree. No material loop path is left uninspected.

| Top-level file or directory | Treatment and material paths | Role and limits |
|---|---|---|
| .claude | Included, inspected: `.claude/CLAUDE.md`, `.claude/settings.json` | Claude bootstrap to shared prompts; recommended permissions. Host enforcement and model behavior are external. |
| .cursor | Included, inspected: `.cursor/rules/bootstrap.mdc` | Cursor bootstrap to shared prompts; actual discovery is not observed. |
| .cursorrules | Included, inspected: `.cursorrules` | Legacy Cursor bootstrap with the same shared destinations. |
| .github | Included, inspected: `.github/copilot-instructions.md` | Copilot bootstrap. The tracked directory contains no shipped Actions evaluator or synchronization workflow. |
| .gitignore | Included, inspected: `.gitignore` | Default persistence exclusions for journal, private material, outputs, local tools, overrides and framework-mode flag. Ignore rules do not establish confidentiality from an AI host. |
| .obsidian | Included, inspected: `.obsidian/app.json`, `.obsidian/core-plugins.json`, `.obsidian/daily-notes.json`, `.obsidian/templates.json` | New-note admission to inbox, attachment placement, journal template and enabled core facilities. Deliberately excluded, not inspected: appearance, graph and CSS presentation settings; no conclusions about visual rendering or graph usability. |
| .windsurfrules | Included, inspected: `.windsurfrules` | Windsurf bootstrap to shared configuration and session instructions. |
| 1-Projects | Included, inspected: `1-Projects/README.md`, `1-Projects/_parked/README.md`; empty shipped archive placeholder identified in tree | Project indexes and active/parked/shipped lifecycle; actual downstream project artifacts are not supplied. |
| 2-Knowledge | Included, inspected: `2-Knowledge/README.md`, `2-Knowledge/log.md`; empty HowTo, Decisions and References placeholders identified in tree | Retained knowledge destinations and operations log. No populated user corpus for retrieval-quality assessment. |
| 3-Journal | Included, inspected: `3-Journal/README.md` | Journal role and default local-only persistence; actual entries are absent, preventing assessment of real journal use or privacy outcomes. |
| 4-Private | Included, inspected: `4-Private/README.md` | Sensitive-content destination; no private corpus or enforcement trace supplied. |
| AGENTS.md | Included, inspected: `AGENTS.md` | Generic tool bootstrap, framework-mode branch and naming/metadata conventions. |
| CODE_OF_CONDUCT.md | Deliberately excluded, not inspected | Community conduct policy; no conclusions about community governance or enforcement. |
| CONTRIBUTING.md | Included, inspected: `CONTRIBUTING.md` | Genericizing learned patterns for upstream contribution; framework-development mode and bootstrap synchronization. Not proof that local changes are safely genericized. |
| LICENSE | Deliberately excluded, not inspected | Legal terms; no licensing interpretation. |
| PHILOSOPHY.md | Included, inspected: `PHILOSOPHY.md` | Declared purpose, substrate/host separation and evolution guidance loaded during early usage phases. |
| README.md | Included, inspected: `README.md` | Setup and user-triggered capabilities; personal/framework README split. Performance and adaptation claims remain attributed intent. |
| WIKI-LOG.md | Included, inspected: `WIKI-LOG.md` | Append-only structural-change log, containing a template initialization entry, not a run trace. |
| _config | Included, inspected: `_config/config.md`, `_config/context.md`, `_config/standard.md`, `_config/tools.md` | Profile, training controller/log, retained personal context, metadata and query/write contracts, optional tool manifest. The local framework-mode flag is not a tracked file at this pin. |
| _inbox | Included, inspected: `_inbox/README.md` | Capture, type-based filing and seven-day triage nudge. No captured user items are supplied. |
| _meta | Included, inspected: `_meta/instructions/general.md`, `_meta/instructions/agent-write.md`, `_meta/instructions/knowledge-query.md`, `_meta/instructions/knowledge-lint.md`, `_meta/instructions/definition-of-done.md`, `_meta/instructions/optimization-review.md`, `_meta/instructions/blog-posts/instructions.md`; all seven shipped templates | Session loading; state production, review/admission, consumption and maintenance; article, decision, initiative, journal, meeting, inbox and blog shapes. Criteria are instructions for the host assistant, not code-enforced gates. |
| _output | Included, inspected: `_output/README.md` | Consumption into one-off exports and presentations; default exclusion from Git. Renderer implementation and generated artifacts are absent. |
| _sources | Included, inspected: `_sources/README.md`; empty placeholder identified in tree | Optional retained originals for later reprocessing; no originals supplied, preventing re-ingestion assessment. |
| assets | Included, inspected: `assets/clipper-template.json`; empty placeholder identified in tree | Shipped external-clipper input template, date naming and inbox routing; template content does not use the canonical YAML frontmatter format. External clipper execution is not observed. |
| docs | Included, inspected: `docs/supported-tools.md`, `docs/claude-code-setup.md`, `docs/obsidian-setup.md`, `docs/journal-sync.md`, `docs/linked-code-repos.md`, `docs/faq.md` | Host setup, optional compact/reload hook recipes, external sync, journal persistence alternatives, and linked-code consumers. Remaining explanatory/design/future/training/metadata/directory/extension pages deliberately not inspected; no independent findings based on those pages. No material shipped executable driver was excluded. |
| examples | Included, inspected: `examples/example-decision-record.md`, `examples/example-inbox-capture.md`, `examples/example-initiative.md`, `examples/example-knowledge-article.md` | Sample retention shapes, outcome fields and cross-links. Sample narratives do not establish real outcomes or system effectiveness. |
| migrate-to-yaml-frontmatter.py | Included, inspected: `migrate-to-yaml-frontmatter.py` | Standalone Python maintenance entry point: recursive Markdown scan, legacy metadata conversion and file rewrite. Not a model caller or the agent loop; not executed. |

### Dependencies, exclusions and evidence limits

External dependencies include a file-capable LLM assistant and its filesystem/shell tools for the prescribed loop; Git/GitHub for versioning, optional upstream updates and hosted sync; Obsidian and its browser clipper for optional human capture/viewing; Marp for optional rendered outputs; and optional journal encryption or external synchronization tools. The target ships instructions and configuration for these integrations, not their implementations (SRC-1, `docs/supported-tools.md`, `docs/obsidian-setup.md`, `docs/journal-sync.md`, `_config/tools.md`).

The host owns model selection, inference, instruction discovery, context-window handling, actual filesystem operations and permission enforcement. These responsibilities are excluded; the boundary cannot establish reliable prompt adherence, isolation, security or cost across Claude Code, Cursor, Copilot, Windsurf or other hosts. Built-in Claude memory outside the repository, referenced in the FAQ, is likewise not target-retained state (SRC-1, `.claude/settings.json`, `docs/supported-tools.md`, `docs/faq.md`).

Documented hooks, connectors, MCP servers, third-party plugins and linked code repositories are included only as shipped recipes or integration expectations. No separate source has been acquired for them. Their implementation, uptime, privacy guarantees and correctness cannot be concluded here. In particular, the optional hook script described in the Claude setup page is not a tracked shipped script; the linked-code scaffold has no executable implementation in this tree (SRC-1, `docs/claude-code-setup.md`, `docs/linked-code-repos.md`).

The frozen evidence is Git commit **6d01cba8e2c22f9ca2519c70073a05cd54378a8c**, verified as the checkout's HEAD, with applicability cutoff **2026-10-14** from the supplied opening record. No live pages, dependencies, other repositories or later revisions are included. The overall tier is **doc-grounded** because the knowledge loop is defined by prompts and documentation, not an inspected internal model-calling runtime. The migration utility supplies a bounded implementation layer for metadata conversion only. No target execution, tests, provider calls or experiments were performed. These limits prevent conclusions about observed adaptation, retrieval accuracy, maintenance reliability, causal improvement or production-scale performance.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/asakin/llm-context-base` | 6d01cba8e2c22f9ca2519c70073a05cd54378a8c | doctrine/design; implementation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-context-base-f63a7c0fb5f2/related-systems/asakin--llm-context-base`. Doctrine/design: all six bootstrap files, shared configuration, all instruction modules and templates, content-directory READMEs and logs, sample records, and the host/setup docs listed in the coverage table. Implementation: metadata migration Python source; declarative Obsidian and clipper settings inspected as configuration, without executing their consumers. | Doctrine/design: [bootstrap](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/AGENTS.md), [session and routing](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/general.md), [write](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/agent-write.md), [query](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/knowledge-query.md), [lint](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/_meta/instructions/knowledge-lint.md), [substrate boundary](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/PHILOSOPHY.md). Implementation: [migration utility](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/migrate-to-yaml-frontmatter.py); configuration: [clipper template](https://github.com/asakin/llm-context-base/blob/6d01cba8e2c22f9ca2519c70073a05cd54378a8c/assets/clipper-template.json). | No access gap in the frozen tracked tree. External host/plugin/service implementations and user corpora are outside this source; no observed run or causal experiment is supplied. Doctrine supports prescribed behavior only; migration source supports static executable behavior only. Deliberate supporting-file exclusions are identified above and are not evidence of unavailable files. |
