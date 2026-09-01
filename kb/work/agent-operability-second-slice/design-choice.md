# Stage 1 design choice — retain a content-addressed project baseline

## Selection

Advance to an ADR with a tracked project-control record under a root
`.commonplace/` directory. The record should map every framework-owned
destination to its role, canonical source identity, rendered baseline hash,
and one content-addressed baseline blob. It should also record its schema
version, producing Commonplace package/source identity, supported compatibility
information, and template render inputs needed to reproduce later upstream
outputs.

This is a Stage 1 selection, not shipped architecture. Stage 2 must record the
load-bearing storage, producer, transition, and recovery decision in an ADR
before code makes the record authoritative.

## Why this candidate best serves the intent

The record separates three identities that the current version comparison
conflates:

- **canonical source** — the package or source-checkout input selected by the
  live scaffold manifest;
- **installed baseline** — the rendered bytes that creation or a later
  successful upgrade established; and
- **current destination** — the bytes now present in the project.

The active command supplies proposed upstream bytes. Comparing those three
states supports deterministic classification:

| Current destination | Proposed upstream | Classification |
|---|---|---|
| equals baseline | equals baseline | current |
| differs from baseline | equals baseline | locally customized |
| equals baseline | differs from baseline | upstream changed |
| differs from baseline | differs from baseline and current | conflict candidate requiring three-way comparison |
| equals proposed upstream | differs from baseline | convergent change; no replacement needed |
| record schema unsupported or source cannot be interpreted | — | incompatible |
| record absent, corrupt, or not trusted | — | unknown |

Content addressing keeps destination identity independent while retaining one
copy of repeated bytes. In the measured fixture, 760 installed files reduced
to 734 unique blobs because the 26 skill-projection destinations repeated
canonical skill content. A later plan can therefore inspect each projection
for drift without storing its base again.

Tracked root control state is selected because provenance must survive a clean
clone and is neither authored KB content nor machine-local report state. The
exact directory schema and blob encoding belong to the ADR and implementation
probe. The semantic commitments are that the record travels with the project,
baseline content remains available offline, and a partial or unsupported record
never masquerades as current.

## Alternatives tested

| Candidate | Result |
|---|---|
| Package/project version only | Reject. An equal `0.1.5` version remained `success` after a real local edit. |
| Destination hashes plus a prior package locator | Reject as the complete baseline. It classifies which side changed while the package is available, but cannot construct an offline three-way plan when that package is absent. |
| One full prior copy per destination | Reject. It works but stores each runtime skill projection separately and obscures their common canonical source. |
| Retain the prior wheel | Reject as the project baseline. The source-checkout path has no originating wheel, a wheel carries non-scaffold package code and metadata, and the measured wheel was larger than the compressed installed-input probe. |
| Git commit or tree identity | Reject as a requirement. Both clean initialized fixtures were valid projects with no Git repository. Git may be supporting evidence when present. |
| Content-addressed baseline plus destination manifest | Select. It distinguishes identities, preserves prior bytes offline, deduplicates projections, and supports both source-checkout and wheel creation. |

## Required record semantics

The ADR and Stage 2 implementation should preserve these properties without
treating this list as a fixed JSON layout:

- one versioned record written by successful initialization or successful
  explicit upgrade, never by status;
- atomic publication so a partial write cannot become a baseline;
- package version plus concrete source identity: wheel hash for a wheel, and a
  source commit or explicit dirty/source-content identity for a checkout;
- one destination entry with its ownership role, canonical source path or
  template identity, installed baseline hash, and blob reference;
- independent destination hashes for projected skills, with their base blob
  shared with the canonical installed skill source;
- canonical template hash, rendered baseline hash, and required render inputs;
- a supported schema/compatibility boundary and an explicit `unknown` or
  `incompatible` result when it cannot be consumed;
- an owner and terminal transition for superseded baselines; and
- no status-time mutation or implicit adoption of a legacy project.

## Stage 2 discrimination tests

Implementation remains free to choose serialization, compression, module
boundaries, and command names. Reject or return the design if a worked probe
shows that it cannot:

1. publish atomically after both source-checkout and wheel initialization;
2. reproduce the same destination identities from equivalent canonical input;
3. preserve a local customization while identifying an upstream-only change;
4. reconstruct the 7,478-byte worked conflict without network or prior-package
   availability;
5. degrade an absent, corrupt, or future-schema record honestly; or
6. keep default status within a materially similar compactness and latency
   envelope.

