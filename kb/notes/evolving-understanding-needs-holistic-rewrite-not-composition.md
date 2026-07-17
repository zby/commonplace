---
description: Holistic rewrite shifts reconciliation from each consumer to the author, but only when the whole-picture narrative can fit within effective context and be refreshed before the narrative goes stale
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, context-engineering, distillation]
---

# A compact, refreshable whole-picture narrative can replace infeasible fragment reconciliation

A note graph distributes knowledge across composable fragments: each note makes one claim, and links provide traversal. This works when a consumer can select a relevant slice or reconcile the needed fragments within the context available for its task. A different delivery form becomes useful when the consumer needs a coherent whole and fragment reconciliation would consume more effective context than the task can spare.

Rapid change can produce this case because revisions add currency decisions (decisions about which fragments or claims remain current), but evolution is not necessary. A stable, highly interdependent set can impose similar loading and coherence work. The claim here is qualitative: more relevant material, unresolved currency, or interdependence can make consumer-side reconciliation infeasible within a bounded [context budget](./context-efficiency-is-the-central-design-concern-in-agent-systems.md).

If the current picture can be faithfully compressed into one document and refreshed at the required cadence, a pre-reconciled narrative moves that work to its author. The author rewrites the narrative as a coherent whole when understanding changes instead of letting fragments diverge. The narrative is a dependent artifact of the understanding it summarizes. When that understanding changes, the narrative becomes stale and remains so until it is reworked; [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) describes this maintenance regime.

If neither fragment reconciliation nor a faithful, timely rewrite is feasible, the whole-picture task falls outside this pattern. It must be narrowed, decomposed, or served by another representation.

## Why fragment reconciliation can become infeasible

Three proposed pressures explain why a whole-picture task may exceed effective context:

1. **Material competes with task context** — before addressing the task, a consumer must bring enough of the relevant set into context, infer currency, and reconstruct connections. Loading that material leaves less context for the task itself.

2. **Change adds currency decisions** — new evidence may supersede only part of an earlier note. Frequent change can leave more local corrections for a consumer to find and apply across the relevant set.

3. **Interdependence adds coordination work** — each note can be internally coherent while the set is collectively inconsistent. Closely coupled claims may need to be compared together before the consumer can resolve their tensions.

## The general pattern

The pattern applies when:

- A consumer needs a coherent whole to act, not just a slice
- Reconciling the relevant fragments within the available context is not feasible
- A faithful narrative can fit effective context and be refreshed before it becomes misleading

Examples: onboarding documents tracking a changing system, investigation summaries during incident response, evolving design rationales during architecture exploration, theory documents during engineering campaigns.

Rapidly evolving working knowledge is an important case, not a requirement. In that case, the narrative's lifecycle is [workshop](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) rather than library: it serves current action and lives only for the period of active evolution. When understanding stabilizes, insights should be extracted into durable notes, a second reshaping into a different form for a different consumer.

## Illustration: theorist

The [theorist](https://github.com/blader/theorist) repository contains a skill authored under the repository owner's GitHub username, `blader`. Version 1.3.0 of its `SKILL.md` is dated 2026-02-28, and the repository uses the MIT License.

The skill prescribes one repo-root `THEORY.MD`, holistic rewrites rather than appended logs, and updates triggered by changes in understanding rather than code churn. It caps the document at roughly 200 lines and tells the agent to record superseded views briefly as pivots.

The repository verifies these implementation mechanics, not their effects. It supplies no controlled comparison with composition, so it does not establish better onboarding or agent performance.

## Open questions

- Can agents perform holistic rewrite reliably, or does it require human judgment about what's still true?
- What's the right extraction bridge when the evolution period ends? The narrative's insights need to become durable notes, but extraction is itself a reshaping step that could lose context.
- How does a size constraint interact with scope? Forced concision is the use-shaping doing its work — but complex situations may resist compression into a single document.
- In which situations is consumer-side reconciliation still cheaper than maintaining a narrative? A few mostly stable fragments are an obvious candidate, but the tradeoffs have not been measured.
- What representation serves a whole-picture task when neither fragment reconciliation nor holistic rewrite is feasible?

---

Relevant Notes:

- [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: reconciliation work reduces effective context, so feasibility depends on the whole task rather than fragment count alone
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — contrasts: composition aids discovery, while a pre-reconciled narrative aids whole-picture consumption
- [Storing LLM outputs is constraining](./storing-llm-outputs-is-constraining.md) — contrasts: storing freezes an output, while holistic rewriting maintains a current view
- [What spec-driven development gets wrong](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.md) — evidence: Augment Code, an AI coding-tool company, describes human-reviewed agent updates to a living specification
