# Agent Workflow Memory pre-integration audit

## Disposition

**Integrate with recorded limits.** No consequential defect requiring a hold was established within this bounded inspection. The published synthesis already qualifies default pipeline operation, generated-workflow validity, observation selection, optional retrieval and unobserved behavioral benefit. This clearance is for the qualified implementation account, not a certification that AWM runs successfully or improves agents.

The parent owns integration and its independent publication checks. No analysis, method, run state or shared bookkeeping was changed; no commands advanced the run, and no workers were launched. Only this report was written.

## Identity and approach

- Run: `AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01`.
- Method: `0b37f22ae1a989fe806c754fea1fe8c1c8e36c63`; independently checked worktree HEAD matches.
- Worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/agent-workflow-memory-cb2da079273e`.
- Local command directory: that worktree's `.venv/bin`; no analysis commands were needed for this audit.
- Source: `https://github.com/zorazrw/agent-workflow-memory`, commit `8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1`, at `related-systems/zorazrw--agent-workflow-memory` in the worktree. Independently checked HEAD matches and source Git status is clean.
- Publication: worktree-relative `kb/agentic-system-analyses/retained/agent-workflow-memory/`.
- Auditor: fresh Pi worker, `openai/gpt-6.1-sol`, medium thinking, as exposed by `PI_PROVIDER`, `PI_MODEL` and `PI_REASONING_LEVEL`; session `01a131be-ee8d-7339-876d-350c17369bc1`.
- Procedure: [audit a rerun](../audit-a-rerun.md). Selected approach: historical mechanism comparison, complete reads of the public overview/synthesis and verification accounts, profile comparison, targeted frozen-source challenges, publication byte checks and nested validation-call/result checks. Not a second analysis.

Evidence shorthand below: **P** is the publication directory above; **R** is worktree-relative `kb/agentic-system-analyses/state/AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01`; **S** is the frozen source directory above.

## Historical comparison boundary

Read the complete origin account `kb/agent-memory-systems/reviews/agent-workflow-memory.md`. It names the same source commit, so revision drift does not explain differences. Its findings were leads, not authoritative requirements or inputs to analytical workers.

The central mechanisms remain covered: plain workflow files; WebArena system-message and Mind2Web exemplar consumption; offline and online trace/example induction; reward/model eligibility and optional human rule approval; random concrete-example selection and token-fit omission; separate FAISS preprocessing; weak content provenance and absent per-entry invalidation. P/synthesis.md carries these mechanisms and their operational limits rather than preserving all legacy prose or Commonplace borrowing suggestions. No consequential coverage regression was established.

Two changed classifications warrant explanation:

- **Read-back direction:** the historical account calls configured file injection push from the acting model's perspective. P/memory-profile.md calls the requested file-consumption chain pull and explains why delivery is not counted again as push. The frozen method's `kb/agentic-system-analyses/types/agentic-system-memory-profile.md`, “Read-back,” explicitly defines fulfillment of requested retained material as pull. The new account still states the actual system/exemplar delivery and lack of default task-targeted search. This is a contract-relative classification change, not loss of the mechanism.
- **Semantic retrieval:** the historical account describes the FAISS utility without its object-handoff defect. The new synthesis qualifies the semantic workflow branch while keeping the concrete-example ablation separate. Direct inspection confirms the narrower new account; the historical description is not grounds for restoring a working-retrieval claim.

## Consequential findings

### 1. Default WebArena coordination is implemented, not reliable evidence-fed updating

P/synthesis.md, “Assessment at the declared boundary,” explicitly carries the evaluator/inducer filename mismatch, accumulated cross-site scan, zero-example generation and unchecked child outcomes. These qualifications materially improve the earlier account's apparent run/evaluate/update progression.

Independent checks: S/webarena/pipeline.py waits on three subprocesses without checking their return codes, passes the whole `results` directory to induction and supplies an output path. S/webarena/autoeval/evaluate_trajectory.py:130–159 writes a model-named result and defaults to `gpt-3.5-turbo`; S/webarena/induce_prompt.py:102–182 defaults to `gpt-4o`, selects its corresponding result filenames without a website predicate, calls generation even with no selected examples and overwrites the output. No target code was executed. The publication correctly withholds successful default progression while retaining the conditional architecture.

### 2. Optional retrieval is not a working default memory lookup service

P/synthesis.md, “From retained file to later decision,” distinguishes optional preprocessing from ordinary file consumption. S/mind2web/workflow/retrieve.py was read completely: `build_memory` constructs/saves FAISS but returns metadata; the semantic caller passes that returned list to `similarity_search_with_score`. The ablation constructs and passes the FAISS object directly. The published qualification is branch-specific and sufficient; neither successful semantic workflow retrieval nor retrieval-quality improvement is asserted.

### 3. Verification limits reach the public synthesis

P/report-verification.md retains two local omissions from lower-level accounts. Both are carried in P/synthesis.md's limitations table, and annotated observation selection also appears in its main progression:

- S/mind2web/utils/env.py:160–176 seeds cleaned observations with the first positive annotated candidate plus ranked negatives. Readers must not treat the scores as annotation-blind live-navigation evidence.
- S/webarena/agents/legacy/utils/chat_api.py:73–91 omits `eai_token` when calling a constructor that requires it at lines 145–151. Readers must withhold working alternate-backend availability through that factory.

Direct source reads confirm those two qualifications. Their presence only in verification would not suffice; here the synthesis carries them. The overview's description also states that workflow validity and beneficial use are unobserved. Its validation section explicitly disclaims semantic certification.

### 4. Behavioral benefit and workflow correctness are not inferred from storage or source success

P/synthesis.md separates source eligibility from generated-procedure acceptance, prompt delivery from content-dependent action, repeated overwrite from criticism-driven revision, and architectural trace-fed updates from improved capacity. P/boundary.md identifies BrowserGym, provider internals, downloaded inputs and absent observed runs as evidence limits. These limits are already public. The historical account's lightweight provenance and stale-guidance concerns remain visible, with more precise limits on task association, whole-file replacement and context delivery.

This finding checks consistency and qualification placement, not all individual theory-related conclusions or every source anchor.

## Operational evidence

### Publication bytes

Read R/effects/publish.json and independently hashed every retained file. All **13 files**, including `ARTIFACT.yaml`, exactly match the journal's `new` map; the retained file inventory has no additions or omissions. All 12 Markdown members also exactly match R/artifact. The sole artifact-directory difference is `ARTIFACT.yaml`: publication expands the initial type-only file into the member-hash and worker manifest. That difference is accounted for and matches the publication journal, not evidence of post-publication drift.

The supplied origin inspection `kb/work/agentic-system-reruns/rolling-05-agent-workflow-memory-inspect.json` reports completed publication, no failed/open attempts, no canonical-peer drift and no current refusals. Its stale acceptances are historical entries; they are not by themselves current failures. Its journal `verified: false` fields are expressly not effect-handler verification. The byte checks above do not substitute for integration's own supported checks.

### Worker validation and correction sequence

Inspected nested traces retained in:

`/home/zby/.pi/agent/sessions/--home-zby-llm-commonplace--/2026-10-12T18-52-06-274Z_01a13175-3102-76ed-b2e9-63d6c88be8db.jsonl`, line **119**, `message.details.jobs[0].result.messages`.

Each of the **16 analytical worker attempts**, including both correction cycles, has an executed local `commonplace-run validate-output <its recorded prompt path>` and a matching result in the same worker reporting “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes the inspected validation obligation, not all worker obligations.

Two deterministic preflight problems were repaired and revalidated:

- `000007-memory`: coordinator message 25, worker result 0, worker message 76 call `call_Q3h1GabNCKPu58w3AHuf2jNC|fc_04fffa50baa0f065016acd314e0b8487d282bd9c21240927f0` returned the pending-validation failure. Messages 80 and 84 have matching passing results after edits.
- `000034-memory-profile`: coordinator message 49, worker result 0, worker message 56 call `call_pzBjodfE8mGticHOijGWv8wz|fc_099f8671c8877c4c016acd38fc0e5887d2bfcd0e2f74f92c74` returned duplicate citation-list failures. Message 62 returned a pass after repair.

Semantic objections were separate: P/report-verification.md documents correction of the vision answer-history claim; P/profile-verification.md documents repaired factual knowledge authority, offline learning authority and manual-rule lineage. The later verification accounts declare no remaining blockers, and the synthesis carries the report's remaining limits. No nonexistent validation-path recurrence was established in the inspected calls.

Useful final correction locators in that same nested trace: coordinator message 37/result 0/message 50 (`000024-epistemic`) and message 57/result 0/message 60 (`000038-memory-profile`), each paired with its own passing tool result. This audit did not infer execution from a tool proposal or a worker's final assertion.

## Coverage limits and follow-up

This was a bounded comparison and spot-check, not an exhaustive source, helper, corpus, citation or worker-compliance audit. No target execution, provider invocation, benchmark reproduction, BrowserGym inspection or causal experiment was performed. Runtime, memory, epistemic and workflow members were used through cited accounts and targeted checks rather than reanalysed in full. The profile, report-verification and profile-verification accounts were read completely; synthesis-verification was not independently assessed. Nested operational checks concentrated on validation execution/results and the visible correction sequence, not complete source-isolation or write-scope reconstruction for every worker.

No integration unblock condition is required. The existing published limits must remain with the analysis. Stronger claims would require source-linked end-to-end operation, generated-procedure checks and controlled later-task comparisons; those are future evidence needs, not conditions for integrating this qualified account. Shared bookkeeping and integration remain the parent's responsibility. Broader graph discovery is outside this audit; `cp-skill-connect` would be a separate commission, not an action taken here.

## Report validation

Ran in origin with bare `commonplace-validate kb/work/agentic-system-reruns/audits/rolling-05-agent-workflow-memory.md`: **VALIDATION SUCCESS**. One text file analysed; zero failures and zero warnings.
