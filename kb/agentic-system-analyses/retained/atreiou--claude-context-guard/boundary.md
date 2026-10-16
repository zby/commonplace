---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Claude Context Guard's shipped prompts, templates, installer and hooks at efcd0a1815887483a862b32bfb3fbfd6aac79aa6."
run-id: AAS-2026-10-13-claude-context-guard-357cd90664df-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: efcd0a1815887483a862b32bfb3fbfd6aac79aa6
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/atreiou/claude-context-guard
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/claude-context-guard-357cd90664df/related-systems/atreiou--claude-context-guard
  revision: efcd0a1815887483a862b32bfb3fbfd6aac79aa6
  sha256: null
---

# Claude Context Guard boundary

## Boundary and evidence

Claude Context Guard is in scope as a memory/knowledge/context-engineering system for Claude Code projects. Its intended use is to retain project state outside a conversation and reload it in later sessions. The shipped model-facing commands create, update, rotate, retrieve and audit that state. This is not an enclosing model runtime: Claude Code supplies model execution, tool dispatch, command discovery and hook events. The classification covers the complete shipped package, not just its shell hooks (SRC-1, `README.md`, `.claude/commands/start.md`, `.claude/commands/save.md`, `.claude/commands/end.md`).

> **Persistent context protection for Claude Code projects.**
> --- `README.md`

> 0. **`RESUME_STATE.md`, READ THIS FIRST.** This file holds only the in-flight state from the last /save. If `Clean save: false`, the previous session was interrupted mid-task, and the In-flight and Next step sections are your handoff note. Surface this in the Step 4 summary under a `🔄 Resume from last session` heading so the user knows you picked it up. If `Clean save: true`, the previous session ended cleanly and RESUME_STATE is empty, so the next-session intent lives in SESSION_LOG's newest "Next step".
> --- `.claude/commands/start.md`

The `whole-system` boundary includes installation into consumer projects; first-run safeguard creation; ordinary-session incremental maintenance instructions; checkpoint and end-of-session writes; archive rotation and indexes; later-session recovery; user-directed lesson admission; code-address and sidecar generation and maintenance; model-directed integrity audits and report retention; and executable pre-commit reminders and pre-compaction file backups. Shipped prompts are operational material, but their instructions establish intended model behavior, not demonstrated compliance. Shell source supplies the executable portion of the evidence (SRC-1, `install.sh`, `templates/CLAUDE.md`, `.claude/commands/start.md`, `.claude/commands/save.md`, `.claude/commands/end.md`, `.claude/commands/lessons.md`, `.claude/commands/itemise.md`, `.claude/commands/audit.md`, `.claude/settings.json`, `.claude/hooks/pre-commit-check.sh`, `.claude/hooks/pre-compact-save.sh`).

> **Do not write, install, or delete anything before the user answers.**
> --- `.claude/commands/lessons.md`

The source is frozen at commit `efcd0a1815887483a862b32bfb3fbfd6aac79aa6`; the analysis cutoff is 2026-10-13. The overall evidence tier is `code-grounded`, with doctrine/design evidence for model-operated procedures. Inspection traced the installer to all six commands, both hooks, conditional settings installation and all eight templates, then traced persistence and consumption through those commands and the project-instruction template. All tracked text files were read in full. The tracked tree has no separate test suite or executable evaluator; the shipped `/audit` prompt and `/itemise` verification instructions are included as evaluation procedures, not executed evaluation results (SRC-1, `install.sh`, `.claude/commands/audit.md`, `.claude/commands/itemise.md`).

### Tracked top-level coverage

