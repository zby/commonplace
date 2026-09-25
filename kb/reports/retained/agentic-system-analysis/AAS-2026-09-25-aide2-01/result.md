---
type: kb/types/agentic-system-analysis-result.md
description: "Complete documentary analysis of AIDE2's two-loop harness improvement and evolved memory mechanisms."
run-id: AAS-2026-09-25-aide2-01
system: AIDE2
run-date: "2026-09-25"
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: "sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e"
analysis-cutoff: "2026-09-25"
evidence-tier: doc-grounded
memory-comparison:
  scope: "Paper-described retained candidate code, execution outputs, extracted scores and feedback, bounded history/error context, outer candidate code/grade history and accepted harness versions from AIDE0 through AIDE85, including outer-reviewer evaluation artifacts. Static seed instructions, provider/model internals, task/scorer implementations and opaque AIDEhuman internals are excluded. Transient summary persistence is unresolved."
  axes:
    storage_substrate:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-9]
      note: "A solution tree and codebase name logical organization, not a physical store; the paper does not establish the complete storage set or summary persistence."
    representational_form:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-9]
      note: "Executable code and numerical scores establish symbolic parts; evolved prompt instructions establish natural-language parts. Compact summaries and outer evaluation artifacts are not specified sufficiently to certify the full aggregate."
    lineage:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-6, OBJ-9]
      note: "Imported task roots, generated code and trace-extracted scores/errors are described. Summary production and the composition of outer evaluation artifacts remain opaque, preventing a complete lineage set."
    behavioral_authority:
      assessment: known
      basis: claimed
      values: [instruction, knowledge, ranking, routing, validation]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-6, OBJ-7, RTE-1, RTE-3, RTE-4, RTE-6, RTE-7, RTE-2]
      note: "History supplies evidence; evolved prompts instruct; stored scores rank candidates and select an incumbent; learned policies route search/context; the learned short-code check validates generated output. Fixed budget enforcement is outside the accumulated-memory authority set."
    write_agency:
      assessment: known
      basis: claimed
      values: [automatic]
      records: [RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6]
      note: "The described in-run acquisition, review, rewrite and acceptance are automatic. Human development of initial agents is seed provenance, not a described manual maintenance route over this accumulated memory."
    curation_operations:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-3, OBJ-4, OBJ-6, RTE-3, RTE-4, RTE-6]
      note: "Harness revision supports evolve and incumbent selection supports promote. Error deduplication is explicit, but its retained output and the bounded summary transformation are unspecified; a complete memory-curation set cannot be certified."
    read_back_direction:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-1, RTE-3, RTE-4, RTE-2]
      note: "Automatic inner prompt assembly and the outer proposal call establish claimed push. The outer reviewer explores artifacts through an unspecified interface, so the full scoped direction set cannot establish or exclude pull."
    read_back_signal:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-1, RTE-3, RTE-4, RTE-2]
      note: "Full-history, root/recent and bug-rate/budget filtering establish coarse push selection. Summary construction and outer-reviewer access leave additional selection signals unresolved; search-arm labels alone do not establish identifier-based memory delivery."
    trace_learning:
      assessment: known
      basis: claimed
      values: ["yes"]
      records: [RTE-2, RTE-4, RTE-5, RTE-6, OBJ-1, OBJ-6, OBJ-7]
      note: "Execution-derived scores persist for later candidate ranking; evaluation-informed accepted harness rewrites persist and change later task runs. These routes qualify independently of uncertain summary persistence."
    trace_source:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-2, RTE-4, RTE-5, RTE-6, OBJ-9]
      note: "Candidate execution outputs support tool-traces and candidate/grade histories support trajectories. The additional evaluation artifacts read by the outer reviewer are opaque, preventing a complete union."
    learning_scope:
      assessment: known
      basis: claimed
      values: [per-task, cross-task]
      records: [RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6]
      note: "Candidate score adaptation serves subsequent search on the same task; accepted harness changes serve later evaluations across tasks. If bounded summaries also qualify, their described horizon is the same individual task run."
    learning_timing:
      assessment: known
      basis: claimed
      values: [online, staged]
      records: [RTE-2, RTE-3, RTE-4, RTE-5, RTE-6]
      note: "Candidate-derived adaptation occurs online within active search. Harness proposals are graded and selected before their adoption in subsequent task runs, a staged write/evaluate/adopt route. No separate offline training route is described."
    distilled_form:
      assessment: not-determinable
      basis: null
      values: []
      records: [OBJ-2, OBJ-3, OBJ-4, OBJ-6, RTE-2, RTE-3, RTE-4, RTE-6]
      note: "Scores and executable policies supply symbolic products and learned prompt instructions supply natural-language products. Reviewer feedback and potentially retained compact summaries lack enough form/persistence detail for a complete union across qualifying routes."
    faithfulness_tested:
      assessment: known
      basis: claimed
      values: ["no"]
      records: [CLM-1, CLM-2, CLM-3, ABS-1]
      note: "Within the inspected paper, no reported test measures dependence on recalled content. Prompt reconstruction measures size, checkpoint evaluation measures aggregate performance, and the selection replay tests ranking; none tests recall faithfulness."
