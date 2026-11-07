# Consumer and verification packet

## Declaration and scope

[ADR 125](../../reference/adr/125-analysis-commands-own-preparation-and-bounded-queues.md)
adopts command-owned preparation and bounded queues. CLI help and the Python
APIs own exact arguments and result fields. The coordinator owns target bindings,
not worker liveness; the pinned workflow and Workjig retain that authority.
Existing runs are not migrated or rebound.

## Consumer inventory

Searches over source, tests, active method/instructions, reference, root doctrine,
installation docs and build hook, excluding frozen retained evidence:

| Pattern | Matching files after edit | Consumer / disposition |
| --- | ---: | --- |
| `commonplace-analysis prepare` | 3 | CLI help, command reference, historical ADR; low-level command retained |
| `analyse-agentic-system` | 34 | method/roles, package and composition tests, instructions, references; canonical name unchanged |
| `isolated-run-setup` | 3 | root doctrine, skill anchor, command reference; anchor retained with command-owned setup |
| `advisory-trace-audit` | 1 | command-reference link; skill anchor retained |
| `shell loop over prepare` | 1 | ADR 118 historical decision; explicitly marked amended by ADR 125 |
| `promoted_skills` | 8 | scaffold, library/init code and installation tests; analysis remains repo-local, not promoted |

- Resolvers/validators, schemas, member types and templates: unchanged. Analysis
  output grammar and role packet inputs are unchanged.
- Emitters: analysis CLI and coordinator emit controller/execution JSON. Worktree
  allocation owns the journal. Headless inspection adds unsettled launch IDs;
  workflow stop events add structured uncertainty. Existing keys remain.
- Skills/procedures: canonical analysis skill now invokes the high-level command;
  recovery routes remain in the command reference. Method-maintenance doctrine
  and the root command-environment exception remain valid.
- References/ADRs: command reference updated; ADR 118 marked amended; ADR 125
  records the execution boundary and origin-policy choice.
- Tests: complete prepared command, frozen offline installation, headless and
  workflow consumers, allocation crash, scheduler and process recovery tests.
- Published views: no path relocation, redirect or index change. KB validation
  and docs tests cover link/contract surfaces.

The post-implementation rescan returned the same counts. The remaining
shell-loop batch rule is the explicitly amended historical ADR, not an active
second skill procedure. Low-level command documentation remains intentional.

## Pins, generated forms and installs

No retained artifact or byte pin is rewritten. New runs commit fixture methods
before preparation; existing opening method/profile bindings stay unchanged.
No migration script, schema copy or identity rename is needed.

Checkout skill projections are symlinks to the canonical skill, so no generated
copy is edited. `scaffold_manifest.py` does not promote this analysis skill;
`test_library_build.py` explicitly checks that it is not shipped as a promoted
skill. Installed generic stubs and control-plane templates therefore need no
change. The command entry point already ships; no dependency or packaging change
is needed. Fresh-install and repeat-init probes plus installation tests cover
unchanged generic pointer behavior. Source clones receive the canonical skill
through their existing symlinks.

## Diagnostic promises and drift guards

- Invalid source/options: before state/preparation, with no network intake probes.
- Startup mismatch/default-branch lag: preparation API refuses, without selecting
  another commit. ADR 118 deliberately omitted origin checks; this commission
  adopts the stricter intake policy rather than claiming a worker inherits origin
  context.
- Allocation: journal before effect; a fresh caller recovers the same binding;
  even a legacy allocator cannot steal an unmaterialized reservation.
- Unknown effects/live child leases/unsettled workers/interrupted audits: pause
  pending claims, expose operator attention, never acknowledge automatically.
- Four slots: six independent barrier-controlled commands prove slot reuse and
  cross-target binding isolation. Real workflow fixtures separately prove harness
  delivery and acceptance.
- SIGTERM: drain owned children and retain pending targets; SIGKILL: inherited
  leases exclude another claimant until orphan completion, then reconcile exact
  allocations without replacement.

The command catalogue's entry-point parity, installation projection tests,
instruction composition tests and real pinned-child fixtures are the drift
guards. There is no new artifact-membership predicate or exclusion set. UUID
allocation keys are local orchestration identities, not publication names.
No relocation changes gated or pinned bytes. Historical method copies and
retained evidence are deliberately untouched.

## Acceptance probes

Recorded results belong in [execution](./execution.md). The temporary fresh and
repeat `commonplace-init` probes exercise generic installed pointers only; they
do not claim an analysis skill was promoted. Deterministic execution uses a
scripted executable with fake model provenance and local Git acquisition. One
complete route also invokes the production installer against the committed
lockfile with networking disabled; the smaller command tests substitute only
installation cost, not method, binding, validation or publication checks.
