# C10 follow-up: oh-my-pi session report

Checked on 2026-09-05 at the operator's request. This triages the
[producer's session report](../../messages/20260905T135445Z-codex-review-machinery-oh-my-pi-session-audit.md)
and applies the classification audit to its reported semantic concerns. It is
a diagnosis, not a corrected system analysis or a whole-result endorsement.

Two classification defects are established: inconsistent compaction scope and
an unsupported exclusion of compaction from trace learning. Identifier-based
push selection remains a mapping question. Canonical-ID drift and inspection
truncation are reported execution errors under existing instructions. The
publisher's lack of an independent integrated-result review is its current
coverage boundary, not a bypass of a required legacy gate.

## Evidence boundary and checks

Selected run: `AAS-2026-09-05-oh-my-pi-01`; source
`https://github.com/can1357/oh-my-pi`; revision
`be6cb8217cd4c1dafcc86793ae5d809ea4d7396a`; cutoff 2026-09-05;
`code-grounded`, with no target execution.

| Input | SHA-256 |
|---|---|
| [Public main review](../../agentic-systems/reviews/oh-my-pi.md) | `1aa5330d7b30b5e390db54b53f02832b55f518f10da3b7b6bf3a03d4eee22212` |
| [Retained exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-05-oh-my-pi-01/result.md) | `f088fbd407c7a8a9a964d88035e472adc7e23c419522b47c9e7903b877f1b0b7` |
| State-side exact result | `f088fbd407c7a8a9a964d88035e472adc7e23c419522b47c9e7903b877f1b0b7` |
| Complete run state | `fdc96622eb4dcee202acdd7c1c19895427a6496b21ce9eba4817c4df0ae7349c` |

The strict reader accepted this explicit population. Retained-result and
complete-state validation also passed without warnings. The audit read the full
result, including the profile, register, both lenses and reconciliation, and
the compact projection. The files are published locally but were still
untracked at the initial check; no clean-committed-checkout claim follows from
that check.

The five core method identities are unchanged from
[C10 acceptance](./c10-acceptance.md#selected-input-and-method-identities):
the audit instruction, producer skill, result type/schema and shared reader.
The representational-form and behavioral-authority definitions also match that
record. Additional material actually consulted has these identities:

| Method or explanatory input | SHA-256 |
|---|---|
| `kb/notes/rule-based-context-selection-needs-a-pre-existing-signal.md` | `73d8020044f8879f09628d8bf3c47b5e91af8147a8f62bc381b278cd798e1d30` |
| `src/commonplace/lib/agentic_publication.py` | `1bf6b05fb70123dcb2c14464b2474d8e5ec4354aba3e79cd6637870044d16dd1` |
| `src/commonplace/cli/agentic_analysis_publication.py` | `9054af6b1d4468dac923722eaa4190b318448f84266f741a21bd22b3e7d42bd7` |
| `kb/instructions/synthesize-agent-memory-landscape/SKILL.md` | `37f8bf9d8dc9357eb5e444416a6d993dc82be72c965476b2e38b35162e751c1b` |

Separate bounded source checks verified the report's cited compaction and
selection mechanisms, using commit-addressed reads after checking clone origin
and resolving the commit. These checks do not replace producer regeneration.
They covered `packages/agent/src/compaction/compaction.ts:1792-1873`,
`packages/coding-agent/src/session/session-context.ts:226-285,410-499`,
`packages/coding-agent/src/extensibility/skills.ts:345-474,499-538`, and
`packages/coding-agent/src/session/session-tools.ts:1266-1286` at that revision.
The provider payload's internal representation was not inspected.

Initial and final population, input and method identities matched. Temporary
check data is under `/tmp/commonplace-omp-audit-19hkzwld/`; this record preserves
the necessary identities without depending on that directory. Truncated output
also occurred during this triage and was reread in bounded ranges; the final
findings rely on delivered spans.

## Dispositions

### 1. Canonical-ID reassignment: execution error

The producer reports giving workers CLM-3 with one referent and assigning it
another in the final result. Reconciliation acknowledges splitting the seeds,
but says no **accepted** ID was reused. That qualification is not in the
producer's canonical-identity rule. Once a worker receives an ID as canonical,
later acceptance cannot retroactively make its old referent provisional.

The existing producer step 3 and result-type identity contract already require
one orchestrator-owned register and stable generic identity. This is primarily
an application failure. A short clarification would help: shared canonical IDs
retain their referents; split claims receive new IDs, and the combined record
is explicitly superseded. A provisional seed uses a local label.

The report is firsthand process evidence; no independent handoff transcript
was retained. The final-file splits are inspectable, but do not reconstruct the
handoff history or prove published misattribution. No new lifecycle ledger or
historical validation mechanism is justified by this check.

### 2. Truncated inspection: execution error

Producer step 2 already treats truncated output as non-evidence and requires a
narrow reread. The reported recurrence supports a budgeting problem, not a new
source-analysis requirement. Bound the selected files and ranges, and budget
the aggregate delivery from parallel reads. A small output cap merely discards
part of an oversized read. No particular false source claim was established
from this error, and no unavailable transcript was inferred.

### 3. Compaction scope/form: classification defect

The profile names durable session branch/compaction memory. Its known
`representational_form` set cites OBJ-2, which describes a **local** summary.
RTE-4 also includes external replay/archive material. The restart forcing case
and synthesis say that material returns to model context, while Lens scoping
narrows the comparison to local summaries. The named backend exclusions do not
explicitly resolve this compaction alternative.

The pinned implementation confirms the distinction: remote compaction uses a
display summary while durable history lives in separate `preserveData`;
reconstruction supplies provider replay and archive material to model context.
A summary string or JSON envelope does not establish the payload's operative
representation.

This violates the result type's requirement that a known set cover its declared
scope. The defect is the inconsistent boundary and unsupported completeness
claim; the payload's replacement form is **not determined**. A new producer run
must either include that part with supported classifications/uncertainty, or
state its exclusion consistently and distinguish it from the local object in
the route mapping. The audit cannot choose the producer's intended boundary or
hand-edit the published profile.

### 4a. Identifier-based push: mapping question remains

Removing `identifier` is not justified merely because a user can choose a
session or request a skill. RTE-3 reconstructs a branch using leaf/parent IDs,
then supplies selected history to a later model invocation. The pinned code
also uses kept-entry and replay-through IDs when rebuilding compacted context.
There are real identity-based selectors, not only names printed in a catalog.

However, the profile combines operator selection, automatic context assembly,
skill-name eligibility and requested full bodies. RTE-12's pinned name checks
establish enabled/disabled and shadowing behavior; they do not alone establish
task-specific memory relevance. A requested full skill is a distinct path.

The shared type says the signal axis covers push selection but does not fully
specify where to split a requested-session/automatic-context chain. The
[selection explanation](../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md)
allows upstream identity signals to feed push, so the branch-assembly reading
is defensible. The correction should name the trigger, selector input, selected
retained part and later consumer, and keep explicit requests separate. This is
a narrow method clarification and route-mapping issue; it is not an established
wrong token or a license to infer semantic retrieval.

### 4b. Compaction excluded from trace learning: classification defect

The learning-scope rationale explicitly excludes compaction as
retention/reshaping. No such exclusion appears in the current contract. OBJ-2,
RTE-4 and BAP-1 record model-generated history summaries, automatic threshold
triggers, durable retention and later contextual use. These meet the existing
architectural criterion of automatic trace-fed writes producing durable
behavior-shaping artifacts. Neither observed improvement nor ampliative
knowledge creation is required. Raw logging alone remains excluded.

The producer must assess this route's contribution to source, scope, timing
and distilled form under the same comparison boundary. Do not simply append
`per-task`: session identity alone does not establish the intended task horizon,
and local versus provider compaction must first be separated. Other extraction
and Auto-Learn routes still support `trace_learning: yes`; the defect concerns
the omitted route and completeness of the dependent assessments.

The existing method is sufficient to reject the stated exclusion. A small
worked distinction between raw logging, generated continuation summaries and
cross-task procedure extraction would reduce repeated application errors.

### 5. Publication and comparison scope: coverage limits

`prepare_publication` returns no review batch when there is no legacy
candidate; the CLI derives `semantic_review_required` from that batch. The
run correctly records `memory-review-required: false` for its enclosing runtime
boundary. No applicable legacy gate was bypassed. Producer step 7 still assigns
semantic verification to the orchestrator, and an unresolved failure should
block publication. Its successful completion here did not detect the two
classification defects.

The migrated reader accepts this row because hashes, identity and structure
are valid. This audit is not an automatic invalidation flag consumed by that
reader. Consumers should withhold the affected scope/form and complete
learning-profile claims until a replacement run resolves them.

C10 therefore has a real positive example of detecting semantic defects after
structural success. The immediate producer improvement is a focused scope and
route-to-axis check during step 7. The current C10 procedure consumes published
inputs, so it cannot simply be inserted before publication unchanged. An
independent integrated reviewer is a separate cost/coverage decision, relevant
when C14 revisits publication; this check does not add that gate.

The profile already carries scope, and the migrated reader preserves it.
Landscape synthesis already requires scope beside comparisons and comparable
scopes for change claims. Excluded alternatives are not absent. Those existing
conditions address the reported comparison risk, provided consumers apply
them; completeness within different scopes is not comparable coverage.

### 6. Repetition and unexecuted tests: economy and evidence limits

Repeated objects/routes across the register and overlays are visible, but
length alone does not prove invalidity. The producer already calls for sparse
lens overlays and prohibits concatenated lens reports. Prefer canonical-record
references and lens-specific judgments; preserve required coverage. No new
mandatory packet, ledger or output section follows.

The result explicitly records no dynamic check planned, lists considered
checks and bounds its claims to wiring. The skill permits this disposition.
It does not claim tests were impossible to run, so lack of a runnable-test
inventory is not a violated prerequisite. Runtime reliability, activation and
summary fidelity remain untested limits.

## Required follow-up

The completed run and generated files remain immutable. Source-based correction
requires a new producer run with the compaction boundary, omitted learning route
and push-selection mapping as explicit review questions. The current check
does not execute that regeneration or certify the other comparison axes.

At completion of this audit, the instruction refinements above were proposals.
The subsequent [producer-check update](./producer-check-acceptance.md) implements
them and records its own verification boundary. This audit added diagnosis and
workshop bookkeeping only. Its changed records passed `commonplace-validate`
without warnings and `git diff --check`; no runtime implementation changed or
pytest run was needed for that diagnostic work.