---

# AIDE2 agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-aide2-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/aide2.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-aide2-01/memory-report.md`

**Memory analysis report SHA-256:** eed1b0ea8e7a981962ba5b8ee36aec6eb4fcad52ead2b747090c3232f6513009

This source-only run names intended destinations; run-state completion separately establishes publication.

## Boundary and evidence

Evidence basis: the paper *Recursive self-improvement of AI research agents*, captured on 2026-09-24 and frozen by the digest above, analysed on 2026-09-25. The target is the described AIDE2 improvement plane: an inner research-agent search and an outer harness-rewrite search, including retained histories and changes from AIDE0 to AIDE85. Boundary kind: complete artifact, partial loop. This characterizes the paper's mechanism and reported results, not inspected implementation.

Included are inner candidate generation/review/selection, outer proposal/grading/incumbent selection, evolved context management, and the reported evaluator repair. Underlying provider/model internals, benchmark/scorer code, actual agent source, opaque internals of AIDEhuman and original run artifacts are excluded. Consequently exact model fixation, isolation, causal implementation paths, scorer integrity and independently observed performance remain uninspected. Dependencies are model calls, task code, public/hidden evaluation data, compute and grading infrastructure. Only the immutable paper supplied system evidence; capture metadata is not runtime evidence.

## Source register

| Source ID | Kind and identity/location | Revision or capture | Evidence layer | Inspected scope/anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|
| SRC-1 | Paper capture, `https://arxiv.org/abs/2609.26457`; local `/home/zby/llm/commonplace/kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` | SHA-256 86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e; 97796 bytes | Doctrine/design | §2; mechanisms in §3.5; Appendix A constraints | No implementation; cannot establish wiring or deployment guarantees |
| SRC-2 | Same frozen paper, `https://arxiv.org/abs/2609.26457` | Same capture and digest as SRC-1 | Reported operation | §§3.2–3.6, Discussion, Appendices C–E | No original traces or runnable candidates; cannot independently observe or causally attribute findings |

## Shared records

### Components

CMP-1 — Outer-loop proposer/reviewer model: Claude Opus 4.7, SRC-1 §2.2. Distributed-parametric model accessed by the outer agent; storage/provider internals uninspected. Parameter-change conclusion status: claimed (model held fixed within loop). Exact-version identity conclusion status: uninspected; a named service model is not a weight hash. Outer reviewer may inspect artifacts over several steps.

CMP-2 — Inner-loop generation/reviewer model: Gemini 3 Flash, SRC-1 §2.2. Distributed-parametric, provider storage uninspected. Parameter-change conclusion status: claimed (held fixed). Exact-version identity conclusion status: uninspected. Inner reviewer makes one LLM call over each solution's execution output. Harness updates do not imply changing either component's parameters.

> During the recursive self-improvement run, we hold the model fixed within each
> loop. The outer-loop agent runs on claude opus 4.7 (Anthropic, 2026b), while every inner-loop
> agent is evaluated with gemini 3 flash (Google DeepMind, 2025).
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

### Operative objects

All existence and representation conclusions below have status claimed. The paper describes code and context, not the exact persisted storage implementation.

| ID | Source-native object | Producer → consumer; form, persistence and evidence |
|---|---|---|
| OBJ-1 | Inner candidate solution tree | Draft/debug/improve → later search and final selector; symbolic runnable code, topology and score metadata; per-task history (§2.1–2.2, SRC-1) |
| OBJ-2 | Candidate execution outputs and reviewer feedback/history | Task execution → subsequent history; reviewer-derived score → candidate ranking. Prose feedback extraction is described, but separate retention/later delivery is uninspected; exact payload form/storage uninspected (§2.2, §3.5, SRC-1) |
| OBJ-3 | Bounded root/recent-candidate summary | Evolved context assembly → draft/improve; compact history, exact representation and persistence mechanism uninspected (§3.5, SRC-1) |
| OBJ-4 | Deduplicated recurring error signatures | Context assembly → draft/improve; recent buggy candidates' final error lines; per-run context selection (§3.5, SRC-1) |
| OBJ-5 | Previously proposed agents and grades, incumbent lineage | Outer proposal/grader → subsequent outer proposal; code and grade archive; exact storage uninspected (§2.1, SRC-1) |
| OBJ-6 | Accepted research-agent harness | Outer search → next rewrite and inner evaluations; symbolic search/context/selection code plus natural-language model instructions; persists across tasks and outer steps (§2.1, §3.5, SRC-1) |
| OBJ-7 | Public task scores and private aggregate agent grade | Evaluators → inner search or outer selector respectively; symbolic measurements; different access horizons (§2.1, SRC-1) |
| OBJ-8 | Held-out scoring script with failure-handling patch | Reported agent repair → subsequent evaluation; symbolic code, admission boundary unclear (§3.5, SRC-2) |

