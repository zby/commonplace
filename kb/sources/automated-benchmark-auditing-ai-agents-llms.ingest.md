---
description: "ABA audits benchmark prompts, environments, and graders; sampled confirmation supports defect discovery, while hidden acceptance conditions and score sensitivity inform KB evaluation design."
type: types/ingest-report.md
source: https://arxiv.org/abs/2605.26079
captured: "2026-09-19"
ingested: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: bdfd01c6656429405c9f70c6701be42ea8cc9f557f5c3b9cbafc8653ceea1d08
domains: [evaluation, benchmark-auditing, agentic-systems]
---

# Ingest: Automated Benchmark Auditing for AI Agents and Large Language Models

## Classification

Scientific paper by Junlin Wang and colleagues, affiliated with Duke University, Together AI, and Stanford University; the captured text identifies itself as arXiv v2, dated 26 May 2026. It presents an implemented auditing method, a cross-benchmark empirical study, external issue-set comparisons, and sampled human confirmation. These are the authors' reported experiments, not an independently reproduced evaluation. The paper includes prompts, schemas, and case studies; no implementation repository was inspected or executed for this ingest.

## Summary

Auto Benchmark Audit (ABA) uses an evidence-collection agent to map heterogeneous benchmark materials into task manifests, then a tool-using auditor to inspect instructions, environments, and grading logic under a shared severity rubric. Its static audit flags at least one Major issue in 8,819 of 34,285 tasks across 168 benchmarks (25.7%); this is an auditor-assigned rate, not a verified defect prevalence. Maintainer fixes and sampled human review support the usefulness of some findings. With the collector–manifest–auditor design and rubric retained, adding recorded execution evidence surfaces more Major findings across eight paired benchmarks, but does not test alternative architectures or demonstrate better downstream repairs. Removing flagged tasks changes scores and rankings for unchanged model submissions. For Commonplace, the clearest contribution is concrete evidence that acceptance tests can reject valid work when authors omit requirements that execution cannot recover.

## Quotes

- **Source extract (verbatim):** “Configure QEMU to accept keyboard input programmatically . . . Set up QEMU with appropriate interfaces to allow external keyboard control.” (instruction.md:10–12). The prompt specifies neither the monitor protocol (HMP vs. QMP), the transport (TCP, telnet, stdio, UNIX socket), nor any path.
  - **Source location:** Appendix F.1, install-windows-3.11 (Terminal-Bench 2), Prompt, p. 36.

- **Source extract (verbatim):** The visual-feedback keyboard test requires a QEMU HMP monitor exposed as a UNIX socket at /tmp/qemu-monitor.sock, but the prompt never discloses the path, transport, or protocol. QEMU satisfies the stated requirement with many valid configurations – HMP over TCP, telnet, stdio, a UNIX socket at a different path, or QMP over UNIX/TCP. The reference solution uses -monitor unix:/tmp/qemu-monitor.sock,server,nowait (solution/solve.sh:118), the exact path/protocol required by the test, but nothing in the prompt points an agent to this specific choice.
  - **Source location:** Appendix F.1, install-windows-3.11 (Terminal-Bench 2), Finding, p. 36.

## Connections Found

ABA supplies bounded evidence for [Exact implementation does not validate a requirement against its objective](../notes/exact-implementation-does-not-validate-a-requirement.md). Its grader cases distinguish executable acceptance from the task objective: narrow tests can reject valid alternatives, while broad tests can accept outputs that do not satisfy the request. These cases support auditing the requirement–objective link separately from checking that the grader runs correctly; they do not establish the correctness of every ABA finding.

The human-aligned QEMU case in Appendix F.1 is particularly direct evidence for [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md). The prompt asks for programmatic keyboard control, but the test accepts only an HMP monitor at a specific UNIX socket path. Several other interfaces satisfy the visible request. Domain expertise cannot select an arbitrary hidden path: either the author must disclose that acceptance condition or the grader must accept the alternatives. This is a concrete instance of omitted acceptance information, not evidence for every aspect of the note's delegation account.

## Extractable Value

