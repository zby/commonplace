---
description: "Archie review: repo-backed Arch Linux desktop configuration whose docs, work items, agent briefs, scripts, and Stow packages shape future maintenance"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-01"
---

# Archie

Archie is Gabriel Chamon's repo-backed Arch Linux desktop configuration and maintenance workspace. It is not a standalone memory database, but it is relevant to agent memory as a durable environment-and-methodology substrate: the repository stores desktop configuration, deployment scripts, architecture decisions, work items, agent instructions, task briefs, bug notes, and a small Python maintenance CLI that future humans and coding agents are expected to read and act on.

**Repository:** https://github.com/gchamon/archie

**Reviewed commit:** [698900ee209f471698987adb595df72b4a4a5961](https://github.com/gchamon/archie/commit/698900ee209f471698987adb595df72b4a4a5961)

**Last checked:** 2026-06-01

## Core Ideas

**The repository is the canonical retained state for a personal desktop.** Archie keeps Hyprland, Waybar, zsh, kitty, Neovim, GTK/Qt, SDDM, Nvidia, XKB, and systemd-logind configuration under `deployment-packages/`, then deploys most of it with GNU Stow into home, XDG config, local shell, `/etc`, and XKB roots ([README.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/README.md), [user guide](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/user/GUIDE.md), [deployment packages](https://github.com/gchamon/archie/tree/698900ee209f471698987adb595df72b4a4a5961/deployment-packages)). The retained artifact is not merely documentation; once Stow-deployed, repo files become the user's live runtime configuration.

**Deployment is scripted, but the guide remains the source of truth.** `docs/user/GUIDE.md` is the canonical deployment handbook, while `scripts/install.sh` implements a quickstart path that installs packages, bootstraps `yay`, clones the canonical GitLab repo when launched remotely, backs up conflicting deployment targets, runs Stow, copies logind drop-ins that cannot be symlinks, scaffolds local `.dist` files, applies theme settings, and prints manual follow-up checks ([GUIDE.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/user/GUIDE.md), [QUICKSTART.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/user/QUICKSTART.md), [install.sh](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/scripts/install.sh)). The quickstart has derived authority: it is behavior-changing code, but its intended lineage runs back to the guide.

**Agent-facing instructions are first-class repo artifacts.** The root `AGENTS.md` tells coding agents how to work in the system, including commands, style rules, project structure, common tasks, troubleshooting, and rules for work-item execution phases ([AGENTS.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/AGENTS.md)). `docs/agents/` adds scoped task briefs for updating quickstart, development-environment scripts, zsh-library docs, and keyboard docs, each naming the canonical docs and implementation files that must stay synchronized ([docs/agents](https://github.com/gchamon/archie/tree/698900ee209f471698987adb595df72b4a4a5961/docs/agents)). This is an instruction substrate more than a search substrate.

**Planning artifacts are durable project memory.** `docs/work-items/` defines a standard shape for executable changes, status vocabulary, metadata IDs, quest subtypes, and GitLab mapping; individual work items preserve outcomes, decision changes, scope notes, acceptance criteria, and sequencing ([work items README](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/work-items/README.md), [work items](https://github.com/gchamon/archie/tree/698900ee209f471698987adb595df72b4a4a5961/docs/work-items)). `docs/epics/` groups those work items and keeps higher-level decision changes visible ([assistant epic](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/epics/assistant.md)).

**Architecture decisions and bug reports carry operational memory.** ADRs record decisions such as moving deployment to GNU Stow and using GitLab as canonical upstream with GitHub as a read-only mirror ([ADR 0001](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/architecture/decisions/0001-use-gnu-stow-for-config-deployment.md), [ADR 0002](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/architecture/decisions/0002-use-gitlab-as-canonical-upstream-with-github-mirror.md)). `bug-reports/` keeps local notes for upstream defects that affect Archie, including an LTS-kernel Bluetooth regression whose mitigation is connected to the repo-owned downgrade CLI ([bug reports README](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/bug-reports/README.md), [downgrade work item](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/work-items/infrastructure-02-archlinux-archive-downgrade-cli.md)).

**The Python CLI turns one operational lesson into executable support.** `archie downgrade` resolves Arch Linux Archive package URLs for packages at or before a target time and can either print or execute a `pacman -U` command ([cli.py](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/src/archie/cli.py), [downgrade.py](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/src/archie/downgrade.py), [tests](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/tests/test_downgrade.py)). This is a small example of promotion from bug/work-item memory into symbolic behavior.

**Context posture is progressive disclosure.** A small always-loaded `AGENTS.md` routes; manuals, work items, ADRs, and bug notes load only on explicit lookup — bounding an agent session to a router plus pulled specifics.

**Read-back:** `both` — Root agent instructions and deployed configs are push by always-loaded location or runtime consumption; manuals, work items, ADRs, and bug notes are mostly pull by explicit lookup. There is no relevance-gated push activation layer in the inspected code

## Artifact analysis

- **Storage substrate:** `repo` — The Git repository, with live deployment as symlinks or copied files under home, XDG config, `/etc`, and `/usr/share/xkeyboard-config-2`
- **Representational form:** `mixed` — Mostly symbolic/procedural configuration with some prose comments

**Deployment packages and copied system files.** The storage substrate is the Git repository, with live deployment as symlinks or copied files under home, XDG config, `/etc`, and `/usr/share/xkeyboard-config-2`. The representational form is mostly symbolic/procedural configuration with some prose comments. Lineage is authored and guide-backed, with Stow packages derived from the desired runtime layout and `copy-deployed-files/` reserved for consumers such as `systemd-logind` that cannot follow home-directory symlinks ([copy-deployed-files README](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/copy-deployed-files/README.md)). Behavioral authority is system-definition authority over the desktop session and system services once deployed.

**Deployment guide, quickstart guide, and install script.** The storage substrate is Markdown plus Bash in the repo. The representational form is mixed: prose procedure in `GUIDE.md` and `QUICKSTART.md`, symbolic package lists and shell functions in `scripts/install.sh`. Lineage is explicit in the task brief: quickstart artifacts are derived from `docs/user/GUIDE.md` and should be updated together when behavior changes ([UPDATE_QUICKSTART.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/agents/UPDATE_QUICKSTART.md)). Behavioral authority splits by path: the guide is a knowledge artifact and prescriptive reference; the script is a system-definition artifact that mutates the host.

**Agent instructions and task briefs.** The storage substrate is repo Markdown. The representational form is prose instruction with structured file lists and ordered procedures. Lineage is authored from the maintainer's current workflow rather than generated from traces. Behavioral authority is system-definition authority for coding agents when `AGENTS.md` or a task brief is loaded into an agent session; the docs constrain tasks, file boundaries, and update order, but do not enforce those constraints mechanically.

**Work items, epics, and ADRs.** The storage substrate is repo Markdown under `docs/`. The representational form is prose with symbolic section contracts, statuses, stable IDs, and child-ID lists. Lineage is authored and sometimes reconstructed from prior repo documentation or session history, as ADR 0001 states for the Stow decision ([ADR 0001](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/architecture/decisions/0001-use-gnu-stow-for-config-deployment.md)). Behavioral authority is mostly knowledge-artifact authority for future maintainers and agents, becoming soft system-definition authority when `AGENTS.md` tells agents to obey work-item phases and status rules.

**Codex session-log documentation.** The storage substrate in the reviewed repo is only a README under `docs/codex-sessions/`; the actual `.jsonl` logs are local artifacts and ignored by Git ([codex session docs](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/codex-sessions/README.md)). The representational form is prose plus JSON schema examples and `jq` query recipes. Lineage is documentary: it describes raw trace format but does not implement extraction, scoring, promotion, or read-back from traces. Behavioral authority is knowledge-artifact authority for humans or agents manually inspecting logs, not trace-derived learning.

**Shell library and model aliases.** The storage substrate is zsh files deployed through the `local` Stow package and documented in `deployment-packages/local/lib/zsh/README.md`. The representational form is symbolic shell code plus prose reference. Lineage is authored, with a task brief requiring docs to be updated from the code when shell commands change ([zsh README](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/deployment-packages/local/lib/zsh/README.md), [commands-agents.sh](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/deployment-packages/local/lib/zsh/commands-agents.sh), [update-zsh-lib-docs.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/agents/update-zsh-lib-docs.md)). Behavioral authority is local command configuration; the `omp:*` aliases are agent-adjacent model preset affordances, not memory retrieval.

**Python maintenance CLI.** The storage substrate is repo Python source plus unit tests. The representational form is symbolic executable code. Lineage is work-item to implementation: the completed work item names the target behavior and tests, while `src/archie/downgrade.py` encodes the resolver. Behavioral authority is operational: it can generate or execute a package downgrade command, but it does not feed retained context into an agent.

### Borrowable Ideas

**Derived artifact briefs.** Commonplace already has collection contracts, but Archie's `docs/agents/UPDATE_QUICKSTART.md` style is a useful compact pattern for keeping generated or derived implementation artifacts synchronized with their canonical prose source. Ready now for narrow maintenance tasks.

**Work items as agent-consumable memory.** Archie's work-item shape is lighter than Commonplace's typed notes, but its `Outcome`, `Decision Changes`, `Main Quests`, and `Acceptance Criteria` sections are well suited to handoff between agents. Commonplace workshops can borrow that shape when a full note would be premature.

**Explicit "not a second source of truth" language.** The quickstart and dev-env briefs repeatedly name which files are canonical and which are derived. Commonplace could use the same language in generated-index and report workflows where agents often overpromote derived views.

**Copy-versus-symlink exception registry.** `copy-deployed-files/` is a small but clear pattern for recording deployment exceptions that cannot follow the general mechanism. Commonplace could use a similar exception namespace for artifacts that must leave the normal generated/indexed path because an external consumer has hard constraints.

**Operational lessons promoted to tools.** The downgrade CLI shows a tight path from a specific recurring system problem to a tested command. Commonplace should keep favoring this promotion path only when a lesson has become repeatable enough to warrant symbolic behavior.

## Comparison with Our System

| Dimension | Archie | Commonplace |
|---|---|---|
| Primary purpose | Maintain and deploy one Arch Linux desktop environment | Build and maintain an agent-operated methodology KB |
| Canonical substrate | Git-tracked config, docs, work items, scripts, and package trees | Git-tracked typed KB artifacts, sources, instructions, reports, and indexes |
| Agent-facing surface | Root `AGENTS.md`, task briefs, work items, Codex-log docs, model aliases | Skills, collection contracts, type specs, review gates, AGENTS.md, navigation |
| Behavior-changing artifacts | Stow packages, copied system files, install script, shell library, CLI | Instructions, validators, skills, type specs, generated indexes, review commands |
| Lineage model | Mostly prose conventions and file-pair briefs; some ADR/work-item history | Frontmatter, source snapshots, citations, status fields, generated indexes, review outputs |
| Read-back | Always-loaded repo instructions and live deployed config, plus manual lookup | Agent loads instructions/skills, searches notes/indexes, runs validators and review gates |

Archie resembles Commonplace less as a knowledge system and more as an operating environment whose repository doubles as memory. Its strongest retained artifacts are system-definition artifacts: deployed configuration, installer behavior, shell functions, and the package downgrade CLI. Its knowledge artifacts are the guides, work items, ADRs, bug notes, and Codex-log schema docs that future maintainers consult before changing those system-definition surfaces.

The main overlap is agent operation. Both systems put agent behavior into repository files rather than hidden service state. Archie is thinner on validation, type structure, source citation, and generated navigation, but it is stronger as an example of a personal system where the boundary between "memory" and "runtime configuration" is literal: changing the repo can change the user's shell, desktop, package workflow, and future agent instructions.

Archie also shows a different adoption affordance. Commonplace asks maintainers to write typed knowledge artifacts. Archie lets its owner keep ordinary desktop files, shell scripts, guides, and task briefs in a familiar repo, then gradually adds more formal structure only where recurring maintenance needs it.

## Curiosity Pass

**The most behavior-shaping memory is mundane configuration.** The reviewed repo's strongest future-action effects come from zsh, Hyprland, Stow packages, install scripts, and system drop-ins, not from an agent-specific memory store.

**Agent support is partly implemented and partly planned.** `AGENTS.md`, `docs/agents/`, and model aliases exist now. The assistant epic and `assistant-03` work item describe optional agent-backed documentation guidance, but that is planned rather than implemented ([assistant epic](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/epics/assistant.md), [assistant-03](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/work-items/assistant-03-agent-backed-documentation-guide.md)).

**The repo documents trace logs without learning from them.** `docs/codex-sessions/README.md` is useful trace literacy, but the inspected source has no pipeline that extracts durable behavior-shaping artifacts from those logs. That keeps Archie outside the `trace-derived` class for this review.

**GitHub is not the canonical upstream.** The review cites GitHub because the task supplied a GitHub mirror, but the repository itself says GitLab is authoritative and GitHub is read-only for `main` and tags ([README.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/README.md), [ADR 0002](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/architecture/decisions/0002-use-gitlab-as-canonical-upstream-with-github-mirror.md)).

**The Python CLI is intentionally narrow.** It does not try to become a broad desktop-management agent. That restraint is part of the architecture: promote only the operational action that has become repeatable and testable.

## What to Watch

- Whether the planned assistant work creates a real agent-backed documentation surface, and whether it loads docs by explicit user topic, relevance-gated selection, or unconditional prompt context.
- Whether Codex session logs remain manually inspected local traces or gain a distillation path into work items, ADRs, task briefs, or agent instructions.
- Whether the quickstart and dev-env derived-file briefs gain enforcement through tests or documentation checks, instead of relying only on agent obedience.
- Whether more bug reports promote into tested `archie` CLI commands, making the repo a growing operational tool surface rather than only a configuration store.
- Whether GitLab canonical state and GitHub mirror citations ever diverge in ways that affect source-pinned reviews.

Relevant Notes:

- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: Archie deployment packages, scripts, shell functions, AGENTS.md, and CLI code instruct or configure future behavior.
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: guides, work items, ADRs, bug reports, and Codex-log docs serve as evidence, context, and maintenance memory.
- [lineage](../../notes/definitions/lineage.md) - frames: Archie uses guide-to-script, code-to-doc, work-item-to-implementation, and ADR-to-future-planning lineage rather than a formal artifact graph.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Archie stores many docs, but most only affect agents or maintainers after explicit lookup; always-loaded AGENTS.md is the simpler push path.
- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - exemplifies: Archie keeps operational memory in inspectable repo files and shell/Python code instead of a separate memory service.
