---
description: "Draft decision that the source and report type specs move from project copies under kb/sources/types and kb/reports/types into the library's global types, named by bare name and usable in any collection, with one fixed alias for immutable snapshots"
type: kb/reference/types/adr.md
tags: []
---

# 087-Source and report types are global library types

**Status:** workshop draft; not accepted
**Date:** 2026-09-25
**Amends:** [ADR 086](../../reference/adr/086-projects-read-the-library-from-the-installed-package.md) (projects read the library from the installed package)
**Promotion condition:** accept only with the implementation that makes the
resolver alias, the emitters, init's migration, and the collection contracts
operative. Allocate the ADR number at promotion; 087 is provisional.

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

Snapshots add a constraint. A tracked ingest pins its local snapshot's bytes
with `snapshot_sha256`, and snapshots are immutable after capture
([ADR 072](../../reference/adr/072-ingests-own-source-authority-and-snapshots-are-local.md)).
About 480 local captures in this checkout carry the path-valued snapshot type,
and every project that has captured sources holds its own. Rewriting their
`type:` line would change bytes that the ingests pin.

## Decision

**The seven types become global library types.** Their specs and schemas move
into the library's `types/` and are named by bare name: `ingest-report`,
`snapshot`, `source-review`, `connect-report`, `full-pass-report`,
`agent-memory-analysis-report`, and `agentic-system-analysis-run-state`. They
resolve, validate, and ship like every other global type under ADR 086.

**No new scoping rule.** Like any global type, these types are eligible in
every collection. No collection is closed to other types, and no type declares
a home collection. The sources and reports collection contracts, and the
procedures that write there, keep describing their default contents; they do
not restrict them.

**One fixed alias for immutable captures.** The resolver treats exactly
`type: kb/sources/types/snapshot.md` as the global `snapshot` type. The alias
exists because a capture's bytes can never be rewritten, so it has no removal
condition while old captures exist. New captures write `type: snapshot`. No
other retired path gets an alias; this is the one exception to ADR 086's
"the form selects the resolver, with no fallback".

**Init stops copying and migrates.** Init no longer installs
`kb/sources/types/` or `kb/reports/types/`. On a rerun it treats an old copy
of these specs like the old `kb/types/` copy: a file matching the library is
removed, and a differing one is kept and listed. It then rewrites the
project's frontmatter pointers to removed copies as bare names, as ADR 086's
migration already does for global types, and skips `.snapshots/`, which the
alias covers. Local schemas that referred to a copied schema move to
`commonplace:types/...`.

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

**Rewrite snapshot pointers and re-pin checksums.** Breaks capture
immutability and the rule that an ingest's `snapshot_sha256` never changes. It
also cannot reach captures on other machines, because snapshots are local.

**A general fallback from old paths to global names.** Would make every
retired `kb/.../types/X.md` path resolve. Lost to ADR 086's no-fallback rule:
only snapshot bytes cannot be rewritten, so only the snapshot path needs an
alias.

Left open: whether the Commonplace-internal report types (full-pass,
agentic-analysis run state, agent-memory analysis report) should later move
out of the shipped library if their procedures stop being promoted. Today
their procedures ship, so their types ship with them.

## Consequences

**Easier.** Every type that Commonplace code or procedures produce now comes
from one installed copy and follows upgrades. Init copies nothing that code
depends on, so the remaining scaffold (starter collection contracts, landings,
ignore files, control-plane templates) is project-owned in fact as well as in
name. The residual subject of copy-provenance tracking disappears.

**Harder or riskier.**

- About 490 tracked ingest reports and the other typed reports in this
  checkout change their `type:` line. Review pairs on those files register a
  content change, and review baselines built on them need acknowledgement or
  refresh.
- Local, ignored report state (full-pass and agentic-analysis reports) also
  carries path-valued types. Init's migration rewrites the ones it can see; a
  file it misses fails validation with a missing type until rewritten.
- The snapshot alias is permanent in practice. It is small and exact, but it
  is a known exception to ADR 086's resolver rule.
- A project that customised a copied spec keeps its fork only if it still
  uses the path form. After migration that fork is an ordinary local type and
  no longer receives framework changes, which is the intended ownership.

**Operativity path.** The type resolver consumes the decision when it resolves
the bare names and the snapshot alias. Validation's type rules, the snapshot
commands, and the full-pass and agentic-analysis code consume it in code
through bare names. `commonplace-init` consumes it when it stops copying the
two type trees and migrates old copies and pointers. Agents consume it through
the sources and reports collection contracts, their installed templates, and
the procedures that name these types, which change to bare names with the
force of the collection contract and the invoked skill.

**Where the decision stops applying.** It covers only the seven types named
above. It does not change the starter `COLLECTION.md` files or other
scaffold, which stay project-owned and unsynchronised by design. It does not
decide where a project should keep ingested sources, and it does not govern
project-authored local types. The snapshot alias covers only the exact old
snapshot path; captures written with any other retired pointer are outside it.
