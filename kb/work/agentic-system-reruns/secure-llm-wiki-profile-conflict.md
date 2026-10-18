# Secure LLM Wiki profile conflict

## Operator conclusion

**Keep this run stopped. Recommend a separately corrected, tested method and a
fresh run lineage, not another unchanged retry.** The refused replacement
profile preserves the two requested semantic repairs. Its remaining comparison
validation failure is a real contract/implementation conflict: a classified
local learning negative does not count toward partially classified coverage.
The same implementation, contract, schema and relevant tests remain in the
current checkout. Preparing from current HEAD alone would repeat the conflict.

There is also a deliberate competing interpretation in the tests: they reject
partial coverage supported only by local negatives, and allow those negatives
inside an indeterminate aggregate. This is not an untested one-line accident.
Maintenance must explicitly resolve that disagreement. Recommended semantics:
count a supported local `"no"` as classified coverage, while continuing to exclude
it from the system-wide value union whenever coverage is incomplete. Neither a
fabricated `"yes"` nor a whole-system `"no"` is justified by this investigation.

**No genuinely supported old-run route resolving both requirements was found.**
Reverting the learning aggregate to indeterminate satisfies the frozen validator
but repeats the independent verifier's explicit refusal. Resetting or retrying
cannot reconcile those rules. Current reset support is not a frozen-run method
upgrade facility; the frozen engine has no corresponding reset module. Preserve
all old bytes and refusals. A successful fresh run would not accept the old
candidate retrospectively.

This report recommends maintenance and a later route decision. It performs no
fix and grants no execution, acquisition, state-transition or integration authority.
Deferral unchanged remains a valid lower-cost decision.

## Commission and evidence addresses

