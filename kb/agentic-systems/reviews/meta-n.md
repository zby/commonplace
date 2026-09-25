---
type: note
description: "Meta^n evolves executable solver layers from task traces, retaining code, rationale and task winners; source-level feedback wiring does not establish improved generalization."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-24-meta-n-01
source-identity: https://github.com/minnesotanlp/meta-n
reviewed-revision: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-24-meta-n-01/result.md
analysis-result-sha256: 24ecfb914dc10ae0571f613ffadb28477110a252bb0bcf6f1e35356dd29dca16
---

# Meta^n

Evidence basis: source code, tests and repository documentation at [revision b7081843](https://github.com/minnesotanlp/meta-n/tree/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8), frozen on 2026-09-24; no live improvement run or causal experiment was performed.

Meta^n is an experimental improvement plane around task solvers. Its Omega model receives earlier solver code, rationale and execution traces, then proposes preprocessing, helper libraries and guidance for a new solver layer. The orchestrator executes and evaluates the resulting candidate, stores it in an archive, and selects parents for subsequent proposals. Native single-shot, native agentic and external-agent execution have different consumption paths. Provider internals, external SDK memory and upstream benchmark validity remain outside this repository-owned boundary.

The connected improvement mechanism is substantial: prior solver organization and its outcomes can change later executable organization. An optional repair loop revises a failed proposal, while downward repair can replace an intermediate layer using full-chain feedback. The archive retains alternatives and supports restart. These mechanisms establish feedback-responsive revision wiring; their ability to improve future capacity was not observed in this pass.

The default benchmark configuration materially changes the interpretation of progress. Consolidation focuses a selected task while preserving other task winners and bypasses the ordinary sampled quality gate. Archive maxima and frozen per-task solutions can improve the retained portfolio through selection among more draws. A rising retained score therefore does not isolate a better proposal process or demonstrate unseen-task generalization. Frozen task-map dispatch is wired in the native MetaLayer path; the early agentic and external paths do not consume that map in the same way.

Memory includes task traces, generated code and rationale, archive indexes, frozen solutions, checkpoints, imported seed helpers and built-in conversation summaries. Later Omega calls receive selected failures, ancestry, task matches and rationale. Native solvers receive injected helpers and guidance; external agents receive guidance and files they can read or call. The built-in agentic solver can summarize older conversation turns and insert the summary into its next model call. This is a separate online, per-task trace-fed write. The analysis establishes these read-back routes, not their behavioral activation or faithful preservation of every relevant fact.

Admission controls have different scopes. Code validation, task scoring, optional sampled gates and optional helper checks are distinct decisions. A missing real helper verifier can return an explicit unverified keep decision. Dependency closure can retain a helper that failed its own check without granting verified status. Later helper-use attribution is syntactic, not a measured causal contribution. Retention, verification and effective use must therefore remain separate findings.

The execution boundary also matters. Preprocessing can execute on the host in a thread whose timeout does not kill the running callback; this is not a universal container boundary. External runs have lifecycle and timeout controls, but dollar limits operate through admission and recorded expenditure rather than an exact per-run stop. Concurrent work and incomplete cost reporting can weaken the spending bound.

Generated rationale and individually editable code expose possible explanations and rules to later revision. Actual formulated theories, criticism of what they say, and capacity improvement attributable to that criticism remain uninspected. The system does wire reflection: retained representations of its own prior layers and outcomes mediate changes to later solver behavior. Dispositional self-improvement is wired relative to configured benchmark feedback and the run/resume horizon; actual update-dependent operation and achieved favorable improvement are unobserved. These are separate findings, not a system-wide grade.

Candidate-linked code, rationale and criticism records, matched sampling budgets, and unseen-task outcomes would distinguish portfolio gains from improvement in solver generation. The exact result retains the route-specific evidence, exceptions and normalized memory findings.

---

- [Evolutionary orchestrator](https://github.com/minnesotanlp/meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/core/evolutionary_orchestrator.py) — evidenced-by: candidate generation, admission, archive selection and repair.
- [MetaLayer](https://github.com/minnesotanlp/meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/core/meta_layer.py) — evidenced-by: native injected execution and frozen task dispatch.
- [Agentic solver](https://github.com/minnesotanlp/meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/core/agentic_solver.py) — evidenced-by: execution feedback and continuation summaries.
- [Exact analysis result](../../reports/retained/agentic-system-analysis/AAS-2026-09-24-meta-n-01/result.md) — see-also: canonical records and evidence limitations.
- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: criticism and improved capacity are separate from retained output.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: self-representation must mediate later behavior.
- [Self-improving system](../../notes/definitions/self-improving-system.md) — defined-in: disposition, occurrence and favorable outcome have separate evidential requirements.
