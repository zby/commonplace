# Analysis collection split implementation result

## State

2026-10-04: phase 1 is implemented. Phase 2 has not started; the plan requires
a return to the operator here. No regeneration is commissioned.
The operator authorized revising ADR 095 alongside ADR 099 in the implementation
conversation. The question explicitly named ADR 095's separate published review
pin, proposed the accepted overview as public entry point while keeping manifest
and member hash checks, and received the answer: "Revise ADR 095 too
(recommended)". This records conversation authorization; the repository alone
does not independently authenticate it.

## Preflight

The initial tracked worktree was clean. Three local workflow runs exist:
`AAS-2026-10-02-dynamic-cheatsheet-01` and
`AAS-2026-10-03-dynamic-cheatsheet-02` have complete run states.
`AAS-2026-10-03-dynamic-cheatsheet-01` has a running run state but its workflow
is stopped after a fetch failure. No old run is resumed or repaired here.

Before mutation, the old reports tree contained 218 files. Its aggregate
SHA-256 was `d9b45e24be4baa2ab97c2672bdabcd208b33fa8d162c47ca1cc6216168fed676`.
The digest uses paths relative to `kb/agentic-systems/reports/`, ordered by
Python `Path` comparison (component order, not POSIX-string order). It includes
ignored local state and excludes only the newly added root validation marker.
For each file it hashes the relative POSIX path's UTF-8 byte length as eight
big-endian bytes, those path bytes, then the raw 32-byte file SHA-256 digest.
This exact recipe reproduces the preflight count and digest:

```bash
python3 - <<'PYTHON'
import hashlib
from pathlib import Path

root = Path("kb/agentic-systems/reports")
files = sorted(
    path for path in root.rglob("*")
    if path.is_file() and path != root / ".commonplace-validation-ignore"
)
aggregate = hashlib.sha256()
for path in files:
    relative = path.relative_to(root).as_posix().encode("utf-8")
    aggregate.update(len(relative).to_bytes(8, "big"))
    aggregate.update(relative)
    aggregate.update(hashlib.sha256(path.read_bytes()).digest())
print(len(files), aggregate.hexdigest())
assert len(files) == 218
assert aggregate.hexdigest() == (
    "d9b45e24be4baa2ab97c2672bdabcd208b33fa8d162c47ca1cc6216168fed676"
)
PYTHON
```

An independent recheck on 2026-10-04 reproduced it. Sorting POSIX strings instead
produces `fc8ede1eaaba0368c100256ebd17ddbc2121643366e6d82eae0dac9cc97fa74d`
over the same files. The original prose did not distinguish these orders.

## Consumer inventory and change packet

[Itemized searches](./evidence/consumer-inventory.json) include ignored and
hidden local state. They exclude Git internals, the virtual environment,
third-party source clones and site build output. Symlink targets were inspected
separately. Counts are matching lines, not assertions of semantic coverage.

| Search | Matching lines | Files |
|---|---:|---:|
| `agentic-systems/reports` | 902 | 134 |
| `agentic-systems/types` | 378 | 117 |
| `agentic-systems/instructions` | 473 | 85 |
| `generated-review` | 70 | 32 |
| `analysis-artifact-sha256` | 25 | 17 |
| `retained_artifact_path` or `retained_overview_path` | 19 | 4 |
| Shared analysis contract names | 225 | 53 |

Authoritative declarations: the workshop plan and designs; collection-local
contracts and schemas; runtime path constants. The new ADR revises ADR 099
and the public review pin clause of ADR 095. Ordinary type eligibility,
packet dependencies, current-set enumeration, publication checks and site
filters must enforce the declared scope without resolver aliases.

