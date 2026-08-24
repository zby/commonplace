# Claim-pull implementation plan

## Prerequisite: fix the installed source collection

Before changing claim-pull behavior, complete the separate
[installed source collection bug fix](./fix-installed-sources-collection.md).
It makes `kb/sources/` a generic user-owned collection in fresh installations
by adding its missing contract and landing. It does not implement any claim
record, grounding instruction, or verification behavior.

Claim pulling may assume that generic collection surface only after the bug fix
passes its fresh-install, packaging, landing, and rerun-preservation checks.
Claim-specific semantics must remain in the ingest type and grounding path:
existing installed `COLLECTION.md` files are user-owned and a later
`commonplace-init` run will not rewrite them.

The implementation landed in commit `bffedcae`. Keep the prerequisite open
until its completion evidence is accepted; do not reabsorb its now-shipped
scaffold changes into the claim-pull implementation surface.

## V1 invariant

Before `cp-skill-write` saves a target in a collection that authorizes source
links and that adds or materially changes an explicit primary-source
dependency:

1. the write skill drafts the candidate in memory and identifies the exact
   source-dependent wording;
2. a fresh grounding worker reads the source's tracked ingest and its complete
   `## Claims` section;
3. when the needed claim is absent or inadequate, the worker reads the exact
   source observation, adds or repairs the grounding, and validates the ingest;
4. the worker returns a compact disposition and the writer reconciles the
   candidate with it; and
5. only then does the writer save a target that links to the ingest and states
   which grounded claim it uses.

An already adequate `Claims` entry is the tracked grounding cache. Reuse checks
the whole section but does not reread the source. Source recovery is required
when that cache entry is added or materially revised.

## Context-cost boundary

Every write pays only for a short local routing check embedded in
`cp-skill-write`. An untriggered write does not load the grounding-worker
instruction, an ingest, a source snapshot, or the claim-pull workshop.

The local check runs after the candidate has been drafted in memory and before
the target is saved. It triggers only when information already present in the
write task or candidate shows one of:

- the user or retained brief names a source, URL, or ingest as support;
- the candidate adds or materially changes an attribution, quotation, empirical
  result, or borrowed mechanism tied to a named external source; or
- a supplied review finding requires grounding a specified claim in a specified
  source.

For an edit, unchanged source-dependent claims do not retrigger. The check does
not scan the source corpus, look for possible prior art, or ask whether every
sentence could have an external source. Passing mentions and examples that do
not support the target's reasoning remain outside the trigger.

When the trigger fires, `cp-skill-write` dispatches a fresh worker with only the
candidate claim, intended target and contribution, named source or ingest, why
the claim is load-bearing, the primary-source authority, and the exact transfer
argument or `none`. The parent receives only the compact result contract. Full
source and ingest text stay out of the writer's context.

## Simplification boundary

V1 deliberately has:

- no claim IDs or claim anchors;
- no `Uses in Commonplace` section or reverse target ledger;
- no separate normalized-claim artifact;
- no claim-record parser or dedicated CLI command;
- no deterministic mapping from a note sentence to an ingest entry;
- no section-scoped extension to the quote validator;
- no secondary-source claim grounding;
- no general external-claim detector or literature search on the write path;
- no standalone user-invocable pull procedure; and
- no migration that invents claims from existing ingest prose.

These are possible later optimizations, not prerequisites. Add claim identities
only after whole-section reading produces observed ambiguity, mistaken matches,
or material context cost.

## Current state (2026-08-24)

- [`ingest-report`](../../sources/types/ingest-report.md) has source identity,
  checksum, source-level analysis, connections, and extractable value, but no
  required claim ledger.
- [`draft-ingest-report`](../../instructions/draft-ingest-report.md) prioritizes
  novelty and may omit an established premise that a later note needs.
- `cp-skill-write` currently combines drafting and saving in Step 6. It has no
  pre-save grounding branch and does not allow its fork to dispatch a worker.
- `cp-skill-write` already hands substantial grounding and synthesis to
  `cp-skill-write-multistage`; that branch remains intact.
- `cp-skill-ingest` always dispatches `mode: create`, withholds the existing
  ingest body, and replaces the output. Without a change, same-checksum
  re-ingestion would erase accumulated `Claims`.
