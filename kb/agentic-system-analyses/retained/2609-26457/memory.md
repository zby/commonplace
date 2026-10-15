---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AIDE2 memory mechanisms: bounded candidate summaries, gated error signatures and accepted harness reuse in the frozen paper capture."
run-id: AAS-2026-10-14-2609-26457-6b3bcd4791cf-01
source-identity: https://arxiv.org/abs/2609.26457
reviewed-boundary: arxiv-2609.26457v1-2026-10-14
---

# AIDE2 memory report

## Boundary and evidence

The subject is AIDE2's documented harness-improvement plane, including the inner agents whose context policies it rewrites. The frozen boundary is `arxiv-2609.26457v1-2026-10-14`, with SRC-1 registered in [boundary](boundary.md#source-register). This is a doc-grounded, complete-artifact/partial-loop account. Memory scope follows the supplied [RT-RTE-inner-search](runtime.md#rt-rte-inner-search) and [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission), but direct source inspection also covers the prompt reconstruction and rejected-proposal accounts.

Included surfaces are candidate code/output history; reviewer-derived scores and feedback; strategy labels and score-based selector state; bounded root/recent summaries; gated failure signatures; outer proposal/grade history and evaluation artifacts; and accepted harness code and persistent prompt instructions. Raw history accumulation is working state, not automatically derived memory. The summaries and signatures qualify as retained memory because transformations of earlier work reach later generation calls. Incumbent code is a separate cross-round retained result.

Direct reads used the absolute capture path in boundary: SRC-1 §§2.1–2.2, §§3.1–3.6, and appendices C–E. A bounded full-capture search for memory, summary, context, error, history, previous proposals, rejection and grades located these passages. Runtime findings provide the baseline route inventory and quoted evidence for robustness, admission and fallback; direct reads confirmed the main context account. Source text supplies doctrine/design and reported operation only. No implementation, raw observed run or independently inspectable causal experiment was supplied.

