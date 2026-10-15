# Self-Training-LLM exact-publication audit

## Decision and identity

**Disposition: integrate with recorded limits.** No consequential defect was established in the inspected scope. The public synthesis already qualifies delivery, scoring validity, checkpoint consumption and unobserved benefit. This is a bounded audit recommendation, not integration or certification of every worker obligation.

- run-id: `AAS-2026-10-15-self-training-llm-5b5ee621bde2-01`
- method-commit: `a568c6dc489ad546374536b642c3889ce23149a8`
- source-revision: `97839b29d0fd8bb474f5549fa3e9d6ca504732e0`
- Source: `https://github.com/wj210/Self-Training-LLM` (Git).
- Auditor: independent `openai/gpt-6.1-sol`, medium; confirmed by `PI_PROVIDER`, `PI_MODEL`, `PI_REASONING_LEVEL`. No delegation.
- Worktree (`W` below): `/home/zby/llm/commonplace/.commonplace/worktrees/self-training-llm-5b5ee621bde2`.
- Source (`S`): `W/related-systems/wj210--Self-Training-LLM`.
- Publication (`P`): `W/kb/agentic-system-analyses/retained/self-training-llm`.
- Run evidence (`R`): `W/kb/agentic-system-analyses/state/AAS-2026-10-15-self-training-llm-5b5ee621bde2-01`.
- Trace (`T`): `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-14/self-training-llm.output`.

Read the commission, complete audit procedure, earlier substantive commission, repository instructions, work collection and workshop framing. Used only the target's inventory row, number 48. Worktree HEAD equals method-commit. Source HEAD equals source-revision; source `git status --short` was empty, using `GIT_OPTIONAL_LOCKS=0`.

## Byte identity and inspection method

Recomputed all 13 published SHA-256 values against row 48's `published-sha256`: all match, and the actual filename set matches. `R/effects/publish.json` records the same complete map, completed state, exact run/source and destination, with no old publication. In particular, assembled `ARTIFACT.yaml` is `482984bbaa1087e4d44953665493d3f63e02ae359ed65ca6778446ea449f3682`; this is not the inventory's type-only working declaration hash.

Chose a discrepancy-led inspection of the historical account's strongest implications: a working end-to-end self-training path, reference-based preference selection, factual evaluation, and parametric rather than retrieval memory. Read public overview, synthesis, memory profile and final report verification; checked consequential differences directly in pinned source and selected completed worker transcripts. This was not a new whole-system analysis or exhaustive citation/axis review.

Historical lead: `kb/agent-memory-systems/reviews/Self-Training-LLM.md`, last checked 2026-06-04. It declares the same repository and commit, but that declaration is not independently authenticated equivalence of every historical input. Its claims were leads, not ground truth. No origin incumbent was supplied; this audit does not recommend replacement of another run.

## Consequential findings and public qualifications

1. **The central memory mechanism is preserved, while its benefit is more carefully bounded.** The historical account's generated QA → selected SFT/DPO examples → checkpoint → later generation account is retained in the synthesis's opening and model-consumer discussion. The new profile retains file/model-weight storage and a positive wired trace-fed update. It withholds a controlled trace-source category rather than repeating historical `trajectories`; that is a classification qualification, not loss of the update mechanism. It also avoids treating all retained reports as demonstrated pull consumers. No coverage regression requiring historical wording was established.

2. **Reference-as-chosen is branch-local, not an all-pairs guarantee.** Direct source check: `S/uncertainty/scorer.py:367–429` assigns `chosen_ans = gold_answer`, uses it in the first pair, then appends later pairs with `chosen_ans: g[0]` from sampled gold answers. `S/uncertainty/train.py:143–162` admits those lists with `extend`; its nonpositive unknown-threshold branch also falls back to the full dataset, not the previously question-filtered subset. The synthesis, “Scores control optimization, not factual warrant,” explicitly retains both exceptions. These are substantive qualifications beyond the historical overview, not unresolved defects.

3. **Experiment labels do not attest the served checkpoint or factual correctness.** `S/script/tgi.sh` defaults to base TinyLlama at revision `main`; `S/script/testing.sh:21–38` requests TGI while naming DPO mode and passes locally unassigned `answer_generator` and `beta`. The public synthesis explicitly warns that a DPO-labeled response file does not attest DPO-weight consumption and that wrappers need operator alignment. `S/uncertainty/pairwise_eval.py:98–115,121–150` divides by counted results without a zero guard and emits hallucination zeros from a disabled branch. The synthesis discloses selective denominators and placeholder zeros. The historical account's evaluation-as-benchmark-comparison is preserved without making it a factuality measurement or observed improvement.

4. **Consistency scoring is not factual acceptance.** `S/uncertainty/scorer.py:444–480` documents bidirectional entailment but clusters on the absence of contradiction in either direction; neutral predictions can remain eligible. The synthesis names this weaker rule and the compatible countercase of consistent false answers. It also states that `gold_answer` is an optimization role, not uniformly grounded truth. No additional audit-only factuality caveat is needed to repair public wording.

