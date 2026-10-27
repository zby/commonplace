# Registered shim harness and scripted validation — 2026-10-27

## Result

W3 through W7 passed with the workshop's registered temporary shim harness over the uv-managed test environment.

| Test | Result |
|---|---|
| W3 shim dispatch | pass; `commonplace-validate.cmd --help`, exit 0 |
| W4 initialized project one | pass; `commonplace-init.cmd --name project-one`, exit 0 |
| W5 initialized project two | pass; `commonplace-init.cmd --name project-two`, exit 0 |
| W6 validation sweep | pass; `types`, `notes`, `reference`, `instructions`, `agent-memory-systems`, `sources`, and `redirects` all exit 0 |
| W7 fresh process | pass; fresh PowerShell process resolves the shim and returns exit 0 |

No antivirus alert appeared during the run. The shim called the selected test-environment Python directly; no generated `commonplace-*.exe` entry point was invoked.

## Boundary

This is harness evidence, not production-shim evidence. The registered shim files are workshop fixtures and use an explicit Python path. W5 proves repeatable initialization from two project roots, but both projects use the same installed test environment; it does not yet prove version-sensitive dispatch between independent Commonplace installations. Antivirus acceptance remains an observation from this machine and policy only.

The `commonplace-init` output records the expected Windows note that generated `.envrc` is for Unix-like shells and that future Windows agent sessions need activation or another PATH handoff. That warning is part of the installation/channel behavior under review.
