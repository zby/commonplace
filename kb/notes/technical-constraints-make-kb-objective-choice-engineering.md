---
description: "Four technical constraints make KB objective-function choice testable engineering, not philosophy; goals set the loss, contracts and profiles specialize it, and oracle strength differs per profile"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, document-system]
---

# Technical constraints turn KB objective-function choice from philosophy into engineering

A knowledge base optimizes something. Call it the KB's **objective function**: the loss its writing, connecting, and review are trying to minimize. Asked in the open — *what knowledge is worth keeping? what does a good note maximize?* — this is a rerun of epistemology, and it terminates in taste, not a decision. The claim here is that in an agent-operated KB the question does not stay open, because four concrete technical constraints set hard rules that delete most candidate objectives before any value judgment is made. What survives is a small, testable space, and choosing within it is engineering.

The constraints do not tell you what to value. They tell you what you *cannot* make the system optimize, which is most of what philosophy would otherwise argue about.

## Why it would otherwise be philosophy

Absent constraints, "what should a KB keep" has the shape of every unbounded normative question: any answer is defensible in isolation, none is falsifiable, and the debate never closes because there is no cost to a bad answer. A KB with unlimited context, no code, an infinitely malleable reader, and free verification could optimize anything you could name — coherence-of-the-whole, aesthetic economy, comprehensiveness — and you would have no engineering reason to prefer one. The objective would be pure stipulation.

The constraints below remove exactly that freedom.

## The four constraints that prune the space

**1. Bounded context.** The consumer attends to one finite window where everything competes, since [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). An objective that can only be evaluated by loading the whole corpus — global coherence, non-redundancy across all artifacts — is not optimizable by the consumer that runs the KB. This forces objectives that are *locally* checkable: what one artifact does when co-present with a handful of others, not what the graph does as a whole.

**2. The codification option.** Any part of an objective whose inputs are already known can be moved out of prose and into a symbolic artifact with formal semantics — [codification](./definitions/codification.md). What the move buys depends on the consumer, because codification changes an artifact's [representational form](./definitions/representational-form.md), never its authority family — a methodology theory is a [system-definition artifact](./definitions/system-definition-artifact.md) already as prose, consumed with instruction force. For that reflective content — the KB's own conventions, gates, and routing rules — codification hardens the *enforcement channel* of authority the artifact already holds: the argument "is this the right rule?" becomes "does the validator pass?", and compliance stops costing context and varying by session. For object-level knowledge artifacts — claims about the KB's domain rather than about its operation — codification hardens only the *oracle*: the claim becomes a runnable test of itself, gaining checkability without gaining force over the system. Whether to discharge a sub-objective in code or leave it to the LLM remains a tradeoff with a decision procedure (see [codify-versus-LLM heuristics](./codify-versus-llm-decision-heuristics.md)). The scope limit matters when generalizing: only content that is a self-representation of the KB's own operation has an enforcement channel to harden, so "settled by construction rather than by debate" covers a KB's methodology, not its domain content. Commonplace's object and reflective layers coincide — the methodology is the content — which makes this lever look more general here than it is in a domain KB.

**3. The model's fixed lexicon and priors.** You write the objective against a consumer that already assigns meanings to words and carries priors over what text means. You cannot redefine that substrate. A convention that fights the model's lexicon is expensive to enforce and degrades silently — the model reverts to its prior under load. So the objective has to be *expressible in terms the model already discriminates reliably*, which prunes exotic value schemes and private vocabularies the model cannot apply consistently. This is the consumer-inherited half of the constraint packet: pick an LLM reader and its lexicon comes along whole.

**4. The verification boundary.** [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). Whatever objective you set, you can automate its optimization only as far as you can build an [oracle](./oracle-strength-spectrum.md) for it; objectives you cannot verify stay manual or advisory. So the *verifiability* of a candidate objective is a first-class selection criterion, not an afterthought — an objective you can score cheaply beats an objective you merely believe is deeper.

None of the four says what to value. Together they turn "what should a KB keep?" into "which locally-checkable, model-expressible, verifiable objective best serves the stated goal within one window?" — a question with testable answers and a cost for wrong ones.

## The objective hierarchy: goals set the loss, contracts specialize it, profiles bundle it

The surviving objective is not monolithic. It is specialized down a three-level hierarchy, each level a narrower loss than the one above.

- **Global KB goals set the loss.** The always-loaded control-plane goals — purpose, scope, quality bar — are the top-level objective every session optimizes against, and they decide inclusion before anything else does, since [KB goals in always-loaded context guide inclusion decisions](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md). This is the domain filter: it deletes off-scope material however well-written.

- **COLLECTION.md text contracts specialize the loss per collection.** Each writable collection declares a quality goal in its [text contract](./definitions/text-contract.md) — the local objective its writers and reviewers treat as decisive. `kb/notes/` optimizes reach; `kb/reference/` optimizes fidelity and economy; `kb/instructions/` optimizes executability and precision. Same global goal, different residual loss per subtree.

