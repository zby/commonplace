---
name: cp-skill-write-multistage
description: Write or rebuild a KB artifact with source-first reconstruction, consolidated authorship, independent review, and guarded promotion. Use when claims need grounding, synthesis, or separation across multiple artifacts; avoid it for settled local edits.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, Skill, Task
argument-hint: "[target path | collection/type/topic] [source paths or brief]"
context: fork
---

# cp-skill-write-multistage

Produce one supported KB artifact without exposing source reconstruction to the incumbent or promoting bytes an independent reviewer did not accept.

## EXECUTE NOW

**Target and inputs: $ARGUMENTS**

Use this when grounding, synthesis, or separation leaves claims, evidence, or artifact shape unsettled.
Confirm before routing a settled edit to `cp-skill-write` or work without a library target to a workshop.

The invoking agent is the **parent**. It owns admission, brief and evidence, run state, decisions,
invalidation, grounding, scheduling, integration, live mutation, concurrency, promotion, validation,
lineage, recovery, cleanup, and reporting. The target stays untouched until promotion; workflow state never enters its frontmatter.

The universal writing path uses only three worker roles: isolated source reconstructor, consolidated
candidate author, and fresh independent reviewer. Do not add a core planner, skeleton writer,
draft-only writer, auditor, acceptor, or repairer. No core worker may delegate. A loaded conditional
procedure may use only the workers, artifacts, and callee-internal calls it explicitly authorizes;
the parent still schedules and integrates them, and no other delegation is allowed. If fresh contexts
are unavailable, initialize the run and stop before reconstruction.

## 1. Admit and initialize

Resolve one target, mode, collection, type, authority, and done state.

Resolve the target collection to a directory under `kb/`, require a local `COLLECTION.md`, and read
that contract in full. Stop if the selected collection has no local contract.

- **Edit:** require an existing Markdown target. Read its frontmatter type spec when present.
  Frontmatter without `type:` stops; no frontmatter means implicit `text`. Run one backlinks
  query. Before workers run, save byte-exact `original.md` and its lowercase SHA-256. The incumbent
  is a reconciliation input, drift baseline, and rollback source, never evidence for itself.
- **New:** resolve the supplied collection, type, topic, or path. Default to `kb/notes/` and
  `kb/types/note.md`; an instruction without a collection goes to `kb/instructions/`. Reject
  `kb/work/`. Verify an explicit type path. Resolve shorthand across global and collection-local
  type specs and require exactly one matching `name:`; stop on zero or several. Explicit `text`
  means no frontmatter. Run one targeted near-duplicate search. Keep a valid user path fixed;
  otherwise use a provisional lowercase-hyphenated filename of at most 70 characters.

A filename may change later only for the same provisional new artifact. A change of identity, mode,
collection, or type restarts setup. Never mutate a near duplicate or retarget without authority.

Create or resume
`kb/work/multistage/multistage-write-<short-topic>-<YYYYMMDD>/` with an immutable run key. Resume
one matching unfinished run; ask if several match. Add a suffix only after proving a collision is a
different valid run. A matching or ambiguous directory without valid state is a recovery stop.
Maintain its exact `kb/work/README.md` line without overwriting unrelated work; if overlap prevents
that, record and report the pending index update.

Keep a small run `README.md`: identity and contracts, sources, current step, one blocker, handoffs,
grounding results, candidate/review digests, whether post-review reconciliation was used, and checks. Keep `brief.md`,
`reconstruction.md`, `claim-disposition.md`, `candidate.md`, immutable review records, and
edit-only `original.md`. Do not require claim architecture, skeleton, separate draft, mutable audit,
separate acceptance, or copied sources; pin only for a concrete identity risk. Scratch is not run state.

## 2. Freeze intent and evidence

Write `brief.md` from current direction or named retained intent with an explicit authoritative or
advisory role. Current direction prevails; conflict stops. Do not search raw interaction history,
derive purpose from the incumbent, or let contracts choose the contribution. Label parent proposals.

