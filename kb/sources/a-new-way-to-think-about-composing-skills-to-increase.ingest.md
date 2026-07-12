---
description: "Sakhuja's practitioner reframe of skill graphs into a three-tier compositional hierarchy (atoms/molecules/compounds) driven by the reliability ceiling of deep skill chains and the 'brain RAM' bottleneck in parallel-agent supervision"
source_snapshot: a-new-way-to-think-about-composing-skills-to-increase-leverage-skill.md
ingested: "2026-04-23"
type: kb/sources/types/ingest-report.md
domains: [skill-composition, agent-orchestration, reliability, capability-placement]
---

# Ingest: A new way to think about composing skills to increase leverage — Skill Graphs 2.0

Source: a-new-way-to-think-about-composing-skills-to-increase-leverage-skill.md
Captured: 2026-04-23
From: https://x.com/shivsakhuja/status/2047124337191444844

## Classification

Type: **practitioner-report** — Sakhuja reports on a specific skill-library organisation his team built ("capabilities / composites / playbooks") and the empirical failure mode (deep skill graphs degrade in practice) that motivated abandoning the flat dependency-graph model. The argument carries some conceptual-essay character (it proposes a taxonomy) but the load-bearing claims are framed as "what we tried, what broke, what we now do."

Domains: skill-composition, agent-orchestration, reliability, capability-placement

Author: @shivsakhuja — practitioner building skill-driven agent workflows, active in the X skills discourse. Unknown depth of track record, but the reported observations (non-deterministic deep-graph traversal, ~8–10 fan-out ceiling) match what multiple voices on Reddit/X have reported. Take as one data point among several, not an authoritative source.

## Summary

