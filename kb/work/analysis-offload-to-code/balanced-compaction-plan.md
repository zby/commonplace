# Plan: balanced compaction of analysis instructions

- **Commissioned:** 2026-10-01, by the operator: propose concrete compressions and measure their savings while another agent owns the live analysis skill.
- **Purpose:** reduce repeated and unnecessarily prescriptive reading while preserving analytical coverage, evidence standards, interoperability and recovery.
- **Status:** plan and candidate text only. No live skill, instruction, type or code is changed; no trial has run.
- **Baseline:** commit `96185f2c0ce3d76cce22a0866a0ac00df5626992`, including the committed reconciliation/synthesis split. All measured live files matched that commit at capture.
- **Scope:** seven bounded text changes below. Excludes new tools, packet generation, skeleton generation, changing report fields/enums, reducing required coverage, and changing the workflow graph.
- **Coordination:** implementation waits until the current skill owner has finished. Rebase the candidates and recompute the numbers if any baseline file changed; do not apply them over concurrent work.

## The balance

A worker receives a short mission, supplied content contracts, explicit authority and acceptance, and a few reminders aimed at observed failures. It chooses search strategy, investigation order and depth within those obligations. Required classification order, output grammar, source scope, ownership and return protocols remain fixed.

This applies the [instruction type](../../types/instruction.md) and the [writing skill's directive-text rule](../../instructions/cp-skill-write/SKILL.md). It does not rely on the model reconstructing a methodology from the name Auftragstaktik. The [Luna follow-up](./parameterized-luna-followup.md) is the reason to keep explicit checks for omitted cleanup/evaluation routes, unsupported inspection claims, heterogeneous objects, and incomplete tool reads.

The five linked instruction candidates are complete replacement texts at their intended live paths. Their frontmatter, bootstrap and parameter tables are preserved. Their workshop location makes them non-operative; no workflow points to them.

## Exact proposed file reductions

All figures are UTF-8 bytes with LF line endings, calculated from concrete candidate text rather than target word counts. Paths beginning `jobs/` and `SKILL.md` are under `kb/instructions/analyse-agentic-system/`.

| Change | Live file | Before | Proposed | Saved | Reduction |
|---|---|---:|---:|---:|---:|
| C1 | `jobs/worker-rules.md` | 5,571 | 5,200 | 371 | 6.7% |
| B1 | `jobs/boundary.md` | 4,756 | 4,485 | 271 | 5.7% |
| R1 | `jobs/runtime.md` | 2,579 | 2,271 | 308 | 11.9% |
| M1 | `jobs/memory.md` | 4,191 | 3,388 | 803 | 19.2% |
| E1 | `jobs/epistemic.md` | 4,458 | 3,238 | 1,220 | 27.4% |
| O1 | `SKILL.md` | 5,928 | 4,038 | 1,890 | 31.9% |
| T1, optional | `kb/types/agentic-system-epistemic-report.md` | 12,505 | 12,203 | 302 | 2.4% |

C1–O1 remove 4,863 bytes from always-delivered files. T1 adds 302 bytes of savings, for 5,165 total. O1 relocates rationale to a maintenance reference, so its gain is in execution reading, not equivalent deletion from the repository. No savings are claimed for new reconciliation or synthesis job text.

## What each compression changes

### C1: consolidate command guidance, retain the concrete read example

Candidate: [worker rules](./balanced-worker-rules-candidate.md).

Replace only `## Commands`, from that heading up to `## Sources`. It shrinks from 1,469 to 1,098 bytes. Consolidate the two command-sequencing statements and repeated status/reading explanations. Keep:

- Separate file-preparation and acceptance calls, or dependent `&&`; pipeline `set -o pipefail`.
- Full returned objects, stdout/stderr and final exit status; wait for running commands and do not let later success erase failure.
- The concrete Codex bounded-read example.
- Separate files, successive ranges to EOF, inspection of both inner and outer truncation, smaller rereads before advancing, and the fact that the two token budgets are independent.
- Apply the same discipline to source searches and reads; report checks only after running them.

All authority, source, quotation and prior-analysis rules remain byte-for-byte unchanged. This is wording consolidation, not delegation of read safety.

### B1: state Git source-freezing obligations once

Candidate: [boundary](./balanced-boundary-candidate.md).

Replace only numbered item 2 under `## Freeze the sources`: 849 → 578 bytes. Remove the explanatory story about a clone without checkout and combine the repeated description of what later workers read. Keep the exact permitted directory, ignore check, origin verification, full revision, fetch/detached checkout, materialized files, clean-status acceptance and prohibition on discarding changes. The candidate explicitly checks an existing checkout for local changes before changing it.

The allowlist, immutable-capture requirements, scope decisions, frontmatter and disposition handling remain unchanged. No extra Git mutation authority is introduced.

### R1: mission and coverage instead of a seven-step investigation order

Candidate: [runtime](./balanced-runtime-candidate.md).

Retain the purpose of supplying the specialists' runtime baseline. Delegate investigation order and selection of forcing cases to the claimed work and inspected guarantees. Remove the suggested count of two to four cases; the obligation becomes the smallest set needed to challenge the load-bearing guarantees. This is an intentional change in permitted means, requiring a trial.

Keep ordinary invocation, the alternate-path checklist, guarantee coverage, capability/grant/isolation separation, relevant operational dimensions, parametric components, admission mechanisms, memory ownership, read-back checks, execution-evidence limits and citation acceptance. The runtime type and shared contracts continue to supply fields and report content.

### M1: remove report-order investigation and consolidate inherited rules

Candidate: [memory](./balanced-memory-candidate.md).

Remove “Work through the report's sections in the order the memory report type gives.” The type still governs the resulting report. Delegate inspection order and depth within the memory boundary; retain source-native write/read-back tracing and challenges to source claims.

Keep explicit CLI/hook/tool/service coverage, evaluation/cleanup/rejection/withdrawal through later consumers, local support for profile citations, overlap dispositions, canonical-split requests and correction-round inputs. Add a concise reminder to distinguish directly read source from supplied findings; this rule already exists in the type and addresses an observed failure.

Correction still means a whole replacement report. Surviving IDs retain referents; new records get fresh numbers; dropped numbers are not reused. Keep validation, repair, updated check results, final revalidation and the publication-owned quotation check. No current Commonplace recommendations enter the report.

### E1: mission and obligations, with known-failure reminders

Candidate: [epistemic](./balanced-epistemic-candidate.md).

This is the earlier intent candidate with an additional explicit reminder about direct inspection versus supplied findings and routes omitted by the runtime. The reminder spends 110 bytes deliberately; its reduction is 27.4%, not the earlier candidate's 29.8%.

Remove the six-stage production sequence and repetitions of delivered type requirements. Delegate search, inspection order and depth. Retain the concrete coverage checklist, unsupported-claim branch, storage-only completion branch, target/domain before evaluator judgment, parametric uncertainty, canonical-split flags, quotation support, peer isolation, validation and semantic acceptance.

The omissions have named owners:

| Omitted repetition | Supplied owner |
|---|---|
| Required report blocks, final order and conclusion relevance | Epistemic type, Required blocks |
| Object/function separation and unchanged-content routes' authority | Epistemic type, inventory and ledger definitions |
| Sequential content-edge assessment, classification order and indeterminate cases | Epistemic type, Assessment limits and content/update definitions |
| Profile-independent canonical identity, annotations and overlap handling | Shared record contract |
| Write scope, source access limits, problems and prior-analysis exclusion | Worker rules |

The exact content-classification checking order remains binding even though investigation order becomes discretionary. No taxonomy value, required field or assessment limit is removed.

### O1: load theoretical rationale only for method maintenance

Move the existing 11 `rests-on` footer links and their explanations into `kb/reference/agentic-analysis-method-rationale.md`, retaining their meanings and correcting their relative paths from `../../notes/` to `../notes/`. Give the new reference a title, description and maintenance purpose; add no execution requirement there.

Replace the skill's final horizontal rule and footer with exactly this text, including the preceding blank line and a trailing newline:

```markdown

---

When revising this method, read [analysis method rationale](../../reference/agentic-analysis-method-rationale.md).
```

The 2,006-byte footer body becomes a conditional reference; including the replacement pointer, the skill saves 1,890 bytes. Keep every operational paragraph and the driver unchanged. The 11 dependency links remain available to the maintainer, with an explicit trigger to read them. This is a routing change, not delegated analytical judgment.

### T1: optional tightening of the epistemic type's assessment limits

This is lower priority: 302 bytes saved is small relative to the semantic review cost. Replace only `## Assessment limits` up to `## Required blocks`, using the text below. The section shrinks from 2,094 to 1,792 bytes; all other type text, schema, terms, fields, enums and templates stay unchanged.

Check preservation clause by clause before adoption. In particular, keep these distinct: accepted ampliative claims versus candidates; architecture versus observed operation; artifacts versus route provenance; outcome success versus causal explanation; formal validity versus source truth; continuation versus epistemic warrant; operational scope versus product failure. A shorter paraphrase that conflates any pair fails this change.

<!-- T1 replacement begins -->

```markdown
## Assessment limits

Assess each content edge separately. Apply these limits:

- Entailed derivation needs warranted premises and a checked interpretation
  or formal domain. Novelty, fluency and plausibility establish only candidate
  generation. A produced accepted ampliative claim needs evidence-consuming
  acceptance decision naming criterion, intended use and scope; retention, retrieval,
  reshaping and operational use do not suffice. Import is acquisition, not
  production; acceptance is fallible and integration does not establish it.
- Keep architecture, activation conditions and observed operation separate.
  Doctrine or implementation alone does not establish observed operation. A candidate
  without route provenance/trace links establishes availability only, not its
  production, checking or acceptance route. Results without consequential
  consumers have no implemented force; absence needs no invented evaluator.
- Bound a check's license by target, contrast, domain, horizon and route.
  Success does not establish process, explanation, replay safety, transfer or
  component effects; reconstructed routes do not prove outcome provenance.
  Consequence fit does not warrant mechanism or transfer. Formal validity
  does not establish source truth, encoding fidelity, omitted premises or
  claims outside the checked domain. Freshness is not endorsement, nor
  continuation epistemic warrant. Shared source-contract limits govern
  causal attribution.
- Operational or lab-tracking scope is not product failure; compare broader
  knowledge-production claims with routes. Require no particular natural-language claim
  format, proposal loop, Commonplace storage model or universal ontology.
  Keep heterogeneous routes' evaluators, statuses and authorities separate.

```

<!-- T1 replacement ends -->

## Savings for each worker

These are the actual constructor dependencies at the baseline commit: job plus worker rules and declared shared/member contracts. The orchestrator row is skill plus driver. Figures exclude AGENTS.md, launch bindings, earlier reports, source reading and tool outputs. No proposed change alters those exclusions or makes each file safe to read in one tool result.

“Core” includes C1, B1, R1, M1, E1 and O1. “With T1” additionally applies the optional type edit. A future edit that changes the candidate text changes these numbers.

| Worker | Baseline bytes | Core proposed bytes | With T1 | Full saving | Full reduction |
|---|---:|---:|---:|---:|---:|
| Boundary | 15,814 | 15,172 | 15,172 | 642 | 4.1% |
| Runtime | 27,163 | 26,484 | 26,484 | 679 | 2.5% |
| Memory | 38,669 | 37,495 | 37,495 | 1,174 | 3.0% |
| Epistemic | 38,140 | 36,549 | 36,247 | 1,893 | 5.0% |
| Reconciliation | 56,892 | 56,521 | 56,219 | 673 | 1.2% |
| Record verification | 55,696 | 55,325 | 55,023 | 673 | 1.2% |
| Synthesis | 31,624 | 31,253 | 31,253 | 371 | 1.2% |
| Synthesis verification | 31,083 | 30,712 | 30,712 | 371 | 1.2% |
| Orchestrator | 10,513 | 8,623 | 8,623 | 1,890 | 18.0% |
| **One first pass, summed reads** | **305,594** | **298,134** | **297,228** | **8,366** | **2.7%** |

The last row assumes one launch of each of the eight worker roles and one orchestrator load, without retries/corrections. Shared files count once per consuming worker. It is not a prediction of total context consumption or billed tokens. Core alone saves 7,460 bytes, or 2.4% of those fixed reads. T1 saves another 906 bytes because three workers consume the epistemic type.

## Implementation and evaluation sequence

1. **Establish a stable baseline.** After the current skill owner's work ends, compare all target files and the job constructors with the pinned commit. Rebase changed passages, preserve the split record/synthesis responsibilities, and regenerate both tables. Hash all delivered files, run inputs and candidate text. Keep shared contracts, AGENTS.md, model, reasoning/tool settings, source pin and runtime input fixed within each comparison. Do not count the other agent's reductions as gains from this plan.

2. **Review the preservation map.** For each deletion, identify its retained sentence or declared inherited owner; otherwise classify it as a deliberately delegated choice. Check every known-failure reminder against the trace evidence. Confirm all candidate `read-first` dependencies are actually delivered. Any lost obligation or ambiguous inheritance blocks that candidate, even if its byte reduction is attractive.

3. **Apply the routing/wording changes independently.** O1 moves only rationale and retains all 11 links under a maintained reference; check that the new file is available through the skill's actual installation/read path. B1 retains every source-freezing invariant and exact interface. Validate the affected documents and run required instruction/contract tests. Keep each change separately revertible. Prepare C1, but evaluate its effect on reads separately from job compaction.

4. **Pilot E1 before changing more analytical instructions.** Use fresh isolated workers, with no earlier report, parent repair or trial-result contamination. Compare baseline and candidate instructions on the frozen Instinctual Memory boundary used in the Luna follow-up, or an equivalent retained case if those inputs are unavailable. State full material-route coverage as the evaluation dimension in both commissions; the earlier analysis itself stays withheld. Run two fresh workers per arm: four worker executions. If their results disagree materially, add one fresh pair and treat unresolved variation as inconclusive. Then screen a second frozen target with a thin/no-knowledge-production boundary, one worker per arm. Total: six to eight epistemic executions. This is a regression screen, not a statistical demonstration of equivalence.

5. **Extend only after the epistemic pilot succeeds.** Screen M1 and R1 separately with one fresh baseline/candidate pair each, changing only that job. For M1, inspect memory maintenance, later consumers, profile coverage and overlap. For R1, choose a boundary exposing a meaningful alternate path around a claimed guarantee, and check forcing-case adequacy rather than a fixed count. Add repetitions only for observed disagreement or regressions; they change the trial budget.

6. **Test C1 as its own factor.** With the accepted job versions fixed, run one baseline/candidate worker-rules pair for memory and one for epistemic. Inspect actual tool deliveries for complete reads, recovery of both truncation layers, visible failed statuses and accurate inspection claims. Do not infer equivalence merely from valid final Markdown. Steps 4–6 total 14–16 analyst executions before any extra disagreement-driven repetitions.

7. **Decide T1 separately.** Prefer to defer it unless the 302-byte reduction earns its review cost. If pursued, check every old clause against the replacement, using both the type and its shared contracts. Run one held-input epistemic pair with only T1 changed; that adds two analyst executions. Restore any qualification whose removal or paraphrase changes a finding. Keep the original type if evidence is ambiguous.

8. **Check integration and commit accepted changes.** Run a full workflow on one frozen target after the individually accepted changes are combined. A successful first pass launches eight worker jobs; record actual retries and corrections rather than assuming none. Validate all changed contracts/instructions, run required tests, check publication and comparison consumers, and commit only accepted changes. Record exact final bytes and outcomes; rejected candidates remain workshop evidence until closure.

Use the existing `scripts/analyst_trial.py` preparation path for isolated analyst work. It reads method files from the working tree, so use controlled isolated copies and verify their hashes at preparation and completion; do not run comparisons against a checkout another agent is editing. The prepared invocation is not a full runtime-context snapshot: record inherited instructions, model and harness settings as well. The trial controller may use earlier audit findings to score coverage; workers may not receive those findings.

## Acceptance, stopping and recovery

The success condition is smaller delivered text with preserved useful analysis, not merely fewer bytes or a passing validator. Judge each candidate against the same source-operation inventory and evidence boundary:

- Every material operation is accounted for as inspected, justified exclusion, or explicit unassessed scope with its prevented conclusion. A skipped branch cannot silently support a system-wide negative.
- Direct-inspection claims agree with delivered source contents. Search hits and supplied runtime findings remain distinguishable from direct reads.
- No lost consequential function, collapsed heterogeneous object, unsupported classification/status, broadened license, unresolved ID, peer contamination or write-scope violation.
- The known cleanup/evaluation case is assessed or explicitly limited; its name alone does not establish factual checking or knowledge production.
- Final outputs pass the actual workflow acceptance checks. Compare retries, blockers and source coverage as well as document validity. Matching a defective baseline is not success.
- A pilot regression restores the responsible reminder or original passage before another trial. Record the cause and revised byte count. If controls fail too, the comparison is inconclusive; fix the evaluation or baseline issue without attributing it to compaction.
- Missing frozen inputs, differing delivered dependencies, concurrent method changes or inaccessible runtime settings stop the comparison and require a new matching baseline. Do not substitute a live source or silently broaden scope.

The implementation owner retains integration and acceptance. Workers choose investigative means within the existing source and output authority; neither the compact brief nor the trial expands it. The main implementation decisions left open are target selection beyond the named failure case, search tactics, forcing cases, and whether optional T1 is worth pursuing. Evidence from each bounded pilot decides the next step.

## Reproducing the arithmetic

For each complete candidate, compare its UTF-8 byte length with `git show 96185f2c0ce3d76cce22a0866a0ac00df5626992:<live-path>`. For O1, retain the skill through the paragraph before its final horizontal rule, then append the exact replacement above. For T1, replace the interval beginning `## Assessment limits` and ending immediately before `## Required blocks` with the fenced replacement text, preserving its trailing blank line. These intervals and all five complete candidates account for every measured edit.

Sum unique declared method paths per job from `src/commonplace/lib/agentic_workflow.py`: job instruction and worker rules, then that constructor's `extra` list. Do not add run inputs, count the same file twice within a job, or amortize a shared file across fresh workers. Record verification uses `RECORD_CONTRACTS`; synthesis and its verification use `SYNTHESIS_CONTRACTS`. Recalculate if those lists change.
