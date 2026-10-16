---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Claude Workstream Kit's shipped work-state lifecycle, prompts, scripts and evaluators at commit 15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64."
run-id: AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/ChristopherA/claude-workstream-kit
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-claude-workstream-kit/related-systems/ChristopherA--claude-workstream-kit
  revision: "15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64"
  sha256: null
---

# Claude Workstream Kit boundary

## Boundary and evidence

### Target and intended use

The target is the complete shipped Claude Workstream Kit: project-local instructions, skills, agent definitions, hooks, state formats, measuring and rewriting utilities, installer and acceptance drivers. Its intended use is preserving multi-session work state in repository files and returning that state to a Claude Code session. This is an in-scope memory/knowledge/context-engineering system, not an enclosing model runtime. The retained content includes work goals, tasks, decisions, learnings, closure criteria and a resume pointer; the model-facing skills prescribe how to write, maintain and later consume it. SRC-1, `README.md`, `.claude/rules/workstreams-rule.md`, `.claude/skills/workstream-work/SKILL.md`.

> A workstream is a unit of multi-session work — a feature, an exploration, a migration — tracked in two small markdown files committed to your repo:
> --- `README.md`

> Read `.state/ACTIVE.md` and the active `workstream.md` first, then announce "Resuming <name> at <task>".
> --- `.claude/skills/workstream-work/SKILL.md`

The boundary is **whole-system** because it includes the shipped producers, maintainers and consumers of work state, not only the Python measurement API. The installer deploys the payload and seeds missing state. Creation, work and capture skills prescribe persistence; review and extract prescribe maintenance; closure prescribes extraction, tagging and deletion. SessionStart reloads the pointer and derives workstream signals. Status reads retained records across workstreams; handoff supplies cross-project filing and receiving instructions. These responsibilities are inside the target even where a model, rather than a script, carries out the instruction. SRC-1, `install.sh`, `.claude/skills/workstream-create/SKILL.md`, `.claude/skills/workstream-capture/SKILL.md`, `.claude/skills/workstream-review/SKILL.md`, `.claude/skills/workstream-extract/SKILL.md`, `.claude/skills/workstream-close/SKILL.md`, `.claude/hooks/session-start.sh`, `.claude/skills/workstream-status/SKILL.md`, `.claude/skills/handoff/SKILL.md`.

> State files are committed in the session that changes them — uncommitted state does not survive to other machines or future triage.
> --- `.claude/rules/workstreams-rule.md`

