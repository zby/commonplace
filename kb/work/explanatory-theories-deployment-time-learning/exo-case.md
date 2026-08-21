# Why Exo can test retained theory-mediated self-improvement

> **Status:** Workshop case. This note explains why Exo is a suitable experimental substrate and what result would support the retained-theory hypothesis. The [evidence ledger](./exo-evidence.md) owns pinned implementation facts, counterevidence, gaps, and falsifiers.

## Exo supplies the substrate, not the result

Canonical Exo exposes an unusually direct reflective path. Its agent can inspect a source tree and self map that describe parts of its own behavior-determining organization, edit symbolic artifacts, run mechanical checks, and rebuild and restart the executor. Event history survives sandbox rewind. Memory, skills, prompts, update reasons, and managed tools provide additional retained forms and routes into later operation. The pinned basis for these claims is recorded in [Exo evidence](./exo-evidence.md#pinned-exo-and-exoworker-facts).

These mechanisms make Exo a promising substrate for three reasons. A theory about Exo can participate in the self-representation through which Exo changes itself. A capable model can interpret the theory and derive consequences from it. The theory can persist as a separately addressable artifact whose premises and scope remain open to criticism and revision. Together, those properties satisfy the architectural conditions for [theory-mediated self-improvement](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

They do not establish that Exo already implements that mechanism. Existing memory facts, skills, self-update reasons, environment history, and source code are not automatically system theories. The inspected system does not require an explicit theory to mediate a self-change, govern a theory lifecycle, demonstrate that a retained change was beneficial, or trace one improvement's benefit into a later improvement episode.

The distinctions matter. **Deployment-time learning** names the setting in which operational evidence drives retained change. **Theory-mediated learning** names an update mechanism in which a scoped, criticizable theory guides a decision. **Reflective self-improvement** names the architecture in which the system changes itself through a causally connected self-representation. Their intersection is **theory-mediated self-improvement**; when its evidence comes from operation, deployment time is the setting.

## The retained-theory treatment

An episode-local theory `tau_n` could explain a current failure or opportunity, identify an intervention point, direct candidate search or choice, and derive consequences to evaluate. Constructing `tau_n` from current evidence and discarding it after the episode tests theory mediation, but not cumulative theory retention.

The stronger Exo treatment maintains an addressable and revisable `T_n`. A later episode retrieves an applicable part of `T_n` and uses it to form `tau_n`. Evidence from the episode can then support a proposed `T_{n+1}`. The experiment must record retrieval and use; storage alone cannot explain an effect.

Candidate acceptance and theory acceptance are separate decisions. A code change can work for a reason the theory gets wrong. A failed candidate can expose a valid counterexample and improve the theory. Exo's build, test, restart, and installation checks can reject mechanical failures, but they do not establish semantic improvement or theory warrant. The objective and comparison rule must therefore be fixed independently of the active candidate, and a theory revision needs its own evidence and gate.

The retained theory may describe an object-level mechanism in Exo, such as how a routing or memory change affects behavior. It may instead describe the improvement process: how failures should be diagnosed, which artifact should change, or which evaluator is adequate. Causal theories are one possible class, not the umbrella. Dependency structure, invariants, program semantics, and other explanatory relations may also constrain a decision.

Exo's value here is addressability. A retained premise, scope condition, evaluator assumption, or promotion rule can be named and selectively revised. Addressability creates a controllable revision surface; it does not guarantee correct interpretation, discovery, retrieval, or improvement.

## The result must appear in a later improvement episode

An accepted Exo change can improve later task behavior without improving the process that produces subsequent changes. That is accumulation, not compounding. Compounding requires an earlier retained benefit to make a later improvement episode counterfactually more productive: cheaper, broader, more reliable, or less dependent on human judgment. [Improvements can accumulate without compounding](../../notes/improvements-can-accumulate-without-compounding.md) develops the distinction.

The metric that accepts the earlier change cannot establish this later link. A tool's tests can show that it installs and meets its immediate target. They cannot show that the next diagnosis or revision became easier. Evidence must come from the later episode and trace either direct use of the earlier benefit or actual reinvestment of saved time, compute, or judgment.

An Exo canary gives the claim a concrete shape. Suppose an earlier episode produces a better behavioral evaluator from a retained theory about what Exo's mechanical checks miss. If that evaluator later rejects a judgment-degrading rewrite that the old checks would have admitted, the earlier benefit has improved a later selection. A matched replay without the evaluator can test the dependence. Merely installing the canary or passing its construction test would establish neither compounding nor even later use.

## An Exo-specific test

Keep Exo's existing memory, skills, tools, prompts, symbolic edit paths, and raw episode history in every arm. Compare:

1. direct reasoning over the available history with no required explicit theory;
2. a fresh `tau_n` reconstructed from the same history in each episode; and
3. a retained, revisable `T_n` that is retrieved and applied to form `tau_n`.

Hold the base model, source observations, edit surface, available actions, evaluator, and total resource budget fixed where possible. The task stream should include later episodes that preserve a theory's stated mechanism, violate one premise, and invalidate it more broadly. Record whether `T_n` was retrieved, which decision it changed, and how outcomes affected any proposed theory revision.

Use later improvement quality at a fixed total cost, or total cost at a fixed quality and harm bound, as the primary endpoint. Charge theory construction, storage, retrieval, applicability checking, review, maintenance, stale-theory failures, and correction. A frozen retained-theory arm can later separate reuse from revision, but it is not needed to establish the first marginal comparison.

Where possible, replay the later episode with the theory artifact frozen or absent. Some benefits, especially better noticing, may change whether an episode begins and resist paired replay; those need an initiation-rate measure plus a trace to what surfaced the opportunity. The general [experiment design](./experiment-design.md) owns the full protocol.

## Claim boundary

Exo demonstrates a mutable reflective substrate. It does not demonstrate an explicit theory lifecycle, beneficial self-improvement, or compounding. The proposed layer should preserve raw episodes and symbolic artifacts rather than replace them with summaries. Natural language is a practical form for currently unformalized theories, not a permanent or exclusive target; stable consequences should move into symbolic forms with mechanical semantics when warranted.

The proposal fails if Exo's existing surfaces plus just-in-time reconstruction match or beat retained theory on later improvement productivity after full costs and harmful transfer are counted. A positive result in one episode would support one local compounding link, not an exponential or indefinitely sustained pathway.
