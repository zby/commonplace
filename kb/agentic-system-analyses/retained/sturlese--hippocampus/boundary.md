---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Hippocampus's shipped personal-knowledge vault framework at commit 99531951ae60a9814ac7d27a32dd00f0c81a5008, including agent workflows, lifecycle hooks, maintenance and retrieval contracts."
run-id: AAS-2026-11-08-hippocampus-30a5ab9b2a87-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "99531951ae60a9814ac7d27a32dd00f0c81a5008"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/sturlese/hippocampus
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/hippocampus-739e5cf901e6/related-systems/sturlese--hippocampus
  revision: "99531951ae60a9814ac7d27a32dd00f0c81a5008"
  sha256: null
---

# Hippocampus boundary

## Boundary and evidence

This run analyses the shipped Hippocampus framework for turning personal sources and conversation conclusions into a persistent, cross-linked Markdown vault and reading that knowledge in later agent sessions. The target is a **memory/knowledge/context-engineering system**, not an enclosing model runtime. Its model-dependent operations are specified by project instructions and skills for external Claude Code and Codex hosts. Its executable components provide lifecycle bookkeeping, deterministic structural checks and framework synchronization (SRC-1: `CLAUDE.md`, `.claude/skills/ingest/SKILL.md`, `.claude/skills/save/SKILL.md`, `scripts/on-stop.sh`, `scripts/vault_lint.py`, `scripts/sync_framework.sh`).

> The user drops messy notes into `inbox/`; the agent turns
> them into a structured, cross-linked knowledge base under `wiki/`.
> --- `CLAUDE.md`

The boundary is **whole-system** for this repository's shipped framework. It includes both host adapters, canonical ingest/save/lint prompts, schema and page skeletons, original-source archiving, catalog/journal/cache upkeep, question-answer read order, session-start reload, stop-time persistence and the framework update/export path. It does not narrow the target to the Python linter or omit the prompts that produce and consume retained state. The source tree and shipped callers were traced from `AGENTS.md` to `CLAUDE.md`, from skill adapters to canonical skills, from host hook configuration to `scripts/on-stop.sh`, and from the lint skill to `scripts/vault_lint.py` (SRC-1: those paths and `.agents/skills/ingest/SKILL.md`, `.agents/skills/save/SKILL.md`, `.agents/skills/lint/SKILL.md`, `.claude/settings.json`, `.codex/hooks.json`, `.claude/skills/lint/SKILL.md`).

The later-consumption path is explicitly shipped, even though its execution belongs to the external host:

> 1. Read `wiki/hot.md` — recent context may already answer it.
> 2. Read `wiki/index.md` — pick the 3–5 relevant pages.
> 3. Read those pages; follow wikilinks at most one hop further.
> --- `CLAUDE.md`

`CLAUDE.md` also supplies a search fallback and instructions for another agent project to consult the vault. Both host configurations print the hot cache at session start and invoke the shared stop hook. The hook checks file modification times, can return a refresh request, and stages content roots before a local commit. These are implementation findings, not evidence that either host executed the configuration successfully (SRC-1: `CLAUDE.md`, `.claude/settings.json`, `.codex/hooks.json`, `scripts/on-stop.sh`).

> if [ "$stop_active" -eq 0 ] && [ -f wiki/hot.md ]; then
> --- `scripts/on-stop.sh`

External dependencies are the model and agent host, their instruction/skill loading, permissions, native file/web tools and hook protocol; Git; Bash and shell utilities; and Python for the linter. Obsidian is the optional browsing consumer. Their implementations are not part of this repository. Consequently the run can characterize the shipped contracts and hook logic but cannot establish host compliance, actual model extraction or retrieval quality, prompt-injection resistance, browser behavior, or compatibility across host versions. Framework synchronization code is in scope, but the live upstream revisions it would fetch are not evidence for this run (SRC-1: `README.md`, `CLAUDE.md`, `.claude/settings.json`, `.codex/hooks.json`, `scripts/sync_framework.sh`).

### Tracked-root coverage

Every top-level tracked file or directory is classified below. “Included” denotes inspected source text unless explicitly identified as an empty scaffold. There is no material shipped loop path left uninspected. Every path in this table belongs to SRC-1.

