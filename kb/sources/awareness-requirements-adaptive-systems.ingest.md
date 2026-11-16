---
description: "Awareness Requirements make requirement-state monitoring explicit, but leave goal authority, proxy validity and knowledge revision outside the demonstrated loop."
source: https://nemo.inf.ufes.br/wp-content/papercite-data/pdf/souza-et-al-seams11.pdf
captured: "2026-11-16"
capture: pdftotext
capture_scope: full-source
doi: "10.1145/1988008.1988018"
genre: scientific-paper
snapshot_sha256: c21c3462537ab42498d65008dc43aa729199076a203e10929629ea2b26c6c349
ingested: "2026-11-16"
occasion: "What can requirements engineering contribute, and what are its limits, for understanding operationalization, goal authority, and revisable knowledge in agent-operated knowledge work?"
type: types/ingest-report.md
domains: [awareness-requirements, requirements-monitoring, goal-oriented-requirements-engineering, self-adaptive-systems]
learning_claims: true
---

# Ingest: Awareness Requirements for Adaptive Systems

## Classification

A SEAMS 2011 research paper proposing a requirements category, formalization patterns and a prototype monitoring implementation, evaluated through constructed scenarios and a small performance experiment. Authors Vítor E. Silva Souza, Alexei Lapouchnian, William N. Robinson and John Mylopoulos were affiliated with Trento, Toronto and Georgia State; Robinson's EEAT requirements-monitoring framework supplies the implementation baseline.

## Summary

Awareness Requirements (AwReqs) specify constraints on the runtime states of other requirements or domain assumptions: never fail, succeed at a specified rate over a time window, avoid declining success rates, or complete within a time bound. They can also refer to other AwReqs in successive strata. The paper connects stakeholder goals and qualitative softgoals to measurable quality constraints, then to requirements about their observed satisfaction. Requirements become monitor-side UML classes and runtime instances, with temporal constraints expressed in OCL with Temporal Message logic and compiled by EEAT into event-processing rules. Constructed scenarios reportedly yield the expected satisfaction verdicts within this instrumented class-and-event representation; they do not compare alternative goal decompositions or demonstrate successful end-to-end adaptation. Compensation, diagnosis and systematic construction of a complete monitor-analyze-plan-execute loop remain future work.

## Contribution assessment (our opinion)

The important contribution appears to be making the requirements problem behind feedback infrastructure explicit: critical requirements may fail, so their acceptable runtime behavior itself needs specification. Named patterns and executable monitoring make that proposal inspectable and testable rather than merely redescribing adaptivity. The scenario tests establish limited feasibility, not improved resilience, and the comparisons with RELAX, FLAGS and probabilistic goal satisfaction are conceptual rather than controlled evaluations. The paper plausibly contributes a useful modeling interface, but its stronger practical significance depends on whether the missing diagnosis and compensation stages improve outcomes without merely weakening targets. The available comparisons do not establish broad originality or superiority.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the occasion, this source is a technical comparison for [Exact implementation does not validate a requirement against its objective](../theory/exact-implementation-does-not-validate-a-requirement.md). Its separation of softgoals, measurable quality constraints and satisfaction-rate requirements exposes several distinct commitments that can be checked locally. Correct monitoring of an adopted threshold does not validate the mapping from that threshold to the stakeholder's purpose. The scenario results hold the selected requirements and instrumentation fixed, leaving those upstream choices untested.

It is also a boundary case for [Diagnostic richness constrains outer-loop learning quality](../theory/diagnostic-richness-constrains-outer-loop-learning-quality.md). AwReqs identify violated constraints and aggregate their histories; they do not by themselves explain a violation or choose a repair. The paper thus supplies a concrete monitoring mechanism to compare with diagnostic evidence, not evidence that satisfaction signals alone support reliable knowledge revision.

## Learning Claims (our opinion)

The proposed adaptation mechanism is a feedback loop driven by violations of explicit requirements about other requirements. Only its monitoring stage is implemented here. Meta-AwReq examples suggest escalation, changing success-rate targets, or temporarily disabling a requirement to avoid repeated notifications. These are illustrations of possible reconciliation policies, not evaluated learning algorithms. The paper's “awareness” means reference to requirement states, not consciousness; its goal decomposition is not itself Commonplace's technical concept of program refinement.

