---
name: cp-skill-write-multistage
description: Write or rebuild one unsettled KB artifact through source-first reconstruction, consolidated authorship, independent review, and guarded promotion. Use when claims need grounding or synthesis; avoid it for settled local edits.
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, Skill, Task
argument-hint: "[target path | collection/type/topic] [source paths or brief]"
---

# cp-skill-write-multistage

Produce one supported KB artifact while preserving the user's contribution and
leaving evidence-dependent choices to fresh workers. The live target remains
untouched until an independent reviewer accepts its exact candidate bytes and
the user approves them.

## Execute now

**Target and inputs: $ARGUMENTS**

Use this skill when the intended contribution is known but its claims,
evidence, or synthesis remain unsettled. Route a settled edit to
`cp-skill-write`. Keep work with no authorized library target in a separate
ordinary workshop and stop.

The invoking agent is the **session agent**. It talks with the user, fixes the
commission and the authority boundary, and owns every live mutation. Workers
choose investigative, structural, and prose means inside their assigned result
and evidence boundary.

Choose the path by the target:

- **An existing note:** follow [part A](#a-rewrite-an-existing-note). The
  rewrite runs as a code workflow, `commonplace-review run rewrite`.
- **A new artifact:** follow [part B](#b-write-a-new-artifact). The session
  agent runs the fresh workers itself.
- **An explicit external-literature question** about an existing note
  (duplication, subsumption, keep/rewrite/thin, merge/retire, cohort): follow
  part B in edit mode. The rewrite workflow has no literature step.

A retitle, replacement, fold, merge, retirement, or artifact-set change
requires explicit user authority; never infer it from a worker
recommendation.

## A. Rewrite an existing note

The workflow runs four fresh workers in order. A reconstructor rebuilds the
evidence from the authorized sources without the note. A claim-account
worker decides, still without the note, how each reconstructed commitment is
treated. An author then receives the frozen claim account and the note, and
writes the candidate with a report that reconciles the note's commitments. An
independent reviewer judges the exact candidate as a review operation, with
a typed review result: `fail` blocks it, `warn` accepts it with findings, and
`pass` accepts it with none. One repair is allowed: on `fail`, a fresh author
receives the review and a fresh reviewer judges the repair. A second `fail`
ends the run unpublished.

This is a deliberate change from part B. Part B uses one author for the
claim account and the candidate, so that claim selection and prose stay one
judgment. In the workflow the two author calls are fresh workers, and the
frozen claim account carries the judgment between them.

The first two workers are not given the note, and their prompt forbids
opening it. They can still read the checkout. The isolation is by supplied
inputs and instruction, not by sandbox.

The author and the reviewer also receive what the revise procedures give
their workers. Before the candidate, the run obtains the note's role report:
a fresh one kept by `commonplace-review run revise <note> --full` on the same
text, without a launch, or else one role-report call. Its `## Role` section,
which lists the terms and claims other notes rely on, reaches the author and
the reviewer as `kb-role`. The operator's decisions in earlier revise and
rewrite runs on the note reach them as `earlier-decisions`. The first two
workers receive neither, so that claim selection comes from the sources
alone.

### A1. Fix the commission with the user

Read the note, its collection's `COLLECTION.md` and its type spec. When the
note declares a write brief (`brief: <stem>.brief.md`), read the brief. The
brief is the one lasting statement of what the note must do, keep and
exclude, and every worker receives it. The commission adds only what is
specific to this rewrite: the current direction, the sources, and any
narrower boundary.

Fix with the user:

- the user's current direction for this rewrite;
- the authorized sources, each with its role;
- without a brief: the intended contribution and what the reader should
  understand or do because of it, what the note must keep and exclude, and
  the decisions reserved for the user, such as a retitle;
- with a brief: only what this rewrite adds to the brief's Intent, Must keep,
  Must exclude and Reserved decisions. Do not restate the brief.

Do not derive the contribution from the existing note. Stop and ask when
several materially different contributions still fit.

The commission must not contradict the brief. When the user's direction
amends a brief item, update the brief with the user before the run, under the
[write brief](../../types/write-brief.md) rules, so that the run captures the
amended brief, and say in the commission which item was amended. A worker
that finds a conflict between the commission and the brief reports a
problem, and the run stops.

A role report on the note states which of its terms and claims other notes
rely on: the one `commonplace-review run revise <note> --full` runs, or the
one a rewrite run obtains (its report's `role` names it). When a role report
lists relied-on terms or claims that the brief does
not keep, tell the user and offer to add them to the brief's Must keep, or to
create the brief when the note has none. Never amend or create a brief
without the user's word. No code writes a brief.

### A2. Ground the sources

Grounding is the session agent's work and comes before the run. Follow
[section C](#c-ground-named-source-dependencies) for each claim that depends
on a named external source. A source the run receives must be a file in the
repository: an ingest, a retained snapshot, or another tracked file.

### A3. Write the commission file

Write the commission as a Markdown file outside `kb/`, for example in the
session's scratch directory. The run captures it; the file is not kept. Use
this format. Code checks the frontmatter and the headings: `## Current
direction` always; the other four only when the note has no write brief.
With a brief, keep only the sections that add something to it, and name in
them any brief item the user amended for this rewrite:

```markdown
---
note: kb/theory/the-note.md
sources:
  - path: kb/sources/some-source.ingest.md
    role: the ingest that states the mechanism
  - path: kb/sources/.snapshots/some-source/page.md
    role: the full text, for exact wording
---

# Commission: <short note name>

## Intended contribution

<The claim or purpose, and the reader update. With a brief: only what this
rewrite adds to its Intent.>

## Must keep

<Passages, distinctions or qualifications, and why. `None.` when empty.
With a brief: only what this rewrite adds to its Must keep.>

## Must exclude

<Content the note must not contain, and why. `None.` when empty. With a
brief: only what this rewrite adds to its Must exclude.>

## Reserved decisions

<Choices the workers must not make. `None.` when empty. With a brief: only
what this rewrite adds to its Reserved decisions.>

## Current direction

<What the user wants from this rewrite.>
```

`note` is the note's repository path. Each source is a repository file other
than the note and its brief. A source that git ignores, such as a snapshot
under `kb/sources/.snapshots/`, is passed by path and SHA-256 and never
copied into the run; any other text source is copied into the run as an
input.

### A4. Run the workflow

```bash
commonplace-review run rewrite <note> --commission <file>
```

Every invocation opens a new run under
`kb/reports/state/review/runs/v2/rewrite/<note path without .md>/<UTC start
stamp>/` and needs the commission. No run is repeated or resumed: to rewrite
under a changed commission, brief or source, run the command again, which
starts a new run.

Read the JSON report and act on it:

- **`held`:** the run holds the accepted candidate; the note is not written.
  Follow [approve a text](../approve-a-text.md#a-held-candidate). On the
  user's word, `commonplace-review publish <run-dir>` publishes the exact
  candidate; for a revision the user states,
  `commonplace-review publish <run-dir> --revised <file>`. Tell the user each
  entry of `new-warnings`. When the report's `accepted` lists
  `warn-findings`, tell the user how many there are and where the review
  is, as `held.what` says, before asking for the decision.
- **`blocked`:** the second review failed the candidate. Read `review-1.md` and
  `review-2.md` under the run's `artifact/` and tell the user. When a finding
  asks for evidence the sources lack, ground or add a source (A2), change the
  commission, and run the command again. When a finding needs a user
  decision, settle it in the commission and run again the same way.
- **`stopped` with a worker problem:** read it to the user. A conflict
  between the commission and the brief needs a changed commission or an
  amended brief, then a new run. A claim that dependents rely on and that
  the claim account leaves out needs the user's decision: keep it, or drop
  it and say so in the current direction, then a new run. Dependents a
  change reaches are the user's separate work. After a transient problem,
  run the command again on the user's word.
- **`stopped` because a referenced source changed:** confirm the new text is
  wanted, then run the command again.
- **`unchanged`:** the reviewer accepted the note's own text. Nothing is
  written.
- **`conflict`:** the note changed during the run. Nothing was written.

After `publish`, its report names the publication. When the published text
is the judged candidate, `current-result` names the accepted review, now the
note's current result. When it left `warn` findings, offer the user a
triage: `commonplace-review run revise <note> --triage`. A `not-current`
report means the user published a revised candidate; its review was not
stored.

The workflow never writes the note itself. `publish` writes it only on the
user's word and only when the note still holds the text the run started
from.

### A5. Keep the commission's lasting parts in the write brief

After publication, write or update the note's
[write brief](../../types/write-brief.md) from the commission's lasting parts:
the intended contribution, what must be kept, what must be excluded, and the
reserved decisions. With a brief, these are the commission's additions to it.
Leave out the current direction and the sources. Follow
the type's rules: do not copy the note's claims, evidence or prose; omit an
empty section; write no brief that would hold only `## Intent`. A new brief
needs `brief: <stem>.brief.md` in the note's frontmatter. Validate the note and
the brief with `commonplace-validate`, one target per call.

A retitle is a separate step on the user's word:
`commonplace-relocate-note <old-path> --to <new-path>`, committed alone.

### A6. Report

Report the run directory, the outcome (published, blocked, stopped or
unchanged), whether the repair ran, the accepted review's `warn` findings and
whether the user took the triage, the brief change, and validation.
Suggest `cp-skill-connect` only as optional follow-up.

## B. Write a new artifact

The parent of this part is the session agent. Use three roles: a fresh source
reconstructor, one fresh consolidated author, and a fresh independent
reviewer. Conditional procedures may add roles only where they explicitly say
so. If the harness cannot provide the required fresh contexts, initialize the
run and stop before reconstruction.

### B1. Commission one artifact

Resolve one target, mode, collection, type, and acceptance condition. Read the
target collection's `COLLECTION.md` and the applicable type contract in full.
Stop if the collection has no local contract or the target identity is
ambiguous.

- **New:** resolve the requested collection and type. Use an explicit collection
  or the project's authored routing for this contribution; ask if it does not
  select one collection. This KB routes theoretical notes to `kb/theory/`;
  scaffold projects commonly use `kb/notes/`. Default the type to
  `types/note.md`; an instruction goes to `kb/instructions/`. Reject
  `kb/work/` as a library target. Verify an explicit type path or resolve type
  shorthand to exactly one type spec. Run a targeted near-duplicate search.
  Preserve a valid user-supplied path; otherwise use a provisional filename.
- **Edit (an external-literature question only):** require an existing
  Markdown target. Frontmatter without `type:` is invalid; no frontmatter
  means implicit `text`. Save byte-exact `original.md`, its lowercase
  SHA-256, and one backlinks query before any worker runs. The incumbent is a
  reconciliation and rollback input, never evidence for itself.

A change of identity, mode, collection, or type restarts setup.

The run parent is exactly `kb/reports/state/multistage/`, in the ignored
operational tree; a run is not a workshop. Before
creating or writing any run artifact, resolve the proposed repo-relative run
path and require its direct parent to be `kb/reports/state/multistage/`, its
basename to match `multistage-write-<short-topic>-<YYYYMMDD>`, and its canonical
path to remain inside that parent. A run directly under `kb/reports/state/`, the
grouping directory itself, or any unresolved or escaping path is a setup blocker.

Create or resume one valid run at that path. An ambiguous or malformed
matching run is a recovery stop, not a reason to create another. The run is
kept after closure; do not commit it or list it in `kb/work/README.md`.

Keep only durable run state:

- `README.md` — identity, contracts, current stage, blocker, handoffs, hashes,
  grounding results, checks, and whether the repair allowance was used;
- `brief.md`, `reconstruction.md`, `claim-disposition.md`, `candidate.md`;
- immutable `review-01.md` and, if needed, `review-02.md`;
- `original.md` for edits.

Scratch, copied sources, skeletons, and separate planning or acceptance files
are optional worker means, not workflow state.

### B2. Freeze intent and reconstruct sources

Write `brief.md` from the user's current direction or named retained intent.
Record what workers cannot recover safely: the intended contribution, audience
and acceptance boundary, mutation authority, binding constraints and external
commitments, authorized sources and their roles, exclusions, and choices
reserved to the user or parent. Label parent proposals as advisory. Do not
derive the contribution from the incumbent or search raw interaction history.
Stop on conflicting authority or when several materially different central
contributions still fit.

Acquire every source needed for the governing question. If an external source
needs ingestion or retained quotations, use the grounding interface in
[section C](#c-ground-named-source-dependencies) before treating it as
available evidence.

For an explicit external duplication, subsumption, keep/rewrite/thin,
merge/retire, or cohort question, run
[assess-a-claim-bearing-artifact-against-external-literature](../assess-a-claim-bearing-artifact-against-external-literature.md),
resolved from this skill's real location. That procedure owns source candidacy and
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

### B3. Give one author staged evidence

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

### B4. Ground, then review exact bytes and allow one repair

Before review, ground each new or materially changed candidate claim that
depends on a named external source, as [section C](#c-ground-named-source-dependencies)
directs. Substantive evidence added here returns to reconstruction. Waiting
for evidence is not completion.

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
run retained.

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

### B5. Promote and close

After final acceptance, read and execute
`references/promotion.md` beside this skill. It owns live-drift checks,
conditional retitle, atomic promotion, rollback, validation, lineage, the
closing account, and run retention. Do not improvise a shorter mutation path.

Report the exact run path, target or blocker, final candidate and review
digests, validation, any source mutation, and whether repair or recovery ran. Suggest `cp-skill-connect` only
as optional follow-up; do not launch sibling work automatically.

## C. Ground named source dependencies

Identify each new or materially changed claim that depends on a named
external source. For every dependency not already grounded by the literature
procedure, invoke `cp-skill-ground` with exactly:

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
  and retain the exact `(snapshot required)` marker. In part A, list the
  snapshot as a source of the commission.
- Any blocker, including a `re-ingest.md` route, stops the work. Do not bypass
  the result or invoke `cp-skill-ingest` directly.

In part A grounding precedes the run, so the claims are those the commission
expects the rewrite to rest on. A source the reviewer finds missing sends the
work back here, then to a restarted run.
