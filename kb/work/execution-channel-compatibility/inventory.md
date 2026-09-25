# Execution-channel inventory

## Status

Rebaselined 2026-09-25 at `5a178374`, after [ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) (commands as a user-level uv tool) and [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) (library served from the installed package). The first lexical baseline was taken on 2026-07-28; both columns are kept below. This rebaseline adds a first semantic classification of the non-promoted instruction files. The promoted skills are classified in the [E1 rebaseline](./e1-promoted-skill-rebaseline-2026-08-27.md) and are not repeated here.

The scan covers `AGENTS.md`, `AGENTS.md.template`, `AGENTS.md.reader-fragment`, `INSTALL.md`, and all Markdown under `kb/instructions/`. Canonical files are counted. The `.claude/skills/` and `.agents/skills/` symlink projections are excluded to avoid double counting.

## Baseline

| Signal | 2026-07-28 | 2026-09-25 | Meaning and limitation |
|---|---:|---:|---|
| Markdown files under `kb/instructions/` | 83 | 120 | Full canonical instruction collection, including type/readme/support files |
| Shell-language fences, column 0 | 66 | 69 | The July regex. It misses fences indented under list items. |
| Shell-language fences, any indentation | — | 89 in 28 files | Use this count from now on. `INSTALL.md` also puts install commands in `text` fences, which neither count catches. |
| Scoped files mentioning `commonplace-*` | 27 | 42 | 39 instruction files plus the three root files |
| Scoped files mentioning `rg` | 14 | 14 | 11 instruction files plus the three root files |
| Promoted and router `SKILL.md` files mentioning `commonplace-*` | 6 | 8 of 11 | Not connect, write-multistage (its `references/promotion.md` does), or the router `cp-skill-library` |
| Promoted and router `SKILL.md` files mentioning `rg` | 4 | 2 | write, connect |

The structural conclusion from July is stronger now: 31 of the 42 files that mention commands are not promoted `SKILL.md` files. A solution scoped to promoted skills leaves most of the command surface untouched.

## Tool census

File counts are lexical and case-sensitive unless marked. The "nature" column comes from reading the hits.

| Tool or family | 2026-07-28 | 2026-09-25 | Nature now |
|---|---:|---:|---|
| `commonplace-*` | 27 | 42 | See the command surface below |
| `rg` | 14 | 14 | Standalone calls in most files; pipelines in `maintain-curated-indexes`, `retire-artifact`, `cp-skill-connect` |
| `find` | 13 | 18 | All prose. No instruction runs `find`. |
| Git | 11 | 12 | Executable in `AGENTS.md` commit rules, `INSTALL.md` reader install, `retire-artifact`, `ingest-paper-with-code`, `analyse-agentic-system`, `stage-an-article-package`, `refresh-a-proposal-current-state`, `analyse-agent-memory` |
| uv | 4 | 9 | Tool install in `INSTALL.md`, health check, snapshot-web; `uv run pytest` / `uv run python` in repo-internal procedures |
| pytest | 4 | 3 | All through `uv run` |
| `python3` | 4 | 3 | Executable in `retire-artifact` (`python3 -c` inside a pipe) and `stage-an-article-package` (`python3 scripts/…`) |
| `python` | 1 | 3 | All `uv run python …` |
| direnv | 3 | 0 | Removed with ADR 064. `.envrc` survives only as legacy residue (see below). |
| `xargs` | 2 | 2 | `xargs -r` in `maintain-curated-indexes` and `cp-skill-connect` |
| `wc` | 2 | 3 | `fix-review-warnings-sweep`, `cp-skill-snapshot-web`, `evaluate-scenarios` |
| `sort` | 2 | 1 | `maintain-curated-indexes` |
| `sed` | 1 | 3 | `maintain-curated-indexes` pipeline; `cp-skill-health-check` prints `.envrc` |
| curl | 1 | 3 | Executable only in `cp-skill-snapshot-web` |
| awk | — | 1 | `cp-skill-snapshot-web` |
| ruff | — | 1 | `AGENTS.md`, through `uv run` |
| Roughdraft | 1 | 2 | `roughdraft-review` (repo-local skill) |
| qmd, mkdocs, sqlite3, jq, gh, flock | — | 0 | Absent from the surface |
| grep, tr, uniq, mktemp, date, printf, basename, dirname | — | — | Present in executable fences: `maintain-curated-indexes`, `fix-descriptions`, `cp-skill-snapshot-web`, `cp-skill-revise-autoreason`, `cp-skill-validate`, `retire-artifact` |

