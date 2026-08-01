# Case packet

Neutral case identifier: case-1b6d3c4df444c1

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Technical constraints turn KB objective-function choice from philosophy into engineering

A knowledge base optimizes something. Call it the KB's **objective function**: the loss its writing, connecting, and review are trying to minimize. Asked in the open — *what knowledge is worth keeping? what does a good note maximize?* — this is a rerun of epistemology, and it terminates in taste, not a decision. The claim here is that in an agent-operated KB the question does not stay open, because four concrete technical constraints set hard rules that delete most candidate objectives before any value judgment is made. What survives is a small, testable space, and choosing within it is engineering.

The constraints do not tell you what to value. They tell you what you *cannot* make the system optimize, which is most of what philosophy would otherwise argue about.

## Why it would otherwise be philosophy

Absent constraints, "what should a KB keep" has the shape of every unbounded normative question: any answer is defensible in isolation, none is falsifiable, and the debate never closes because there is no cost to a bad answer. A KB with unlimited context, no code, an infinitely malleable reader, and free verification could optimize anything you could name — coherence-of-the-whole, aesthetic economy, comprehensiveness — and you would have no engineering reason to prefer one. The objective would be pure stipulation.

The constraints below remove exactly that freedom.

## The four constraints that prune the space

**1. Bounded context.** The consumer attends to one finite window where everything competes, since [context efficiency is the central design concern in agent systems]. An objective that can only be evaluated by loading the whole corpus — global coherence, non-redundancy across all artifacts — is not optimizable by the consumer that runs the KB. This forces objectives that are *locally* checkable: what one artifact does when co-present with a handful of others, not what the graph does as a whole.

**2. The codification option.** Any part of an objective whose inputs are already known can be moved out of natural-language content and into a symbolic artifact with formal semantics — [codification]. What the move buys depends on the consumer, because codification changes an artifact's [representational form], never its authority family — a methodology theory is already a natural-language [system-definition artifact], consumed with instruction force. For that reflective content — the KB's own conventions, gates, and routing rules — codification hardens the *enforcement channel* of authority the artifact already holds: the argument "is this the right rule?" becomes "does the validator pass?", and compliance stops costing context and varying by session. For object-level knowledge artifacts — claims about the KB's domain rather than about its operation — codification hardens only the *oracle*: the claim becomes a runnable test of itself, gaining checkability without gaining force over the system. Whether to discharge a sub-objective in code or leave it to the LLM remains a tradeoff with a decision procedure (see [codify-versus-LLM heuristics]). The scope limit matters when generalizing: only content that is a self-representation of the KB's own operation has an enforcement channel to harden, so "settled by construction rather than by debate" covers a KB's methodology, not its domain content. Commonplace's object and reflective layers coincide — the methodology is the content — which makes this lever look more general here than it is in a domain KB.

**3. The model's fixed lexicon and priors.** You write the objective against a consumer that already assigns meanings to words and carries priors over what text means. You cannot redefine that substrate. A convention that fights the model's lexicon is expensive to enforce and degrades silently — the model reverts to its prior under load. So the objective has to be *expressible in terms the model already discriminates reliably*, which prunes exotic value schemes and private vocabularies the model cannot apply consistently. This is the consumer-inherited half of the constraint packet: pick an LLM reader and its lexicon comes along whole.

**4. The verification boundary.** [The boundary of automation is the boundary of verification]. Whatever objective you set, you can automate its optimization only as far as you can build an [oracle] for it; objectives you cannot verify stay manual or advisory. Verifiability is therefore a first-class *engineering* fact about a candidate objective, not an afterthought — it decides how much of the pursuit can run without a person, and what the remainder costs.

What it does not do is settle which objective to hold. Reading it that way — the cheaply scored option beats the one you merely believe is deeper — is how a proxy displaces the thing it stands in for, [since a property adopted as a goal is checked for achievement rather than for warrant], and a cheap score supplies the full signature of a verified objective while establishing nothing about whether it was worth adopting. This KB is the demonstration: the profile carrying its most valued content has the weakest oracle, as below, and that objective was kept anyway. The constraint prunes the space of objectives you can *automate against*; the choice within it stays a choice.

None of the four says what to value. Together they turn "what should a KB keep?" into "which locally-checkable, model-expressible, verifiable objective best serves the stated goal within one window?" — a question with testable answers and a cost for wrong ones.