- **A precise hidden-acceptance-condition example [quick-win].** Appendix F.1 turns an abstract author–executor boundary into a checkable case: the required QEMU path, protocol, and transport appear in the grader and reference solution but not the prompt. The paper reports human agreement with the finding. This can strengthen the existing determinability note without introducing a new general theory.
- **Audit the evaluator through explicit evidence [experiment].** ABA separates instruction, environment, and evaluation findings, with a claim, consequence, severity, evidence pointers, and proposed fix. Its collector inlines lightweight task information and provides file references for larger artifacts; the auditor must inspect them. A bounded Commonplace evaluation trial could borrow this evidence discipline. The paper does not compare this representation or the collector–auditor split with alternatives, so it supplies a working method rather than proof that these boundaries are optimal.
- **Keep discovery, confirmation, and scoring sensitivity separate [quick-win].** The Terminal-Bench maintainer comparison recovers 14 of 21 selected issues strictly and 17 with partial matches. Table 3 reports 73% strict and 91% partial confirmation for sampled static Major findings. These checks answer different questions from the corpus flag rate or leaderboard changes. Reusing the paper as evaluation evidence requires preserving those denominators and match criteria.
- **Execution evidence can change the defect set [just-a-reference].** The paired static-versus-trajectory comparison changes available evidence within ABA's existing manifest, rubric, and auditor design. It supports inspecting traces when static artifacts may conceal runtime conflicts. More findings alone do not establish higher accuracy, an optimal context policy, or improved revisions after diagnosis.

## Limitations (our opinion)

The population is selected from frontier-model release reports and NeurIPS 2025 benchmark papers, then filtered for scope and feasible auditing. It excludes modalities and tasks outside the chosen portfolio, including inherently subjective evaluation. Task sampling and unequal benchmark sizes also limit generalization. The 25.7% Major share must remain an estimate produced by this auditor on these versions, not a general rate of invalid AI benchmarks.

Validation is partial. Known maintainer fixes are useful external checks but not an exhaustive gold set; unmatched findings can be either new defects or false positives. Reviewing flagged findings cannot estimate how many defects remain among unflagged tasks. Strict and partial matches must remain distinct. The paper also has a sample-count inconsistency: section 4.3 and Table 3 say 56 static Major findings, while Appendix D.3 says 54. The confirmation percentages above are attributed to Table 3 rather than silently resolving the discrepancy.

The strongest matched-baseline evidence is narrow. With Opus 4.6 and BenchGuard's issue sets and alignment procedure, ABA improves strict recall on BixBench from 54.2% to 62.5% at matched partial recall, while matching recall on ScienceAgentBench. It does not uniformly improve every metric: ScienceAgentBench partial precision is lower. This comparison evaluates method packages on two scientific benchmarks; it does not isolate the value of the standardized manifest, agent separation, or each prompt rule. Most corpus audits use Opus 4.7. Appendix C.4's statement that every audit used that model conflicts with the explicit Opus 4.6 comparisons in section 4.2 and Table 2.

The collector's standard schema and ordered output do not make evidence acquisition deterministic. Appendix C.2 directs an agent to discover data, interpret task boundaries, and write and execute a collector script, after which the runtime validates its outputs. Mapping errors could affect what the auditor sees. No ablation establishes that this representation preserves every consequential feature of each benchmark.

Trajectory audits see agent outcomes as well as execution traces. Appendix E.2's passed-and-flagged cases show that flags do not simply duplicate failures, but the outcome cross-tabs cannot rule out subtler outcome bias. Filtering flagged tasks also changes the task distribution while leaving model submissions fixed. Higher scores and changed rankings are therefore sensitivity results, not evidence that capability improved or that the filtered leaderboard is uniquely correct. As the [requirement–objective distinction](../notes/exact-implementation-does-not-validate-a-requirement.md) implies, an audit's own severity rubric remains a judgment whose suitability needs separate assessment.

## Recommended Next Action

Update [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) with the human-aligned QEMU case from Appendix F.1 as a bounded example of an undisclosed acceptance condition, retaining the necessary source support when making that update.

---

- [Original paper](https://arxiv.org/abs/2605.26079) — derived-from: source of the reported method, experiments, and case evidence
