---
description: "Commonplace's theoretical collection and shipped library use Theory; project scaffolds keep Notes, generic operations retain explicit scope, and exact historical captures retain their bytes"
type: reference/types/adr.md
status: accepted
---

# 123-Theory names the Commonplace library collection

**Status:** accepted
**Date:** 2026-10-23

## Context

Commonplace distinguishes claims about the design space from its selected
system and procedures. The theoretical collection's name should express that
role beside Reference and Instructions. Calling it Theory only in navigation
would leave conflicting names in paths, library addresses and authoring rules
([ADR 116](./116-one-word-per-concept-across-prose-and-code.md)).

A consuming project's general domain-understanding collection has a broader
purpose. Its starter contract need not impose this KB's theoretical standard
or share its collection name. Library layout and operation eligibility are
separate: a discovered collection is not automatically a review, promotion or
validation scope.

## Decision

This KB's theoretical collection is **Theory**, at `kb/theory/`. The shipped
library exposes it at `theory/`, including the `commonplace:theory/` namespace.
Its members remain notes. The note type, generic note APIs and `source_notes`
field keep their names. Definitions, theory-facing evidence and unadopted
theory retain their existing subareas and placement rules.

Project scaffolds continue to create `kb/notes/` from the soft user templates.
Existing projects keep their collection names and customized contracts. There
is no dual-root library alias or automatic consumer collection migration.
Consumers reconcile references into the changed library namespace on upgrade.

Generic operations keep explicit collection or artifact scopes. The Theory
contract carries `unquoted-source-limit: 5`; applicability follows that contract,
not the directory name ([ADR 122](./122-collections-set-the-unquoted-source-limit.md)).

Historical prose preserves its decision or finding, not necessarily its bytes.
Mechanical navigation repairs may retarget the same relocated artifact in ADRs,
legacy reviews and authored ingest analysis. They must not change historical
claims, quoted source wording, source revisions or snapshot checksums. Exact
captures, experimental inputs and versions, and hash-pinned analysis payloads
remain byte-identical. Historical paths inside those records remain historical;
site redirects do not supply filesystem compatibility.

Old review and freshness state remains intact without identity migration or
carrying old reviews forward. Its continuity is not required. Designing a
replacement review/freshness system is outside this decision.

## Considered alternatives

**Keep Notes, or change only the label.** Keeping the name leaves the collection's
role implicit. A label-only change names one concept differently across operator
and implementation surfaces. The operator chose the full collection rename.

**Rename every consuming project's collection.** Rejected: a project's Notes
collection serves a different, broader purpose. Generic operations already
accept its actual collection name. Init need not create a Theory twin.

**Treat all historical files as byte-frozen, or rewrite all links indiscriminately.**
Both lose the relevant distinction. The former needlessly breaks navigation in
ADRs and other authored prose. The latter corrupts exact captures and hash pins.
Protection follows each artifact's actual contract and evidential role.

**Migrate review identities or add a library alias.** Neither has a demonstrated
consumer requirement. The operator considers the old reviews stale and does not
require continuity. Compatibility machinery and a new state design are not
necessary for this layout change.

## Consequences

Authors and agents read the Theory contract and current routing instructions to
place theoretical work. Build manifests package `theory/`; installed readers
resolve the new library address. Validators, promotion and review selectors
consume explicit scopes rather than infer eligibility from this name. Local
type pointers and schemas use `theory/types/`. Site readers reach moved pages
through direct redirects from old published addresses.

Existing library references in consuming projects require reconciliation after
upgrade, even when those projects keep their own Notes collection. Protected
captures can retain links that no longer resolve in a current checkout. Moved
artifacts have new review identities; no freshness acknowledgement is implied.

This decision names this KB's collection and shipped library. It does not rename
the note type, prescribe collection names for other KBs, broaden operation scope,
change theoretical placement tests, or settle Work/Tasks/proposal lifecycles.
