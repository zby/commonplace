---
description: "Proposal (adopted): the single-target CLI and five-file timing comparison behind explicit Markdown file batches"
type: reference/types/design-proposal.md
tags: []
---

# Multi-target validation in commonplace-validate

> **Archived** (see [archive README](./README.md)). Option A shipped for explicit Markdown file paths in commit `dc94eed87` on 2026-11-23. The [commands reference](../../commands.md) and [validation contract](../../validation-contract.md) describe the shipped interface. This record retains the pre-adoption baseline and timing evidence.

## Current state (as of 2026-11-19)

The CLI accepted one positional target, although the validation library already accepted a tuple of paths in one run. Checking an explicit list of edited files meant starting the CLI once per file. Checking their collections instead included untouched files and ran collection-level checks.

## Timing evidence (2026-11-23)

Checking five definition files in five separate CLI processes took 1.17 seconds. A prototype checked the same files in one fresh process through the existing library API and built a JSON report in 0.25 seconds. Both figures are medians of five trials on the same checkout. This measured the benefit of sharing a process and validation run, not the speed of the subsequently shipped CLI or its performance on collection sweeps.
