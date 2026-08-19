# E1 plan — Make native Windows support operative

**State:** open, with partial health-check improvement. The manifest now
promotes nine skills. The health check pairs only its uv ownership step with
PowerShell; its layout, projection, and legacy-residue checks remain Bash-only.
Connect still uses a load-bearing `xargs -r` pipeline, and validate still embeds
a Bash `if`/`for` program.

## Resolution selected

Retain native Windows support. Installation, PATH ownership, and copied skill
projection already have native-Windows behavior; narrowing support now would
discard working product surface to avoid fixing three visible procedures.

Prefer shell-neutral package commands or runtime-native tool operations for
load-bearing behavior. Use paired POSIX/PowerShell snippets only where diagnosis
must work before a package command can be assumed available.

## Work

1. Rebaseline the execution-channel workshop on the user-level uv-tool model.
   Remove its stale project-venv/session-activation premise, inventory all nine
   promoted skills, and collect at least one native-Windows PowerShell result.
2. Consume V1: make `cp-skill-validate` pass the requested file, collection,
   `all`, `types`, `landings`, or `redirects` target directly to
   `commonplace-validate <target>`, with the CLI interpreting `all` and no shell
   program in the skill.
3. Replace connect's pipeline with an explicit two-call algorithm using the
   runtime's search/read tools: collect paths carrying the tag, stop cleanly on
   an empty set, then inspect descriptions only in returned paths. Preserve a
   no-match test proving the search never widens to the repository.
4. Pair every health-check preflight:
   - project/layout presence;
   - canonical and projected skill presence;
   - uv command ownership;
   - legacy `.envrc` and `.venv` inspection.
   Keep repair instructions labelled by channel and do not treat the historical
   `.venv/bin` signature as a current dependency.
5. Audit the remaining six promoted skills for shell syntax, utility flags,
   `/tmp`, path separators, executable discovery, process-persistence
   assumptions, `allowed-tools` declarations, and any declared Bash-only
   execution interface. In particular, recheck snapshot-web's temporary paths
   and revise-autoreason's POSIX file choreography.
6. Add Windows CI for package install, pristine init, validation, and focused
   health checks. Add a narrow static inventory/check for known incompatible
   idioms so a new unpaired `xargs`, POSIX conditional, or hardcoded `/tmp`
   becomes visible at review time.

## Completion

Every executable promoted-skill step is shell-neutral, runtime-native, or
explicitly paired, and Linux and Windows CI pass. Native-Windows evidence must
name successful health preflight, arbitrary-target validation, `validate all`,
connect's empty-tag path, and snapshot temporary-file handling, plus the audit
or static coverage of every remaining promoted step. The execution-channel
workshop then promotes the durable rule and owns closure of E1.
