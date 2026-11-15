# Contract and first implementation slice

## Status and recommendation

The operator authorized this implementation commission on 2026-11-15 after the family/form checkpoint and its atoms-only correction. Paid trials remain separately authorized. [Implementation status](./implementation.md) records verification and the completed operator-authorized cutover. [Decisions](./decisions.md) owns family distinctions and consumer evidence. [Execution design](./execution-design.md) owns the selected boundaries. This file specifies their implementation contract and acceptance conditions.

**Implement one vertical slice:** catalog gates, type/collection conformance and critique through the existing `commonplace-review` and Workjig route, with exact input capture, typed individual results, per-execution evidence and single-atom fixtures. Include explicitly supplied draft gate criteria. Do not admit the other report methods in this slice, design their combinations, or add `commonplace-operation`.

Use the existing [review-result type plan](../review-on-workjig/types-plan.md), including its worker/code field split, anchored findings, captured contract validation and removal of the result footer. Extend that design with finding levels and observation/capture references. Do not create a second result type or a second implementation of typed acceptance. Coordinate the one review-result cutover with that workshop; its other type slices are not prerequisites.

There is no technical reason to commission another paid experiment before implementing this infrastructure. Format changes may affect judgments; deterministic acceptance tests cannot establish calibration. Paid format comparisons remain separately authorized evaluation work. The stability pilot and three higher-order calibration rounds used the old format: retain their figures as old-format evidence, not a directly comparable post-cutover baseline. A comparison across the boundary must explicitly treat output format as a changed condition.

Recommended work order within this one commission: result type/schema; input capture and observation records; coordinated consumer cutover; explicit draft selector; fixtures. Fixtures remain part of the commission. If interrupted before fixtures, report the implementation as partial rather than declaring a smaller slice complete.

## 1. One atom, one observation, retained attempts

Distinguish these identities:

| Identity | Meaning and lifetime |
|---|---|
| Criterion | The instruction or contract being applied. Preserve existing repository/library identities. A wording change changes its content hash, not its logical identity. |
| Run | Existing Workjig-owning directory. A sweep can contain many atom executions; a fixture trial in this slice contains one selected atom on one target. |
| Observation | One execution of an atom against a captured target and request. Identifies its inputs, result contract, requested configuration and attempt history. |
| Attempt | A launch or rejected answer within that observation. Workjig remains authoritative for launch/retry state. |
| Completed result | A deterministically valid output with code-owned provenance. It is evidence of a completed assessment, not approval of the judgment. |

Allocate and persist an observation before launching. Resolve it on resume from the run, logical job and captured initial request identity, not from a new timestamp. Correction prompts and retries belong to that same observation even though Workjig assigns different request keys. A completed replay retains the original completion identity and time. Explicit dismissal/retry retains the earlier result and its supersession history; it does not manufacture an independent trial.

Changed inputs or execution contracts inside a composed workflow can create another observation within its run. They are not repetitions under identical conditions. Preserve full-pass initial/closing behavior and Workjig's existing reuse; do not redesign its composition. Existing bundle calls can produce several per-atom observations sharing one launch. Record that shared launch; do not claim those observations were generated independently.

A fresh-result skip is a selection event pointing to an existing result, not a new observation. Two fixture invocations create different run roots and observations even when every fixture byte matches. Resume continues only one of them. No aggregation, voting or automatic statistical scheduling.

## 2. Capture and record ownership

Keep the current state root. Proposed layout additions are inside existing runs:

```text
kb/reports/state/review/runs/<run>/
  sweep.json                         existing options, with a format/version discriminator
  calls/                             existing Workjig evidence, unchanged ownership
  artifact/reviews/<observation>/
    observation.json                 versioned execution manifest and references
    inputs/target/<original-path>    exact captured target, original relative path preserved
    inputs/...                       explicitly supplied criteria/contracts/operational files
    results/<launch>/<output>.md     completed typed results; never overwrite an earlier output
kb/reports/state/review/results/...  existing replaceable current-result view
```

The manifest is execution state checked by Python, not a new KB directory type. No attempt to type the entire Workjig tree. The completed Markdown artifact uses `types/review-result.md` and its schema, supplied by the coordinated type slice.

