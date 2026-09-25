---
description: "Source and report type specs are global library types named by bare name and usable in any collection; local snapshots are retyped once and their ingest checksums re-pinned"
type: reference/types/adr.md
tags: []
status: accepted
---

# 087-Source and report types are global library types

**Status:** accepted
**Amended by:** [ADR 088](./088-type-values-are-paths-on-a-two-root-search-path.md) — type values become paths such as `types/snapshot.md`, and captures get one more recorded type-line rewrite
**Date:** 2026-09-25
**Amends:** [ADR 086](./086-projects-read-the-library-from-the-installed-package.md) (projects read the library from the installed package) and [ADR 072](./072-ingests-own-source-authority-and-snapshots-are-local.md) (ingests own source authority; snapshots are local and immutable)

## Context

ADR 086 stopped copying the library into projects, but init still copies the
type specs of two collections: `kb/sources/types/` (ingest report, snapshot,
source review) and `kb/reports/types/` (connect report, full-pass report,
agent-memory analysis report, agentic-system analysis run state). Init
installs them as project-owned, and projects name them by path.

The copies are project-owned in name only. Commonplace code and procedures
depend on their exact paths and shapes:

- the snapshot commands write `type: kb/sources/types/snapshot.md`;
- validation keys its type rules to `kb/sources/types/snapshot.md` and
  `kb/reports/types/agent-memory-analysis-report.md`;
- the full-pass and agentic-analysis code writes its report types by path;
- the ingest, connect, full-pass, and agentic-analysis procedures produce
  exactly these shapes.

A project that edits its copy therefore gets code and skills that still assume
the original. A release that changes a spec leaves every existing project on
its old copy with no signal. This is the divergence ADR 086 removed for the
rest of the library, left in place for seven types. Init also installs
Commonplace-internal report types that a project never authors by hand.

These types are not tied to their collections by necessity. The sources and
reports collections are where Commonplace's procedures put these artifacts by
default. A user may reasonably keep ingested sources, or reports, somewhere
else (operator, 2026-09-25). The global
[agentic-system analysis result](../../types/agentic-system-analysis-result.md)
type is a precedent: a procedure-produced type that already lives in the
library.

Snapshots add a constraint. A tracked ingest pins the exact bytes of its local
snapshot, frontmatter included, with `snapshot_sha256`; a derived ingest also
pins its precursor capture with `original_snapshot_sha256`. ADR 072 makes
snapshots immutable after capture and forbids changing an existing ingest's
checksum. Validation of `kb/sources` warns on a mismatch, and grounding
(`cp-skill-ground` and the grounding-alignment gate), ingest, and re-ingest
stop on one. About 480 local captures in this checkout carry the path-valued
snapshot type, and every project that has captured sources holds its own.
Snapshots are local and ignored, so each clone on each machine holds its own
copy of the same bytes.

## Decision

**The seven types become global library types.** Their specs and schemas move
into the library's `types/` and are named by bare name: `ingest-report`,
`snapshot`, `source-review`, `connect-report`, `full-pass-report`,
`agent-memory-analysis-report`, and `agentic-system-analysis-run-state`. They
resolve, validate, and ship like every other global type under ADR 086. No
retired path resolves; ADR 086's rule that the form selects the resolver, with
no fallback, stands.

**No new scoping rule.** Like any global type, these types are eligible in
every collection. No collection is closed to other types, and no type declares
a home collection. The sources and reports collection contracts, and the
procedures that write there, keep describing their default contents; they do
not restrict them.

**Snapshots are rewritten once, and their checksums re-pinned.** A single
migration replaces a capture's frontmatter line naming a retired snapshot type
path (`kb/sources/types/snapshot.md` or `./types/snapshot.md`) with
`type: snapshot` and changes nothing else. The transformation is
byte-deterministic, so identical old bytes on any machine become identical new
bytes. The migration retypes every such capture. An ingest beside it that pins
the capture's old bytes, through `snapshot_sha256` or
`original_snapshot_sha256`, gets the new checksum. An ingest that already pins
the new bytes, because another clone migrated it, needs nothing more. A capture
that no ingest pins is retyped too: no checksum names its bytes, so nothing can
break. An ingest that pins neither form stays mismatched, as validation already
reports.

The migration is idempotent. It amends ADR 072 in exactly one place: this
recorded migration is the only permitted change to a capture's bytes and to an
existing ingest's checksum. New captures write `type: snapshot`. Installed
projects run it through init; clones of the source checkout, which never run
init, run it through a one-off script.

