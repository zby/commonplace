# Windows Claude read rule: matched and path-form tests (2026-11-03)

## Purpose

The [default-permission check](./results-2026-11-03-windows-claude-default.md) could not attribute library reads to init's Claude Code read rule. This run compares disposable projects that differ only in that rule, then tests two other spellings of the same path. The operator authorized the matched test in chat on 2026-11-03.

## Setup

- Machine and installation as in the [Workjig 0.3.1 report](./results-2026-11-03-windows-workjig-031-recovery.md): Windows 11, `llm-commonplace` 0.3.3 from PyPI with Workjig 0.3.1, library root `C:/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace`.
- Four disposable projects under `<HOME>`, each made the same way: `git init`, `commonplace-init`, templates renamed, first commit. They differ only in the untracked `.claude/settings.local.json`:

  | Project | `settings.local.json` |
  |---|---|
  | `cp-read-rule-on` | init's rule, unchanged: `Read(//C:/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace/**)` |
  | `cp-read-rule-off` | deleted |
  | `cp-read-rule-home` | `Read(~/.local/share/uv/tools/llm-commonplace/share/commonplace/**)` |
  | `cp-read-rule-lowerc` | `Read(//c/Users/zzbby/.local/share/uv/tools/llm-commonplace/share/commonplace/**)` |

- No project has `.claude/settings.json`; no `~/.claude/settings.json` or `~/.claude/settings.local.json` exists. Managed policy was not observable.
- Each probe was a new Claude Code desktop-app session rooted in its project, started by the maintainer's session with `permission_mode: default`. Each session's metadata reported `permissionMode: "default"`. Each read `.claude/settings.local.json`, then read the first 10 lines of `<library>/instructions/cp-skill-validate/SKILL.md` with the native Read tool only. The operator accepted the workspace-trust prompt for each new folder and rejected every file-read permission prompt.

## Results

| Project | Rule form | Library read |
|---|---|---|
| `cp-read-rule-on` | `//C:/…` (init's) | Prompted; rejected by the operator. |
| `cp-read-rule-off` | none | Prompted; rejected by the operator. |
| `cp-read-rule-home` | `~/…` | Content returned, no rejection. |
| `cp-read-rule-lowerc` | `//c/…` | Content returned, no rejection. |

The on/off pair prompted alike, so init's rule as written has no effect on Windows. Both other spellings let the same read through. The probes cannot see prompts. The operator rejected every read prompt, so a returned read means no read prompt appeared; this was not separately confirmed for the two variant sessions. Workspace trust was the same in all four and does not explain the difference: per the [settings documentation](https://code.claude.com/docs/en/settings), allow rules in an untracked `settings.local.json` apply without trust, and trust does not grant reads outside the project.

## Interpretation

Claude Code appears to match Windows paths in a POSIX form with a lowercase drive (`/c/Users/…`), so a `//C:/…` rule never matches. init builds the rule with `root.as_posix()` ([`library.py`](../../../src/commonplace/lib/library.py)), which on Windows yields `C:/Users/…`. This is a Commonplace product defect on Windows: every Windows project gets a rule that does nothing, and library reads prompt in default mode. The Claude Code [permissions documentation](https://code.claude.com/docs/en/permissions) gives only POSIX examples for `//path` and does not state the Windows form; this run is the evidence for it.

Either form that passed would fix init. `//c/…` works for any library location; `~/…` works only when the library is under the home directory.

The [earlier default-permission report](./results-2026-11-03-windows-claude-default.md) found both the library read and an outside-rule control read succeeding in a project with the same `//C:/…` rule. The operator recalls accepting only workspace trust there, not read prompts. That result is unexplained; it does not affect the on/off comparison, which ran under the same conditions in both projects.

## Disposition

Operator decision (2026-11-03): record the defect and do not fix init now; return to it when a Windows user reports library-read prompts. The proposed fix is for init to write `//<lowercase drive>/<path>` on Windows, then confirm with one disposable project.

## Not covered

- The control-file reads: rejecting a prompt ends the session's turn, and the on/off library reads already settle the question.
- A library outside the home directory, other drive letters, and UNC paths.
- Codex, which needs no read rule.
- Why the earlier default-permission probe read without prompting.

## State left behind

The four projects and their control files in `%LOCALAPPDATA%\Temp` remain; the operator may delete them. Nothing in the checkout or the installed tool changed.
