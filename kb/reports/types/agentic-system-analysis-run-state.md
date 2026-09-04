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
2. `source-frozen` fixes revision, capture identity, source access root, and the
   versioned source register.
3. `runtime-sealed` points to one immutable runtime-baseline packet and records
   its digest and the canonical-register version. The packet has a structured
   identity and route-closure header described below. No lens packet may exist
   before this phase validates.
4. `lenses-issued` records immutable packet files and their supplied source,
   canonical-register, and runtime-seal identities.
5. `lenses-complete` records immutable return files and identifies the accepted
   packet for both mandatory lenses.
6. `reconciled` records the reconciliation seal. A correction names the
   invalidated packet, replacement packet, and old and new register versions;
   an invalidated packet cannot be accepted. Accepted new-record proposals and
   amendments may advance the canonical register during reconciliation without
   invalidating the packet that proposed them.
7. `assembled` records the exact entry bytes and, for a package, its canonical
   manifest bytes.
8. `validated` records the SHA-256 of a `commonplace-validate --json` receipt
   for those exact entry bytes. The receipt must identify exactly one
   `agentic-system-analysis-result` and zero warnings or failures.
9. `handoff-ready` rechecks that the declared carrier still contains the
   assembled bytes and that its type and run ID match this record. It also
   supplies the complete structured input to the operator-handoff renderer.

`runtime-baseline-path`, `diagnostic-ledger-path`, every packet and return
`path`, and `validation-receipt-path` are normalized relative to the run-state directory.
For `state` and `retained`, `canonical-entry`, `canonical-manifest`,
`assembled-entry`, `assembled-manifest`, and `validation-target` are normalized
repository-relative `kb/` paths. A response has null canonical paths; its
assembled validation copy may instead use either a repository-relative `kb/`
path or an absolute temporary path. `validation-target` uses exactly the same
path spelling as `assembled-entry`. Every byte-identified path carries a
lowercase SHA-256. Lens packets and returns also record byte length. A return
may not exceed the positive `lens-return-byte-budget` declared at `opened`;
the template's 32768-byte budget is a default, not a claim that every full lens
has the same information need.

Packet IDs start with the parent `run-id`. Every packet and return begins with
the same YAML header fields: `run-id`,
`lens`, `packet-id`, `reviewed-boundary`, `source-register`,
`canonical-register`, and `runtime-baseline-sha256`. The validator checks those
values against this record. Correction packets get new identities; never
relabel an in-flight packet or overwrite an earlier packet or return.

The runtime baseline begins with a YAML header carrying `run-id`,
`reviewed-boundary`, `source-register`, `canonical-register`, and
`route-closure`. The first four values match the seal-time run-state identities.
The run state preserves that seal-time register separately as
`runtime-baseline-canonical-register`, so later reconciled register advances do
not rewrite or ambiguously infer the baseline identity.
`route-closure` contains exactly one mapping per `RTE-*` row under
`## Canonical routes`. Every mapping has non-empty `route-id`,
`immediate-return`, `later-read-back`, `delegated-visibility`,
`selection-predicate`, `invalidation-or-expiry`, `activation-or-effect`, and
`evidence-and-limits` fields. Use an explicit reason for an inapplicable or
uninspected stage. The validator rejects duplicate, missing, or unknown routes
before lens work can inherit the baseline.

For a repository archive, use an absolute acquisition path and record its byte
length and SHA-256; validation checks the exact archive while the run is active.
For every source kind, use an absolute `source-root`; validation requires that
directory to exist while phase state is active. For `source-kind: checkout`,
the root is a Git checkout, `source-revision` is a full commit object ID, and
`source-capture-path` equals `source-root`. Validation checks that the commit
still resolves from that checkout. The commit is the frozen evidence boundary;
the checkout is only its persistent access root, so its current HEAD may move
without changing the completed analysis. A GitHub repository acquired by
`analyse-agentic-system` uses the ignored owner-qualified path
`related-systems/<owner>--<repo>/`. A retained result must still carry the
immutable public source identity needed after local cleanup.

The byte-identified diagnostic ledger is UTF-8 JSON Lines with no blank lines.
It exists from `phase: opened`; an empty ledger is a zero-byte file. Each object
has these fields:

`id | producer | phase | operation | working-directory | relevant-environment | outcome | classification | exit-status | exact-output or output-path plus output-byte-length and output-sha256 | material | disposition | recovery when recovered`

The ID begins `<run-id>-DIAG-`. `working-directory` is absolute.
`relevant-environment` is a list of non-secret strings. `outcome` is `failed`,
`truncated`, or `non-executed`. `classification` is `tool-failure`,
`execution-error`, `expected-invalidation`, `environmental-condition`,
`source-conflict`, or `harness-error`. `exit-status` is an integer or null.
Exactly one of non-empty `exact-output` and run-relative `output-path` is set;
an output file also carries its byte length and SHA-256. `material` is Boolean.
`disposition` is `recovered`, `unresolved`, or `non-evidentiary`; only a
recovered record has the non-empty `recovery` field. Every unresolved material
diagnostic is named by ID in an assembled result before handoff.

The four body sections are the human audit view. Summarize diagnostic and
recovery disposition under `## Diagnostics and handoff`, but keep exact
machine-checked records in the ledger. An unavailable historical transcript
stays an evidence gap rather than a reconstructed quotation. The ledger proves
the integrity of recorded events, not that a harness exposed every event.

`handoff` is null before `phase: handoff-ready`. At handoff it contains exactly
two `lens-runs` mappings, one for each mandatory lens, with non-empty `scope`
and `brief` or `full` depth. It also contains:

- `legacy-memory-review`: detection, invocation, optional location, and
  validation or blocker disposition;
- `transfer-scan`: disposition and optional location;
- `retention-disposition` for every workflow-owned file;
- concise `limitations`; and
- concise `blockers`.

These are the fields not otherwise available as structured run or result
frontmatter. `commonplace-agentic-analysis-handoff` combines them with the
existing lifecycle, result, boundary, revision, tier, digest, and receipt
identities. Do not re-extract these values from prose or maintain a second
hand-written handoff.

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
canonical-consumers: [requesting operator]
retention-rule: "Keep until the requesting operator explicitly disposes the result or selects another authorized disposition."
cleanup-condition: "The requesting operator explicitly disposed the result or its recorded downstream disposition completed; no unresolved transfer or projection disposition remains."
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
runtime-baseline-canonical-register: null
diagnostic-ledger-path: diagnostics.jsonl
diagnostic-ledger-byte-length: 0
diagnostic-ledger-sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
lens-return-byte-budget: 32768
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
handoff: null
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
