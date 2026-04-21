---
description: Arch Linux config repo with Stow-managed multi-root deployment, Incus dev VMs, and agent-executable work-item docs; strong operational packaging, no real knowledge-learning loop
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-05"
---

# Archie

Archie is Gabriel Chamon's repo-backed Arch Linux desktop system: Hyprland configuration, deployment packages, installation scripts, development-environment helpers, and a substantial documentation workspace. GitLab is the canonical upstream and GitHub is a read-only mirror. The interesting part for us is not "dotfiles" alone, but the way Archie keeps deployment logic, staged planning, agent-facing task briefs, and even Codex session-log documentation in the repository as inspectable text and scripts.

**Repository:** https://github.com/gchamon/archie

## Core Ideas

**Stow-managed multi-root deployment.** Archie treats the repository as the source of truth for files that ultimately land in `$HOME`, `~/.config`, `~/.local`, `/etc`, and optionally `/usr/share/xkeyboard-config-2`. `scripts/install.sh` backs up conflicting existing targets before calling `stow`, then scaffolds machine-local files such as `device.conf`, `hyprpaper.conf`, and `overrides.sh` from deployed `.dist` templates. This is a real representation change from copy-based dotfile setup to a managed symlink graph with explicit local-exception points.

**Canonical guide first, automation second.** `docs/user/GUIDE.md` is the canonical deployment reference, while `docs/user/QUICKSTART.md` and `scripts/install.sh` are derived fast paths. `docs/agents/UPDATE_QUICKSTART.md` makes that contract explicit: update the script first, then update quickstart prose, and keep both recoverable from the guide. That is a strong anti-drift pattern for repos that want both a full handbook and a safe automation path.

**Repo-local workshop artifacts for agent execution.** `docs/work-items/` and `docs/agents/` are written as self-contained execution packets for staged work. `docs/work-items/README.md` defines filename conventions, status conventions, and the work-item hierarchy; the repo `AGENTS.md` tells agents to ground themselves in a work item before editing and to propagate decisions forward. This is a workshop-like planning layer inside an operational repo, not a semantic library or learning loop.

**Disposable validation environments.** Archie contains a concrete verification story for risky system changes: use Incus VMs bootstrapped through cloud-init templates, publish a reusable base image, then launch disposable Archie guests for manual validation. `scripts/dev-env/common.sh`, `scripts/create-arch-base-image.sh`, and `scripts/launch-archie-instance.sh` operationalize the process described in `docs/development/DEV_ENV.md`. The value is containment: workstation configuration can be tested in a repeatable guest instead of directly on the host.

**Codex session logs are observability, not learning.** `docs/codex-sessions/README.md` carefully documents the local `.jsonl` event stream format and provides `jq` queries for inspection. But the repo contains no consumer that mines those logs into updated work items, docs, rules, or configs. The trace substrate exists as an audit artifact, not as a promotion loop.

## Comparison with Our System

Archie and commonplace agree on one deep architectural bet: keep the important artifacts as ordinary repo files that an agent can read, diff, and edit with standard tools. But the systems optimize for different end states. Archie is trying to deploy, test, and evolve a workstation environment plus its maintenance workflow. Commonplace is trying to distill and connect durable knowledge so future agents can load the right context.

| Dimension | Archie | Commonplace |
|---|---|---|
| Primary artifact | Deployable configs, helper scripts, work-item docs, user guides | Notes, instructions, sources, reviews, workshop artifacts |
| Main operation | Configure and validate a system | Write, connect, distill, and review knowledge |
| Workshop layer | `docs/work-items/` and `docs/agents/` as staged execution packets | `kb/work/`, tasks, and skills as work-in-flight machinery |
| Relationship model | Mostly directory structure plus ordinary doc links | Explicit semantic links and curated indexes |
| Validation model | Stow conflict handling, service reloads, disposable VM testing | Structural note validation plus review-gate bundles |
| Trace use | Session logs documented for inspection only | Workshop artifacts are candidates for later promotion into durable KB artifacts |

The strongest alignment is the inspectable-substrate choice. Archie does not hide deployment logic behind a hosted service or opaque state store; the repo contains the deployment packages, the wrapper scripts, the plans, and the agent guidance. That matches our view that inspectable files are often a better early substrate than a database or hidden runtime state.

