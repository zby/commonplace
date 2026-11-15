# Sketch: the unified review command

`commonplace-operation` is a provisional name, not an implemented command. This sketch specifies a possible interface for the [execution design](./execution-design.md), within the [review-only scope](./README.md). It does not register connect or any other candidate family before the form decision.

## Ordinary execution

```bash
commonplace-operation list
commonplace-operation run gates NOTE --criteria prose
commonplace-operation run gates DIRECTORY --all-gates --profile opus
commonplace-operation run critique NOTE
commonplace-operation run connect NOTE
commonplace-operation status NOTE --operation connect
commonplace-operation show RUN
commonplace-operation resume RUN
```

| Surface | Proposed behavior |
|---|---|
| `list` | Show admitted operations and their instruction, input/output, profile and freshness contracts. Use a small explicit registry, not automatic registration of every instruction. |
| `run` | Start an invocation. Apply a supported freshness policy and report skips explicitly. Preserve `--force`, profile, grouping, worker-count and timeout controls where applicable. |
| `status` | Show current results and freshness under the selected operation's policy. Use `unassessed` when no policy is defined; this is not `fresh`. |
| `show` | Inspect a run's provenance, captured inputs, attempts, outputs and completion. |
| `resume` | Continue the same invocation using existing Workjig recovery and answer replay. Do not count continuation as an independent trial. |

`gates` keeps criterion selection and applicability. `--all-gates` does not expand to reports merely because they share the runner. Batch support for another operation must declare independent target execution and avoid output collisions; a directory argument alone does not establish that support.

## Controlled execution

```bash
commonplace-operation fixture create --from RUN
commonplace-operation run connect --fixture FIXTURE
commonplace-operation run connect --fixture FIXTURE
```

`fixture create` reports which inputs were recovered, missing or explicitly substituted under the execution design. The interface for supplying missing content and selecting executable/configuration versions remains to be decided from the first supported case; do not introduce a general environment manager.

With `--fixture`, the fixture supplies target paths, operation and execution configuration. The named operation must match. Each invocation makes an independent trial; `resume` continues one. Initially reject configuration overrides so a deliberate treatment change gets a separately identified fixture rather than masquerading as a replicate. Automated trial scheduling and statistical summaries are deferred.

## Transition from commonplace-review

The current command also owns `full-pass`, `revise`, approval, packet and decision interfaces outside this subset. Keep those consumers working; replacing the review surface does not authorize removing them.

Inventory review callers before choosing a cutover. Prefer migrating them to one implementation, not maintaining two execution paths. If an old review entry point is needed temporarily, name its consumer and removal condition. Existing runs need an explicit continuation or restart disposition; do not promise compatibility with changed Workjig record formats.

The command name does not require moving the state tree. Reuse current layouts unless an actual result consumer requires a change. Complete retirement of `commonplace-review` waits for disposition of its non-review interfaces and is not this subset's completion condition.