> Every resolved Learning and settled Open Question ends in exactly one of: **applied** to a named file outside `.state/` (cite it; make the edit now if it is missing), **handed off** via `/handoff` (in this run, not "later", and through that skill's own gate, which this skill names and does not pass), or **dropped** with stated rationale, in place.
> --- `.claude/skills/workstream-extract/SKILL.md`

### Coverage of tracked top-level paths

The tracked tree and shipped entry points were inspected at the frozen commit. “Included” specifies analysis scope, not a claim that every line has already been examined. Initial inspection below distinguishes full reads, selected implementation ranges and bounded searches. Unread detail remains available under SRC-1; it is not an access gap.

| Top-level path | Treatment and material paths | Role and initial inspection; consequence of exclusion |
|---|---|---|
| `.claude/` | Included: `CLAUDE.md`, `rules/workstreams-rule.md`; all nine `skills/` directories, their `references/failures.md` and creation templates; `agents/{scout,worker,verifier}.md`; `settings.json`; both `hooks/`; all five `scripts/` files | Model instructions, state lifecycle, delegation, host registration, reload, output admission, measurement, rewrite and context telemetry. Full reads of the rule, settings, work/extract/close skills, workstream template, hooks and forwarding shim; bounded searches of the other skills and agents; selected implementation reads in record, rewrite and status-line scripts, and function/pattern searches of the shared state module. References and remaining implementation detail are included but not yet read in full. SRC-1, `.claude/settings.json`, `.claude/scripts/workstream_state.py`, `.claude/skills/workstream-extract/SKILL.md`. |
| `.gitignore` | Included | Repository hygiene: ignores Python bytecode. Read in full. No persistence guarantee is inferred from this ignore rule. SRC-1, `.gitignore`. |
| `.public-sweep-allow` | Included as maintainer metadata, not an installed runtime component | Publication-sweep exceptions. Header and bounded searches inspected. Its named external checker is unavailable in this repository; the allowlist cannot establish that private-content leakage is prevented. SRC-1, `.public-sweep-allow`. |
| `.state-seed/` | Included: `ACTIVE.md`, `PROJECT.md`, `workstreams/ARCHIVE.md`, `handoffs/.gitkeep` | Installer seed state, including the status skill's context-file allowlist. `PROJECT.md` read; remaining seed paths traced through installer writes and tree inventory. SRC-1, `.state-seed/PROJECT.md`, `install.sh`. |
| `.state/` | Included: `ACTIVE.md`, `workstreams/ARCHIVE.md`, `handoffs/.gitkeep` | Repository's shipped state skeleton, distinct from the installation seed. Pointer read in full; ledger and placeholder inventoried. This skeleton is not a supplied multi-session execution trace. SRC-1, `.state/ACTIVE.md`, `.state/workstreams/ARCHIVE.md`. |
| `LICENSE` | Excluded from operational analysis | Legal terms only; no conclusion about licensing compatibility or patent coverage. Path identified in tracked-tree inventory. SRC-1, `LICENSE`. |
| `README.md` | Included | Installation, lifecycle, dependency and release contracts; also attributed operation claims. Read in full. Claims about prior live runs are not promoted to observed evidence. SRC-1, `README.md`. |
| `VERSION` | Included | Installer provenance and upgrade-currency input, traced through installer and SessionStart consumers; value not needed for this commit-based pin. SRC-1, `VERSION`, `install.sh`, `.claude/hooks/session-start.sh`. |
| `docs/` | Included: `design.md` | Source-native rationale and intended host/kit split. Read in full, as doctrine and attributed reports rather than independent proof of operation. SRC-1, `docs/design.md`. |
| `install.sh` | Included | Payload enumeration/deployment, settings merge, state seeding, overwrite/drift checks and provenance stamps. Selected implementation ranges and function/comment searches inspected, including deployment and seed writes. It is a shipped state producer, not an excluded application caller. SRC-1, `install.sh`. |
| `tests/` | Included: all tracked `*-acceptance.sh` drivers | Offline fixtures for measures, rewrite safety, hooks, installer and state formats; `va3-acceptance.sh` supplies a three-session model-driven create/work/close evaluator. Full read of that driver; bounded searches of session-start, rotate and goal-delivery suites; all suite paths inventoried. Other assertions remain to be inspected as relevant. No suite was executed. SRC-1, `tests/va3-acceptance.sh`, `tests/session-start-acceptance.sh`, `tests/rotate-acceptance.sh`, `tests/goal-delivery-acceptance.sh`. |

The included evaluator is material: it installs the kit into a temporary project and invokes `claude -p` for creation, work and closure. Excluding it would miss the repository's own model-calling driver and its consumers of generated state. It is test machinery, not evidence that this analysis observed those sessions. SRC-1, `tests/va3-acceptance.sh`.

> # End-to-end acceptance test for the workstream kit: three `claude -p` sessions
> # create, work, and close a demo workstream in a throwaway project.
> --- `tests/va3-acceptance.sh`

### External responsibilities and limits

Claude Code itself, its model providers, account-side memory, native Tasks, plan mode, `/goal` evaluation and subagent execution are external. The kit supplies instructions, registrations and supporting scripts; the host executes model turns and implements the native controls. Their exclusion prevents conclusions about the host's actual scheduling, model behavior, context compaction or enforcement beyond the inspected integration contracts. The kit explicitly delegates native capabilities rather than reimplementing them. SRC-1, `README.md`, `docs/design.md`, `.claude/settings.json`, `.claude/skills/workstream-work/SKILL.md`.

Git, a shell and standard command-line utilities are external execution dependencies; Python 3 supports the measuring/rewriting scripts and Stop hook, and jq supports settings merging and the status line. Consumer projects and handoff destinations provide the actual work artifacts and state; no such external project or live host transcript was supplied. These limits prevent claims of successful installation, reliable cross-session retention, correct autonomous execution, safe publication or realized learning transfer in a deployed consumer. Source-native reports of runs remain attributed reports. SRC-1, `install.sh`, `.claude/hooks/bare-id-guard.py`, `.claude/scripts/status-line.sh`, `.claude/skills/handoff/SKILL.md`, `tests/va3-acceptance.sh`.

### Frozen evidence and time boundary

The sole evidence source is the acquired repository at full commit `15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64`, with analysis cutoff **2026-10-15**. HEAD was checked against the acquired revision. The checkout was inspected read-only; no target code, examples, tests or providers were run. The source object is preserved unchanged. No moving web pages, external repositories or later revisions belong to this boundary.

The overall tier is **code-grounded**: executable installation, hooks, state readers, rewrite entry points and the acceptance driver are inspectable, alongside the prompts that govern model-mediated operations. This tier does not make prompt compliance observed behavior. The repository supplies implementation and doctrine/design, plus attributed reported operation in its documentation and comments. It supplies no separately inspected execution artifacts or causal experiment for this run.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ChristopherA/claude-workstream-kit` | 15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-claude-workstream-kit/related-systems/ChristopherA--claude-workstream-kit`. Tracked top-level and recursive tree inventoried. Implementation: `.claude/settings.json`, both hooks, selected ranges of `install.sh`, `.claude/scripts/workstream-record.py`, `.claude/scripts/workstream-rewrite.py`, `.claude/scripts/status-line.sh`; full forwarding shim; shared-module searches; full `tests/va3-acceptance.sh` and bounded evaluator searches. Doctrine/design: full `README.md`, `docs/design.md`, workstreams rule, work/extract/close skills, workstream template and seed project context; bounded searches of other skills, agent definitions and maintainer metadata. Reported operation: documentation and comments describing earlier runs, not independently verified. | Implementation: [installer](https://github.com/ChristopherA/claude-workstream-kit/blob/15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64/install.sh), [reload hook](https://github.com/ChristopherA/claude-workstream-kit/blob/15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64/.claude/hooks/session-start.sh), [model-calling evaluator](https://github.com/ChristopherA/claude-workstream-kit/blob/15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64/tests/va3-acceptance.sh). Doctrine/design and reported operation: [README](https://github.com/ChristopherA/claude-workstream-kit/blob/15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64/README.md), [design](https://github.com/ChristopherA/claude-workstream-kit/blob/15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64/docs/design.md), [state contract](https://github.com/ChristopherA/claude-workstream-kit/blob/15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64/.claude/rules/workstreams-rule.md). | No repository access gap found. The external host implementation, consumer projects, maintainer publication checker and underlying artifacts of reported live runs are not supplied. No observed-run or causal-experiment layer is established; deployment success, model compliance and effectiveness cannot be inferred from source availability or documentary reports. Remaining uninspected source detail is available within this same registered commit. |
