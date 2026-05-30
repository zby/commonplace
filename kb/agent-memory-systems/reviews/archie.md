---
description: "Arch Linux workstation configuration repo with Stow deployment, agent-readable work items, and session-log documentation but no automated memory-learning loop"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# Archie

Archie is Gabriel Chamon's repo-backed Arch Linux workstation system: Hyprland desktop configuration, shell tooling, deployment scripts, user guides, architecture decisions, work items, agent instructions, and local Codex session-log documentation. Its relevance to agent memory is not that it learns automatically. The useful comparison is that the repo treats workstation state, planning state, and agent-facing operating rules as retained artifacts in one git substrate.

**Repository:** https://github.com/gchamon/archie

**Reviewed revision:** [517a3717596c80abfc9fe7e05049e435ce6c91a4](https://github.com/gchamon/archie/commit/517a3717596c80abfc9fe7e05049e435ce6c91a4)

## Core Ideas

**The repo is the workstation memory substrate.** Archie keeps durable state in a git repository rather than in a database or hidden agent store. The visible substrate includes Stow packages under [`deployment-packages/`](https://github.com/gchamon/archie/tree/517a3717596c80abfc9fe7e05049e435ce6c91a4/deployment-packages), user docs under [`docs/user/`](https://github.com/gchamon/archie/tree/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/user), planning docs under [`docs/work-items/`](https://github.com/gchamon/archie/tree/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/work-items), and agent briefs under [`docs/agents/`](https://github.com/gchamon/archie/tree/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/agents). The same stored repo contains knowledge artifacts when docs are read as reference, and system-definition artifacts when configs, scripts, or agent instructions are consumed with configuration or instruction force.

**Stow gives deployment rules hard behavioral authority.** The accepted architecture decision is to use GNU Stow for managed configuration deployment, replacing copied files and ad hoc symlinks because they drift from repo state ([ADR 0001](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/architecture/decisions/0001-use-gnu-stow-for-config-deployment.md)). The canonical guide deploys `home`, `config`, `local`, `/etc`, and `xkb` packages into their target roots ([GUIDE.md](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/user/GUIDE.md)); the quickstart script implements backup, package installation, and Stow deployment paths in Bash ([install.sh](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/scripts/install.sh)). The docs remain prose, but the deployed symlinks and shell script are symbolic system-definition artifacts because the workstation runtime and installer consume them directly.

**Canonical-versus-derived documentation is explicit.** Archie names `docs/user/GUIDE.md` as the canonical deployment reference and treats `docs/user/QUICKSTART.md` plus `scripts/install.sh` as derived fast-path artifacts ([QUICKSTART.md](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/user/QUICKSTART.md), [UPDATE_QUICKSTART.md](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/agents/UPDATE_QUICKSTART.md)). That is a real lineage convention: when quickstart behavior changes, the agent brief tells maintainers to re-read the guide, update the script, then update quickstart prose. The enforcement is still social and agent-instructional, not a validator.

**Work items are agent-executable planning artifacts.** `docs/work-items/README.md` defines a stable shape with status, outcome, decision changes, quests, acceptance criteria, GitLab mapping, and status vocabulary ([work-items README](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/work-items/README.md)). `AGENTS.md` adds a work-item engagement protocol: ground in the work item, iterate during execution, then propagate decision changes to later work items and avoid marking work complete unless criteria were checked ([AGENTS.md](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/AGENTS.md)). These files are prose representational form, but their behavioral authority is stronger than ordinary reference docs when a coding agent is launched with them as instructions.

**Agent support is planned as constrained guidance, not autonomous memory.** The assistant epic and work item define a future documentation-first assistant that may layer in Codex, Claude, Gemini, or OpenCode through a local contract, with read-only documentation lookup and safe guidance as the center ([assistant epic](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/epics/assistant.md), [assistant-03](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/work-items/assistant-03-agent-backed-documentation-guide.md)). At the reviewed commit this is planning material, not an implemented agent runtime.

**Session-log documentation is retained evidence, not trace-derived learning.** Archie documents local Codex JSONL session logs, record types, and jq queries under [`docs/codex-sessions/README.md`](https://github.com/gchamon/archie/blob/517a3717596c80abfc9fe7e05049e435ce6c91a4/docs/codex-sessions/README.md), and ADR 0001 says its rationale was reconstructed partly from Codex session history. The inspected repo does not include a checked-in pipeline that mines those logs into rules, skills, prompts, tests, or learned weights. The session-log docs are knowledge artifacts for manual investigation and possible future distillation, so this review does not classify Archie as trace-derived learning.

## Comparison with Our System

Archie and commonplace share the repo-first bet: durable behavior-shaping material should be inspectable as files, searchable with ordinary tools, and versioned with git. Archie applies that bet to a workstation. Commonplace applies it to a knowledge base methodology and agent operating surface.

The authority split is different. In Archie, the strongest system-definition artifacts are shell scripts, deployed config files, Stow package layouts, and prompt-loaded `AGENTS.md` rules. The docs often matter because a human or agent reads them before editing the system. In commonplace, the strongest artifacts are typed notes, collection contracts, validators, review gates, generated indexes, and skills. Commonplace has a more explicit artifact taxonomy; Archie has a more concrete deployment target.

Archie's planning layer is closer to a workshop than to a library. Epics and work items preserve rationale, status, acceptance criteria, and decision changes for staged implementation. They are not meant to accumulate as general theory. Commonplace separates workshop artifacts from library notes more explicitly; Archie keeps them in one docs workspace and relies on naming, status, and agent instructions to preserve lifecycle boundaries.

Archie is also a useful negative example for trace-derived classification. It retains session-log format knowledge and allows an agent to consult local Codex sessions during work, but it does not implement automatic extraction or promotion from those traces. The memory effect is manual: a later agent can read docs, work items, and perhaps session logs, then update durable artifacts by judgment.

**Read-back:** both — prompt-loaded agent rules can enter context automatically, while docs and work items are read deliberately.

## Borrowable Ideas

**Canonical-guide plus derived-helper lineage.** Archie states that quickstart docs and installer behavior are derived from the canonical guide, then gives an agent brief for keeping them synchronized. Commonplace already has generated indexes and copied operational artifacts; a similar brief format would help for any derived behavior-facing view whose source cannot yet be checked mechanically. Ready now for narrow generated surfaces.

**Work-item decision-change propagation.** The instruction to carry decision changes forward to the next work item is a lightweight lifecycle rule that prevents planning documents from going stale one file at a time. Commonplace workshop artifacts could use the same pattern when a sequence of implementation notes depends on earlier decisions. Ready now where workshop sequences exist.

**Deployment packages as inspectable system definition.** Archie makes the deployed workstation state legible by storing target-root packages in a single repo layout and using Stow as the activation step. Commonplace should keep preferring similarly inspectable package boundaries when it ships skills, instructions, type specs, or generated control-plane files. Already aligned, but Archie is a concrete workstation-scale example.

**Agent briefs for recurring maintenance tasks.** `docs/agents/` contains small task briefs that constrain a coding agent without turning every procedure into executable code. This is a useful middle authority level between freeform docs and scripts. Commonplace has skills for higher-value procedures; agent briefs may be enough for rare but structured maintenance tasks that do not justify a promoted skill.

## Curiosity Pass

- The repo's strongest memory mechanism is ordinary configuration management, not agent memory. It changes future behavior because the shell, desktop, installer, and coding agent consume retained files with real authority.
- The session-log material is easy to overread. The docs make traces inspectable, and at least one ADR reports using session history as evidence, but there is no durable trace-to-artifact learner at the reviewed commit.
- The agent-facing work-item workflow may be more portable than the desktop config itself. The preparation, execution, post-phase propagation, and completion-check rules are small enough to transfer to any repo that uses agent-executed planning docs.
- The assistant plan is intentionally documentation-first. If implemented that way, Archie may become a useful reference for constrained local agent guidance rather than autonomous self-improvement.

## What to Watch

- Whether the planned assistant becomes an implemented local context surface, and whether it reads docs only or starts writing/promoting retained artifacts.
- Whether Codex session logs remain manual evidence or gain a pipeline that extracts decisions, lessons, or rules into work items, docs, scripts, or agent instructions.
- Whether quickstart/script/guide lineage gains deterministic validation, because the current synchronization contract is mostly prose.
- Whether Stow remains the activation substrate or is replaced by Guix/Home-style declarative system management work described in the planning docs.

---

Relevant Notes:

- [Retained artifact](../../notes/definitions/retained-artifact.md) - defined-in: Archie is best read as a collection of retained behavior-shaping files rather than as a memory database.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: Archie docs and session-log references mostly advise or inform later agents.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: Archie configs, scripts, Stow layouts, and prompt-loaded rules have configuration or instruction force.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - defined-in: the same Markdown file can be reference material or instruction depending on the consumer path.
- [Workshop](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: Archie work items fill a workshop-like role for staged implementation decisions.
