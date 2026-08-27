# E1 promoted-skill execution rebaseline — 2026-08-27

## Scope and evidence boundary

This is the E1-specific rebaseline of the promoted skill surface. It was
inspected at repository `HEAD` `2f87aceb`; the manifest and selected canonical
skill files had no local diff at inspection time. The wider execution-channel
workshop and its retained probe reports remain useful historical evidence, but
their project-venv activation forcing case is not the current Commonplace
command model.

[ADR 064](../../reference/adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)
now makes the uv tool executable directory the command authority. One
user-level uv tool installation supplies the active `commonplace-*` command
version for an OS user. Projects may have a `.venv` for their own dependencies,
but that environment, activation, and direnv are not prerequisites for
Commonplace commands. After `uv tool update-shell`, the consuming shell, IDE,
desktop agent, or service must be fully restarted before bare-name lookup is a
valid test.

E1 therefore starts from two separate concerns:

1. The health preflight must establish uv ownership and bare-name resolution in
   the launch class being diagnosed.
2. After a package command resolves, promoted procedures must not depend on
   POSIX shell programs for their load-bearing behavior.

This run inspected source text from a POSIX environment. It did **not** execute
any procedure in native Windows PowerShell. The workshop's current evidence
directory contains only POSIX reports. ADR 064 records an earlier Windows
installation experiment, but that is not a native-Windows E1 result for the
current promoted skill set. E1's Windows runtime gate remains open.

## Manifest-derived selection

The selection authority is `MANIFEST.promoted_skills` in
`src/commonplace/scaffold_manifest.py`. A repeat audit must read that tuple,
preserve its order, map each value to
`kb/instructions/<skill-name>/SKILL.md`, and fail if a selected source is
missing or duplicated. It must not select a remembered list or stop after a
remembered count. Generated `.agents/skills/` and `.claude/skills/` projections
are drift-check surfaces, not additional inventory members.

The tuple currently resolves to the following dated observation:

| Manifest value | Canonical audit source |
|---|---|
| `cp-skill-write` | `kb/instructions/cp-skill-write/SKILL.md` |
| `cp-skill-validate` | `kb/instructions/cp-skill-validate/SKILL.md` |
| `cp-skill-connect` | `kb/instructions/cp-skill-connect/SKILL.md` |
| `cp-skill-convert` | `kb/instructions/cp-skill-convert/SKILL.md` |
| `cp-skill-health-check` | `kb/instructions/cp-skill-health-check/SKILL.md` |
| `cp-skill-ingest` | `kb/instructions/cp-skill-ingest/SKILL.md` |
| `cp-skill-snapshot-web` | `kb/instructions/cp-skill-snapshot-web/SKILL.md` |
| `cp-skill-revise-autoreason` | `kb/instructions/cp-skill-revise-autoreason/SKILL.md` |
| `cp-skill-write-multistage` | `kb/instructions/cp-skill-write-multistage/SKILL.md` |
| `cp-skill-ground` | `kb/instructions/cp-skill-ground/SKILL.md` |

Ten entries were observed in this run. That number describes this snapshot; it
is not the selection mechanism or a future completion condition.

## Classification rule

- **Shell-neutral now** means one executable is invoked with ordinary arguments
  and no shell control flow, expansion, pipeline, redirection, environment
  assignment, or POSIX-only utility semantics. The skill may still require the
  executable as a declared prerequisite.
- **Neutralize behind package/runtime operations** means shared, load-bearing
  behavior should use a tested `commonplace-*` command, a shared Python helper,
  or a runtime-native filesystem/process operation. Duplicating the whole
  procedure in PowerShell would create two implementations of the same
  semantics.
- **Paired preflight** is reserved for checks that must work before the package
  command can be trusted, or before an optional external capture tool is used.
  These checks need explicit POSIX and PowerShell forms with the same reported
  fields.
- **Dependency** means the skill should not receive an interim translation.
  Its portable form follows another packet that owns the missing semantics.

## Per-skill inventory

