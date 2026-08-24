# Claim-pull implementation surface

## New files

| Workshop draft | Intended target | Role | Promotion gate |
|---|---|---|---|
| [`draft-adr-source-claims-are-pulled-through-ingests.md`](./draft-adr-source-claims-are-pulled-through-ingests.md) | `kb/reference/adr/NNN-untracked-source-snapshots-require-ingest-grounding.md` | Adopt the one-section grounding invariant for the untracked-snapshot profile, distinguish both verification hops, and record portability limits | Implemented behavior matches the scoped decision and the ADR contract is satisfied |
| [`draft-ground-source-dependent-claims.md`](./draft-ground-source-dependent-claims.md) | `kb/instructions/ground-source-dependent-claims.md` | Fresh delegated worker that grounds caller-selected external-source dependencies without editing the target | Section syntax, bounded handoff, compact result, and failure behavior fixed; acceptance cases pass |

The earlier
[`draft-user-sources-COLLECTION.md`](./draft-user-sources-COLLECTION.md) is no
longer a promotion target. The separate
[installed-source-collection bug fix](./fix-installed-sources-collection.md)
owns the generic scaffold contract and landing. Claim-specific clauses from the
earlier combined draft must instead be dispositioned into the current source
checkout's contract, the ingest type, or the grounding instruction according to
which consumer needs them.

V1 introduces no standalone pull instruction, claim artifact, claim parser,
command, promoted skill, reverse use ledger, or review criterion. Add one only
after a worked failure demonstrates that the worker plus whole-section reading
is insufficient.

## Existing authority to amend

| Path | Expected delta | Consumer / force |
|---|---|---|
| `kb/sources/COLLECTION.md` | Distinguish the external source's authority from the ingest's tracked claim-grounding record, and authorize a target to cite that record through the ingest | Source authors and target collection contracts |
| `kb/sources/types/ingest-report.md` | Define required primary-source-only `## Claims`, its empty state, simple entry semantics, re-ingest derivation boundary, and template placement | Authors and validators loading the type contract |
| `kb/sources/types/ingest-report.schema.yaml` | Require the heading; do not attempt semantic claim validation | `commonplace-validate` |
| `kb/instructions/draft-ingest-report.md` | Emit the required section for a new ingest; accept `preserved_claims` plus `preserved_claims_sha256` and reproduce the exact heading-and-body bytes during same-checksum re-ingestion and repair | Delegated ingest worker |
| `kb/instructions/cp-skill-ingest/SKILL.md` | Detect new versus same-checksum re-ingest; capture and hash the preserved `Claims` section before mutation; pass both fixed inputs to every drafting attempt; verify byte preservation; block a changed checksum with grounded claims | Promoted ingest skill |
| `kb/instructions/cp-skill-write/SKILL.md` | Split draft from save; add `Task` to allowed tools; perform the cheap explicit-dependency check; dispatch the fresh worker with primary authority and exact transfer wording; redispatch material revisions; save only `SUPPORTED` wording | Promoted ordinary write skill |

No change to `cp-skill-write-multistage` or the quote-verification code is
expected for V1. The existing checker remains whole-file; the worker and verifier
own the separate requirement that the extract appear in `Claims`. Generic
installed source-collection operativity is a completed prerequisite, not an
implementation surface here. A cold miss may invoke the amended ingest skill as
a subroutine; the grounding worker then populates `Claims`.

`kb/notes/COLLECTION.md` already authorizes note-to-source edges through
`evidenced-by`, `derived-from`, and `abstracted-from`. The implementation must
recheck every other target collection rather than silently broadening its link
grammar. The write-skill branch applies only where the loaded collection
contract permits a link to `kb/sources/`.

The prerequisite preserves the current scaffold's ignored `.snapshots/`
default, but that retention policy is not an intrinsic Commonplace requirement.
Before the type change ships, fix whether the required section belongs to the
default untracked-snapshot profile or to every ingest-report instance. V1 should
document a tracked-snapshot alternative without adding configuration machinery
until a worked installation needs it.

## Tests and acceptance records

Before claim-pull acceptance begins, attach the prerequisite's fresh-install,
packaging, landing, and rerun-preservation evidence. Claim-pull tests should
then cover the required heading, ingest template output, structural migration,
write-skill tool declaration, re-ingest preservation, and instruction
integrity. Acceptance cases remain agent-read:

- an ordinary write with no explicit external-source dependency, proving the
  worker and source context are not loaded;
- a new source and demanded claim;
- an existing ingest whose section already contains the claim;
- an existing ingest that needs one claim added;
- an edit whose existing sourced claim is unchanged;
- a same-checksum re-ingest with populated `Claims`, preserved byte-for-byte
  through both the primary and repair handoffs;
- a changed-checksum re-ingest with populated `Claims`, blocked before mutation;
- a `verbatim` note quote that resolves against the ingest with the local
  snapshot absent;
- a quote present only outside `Claims`, demonstrating that the whole-file
  checker passes while the agent-side `Claims` check rejects the grounding;
- several claims in one section, with the verifier selecting the right one;
- a primary paper claim accepted and an implementation-secondary claim blocked
  before the paper snapshot is read;
- a narrowed or transfer-revised candidate redispatched and accepted only after
  the corrected wording returns `SUPPORTED`;
- unavailable evidence;
- missing legacy evidence that blocks the promoted worker, is recovered only by
  the cleanup runner, and is then handled by a new worker dispatch;
- repeated pull without an obvious duplicate;
- narrower source scope and contradiction;
- a target that links the ingest but fails to articulate what it uses; and
- a large-source case where `Claims` demonstrates useful cache or index behavior
  independent of snapshot retention.

## Promotion order

1. Accept the installed-source-collection bug fix's completion evidence.
2. Fix the simple section shape and fidelity labels through worked cases.
3. Make re-ingestion preserve the cache, then implement the type contract,
   template, migration, and grounding-worker
   instruction.
4. Wire the cheap branch and fresh-worker dispatch into `cp-skill-write`.
5. Pass acceptance cases, Markdown validation, and relevant tests.
6. Promote the ADR only after it describes shipped behavior.
7. Begin semantic cleanup after prospective writes use the new path.
8. At cleanup closure, remove every active route to the legacy-recovery runbook,
   extract its permanent safety rules, and retire the frozen runbook to an
   authorized non-operative archive.