The overview description already says operator-mediated stages do not demonstrate factual or learning gains and calls deterministic checks nonsemantic. The synthesis further states that no target execution, weights, dataset or comparison artifacts were supplied, and makes unchanged-wrapper delivery conditional. These qualifications support the disposition; they are not introduced only here.

## Selected performed-worker evidence

Streamed `T` read-only. Used completed outer `tool_execution_end` records and matched assistant tool calls to `toolResult.toolCallId` inside the same worker's `details.results[].messages`. Did not count update snapshots, tool proposals or a publication receipt as worker performance.

- **Semantic refusals and revision:** `R/state/judgments/000023-apply-report-verification-1.json` refused the runtime all-pairs reference invariant. `000033-apply-report-verification-1.json` subsequently refused the dependent epistemic wording. These are semantic scope objections, not validator failures. Final `000043-apply-report-verification-{1,3}.json` accepts the revised runtime/epistemic versions matching the publication hashes.
- **Runtime correction actually inspected and checked:** `T` line 2852, worker for `000024-runtime`, pairs `call_V9G0k7xXN1yDSrRhLnW38wEP` with its successful scorer-read result, then pairs `call_cUD2zoLZpklEjSxvtLUg0geC` with the standalone `commonplace-run validate-output .../000024-runtime/prompt.md` result: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Short IDs here identify the prefix before `|fc_` within that worker.
- **Dependent correction was performed separately:** `T` line 3870, `000034-epistemic`, pairs scorer read `call_nArhz7J4xCJy4ROysD1eNvF9` and validation `call_yokl5uCOVcGxQsTu4ZL9h08W` with successful results. The latter returns the same explicitly limited content-check message.
- **Final independent verification inspected the disputed source:** `T` line 4590, `000042-report-verification`, pairs `call_VxLLr9Qp7wllj7GVtQOWvBDZ` with scorer lines 231–470, `call_bV9dgXzxOFUGq2GWeR1YGVDF` with the subsequent scorer range, and `call_9cNveaAB9iyuyivTnGF2ELwp` with the training driver. `call_jE3uxNy5ZagPLWwFollenmTO` has the successful standalone content-check result, not merely a promise to validate. The same worker read the correction answers and wrote the final verification.

No consequential scope violation was established by these selected actions. This does not certify every required read, all worker isolation or every write across the run. The final verifier's broad self-report was not used as proof of exhaustive performance.

One retained handout path was unavailable: reading `R/state/handouts/000042-report-verification/prompt.md` returned `ENOENT`. Recovered its complete invocation from the matched read/result in `T` line 4590 (`call_SVHuzdLWQ8qhPKwl1kNF6MUs`). An initial guessed source filename `S/script/run_tgi.sh` also returned `ENOENT`; directory listing located the actual `script/tgi.sh`, which was read. Neither error was treated as successful evidence or repaired by mutation.

## Validation

Called from `W`, using the recorded prefix `W/.venv/bin`:

```text
W/.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/self-training-llm
W/.venv/bin/commonplace-validate --full kb/agentic-system-analyses/retained/self-training-llm
```

Actual summary: `VALIDATION SUCCESS`; Files analysed: 1; Text files: 0; 0 failures across 0 subjects; 0 warnings across 0 subjects. The full output identifies one directory artifact, checks all twelve Markdown members plus directory requirements and members/roles/relations, and ends `Overall: PASS (clean)`. WARN, FAIL and INFO: `(none)`. No validation-excluded subtrees. This is structural/source-register checking, not independent verification of every quotation or claim.

Report validation uses this absolute origin path from the same worktree:

```text
W/.venv/bin/commonplace-validate --full /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/next-publications/AAS-2026-10-15-self-training-llm-5b5ee621bde2-01.md
```

Actual report result: Type: text; `[base] text file: no frontmatter, no structural requirements`; WARN, FAIL and INFO: `(none)`; `Overall: PASS (clean)`. This checks an implicit text artifact, not the audit's semantic judgment.

## Limits and conditions

No target code, training, serving, external services or benchmarks were executed. No sources were acquired or expanded. No exhaustive record/quotation audit, alternative-configuration review or full operational compliance review was performed. Public delivery/benefit and classification uncertainty remain necessary limits, not defects cleared by engine acceptance.

No semantic unblock is required within this bounded inspection. Parent acceptance still requires review of this report, unchanged byte-map confirmation and separate authorized integration. To remove the public operational limits would require separately commissioned evidence linking generated data, trained weight identity and actual inference consumption, plus controlled evaluation for benefit. An unchanged-wrapper delivery claim would additionally require resolving launcher/path defects and an initialization-to-delivery trace. This audit neither requests nor performs those expansions.
