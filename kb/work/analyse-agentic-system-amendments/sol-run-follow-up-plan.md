# Sol run follow-up plan

## Commission and completion

Commissioned by the operator on 2026-10-03: plan the remaining procedure
repairs from the stopped Graphiti Sol run while isolated analysis environments
are being developed separately. This document authorizes planning, not live
method edits, a new model run, or recovery of the stopped run.

The intended result is fewer avoidable input-discovery, quotation, formatting,
and classification errors without weakening source grounding, independent
review, or publication safeguards. This planning commission is complete when
scope, evidence prerequisites, acceptance criteria, and decision returns are
explicit. Implementation, including evidence-retention step 0, needs a separate
operator commission. For a subsequently commissioned implementation, completion
means each authorized item has an implemented and checked disposition or an
explicit reason for deferral. A live analysis needs a further commission.

Do not change the isolation owner's files or overlap its command/environment
setup work. Do not modify the stopped run, retained sets, source checkout, or
raw session logs. Preserve the existing 24 KiB read budget; another budget
experiment is outside this plan. Keep independent analysts and reconciliation.

Implementation target after authorization: `/home/zby/llm/commonplace`, on
`main`, or a new development worktree branched from its then-current committed
revision. Do not implement in the stopped run's `commonplace-pi-subagents`
worktree or assume its branch matches `main`. Recheck ownership and status
before writing; the isolation task may have changed since this plan was read.

## Evidence boundary

Run: `AAS-2026-10-03-graphiti-05`, in
`/home/zby/llm/commonplace-pi-subagents/kb/agentic-systems/reports/state/`.
Coordinator and completed workers used `openai/gpt-6.1-sol`.

The local session evidence is:

```text
/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace-pi-subagents--/2026-10-03T08-49-33-387Z_01a100f4-4ecb-7313-8182-9eae6f2c8fec.jsonl
```

Diagnostic anchors in that JSONL:

- Line 25, boundary worker message 57: missing quotation selection key; the
  worker then consulted `commonplace-quote --help` and repaired the JSON.
- Line 33, epistemic worker messages 85 and 139: nonexistent collection
  contract and guessed source path.
- Line 33, memory worker messages 97, 121 and 127: the same nonexistent
  collection contract, another guessed source path, and empty quote text.
- Line 41, correction worker message 137: malformed frontmatter indentation,
  subsequently repaired and validated.
- `jobs/reconcile-0/reconcile-0.md`: under `Returned to the memory analyst`,
  item 1 returns the decay classification and item 2, **Assess entity and
  relationship properties separately using the already declared epistemic
  parts**, returns the combined property-part assessment. The reconciliation
  also contains epistemic identifier and ledger amendments.

These seven tool errors were recovered inside their workers. Reconciliation
findings are reviewer findings, not independently reverified source conclusions
in this plan. The run stopped before final verification/publication and was
confounded by changing code during execution. It is not a controlled model
comparison or an accepted Graphiti analysis.

## 0. Retain the diagnostic evidence before implementation

Local evidence is not guaranteed to survive cleanup. This is a prerequisite
for items 1–6 and must finish before cleanup or an observation-driven method
change. Retain a bounded trace record alongside this plan, following the
workshop's [second-run trace evidence](./second-run-trace-evidence.md) precedent.
Record the session's exact-byte SHA-256, line count, model, parent-line and
embedded-worker message anchors, and selected diagnostic calls/results. Hash
and retain the relevant reconciliation excerpts, including returned items 1
and 2. Preserve the distinction between recovered tool errors, reviewer
findings, method drift, and an incomplete run.

Acceptance: all seven error anchors and the named reconciliation findings
are checked against their original files, the inventory hashes reproduce, and
the bounded excerpts support each proposed repair without needing raw log
survival. Do not copy entire conversations into tracked KB content. If any
original is unavailable, record that gap and return the affected repair for
decision rather than claiming verified observation evidence.

## First implementation scope