Capture before dispatch, then feed the worker from those captures. Do not hash a live file and reread it for execution. Use strict UTF-8 decoding without newline normalization; preserve CRLF, final-newline absence and all other supplied bytes. If a transport changes bytes, detect that by checking the launch input against the capture and refuse to claim an exact match. Preserve existing normalized freshness hashes separately. For full-pass in-memory text, capture exactly the text supplied by that caller and label its origin as supplied text, not as bytes read from the current checkout.

Required manifest information:

| Group | Minimum fields or references |
|---|---|
| Identity | Record version, observation id, run, logical job, criterion identity/kind, requested output contract and mode (ordinary or fixture) |
| KB baseline | Repository HEAD commit, target's original relative path, live-context qualification; null commit only with an explicit unsupported-reconstruction reason |
| Captures | Role, origin identity, retained relative path, exact SHA-256 and byte count for target, criterion, output type/schema inputs and supplied operational inputs |
| Execution request | Captured wrapper/prompt identity, resolved profile including flags, grouping, worker limit and timeout; Workjig request keys and launch references |
| Executor | Commonplace source/install identity and Workjig version, resolved harness executable and reported version when available; distinguish unavailable from empty |
| Observations | Actual reported model per launch, available effective tool/configuration evidence and its source; unknowns explicitly listed |
| Completion | Attempt references, validation failures, problem/interruption state, accepted launch/output path and exact raw-output hash, completed typed-result path/hash, supersession if any |
| Fixture link | Fixture identity/hash for trials; otherwise absent |

Store values once where practical and reference existing Workjig records. The manifest is an index and a binding record, not a duplicate launch log. Keep it atomic and under the existing run lock; write the completed result before publishing its current-result copy. Recovery can finish publication idempotently. A crash must not leave a current result referring to an absent completed artifact.

**Target ownership:** the review execution owns its assessed target capture. An improvement run may cite it instead of retaining another evidence copy once the retention guarantee and its type contract are updated. The improvement run owns edit-produced texts not yet captured by a review. Do not delete existing copies or change those types in this slice. Referenced run evidence must not be removed as orphaned current state. No automatic run garbage collector is introduced.

Operational input copies remain necessary even when evidence ownership is unique. A launcher selects an explicit list, copies and hashes each input, and records its origin. Workers read those copies, not their origin paths. Missing referenced substance is a missing-input problem, not permission to search another run or recursively copy dependencies. Read-only provenance links need not resolve in the worker's accessible tree.

## 3. Draft criteria and uncommitted execution inputs

Add an explicit draft-file selector to `run gates`, mutually exclusive with catalog selection. For the first slice, accept a repository-local UTF-8 file conforming to the review-gate input contract; preserve its existing `gate_id` but identify it by repository path plus captured hash. It may be untracked. Reject unsafe paths, conflicting identities and an invalid declaration before launching. No scratch library, automatic catalog insertion or generic plugin registry.

A draft run is evidence-only by default: retain observations but do not publish over catalog current results. Draft status is inspected through its run, not by pretending it is a catalog member. A repeated trial uses the same criterion identity and bytes. Supporting operational inputs must be explicit; authorized authored-KB reading follows the selected reading contract. This slice does not broaden the generic reading scope for experimental higher-order drafts: a draft needing inbound search must have an explicit supported reading contract before execution, rather than silently overriding the current linked-file boundary.

Preserve `COMMONPLACE_LIBRARY_ROOT` as the existing library-selection mechanism, not a legacy result-format path. Calibration can continue to supply a scratch catalog through it, but that library must provide the new result type and resolved schema dependencies, and its wordings must use the new output contract. Library selection does not expand worker reading permissions: the current `gates.READING` wrapper already restricts grounding/consistency checks to linked files and one explicitly derived path. A higher-order wording requiring unrestricted neighbor or inbound search is not made compatible merely by placing it in a scratch catalog. Confirm its actual reading requirements against that wrapper; do not promise a bypass. No broader reading policy is added in this chunk.

For all first-slice operations, capture the exact instruction, conformance wrapper, output type and resolved schema inputs used. The latter is a bounded output-contract dependency set resolved by the existing type machinery, not recursive operational-evidence discovery. Bind the resulting contract fingerprint into call identity so schema changes cannot silently reuse an answer validated under another contract. Do not put changing execution ids or timestamps into the worker's criterion text.

