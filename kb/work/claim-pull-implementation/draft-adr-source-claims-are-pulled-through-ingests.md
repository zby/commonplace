# Draft ADR: Untracked source snapshots require grounding through ingests

Intended target:
`kb/reference/adr/NNN-untracked-source-snapshots-require-ingest-grounding.md`.
Assign the next number at promotion. This workshop draft is not an accepted ADR
and must not gain ADR frontmatter or `status: accepted` until implemented.

## Context

Ingest reports retain durable source identity, capture provenance, an exact
snapshot checksum, and source-level analysis. Their novelty-oriented sections do
not require an enumerable account of established source claims. A note can
therefore rely on recalled literature or an external URL without leaving a
tracked statement of what the source establishes, where it says it, or how far
the result reaches.

This gap is partly created by a deployment constraint of this KB, not by a
universal property of knowledge bases. Commonplace is published in a public Git
repository and does not commit full third-party source snapshots. Under
[ADR 072](../../reference/adr/072-ingests-own-source-authority-and-snapshots-are-local.md),
snapshots are ignored local reading copies; the tracked ingest retains the
canonical URL and checksum without redistributing the captured body. A fresh
checkout can therefore identify and attempt to recapture the observation, but
it cannot assume the exact source text is present.

That constraint breaks the direct form of
[ADR 046](../../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md):
a note cannot durably link to an ignored snapshot and later verify its quoted
text against that file. Linking only to an external URL does not restore the
same guarantee because the historical bytes may have changed or disappeared.
The tracked ingest is the available durable place to retain the small source
extracts that local notes actually use.

The Pirolli worked case found local claims that the source supported but the
ingest did not expose as a ledger, plus a local claim that became false under
source comparison. This requires a prospective write-time rule and a tracked
claim section. It does not yet require claim-level graph machinery.

## Candidate decision

When `cp-skill-write` adds or substantively revises a commitment that explicitly
rests on a named external source claim, and the target collection authorizes a
link to `kb/sources/`, it drafts the candidate in memory and dispatches a fresh
grounding worker before saving. The worker ensures that the source's tracked
ingest grounds the needed claim under a required `## Claims` section and returns
a compact disposition to the writer.

The target links to the ingest as a whole. Its prose states which claim it uses
and supplies any target-specific transfer argument. A verifier follows the link
and reads the complete `Claims` section.

V1 has no claim IDs, anchors, reverse-use section, separate claim artifacts,
claim parser, or dedicated command. The section uses the simplest repeated prose
or bullet shape that preserves source claim, fidelity, passage location, scope,
and relevant source-side limitations. A new ingest draft carries an explicit
empty state. When the current demand caused the ingest, the grounding worker may
populate the section immediately after ingestion.

The worker first reads the complete `Claims` section. An adequate entry is a
demand-built grounding cache and can be reused without rereading the source. If
the entry is absent, ambiguous, or inadequate, the worker resolves and reads the
exact source observation named by the ingest checksum before adding or revising
it. Wording marked verbatim is checked against those bytes. Paraphrase is
labelled and remains judgment-based. The entry is checked or attested at
grounding time according to its fidelity layer; ordinary validation does not
promise continuous verification after the local snapshot becomes absent.

V1 admits only claims grounded in the ingest's primary source. The write-skill
handoff names `authority_role: primary`, and only then may the worker resolve
the observation identified by `snapshot_sha256`. Claims whose authority is an
implementation repository or another `secondary_sources` resource return
`BLOCKED`; ambiguous authority also blocks. Supporting those claims later
requires explicit resource identity and resolution of that pinned secondary.
The primary paper snapshot must never stand in for code authority.

This creates a deliberately asymmetric two-hop guarantee:

1. **Source to ingest, at grounding time.** When an entry is added or materially
   revised, the worker checks its exact wording against the checksum-identified
   observation and records the source location, scope, and fidelity. If those
   bytes later become unavailable, this remains a past attestation with a
   recomputation path, not continuous enforcement.
2. **Ingest to note, at validation time.** A note that reproduces exact wording
   links its `verbatim` citation to the tracked ingest. The existing quote
   validator can then check that the note's quote occurs in that tracked file,
   even in a fresh checkout with no snapshot. The grounding-worker contract
   requires the matched extract to be in `Claims`; V1's validator does not scope
   the match to that section. The check proves that the downstream copy has not
   drifted from the tracked ingest. By itself it does not re-prove that the
   ingest still matches an unavailable source observation.

The schema requires the `Claims` heading. A structural migration adds that
heading and the selected empty-state sentence to every existing ingest without
inferring claims from `Summary`, `Connections Found`, or `Extractable Value`.
Semantic cleanup later populates the section by reading selected sources.

