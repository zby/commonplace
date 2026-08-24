# Worked case: `commands.md`

Executed 2026-08-24. The second artifact taken through the full disposition.

## Result

**Keep the complete catalogue; remove the repeated manuals.** The command-name
inventory is a useful routing cache for a reader who knows a task but not its
command. Exact arguments belong to live `--help`, exact behavior belongs to the
executing source, and multi-command workflow belongs to the review and
operation instructions.

The executed edit reduced `commands.md` from 20,380 bytes and 296 lines to
5,704 bytes and 166 lines. All 22 published commands retain one heading and a
short purpose. Examples, option descriptions, result shapes, and
implementation detail were removed when help, source, or a stronger workflow
document already owned them.

## Consumption events

Three questions take three paths:

| Consumer event | Required answer | Path |
|---|---|---|
| A reader knows the task but not the command | approximate name and purpose, enough to choose the next lookup | complete `commands.md` catalogue |
| A reader knows the command and needs to invoke it | exact arguments and options | `commonplace-X --help` |
| A changer needs behavior, failure semantics, or data flow | exact implementation or cross-command workflow | `commonplace-source` plus source; linked instruction or architecture document for the workflow |

The first event is not served by command-local help: the reader must know the
name before invoking it. It also cannot rely on `pyproject.toml` in an installed
project, where the executing package is present but the source repository's
build metadata need not be.

## Discovery test

The published set contained 22 commands. Searching the root and installed
control-plane files, root README and install guide, all instructions, the
reference landing, and the review-system guide found no mention of six:

- `commonplace-ack-trivial-note-changes`
- `commonplace-promotion-candidates`
- `commonplace-resolve-criteria`
- `commonplace-review-job-list`
- `commonplace-store-healthcheck`
- `commonplace-verify-quotes`

Removing catalogue completeness would make those commands invisible to the
current task routes. A check that only rejects nonexistent mentioned commands
would not detect that loss. The exact set-parity test therefore stays: it
guards discovery rather than treating the prose as the CLI contract.

## Live-help failure found by the audit

Twenty commands already handled `--help` through `argparse`. Two did not:

- `commonplace-source --help` ignored the argument and printed the source path;
- `commonplace-promotion-candidates --help` ignored the argument, executed the
  report generator, and rewrote `kb/reports/promotion-candidates.md`.

The accidental report rewrite during this audit was reversed byte for byte.
Both commands now parse arguments before acting. A test invokes `--help` for
every published entry-point module in an empty directory and requires exit 0,
a usage line, and no filesystem change. The documented live-help path is now
an enforced command-wide contract rather than an assumption.

## Section dispositions

In the table, **help/source** means live help owns exact invocation and the
executing module owns exact behavior.

| Section | Stronger recovery or workflow home | Residue worth retaining | Disposition |
|---|---|---|---|
| `commonplace-init` | help/source; `architecture.md` | setup routing and the no-overwrite rerun distinction | keep heading, short purpose, architecture link |
| `commonplace-source` | help/source | route from installed commands to their exact package | keep heading and purpose |
| `commonplace-validate` | help/source; `validation-contract.md`; validate skill | distinguish deterministic validation and route its check domains | keep heading, short purpose, contract link |
| `commonplace-verify-quotes` | help/source | command discovery and corpus-audit purpose | keep heading and purpose |
| `commonplace-guard-full-pass-report` | help/source; full-improvement instruction | route to the guarded-transition workflow | keep heading, purpose, instruction link |
| `commonplace-relocate-note` | help/source | dry-run safety distinction | keep heading and one sentence |
| `commonplace-relocate-directory` | help/source | dry-run safety and optional redirect distinction | keep heading and one sentence |
| `commonplace-promotion-candidates` | help/source | otherwise-missing discovery and report destination | keep heading and purpose; repair help |
| `commonplace-github-snapshot` | help/source; snapshot skill | distinguish the GitHub adapter | keep heading and purpose |
| `commonplace-x-snapshot` | help/source; snapshot skill | distinguish the X/thread/article adapter | keep heading and purpose |
| `commonplace-create-review-jobs` | help/source; review guide and batch instruction | place it after selection in the pipeline | keep heading and purpose |
| `commonplace-review-job-list` | help/source | otherwise-missing discovery | keep heading and purpose |
| `commonplace-finalize-review-job` | help/source; review guide and architecture | all-or-nothing finalization and provenance role | keep heading and purpose |
| `commonplace-freshness-status` | help/source; freshness architecture and schemas | global registered-target role and schema route | keep heading, purpose, schema link |
| `commonplace-freshness-ack` | help/source; freshness schemas | distinguish acknowledgement from initial acceptance | keep heading and purpose |
| `commonplace-freshness-retire` | help/source; freshness schemas; retirement instruction | deleted-input remedy | keep heading and purpose |
| `commonplace-store-healthcheck` | help/source | otherwise-missing diagnostic discovery | keep heading and purpose |
| `commonplace-ack-review` | help/source; review guide | preservation is not endorsement or report resolution | keep heading and semantic warning |
| `commonplace-ack-trivial-note-changes` | help/source | explicit human-authorization boundary | keep heading and semantic warning |
| `commonplace-resolve-criteria` | help/source | otherwise-missing discovery | keep heading and purpose |
| `commonplace-review-target-selector` | help/source; review guide and batch instruction | selection's place before job creation | keep heading and purpose |
| `commonplace-warn-selector` | help/source; fix-system instruction | route from review state into fixing | keep heading, purpose, instruction link |

Three non-command regions also survived in reduced form:

| Region | Reason |
|---|---|
| Installation and authority | tells the reader where commands come from and which live surface answers the next question |
| Generated indexes, no command | records an operational absence and retired names that a command inventory cannot derive from current entry points |
| Review composition and model flags | relates several commands and prevents the partition-versus-concrete-model category error |

## Maintenance form

The catalogue is a checked routing cache:

- package metadata and the heading set must remain equal;
- every published entry-point module must provide side-effect-free `--help`;
- purpose prose is deliberately approximate and partial, so exactness routes
  onward rather than being trusted here.

Purpose text still requires judgment and can drift, but its required
reliability is only command selection. The exact live surfaces remain the
fallback. Generating a purpose catalogue was not justified by this 22-command
case.

## Next

`freshness-schemas.md` remains the strongest opposite case: exact serialized
shapes may be removable, while the semantic distinction between stale inputs
and a false target may survive.
