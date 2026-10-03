---
description: Publish an accepted analysis at its stable source path and archive any superseded set without rewriting member bytes
type: types/instruction.md
---

# Publish an accepted analysis

Expose one accepted analysis per source while preserving exact accepted bytes.
Only the coordinator loads this instruction. Analyst obligations end at their
accepted output. No regeneration or Git authority follows from this instruction.

Use `commonplace-agentic-analysis-publication` through the run driver. It
validates the complete set, frozen source, method commit, member hashes and
expected incumbent identity before changing a public path. The accepted
`output/overview.md` is the candidate. There is no separate review projection.

Publish to `retained/<source-slug>/`; the slug is the run-ID source slug. Move
an incumbent unchanged to `retained-archive/<its-run-id>/`, then copy the
accepted manifest and members unchanged. Complete run state pins the working
manifest and published overview. The manifest pins every member. Stage and
commit the full archive move and replacement together when Git publication is
authorized; do not commit a partial set.

Ordinary I/O failures restore the incumbent and previous run state. An abrupt
interruption may leave a partial directory or an archive with no current set.
Treat uncertain publication as stopped evidence. Inspect both areas; restore
the old set or finish the exact accepted copy under separate recovery authority.
Never resume an old-method run by changing its method commit.

The site and comparison tools use the shared current-set enumerator. It rejects
partial sets, duplicate sources and directory names that disagree with source
identity. No list or per-source reference file is committed. Links to the
current path follow its newest analysis; version-dependent claims cite the run
ID and commit or the superseded set's archive path.