OBJ-9 — Outer-reviewer evaluation artifacts: produced by candidate evaluation and explored by CMP-1 reviewer over several steps. Conclusion status claimed for this access; content, physical store, exact overlap with OBJ-2/OBJ-7, lifetime and interface uninspected. SRC-1 §2.2; RTE-2 outer branch.

### Routes

All described route operation conclusion statuses: claimed. Implementation conclusion status: uninspected. These records distinguish scheduling and effects from model decisions. No declared protocol is promoted to an enforced guarantee.

RTE-1 — Inner search: operator supplies a task codebase, measurable public metric and dollar budget. The harness selects draft/debug/improve and a parent candidate. CMP-2 proposes code; task execution produces outputs; RTE-2 interprets them; search repeats until budget exhaustion, then RTE-7 returns a solution. AIDE0 greedily expands the highest scorer. AIDE85 instead selects among five fixed strategy arms using UCB1 with 30% softmax arm sampling, expands the best node on that arm and forks the global best under another arm every five steps (SRC-1 §2.1–2.2, §3.5). Immediate output is candidate code/execution; later read-back is prior candidates and feedback. Labels select parents, but do not alone establish identifier-based memory injection. Search policy is symbolic, code-generation choices are model-mediated. State spans OBJ-1 and OBJ-2; external effect boundary is task code execution. Debugging handles reported bugs; deployed containment/recovery is uninspected. BAP-1.

RTE-2 — Review: after execution, a reviewer extracts score and relevant feedback from OBJ-2. Inner review is one model call; outer review may explore evaluation artifacts over several steps. Retained scores guide later parent selection through OBJ-7. Exact persistence and later consumption of reviewer prose feedback remain uninspected. The outer branch reads OBJ-9 across several steps; whether it requests artifacts or receives automatic selections, and their overlap with other objects, are uninspected. The reviewer supplies interpretation, not an independently trusted answer oracle. Public benchmark evaluation supplies the task-specific measurement/reference. Feedback selection and exact retention mechanics are uninspected; broader outer-reviewer content and read-back directions/signals remain unresolved rather than guessed from the word explores. SRC-1 §2.2; BAP-2.

> highest-scoring solution becomes the parent for the next operation. AIDE0 employs a reviewer agent
> that reads execution outputs from evaluating solutions and extracts a score and any relevant feedback.
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

> the inner-loop reviewer makes a single LLM call over each solution’s execution output, while
> the outer-loop agent’s reviewer explores the evaluation artifacts over several steps.
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

RTE-3 — Context management: in AIDE0, draft/improve receive concatenated previous candidate code and outputs. In AIDE85, those operators receive OBJ-3 rather than full history, plus up to three OBJ-4 error signatures only when candidate bug rate reaches 15%. The harness selects the root/recent candidates and deduplicated recent error lines; consumer did not request each retained item. Immediate return is assembled context for a later model call, not a user answer. Per-run retention of input history is described; whether summaries persist independently or are rebuilt, and exact selector identities/forms, remain uninspected. No cross-task error-memory lifetime is established. SRC-1 §3.5; SRC-2 Appendix E; BAP-3.

> the draft and improve operators read a compact summary of the root and recent candidates rather than
> the full history. AIDE85 also uses a form of failure memory in the context. When a run’s candidates
> show a bug rate of at least 15%, the agent injects up to three recurring error signatures (the final error
> lines of recent buggy candidates, deduplicated) into draft and improve prompts.
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

RTE-4 — Outer proposal: AIDEhuman, driven by CMP-1, reads prior agents/grades (OBJ-5), edits the current incumbent OBJ-6 and proposes a runnable harness rewrite. Guidance consists of code, evaluation outcomes and reviewer diagnosis, not a supplied catalogue of proven improvements. Changes can affect search, memory, prompts and inner final selection. Proposal writer is computational; humans define initial agents, task suite, budgets and protocol. RTE-6 decides promotion; no human per-rewrite veto is specified in the reported autonomous run. A new candidate is returned to RTE-5 and remains in the outer search history. Exact recovery of malformed or crashing rewrites is uninspected; SRC-2 Figure 2 reports buggy proposals receive no grade. BAP-4; SRC-1 §2.1.