Ordinary runs record the executable separately from the KB: installed package version/source location, source revision when available, and dirty/unknown state. Capture locally changed operation-specific prompt/wrapper bytes. Do not claim a package version describes uncommitted code or comprehensively archive a development environment during every review.

Fixture preparation is stricter. It must identify a retrievable executable source/build and dependencies, or require an explicitly supplied, retained substitute. Dirty executable code without a retained recoverable version blocks faithful reconstruction. A substitute creates a new documented baseline; it does not erase the original gap. No general dependency/environment manager is part of this slice.

## 4. Individual result contract

Use the prior type plan's single `types/review-result.md` contract for gates, conformance and critique. Its adapter completes worker output in memory, rejects worker-supplied reserved provenance, validates the complete candidate at its intended path, and writes the same completed candidate after acceptance. Explicit validation must reach artifacts under ignored state directories. Capture the type/schema contract and use normal type validation, not a separate approximate validator.

### Worker-owned content

- `type`, `findings`, `outcome`, and the operation's report body. One authoritative outcome in frontmatter; remove `## Result:` from new outputs.
- Gate/conformance `outcome`: `pass`, `warn` or `fail`. Critique: `report`, including when no attack survives. Inability to complete uses the existing worker-problem mechanism, not a fabricated judgment.
- Findings use the prior plan's `scope`, `quotes` and `reason`. Add a required `level: info | warn | fail` for gate/conformance findings, so INFO remains machine-readable. Critique findings have no forced severity; their level is absent. Operation kind controls this conditional requirement.
- Passage quotes must locate unique verbatim spans in captured assessed text; document/absence findings have empty quotes and explain the condition. WARN/FAIL require findings. PASS can still carry INFO findings; a genuinely empty list means no findings, not missing output. Do not manufacture a finding to carry “no proposal.”
- Preserve critique's central commitment, mode, attack outcome and required sections. Expose its attack outcome as a report-specific structured field with the current four alternatives, not as an overall pass/fail. The report body carries the strongest attack and how the note answers it. Structural checks cannot prove the attack is strong.

For Fable's verdict-kind draft wordings, replace the terminal `## Result:` instruction with frontmatter containing `type: types/review-result.md`, a `findings` list and `outcome: pass | warn | fail`. Each finding contains `level`, `scope`, `quotes` and `reason` as specified above. Keep proposal kind, force and grounds in the higher-order wording's report body; this chunk does not invent a new structured proposal schema. PASS/no proposal can use an empty finding list; WARN/FAIL need at least one finding. The controller supplies all provenance. The [review-result type](../../types/review-result.md) now declares this authoring contract.

Make anchor rejection diagnostic: name the finding index and quote, distinguish absent from ambiguous matches, and report the match count without substituting a paraphrase. Run inspection must expose each rejection reason, launches, content-validation retries and infrastructure failures separately. A shortened or paraphrased quote can invalidate the output even when its judgment is sound; the first real sweep must make that cost visible. Do not weaken exact matching or add a repair model implicitly.

Do not ask the worker for two independently authored versions of each finding. Structured findings are authoritative for mechanical extraction; the body can explain and synthesize them. The schema owns structural enums and requiredness. Runtime checks own expected criterion kind, exact anchors, field ownership and filesystem identity.

### Code-owned completion and publication

Preserve current note/criterion identities, freshness hashes, requested profile, observed model, run/launch and completion fields. Add exact target-capture reference/hash, observation reference, result-contract version/fingerprint and raw launch-output path/hash. These are not worker assertions.

Raw worker output remains byte-for-byte in its launch directory and stays citable. Completed typed result bytes differ because code adds provenance. Consumers must distinguish `raw-output-sha256`, completed-result hash and captured-target hash. The old empirical equality between current-result body and raw launch output is not a future protocol guarantee after structured frontmatter is introduced. Keep the old raw files and their citations unchanged.

Expose findings through a read-only JSON inspection surface so an improvement-run author need not parse prose or transcribe levels. Include outcome, structured findings, observation, exact target hash and raw-output locator/hash. Current-result replacement changes only the selected view; retained results and attempts remain accessible. No public accept step.

## 5. Freshness and legacy state

