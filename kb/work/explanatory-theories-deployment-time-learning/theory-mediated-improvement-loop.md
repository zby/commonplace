# How theory enters an improvement loop

> **Status:** Working model. This note defines the theory-mediated addition used throughout the workshop. Detailed comparisons and controls are in the [experiment design](./experiment-design.md).

A [proposal-selection improvement loop](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) normally moves from evidence to candidate changes, evaluates them, and either retains one or keeps the current system. **Theory-mediated learning** inserts a scoped, criticizable theory between the evidence and one or more stages of that loop. The theory can guide diagnosis, search, candidate choice, evidence acquisition, or outcome interpretation.

For this workshop, an artifact counts as a working theory only when it explains why the system behaves as it does by proposing a mechanism, invariant, or other explanatory relation. It must state its assumptions, scope, and testable consequences. It must also be recorded before the stage or decision it is meant to guide and before the relevant held-out outcomes are revealed. A recommendation or post-hoc rationale is not enough.

## The minimal loop

Let `tau_n` denote the working theory used in episode `n`. It may be constructed from the current evidence or formed by applying a retained theory `T_n` to the current episode.

```text
current system + objective + evidence
    → construct or retrieve working theory tau_n
    → diagnose and search
    → propose and prioritize candidate changes
    → choose evaluation evidence
    → accept a change or keep the current system

outcomes + audits + working theory tau_n + prior retained theory T_n
    → assess or revise the theory
    → retain T_{n+1} or keep T_n
```

The first path decides whether to change the system. When theory retention is in scope, the second decides whether to change the retained theory. The paths share evidence, but they end in separate decisions.

## Where theory can help

A working theory can affect four parts of an improvement episode:

1. **Diagnosis and search.** It can explain the observed failure or opportunity, identify a likely intervention point, and direct search away from irrelevant components.
2. **Candidate proposal and choice.** It can derive possible changes, state the premises on which they depend, prioritize them before evaluation, and help rank or reject them afterward.
3. **Evidence acquisition.** It can predict which functions a candidate may affect and which observations would distinguish intended benefits, regressions, and rival explanations. The [selective-evaluation model](./selective-evaluation-model.md) develops this role.
4. **Outcome interpretation and theory revision.** It can explain how a result bears on a premise or scope condition and propose a narrower theory, a broader one, or a replacement for later episodes.

These roles can succeed or fail independently. A theory may locate a useful intervention while missing its regressions, or identify a discriminating test while generating no useful candidate. The experiment should therefore test each role separately before testing them in combination. A theory-derived prediction remains a claim to test; it is not additional empirical evidence.

## Two decisions, not one

A candidate can work for a reason the theory gets wrong. Conversely, a failed candidate can expose a useful counterexample to the theory. Accepting a system change therefore does not also accept its explanation, and rejecting the change need not discard everything learned from the episode.

A reusable theory needs a separate assessment and retention decision. Evidence should warrant only the claims and scope it actually tests: a [checked outcome licenses the episode, not an abstracted explanation](../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md), and [theory warrant should remain as narrow as the evidence](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md).

## On-the-spot and retained theories

An **on-the-spot treatment** constructs `tau_n` for the current episode and discards it afterward. It tests whether theory mediation improves the present search or decision. If the theory guides a behavioral change that is accepted and later becomes operative, the episode can still count as theory-mediated learning even though the theory itself did not accumulate.

A **retained-theory treatment** starts from an addressable `T_n`, records whether the episode retrieves and uses it, and allows a revision to be retained separately as `T_{n+1}`. This tests the stronger claim that theory work in earlier episodes can improve later ones. Any benefit must outweigh the costs of retrieval, applicability checking, maintenance, and correction, as well as the risk that a false retained theory misdirects several episodes. The retained self-improvement case is developed in [theory-mediated self-improvement](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

## What the theory is about

Most of this workshop concerns an **object theory**: an account of how the system will behave under a proposed change. An **improvement-process theory** instead says how observations should become retained changes and how those changes should later be activated, revised, or retired. Both can shape behavior, but evidence for one is not evidence for the other. The [Exo case](./exo-case.md) develops this distinction.

The [experiment design](./experiment-design.md) specifies how to distinguish genuine mediation from extra deliberation or post-hoc explanation. The workshop README routes the HCL, SPADE, and Exo applications. Those systems supply settings in which to test this proposed addition; they are not evidence for the combined loop.