> In practice, the outer-loop agent edits the current incumbent, so each accepted rewrite becomes
> the codebase that is edited at the next step. At step 𝑘, the incumbent is the best agent graded so far.
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

> level up. At step 𝑘, the outer-loop agent 𝑎out reads the previously proposed agents and their grades
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

RTE-5 — Grading check: each proposed agent runs as an inner optimizer on the fixed selection suite of ML, heuristic and harness engineering tasks. It receives public optimization scores and a fixed per-task cost budget including tokens and solution execution. It selects a final solution. Held-out private scoring evaluates that returned solution and aggregates scores over tasks and repeats into OBJ-7. Check output is a grade to the outer loop, not immediate successor admission. Benchmark designers supply reference outcomes/data and scoring authority; exact formulas, access enforcement and oracle validity remain uninspected. Hidden data are hidden from the optimizing inner agent; aggregate grade is visible to outer search, so it is itself a selection signal rather than untouched external validation. BAP-5; SRC-1 §2.1–2.2.

> Candidate selection differs between the two levels: inner-loop selection is part of the agent’s editable
> policy and is repeatedly rewritten during the run, whereas outer-loop selection is fixed by:
> 𝑎∗𝑘 = arg max 𝑔 ( 𝑎)
> 𝑎 ∈ 𝑎≤ 𝑘
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

RTE-6 — Incumbent admission: the fixed outer selector chooses the highest private grade among evaluated agents. Only an improvement replaces the incumbent; later RTE-4 edits that code and later RTE-5 evaluates it. Rejection leaves the incumbent intact but proposal/grade history remains available. Guarantee owner is the outer protocol; point is max-grade selection; strength protocol; conclusion status claimed. Required external contracts: comparable grades, fixed task budgets and reliable private scoring. The gate can reject public-score wins; SRC-2 Appendix D reports this for about a quarter of graded rejected rewrites. Crash recovery and external manual bypasses are uninspected. BAP-6.

RTE-7 — Inner final selection and generation guard: inner agent code chooses returned OBJ-1, and the outer search may rewrite that policy. AIDE85 re-prompts when generated code has fewer than 40 characters, which rejects near-empty output without proving correctness. A score penalty based on distance from the top-candidate median is described as a robustness rule; SRC-2 §3.5 reports it preserved candidate ordering and never changed the selected candidate in replay. These checks have different force: the short-code guard changes generation, while the penalty had no reported selection effect. Immediate return is one selected solution to RTE-5; no broad robustness guarantee follows. BAP-7.

> Because the penalty preserves the
> ordering of the candidates, replaying the rule over the held-out runs shows that it never changed
> which candidate the agent selected.
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

> a fixed instruction in every code-generation prompt reminding the model that solutions are scored on
> a private split it cannot see and that it should prefer robust, generalizable approaches, and a guard that
> re-prompts when generated code is nearly empty (under 40 characters, e.g. a stub or placeholder).
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

RTE-8 — Evaluator repair: SRC-2 §3.5 reports an agent patch to OBJ-8 so one failed test case no longer crashes the whole held-out evaluation. Trigger is evaluator failure; proposal is code correction; claimed effect is narrower failure propagation. Who independently verified/admitted that evaluator change, ability to veto it, preservation of scoring semantics and rollback are uninspected. This is a distinct revision mechanism, not silently folded into performance-gated harness admission. A favorable narrative cannot establish protected measurement integrity. BAP-8.

> One task’s held-out scoring script crashed on all of its test cases whenever
> any single test case failed, and AIDE85 adds a small patch,
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

### Claims

CLM-1 — Repeated harness improvements transfer to held-out tasks. Conclusion status claimed. SRC-2 §3.2 reports 99 proposals and seven accepted rewrites over eight days, grade 0.703 to 0.778, plus two other runs with two and four improvements. §3.3 reports gains on four external benchmarks. This supports the authors' bounded harness-improvement account; it does not identify each mechanism's effect or demonstrate an accelerating improvement loop.

> Because candidates were selected on 𝑔,
> the recursive self-improvement trace is not meant to demonstrate generalization beyond the selection
> pub
> benchmark.
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

CLM-2 — Bounded context reduces prompt growth. Conclusion status claimed; SRC-2 §3.5/Appendix E report rebuilt prompts from held-out runs, with late-run reductions from 7× to around 50× versus AIDE0 depending on benchmark, and context-limit failures only in the baseline comparisons. This is a reported size/recovery result, not a faithful-recall test or isolated proof of task-performance gains from compaction.