### 1. Supply the enclosing collection contract (deferred to the split)

**Observed problem:** both parallel analysts guessed
`kb/agentic-systems/reports/COLLECTION.md`, which does not exist. The root
writing rule requires the destination's collection contract, but the invocation
does not supply its exact path.

**Disposition, operator decision 2026-10-03:** do not implement this item
under this plan. Supplying the current 13.7 KB contract to every job would
make its full reading cost routine. The
[report-collection split](./report-collection-split-proposal.md) creates a
small analysis-only contract, and the relocation supplies that contract to
every job packet as a `read-first` path and job dependency. Until then the
packets stay as they are. Do not add a worker exemption from the reading rule.

The requirement carries over to the split's implementation:
`AnalyseAgenticSystem.job()` supplies the contract by absolute path, its bytes
participate in job dependencies, and tests establish this for every job and
for the `scripts/analyst_trial.py` route, which uses the same job builders.

### 2. Make the quotation batch interface explicit

**Observed problem:** the boundary worker inferred a batch shape using
`source-path` without `key`. The memory worker submitted an empty selection
produced by source extraction. Both were correctly rejected by the helper.

**Result required:** put one valid `{key, source_path, text}` batch example
beside `--selections` in the shared worker rules. State that CLI option names
and JSON property names differ. Use scratch for selection and result files.
Require reading every returned key's status: insert a supplied `citation`,
choose an eligible occurrence for `candidates`, and resolve `error` before
relying on that selection. Repair unresolved entries or exclude their claims
with the resulting evidence limit; partial success is not success for every
entry. Text extracted by a worker must remain verbatim source material.

`generate_quote_batch()` in `src/commonplace/lib/quote_generation.py` already
rejects missing keys and returns per-key errors for empty text. Reuse those
checks; do not add a duplicate pre-invocation validator. Check the documented
example against the helper and retain missing-key and empty-text negatives.

The helper currently ignores misspelled `source-path`, treating `source_path`
as absent and giving a misleading missing-path error. Add a narrow diagnostic
for that known misspelling, naming the expected `source_path` property. Preserve
per-key failure behavior when a key is valid. Test the typo, valid Git entries,
and capture entries with omitted/null `source_path`. Do not introduce blanket
unknown-property rejection, weaken matching, or add a quotation protocol.

### 3. Reduce guessed-path reads

**Observed problem:** analysts inferred two source paths that were wrong at
the frozen commit.

**Result required:** shared source-reading guidance distinguishes supplied
paths from inferred paths. Supplied paths can be read directly. Locate an
inferred filename through a scoped tree or file search before opening it; an
absent guessed path is not evidence that the mechanism is absent.

Keep discovery bounded to the registered source. Do not require a full tree
inventory before every read. Review the actual failed paths as examples, but
do not hardcode Graphiti-specific filenames into generic instructions.

Acceptance is wording review against the two failure cases and supplied-path
fast path, plus KB validation. No deterministic test can establish that a
model will perform the discovery; adherence is measured in a later live run.

## Bounded follow-ups

### 4. Safer structured-frontmatter repair

The correction worker's manual edit produced invalid YAML. Inspect that edit
and the existing generation/repair instructions. Prefer parsing and serializing
structured frontmatter, preserving the body and unrelated metadata, rather
than hand-splicing nested indentation. Validate the exact final file after any
repair, as the memory job already requires.

Before adopting an instruction, demonstrate on a scratch fixture that nested
profile edits preserve other fields and body bytes. Do not build a general
frontmatter editor unless existing tooling cannot achieve that result. Stop
for replanning if this requires a new authoring interface or metadata policy.

### 5. Targeted semantic submission checks

Reconciliation returned two memory findings: `decay` was interpreted as
requiring time-based policy, and property mechanisms with different updates
were combined. It also flagged an inaccurate epistemic checkpoint identifier.