## The objective hierarchy: goals set the loss, contracts specialize it, profiles bundle it

The surviving objective is not monolithic. It is specialized down a three-level hierarchy, each level a narrower loss than the one above.

- **Global KB goals set the loss.** The always-loaded control-plane goals — purpose, scope, quality bar — are the top-level objective every session optimizes against, and they decide inclusion before anything else does, since [KB goals in always-loaded context guide inclusion decisions]. This is the domain filter: it deletes off-scope material however well-written.

- **COLLECTION.md text contracts specialize the loss per collection.** Each writable collection declares a quality goal in its [text contract] — the local objective its writers and reviewers treat as decisive. `kb/notes/` optimizes explanatory-reach; `kb/reference/` optimizes fidelity and economy; `kb/instructions/` optimizes executability and precision. Same global goal, different residual loss per subtree.

- **Profiles are named, proven objective-function bundles.** A [profile] is a pre-packaged objective a collection adopts, extends, or replaces wholesale — theoretical, descriptive, prescriptive are the shipped defaults, and the set is open and worked-case-gated. A profile is exactly what an optimization framework calls a loss template: a bundle of orientation, quality goal, and link grammar that has been shown to travel together (see [a knowledge base holds theories, descriptions, and prescriptions with asymmetric linking]).

The hierarchy is why objective choice is cheap in practice: a new collection rarely designs a loss from scratch, it adopts a proven bundle in one line and only writes a contract when no bundle fits.

## Judge strength differs per profile

The payoff of specializing through profiles is that the same global goal lands on very different **verification regimes**. Oracle strength — how cheaply and reliably you can check correctness — is not uniform across the KB; it is a property of the profile.

- **Descriptive has the strongest oracle.** The described system exists, so fidelity is checkable against ground truth: read the code, run it, compare the account to the referent. This is the closest a KB profile gets to a hard oracle, and it is why descriptive review can lean on mechanical checks.

- **Prescriptive has a behavioral oracle.** An instruction's correctness is whether executing it produces the intended behavior. That is checkable by running the instruction against a controlled boundary and asserting on what it does, as in [unit testing LLM instructions by mocking the tool boundary]. The ground truth is the produced behavior rather than a fixed external referent — a medium-strength oracle, verifiable but only by execution.

- **Theoretical has the weakest oracle and must compensate with the widest judges.** Reach — a claim's generality across contexts — has no ground truth to check against; no single test decides whether a claim is as general as it says. So the theoretical profile cannot harden the oracle and instead widens the judge: multiple decorrelated critics, falsifier attempts, cross-domain probing. This is why [error correction needs above-chance oracles and decorrelated checks] is load-bearing here — width of independent checking substitutes for the missing hard oracle. It is also why theoretical review is the most expensive and the least automatable.

That the profile with the weakest oracle (theoretical) carries the KB's most valued content (transferable claims) is the structural tension the whole review system is built around: the objective you most want to optimize is the one you can least cheaply verify.

## Scope

- **The constraints are inherited, not universal.** They arrive in the constraint packet of this framework's boundary commitments — an LLM consumer, a file substrate, a knowledge domain, the built machinery — so "engineering, not philosophy" is relative to those commitments, since [first principles are inherited constraints, not design choices]. A framework built on a different consumer inherits a different packet and a different pruned space. The value question is dissolved *for this framework*, not in general.
- **Pruning is not determination.** The four constraints delete most candidate objectives; they do not select a unique survivor. Choosing among what remains — which quality goal, how much to codify, how wide a judge to fund — still takes judgment. The claim is that the residual is small and testable, not that it is a single point.
- **Per-profile oracle strength is a characteristic default, not a law.** A theoretical note resting on one described system can borrow that system's oracle; a descriptive account of a system not yet built has no referent to check against. The dependency edge overrides the profile default.

## Open Questions

- Is the model's fixed lexicon a genuinely independent constraint, or a facet of the bounded-context/consumer commitment already covered by inheritance?
- Can the theoretical profile's "widest judges" ever be hardened into a real oracle, or is explanatory-reach permanently a no-oracle objective — in which case the KB's central objective is structurally the one it can never fully automate?

---

Relevant Notes:

## Artifact B

# KB goals in always-loaded context guide inclusion decisions

