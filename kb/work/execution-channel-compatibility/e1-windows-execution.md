# E1 plan — Make native Windows support operative

**State:** open; moved here from the system-contract consistency workshop
when it closed on 2026-09-25; rebaselined at commit `6660bd2a` on 2026-08-27. The
[manifest-derived promoted-skill audit](./e1-promoted-skill-rebaseline-2026-08-27.md)
classifies all ten skills selected in that snapshot without making the count a
future inventory. The implementation dispositions and native-Windows evidence
remain open. Rechecked 2026-09-25: health check, connect, and validate still
carry the unpaired POSIX commands the audit names.

## Resolution selected

Retain native Windows support. Installation, PATH ownership, and skill stubs
already have native-Windows behavior; narrowing support now would
discard working product surface to avoid fixing three visible procedures.

Prefer shell-neutral package commands or runtime-native tool operations for
load-bearing behavior. Use paired POSIX/PowerShell snippets only where diagnosis
must work before a package command can be assumed available.

A skill must not recreate collection discovery with shell globs; it calls the
package's contract-based discovery.

## Work

1. **Static rebaseline — complete 2026-08-27.** The owner workshop now uses the
   user-level uv-tool model, and the dated audit derives its exact selected set
   from `MANIFEST.promoted_skills`. Its implementation guard must preserve that
   set equality rather than encode “all ten” or a remaining count.
2. Collect at least one native-Windows PowerShell result after the owning
   package operations land. The current audit is source-static and Linux-hosted;
   it makes no native-Windows runtime claim.
3. Add a package-owned `commonplace-validate all` target. V1 closed without
   it (ADR 086 removed the nested library collections the glob missed), so
   E1 now owns it: the CLI enumerates collections through the existing
   contract-based discovery, honours validation-ignore markers, continues
   after failures, and reports one aggregate result. Then make
   `cp-skill-validate` pass its requested target straight to
   `commonplace-validate <target>` with no shell program in the skill.
4. Do not replace connect's pipeline with permanent runtime-specific Grep/Read
   choreography. Put deterministic tag/path collection behind a package command
   or shared Python helper, preferably T1's exact resolver once available, and
   keep the skill a thin caller. Preserve a no-match test proving the search
   never widens to the repository.
5. Pair every health-check preflight:
   - project/layout presence;
   - canonical and projected skill presence;
   - uv command ownership;
   - legacy `.envrc` and `.venv` inspection.
   Keep repair instructions labelled by channel and do not treat the historical
   `.venv/bin` signature as a current dependency.
6. Implement the audit's remaining package/runtime dispositions: shared
   checksum and byte-preservation operations for write, ingest, ground, and
   multistage writing; portable capture and temporary-file operations for
   snapshot-web; runtime-native orchestration for AutoReason; and an explicit
   disposition for promoted skills' `allowed-tools: Bash` declarations.
7. Add Windows CI for package install, pristine init, validation, and focused
   health checks. Add a narrow static inventory/check for known incompatible
   idioms so a new unpaired `xargs`, POSIX conditional, or hardcoded `/tmp`
   becomes visible at review time.
8. Exercise a freshly initialized project on Windows, including stub and
   `library.md` paths into the installed library, without path-separator
   leaks.

## Completion

Every executable promoted-skill step is shell-neutral, runtime-native, or
explicitly paired, and Linux and Windows CI pass. Native-Windows evidence must
name successful health preflight, arbitrary-target validation, `validate all`,
connect's empty-tag path, and snapshot temporary-file handling, plus the audit
or static coverage of every remaining promoted step. The execution-channel
workshop then promotes the durable rule and owns closure of E1.