CLM-3 — Discovered agents can drive further outer-loop improvement; superiority as self-improvers is unresolved. Conclusion status claimed; SRC-2 §3.6 compares AIDE47 versus AIDEhuman over three seeds each from the same inner agent, with similar mean endpoints. The evidence does not establish the claimed stronger ignition condition.

> with only three seeds per outer-loop agent, we find these results to be inconclusive; they do not
> establish that AIDE47 is more sample-efficient as a self-improver than AIDEhuman .
> --- `kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md` @ `sha256:86d1b094380280450bf2281b1e38945a4f0c2528f2b88aebdf9ea8b9a1e8da8e`

CLM-4 — Reduced reward hacking. Conclusion status claimed; SRC-2 §3.4 reports 55% to 32% across 38 held-out kernel/training-context pairs, using proxy versus downstream behavior. The paper explicitly does not identify which rewrites caused the change. It is not a general guarantee against metric exploitation.

### Evidenced absences

ABS-1 — Conclusion status absent, bounded to reported recall-dependence or summary-faithfulness testing in this paper. Inspected SRC-2 §§3.2–3.6 and Appendices A–E plus full-capture searches for memory, feedback, summaries, artifacts, recall, retrieval and ablation. Reported checkpoint performance, prompt-size reconstruction and ranking replay do not test dependence on particular recalled content. This supports the scoped faithfulness-tested no, not an implementation-wide absence. Other missing implementation/original traces remain access limits.

### Behavioral-authority paths

| ID | Consumer | Channel | Force and horizon | Evidence |
|---|---|---|---|---|
| BAP-1 | Inner search | Retained candidate scores/tree | Ranking and parent choice during one task | SRC-1 §2.2, §3.5 |
| BAP-2 | Later operators | Reviewer feedback/history | Advisory diagnosis and score-derived ranking in later steps | SRC-1 §2.2 |
| BAP-3 | Draft/improve model | Assembled summary/error context | Advisory guidance per subsequent call | SRC-1 §3.5 |
| BAP-4 | Outer proposer | Prior agent code and grades | Evidence/instruction shaping next rewrite | SRC-1 §2.1 |
| BAP-5 | Outer selector | Private aggregate grade | Validation evidence for candidate agent | SRC-1 §2.1 |
| BAP-6 | Next outer/inner loop | Admitted harness code | Enforced-by-design algorithm and prompt instructions until replaced | SRC-1 §2.1 |
| BAP-7 | Inner generation/final selector | Length guard/score penalty | Re-prompt or ranking policy within current task; no observed penalty effect here | SRC-1, SRC-2 §3.5 |
| BAP-8 | Held-out evaluator | Patched failure handling | Changes evaluation execution; exact admission authority unresolved | SRC-2 §3.5 |

## Runtime account

A benchmark operator chooses initial AIDE0, the human-engineered outer agent, task suite, models and budgets. RTE-4 proposes an incumbent rewrite. RTE-5 runs that candidate on tasks; internally RTE-1 generates code, RTE-2 reviews outputs, RTE-3 assembles retained context, and RTE-7 returns a selected solution. RTE-5 privately scores that solution. RTE-6 admits the best agent and retains its code for the next step. Terminal output is the best agent after the bounded search. This is a bounded experiment, not an open-request service. Human design choices are initial conditions; the reported run supplies no evidence of per-candidate human intervention.

The operating answer oracles are task-specific reference outcomes and hidden evaluation data, not the reviewer model. Public scores guide inner search, private grades select outer agents, and four further benchmarks assess generalization without feeding that search. These are three distinct horizons. Holding token/execution budgets fixed constrains the comparison, but reported held-out benchmark constraints also include step caps and time safeguards (SRC-2 Appendix A); no unlimited efficiency claim follows.

Material alternatives: AIDE0 uses full history and greedy selection; AIDE85 uses bounded context and strategy allocation; the ignition test substitutes a discovered outer agent for AIDEhuman; RTE-8 changes an evaluator rather than only an agent. No code reveals direct model calls, shell/subprocess bypasses or deployed permission grants, so those remain uninspected and no isolation guarantee is asserted.

Three documentary forcing cases: a public-score improvement can fail private-grade admission (RTE-6); a buggy rewrite can remain ungraded while incumbent retention allows continued search (RTE-4, RTE-6); error memory stays dormant below 15% bug rate, then supplies up to three signatures above it (RTE-3). Short-code reprompt and the inactive ranking penalty are further described controls, not executed tests here. No dynamic check planned: no implementation, executable candidate, credentials, scorer bundle or authorized target environment was supplied.