Record question, contribution, audience, scope, done state, acceptance, constraints, privileged facts,
external commitments, coupling, target authority, evidence paths and roles, exclusions, and reserved
choices. Acquire and verify every source needed for the governing question before reconstruction.
When a required source lacks a readable authorized path, use the `cp-skill-ground` call and result
contract in Section 5 with the tracked ingest or authorized canonical URL and the exact source-side
question. Obtain user authority first for an agent-nominated untracked URL. Include substantive
evidence produced here in the first reconstruction. For a blocker use `DECISION NEEDED: intended contribution (specification gap)`,
`DECISION NEEDED: central contribution`, `EVIDENCE NEEDED`, or `DEFINE`; record owner and resume point, then stop.

Only for an explicit external duplication, subsumption, or keep/rewrite/thin/merge/retire/cohort
question, execute `assess-a-claim-bearing-artifact-against-external-literature.md` from
`kb/instructions/` in the source checkout or `kb/commonplace/instructions/` when installed. It
owns source candidacy, comparison, disposition, and calls to `cp-skill-ground`; do not duplicate it.
Add its required assessment records to this run. When that procedure authorizes bilateral isolation,
its fresh target worker, target-blind source/grounding worker, and isolated comparison worker may
write `target-claim-inventory.md`, `source-reconstruction.md`, and `isolated-comparison.md`; this is
the exact conditional exception to the three-role core. The multistage parent retains final
authorship, review, promotion, and integration. Separate source-only records from incumbent-aware
records when constructing later packets. Do not load it for ordinary grounding, synthesis, or
revision. Stop on an interface or authority gap.

## 3. Reconstruct in isolation

Launch a fresh report-only worker with this complete packet:

- **Result and constraints:** reconstruct enough authorized source evidence to answer `brief.md`.
  Separate support from inference; retain source roles, conflicts, scope, uncertainty, and proportional
  detail; invent no precision; do not delegate.
- **Inputs and exclusions:** read only `brief.md`, its exact source-only paths, and named collection
  or type contracts. Exclude the target, `original.md`, incumbent-aware assessments, earlier
  reconstruction/disposition, planning or scratch, candidate, reviews, and incumbent-derived text.
  The brief must therefore contain no incumbent paraphrase.
- **Output and coordination:** write only `reconstruction.md`; the parent alone schedules and
  integrates it, and no other writer touches it.
- **Verification and stop:** record material facts, mechanisms, distinctions, quantities, definitions,
  evidence strength, conflicts, labeled inferences, gaps, and irrelevant detail with each material
  basis and boundary. Stop on a missing input or governing gap with `EVIDENCE NEEDED` or `DEFINE`.

The parent verifies and freezes the output before incumbent-aware work. Never append reconciliation
or review findings. Changed premises require a new fresh run of this role.

## 4. Author disposition and candidate

Launch one author role with staged incumbent reveal and this complete packet:

- **Result and constraints:** write a complete disposition, then exact target-compatible candidate
  bytes. Preserve evidence roles, scope, qualifiers, uncertainty, definitions, dependencies, simple
  wording, and target contracts. Add no undisposed claim; do not delegate or infer mutation authority.
- **Output and coordination:** write only `claim-disposition.md` and `candidate.md`. The parent
  controls reveals, decisions, and feedback. The worker cannot mutate target, run state, sources,
  ingests, lineage, index, siblings, near duplicates, citers, or other artifacts.

**First reveal:** provide only brief, frozen reconstruction, exact target contracts, source-only
literature records, and any bounded read-only duplicate/premise search whose scope and purpose the
packet names and which excludes the target. Exclude original, target, incumbent-aware comparisons,
prior dispositions, candidates, and reviews. The author writes only `## Source-first disposition`.
For every material reconstructed commitment, record basis, scope, qualifiers, dependencies,
definitions, unsupported status or gap, independent-claim boundary, and one treatment:
central/type-required content, support/example/scope, cite existing, proposed fold, separate-artifact
handoff, omit, or evidence/authority gap. Name the existing or proposed target and the useful
citation or revision boundary when relevant. A claim-bearing note normally has one importable central
proposition; `synthesis` requires the relation among citable components to be central; instructions
and similar types may have their required multiple commitments.

