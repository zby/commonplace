---
description: Runtime structure and runtime governance are separable, but the runtime's structure determines which inspection, validation, correction, and drift-control operations governance can actually perform
type: kb/types/note.md
traits: []
tags: [architecture, computational-model]
---

# Runtime structure determines the control surfaces available to governance

It is useful to separate runtime **structure** from runtime **governance**, but "separate axes" can be misleading if it implies independence. The structural decomposition answers what the runtime is made of: scheduler, context engine, execution substrate. Governance answers how the system is informed, validated, corrected, and kept from drifting over time. These are different questions, but governance is not free-floating: even when it works through channels the runtime's structure doesn't expose — a human reading logs, a norm enforced among maintainers, a wrapper-level guardrail — those channels can only react to what has already happened. Structure determines whether governance can also act earlier, on the decision itself, or is confined to reacting after the fact.

That is why governance should not be modeled as a fourth peer component beside scheduler, context engine, and substrate. Each component owns part of normal execution, but governance functions cut across components instead: review may inspect outputs from the context engine, compare artifacts in the substrate, and then trigger corrective edits that alter future scheduling decisions. The role is supervisory, not a separate execution slot in the runtime anatomy. Keeping structure and governance as separate questions also avoids a category error: files, tools, and routing artifacts are not themselves validation or correction.

## Structural affordances for governance

Each structural component affords particular governance operations.

**Scheduler.** When progression logic is explicit, governance can attach retry limits, decomposition rules, delegation boundaries, and recovery policies to it — including escalation to a different authority when automated handling is insufficient, a correction that reroutes the decision rather than editing it. When scheduling is instead hidden inside a framework-owned chat loop, governance is not absent — wrapper-level guardrails, output validators, and behavioral evals are the dominant real-world pattern for governing exactly these systems — but it is reactive rather than preventive: a wrapper can catch a bad output after the fact, but it has no handle on the decision that produced it, so it cannot inspect or retry the scheduling choice itself.

**Context engine.** When context selection is explicit, governance can audit routing rules, check what entered a bounded call, measure compaction quality, and review whether the right materials were loaded. When context is instead inherited as an undifferentiated transcript, the same asymmetry holds: governance can complain about prompt quality or re-prompt after a bad output, but it cannot inspect or retry the loading decision itself, because that decision was never externalized to act on.

**Execution substrate.** When state lives in inspectable external artifacts, governance can diff, test, review, revert, compare content hashes, and detect staleness. This is the strongest governance surface because exact external state is easier to validate than hidden internal state. Content-addressed comparison in particular is a stronger drift oracle than timestamps: a hash reflects exact current state, while a timestamp only reflects when something last touched — a file can be re-saved unchanged and still look "modified," or edited and still look untouched if the clock is wrong. The substrate is therefore not just where actions land; it is also what makes strong governance possible.

## The dependence is asymmetric

The relationship is not symmetrical.

- Structure **affords and constrains** governance. A runtime with no inspectable substrate cannot support repo-style review and rollback. A runtime with no explicit context engine cannot support precise loading audits.
- Governance **hardens and reshapes** structure over time. Repeated review findings can turn into scripts, checks, or policy boundaries, making previously soft guidance part of the runtime's effective structure.

So the right picture is neither "one unified taxonomy" nor "two fully independent axes." It is a layered relationship: structural choices determine the control surfaces available to governance; governance exploits those surfaces to keep the runtime reliable over time.

## Consequence for runtime comparison

This changes how runtimes should be compared. It is not enough to ask whether two systems both have scheduling, context loading, and tools. The next question is whether those parts are exposed in a way that governance can act on them. Two runtimes can have similar structure but very different governance capacity because one externalizes its state and decisions while the other leaves them implicit.

## Structure × governance matrix (commonplace)

Crossing the two axes for commonplace itself is one worked example of the general claim:

|  | Inform | Validate | Correct | Detect drift |
|---|---|---|---|---|
| **Scheduler** | skill/tool selection descriptions | — | — | — |
| **Context engine** | routing conventions, escalation boundaries | frontmatter/link/description checks | targeted rewrite instructions | content-hash comparison against accepted baselines |
| **Execution substrate** | discovery reports, index notes | link-health and uncommitted-state checks | direct file edits | git history and content-hash staleness sweeps |

The scheduler row is mostly empty because commonplace doesn't have a scheduler — it plugs into the harness's scheduler (Claude Code, Codex, or another) and authors the content and substrate artifacts that scheduler consumes, rather than implementing scheduling itself. That is a design boundary, not a gap: commonplace's governance can only act on the surfaces it actually owns.

---

Relevant Notes:

- [Agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — grounds: names the structural decomposition this note qualifies
- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: describes one governance gradient that operates across the runtime rather than inside a single structural component
- [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation.md) — exemplifies: review and validation are governance operations with different oracle and cost profiles
- [Inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — grounds: explains why externalized exact state gives governance unusually strong control surfaces
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — contrasts: sibling argument over the same scheduler/context-engine/substrate decomposition — both deny "fourth component" status, governance here, memory there
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — contrasts: this note rates content-hash a stronger drift oracle than the timestamp mechanism that note builds on
- [Review architecture](../reference/review-architecture.md) — evidence: the shipped review subsystem realizes the substrate/context-engine governance cells in this note's worked matrix
