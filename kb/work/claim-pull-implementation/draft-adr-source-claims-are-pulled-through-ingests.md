# Draft ADR: Ground source claims through tracked ingests

Intended target:
`kb/reference/adr/NNN-untracked-source-snapshots-require-ingest-grounding.md`.
Promote only after implementation.

## Context

Commonplace tracks source ingests but not full third-party snapshots. A fresh
checkout therefore retains source identity and checksum without the passages a
note used. Existing ingest analysis is novelty-oriented and may omit an
established premise later needed by a note.

## Decision

Every ingest has one `## Claims` section before `## Connections Found`. Empty:

```markdown
## Claims

No claims have been grounded yet.
```

Each entry contains a normalized `Claim (paraphrase)` with one or more adjacent
`Source extract (verbatim)` / `Source location` pairs, followed by `Scope`,
`Confidence`, and `Limitation`.

Grounding is an explicit preparation step. An ingest and snapshot pair by their
shared slug; the ingest checksum verifies that named snapshot. Grounding reads
that primary source and either reuses an entry or asks `cp-skill-ingest` to
append a new one. Existing entries are immutable to grounding. Later runs may add
similar, narrower, or disputed entries; V1 does not reconcile them.

`cp-skill-write` only checks. It prefers an adequate normalized claim's exact
wording and otherwise stops with the grounding route. Target-specific transfer
reasoning remains in the target.

A virtual source-as-gate review pair independently checks each reviewable
artifact-to-ingest link. The ingest is the criterion-side freshness input, so a
change to either artifact stales the judgment.

Same-checksum re-ingest preserves Claims. A changed observation requires
explicit approval and is allowed only for the same source and path while Claims
are empty.

This is the default for KBs that do not retain immutable snapshots. A KB that
does retain them may verify directly and use Claims only as a cache.

## Boundaries

V1 intentionally has no write-time grounding dispatch, lock, multi-file commit,
claim ID, semantic parser, deduplication, secondary-resource grounding, or
upgrader. Same-ingest concurrent writes may be last-writer-wins. These costs are
smaller than permanent coordination machinery and can be revisited from observed
failures.

The writer guard catches unsupported named citations, not unattributed prior
art. Source-to-ingest checking happens when an entry is added; source-as-gate
review checks note-to-ingest use. Neither claims continuous verification against
an absent snapshot.

## Consequences

Claim capture grows on demand and remains inspectable from tracked state.
Authors may pay a prepare-then-retry round trip, and similar entries may
accumulate. Re-ingest gains a Claims-preservation obligation. The harder
support/transfer judgment stays outside the common write path and uses the
existing review-freshness architecture.
