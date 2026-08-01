# Case packet

Neutral case identifier: case-3f238a6bfb20f0

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# False-positive generation is filtered; false-positive acceptance becomes operative

In a [proposal-selection improvement loop], search and evaluation fail in ways that are not symmetric, and the asymmetry is structural rather than incidental.

Search sits *upstream of a filter*. A bad candidate — useless, harmful, off-target — reaches evaluation and is rejected. It cost effort and nothing else; it never became operative.

Evaluation *is* the filter. A bad acceptance is not caught by anything downstream, because retention is not a filter — retention is the machinery that makes the change stick. The accepted artifact acquires a consumer, a channel, and a force, and starts shaping behavior.

> Only the last filter's errors survive.

## What the claim covers, and what it does not

The asymmetry is between the two kinds of *false positive*. Search produces something that should not have been produced, and the filter catches it. Evaluation passes something that should not have passed, and nothing catches it.

Search's other failures are not filtered, because there is nothing to filter. Search also fails by **omission** — never generating the candidate worth having, choosing the wrong target, stopping too early — and those errors are invisible and permanent. No evaluator recovers them: [evaluation cannot select a candidate that search never reaches]. They are not *retained* either, since nothing enters the system; they are simply forgone, and the system cannot tell that they were.

The precise claim is:

> False-positive generation is filtered before retention; false-positive acceptance becomes operative.

That is what makes "make the evaluator stronger" no answer to a weak generator, and it is why the two functions cannot be traded against each other. It also means the consequence below ranks what to automate *among the errors the loop can see*. Omission errors are the reason automating search is not free either — a generator with narrow range costs improvements no one will ever miss.

## The consequence: automate search first

The costs of automating the two functions are paid in different currencies.

**Automating search costs evaluation throughput.** Machine-generated candidates are judged by the same evaluator that judged the human's. The failure mode is a queue: candidates arriving faster than anything can judge or prune them, which is exactly the pathology in [entropy management must scale with generation throughput]. That is a *capacity* problem, and capacity problems are tractable — batch, prioritize, sample, or strengthen the evaluator.

**Automating evaluation costs correctness.** A weak oracle accepts changes that do not help, they are retained, and they compound: a bad note gets linked, cited, and reshaped into a skill. That is not a capacity problem and no amount of throughput fixes it. It is bounded by [the boundary of automation is the boundary of verification].

And taking the autonomy anyway does not break anything visibly — which is what makes it dangerous. A fallible evaluator still rejects some candidates, so it is a real evaluator and [the loop still closes]. The system stays self-improving and looks healthy, running unattended, while its mistakes accumulate in the artifacts it keeps. Nothing announces the degradation, because the machinery that would have announced it is the machinery that was weakened.

So search is the function whose failures the loop already catches, and it is the one to automate first. Evaluation is the one that has to be *bought*, with an oracle.

This explains a common disappointment in agent-memory systems. Most of them automate search — mine the traces, extract the tips, write them down — and leave evaluation to a human or to nothing at all. The result is a growing pile of unjudged candidates that changes little. The [agent-memory-system-review] type already points at the same place from the other end when it says the distillation step's "trigger, oracle, and curation policy is often the most discriminating part." This claim says why: the oracle is the only part whose errors are both permanent *and* operative — an omitted candidate is lost, but an accepted bad one goes to work.

## The correction path does not escape the bound

The asymmetry is not absolute, and pretending otherwise would overstate it. A bad acceptance *can* be caught later — by a review sweep, a freshness pass, or a Popperian "do I still believe this?" reread. Retention is revocable.

But that correction path is itself evaluation, and it inherits the same bound. Three things follow:

- It spends evaluation capacity, which was the scarce resource to begin with.
- It runs against the same oracle that made the original mistake, so the blind spot that let the change in is the blind spot that lets it stay. A second pass with an unchanged oracle is not a second chance.
- Meanwhile the artifact has been operative, and may have acquired dependents — the cost of removing it is no longer the cost of never having accepted it.

False-positive generation is caught by machinery already running in the loop, at no extra cost. False-positive acceptance is caught only by spending more of the thing that was scarce, and only if the oracle has meanwhile improved.

## Scope

- The claim is scoped to the proposal-selection subtype of [self-improvement] — the architecture that has an acceptance step at all. A direct evidence-driven update pathway (gradient, reward, viability) adopts every update, so its failure surface is the adequacy of the objective and the update rule, not a gate's false positives.
- The claim assumes evaluation is the terminal filter. If a system adds monitoring or rollback downstream, that is not a counterexample — it is more evaluation, and it inherits the same bound.
- It holds whether evaluation runs before a candidate becomes operative or after. Post-hoc evaluation changes when the bad change is caught, not whether an unfiltered acceptance is retained.
- It ranks *what to automate first* under a fixed oracle. It does not say search is easy: [automating KB learning is an open problem], and the judgment-heavy parts of search remain hard for their own reasons.