The parent verifies and freezes that section. **Second reveal:** give the same role byte-exact
`original.md` and named incumbent-aware assessments, or confirm new mode. It appends
`## Incumbent reconciliation`, mapping each material incumbent commitment to keep/change/omit and
making replacement, fold, retitle, merge, retirement, and artifact-set effects explicit. The
incumbent supplies no warrant.

- **Stop:** before prose, return any user-owned central contribution or mutation choice and its resume
  point. Broader work is only a handoff.
- **Complete and verify:** after gates clear, write `candidate.md`. The author chooses decomposition,
  order, paragraphs, examples, and wording. Preserve valid metadata and links unless authorized
  change requires otherwise; remove `user-verified` after substantive change unless a human verifies
  these bytes; resolve links from the final destination. A new commitment first updates disposition
  or returns upstream. The parent checks both disposition sections, claim coverage, contracts, and
  write scope.

Feedback returns through the parent. A premise change before any completed review invalidates the
affected stages and repeats both reveals with a fresh author when source-first isolation was lost; it
does not consume the post-review reconciliation allowance.

## 5. Ground named source dependencies

Before review, identify each new or materially changed candidate claim that depends on a named external
source; unchanged edit wording and passing mentions do not retrigger the gate. For an exact dependency
already grounded by the external-literature procedure, consume and verify its current grounding
result instead of calling the skill again. For each new or unresolved dependency, invoke
`cp-skill-ground` with exactly:

```text
Target: <exact ingest path or authorized canonical source URL>
Claim needed: <source-side proposition or question>
```

Never include target prose or target-specific transfer reasoning. Get user authority before passing
an agent-nominated untracked URL because the callee may invoke `cp-skill-ingest`. The callee owns
resolution, permitted ingest creation, and the only allowed reuse or append in an ingest's Quotes
section; it validates or restores that mutation and never edits target or other ingest sections. This
parent never edits or creates an ingest.

For `quotes sufficient` or `quotes added`, read complete Quotes, use only its verbatim extracts,
apply `semantic/grounding-alignment`, and use an unmarked ingest link; record path and returned
appended text for `quotes added`. For `snapshot required`, follow the returned name-paired snapshot
and gate requirements and retain the exact `(snapshot required)` marker. Any blocker, including the
exact `re-ingest.md` route, stops the run; never bypass it or invoke `cp-skill-ingest` directly.
Substantive new evidence invalidates reconstruction. Waiting is not completion.

## 6. Review and reconcile

After grounding, hash exact candidate bytes. Launch a fresh reviewer who did not author or revise
them; changed bytes require a different fresh reviewer. Its complete packet is:

- **Result and constraints:** decide whether those exact bytes may be promoted. Use only authorized
  inputs; anchor findings; edit nothing; do not delegate; return exactly `accept` or `block`.
- **Inputs and exclusions:** read candidate and full SHA-256, brief, reconstruction, disposition,
  edit-only original when present, exact target contracts, parent-supplied grounding results, and
  every authorized external-literature assessment record when that branch ran. Exclude target,
  parent conversation, scratch, prior reviews, and every unnamed path.
- **Output and coordination:** write only immutable `review-01.md`, or `review-02.md` after
  reconciliation, naming the full digest. The parent verifies and acts; the reviewer neither contacts
  the author nor repairs.
- **Verification and stop:** check candidate/incumbent delta against disposition, then intent and
  omissions, shape, evidence and grounding, specificity/audience/relevance, and compression/prose.
  Each finding gives anchor, basis, byte-change requirement, and a block's upstream return. End with
  a line containing only `accept` when no byte change is required, otherwise `block`; absent or
  mismatched input requires `block`.

Recompute the digest after return. Acceptance applies only to matching unchanged bytes. Never mutate
a review record. A malformed, missing, or unavailable review is a worker-failure stop; it neither
authorizes promotion nor consumes semantic reconciliation. Every admitted run,
including a no-change candidate, needs final `accept`.