Guidance and theory-path classification: SRC-2 Figure 2 attributes a root-cause-before-fix instruction to an accepted rewrite; §3.5 describes a diagnosis about plateaued lineages and context growth. Formulation conclusion status claimed for these explanations; operative-use conclusion status claimed for code/prompt changes and outer diagnosis; content-directed criticism conclusion status uninspected without original reasoning/consequence tests; resulting revision conclusion status claimed; improved research capacity conclusion status claimed at bundle level, but improvement attributable specifically to holding and criticizing an operative formulated theory remains uninspected. Code is individually editable, but full semantic addressability of assumptions and scope is uninspected. Accepted code persists; complete rationale/criticism preservation and later reading are uninspected.

Reflection conclusion status claimed: agent code and performance history represent aspects of the inner research process; execution changes that history, and history-mediated edits change later behavior. Self-improvement conclusion status claimed for the reported harness lineage and held-out outcomes. The fixed outer protocol's autonomous improvement, or improved self-improver efficiency, is not established by this connection; CLM-3 is explicitly inconclusive.

## Lens scoping

### Memory/context scope

Full documentary lens; triggers SRC-1 §3.5 and CLM-2. Included OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-9 and their RTE-1, RTE-2, RTE-3, RTE-4, RTE-6 later-consumer routes. Account separately for AIDE0 history, evolved context, and outer retained harness changes. Storage and opaque payload details remain uncertain. Exclude task-trained model weights, provider internals, task/scorer implementation OBJ-8 and static instructions not changed through use. The reported scorer repair remains a baseline/epistemic route; no memory store or later rationale reader is inferred from it.

### Epistemic scope

Full documentary lens. Triggers: CLM-1, CLM-3, CLM-4 and proposed self-improvement/warrant claims. All eight routes are assessed at described scope, including evaluator mutation. Missing original artifacts prevents observed lifecycle states; opaque reviewer/model processing prevents inferring content criticism merely from a successful rewrite.

## Lens outputs

### Memory/context lens

The fresh specialist distinguishes two established claimed adaptation routes. RTE-2 extracts execution-derived scores that remain with candidate history and shape subsequent RTE-1 ranking within a task. RTE-4, RTE-5 and RTE-6 use evaluation history to produce and retain an accepted harness, which shapes later tasks and further rewrites. The latter is durable procedural adaptation even without a named memory database. These routes support trace-learning yes, per-task and cross-task horizons, and online/staged timing. They do not establish conjectural learning through criticism.

RTE-3 supplies compact root/recent context and conditional error signatures, but the paper does not say whether these transformed products persist separately or are rebuilt per prompt. Both interpretations fit; the route cannot independently establish durable summary learning. If it qualifies, its described horizon is the same task and its timing online, so those aggregate axes remain known. Unknown summary and outer-artifact payloads prevent complete store/form/lineage/curation/source/distilled-form sets; the profile preserves that uncertainty. A logical tree does not establish graph storage and a codebase does not establish a Git repository.

Automatic inner prompt assembly and outer history supply are push. Default selector inputs are all history, root/recent candidates, recent buggy outputs, the 15% gate and three-signature limit: coarse selection. Search-arm labels select parents, not demonstrably delivered memory. The RTE-2 outer branch explores OBJ-9 using an unspecified interface, preventing a complete direction/signal set rather than allowing an invented pull or semantic retrieval route.

Retained content supplies knowledge, evolved prompt instructions, score ranking, learned search/context routing and the evolved short-code validation rule. Human authorship of the seed agents is not an in-run manual-memory write route. The private-split reminder supplies a limited rationale to later generation; paper explanations of forking and agent analyses of rejected ideas do not establish retained explanations with later readers. Prose reviewer-feedback reuse likewise remains uninspected. Faithfulness-tested no is bounded by ABS-1; prompt-size or checkpoint comparisons do not test recalled-content dependence. RTE-7's reported inactive ranking penalty prevents assigning benefit from retained presence alone.

### Epistemic lens

1. **Source-and-claim boundary.** Source register SRC-1 supplies mechanism declarations and SRC-2 attributed empirical findings. Question: what checks license candidate solutions and agents, and what do those checks leave open? All material route families above are assessed; model internals, scorer implementations and original runs remain unassessed. CLM-1, CLM-3 and CLM-4 are the consequential improvement/generalization claims.