Against the [theory builder](../theory/definitions/theory-builder.md) conditions, the implemented monitor has **localized content**: named requirements, domain assumptions and temporal predicates. These provide [addressability](../theory/definitions/addressable-theory.md) for reporting a violated constraint, though locating that constraint does not uniquely locate the faulty commitment. **Consumption** is demonstrated for monitoring: predicate content determines event evaluation. The mapping from these predicates to corrective system behavior remains proposed. **Content-directed criticism** is partial: observations can contradict a domain assumption or a claim that a performance constraint held, but a failed normative requirement does not refute the desirability of that requirement. No working process is shown for criticizing the softgoal-to-metric mapping, instrumentation or compensation policy. **Iteration** in the theory-builder sense is not demonstrated: accumulating events for successive monitoring windows is not evidence that retained criticism changes a subsequent conjecture or its use.

The implementation retains runtime evaluation objects and temporal event histories for monitoring. The paper does not establish reuse of revisions or critical records across runs or problems. Nor does it report improved capacity for future action. Relative to [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the tests hold requirement classes, event mappings and satisfaction semantics fixed. Proposed target relaxation changes a parameter within that representation; it does not establish that the system can revise the representation or its governing purpose. The source supports separating observable violation from diagnosis and revision, rather than treating monitoring as sufficient for learning.

## Extractable Value

1. **Make operationalization links separately inspectable.** Distinguish the stakeholder purpose, its measurable quality constraint, the required satisfaction rate and window, and the instrumentation that supplies the verdict. The paper gives concrete modeling machinery for these distinctions; the existing exact-implementation note supplies the warning that correctness at one link does not warrant the others. [quick-win]
2. **Separate authority to change a target from detection of failure.** The meta-AwReq example reduces response-time success targets to suppress repeated notifications. For agent-operated knowledge work, this illustrates why an alert-control policy must not silently become authority to redefine substantive success. The paper illustrates the change but does not establish its legitimacy or benefit. [quick-win]
3. **Use temporal requirement patterns as candidate monitoring specifications.** Never-fail, windowed success-rate, trend and bounded-delay predicates could make selected KB maintenance commitments observable. Their reuse would require testing event coverage and verdict semantics in the KB setting; the paper's scenario tests only support monitoring within its instrumented requirement representation. [experiment]
4. **Treat domain assumptions as monitorable commitments where observations permit.** Requirements about assumption failures distinguish environmental breakdown from task nonconformance. This offers a useful diagnostic partition, not a guarantee that the instrumentation can determine why an assumption failed or which theory to revise. [just-a-reference]

## Limitations (our opinion)

The central empirical support is correct evaluation of authored scenarios, including true, false and indeterminate cases for selected patterns. This tests implementation against expected monitor verdicts, not improved ambulance-dispatch outcomes, usability of elicitation, or superiority to competing formalisms. The claims that AwReqs are simpler or more accessible than fuzzy alternatives lack a comparative stakeholder study here.

Monitoring depends on developers or validators supplying meaningful requirement-instance boundaries, identities and state events. An emitted success event is not independent evidence that the underlying task met its purpose. Goal decomposition, quality metrics and threshold selection remain external design choices. Gradual elicitation through qualitative labels makes mappings easier to maintain but does not justify a particular mapping. Consequently, the framework cannot settle who has authority to choose or revise goals merely by formalizing them.

The performance evidence is narrow: a two-event sequence repeated 10,000 times across temporal-pattern configurations yielded about 137 event-pairs per second in the reported EEAT setup. It does not establish scalability for rich, long-lived knowledge-work traces. The paper's low target-system overhead discussion also relies partly on separating monitor and target machines.

Several textual details need checking before implementation: section 5.1's prose for AR8 reverses the temporal ordering stated in Table 1 and section 4, and Table 2 uses strict inequalities where some pattern descriptions suggest inclusive bounds. The plain-text capture does not preserve full graphical notation, so these are reasons to consult the published figures and specifications rather than copy extracted idioms as authoritative code. Full adaptation and compensation remain future work; threshold relaxation is not evidence that the revised target better serves the original purpose.

## Recommended Next Action

Review `kb/theory/exact-implementation-does-not-validate-a-requirement.md` against the paper's softgoal → quality constraint → satisfaction-rate requirement → instrumented verdict chain, focusing on which links require separate evidence and which target changes require explicit authority.