The complete `Claims` section is derived from the observation named by the
ingest's top-level checksum. Same-checksum re-ingestion preserves that section
byte-for-byte while redrafting other analysis. `cp-skill-ingest` passes the
preserved heading-and-body bytes and their SHA-256 as fixed inputs, retains the
same inputs for any replacement attempt, and verifies the digest against the
returned section before accepting the result. New ingestion passes neither
value. A changed checksum with non-empty `Claims` blocks before mutation: V1
neither carries the cache to a different observation nor erases it while notes
may depend on it. A later procedure must coordinate regrounding or invalidation
for that case.

The write skill carries only a cheap local trigger, bounded handoff, compact
result handling, and the grounding instruction's path. It does not load the
instruction, ingest, or source for an untriggered write. When triggered, it gives
the fresh worker only the exact candidate claim, intended target and
contribution, named primary source or ingest, dependency, and exact candidate
transfer argument or `none`. The worker never edits the target. If it returns a
narrowing, the writer revises the candidate and dispatches a new fresh worker
with the exact changed wording. The writer saves only a final `SUPPORTED` form.

The trigger uses only the supplied task, incumbent, and in-memory candidate. It
fires for a new or materially changed attribution, quotation, empirical result,
or borrowed mechanism tied to a named source. It does not search for possible
prior art, and an edit does not reground an unchanged dependency.

V1 changes only `cp-skill-write`. Its existing handoff to
`cp-skill-write-multistage` for substantial grounding or synthesis remains
unchanged. The multistage path is integrated only if a worked case later shows
that its source reconstruction needs the same cache.

The source collection contract distinguishes two kinds of authority: the
external source remains the evidential authority for what it says, while the
ingest owns durable local source identity and the tracked grounding record
checked against that source. Existing note link labels already permit routes to
ingests. Other collection link grammars remain authoritative and are not
broadened implicitly by this decision.

## Applicability to other Commonplace KBs

This decision is selected for the current Commonplace repository and for KBs
using the same untracked-snapshot retention profile. It is not a claim that
every installed Commonplace KB should mediate source claims through ingests.

A private KB, or one with permission and capacity to retain immutable source
snapshots, can link a note directly to the tracked observation and verify the
quote end to end. For small sources, that may be simpler and stronger than
copying a claim into an ingest.

The ingest route can still be useful under tracked snapshots. For a paper,
book, long transcript, or large repository, `Claims` is a sparse semantic cache
and index of the pieces this KB has actually used. It reduces repeated source
search and context loading, records scope beside the extract, and gives later
writers a cheap first lookup. Those are performance and navigation advantages,
not a reason to pretend the intermediate copy is the primary authority or an
exhaustive source index.

The shipped Commonplace scaffold currently ignores snapshots, so its default
retention profile shares this repository's constraint. An installation may
choose differently. This ADR must record which parts of the implementation are
default-profile policy and must not present them as architecture required by all
Commonplace KBs.

Installed projects also need a source-side collection contract. A separate
prerequisite bug fix adds a generic user-owned `kb/sources/COLLECTION.md` and
landing alongside the already installed source types and `.gitignore`; this ADR
does not own that scaffold correction. Claim-specific semantics remain in the
ingest type and grounding path, because later `commonplace-init` runs preserve
an installed project's user-owned collection contract rather than rewriting it.

## Open before promotion

- Fix the exact repeated claim shape and empty-state wording.
- Decide the permitted fidelity labels and the minimum support for a paraphrase.
- Fix the section's template position.
- State whether source unavailability blocks every new entry or only fidelity
  levels that cannot be warranted from available material.
- Decide whether the required `Claims` heading belongs to the shipped default
  ingest type or to an untracked-snapshot profile. Do not add a configuration
  system without a worked installation need, but do not encode a local public-KB
  constraint as a universal optimum.
- Define the future owner of changed-checksum regrounding or invalidation. V1
  blocks that transition when grounded claims exist; it does not need to
  implement the later procedure before same-checksum preservation ships.

Remove this section by deciding each item before promotion.

## Considered alternatives

**Assign claim IDs and anchors.** Rejected for V1. Agents can read the entire
small section, and no observed ambiguity or context cost yet warrants a finer
address. IDs remain an upgrade if worked use produces that pressure.

**Add a reverse `Uses in Commonplace` ledger.** Rejected for V1. Notes already
link to ingests, backlinks are searchable, and target-specific transfer belongs
in target prose. A reverse ledger would add synchronization and a second write
phase before a consumer needs it.

**Create a separate claim artifact kind.** Rejected until an ingest section
fails to provide a useful citation and revision boundary in practice.

**Ground primary and secondary resources under one implicit claim shape.**
Rejected for V1. The top-level checksum identifies only the primary observation;
silently using it for an implementation claim is false grounding. V1 blocks
secondary authority until the handoff and entry can identify and resolve the
exact pinned resource.

**Mine every source at ingest time.** Rejected as the primary path because it
must predict future demand and charges full extraction cost before any local
claim needs the source. The ledger grows when claims are pulled.

