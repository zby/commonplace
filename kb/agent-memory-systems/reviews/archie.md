---
description: "Archie review: Git-native Arch Linux desktop configuration with Stow deployment, agent briefs, ADRs, and pull-only repo read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
---

# Archie

Archie, from `gchamon/archie`, is a personal Arch Linux desktop configuration and operations repository for a Hyprland-based system. At reviewed commit `698900ee209f471698987adb595df72b4a4a5961`, it is not an autonomous memory service; its memory-like value is the Git-retained operating substrate: deployment packages, canonical guides, architecture decisions, agent-facing task briefs, convenience scripts, and local templates that shape future human and coding-agent maintenance.

**Repository:** https://github.com/gchamon/archie

**Reviewed commit:** [698900ee209f471698987adb595df72b4a4a5961](https://github.com/gchamon/archie/commit/698900ee209f471698987adb595df72b4a4a5961)

**Source directory:** `related-systems/gchamon--archie`

## Core Ideas

**The repository is the durable system memory.** Archie keeps desktop configuration, system deployment packages, shell commands, backup notes, ADRs, work items, and agent briefs in one Git repository. The README points readers to the installation guide, quickstart, migration guide, keyboard docs, backup guide, bug reports, and contribution workflow, while also saying GitLab is canonical and GitHub is a read-only mirror ([README.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/README.md), [docs/user/DEVELOPMENT.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/user/DEVELOPMENT.md), [docs/architecture/decisions/0002-use-gitlab-as-canonical-upstream-with-github-mirror.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/architecture/decisions/0002-use-gitlab-as-canonical-upstream-with-github-mirror.md)).

**Deployment uses Stow as a symbolic projection from repo to machine.** The main guide says Archie is cloned outside deployment targets, then Stow links tracked packages into `$HOME`, `$HOME/.config`, `$HOME/.local`, `/etc`, and optionally `/usr/share/xkeyboard-config-2`; copy-managed logind files are handled separately because systemd cannot read `/etc` symlinks into `$HOME` under `ProtectHome=yes` ([docs/user/GUIDE.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/user/GUIDE.md), [docs/architecture/decisions/0001-use-gnu-stow-for-config-deployment.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/architecture/decisions/0001-use-gnu-stow-for-config-deployment.md)).

**The quickstart is executable documentation over the deployment model.** `scripts/install.sh` installs base packages, bootstraps `yay`, backs up conflicting deployment targets, deploys Stow packages, copies privileged files, scaffolds machine-local files from `.dist` templates, applies theme defaults, and prints manual follow-up checks. This makes the repo a configuration memory that can be replayed into a new machine, not just a handbook ([scripts/install.sh](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/scripts/install.sh), [docs/user/QUICKSTART.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/user/QUICKSTART.md)).

**Agent affordances are authored briefs and local rules, not learned behavior.** `AGENTS.md` gives coding agents commands, style rules, project structure, common tasks, troubleshooting, and engagement rules for work items. `docs/agents/` contains scoped task briefs intended to be executed by coding agents. These are system-definition artifacts for future maintenance sessions, but they are manually authored and read on demand rather than generated from traces ([AGENTS.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/AGENTS.md), [docs/agents/README.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/agents/README.md), [docs/agents/UPDATE_DEV_ENV_SCRIPTS.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/agents/UPDATE_DEV_ENV_SCRIPTS.md)).

**Development VMs make the environment partially reproducible.** The dev-environment guide and scripts render cloud-init templates into `.state/dev-env/...`, create Incus VMs, wait for the VM agent and cloud-init, publish a reusable base image, launch an Archie instance, and provide shell/console/clipboard helpers. This is a retained operations path for testing configuration changes against a disposable Arch desktop ([docs/development/DEV_ENV.md](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/docs/development/DEV_ENV.md), [scripts/create-arch-base-image.sh](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/scripts/create-arch-base-image.sh), [scripts/launch-archie-instance.sh](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/scripts/launch-archie-instance.sh), [scripts/dev-env/common.sh](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/scripts/dev-env/common.sh)).

**Context efficiency is file-native and scoped by navigation, not retrieval infrastructure.** Archie does not implement embeddings, a database, or automatic context packing. Efficiency comes from directory separation, README hubs, canonical docs, work-item/agent briefs, generated TOCs, and the agent guide's project map. A future agent still has to pull the relevant file with ordinary repo navigation; nothing selects and injects task-relevant memory automatically.

## Artifact analysis

- **Storage substrate:** `repo` `files` — The canonical retained state is the Git repository: Markdown docs, ADRs, work items, task briefs, Stow packages, templates, scripts, and Python maintenance tooling. Runtime projection creates file-system state through symlinks, copied system files, generated machine-local `.conf` files, `.state/dev-env/...` render outputs, and `/etc/pkglist.txt` package snapshots.
- **Representational form:** `prose` `symbolic` — Guides, ADRs, agent briefs, changelog entries, bug reports, and comments are prose; Stow package layout, shell scripts, Python CLI code, cloud-init templates, Hyprland/Waybar/Zsh/Neovim configs, cron jobs, and tests are symbolic. I found no durable embeddings, learned model weights, or other parametric memory surface.
- **Lineage:** `authored` `imported` — Most retained artifacts are authored by the maintainer. Some state is imported or mirrored from external systems: Arch package/archive data resolved by the `archie downgrade` CLI, upstream package lists, GitLab-to-GitHub mirroring policy, backup paths, external themes, cloud images, and machine-local config templates. I did not find an implemented automatic trace-to-memory learner.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Guides, ADRs, backup docs, and bug reports are knowledge artifacts for maintainers and agents; `AGENTS.md`, `docs/agents/*`, shell helpers, and deployment docs instruct future work; Stow layout, copied logind files, system configs, and scripts enforce machine behavior; README hubs, TOCs, package directories, work-item names, and task briefs route attention; tests, `bash -n` expectations, `shellcheck` guidance, pytests, and service reload checks validate changes.

**Deployment packages.** `deployment-packages/` is the highest-authority retained surface: once Stow-deployed, its symbolic files become the actual Hyprland, Waybar, Zsh, Neovim, Kitty, SDDM, `/etc`, and XKB configuration. It has instruction authority in docs and enforcement authority on the running machine through the symlinked files.

**Machine-local templates and generated files.** `device.dist.conf`, `hyprpaper.dist.conf`, and `overrides.dist.sh` are retained templates; `scripts/install.sh` copies them into editable local-only files when missing. That keeps source-controlled defaults separate from machine-specific state, but it also means the repository cannot fully reconstruct a machine without local choices and backup material.

**Agent guide and task briefs.** `AGENTS.md` and `docs/agents/*.md` are prose system-definition artifacts. They shape future coding-agent behavior by declaring commands, style rules, file boundaries, task sequencing, and verification expectations. Their authority is advisory/instructional rather than enforced by a harness.

**Development VM workflow.** The Incus scripts and cloud-init templates compile repo-authored defaults plus local environment variables into rendered files under `.state/dev-env/...`, then into Incus VM configuration. These artifacts are derived access paths for reproducible testing; the repo keeps the templates and scripts, while the rendered state is local build output.

**Package and downgrade tooling.** `archie downgrade` resolves Arch Linux Archive package URLs and can print or execute a `pacman -U` command; tests cover parsing and resolution behavior ([src/archie/downgrade.py](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/src/archie/downgrade.py), [tests/test_downgrade.py](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/tests/test_downgrade.py)). The hourly cron job writes explicit package state to `/etc/pkglist.txt`, giving the system a simple snapshot of installed package choices ([deployment-packages/etc/cron.hourly/yay_pkglist](https://github.com/gchamon/archie/blob/698900ee209f471698987adb595df72b4a4a5961/deployment-packages/etc/cron.hourly/yay_pkglist)).

**Promotion path.** Archie promotes decisions from work items or session-derived reasoning into durable docs, ADRs, scripts, and deployment packages. That promotion is manual and Git-mediated. There is no automatic curation loop that consolidates logs, deduplicates memories, or changes future instructions from observed agent trajectories.

## Comparison with Our System

Archie and Commonplace share the premise that a Git repository can be a behavior-shaping memory substrate for future agents. Both use plain files, authored contracts, scoped directories, and validation habits instead of hiding durable knowledge in a service. The difference is register and authority: Archie is an operating-environment repo whose retained state eventually configures a real desktop; Commonplace is a KB methodology repo whose retained state configures agent navigation, writing, review, and validation.

Archie is stronger as an adoption model for a whole local environment. It keeps setup, rollback-ish backups, deployable packages, VM reproduction, and agent briefs together, so the maintainer can rebuild the workbench that future agents operate in. Commonplace is stronger as an epistemic substrate: it requires typed notes, source-grounded reviews, link semantics, controlled vocabulary, and deterministic validation around knowledge artifacts.

The main comparison point is the boundary between authored memory and generated local state. Archie is careful about `.dist` templates and Stow packages, but generated files and machine-specific choices live outside the repo. Commonplace faces the same boundary with generated indexes, snapshots, review runs, and workshop artifacts; Archie is a reminder that the canonical artifact and its deployed projection should be classified separately.

The second comparison point is agent affordance. Archie includes `AGENTS.md` and scoped agent briefs, but read-back remains pull-only: the acting agent must notice and read them. Commonplace already has stronger collection/type contracts and skills, but it can still borrow Archie's concrete "agent task brief" pattern for repeatable maintenance tasks that should not become global instructions.

### Borrowable Ideas

**Repo-backed environment memory.** Commonplace could document the surrounding operator environment more explicitly: required shell tools, validation entrypoints, local viewers, and expected installed commands. Ready now as reference documentation, not as another global instruction layer.

**`.dist` template plus local generated file boundary.** Archie's split between tracked templates and untracked machine-local files is a useful pattern for Commonplace configuration that should be reproducible but not identical across installations. Ready when Commonplace grows more operator-local config.

**Scoped agent briefs.** `docs/agents/UPDATE_DEV_ENV_SCRIPTS.md` is a good shape for task-local guidance: it names the files that move together, the source of truth, update order, boundaries, and verification. Commonplace could use the same shape for recurring multi-file maintenance procedures. Ready for procedures that are too specific for global `AGENTS.md` but too repeatable for ad hoc prompts.

**Executable quickstart as current documentation pressure.** The install script forces docs and scripts to stay close. Commonplace can borrow this for setup or review workflows only where side effects are acceptable and testable; most KB writing workflows should remain explicit rather than one-shot automation.

**Do not borrow unreviewed local state as canonical memory.** Archie's local backups, generated `.state` files, and machine-specific configs are necessary, but they should not be treated as source-grounded knowledge without capture and review. This is a design constraint for Commonplace's workshop and generated-artifact layers.

## Write side

**Write agency:** `manual` `automatic` — Maintainers and coding agents manually edit docs, configs, task briefs, scripts, package lists, and ADRs. Automatic writes exist for operational projection and snapshots: the quickstart backs up conflicting deployment targets, deploys Stow symlinks, copies privileged files, scaffolds local configs, renders dev-VM cloud-init, and the cron job writes `/etc/pkglist.txt`. These automatic writes do not curate a memory store from traces.

**Curation operations:** `promote` — The only automatic operation close to memory promotion is operational: repo files are promoted into deployed symlinks/copies or rendered VM state. I did not find automatic consolidate, dedup, evolve, synthesize, invalidate, or decay over retained knowledge artifacts.

## Read-back

**Read-back:** `pull` — Archie stores guidance and operational memory in repo files, deployed configs, and local generated state, but future agents or maintainers must intentionally read the relevant README, guide, ADR, task brief, script, or config. There is no implemented service, hook, embedding retriever, or session-start injector that pushes retained memory into an agent's context.

The nearest edge case is `AGENTS.md`: harnesses may load it automatically when working inside the repository, but that is baseline repository instruction rather than Archie implementing its own memory read-back path. Static docs and deployed configs shape the environment, but they do not perform instance-targeted memory selection for the next model call.

## Curiosity Pass

**Archie is closer to "environment memory" than "agent memory."** It remembers how a maintainer wants a desktop, shell, editor, package set, and development VM to behave. That can strongly shape agents working on the machine, but the mechanism is operating-system configuration and prose instruction, not retrieval or learning.

**The repo has many agent-adjacent hooks without an agent runtime.** `AGENTS.md`, `docs/agents/`, OMP aliases, Codex-session documentation, and work-item engagement rules all assume agents will consume the repo. None of them implement automatic agent-state retention or relevance selection.

**The highest-authority artifacts are not the Markdown files.** Markdown explains and routes, but Stow-deployed configs, scripts, cron jobs, systemd drop-ins, and cloud-init templates actually change machine behavior. For review purposes, Archie is a useful reminder to classify the operative part, not the file extension.

**Context efficiency depends on the next reader's discipline.** README hubs, TOCs, task briefs, and directory names reduce search cost, but nothing prevents a future agent from loading too much or missing the relevant brief. That is the main gap relative to engineered read-back systems.

## What to Watch

- Whether the planned assistant work items produce an actual help topic applet, Kitty TUI, or agent-backed documentation guide. That could move Archie from static agent affordances toward an explicit context-serving interface.
- Whether the dev-environment scripts gain automated smoke tests for a deployed Archie instance. That would strengthen validation authority for repo-backed environment memory.
- Whether package snapshots such as `/etc/pkglist.txt` become source-controlled manifests or typed inventory artifacts. That would change them from local operational snapshots into durable, reviewable system memory.
- Whether task briefs begin deriving from real agent sessions with retained rationale and review state. That would create trace-extracted artifacts, but it is not implemented at this commit.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Archie bundles prose docs, symbolic configs, scripts, generated local files, and deployed OS state under different authorities.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: Archie stores extensive guidance, but future agents still need to pull the relevant file.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - applies: Archie's retained artifacts range from advisory docs to system-enforced configuration.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: Stow packages, scripts, AGENTS.md, task briefs, and VM templates shape future behavior through instruction, routing, validation, and enforcement.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Archie manages context by repo organization and task-local briefs rather than by automatic retrieval.
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - compares: Archie is discoverable and inspectable, but it leaves activation to manual repo navigation.
