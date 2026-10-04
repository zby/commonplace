# Analyst acceptance check: implementation result

Commission: [implementation plan](./analyst-acceptance-check-plan.md).
Execution began on 2026-10-04. No analysis run is commissioned.

## Change packet

- Authoritative declaration: plan; shared job validator factory; analysis source contract; [ADR 105](../../../reference/adr/105-let-analysts-run-their-acceptance-check-before-submission.md).
- Scope: every analysis job uses the same validator through acceptance and the new read-only command. Quotation normalization and uniqueness remain unchanged.
- Consumers: run-context resolvers, shared citation parser, structural and frozen-source validators; command entry points; worker rules and job instructions; source contract; command reference and ADR 094; tests and fixtures. Search inventory and byte baseline: [baseline](./analyst-acceptance-check-baseline.json). No other live quotation-helper consumer was found.
- Schemas: citation shape is parsed in code, not a schema constant. Type assertions are supplied through existing type validation.
- Emitters: remove the quotation command; the new check emits advice only. No migration scripts or frozen member rewrites.
- Byte pins: retained sets, snapshots and historical fixtures are read-only; no re-pinning.
- Projections and generated forms: canonical instructions feed existing skill projections and installed library. Entry points require editable metadata refresh. No generated index edit.
- Fresh/existing installs: fresh init, repeated init, pointer checks and old-citation validation passed in a temporary project; no init in this checkout.
- Diagnostic promises: parity, independent failures, rule/location/repair messages, candidate uniqueness and state preservation tests passed.
- Identity conventions: job names identify run-context validators; source paths identify frozen blobs. No new artifact identity or relocation.
- Shared exclusions: citation parser excludes fenced examples; quotation bodies stay excluded from record and link scans.
- Historical witnesses: old completed citations stay accepted; frozen results and archived proposals keep their bytes. ADR 094 carries an amendment notice.

## Implementation choices and verification

Implemented all eight parts of the supported route. The command is installed
as `commonplace-analysis-check <run-state> <job> [draft]`.

- **Command and validator selection:** read the recorded workflow definition
  and its parameters, then use existing job constructors in a mode that builds
  only their job value. It neither replays the definition nor creates a worker
  workspace. The command is outside the engine's mutation APIs. Checks remain
  functions of a path and supplied context.
- **Rounds:** a reconciliation round can follow blockers without a new memory
  report. Its supplied invocation identifies the actual memory report; the
  check reads only the invocation header. Record verification uses its supplied
  set-check file for the structural failures acceptance expects it to report.
  Memory corrections, profile corrections and synthesis corrections retain
  their existing validators and contexts.
- **Draft and statuses:** the optional draft defaults to the assigned output.
  Exit 0 means a mechanical pass; 1 means refusals; 2 means an input or command
  error prevented checking. Text output preserves every validator's detail and
  adds a stable rule name, output location and repair. Determined identity,
  source and enum values are stated. Failed source lookups request rereading
  and reconsideration of the supporting claim, without proposing replacement
  text.
- **Independent failures:** member structure, reference resolution, identity,
  declaration ownership and quotation matching accumulate instead of using
  the first nonempty result. Reconciliation, verification, profile and synthesis
  do the same. Parsing or unavailable inputs still prevent dependent checks.
- **Capture attribution:** use the registered capture path without a checksum
  in the attribution. The resolver verifies the frozen checksum and checks the
  path; an explicitly supplied checksum must agree. Git paths use the run's
  frozen commit, never modified worktree text. Existing URLs and complete
  attributions retain their identity checks.
- **Ambiguity:** occurrence extraction never expands the passage. Diagnostic
  context is separate. Each proposed range is verified against the unchanged
  passage; same-line repeats receive context and an instruction to lengthen,
  with no unusable attribution. Overlapping ranges do not duplicate candidates;
  the existing limit remains one shared constant.
- **Logging:** one JSONL line per successful command invocation in
  `jobs/<job>/scratch/acceptance-checks.jsonl`, containing time, job, draft,
  refusals by rule and quotation totals. A pass also gets a line. Totals of
  quotations written come from the accepted member; local failures are counted
  per check run. Neither caller edits output text.
- **Removal and input:** the quotation CLI, its entry point, generation functions
  and command-specific tests were removed. Occurrence matching remains in the
  shared library. Every job now requests the acceptance check; the separate
  local-validation steps and old quotation route are gone. The user-level
  editable installation was refreshed as required by INSTALL.md.

## Measurements and evidence

The [ambiguity measurement](./analyst-acceptance-check-ambiguity.json) confirmed
39 quotations: 38 unique, one ambiguous, none missing or unavailable. The
ambiguous passage has two occurrences on separate lines and can use a checked
range. Neither retained set was edited.

The [byte measurement and rescan](./analyst-acceptance-check-measurements.json)
records 51,326 affected instruction bytes before and 51,155 after: **171 fewer**.
The changed inputs of each initial job packet are between 150 and 340 bytes
smaller, including the new invocation parameter. The source contract and shared
worker rules shrink; each job's short submission instruction fits within that
saving. Correction-round names add only a few bytes and remain below baseline.
The final live-consumer scan found zero references to the old command or its
generation APIs in runtime code, tests, current analysis instructions and the
command reference. The general validator's own CLI tests retain its full mode.

The [producer inventory](./analyst-acceptance-check-messages.json) records the
message review. Job-level advice covers existing schema/type findings without
maintaining another validation implementation. Expected identity/checksum/path
values and controlled ledger values now appear where they are determined.

## Verification

- Final full suite: **999 passed** on the completed code.
- Ruff passed. Targeted Commonplace validation reported zero failures and
  zero warnings for all 11 job files, the source contract, command reference,
  ADR 094 and ADR 105. Directory-scoped orphan notices remain notices.
- Scripted job tests compare the real acceptance callback with the command on
  both invalid and valid bytes for every scheduled job kind, including returned
  memory and blocker-driven reconciliation. File contents and modification
  times stay unchanged. Only the CLI's scratch log changes.
- A draft with unresolved references, a wrong run identity and an absent quote
  reports all three. Messages state rule, location and repair; the identity
  message includes the run's value.
- Quotation fixtures cover path-only uniqueness, altered spacing, altered
  non-whitespace characters, missing passages, several ambiguous blocks,
  checked and invalid ranges, same-line repeats, the occurrence limit,
  overlapping ranges, capture URL/path/hash checks, completed legacy citations,
  ordinary blockquotes and fenced examples. Publication still reads frozen Git
  blobs even when the source worktree has different text.
- Temporary-project fresh and repeated init passed; installed pointers checked
  cleanly; the legacy complete citation remained byte-identical and validated.
  Installed command help resolves by bare name, and the old executable is gone.

## Deviations and remaining work

No commissioned feature was deferred and no run-loop behavior was changed.
The first full suite found four fixture expectations treating the new scalar
`job` parameter as a path. Those expectations were updated; no acceptance rule
was weakened. The command retains plain validator findings with a shared advice
wrapper; broad integration with `commonplace-validate` remains the separately
recorded TODO.

An analysis run and an outcome assessment remain outside this commission.
Fixtures do not show that analysts use the check or make fewer failed calls.
ADR 105 carries both required TODOs and the revisit observations and counts.

