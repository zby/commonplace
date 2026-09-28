---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agent runtime, orchestration system, agent operating layer, agent memory/knowledge/context-engineering system, or narrower model-dependent operational mechanism from inspectable sources."
type: types/instruction.md
user-invocable: true
argument-hint: "<system identifier> plus source input (repository, checkout, snapshot/bundle, or documents) and optional public review path"
allowed-tools: Read, Write, Grep, Glob, Bash, Task
context: fork
model: opus
---

# Analyse an Agentic System

Analyse one external agentic system at one frozen evidence boundary. Identify
what the system wires, where its responsibilities end, and what its
memory/context and epistemic routes support. Run a runtime baseline and both
mandatory lenses, then write the run's retained set (overview, runtime,
memory and epistemic members) and publish a compact generated review. Delegate
memory/context analysis to a fresh specialist and finalize its typed report as
the set's memory member.

Invocation authorizes the run directory under
`kb/reports/state/agentic-system-analysis/`, one generated review under
`kb/agentic-systems/reviews/`, the identical retained copy of the four members
under `kb/reports/retained/agentic-system-analysis/<run-id>/`, and the local
memory specialist input and report inside that run directory. It does not authorize
changes to source worktrees, auxiliary indexes or surveys, transfer scans,
landscape synthesis, other retained reports, or Git staging and commits.

## Failure rule

Keep a correctable pre-publication failure in `running` state, fix the candidate
or member, and repeat the failed check. Set `run-status: failed` with one concise
reason only when abandoning the run or when a publication error leaves public
state uncertain. Do not resume a failed run or maintain a phase ledger,
packet, correction log, retry log, or validation receipt. Use a new run ID.
Temporary candidates are non-canonical and may be overwritten or removed by
the run owner.

Run acceptance commands separately and inspect each exit status, or chain
dependent commands with `&&`. Shell pipelines also need `set -o pipefail`.
When wrapping tool calls, retain status and stderr as well as stdout; a final
hash or later successful command does not clear an earlier failure. Use
`commonplace-quote` rather than writing a separate citation formatter.

## Steps

### 1. Open the run and resolve output paths

1. Allocate `AAS-<YYYY-MM-DD>-<system-slug>-<nn>`. Create
   `kb/reports/state/agentic-system-analysis/<run-id>/run-state.md` from the
   [run-state template](../../types/agentic-system-analysis-run-state.md)
   with `run-status: running`. The artifact manifest is
   `<run-id>/output/ARTIFACT.yaml`; it pins every report beside it, including
   `overview.md`. Record the method commit now: run
   `git rev-parse HEAD` and keep the full commit for the overview's
   `inputs-commit`. Publication requires HEAD to still descend from it with
   the method paths unchanged (the list is the `METHOD_PATHS` constant in
   `src/commonplace/lib/agentic_publication.py`), and requires the worktree
   to be clean outside the publication outputs: no staged change, no
   modified tracked file and no untracked file under `kb/`, except untracked
   or modified files under `kb/agentic-systems/reviews/` and
   `kb/reports/retained/agentic-system-analysis/`. It also requires the
   running `commonplace` package's source to equal `inputs-commit`, since an
   editable install executes its own checkout's code even inside another
   worktree. Commit a pending method change before opening the run, not
   after.
   Run `commonplace-validate <run-state-path>` immediately. Choose the
   source-native system name once here and copy it exactly into the overview.
2. Derive the public review path as
   `kb/agentic-systems/reviews/<system-slug>.md` unless the caller supplied one.
   A caller-supplied path must also be directly under `reviews/`. Before
   reading sources or drafting, run:

   ```bash
   commonplace-agentic-analysis-publication inspect-destination --generated-destination <review-path> --source-identity <source-identity>
   ```

   This reads incumbent metadata internally and returns only eligibility and
   `expected_incumbent_sha256` (a digest or `absent`). Save that value in this
   run's `## Run` prose for both publication commands. Never inspect incumbent
   prose, descriptions, prior results or audits to resolve the destination;
   guessed line counts such as `head` or `sed -n '1,22p'` are not metadata
   extraction. Hand-authored or different-source collisions need a qualified
   slug. Other inspection failures are publication blockers to report at once;
   analysis may continue, but do not promise publication or bypass the guard.
   Resolve the blocker and repeat inspection before publication. An
   incumbent is checked by bytes: a generated review of the same source whose
   retained set hashes to its pins, whether committed or a sibling run's
   fresh uncommitted publication. Inspection also applies the worktree rule
   above; a dirty tree is a blocker to report, not to work around.
