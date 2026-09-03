---
type: kb/types/type-spec.md
name: agentic-system-analysis-run-state
description: Checked operational state for one agentic-system analysis from declared authority through handoff-ready canonical bytes
schema: kb/reports/types/agentic-system-analysis-run-state.schema.yaml
---

# Agentic system analysis run state

## Authoring Instructions

Use this type only for
`kb/reports/state/agentic-system-analysis/<run-id>/run-state.md`, owned by
`kb/instructions/analyse-agentic-system/SKILL.md`. It is a mutable operational
record, not the canonical analysis. The producing workflow validates it after
every phase change. If the run stops, leave the latest valid record in place so
another operator can distinguish unfinished work from a missing result.

Choose the canonical carrier before source work. `response` is valid only when
the caller explicitly selected it and no local operation needs the exact
result. `state` keeps exact bytes for named local consumers until the recorded
cleanup condition is satisfied. `retained` keeps exact bytes needed by a named
future operation from a clean checkout. `cache` is never a canonical carrier.
The canonical entry is the typed `agentic-system-analysis-result`; any compact
artifact under `kb/agentic-systems/` is listed only as a permitted projection.

Advance `phase` in order:

1. `opened` fixes producer, consumers, carrier, retention, projections, and
   exact write authority.
2. `source-frozen` fixes revision, capture identity, source root, and the
   versioned source register.
3. `runtime-sealed` points to one immutable runtime-baseline packet and records
   its digest and the canonical-register version. No lens packet may exist
   before this phase validates.
4. `lenses-issued` records immutable packet files and their supplied source,
   canonical-register, and runtime-seal identities.
5. `lenses-complete` records immutable return files and identifies the accepted
   packet for both mandatory lenses.
6. `reconciled` records the reconciliation seal. A correction names the
   invalidated packet, replacement packet, and old and new register versions;
   an invalidated packet cannot be accepted.
7. `assembled` records the exact entry bytes and, for a package, its canonical
   manifest bytes.
8. `validated` records the SHA-256 of a `commonplace-validate --json` receipt
   for those exact entry bytes. The receipt must identify exactly one
   `agentic-system-analysis-result` and zero warnings or failures.
9. `handoff-ready` rechecks that the declared carrier still contains the
   assembled bytes and that its type and run ID match this record.

Every packet and return path is normalized relative to the run-state directory
and carries a lowercase SHA-256. Packet IDs start with the parent `run-id`.
Every packet and return begins with the same YAML header fields: `run-id`,
`lens`, `packet-id`, `reviewed-boundary`, `source-register`,
`canonical-register`, and `runtime-baseline-sha256`. The validator checks those
values against this record. Correction packets get new identities; never
relabel an in-flight packet or overwrite an earlier packet or return.

For a repository archive, use an absolute acquisition path and record its byte
length and SHA-256; validation checks the exact archive while the run is active.
For every source kind, use an absolute `source-root`; validation requires that
frozen directory to exist while phase state is active. A retained result must
still carry the immutable public source identity needed after local cleanup.

The four body sections are the human audit view. Record each material failed or
recovered command under `## Diagnostics and handoff` with producer, phase,
working directory, exact command, relevant non-secret environment, exit or
non-execution disposition, and exact output or a resolvable retained output
location. An unavailable historical transcript stays an evidence gap rather
than a reconstructed quotation.

## Template

```markdown
---
type: kb/reports/types/agentic-system-analysis-run-state.md
description: "Operational state for <run-id>, retaining phase and byte identities until its declared consumers finish"
run-id: AAS-YYYY-MM-DD-system-slug-nn
phase: opened
producer: kb/instructions/analyse-agentic-system/SKILL.md
canonical-carrier: state
canonical-physical-form: one file
canonical-entry: kb/reports/state/agentic-system-analysis/AAS-YYYY-MM-DD-system-slug-nn/result.md
canonical-manifest: null
canonical-consumers: [operator handoff]
retention-rule: "Keep until every declared consumer completes or is explicitly disposed."
cleanup-condition: "All declared consumers completed; no unresolved transfer or projection disposition remains."
permitted-projections: []
write-authority:
  - kb/reports/state/agentic-system-analysis/AAS-YYYY-MM-DD-system-slug-nn/
source-kind: null
source-revision: null
source-capture: null
source-capture-path: null
source-byte-length: null
source-sha256: null
source-root: null
source-register: null
canonical-register: null
runtime-baseline-path: null
runtime-baseline-sha256: null
lens-packets: []
lens-returns: []
accepted-lens-packets: []
corrections: []
reconciliation-seal: null
assembled-entry: null
assembled-entry-byte-length: null
assembled-entry-sha256: null
assembled-manifest: null
assembled-manifest-byte-length: null
assembled-manifest-sha256: null
validation-target: null
validation-target-sha256: null
validation-receipt-path: null
validation-receipt-sha256: null
handoff-entry-sha256: null
handoff-manifest-sha256: null
---

# Agentic-system analysis run state — <run-id>

## Authority and lifecycle

<Declared consumers, carrier, retention, projections, and write authority.>

## Source and phase receipts

<Frozen source and monotonic phase receipts.>

## Packet and correction ledger

<Packet, return, invalidation, correction, and reconciliation identities.>

## Diagnostics and handoff

<Exact failure evidence, validation receipt, and handoff disposition.>
```