| Selected skill | Current executable or channel-sensitive loci | Disposition | Dependency |
|---|---|---|---|
| `cp-skill-write` | Targeted `rg`; direct `commonplace-validate <path>`; `commonplace-relocate-note`; exact snapshot-hash check on the conditional source route | The three commands are shell-neutral single-process calls. Use the shared snapshot verification operation for the source route rather than inventing a shell hash command. | None for the ordinary write path. Source-grounded writes share the checksum work described below. |
| `cp-skill-validate` | One Bash `if`/`for` program using glob expansion, `test`, `basename`, `dirname`, command substitution, and fail-fast exits | Remove the shell program after V1. The skill becomes one shell-neutral `commonplace-validate <target>` invocation and passes `all`, `types`, `landings`, `redirects`, a collection, or a path unchanged. | [V1](../system-contract-consistency/plans/v1-validate-all.md) owns recursive collection discovery, complete accumulation, and repository phases for `all`. |
| `cp-skill-connect` | Standalone title, description, and body `rg` calls; a by-tag `rg -l | xargs -r rg` pipeline whose no-match guard is load-bearing | Keep standalone `rg` calls as shell-neutral process invocations. Do not produce a PowerShell copy of the tag pipeline. Replace it with the exact shared tag/path resolver and retain a no-match test that proves search does not widen. | The tag pipeline depends on the exact resolver owned by [tag-contract convergence](../tag-contract-convergence/README.md), tracked from [T1](../system-contract-consistency/plans/t1-tag-scope.md). |
| `cp-skill-convert` | Backlink `rg -l`; `git mv`; backlink edits through runtime tools | `rg` and `git mv` are shell-neutral single-process calls. Git remains an explicit prerequisite. No paired shell program is needed. | None. |
| `cp-skill-health-check` | POSIX-only layout, projection, and legacy-residue blocks; paired but non-identical uv ownership blocks; direct validator, pytest, and repair commands | Add field-equivalent POSIX/PowerShell preflights for project/layout presence, canonical and projected skill presence, uv command ownership, and legacy `.envrc`/`.venv` inspection. Keep validation, `uv run pytest`, `uv tool install`, and `uv tool update-shell` as shell-neutral calls. The old `.envrc` body is a historical residue signature, not an active dependency. | Must remain independently executable when `commonplace-*` lookup fails; it cannot depend on V1 for its preflight. |
| `cp-skill-ingest` | Skill dispatch and direct validation; exact-byte SHA-256 checks; platform temporary backup; byte-copy, restore, and verification | Dispatch and validation are shell-neutral. Put checksum and handled-failure backup/restore semantics behind shared package/runtime byte operations. The current `cp`/`Copy-Item` examples acknowledge both channels but do not yet specify one parity-tested operation. | Mandatory connection discovery inherits `cp-skill-connect`'s portable completion. No direct V1 dependency. |
| `cp-skill-snapshot-web` | Shell-neutral GitHub/X package calls; POSIX `command -v` checks; `mktemp`, redirection, `awk`, `cp`, `cat`, `wc`, arithmetic, and `test` in PDF/HTML capture and assembly | Pair only optional-tool discovery (`command -v` / `Get-Command`). Move temporary-directory creation, subprocess execution, metadata stripping, byte assembly, checksum, verification, and cleanup behind a package capture operation or shared helpers. Temporary paths must come from the platform temporary-directory API. | Independent of V1 and the tag resolver. |
| `cp-skill-revise-autoreason` | POSIX `pwd`/`basename`/`date`, command substitution, variables, `mkdir`, `cp`, `printf`, redirection, and repeated blind-packet copies; later `git mv` | Replace run setup, path construction, copying, packet materialization, result writing, cleanup, and restoration with runtime-native or package operations. Resolve concrete paths before actor dispatch instead of sending shell-variable placeholders. The final `git mv` remains a shell-neutral process call. | Independent of V1 and the tag resolver. |
| `cp-skill-write-multistage` | Direct `commonplace-validate <path>`; abstract runtime file/workshop operations; exact snapshot-hash check on the conditional source route | Validation is already shell-neutral. Keep workshop orchestration runtime-native and use the shared snapshot verification operation for the source route. No paired shell blocks are needed. | No direct V1 dependency. Its conditional grounding path inherits `cp-skill-ground` and ingest portability. |
| `cp-skill-ground` | No literal shell program; exact-byte checksum, byte-preserving Quotes splice, one-write mutation, restoration, and direct validation | Validation is shell-neutral. Expose or reuse package/runtime operations for checksum, byte-preserving splice, and verified restore so an executor does not improvise platform commands for the load-bearing preservation contract. | A URL without an ingest inherits ingest and snapshot portability. No direct V1 or tag-resolver dependency. |

