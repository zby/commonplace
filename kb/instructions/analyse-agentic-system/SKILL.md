---
name: analyse-agentic-system
description: "Use when asked to analyse, review, or refresh an external agent runtime, orchestration system, agent operating layer, agent memory/knowledge/context-engineering system, or narrower model-dependent operational mechanism from inspectable sources."
type: kb/types/instruction.md
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
mandatory lenses, then write one exact result and publish a compact generated
review. Delegate memory/context analysis to a fresh specialist and integrate
its typed report into that result.

Invocation authorizes the run directory under
`kb/reports/state/agentic-system-analysis/`, one generated review under
`kb/agentic-systems/reviews/`, its identical exact-result copy under
`kb/reports/retained/agentic-system-analysis/<run-id>/result.md`, and the local
memory specialist input and report inside that run directory. It does not authorize
changes to source worktrees, auxiliary indexes or surveys, transfer scans,
landscape synthesis, other retained reports, or Git staging and commits.

## Failure rule

Keep a correctable pre-publication failure in `running` state, fix the candidate
or result, and repeat the failed check. Set `run-status: failed` with one concise
reason only when abandoning the run or when a publication error leaves public
state uncertain. Do not resume a failed run or maintain a phase ledger,
packet, correction log, retry log, or validation receipt. Use a new run ID.
Temporary candidates are non-canonical and may be overwritten or removed by
the run owner.

## Steps

### 1. Open the run and resolve output paths

1. Allocate `AAS-<YYYY-MM-DD>-<system-slug>-<nn>`. Create
   `kb/reports/state/agentic-system-analysis/<run-id>/run-state.md` from the
   [run-state template](../../reports/types/agentic-system-analysis-run-state.md)
   with `run-status: running`. The
   exact result path is always `<run-id>/result.md`.
   Run `commonplace-validate <run-state-path>` immediately. Choose the
   source-native system name once here and copy it exactly into the result.
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
   Resolve the blocker and repeat inspection before publication. A verified,
   unchanged earlier publication can be replaced while uncommitted; arbitrary
   local edits cannot. No Git commit is required merely to rerun the review.
3. Record separately any caller-authorized auxiliary paths and any separately
   commissioned transfer scan. Automatic review publication does not authorize
   those operations.
4. Confirm the target is in scope: an agent runtime, orchestration framework,
   agent operating layer, memory/knowledge/context-engineering system, or a
   narrower mechanism whose operation depends on model calls it issues or
   serves. An MCP server, tool, or returning computation may qualify without
   owning the enclosing runtime. If the target is outside this boundary, write
   and validate an `out-of-scope` result, complete the run without a public
   review, and stop.
5. Classify the target as an `enclosing runtime`, `embedded inner runtime`,
   `runtime client`, `returning computation`, `workflow`, `extension or tool
   mechanism`, `builder or improvement plane`, `host integration`,
   `memory/knowledge/context-engineering system`, or another defined class.
   State functional inclusions, exclusions, external dependencies, and one
   boundary kind: `whole-system`, `subsystem-only`, or
   `complete artifact, partial loop`. Do not assign responsibilities owned by
   an excluded host to the selected target.

If no coherent boundary or reachable source can be established, write a typed
`blocked` result with every required section and explicit unreached
dispositions. Complete the run without publishing a review.

If a coordinator reads prior-review prose or substantive prior audit findings
before freezing the exact result and candidate, disclosure does not restore a
source-only pass. Stop that analysis, mark the run `failed` for prior-analysis
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
   register in the result with evidence
   layer, inspected scope, citation anchors, and access gaps. Keep
   implementation, doctrine/design, reported operation, observed runs, and
   causal experiments distinct.
5. Use a recorded search boundary only for a load-bearing absence claim. Name
   the searched roots or files, query, and revision; a casual search miss is a
   limitation, not an `ABS-*` record.
