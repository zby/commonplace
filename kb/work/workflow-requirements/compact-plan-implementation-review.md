# Compact-plan implementation review

## Scope and outcome

The operator requested a review for bugs, inconsistencies, overengineering
and other issues in these commits:

- `c9a8b1f09`: compact-plan loader, code-job options and compact toy plan.
- `4baff3776`: toy frontmatter fix.
- `2730e7937`: synthesis citations to both verifications.
- `d17a53d4a`: compact analysis plan, fidelity tests and judgment test.
- `204ac66e8`: deletion of analysis structural wrapper handlers.
- `52f77aa8a`: cleanup.

The review found one blocking regression, three supported-plan edge cases
and a fidelity-test gap. The overall design is sound: it removes wrapper
duplication without turning scheduling into a configurable validation
framework. The integration regression should be fixed before the migration
is considered complete.

This is a snapshot review, not a current-state guarantee. File locations
and observations refer to the implementation through `52f77aa8a`. The
review changed no code. Suggested fixes below are recommendations, not
implementation authorization.

## 1. High: published compact-plan analyses cannot be integrated

**Location:** `src/commonplace/lib/agentic_analysis/worktree.py:108–110`.

The engine stores the expanded declaration and reports its digest through
`inspect()`. The integration guard still compares that digest with the raw
compact YAML file:

```python
fixed["sha256"] != sha256(shipped.read_bytes()).hexdigest()
```

Those hashes differ for the shipped analysis plan. A successfully published
analysis therefore fails with:

```text
ValueError: integration requires the fixed shipped analysis plan
```

A temporary reproduction used the shipped plan's expansion and mocked
inspection metadata carrying the digest the engine would produce. The
integration guard rejected it immediately.

**Suggested fix:** compare against the shipped plan's expansion, or retain
a separate raw-plan identity. Keep the artifact-type identity guard.

**Test gap:** integration tests supply an unexpanded declaration and its
raw-file digest. Add a test connecting a real compact plan's engine-produced
metadata to the integration guard.

## 2. Medium: derived apply jobs can omit their configured frozen source

**Location:** `src/commonplace/artifactrun/compact.py:343–360`.

`check_job()` and `standard_job()` add the configured frozen-source role as
a dependency when necessary. `apply_job()` does not. It sets the
`frozen-source` option but snapshots only the verifier's declared reads.

A plan declaring `frozen-source: boundary`, whose verifier reads its
subjects but not `boundary`, derives an apply job that fails while
constructing its candidate:

```text
TypeError: ... the frozen-source member boundary has no source field
```

The boundary can exist and contain a valid source; it is not an input of
that job. Independent review confirmed that expanding a compact toy plan
with a frozen-source role absent from the verifier's reads produces the
option without the corresponding input. The runtime failure follows from
the handler's missing-member check.

**Suggested fix:** derive the source dependency consistently, or reject the
declaration during expansion with an explicit requirement. Decide whether
application uses the source handed to the verifier or a live source input.

The shipped analysis avoids this case because its verifiers explicitly
read the boundary.

## 3. Medium: derived schema closure mishandles commonplace references

**Location:** `src/commonplace/artifactrun/compact.py:98–100`.

The closure walker treats every external `$ref` as file-relative. The
validator supports library-root references such as:

```yaml
$ref: commonplace:types/base.schema.yaml
```

The loader instead looks for a path resembling
`types/commonplace:types/base.schema.yaml` and silently skips the nonexistent
path. A temporary reproduction created an existing base schema and derived
a closure containing only the member type and member schema.

Closed validation fails because the required schema is not pinned. Changes
to that omitted dependency are not recorded as inputs either.

**Suggested fix:** match the validator's reference-resolution semantics,
preferably through a shared resolver rather than another independent
implementation. Add a closure test with a `commonplace:` reference.

## 4. Medium: optional partner disappearance can leave coverage stale

**Locations:** `src/commonplace/artifactrun/compact.py:332–334` and
`src/commonplace/artifactrun/run.py:268–272`.

Derived checks read cited partners optionally. If a previously present
partner disappears, the check's old acceptance becomes stale because its
basis changed. But `Run.ready()` ignores transitions to absence through its
`resolved.version is None` condition. The check does not rerun to accept the
remaining snapshot.

Independent review reproduced this with a modified compact toy scenario:

1. A summary remains required under both dispositions and is not a
   verification subject.
2. Its cited reports exist and its check accepts.
3. A disposition change removes those reports.
4. The summary's acceptance becomes stale, but `check-summary` is not ready.
5. The run has no open attempts or stops and cannot publish.

**Suggested fix:** allow judging code jobs to renew judgments when an
optional basis disappears. Do not indiscriminately rerun model jobs.

This is a pre-existing readiness limitation exposed by the new derived
optional inputs, rather than a defect wholly introduced by these commits.
The reproduction establishes a supported compact-plan edge case, not a
failure observed in the shipped analysis.

## 5. Medium: fidelity tests do not verify consumer-hook substitution

**Location:** `tests/commonplace/agentic_analysis/test_compact_plan.py:121–134`.

Despite its name,
`test_handlers_are_substituted_by_standard_ones_and_declared_checks`
asserts only the standard handler path and `frozen-source`. It does not
assert `checks` or `feedback`.

Independent review removed those options in memory. The plan-comparison
fidelity tests still passed despite removing wiring for:

- boundary binding;
- record-ID preservation;
- memory source identity;
- profile comparison version;
- the record-check gate;
- cited-record feedback.

Separate behavioral tests protect several individual functions, but the
fidelity suite does not establish that the migrated plan invokes them.
This is a confirmed test gap, not an observed loss of hooks in production.

**Suggested fix:** assert the expected hook functions and feedback function
for every derived job, including mapping-form hooks' declared inputs. Keep
the behavioral tests as well.

## Design assessment

The review did not find substantial overengineering. The loader, opaque
code-job options and small consumer hooks form a reasonable boundary.

The main architectural caution is `type_closure()`: it duplicates schema
resolution and already differs from the validator. This is the clearest
place to consolidate implementation rather than add special cases.

## Verification and limits

Coordinator checks:

```text
uv run pytest -q tests/commonplace/artifactrun tests/commonplace/agentic_analysis
562 passed, 96 deselected

uv run pytest -q -m '' tests/commonplace/agentic_analysis/test_integration.py
19 passed

uv run ruff check .
All checks passed!
```

The first command excluded slow tests under the repository's default pytest
configuration. The second disabled that filter for the integration test
file. The full repository test suite and a real end-to-end analysis were
not run.

Two independent read-only reviews examined loader/engine integration and
the analysis migration. Temporary reproductions and in-memory mutations
made no repository changes. Passing tests do not negate the integration
finding: the integration fixtures do not exercise the raw-versus-expanded
identity boundary.

**Recommended priority:** fix finding 1 first, then strengthen migration
wiring tests. Cover findings 2–4 before treating compact plans as generally
supported beyond the shipped analysis.

## Related design

- [Plans without structural wrapper code](../../reference/proposals/plans-without-structural-wrapper-code.md).
- [The correction and verification protocol as implemented](./verification-protocol.md).