**Put the full grounding procedure into every write context.** Rejected because
ordinary writes would pay for source-resolution and mutation instructions even
when no explicit external-source dependency changes. A short router plus a fresh
worker keeps that context conditional.

**Expose a standalone user-invocable pull procedure.** Rejected for V1. The
operation is a pre-save branch of authoring, and requiring an operator to invoke
it separately creates a bypass. The reusable unit is a delegated worker
instruction; `cp-skill-write` owns the decision to call it.

**Wire the multistage writer immediately.** Rejected for V1. It already owns a
heavier independent reconstruction and claim-disposition path. Integrating it
without a worked failure would broaden the first implementation without reducing
the cost of ordinary writes.

**Leave claims only in target prose and external URLs.** Rejected because a
fresh reader cannot inspect from tracked state what the source was read to
establish and must reconstruct the grounding before evaluating the target.

**Track snapshots and verify notes directly against them.** Not rejected in
general. This is the cleaner and stronger route for a KB allowed to retain
immutable source bodies. It is unavailable as the general policy of this public
repository because it would redistribute third-party captures and make them
part of the durable Git history. The ingest bridge exists because this KB chose
the untracked-snapshot boundary.

**Build continuous source verification now.** Rejected for V1. Ignored snapshots
make the stronger guarantee unavailable without a separate retention decision.
The first implementation states and checks its pull-time evidence boundary.

**Make quote validation section-scoped now.** Rejected for V1. The existing
checker proves only that a quote occurs somewhere in the linked ingest. The
worker contract places grounded extracts in `Claims`, and an agent verifies the
whole section. The ADR states that composite boundary explicitly; a scoped
referential checker is an upgrade only if the agent-side check proves
insufficient.

**Let re-ingestion regenerate `Claims` from the empty template.** Rejected
because it would silently delete a cache that notes already depend on.
Same-checksum refresh preserves the section exactly. Changed-checksum refresh
with grounded claims fails closed because preservation would be false and
erasure would break consumers.

## Consequences

Source-dependent writing gains a simple tracked grounding surface and pays
claim-extraction cost only on demand. Every ordinary write pays for a short
local check; only a triggered write pays for a worker and a whole `Claims`
section read. The parent writer receives a compact result instead of source
context. The design accepts the worker-side whole-section cost until measurements
justify finer addressing.

All ingests gain one required heading and honest empty state. Existing content
is not semantically migrated. Ingests become incrementally mutable as later
claims are pulled through them.

An unavailable source observation can block a claim that previously would have
been written from recollection. Pull-time checking still does not guarantee later
recoverability; the checksum makes a later loss or mismatch detectable when
rechecking is attempted.

Automatic legacy recapture is rollout scaffolding, not permanent authoring
machinery. The promoted grounding worker blocks when neither the tracked cache
nor an exact local observation suffices. Only the bounded retrospective cleanup
may invoke the checksum-first ingest path and redispatch a fresh worker. Once
cleanup closes, that backup runbook leaves active routing and is preserved only
as non-operative archive history; the fail-closed and checksum-preservation
rules remain current.

For exact quotations, a fresh checkout can deterministically verify the note
against the tracked ingest even when it cannot verify the ingest against the
absent source. The ADR therefore makes both hops visible rather than describing
the ingest check as end-to-end source verification.

Installed KBs that retain immutable snapshots may pay unnecessary duplication
if the required `Claims` section is treated as universally mandatory. They may
instead use the section only as a demand-built cache or index, or prefer direct
note-to-snapshot grounding. Supporting that alternative is a retention-profile
decision, not evidence against the local design.

Re-ingestion gains a retained-state obligation. Its clean-context drafting
boundary may still exclude prior analysis, but it must receive the exact
`Claims` section as preservation input. This adds context only to a re-ingest,
not to ordinary writes or first ingestion.

V1 leaves implementation-code claims outside the cache. Those claims fail
closed instead of receiving a plausible-looking but wrong primary-source
attestation.

The operativity path is the ingest type, schema, and template for the required
section; cache-preserving changes to `cp-skill-ingest` and its drafting
instruction; the structural migration; the delegated grounding-worker
instruction; and a pre-save branch in `cp-skill-write` that dispatches a clean
context with a bounded handoff. The separately fixed generic installed source
collection is a prerequisite to this path, not an implementation output of the
ADR. Validators check the heading and ordinary artifact invariants. Agents
judge claim content and note-to-ingest support by reading the section.

## Promotion checklist

- Resolve every open item.
- Make the candidate decision match implemented behavior.
- State the public-repository constraint, the two verification hops, and the
  tracked-snapshot alternative without universalizing the local solution.
- Preserve populated claims across same-checksum re-ingestion, reject ambiguous
  and secondary authority, and record acceptance of the installed-source-
  collection prerequisite.
- Pass the Pirolli and held-out whole-section verification cases.
- Pass the instruction, contract, migration, authoring-integration, and relevant
  test checks.
- Add ADR frontmatter, number, status, date, and library-relative links only
  after implementation.