| Consumer class | Disposition |
|---|---|
| Workflow, analysis completion, finalize and publication emitters | Update paths, packet inputs, public entry point and publication transaction. |
| Set loader, validators and schemas | Relocate local identities; validate current directory/source identity; preserve exact member hashes. |
| Matrix reader and matrix scripts | Enumerate current retained sets directly through the shared library function. |
| Analysis method and shared contracts | Relocate; supply the small collection contract and sufficient operative vocabulary. |
| Landscape synthesis, taxonomy refresh and transfer scan | Update their entry points; comparison operations stay in agentic-systems. |
| Collection contracts and local type prose | Split ownership; keep publication and maintenance instructions out of analyst packets. |
| Root doctrine, install reference and skill projections | Update method paths and both analyse-agentic-system symlink targets. |
| Command and validation references, scripts README and analyst trial | Update runtime paths, publication behavior and packet contract coverage. |
| Site hooks, site configuration and redirects | Generate current analyses from the shared enumerator; exclude state and archives; publish retained members. |
| Unit tests, document composition tests, site boundary tests and build tests | Update identities and check the new interfaces and boundaries. |
| Historical reports, old run state and committed landscape evidence | Preserve their bytes and pins; exclude old reports from current validation and comparison. |
| Hand-authored reviews | Preserve paths and content; regeneration is separately commissioned. |
| The sole generated review, Dynamic Cheatsheet | Retire the old pin when its member types move. |

Byte pins: no retained output is migrated or repinned. Old run-state pins,
manifest member pins, the generated review pin and historical synthesis hashes
refer to producing versions; removing the generated review retires its consumer.
New acceptance still pins the exact output manifest and every member.

Spellings: searches cover repository paths, collection-relative type identities,
shared contract basenames, generated-review metadata and retained-path helper
names. Relocation dry runs cover relative Markdown links. Schema constants,
Python strings, shell examples and method-change guards need explicit updates.

Generated/projected forms: both skill projections now target the relocated
method. The site hook is `src/commonplace/docs/properdocs_hooks.py`, not a
root-level file. The library build test asserts exclusion of collection-owned
analysis. Generic installation remains generic; no research collection is
added to the shipped library. Fresh and existing-project probes pass; their command outputs are retained
in [the init probe](./evidence/init-probe.json).

Diagnostic promises and acceptance probes: the plan requires rejection of
wrong current directory names and duplicate source identities, byte-preserving
archive moves, publication failure recovery, packet dependencies, and public
site boundaries. These are exercised by deterministic tests.

## Implementation and choices

The operator resolved the ADR 095 conflict before live mutation. Publication
must continue to validate before replacing the incumbent, preserving ADR 083's
acceptance boundary. A publication I/O failure needs an exercised inverse.

The relocation command results were committed separately as `2499aed76`:
30 method, contract and type/schema files moved, with backlinks updated.
The remaining implementation supplies the small contract by absolute path in
every packet and dependency hash, including analyst-trial preparation. Method
maintenance and publication have coordinator/maintainer instructions outside
analyst packets. Generic installation continues to omit this research collection.

The public entry point is the accepted overview, copied unchanged alongside its
manifest and four other members. A source slug uses the normalized URL's final
path segment, falling back to the supplied system name, exactly as run opening
did. Publication refuses conflicting source identities and names. Replacement
moves the entire incumbent directory unchanged to its run-ID archive path.
Ordinary failures restore the directory and run state. An abrupt interruption
is uncertain and needs separately authorized recovery; it is not retried as if
nothing happened. No retained set or old run is migrated.

`current_analyses()` is the sole current-population enumerator for the site and
comparison reader. It validates complete sets and their member hashes, refuses
partial or misplaced sets and duplicate sources, and returns no legacy fallback.
The site list is generated in memory, with system, description, boundary, run,
date and evidence tier. It adds a navigation link at render time. Existing
historical reports remain publicly reachable so old evidence links keep working;
new run state and superseded archives are excluded from the site. Historical
reports are excluded from collection validation sweeps by an ignore marker.
Explicit selection of a historical subtree still asks the validator to inspect
it under today's contracts and can fail; no resolver alias hides that mismatch.

The existing `generated-review` run-state slot and publication CLI argument
names now identify the public overview. They do not write or read a second
review. The relocated generated-review type remains explicitly historical and
is absent from current packets and publication's method guard. The sole old
generated review was retired and its URL points to its historical overview.
The twelve hand-authored reviews remain unchanged.

The record contract now carries sufficient operative definitions of theory
builder, addressable theory, representational form and explanatory reach.
Their definition notes remain maintainer dependencies. Worker rules state the
supplied contracts' binding force. This is the plan's vocabulary deviation;
no other root rule is waived. Boundary receives only inputs-commit and run-date
in derived run metadata; destination and incumbent publication metadata stay
with the coordinator. Memory's publication-check mention was removed.