- Source snapshots are local. A fresh checkout has the ingest's URL and checksum
  but may not have the exact source bytes.
- This public repository does not track full third-party snapshots. That makes
  an ingest-held extract necessary for durable note-to-extract verification here,
  but not necessarily in an installed KB that retains immutable snapshots.
- Before commit `bffedcae`, installed projects received `kb/sources/types/` and
  `.gitignore` but no `kb/sources/COLLECTION.md` or landing. The fix has landed;
  its completion evidence remains the first prerequisite gate.
- There are 284 tracked ingests. Requiring `## Claims` creates a mechanical
  heading migration, not permission for semantic backfill.

## Decisions to close

### Deployment scope

Treat ingest-mediated grounding as a response to the current untracked-snapshot
retention profile, not as a universal KB architecture. The Commonplace scaffold
currently ignores snapshots, so the default installation shares this profile.
An installation that tracks immutable snapshots may instead verify notes
directly against them.

Before changing the shipped ingest type, decide whether `Claims` is a required
part of that default profile or a universal type requirement. Do not build a
configuration system without a worked installed-KB case. Whichever choice V1
makes, the ADR must preserve the alternative and its stronger direct-verification
path.

### Installed-project operativity

The prerequisite bug fix owns the generic source collection contract, landing,
manifest entries, packaging checks, and rerun-preservation tests. Do not fold
those changes into claim pulling or add proposed `Claims` behavior to that bug
fix.

After the prerequisite ships, an installed worker may read the user-owned
source contract for collection scope and the ingest type for claim-specific
semantics. The claim-pull implementation must not depend on later scaffold runs
updating an already installed source contract.

### Claims section

Add one required `## Claims` section to the ingest template. It may contain
simple prose, bullets, or repeated short blocks under one contract fixed before
migration. For every retained source claim, the section must make clear:

- what the source establishes;
- source wording or an explicitly named lower-fidelity paraphrase;
- where the supporting passage occurs;
- the population, conditions, exclusions, and confidence that bound it; and
- any source-side limitation needed to prevent overstatement.

Do not put target-specific transfer arguments into the ingest as if they were
properties of the source. The target states why the source claim applies to its
own mechanism and scope.

### Primary-resource boundary

V1 grounds claims from the ingest's primary source only. Every worker handoff
names `authority_role: primary`; the worker resolves the observation identified
by `snapshot_sha256` only after confirming that role. A claim resting on a
pinned implementation repository or any other `secondary_sources` entry returns
`BLOCKED`. Ambiguous authority also blocks.

This is a deliberate simplification, not evidence that secondary material is
irrelevant. A later extension must carry the exact secondary resource identity
and resolve its pinned observation before it can add secondary-grounded entries.
It must never treat the primary paper snapshot as evidence for a code claim.

### Re-ingestion and invalidation

The `Claims` cache is derived from the observation named by the ingest's
top-level `snapshot_sha256`. Re-ingestion against the same checksum must preserve
the complete `Claims` section byte-for-byte, including its empty state, while
redrafting the other analysis. `cp-skill-ingest` must pass the preserved section
as an explicit fixed input to every primary or repair worker, and must verify it
after the handoff. Before any worker writes, the parent captures
`preserved_claims` as the exact heading-and-body bytes and records their
lowercase SHA-256 as `preserved_claims_sha256`. New ingestion passes both values
as `none`; same-checksum re-ingestion passes the captured block and digest to
every replacement attempt.

When the incoming checksum differs and `Claims` is non-empty, stop before
mutation. V1 does not silently carry claims to a new observation and does not
erase them while notes may still depend on them. Changed-observation
re-ingestion requires a later explicit regrounding or invalidation procedure. An
empty `Claims` section may move to a new checksum through the already explicit
re-ingestion path.

### Note-to-ingest route

The target links to the ingest as a whole. Its surrounding prose must articulate
which claim it uses and, when domains differ, why the mechanism transfers. A
link without that connective does not establish support.

The source collection's existing `Connections Found` section remains ingest-time
discovery context. It is not a reverse index of every note that later cites the
ingest.

### Fidelity guarantee

When a claim entry is added or materially revised, the worker resolves and reads
the exact observation named by the ingest checksum. Exact wording marked
verbatim must occur in that observation. Paraphrase remains judgment-based and
must be labelled as such.