| Operation | Initial freshness decision |
|---|---|
| Catalog gates | Preserve current watched-parts target hash plus full criterion hash. |
| Type/collection conformance | Preserve current whole-text fallback and criterion hash. Preserve ADR 131 exclusions. |
| Critique | Preserve its existing whole-text target and criterion hash policy; qualify that linked context is outside it. |
| Explicit drafts | Evidence-only execution; do not skip from a catalog current result. |
| Compression checks, friction, premises, connect | Not implemented in this slice. On later admission, use `unassessed` until an explicit policy is adopted. Do not infer corpus freshness from target equality. |
| Higher-order draft | Experimental execution only under a supported reading contract; corpus-dependent freshness remains unassessed. |

Record wrapper/code/configuration changes for provenance without automatically staling every judgment. A contract-version incompatibility is a validation/reuse issue, distinct from watched-content freshness. A new run must not skip merely because an old-format result has matching content hashes. Use explicit format/reusability fields in status rather than calling a structurally incompatible result fresh enough to reuse.

The prior type plan's empty-store assumption is obsolete, but the operator rejects backward-compatibility work: agents tend to extend compatibility layers instead of the main implementation. **Support one result format and one implementation path.** Update current consumers together and remove the old result parser and footer protocol at cutover. Do not add a legacy reader, fallback parser, dual writer or automatic migration layer.

The operator selected archival and a fresh start at cutover. Inventory old state and archive current-result files outside the active result tree. Retire old runs from active discovery and resume; preserve their launch outputs and target copies as opaque, citable evidence. Prefer archival in place for cited run directories, with new runs in an explicit versioned namespace and active discovery restricted to that namespace. This keeps historical output paths and hashes intact without an old-format reader. Record the archived inventory and active namespace in a cutover receipt. Encountering an old-format file in active state is an actionable unsupported-format error, not a fresh result or a silent skip. Do not rewrite historical evidence or delete it. No automatic paid regeneration is authorized.

**Pre-cutover inventory, 2026-11-15:** a corrected read-only recount found 132 Markdown current-result files and 153 run option files under the review tree. Disposition under the operator's archive-and-start-fresh direction: archive all 132 active old-format results together at cutover, regenerate none up front, and let each note acquire new results on its next requested review. Recount immediately before acting; no paid sweep is a precondition.

The available `calls/run.json` records contain 613 request versions with attempts, all marked delivered, and no recorded reserved/running launches. This is not proof that every workflow finished: a controller may have stopped between calls, and process/lock state was not inspected. The single full-pass run (`types-give-agents-structural-hints-before-opening-documents/3fe0a68b3910`) has no publication manifest; its current packet is already `alternative-applied` by user authority after deletion, not awaiting approval. Two revision runs have publication manifests (`what-an-automated-reviewer-should-measure/1bac5e289ba8` and `position-and-proportion-set-what-a-reader-retains/0090306470d3`); manifest presence alone does not establish a pending approval. Before cutover, reconcile workflow endings, current approval keys and actual active processes, list every unfinished or awaiting-approval run, and obtain operator closure or abandonment of each. Do not equate a delivered call with a completed run.

New results use only the typed format. Do not keep two authoritative outcome channels. Status and project-summary readers consume only that format; inspection of old evidence is by its retained files, not a compatibility API.

**Existing runs:** archive and restart, rather than continue through the new runtime. Check for active controllers/workers before archival and stop cutover until they are settled; do not move state under a running process. A new runtime refuses old-format resume with an actionable message. New full-pass/revise runs use the new namespace so an old deterministic directory cannot block or replay into them. Preserve their recovery and approval semantics for new runs. Old answers, pending packets and approvals stay historical and confer no authority on a new invocation. Include those active views in the cutover inventory so they cannot block the fresh start. Do not redesign the workflows themselves.

## 6. Single-atom fixtures

Fixture creation selects one retained observation, not an entire sweep. Preparation makes no model calls. Reconstruct the recorded KB commit, overlay the exact captured target at its original relative path, and supply captured criterion, contract and operational inputs. An installed-project fixture must also retain the library content it needs, separately from the consuming KB's commit. A worktree's HEAD does not pin an editable installation or an external library.