3. Record separately any caller-authorized auxiliary paths and any separately
   commissioned transfer scan. Automatic review publication does not authorize
   those operations.
4. Confirm the target is in scope: an agent runtime, orchestration framework,
   agent operating layer, memory/knowledge/context-engineering system, or a
   narrower mechanism whose operation depends on model calls it issues or
   serves. An MCP server, tool, or returning computation may qualify without
   owning the enclosing runtime. If the target is outside this boundary, write
   an `out-of-scope` overview with an overview-only artifact, skip steps 2 to 6 with
   both scoping records stating `not reached`, and continue at step 7.
5. Classify the target with one `target-class` and one `boundary-kind` value
   from the overview type's frontmatter table, and state functional inclusions,
   exclusions, and external dependencies. Do not assign responsibilities
   owned by an excluded host to the selected target.

If no coherent boundary or reachable source can be established, write a
`blocked` overview with an overview-only artifact, skip steps 2 to 6 with both scoping records stating `not
reached`, and continue at step 7.

If a coordinator reads prior-review prose or substantive prior audit findings
through any tool before freezing the set and candidate, disclosure
does not restore a source-only pass. Stop that analysis, mark the run `failed` for prior-analysis
exposure, and require a fresh coordinator context with a new run ID and clean
source-only inputs. Do not publish the exposed draft or try to repair its
independence claim. A later, separately commissioned audit after both artifacts
were frozen records its timing; it does not retroactively contaminate their
construction. Keep subsequent analytical changes outside that exposed context.

### 2. Freeze and inspect sources once

1. Before inspection, record a compact source allowlist: the exact repositories,
   captures, documents, and time boundary that may supply evidence. A supplied
   repository reference authorizes creating its missing ignored
   checkout and fetching the objects needed for the selected revision. It does
   not authorize changing an existing worktree, switching branches, merging,
   pulling, or resetting.
2. For GitHub, normalize the repository identity and use
   `related-systems/<owner>--<repo>/`. Require `git check-ignore -q
   related-systems` before creating it, verify an existing checkout's origin,
   and resolve the selected revision to a full commit. Inspect only with
   commit-addressed `git --no-replace-objects -C <absolute-root> ls-tree`,
   `show`, and `grep`; never read evidence from the worktree.
3. Turn every non-Git source set into one immutable capture or bundle with a
   stable identity, version or capture label, absolute path, and SHA-256. Do
   not analyse a moving live page as though it were frozen.
4. Put the Git commit or capture identity in `run-state.source` while the state
   remains `running`, using the source mapping in the run-state type. Validate
   that state again before inspecting sources or delegating. Build one `SRC-*`
   register with the columns and evidence layers the overview type's Source
   register requires.