The resulting tracked claim is checked or attested at grounding time according
to the selected fidelity layer. It is not continuously source-verified after
the local snapshot disappears. A later use may trust the tracked entry; a
recheck is required only when the entry itself is inadequate for the new use.

For exact wording, distinguish both verification hops. The worker checks
source-to-ingest when it writes the entry. Later, the existing quote validator
checks note-to-ingest by resolving the note's `verbatim` citation against the
tracked ingest. The worker contract places the extract in `Claims`; the V1
validator checks the file, not that section specifically. The second check does
not imply that an absent source was reverified.

### Temporary legacy recovery and retirement

The promoted grounding worker is steady-state machinery. It may use an exact
local checksum match, but it does not recapture a missing legacy observation or
invoke `cp-skill-ingest` as a fallback. On a cache miss with no exact local
snapshot it returns `BLOCKED` with `legacy recovery required`, the ingest path,
expected checksum, and canonical source URL. Ordinary `cp-skill-write` stops at
that result.

Only the retrospective cleanup runner may use the temporary backup path. For a
frozen cleanup item it:

1. invokes `cp-skill-ingest` with the ingest's exact canonical URL;
2. requires the returned ingest path and `snapshot_sha256` to remain unchanged;
3. requires same-checksum re-ingestion to preserve the complete `Claims` block;
4. resolves exactly one local snapshot matching that checksum; and
5. dispatches a new fresh grounding worker rather than resuming the blocked
   worker.

Duplicate exact matches, unavailable capture, checksum mismatch, changed ingest
identity, or unavailable nested-worker capability leave the cleanup item with a
named blocker. The backup path is never linked from or embedded in the promoted
write or grounding instructions.

Retire this rollout procedure when the cleanup scope is closed: every frozen
item has a terminal disposition or named blocker, no active instruction invokes
the procedure, and the permanent fail-closed and checksum-preservation rules
have been extracted into the ADR, ingest contract, and tests. Preserve the
frozen recovery runbook only in a non-operative archive and remove its workshop
and routing copies, so ordinary retrieval and execution expose only the
steady-state machinery. The archive destination must follow an authorized
lifecycle contract; do not turn the live instruction tree into an ad hoc
archive.

### Authoring integration

Split `cp-skill-write`'s current Step 6 into draft-in-memory, conditional
grounding, and save stages. Add the harness worker capability to its allowed
tools. The skill contains only the trigger, bounded handoff, result handling,
and path of the grounding instruction. The fresh worker loads and executes the
full instruction.

The packet contains the exact candidate transfer argument, not merely a
question about transfer. If grounding returns `NARROW`, or the writer otherwise
materially changes the claim or transfer argument, it dispatches a new fresh
worker with the revised wording. Only `SUPPORTED` wording may be saved.

The loaded target collection contract remains authoritative. Run this branch
only when it permits the target to link to `kb/sources/`; do not use grounding as
a reason to expand a collection's link grammar implicitly. `kb/notes/` already
permits the required edges and is the primary V1 target.

Keep the existing Step 4 branch for claims needing substantial grounding or
synthesis. Do not change `cp-skill-write-multistage` in V1: its independent
source reconstruction is a different, heavier path. Integrate the grounding
cache there only after a worked multistage case exposes a gap.

## Dependency order

1. **Accept the installed-source-collection bug fix.** Require its
   fresh-install, packaging, landing, and rerun-preservation evidence before
   claim-pull implementation changes begin.
2. **Write the simplest candidate `Claims` section for the Pirolli ingest.** Use
   the worked claim set and check whether a verifier reading the whole section
   can judge C1-C4 without IDs.
3. **Try one held-out source.** Select it after the first shape exists and prefer
   a case with different pressure: non-PDF source, several relevant claims, or
   an existing ingest.
4. **Finish the ADR decision.** Fix deployment scope, primary-resource scope,
   re-ingestion semantics, section syntax, fidelity labels, empty-state wording,
   routing trigger, note-link requirement, migration, and worker boundary.
5. **Finish the grounding-worker instruction.** Remove draft markers and make
   every source-resolution, mutation, result, and failure branch executable.
6. **Make re-ingestion cache-safe.** Update `cp-skill-ingest` and
   `draft-ingest-report`, then pass preservation and changed-checksum tests.
