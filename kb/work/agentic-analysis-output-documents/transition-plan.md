# Transition plan: from one result to the member set

Step 3 of the [workshop](./README.md). Built on the
[consumer inventory](./consumer-inventory-20260928.md), the confirmed
[partition candidate](./partition-candidate.md) and the
[draft contracts](./contracts/README.md). It fixes what changes in the
producer, the validators, the consumers and the tests, the order of the
work, and the one decision that is the operator's.

The later [directory-artifact deployment](#directory-artifact-deployment-implemented-2026-09-28)
is a separate workflow integration after the generic feature is available.
It replaces this transition's output layout and overview pin when adopted.

## Historical results: archive, then rerun

Only three of the forty-one generated reviews load under today's contract:
the three 2026-09-27 pilots. The other thirty-eight fail validation on the
pre-ADR-093 profile shape, so the default matrix build already raises and
the committed comparison CSV cannot be regenerated. Historical results
are already retained bytes rather than loadable inputs.

The operator's direction (2026-09-28): move the retained corpus into an
archive so that the retained directory and the public reviews hold only
data produced under the current method, and rerun the analyses. No
compatibility code and no migration of old results. The archive keeps
the exact records for citation; the corpus refresh regenerates each
review as a fresh run under the new producer.

Proposed move list, held for approval before any file moves:

| What | From | To | Count | Notes |
|---|---:|---|---:|---|
| Retained single-file results | `kb/reports/retained/agentic-system-analysis/` | `kb/reports/retained/agentic-system-analysis-archive/` | 60 run directories plus the validation-ignore file | stays under `retained/`, so the retention contract is unchanged; a README states the retired type and that no loader reads them; the source directory is left empty for the new sets |
| Generated reviews | `kb/agentic-systems/reviews/` | `kb/agentic-systems/reviews-archive/` | 41 files | the 12 hand-authored reviews stay; each archived review's `analysis-result` pin and its body links are rewritten to the archive path, hashes unchanged, so every pinned pair stays verifiable; a README says these are superseded projections awaiting regeneration |
| Generated comparison outputs | `kb/agentic-systems/comparisons/` | deleted | `memory-systems.csv`, `memory-systems-table.md` | derived from archived inputs and already unregenerable; git history keeps them; the comparisons README says outputs return with the reruns |
| Site config | `properdocs.yml` | | | publish the archive's results as today's exception does, so archived reviews still resolve their links; the archived reviews directory is published under its own path |

Mechanics: `commonplace-relocate-directory` moves the results directory and
rewrites the 81 body links in reviews and the links in workshop and
reference documents. The pin fields are not links and are rewritten by a
scripted pass with hashes rechecked afterwards. The reviews move one by
one with `commonplace-relocate-note`, which rewrites the ten library
documents that cite a review and adds a redirect per file. When a rerun
republishes a review at its original path, that redirect must be removed;
publication gains that step, or the redirects are dropped in one cleanup
after the refresh. Relocation commits are pure: the moves land alone,
then the README and config edits.

Sequence: archive first, since nothing loads the corpus today except the
three pilots, which are rerun in step 4; then the eight implementation
commits; then the reruns under the corpus-refresh workshop.

## Producer changes

**Run state.** The `result` mapping becomes `overview`, pinning
`<run-id>/overview.md`. The run state pins nothing else; the overview's
manifest pins the members. Schema, `_output_identity`, the expected-path
check, the state dataclass, `_render_final_state` and the receipt
comparison follow. The reserved candidate names gain `overview.md`,
`runtime.md`, `memory.md`, `epistemic.md`.

**Coordinator outputs.** The skill's step 7 writes four members instead
of one result. The overview's manifest is written last, after the other
three are final, since it carries their hashes. `memory.md` is authored
by the coordinator as the local report with the Reconciliation mapping
applied by exact-token replacement, seeded re-declarations turned into
`On <ID>` annotations, and an `## Amendments` section appended. No new
command: finalization is authored, and its integrity is verified.

**Finalization integrity check**, in run-state verification. Read the
local `memory-report.md`, apply the mapping table from the overview's
Reconciliation and the re-declaration rewrite, and require the result to
equal `memory.md` up to its `## Amendments` section and its
`finalized-from` field; require `finalized-from` to equal the local
report's hash. This replaces the current memory-report projection lines
in the result body and makes the derivation checkable rather than
trusted.

**Set verification**, in run-state verification and publication. Verify
the manifest (existence, hash, type of each member); verify identity
fields across members against the overview; run source and quote anchor
resolution on every member and the review; build the declaration union
across members and fail on a duplicate or an unresolved reference in any
member or in the profile; require the memory member's `report-status`
to be `complete`; require at least one attributed quote across the set.

**Publication.** `_check_bundle` reads the disposition from the overview
and the profile from `memory.md`; prepare validates every member as its
retained path; publish retains the four members, backs up the incumbent
set under `incumbent-<member>.md`, and writes the review with
`analysis-overview` and `analysis-overview-sha256`.

**Site.** `properdocs.yml` publishes the four member names instead of
`result.md`.

## Revised layering (2026-09-28, during implementation)

The operator reviewed the size of the analysis code while commits 3 to 7
were in progress: about 3,700 lines of library, command and script code
and 3,200 lines of tests exist to produce, verify, publish and compare one
document kind, a fifth of the package. Much of it re-implements checks
that a schema states or that another module already performs. The plan
above ports that shape to the set; the revised layering below replaces
its "set verification" and "validator changes" paragraphs, and the worker
was redirected to it mid-flight.

1. **Schema**: one document's structure. Each member's schema, landed in
   commit `9fdde307`, is the only place single-document structure is
   checked. Code re-checks nothing a schema states.
2. **Set rule**: a validator type rule on the overview type. Validating an
   overview dereferences its manifest (existence, hash, declared type of
   each member), validates each member by its schema, checks identity
   agreement, runs the cross-member records check, validates the memory
   member's profile against the set's declarations, requires at least one
   attributed quote in the set, and for a complete overview requires the
   memory member complete and finalized. It needs nothing outside the
   retained directory, so it runs from a clean checkout.
3. **Directory as artifact**: `commonplace-validate <run-directory>`
   validates the set through its overview and reports it once; a
   collection sweep treats the directory as the unit. One recognition
   rule, not a manifest framework, since only the analysis set has an
   entry type.
4. **Source-bound checks** stay in run-state verification alone, because
   they need the run directory and the frozen checkout: anchor resolution
   for every member and the review, and the finalization integrity check
   against the local specialist report.
5. **Consumers call validate.** Publication validates the candidate
   overview as its retained path; the matrix loader validates the overview
   and reads identity from it and the profile from the memory member; the
   handoff renders from the run state. None re-implements hashing or
   identity comparison, and the code those calls make redundant is deleted
   rather than kept in parallel. Each commit names its removals.

Two follow-ups this exposed, both outside the transition: the verbatim
quote verifier for notes and the analysis quote-anchor verifier are two
implementations over one matcher and should converge; and the
`commonplace-verify-quotes` command is a reporting wrapper over the
validator's own check, kept only for its corpus-wide counts. Both belong
to the code review the operator asked for after the batch runs, together
with the question of which retained-set checks a reader actually relies
on. The decision recorded here is promoted to an ADR when the workshop
closes.

## Validator changes (superseded by the revised layering above)

**Types and schemas.** The five draft contracts move to `kb/types/`
(the review type to `kb/agentic-systems/types/`) with schemas: the
overview's eleven-minus-three sections and the `members` manifest; the
runtime report's sections; the memory report's sections plus
`finalized-from`; the epistemic report's six sections; the review's
frontmatter. The result type is retired with a redirect.

**Records.** `record_reference_errors` gains a set mode: declarations
are level-four headings under the six kind headings in any member,
annotation headings are neither declarations nor errors, `SRC-*`
declarations come from the overview's register, and references are
checked against the union. The single-file mode stays for a member
validated alone, checking only shorthand and the member's own
duplicates, since a member cannot know the set's declarations.
`validate_comparison` takes the union instead of one section.

**Type rules.** The evidence-and-references rule runs on the runtime,
memory and epistemic types; the quote-minimum rule applies to the set,
not to each member, since the epistemic member cites and does not quote.
The comparison rule runs on the memory type only.

## Consumer changes

**Matrix loader.** `retained_overview_path` replaces
`retained_result_path`; `load_results` verifies the review pin, opens
the overview, verifies the manifest, takes identity from the overview,
the register text from the overview, the profile from `memory.md`, and
validates each member. The CSV's `result_file` and `result_sha256`
columns become `overview_file` and `overview_sha256`. The three scripts
follow the loader; the table's link points at the overview.

**Landscape bundle.** Copies every member; `METHOD_INPUTS` lists the
member types and schemas.

**Init.** Retained analyses remain frozen bytes. The implementation
handoff selected preserving them and removing the repin path; there is no
open init-repin decision for directory-artifact deployment.

**Skills and contracts.** The transfer-scan and landscape-synthesis
skills name the overview and say which member holds what: boundary,
register, reconciliation, synthesis and limits in the overview; runtime
account and runtime records in the runtime report; memory findings and
profile in the memory report; epistemic blocks in the epistemic report.
The collection contract and the comparisons README promise the overview
pin and the retained set. The analysis skill's steps 1, 7, 8 and 10 name
the members.

## Order of work

Each item is one commit with its tests; the suite stays green throughout
except between items 6 and 7, which land together.

1. Types and schemas for the four members and the review; result type
   retired with a redirect. Composition and type tests updated.
2. Records set mode and comparison union, with unit tests on a small
   fixture set.
3. Run-state schema and parsing: the `overview` pin.
4. Run-state verification: manifest, identity, anchors on every member,
   finalization integrity, set-wide records.
5. Publication: bundle check, prepare, publish, incumbents, review pin.
6. Matrix loader, scripts, bundle, init repin.
7. Skill steps, memory instruction, epistemic instruction, collection
   contract, comparisons README, site config.
8. Step 4 trial on one target with source pin and functional scope fixed.

The one-off fixture script is deleted with item 1, since the draft
contracts supersede it.

## Committed inputs replace the bundle (2026-09-28, operator decision)

An analysis runs only from a clean worktree with every input committed,
and the landscape bundle is removed. The commit hash then identifies the
method and the inputs, which is what the bundle's manifest and method
hashes reproduced by hand.

- The overview gains a required `inputs-commit` field: the full commit
  whose tree supplied the run's method files, types and instructions. The
  coordinator writes HEAD there at step 1 and publication requires that it
  still equals HEAD.
- Publication requires that the inputs are committed, stated as two
  checks that let several runs publish side by side (operator relaxation,
  2026-09-28). First, the method paths are unchanged between
  `inputs-commit` and HEAD: `git diff --quiet <inputs-commit> HEAD --`
  over the method set, which is the package source, the analysis skill
  and its two instructions, the five member type specs with their
  schemas, and the run-state type. Unrelated commits during a batch,
  including sibling publications, do not invalidate a run. Second, the
  worktree is clean outside the workflow's own output locations: no
  modified or staged tracked file, and no untracked file under `kb/`,
  except under `kb/agentic-systems/reviews/` and
  `kb/reports/retained/agentic-system-analysis/`, where a sibling run's
  uncommitted publication may sit, and except ignored paths. The
  incumbent check's dirty-tree branch, which compared an incumbent with
  local changes against its publication receipt, is deleted; an incumbent
  is committed, or it is a sibling run's fresh publication of a different
  source, and either way the check compares bytes, not receipts.
- `scripts/bundle_agentic_landscape.py`, its tests and its command
  documentation are deleted. The landscape-synthesis skill records the
  commit its inputs came from instead of preparing a bundle. Retained
  bundles from earlier trials stay as historical records.

## Relaxed run-state verification (2026-09-28, superseded interim decision)

Before directory artifacts landed, run-state verification kept only the
cheap checks that had caught real errors. The deployment below supersedes
this temporary arrangement.

Kept: per-member schema validation; the pin chain (run state to overview,
manifest to members, review to overview); quote and source anchors on
every member and the review against the frozen source; the committed-inputs
checks; `run-id` agreement across members.

Dropped: the finalization derivation check (replaced by the `finalized-from`
hash as recorded provenance); cross-member record resolution and the
profile-against-union check (members keep their own syntax and duplicate
checks); the set-level quote minimum. The coordinator finalizes the memory
member by mapping IDs and appending amendments, with no exactness
constraint. Accepted cost: a dangling cross-member ID can reach
publication until the workshop lands.

## Directory-artifact deployment (implemented 2026-09-28)

[ADR 095](../../reference/adr/095-directory-artifacts-add-shared-set-validation.md) records the implemented model. Working reports now live in
`<run-id>/output/` beside `ARTIFACT.yaml`; run state and specialist inputs
remain outside. Run state and reviews pin the manifest, and all consumers
use shared artifact validation. The schema owns outcome-dependent
membership and required hashes. The method-version check includes the new
set spec and schema.

There are no active generated reviews or retained sets on main to retire.
The three overview-pinned batch-01 sets remain historical output on
`refresh-batch-01`; preserve those bytes and their recorded method revision.
Do not merge them into active discovery under the new contract. Rerun their
systems with new IDs under the current method before active publication.
The first publication on main therefore has no incumbent; its successors
use normal manifest-pinned replacement checks.

## Open items for the operator

- Approval of the move list above.
- Whether the trial target should be a harness-class system, to see the
  runtime member dominate for the first time.
