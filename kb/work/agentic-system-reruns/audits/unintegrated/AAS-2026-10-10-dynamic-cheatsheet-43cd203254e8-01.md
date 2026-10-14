# Dynamic Cheatsheet alternative-publication audit

## Decision

**Integrate with recorded limits** as a bounded publication-readiness judgment.
**No reason established to replace the integrated incumbent.** This candidate
is an older alternative at the same source revision, not new corpus coverage.
No content blocker was established in the inspected scope. Integration or
replacement remains a separate coordinator/operator decision; neither occurred.

## Identity and inspection boundary

- Candidate: `AAS-2026-10-10-dynamic-cheatsheet-43cd203254e8-01`.
- Method: `5153e267a903ef18c3f416347dd48844e370f2f9`.
- Worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-43cd203254e8` (W below).
- Publication: W/`kb/agentic-system-analyses/retained/dynamic-cheatsheet` (P).
- Run evidence: W/`kb/agentic-system-analyses/state/AAS-2026-10-10-dynamic-cheatsheet-43cd203254e8-01` (R).
- Frozen source: W/`related-systems/suzgunmirac--dynamic-cheatsheet` (S), identity `https://github.com/suzgunmirac/dynamic-cheatsheet`, revision `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`; actual HEAD matches and Git status is clean.
- Auditor: `audit-dynamic-cheatsheet-43cd203254e8`, `openai/gpt-6.1-sol`, medium; session `01a13b25-dabe-706a-9d5b-5dcce285540d`.
- Method: discrepancy-led comparison of public overview/synthesis, scoped member searches, historical accounts and incumbent; direct frozen-source checks of admission, retrieval fallback, scoring order and resume. No execution, acquisition or delegation.

## Consequential findings and comparisons

1. **The central qualifications are public.** P/`overview.md` and P/`synthesis.md`
   distinguish wired reference replacement/delivery from verified content,
   actual reliance and causal benefit. The synthesis explicitly excludes fresh
   execution, inspected result bodies, notebook outputs and provider internals.
   It retains context-budget, host-execution, scoring and recovery limitations.
2. **Admission and scoring are correctly separated.** S/`dynamic_cheatsheet/utils/extractor.py`
   admits text after an opening tag without requiring a closing tag; empty
   bodies can replace prior text. S/`run_benchmark.py:253–311` assigns the sheet
   before scoring and saving. Scores do not veto that assignment. S/`dynamic_cheatsheet/language_model.py:503–545`
   confirms retrieval-synthesis fallback is assembled examples, not necessarily
   the previous sheet. These distinctions are explicit in P/`synthesis.md`.
3. **The recovery correction is present and supported.** S/`run_benchmark.py:169–197`
   restores only the final record's non-null sheet and otherwise keeps initialized
   text; it does not search backward. P/`report-verification.md` and the synthesis
   retain that corrected rule. No current contradictory public recovery claim
   was established by the scoped inspection.
4. **Historical comparison is bounded, not a demand to preserve old certainty.**
   Read `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md` (June account)
   and the moved account `kb/agentic-systems/reviews-archive/dynamic-cheatsheet.md`
   (September run), both at this source revision. The candidate preserves the
   six approaches, automatic reuse, prompt-only maintenance and separate scoring.
   It improves on the June wrapper description and curation-operation certainty.
   It does not inspect the September account's target-inconsistent historical
   sheet; this is a declared evidence limit, not a contradiction or proof that
   erroneous reuse cannot occur. No historical causal-benefit claim is adopted.
5. **The incumbent remains preferable.** Origin `kb/agentic-system-analyses/retained/dynamic-cheatsheet/{overview,synthesis}.md`
   identifies `AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01`, method
   `bb155f68660d0c7294f410e3aea4816ae3c6e2b1`, at the same source revision.
   It adds a workflow member and publicly covers separate client history/search
   surfaces and profile omissions. The candidate deliberately excludes those
   independent adapter features in P/`boundary.md` and P/`memory.md`; its account
   is narrower, not evidence for removing the incumbent's coverage. Both retain
   the principal no-semantic-gate/no-causal-benefit qualifications.

## Bytes, operational evidence and verification

- Ready preparation and R/`effects/publish.json` inspected. Actual file set and
  all 12 SHA-256 values exactly match the effect, including assembled manifest
  `6e928b281a7d5af17ca3c6c87ea571a75df1eb919079b92e200527d700a1bd0a`.
  Working type-only declaration is separately `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322`.
- R/`state/attempts/000037-publish.json` is completed and pins that manifest.
  Attempt inventory shows runtime revision and report reverification before
  assembly/publication; judgment `000027-apply-report-verification-0.json`
  accepts the final verification on the published runtime version. This establishes
  recorded engine acceptance, not performed worker source-read/validation obligations.
- The exact-run inventory supplies no traces. No executed worker call/result
  pairs were available for compliance certification. Full operational compliance,
  target operation and causal learning remain unverified; publication does not
  establish them. No old hold is cleared by this report.
- From W, `.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/dynamic-cheatsheet --full`:
  **PASS (clean)**, set plus all 11 declared Markdown members, schemas, source
  quotations, links, roles and relations; no warnings or failures, exit 0.
- From W, the same validator with this report's absolute origin path and
  `--full`: **PASS (clean)** as implicit text; no warnings/failures, exit 0.
  Text validation imposes no structural requirements; it is not semantic review.

Blockers: none established for bounded readiness. Replacement is not recommended.
Stop boundary: broader source/trace reconstruction or incumbent reanalysis would
require a separate commission. Only this report was written.
