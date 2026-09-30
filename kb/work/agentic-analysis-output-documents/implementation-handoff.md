# Implementation handoff: commits 3 to 7 of the transition

Worker packet for step 3 of the [workshop](./README.md), written
2026-09-28. Purpose: make the producer, the validators and the consumers
read and write the member set instead of the single result, so that the
refresh batch prepared in `kb/work/agentic-memory-refresh/batch-01-handoff.md`
can run. The [transition plan](./transition-plan.md) fixes what changes;
the [consumer inventory](./consumer-inventory-20260928.md) gives file and
line for every reader; the type specs landed in commit `9fdde307` and the
records set mode in `65f5996b`. Read those three documents and the five
type specs before writing code.

## Result and acceptance

The result is the working tree at a commit where:

- the run state pins `overview` instead of `result`; the overview's
  `members` manifest pins the other three members; the review pins
  `analysis-overview` and `analysis-overview-sha256`;
- run-state verification checks the manifest, identity across members,
  source and quote anchors on every member and the review, the set-wide
  records check (`set_record_errors`), the memory member's `report-status`
  and `finalized-from`, and the finalization integrity described in the
  plan: the memory member minus its `## Amendments` section equals the
  local `memory-report.md` with the overview's Reconciliation mapping
  table applied by exact-token replacement and seeded re-declarations
  rewritten to `On <ID>` headings;
- publication validates, retains and backs up the four members and writes
  the review with the overview pin; the reserved candidate names include
  the member names; incumbent inspection accepts an overview-pinned
  incumbent and no other kind;
- the matrix loader, the three scripts and the landscape bundle read the
  overview, verify the manifest, take the profile from the memory member
  and validate each member; the CSV columns become `overview_file` and
  `overview_sha256`;
- init stops rewriting type lines inside `kb/reports/retained/agentic-system-analysis/`
  and its archive sibling, treating retained analysis directories as frozen
  bytes, and its repin regex is removed with them;
- the analysis skill's steps 1, 7, 8 and 10, the memory instruction, the
  epistemic instruction, the run-state type, the collection contract, the
  comparisons README, the transfer-scan and landscape-synthesis skills name
  the members and say which holds what;
- the single-file result type, its schema and its docs test are deleted,
  with a redirect from `types/agentic-system-analysis-result.md` to the
  overview type added to the redirect map by editing nothing but the
  worker's own commit's files (see coordination below);
- `uv run pytest` passes in full, `uv run ruff check .` is clean, and
  `commonplace-validate` passes on every KB file the worker changed.

Acceptance is the full test suite plus the checks above; the trial in
step 4 is not part of this packet.

## Order and commits

Land the work as separate commits in this order, each with its tests, each
message in the repository's commit style with the trailer
`Workshop: kb/work/agentic-analysis-output-documents`:

3. Run-state schema, parsing and dataclass: the `overview` pin.
4. Run-state verification: manifest, identity, anchors on every member,
   finalization integrity, set-wide records. Rebuild the test fixtures
   around a four-member set here; the fixture set is the reference
   instance of the contracts.
5. Publication: bundle check, prepare, publish, incumbents, review pin,
   reserved names, final state.
6. Matrix loader, scripts, landscape bundle, init.
7. Skill, instructions, run-state type prose, collection contract,
   comparisons README, downstream skills; retire the result type.

The suite may be red between commits 3 and 4 if the fixture rebuild
cannot be split; say so in commit 4's message. It must be green after
commit 4 and after every later commit.

## Fixed choices

- No compatibility code: no reader accepts the single-file result once
  its consumer moves. Mark nothing `BACKCOMPAT`.
- Member file names are `overview.md`, `runtime.md`, `memory.md`,
  `epistemic.md`, in the run directory and the retained directory.
- The run state's key is `overview`; `$defs.output` is reused for it.
- The review's pin fields are `analysis-overview` and
  `analysis-overview-sha256`; the review type is
  `agentic-systems/types/generated-review.md`.
- The memory member is authored by the coordinator; the code verifies the
  derivation and never generates it. The mapping table grammar is the
  overview type's: `specialist proposal | canonical record | disposition`.
- Finalization integrity compares whitespace-normalized text.
- The quote minimum (at least one attributed quote) applies to the set,
  checked in run-state verification, not to each member's type rule.
- Retained analysis directories are frozen bytes for init.

## Left to the worker

The internal shape of the verification code, how the fixture set is
built, where helper functions live, the exact wording of skill steps
provided they point at the types for content, and any refactor the tests
force. Where the plan and the inventory leave a detail open, choose from
the code and say what was chosen in the commit message.

## Write scope and coordination

