# Execution-channel inventory

## Status

Initial lexical baseline, 2026-07-28. These counts establish the search boundary; they are not yet a semantic classification of executable versus illustrative occurrences.

The scan covers `AGENTS.md`, `AGENTS.md.template`, `INSTALL.md`, and all Markdown under `kb/instructions/`. Canonical instructions are counted; generated `.claude/skills/` and `.agents/skills/` projections are excluded to avoid double counting.

## Baseline

| Signal | Initial result | Meaning and limitation |
|---|---:|---|
| Markdown files under `kb/instructions/` | 83 | Full canonical instruction collection, including type/readme/support files |
| Shell-language fences in the scoped surface | 66 | `bash`, `sh`, PowerShell, batch/cmd, console, or shell fences; a fence may be illustrative |
| Scoped files mentioning `commonplace-*` | 27 | 24 canonical instruction files plus `AGENTS.md`, its template, and `INSTALL.md` |
| Scoped files mentioning `rg` | 14 | 11 canonical instruction files plus the three root/control-plane surfaces |
| Promoted `SKILL.md` files mentioning `commonplace-*` | 6 | Compilation of promoted skills alone cannot cover the other 18 canonical instruction files |
| Promoted `SKILL.md` files mentioning `rg` | 4 | `rg` also appears outside promoted skills |

The first conclusion is structural: promoted skills are not a sufficient compilation or portability boundary. Any solution scoped only to them leaves executable Commonplace commands in non-promoted instructions and leaves part of the `rg` surface unresolved.

## Initial tool census

File counts below are lexical counts over the same broad surface, not yet confirmed command invocations.

| Tool or family | Files | Initial concern |
|---|---:|---|
| `commonplace-*` | 27 | Project-local venv, bare-name resolution, `.exe` layout on Windows, package version identity |
| `rg` | 14 | Availability outside bundled agent runtimes; compatible flags and regex behavior on native Windows |
| `find` | 13 | POSIX utility absent from stock PowerShell; some mentions may mean search conceptually rather than the executable |
| Git | 11 | Declared development prerequisite, but command availability, repository discovery, and sandboxed `.git` access differ |
| uv | 4 | Installation/update owner versus runtime dependency; cache location and sandbox access |
| pytest | 4 | Project-venv resolution and Windows executable suffix; should not silently fall back to a global pytest |
| `python3` | 4 | Native Windows normally exposes `py -3` or `python`, not necessarily `python3` |
| `python` | 1 | May resolve differently from `py -3` or the project venv |
| direnv | 3 | Shell-hook inheritance; not a native Windows baseline and not inherited by desktop apps automatically |
| `xargs` | 2 | POSIX-only baseline; `-r` semantics are load-bearing in at least one known instruction |
| `wc` | 2 | POSIX pipeline dependency with easy but non-literal PowerShell alternatives |
| `sort` | 2 | Name exists in several systems with different command resolution and behavior |
| `sed` | 1 | POSIX text-processing dependency; broader substring scans overcount prose such as “used” |
| curl | 1 | Modern Windows often aliases or ships curl differently; flags and proxy behavior need verification |
| Roughdraft | 1 | Optional external application/CLI with GUI-launch and platform-support questions |
| Codex / Claude runner names | 3 / 10 | Mostly runtime discussion today; later semantic classification must separate prose references from nested CLI invocation |

Known workflow-specific tools not surfaced by this first broad lexical count—because they live in narrower references, code, local settings, or adjacent workflows—must still be checked when a live instruction routes to them. Candidates include `qmd`, `ruff`, `mkdocs`, `sqlite3`, `jq`, `gh`, `awk`, and `flock`.

## Commonplace command surface

The initial scan found these command-like identifiers. Some are placeholders or prose identifiers and must be classified before being treated as real entry points:

- `commonplace-ack-review`
- `commonplace-create-review-jobs`
- `commonplace-finalize-review-job`
- `commonplace-freshness-retire`
- `commonplace-freshness-status`
- `commonplace-github-snapshot`
- `commonplace-guard-full-pass-report`
- `commonplace-init`
- `commonplace-relocate-directory`
- `commonplace-relocate-note`
- `commonplace-review-target-selector`
- `commonplace-validate`
- `commonplace-warn-selector`
- `commonplace-x-snapshot`

False-positive or vocabulary candidates already visible include `commonplace-foo`, `commonplace-repo`, `commonplace-store`, and `commonplace-checkout-refreshed-at`. The semantic pass must reconcile every apparent command against `[project.scripts]` in `pyproject.toml` rather than accepting lexical shape as existence.

## Inventory record

Each executable locus should receive one record with these fields:

| Field | Purpose |
|---|---|
| `locus_id` | Stable identifier derived from canonical path plus heading/role |
| `artifact_path` | Canonical source, not a generated projection |
| `consumer` | Agent, operator, hook, subprocess, or generated worker |
| `instruction_excerpt` | Minimal literal command or procedure under analysis |
| `tool_ids` | Every external executable or runtime facility required |
| `shell_constructs` | Pipes, redirects, command substitution, environment assignment, globbing, conditionals, quoting |
| `path_assumptions` | Separator, venv layout, executable suffix, current directory, project-root discovery |
| `availability_class` | Required prerequisite, package-owned, runtime-bundled, optional accelerator, or replaceable detail |
| `install_owner` | Commonplace install, project install, runtime, OS, or operator |
| `verification` | Exact bare-name/session probe and expected result |
| `fallback` | Explicit alternative or “none”; distinguish loud from silent degradation |
| `channels_verified` | Dated runtime/OS/shell observations with versions |
| `candidate_solutions` | References into the solution catalogue, without selecting one prematurely |

Every proposed probe also needs an implementability record before it enters the shared procedure:

| Field | Purpose |
|---|---|
| `target_environment` | Source checkout, initialized full project, reader/vendor install, package-only, remote/restricted, or other |
| `prerequisites` | Required shell facility, resolved executable, local fixture, readable path, write scope, launch action, or second prepared environment |
| `prerequisite_probe` | Observation that establishes each prerequisite without assuming the conclusion |
| `safe_when_absent` | Exact `not run` result when a prerequisite is missing or unknown |
| `mutation_scope` | Expected state changes; landscape probes should be read-only except for explicitly bounded process-local state |
| `layout_independence` | Whether the probe works outside this source checkout and how its targets are discovered |

No check joins the cross-environment procedure merely because it is useful in this repository. It must either be executable through facilities already known to exist in the target environment or be guarded by a preceding capability observation.

## Runtime capability matrix schema

For every execution system, record:

- operating system and filesystem/path model;
- shell used for ordinary tool calls and for hooks;
- whether separate tool calls share a process, current directory, aliases, functions, and exported environment;
- how a runtime launched from a shell inherits environment;
- whether desktop/IDE surfaces reuse a long-lived process across projects;
- session-start, resume, compact, and directory-change hooks;
- whether hooks can persist environment into later tool calls;
- project-local environment configuration and whether it can prepend to inherited `PATH`;
- worktree creation/setup behavior;
- executable suffix and command lookup rules;
- bundled tools, with version and whether bundling is a documented contract;
- sandbox filesystem, network, process, and home/cache constraints.

## Round 1 procedure feedback

The retained Round 1 reports—[Codex source checkout](./evidence/2026-07-28-codex-api-posix-linux-a5.md), [Codex initialized project with an unallowed `.envrc`](./evidence/2026-07-28-codex-api-posix-linux-a4.md), and [Claude Code source checkout](./evidence/2026-07-28-claude-code-cli-linux-bash-c4.md)—established ten corrections to the breadth probe:

1. Record exact project-venv `PATH` membership separately from `VIRTUAL_ENV`. The report observed project-venv command resolution with `VIRTUAL_ENV` unset; that is compatible with a stable baseline `PATH` supplied independently to each fresh tool call.
2. Treat PID equality as inconclusive. Fresh isolated processes can reuse the same small PID, while the deliberately mutated environment variable and shell function directly test shell-state persistence.
3. Scope Git status to one established fixture. Whole-worktree cleanliness is unrelated to command-channel capability and can produce large, privacy-sensitive, or distracting output.
4. Treat the unchanged working directory as call context, not a persistence test. Round 1 does not mutate it, so only the deliberately mutated environment variable and function answer the same-shell question.
5. Make every ordinary block self-contained. Once fresh-call behavior is a live possibility, a later block cannot reuse a shell variable assigned during layout discovery.
6. Record baseline-provider evidence without dumping it. Marker values and `.envrc` contents are unnecessary and may contain secrets.
7. Do not equate `.envrc` or direnv-marker presence with authorization or loading. The initialized-project report had both while its `.venv/bin` was absent from `PATH` and the bare Commonplace command failed. A conditional, redacted `direnv status` check must distinguish the workspace file being found, allowed, and loaded from state inherited from another directory.
8. Treat failed direnv authorization as decisive when the expected venv directory is absent from `PATH`. `Loaded RC path` may still name the current file; that label alone does not show its exports were applied.
9. Record command kind without dumping definitions. Claude Code supplied `find` as a runtime function shim, demonstrating that name resolution is not executable identity; alias targets and function bodies are unnecessary and potentially sensitive in a breadth report.
10. Keep shell-mutation persistence separate from launcher inheritance. Fresh tool shells rule out activating once inside a tool call, but an environment established before launching the runtime may still be inherited as the baseline of every fresh child; that requires a separate launch comparison.