6. Select files and line ranges before reading content. Budget the aggregate
   output of parallel reads against the tool wrapper's delivery limit; an
   output cap alone does not bound the inspection. Treat truncated output as
   non-evidence. Narrow and repeat the read before citing it. For Git, cite the
   `SRC-*` ID plus a full commit-relative path; line ranges are optional
   navigation, not evidence-text verification. For each load-bearing finding
   (a disputed mechanism, comparison classification or assessment), retain the
   minimum verbatim supporting code or prose as an attributed blockquote.
   Number excerpts when locating statements, but omit display line numbers,
   invented ellipses and formatting fences from the quoted source text. Put
   discontiguous excerpts in separate quote blocks. End each block with a
   matching full-commit GitHub blob URL or
   ``> --- `commit-relative/path` @ `full-commit` ``. For captures, name the
   frozen captured source. Publication searches the complete pinned blob or
   capture for the quoted text with whitespace normalization. It never uses
   the worktree or line numbers as a substitute for matching source text.
   Verify that the matched passage supports its attached finding separately.
   An absence still requires the searched boundary; a quotation cannot prove
   that no other route exists.

Carry specialist quotes into the canonical records they support. Quote each
passage once in the exact result and reference those records from lens overlays
and the compact review. The retained result must not depend on opening a local
specialist report. Bare file/line citations alone cannot substantiate the
load-bearing findings. Structural validation rejects a complete result or
memory report with no quote anchors, but cannot certify that every material
claim has adequate evidence.

The source pin is an evidence boundary, not a recovery protocol. If it changes
or cannot be verified, fail the run and start another one.

### 3. Use one vocabulary and one record set

Use the result type's conclusion statuses exactly: `absent`, `inapplicable`,
`uninspected`, `claimed`, `afforded`, `wired`, `observed`, and
`causally supported`. Never upgrade context presence to activation, a claim to
an affordance, an affordance to wiring, wiring to observation, observation to
causality, or curation to warrant. Every negative or uncertain finding names
the inspected boundary and conclusion prevented.

Keep these distinctions:

- **Memory read-back** means material accumulated or changed through use affects
  a later consumer invocation. Static shipped material and ordinary current-run
  state are not read-back.
- **Activation** requires evidence that delivered material changed behavior.
- **Behavioral authority** records consumer, channel, force, and horizon.
  Epistemic and operational authority remain separate.
- **Guarantee strength** is separate from evidence status: invariant, protocol,
  policy, best effort, deployment guarantee, or no claimed guarantee.

Describe every external mechanism in source-native terms before mapping it to
Commonplace ontology. Explain the fit and mark partial or unresolved mappings.
Do not turn omission of an open-ended mechanism into evidence of absence.

Maintain one canonical register: `SRC-*` sources, `CMP-*` components, `OBJ-*`
operative objects, `RTE-*` routes, `CLM-*` claims, `ABS-*` evidenced absences,
and `BAP-*` behavioral-authority paths. The orchestrator owns IDs and generic
identity. A lens annotates existing IDs and proposes new records under local
tags that disappear when the orchestrator registers or merges them. An
`uninspected` gap is a limitation, not an `ABS-*` record.
Allocate canonical IDs monotonically. Never reuse an ID after merging or
rejecting its record; gaps are harmless. An ID shared with a worker is canonical
before final integration. Amend its evidence or status without changing its
referent. Splitting a combined record requires new IDs for the parts and an
explicit superseded disposition on the original record; do not assign its ID
to one part. Use local labels for provisional seeds.

The memory/context lens runs in a fresh specialist context under step 5. The
parent owns scheduling, canonical IDs, integration, and recovery. The epistemic
lens may run locally or in a separate worker with the same frozen boundary and
sparse overlay contract. Workers do not publish or delegate. If a fresh memory
worker is unavailable, report the execution blocker; do not silently perform
that specialist pass in the coordinator's context.

### 4. Run and challenge the runtime baseline

1. Begin with consequential claimed work and shipped entry paths. Trace one
   ordinary invocation end to end: principal, identity, context, state, model
   call, effects, runtime-client controls, coordination, terminal result, and
   retained or lost state.