| Top-level path | Coverage | Material paths and role | Exclusion or evidence limit |
|---|---|---|---|
| `.agents/` | Included | `.agents/skills/ingest/SKILL.md`, `.agents/skills/save/SKILL.md`, `.agents/skills/lint/SKILL.md`: Codex adapters redirect to canonical workflows. | Establishes adapter text, not host loading. |
| `.claude/` | Included | `.claude/skills/ingest/SKILL.md`, `.claude/skills/save/SKILL.md`, `.claude/skills/lint/SKILL.md`: model-operated production and maintenance; `.claude/settings.json`: session-start consumer, stop-hook driver and permissions. | Prompt prescriptions are doctrine/design, not executed transformations. |
| `.codex/` | Included | `.codex/hooks.json`: alternate session-start cache injection and shared stop-hook driver. | External hook interpretation is not observed. |
| `.gitignore` | Included | `.gitignore`: excludes machine-local state, hook errors and template markers from tracking. | Does not supply those local files or their contents. |
| `.obsidian/` | Included | `.obsidian/app.json`, `.obsidian/core-plugins.json`: browsing/link/attachment settings; `.obsidian/appearance.json`, `.obsidian/graph.json`, `.obsidian/snippets/vault-colors.css`: display configuration. | Obsidian's implementation and actual rendering are outside the source. |
| `AGENTS.md` | Included | `AGENTS.md`: Codex entry point delegating the project contract to `CLAUDE.md`. | No observed loading. |
| `CHANGELOG.md` | Included | `CHANGELOG.md`: attributed release and adapter history. | Release assertions are not execution evidence. |
| `CLAUDE.md` | Included | `CLAUDE.md`: canonical schema, layout, retrieval, contradiction handling, operations, persistence expectations and cross-project consumer instructions. | Does not implement or prove model obedience. |
| `LICENSE` | Included | `LICENSE`: distribution terms. | No operational evidence. |
| `README.md` | Included | `README.md`: setup, intended use, dependencies, triggers, framework/content separation and template marker setup. | Marketing and performance claims remain declared claims. |
| `_attachments/` | Included scaffold | `_attachments/.gitkeep`: attachment root; referenced by `.obsidian/app.json`, `scripts/on-stop.sh` and `scripts/vault_lint.py`. | Empty placeholder identified by tree; no attachment corpus is supplied. |
| `_templates/` | Included | `_templates/source.md`, `_templates/entity.md`, `_templates/concept.md`, `_templates/project.md`, `_templates/note.md`: persisted page skeletons, provenance and type-specific fields. | Schemas/templates do not demonstrate populated-page quality. |
| `assets/` | Deliberately excluded | `assets/hippocampus.png`, `assets/hippocampus-dual-agent.png`: README illustrations; listed in the tracked tree, not image-inspected. | No conclusions about image content or visual architecture depictions. No shipped state-producing or consuming code resides here. |
| `docs/` | Included | `docs/README.md`, `docs/what-happens-when-you-ingest.md`, `docs/why-no-vector-db.md`: pipeline walkthrough, reverse read path and design rationale. | Source-native explanation, not independent measurement or proof of comparative superiority. |
| `inbox/` | Included scaffold | `inbox/_done/.gitkeep`: archived-original root; production/archive policy traced in `.claude/skills/ingest/SKILL.md`, persistence in `scripts/on-stop.sh`. | Empty placeholder identified by tree; no real ingest inputs or archived originals available. |
| `scripts/` | Included | `scripts/on-stop.sh`: freshness request and persistence; `scripts/vault_lint.py`: all structural checks and CLI reporting; `scripts/sync_framework.sh`: update/diff/export and content boundaries. | Read completely, not executed; synchronization destinations and fetched revisions excluded. |
| `wiki/` | Included | `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`: initial cache, catalog and journal; `wiki/concepts/.gitkeep`, `wiki/entities/.gitkeep`, `wiki/meta/.gitkeep`, `wiki/notes/.gitkeep`, `wiki/projects/.gitkeep`, `wiki/sources/.gitkeep`: empty content roots identified by tree. | Scaffold only, not a populated private vault, execution trace or evaluation dataset. |

The frozen evidence is repository commit `99531951ae60a9814ac7d27a32dd00f0c81a5008`; the applicability cutoff is **2026-11-08**. Overall evidence is **code-grounded** because hook, linter and synchronization implementations and their shipped drivers were inspected. Semantic ingest, save, retrieval and editorial maintenance remain instruction-grounded within that overall tier. No target execution was performed. The tracked tree supplies no test/evaluation suite or observed-run artifacts; the linter is a structural evaluator, with the lint skill supplying an editorial procedure, not a retrieval benchmark (SRC-1: `scripts/vault_lint.py`, `.claude/skills/lint/SKILL.md`, `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`). These limits prevent claims of measured reliability, recall, latency, scalability or successful end-to-end operation; they do not prevent source-level analysis of the complete shipped framework.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sturlese/hippocampus` | 99531951ae60a9814ac7d27a32dd00f0c81a5008 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/hippocampus-739e5cf901e6/related-systems/sturlese--hippocampus`. Implementation: complete `scripts/on-stop.sh`, `scripts/vault_lint.py`, `scripts/sync_framework.sh`, both host hook configurations and `.obsidian/` configuration. Doctrine/design: complete root Markdown files, all three canonical skills and three adapters, all five templates, all three docs and initial `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`; tracked tree and `.gitignore`. | Implementation: [stop hook](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/scripts/on-stop.sh), [linter](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/scripts/vault_lint.py), [framework sync](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/scripts/sync_framework.sh), [Claude wiring](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/.claude/settings.json), [Codex wiring](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/.codex/hooks.json). Doctrine/design: [project contract](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/CLAUDE.md), [ingest](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/.claude/skills/ingest/SKILL.md), [save](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/.claude/skills/save/SKILL.md), [lint](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/.claude/skills/lint/SKILL.md), [source template](https://github.com/sturlese/hippocampus/blob/99531951ae60a9814ac7d27a32dd00f0c81a5008/_templates/source.md). | Frozen checkout reachable and commit verified; no material source access failure. External host/model/Obsidian implementations, populated private vaults and observed executions are unavailable within this source set, preventing behavioral and performance verification. Image assets deliberately uninspected as recorded above, not an access gap. No observed-run or causal-experiment layer is claimed. |