- **Profiles are named, proven objective-function bundles.** A [profile](./definitions/text-contract.md) is a pre-packaged objective a collection adopts, extends, or replaces wholesale — theoretical, descriptive, prescriptive are the shipped defaults, and the set is open and worked-case-gated. A profile is exactly what an optimization framework calls a loss template: a bundle of orientation, quality goal, and link grammar that has been shown to travel together (see [a knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md)).

The hierarchy is why objective choice is cheap in practice: a new collection rarely designs a loss from scratch, it adopts a proven bundle in one line and only writes a contract when no bundle fits.

## Judge strength differs per profile

The payoff of specializing through profiles is that the same global goal lands on very different **verification regimes**. Oracle strength — how cheaply and reliably you can check correctness — is not uniform across the KB; it is a property of the profile.

- **Descriptive has the strongest oracle.** The described system exists, so fidelity is checkable against ground truth: read the code, run it, compare the account to the referent. This is the closest a KB profile gets to a hard oracle, and it is why descriptive review can lean on mechanical checks.

- **Prescriptive has a behavioral oracle.** An instruction's correctness is whether executing it produces the intended behavior. That is checkable by running the instruction against a controlled boundary and asserting on what it does, as in [unit testing LLM instructions by mocking the tool boundary](./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md). The ground truth is the produced behavior rather than a fixed external referent — a medium-strength oracle, verifiable but only by execution.

- **Theoretical has the weakest oracle and must compensate with the widest judges.** Reach — a claim's generality across contexts — has no ground truth to check against; no single test decides whether a claim is as general as it says. So the theoretical profile cannot harden the oracle and instead widens the judge: multiple decorrelated critics, falsifier attempts, cross-domain probing. This is why [error correction needs above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) is load-bearing here — width of independent checking substitutes for the missing hard oracle. It is also why theoretical review is the most expensive and the least automatable.

That the profile with the weakest oracle (theoretical) carries the KB's most valued content (transferable claims) is the structural tension the whole review system is built around: the objective you most want to optimize is the one you can least cheaply verify.

## Scope

- **The constraints are inherited, not universal.** They arrive in the constraint packet of this framework's boundary commitments — an LLM consumer, a file substrate, a knowledge domain, the built machinery — so "engineering, not philosophy" is relative to those commitments, since [first principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md). A framework built on a different consumer inherits a different packet and a different pruned space. The value question is dissolved *for this framework*, not in general.
- **Pruning is not determination.** The four constraints delete most candidate objectives; they do not select a unique survivor. Choosing among what remains — which quality goal, how much to codify, how wide a judge to fund — still takes judgment. The claim is that the residual is small and testable, not that it is a single point.
- **Per-profile oracle strength is a characteristic default, not a law.** A theoretical note resting on one described system can borrow that system's oracle; a descriptive account of a system not yet built has no referent to check against. The dependency edge overrides the profile default.

## Open Questions

- Is the model's fixed lexicon a genuinely independent constraint, or a facet of the bounded-context/consumer commitment already covered by inheritance?
- Can the theoretical profile's "widest judges" ever be hardened into a real oracle, or is reach permanently a no-oracle objective — in which case the KB's central objective is structurally the one it can never fully automate?

---

Relevant Notes:

- [KB goals in always-loaded context guide inclusion decisions](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — grounds: the global goals are the always-loaded top-level loss the hierarchy specializes
- [text contract](./definitions/text-contract.md) — defined-in: the contract and profile vocabulary the objective hierarchy is built from
- [a knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — grounds: the three profiles and their quality goals this note treats as proven objective bundles
- [first principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md) — grounds: the constraints prune because they are inherited from boundary commitments, so the dissolution is framework-relative
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: bounded context, the first pruning constraint
- [codification](./definitions/codification.md) — defined-in: the move-logic-into-code option whose payoff splits by the consuming path's authority family
- [system-definition artifact](./definitions/system-definition-artifact.md) — grounds: authority is set by the consumption path, so codification hardens a channel rather than conferring a role
- [representational form](./definitions/representational-form.md) — grounds: codification is a form change; form sets how well authority is exercised, not whether it is held
- [codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) — mechanism: the codify-or-leave-to-LLM tradeoff is a concrete lever inside the pruned space
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: the verification boundary that makes an objective's verifiability a selection criterion
- [oracle-strength spectrum](./oracle-strength-spectrum.md) — mechanism: the hard/soft/no-oracle gradient that differentiates the per-profile judges
- [error correction works above-chance oracles with decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: decorrelated critics are how the theoretical profile substitutes judge width for a missing oracle
- [unit testing LLM instructions requires mocking the tool boundary](./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) — exemplifies: the prescriptive profile's behavioral oracle in concrete form
