# Analysis consumer tests

This directory tests `src/commonplace/lib/agentic_analysis/` and
`src/commonplace/cli/analysis.py`: member types and records, source checks,
the plan's data and worker prompts, the workflow, publication, withdrawal,
worktrees and integration.

- `test_workflow.py` drives the whole workflow end to end with a fake
  harness on a local Git source: corrections, publication, inspect, reset,
  integrate and the CLI's exit codes. Its tests are slow.
- The other modules test one domain module over plain values; where the
  workflow already covers a behaviour end to end, they test only what it
  cannot reach, such as interrupted or refused effect states.
- `fixtures.py` constructs member and retained-artifact data without running
  the workflow.
- `execution_fixtures.py` supplies the prepared method checkout, the local
  source upstream and member generators that pass the real checks.

Run this consumer's tests with:

```bash
uv run pytest tests/commonplace/agentic_analysis
uv run pytest tests/commonplace/agentic_analysis -m slow
```
