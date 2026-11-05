# E1 plan — Make native Windows support operative

## State — 2026-11-03

Open for **procedure portability**, not installation acceptance. The
[current rebaseline](./rebaseline-2026-11-03.md) selects 11 promoted skills plus
one router from `src/commonplace/scaffold_manifest.py`. It supersedes the
[August audit](./e1-promoted-skill-rebaseline-2026-08-27.md) as current triage;
the old audit remains a dated observation, not the current manifest.

Windows package installation, supported software CI, installed-project command
resolution and bounded native/index skill routing passed. See the
[retained delivery record](../../reports/retained/framework-delivery-acceptance-2026-11-03.md)
and [release CI](https://github.com/zby/commonplace/actions/runs/41342248088).
The delivery workshop is closed. Its release/platform/runtime deferrals and
Windows read-rule defect belong to INSTALL.md, not a duplicate queue here.
These passes do not establish every promoted procedure's portability.

## Resolution selected

Retain native Windows support. Prefer shell-neutral package commands or
runtime-native operations for load-bearing behavior. Pair literal preflight
commands where diagnosis must work before package commands can be trusted.
Do not duplicate entire workflows in Bash and PowerShell.

Do not implement from the August inventory without checking current consumers.
The scope here is the promoted set plus its required references; the parent
workshop owns non-promoted instructions, the control plane and tool policy.

## Work and disposition

The numbers retain the earlier E1 item identities.

1. **Static rebaseline — refreshed.** The November source triage covers all
   12 selected skills and identifies relocated instruction trees. It is not
   exhaustive per-locus coverage or a Windows test. Required references and
   byte-sensitive operations still need worked cases. Any eventual inventory
   check must derive set equality from the manifest rather than a fixed count.
2. **Native-Windows procedure verification — open.** After each selected change,
   exercise it under the relevant normal-policy PowerShell runtime. Installation
   and a simple validation invocation are not substitutes for health preflight,
   aggregate validation, empty-tag search or snapshot temporary-file handling.
3. **Aggregate validation — design reconciliation required.** The older plan
   proposed a package-owned `commonplace-validate all`. Current
   `resolve_validation_target()` explicitly rejects `all`, `kb` and `kb/`, and
   `tests/commonplace/validation/test_validate_notes.py` tests that boundary.
   Meanwhile the skill implements `all` with a POSIX collection loop. Decide
   how to provide portable requested aggregate validation without silently
   overriding the current narrow-scope contract. If a package target is adopted,
   use contract-based collection discovery, honor ignore markers, continue after
   failures and report an aggregate result. Preserve draft-role, today/recent,
   landings, redirects and receipt behavior. No production change is authorized
   by this rebaseline.
4. **Connect's tag/path selection — open.** The current `rg -l | xargs -r rg`
   pipeline still requires the zero-match guard to avoid widening to the whole
   repository. Prefer a package command or shared Python helper over permanent
   per-runtime Grep/Read choreography. The old reference to a future T1 resolver
   is not a verified implementation dependency; establish the current resolver
   and consumers before choosing the change. Require a no-match regression case.
5. **Health preflight — partly implemented, partly open.** Steps 1–2 retain
   POSIX layout/presence tests. Step 3 uses runtime-native delegation diagnosis.
   Step 4 already has POSIX/PowerShell ownership checks and recognizes supported
   Windows shims. Step 5 compares legacy `.envrc` without exposing its contents,
   in both shell forms; complete Windows behavior remains unverified. Step 6
   uses plain command invocations and is not itself a POSIX program. Pair the
   actual shell-dependent checks and retain diagnose-only behavior. Also update
   the denial interpretation: an `ok` init check cannot prove that the generated
   Windows Read rule grants access. Leave the product rule fix under INSTALL.md's
   operator-approved trigger.
6. **Byte-sensitive and workflow operations — open, narrowed by current text.**
   Ingest now explicitly permits native byte-copy and requires hash verification;
   ground states digest checks without a shell recipe. Neither is proof of
   Windows runtime success. Multistage promotion requires exact-byte drift checks
   and rollback in a supporting reference. Snapshot-web still has POSIX capture,
   temporary-directory and concatenation blocks; AutoReason has shell filesystem
   preparation even though delegation is harness-native. Choose shared operations
   from actual consumers and failure cases, not a blanket checksum-helper plan.
   All 12 skills include `Bash` in allowed-tools; its enforcement needs a
   runtime-specific disposition, not inference from successful command execution.
7. **CI — package coverage done; procedure guard open.** Current CI tests the
   supported suite on Ubuntu and Windows, builds/installs a wheel, checks every
   entry point and initializes/checks/validates a temporary project. Analysis
   tests remain skipped on Windows. Focused procedure fixtures and a narrow
   incompatible-idiom inventory/check are not established by that CI. Avoid
   classifying every Bash-labelled single-command fence as incompatible.
8. **Fresh installed-project delivery — bounded pass.** The retained Windows
   checks cover stubs, arguments, library pointers and command resolution.
   Do not rerun those merely to keep this item open. New procedure checks still
   need installed-project fixtures where source-checkout access would hide a
   dependency; the newest source-rooted Codex chat is not such a fixture.

## Next bounded step

The operator approved the sequence recorded in the
[parent plan](./README.md#agreed-next-work): first reconcile the breadth probe
with supported shims and effective permission evidence, then take health-check
layout/presence checks as the first E1 slice. The probe revision is a prerequisite
for a new comparable breadth report, not proof of health-check acceptance.

**Health slice scope.** Pair the shell-dependent layout/presence tests in
`cp-skill-health-check` Steps 1–2 with PowerShell forms. Correct the denial
interpretation so matching init outputs or an `ok` init check do not establish
effective library-read permission. Preserve diagnose-only behavior and existing
Step 4 shim recognition. Do not rewrite Step 3's runtime-native diagnosis or
Step 6's plain argv as if they were POSIX programs. Do not implement the Windows
read-rule product fix here; INSTALL.md retains that trigger.

**Before editing.** Trace the affected consumer instructions and identify
Linux/Windows fixtures for the layout branches being changed. Include missing
and present paths, paths requiring quoting, and permission-denial evidence where
the runtime exposes it. Use an initialized-project fixture where source-checkout
access would hide a dependency. Define expected observations before the run;
do not repair an environment to obtain them.

**Acceptance.** Validate changed Markdown and retain results for the selected
checks on Linux and normal-policy native Windows PowerShell. Report unavailable
runtime cases as pending, not passed. The slice must preserve the distinction
between file presence, matching generated files and effective access. Package CI
or a simple validation invocation alone cannot satisfy this acceptance.

**Stop and replan** if the slice needs broader workflow changes, a new command
interface or permission repair. After retaining its checks and remaining gaps,
choose the next slice. Connect's zero-match selection is the next candidate;
establish consumers and package/helper ownership and require a no-match
regression case before implementation. Aggregate validation still needs the
explicit contract decision in item 3. Complete the wider required-reference
inventory before deciding whether channel compilation is unnecessary.

## Completion

Every executable promoted-skill step and required reference is shell-neutral,
runtime-native or explicitly paired, with applicable Linux/Windows tests passing.
Native-Windows evidence must cover health preflight, ordinary and aggregate
validation, connect's empty-tag behavior and snapshot temporary-file handling,
plus a disposition for every remaining promoted step and its runtime metadata.
The parent execution-channel workshop promotes the durable results and owns
closure of E1. Missing runtime coverage remains an explicit gap, not a static
inspection pass.
