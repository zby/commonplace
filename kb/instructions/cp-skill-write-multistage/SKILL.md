---
name: cp-skill-write-multistage
description: Write or rebuild one unsettled KB artifact through source-first reconstruction, consolidated authorship, independent review, and guarded promotion. Use when claims need grounding or synthesis; avoid it for settled local edits.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, Skill, Task
argument-hint: "[target path | collection/type/topic] [source paths or brief]"
context: fork
---

# cp-skill-write-multistage

Produce one supported KB artifact while preserving the user's contribution and
leaving evidence-dependent choices to fresh workers. The live target remains
untouched until an independent reviewer accepts its exact candidate bytes.

## Execute now

**Target and inputs: $ARGUMENTS**

Use this workflow when the intended contribution is known but its claims,
evidence, or synthesis remain unsettled. Route a settled edit to
`cp-skill-write`. Keep work with no authorized library target in a workshop.

The invoking agent is the **parent**. It fixes the commission and authority
boundary, supplies privileged context, schedules workers, integrates returns,
owns all live mutations, and handles recovery. Workers choose investigative,
structural, and prose means inside their assigned result and evidence boundary.

Use three roles: a fresh source reconstructor, one fresh consolidated author,
and a fresh independent reviewer. Workers write only their run artifacts and
do not delegate. Conditional procedures may add roles only where they
explicitly say so. If the harness cannot provide the required fresh contexts,
initialize the run and stop before reconstruction.

## 1. Commission one artifact

Resolve one target, mode, collection, type, and acceptance condition. Read the
target collection's `COLLECTION.md` and the applicable type contract in full.
Stop if the collection has no local contract or the target identity is
ambiguous.

- **Edit:** require an existing Markdown target. Frontmatter without `type:` is
  invalid; no frontmatter means implicit `text`. Save byte-exact `original.md`,
  its lowercase SHA-256, and one backlinks query before any worker runs. The
  incumbent is a reconciliation and rollback input, never evidence for itself.
- **New:** resolve the requested collection and type. Default to `kb/notes/`
  and `kb/types/note.md`; an instruction goes to `kb/instructions/`. Reject
  `kb/work/` as a library target. Verify an explicit type path or resolve type
  shorthand to exactly one type spec. Run a targeted near-duplicate search.
  Preserve a valid user-supplied path; otherwise use a provisional filename.

A change of identity, mode, collection, or type restarts setup. A retitle,
replacement, fold, merge, retirement, or artifact-set change requires explicit
user authority; never infer it from a worker recommendation.

Create or resume one
`kb/work/multistage/multistage-write-<short-topic>-<YYYYMMDD>/` run. An
ambiguous or malformed matching run is a recovery stop, not a reason to create
another. Maintain its exact `kb/work/README.md` entry without overwriting
unrelated edits.

Keep only durable run state:

- `README.md` — identity, contracts, current stage, blocker, handoffs, hashes,
  grounding results, checks, and whether the repair allowance was used;
- `brief.md`, `reconstruction.md`, `claim-disposition.md`, `candidate.md`;
- immutable `review-01.md` and, if needed, `review-02.md`;
- `original.md` for edits.

Scratch, copied sources, skeletons, and separate planning or acceptance files
are optional worker means, not workflow state.

## 2. Freeze intent and reconstruct sources

Write `brief.md` from the user's current direction or named retained intent.
Record what workers cannot recover safely: the intended contribution, audience
and acceptance boundary, mutation authority, binding constraints and external
commitments, authorized sources and their roles, exclusions, and choices
reserved to the user or parent. Label parent proposals as advisory. Do not
derive the contribution from the incumbent or search raw interaction history.
Stop on conflicting authority or when several materially different central
contributions still fit.

Acquire every source needed for the governing question. If an external source
needs ingestion or retained quotations, use the grounding interface in section
4 before treating it as available evidence.

For an explicit external duplication, subsumption, keep/rewrite/thin,
merge/retire, or cohort question, run
`kb/instructions/assess-a-claim-bearing-artifact-against-external-literature.md`
(or its installed Commonplace path). That procedure owns source candidacy and
comparison. Its explicitly authorized bilateral-isolation workers are the only
exception to this workflow's three-role topology.

Launch a fresh source reconstructor. Give it `brief.md`, the authorized
source-only paths, and the exact collection/type contracts it needs. Do not
give it the target, `original.md`, incumbent-derived material, prior run
interpretations, candidates, or reviews. Its result is a source-faithful basis
for the commissioned artifact: distinguish support from inference, preserve
conflicts, scope, uncertainty, and source roles, and expose governing evidence
or definition gaps. It owns only `reconstruction.md`; its internal organization
and investigative sequence are its choice.

The parent verifies that the reconstruction answers the brief from authorized
sources and then freezes it. A changed governing premise or substantive new
evidence invalidates this stage and every dependent stage.