The `decay` finding concerns the memory comparison profile. The operator
decided on 2026-10-03 to move the profile to its own job; see the
[comparison-profile job proposal](./comparison-profile-job-proposal.md). Do
not repair profile classification in the memory job under this plan. The rule
"classify from the supplied definitions without extra conditions" goes into
the profile job's instruction.

Amend only the remaining job checks: assess parts separately where consumers,
admission, or update semantics differ; verify exact code identifiers against
source.
Inspect the existing type/job requirements first and strengthen their
application rather than duplicate long contract passages.

Accept a small pre-submission check, not a new analytical stage. Identity
and containment amendments arising from independently produced lens records
remain legitimate reconciliation work; their count is not a failure metric.

### 6. Decide claim-column validation from a bounded probe

The reconciler flagged five ledger cells containing evidence references or
non-claim IDs in `claim IDs or none`, as named in
`kb/agentic-systems/types/agentic-system-epistemic-report.md`. The parser is
`epistemic_ledger_errors()` in `src/commonplace/lib/agentic_ledger.py`; it
currently checks syntax and controlled function/status values. Investigate
whether it exposes this column reliably. A candidate check would accept
permitted claim references or `none` and reject other reference categories.

Before adoption, test the observed malformed cells against valid ledgers,
including cells with several claims and any permitted explanatory syntax.
The warrant is column-category conformance, not factual truth or relevance.
If this needs a grammar change or creates false positives, retain the cases
and return the design choice to the operator. Do not broadly tighten shared
record parsing under this item.

### 7. Small repairs found by the complexity measurement

Added on 2026-10-03 from the
[complexity measurements](./split-drafts/complexity-measurements.md). These
touch neither the collection contract nor the memory profile.

- **No-ranges rule.** The rule against ID ranges is stated once, in the
  records contract, and restated only in the two verification job files.
  Range lapses then appeared in reconcile and synthesize. Restate it in those
  two job files, in the wording the verification files use.
- **Unsupplied definitions.** Synthesis needs the self-improving-system
  definition and record verification needs the boundary contract's
  boundary-kind definitions; neither packet supplies them. Add them as
  `read-first` inputs, and check the packet size against the read budget.
- **Link rule against validator.** The measurement reports, from reading
  code, that the set-member link validator refuses links to `kb/sources/`
  and `kb/notes/` that the contracts permit. Confirm by test before changing
  anything, then make the rule and the validator agree.

Not included: whether the root vocabulary rule binds workers. It accounts for
every remaining model-resolved reference in the measurement and has no
recommendation yet; return it to the operator.

## Verification and integration

Each repair must name its instruction or code consumer, update affected
producers and tests together, and retain a concise implementation result here.
Local means remain open within the stated scope. Parallel contributors need
disjoint ownership; changes to shared worker rules or invocation construction
must be coordinated rather than merged from independent rewrites.

For code changes, run relevant deterministic cases, `uv run pytest -q`, and
`uv run ruff check .`. For instruction-only changes, acceptance is wording and
composition review plus targeted `commonplace-validate` checks; do not invent
behavioral test claims for prose. A fixture passing demonstrates interface
behavior, not model adherence or analytical truth. Do not stage the isolation
task's changes with this work.

Before a separately authorized live trial, integrate committed method changes
with the isolated-environment work. Freeze that revision and its read budget
before opening the run. Keep the source revision and model recorded. Track
wrong-path reads, malformed quote batches, empty selections, YAML repairs,
returned classification findings, and integrity blocks separately. Zero
recurrence in one run is bounded evidence, not proof of elimination.

## Exclusions and decision returns

Isolation, package ownership, method-drift guards, sandbox enforcement, native
TypeScript orchestration, and cross-implementation recovery remain separately
owned or uncommissioned. This plan does not reopen them. It neither resumes
the stopped run nor authorizes a new analysis.

After items 2, 3 and 7, reassess whether the evidence justifies all bounded follow-ups.
Return to the operator before adding workflow stages, changing comparison
vocabulary, broadening semantic automation, or expanding the implementation
scope. A partial result must name completed repairs and remaining items.
