# Sketch: extend the existing review command

Design sketch for the [first-slice contract](./execution-contract.md). Its additions are now implemented; `commonplace-review --help` and the [command reference](../../reference/commands.md#commonplace-review) own the live interface. [Implementation status](./implementation.md) records verification and cutover. Keep `commonplace-review`: no inspected consumer needs the earlier provisional `commonplace-operation` name.

## Ordinary execution — existing surface

```bash
commonplace-review run gates NOTE --criteria prose/proportion-mismatch
commonplace-review run gates NOTE --criteria critique
commonplace-review run gates DIRECTORY --all-gates --profile opus
commonplace-review status NOTE --criteria critique --json
commonplace-review run gates NOTE --criteria critique --resume RUN
```

Preserve current selection, applicability, `--force`, profile, grouping, worker-count and timeout controls. `--all-gates` does not acquire report operations merely because they share execution support. This workshop does not prescribe which atoms a caller selects together.

For new versioned standalone runs, `--resume` uses the recorded selection, captures and execution contract. Supplied arguments must match the recorded request; reject a mismatch rather than silently redefine that execution. A new run is the route for changed inputs. Existing full-pass/revise continuation remains their own workflow contract, not this standalone rule.

## Draft selection

```bash
commonplace-review run gates NOTE --criterion-file kb/work/example/wording.md
```

Initially accept one repository-local draft review-gate file, mutually exclusive with `--criteria` and `--all-gates`. Validate and capture it without adding it to the catalog. Retain evidence without publishing over catalog current results. Repetition needs no alternate criterion id. A draft needing a broader reading scope than the supported operation must fail clearly; this option is not permission to bypass reading boundaries.

## Inspection

```bash
commonplace-review show RUN
commonplace-review show RUN --observation OBSERVATION --json
```

Show captures, attempt history, validation state, completed results and configuration gaps. JSON exposes the outcome and structured findings, including levels where the result form defines them, plus exact target and raw-output citations. It never launches a worker or validates judgment quality.

Existing `status` keeps the current-result view for the supported format. An old-format file in active state produces an actionable error requiring explicit archival or regeneration; no fallback parser interprets it. Historical observations do not inflate current-result summaries.

## Fixtures

```bash
commonplace-review fixture create --from RUN --observation OBSERVATION --substitute-current-executor
commonplace-review run gates --fixture FIXTURE
commonplace-review run gates --fixture FIXTURE
commonplace-review run gates --fixture FIXTURE --resume TRIAL_RUN
```

Creation is a no-model-call preparation step. It selects one atom and target, retains a content baseline and reports missing recovery inputs. Store fixtures under `kb/reports/state/review/fixtures/`; give each trial its own run and working tree. No second state repository is required.

The fixture supplies target, criterion, profile and execution configuration. Reject positional targets, criterion selectors and configuration overrides in fixture mode. A deliberate change requires a separately identified fixture baseline, with substitutions recorded. Missing-input repairs must explicitly name supplied files and roles; never discover operational dependencies recursively. The manifest is versioned execution data, not a new general environment-description language.

Every invocation without `--resume` makes a fresh independent trial, bypassing current-result freshness and cross-trial answer replay. Resume continues one trial. The first slice uses one atom/target, pair grouping and one worker. A source bundled observation therefore yields a documented change of grouping, not a claim of exact replay.

## Compatibility boundary

Keep `full-pass`, `revise`, approval, packet, retry, launch acknowledgment and decision interfaces, updating their result consumers together. Reuse Workjig and the existing state tree. The operator requires one supported format and implementation path: no legacy adapter, fallback parser, dual writer or automatic migration layer. Retain old evidence as files without preserving executable support for its format.

The operator selected archival and a fresh start at cutover. New runs use a versioned active namespace; cited old launch files can remain in place as historical evidence, outside active discovery. Archive old current results and pending views; carry no old answers or approvals into new runs. Refuse old-format resume. Settle active workers before cutover and record the inventory. See the [cutover decision](./execution-contract.md#5-freshness-and-legacy-state).