2. Enumerate materially equivalent alternate paths before judging a guarantee:
   direct model calls, provider-native tools, host callbacks, shell access,
   extension code, subprocesses or remote workers, manual graph control, and
   durable variants where present. A guarantee covers only the paths its
   enforcement point covers.
3. Trace the smallest warranted set of forcing cases, ordinarily two to four
   for a full code-grounded pass. Prefer static inspection. Before any dynamic
   check, record the result type's execution-preflight fields and verify tools,
   packages, services, credentials, configuration, and authority. A check that
   never reaches the target remains `not run` and supports no negative finding.
   If no dynamic check is warranted, briefly list the checks considered and why
   static evidence was sufficient; keep the result's required disposition `no
   dynamic check planned`.
4. Record an executed check as a `SRC-*` probe evidence capsule. Use
   `causally supported` only for an actual intervention and comparison whose
   design supports the attribution. Exact output must remain inspectable in the
   one-file result.
5. For each material route record trigger, next-step owner, decision policy and
   form, context, state, executor and effect boundary, persistence, return,
   recovery, and terminal output. A load-bearing guarantee also names its owner,
   enforcement point, strength, covered and alternate paths, and required
   external contract.
6. Audit every `RTE-*` route for immediate return, later read-back, delegated
   visibility, selection predicate, invalidation or expiry, activation or
   effect, and evidence limits. Use explicit inapplicable or uninspected reasons
   instead of empty fields.
7. Distinguish the capability surface, current grant set, and deployed isolation
   envelope. Inspect permissions, approval, delegation, dynamic extension,
   reliability, observability, providers, packaging, and performance only where
   they change claimed work, a control path, evidence strength, or a lens result.
8. Inventory the distributed-parametric components used by the inspected
   runtime routes — LLMs, embedding models, parametric routers, critics, and
   adapters — as `CMP-*` records. For each, distinguish parameter changes
   during operation from identity pinning to an exact version or resolution
   through a mutable provider endpoint. Give each finding its evidence status;
   leave inaccessible provider internals explicitly uninspected. Fixed weights
   do not preclude learning through retained knowledge or changed procedures.
9. Inspect materially distinct mechanisms that admit changes to the product,
   retained knowledge or instructions, capabilities, or production machinery.
   Record the trigger, proposed change, admission mechanism, rejection ability,
   and rollback or recovery path on the admitting `RTE-*` record. Group writes
   governed by the same mechanism; routine logging, counters and unchanged
   checkpoint persistence need no separate revision analysis unless they alter
   later decisions or recovery. Reuse the memory specialist's findings for
   memory revisions rather than tracing those mechanisms twice.
   For diagnosis, candidate comparison, admission and successor selection,
   identify who proposes, decides, and can veto. Describe computational and
   human contributions separately when they share a step. Independently name
   any answer oracle: a supplied expected answer or reference outcome used to
   judge the candidate, including its provider and authority. A model judgment
   alone does not establish access to such an answer. State what triggers
   improvement and whether operation serves open requests, bounded experiments or curricula,
   or multiple modes; attach oracle use to the applicable mode. Unknowns and
   inapplicable steps remain explicit, without assigning an autonomy grade.

### 5. Run both lenses

For memory/context and epistemic, first record trigger evidence, inspected
boundary, pointed-to routes and objects, warranted `brief` or `full` depth, and
rationale. Both lenses always run. A brief result still states what was
inventoried, what was found, and which conclusions its thin evidence prevents.

Write `<run-id>/memory-input.md` before launching the specialist. Freeze the
run identity, source register (full revisions or capture hashes and access
roots), reviewed boundary, provisional canonical records, memory lens scope
and depth, exclusions, and the question the report must answer. Records are
source-checkable seeds, not accepted conclusions. Do not supply legacy reviews
or precomputed memory classifications. Hash the complete input file.

Invoke [Analyse agent memory](../analyse-agent-memory/SKILL.md) in a fresh
sub-agent context with that input and `<run-id>/memory-report.md` as its sole
output. The worker owns source-native memory analysis and the proposed
`memory-comparison` profile. Its typed report is the substantive handoff.
Off-band messages may carry progress or access problems; all findings and
integration issues must be retained in the report. Check its run, source,
boundary, input hash, completion status, and source anchors before integration.
If the frozen input changes, commission a new report against the new bytes.

Invoke
[`analyse-external-system-epistemic-architecture.md`](../analyse-external-system-epistemic-architecture.md)
for the epistemic lens. Pass the frozen boundary, registers, statuses, scoping
record, and classify-only routes. Require a sparse overlay on canonical IDs.
Keep that procedure's architectural status and observed candidate state in
their own vocabulary; never translate `implemented` into this workflow's
conclusion-status field.

### 6. Reconcile and synthesize

Require complete identifiers in worker returns and integration: `OBJ-1, OBJ-2`,
never `OBJ-1/O2` or an ID range. Return abbreviated proposals for expansion
before assigning canonical IDs. Map exact identifier tokens, not substrings;
verify that every mapped target is declared and unique. Keep proposal-to-ID
mappings in Reconciliation; outside it, refer to accepted canonical IDs.

Resolve proposed records into canonical IDs, attach corrections and amendments
to the affected records, preserve anchored conflicts, and report independent
convergence only when the lenses reached it independently. Recheck shared-route
ownership. Record mappings from specialist proposal IDs to canonical IDs and
the disposition of every material integration issue. Return substantive
conflicts to the specialist or retain explicit uncertainty; do not silently
strengthen its findings. If reconciliation exposes stale or unsupported lens
work, rerun that lens before continuing.

Write a system-organized synthesis: evidence basis and boundary,
architectural characterization and claimed work, runtime map, discriminating
mechanisms, scenario-relative assessment, limitations, and evidence or system
changes that would alter the assessment. Do not concatenate lens reports or add
a product ranking, generic adoption advice, system-wide epistemic grade,
Commonplace delta, transfer recommendation, or universal maturity model.

### 7. Write and validate the exact result

Write `<run-id>/result.md` using
`kb/types/agentic-system-analysis-result.md`. Every disposition keeps all
required headings. Its Run identity names the run state, generated review
disposition, memory report path, and SHA-256 of the report bytes. Put probe
evidence inline.

Integrate the specialist's `memory-comparison` profile by mapping its proposed
record IDs to accepted canonical IDs. Preserve its scope, evidence basis,
uncertainties, and rationale. The parent checks integration and shared-record
conflicts; it does not independently draft a second memory analysis. Include
all adopted findings and evidence needed to understand the main result without
opening the local report. The report is provenance, not independent semantic
clearance.

After reconciliation, check the integrated result against the type's comparison
rules, not just the separate lens returns:

- Match the profile scope to canonical objects, route branches and lens scope.
  Account for included alternatives and opaque parts in each known aggregate;
  distinguish excluded branches explicitly.
- Check every scoped trace-fed write against the learning criterion, including
  compaction. Carry each qualifying route into the dependent assessments with
  its own source, task horizon, timing and form.
- For each push signal, identify the consumer, trigger, selector input and
  selected retained part. Separate requested reads from automatic selection;
  a named object alone does not establish identifier-based push.
- Check that source/status amendments still concern the same canonical IDs,
  and that overlays cite rather than duplicate their generic records.

Record the checked routes and material dispositions in the existing Semantic
verification section. A known assessment unsupported by its records blocks
publication; properly scoped explicit uncertainty does not. Structural
validation does not perform this check.

Run `commonplace-validate --full <result-path>` and verify every source anchor,
canonical ID, evidence status, boundary, lens output, limitation, and blocker.
Correct deterministic formatting errors before continuing. An unresolved
evidence or semantic failure blocks publication. Correct it while the run stays
`running`, or abandon the run under the failure rule. The result's `complete`
disposition means its analysis content is complete; it does not claim that the
review projections have been published. Do not persist a JSON validation
receipt or review-job details in the result.

### 8. Publish validated candidates

Skip publication for a blocked or out-of-scope result. For a complete result:

1. Generate the compact whole-system review solely from the validated result
   and its primary-source anchors. Write it first as a temporary candidate in
   the run directory. Use `kb/types/note.md` and exact frontmatter fields
   `generated-by: analyse-agentic-system`, `analysis-run`, `source-identity`,
   `reviewed-revision`, `analysis-result`, and `analysis-result-sha256`.
   The last two fields name
   `kb/reports/retained/agentic-system-analysis/<run-id>/result.md` and the SHA-256
   of the validated exact result. Publication retains those identical bytes;
   do not draft a separate retained report or rewrite the result for the matrix.
2. Run `commonplace-agentic-analysis-publication prepare` with the run state,
   generated candidate, destination, and `--expected-incumbent-sha256` from
   destination inspection. It validates candidate bytes as their
   intended public path, source anchors and quote blocks against the frozen
   source, workflow identity, memory report and input, and incumbents. It
   changes no public artifact and dispatches no semantic review job.
3. Run `commonplace-agentic-analysis-publication publish` with the same
   arguments, including the same incumbent digest. It validates the
   prospective complete run state, replaces the
   compact review, retains the exact result, and writes the complete run state
   last. It rolls back ordinary in-process write or validation failures. A
   crash during replacement may leave partial public writes; inspect them,
   mark the run `failed`, and use a new run ID. Existing review and retained
   result bytes are saved as `incumbent-review.md` and `incumbent-result.md`
   in the new run before replacement. Keep those recovery copies with the run.

The run state binds the exact result, compact review, and memory report hashes.
Keep the frozen input and report with the local run while completion checks
need them. Candidate cleanup after success is best effort. A cleanup warning
does not undo completion. Never patch generated prose independently of its
source boundary and method. Never stage or commit unless separately requested.

After a main review changes, report the comparison outputs under
`kb/agentic-systems/comparisons/` stale unless rebuilt and validated under
separate authority. The matrix, table, and numerical-analysis scripts read the
retained result directly. Repeated `--review` arguments select a bounded corpus;
without them every generated main review must meet the input contract.
The old `kb/agent-memory-systems/systems.csv` and `systems-table.md` are historical
snapshots and are not rebuilt by these scripts.
Report a prior current landscape synthesis as historical unless it was refreshed
under separate authority.
Authorization alone does not establish that an operation completed. The new
matrix records both evidence tiers; numerical claims use code-grounded rows,
with doc-grounded findings kept separate.

### 9. Run an optional transfer scan after completion

A transfer scan is separate, interest-conditioned state. Run
[`scan-agentic-system-transfer`](../scan-agentic-system-transfer/SKILL.md) only
when separately commissioned and only after the complete run state validates.
Pass `result.md`, its SHA-256, the sibling `run-state.md` path, the interest
brief, and permitted Commonplace read and output scope. The scan verifies the
completed run and reads the exact result directly; a legacy review or compact
public review is not a substitute. The scan never edits the analysis, published reviews,
or comparison corpus. If it exposes an analysis defect, fail that conclusion
and rerun the analysis before scanning again.

### 10. Report

Run `commonplace-agentic-analysis-handoff <run-state-path>` and include its
Markdown output unchanged in the final response. It validates the run state
and current output bytes before rendering.

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
- Both lenses and both scoping records exist; thin evidence produces a bounded
  brief result, not a skipped lens.
- Source-native mechanisms remain visible beneath Commonplace mappings, and no
  conclusion status is upgraded.
- The exact result validates before publication.
- Each public review has the SHA-256 and workflow identity recorded by the
  complete run state; the memory report and frozen input match that run.
- Correctable pre-publication failures keep the run `running`. A failed run was
  abandoned or has uncertain public state; its replacement is a new run.

---

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — rests-on: the causal runtime responsibilities in step 4
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — rests-on: why the runtime inventory remains open
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — rests-on: why memory is a mandatory lens
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — rests-on: the retention, read-back, presence, and activation distinctions
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — rests-on: the consumer, channel, force, and horizon record
