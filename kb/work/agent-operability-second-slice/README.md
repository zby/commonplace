# Agent operability — second improvement slice

## Commission

On 2026-08-31, the operator asked for another workshop to continue the
improvements identified by the retained
[agent operability audit](../../reports/retained/agent-operability-audit-2026-08-31.md).
This workshop owns the next bounded implementation round after the
[first-slice result](../../reports/retained/agent-operability-first-slice-20260831/README.md).

## Goal

Make the relationship between an installed Commonplace project's copied
framework surfaces and the active Commonplace command inspectable and safe to
change. A later agent should be able to distinguish a current project, an
intentional local customization, an upstream update, and an incompatible skew
without inferring provenance from file contents or rerunning initialization.

The target round is:

1. record a project-source baseline with enough identity to compare installed
   framework inputs;
2. report useful skew categories through the compact status surface;
3. generate an inspectable three-way upgrade plan without mutating the project;
   and
4. decide from the worked plan whether apply and receipt belong in this round
   or require the next workshop.

The exact manifest format and command shape are deliberately left to execution
evidence. They must fit the existing packaging and scaffold authorities rather
than create a second authored inventory.

## Fixed constraints

- Preserve authored project customizations. No upgrade operation may silently
  overwrite a differing file.
- Keep `commonplace-status` read-only and compact. Detailed evidence belongs
  behind drill-down or structured output.
- Keep review-system state behind `commonplace-status --review`. The review
  system is not regularly operated yet, and stale review pairs remain normal
  state for now. Revisit that default only under the TODO already retained in
  the implementation.
- Use the live scaffold manifest and packaged inputs as authorities. A recorded
  project baseline is evidence about what was installed, not another scaffold
  definition.
- Do not generalize a universal operation, receipt, or lifecycle framework from
  this one path. Extract reusable machinery only after a second concrete
  consumer appears.
- Do not make `commonplace-init` the upgrade command.

## Evaluation boundary

Exercise at least these project cases against packaged or fixture-controlled
inputs:

| Case | Required distinction |
|---|---|
| Installed inputs still match their recorded baseline | current |
| A project file changed while its upstream input did not | intentionally customized |
| An upstream input changed while the project retained its baseline | upstream update available |
| The project and upstream changed the same input incompatibly | conflict or incompatible skew |
| The command cannot read the recorded schema/version | incompatible skew with a recovery route |

The evaluation covers copied framework library artifacts, scaffold-owned
files, and projected skills. It does not claim to version user-authored notes,
instructions, or reference content.

## Closure

Close this workshop when:

- the committed scope in [plan.md](./plan.md) is implemented or explicitly
  rejected from worked evidence;
- the cases above have deterministic tests and a recorded before/after result;
- operator documentation states the authority, inspection, plan, and recovery
  paths;
- any shipped architectural decision has an ADR and current reference docs;
- deferred audit recommendations are named with their dependency or trigger,
  not silently absorbed into this round; and
- durable results are extracted to the appropriate reference, ADR, or retained
  report surface, after which this directory and its active-work entry are
  deleted.

## Working files

- [plan.md](./plan.md) — intent-framed mission order, rolling-wave execution
  stages, delegated decision rights, acceptance evidence, and return conditions
- [baseline.md](./baseline.md) — current implementation map, unknowns, and
  measurement template

## Related work

- [Instruction generation](../../reference/instruction-generation.md) — the
  current scaffold-copy and preservation behavior
- [Commonplace architecture](../../reference/architecture.md) — the package,
  project, and command boundaries this work must preserve
- [Lifecycle-management workshop](../lifecycle-management/README.md) — owner of
  broader artifact retirement semantics, not a dependency to duplicate here
- [Agent-runtime design workshop](../agent-runtime-design/README.md) — owner of
  runtime approval and suspension concerns beyond this CLI path
