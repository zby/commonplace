---
description: Publish an accepted analysis at its stable source path and archive any superseded analysis without rewriting member bytes
type: types/instruction.md
---

# Publish an accepted analysis

Expose one accepted complete analysis per source while preserving exact accepted
bytes. Only the coordinator loads this instruction. Analyst obligations end at
their assigned outputs. No regeneration or Git authority follows from this
instruction.

Let the bound assembly and publication jobs run through `commonplace-run advance`
in the prepared worktree. They require exact members, current acceptance and
relation coverage, pinned validation criteria, completed producer provenance,
frozen source and unchanged method/code. Assembly produces the exact-byte
manifest separately from the engine's type-only working projection in `artifact/`.
Publication consumes the pinned manifest and members, not a second `output/` artifact.
There is no standalone finalize, handoff or publication command.

A `complete` disposition publishes GitHub sources to
`retained/<owner>--<project>/`, lowercasing both components and preserving
repository punctuation. Other source kinds retain their existing naming.
Publication names do not change run IDs. An incumbent
moves unchanged to `retained-archive/<its-run-id>/`, then the accepted manifest
and members are copied unchanged. `blocked` and `out-of-scope` dispositions
complete locally without retained mutation. Use `commonplace-analysis
report <run>` to distinguish these results. Its `completed` state means
the bound job completed on current inputs; neither that state nor engine
publishability is a fresh audit of retained files.

After the report and separate operator authorization, run
`commonplace-analysis integrate <run>` with the prepared worktree's
command directory and working directory; its recorded origin must be clean and
on `main` (an agent adds `--model <model-id>`). Integration independently checks
current completion and coverage, exact pinned publication inputs, retained bytes,
publication journal and archive evidence. It stages only the changed retained
artifact and its archive, commits them on `analysis/<run-id>` from the method commit,
and merges that branch into `main`. It refuses unrelated tracked changes or
pre-existing staging in the worktree and a method commit not ancestral to
`main`. A merge conflict is aborted; preserve the branch and worktree for the
operator. Do not copy the artifact or choose a conflict side automatically.

Publication journals record exact trees before mutation. A shared repository
lock coordinates cooperating publishers; exclude non-cooperating writers from
the destination. Ordinary failures restore the incumbent. Abrupt interruption
or failed preliminary guards can leave an uncertain effect. Stop and preserve
the evidence for separately authorized recovery; a journal's state label does
not establish the filesystem outcome. Never edit state to claim completion.
Old/mixed run directories are rejected. Keep old retained data; independently
chosen old-evidence handling requires its archived method checkout, not an
adapter in this tree.

A frozen pre-namespace-migration worktree still uses its pinned publication
name and integration code. Do not patch its members, receipts, method or run ID.
Before separately authorized integration, compare its source identity with the
origin's current publications. If an owner-qualified incumbent exists, stop:
the old integration path does not establish replacement or archive correctness
at the new path. Preserve the audit hold for a separately planned transfer.
If no incumbent exists, an authorized legacy integration may use its pinned
commands, followed immediately by the separately authorized
`uv run python scripts/migrate_analysis_publications.py --apply --record <new-record-path>`
in the origin. Review its dry run first. The migration rejects duplicate sources,
destination collisions and member edits; validate before exposing the result.
This migration command belongs to this checkout, not the installed framework.

The site and comparison tools use the shared current-analyses enumerator. It rejects
partial sets, duplicate sources and directory names that disagree with source
identity. No list or per-source reference file is committed. Links to the
current path follow its newest analysis; version-dependent claims cite the run
ID and commit or the superseded analysis's archive path.
