# Cognee current-batch publication audit

## Disposition

**Integrate with recorded limits.** No consequential defect requiring a hold was established in this bounded audit. The published synthesis already carries partial-loop coverage, unobserved operation/benefit, route-specific context delivery and the shipped skill-feedback inventory omission. This finding does not certify every worker obligation or successful target behavior. Blockers: **none**.

## Identity and auditor

- Exact inventory row: Cognee, batch 01, `AAS-2026-10-14-cognee-d8839fe03c5b-01`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/cognee-d8839fe03c5b` (abbreviated `W` below).
- Publication: `W/kb/agentic-system-analyses/retained/cognee/` (abbreviated `P`).
- Run evidence: `W/kb/agentic-system-analyses/state/AAS-2026-10-14-cognee-d8839fe03c5b-01/` (abbreviated `R`).
- Frozen SRC-1: `https://github.com/topoteretes/cognee`, commit `f154b32a9e544dac73e7ddf2010327cf9988edcd`, at `W/related-systems/topoteretes--cognee/` (abbreviated `S`). Cutoff: 2026-10-14; code-grounded; complete artifact, partial loop.
- Method commit: `4266dabc470929df0ff753e57fee0c55d7b87fc6`; pinned plan SHA-256: `5a5f56891d95a819c3f4fde00bb92eb301876598c022924ee52bed6262721bfd`.
- Auditor runtime: Pi, `openai/gpt-6.1-sol`, medium reasoning, confirmed from `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`; session `01a138ea-a0b1-73fb-8e93-698a6a0a0bc2`. No delegation.

The sibling preparation record is ready and supplies `W/.venv/bin` as command prefix. Preparation, opening metadata, acquire output, boundary and overview agree on their respective identities. Git HEAD matches both the method and source pins; source `git status --porcelain` is empty. The opening/publication receipt's null requested `source-revision` is not the acquired revision: the acquire record and boundary retain the actual pin.

## Method and historical boundary

I read the complete overview, synthesis, boundary and three final verification members, then selected runtime/memory passages and frozen sources for consequential differences. I inspected stored attempts, publication hashes and selected nested worker evidence. This is a discrepancy-led audit, not a rerun or exhaustive analysis.

The `systems.md` row points to [the historical Cognee review](../../../agent-memory-systems/reviews/cognee.md). Scoped search of `kb/agent-memory-systems/` found that review and catalog references, not a second substantive Cognee report. The historical review is still at its original location; no moved account was substituted. Its boundary is commit `cfb0aa4d0b3ae0154cf9f24e5908263d565341f4`, last checked 2026-06-04. I used its claims as coverage leads, not ground truth, and did not acquire or inspect that older source revision.

## Consequential findings

1. **The core historical architecture is retained, with sharper limits.** The old review's graph/vector permanent memory, session cache, trace promotion, ranking feedback, global summaries, progressive skills and decorator/gateway push all have corresponding named routes or objects in `P/runtime.md`, `P/memory.md` and the synthesis. The new account separates storage from admission and later consumption, and recall from the explicit agentic loop. It does not repeat the old Commonplace borrowing recommendations; these are outside the source-first characterization, not a coverage regression. This was a topical comparison, not independent revalidation of every backend/default claim.

2. **“Improve is infrastructural rather than epistemic” now needs qualification, and the publication provides it.** The old account emphasizes a durability/ranking bridge without semantic review. At the current pin, `S/cognee/modules/session_distillation/distill.py` implements curator proposals, a writer/rejecter and code filtering on nonfailed, accepted, nonblank statements before `add`/`cognify`. `build_writer_input`, `evaluate_proposed_lesson`, `accept_proposed_lessons` and `distill_session` support the synthesis's positive admission architecture and its limits: no original QA transcript in the writer input, missing member IDs omitted, failed novelty/glossary search yielding empty results, and surviving publication preceding a later failed-call exception. This is model judgment with publication force, not an independent truth oracle or demonstrated benefit. See `P/memory.md#mem-rte-session-distillation` and the synthesis's maintenance section. No claim about when this mechanism was introduced follows from this audit.