---

Relevant Notes:

## Artifact B

# A proposal-selection improvement loop requires search, evaluation, and operative retention

A **proposal-selection improvement loop** is the architecture of improvement in which candidate changes are generated, evaluated with a possibility of non-adoption, and selectively made operative. It is a named subtype, not the whole of the phenomenon: a [self-improving system] needs its changes to be responsive to evidence bearing on an improvement objective, and evidence may instead determine an update directly — gradient-, reward-, error-, or viability-driven — with no candidate ever standing to be rejected. What follows is the anatomy of the subtype, and it applies with full force exactly there.

A proposal-selection loop requires three functions: **search** brings a candidate change into consideration, **evaluation** supplies grounds for accepting or rejecting it, and **operative retention** preserves an accepted change with behavioral authority. Remove any one and the loop does not close — a change nobody proposed, nobody could reject, or nobody will ever act on.

The loop is therefore narrower than self-modification. A blind, accidental, or unconditional rewrite may change later behavior without applying any criterion; a transient rewrite may fail to preserve the result. Both can count as self-modification, but neither closes a proposal-selection loop. Conversely, the three functions can close the loop in a system that is not reflective at all.

A terminology note: the concept descends from Ashby's **adaptation** — his ultrastable system, examined below, is the conceptual ancestor even though it classifies outside the subtype — but it is named for what the loop aims at rather than by his word for it. Everyday adaptation is transient compensation, an eye adjusting to the dark, and retains nothing; retention is one of the three requirements. Where this note says *adaptation* or *adaptive*, it means Ashby's phenomenon. The architecture described here is named **proposal-selection** throughout.

A [reflective system] supplies one possible causal path into this loop. Through **intercession** — an operation that changes the system through its causally connected self-representation — it can modify a represented aspect of itself. Making that path available does not itself provide search, evaluation, or retention.

The independence runs both ways. A directly determined update can land on a self-representation as readily as on an opaque substrate — evidence can revise an explicit policy or a recorded lesson with nothing rejectable anywhere in the path — so neither architecture is the general form of reflective improvement.

## Search determines what enters consideration

Search brings an unrealized change under consideration. It may include:

- detecting a problem, opportunity, or adaptation signal;
- selecting the aspect and operation to change;
- generating one or more candidates;
- allocating effort and deciding when to stop or escalate.

At minimum, search must produce a candidate from a space in which other possible changes remain unrealized. It need not compare several candidates at once or operate autonomously. A maintainer may choose the problem, a model may draft a candidate, and a script may enumerate alternatives within one declared socio-technical loop. Assigning those functions establishes the loop's boundary; it does not make the loop reflective.

Search range and evaluation strength are independent limits:

> Evaluation cannot select a candidate that search never reaches.

A strong verifier can improve judgments within a narrow generator's range, but it cannot expand that range. [Automating KB learning is an open problem] gives one concrete search space—extract, split, synthesize, relink, regroup, reformulate, retire—whose judgment-heavy parts remain substantially human-driven.

## Evaluation determines which changes may remain operative

Evaluation applies criteria to a proposed or already actualized change. Its result must be able to affect selection, rollback, or continued retention. Evaluation is non-vacuous only if some possible result permits rejection: an unconditional trigger is not an evaluator merely because it precedes a transition, and a conditional trigger whose only effect is to launch the next variation is not one either. The verdict must control an operation distinct from producing the next candidate — select, discard, block, roll back — so that rejecting a change and merely changing again are different events in the mechanism.

**Oracle** is shorthand for the component or procedure that supplies the evidence or judgment. It may be a proof system, test, validator, empirical measurement, rubric, model evaluator, human review, or some combination. The [oracle-strength spectrum] grades these mechanisms, while [the boundary of automation is the boundary of verification] explains why constructing an adequate oracle is often harder than generating candidates.

Any judgment remains scoped to what the check establishes. An oracle may accept a candidate under specified criteria without establishing that the change is globally beneficial. Search and evaluation may be performed by the same person or process, but they fail in different ways and improve by different means. They are analytically separable rather than independent: automating one changes the load on the other.

## Operative retention makes the change consequential

Acceptance alone does not make a change consequential. Operative retention combines persistence with an authority path through which the retained result can affect later behavior. In [behavioral authority] terms, the change needs a **consumer**, a **channel**, and a **force**.

- A reviewed note that no future reader or prompt-assembly step loads has no consumer.
- An approved patch that is never merged has no channel.
- A generated validator that no command invokes has no force.

In each case, search ran and evaluation passed, but the proposal-selection loop remained open: the artifact exists without becoming behaviorally consequential.

