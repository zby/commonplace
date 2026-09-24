# Framework delivery

## Commission

Posed by the operator on 2026-09-23. Decide how Commonplace delivers what agents read — the framework library, global types, review gates, and skills — to installed projects. Today `commonplace-init` copies all of it into every project, which confuses users and drifts from the installed code (see [design.md](./design.md#problem)). On 2026-09-24, at the operator's direction, the proposal `library-served-from-the-installed-package` was moved into this workshop as `design.md` and removed from `kb/reference/proposals/`, so the design is kept in one place while it changes.

## Operator direction and constraints

- **Copy GBrain by default** (2026-09-23). GBrain is Commonplace's dominant competitor. Depart from a GBrain method only for a Commonplace-specific reason, and record the reason.
- **One tree, one channel** (2026-09-24). The uv-installed package is the only tree that commands, agents, and harnesses read. There is no separate plugin tree, and projects get no copy of framework content. uv is the only release channel. This departs from GBrain, whose CLI and plugins install through separate channels and can skew.
- **One install path on every platform** (2026-09-24). If one platform needs something different, every platform does it that way; there are no platform-specific install paths. Symlinks are unreliable on Windows, so nothing is linked.
- **Init only, per project** (2026-09-24). No per-machine setup command. `commonplace-init` writes everything a project needs.
- **Skill stubs** (2026-09-24). Each project gets a stub per skill that redirects to the real skill in the installed package. It costs one extra read per skill use; every alternative was worse.
- **Generated routing file** (2026-09-24). Agents find the library through a gitignored file that init writes with full paths, not through commands.
- **Sub-agents are emulated where missing** (2026-09-24). Users should be able to start using Commonplace in a harness without sub-agents, even though skills that need workers are less useful there. The probing agent designs the emulation for its harness.
- **Plan for harnesses without skills** (2026-09-24). The routing file carries a skill index that emulates the skills mechanism; stubs stay for harnesses with native skills.
- **No hooks** (2026-09-24). No harness hooks until hooks are standardised. At least one enterprise user runs their own harness.
- **Harness-neutral base** (2026-09-24). The design rests on files and a project `AGENTS.md`, with Agent Skills as an optional layer above that base. The base must still let an agent find a library instruction that the user names in conversation, outside any skill.

## Design

[design.md](./design.md) holds the design; keep it only there. In short: the library stays in the installed package, and `commonplace-init` writes three uncommitted, machine-specific files into each project — a stub per skill that redirects to the real skill, `.commonplace/library.md` with the library's full paths, and one Claude Code read rule. Agents reach the library by reading files. Rejected options and their evidence are in [alternatives.md](./alternatives.md).

## Open questions

- **Missing initialization.** In Codex's revision 4 run, an agent in a clone without init found a nearby source checkout and answered from it instead of reporting the missing `library.md`. The design now has the `AGENTS.md` template say to stop and ask for init; does that work in both harnesses?
- **Emulated skills.** Does the skill index in `library.md` trigger the right skill reliably when no native skill exists (probe case 9)? In Codex, the agent sees the index only after reading `library.md`.
- **Skill metadata.** Does any harness need skill metadata beyond name and description copied into the stub? The probe's skills had none.
- **The enterprise harness.** It loads neither `AGENTS.md` nor `CLAUDE.md`. What does load standing instructions there, and who can set it? The probe request asks the agent to find out and propose where the pointer line goes. More generally: which of the design's harness assumptions (H1–H6 in [design.md](./design.md#what-the-design-assumes-about-a-harness)) hold there? The enterprise colleague cannot give detailed answers, so the probe request asks whether an agent in the harness can adapt the design to reach five outcomes, and reports whether each was reached and how large any workaround was, and how it works where company policy allows; the table maps an outcome not reached to the assumption that failed. If the harness is built on Codex's app-server, `skills/extraRoots/set` may let it discover the package's skills in place.
- **The router skill at scale.** It worked with a small index. Does it still select the right instruction with an index the size of the real library?
- **The source checkout.** The design has the source repo run init like any project, so its stubs replace the committed symlinks in `.claude/skills/`. Not yet tried on the real repository.
- **Windows and macOS.** Not tested systematically. One Windows observation so far: init crashed on a `settings.local.json` that PowerShell 5.1 had written with a byte-order mark; fixed in probe revision 5. Still unknown on Windows: the form of Claude Code's read rule for a Windows path. Do the full paths that init writes, and reads of files under `share/`, work on both?
- **Running sessions.** A running Claude Code session picked up skills added after it started. An upgrade inside a running session was not tested.
- **Centrally managed settings.** Init writes Claude Code's read rule into the project's `.claude/settings.local.json`. Does a centrally managed policy override it?

## Next steps

1. Claude Code and Codex run revision 5's new cases: 8 (the stop-on-missing-init rule) and 9 (a skill reached through the index alone).
2. Agents in other harnesses answer the same [probe request](./probe-request.md), reporting which outcomes they reached and the size of any workaround: Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, and enterprise harnesses. Enterprise results may come back through the operator, anonymised.
3. Update [design.md](./design.md) from the results, then decide it: an ADR and the `INSTALL.md` change, followed by implementation. No end-to-end rehearsal before the decision (operator, 2026-09-24): Commonplace is in alpha, so problems found in use are fixed in use.

## Evaluation boundary

- Harnesses: Claude Code and Codex, plus the base layer in any harness that meets its stated assumptions.
- Operating systems: Linux, macOS, and Windows.
- Places: the source checkout and an installed project.
- Upgrade cases: an upgrade that changes a skill, one that changes only library files, and one that moves the install location.

## Coupling

- [agent-operability-second-slice](../agent-operability-second-slice/README.md) builds install baselines and a three-way upgrade plan for copied framework files. Without the library copy, its subject shrinks to whatever copies remain. Coordinate before either side ships.
- [system-contract-consistency](../system-contract-consistency/README.md) holds findings I1 (shipping and upgrade contracts disagree) and I2 (the install projection breaks library links). Both change meaning once the library stops being copied.

## Closure

Close when the operator decides the design: an adopted design becomes an ADR and an `INSTALL.md` change; a design left undecided goes back to `kb/reference/proposals/` as a proposal. Before closing, each open question is answered or deferred with a trigger, and each departure from GBrain has a recorded reason. The rejected alternatives go into the ADR or proposal as its considered options. Then delete this directory and its entry in `kb/work/README.md`.

## Files

Current:

- [design.md](./design.md) — the chosen design, including the proposed install procedure
- [alternatives.md](./alternatives.md) — rejected options, why, and the evidence by probe revision
- [probe-package/](./probe-package/PROTOCOL.md) — the shared probe (revision 4): a throwaway uv package, a test project, the protocol every harness runs, and a results template
- [probe-request.md](./probe-request.md) — the open request to agents in any harness to run the probe, with a log of replies
- [results-claude-code-r4.md](./results-claude-code-r4.md) — Claude Code's run of revision 4
- [results-codex-r4.md](./results-codex-r4.md) — Codex's run of revision 4
- [adr-draft.md](./adr-draft.md) — draft ADR 086 recording the decision, for the operator to adopt

Background research:

- [comparable-systems-survey.md](./comparable-systems-survey.md) — how harnesses and 14 comparable systems deliver skills and libraries
- [gbrain-delivery-methods.md](./gbrain-delivery-methods.md) — code-grounded study of GBrain v0.54.1.0's delivery methods

Evidence from earlier revisions, cited by `alternatives.md`:

- [probe-results.md](./probe-results.md) — early probes: a Claude Code link-mode plugin, a Codex skill symlink, uv shared data
- [results-codex.md](./results-codex.md) — Codex's runs of revisions 1–3
- [results-claude-code.md](./results-claude-code.md) — Claude Code's run of revision 3