2. **Epistemic-object annotations.** OBJ-1 and OBJ-6 are operative code with possible embedded predictions/diagnoses, not automatically formulated explanatory theories. Their default update class is direct policy adaptation; particular truth-apt content remains indeterminate without original candidates. OBJ-2 acquires execution evidence plus model interpretations; interpretation may reshape or conjecture, but exact content is opaque. OBJ-3 compression intends reshaping; fidelity/possible ampliation is indeterminate. OBJ-4 selects observed error text rather than establishing error causes. OBJ-5 retains agent code and measurements; OBJ-7 measures a particular evaluator/task distribution. OBJ-8 changes measurement machinery and requires its own validity account. OBJ-9 is acquired evaluation material whose exact interpretation and retention are opaque; no produced truth-apt candidate is established. Canonical identity/form/ownership remain in Shared records.

3. **Authority-route ledger.** Architectural status is doctrine only for mechanism descriptions, including reported repairs without inspected execution artifacts. Observed candidate state is no instance observed at this boundary. Implemented force is uninspected; described consequences follow BAP records.

| Route | One function per row; content/update relation | Target, evaluator, timing and operational consequence | Epistemic license / limit |
|---|---|---|---|
| RTE-1 | Content transformation; non-truth-apt code/policy update, truth-apt parts indeterminate | Operator model proposes task solution | Candidate capability, not proven explanation |
| RTE-1 | Check/evidence production; acquisition | Run solution against public metric | Public task outcome, not hidden generalization |
| RTE-2 | Content transformation; indeterminate reviewer interpretation | Model extracts feedback/score after execution | Depends on faithful interpretation; no model-as-oracle assumption |
| RTE-3 | Content transformation; intended non-ampliative compaction/selection | Root/recent history and gated signatures → later model context | Reduced context size does not certify preserved meaning |
| RTE-3 | Operational consumption; no content change | Draft/improve use selected retained context | Advisory behavior influence; faithful activation uninspected |
| RTE-4 | Content transformation; policy/code adaptation | Outer model revises incumbent from history | Candidate agent; no theorem of improvement |
| RTE-5 | Check/evidence production; no candidate content change | Returned solutions privately scored across fixed tasks/repeats | Estimated selected-task research performance under budgets |
| RTE-6 | Disposition/acceptance; no content change | Fixed max-grade rule admits agent | Performance-relative acceptance, vulnerable to noise |
| RTE-6 | Retention; no additional content change | Accepted code/history kept for later steps | Availability and successor identity, not explanatory warrant |
| RTE-6 | Behavior/policy adaptation; successor replacement | Admitted harness operates in later evaluations | Reported persistent algorithm change; component effects unresolved |
| RTE-7 | Operational admission/selection; no content change | Length guard re-prompts; penalty ranks candidates | Minimal code presence/score ordering, not correctness |
| RTE-8 | Content transformation; evaluator code adaptation | Patch failure handling | Claimed recovery; independent semantic/integrity acceptance uninspected |

Rows cite their canonical source anchors and BAP-1, BAP-2, BAP-3, BAP-4, BAP-5, BAP-6, BAP-7, BAP-8 respectively. CLM-1 concerns RTE-4, RTE-5, RTE-6; CLM-2 RTE-3; CLM-3 outer-loop substitution; CLM-4 held-out behavior. Operational performance acceptance is not silently upgraded into epistemic endorsement of diagnoses.

4. **Per-object lifecycle disposition.** OBJ-1, OBJ-6 and OBJ-8 have no individuated truth-apt candidate output evidenced here; their direct-adaptation routes are RTE-1, RTE-4, RTE-6 and RTE-8. Their possible embedded claims remain indeterminate among reshaping, derivation and ampliative conjecture, with original proposal/rationale and tests needed to decide. OBJ-2 reviewer interpretations and OBJ-3 summaries also remain indeterminate; inputs and faithful outputs are needed. OBJ-9 is an opaque acquired evidence container; its truth-apt contents and transformations are indeterminate until original artifacts and access traces exist. OBJ-4 error-text selection, OBJ-5 history retention and OBJ-7 measurement have acquisition/reshaping routes, not demonstrated ampliative discovery lifecycles. No original candidate-linked trace establishes formulation, derivation, test of an explanation, truth acceptance or post-acceptance integration. For the paper-reported plateau diagnosis, formulation/operative adaptation is claimed; direct criticism and lifecycle phases are not determinable architecturally and have no instance observed in inspectable original evidence. Numeric selection of code cannot fill these missing phases.

5. **Claims versus routes.** CLM-1 has design support RTE-4, RTE-5, RTE-6 and reported accepted lineages plus external benchmark comparisons; no independently observed or causal support here. CLM-2 has described compaction and reported reconstructed size curves, but no isolated memory-fidelity effect. CLM-3's experimental comparison explicitly stops short of superiority. CLM-4 reports changed behavior for the whole evolved bundle and explicitly leaves component attribution unresolved. The fixed outer objective and RTE-8 evaluator mutation require distinct authority accounts.