**Init stops copying and migrates.** Init no longer installs
`kb/sources/types/` or `kb/reports/types/`. On a rerun it treats an old copy of
these specs like the old `kb/types/` copy: a file matching the library is
removed, and a differing one is kept and listed. It then rewrites the
project's frontmatter pointers to removed copies as bare names, as ADR 086's
migration already does for global types, and runs the snapshot migration
instead of skipping `.snapshots/`. Local schemas that referred to a copied
schema move to `commonplace:types/...`.

**Projects keep local types.** A project may still author its own type specs
under `kb/sources/types/` or `kb/reports/types/`, named by path, like any
collection-local type.

## Considered alternatives

**Keep project copies (status quo).** Loses on divergence, the reason ADR 086
exists. The copies cannot be truly project-owned while code writes and checks
their paths.

**Library-owned collection-local types.** Keep the specs under the library's
`sources/types/` and `reports/types/`, with a new reference form such as
`type: sources/ingest-report` that resolves in the library and stays eligible
only in the matching project collection. Lost: it adds a second library
resolution form next to bare names, and it keeps a scope restriction that the
operator does not want.

**Global types with a home collection, or closed collections.** Each spec
declares `collection: sources`, and the validator rejects the type elsewhere
or rejects foreign types in a closed collection. Rejected by the operator
(2026-09-25): users may want ingested sources in other places, and no failure
has shown that the restriction is needed.

**A permanent resolver alias for the old snapshot path.** Leave captures
untouched and resolve exactly `kb/sources/types/snapshot.md` as the global
`snapshot` type. It keeps ADR 072's immutability without exception, but it
keeps a retired path alive indefinitely as the one fallback in ADR 086's
resolver. Lost to the operator's choice (2026-09-25) to rewrite: the checksum
guards against unrecorded change, and a deterministic, recorded rewrite that
re-pins the checksum preserves that guarantee without a lasting exception.

**Retype only pinned captures.** The draft of this decision left unpinned
captures alone and reported them. Lost in implementation: an unpinned capture's
bytes are named by no checksum, so retyping it cannot break a pairing, and
leaving it would keep the retired path alive in captures awaiting ingest.

**A general fallback from old paths to global names.** Would make every
retired `kb/.../types/X.md` path resolve. Lost to ADR 086's no-fallback rule;
every other pointer can be rewritten directly.

Resolved in implementation: clones of the source checkout run the migration
through a one-off script rather than a package command, because the source
checkout is the only consumer that never runs init.

Left open: whether the Commonplace-internal report types (full-pass, agentic-analysis
run state, agent-memory analysis report) should later move out of the shipped
library if their procedures stop being promoted. Today their procedures ship,
so their types ship with them.

## Consequences

**Easier.** Every type that Commonplace code or procedures produce now comes
from one installed copy and follows upgrades. Init copies nothing that code
depends on, so the remaining scaffold (starter collection contracts, landings,
ignore files, control-plane templates) is project-owned in fact as well as in
name. The residual subject of copy-provenance tracking disappears, and no
retired type path survives in any resolver.

**Harder or riskier.**

- About 490 tracked ingest reports change their `type:` line, and those whose
  snapshots are present locally also change their checksum. Review pairs on
  those files register a content change, and review baselines built on them
  need acknowledgement or refresh.
- Until a clone runs the migration, its snapshots mismatch the pulled ingests.
  Validation warns, and grounding, ingest, and re-ingest stop on those pairs,
  until the migration rewrites them. A clone whose capture had already drifted
  keeps its mismatch, which validation reports.
- An ingest whose snapshot is absent on the machine that runs the migration
  keeps its old checksum. It is re-pinned only by a later run on a machine
  that holds the capture, which then commits the new checksum.
- Local, ignored report state (full-pass and agentic-analysis reports) also
  carries path-valued types. Init's migration rewrites the ones it can see; a
  file it misses fails validation with a missing type until rewritten.
- A project that customised a copied spec keeps its fork only if it still
  uses the path form. After migration that fork is an ordinary local type and
  no longer receives framework changes, which is the intended ownership.

**Operativity path.** The type resolver consumes the decision when it resolves
the bare names. Validation's type rules, the snapshot commands, and the
full-pass and agentic-analysis code consume it in code through bare names. The
snapshot migration consumes the ADR 072 amendment when it rewrites captures and
re-pins checksums; `commonplace-init` runs it in installed projects, together
with removing old copies and rewriting pointers. Agents consume the decision
through the sources and reports collection contracts, their installed
templates, and the procedures that name these types, which change to bare
names with the force of the collection contract and the invoked skill.

**Where the decision stops applying.** It covers only the seven types named
above. It does not change the starter `COLLECTION.md` files or other
scaffold, which stay project-owned and unsynchronised by design. It does not
decide where a project should keep ingested sources, and it does not govern
project-authored local types. The ADR 072 exception covers only the one
frontmatter line this migration replaces; any other change to capture bytes or
ingest checksums remains forbidden.
