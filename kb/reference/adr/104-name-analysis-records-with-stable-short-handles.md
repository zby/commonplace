---
description: Use analyst-owned short named record handles, checking whole tokens and written grouping endpoints without inferred intervals
type: reference/types/adr.md
status: accepted
---

# 104-Name analysis records with stable short handles

**Status:** accepted
**Date:** 2026-10-04
**Amends:** [ADR 096](./096-analysis-passes-declare-their-own-records-under-lens-prefixes.md) for record suffixes; analyst ownership and immutable identities remain in force.
**Amended by:** [ADR 115](./115-analysis-records-are-cited-by-markdown-links.md): records are cited by Markdown links; bare IDs are literal, so the grouping-prose and token-prefix rules below record the prior decision.

## Context

Numeric record IDs require a lookup to identify their referent. A wrong number
can resolve to a different record without any syntax error. Numeric grouping
also implies intermediate records that endpoint scanning does not check. This
was the reason for refusing ranges; it did not establish that grouping prose
was analytically wrong. Range refusal also incurred repairs in analysis jobs.

Names can use identities and labels already present in the analysis. A naming
check of both retained Dynamic Cheatsheet sets found handles for all fifty
records within three words, without duplicates or token-prefix collisions.
That check establishes feasibility for those records, not improved reliability.

## Decision

Current analysis records use `<analyst>-<kind>-<name>` under the
[shared record contract](../../agentic-system-analyses/instructions/agentic-analysis-records.md).
Names have one to three lowercase hyphenated words, each starting with a letter
and optionally containing digits. Components and objects use available
source-native names. Other kinds use their labels. Source-path or role qualifiers
distinguish generic names and parts. When no source-native name exists, role,
input or label may suggest a handle; no fallback is prescribed.

An ID is a permanent handle, including across corrections. Dropped IDs cannot
be reused for different referents. Names do not encode analytical conclusions.
Analysts choose names; code checks grammar, uniqueness and reference resolution.
No step renames IDs, and reconciliation allocates none.

Check whole candidate tokens before grammar validation. Refuse a declaration
whose ID extends another declared ID by a hyphenated word within the same analyst
and kind. This prevents attached prose from silently resolving to another record.
The refusal explains the rule without adding it to worker instructions.

Named `through`, dash and `to` grouping prose is permitted. Resolve each written
endpoint without expanding an interval. Semantic review judges whether the group
supports its claim. Single-ID fields and structured citation lists stay explicit.
Numbered `SRC-*` IDs retain source-range refusals. Source quotations and fenced
excerpts remain outside record syntax checks.

## Considered alternatives

**Numeric IDs with role-local range guidance.** Keeps allocation simple, but
retains lookups, wrong-number references and guidance that must reach each job.
It remains the alternative to weigh at the revisit below.

**Use names without a word bound or source preference.** Allows more description,
but increases reference length and gives parallel analysts fewer shared naming
cues. The retained naming check supports three words for now. Naming requires
analyst judgment; code does not generate names or enforce semantic suitability.

**Forbid named grouping prose.** Treats an analytical grouping choice as a syntax
fault. Named handles remove implied numeric intervals; resolving written endpoints
and reviewing the claim address separate concerns.

**Accept both suffix formats or migrate history.** No current consumer requires
this. Historical sets remain frozen and excluded from the current population.
Future analyses use one grammar.

## Consequences

Analysts, reconciliation, verification and synthesis receive the shared contract
through declared worker dependencies. Their Markdown records and profile citations
reach member and set validators through the shared parser. Workflow acceptance and
publication refuse malformed, duplicate, colliding and unresolved IDs. Matrix and
landscape consumers resolve profile citations against the same declarations;
absence classification also uses the named grammar. A nearest declared name in
the same analyst/kind may be suggested on refusal; it never substitutes an ID.

Naming adds worker instructions and a new source of misspellings. The shared
contract's net growth is bounded to about 700 bytes; other worker files do not grow
in net. Token checks and diagnostic suggestions stay in code. Historical records
are unchanged, and current readers provide no numeric-suffix fallback.

The retained naming check and fixtures establish feasibility and parser behavior.
They do not establish that analysts choose stable names or make fewer reference
errors. The first analysis under this contract needs a separate commission.

**TODO: revisit named record IDs** after the first few analyses under them,
or earlier if one of these is observed:

- a group phrase or named range that leaves membership too vague for the claim;
- repeated refusals for misspelled or unresolved names;
- attempts to rename an ID after an interpretation changed, or IDs that encode a conclusion;
- names that made two different records look the same, or hid a duplicate;
- naming rules growing in the worker's input.

Count source-ID range refusals, unresolved or altered references, collisions,
and within-job repairs and retries separately. Record semantic grouping faults
separately from syntax refusals. Named ranges are not errors merely because they
use `through` or a dash. Compare numeric IDs with role-local range guidance and
the existing checks before extending or reverting this decision.
