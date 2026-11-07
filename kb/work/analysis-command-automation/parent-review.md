# Independent parent acceptance

## Decision

Accept implementation attempt 1 after local repairs. No substantial
rearchitecture, revert or second implementation commission was needed.
Implementation commit: `2b6db4a6badf6a4ff14b932f66f48fca85156703`.
The repair commit contains this record. No live pilot is authorized by acceptance.

## Review and repairs

The parent read the coordinator, allocation journal, pinned-child protocol,
leases, preparation changes, workflow inspection and affected command surface.
A fresh Sol worker independently reviewed the implementation read-only and
returned three concrete findings. All were locally repairable:

1. Repository intake accepted a locator and conflicting source identity, while
   code-owned acquisition selects the identity. Intake now requires agreement
   after normalization, before preparation or allocation. Regression cases
   cover a different repository and an alias used to evade duplicate detection.
2. Shared opening guard failures were classified as ordinary stops, so the
   queue could prepare every remaining target against the same invalid method.
   Opening and pinned-method guard refusals now record `OpeningFailed` and a
   command-failure classification that pauses new claims. Acquisition errors
   and analytical stops retain their existing classification. The lower-level
   `run` still exits 2 on a guard refusal. A real prepared-command regression
   pins invalid shared retained content and proves that the next target is not
   prepared and no fake model is called.
3. Preparation's Git/installer commands inherited the terminal process group.
   Group signals could terminate them despite the controller's drain policy.
   Preparation command and Git-probe subprocesses now start separate sessions
   only within a context owned by the controller's drain handler. A read-only
   follow-up caught the unconditional variant orphaning low-level callers'
   children; the final repair scopes isolation to controller preparation.
   Low-level group SIGINT/SIGTERM regressions prove cancellation reaches a
   descendant as well as the immediate command. Controller regressions send both group SIGINT and group SIGTERM while a
   temporary installer runs through production `run_command`; preparation
   finishes, and the next queued target remains unclaimed.

The command reference and ADR 125 record the clarified boundaries. The parent
updated the existing low-level guard-refusal test to assert the new stop type,
queue failure flag, unchanged exit 2, guard reason and absence of worker launches.
No validator, pinning rule, isolation assertion or workflow budget was weakened.

## Verification

Final parent run: **`uv run pytest -m ''`: 1437 passed, 2 skipped in 631.50 s**.
This is the complete suite, including relevant slow analysis/headless cases,
general tests, documentation, installation and shared consumers. All 44
automation cases passed. Targeted intake/opening/group-signal regressions also
passed independently, including low-level descendant cancellation:
16 passed, 28 deselected.

An initial parent full-suite run exceeded a 600-second tool limit and is not a
passing result. A later complete run exposed one outdated expected exception
name in the low-level guard-refusal test. After strengthening that assertion to
the new classification, that complete run passed (1435 passed, 2 skipped).
The final run above also includes the scoped signal-isolation repair and both
low-level descendant-cancellation regressions.

The independent reviewer confirmed that complete-command fixtures reach the
prepared executable, real Workjig frames and workflow/publication validators;
one fixture exercises the production frozen installer offline. Some scheduling
cases use scripted children or substitute the scheduler work function.
Allocation crash tests inject a failure into the allocator rather than killing
an end-to-end controller at every instruction boundary. These are coverage
limits, not evidence of exhaustive crash safety.

`uv run ruff check .` and `git diff --check` passed. KB validation of this
workshop, the command reference, ADR 125 and the shared workshop index passed
with zero warnings and failures.

## Remaining authority and limits

No live models/providers, campaign, analysis-publication integration or evidence
cleanup ran. Deterministic fixtures establish mechanics, not analytical quality
or provider behavior. POSIX local-filesystem lock semantics are required.
A live pilot still needs an explicit commission, a committed method choice,
provider capacity, storage/inode checks and worktree placement. Four analyses
with three concurrent role workers permit up to twelve role workers.

The workshop is retained for operator handoff and later archival; its adopted
command contract and design decisions are in the reference collection.
Unrelated dirty files and the shared workshop index remain unstaged.