The July Codex/Claude runner counts (3 / 10) cannot be reproduced because the July method was not recorded.

No executable `/tmp` or `$TMPDIR` path appears on the surface. The only temporary directory is `mktemp -d kb/reports/cache/…` in snapshot-web.

## Commonplace command surface

All 17 command names found on the surface are declared in `[project.scripts]`: `validate`, `init`, `relocate-note`, `relocate-directory`, `warn-selector`, `review-target-selector`, `create-review-jobs`, `finalize-review-job`, `ack-review`, `guard-full-pass-report`, `agentic-analysis-handoff`, `agentic-analysis-publication`, `freshness-status`, `freshness-retire`, `github-snapshot`, `x-snapshot`, and `source` (only in `AGENTS.md.template`).

Four `commonplace-…` strings are not commands: `commonplace-doctrine` and `commonplace-store` (file names), `commonplace-relocate-*` (the command family), and `commonplace-freshness-retire/1` (a JSON schema id). The July false positives are gone.

Eight declared entry points are never mentioned on the surface: `ack-trivial-note-changes`, `freshness-ack`, `store-healthcheck`, `promotion-candidates`, `review-job-list`, `resolve-criteria`, `status`, `verify-quotes`. That is a documentation question, not a channel one.

## Non-promoted instruction files

Every non-promoted instruction file that mentions `commonplace-*`, contains a shell fence, or carries inline executable commands. **E** means the agent is told to run commands; **P** means prose or illustration only. **Repo-internal** means the procedure assumes the Commonplace source checkout (`scripts/`, `src/`, `tests/`, `properdocs.yml`, `related-systems/`) and does not run in an initialized project.

### Shell-dependent (load-bearing constructs beyond one argv call)

| File | Kind | Constructs in executable position |
|---|---|---|
| `retire-artifact.md` | E | `rg … \| rg -i …`; variable assignment; `python3 -c` program inside a pipe; `while IFS= read -r … ; do printf … ; done` loop feeding `commonplace-freshness-retire --input -`; also edits `properdocs.yml` |
| `maintain-curated-indexes.md` | E | `rg \| grep -o \| tr \| tr \| sed \| sort \| uniq -c \| sort -rn`; `rg -l \| xargs -r rg`; unquoted glob `kb/notes/*.md`; line continuations |
| `fix-warnings/fix-descriptions.md` | E | `commonplace-validate notes 2>/dev/null \| grep "description:"` |
| `fix-warnings/fix-review-warnings-sweep.md` | E | `commonplace-warn-selector --json \| wc -l` |
| `run-review-batches.md` | E | selector `\| commonplace-create-review-jobs --input -` |
| `run-full-improvement-pass-on-note.md` | E | selector `\| commonplace-create-review-jobs --input -` |
| `review-triage.md` | E | selector `… > {ack-manifest}` |
| `migrate-semantics-preserving-gate-changes.md` | E | selector `… > {ack-manifest}` |
| `stage-an-article-package.md` | E; repo-internal | `python3 scripts/… > kb/work/staging/{slug}/inventory.md` |
| `refresh-agent-memory-review-taxonomy.md` | E; repo-internal | `uv run python - <path> <<'PY' … PY` heredoc importing package internals |
| `synthesize-agent-memory-landscape/SKILL.md` (repo-local) | E; repo-internal | `uv run python scripts/…` |
| `evaluate-scenarios/SKILL.md` (repo-local) | E; repo-internal | unquoted glob `tests/scenarios/*.md`; `wc -c < {path}` |