The run has one post-review reconciliation allowance. Consume it the first time candidate bytes
change after a well-formed completed review, whether that review returned `accept` or `block`.
Missing evidence returns to evidence then reconstruction; missing authority returns to the user then
disposition; a supported finding within settled claims returns to the author. Update upstream
artifacts and rerun grounding. Changed bytes get a new digest and different fresh reviewer. A second
`block`, or any further need to change candidate bytes after review, stops with records and workshop
retained. Metadata, whitespace, links, validator repair, and rebase are byte changes.

Clear every dependent completion:

| Change | Resume |
|---|---|
| Target identity, mode, collection, or type | Setup |
| Question, result, audience-bearing acceptance, evidence, or substantive new evidence | Reconstruction |
| Choice among reconstructed claims or authority for replacement, fold, retitle, merge, retirement, or artifact set | Disposition |
| Disposition only | Candidate |
| Candidate bytes | Fresh review |
| Live-target drift | Stop for abandon/rebase; authorized unchanged-evidence rebase returns to disposition |

## 7. Promote and close

Only the parent promotes. Require no blocker; grounding passed; candidate SHA-256 equals final
`accept`; destination-relative frontmatter, required sections, and links pass preflight; and the
live edit target still equals `original.md`, or the new target is absent. Never auto-overwrite or
auto-rebase. A digest is not a lock; compare and write in one parent-controlled sequence.

An edit retitle needs explicit authority and stays separate from substantive replacement. Dry-run
`commonplace-relocate-note <old-path> --to <final-path>`; require the destination absent and inspect
every reported move, Markdown rewrite, and ProperDocs change. Stop if the report includes
`original.md`, `candidate.md`, a frozen reconstruction/disposition, or an immutable review record.
Before `--apply`, require mutation and separate-commit authority plus a concrete authorized recovery
mechanism covering the move, destination absence, every reported Markdown file, and ProperDocs. If
that complete recovery path is unavailable, stop after the dry run and report the retitle blocker.

Re-run the exact command with `--apply`. The command is non-transactional. On error, stop, inventory
the actual state, execute only the preauthorized recovery, and verify every affected path before any
other edit. On success, require the old path absent and destination present; require the diff to
contain only the reported address-preserving mutations; re-hash candidate and accepting review
against their pre-apply hashes; and validate the relocated target, every changed Markdown file, and
the redirect map when ProperDocs changed. Any mismatch or invalid output stops and uses the recovery
path. Keep a successful address-only relocation pure and separate under repository commit policy.
Capture byte-exact `relocated-original.md` as the new drift and substantive rollback baseline;
before replacement require it unchanged. Candidate title, frontmatter, and links must already fit
the destination. The command does not change the title or frontmatter and does not preserve review
freshness.

Write only accepted candidate bytes, then run `commonplace-validate <target>`. On failure restore
`original.md`, or `relocated-original.md` after relocation, byte for byte; remove a new target.
Verify recovery, retain the workshop, and report failures. Never patch live bytes after acceptance;
repair and fresh review are allowed only while the post-review reconciliation allowance is unused.

After target validation, add only authorized source-to-target lineage. Prevalidate and preserve each
source, add its collection-authorized footer without a reverse edge merely for symmetry, and validate
each changed source. On failure restore all sources and target to their pre-promotion substantive
bytes and verify them. A prior address relocation remains separate; do not claim this reverses it.

Before cleanup assemble the final account: commission and decisions; replacement/fold/merge/
retirement/retitle choices; grounding results including `quotes added` text; final candidate and
review paths/digests; validation, promotion, relocation, lineage, and recovery; removed or retained
paths; and handoffs. Extra artifacts or sibling changes converge only by explicit decline, user
acceptance, or separate completion; never launch them automatically. A composition mismatch blocks
promotion. `cp-skill-connect` is only an optional suggestion.

Remove only the exact workshop and index line after target and lineage validation, a complete closing
account, no unexecuted authorized decision, and no retention reason. Retain blocked, failed,
inspection, and experiment runs; report cleanup and pending index work.