Keep the fixture as a sealed local content baseline with a versioned manifest and digests, not just pointers to a disposable worktree. Retain a recoverable committed-tree archive plus overlays and explicitly supplied ignored sources, selected executable/dependency evidence and safe configuration copies. Never copy all shared report state or follow provenance links recursively. If the historical tree cannot be recovered, preparation stops unless the operator supplies and labels a substitute baseline.

Each trial gets independent mutable files, Git state, Workjig calls and result state. No previous answer or live current result is copied into executable state. Keep evidence for the parent observation out of the trial worker's operational inputs unless the criterion explicitly calls for it; fixtures normally test the note, not the earlier answer. Trial results never publish to the live KB's current-result view. Resume only reuses answers within that trial.

Use the same atom implementation as ordinary execution. Initially fixtures run one atom/target with pair grouping and one worker. If the source observation used a shared bundle launch, record the grouping change as a substitute baseline rather than claiming identical context. No automated repeated-run loop and no new composition engine.

### Configuration preflight and comparison limits

Preflight records the resolved executable, versions, selected library, effective requested flags, safe environment overrides, working directory and known automatically loaded configuration. Secret values are never retained; list omitted settings by safe role/name where possible. Missing required configuration blocks preparation; an explicitly accepted substitution is identified in the fixture. Never dump an unrestricted environment or credentials into manifests.

For the first fixture adapter, use the existing Claude Code path demonstrated by the reconstruction exercise. Ordinary harness support remains unchanged. Capture observed model/tool/MCP information when the harness emits it and attach it to the trial. If a different harness lacks this inspection support, refuse an assertion of equivalent effective configuration; support can be added when a consumer needs it.

Requested flags are not proof of effective tool availability. The reconstruction exercise showed that MCP readiness differed despite stable settings. Distinguish **content-reconstructed** from **effective configuration verified**. When launch evidence is missing or mismatched, retain the trial with that gap; do not silently count it as environment-matched. This does not require a paid readiness probe, and unknown provider internals remain explicit. No claim of OS-level filesystem isolation follows from a worktree or a prompt boundary.

## 7. Consumer and cutover map

| Consumer | Required preservation or bounded change |
|---|---|
| `criteria.py`, `gates.py`, CLI `run gates` | Existing selection, applicability, pair/bundle options and status exit behavior; capture once; version new runs; add draft and fixture selectors without a second execution path. |
| `full_pass._methods`, `gates.ask` | Continue returning individual results without publishing current state. Capture in-memory judged text. Keep report distinctions, shared call grouping, replay and final-only publication. Schema adoption must not bypass publication approval. |
| `full_pass` result-body/context use | Adapt reads to typed findings and report body; bind stable accepted provenance rather than a replay-time timestamp. Preserve result citations even though worker frontmatter is no longer part of prose body. |
| `revise.py`, `edits.py` | They use `results.note_parts`; do not change its normalization semantics to implement byte capture. Preserve edit guards, approval and compare-before-write. |
| `project_status.py`, review status | Preserve current verdict summaries, report outcomes, orphan detection and existing fields; add format/reusability information. Do not count retries or historical trials as current results. |
| Relocation and retirement | Current-result paths and orphan handling remain. Moving/retiring a target must not move or delete its historical captures and launch evidence. |
| Improvement-run findings and texts | Keep old output citations valid; expose new structured findings and exact input references. Defer removal of its duplicate texts until its own reader/retention contract is updated. |
| Installed KBs | Resolve project versus library identity as today, ship the new result type/schema, and run without this checkout, a second state repository or ignored workshop files. |
| Existing Workjig runs | Archive and start new runs in the new namespace; no migration or old-answer replay. Settle active workers before cutover. Preserve locks, launch acknowledgment and usage-limit recovery for new runs. |

Inspection baseline: `c660d2ec8ca3aad13ce4a06a97e1ac70d1d1933b`; inspected runtime sources and the adjacent type plan had no tracked changes when checked. Inventory basis: `src/commonplace/cli/review_workflows.py`, `review_workflows/{criteria,gates,results,full_pass,revise,edits}.py`, `headless/{jobs,harness}.py`, `lib/project_status.py`; scoped command/result searches in `scripts/` and `kb/instructions/`, including run-review-batches, warning fixes and retire-artifact. No external consuming projects were inspected. Recheck caller inventory at implementation time; no guarantee is made for unpublished external parsers.

