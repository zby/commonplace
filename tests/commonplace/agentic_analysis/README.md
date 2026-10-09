# Analysis consumer tests

This directory tests `src/commonplace/lib/agentic_analysis/`: data contracts,
source checks, handlers, publication, worktrees, CLI lifecycle and instruction
composition. Generic engine tests remain in `tests/commonplace/artifactrun/`.

- `fixtures.py` constructs member and retained-set data without artifact-run execution.
- `execution_fixtures.py` supplies scripted local-Git runs. Stage tests deliberately
  restrict the shipped graph; their passing results are not full-pipeline proof.
- `tests/commonplace/artifactrun/support.py` supplies the shared scripted coordinator.
  Test modules are not fixture libraries.

Run this consumer's tests with:

```bash
uv run pytest tests/commonplace/agentic_analysis
```