Owned: `src/commonplace/**`, `tests/**`, `scripts/build_systems_matrix.py`,
`scripts/render_systems_table.py`, `scripts/analyze_matrix.py`,
`scripts/bundle_agentic_landscape.py`, `kb/types/agentic-system-analysis-run-state.md`
and its schema, `kb/types/agentic-system-analysis-result.md` and its
schema (deleted), `kb/types/README.md`, the five type specs where a test
forces a wording fix, `kb/instructions/analyse-agentic-system/SKILL.md`,
`kb/instructions/analyse-agentic-system/jobs/memory.md`,
`kb/instructions/analyse-agentic-system/jobs/epistemic.md`,
`kb/instructions/scan-agentic-system-transfer/SKILL.md`,
`kb/instructions/synthesize-agent-memory-landscape/SKILL.md`,
`kb/agentic-systems/COLLECTION.md`, `kb/agentic-systems/comparisons/README.md`.

Not owned, do not touch: `properdocs.yml` (the parent adds the result
type's redirect and the member publication patterns), everything under
`kb/agentic-systems/reviews/` and `kb/agentic-systems/reviews-archive/`,
`kb/reports/retained/**`, `kb/agentic-systems/comparisons/*.csv` and
`*.md` other than the README, `kb/work/**`. A relocation of the review
corpus is running in the working tree while this packet executes and
modifies files in those paths; stage only owned files, by explicit path,
never with `git add -A`.

Stop and report instead of guessing when: a test pins behaviour the plan
contradicts and the fix is not obvious; the finalization integrity check
cannot be made to pass on the fixture without changing the contract; or
a consumer outside the owned scope must change for the suite to pass.

## Return

Report per commit: hash, what changed, what was chosen where the plan was
open, and test counts. Report every place a type spec had to be corrected
and every open issue for the trial in step 4.

## Second packet (2026-09-28): finish the transition on the approved plan

Commits 3, 4 and the init part of 6 landed (`6f0c5e7b`, `7ae02a4e`,
`4009cb08`); the validator-extension commit was reverted (`597055b5`)
because that change is planned in `kb/work/directory-artifacts/` first.
This packet finishes the transition on the plan's original layering, with
set checks in run-state verification, plus the operator's simplification
recorded in the plan under "Committed inputs replace the bundle". The
first packet's fixed choices, write scope and stop conditions stand,
with these changes: `properdocs.yml` and
`tests/commonplace/docs/test_site_publication_boundaries.py` are now in
the worker's scope, and the set rule, directory-as-artifact validation and
consumers-call-validate items are out of scope.

Deliver, as separate commits in this order:

A. **Committed inputs.** Add `inputs-commit` (required, 40-hex) to the
   overview type spec, its schema and the fixtures; publication's
   inspect-destination, prepare and publish require a clean worktree as
   the plan defines it and `inputs-commit` equal to HEAD, with a clear
   error naming the offending paths; delete the incumbent dirty-tree
   receipt branch; delete `scripts/bundle_agentic_landscape.py`,
   `tests/commonplace/lib/test_landscape_bundle.py`, and the bundle's
   entry in `kb/reference/commands.md` and `kb/agentic-systems/comparisons/README.md`.
   Tests must not depend on the test repository being a real clean git
   worktree in a way that makes them flaky: build the fixture repository
   with an initial commit of its inputs.
B. **Instructions and contracts.** The analysis skill's steps 1, 7, 8 and
   10 write and name the four members, record `inputs-commit` at step 1,
   and state the clean-worktree requirement; the memory and epistemic
   instructions, the run-state type prose, `kb/agentic-systems/COLLECTION.md`,
   the comparisons README, the transfer-scan and landscape-synthesis skills
   name the members and say which holds what; the landscape-synthesis
   skill records the inputs commit instead of a bundle. The memory type's
   quote-minimum sentence says the minimum is enforced on the set.
C. **Retire the result type.** Delete `kb/types/agentic-system-analysis-result.md`,
   its schema and `tests/commonplace/docs/test_agentic_system_analysis_result_type.py`;
   update `tests/commonplace/docs/test_agentic_system_instruction_composition.py`
   to read the overview and runtime types; fix the links to the result type
   in ADRs 087, 088 and 093, `kb/reference/commands.md`, and the two
   instructions and one proposal that link it, pointing at the overview
   type; add the redirect `types/agentic-system-analysis-result.md` to
   `types/agentic-system-analysis-overview.md` in `properdocs.yml`;
   replace the site's `result.md` publication pattern with the four member
   names and add the archive's `result.md` pattern; update the site test.

Green suite and clean `ruff check src tests scripts` after each commit.
Report per commit as before, plus the exact clean-worktree rule you
implemented and every file whose link to the result type you changed.