The strongest divergence is where knowledge structure lives. Archie's documents are operationally useful, but they are not arranged as a semantic library with title-as-claim traversal, relationship-typed links, or explicit maturation paths. Its planning layer is closer to a workshop than a library: the files coordinate multi-session work, but they do not aim to become a reusable graph of durable concepts.

The trace-derived boundary is also clear. Archie records Codex sessions and documents the schema, which is already more concrete than many repos. But there is still no implemented bridge from trace to durable artifact. So Archie belongs near our workshop and observability concerns, not in the trace-derived learning queue.

## Borrowable Ideas

**Derived fast paths with an explicit canonical source.** Ready now. The `GUIDE.md` -> `install.sh` + `QUICKSTART.md` relationship is disciplined instead of informal, and `docs/agents/UPDATE_QUICKSTART.md` encodes the maintenance rule. If we create more "fast path" helpers around a deeper canonical method, this is the right shape: one source of truth, derived automation, and an explicit sync instruction.

**Self-contained execution packets for staged agent work.** Needs a use case first. Archie's work-item files are written to be handed to an engineer or agent without re-explaining the project. That is stronger than a bare issue tracker ticket. We already have workshop artifacts, but there is room to make some long-running initiatives more handoff-ready in this style.

**Verification through disposable environments.** Needs a use case first. Archie assumes some changes are too risky to validate only in-place, so it invests in a reproducible guest path. For commonplace this is not generally needed, but the pattern matters: when the artifact controls an environment, not just a document set, a disposable validation substrate becomes part of the knowledge system.

**Document the raw trace format before building learning on top of it.** Needs a use case first. Archie's Codex session-log README is valuable even without a learning loop because it makes the trace inspectable and queryable. If we ever promote session traces into workshop or library artifacts, documenting the trace schema first would avoid building on a vague substrate.

## Curiosity Pass

The most convincing Archie mechanism is the Stow deployment layer. It really does more than relocate files: copied deployment becomes managed symlink deployment, conflict handling becomes explicit, and local overrides get a clearly bounded escape hatch through `.dist` templates. That is codification, not just renaming.

The agent/work-item layer is more ambiguous. It clearly improves handoff quality, but it mostly relocates planning into markdown files rather than transforming it into a new machine-enforced representation. The repo gains clarity for humans and agents, yet the files remain descriptive packets rather than a scheduler, validator, or extraction system. That is still useful, but the ceiling is lower than the structure might initially suggest.

The Codex session-log material is the clearest naming-versus-mechanism checkpoint. The repo has traces and a schema for reading them, but no implemented learning loop. So the interesting signal is not "Archie learns from Codex sessions." It does not, at least in this reviewed state. The real signal is that Archie treats traces as first-class operational artifacts and has laid down the observability substrate that a later learning loop could use.

One more boundary matters: the distro plan in `docs/architecture/DISTRO.md` is still a plan. The repo currently has no `iso/`, `profiles/`, or release-pipeline implementation matching that document. So Archie should be read as a strong operational repo for workstation deployment and maintenance, with a documented future distro ambition, not as an already implemented distro-build system.

## What to Watch

- Whether the documented distro/ISO plan ever lands as actual build artifacts and release tooling
- Whether Codex session logs remain an observability layer or get promoted into work-item, ADR, or guide updates
- Whether the work-item and agent-brief layer gains stronger validation or extraction bridges instead of remaining descriptive coordination
- Whether the canonical-guide-versus-derived-automation pattern stays disciplined as the repo grows

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — convergence: Archie keeps deployment logic, planning packets, and agent guidance as inspectable repo files instead of hidden runtime state
- [a functioning knowledge base needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: `docs/work-items/` and `docs/agents/` are a repo-local workshop layer for staged execution
- [AGENTS.md should be organized as a control plane](../../notes/agents-md-should-be-organized-as-a-control-plane.md) — contrasts: Archie uses `AGENTS.md` as a broad implementation handbook, not a minimal routing control plane
- [inspectable artifact, not supervision, defeats the blackbox problem](../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — exemplifies: deployment scripts, plans, and agent-facing docs all stay in a substrate that another agent can inspect and revise
- [Agent Skills for Context Engineering](./agent-skills-for-context-engineering.md) — contrasts: Archie uses repo-specific work items and task briefs rather than a reusable cross-repo skill library
