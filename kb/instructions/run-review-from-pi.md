---
description: "Configure and run commonplace-review using Pi as the launching session or as the headless reviewer worker (profile entry, auth check, and smoke test)."
type: types/instruction.md
---

# Run a review from Pi

Goal: run `commonplace-review` from a Pi session or configure Pi as the headless reviewer worker in `review-profiles.yaml`.

The Pi session that starts a review and the worker that judges the note are separate. To use Pi only to **start** a review, ask it to run `commonplace-review NOTE --criteria prose/source-residue --profile sonnet` from the project root; that uses a Claude Code worker and needs no Pi worker credentials or subagent extension.

## Use Pi as the reviewer worker

1. Follow [INSTALL.md](../../INSTALL.md) for the consuming project. Use a Git repository with at least one commit (the checkout guard reads `HEAD`) and an existing KB note. Confirm `commonplace-review --help` and `pi --version` work in the launch shell.
2. Pick a provider and model from `pi --list-models`, set up provider credentials (for example via `/login` in Pi), and verify in the launch environment with `pi auth check --model PROVIDER/MODEL`. The worker must read the note and installed library and write its result under `kb/reports/state/review/runs/` without prompting.
3. Add an entry under the existing `profiles:` key in the library's [review-profiles.yaml](./review-profiles.yaml), replacing `PROVIDER/MODEL` with your chosen ID. For durable customization, use an editable Commonplace install and edit `kb/instructions/review-profiles.yaml` in that checkout (a file of the same name in a consuming KB is not an override):

   ```yaml
     pi-review:
       harness: pi
       launch-model: PROVIDER/MODEL
       effort: medium
       flags:
         tools: read,grep,find,ls,write
   ```

   The built-in adapter selects print mode and JSON output; do not start a headless server or add those flags yourself. Because Pi's `write` tool is not restricted to the result path, always inspect the checkout guard (`guard.changed`) after a run.

## Verify

Run one missing or stale gate on one note (replace `NOTE` with its repository-relative path):

```bash
commonplace-review status NOTE --criteria prose/source-residue
commonplace-review NOTE --criteria prose/source-residue --profile pi-review
commonplace-review status NOTE --criteria prose/source-residue
```

The review run should report `reviewed` (use `--force` only if the pair is already fresh) and the final `status` should report `fresh`, regardless of the verdict.
