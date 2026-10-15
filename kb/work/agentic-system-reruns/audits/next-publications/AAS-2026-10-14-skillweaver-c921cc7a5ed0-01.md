# SkillWeaver exact-publication audit

## Decision

**Integrate with recorded limits.** No consequential defect was established in the inspected discrepancies. The public synthesis already qualifies admission, tested status, evidence loss, executable authority and unobserved improvement. This is one bounded independent audit, not a complete reanalysis or certification of every worker obligation. Parent review and integration remain separate.

## Identity and authority

- Exact run: `AAS-2026-10-14-skillweaver-c921cc7a5ed0-01`.
- Auditor: independent project worker; runtime environment reports `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`.
- Commission: [next-61 commission](../../audit-next-61-commission.md), [audit procedure](../../audit-a-rerun.md), substantive rules of [earlier commission](../../audit-unintegrated-prompt.md), root `AGENTS.md`, `kb/work/COLLECTION.md` and [workshop framing](../../README.md). The commission fixes this report as the sole write and authorizes direct frozen-source audit reads; no ingest, graph discovery or source acquisition was undertaken.
- Inventory: exact-run JSON row 24 of [next-publication inventory](../../next-publication-audit-inventory.md).
- Prepared worktree, abbreviated **W** below: `/home/zby/llm/commonplace/.commonplace/worktrees/skillweaver-c921cc7a5ed0`.
- Method: `a568c6dc489ad546374536b642c3889ce23149a8`; independently verified W's HEAD. Preparation record `W.preparation.json` is ready, token `c921cc7a5ed0`, with the same commit and command prefix.
- Recorded command prefix: `W/.venv/bin` (expand W to its absolute path above).
- Source: `https://github.com/OSU-NLP-Group/SkillWeaver`, frozen Git checkout `W/related-systems/OSU-NLP-Group--SkillWeaver`, HEAD `f2a63d65d0f6ff46ac30e817cede8797f8f25b97`. `GIT_OPTIONAL_LOCKS=0 git status --porcelain` returned empty for that checkout.
- Publication, abbreviated **P**: `W/kb/agentic-system-analyses/retained/skillweaver`. Run state, abbreviated **R**: `W/kb/agentic-system-analyses/state/AAS-2026-10-14-skillweaver-c921cc7a5ed0-01`.

Independently enumerated and SHA-256 hashed every regular file under P: **all 13 files and the complete filename/hash map match the inventory exactly**, with no extra files. `R/effects/publish.json` names this run, source identity and destination, is completed, and carries the same map. `R/state/attempts/000053-publish.json` is completed. The assembled `ARTIFACT.yaml` hash is `eaa5d002869db0b44af3b0e137a79fc39652ac4fdbeb3fb6f4ce69d799d29f6e`; it is not the working declaration hash `093c6e4a6c7cab7e4e1a9db63f6d2d45eec6a24bf51f7b287dd1db929b388322`. W's status showed only the untracked retained `skillweaver/` publication. These checks establish byte identity and completed publication, not analytical correctness or performed worker obligations.

## Method and historical comparison boundary

Read the complete historical [SkillWeaver account](../../../../agent-memory-systems/reviews/SkillWeaver.md), public overview, synthesis and current report verification. Used the historical account to select discrepancies, not as source truth. Both accounts declare the same Git revision, but that declaration is not asserted equivalence of historical source copies, environments, inspected coverage or execution evidence. No origin incumbent is supplied for this intake; no alternative publication was substituted.

Selected four questions that could change a reader's understanding: whether static validation actually vetoes installation; what a tested label proves; whether recovery evidence reaches synthesis; and whether the old push/new pull classification hides a lost consumer mechanism. Checked the corresponding frozen source ranges and selected profile/type passages. Source locators below are commit-relative to the frozen checkout above. This deliberately stops short of auditing every skill body, evaluator or analysis record.

## Consequential findings

### 1. New admission wording corrects an overstrong historical gate

The historical account says code enters the store only after checks pass. In `skillweaver/knowledge_base/knowledge_base.py:293-363`, the update loop retries at most ten proposals; violation-bearing proposals continue, but the final `self._apply(updated_code, reference)` is outside the loop without a final violations veto. The public synthesis's “Installation makes skills durable, not warranted” section explicitly says exhaustion still reaches application and distinguishes parse/format failure from semantic acceptance. This qualification is public, not supplied only by this audit.