## Cross-cutting conclusions

### The user-level tool model removes the old activation problem

No promoted procedure should look for a project `.venv` to find Commonplace.
Only the health skill inspects `.venv` and `.envrc`, and it does so to identify
legacy residue or a project-owned environment. The operative command probe is
bare-name resolution plus ownership relative to `uv tool dir --bin`, followed
by a full restart test in the failing launch class.

### Pair only preflight, not workflow semantics

The required paired surface is small:

- health: layout, projection, uv ownership, and legacy-residue inspection;
- snapshot-web: discovery of optional capture executables.

Everything else either already has stable argv semantics or performs shared
file, checksum, capture, or orchestration behavior that should have one
implementation. Large paired Bash/PowerShell workflow blocks would duplicate
failure handling and byte-preservation rules.

### Two upstream packets own two exact removals

- V1 removes the complete Bash program from `cp-skill-validate`; a PowerShell
  translation would preserve the current incomplete `all` semantics.
- The tag resolver removes connect's `xargs -r` pipeline; a PowerShell pipeline
  would create a second tag membership implementation and still need an
  independently tested empty-set guard.

Direct validation of one path in write, ingest, multistage write, and ground
does not wait for V1. Only full-product `all` semantics do.

### Byte-level work is a shared portability surface

Snapshot SHA-256 verification appears in write, ingest, multistage write, and
ground. Snapshot-web creates and hashes the bytes; ingest and ground also
require exact copy, splice, restoration, and post-write verification. These
procedures should reuse one byte-oriented package layer rather than select
`sha256sum`, `cp`, or PowerShell equivalents independently. Existing internal
snapshot hashing can be the starting point, but this audit does not select a
new public command or implement one.

### `allowed-tools` remains an unresolved execution-interface contract

Every currently selected skill includes `Bash` in `allowed-tools`; none names
PowerShell. Static source inspection cannot establish whether each consuming
runtime treats `Bash` as a generic process tool, ignores the field, or denies a
native PowerShell interface. Do not count this declaration as either Windows
support or a demonstrated failure. E1 needs a documented projection/runtime
rule: normalize the capability, generate channel-specific allowlists, or prove
that the field is non-binding on the native-Windows consumer. The
manifest-derived static audit should flag a new selected skill until its
execution-interface declaration has a disposition.

## Static and runtime closure checks

The eventual static check should derive the selected set from
`MANIFEST.promoted_skills` and require exact set equality with its audit
records. For every selected source and required linked execution reference, it
should flag at least:

- unpaired Bash conditionals, loops, pipelines, redirections, substitutions,
  environment assignments, and glob expansion;
- `xargs`, `mktemp`, `awk`, `sed`, `wc`, `cat`, and `cp` in load-bearing command
  positions;
- hardcoded `/tmp`, `.venv/bin`, `.venv\\Scripts`, or path separators when
  they are operative rather than historical signatures;
- a Bash-only execution-interface or `allowed-tools` declaration without a
  recorded platform disposition;
- selected skills missing from the audit and stale audit rows no longer in the
  manifest.

Static coverage does not establish runtime behavior. E1 still needs a real
native-Windows PowerShell run, recorded as a new evidence report, covering the
health preflight, arbitrary-path validation, `validate all`, connect's empty-tag
path, and snapshot temporary-file handling after their owning changes land.
Linux and Windows CI should separately exercise user-level uv-tool install,
pristine init, the same bare-name commands, and the focused promoted-skill
paths. No native-Windows result was collected by this audit.