No analyst packet keeps a publication, comparison-writing or method-authoring
rule. The retained-output correction rule stays as a write boundary: an analyst
cannot turn a working edit into correction of accepted evidence. Under the
baseline's counting rules it still contributes A7, retained-set maintenance.
The memory profile and its independent record verification remain unchanged
until phase 2.

[ADR 102](../../reference/adr/102-separate-the-analysis-collection-and-publish-stable-system-paths.md)
amends ADR 099 and the operator-approved public review pin clause of ADR 095.
Its two literal TODO revisit conditions remain. Manifest and member hash checks,
source grounding and independent review remain acceptance gates.

## Measurements

[Itemized phase 1 measurements](./evidence/phase1-measurements.json) retain the
baseline obligation IDs, current mandatory-file bytes and hashes, rule-bearing
files, concern/reference/conflict IDs, flagged consumers and composition depths.
Counts follow the [baseline rules](./evidence/complexity-measurements.md#counting-rules).
These are semantic classifications of instructions, not an automated proof that
workers follow them. Input bytes exclude harness/root context and source/task
data, as the baseline does. The collection contract is 2,328 bytes.

| Role | Mandatory bytes before | After | Reduction |
|---|---:|---:|---:|
| boundary | 37,844 | 26,684 | 11,160 |
| runtime | 46,930 | 36,523 | 10,407 |
| memory | 61,720 | 51,278 | 10,442 |
| epistemic | 58,271 | 47,864 | 10,407 |
| reconcile | 80,981 | 70,622 | 10,359 |
| verify | 82,391 | 72,032 | 10,359 |
| synthesize | 51,451 | 40,555 | 10,896 |
| verify-synthesis | 51,041 | 40,145 | 10,896 |

Each pair below is before → after. Composition depth is the maximum number of
rule-bearing files combined for an obligation.

| Role | Concerns | References | Conflicts | Output obligations | Max depth |
|---|---:|---:|---:|---:|---:|
| boundary | 10 → 1 | 1 → 0 | 4 → 0 | 16 → 15 | 4 → 4 |
| runtime | 10 → 1 | 9 → 0 | 3 → 0 | 41 → 39 | 3 → 3 |
| memory | 10 → 1 | 9 → 0 | 4 → 1 | 62 → 60 | 4 → 4 |
| epistemic | 10 → 1 | 9 → 0 | 3 → 0 | 51 → 49 | 4 → 4 |
| reconcile | 10 → 1 | 5 → 0 | 5 → 1 | 20 → 19 | 5 → 4 |
| verify | 10 → 1 | 6 → 1 | 4 → 0 | 14 → 13 | 4 → 3 |
| synthesize | 10 → 1 | 11 → 2 | 4 → 0 | 18 → 16 | 5 → 3 |
| verify-synthesis | 10 → 1 | 6 → 1 | 4 → 0 | 11 → 10 | 5 → 4 |

Concerns, references and conflicts fall for every role. Memory keeps the
blocked-member versus problem-report conflict; reconciliation keeps the
conditional note-link versus within-set-link conflict. These are retained
findings, not fixes to analytical contracts. Verify still needs boundary-kind
semantics not supplied in its packet; synthesis roles still resolve the
self-improvement definition, and synthesis derives future sibling links.
The fourteen memory-profile obligations and the reconciliation/verification
profile checks remain for phase 2. Several maximum depths remain unchanged.
The first regenerated analysis is the outcome check, outside this commission.

## Verification and final inventory

The required full suite passes: 980 tests. Ruff passes. Targeted validation
passes for the new collection, old collection, comparison instructions,
transfer scan, command reference, amended ADRs, ADR 102 and redirect map.
The new collection has nine orphan notices for code-loaded job files; there
are no failures or warnings. Site tests exercise retained publication and
state/archive exclusion, and show that the generated list and matrix consume
the same population without committing a list file.

Publication tests cover first acceptance, replacement, archive collision,
incumbent drift, ordinary failures before and after the move and during copy,
partial-state recognition, duplicate identities and wrong source slugs.
A copy of the real Dynamic Cheatsheet retained set moved to an archive at the
same depth preserves all file hashes, manifest pins and relative Markdown
links. The original reports tree still has the same 218 files and aggregate
SHA-256 recorded above; its only addition is the permitted exclusion marker.
No model job was started.

[The final rescan](./evidence/consumer-rescan.json) retains each matching line. It excludes its own search-log JSON files to avoid
recursively recording evidence.
Remaining old paths identify frozen reports and local stopped run state,
historical workshop evidence, amended ADR history, redirect origins and the
explicit old-corpus read prohibition. Comparison and landscape procedures stay
in the old collection by design. Active runtime paths, schemas, packet inputs,
CLI examples and skill projections use the new owner. Generated-review spellings
remain for the public-overview slot/API names and the historical type, not a
second projection. The consumer dispositions above are complete for phase 1.
Fresh init validates; repeated init and pointer checks pass; existing user
content with historical research paths survives unchanged. No research method
is installed in consuming projects.

The tests questioned in the operator's review are:

- `test_comparison_population_must_select_one_review_per_source` in
  `tests/commonplace/lib/test_agentic_analysis.py`: duplicates a current set
  under `twin` and requires the duplicate-source diagnostic from the comparison
  reader, which calls the shared current-set enumerator.
- `test_each_job_declares_the_contracts_it_writes_or_judges` in
  `tests/commonplace/lib/test_agentic_workflow.py`: covers all eight roles,
  requiring the resolved collection path in read-first and declared inputs.
- `test_invocations_resolve_each_jobs_inputs_and_round` in that file: checks
  absolute invocation paths and that every read-first file is a dependency,
  including correction/reconciliation variants.
- `test_analyst_trial_tracks_the_supplied_collection_contract`: checks all three
  analyst trials, including the contract's recorded hash.

The operator's review also identified deliberate limits already recorded above:
old reports remain published as historical evidence; hard interruptions require
separately authorized recovery; residual conflicts and references are not fixed
by the collection split. Phase 2 remains unstarted. After making the all-role dependency assertion
explicit, the nine targeted tests above pass; Ruff and result validation pass.

## Phase 2: separate profile job

Completed on 2026-10-04 after the operator's explicit phase 2 continuation.
The operator also approved amending ADR 093's carrier and author-role clauses;
[the ADR check](./phase2-adr-check.md) records the clause dispositions. ADR 083's
current state-path annotation was corrected without changing its policy.
ADR 093 keeps its analytical definitions, evidence and counting rules.
[ADR 103](../../reference/adr/103-classify-memory-profiles-after-record-verification.md)
records the implemented separation.

The [replay record](./replay/README.md) retains stripped inputs and their receipts,
initial and corrected candidates, independent reviews, read audits, twenty-axis
comparisons and model provenance. Four workers ran exactly `gpt-6-luna`, confirmed
from their own session turn contexts, including the correction and recheck turns.
Both candidates matched all twenty retained assessments and value sets initially.
Three per-value strengths were corrected from afforded to wired using existing
records. An independent verifier's proposed inferred-judgment signal was disputed
and then cleared on independent recheck: generation of a new view was not evidence
of judgment selecting retained parts for delivery. Final values, coverage and
per-value bases all match. No missing recorded fact weakened an axis; all source
read counts are zero. Both final reviews have no blockers. The replay gate passed
before live type or workflow edits.

### Implementation and choices

- `profile` and `verify-profile` run after record verification closes and before
  synthesis. One correction changes only the profile; persistent blockers stop
  before synthesis or publication. The overview keeps all three independent
  verification accounts separately.
- `memory-profile.md` is the sixth required member of complete sets. Code copies
  its accepted bytes unchanged and pins them in the manifest. Blocked and
  out-of-scope sets remain overview-only. Source and boundary identity, all
  member hashes and publication/archive safeguards remain enforced.
- The memory type/job lose the mapping, axis definitions, Comparison rationale,
  profile/prose agreement and profile-driven local annotation rule. They retain
  every descriptive record and annotation field, write-side/read-back tracing
  and evidence rule. Memory describes those mechanisms in source-native terms.
  Reconciliation and record verification lose classification checks and
  profile-only return reasons.
- Profile validation resolves references against canonical declarations in the
  supporting record members and overview/boundary. It rejects profile declarations,
  annotations, source quotations and unresolved references. A worker candidate
  resolves against its run's already accepted `output/` records; a retained profile
  resolves against sibling members. An isolated profile cannot validate support.
  Analytical warrant stays with the independent verifier.
- Matrix and comparison procedures read the new member without a fallback. CSV
  columns and counting semantics stay unchanged. Publication's method guard pins
  the new jobs, type and schema. Site rules publish the current retained profile
  and exclude it from run state and archive publication.
- Workshop drafts were used for replay before promotion, a small deviation from
  drafting directly in the collection, so an untested type did not become live.
  Initial replay artifacts remain separate from adopted contracts. Source-read
  audit entries belong in Comparison rationale or Profile verification rather
  than creating another member or workflow stage.

The [consumer inventory](./evidence/phase2-consumer-inventory.json) and [final
rescan](./evidence/phase2-consumer-inventory-final.json) cover runtime readers, types/schemas, jobs, comparison procedures and
landing, command/validation references, scripts, tests, site rules and method
pins. Historical ADR 096/098 passages describe their earlier single-file/five-member
layouts; their identity and independent-review rules remain intact. Current
carriers are specified by ADR 102/103. Frozen historical reports remain consumers
of their original contracts, outside current validation and comparison.

### Phase 2 measurements

[Itemized measurements](./evidence/phase2-measurements.json) retain the original
baseline and phase 1 summaries, current mandatory-file byte/hash receipts,
removed obligation IDs and the units behind all five counts. Mandatory input
excludes root/harness context, task data and optional source reads.

| Role | Phase 1 bytes | Phase 2 bytes | Output obligations | Other-activity concerns | Unresolved references | Conflicts | Maximum composition depth |
|---|---:|---:|---:|---:|---:|---:|---:|
| memory | 51278 | 41451 | 60 → 46 | 1 | 0 | 1 | 4 → 4 |
| reconcile | 70622 | 60343 | 19 → 18 | 1 | 0 | 1 | 4 → 3 |
| verify | 72032 | 61811 | 13 → 12 | 1 | 1 | 0 | 3 → 3 |
| profile | — | 43983 | — → 23 | 1 | 0 | 0 | — → 3 |
| verify-profile | — | 43529 | — → 8 | 1 | 0 | 0 | — → 3 |

Memory loses fourteen comparison obligations and 9,827 mandatory bytes;
reconciliation loses one obligation and 10,279 bytes, and record verification
loses one and 10,221 bytes. Obligations composing more than two files fall from
4 to 3, 7 to 6 and 3 to 2 respectively. The new classifier has 23 obligations
and verifier 8, at maximum depth 3. Reconciliation's maximum falls from 4 to 3.
Concerns, unresolved references and conflicts do not fall further in phase 2:
the retained-output correction concern stays in every packet, memory retains
its blocked-report conflict, reconciliation its conditional link conflict, and
record verification its boundary-definition reference. Separation reduces each
old role's classification work; the total workflow gains two jobs. This is not
proof of improved worker adherence or analytical outcomes.

### Verification

- `uv run pytest -q`: 987 passed. Added checks cover profile-only correction,
  persistent blockers stopping before synthesis/publication, refusal of self-created
  support, all ten packets' absolute collection dependency, and site visibility
  for the new member. Existing publication, hash, identity and archive tests pass.
- `uv run ruff check .` passes. Relevant deterministic validation passes with
  zero failures and warnings for the collection, changed comparison/reference
  contracts, ADRs and redirect map; only orphan information remains.
- Collection-scoped validation of `kb/agentic-systems/` excludes old reports and
  passes. An explicit validation request for the old reports directory bypasses
  collection exclusions and reports twelve missing historical-type failures;
  this is the existing marker's documented explicit-target behavior. No historical
  evidence was altered to make that explicit check pass.
- The 218-file historical reports digest is still
  `d9b45e24be4baa2ab97c2672bdabcd208b33fa8d162c47ca1cc6216168fed676`, using the
  runnable recipe above. No retained set, archive or stopped run was migrated,
  retyped, repinned or resumed.

## Remaining work

Both implementation phases are complete. Regeneration and the first live outcome
check need their own commission. The replay used records authored with the axes
in view and two sets from one source; it does not establish sufficiency of future
source-native records. Old reports remain historical published evidence. Hard
publication interruptions still require separately authorized recovery. The Sol
follow-up plan was not changed. An unrelated `reliability/` workshop directory
appeared during execution and was left outside this work's commit.
