# Implementation staging

## Intent

Prepare the whole implementation of [design.md](./design.md) (draft [ADR 086](./adr-draft.md)) without changing the live system, so that adopting the ADR is one apply step followed by the test suite. The operator chose to go ahead without waiting for more probe replies (2026-09-25). The stage is finished when applying it to a clean copy of the repository gives a tree where `uv run pytest` and `uv run ruff check .` pass, `commonplace-validate` passes on the changed documents, and an installed project initialised from the built package works as the design describes.

## How the stage is laid out

- `staged/files/` holds every large change as the complete new file, at the path it will have in the repository. A file that tools would read as live configuration, such as `pyproject.toml`, is stored with a `.staged` suffix so the live ruff and uv do not pick it up.
- `staged/delete.txt` lists repository paths the change removes, one per line.
- `staged/migrations/` holds scripts for mechanical rewrites across many files, such as the `type:` pointer rewrite. They run in name order after the files are copied.
- [CHANGES.md](./staged/CHANGES.md) lists the changes of one or two lines, which are made directly at apply time instead of being staged (operator direction, 2026-09-25).
- `staged/apply.py <repo root>` copies the files, deletes the listed paths, and runs the migrations. Apply it to a scratch copy to test; applying it to the checkout is the adoption step.

A staged file is a full replacement. If its live counterpart changes before adoption, the staged copy must be rebased on the new version; `apply.py` refuses to overwrite a file whose live content no longer matches the base recorded when it was staged.

## Work order

The pieces depend on each other (removing the copy needs the library reads, which need review identity and the schema changes), so only the complete stage has to be coherent. They are built in this order, each to completion before the next:

1. **Delivery core.** Ship the library as wheel shared data mirroring `kb/`. A library-root module (source tree in editable installs). `commonplace-init` rewritten: stubs, `.commonplace/library.md` with the skill index, the Claude Code read rule, `.gitignore` entries, `--check`, migration that keeps differing files, UTF-8 with BOM tolerance. `AGENTS.md` and new `CLAUDE.md` templates. The new router skill `cp-skill-library`. The shared staleness check in every `commonplace-*` command.
2. **Types.** Bare global type names in the resolver, rule dispatch, type specs' `schema:` pointers, and schema `const:` pins. Local schemas, including the scaffolded report and source types, restate what they took from `note.schema.yaml`. A migration rewrites the `type:` lines.
3. **Review.** Gates and the critique instruction read from the library root; `commonplace:` criterion identifiers; freshness accepts package inputs; a migration retires the affected baselines once.
4. **Skills and health check.** Promoted skills use relative links and lose the two-branch wording. `cp-skill-health-check` checks init's outputs instead of `kb/commonplace/`.
5. **Documentation.** `INSTALL.md`, architecture, collections and types, commands, the `AGENTS.md` template, and the other references the survey listed. The ADR moves to `kb/reference/adr/`.

## Status

| Step | State |
|---|---|
| 1 Delivery core | staged 2026-09-25. Applied to a clean worktree: pytest (774) and ruff pass. A wheel built from it, installed in an isolated uv tool directory, put the library under `share/commonplace/`; init in a new project wrote 24 outputs, all `ok`, and a command run from a project subdirectory warned after `library.md` was altered. The command check is a decorator on each command's `main`, added by `migrations/10_decorate_command_mains.py`, which keeps the `module:main` convention the command catalogue test enforces. |
| 2 Types | staged 2026-09-25, together with most of step 3, because type-conformance review uses global type specs as criteria. `lib/type_resolver.py` resolves bare global names in the library and rejects path forms to them; `migrations/20_bare_type_names.py` rewrites `type:` lines and inline spans, global `schema:` pointers and `const:` pins, local schema refs to `commonplace:types/...`, identity literals in `src/`, and test fixtures. Applied to a clean worktree: pytest (774) and ruff pass; `commonplace-validate` on notes, reference, instructions, types, sources, and agent-memory-systems reports the same failures as before the stage. |
| 3 Review | mostly staged with step 2: `artifact_identity`/`artifact_file` in `lib/library.py`; the gate catalog and critique instruction read from the library; `commonplace:` identities for criteria outside the repository; freshness reads them. `commonplace-init` retires, once per installed project, current baselines recorded under the old copy's criteria (`kb/commonplace/...`, and `kb/types/<name>.md` for global types); review history is kept. Step complete. |
| 4 Skills and health check | staged 2026-09-25. Promoted skills use relative links resolved from their real location; worker packets get absolute paths resolved the same way; the re-ingest route names the library instruction instead of a path. `cp-skill-write` names global types by bare name. `cp-skill-health-check` classifies layouts by `.commonplace/`, runs `commonplace-init --check`, and flags an old `kb/commonplace/` copy. Applied: pytest (775), ruff, and `commonplace-validate kb/instructions` pass. |
| 5 Documentation | not started |