## 8. Acceptance tests for the implementation commission

Use fake harnesses and independent temporary repositories. These tests establish execution and evidence integrity, not judgment quality.

| Case | Required assertion |
|---|---|
| Uncommitted target | Capture differs from HEAD; worker input equals capture exactly; original relative path is recoverable. CRLF and no-final-newline cases preserve exact bytes without changing the selected freshness normalization. |
| Dispatch race | Edit the live target/criterion after capture; worker and result remain bound to captured inputs, and status/guard reports the appropriate live difference. |
| Draft identity | Run an untracked gate twice without changing `gate_id` or setting a scratch library; independent runs retain both outputs and cannot replace a catalog result. |
| Installed library | KB commit and library/executable identities differ; captures and fixture reconstruction use the correct library, not the main checkout's editable source by accident. |
| Input boundary | Missing explicit input, unsafe path, symlink escape or hash mismatch stops before launch. A provenance reference never triggers recursive copying. Worker prompt uses only supplied operational copies. |
| Typed result | Pair and existing bundle calls validate individual outputs against one contract. Wrong type/kind, spoofed metadata, duplicate YAML keys and invalid enum are rejected. |
| Findings | INFO/WARN/FAIL levels are mechanically recoverable; PASS+INFO and empty findings are represented honestly. Critique's no-surviving-attack variants remain completed reports without forced severity. |
| Anchors | Invented or ambiguous passage quotes fail against the capture even if they match a changed live file. Document/absence findings need no invented anchor. |
| Schema identity | Changed type/schema invalidates reuse, including within one process; retained raw output remains untouched. Saved and in-memory candidates receive the same validation. |
| Attempts and interruption | Rejected, timed-out and interrupted attempts remain; resume neither loses them nor increments the observation count. Usage-limit, locks and acknowledgment follow existing Workjig behavior. |
| Replay | Resume uses frozen first-slice standalone request/captures and stable completion metadata. Explicit retry preserves superseded accepted output. Changed caller inputs in full pass do not silently overwrite old evidence. |
| Publication crash | Stop between retained-result creation and current-result write; resume finishes idempotently, with no current pointer to missing evidence. |
| Replacement | Second ordinary execution replaces current result but leaves the first observation, launch output and hashes readable. Concurrent current writes retain existing last-writer behavior; each historical result survives. |
| Clean cutover | All supported consumers read the new format. Old active results and old-format resume fail clearly without deletion or fallback parsing. Archived launch outputs and their exact hashes remain unchanged and citable. |
| Fixture preflight | Missing commit/library/ignored input/executable evidence fails or requires a named substitute; content archives and all overlays verify by hash. No recursive report-tree capture. |
| Independent trials | Two fixture invocations make fresh calls with independent mutable state and no freshness skip; resuming either replays only within it. Neither modifies live current results. |
| Configuration gap | Fake differing or absent tool/MCP evidence prevents an environment-equivalence claim while preserving completed outputs. Secret test values do not appear in retained manifests or copied safe config. |
| Existing consumers | Full-pass final-only result publication, pending packets, exact approval, conflict guards, revise bounds, status summaries and relocation invariants still pass. |

Run local coverage according to [test selection](../../../tests/README.md): general, review-workflows, relocation, validation, docs and relevant installation tests for this slice. Shared headless changes additionally require headless and analysis consumer suites, including relevant slow tests. Foundational parsing/type-resolution changes require the full fast suite; packaging changes require the full suite and installation checks. Run `uv run ruff check .`. Validate the type and representative completed results explicitly. No tests or paid calibration were run during this design investigation.

## Implementation authorization still required

The operator has selected archival and a fresh start without backward-compatibility layers. The operator accepted this implementation commission's specification. Perform the recorded cutover only when the new implementation is ready and active workers are settled; no archival was executed during this design work. The new runtime does not reinterpret old results or runs. The first slice does not change judgment wording beyond the declared result-format/anchor requirements, ship other report atoms, redesign full-pass/revise, or remove improvement-run text copies.

Remaining uncertainty is stated rather than hidden: semantic effects of the new result format, completeness of effective harness evidence, and external callers not inspected here. These limit what the implementation may claim; they do not require a general operation framework or another broad design phase.
