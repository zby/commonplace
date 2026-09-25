---
type: kb/types/note.md
description: "Enoch's persistent personal-agent core: task recovery, conditional memory read-back, rationale-bearing evolution, and bounded code-adoption gates"
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-enoch-01
source-identity: https://github.com/our-ark/enoch
reviewed-revision: 81000d502e776a7fd2ff39904f71f14084c9b4a8
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-enoch-01/result.md
analysis-result-sha256: cb18228f3e7c56951d7d401e3b96b12aa24f8aaf77ad4ae87b36eeffe57c5a20
---

# Enoch

**Evidence basis:** code-grounded inspection of `our-ark/enoch` at `81000d502e776a7fd2ff39904f71f14084c9b4a8`, frozen 2026-09-25; no target execution or causal experiment. The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-enoch-01/result.md) retains the source quotations, route records and memory comparison profile.

Enoch is a persistent personal-agent application around replaceable runtime, chat, repository and review providers. Conversation can invoke the same registered operations as commands; substantial work enters a durable task queue. Its governed-change path separates proposing code, checking it, publishing a review, landing it and updating the running body. The source supports these routes, but does not demonstrate improved capability at this revision. [Application workflow](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/app/task_workflow.py), [update path](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/operations/updater.py).

A conversation journal records planned, running and completed actions. It preserves actual receipts and stops automatic replay when an interrupted action may already have happened. The local queue records one running task, worker identity, attempts and publication state; recovery distinguishes a live worker, compatible terminal evidence, conflicting evidence and bounded retry. These are host protocols, with no claim of exactly-once arbitrary external effects. Exact records RTE-1 and RTE-6. [Conversation journal](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/app/conversation.py), [reconciliation](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/tasks/queue.py).

Ordinary coding work uses an isolated repository workspace, then doctor checks and bounded repair under the original deadline. Failed validation preserves the workspace and prevents host publication. A remote-required review must have a confirmed typed state and URL. Updating to the authoritative revision runs a fresh-source doctor and attempts rollback on failure before requesting restart. No-change tasks and specialized maintenance/publication paths do not all pass this same gate. Exact records RTE-2, RTE-3 and RTE-4. [Task validation](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/app/task_workflow.py), [review predicate](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/app/review_publication.py).

These controls have a specific enforcement boundary. Task execution requests `danger-full-access`; plugin factories run Python, and provider effects rely on external contracts. Structured conversation actions can reach the merge handler, which checks the locked conversation and forge capability. The inspected source does not prove a separate human confirmation for each merge. Scheduled evolution does stop after presenting a proposal pending approval. Exact records RTE-3, RTE-5, RTE-8 and RTE-11. [Sandbox constants](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/runtime.py), [application handlers](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/app/core.py), [extension loading](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/extensions/registry.py).

Enoch's memory is several mechanisms, not one store:

- Long-term JSON entries are descriptive context, explicitly subordinate to instructions and current requests. Startup selects by confidence, age and character budget. The ordinary model-extraction call uses defaults labelled explicit/high confidence without source references, weakening provenance.
- Private personal identity is separately rendered and schema-validatable. It is manually replaceable; the inspected path does not establish automatic experiential identity rewriting.
- Task, backlog and recurring-job briefs retain selected prior conversation decisions. Workers later receive those briefs; recurring jobs can reuse a captured brief across tasks. Failed-task diagnostics also reach later retries.
- Evidence scans and candidate synthesis retain observations, rationale, proposed benefit, risks and test plans. Curators and selected task workers read those reasons. Imported skill and parent-lineage assessments have their own provenance and admission routes.
- Provider session identifiers preserve access to opaque additional context. Explicit startup reconstruction and provider resume coexist; a fresh fallback cannot be assumed to recover all prior conversation state.

These findings are the fresh specialist's integrated records RTE-9, RTE-10, RTE-11, RTE-12, RTE-13, RTE-14 and RTE-15. [Memory store](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/memory/store.py), [evolution](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/evolution/core.py), [session adapter](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/brain.py).

Automatic trace-fed memory writes are wired, including conversation briefs and diagnostic continuation. Candidate rationale is both retained and delivered, making proposed repairs inspectable rather than merely logging an outcome. Tests can reject changed implementations. The evidence does not establish a specific formulated theory, criticism of its content, and an attributable improvement in later capacity as one observed chain. Exact result epistemic overlay separates those findings.

A limited reflective route is wired: representations of Enoch's own task activity can update evidence and proposals that guide changes to its body. That is separate from proving improved performance or revision of a self-theory about its theory-building organization. Migration also preserves selected private state, body identity and local continuation authority; it does not demonstrate behavioral equivalence across models or hosts. [Evidence extraction](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/evolution/evidence.py), [migration](https://github.com/our-ark/enoch/blob/81000d502e776a7fd2ff39904f71f14084c9b4a8/src/enoch/migration.py).

## Scope

This review covers the repository-owned core and its interfaces. External model/session contents, installed provider packages pinned at other revisions, live deployments, arbitrary extensions and descendant execution remain uninspected. The memory comparison therefore names its core-owned boundary and leaves complete behavioral authority and faithfulness undetermined. Current-pin executions linking evidence, criticism, adopted code and later capacity—or recall and cross-provider migration experiments—would materially strengthen the assessment.

---

- [Exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-enoch-01/result.md) — see-also: canonical evidence, limitations and normalized memory fields.
- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: the stronger learning claim distinguished from trace-fed memory writes.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: the limited representation/action route assessed here.