Two patterns recur. The selector-to-jobs pipe (`… | commonplace-create-review-jobs --input -`) and the selector-to-file redirect (`… > manifest`) are one command feeding another. PowerShell supports both, but its `>` writes UTF-16 by default in Windows PowerShell 5.1, which a JSON reader may reject. Letting the consuming command read from the producing command, or giving the producer an `--output` path, would remove the shell from both. `retire-artifact` and `maintain-curated-indexes` are the only instructions with real POSIX programs; they are the non-promoted counterparts of E1's validate and connect items.

### Shell-neutral (single argv calls; tool prerequisites only)

`analyse-agent-memory.md` (validate, `git show`), `asd-ste100-inspired-rewrite.md`, `change-a-contract-that-several-consumers-read.md` (repo-internal `commonplace-init --root` probe), `draft-ingest-report.md`, `extract-adopted-part-of-a-proposal.md`, `FIX-SYSTEM.md`, `fix-warnings/fix-review-warnings.md`, `publish-an-article.md` (partly repo-internal), `refresh-a-proposal-current-state.md` (`git log --since`), `resolve-full-pass-disposition.md`, `revise-note.md`, `re-ingest.md` (`rg`), `simplification-passes/place-external-systems.md`, `simplification-passes/revise-an-article-or-note.md`, `ingest-paper-with-code.md` (Git clone/fetch/merge in `related-systems/`), `cp-skill-write-multistage/references/promotion.md`, and the repo-local skills `analyse-agentic-system`, `scan-agentic-system-transfer`, `roughdraft-review` (external GUI/CLI).

### Prose only

`COLLECTION.md`, `README.md`, `write-instruction.md`, `review-gates/semantic/grounding-alignment.md`, `example-onboard-second-brain.md`.

## Library paths that break in an initialized project (ADR 086)

In an initialized project the library is at `<library root>/…`, and the project's own `kb/instructions/`, `kb/notes/` and `kb/reference/` hold only the project's own files. Relative Markdown links inside the library still work, because the installed tree mirrors `kb/`. The files below instead name a library file by a workspace-root path in prose or code spans. In a project that path finds nothing, or finds a project file of the same name.

This is a library-reachability defect rather than a shell one, but it has the same effect: the instruction works in the source checkout and fails silently elsewhere.

| Kind of path | Files (line numbers) |
|---|---|
| `kb/instructions/…` | `FIX-SYSTEM.md` (17, 60, 73, 83, 89); `fix-warnings/fix-review-warnings.md` (31, 55); `fix-warnings/fix-review-warnings-sweep.md` (38, 64); `run-compression-bundle-on-note.md` (10, 21–26, 61); `compression-bundle/README.md` (3); `run-full-improvement-pass-on-note.md` (8); `simplification-passes/revise-an-article-or-note.md` (71) |
| `kb/types/…` | `maintain-curated-indexes.md` (10, 61); `analyse-agent-memory.md` (23) |
| `kb/reference/…` | `evaluate-log-entry-for-note-creation.md` (32) |
| Ambiguous (project's collection or the library's) | `review-gates/semantic/grounding-alignment.md` (26–27); `extract-adopted-part-of-a-proposal.md` (22); `refresh-a-proposal-current-state.md` (19) |

Repo-internal and repo-local files with the same pattern are not listed; they only run in the source checkout. `cp-skill-health-check` (192) and `cp-skill-ground` (63–64) use such paths only in branches guarded for the source checkout, which is correct.

Fixed on 2026-09-25: the unambiguous paths became relative links from each instruction's own location, as ADR 086 did for promoted skills. Two worker-packet templates now ask for the absolute path resolved from the instruction's directory instead. The three ambiguous cases were left as they are, read as naming the project's own collections.

## Legacy `.venv` / `.envrc` references

No instruction tells an agent to run commands through a project venv. What remains:

- `AGENTS.md.template:151` and `AGENTS.md:214` prohibit prepending project-venv paths. Operative and correct.
- `INSTALL.md:302` and `:312` diagnose a venv shadowing the uv tool and describe removing the old two-line `.envrc`. Troubleshooting for migrated projects.
- `cp-skill-health-check/SKILL.md:168–169` detect residue. Line 168 runs `sed -n '1,80p' .envrc`, which prints up to 80 lines of the file into the agent transcript. An `.envrc` may hold secrets; the probe procedure forbids reading it for that reason. The health check needs only to know whether the file matches the old two-line signature, which can be tested without printing it. Routed to [E1](./e1-windows-execution.md) item 5, which already owns the health-check preflight.

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
| `path_assumptions` | Separator, executable suffix, current directory, project-root discovery, library root versus workspace path |
| `availability_class` | Required prerequisite, package-owned, runtime-bundled, optional accelerator, or replaceable detail |
| `install_owner` | Commonplace install, project install, runtime, OS, or operator |
| `verification` | Exact bare-name/session probe and expected result |
| `fallback` | Explicit alternative or “none”; distinguish loud from silent degradation |
| `channels_verified` | Dated runtime/OS/shell observations with versions |
| `candidate_solutions` | References into the solution catalogue, without selecting one prematurely |

Every proposed probe also needs an implementability record before it enters the shared procedure:

| Field | Purpose |
|---|---|
| `target_environment` | Source checkout, initialized project, legacy copied-library project, reader/vendor install, package-only, remote/restricted, or other |
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
- how a runtime launched from a shell inherits environment, and whether a restart picks up a changed user `PATH`;
- whether desktop/IDE surfaces reuse a long-lived process across projects;
- session-start, resume, compact, and directory-change hooks;
- whether hooks can persist environment into later tool calls;
- project-local environment configuration and whether it can prepend to inherited `PATH`;
- whether the file-read tool and a shell process can read the library root outside the workspace;
- worktree creation/setup behavior;
- executable suffix and command lookup rules;
- bundled tools, with version and whether bundling is a documented contract;
- sandbox filesystem, network, process, and home/cache constraints.

## Round 1 procedure feedback

This section records how the probe evolved from v3 to v6 under the project-venv model. Corrections 1, 7 and 8 and the direnv contrast describe a mechanism ADR 064 retired; the rest still apply to v7.

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

### V7 rebaseline (2026-09-25)

Procedure v7 follows ADR 064 and ADR 086. It drops the project-venv `PATH` signals and the `direnv status` check, and records `.venv` and `.envrc` as presence-only residue. It adds `.commonplace/library.md` and the legacy `kb/commonplace/` copy to layout classification, a library-reachability step (read the routing file, the library root, and one skill stub), command authority against `uv tool dir --bin`, `commonplace-init --check`, and `<UV_TOOLS>`/`<UV_TOOL_BIN>` normalization. v6 reports stay valid for tool-call persistence, discovery and bare-name results.

## Repeatable sweeps

The workshop should turn these exploratory searches into a checked script only after the inventory record stabilizes. Until then, retain the commands as investigation aids:

```bash
rg -l '\bcommonplace-[a-z0-9-]+' AGENTS.md AGENTS.md.template INSTALL.md kb/instructions --glob '*.md'
rg -l '(^|[^[:alnum:]_-])rg([^[:alnum:]_-]|$)' AGENTS.md AGENTS.md.template INSTALL.md kb/instructions --glob '*.md'
rg -n '^\s*```(bash|sh|powershell|batch|cmd|console|shell)' AGENTS.md AGENTS.md.template INSTALL.md kb/instructions --glob '*.md'
```

The eventual sweep must parse fenced blocks and declared command positions rather than relying only on regex. It must also inspect files linked as required execution references and reconcile `commonplace-*` names against the package entry-point registry.

## Next inventory passes

1. Classify every locus in the 12 shell-dependent non-promoted files with the inventory record above, and decide for each whether a package operation (catalogue option 9) or an `--output`/stdin change on an existing command removes the shell.
2. Fix or route the ADR 086 path hazards listed above; confirm the three ambiguous cases.
3. Trace required links from every canonical instruction so command-bearing references enter the graph.
4. Verify the `rg` contract per runtime: installation source, version, command lookup, regex/flag compatibility, and sandbox behavior.
5. Repeat for Git, then for workflow-specific tools (curl, awk, Roughdraft).
6. Extend the sweep to `text` fences and inline code spans that carry commands, which the fence count misses.