5. Select files and line ranges before reading content. Budget the aggregate
   output of parallel reads against the tool wrapper's delivery limit; an
   output cap alone does not bound the inspection. Treat truncated output as
   non-evidence. Narrow and repeat the read before citing it. For each
   load-bearing finding, generate the quote block the overview type's Source
   register requires with
   [`commonplace-quote`](../../reference/commands.md#commonplace-quote):
   `commonplace-quote <run-state-path> --source-path <commit-relative-path>
   --text-file <selection-file>`, omitting `--source-path` for the run's
   capture, or `--selections <json-file>` to resolve many selections across
   files in one call. Choose the occurrence whose context supports the
   finding and insert its citation unchanged. Request discontiguous passages separately.
   Only a quote attribution carries a line range. Cite a source in prose by
   path only; do not copy a generated range into a prose reference.
   A failed lookup requires rereading the source and revising the selection;
   never format a citation, strip source characters, or calculate a range by
   hand. Assess semantic support yourself: a generated citation proves
   occurrence, not support, and a quotation cannot prove that no other route
   exists.

Check the delivered output for truncation at both the command and wrapper
levels. Split a batch whose combined output exceeds delivery limits; reread
the missing span before claiming full coverage. Do not infer coverage from a
successful command or its requested line range.

The source pin is an evidence boundary, not a recovery protocol. If it changes
or cannot be verified, fail the run and start another one.

### 3. Use one vocabulary and one record set

Load the [overview type](../../types/agentic-system-analysis-overview.md)
before recording findings: its set-wide sections own the namespace, the
declaration and annotation grammar, the conclusion-status values, the source
anchors and the quotation contract for every member. The
[runtime report type](../../types/agentic-system-runtime-report.md) owns the
runtime account, probe evidence and record fields written in step 4, and the
theory-builder terms used below; the
[memory report type](../../types/agent-memory-analysis-report.md) owns the
`memory-comparison` contract; the
[epistemic report type](../../types/agentic-system-epistemic-report.md) owns
the six epistemic blocks. Load the
[epistemic instruction](../analyse-external-system-epistemic-architecture.md)
at the same point: the route records written in step 4 feed its ledger.

Judging norms:

- Never upgrade context presence to activation, a claim to an affordance, an
  affordance to wiring, wiring to observation, observation to causality, or
  curation to warrant.
- Give each theory-builder condition, and learning, reflection and autonomy,
  its own conclusion status from its own evidence, under the
  [Shared records](../../types/agentic-system-runtime-report.md#shared-records)
  rules for theory routes.
- When describing revision selection, write that it prefers reach among
  revisions that fit the evidence, not "reach rather than fit". This applies
  whether or not the route is reflective.
- Describe every external mechanism in source-native terms before mapping it
  to Commonplace ontology. Explain the fit and mark partial or unresolved
  mappings. Do not turn omission of an open-ended mechanism into evidence of
  absence. An `uninspected` gap or a casual search miss is a limitation, not
  an `ABS-*` record; record the searched boundary only for a load-bearing
  absence claim.

Register ownership: the coordinator owns canonical IDs and generic identity. A
lens annotates existing IDs and proposes new records under local proposal
IDs that disappear when the coordinator registers or merges them. Allocate IDs
monotonically and never reuse one after merging or rejecting its record; gaps
are harmless. An ID shared with a worker is canonical before final
integration: amend its evidence or status without changing its referent, and
split a combined record only by giving the parts new IDs and marking the
original superseded.

### 4. Run and challenge the runtime baseline

1. Begin with consequential claimed work and shipped entry paths. Trace one
   ordinary invocation end to end and record it with the fields the runtime
   report type's Runtime account requires.
2. Enumerate materially equivalent alternate paths before judging a guarantee:
   direct model calls, provider-native tools, host callbacks, shell access,
   extension code, subprocesses or remote workers, manual graph control, and
   durable variants where present. A guarantee covers only the paths its
   enforcement point covers.
3. Trace the smallest warranted set of forcing cases, ordinarily two to four
   for a full code-grounded pass. Prefer static inspection. Before any dynamic
   check, write its execution-preflight record and verify tools, packages,
   services, credentials, configuration, and authority.
4. Record an executed check as a `SRC-*` probe evidence capsule.
5. Record each material route and load-bearing guarantee with the fields the
   runtime report type's Runtime account and Routes records require, then
   audit every `RTE-*` record for the read-back fields the Routes records list.
6. Distinguish the capability surface, current grant set, and deployed isolation
   envelope. Inspect permissions, approval, delegation, dynamic extension,
   reliability, observability, providers, packaging, and performance only where
   they change claimed work, a control path, evidence strength, or a lens result.
7. Inventory the distributed-parametric components used by the inspected
   runtime routes — LLMs, embedding models, parametric routers, critics, and
   adapters — as `CMP-*` records with the fixity fields the runtime report
   type's Components records require.
8. Inspect materially distinct mechanisms that admit changes to the product,
   retained knowledge or instructions, capabilities, or production machinery.
   Record each on its admitting `RTE-*` record with the admission,
   decision-role, answer-oracle, operating-mode, and guidance fields the
   runtime report type requires. Defer memory revisions to the specialist's
   report; step 6 attaches them.

### 5. Run both lenses

For memory/context and epistemic, first write the scoping record the
overview's Lens scoping section requires, choosing `brief` or `full` depth from the
trigger evidence. Both lenses always run; thin evidence produces a bounded
brief result, not a skipped lens.

Write `<run-id>/memory-input.md` before launching the specialist. Freeze the
run identity, source register (full revisions or capture hashes and access
roots), reviewed boundary, provisional canonical records, memory lens scope
and depth, exclusions, and the question the report must answer. Records are
source-checkable seeds, not accepted conclusions. Do not supply legacy reviews
or precomputed memory classifications. Hash the complete input file.

Launch a fresh sub-agent to execute the
[Analyse agent memory](../analyse-agent-memory.md) instruction with that input
and `<run-id>/memory-report.md` as its sole output. The worker owns source-native
memory analysis and the proposed `memory-comparison` profile. Its typed report
is the substantive handoff. The parent owns scheduling, canonical IDs,
integration, and recovery; workers do not publish or delegate. If a fresh
memory worker is unavailable, report the execution blocker; do not perform
that specialist pass in the coordinator's context.
Reserve capacity for that worker before opening another analysis coordinator.
Do not use agent listings to wait or obtain status in a source-only worker:
even filtered listings can return completed reports. Use the commissioned
worker's completion event or report path. If launch or communication fails,
report the failed operation to the supervising coordinator and end the turn
when it must free capacity. Interruption alone does not establish free capacity.
The supervisor may launch a fresh specialist with the same frozen input and
output ownership, then resume this coordinator after that worker ends. Do not
start a second writer while ownership of the first is unresolved. A failed
notification is not delivery; the final report remains the handoff and the
supervisor may relay its path, hash and status without analytical prose.
Off-band messages may carry progress or access problems; all findings and
integration issues must be retained in the report. Check its run, source,
boundary, input hash, completion status, and source anchors before integration.
If the report comes back `blocked` and the block is correctable, commission a
fresh specialist against the same frozen input; otherwise the run completes as
`blocked`.
If the frozen input changes, commission a new report against the new bytes.
Prior-analysis exposure has the consequence step 1 states.

Invoke
[`analyse-external-system-epistemic-architecture.md`](../analyse-external-system-epistemic-architecture.md)
for the epistemic lens, locally or in a separate worker with the same frozen
boundary. Pass the frozen boundary, registers, statuses, and scoping record.
Its output is `<run-id>/output/epistemic.md` under the epistemic report type; it
declares no records and cites the set's. Write it, or remap its `EPI-`
proposal IDs, after step 6's reconciliation, so the member cites only
canonical IDs.

### 6. Reconcile and synthesize

Resolve proposed records into canonical IDs: return a worker's abbreviated
proposals for expansion first, map exact identifier tokens rather than
substrings, and verify that every mapped target is declared and unique.
Record corrections as `Amendment:` entries in the declaring member's
`## Amendments` section, preserve anchored conflicts, and report independent convergence only when the lenses reached it
independently. Recheck shared-route ownership. Attach the admission fields
of memory routes from the specialist's findings rather than tracing those
mechanisms twice. The specialist's `memory-comparison` profile stays in the
memory member with its scope, per-value evidence bases and records, coverage
assessments, uncertainties, and rationale preserved; check it against the
records of the whole set. Each specialist quote stays in the memory member
beside the record it supports; a runtime record cites that record rather
than repeating the passage. The parent checks integration and shared-record
conflicts and does not draft a second memory analysis. Return substantive conflicts to the specialist or retain
explicit uncertainty; do not silently strengthen its findings. If
reconciliation exposes stale or unsupported lens work, rerun that lens before
continuing.

If a specialist correction cannot be delivered, wait for capacity or retain
the blocker. The coordinator may replace a malformed citation with a generated
citation only after checking the selected occurrence still supports the same
finding. Disclose such mechanical edits in the report and Reconciliation and
bind the new report hash through `finalized-from`. A substantive change
requires specialist reanalysis.

Write the Bounded synthesis the overview type requires from the reconciled
records,
organized around the system's operational progression rather than by lens.

### 7. Write and validate the set

| File (relative to `<run-id>/`) | `type:` value | Schema |
|---|---|---|
| `output/overview.md` | `types/agentic-system-analysis-overview.md` | `kb/types/agentic-system-analysis-overview.schema.yaml` |
| `output/runtime.md` | `types/agentic-system-runtime-report.md` | `kb/types/agentic-system-runtime-report.schema.yaml` |
| `output/memory.md` | `types/agent-memory-analysis-report.md` | `kb/types/agent-memory-analysis-report.schema.yaml` |
| `output/epistemic.md` | `types/agentic-system-epistemic-report.md` | `kb/types/agentic-system-epistemic-report.schema.yaml` |
| `output/ARTIFACT.yaml` | `reports/types/agentic-system-analysis-set.md` | `kb/reports/types/agentic-system-analysis-set.schema.yaml` |
| `run-state.md` | `types/agentic-system-analysis-run-state.md` | `kb/types/agentic-system-analysis-run-state.schema.yaml` |
| generated review candidate (any non-reserved name, e.g. `review-candidate.md`; published to `kb/agentic-systems/reviews/<system-slug>.md`) | `agentic-systems/types/generated-review.md` | `kb/agentic-systems/types/generated-review.schema.yaml` |

Write reports under `<run-id>/output/`, keeping run state, specialist inputs,
local reports and review candidates outside that directory. A `blocked` or
`out-of-scope` outcome contains only `overview.md`; a complete outcome has
four members, each under its type:

1. `<run-id>/output/runtime.md` under the runtime report type: the runtime account,
   probe evidence, the records the runtime pass declared, and its annotations
   on records the memory member declares.
2. `<run-id>/output/memory.md` under the memory report type, authored from the local
   `memory-report.md` and nothing else: replace proposal IDs by exact-token
   mapping from the overview's Reconciliation table, rewrite a seeded record
   the specialist re-declared under `## Shared records` to an `On <ID>`
   annotation heading, set `finalized-from` to the SHA-256 of
   `memory-report.md`, and append `## Amendments`. Code checks the hash
   pins, not the derivation; keeping the member to those mechanical edits is
   your responsibility, and a substantive change goes back to the specialist.
3. `<run-id>/output/epistemic.md` under the epistemic report type, from step 5.
4. `<run-id>/output/overview.md` under the overview type, with `inputs-commit`
   from step 1. Its Reconciliation names the local report by path and SHA-256
   and every mechanical edit finalization made.

Write `output/ARTIFACT.yaml` last, under the
[analysis set type](../../reports/types/agentic-system-analysis-set.md).
Set `type: reports/types/agentic-system-analysis-set.md` and a `members`
mapping from each actual report filename to `{sha256: <digest>}`, including
`overview.md`. Recompute hashes after any member edit. The schema owns
required members and closed membership; the manifest supplies integrity
metadata only.

After reconciliation, check the whole set, not just the separate lens
returns, against the memory report type's Memory comparison fields: scope
agreement with the canonical records across members, every scoped trace-fed
write including compaction, each push signal's consumer and selector, and
amendments and annotations on the same canonical IDs.

Record the checked routes and material dispositions, and the check of every
source anchor, canonical ID, evidence status, boundary, member, limitation
and blocker, in the overview's Semantic verification section. A known
assessment unsupported by its records blocks publication; properly scoped
explicit uncertainty does not. Structural validation does not perform this
check.

Run `commonplace-validate <run-id>/output --full` for the whole artifact.
It validates every member and checks the set's membership, hashes, identity,
record declarations and references, and comparison-profile references.
Explicit file validation checks that member alone. Publication additionally
verifies run-state and review pins, the memory member's `finalized-from`
against the local report and `canonical-register-sha256` against the frozen
input, and source anchors and quotations for every member and the review.
Correct deterministic formatting errors before continuing. An
unresolved evidence or semantic failure blocks publication. Correct it while
the run stays `running`, or abandon the run under the failure rule. The
overview's `complete` disposition means the set's analysis content is
complete; it does not claim that the review projection has been published.

### 8. Publish validated candidates

For a blocked or out-of-scope overview, complete the run without publication:
set `run-status: complete`, the disposition, and the `artifact` manifest path and
SHA-256, leave `generated-review: null`, and validate the run state. For a
complete set:

1. Generate the compact whole-system review solely from the validated set
   and its primary-source anchors. Write it first as a temporary candidate in
   the run directory under the
   [generated review type](../../agentic-systems/types/generated-review.md)
   with exact frontmatter fields `generated-by: analyse-agentic-system`,
   `analysis-run`, `source-identity`, `reviewed-revision`,
   `analysis-artifact`, and `analysis-artifact-sha256`. The last two fields
   name `kb/reports/retained/agentic-system-analysis/<run-id>/ARTIFACT.yaml`
   and the SHA-256 of the validated manifest. Publication retains the manifest and
   members byte for byte; do not draft a separate retained report or rewrite
   a member for the matrix.
2. Run `commonplace-agentic-analysis-publication prepare` with the run state,
   generated candidate, destination, and `--expected-incumbent-sha256` from
   destination inspection. It applies the worktree rule and the method
   commit check from step 1, validates candidate bytes as their intended
   public path and every member as its retained path, and checks source
   anchors and quote blocks against the frozen source, workflow identity,
   the memory member's finalization, and the incumbent. It changes no public
   artifact and dispatches no semantic review job.
3. Run `commonplace-agentic-analysis-publication publish` with the same
   arguments, including the same incumbent digest. It validates the
   prospective complete run state, replaces the compact review, retains the
   four members, and writes the complete run state last. It rolls back
   ordinary in-process write or validation failures. A crash during
   replacement may leave partial public writes; inspect them, mark the run
   `failed`, and use a new run ID. Existing review and retained member bytes
   are saved as `incumbent-review.md` and `incumbent-<member>.md` in the new
   run before replacement. Keep those recovery copies with the run.

The run state binds the manifest and compact review hashes; the manifest
binds every report, and the memory member binds the local report
hash. Keep the frozen input and report with the local run while completion
checks need them. Candidate cleanup after success is best effort. A cleanup
warning does not undo completion. Never patch generated prose independently
of its source boundary and method. Never stage or commit unless separately
requested.

After a main review changes, report the comparison outputs under
`kb/agentic-systems/comparisons/` stale unless rebuilt and validated under
separate authority, and a prior landscape synthesis as historical unless it
was refreshed under separate authority. Authorization alone does not
establish that an operation completed.

### 9. Run an optional transfer scan after completion

A transfer scan is separate, interest-conditioned state. Run
[`scan-agentic-system-transfer`](../scan-agentic-system-transfer/SKILL.md) only
when separately commissioned and only after the complete run state validates.
Pass the run's `output/ARTIFACT.yaml` path, its SHA-256, the `run-state.md`
path, the interest brief, and permitted Commonplace read and output scope.
The scan verifies the completed run and reads the overview and the members
the artifact manifest pins directly; a legacy review or compact public review is not a
substitute. The scan never edits the analysis, published reviews,
or comparison corpus. If it exposes an analysis defect, fail that conclusion
and rerun the analysis before scanning again.

### 10. Report

Run `commonplace-agentic-analysis-handoff <run-state-path>` and include its
Markdown output unchanged in the final response. It validates the run state,
the artifact and every member its manifest pins before rendering, and names
the members.

Append the downstream freshness dispositions required by step 8. For a
separately commissioned transfer scan, also return its output path and material
findings, or its full output when no file was written. Report any blocker
that prevented the scan from completing. These session outcomes supplement the
checked handoff; they do not require additional run-state fields.

A failed run reports its failure reason and does not use the handoff command.

## Verify

- One run ID, frozen source boundary, and source register govern every finding.
- Git reads use the full recorded commit; captures match their SHA-256; no
  truncated output supports a claim.
- The runtime baseline covers ordinary, material alternate, and warranted
  forcing routes at the target's actual responsibility horizon.
- Component fixity, material revision admission, decision roles, improvement
  triggers, operating modes and answer-oracle access are recorded or carry
  explicit `uninspected` or `inapplicable` reasons.
- Every admitting route records its guidance and retention with the type's
  theory-route fields, each condition at its own status.
- Both lenses and both scoping records exist; thin evidence produces a bounded
  brief result, not a skipped lens.
- Source-native mechanisms remain visible beneath Commonplace mappings, and no
  conclusion status is upgraded.
- Every member validates before publication, and the set's checks pass at
  publication.
- Each public review has the SHA-256 and workflow identity recorded by the
  complete run state; the memory member is the local report finalized under
  the recorded mapping, and the frozen input matches that run.
- Correctable pre-publication failures keep the run `running`. A failed run was
  abandoned or has uncertain public state; its replacement is a new run.

---

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: the causal runtime responsibilities in step 4
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — rests-on: why the runtime inventory remains open
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — rests-on: why memory is a mandatory lens
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: the retention, read-back, presence, and activation distinctions
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — rests-on: the consumer, channel, force, and horizon record
- [Tentative theory](../../notes/definitions/tentative-theory.md) — rests-on: the status of the theory, independent of structure or retention
- [Theory builder](../../notes/definitions/theory-builder.md) — rests-on: localized, consumed, criticized, and retained theories, and the reflective and autonomous qualifiers
- [Addressable theory](../../notes/definitions/addressable-theory.md) — rests-on: separately inspectable and editable parts as an additional property
- [A complete theory path does not establish improved capacity](../../notes/a-complete-theory-path-does-not-establish-improved-capacity.md) — rests-on: the separate evidence claims and stronger requirements for later or recurrent use
- [Reflective system](../../notes/definitions/reflective-system.md) — rests-on: the causally connected self-representation required for reflection
- [Self-improving system](../../notes/definitions/self-improving-system.md) — rests-on: the operative, evidence-responsive change the revision-admission records describe
