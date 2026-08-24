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

The two promoted artifact-writing workflows, `cp-skill-write` and
`cp-skill-write-multistage`, only check. They prefer an adequate normalized
claim's exact wording and otherwise stop with the grounding route before the
durable target changes. A blocked multistage run retains its candidate and
workshop. Target-specific transfer reasoning remains in the target.

A virtual `source` verdict lens independently checks each resolved
artifact-to-ingest link within the standard selector's `--note` or
`--user-verified` scope. `source/<slug>` narrows to one ingest and `--all-gates`
includes the lens. The persisted criterion is the raw ingest file, so a change
to either artifact or ingest stales the judgment. Its fixed prompt wrapper is
mechanical scaffolding outside the freshness hash, as with type and collection
conformance; a semantic wrapper change requires deliberate corpus-wide
re-review or acknowledgement.

Same-checksum re-ingest preserves Claims. A changed observation requires
explicit approval and is allowed only for the same source and path while Claims
are empty. Before a worker overwrites an existing report, the ingest parent
makes and verifies an exact-byte backup outside the KB. It retains that backup
through the primary and one repair attempt, restores it byte-for-byte after a
handled final failure, and removes it only after validated success or verified
restore.

This is the default for KBs that do not retain immutable snapshots. A KB that
does retain them may verify directly and use Claims only as a cache.

## Boundaries

V1 intentionally has no write-time grounding dispatch, lock, atomic staging,
multi-file commit, crash recovery, claim ID, semantic parser, deduplication,
secondary-resource grounding, or upgrader. Same-ingest concurrent writes may be
last-writer-wins. Ordinary handled failure restore is included; crash-safe and
concurrent-writer machinery can be revisited from observed failures.

The writer guard covers the two promoted writers, not direct manual edits or
every specialized Markdown-mutating workflow. It catches unsupported named
citations, not unattributed prior art. The source lens follows the selector's
existing artifact scope and does not expand its global scan roots.
Source-to-ingest checking happens when an entry is added; source-as-gate review
checks note-to-ingest use. Neither claims continuous verification against an
absent snapshot.

## Consequences

Claim capture grows on demand and remains inspectable from tracked state.
Authors may pay a prepare-then-retry round trip, and similar entries may
accumulate. Re-ingest gains Claims-preservation and ordinary-failure restoration
obligations. The harder support/transfer judgment stays outside the common write
path and uses the existing review-freshness architecture.
