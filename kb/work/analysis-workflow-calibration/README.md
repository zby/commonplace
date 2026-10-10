# Workshop: analysis workflow calibration

- **Posed:** 2026-10-10, by the operator, to build evaluation alongside the
  implementation of the compact-plan proposal without editing its files.
- **Question:** do the registered worker profiles distinguish unsupported
  synthesis claims from supported, explicitly bounded claims?
- **Closes when:** the initial paired-case pilot has a reviewed result for each
  runnable profile, unavailable profiles have exact launch evidence, and the
  operator has decided which findings warrant production changes or further
  tests. Extract durable conclusions before closing the workshop.

## Scope and ownership

This workshop owns this directory, `scripts/analysis_workflow_calibration.py`
and `tests/calibration/`. It does
not own the live plan, handlers, type rules, production instructions, proposal,
or the other agent's tests. The active-workshop index gets only a navigation
entry. Neither agent stages or commits the other's files.

The first pilot is a focused semantic-support assay using synthetic excerpts
and the committed synthesis-verifier mission. It is not full artifact
validation, source acquisition, tool-mocked instruction testing, a production
analysis, or evidence of production fitness. Those extensions return to an
operator decision after the pilot; do not build them speculatively.

## Materials

- [Protocol](./protocol.md): evaluation boundary, profile selection, isolation,
  annotation and interpretation.
- `cases/packets.json`: eight public inputs, four faulty/control pairs.
- `expected/judgments.json`: private expected judgments and reasons. These are
  author-proposed answer keys, not independently verified ground truth.
- `runs/README.md`: retention and run-index conventions.

The helper prepares packets and scores annotations. It launches no model and
supplies no filesystem sandbox. The operator-authorized baseline uses fresh
worker conversations, packet-specific inputs and explicit read/write scope.
Wider filesystem access remains technically possible, and repository instructions
may load. Report these limitations; do not call the trials sandboxed or claim
technically enforced blinding. Sandboxing is deferred, not a launch prerequisite.

## Theory used

- [Reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md)
  motivates faulty-support cases with plausible conclusions.
- [Final task success does not establish intended-path health](../../notes/final-task-success-does-not-establish-intended-path-health.md)
  motivates separate execution and judgment outcomes.
- [Oracle accumulation](../../notes/oracle-accumulation-improves-the-selection-environment.md)
  motivates retaining valid controls alongside failure-derived tests. Passing
  this small authored set does not establish broad verifier discrimination.

## Mechanical tests

Calibration tests live outside the normal `tests/commonplace/` suite and have
an independent pytest configuration. Run them explicitly:

```bash
uv run pytest -c tests/calibration/pytest.ini tests/calibration
```

Normal `uv run pytest` does not collect them. These tests check packet preparation,
profile binding, input integrity and scoring mechanics; they launch no models.

## Status

Cases and mechanical tooling are built. The first exploratory `pi-luna-low`
pilot completed eight calls: four inserted defects detected, three supported
controls accepted, and one control disputed. See the [run index](./runs/README.md).
The answer key still needs independent review before an evidential pilot. The
other agent may continue implementing the proposal without waiting for this work.