There is no frozen CLI dispatch, hook registry, tool registry, library implementation or service operation to inspect. Algorithm 1 is a documented invocation, not a shipped interface. Debug/reviewer prompt contents, exact summary construction, raw archives, disk layouts, checkpoint/reload and deletion protocols remain unavailable. Provider internals and model state are opaque; fixed-model declarations are recorded in [RT-CMP-gemini3-flash](runtime.md#rt-cmp-gemini3-flash) and [RT-CMP-claude-opus4](runtime.md#rt-cmp-claude-opus4). No model-weight update follows from the memory account. The wider production product, provider behavior, external benchmark implementations and cited systems are excluded as in boundary; these exclusions prevent broader lifecycle or deployment claims.

| Entry or operation | Frozen source location | Coverage and missing fact | Conclusion prevented |
|---|---|---|---|
| Candidate generation, execution and review | SRC-1 §§2.1–2.2 | Direct read; [MEM-OBJ-candidate-code](#mem-obj-candidate-code), [MEM-OBJ-execution-output](#mem-obj-execution-output), [MEM-OBJ-review-feedback](#mem-obj-review-feedback); supplied [RT-RTE-inner-search](runtime.md#rt-rte-inner-search) | Full artifact schema and reviewer faithfulness unverified. |
| Full-history draft/improve context in AIDE0 | SRC-1 §3.5, appendix E | Direct read; raw code/output objects above | Plain accumulation does not establish transformed experience memory. |
| Root/recent compaction and later prompt delivery | SRC-1 §3.5, appendix E | Direct read; [MEM-OBJ-candidate-summary](#mem-obj-candidate-summary), [MEM-RTE-summary-delivery](#mem-rte-summary-delivery) | Summary producer, recency count, exact budget and reload unknown. |
| Bug-rate-gated failure injection | SRC-1 §3.5 | Direct read; [MEM-OBJ-error-signatures](#mem-obj-error-signatures), [MEM-RTE-failure-injection](#mem-rte-failure-injection) | Frequency estimation, tie-breaking and correction/expiry unknown. |
| Strategy-arm selection and periodic fork | SRC-1 §3.5 | Direct read; [MEM-OBJ-strategy-state](#mem-obj-strategy-state); supplied [RT-RTE-inner-search](runtime.md#rt-rte-inner-search) | State serialization and invocation reset unknown; no strategy-specific episodic archive established. |
| Debug, inner reviewer and outer artifact exploration | SRC-1 §2.2 | Direct read; review-feedback object; supplied inner and admission routes | Separate roles exist, but fresh-context isolation, crossing payloads and full prompt compaction cannot be inferred. |
| Outer history, private-grade acceptance and incumbent reuse | SRC-1 §2.1, algorithm 1, §§3.2–3.3, appendix D | Direct read; annotations on [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code) and [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission) | Archive retention, retracted content, regrade, checkpoint and loading contracts unknown. |
| Fixed reminder, short-output rejection, ranking penalty, scorer repair | SRC-1 §3.5 | Direct confirmation; supplied [RT-OBJ-robustness-instruction](runtime.md#rt-obj-robustness-instruction), [RT-RTE-robustness-controls](runtime.md#rt-rte-robustness-controls) | No automatic failure-signature-to-patch derivation established. |
| Context failure, fallback scoring and compression evaluation | SRC-1 appendix E; appendix A through runtime | Direct appendix E read; [MEM-CLM-prompt-compression](#mem-clm-prompt-compression); supplied [RT-RTE-terminal-fallback](runtime.md#rt-rte-terminal-fallback) | Restart/resume and memory cleanup unknown. |
| AIDE47, AIDEhuman, rejected context variants | SRC-1 appendix E, appendix D, §3.6 | Direct read; compression claim and supplied [RT-RTE-ignition-test](runtime.md#rt-rte-ignition-test) | Their full context policies and rejected context edits are not exposed; AIDE85's failure gate cannot be generalized to them. |

## Core ideas

AIDE85 separates the searchable candidate history from the bounded history delivered to draft/improve. It selects root/recent material and replaces full code/output history with summaries. A second selector conditionally injects a small set of deduplicated final error lines. These are different transformations: a compact history account versus selected execution fragments, with different triggers and budgets. Neither establishes a validated explanation of failures.

The selectors have different authority. Scores and strategy labels feed symbolic parent selection. Summaries, feedback and signatures shape generation through model interpretation. Accepted harness code changes executable selection and context rules across outer rounds; embedded instructions retain advisory force. Retaining code is not the same mechanism as retaining reasons for its design.

Source trust is bounded by the public/private scoring split, not by provenance validation of every context item. Candidate output comes from generated task code; the reviewer extracts a score and feedback; only private grading admits a harness successor. Outer admission can reject a publicly promising rewrite, but noisy grading can still admit a worse true performer. See [RT-CLM-private-signal](runtime.md#rt-clm-private-signal) and [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission). Prompt-size reductions are reported; independent benefit from either memory component is not established.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-candidate-code
Label: Task candidate code history

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Source-native identity: runnable scripts at task solution nodes, including the root codebase. Representational form: symbolic code at execution; when included in a generation prompt, the code also receives model interpretation. Storage substrate: documented solution tree/codebase; physical persistence and schema uninspected. Lineage: supplied task codebase, then draft/debug/improve edits. Consumers: executor, parent-edit generation calls and final private scoring. AIDE0 supplies all prior code in draft/improve prompts; AIDE85's summaries are a distinct derived object, not the executable candidate. Current-run code retention alone is working state, not transformed memory. Initial codebase provenance and human per-content control are unspecified. Subsequent generation is model-authored under the harness; selection is software policy, not evidence of human approval. Evidence: SRC-1 §§2.1–2.2, appendix E; passage in [MEM-CLM-prompt-compression](#mem-clm-prompt-compression). Distinct from [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code), which is the outer harness rather than task solutions.

#### MEM-OBJ-execution-output
Label: Raw candidate execution output

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Source-native identity: execution outputs from evaluating task solutions. Representational form: readable output consumed through model interpretation; underlying structured fields and numerical payload schema uninspected. Storage substrate: candidate history/evaluation artifacts, with actual files and persistence unknown. Lineage: execution of candidate scripts against public evaluation machinery. This is raw trace material, distinct from reviewer feedback, compact summaries and extracted signatures. Consumers: inner reviewer and AIDE0 draft/improve prompts. Automatic production is described; physical write owner and human content admission are not specified. Retention across task runs and provenance integrity are uninspected. Evidence: SRC-1 §2.2 and appendix E; no separately declared counterpart in runtime, only the containing inner route.

> AIDE0\mathrm{AIDE}_{0} employs a reviewer agent that reads execution outputs from evaluating solutions and extracts a score and any relevant feedback.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### MEM-OBJ-review-feedback
Label: Reviewer score and relevant feedback

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Source-native identity: score and relevant feedback extracted by the inner reviewer. Operative parts: numerical score is symbolic at the selector; relevant feedback is natural language at model interpretation. They are separated here by consumer; their exact serialization is unknown. Storage substrate: candidate-associated evaluation state; no artifact schema supplied. Lineage: one reviewer LLM call over each candidate's execution output. The metric/evaluator supplies the outcome; the reviewer interprets/extracts it rather than creating an independent answer oracle. Scores affect later candidate selection; the full feedback-to-generation delivery contract is not exposed. Admission: model extraction, with no described human per-result approval or separate extraction-validity gate. Reasons beyond the extracted feedback, correction history and expiry are uninspected. Evidence: SRC-1 §2.2, quote in [MEM-OBJ-execution-output](#mem-obj-execution-output), and supplied [RT-RTE-inner-search](runtime.md#rt-rte-inner-search). No separate runtime object counterpart.

#### MEM-OBJ-candidate-summary
Label: Compact root and recent-candidate summary

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Source-native identity: compact summary read by AIDE85 draft and improve operators. Representational form: readable summary consumed by model interpretation; exact field structure and whether code excerpts remain are uninspected. Storage substrate: prompt-assembly state, with an independent persisted summary file or checkpoint unknown. Lineage: root/recent candidates selected from prior history; appendix E identifies replacement of the code/output history. Summary authorship is not stated: the paper does not establish a model summarizer versus deterministic rendering. Known curation is bounded selection/compaction, not a proven semantic abstraction algorithm. Consumer horizon: later operator calls within a task run. Full rationale and removed history are not shown to remain in the delivered summary. Admission and delivery are described in [MEM-RTE-summary-delivery](#mem-rte-summary-delivery). Distinct derived payload within the supplied inner route; no separate runtime object counterpart. Evidence: SRC-1 §3.5 and appendix E.

> AIDE85\mathrm{AIDE}_{85} instead has the draft and improve operators read a compact summary of the root and recent candidates rather than the full history.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### MEM-OBJ-error-signatures
Label: Deduplicated recent failure signatures

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Source-native identity: recurring error signatures, defined as final error lines of recent buggy candidates. Representational form: natural-language error fragments at the generation consumer; deduplication/gating acts on symbolic text and counts. Storage substrate: delivered context, with separate archive/cache unknown. Lineage: raw execution failures → final-line extraction → deduplication/selection → draft/improve prompts. This is derived trace-fed memory rather than full error logs or a retained causal diagnosis. Consumers and admission are [MEM-RTE-failure-injection](#mem-rte-failure-injection). The final line can omit preceding causes; no assertion of diagnostic completeness follows. Source evidence establishes selected fragments, not retention of the reasons for failed approaches or model compliance. Distinct object from the robustness reminder in [RT-OBJ-robustness-instruction](runtime.md#rt-obj-robustness-instruction); no duplicate object in runtime. Evidence: SRC-1 §3.5.

> AIDE85\mathrm{AIDE}_{85} also uses a form of failure memory in the context. When a run’s candidates show a bug rate of at least 15%, the agent injects up to three recurring error signatures (the final error lines of recent buggy candidates, deduplicated) into draft and improve prompts.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### MEM-OBJ-strategy-state
Label: Strategy labels and score-based arm state

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Source-native identity: five strategy labels, inherited node labels and arm best scores used by the AIDE85 selector. Representational form: symbolic categorical/numerical state. Storage substrate: search tree and selector working state; backing storage unknown. Lineage: fixed strategy vocabulary in harness, labels inherited along task nodes, scores from candidate evaluation. Consumers: UCB1/softmax arm selector and best-node expansion; periodic forking reuses the global best solution under a different arm. This is decision metadata, not prose experience memory or distributed-parametric model learning. UCB1's complete counter/update representation is not exposed, so do not infer a serialized bandit checkpoint. Admission is automatic label assignment and evaluation-fed score updating within the fixed-budget search; no human per-node approval is described. Evidence: SRC-1 §3.5, quoted selector in [RT-RTE-inner-search](runtime.md#rt-rte-inner-search). No separate object counterpart; this is a material state part of that route.

### Routes

#### MEM-RTE-summary-delivery
Label: Root and recent-history summary delivery

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Endpoints/progression: accumulated candidate history → root/recent selection and compact summary → later draft/improve invocation. Owner: AIDE85 harness context policy; summary-producing agent/function uninspected. Trigger: assembling a draft/improve prompt. Selected payload is [MEM-OBJ-candidate-summary](#mem-obj-candidate-summary), not the entire tree. Budget: documented bounded history and roughly constant prompt size, but no fixed token count or exact recency window. Persistence: survives earlier steps as delivered derived history; across-process or across-run storage uninspected. Authority: model-interpreted context, not executable enforcement of a solution. Operating mode: bounded task search; improvement guidance is recent/root candidate experience. Software policy admits this material into prompts; no human per-summary approval or veto is described. Summarizer authorship, separate semantic validation and rollback are unspecified. Replacing the delivered history is not evidence of deleting raw candidates.

- Immediate return: compact prompt context for draft/improve.
- Later read-back: a later generation invocation consumes a summary derived from earlier candidate history.
- Delegated visibility: draft/improve see root/recent summaries rather than full history; debug/reviewer visibility is uninspected.
- Selection predicate: root and recent candidates; exact recent count, contents and ranking within the summary are uninspected.
- Invalidation or expiry: uninspected — the recent window implies changed selection as search proceeds, but no summary-expiry, correction or persisted deletion contract is supplied.
- Activation or effect: the source reports smaller assembled prompts; reliable generation changes or independent summary benefit are not established.
- Evidence limits: SRC-1 §3.5 and appendix E; quote in the summary object and compression claim; no exact summary code, prompts or raw reconstruction artifacts.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed

#### MEM-RTE-failure-injection
Label: Bug-gated failure-signature injection

Part of: [RT-RTE-inner-search](runtime.md#rt-rte-inner-search)

Endpoints/progression: recent buggy candidate outputs → final error lines → deduplication → gated selection → later draft/improve prompts. Owner/decider: AIDE85 context policy. Trigger: assembling generation context when run candidate bug rate is at least 15%. Automatic admission differs from model authorship of the failed code: software gates and selects trace fragments; there is no described human per-signature approval/veto. Budget: at most three signatures. Operating mode: bounded task optimization, with frequent evaluation errors as the improvement trigger. The public execution failures supply evidence, not an expected-correct-solution oracle. Rejection: below the gate no signature injection is described; this is not evidence of deleting stored failures. Recovery through future generation is intended; no separately validated signature-repair or rollback protocol is exposed. The mechanism retains error text rather than formulated criticism or reasons for harness design.

- Immediate return: up to three deduplicated error signatures in a draft/improve prompt when the gate is met.
- Later read-back: later generation reads selected final error lines from earlier buggy candidates.
- Delegated visibility: code-generation model receives fragments, not necessarily full logs, stack traces or evaluator internals.
- Selection predicate: bug rate at least 15%; recurring final error lines from recent buggy candidates, deduplicated, up to three. Rate denominator, recent window and ties are unspecified.
- Invalidation or expiry: uninspected — gate dormancy is specified, but persistence, withdrawal after a fix, stale-signature filtering and expiry are not.
- Activation or effect: source describes conditional injection; raw gate events and subsequent avoidance of the particular error are unavailable, so delivery does not establish compliance or benefit.
- Evidence limits: SRC-1 §3.5; minimum quote in [MEM-OBJ-error-signatures](#mem-obj-error-signatures); no failure-memory-only ablation or raw traces supplied.
- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: claimed

### Claims

#### MEM-CLM-prompt-compression
Label: Reported bounded-prompt compression

Claimed operation: discovered agents replace full candidate code/output history with bounded summaries; the paper reports approximately constant per-step prompt sizes and end-of-run reductions relative to AIDE0. Source: SRC-1 §3.5 and appendix E, reported operation. Appendix E reconstructs each assembled prompt rather than furnishing the raw requests here. Measurements are characters, task means and run-relative progress, not a specified token/context budget invariant. AIDE47 also has bounded history; only AIDE85's detailed root/recent and failure-gate account is exposed. This is narrower than a guarantee that every role or every future task fits the model window. No duplicate runtime claim: [RT-CLM-harness-improvement](runtime.md#rt-clm-harness-improvement) concerns full-harness improvement, not the prompt reconstruction measurement.

> AIDE0\mathrm{AIDE}_{0} concatenates the code and execution output of every prior candidate into each drafting and improvement prompt, so its prompts grow as its run progresses. The discovered agents replace this history with a bounded summary, so their prompts stay small in comparison.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

> AIDE85\mathrm{AIDE}_{85}, AIDE47\mathrm{AIDE}_{47} and AIDEhuman\mathrm{AIDE}_{\mathrm{human}} did not encounter any such issues.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

The second passage concerns the evaluated runs' context-window terminations. It is author-reported nonoccurrence under those conditions, not an evidenced absence of arbitrary context errors. The captured full-harness comparisons do not independently vary compaction or signatures. Learning as improved future task capacity is reported at the harness level in the runtime claim; trace-fed transformations here establish a retained experience-to-context route, not independent capacity improvement from either component.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-history-context
Label: Derived task history guides generation

Consumer: later AIDE85 draft/improve model invocations. Channel: assembled prompt carries compact root/recent summaries and, conditionally, selected failure signatures. Force: advisory model interpretation; no guaranteed solution change or error avoidance. Horizon: subsequent steps of one task search, not demonstrated cross-task memory reuse. Evidence: SRC-1 §3.5, [MEM-RTE-summary-delivery](#mem-rte-summary-delivery) and [MEM-RTE-failure-injection](#mem-rte-failure-injection). Distinct from [RT-BAP-incumbent-code](runtime.md#rt-bap-incumbent-code), which carries accepted executable organization across outer rounds, and [RT-BAP-robustness-prompt](runtime.md#rt-bap-robustness-prompt), which carries a fixed robustness instruction rather than derived history.

## Annotations

#### On [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code)

Memory horizon is outer rounds and subsequent held-out problems. Retained code carries executable context/selector policies and embedded prompt text; it is not merely a display summary of search. Physical archive, package installation and process reload are uninspected. The known lineage is AIDE0 → proposed incumbent edits → privately admitted successors. Model authorship and software grade admission are distinct from the human choice of initial setup. Public/private outcomes feed that retention chain; retained reasons and criticism are not furnished alongside the complete code in the capture. Evidence: SRC-1 §2.1; minimum accepted-code passage in [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission). The documented code-reuse path can preserve behavior even when historical rationale is unexposed.

#### On [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission)

Read-back targeting has two distinct purposes: previous proposed agents/grades and reviewed evaluation artifacts guide the next rewrite; the current incumbent supplies its edit base. Their exact prompt selection, budgets and artifact contents are uninspected. Accepted code shapes downstream search; numerical grades are decision evidence and symbolic outer-selection inputs, not themselves new executable policy. Rejected code need not become incumbent, but the phrase “previously proposed agents” does not establish that rejected proposals are erased from future guidance. Raw/derived artifact distinctions and error/no-grade history retention are uninspected. No new route is declared because this is the supplied admission route's memory chain. Evidence: SRC-1 §2.1 and appendix D; runtime rejection and incumbent quotes, plus the direct passage:

> At step kk, the outer-loop agent aouta^{\mathrm{out}} reads the previously proposed agents and their grades and proposes a rewrite.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/aide2-6b3bcd4791cf/kb/agentic-system-analyses/state/AAS-2026-10-14-2609-26457-6b3bcd4791cf-01/sources/arxiv-2609.26457v1-2026-10-14.txt`

#### On [RT-OBJ-robustness-instruction](runtime.md#rt-obj-robustness-instruction)

This is persistent static guidance in the accepted harness, not a summary automatically learned from task error lines. Its write agency is the harness rewrite proposer followed by private-grade admission; the paper's experiment setup does not establish per-instruction human approval. Context delivery recurs in generation calls, but reminder-specific benefit and retained historical rationale remain uninspected. Evidence: SRC-1 §3.5 and the safeguard passage in [RT-RTE-robustness-controls](runtime.md#rt-rte-robustness-controls).

## Write side

Task code generation and execution supply raw candidate history; the reviewer transforms execution output into a score and relevant feedback. AIDE0 largely concatenates history. AIDE85 instead selects root/recent material for summary delivery and extracts/deduplicates final error lines for a separate failure gate. These trace-fed transformations produce later generation inputs, not just an archive. Summary creation control remains unknown while subsequent bounded delivery is documented. Neither unknown authorship nor unavailable filesystem I/O suppresses those known transformations.

Admission is per mechanism. Task candidate authoring is model-driven; task parent/final selection is editable harness policy. Reviewer extraction is a model transformation without an exposed validation gate. Summary inclusion uses root/recent selection. Signature inclusion uses a numerical bug-rate gate and a three-item cap. Outer harness retention uses fixed private-grade comparison; this does not imply private grading of each summary/signature. Human experiment design is not per-content approval. See the object and route declarations and [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission).

Maintenance has documented selection and deduplication, but no inspected raw-history deletion, semantic summary correction, signature withdrawal, memory checkpoint or alternate checkpoint form. Recent selection removes older detail from delivered context; it does not show physical deletion. The outer loop can reject a rewrite; appendix D reports rejected context/robustness changes but does not enumerate their payloads. A rejected proposal fails incumbent adoption, not necessarily future historical visibility. The short-code guard rejects stub-like generation for re-prompting; the score penalty reportedly never changes candidate ranking; the scorer patch changes failure handling. Those are not established memory-cleanup mechanisms ([RT-RTE-robustness-controls](runtime.md#rt-rte-robustness-controls)).

The raw → derived → consumer chain is explicit for signatures and bounded summaries. Complete reasons do not necessarily survive final-line extraction or history compaction. The capture does not establish whether summaries retain diagnoses or whether accepted harnesses retain their design arguments. It also does not establish that they omit all reasons. Retained proposal code and scores can support later search without demonstrating content-directed criticism of formulated theories.

## Read-back

[MEM-RTE-summary-delivery](#mem-rte-summary-delivery) and [MEM-RTE-failure-injection](#mem-rte-failure-injection) are automatic prompt-assembly supply routes. The foreground generator is not documented requesting an external memory search. The harness decides what earlier experience enters its next input: root/recent summary, plus up to three signatures when the gate is met. No embedding retrieval, query-driven store, pointer dereference or model-controlled reload is established. That is a conclusion limit within this paper, not an evidenced absence in the uninspected implementation.

Working-context control is preferential replacement of full prior candidate code/output with a bounded root/recent account. Raw history may remain available to the search machinery, but its on-demand recovery into a model window is unspecified. The signatures add selected failures after that reduction. Role-specific prompts do not by themselves establish isolated sub-agent contexts: the inner reviewer makes one call, while the outer reviewer explores artifacts over several steps (SRC-1 §2.2). No pushed/popped frame, fresh fork semantics or complete return payload is shown. The stack-frame lens therefore cannot be asserted as an implementation mechanism; the window contains delivered summaries/fragments by value, not documented references to older records that a model can dereference.

The other retained route is [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission): prior proposal/grade evidence reaches later outer rewriting, and accepted code supplies future inner execution. This has stronger executable authority than advisory history text, but loading and exercised dependence remain attributed. Held-out scoring consumes the chosen task solution; it is not evidence of automatic held-out-feedback reinsertion into the principal search. Early context failure still yields fallback scoring, not a demonstrated resumable memory checkpoint ([RT-RTE-terminal-fallback](runtime.md#rt-rte-terminal-fallback)).

## Integration issues

- No supported correction to a supplied runtime fact is required. The runtime's memory statements are provisional but match the inspected context passages. Its accepted-harness account should remain distinct from derived task history.
- No possible duplicate is proposed after comparison. The six object declarations and two context routes are material parts of [RT-RTE-inner-search](runtime.md#rt-rte-inner-search); their `Part of` relations identify containment rather than replacement. [MEM-BAP-history-context](#mem-bap-history-context) differs from the supplied incumbent-code and fixed-reminder authority paths. [MEM-CLM-prompt-compression](#mem-clm-prompt-compression) concerns prompt reconstruction rather than full-harness research improvement.
- Summary producer, exact retained fields, recency window, fixed budget and historical-reason retention remain unresolved for [MEM-OBJ-candidate-summary](#mem-obj-candidate-summary) and [MEM-RTE-summary-delivery](#mem-rte-summary-delivery). SRC-1 §3.5/appendix E expose bounded delivery but not its implementation. This prevents assigning exact curation agency or semantic completeness.
- Bug classification, rate denominator, signature recurrence/tie selection, stale-error withdrawal and cross-run retention remain unresolved for [MEM-OBJ-error-signatures](#mem-obj-error-signatures) and [MEM-RTE-failure-injection](#mem-rte-failure-injection). SRC-1 §3.5 gives the gate/cap but not those rules; delivery and benefit cannot be equated.
- Reviewer feedback fidelity and delivery, strategy-state reset, and fresh-context isolation remain unresolved for [MEM-OBJ-review-feedback](#mem-obj-review-feedback), [MEM-OBJ-strategy-state](#mem-obj-strategy-state) and [RT-RTE-inner-search](runtime.md#rt-rte-inner-search). SRC-1 §§2.2/3.5 do not expose full prompts or state schemas; a complete context or provenance guarantee is prevented.
- Outer archive coverage, no-grade/rejected-proposal visibility, rationale retention and restart/reload/rollback remain unresolved for [RT-OBJ-agent-code](runtime.md#rt-obj-agent-code) and [RT-RTE-harness-admission](runtime.md#rt-rte-harness-admission). SRC-1 §2.1/appendix D establish proposal history and incumbent selection, not complete retention or withdrawal semantics.
- AIDE47/AIDEhuman full context policies, rejected context variants and alternative checkpoints remain opaque in SRC-1 appendix E/appendix D. [MEM-CLM-prompt-compression](#mem-clm-prompt-compression) supports their reported prompt-size comparison but not attribution of AIDE85's specific gate to them. No component-isolated experiment closes the benefit attribution for either context route.

## Limitations and checks

The complete capture is not a complete executable lifecycle. No repository-tree, dispatch or registry audit was possible, and no target code, models, tests or providers were executed. Bounded source searches and direct reads challenged the inference that all prompt roles use the same memory, that final error lines preserve complete diagnoses, that gate dormancy deletes failures, and that full-harness gains identify memory-component benefit. Each was limited above rather than treated as an invariant or absence.

The capture SHA-256 was rechecked as `8bb54e9df49aa71a3e21fe27569bfa4031a9f53185c84861854e89b1f5e5d772`, matching boundary. Source identity and capture label repeat the supplied identities exactly. The local method checkout was rechecked at `f7732e9c6bc5622031571d2d429bc017253eb64f`; Git status was clean before output creation. Governing inputs were read completely, with runtime's terminal range recovered. The deterministic output check passes; it establishes form, identity and quotation occurrence, not empirical truth or semantic acceptance.
