# Baseline — project provenance and upgrade safety

This file holds observations and measurements for the second operability
slice. Keep implementation decisions in an ADR if they ship; use this file to
show which evidence selected them.

## Current implementation map

| Concern | Current authority or consumer | What it proves now | Known gap to test |
|---|---|---|---|
| Shipped scaffold inventory | `src/commonplace/scaffold_manifest.py` | Which directories, trees, files, templates, and skills initialization processes | It does not record which source bytes reached a particular project. |
| Scaffold application | `src/commonplace/cli/init_project.py` | Missing files are created; identical and differing existing files are classified; differing files are preserved | Rerun comparison is against the active package, not a retained prior baseline, so upstream and local changes are conflated. |
| Command identity | installed `llm-commonplace` package metadata | The active command package version | It does not identify the copied doctrine, library, or projected skills in an installed project. |
| Project identity in status | project `pyproject.toml` version when present | A project-declared package version in source checkouts | Installed KB projects need not be Python packages, and equality does not establish copied-input identity. |
| Situation projection | `src/commonplace/lib/project_status.py` and `commonplace-status` | Compact Git, notes-validation, lifecycle, and optional review state | Version mismatch currently has only one coarse failure classification. |
| Installation description | `kb/reference/instruction-generation.md` | Current copy, template, package-data, and preservation semantics | The documented upgrade path is still manual diff-and-merge. |

## Required baseline observations

Fill this table before choosing the project-source record:

| Measure | Baseline | Probe or fixture |
|---|---:|---|
| Canonical copied files tracked | TBD | Clean disposable initialization |
| Canonical copied bytes tracked | TBD | Clean disposable initialization |
| Projected skill files tracked | TBD | Clean disposable initialization |
| Time to hash canonical and installed inputs | TBD | Warm and cold local runs |
| Default `commonplace-status` lines and bytes | TBD | Clean fixture project |
| Default status elapsed time | TBD | Clean fixture project |
| Per-file baseline bytes needed for a real conflict | TBD | Customized-project upgrade fixture |

Record exact commands, commit/package identity, operating system, and whether
caches were warm beside the filled results. Timing is diagnostic, not a release
gate unless the new projection makes the compact front door materially slower.

## Open questions for the first decision gate

1. Can the installed baseline identify canonical source content by package
   version plus hashes, or must it retain source bytes to make three-way plans
   available offline?
2. Where should load-bearing project-source state live so installed projects
   receive the same contract without confusing it with user-authored KB
   content or disposable reports?
3. How should template substitutions be represented so both the canonical
   template and installed result remain verifiable?
4. Are projected skills compared to their installed `kb/commonplace/`
   canonical copies, to package inputs, or both? Which comparison identifies a
   partially refreshed project without creating duplicate authority?
5. What is the honest state of a legacy project with no source record: unknown,
   adoptable after inspection, or upgrade-blocked until a baseline operation?
6. Does a three-way plan need retained baseline bytes, reconstructible package
   artifacts, or a content-addressed cache? Test offline and missing-version
   cases before choosing.

## Evidence log

Add dated observations here. Each entry should state the case exercised, exact
inputs, observed classification or failure, and what plan choice it bears on.
Do not use this log as an implementation status list; [plan.md](./plan.md) owns
execution state.