7. **Amend and migrate the ingest template.** Update the type spec, schema,
   template, and drafting instruction, then add the required heading and honest
   empty state to all tracked ingests in the same coherent change.
8. **Wire `cp-skill-write`.** Split draft from save, add the cheap trigger and
   fresh-worker dispatch, and leave its multistage handoff unchanged.
9. **Run acceptance cases.** Exercise untriggered write, triggered new write,
   triggered edit, unchanged sourced claim, exact transfer redispatch, existing
   adequate ingest, absent claim, exact source unavailable, several claims in
   one section, narrower source scope, contradiction, and rejected secondary
   authority.
10. **Start semantic cleanup.** Freeze the first claim cohort and apply
   [cleanup-plan.md](./cleanup-plan.md) after the prospective path is live.
11. **Promote and close.** Promote the ADR and worker instruction after
   implementation, retire the cleanup-only recovery runbook to its authorized
   non-operative archive, validate all changed artifacts, run relevant tests,
   update routing, and remove the workshop when owned handoffs are complete.

## Acceptance boundary

- Every ingest contains exactly one `## Claims` section.
- Empty sections state only that no claims have been grounded yet.
- An untriggered write loads no grounding instruction, ingest, or source.
- A triggered write leaves the target untouched until the worker returns an
  acceptable disposition.
- An edit does not reground an unchanged external-source dependency.
- The worker receives only the bounded claim packet and returns only its compact
  result.
- Every packet includes the exact transfer argument or `none`; a material
  revision is redispatched and only a final `SUPPORTED` form is saved.
- Primary-source claims resolve through `snapshot_sha256`; secondary or
  ambiguous authority blocks before that observation is read.
- A verifier can read the full section and determine whether it contains the
  claim the target says it uses.
- Source wording, location, and scope prevent an ingest summary from standing in
  for claim-level grounding.
- Exact wording is checked against the source observation when an entry is added
  or revised.
- A note's `verbatim` quote validates against the tracked ingest when the local
  snapshot is absent, while the result is described only as note-to-ingest
  verification.
- A quote present outside `Claims` can satisfy the unmodified whole-file quote
  checker, but fails the worker/verifier's separate whole-section requirement.
- The target links to the ingest and articulates its dependency and transfer.
- Repeated grounding does not add an obvious duplicate after the worker reads
  the existing section.
- Missing exact source bytes block a new or repaired grounding assertion rather
  than being filled from recall.
- The structural migration preserves every existing ingest's frontmatter,
  checksum, links, and analysis.
- Same-checksum re-ingestion preserves `Claims` byte-for-byte; a changed checksum
  with non-empty `Claims` blocks without mutating the ingest.
- The prerequisite's completion evidence shows that a fresh installed project
  contains both source collection heads and that rerunning initialization
  preserves user edits to them.
- The ADR states that a tracked-snapshot KB may prefer direct verification and
  that `Claims` can instead serve as a cache or index for large sources.

## Upgrade triggers

Claim IDs, anchors, parsers, reverse-use records, or a separate claim node become
candidates only when a worked corpus shows at least one of:

- agents repeatedly select the wrong claim from a `Claims` section;
- whole-section loading consumes material context inside the delegated worker;
- several notes need stable references while the section is frequently revised;
- duplicate claims accumulate despite whole-section review; or
- deterministic freshness or referential checks require a finer address.

A broader automatic trigger becomes a candidate only when measured misses from
the cheap explicit-dependency check matter more than the context it would add to
every write.

## What closes the workshop

1. The ADR and grounding-worker instruction are promoted to their library paths.
2. The required `Claims` section, cheap trigger, bounded handoff, note-link rule,
   and fidelity boundary are operative through `cp-skill-write`.
3. The installed-source-collection prerequisite is accepted; re-ingestion
   preservation, primary-resource rejection, structural migration, and
   acceptance cases pass.
4. Relevant Markdown validation and code tests pass.
5. The cleanup plan has a frozen first cohort, terminal dispositions, and a
   dated execution state.
6. Cleanup-only recovery has no active caller and its frozen runbook has moved
   to an authorized non-operative archive.
7. Handoffs are executed or retained with an owner, proposed delta,
   authorization state, and completion state.