## 3. Give one author staged evidence

Use one consolidated author so claim selection and prose remain one coherent
judgment. Its result is a complete target-compatible candidate whose material
commitments are accounted for. It owns only `claim-disposition.md` and
`candidate.md`; it cannot change the live target, sources, ingests, indexes,
lineage, siblings, or run control.

First give the author only `brief.md`, frozen `reconstruction.md`, exact target
contracts, source-only assessment records, and any explicitly bounded
duplicate or premise search. Exclude the target, `original.md`, incumbent-aware
comparisons, prior candidates, and reviews. The author records how every
material reconstructed commitment is treated, including its basis, scope,
qualifiers, dependencies, unsupported boundary, and destination. The author
chooses the disposition format.

After the parent verifies and freezes that source-first account, give the same
author `original.md` and any named incumbent-aware assessment, or confirm new
mode. It reconciles every material incumbent commitment and makes every
replacement, omission, fold, retitle, merge, retirement, or artifact-set
effect explicit. The incumbent supplies no warrant.

The author then writes exact candidate bytes. It chooses decomposition, order,
examples, and wording within the brief, evidence, and target contracts. It
preserves valid metadata and links unless an authorized change requires
otherwise, removes `user-verified` after substantive change unless a human
verifies these bytes, and resolves links from the final destination. A new
material commitment first returns to disposition; a user-owned contribution
or mutation choice returns to the user with the exact decision and resume
point.

## 4. Ground named source dependencies

Before review, identify each new or materially changed candidate claim that
depends on a named external source. For every dependency not already grounded
by the literature procedure, invoke `cp-skill-ground` with exactly:

```text
Target: <exact ingest path or authorized canonical source URL>
Claim needed: <source-side proposition or question>
```

Do not pass target prose or target-specific transfer reasoning. Obtain user
authority before using an agent-nominated untracked URL. The grounding skill
alone owns ingest resolution and permitted Quotes mutations.

- For `quotes sufficient` or `quotes added`, verify the ingest's complete
  Quotes section, apply `semantic/grounding-alignment`, and record the result;
  retain the appended text for `quotes added`.
- For `snapshot required`, follow the returned snapshot and gate requirements
  and retain the exact `(snapshot required)` marker.
- Any blocker, including a `re-ingest.md` route, stops this run. Do not bypass
  the result or invoke `cp-skill-ingest` directly.

Substantive evidence added here returns to reconstruction. Waiting for evidence
is not completion.

## 5. Review exact bytes and allow one repair

Hash `candidate.md`. Launch a fresh reviewer who did not author or revise it.
Give the reviewer the exact candidate and digest, brief, reconstruction,
disposition, edit-only original, target contracts, grounding results, and any
authorized literature-assessment records. Exclude the live target, parent
conversation, scratch, and prior reviews.

The reviewer decides whether those exact bytes may be promoted. It checks the
candidate/incumbent delta against disposition, then intent and omissions,
contract fit, evidence and grounding, specificity, relevance, and prose. Each
blocking finding names its anchor, basis, required byte change, and upstream
return. It writes only immutable `review-01.md` (or `review-02.md` after repair),
names the full digest, and ends with a line containing only `accept` or `block`.
It edits nothing and chooses no repair.

The parent verifies the output and recomputes the digest. Missing, malformed,
or mismatched review is a worker-failure stop. Every run, including a no-change
candidate, requires `accept` for unchanged bytes.

One post-review repair is allowed. Any candidate-byte change after a
well-formed review consumes it, including metadata, whitespace, links,
validator repair, or rebase. Return missing evidence to reconstruction,
missing authority to the user and disposition, and a supported finding within
settled claims to the author. Rerun grounding and use a different fresh
reviewer. A second `block` or any further required byte change stops with the
workshop retained.

When new evidence invalidates reconstruction after the author has seen the
incumbent, rerun reconstruction in a fresh source-only context and repeat both
reveals with a fresh author. Reconfirming byte-identical candidate content does
not spend another repair; any additional byte change does.

Invalidate only what the changed premise affects:

- identity, mode, collection, or type → setup;
- governing intent or substantive evidence → reconstruction;
- claim selection or mutation authority → disposition;
- candidate bytes → fresh review;
- live-target drift → stop for abandon or authorized rebase; a rebase may
  return to disposition only while the repair allowance remains, otherwise a
  new run is required.

## 6. Promote and close

After final acceptance, read and execute
`references/promotion.md` beside this skill. It owns live-drift checks,
conditional retitle, atomic promotion, rollback, validation, lineage, the
closing account, and cleanup. Do not improvise a shorter mutation path.

Report the target or blocker, final candidate and review digests, validation,
any source mutation, whether repair or recovery ran, and whether the workshop
was removed or retained. Suggest `cp-skill-connect` only as optional follow-up;
do not launch sibling work automatically.
