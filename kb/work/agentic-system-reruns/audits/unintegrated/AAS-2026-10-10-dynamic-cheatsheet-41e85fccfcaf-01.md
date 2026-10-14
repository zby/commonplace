# Audit: Dynamic Cheatsheet alternative 41e85fccfcaf

## Decision

**Integrate with recorded limits** as an assessment of this candidate's bounded content readiness, not a recommendation to replace the incumbent. No consequential unqualified defect was established in the inspected scope. **No replacement reason found**: retain the incumbent unless the operator separately chooses otherwise. This is alternative evidence, not new corpus coverage. No integration occurred.

## Identity and scope

- Run: `AAS-2026-10-10-dynamic-cheatsheet-41e85fccfcaf-01`.
- Auditor: `audit-dynamic-cheatsheet-41e85fccfcaf`; independent Pi worker, `openai/gpt-6.1-sol`, commissioned medium effort; `PI_MODEL=gpt-6.1-sol` observed.
- Frozen method: `1a20deff31df32a332835974cf1a61d3b58fc8a6`.
- Worktree (`W`): `/home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-41e85fccfcaf`.
- Publication (`P`): `W/kb/agentic-system-analyses/retained/dynamic-cheatsheet`.
- Run evidence (`R`): `W/kb/agentic-system-analyses/state/AAS-2026-10-10-dynamic-cheatsheet-41e85fccfcaf-01`.
- Source (`S`): `W/related-systems/suzgunmirac--dynamic-cheatsheet`, identity `https://github.com/suzgunmirac/dynamic-cheatsheet`, revision `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`. HEAD matched; `git status --short` was empty.
- Method: discrepancy-led comparison of public overview/synthesis, historical leads and incumbent; targeted checks of admission, scoring order, saved guidance, resume and execution containment. No target execution, source acquisition, delegation or state-writing inspection.

## Historical and incumbent boundaries

Read the June account at `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md` and the later account at `kb/agentic-systems/reviews-archive/dynamic-cheatsheet.md`. The account moved outside agent-memory-systems; the archive records run `AAS-2026-09-27-dynamic-cheatsheet-04`. Both name the same source revision, but are coverage leads, not current authority.

The candidate retains the important mechanisms: whole-text replacement, six context approaches, automatic later supply, prompt-only semantic maintenance, scoring after admission, non-enforced context budgets, provider opacity and host execution risks. It corrects the June account's implication that both cheatsheet tags are required. Omission of Commonplace borrowing advice is not a system-coverage regression.

Compared current origin `kb/agentic-system-analyses/retained/dynamic-cheatsheet/overview.md` and `synthesis.md`, incumbent `AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01`, at the same source revision. All incumbent publication files matched current `main` bytes. Incumbent overview SHA-256: `0019966a29c5e23c376f6d2a53bf68c27ac02bd23cf26df58d5cd26ccc32d2d0`.

The incumbent adds a separate workflow member, explicitly qualifies the CLI's missing default curator-prompt path, and avoids the candidate's retained resume wording conflict. The candidate adds one saved-sheet content witness that the incumbent explicitly did not assess. That narrower evidence difference does not demonstrate a better overall replacement. Different profile inventory limits are already public in each set; neither is an exhaustive inventory.

## Findings

1. **Admission and scoring are correctly separated.** `S/dynamic_cheatsheet/language_model.py:386–454` supplies the question, full response and old sheet to the curator, then extracts replacement text without an independent correctness gate. `S/dynamic_cheatsheet/utils/extractor.py:65–90` requires only an opening tag; an empty extracted body can replace the sheet. `S/run_benchmark.py:253–309` updates the response corpus and active sheet before scoring. Candidate synthesis explicitly carries these limits and does not claim target labels validate memory.
2. **Resume defect is bounded publicly.** `P/runtime.md`, record `RT-RTE-benchmark-recovery`, retains the ambiguous “last non-None sheet” wording. `S/run_benchmark.py:174–193` uses only `outputs[-1].get("final_cheatsheet")` and conditional assignment, not backward search. `P/synthesis.md` states the precise rule and identifies the faulty wording in its limitations, following report verification. This existing public correction prevents a stronger recovery inference; no audit-only repair is needed.
3. **Historical concrete inconsistency is a coverage limit, not contradicted by the candidate.** Read-only parsing of the first two rows of `S/results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` confirms target `315`, answer `15`, a sheet asserting `15`, and that sheet in the next generator prompt. Candidate `EPI-OBJ-final-cheatsheet` inspects the first sheet as localized content, not target truth or producing-route provenance. Its synthesis explicitly withholds reliable checking, reliance and benefit. It does not preserve the archive's stronger two-row illustration, but does not deny it. These historical rows do not establish current-revision operation or downstream dependence.
4. **Containment qualifications are adequate.** `S/dynamic_cheatsheet/utils/execute_code.py` launches host `python3`, captures output and kills the direct child on timeout; no sandbox is established. `S/dynamic_cheatsheet/language_model.py:249–285` executes before testing continuation depth. Candidate synthesis already states ambient privileges, post-execution depth checking, separate native tools and evaluator `eval`; it does not imply a universal execution veto.
5. **Other known incompleteness remains visible.** The candidate synthesis carries the profile omission of decoded in-memory embedding arrays, unresolved vector/corpus provenance, opaque provider state, non-transactional continuation and lack of controlled benefit evidence. Neither the overview description nor synthesis upgrades implemented delivery to demonstrated learning success.

## Publication and operational evidence

Recomputed SHA-256 for every actual publication file. Exact set and all **12/12** hashes matched `R/effects/publish.json` and the inventory map, including assembled `ARTIFACT.yaml`:

`d47f8d256b1ad84cdd5190829fcf73a05fe9655676371339944840523697a626`.

The working type-only declaration is distinct: `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322`. Publish attempt `R/state/attempts/000028-publish.json` is completed and pins the assembled hash. The effect also says completed and names this destination and run.

Read-only inspection found all 28 retained attempts completed and all stored judgment outcomes accepted. Repeated runtime checks concern the same report hash with expanding cross-report scope, not evidence of newly performed analysis. Attempt `000005-runtime.json` records worker model `openai/gpt-6.1-sol` and medium effort; acceptance records are not worker tool-call traces. Report verification declares a targeted source read resolving resume; synthesis verification carries that limit and the profile omission.

No exact-run trace was supplied in the inventory. No executed worker call/result pairs were available for certification in this audit. Worker preflight validation, complete source-isolation compliance and all performed worker obligations therefore remain unverified. Publication acceptance is established; exhaustive worker compliance, target operation and causal benefit are not.

## Validation and stops

From `W`, used `W/.venv/bin/commonplace-validate` without output/state-writing options:

- Publication directory: `VALIDATION SUCCESS`; `Files analysed: 1`, `Text files: 0`; `0 failures`, `0 warnings`. This is the set entry-point check, not eleven individual member checks.
- Each of the eleven published `.md` members separately: `VALIDATION SUCCESS`; each `Files analysed: 1`, `Text files: 0`; each `0 failures`, `0 warnings`.
- Owned origin report, absolute path: `VALIDATION SUCCESS`; `Files analysed: 1`, `Text files: 1`; `0 failures`, `0 warnings`.

No substantive readiness blocker found within this bounded scope. Replacement would require a separately authorized operator decision identifying an advantage sufficient to supersede the incumbent; this audit supplies none. Broader payload/provenance inspection, live operation and worker-trace recovery were not undertaken. No shared inventory, accepted output, source, method or engine state was changed.
