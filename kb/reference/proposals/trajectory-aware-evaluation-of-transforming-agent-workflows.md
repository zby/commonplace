---
description: "Proposal: compare blinded output-only and trajectory-aware judges on transforming agent workflows before adding trajectory evaluation to closure"
type: kb/types/note.md
traits: [design-proposal, has-external-sources]
tags: [evaluation, agent-runtime]
status: seedling
---

# Trajectory-aware evaluation of transforming agent workflows

An agent can finish with a plausible artifact while failing inside the route that produced it: reusing a worker that should have been fresh, reading stale input, silently accepting a failed tool call, omitting a required method, or claiming completion without durable evidence. An output-only judge cannot observe those failures when the final artifact papers them over. A trajectory-aware judge can inspect prompts, model calls, tool calls, intermediate artifacts, errors, recovery, and lifecycle events—but its extra context and discretion may also create false positives, length bias, inconsistency, and much higher cost.

This proposal defines a controlled comparison before Commonplace adds trajectory judging to any workflow. The motivating [agent-as-a-judge framing](https://x.com/aparnadhinak/status/2075688574960488558) argues that agent failures live in trajectories and therefore need an agent capable of investigating them. Commonplace has suggestive local evidence from manually inspecting full-improvement-pass traces, but that inspection had no blinded output-only control. The proposal turns that observation into an evaluable design rather than treating trajectory access as an automatic improvement.

## Current state (as of 2026-07-11)

- `run-full-improvement-pass-on-note.md` is a transforming workflow with explicit method order, fresh-worker requirements, final-byte reassessment, retained reports, and a one-cycle stopping rule.
- Five transformation-closure runs retained initial and closing reports, control outputs, observation records, and enough pass history to identify candidate runs. Complete chronological model/tool traces are harness-owned rather than canonical Commonplace artifacts, so trace completeness must be checked before a run enters the comparison.
- An earlier manual trace audit found orchestration confusion, including worker-lifecycle ambiguity, and led to clearer fresh-worker instructions. It was useful diagnosis, not an evaluation result: the reviewer knew the trajectory and there was no output-only arm.
- Commonplace review gates and critique assess note content. They do not evaluate whether the orchestrator followed the workflow that produced the note. This proposal is protocol meta-evaluation, not another note assay and not another review `result_kind`.
- The review system has no trajectory store, judge runner, trajectory rubric, or acceptance semantics for workflow-level judgments.

The system distinction rests on [reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md): reconstructing a plausible successful route from a good output is not checking the route that actually ran. The harness survey independently places trajectory and intermediate-state evaluation inside the harness evaluation interface rather than after final-output generation.

## Proposed comparison

Build a small paired benchmark from complete full-improvement-pass histories. Each case has one frozen workflow request, its final artifacts, and—only for the trajectory arm—the chronological execution record. Run two independent judges against the same rubric:

1. **Output-only judge.** Receives the original request, operative workflow contract, final note, final pass report, and declared completion evidence. It cannot inspect intermediate prompts, worker identities, tool results, or temporal ordering.
2. **Trajectory-aware judge.** Receives the same material plus read-only tools for locating and inspecting the frozen chronological trace and retained intermediate artifacts. It chooses what evidence to inspect and must cite the exact event or artifact supporting each finding.

Both judges answer the same questions:

- Were all required methods and transformations actually executed?
- Were isolation, freshness, ordering, ownership, and worker-lifecycle constraints followed?
- Did tool failures or malformed results receive valid recovery?
- Does each completion claim have matching durable evidence?
- Did the workflow violate a process constraint while still producing an acceptable-looking final artifact?

Judges emit structured findings with `requirement`, `status`, `evidence`, `severity`, and `explanation`. They do not edit artifacts or propose workflow fixes during scoring.

## Gold standard and blinding

A human adjudicator reviews the union of findings after both arms finish, without seeing which arm produced each finding. The adjudicator labels each finding confirmed, unsupported, or indeterminate and records the minimum evidence needed to decide it. Cases with incomplete traces remain eligible for the output-only arm but cannot support claims about trajectory-judge recall; they are reported separately rather than treated as clean negatives.

Natural traces alone may contain too few known failures. The comparison may therefore add paired, semantics-preserving trace mutations—such as replacing a fresh worker with a reused one, hiding a failed tool result behind a successful-looking report, or reordering two required stages—while leaving the final artifact unchanged. Mutation authorship and condition remain hidden from judges and adjudicators until labels are locked. Natural and mutated cases are reported separately so injected detectability is not mistaken for production prevalence.

Repeat each arm on the same cases enough times to measure within-judge consistency. Randomize case and arm presentation, keep rubrics identical, and cap the trajectory judge's evidence budget so “read everything” is not the hidden treatment.

## Measurements

The primary measurement is **confirmed incremental detection**: process failures found by the trajectory-aware arm and missed by the output-only arm. Report it beside:

- confirmed findings shared by both arms;
- false-positive and indeterminate rates by arm;
- evidence-localization quality;
- repeat-run agreement on the same case;
- cost, latency, and trace events inspected;
- sensitivity to trajectory length;
- results split between natural and mutated cases.

Final-artifact quality is not the gold label for process compliance. A good output can coexist with a real protocol violation, and a protocol-compliant run can still produce a weak note. The comparison measures whether trajectory access improves discrimination over workflow execution, not whether the trajectory judge prefers the final prose.

## Option space and free choices

- **Corpus source:** retrospective retained passes, prospectively instrumented passes, controlled mutations, or a mix. Retrospective cases are cheap but may have incomplete traces; prospective cases improve capture while risking observer effects; mutations supply known contrasts but weaken prevalence claims.
- **Trajectory representation:** raw harness transcript, normalized chronological events, or both. Raw traces preserve evidence but couple the benchmark to one harness; normalized events improve portability but may erase the failure being tested.
- **Judge tools:** direct full-trace context, indexed read-only search, or staged disclosure. Full context is simplest and most vulnerable to overload; search makes the judge genuinely agentic but adds tool-policy variance.
- **Adjudication:** one human with documented evidence, independent humans followed by consensus, or a third blinded agent plus human escalation. Stronger consensus costs more and is most important for ambiguous natural failures.
- **Decision threshold:** any confirmed unique failure, a minimum incremental-detection rate, or a cost-adjusted threshold. The threshold must be chosen before results are read.
- **Operational destination if adopted:** an on-demand workflow audit, sampled production audit, or required closure step. The experiment selects whether trajectory judging adds value; it does not by itself select deployment frequency.

## Forces and risks

- **Trace completeness:** a judge cannot verify absent events. Missing telemetry must remain “unknown,” never “compliant.”
- **Judge self-similarity:** the evaluating agent may share the orchestration biases of the agent it judges. Evidence citation and blinded human adjudication constrain but do not remove this risk.
- **Length bias:** longer trajectories expose more inspectable surface and may attract more findings even when the extra steps are harmless.
- **Hindsight reconstruction:** a judge may infer an ideal route from the final artifact and then hallucinate deviations. Findings require event-level evidence.
- **Sensitive context:** raw traces may contain credentials, user data, or unrelated context. Corpus construction needs redaction without erasing process evidence.
- **Harness coupling:** worker identities, tool events, and lifecycle operations differ across harnesses. A normalized representation may become necessary before any framework-level adoption.
- **Cost displacement:** a full agent judge per run may cost more than the workflow failures it catches. Sampling and escalation remain deployment choices, not assumptions.

## Adoption criteria

Do not add trajectory judging to the full-improvement-pass instruction or review store merely because the trajectory arm finds more issues. Adopt a workflow-level audit only if the preregistered comparison shows:

1. confirmed process failures that the output-only arm systematically misses;
2. an acceptable false-positive and indeterminate rate under blinded adjudication;
3. repeatability sufficient to make the same run receive materially consistent judgments;
4. evidence localization precise enough for an operator to verify and fix the failure;
5. measured cost and latency compatible with a stated sampling policy; and
6. a trace capture boundary that can be implemented without silently treating missing events as success.

If the trajectory arm adds no material discrimination, retire the proposal. If it helps only on selected failure classes, adopt targeted deterministic instrumentation or narrow audits for those classes before adding a general agent judge.

---

Relevant Notes:

- [Reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) — rationale: a plausible reconstructed route cannot validate the route that actually produced the result
- [An outcome check licenses replay; a rule needs the process verified](../../notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md) — rationale: outcome and process checks inspect different evidence and license different conclusions
- [Agent Harness for Large Language Model Agents ingest](../../sources/agent-harness-large-language-model-agents-survey.ingest.md) — evidence: locates trajectory and intermediate-state evaluation in the harness evaluation interface
- [Harness-orchestrated review sweeps](./harness-orchestrated-review-sweeps.md) — see-also: adjacent proposal separating harness-owned orchestration from deterministic review endpoints