The tweet argues that the naive "skill graph" model (skills linking to dependent skills via Obsidian-style markdown links) breaks once the dependency depth grows: agents stop reliably traversing deep chains, circular dependencies cause trouble, and the human operator loses intent-level control. Sakhuja proposes replacing the flat graph with a three-tier compositional hierarchy — **atoms** (narrow, near-deterministic primitives that don't call other skills), **molecules** (small structured workflows or few-atom orchestrators, 2–10 atoms, explicit instructions on when to call what), and **compounds** (higher-level orchestrators over molecules, human-driven, deliberately less deterministic). The leverage argument: each tier is an order of magnitude more output per "brain RAM" slot, so operators should spend their parallel-supervision budget on compounds, not atoms. Reliability ceiling conjecture: compounds past ~8–10 molecules start breaking. Open problem: per-tier testing is expensive; Sakhuja hopes autoresearch can eventually automate it.

## Connections Found

The connect report mapped this tweet to a dense ring of already-present theoretical notes — the KB has strong coverage of the underlying ideas. Key edges:

- **see-also** [capability-placement-should-follow-autonomy-readiness](../notes/capability-placement-should-follow-autonomy-readiness.md) — convergent independent arrival at a three-tier capability hierarchy. The commonplace note's axis is *autonomy readiness* (skill / instruction / methodology note); Sakhuja's axis is *determinism × composition depth*. Near-parallel hierarchies, different framing.
- **see-also** [topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling](../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — the tweet is the practitioner version of the note's formal topology → isolation → verification argument, with the isolation and verification primitives under-developed.
- **see-also** [bounded-context-orchestration-model](../notes/bounded-context-orchestration-model.md) and [decomposition-heuristics-for-bounded-context-scheduling](../notes/decomposition-heuristics-for-bounded-context-scheduling.md) — atoms/molecules is the select/call loop pattern; Sakhuja's ~8–10 molecules-per-compound ceiling is evidence about `select` fan-out difficulty.
- **see-also** [agent-orchestration-occupies-a-multi-dimensional-design-space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — the tweet's one-axis taxonomy collapses several orthogonal dimensions (coordination guarantee, return artifact, scheduler placement) and is interesting precisely because it shows how a single-axis framing still has explanatory reach despite the lossiness.
- **see-also** [skills-derive-from-methodology-through-distillation](../notes/skills-derive-from-methodology-through-distillation.md) and [methodology-enforcement-is-constraining](../notes/methodology-enforcement-is-constraining.md) — the tweet rediscovers the distillation/constraining gradient at the composition level (atoms near codification, compounds deliberately prose-shaped to preserve human judgement).
- **see-also** [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — "compounds need human drivers" is a clean practitioner statement of the augmentation side of the discrimination-boundary.
- **see-also** [context-efficiency-is-the-central-design-concern-in-agent-systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — the depth-degradation observation is a context-efficiency failure on the complexity dimension (deep skill chains = high compositional load even at low token count), and the "brain RAM" argument extends the scarcity framing from agent context to operator context, making the operator's working memory a second finite-attention resource that constrains architecture.
- **compares-with** [skill-synthesis-materializing-knowledge-as-skills (Cramer)](./skill-synthesis-materializing-knowledge-as-skills-2032179291031.ingest.md), [improving-ai-skills-with-autoresearch-evals (Nurijanian)](./improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md), [xinmingtu-structured-test-time-scaling-hierarchical-mas-theory](./xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md) — Cramer gives the atom-tier production pipeline; Nurijanian addresses the tweet's "testing is expensive" open problem; Tu gives the formal theoretical counterpart to the informal hierarchy argument.

Novelty relative to the existing cluster: the tweet's vocabulary (atoms/molecules/compounds; capabilities/composites/playbooks) and its *brain-RAM leverage argument* — explicitly tying tier choice to the operator's parallel-supervision budget — is not currently articulated in the library.

## Extractable Value

1. **"Brain RAM" as the binding constraint on human-in-the-loop leverage.** [quick-win] — The claim that the operator's context-switching capacity (not agent capability) caps throughput is a high-reach framing: it explains *why* pushing work up a tier multiplies output even when each tier is less reliable, and it shapes the design question for compounds ("how few compounds can I drive in parallel?" rather than "how many atoms can one agent call?"). Worth a short note or a section inside `the-augmentation-automation-boundary-is-discrimination-not-accuracy` — the augmentation boundary is the *quality* condition; brain-RAM is the *quantity* condition.

2. **Empirical fan-out ceiling at ~8–10 molecules per compound.** [just-a-reference] — Practitioner-reported ceiling that matches the qualitative predictions of `topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling` and `bounded-context-orchestration-model`. Weak as evidence (n=1, no measurement method), but the specific number is quotable as a planning heuristic and as a data point that the topology step without explicit isolation hits a low ceiling.

3. **Convergent independent three-tier hierarchy.** [quick-win] — Two independently derived three-tier taxonomies (Sakhuja's determinism axis vs. commonplace's autonomy-readiness axis) arriving at structurally similar capability-tier counts is meaningful evidence that *three tiers* is a real regularity rather than a commonplace-local convention. Worth an `evidence` edge from `capability-placement-should-follow-autonomy-readiness` to this snapshot, with a context phrase naming the convergence.

4. **"Compounds carry deliberate indeterminism because human judgement is kept in the loop."** [quick-win] — Inverts the usual reliability framing: at the top tier, more determinism is a *bug*, not a feature, because it removes the surface on which the human discriminates. Useful reframe for the constraining gradient in `methodology-enforcement-is-constraining` — the gradient has a cutoff above which further constraining is harmful.

5. **Molecules as the externalisation boundary.** [deep-dive] — Sakhuja says molecules push composition into the skill file ("minimise the agent's runtime decision-making") while compounds accept LLM-mediated orchestration. This is the same pattern as `llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model`: molecules are the clean scheduler, compounds are the degraded-but-necessary one. Worth a note or a section: "externalisation ends at the tier where human judgement enters — and that is a feature."

6. **Testing cost is verification cost, and it stratifies by tier.** [experiment] — Cross-referencing with Nurijanian's autoresearch-evals report: atom verification is hard-oracle (cheap to automate), molecule verification is interaction-profile (harder), compound verification is goal-specification (hardest, phase-gated by comprehension). A synthesis note here would turn the tweet's hand-wave ("autoresearch will solve testing someday") into a structured claim about where verification cost concentrates in the tiered hierarchy.

7. **The vocabulary question.** [just-a-reference] — Sakhuja offers two naming systems in one tweet (atoms/molecules/compounds; capabilities/composites/playbooks) which hints he's not fully confident in either. The chemical-metaphor names collide with commonplace's existing distillation vocabulary (already uses "distillate"/"residue"); the capability-names collide with our "capability-placement" framing. If any synthesis adopts tier language, `tier-1 / tier-2 / tier-3` or `primitive / composite / orchestrator` avoid both collisions.

**Reach assessment.** The brain-RAM leverage argument (item 1) and the "deliberate indeterminism at the top tier" frame (item 4) are the highest-reach — they explain *why* tier choice matters in terms that hold beyond skill-library design. The fan-out ceiling (item 2) is context-bound practitioner data. The convergent-hierarchy observation (item 3) is reach-positive only once paired with a third independent arrival; with n=2 it is suggestive, not structural.

## Curiosity Gate

- **Most surprising.** The admission that compounds *should* be less deterministic — most practitioner writing on skills sells determinism as the prize. Sakhuja argues determinism at the top tier removes the human's discrimination surface. This flips the constraining gradient and is the piece most worth following.
- **Simpler account.** A simpler explanation for the depth-degradation observation is that flat-context agents accumulate contamination across skill boundaries (per `llm-context-is-composed-without-scoping`) — so the depth ceiling is a scoping problem, not a graph-shape problem. Sakhuja's hierarchical remedy works not because "tiers" are structurally special but because materialising a named molecule/compound creates a clean execution frame. If that's right, his observation is real but his mechanism is wrong. The connect report already flags this synthesis opportunity.
- **Hard to vary.** The leverage argument is *not* hard to vary — it survives swapping "compound" for any durable orchestrator abstraction and "brain RAM" for any finite human-attention resource. The tier names are arbitrary; only "composition depth times parallel-agent count saturates operator attention" survives the swap. The depth-degradation observation *is* hard to vary in the sense that many practitioners report it independently, but Sakhuja does not offer a mechanism hard to vary — any account that gets fragile deep traversal on flat-context agents reproduces his conclusion.

## Limitations (our opinion)

**What is not visible.**

- **Sample size of one team's skill library.** Sakhuja reports what his team built works "pretty well" without describing the workloads, how many operators use it, or what the failure rate at each tier actually is. The ~8–10 molecules-per-compound ceiling is a guess ("My guess: compounds that span more than 8–10 molecules start hitting their own reliability ceiling") — he has not hit it yet. This is practitioner intuition presented as if it were a measurement.
- **No comparison to a non-tiered baseline.** The tweet contrasts naive skill graphs (which broke) with tiered hierarchies (which work) but does not describe a controlled comparison — different team, different prompts, different model may have mattered more than the tier structure. Per `the-augmentation-automation-boundary-is-discrimination-not-accuracy`, the relevant counterfactual ("same team, no tiers, equivalent investment in atom quality") is absent.
- **Survivorship bias on the reliability claim.** "Atoms should be almost deterministic" presumes the team successfully constructed reliable atoms. The cost of getting atoms to that point is invisible — which is exactly the cost Nurijanian's autoresearch report makes legible, and which Sakhuja waves at as "non-trivial."
- **Mechanism under-developed.** The tweet diagnoses the failure (depth-induced unreliability) but not the cause. No discussion of scoping, isolation, or context contamination (see `llm-context-is-composed-without-scoping`, `subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks`). Without a mechanism, the remedy is offered on authority rather than argument — which matters because alternative remedies (better scoping, sub-agent frames, typed-callable boundaries) are invisible within the tier frame.
- **One-axis taxonomy.** The tier model collapses multiple orthogonal design dimensions (coordination form, scheduler placement, return-artifact shape, coordination guarantee) onto a single "composition depth" axis, per `agent-orchestration-occupies-a-multi-dimensional-design-space`. Two "molecules" at the same depth can have very different reliability profiles — the tier language hides this.
- **Unfalsifiable edges.** "Compounds need human drivers *at least today*" — the "at least today" clause turns a structural claim into a temporary one, making the compound-tier boundary unfalsifiable in practice (any autonomous compound can be redefined as "not yet a compound" or "a playbook that crossed into molecule territory"). Sakhuja is aware of the softness ("still figuring out where this breaks") but the frame does not carry its own test.

## Recommended Next Action

**Write a short note titled "tiered skill composition trades determinism for human discrimination surface"** — connecting to `the-augmentation-automation-boundary-is-discrimination-not-accuracy`, `methodology-enforcement-is-constraining`, and `capability-placement-should-follow-autonomy-readiness`. The thesis: the constraining gradient has a cutoff above which further constraining is harmful because it removes the surface on which the operator discriminates. Sakhuja's tier model is one instance of this; commonplace's autonomy-readiness tiers are another. The note would generalise the observation beyond Sakhuja's specific taxonomy and anchor it in the augmentation-boundary argument.

Lower-lift alternative if deferring the note: **add a single `evidence` link from `capability-placement-should-follow-autonomy-readiness` to this snapshot** with the context phrase "independent practitioner arrival at a parallel three-tier capability hierarchy, driven by reliability rather than autonomy readiness." This is the connect report's highest-confidence reverse-edge candidate and the most visible quick-win.