Every time an agent creates a note, it makes an inclusion decision: does this knowledge belong in *this* KB? A writing guide can provide universal quality criteria (claim titles, retrieval-oriented descriptions, composability) but says nothing about domain scope. A [routing table] can say where artifacts go, but not whether they should exist.

This gap doesn't surface in a KB about its own domain — a methodology KB about methodology is self-defining. It surfaces the moment a KB is deployed for a specific domain (legal research, system architecture, API design), where the agent otherwise has no basis for:

- Rejecting knowledge that's well-written but out of scope
- Deciding whether a source is worth ingesting
- Choosing between a note and a log entry for marginal material
- Evaluating whether accumulated knowledge serves the KB's purpose

## Where goals belong

The [control-plane model] defines three layers: invariants, routing, escalation boundaries. KB goals are a new invariant in Layer 1 — "this KB is about X, not Y" is a rule that must hold in every session. They define the *domain scope* within which routing operates. They belong in the control-plane file (the always-loaded agent instructions) because:

1. **Every write is an inclusion decision.** The question "does this belong here?" is as frequent as "where does this go?" — both need zero-hop access.
2. **Loading frequency is high, failure cost is high.** An agent that ingests off-topic material wastes context and pollutes search results. Both placement criteria from the control-plane model point to always-loaded.
3. **No extra hop.** A separate `GOALS.md` would add one tool call to every write path. Since the control-plane file is already loaded, embedding goals there costs nothing.

## What varies per installation

| Concern | Per-installation or universal? |
|---|---|
| Purpose — what decisions/actions the KB supports | Per-installation |
| Scope — the domain boundary, with in-scope and out-of-scope lists | Per-installation |
| Quality bar — domain-specific "good enough" standards | Per-installation |
| Routing, type system, writing conventions, link semantics | Framework-shipped defaults |

Only the per-installation rows require human input. The default rows ship with the framework and can be updated mechanically on upgrade — but they are defaults, not universals: what is framework-fixed is the machinery (that collections declare contracts, that types and link labels exist), while the taxonomies themselves are collection-local and extendable, since [a universal knowledge framework demotes content taxonomies to defaults and keeps answerability] (shipped instances: ADR 018 made the type set open and collection-local, ADR 019 made link vocabulary collection-owned).

## What makes each subsection work

**Purpose** — Start from the users, not the domain. Who will use this KB? What are they trying to do better? A good purpose statement names the decisions or actions the KB supports: "supports the API team in making design decisions about the payment service" is actionable; "stores knowledge about payments" is not.

**Scope** — Draw a boundary an agent can apply without asking: a domain statement naming adjacent domains and whether they're in or out ("adjacent systems (auth, billing) are in scope only where they interact with payments"), made operational by an in-scope list and an out-of-scope list. The out-of-scope list is the most valuable part: scope creep is the default failure mode of a KB — every piece of knowledge looks relevant in isolation — so naming what seems relevant but doesn't belong ("business rules live in the product wiki, not here") is what makes the in-scope list meaningful. The in-scope list is less critical because the routing table already covers structural placement.

**Quality bar** — When is a piece of knowledge worth a note vs. a log entry vs. nothing? A writing guide says how to write well; this subsection says when to write at all. Domain-specific standards: "a design decision is worth a note when it affects more than one endpoint; single-endpoint details belong in code comments."

## Relation to explanatory-reach

The KB Goals section is not a replacement for the [explanatory-reach criterion]. Explanatory-reach is a quality criterion — knowledge with explanatory depth that transfers to new situations. Goals are the domain filter — *which* situations this KB cares about transferring to. A note can have high explanatory-reach but be out of scope (a brilliant insight about compiler optimization in a KB about payment architecture), or low explanatory-reach but in scope (a specific failure case that the team needs to remember).

Both filters apply. Goals first (is this in scope?), then explanatory-reach (is this worth the context it costs?).

## Goal revision

Goals are set at installation time but domains evolve. When a KB's scope shifts — new responsibilities, deprecated subsystems, changed team boundaries — the Goals section should be updated to match. Stale goals are worse than absent goals: they actively misdirect the agent into rejecting relevant material or accepting irrelevant material. Review goals when the KB's domain changes, not on a schedule.

---

Relevant Notes:

## Under-review context phrase

the global goals are the always-loaded top-level loss the hierarchy specializes
