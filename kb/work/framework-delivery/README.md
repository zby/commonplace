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
- **The source checkout keeps its skill symlinks and does not run init** (2026-09-25).
- **Report and source types stay scaffolded into projects** (2026-09-25); their schemas stop `$ref`-ing the global note schema.
- **Plan for harnesses without skills** (2026-09-24). The routing file carries a skill index that emulates the skills mechanism; stubs stay for harnesses with native skills.
- **No hooks** (2026-09-24). No harness hooks until hooks are standardised. At least one enterprise user runs their own harness.
- **Harness-neutral base** (2026-09-24). The design rests on files and a project `AGENTS.md`, with Agent Skills as an optional layer above that base. The base must still let an agent find a library instruction that the user names in conversation, outside any skill.

## Design

Decided and adopted on 2026-09-25 as [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) (commit `e6103225`). ADR 086, `INSTALL.md`, and the code are now authoritative. [design.md](./design.md) and [alternatives.md](./alternatives.md) are the pre-adoption records; do not update them. This workshop stays open for the follow-ups below.

## Status (rebaselined 2026-10-24)

Nothing in this workshop changed after 2026-09-25 except mechanical path
rewrites. A recheck against the repository on 2026-10-24 found:

- **Shipped state.** v0.2.0 (tagged 2026-09-25, commit `5c99505a3`) is the
  only release carrying ADR 086. Since then 1603 commits landed and
  `pyproject.toml` still says `0.2.0`, so none of them is installable from PyPI.
- **Delivery-surface drift since v0.2.0** that an installed project would see:
  a new runtime dependency on `workjig` from PyPI (commit `005a3f2dd`); two new
  commands, `commonplace-analysis` (`83c641f00`) and `commonplace-task`
  (`ef57a1175`), and the two `commonplace-agentic-analysis-*` commands removed;
  report and source types moved from the project scaffold into the global
  library types (`704c42c09`); `kb/tags/` and `kb/work/` added to the scaffold
  (`02ffd8329`, ADR 089); automatic legacy migrations removed from init
  (`8b8a9c742`); the library's theory collection renamed from `kb/notes/` to
  `kb/theory/` (ADR 123, `e4c1bfcf1`) while project scaffolds deliberately keep
  `kb/notes/`. `src/commonplace/cli/init_project.py` shrank by about 260 lines.
- **Probe package.** [probe-package/](./probe-package/PROTOCOL.md) was still
  revision 6, modelled on the revision 4 init, until 2026-10-24; revision 7 now
  mirrors the current `commonplace-init` (see its revision log). Results from
  revisions 4–6 stay valid for cases 1–7.
- **Evidence.** Revision 7 ran on 2026-10-24 in three harnesses on Linux:
  [Claude Code](./results-claude-code-r7.md) (cases 0, 8–11),
  [Codex](./results-codex-r7.md) (cases 0, 8–11) and [pi](./results-pi-r7.md)
  (full protocol). No clean-machine install from PyPI is recorded anywhere, on
  any platform, and there is still no Windows or macOS run. Findings that
  changed the code: Claude Code substitutes `$ARGUMENTS` at every occurrence
  in a stub, so the stub's second sentence lost its placeholder (fixed in
  `library.py` and the probe the same day); the Codex agent reached a skill
  through the index and reported the literal placeholder, so the routing
  file now tells index readers to apply the request's arguments. Findings
  for the record: pi needs no Claude read rule and loads `.agents/skills/`
  under explicit project trust; stock pi has no sub-agent and the delegate
  skill stopped safely without emulating one; an editable-install switch let
  a file-only pi session read stale `share/` paths with no warning until init
  ran; a sub-agent started from a runner session inherits the runner's
  project, so probe cases must run as headless sessions rooted in the scratch
  project.
- **Sub-agent emulation: decided.** On 2026-10-24 the operator kept the
  harness-provided sub-agent as the only worker route and ruled that the
  ADR 118/119 headless launches are not an emulation of it (see next step 3
  and the ADR 086 worker amendment).
- **Health check.** `cp-skill-health-check` pairs PowerShell forms only in its
  uv-tool and legacy-residue steps; layout, pointer and validator steps are
  Bash-only. Owned by E1 in
  [execution-channel-compatibility](../execution-channel-compatibility/README.md).