The same source's `_apply` at lines 181-219 supports name-local replacement, retained omitted functions, metadata version increment and counter reset. The durable procedural-library mechanism was not lost. No target execution was needed or performed to inspect these control-flow facts.

### 2. Tested status does not establish dynamic execution

The historical prose repeatedly associates testing with successful or exception-free calls. The frozen `skillweaver/attempt_task.py:25-31` walks the action AST for a matching named call, not a runtime call record. `skillweaver/explore.py:140-156,241-269` combines that occurrence with the last action's exception/recovery fields and increments the counter without the success-model/synthesis branch. An unreachable matching call can satisfy the source predicate. This is a static deduction, not an observed exploit.

The synthesis's “Two branches confer different kinds of reliance” explains the `if False` case, bypassed success judgment and consequential visibility/scheduling effects. `knowledge_base.py:162-170` also supports its qualification about blanket tested marking. These are important improvements over the historical confidence, not regressions requiring preservation of the old wording.

### 3. Retained recovery artifacts are not equivalent to update inputs

`skillweaver/attempt_task.py:233-242` writes the richer trajectory with intermediate states and recoveries. `skillweaver/explore.py:230-234` then rewrites the same readable file with default rendering. `skillweaver/agent.py:164-180` defaults to only the initial state and no explicit recovery rendering. The success call separately receives the final screenshot; the subsequent update call receives trajectory text, not that separate screenshot (`explore.py:249-265`).

The synthesis states this loss in “Practice supplies the update evidence” and in its limitations table. Raw artifacts surviving separately do not establish that recovery information reaches skill synthesis. The historical account's recovery-learning story therefore does not establish a missing new feature. The new public qualification is necessary and present.

### 4. Read-back terminology changed without losing the relevant wiring

The historical account calls host-selected context push from the action model's viewpoint. The frozen method's `agentic-system-memory-profile.md`, Read-back section, instead classifies fulfillment of a consumer request as pull and prohibits counting delivery of that requested return as a separate push. The new profile applies that convention and leaves optional capabilities without later-consumer routes unresolved, rather than claiming complete pull-only coverage.

Actual wiring is still described: `skillweaver/create_skill_library_prompt.py` requests LLM relevance selection for production and retrieval-enabled exploration/testing; `attempt_task.py:121-160` selects once and reuses the visible function text through the task loop. `knowledge_base.py:438-465` supplies model-based relevant-name selection. The synthesis retains one-shot selection, readable descriptions versus executable bodies, optional embedding capability, unchanged semantic text and the limits of visibility controls. The category difference is explained by the method's unit/definition, not evidence that the new account omitted skill delivery. This audit does not independently certify every profile classification.

## Selected worker execution evidence

