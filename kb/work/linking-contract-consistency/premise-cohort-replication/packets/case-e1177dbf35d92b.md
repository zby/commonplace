# Case packet

Neutral case identifier: case-e1177dbf35d92b

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

# First principles are inherited constraints, not design choices

A companion note shows which rules a universal framework *cannot* keep as universals: first-order content taxonomies [demote to guarded defaults] because they are not universal — the next kind of KB breaks them. This note is the other half: the rules that genuinely constrain the design space and therefore cannot demote.

The membership test: **a rule is a first principle iff it arrives in the constraint packet of one of the framework's boundary commitments** — the *consumer* it serves, the *substrate* it is built on, the *domain* it commits to (knowledge), or the *machinery* it has built. The commitments themselves are chosen, sometimes for features unrelated to the constraints they bring — files picked for ubiquity and tooling, not for how placement behaves. But every such choice is a packet deal: whichever substrate is chosen, its limitations come along whole, and the framework cannot cherry-pick the features it likes out of the bundle. What is unchoosable is not the boundary but the unbundling — and that is the sense in which a first principle is *inherited*: it comes with a commitment, never on its own terms.

Nor does composition escape a packet: a framework can combine parts built on different substrates, but each part still answers to its own substrate's limitations — artifacts held in files obey the file packet even when acceptance state lives in a database next door. Machinery coherence fits the same shape, just later: building machinery of a given kind is the choice, and its coherence rules are the packet. These four are the boundary commitments currently visible; the list is open, like the list of principles itself.

The two halves are therefore not symmetric. Design choices are *positions within* the design space: a rival can be swapped in while every boundary commitment stays, so a framework aiming at universality can offer several and let a collection pick — they demote to guarded defaults. First principles are *boundaries of* the design space: there is no rival position to demote to, and dropping one means re-choosing a boundary commitment and taking a different packet whole — not reconfiguration but a different framework.

## The principles that currently pass the test

Each is named with the boundary it inherits from. The list is what passes today, not a closed set.

1. **Bounded context / context economy** — inherited from the *consumer's architecture*. The reader attends to one finite window in which everything competes (since [context efficiency is the central design concern in agent systems]), and the binding pressure is silent degradation before any hard limit (since [agent context is constrained by soft degradation, not hard token limits]). Specific length norms are *local strategies* serving this economy; the economy itself cannot be opted out of while the consumer is an LLM.

2. **Composability / co-loading** — inherited from *how the consumer ingests artifacts*: files load as whole units into one shared window, so an artifact's usefulness is decided by what it does when co-present with others (see [short composable notes maximize combinatorial discovery]). The inherited form is weak — every artifact must stay usable when loaded alone, without dragging in unrelated claims. The stronger "citable as a bare premise" rule is a theoretical-register design choice layered on top, not the principle.

3. **Substrate asymmetry** — inherited from the *file substrate*. Directory placement is total (every file has exactly one location, no opt-out) while frontmatter classification is partial and opt-in, so location contracts and type contracts encode different guarantees and cannot substitute for each other (because [directory placement is total, frontmatter classification is partial]). On files this asymmetry is not negotiable.

4. **Answerability** — inherited from the *domain commitment* to knowledge. Every artifact must answer to something outside itself and can therefore be wrong or stale; a collection that cannot state what its artifacts answer to and what makes one stale is not holding knowledge (see [the complement note's scope test], which states the answerability property; the [knowledge-artifact] definition supplies the artifact class this commitment quantifies over). Which relation an artifact bears — to the world, a system, an outcome, a source — is local; *having* one is not.

5. **Declaration obligation** — inherited from *machinery coherence*. Every writable collection must carry a loadable contract, because the machinery routes and validates by reading that contract; a collection without one is an operational defect regardless of content. The complement note treats this as the surviving second-order universal (its shipped instance is ADR 017's `COLLECTION.md`).

6. **Admission discipline** — inherited from *machinery coherence*. Once taxonomies are opened into extensible sets, some admission brake is required: without one, the open sets proliferate until no convention is shared — which is the other way to stop being a framework. As with composability, the inherited form is weak — *an* admission discipline must exist — while the specific worked-case guard (entries admitted only after surviving use in a real collection, never from anticipation) is the discipline this framework chose, layered on top. The complement note identifies that guard as the load-bearing piece that lets closed taxonomies safely open.

7. **Derived-copy rule** — inherited from *machinery coherence*. A copy of information recomputable from a ground-truth source must be machine-checked against that source or not exist; a hand-maintained-and-trusted copy is a trap (because [a derived copy of recomputable truth must be checked or absent]). Any framework that caches recomputable values inherits this, since a silently stale trusted cache corrupts the consumers that trust it.

## Contrast: rules that look like principles but demote

The membership test earns its keep by *excluding* rules that feel foundational but are positions the framework chose and could re-choose. Each of these demotes to a guarded default per the complement note:

- The **three [registers]** (theoretical / descriptive / prescriptive) — a proven bundle, but a new kind of KB can need a fourth; they demote to default text-contract profiles.
- **Link-label sets** — `extends`, `grounds`, `contradicts`, and the rest are a collection-owned selection from a shared catalogue, not a universal vocabulary.
- **Type sets** — open and collection-local; the framework fixes that types *exist* and are path-valued (machinery), not *which* types there are (choice).
- **Spending the directory tree on content-area** rather than on kind — a routing decision a given KB makes, reversible without touching the framework.
- **Status / lifecycle enums** — the existence of a lifecycle is machinery; the specific values, and whether status fuses structural state with first-person endorsement, are a choice sitting one level too high.

The tell in every case: you can name a rival that also works *under the same boundary commitments*. When no rival exists — because the only alternative is to change the consumer, substrate, or domain, or to break the machinery — the rule is inherited, and the list above collects the ones currently visible.

## Caveats

The durable content is the *test*, not the enumeration: a later principle may be recognized as inherited, or one of these may turn out to be a disguised choice with an unnoticed rival, and neither outcome would touch the test itself. The test defines first-principle status rather than deciding it — the rival-hunt is how the test is applied, and application is fallible in both directions. And "inherited" is always relative to a framework's own boundary commitments: a framework that changed consumer or substrate would inherit a different set. So these are first principles *of this framework*, not of knowledge bases in general.

---

Relevant Notes:

## Under-review context phrase

the constraints prune because they are inherited from boundary commitments, so the dissolution is framework-relative