Artifact labels do not decide whether retention is operative. A knowledge artifact consumed as evidence or advice can affect later behavior, while a nominal system-definition artifact with no consumer cannot. The test is the [behavioral-authority] path: consumer, channel, and force relative to the objective and declared horizon.

For self-improvement, the accepted change must reach the system's own [behavior-determining organization]. Promotion into instruction, enforcement, or configuration is one way to strengthen that path, and may itself run as another proposal-selection instance — [the two-layer execution system] develops that promotion architecture, with recurrence as the trigger, pre-promotion verification as the gate, and methodology growth plus a coverage-test update as retention — but it is not universally required for reflective or operative change.

## Repetition does not establish cumulativity

A proposal-selection loop can repeat on a timer or fresh request without using anything retained by an earlier iteration. Whether later improvement consumes or preserves earlier improvement-relevant information is **cumulativity**, whose criterion and counterexamples belong to [the informational-dependence test on the retained result]. Retained rationale can provide that dependence when later search or evaluation actually consumes it; [design rationale management in Commonplace] documents that path.

## Boundary cases clarify the claim

Cybernetician W. Ross Ashby's ultrastable system marks the subtype's edge from just outside it, and its exclusion follows from the evaluation criterion above, not from a missing component. The electromechanical Homeostat has exactly one evidence-responsive transition: when essential variables leave viable bounds, the parameters jump to new random values ([Ashby 1960, chapters 7–8]). That single jump both discards the incumbent configuration and produces its successor — rejection is not an operation distinct from generation — and a configuration that restores viability persists through equilibrium, with nothing whose function is to accept it. The functions collapse into one trigger, so under the definitions here the machine is a non-reflective, **direct viability-driven** [self-improving system], not an instance of this subtype.

What the Homeostat does admit is a functional variation–selection–retention reading: configurations vary, viability determines whether variation continues, and the survivor persists through non-displacement. That reading is an analyst's reconstruction, not architecture, and its value is to mark the floor of each function — search as a draw from a random-number table bearing no relation to the problem, evaluation as a one-bit viability boundary that ranks nothing, retention as equilibrium, a configuration surviving because nothing is left to displace it. Read this way, the Homeostat is the cheapest demonstration of what a stronger generator and a real oracle actually buy. Reflection is still not a premise of the decomposition. An evolutionary strategy supplies the genuine non-reflective instance: it runs an explicit generate-and-select loop over parameters nothing inside it can read.

The Homeostat's contrast with a gated system is architectural, not a difference of gate strength: a gradient learner has no evaluator either — [online gradient descent] adopts every step the revealed cost dictates, with no accept/reject anywhere (Zinkevich 2003) — and Zinkevich's Greedy Projection/GIGA result supplies the technical counterexample to treating an acceptance gate as universal. The Homeostat stands with it, on the excluded side of the boundary just drawn. [Gödel machines] sit inside the subtype at its formal extreme, a proof-mediated gate rather than none at all; that architecture is developed in their own note.

Reflection is a separate axis from this exclusion: the Homeostat is also non-reflective, and [what that costs is addressability, not category membership] — evidence-responsive operative change to the system's own organization, with or without a self-representation and with or without a gate, is what makes a [self-improving system].

## What the decomposition claims

The three functions are analytically separable, not architecturally separate. One process may perform several of them — a maintainer who notices a problem, drafts the fix, and merges it performs all three — and evaluation may run before a candidate becomes operative or after. Co-location has a floor, though: the functions must remain causally distinguishable even when one process performs them — rejection, in particular, must be an event distinct from the arrival of the next candidate. Where they collapse into a single evidence-triggered transition, as in the Homeostat, the loop is not weakly present; it is absent, and the pathway is direct. The decomposition specifies what the loop must accomplish, not a sequence, a component diagram, or a division of labour. Its use is diagnostic: when a loop stalls, ask which of the three is missing rather than which component failed.

The status claimed here matches how the neighboring self-adaptive-systems field treats its own loop models: MAPE-K — introduced in [Kephart and Chess's autonomic-computing vision], which itself supplies no membership test — and its relatives are presented as reference models for *engineering* adaptation, not as the definition of it ([Weyns, Software Engineering of Self-Adaptive Systems]), and a systematic review of that literature finds no settled formal definition from which any single loop architecture would follow ([Petrovska, Erjiage, and Kugele 2025]). The proposal-selection decomposition is offered in the same spirit — a conceptual model of one architecture, with the [category membership question] settled elsewhere.

## Open Questions

- Whether search range can be measured or bounded for a socio-technical loop in the way oracle strength can be graded.
- Whether a fallible evaluator can govern changes to its own acceptance criteria without either an external criterion or the axiomatization that buys formal closure.

---

Relevant Notes:

## Under-review context phrase

the loop whose functions this claim distinguishes, and the search-range-versus-oracle-strength point it extends