The commission is the user's bounded read-only investigation, informed by
[batch 21 source decisions, section 8](./batch-21-source-decisions.md#8-secure-llm-wiki)
and the exact Secure LLM-Wiki row in [batch-21.json](./batch-21.json), beginning
at line 1341. That row records `execution-authorized: false`, no publication,
no candidate-author jobs and no verification barriers. These scheduling fields
are not new execution permission or a certification of current writer idleness.

Path aliases below expand literally:

- `W` = `/home/zby/llm/commonplace/.commonplace/worktrees/secure-llm-wiki-c9867e0e576a`.
- `R` = `W/kb/agentic-system-analyses/state/AAS-2026-10-15-secure-llm-wiki-c9867e0e576a-01`.
- `V/<hash>` = `R/state/versions/<hash>`, the immutable content-addressed file,
  not the mutable artifact projection.
- Current paths are relative to `/home/zby/llm/commonplace`.

The recorded method revision is `a568c6dc489ad546374536b642c3889ce23149a8`.
Opening metadata `V/eceab92e64a2b6f28f2b49fd92e41602c459dfc890283c2ed734a0cf75047292`
confirms that `inputs-commit`. The source identity is
`https://github.com/nicobleh/secure-llm-wiki`; the candidate and pinned boundary
name `dfbc60e37487b61e9a5cbce1271a13576a776d51`. Opening metadata has
`source-revision: null`: do not confuse that allocation input with the subsequently
frozen reviewed boundary. This report does not inspect the target checkout.

### Exact-byte evidence register

SHA-256 values were calculated from local bytes unless explicitly described as
recorded. All 17 criterion-version blobs in judgment 000031 were hash-checked.

| Evidence path | SHA-256 |
|---|---|
| `R/run.json` | `2c27d2f01f8b4967c3e21e09a34679b1d9d3f84b5b97708005998d22c9d59df8` |
| `R/artifact/profile-verification.md` | `c8da5c9f27b6ed66e300f0509a90540949accae905e5740f0a76ccc936d62bb2` |
| `R/state/attempts/000030-memory-profile.json` | `9fca153dfbe87de77bf6daf00f17f9b56e15228f5315128e8bda49007393da2e` |
| `R/state/judgments/000031-check-memory-profile-0.json` | `bcea5ffd4f7392a5cbeb2b698fea22c5ab64ced9ca5282340e66e68f06728666` |
| Original profile, `V/9e8d073a24a49d829cc4574d7e6339b10ed479c248b10363eaa8642149809882` | Filename is its content hash |
| Refused replacement, `V/bbaaf083f353a34e288d1805626cd1bf3ced2b0defd5254d60c2189e05b3893d` | Filename is its content hash; independently recomputed |
| `W/kb/agentic-system-analyses/types/agentic-system-memory-profile.md` | `8921fd68da847aba91a449f81c8dd3b52d8bf5cb3242e2169f39bebc7f018758` |
| `W/kb/agentic-system-analyses/types/agentic-system-memory-profile.schema.yaml` | `4b0db3711d105b953c3f9734f8f188f65fbf26f512772dafc1079ef930a08f5f` |
| `W/src/commonplace/lib/systems_matrix.py` | `8701042ad1a42b4afbf2192779265c3150555b2ce9dbf5f28719e4d62c8f7ed5` |
| `W/tests/commonplace/comparison/test_systems_matrix.py` | `543f6c7c0a22b1e3abc90c32f183b16db1a0c89195e7c27a9b6eff7aa230eb0e` |
| `W/kb/agentic-system-analyses/instructions/analyse-agentic-system/plan.yaml` | `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd` |

The recorded `000031` **attempt** hash in the batch row is
`5aced0e13d74602274413e9a101cfdfc32cae748fb1ef9508a51a189172cf5e8`.
It is not the judgment hash above. The candidate/criterion version addresses
come from the judgment's basis, not guesses from artifact filenames.

## What was authored incorrectly, and what the replacement repairs

1. `R/state/judgments/000025-check-memory-profile-0.json` structurally accepted
   original profile `9e8d…9882`. Independent verification then refused those
   same bytes in `000027-apply-profile-verification-1.json`.
2. `R/artifact/profile-verification.md:24–29` identifies two coverage defects:
   the storage aggregate and embedding unit say `known` despite unresolved
   embedding Git membership; the learning aggregate says `not-determinable`
   despite a supported local negative and an unresolved external-caller unit.
   These are distinct defects. The storage defect is not explained away by
   the learning-validator conflict.
3. Comparing the exact original and replacement blobs shows changes to those
   three assessments and their explanatory notes/prose. Replacement lines
   11–76 make storage and the embedding unit partial, retaining wired file
   storage and the separately warranted repository findings. Lines 569–607
   make learning partial, retain the known shipped-route `"no"` with an absence
   record, and retain the separate `not-determinable` direct-caller unit.
   Lines 608–633 leave trace source indeterminate, with a locally inapplicable
   shipped-route unit and an unresolved external unit. The replacement does
   not manufacture a trace source or infer embedding Git membership.
4. `000029-check-memory-profile-0.json` refuses replacement `bbaaf…893d`.
   Attempt 000030 returns the same primary bytes; its `previous_outputs` and
   `outputs` agree for the profile (`:8–11,158–162`). Its problem field reports
   the validation conflict, not a transport failure or accepted completion.
   Judgment 000031 again refuses these bytes (`:37–46,313–317,352–356`).

The replacement therefore addresses the **specified** semantic blockers on
its face. This is not an independent certification of the target's substantive
classifications. The verifier has not independently accepted this replacement.

The latest judgment repeats the original semantic blockers as well as the new
structural diagnostic. That repetition does not prove the replacement still has
the old `known`/`not-determinable` labels. The correction machinery deliberately
carries blockers forward when structural validation fails
(`src/commonplace/artifactrun/checks.py:130–158`). Attempt 000030's two
`declined` answers, `V/2fc87c17563740767ab66add0c0051d674bbd731be2c2fac91e09e4756f011db`,
explain that the supplied baseline already has the requested repairs. The
unchanged-primary-output check permits reasoned `declined` answers; it rejects
unchanged bytes falsely labelled `corrected` (`checks.py:105–121`). No additional
correction-answer diagnostic is recorded in judgment 000031.

## Exact structural conflict

The frozen and current [profile type](../../agentic-system-analyses/types/agentic-system-memory-profile.md)
are byte-identical. Lines 61–83 distinguish complete classification, partial
classification and indeterminacy. Lines 85–93 explicitly allow local learning
`"no"` in a partial axis and forbid treating it as a system-wide negative.
The independent verifier applies that coverage interpretation.

The frozen and current [validator](../../../src/commonplace/lib/systems_matrix.py)
are also byte-identical:

- Lines 206–210 require a local `"no"` to belong to a `known` unit and cite an
  absence record, but exclude it from `positives`.
- Lines 218–225 separately detect unresolved units, then require nonempty
  `positives` for axis `partial`.
- This candidate has a valid bounded local negative, an unresolved unit, and
  no `"yes"`. Its accumulator is empty. Hence the exact diagnostic:
  `trace_learning: partial coverage needs positives and unresolved coverage`.
- Lines 226–227 allow that local negative inside an `uninspected` or
  `not-determinable` aggregate because it is also omitted from the guard for
  non-positive assessments. This explains why the original learning label
  passed deterministic checking and failed semantic verification.

The word “positive” is doing two incompatible jobs: **classified coverage**
(including a controlled negative) and **positive existence of learning**.
Counting a negative toward the former must not assert the latter.

The schema does not resolve this conflict. Its `$defs/unit` and `$defs/axis2`
permit the replacement's structure; it requires findings for known/partial
units, not a learning-`yes` witness for partial axes. Cross-unit aggregation is
owned by Python validation. The type's generic “needs positives” sentence is
ambiguous alone; its explicit local-negative paragraph and the verifier favor
classified coverage. However, current and frozen tests deliberately encode the
other reading:

- `tests/commonplace/comparison/test_systems_matrix.py:395–402`,
  `test_revision2_partial_axis_cannot_promote_only_local_negatives`, expects
  this exact rejection.
- Lines 405–418, `test_revision2_local_negative_survives_unresolved_axis_without_system_no`,
  permit indeterminate aggregates with local negatives.
- Lines 228–242 test `yes` plus local `no`, optionally with unresolved coverage.
  That case passes because `yes` fills the accumulator; it does not test this
  candidate's no-plus-unknown case.

Thus merely changing the candidate to match existing tests would not honor the
retained refusal. Merely changing code without updating the contradictory tests
and clarifying the contract would also leave an inconsistent method.

## Full comparison probe and its limits

A stdlib-only in-memory probe parsed the exact candidate's restricted YAML
subset (quoted scalars, integer version, empty lists, indented mappings/lists).
It asserted complete token consumption and unique mapping keys. No third-party
YAML/schema library or target code was imported. Selected pure functions and
constants were extracted by AST from frozen **Commonplace** code; module imports,
I/O functions and workflow handlers were not executed.

Support IDs were obtained from `#### ID` declarations under `Shared records` in
the exact judgment-pinned runtime, memory, epistemic and workflow blobs. The
record grammar and quote/fence exclusion came from the frozen record helpers
(`records.py:25–50,112–140,165–167`). This yielded 35 declarations, not IDs merely
mentioned in prose. Checks covered all ten axes, 36 units, 36 findings and 250
frontmatter citation occurrences.

Results:

| Probe | Result |
|---|---|
| Unmodified frozen `validate_comparison` | The recorded partial-learning diagnostic, exactly |
| In-memory diagnostic collector replacing every `raise ValueError` with an append, keeping predicates | Exactly one diagnostic across the complete comparison, the same one |
| All comparison keys, assessments, vocabulary, evidence bases, unit scopes/notes, citation resolution, nonempty/unique reference lists, local-negative warrant, absent/inapplicable rules and cross-axis applicability | No additional diagnostic |
| Supplementary schema-pattern, top-level field, description-length, required rationale heading and identity comparisons against pinned boundary/memory | Pass |
| Hypothetical excerpt counting the already validated local negative toward classified coverage; candidate unchanged | Full comparison function returns successfully |
| Projection of that hypothetical accepted comparison | Learning values `[]`, assessment `partial`, supported values empty, complete values `None`; local `"no"` stays in unit data |

The collector is a diagnostic probe, not the shipped validator: continuing after
an exception is safe here because this candidate's shapes are well formed.
The hypothetical alteration exists only in memory. It removes the local-negative
exception to accumulation, **not** the bounded-absence check or projection guard.
It establishes feasibility for these bytes, not a reviewed patch or full
regression result.

This is strong evidence of a single comparison-aggregation blocker, not a full
native artifact validation pass. No native candidate validation or source guard
was executed. The manual structural checks are not a general JSON Schema engine.
Full quotation/link semantics, reconciliation support, source integrity,
publication guards and independent semantic re-verification remain outside this
probe. In particular, broad factual certification of all 36 findings would
require the source analysis this commission excludes. The retained judgment
contains no other structural diagnostic, but that is not a guarantee that every
later gate would pass.

## Consumers and minimum separately commissioned maintenance

The maintenance goal is to distinguish classified coverage from system-wide
learning existence while preserving uncertainty and exact-byte verification.
The minimum plausible repair is narrow, but needs explicit semantic adoption:

1. Clarify in the profile type that a warranted known local `"no"` counts as
   classification for a partial learning inventory. No new axis value, schema
   version, representation kind or source evidence is needed for this example.
2. Separate coverage accumulation from positive system-value accumulation in
   `validate_comparison`. Keep known-unit/absence-record requirements. Under
   the recommended reading, an unresolved aggregate containing a classified
   local negative should require partial coverage rather than silently permit
   the original indeterminate label. Preserve the no-finding indeterminate case.
3. Retain `project_comparison:253–277`: it suppresses system `no` whenever
   learning coverage is not known, or `yes` exists, but preserves all unit data.
   Retain prerequisite checks at `:115–133,232–248`: partial learning must not
   make the whole trace-source axis inapplicable. This candidate's trace-source
   label should remain indeterminate, not be changed as part of this repair.
4. Reconcile the contradictory tests explicitly; do not just delete a failing
   assertion. Test the adopted coverage interpretation and unchanged union and
   applicability behavior through consumers.

Relevant consumers and regression obligations:

| Consumer/interface | Evidence and required regression |
|---|---|
| Producer/verifier contract delivery | Frozen `artifactrun/compact.py:329–339,359–400` supplies member/read types and criterion closures to derived checks; plan `:125–147` orders profile after report verification and synthesis after both verifications. Test that author, independent verifier and code check receive the same clarified criterion. |
| Candidate checking and correction answers | `artifactrun/handlers.py:156–203`, `checks.py:66–86,105–158`; `tests/commonplace/agentic_analysis/test_profile.py` tests identity, comparison revision, exact delivered baseline, stale blockers and refusal retention. Add a no-plus-unknown profile passing structural checking without claiming semantic verification acceptance. Preserve unchanged-output/declined-answer behavior. |
| Artifact validation | `lib/agentic_analysis/rules.py:322–328` calls `profile_member_comparison`, converting its first exception into an artifact finding. Test the exact candidate-shaped comparison and later axes, not only a tiny synthetic axis. |
| Matrix extraction/projection | `systems_matrix.py:280–286,311–363`; `test_systems_matrix.py:323–364` exercises loading/CSV. Add no-plus-unknown roundtrip: partial assessment, empty system union/evidence, retained local negative and unresolved unit, no input mutation. |
| Statistics | `systems_matrix.py:370–409` and `scripts/analyze_matrix.py:53–58` consume supported/complete values. Verify that this case contributes neither system learning absence nor a complete profile; a strong local witness must not upgrade unknown coverage. |
| Independent verdict application | `handlers.py:206–252` judges exact handed subject bytes, separately from the verdict's own validity. A structural pass must not clear old `verifies` refusal or reuse a verdict about the original profile. Existing `test_profile.py` covers this separation. |

Regression cases should include: no-plus-`not-determinable` and
no-plus-`uninspected`; yes/no/unknown; complete bounded no with inapplicable trace
source; unresolved-only without findings; a local no lacking an absence warrant;
a partially assessed local-negative unit; mixed yes/no in one unit; wrongly
inapplicable trace source with unresolved learning; partial embedding storage
with a wired file finding and unknown Git membership; and ordinary non-learning
partial axes. Retain the existing guards at
`test_systems_matrix.py:305–310,421–488`, revising only expectations that conflict
with the adopted coverage interpretation.

Under [test selection](../../../tests/README.md), future maintenance should run
`general/`, `comparison/`, and affected `agentic_analysis/` suites, including
relevant slow profile/verification tests; include `validation/` and `docs/` for
the clarified contract. Run broader coverage if impact proves uncertain and the
complete suite before a push. None of these suites was run in this investigation.
No dependency, packaging or general recovery-engine change is demonstrated as
necessary to solve this classification conflict.

## Recovery routes and preservation obligations

### Recommended: corrected method, fresh lineage

First commission and review method maintenance outside `W`, commit the consistent
method, and select that revision explicitly for a future run. Only after separate
execution permission should preparation/source reuse, acquisition requirements,
worker launch, publication or integration be considered. Preserve the exact
source identity and selected pin unless the operator separately changes them.
A fresh source-first run must not receive this report or old profile judgments
as source evidence. Retain the old lineage as refused, with this method-conflict
explanation; do not copy candidate bytes directly into a publication.

This route costs more analysis but respects frozen-method integrity. It does
not assume a new worktree already exists, that source copying is authorized, or
that a changed method automatically passes every gate.

### Old run: no conforming supported route established

The frozen plan and expansion explain the loop. `compact.py:342–356` pins candidate,
answers and exact answered refusal; changing answers can trigger the code check
even when the primary output is unchanged. Frozen `run.py:277–317` schedules by
changed inputs and avoids repeatedly spending a model attempt on the same
already answered refusal. Attempt 000030 changed answers, not the candidate;
000031 therefore checked again and reproduced the same conflict. No next action
is inferred from that historical scheduling behavior.

The frozen method's `artifactrun/` contains no `reset.py`. The current
`src/commonplace/artifactrun/reset.py:143–239` archives state and resets an active
dependency closure, with idle/uncertain-effect guards. It does not migrate
contracts or permit substituting newer code for a frozen method. Its tests
(`tests/commonplace/artifactrun/test_reset.py:14–96`) establish state-transition
and preservation behavior, not compatibility of this old run with a new method.

Frozen `artifactrun/worktree.py:178–205` binds commands to the run's own checkout.
Frozen `lib/agentic_analysis/publication.py:67–71` and
`guards.py:51–56,71–73` require the opened/prepared method commit, clean method
files and matching package at publication. The current matching guard files do
not remove those obligations. Editing `W`, changing its commit/preparation
metadata, borrowing current reset, or overriding the refusal is not a supported
resolution. Resetting an unchanged method would only renew the opportunity to
hit the same incompatible requirements.

An alternative old-run route would need separately demonstrated support for an
authorized method migration or a source-faithful classification that satisfies
both frozen requirements. Neither was found. Inventing a positive, discarding
the external unit, treating uncertainty as complete absence, or returning the
explicitly refused aggregate is not such a route. This is a bounded finding,
not proof that no future migration mechanism could ever be designed. Designing
one is a larger maintenance commission, not the minimum repair here.

## Scope and verification record

Only this report was authored. No worker prompts, handouts or logs were read;
no target checkout or target code was read, executed or imported. No acquisition,
installation, agent launch, native reset/judge/advance/validate-output/inspection,
state edit, new worktree, method/code/type/test/configuration change, integration,
staging or commit was performed. Probes used stdlib and memory only; no fixture
files were created. The parent owns concurrent batch-22 planning and all other
files. Initial unrelated worktree changes were left untouched.

Current HEAD observed: `f12f9a7467f4b01a5777bf8f65f109560b05e848`.
Frozen/current byte comparisons confirmed equality of the matrix implementation,
profile type/schema, matrix tests, compact expansion, handlers, method guards and
plan. Equality of those selected files does not claim equality of the whole
method or compatibility of every newer recovery interface.

Report-only `commonplace-validate kb/work/agentic-system-reruns/secure-llm-wiki-profile-conflict.md`
passed: one text file, zero failures and zero warnings. A whitespace check of
this new file against `/dev/null` passed. No pytest or native run validation was
performed. Broader graph discovery, if later wanted, belongs to a separately
commissioned `cp-skill-connect` pass; it is unnecessary for this route decision.