3. **The decorator push claim remains explicitly gateway-local.** `S/cognee/modules/agent_memory/runtime.py` selects recent feedback and graph-summary search results, requests bare `context_result` in only-context mode, truncates combined supply to 4,000 characters and persists sanitized traces separately. This supports `P/runtime.md#rt-rte-decorated-agent` and its public synthesis account, not automatic memory delivery to arbitrary host LLM clients. The old review loosely grouped graph recall as embedding-based; the current profile correction appropriately leaves this decorator selector unresolved rather than inferring it from an available index. I did not trace that selector further. Its uncertainty is already public, not an audit-only repair.

4. **The shipped automatic skill-feedback driver is a real omission, already disclosed.** Independent reading of `S/examples/demos/feedback/skill_feedback_loop/skill_feedback_loop_demo.py` confirms an agentic answer is parsed into feedback and score, a typed SkillRun is recorded, a proposal is obtained, and `improve_skill(..., apply=True)` is called automatically. It does not perform a later revised-skill invocation or a post-install performance test. The report verifier found this additional producer; the synthesis repeats its consequences in the adaptation account and limitations table. Therefore the core recorder's neutral default and unresolved apply caller must not be generalized to all shipped callers. The qualified publication does not make that generalization. Canonical inventory expansion remains deferred; a complete score-provenance/autonomy comparison would require it.

## Publication and operational evidence

`R/state/attempts/000037-publish.json` is completed and pins the final members and assembled manifest. Its receipt states `published: true`; `R/effects/publish.json` is completed. I independently recomputed all 13 published file hashes, including `ARTIFACT.yaml`, and checked the exact file set against the publication effect: all match. All 12 Markdown files also match the working artifact byte-for-byte. The working artifact's manifest contains only its type declaration; the published manifest is the assembled version pinned by the publish attempt and stored in `state/versions`. This is not an unexplained publication mismatch.

Stored model attempts record completed outputs and self-reported `openai/gpt-6.1-sol`/medium identity. The memory profile went through an initial verifier blocker, correction and final verification (`000024`, `000026`, `000028`, `000030`); final profile verification explicitly resolves the unsupported decorator embedding classification. Engine completion and these declarations are evidence of acceptance, not exhaustive compliance proof.

The origin log `kb/work/agentic-system-reruns/outputs/cognee.output` retains nested messages in completed subagent results. Relevant result lines include 617 (boundary), 948 (runtime), 1719 (memory/epistemic/workflow), 2498 (report verifier), 2818–3800 (profile rounds), 4130 (synthesis) and 4453 (synthesis verifier). Launch/result records name the project worker, worktree, selected model and medium effort. I paired recorded tool-call IDs with results within each result's worker messages; each recorded call had a result. In particular, line 2498 contains an executed read and returned contents for the feedback demo, not merely a proposed read. A narrow scan of worker call arguments did not find explicit reads of historical review paths; that scan cannot rule out indirect access or certify source isolation.

The run's handout directory is now empty; original prompt files and standalone worker session paths are not available there. The outer log preserves useful embedded evidence, but I did not audit every read, truncation recovery, instruction obligation or action across the full traces. Missing original handouts remain missing evidence. Neither a zero worker exit code nor deterministic publication acceptance establishes fulfilled worker obligations. No target execution or causal benefit is certified.

## Validation

Called from `W`, using its prepared command environment, without output/receipt options:

```text
.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/cognee
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/cognee
Scope: kb/agentic-system-analyses/retained/cognee
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

Details: commonplace-validate --full kb/agentic-system-analyses/retained/cognee
```

The command reports one directory artifact, not thirteen independently counted files. Hash inspection above is separate from this validation. The report check, also called from `W`, returned:

```text
.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-cognee.md
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-cognee.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-cognee.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects

Details: commonplace-validate --full /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-cognee.md
```

## Limits and follow-up

No hold unblock condition is needed. Integration is supported only as this published, qualified implementation account. Whole-system transport/lifecycle closure, actual lesson fidelity, comprehensive derivative withdrawal, complete score-producer/apply-driver coverage and beneficial future-task change remain unestablished, as the synthesis states. I did not independently recheck every truth-epoch, deletion, ranking, permission or tool-loop claim. Stronger claims would require separately commissioned source tracing and linked execution/comparison evidence, not qualifications added only to this report. Integration, bookkeeping and any recovery remain the coordinator's responsibility.