6. **Bounded conclusion.** AIDE2 describes evidence-responsive code search with separate public task feedback, private agent-selection grades and external generalization checks. It reports persistent harness improvements and transfer under bounded protocols. These license a reported self-improvement finding at the harness level. They do not license a stronger claim that the system improves its own improvement efficiency, that a particular explanation was accepted as true, or that evaluation integrity survives every code mutation.

## Reconciliation

The report's run/source/boundary, input digest, complete status and source quotations matched. Proposal mapping: MEM-OBJ-1 → OBJ-9; MEM-RTE-1 → the already described outer-reviewer branch of RTE-2; MEM-ABS-1 → ABS-1. The merged route retains its existing review identity and gains the explicit opaque-artifact boundary; no canonical ID is repurposed.

All seven specialist issues are retained: opaque outer artifacts/access; bounded faithfulness-test absence; score/raw-history reuse separated from unproven feedback-prose reuse; summary/error-product persistence unresolved; search labels separated from memory delivery; accepted outer harness changes counted as trace-fed adaptation; inactive penalty and inconclusive outer-agent comparison preserved. Generic records and epistemic annotations were narrowed accordingly. Memory findings come from the specialist, with aggregate uncertainty preserved. Both passes distinguish retained presence from effective operation; this is analytical convergence, not independent empirical replication.

## Bounded synthesis

AIDE2's strongest reported result is a retained lineage of improved research harnesses that performs better on held-out benchmarks under stated budgets. Its two loops separate public feedback used to optimize task solutions from private scores used to select agents. A further external test boundary is needed because the outer loop itself sees the private aggregate grade. The evolved code changes both search allocation and context delivery, so the result is more than a static prompt adjustment, but individual component contributions remain unresolved.

The paper supports self-improvement with conclusion status claimed at the harness lineage boundary. Reflection has conclusion status claimed for code/performance representations guiding later edits. Conjectural learning attributable to criticism of operative formulated theories remains uninspected: diagnosis and root-cause instructions are reported, but score selection alone does not establish that process or its effect. Superior self-improver efficiency remains unresolved by the ignition test. The reported inactive ranking penalty illustrates why a retained mechanism should not be assigned credit merely because it appears in the winning agent.

Pinned code, original run artifacts, candidate-linked diagnosis/criticism, controlled component comparisons and a verified evaluator-change authority boundary would materially strengthen or change these findings. More outer-loop seeds and independent final-agent evaluation would address the narrower ignition uncertainty.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| No code or original executions | SRC-1, SRC-2; all routes | Immutable paper | Wired/observed/causal conclusions | Pinned agents, scorer code and raw records |
| Provider identity and internals opaque | CMP-1, CMP-2 | §2.2 | Exact parameter/endpoint fixation | Immutable model/version metadata |
| Summary storage/form and preservation unspecified | OBJ-2, OBJ-3, RTE-3 | §3.5, Appendix E | Complete aggregate memory classification and faithful recall | Exact assembler and retained inputs/outputs |
| Bundled agent changes and noisy grades | CLM-1, CLM-4, RTE-6 | §§3.2–3.5, Discussion | Individual mechanism attribution and guaranteed improvement | Replications and controlled interventions |
| Evaluator itself reportedly patched | OBJ-8, RTE-8 | §3.5 | Independent measurement integrity | Patch/admission audit and unaffected reference evaluator |
| Ignition comparison inconclusive | CLM-3 | §3.6 | Improved self-improvement efficiency | More seeds and external final-agent evaluation |
| Dynamic task model training lies outside agent-memory scope | OBJ-1, CMP-2 | §2.2 | Confusing task model weights with harness learning | Separate task-level analysis if needed |

## Verification and blockers

### Semantic verification

Capture digest and output guard verified before inspection. Different inner/outer/reference evaluation horizons retained. Model fixity separated from harness adaptation; evaluator mutation has its own record. Ordinary flow and private/public disagreement, buggy candidate and conditional failure-memory cases traced documentarily. No mechanism receives observed or causal status from prose reports. Integrated profile checked against OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-9 and RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7. Score-derived ranking and outer harness adoption both qualify; compaction remains an unresolved durable-write candidate whose horizon/timing do not expand the known union. Push consumers/predicates specified; opaque outer access prevents unsupported complete direction/signal values. Storage/form/source uncertainties retained across the entire declared scope. Source/status amendments preserve identity and lens overlays cite canonical records.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-aide2-01/result.md`; `commonplace-validate --full` passed with no failures or warnings.

### Blockers

None.