## Open questions

Status as of the 2026-10-24 runs in brackets.

- **Missing initialization.** [answered on Linux] In Codex's revision 4 run, an agent in a clone without init found a nearby source checkout and answered from it. The `AGENTS.md` rule to stop and ask for init was followed in Claude Code, Codex and pi (case 8, one session each); the Codex result notes one observation does not establish reliability across configurations.
- **Emulated skills.** [answered on Linux for a named check] The skill index in `library.md` led to the real skill in nine of nine fresh sessions with no stub present (three per harness). Whether the index triggers on an unnamed task, as the router stub did in case 4, is untested. Through the index the request's arguments reached the skill only when the model carried them (pi yes, Codex no), hence the routing-file sentence added 2026-10-24.
- **Skill metadata.** [no new evidence] No harness needed metadata beyond name and description. The probe's skills still carry none.
- **The enterprise harness.** [open] No reply. Which of the design's harness assumptions (H1–H6 in [design.md](./design.md#what-the-design-assumes-about-a-harness)) hold there, and what loads standing instructions, remain unknown; the probe request's pointer line is the proposed answer.
- **The router skill at scale.** [open] It worked with a small index in all three harnesses. Untested with an index the size of the real library.
- **Windows and macOS.** [open] No run. The byte-order-mark crash (fixed in revision 5) is the only Windows observation. The read rule's form on Windows, `Read(//C:/…/**)`, is what init writes and is untested; the protocol's case 2 asks Windows runners to record whether Claude Code honours it.
- **Running sessions.** [open] A running Claude Code session picked up skills added after it started. An upgrade inside a running session was not tested; the pi run showed that a file-only session reads stale paths after an install-mode switch with no warning until init runs.
- **Centrally managed settings.** [open] Untested.
- **Sub-agents in pi.** [resolved in principle 2026-10-24] Stock pi has no sub-agent tool; the delegate skill stopped with "no sub-agent available". The route is a pi extension supplying one (this checkout's `.pi/extensions/subagent`), per the ADR 086 worker amendment; delivering it to pi users of installed projects is next step 3's remaining follow-up.

## Next steps

Status as of 2026-10-24 in brackets. Order reflects dependency: the probe
package and the release must match before any new run is evidence.

0. **Refresh the probe package.** [done 2026-10-24] Revision 7 mirrors the
   current `commonplace-init`: `--root` and `--check` with relative paths and
   `collision`, symlink-as-foreign, POSIX stub paths with `$ARGUMENTS`
   pass-through, the four-entry-point `library.md`, the `Read(//…/**)` rule,
   a fixed skill list, the two control-plane templates, and nearest-project
   staleness warnings. It adds case 11 (a stub invoked with arguments). The
   protocol states which cases a revision 4 or 6 runner must repeat. Verified
   in a scratch venv: normal install, idempotent rerun, upgrade without init
   (all `ok`), description change (`stale` and warning), collision, foreign
   symlink, extra stub removal, editable install (`stale`), and `--remove`.
1. **Release.** [half done] Bump the version and publish to PyPI, the only
   channel; v0.2.0 shipped 2026-09-25 but 1603 later commits are unreleased.
   Then install from PyPI on a clean machine, including macOS and Windows where
   possible, and run `commonplace-init` and `commonplace-init --check` in a new
   project. [the clean-machine install has no recorded run on any platform]
2. **Probe follow-ups.** [Linux done 2026-10-24; other harnesses open]
   Claude Code and Codex ran cases 0 and 8–11 and pi ran the full protocol,
   all on Linux. Still open: the index route with arguments after the
   2026-10-24 routing-file change (rerun case 11 without stubs in Codex); a
   Codex run with sessions rooted in the project, since its revision 7 agents
   kept the repository's instructions and never read a stub; Windows and
   macOS; and agents in other harnesses answering the same
   [probe request](./probe-request.md): Gemini CLI, OpenCode, Cursor, Goose,
   GitHub Copilot, and enterprise harnesses; enterprise results may come back
   through the operator, anonymised. Findings that change the decision amend
   ADR 086.
3. **Sub-agent emulation.** [decided 2026-10-24; ADR 086 worker amendment]
   The operator chose the sub-agent route and rejected headless launches as an
   emulation: a sub-agent is a two-way, inspectable relationship, a headless
   launch a one-way action. Skill rules stand unchanged; `cp-skill-ingest`
   keeps forbidding CLI launches. A harness without a native sub-agent gets
   one as a harness extension, as this checkout's `.pi/extensions/subagent`
   does for pi, and until then its users lack the worker-dependent skills.
   Remaining follow-up: how pi users of an installed project receive that
   extension, since it lives in this checkout's `.pi/`, not in the package or
   in anything init writes; decide and record when a pi user outside this
   checkout needs it. What the facility must do is fixed in
   [sub-agent-requirements.md](./sub-agent-requirements.md) (2026-10-26).
   Delivery decided the same day, kept simple: `INSTALL.md` step 5 tells pi
   users to copy the extension and the worker definition from a checkout into
   their user-level `~/.pi/agent/` once; nothing is added to the package or to
   init. Untested outside this checkout; the probe's case 10 in a scratch
   project with that copy in place is the acceptance test. The analysis workflow's Workjig launches are a workflow
   engine's workers under ADR 118/119 and are unaffected.
4. **Coupled workshops.** [done 2026-09-25] Both coupled workshops closed that
   day; no replies are outstanding.

## Evaluation boundary

- Harnesses: Claude Code and Codex, plus the base layer in any harness that meets its stated assumptions.
- Operating systems: Linux, macOS, and Windows.
- Places: the source checkout and an installed project.
- Upgrade cases: an upgrade that changes a skill, one that changes only library files, and one that moves the install location.

## Coupling

None open.

## Closure

The design is recorded in ADR 086. Close when each follow-up above is done or deferred with a trigger and each open question is answered or deferred with a trigger. Then delete this directory and its entry in `kb/work/README.md`.

## Files

Current:

- [design.md](./design.md) — the design as it stood at adoption (pre-adoption record; ADR 086 is authoritative)
- [alternatives.md](./alternatives.md) — rejected options, why, and the evidence by probe revision (pre-adoption record)
- [probe-package/](./probe-package/PROTOCOL.md) — the shared probe (revision 7, 2026-10-24, mirrors the current `commonplace-init`): a throwaway uv package, a test project, the protocol every harness runs, and a results template
- [probe-request.md](./probe-request.md) — the open request to agents in any harness to run the probe, with a log of replies
- [sub-agent-requirements.md](./sub-agent-requirements.md) — what a skill needs from a harness sub-agent (S1–S13), who demands each, and what the pi extension claims to cover
- [pi-nesting-control.md](./pi-nesting-control.md) — analysis and handoff for making worker nesting a budget instead of a ban in the pi subagent extension (2026-10-26)
- [run-prompts.md](./run-prompts.md) — the prompts to paste into a fresh Claude Code, Codex or pi session to run revision 7, and the one-harness-at-a-time rule
- [results-claude-code-r4.md](./results-claude-code-r4.md) — Claude Code's run of revision 4
- [results-codex-r4.md](./results-codex-r4.md) — Codex's run of revision 4
- [results-claude-code-r7.md](./results-claude-code-r7.md) — Claude Code's run of revision 7 (cases 0, 8–11)
- [results-codex-r7.md](./results-codex-r7.md) — Codex's run of revision 7 (cases 0, 8–11; agents not rooted in the project)
- [results-pi-r7.md](./results-pi-r7.md) — pi's run of revision 7 (full protocol)

Background research:

- [comparable-systems-survey.md](./comparable-systems-survey.md) — how harnesses and 14 comparable systems deliver skills and libraries
- [gbrain-delivery-methods.md](./gbrain-delivery-methods.md) — code-grounded study of GBrain v0.54.1.0's delivery methods

Evidence from earlier revisions, cited by `alternatives.md`:

- [probe-results.md](./probe-results.md) — early probes: a Claude Code link-mode plugin, a Codex skill symlink, uv shared data
- [results-codex.md](./results-codex.md) — Codex's runs of revisions 1–3
- [results-claude-code.md](./results-claude-code.md) — Claude Code's run of revision 3