These changes define procedure ID `execution-channel-round1-v4-2026-07-28`. The retained v4 reports supersede and replace their v3 runs.

### V4 confirmation

The retained [Claude Code v6 report](./evidence/2026-07-28-claude-code-cli-linux-bash-c4.md) reproduces the earlier v4 environment while classifying the runtime-supplied `find` name as a function without disclosing its definition. The [Codex initialized-project v4 repeat](./evidence/2026-07-28-codex-api-posix-linux-a4.md) reproduced command-discovery failure and correctly concluded that an unallowed `.envrc` had not prepared the environment despite a matching `Loaded RC path` label.

Together they form an allowed/unallowed direnv contrast:

| Environment | `.envrc` found | allowed | loaded path names workspace | project venv on `PATH` | bare Commonplace command |
|---|---:|---:|---:|---:|---:|
| Claude Code source checkout | yes | yes | yes | yes | succeeds |
| Codex initialized project | yes | no | yes | no | fails |

This confirms v4's observation rules. Causal attribution remains weaker than the observed state: the positive report is consistent with direnv preparation but does not isolate hook execution from launcher inheritance. For solution comparison, directory-aware environment management is therefore catalogued separately from runtime-native project configuration.

### V5 disclosure hardening

Reviewing the probe as a payload sent to collaborators exposed a retention risk independent of its final report rules: raw `direnv status` enters the tool transcript before an agent can summarize it, carrying allow hashes, watch metadata, and local paths. Procedure v5 captures that output inside the shell process and emits only workspace-match, authorization, and loaded-identity classifications.

V5 also makes disclosure review a completion condition. Reports normalize workspace/home/temp prefixes, inspect the final payload for credential and configuration material, withhold evidence that cannot be safely redacted, and append an explicit attestation. The review itself is tool-independent; an already available scanner may supplement it but cannot become a new prerequisite.

### V6 persistence-output correction

The superseded Claude Code v5 run identified an internal inconsistency: the step-7 census used kind-only discovery, but the published POSIX persistence blocks still used `type commonplace_shell_probe_function`, which prints the function definition before the final disclosure review can remove it. The reporter safely substituted `type -t`, but that is Bash-specific and would make nominally comparable runs differ from the instruction.

Procedure v6 removes resolver output from the persistence test entirely. Call A invokes the controlled function and records its literal result; call B runs `command -v` with output discarded and records only a presence boolean. The persistence evidence is unchanged, works in a POSIX shell, and cannot retain the definition.

The retained [Claude Code](./evidence/2026-07-28-claude-code-cli-linux-bash-c4.md) and [Codex](./evidence/2026-07-28-codex-api-posix-linux-a5.md) v6 reports both execute the published blocks without deviation, retain only the controlled result and presence boolean, and pass the disclosure review. Their option-4 wording about `.envrc` is provisional report interpretation: until a runtime-native project configuration mechanism is observed, directory-aware direnv evidence belongs to option 16.

## Repeatable sweeps

The workshop should turn these exploratory searches into a checked script only after the inventory record stabilizes. Until then, retain the commands as investigation aids:

```bash
rg -l '\bcommonplace-[a-z0-9-]+' AGENTS.md AGENTS.md.template INSTALL.md kb/instructions --glob '*.md'
rg -l '(^|[^[:alnum:]_-])rg([^[:alnum:]_-]|$)' AGENTS.md AGENTS.md.template INSTALL.md kb/instructions --glob '*.md'
rg -n '^```(bash|sh|powershell|batch|cmd|console|shell)' AGENTS.md AGENTS.md.template INSTALL.md kb/instructions --glob '*.md'
```

The eventual sweep must parse fenced blocks and declared command positions rather than relying only on regex. It must also inspect files linked as required execution references and reconcile `commonplace-*` names against the package entry-point registry.

## Next inventory passes

1. Classify all 27 `commonplace-*` files by executable locus and distinguish real commands from placeholders.
2. Parse all 66 shell-language fences, recording constructs separately from executable names.
3. Trace required links from every canonical instruction so command-bearing references enter the graph.
4. Verify the `rg` contract per runtime: installation source, version, command lookup, regex/flag compatibility, and sandbox behavior.
5. Repeat for Git and the POSIX utility cluster, then for workflow-specific tools.
6. Compare source checkout, installed KB, and worktree command environments.