Trace **T**: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/skillweaver.output`. Parsed actual outer `tool_execution_end` records and paired nested assistant tool calls with same-worker `toolResult.toolCallId` values. Did not count stream updates, proposals or repeated snapshots as actions. Line numbers below are physical JSONL lines; short call IDs denote the unique prefix before `|fc_…`.

- **Semantic objection was acted on, not erased by publication.** Initial report-verifier result T:2462 belongs to `000022-report-verification`; its completed attempt stores version `0c5f974c893451310e4912ae6effb4d4f47f2d9a6bd1defffe8d3a586b3cfa37`. The later accepted verification identifies its three blockers as the mistaken dynamic-execution claim in runtime, memory and workflow. The correction worker result T:2765 for `000024-runtime` contains call `call_ItrSMURVzriJnuDRkHjlr80B` reading its supplied refusal with a successful matching result; calls `call_gjwKBLGJZmLsGBTf5UMRvL2R` and `call_X1wS63CVthrurM2TfKe364QL` read the actual task/predicate sources with successful matching results. `call_TZZQccIoY1LjOAu2784I67NP` edits its owned output; the matching result reports eight replacements. `call_l79heGM7b51fod1KG6BQTmN6` writes its correction answers successfully. This demonstrates a performed source-backed correction in the sampled worker, not just an author claiming repair.
- **Independent recheck is visible.** Final report-verifier result T:3949 corresponds to outer call `call_IALiidtdSze7UQSPifOL44Ve` and handout `000038-report-verification`. Within that worker, `call_gPr9vJi3mLkiQwFZQytYtmiS` reads `explore.py:1-280`, and `call_wU8g4TR7kvSg50XV0mg9SFGG` reads `attempt_task.py:1-300`; both have successful matching source results containing the disputed branches. `call_JZYsy3TjXkir3eGRTWzu7dWR` reads `knowledge_base.py:281-630`, including retry/application and retrieval, with a successful matching result. `call_PoSD1Xx9U9vhgnfDF2pCYVI3` writes the verifier's owned output successfully. The stored attempt pins the corrected runtime/memory/workflow and outputs current report-verification hash `c35f75c128f5fe6f28ec4a818a1b0fcbbb8e2233d58e1c02ff2b96f7590abcef`.
- **Content check is narrower than acceptance.** Same verifier's `call_RIRWQD9pb4luCA5ZE2MFWJkt` invokes the prepared `commonplace-run validate-output`; its matching result says: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” The nested worker also returned exit code 0. Neither fact certifies all semantic obligations.
- **A second semantic correction is retained.** Stored attempt `000042-profile-verification` outputs version `6060791aaf75d2fc6398117827f7375417f9e37bbc69f2ea71648439e1e5411a`, whose blocker rejects classifying optional request/return capabilities as established consumer routes. The current profile's direction coverage and synthesis explicitly retain that uncertainty. This is a stored-artifact comparison, not a separate claim that every profile worker call was audited.

The sampled runtime-correction and final-verification calls show source inspection, correction and content checking; no consequential scope violation was established in that sample. I did not reconstruct the complete run or certify absence of deviations elsewhere. There is no assertion that publication proves observed target operation or benefit.

## Validation

Executed from W with the recorded absolute command prefix, without output/state-writing flags:

```text
W/.venv/bin/commonplace-validate /home/zby/llm/commonplace/.commonplace/worktrees/skillweaver-c921cc7a5ed0/kb/agentic-system-analyses/retained/skillweaver
W/.venv/bin/commonplace-validate --full /home/zby/llm/commonplace/.commonplace/worktrees/skillweaver-c921cc7a5ed0/kb/agentic-system-analyses/retained/skillweaver
```

Both returned exit 0. Summary: `VALIDATION SUCCESS`, files analysed 1 (the directory artifact), text files 0; **0 failures, 0 warnings**. Full output: `Overall: PASS (clean)`, all twelve Markdown members plus directory schema/member/role/relation checks listed; WARN, FAIL and INFO all `(none)`; no excluded subtrees. No source-unavailable notice occurred. Validation is deterministic evidence, not a semantic warrant or observed-operation result.

Owned report: ran the same prefixed validator from W against absolute origin path `/home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-14-skillweaver-c921cc7a5ed0-01.md`, both summary and `--full`. Both returned exit 0. Summary: `VALIDATION SUCCESS`, files analysed 1, text files 1, **0 failures, 0 warnings**. Full output: type `text`, `[base] text file: no frontmatter, no structural requirements`; WARN, FAIL and INFO all `(none)`; `Overall: PASS (clean)`. This text-file check does not validate the audit's factual claims.

## Limits and integration conditions

The public overview description already withholds exercised improvement and generalized correctness. The synthesis additionally withholds update-linked observed use and causal benefit; describes non-vetoing bounded retries and syntactic tested labels; limits recovered evidence delivery; distinguishes context visibility from execution authority; and carries external-environment, optional-consumer and benchmark-entry limitations. This audit relies on those existing public qualifications, not an audit-only repair.

No substantive integration blocker remains within the selected scope. **Unblock conditions: none for this disposition.** Parent acceptance still requires review of this report and unchanged publication bytes. If identity/hash changes or a consequential contradiction is found, review must reopen rather than treating this disposition as transferable. Stronger performance or reliability conclusions would require separately authorized update-linked execution/outcome evidence and controlled comparisons; collecting them is outside this audit.

Coverage deliberately excludes exhaustive per-record verification, all trace workers and command exits, every skill/evaluator body, provider behavior and target execution. No delegation, source acquisition, state-writing inspect/advance/recovery, source/method/publication edit, integration, cleanup or Git staging/commit/push was performed. Only this owned report was written. Broader graph discovery is not part of this commission; any later `cp-skill-connect` work requires separate authorization.
