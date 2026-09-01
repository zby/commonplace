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

| Measure | Baseline | Probe or fixture |
|---|---:|---|
| Unique canonical source files | 733 files; 5,275,008 bytes | Wheel package resources resolved through the live scaffold manifest |
| Base installed destinations | 734 files; 5,275,006 bytes | Clean source-checkout initialization, including the empty `kb/log.md` and rendered template |
| Projected skill files | 26 files; 245,280 bytes | Thirteen files copied into each of `.agents/skills/` and `.claude/skills/` |
| Complete installed tree | 760 files; 5,520,286 bytes | Clean source-checkout fixture |
| Unique installed content | 734 blobs; 5,275,006 bytes | Content hashes deduplicate both skill projections |
| Initial full-tree hash pass | 45.7 ms source; 53.0 ms wheel | First observed pass after fixture creation; OS page cache was not controlled |
| Warm full-tree hash median | 44.3 ms source; 44.9 ms wheel | Median of the following eight passes |
| Default `commonplace-status` lines and bytes | 8 lines; 400 source / 399 wheel bytes | Clean fixture projects; the one-byte difference is the project-root path |
| Default status elapsed time | 187 ms source; 193 ms wheel | Median of four warm runs after one process-level first run |
| Baseline bytes for the worked conflict | 7,478 bytes raw | Both sides changed `kb/commonplace/reference/commands.md`; its prior content was needed to locate the conflict |
| Compressed complete-base probe | 1,758,050 bytes | Gzip tar of the 734 non-projected installed destinations; format is not selected |

Record exact commands, commit/package identity, operating system, and whether
caches were warm beside the filled results. Timing is diagnostic, not a release
gate unless the new projection makes the compact front door materially slower.

## First decision-gate conclusions

1. Package identity plus hashes is enough to classify change only while the
   prior package remains available. It is not enough to construct an offline
   three-way plan. The baseline therefore needs the prior installed content,
   not only its hashes.
2. The state must be tracked project-control data, because an ignored local
   record would disappear on a clean clone and turn a known project into an
   unknown one. The selected placement is a root `.commonplace/` control
   directory, subject to an ADR before implementation. `kb/reports/state/` is
   rejected because its payloads are deliberately ignored and machine-local.
3. A template destination needs both the canonical template identity and the
   rendered baseline blob. Its render inputs must also be recorded when they
   are needed to render a later upstream template; the current template uses
   only the project name.
4. Projected skills should map to the same canonical source and baseline blob
   as their `kb/commonplace/instructions/` copies. Their destination hashes are
   still checked independently, but their prior bytes are retained once.
5. A project without a readable supported record is `unknown`. It must not be
   called current or customized. Baseline adoption needs a separate inspectable
   operation; initialization or status must not guess.
6. The selected design is a versioned destination manifest plus
   content-addressed baseline blobs. Exact encoding and compression remain
   implementation choices; content availability and deduplication are the
   required semantics.

## Evidence log

Add dated observations here. Each entry should state the case exercised, exact
inputs, observed classification or failure, and what plan choice it bears on.
Do not use this log as an implementation status list; [plan.md](./plan.md) owns
execution state.

### 2026-09-01 — controlled initialization and cost probe

The fixtures were produced from commit
`e3d4bbbb65d9c489379c8ef377d692db7d81c6d1`, package version `0.1.5`, and
wheel SHA-256
`a5438653c14aaec7560207efca5b9c2198c38bed54d619a3537caefc0bc96ca6`
on Linux 6.8 x86-64. Before recording the result at commit
`30b60fdb208b41fb6d4cf1d838dbb95b984849a5`, a scoped Git diff confirmed that
no package, scaffold, template, or canonical copied input had changed.
`commonplace-source` resolved the source path to this checkout. The wheel ran
in an isolated Python 3.13.1 environment. The source and wheel initializations
produced the same 760 destination paths. Only `AGENTS.md.template` differed
because the fixtures deliberately used different project names.

Hash timings used nine complete sequential SHA-256 passes over all installed
destinations. The first observed pass is not a controlled cold-disk
measurement: initialization had already read the inputs, and the probe did not
flush the OS page cache. Status timings used five new command processes per
fixture. Every run exited zero, returned stable output, and did not create the
Commonplace store.

Commands used: `uv build --wheel`; isolated `uv venv` and `uv pip install` of
the built wheel; `commonplace-init` from the editable tool and the isolated
wheel; `commonplace-status`; and a stdlib measurement probe over the fixture
trees. All fixture state remained under `/tmp`.

### 2026-09-01 — version equality does not establish project identity

A fixture `pyproject.toml` declared version `0.1.5`, equal to the active
command. `commonplace-status --json` returned `success` with no action. After a
local edit to the installed `kb/commonplace/reference/commands.md`, the result
was unchanged. The fixture had no Git repository, matching a supported
downstream condition already handled by status. Package/project version
equality therefore cannot distinguish current content from customization.

### 2026-09-01 — a real conflict requires prior content

The local and upstream fixtures changed the same heading in the 7,478-byte
baseline `commands.md` differently. `git merge-file` produced a content
conflict only when given the prior file. A retained hash can prove that both
sides differ from the baseline, but it cannot locate the conflicting region or
preserve unaffected content when the prior package is unavailable. This case
selects content-addressed prior blobs over a hash-only record.

The complete clean baseline contained 5,275,006 unique content bytes. A
non-authoritative gzip-tar probe occupied 1,758,050 bytes, compared with the
2,502,998-byte wheel. This establishes that offline retention is bounded at the
current scale; it does not select an archive format.
