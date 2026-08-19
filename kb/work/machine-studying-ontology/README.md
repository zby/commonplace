# Machine Studying ontology integration

## Goal

Determine which distinctions introduced by [Machine Studying](../../sources/machine-studying.md) materially improve Commonplace's account of how an agent learns from a corpus before it knows its downstream tasks. For each distinction, decide whether to adopt it, translate it into existing vocabulary, merge it with an existing concept, reject it, or defer it.

The workshop treats the source's ontology as the main contribution. It does not assume that the proposed expertise scalar, StudyBench implementation, or preliminary experimental results should become Commonplace theory.

## Source-defined working inventory

These are claims to examine, not yet Commonplace vocabulary:

- **Machine studying**: pre-task adaptation from a corpus alone, while the downstream task distribution and reward remain unknown.
- **Agent**: the mutable system `Sigma = (model, harness)`, so studying may change weights, prompts, tools, indexes, notes, or other harness state.
- **Studying algorithm**: a transformation from `(agent, corpus)` to a changed agent, with the corpus still available during later evaluation.
- **Expertise**: domain-relative performance across inference-compute budgets, rather than accuracy at one budget or possession of retrievable text.
- **Studying intelligence**: how effectively additional study compute converts into expertise.
- **Evidence-timing boundary**: corpus-only preparation is distinct from learning that already has downstream tasks, rewards, demonstrations, or execution traces.
- **Three intervention families**: self-supervised weight updates, self-synthesized training environments, and amortized context management.

## Existing anchors

The comparison should begin from the KB's existing claims that:

- [the deployed system, not the model, is the unit of learning](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md);
- [the deploy-time learning cluster](../../notes/deploy-time-learning-README.md);
- [learning must improve action capacity, not just retrieval](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md);
- [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md); and
- [learning inside a fixed decomposition inherits its mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

Nearby systems provide boundary cases. [Knowledge-Centric Self-Improvement](../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md), [Passive Skill Distillation](../../sources/reason-wide-not-deep-distilled-skills.ingest.md), and [Dynamic Cheatsheet](../../agent-memory-systems/reviews/dynamic-cheatsheet.md) can use task outcomes or trajectories. The comparison should determine whether excluding those signals identifies a useful regime or merely a special case of an existing adaptation category.

## Questions to resolve

1. Is machine studying a distinct kind of learning, a restriction on deploy-time adaptation, or a useful experimental protocol rather than an ontological category?
2. Does expertise name anything beyond domain-relative action capacity measured across inference budgets?
3. Does the studying-algorithm relation add a useful distinction between access to a corpus and a retained change in the agent's behavior-determining organization?
4. Is evidence timing the right boundary? Which task descriptions, synthetic questions, self-sampled traces, graders, and privileged models violate corpus-only preparation?
5. Do the three intervention families form a stable comparison frame, or do mixed systems and alternative representational forms cut across them?
6. Which distinctions change a KB design, routing, or evaluation decision? Which only rename existing ideas?
7. Where does Commonplace itself fall when ingesting a source, writing a note, changing an instruction, or leaving the source available for later retrieval?

## Evaluation boundary

A source term earns promotion only if it changes at least one classification, design choice, or evaluation. A clean paraphrase of an existing Commonplace claim is not enough. Any promoted term must have an explicit boundary against existing vocabulary and at least one case that the new distinction classifies more clearly.

Keep three layers separate:

- the source's definitions;
- what its reported experiments actually establish; and
- the broader interpretation Commonplace might adopt.

The workshop does not need to adopt StudyBench's scalar, prove that any studying intervention works, generalize from the reported treatments, or anticipate a later research article.

## Disposition ledger

| Candidate | Status | Disposition record |
|---|---|---|
| machine studying | translate | Corpus-only, pre-task preparation is deploy-time adaptation restricted by evidence timing — a regime and experimental protocol (StudyBench), not a new ontological category. Destination: the capture signal-timing sub-axis in [memory design adds operational axes](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md). |
| agent as model plus harness | merge | `Sigma = (model, harness)` adds nothing beyond the deployed-system unit of learning plus the definition/session relations. Destination: convergent evidenced-by on [the deployed system, not the model alone, is the unit of learning](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md); the update relation is owned by [instantiation alone cannot model agent learning across sessions](../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md). |
| studying algorithm | merge | The `(agent, corpus) -> changed agent` map is the definition-update relation of [instantiation alone cannot model agent learning across sessions](../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md), where it is cited; the corpus-remains-available clause translates to frontloading rather than internalization. |
| expertise | translate | Domain-relative action capacity under activation constraints, covered by [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md); the retrieval-controlled selection experiment is promoted as evidence there, and the across-budget measurement residue is recorded as an open question on the same note. |
| studying intelligence | defer | Second-order scalar over a measurement the KB did not adopt; no current consumer. Revisit if across-budget evaluation enters KB practice — the open question on the knowledge-storage note is the hook. |
| evidence-timing boundary | adopt | As the capture signal-timing sub-axis (corpus-only versus task-, reward-, demonstration-, or trace-conditioned) in [memory design adds operational axes](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md). Boundary cases survived: self-posed questions stay pre-task, self-mined execution traces do not; AWM, Voyager, and Dynamic Cheatsheet classify to the conditioned pole. |
| three intervention families | translate | The families are representational-form placements of the retained change — parametric via raw-corpus loss, parametric via synthesized signal, readable context artifacts — so mixed systems are points on the existing form-coevolution axis, not a taxonomy failure. Destination: the signal-timing paragraph plus the cheatsheet evidence edges on [retained artifacts](../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) and [frontloading](../../notes/frontloading-spares-execution-context.md). |

Allowed dispositions are `adopt`, `translate`, `merge`, `reject`, and `defer`. Record a reason and durable destination for every non-open disposition.

## Closure

This workshop closes when every candidate in the ledger has a disposition, each adopted distinction has survived at least one boundary-case comparison, and any durable conclusions have been promoted to the appropriate library artifact and validated. Then delete this directory and remove its entry from `kb/work/README.md`.