| Top-level file or directory | Status and inspected material paths | Role and limits |
|---|---|---|
| `.claude/` | Included; fully inspected `commands/start.md`, `commands/save.md`, `commands/end.md`, `commands/audit.md`, `commands/lessons.md`, `commands/itemise.md`, `hooks/pre-commit-check.sh`, `hooks/pre-compact-save.sh`, `settings.json` beneath this directory | Shipped entry points for creation, retention, admission, recovery, audit, code navigation and hook integration. All six prompts, both shell hooks and their event wiring belong to the boundary. Prompt inspection cannot establish host/model compliance. |
| `templates/` | Included; fully inspected `CLAUDE.md`, `COMMENTS.md`, `DECISIONS.md`, `FEATURE_LIST.json`, `LEARNED_BEHAVIOUR.md`, `RESUME_STATE.md`, `SESSION_LOG.md`, `TASK_REGISTRY.md` beneath this directory | Initial retained-state formats, maintenance rules, read instructions, archive indexes, task provenance and human-verified feature status. These are templates, not populated consumer histories. |
| `install.sh` | Included; fully inspected | Installs commands, hooks, settings and templates, with optional parent-directory deployment. Inspection does not establish success in any consumer environment. |
| `README.md` | Included; fully inspected | Declared purpose, installation, usage and design claims. Claims of reliable recovery or token savings remain declarations without run evidence. |
| `.gitignore` | Included; fully inspected | Distinguishes generated consumer safeguards, archives, plans, audits, backups and local settings from tracked package content. It does not supply those generated artifacts. |
| `Assets/` | Deliberately excluded; `Images/CCG vs Claude 'Init'.jpg` and `Images/CCG vs Claude Auto-Memory.jpg` not inspected | Comparison illustrations, not shipped persistence or consumption paths. This analysis cannot assess their visual comparisons or use them as evidence of superiority over Claude Code features. |

Coverage roles above are grounded in SRC-1 at `install.sh`, `README.md`, `.gitignore`, the named `.claude/` paths and the named `templates/` paths. The image exclusions do not exclude any identified state-producing, state-maintaining or state-consuming entry point.

External dependencies are Claude Code and its model/tool capabilities, a local writable filesystem, Bash and shell utilities, and Git plus remotes when the configured version-control mode uses them. Consumer project source files, scratch scripts, helper libraries, custom context files and host-generated plans are inputs to the shipped procedures, not supplied frozen evidence. Human confirmation controls several operations, including lesson admission and feature QA (SRC-1, `install.sh`, `.claude/settings.json`, `.claude/commands/start.md`, `.claude/commands/lessons.md`, `.claude/commands/save.md`, `templates/CLAUDE.md`, `templates/FEATURE_LIST.json`).

Claude Code internals, provider behavior and consumer deployments are outside the source boundary. No host implementation, populated consumer ledger, execution trace or causal experiment was supplied. These gaps prevent conclusions about actual recall, loss-free recovery, model adherence, measured token use, backup restoration, cross-platform reliability or comparative performance. Referenced external research and moving live documentation are not acquired sources. Their findings cannot support this run. Available text not yet inspected is not being presented as an access gap; none remains among tracked text files.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/atreiou/claude-context-guard` | efcd0a1815887483a862b32bfb3fbfd6aac79aa6 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/claude-context-guard-357cd90664df/related-systems/atreiou--claude-context-guard`. Implementation: complete `install.sh`, `.claude/settings.json`, `.claude/hooks/pre-commit-check.sh`, `.claude/hooks/pre-compact-save.sh`, and `.gitignore`. Doctrine/design: complete `README.md`, all six `.claude/commands/*.md` files and all eight `templates/` files listed in the coverage table. Inspected tree confirms the package layout. | Implementation: [installer](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/install.sh), [settings](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/settings.json), [backup hook](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/hooks/pre-compact-save.sh), [commit reminder](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/hooks/pre-commit-check.sh), [ignore rules](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.gitignore). Doctrine/design: [README](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/README.md), [recovery](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/commands/start.md), [checkpoint](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/commands/save.md), [rotation](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/commands/end.md), [audit](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/commands/audit.md), [lesson admission](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/commands/lessons.md), [itemisation](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/.claude/commands/itemise.md), [project instructions](https://github.com/atreiou/claude-context-guard/blob/efcd0a1815887483a862b32bfb3fbfd6aac79aa6/templates/CLAUDE.md). Other template anchors: `templates/COMMENTS.md`, `templates/DECISIONS.md`, `templates/FEATURE_LIST.json`, `templates/LEARNED_BEHAVIOUR.md`, `templates/RESUME_STATE.md`, `templates/SESSION_LOG.md`, `templates/TASK_REGISTRY.md`, all at this same revision. | No source-checkout access gap. Deliberately excluded images prevent visual-comparison assessment. Host implementation and generated consumer artifacts are unavailable within this frozen source; no observed-run or causal-experiment layer is supplied. Implementation supports source-level shell behavior, not successful host execution; doctrine/design supports specified procedures, not achieved retention or recovery. |
