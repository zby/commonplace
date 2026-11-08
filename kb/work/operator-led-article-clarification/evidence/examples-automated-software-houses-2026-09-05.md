# Examples: the conjecture article, 2026-09-05

Every edit made to `kb/articles/automated-software-houses-with-fixed-llms.md` by the
operator-led method in one session, with the operator's words where the operator
gave them, the agent's diagnosis, and the text before and after. Before/after
blocks are taken from the commits verbatim; a commit with several hunks shows each.
Read this file before running the method on another article: the verdicts are the
phase-1 inputs, the diagnoses are what phase 2 generalizes from.

Not listed: the eight scope-removal commits from a concurrent session and the two
supplement renames. They are conceptual changes the method surfaced, not edits it made.

## 1. The claim: reachability to operability

- **Commit:** `298295d2`
- **Kind:** Vestigial framing
- **Operator's verdict:** "read kb/articles/automated-software-houses-with-fixed-llms.md and check why we have Practically reachable in the conjecture. The conjecture should not be about reachability - but about operatibility"
- **Diagnosis:** The word survived from the article's earlier life as *the reachability conjecture*, when reaching an adequate house from a human seed was the claim. After the series split, the article allowed the seed to be adequate already, so nothing was reached; the only thing left in the claim was that the house operates reliably. Fixed by renaming the concept and rethreading every consumer (condition 4, protocol bullets, uncertainty paragraph, the supplement's name).

**Before (hunk 1):**

> software change is practically reachable using only LLMs and other learned
> components available by 2026-09-02 and held fixed during the run.
>
> *Practically reachable* means that the house succeeds within a product scope,
> request-generating process, operating horizon, and budget of compute, time,
> and cost declared before the run. *Open-ended* means that the declared
> process can produce relevant requests and consequences that were not listed
> one by one in advance. It does not mean that one house must handle every
> possible software product or request.

**After (hunk 1):**

> software change can operate practically using only LLMs and other
> [distributed-parametric](../notes/definitions/representational-form.md) models
> available by 2026-09-02, the cutoff chosen for this conjecture, and held fixed
> during the run.
>
> *Operates practically* means that the house, started from a declared seed,
> sustains adequate performance over a stated horizon within a stated resource
> budget, reliably rather than by chance. An adequate house applies program
> theory, revises coherently, and continues automatically within the declared
> product scope. The four conditions below specify these capacities and the
> evidence needed for their reliability. The seed may be human-built; how it is
> reached from human-agent production is the bootstrap article's question.
> Report the resources used to build the seed separately from the operating
> budget.
>
> *Open-ended* means that the declared process can produce relevant requests and
> consequences that were not listed one by one in advance. It does not mean that
> one house must handle every possible software product or request.
>
> A *witness* is a concrete example that establishes an existence claim. Here a
> **witness house** would establish the conjecture by meeting its four conditions.
> A **witness run** is an attempt to demonstrate them; its **witness protocol**
> specifies the conditions and evaluation procedure before testing.

**Before (hunk 2):**

>    success within the resource budget and continued adequacy across the
>    horizon. A single successful sequence may result from chance and establishes
>    only possibility, not practical reachability.

**After (hunk 2):**

>    success in sustaining adequacy across the horizon within the resource
>    budget. A single successful sequence may result from chance and
>    establishes only possibility, not practical operability.

**Before (hunk 3):**

> Declare the scope, request process, horizon, resource budget, and success
> threshold before testing to prevent narrowing them after failure. Distinguish
> the allowed histories, the history realized in a run, and the selection
> procedure over histories. Fix the allowed set and selection procedure in
> advance; use repeated runs or another justified estimate to assess success
> across the horizon.

**After (hunk 3):**

> The witness protocol must declare the following before testing:
>
> - **Starting system:** seed, mutable state, pinned distributed-parametric models, and
>   update procedure, including what that procedure may revise.
> - **Boundary and workload:** product scope, permitted external inputs, allowed
>   request and consequence histories, and the procedure selecting those histories.
> - **Resources:** seed-construction effort, the budget for sustaining
>   adequacy, and the operating horizon.
> - **Evaluation:** success thresholds for sustained adequacy,
>   repetitions or another justified estimation method, and the interventions
>   used to test program-theory application.
>
> Keep the allowed histories and selection procedure distinct from the history
> realized in one run. Fixing them in advance prevents removing failed cases
> afterward. The [transition-closure supplement](./transition-closure-and-practical-reachability.md)
> explains how these declarations constrain possible paths and their probabilities.

**Before (hunk 4):**

> Whether current LLMs can participate in a practically reachable system that

**After (hunk 4):**

> Whether current LLMs can participate in a practically operable house that

## 2. TL;DR: restore the existential claim

- **Commit:** `9f864870`
- **Kind:** Lost claim after restructure
- **Operator's verdict:** "we also need to fix the tldr which is mangled now - our conjecture is that there can be an automated software house with todays llm weights"
- **Diagnosis:** A concurrent scope-removal pass had rewritten the TL;DR so that it said only that a house can sustain coherent change while computation decides. The existence claim and the fixed-weights cutoff, which are the conjecture, had dropped out. Fixed by stating the claim first and naming the cutoff.

**Before:**

> changing software for its users. We conjecture that such a house can sustain
> coherent change as requirements and operating conditions develop, while
> computation performs every production decision.
> Its LLMs and other distributed-parametric models stay fixed. The house learns
> by revising its retained knowledge and production machinery, and may begin
> from a human-built seed.

**After:**

> changing software for its users. We conjecture that an automated software
> house is possible with today's LLM weights: a house in which computation
> performs every production decision can sustain coherent change as
> requirements and operating conditions develop, using only LLMs and other
> distributed-parametric models available by 2026-09-02 and held fixed. The
> house learns by revising its retained knowledge and production machinery,
> not its models, and may begin from a human-built seed.

## 3. Open-ended: from caveat to comparative standard

- **Commit:** `4d5bf80d`
- **Kind:** Defensive definition
- **Operator's verdict:** "the problem is that we want to say the house should do everything reasonable - but it is hard to define strictly - maybe just give up and leave 'reasonable' - this is a working paper - so it does not need to be so defensive against adversary reading. The point is that there are programs that cannot be produced even theoretically, others are not possible with available bundget - but the house should in general do at least as well as a human including counterpart"
- **Diagnosis:** The agent had first proposed a tighter definition (fixed selection rules, benchmark contrast, refusals counted). The operator rejected tightening: the caveat that no house must handle every request invited a degenerate house that meets the conditions by declining hard work. Fixed by leaving *reasonable* informal and naming a comparative baseline instead.
- **Frame correction:** The operator's frame replaced the agent's. Lesson: for a working paper, a plain working standard beats a defensive definition; the agent's instinct to close every adversarial reading was wrong here. Operator's closing words: "the previous version that allowed rejecting tasks could lead to degenerate results".

**Before:**

> *Open-ended* means that relevant requests and consequences arise during
> continued development without being listed one by one in advance. The house's
> products and responsibilities can change with those requests. This does not
> mean that one house must handle every possible software product or request.

**After:**

> *Open-ended* means that the house handles whatever reasonable requests and
> consequences arise as development continues, without their being listed in
> advance, including requests that change what the house is responsible for.
> *Reasonable* is left informal. Some programs cannot be produced at all, and
> others not within the available budget; those do not count against the house.
> The working standard is comparative: given the same requests and resources,
> the house should do at least as well as a counterpart house with people in
> its internal production roles.

## 4. The program-theory mechanism paragraph

- **Commit:** `383244f8`
- **Kind:** Unlabelled example; unintroduced term; verdict without its why
- **Operator's verdict:** "this is a bit hard to read - do you have any ideas how to make it easier?"
- **Diagnosis:** Three things were missing: the tenant commitments were mapped onto the mechanism's three functions without being announced as examples; *search* appeared once with no setup; and the closing capacity-versus-mechanism distinction was two elliptical clauses. Fixed by splitting into what program theory is and how it is tested, then the mechanism with the example labelled, *search for a design* introduced before the link, and the distinction in two plain sentences.

**Before:**

> Computer scientist Peter Naur called the understanding needed to choose and
> revise such designs a program theory. Coherent modification across later
> requests is its main behavioural test here. The proposed mechanism is that
> project-specific commitments constrain changes, direct diagnosis, and identify
> what recovery must preserve. Separating a person's identity from organizational
> membership suggests where to revise the model; tenant isolation states what
> must survive. These commitments could [keep search coherent until delayed
> evidence arrives](../notes/program-theory-sustains-search-under-delayed-feedback.md).
> Success tests the capacity; intervening on the commitments tests this proposed
> explanation of how the house achieves it.

**After:**

> Computer scientist Peter Naur called the understanding needed to choose among
> such designs, and to revise them later, a *program theory*. In this article its
> main behavioural test is coherent modification: later requests are handled in
> ways that fit the earlier design.
>
> How would a house achieve that? The proposed mechanism is that retained
> project-specific commitments do three jobs: they rule out changes that break
> the design, they point diagnosis at the likely cause, and they say what a
> recovery must preserve. In the tenant example, the commitment that a person's
> identity is separate from their organizational membership shows where the data
> model has to change; the commitment to tenant isolation says what every change
> must keep true. Commitments like these could [keep the house's search for a
> design coherent while the consequences of a choice are still
> unknown](../notes/program-theory-sustains-search-under-delayed-feedback.md).
> Passing the test shows that the house has the capacity. Changing the
> commitments and observing what the house does next tests whether this
> mechanism explains it.

## 5. The Naur section: signpost the two claims

- **Commit:** `c65e2933`
- **Kind:** Unsignposted roles
- **Operator's verdict:** "here the transition is not clear - the paragraphs have different roles and it is not clear what they do one after another"
- **Diagnosis:** The two paragraphs argued against different targets (the retained-commitment mechanism; the conjecture itself) without saying so. The agent proposed "two reasons for doubt"; the operator corrected the frame. Fixed with a lead-in naming the claims and a topic sentence per paragraph saying which claim it takes up and what it would cost the conjecture.
- **Frame correction:** Operator: "I think actually Naur makes two claims - one is about documentation being not enough to pass the theory another is about only humans being able to hold the theory". The agent's framing (objections the agent attributed to Naur) became the source's own claims. Lesson: when signposting, name what the source says, not what the agent reconstructs.

**Before (hunk 1):**

> [Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
> reports that full code, annotations, extensive design discussion, and personal
> advice did not give one successor team enough program theory. More documentation
> of the same kind did not automatically transfer that understanding. But the
> case tested [one historically bounded package and way of using

**After (hunk 1):**

> Naur makes two claims that bear on the conjecture. The first is that
> documentation cannot pass a program theory to a new team. The second is that
> only people can hold one.
>
> The first claim bears on the mechanism. [Naur's compiler
> case](../sources/programming-as-theory-building.ingest.md) reports that full
> code, annotations, extensive design discussion, and personal advice did not
> give a successor team enough program theory, and that more documentation of
> the same kind did not help. If that generalizes, the retained commitments
> above would be inert. But the case tested [one historically bounded package
> and way of using

**Before (hunk 2):**

> material at the decision point.
>
> One objection is that only people can hold program theory, so computation
> cannot replace every production role. The inference from Naur's argument to
> that conclusion treats machine execution as execution of explicitly formulated
> criteria. An LLM is formal computation, yet can interpret an explanation of
> tenant isolation without that judgment first being reduced to a complete rule. [Formal execution and
> explicitly formulated criteria are different
> things](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
> A successful computational house would refute that inference to a human-only
> conclusion. It would not settle Naur's separate claim that the relevant
> judgment cannot be reduced to a finite set of formulated criteria.

**After (hunk 2):**

> material at the decision point. Whether those transfer more remains open.
>
> The second claim, if true, rules out the conjecture: computation could not
> fill every production role. Naur's argument reaches it only by treating
> machine execution as executing explicitly formulated criteria. [Formal
> execution and explicitly formulated criteria are different
> things](../notes/naur-equates-machine-execution-with-formulated-criteria.md):
> an LLM is formal computation, yet it can act on an explanation of tenant
> isolation without that judgment first being reduced to a complete rule. A
> working computational house would refute the human-only claim. It would leave
> untouched Naur's separate point that the judgment cannot be reduced to a
> finite set of formulated criteria.

## 6. The Naur lead-in: thesis and its evidence

- **Commit:** `b06e616b`
- **Kind:** Unsignposted roles (weighting)
- **Operator's verdict:** "the first claim was probably not very important for Naur - it is kind of passing by claim - but he still makes it - I don't know if we should discuss this"
- **Diagnosis:** The operator doubted the documentation claim deserved discussion. The agent checked the ingest and pushed back: both of Naur's reported cases are documentation failures and Section 6 states it as a rule, so it is the evidence for his thesis, and the one the conjecture's mechanism must actually beat. The operator accepted. Fixed by giving the two claims their relation (thesis, evidence) instead of equal billing.
- **Frame correction:** Lesson: a verdict of "not important" is checked against the source before the passage is cut; the agent's job includes disagreeing with evidence.

**Before (hunk 1):**

> Naur makes two claims that bear on the conjecture. The first is that
> documentation cannot pass a program theory to a new team. The second is that
> only people can hold one.

**After (hunk 1):**

> Naur's thesis is that only people can hold a program theory. His evidence
> for it is that documentation did not pass the theory to new programmers. Both
> bear on the conjecture.

**Before (hunk 2):**

> The first claim bears on the mechanism. [Naur's compiler

**After (hunk 2):**

> The evidence bears on the mechanism. [Naur's compiler

**Before (hunk 3):**

> The second claim, if true, rules out the conjecture: computation could not

**After (hunk 3):**

> The thesis, if true, rules out the conjecture: computation could not

## 7. What a working house would and would not refute

- **Commit:** `5fbf07d7`
- **Kind:** Verdict without its why
- **Operator's verdict:** "I don't understand this"
- **Diagnosis:** "Refute the human-only claim" and "leave untouched Naur's separate point" stated a conclusion whose reason the reader could not reconstruct: an LLM's judgment has no formulated criteria either, so a house shows a program can make the judgment without showing the judgment can be written as rules. Fixed by saying exactly that in three sentences.
- **Frame correction:** The agent explained the passage in plain words first, in the reply, and the explanation became the rewrite. Lesson: when the operator says "I don't understand", the plain-language explanation is usually the fix.

**Before:**

> working computational house would refute the human-only claim. It would leave
> untouched Naur's separate point that the judgment cannot be reduced to a
> finite set of formulated criteria.

**After:**

> working computational house would show that a program can make this judgment,
> refuting the human-only thesis. It would not show that the judgment can be
> written as rules. An LLM's judgment has no formulated criteria either, so
> Naur's claim that the criteria cannot be formulated would stand.

## 8. Sweep 1: the two limits of a retained-theory intervention

- **Commit:** `b108973f`
- **Kind:** Verdict without its why
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. One clause folded a null-result caveat and a positive-result caveat together. Fixed as two sentences: no change may mean other records carry the same understanding; a change shows the note mattered but not whether as explanation, extra facts, or instruction.

**Before (hunk 1):**

> in proposal, diagnosis, or recovery would test its causal contribution. An

**After (hunk 1):**

> in proposal, diagnosis, or recovery would test its causal contribution. Such an

**Before (hunk 2):**

> is local to that component: other records may encode the same understanding,
> and an effect alone need not distinguish explanatory guidance from extra
> information or instruction following.

**After (hunk 2):**

> has two limits. If removing the retained theory changes nothing, that may be
> because other records carry the same understanding. If it changes the house's
> decisions, that shows the note mattered, but not how: the house may have used
> it as an explanation, as extra facts, or as an instruction to follow.

## 9. Sweep 2: the components paragraph

- **Commit:** `485156d0`
- **Kind:** Unsignposted roles
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. One paragraph argued that no component holds the theory alone and that the carrier's form is not fixed. Split with a topic sentence each.

**Before:**

> The components must work together. An unloaded note has no effect; a model
> without enough project state must reconstruct or guess missing understanding;
> software executes a decision without supplying all the judgment that selected
> it. The house may retain an explicit project theory, reconstruct understanding
> from records, or combine both. What matters is causal use: project-specific

**After:**

> No component holds the program theory alone. A note that is never loaded has
> no effect. A model without enough project state must reconstruct or guess the
> missing understanding. Software executes a decision without supplying all the
> judgment that selected it.
>
> Nor does the conjecture fix which form carries the theory. The house may
> retain an explicit project theory, reconstruct understanding from records
> each time, or combine both. What matters is causal use: project-specific

## 10. Sweep 3: equivalent reconstruction in condition 1

- **Commit:** `82a6c51e`
- **Kind:** Unintroduced term
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. The term appeared before the sentence that explained it. Reordered: test, then the written-carrier example, then the term named from it.

**Before:**

>    program theory to guide proposal, evaluation, diagnosis,
>    or recovery, including cases whose correct handling is not stated verbatim
>    in its retained state. Test causal use through matched interventions on
>    retained commitments or the paths used to reconstruct and consume them.
>    The test must connect a changed commitment or access path to a predicted
>    change in the house's decisions, accounting for equivalent reconstruction.
>    Removing one written carrier without changing behaviour is inconclusive
>    when other records supply the same understanding.

**After:**

>    program theory to guide proposal, evaluation, diagnosis, or recovery,
>    including cases whose correct handling is not stated verbatim in its
>    retained state. Test causal use through matched interventions on retained
>    commitments or on the paths used to reconstruct and consume them: a
>    changed commitment or access path must produce a predicted change in the
>    house's decisions. Removing one written carrier without changing behaviour
>    is inconclusive when other records supply the same understanding; call
>    that equivalent reconstruction, and the test must account for it.

## 11. Sweep 4: the Gödel-machine contrast

- **Commit:** `41920fc4`
- **Kind:** Unlabelled parallel; unsignposted role; compressed description
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. The section opened without saying why the contrast is there; the human-written formalization was the seed parallel without saying so; how requests reach an update in each system was compressed. Fixed with a purpose sentence, a labelled parallel, and an unpacked comparison.

**Before (hunk 1):**

> is a formal construction that can rewrite its own code. Its embedded prover
> admits a rewrite only after proving, from the current axioms and formal utility
> function, that switching pays. The starting formalization is supplied in
> advance, as the conjecture allows. Its limit is that it "must ignore those
> self-improvements whose effectiveness it cannot prove"

**After (hunk 1):**

> is the nearest formal construction that changes itself under the same
> provenance requirement as the conjectured house, and the contrast shows what
> proof-gated admission costs. The machine can rewrite its own code. Its
> embedded prover admits a rewrite only after proving, from the current axioms
> and formal utility function, that switching pays. Its starting axioms and
> utility function are written by people in advance, as the conjecture's seed
> may be. Its limit is that it "must ignore those self-improvements whose
> effectiveness it cannot prove"

**Before (hunk 2):**

> consequences, and recover. External requests affect a Gödel-machine rewrite only
> as its formalization gives them utility-relevant meaning. The house relies on
> model interpretation, available checks, and later exposure. The Gödel-machine
> paper does not demonstrate a software house meeting the witness conditions.

**After (hunk 2):**

> consequences, and recover. They also differ in how the outside world reaches
> an update. A request can influence a Gödel-machine rewrite only if its
> formalization already assigns that request a utility; the house instead
> interprets the request with its models, checks what it can, and learns the
> rest from later consequences. The Gödel-machine paper does not demonstrate a
> software house meeting the witness conditions.

## 12. Sweep 5: what pinning shows

- **Commit:** `d12e15e9`
- **Kind:** Verdict without its why
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. "Depends on the rest of the evaluation" was a verdict without its reason. Fixed: pinning isolates one variable and proves nothing on its own.

**Before:**

> the run. Whether the resulting system performs every software-house
> function depends on the rest of the evaluation. Pinning is an experimental
> condition, not a recommendation for mature houses or a claim that updates
> outside weights are generally better.

**After:**

> the run. It isolates one variable and proves nothing on its own: whether the
> house performs every software-house function is what the rest of the
> evaluation must show. Pinning is an experimental condition, not a
> recommendation for mature houses or a claim that updates outside weights are
> generally better.

## 13. Sweep 6: the pinning rules

- **Commit:** `bad358db`
- **Kind:** Vestigial framing (vocabulary); ordering
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. Pinning rule, provider caveat, and cutoff scope were interleaved with stray line breaks; *trial-specific* was bootstrap vocabulary. Reordered and renamed to *run-specific*.

**Before:**

> parametric routers and critics.
> A provider endpoint that may change silently is insufficient unless its model
> lineage can be audited. The cutoff applies to witness runs; ordinary development may use
> newer models. During a witness run, no newer model may supply trial-specific theory,
> diagnosis, candidate comparison, successor selection, or another internal
> production decision.

**After:**

> parametric routers and critics. A provider endpoint that may change silently
> is insufficient unless its model lineage can be audited. The cutoff binds only
> witness runs; ordinary development may use newer models. During a witness run,
> no newer model may supply run-specific theory, diagnosis, candidate
> comparison, successor selection, or another internal production decision.

## 14. Sweep 7: the future-work workload

- **Commit:** `f462b3d8`
- **Kind:** Compressed description
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. "Expose an architectural assumption after intervening changes" and "unlisted parameter variations" said in ordinary words: an assumption whose consequences surface only after later changes; requests that vary within the anticipated design.

**Before:**

> conditions is to expose an architectural assumption after intervening changes,
> then continue maintenance after its revision. The evidence must demonstrate
> application and revision of program theory; a stream of unlisted parameter
> variations does not establish those capacities by itself.

**After:**

> conditions is to build in an architectural assumption whose consequences
> surface only after later changes, then continue maintenance after the house
> revises it. The evidence must demonstrate application and revision of program
> theory. A stream of requests that vary within the anticipated design, even if
> none was listed in advance, does not establish those capacities by itself.

## 15. Sweep 8: the human-agent baseline

- **Commit:** `3f3fa5f7`
- **Kind:** Missing baseline; one term per concept
- **Operator's verdict:** none; found in the phase-2 sweep and applied on "ok - apply these"
- **Diagnosis:** Sweep candidate. Open-ended had been defined by comparison with a house that has people in internal roles, but condition 4 and the evaluation bullet still said *useful success* with no baseline, and the comparison house had two names. Both now name the baseline; the term is *human-agent house* throughout.

**Before (hunk 1):**

> the house should do at least as well as a counterpart house with people in
> its internal production roles.

**After (hunk 1):**

> the house should do at least as well as a *human-agent house*, one with
> people in its internal production roles.

**Before (hunk 2):**

> 4. **Practical reliability.** The declared evaluation must show useful
>    success in sustaining adequacy across the horizon within the resource
>    budget. A single successful sequence may result from chance and
>    establishes only possibility, not practical operability.

**After (hunk 2):**

> 4. **Practical reliability.** The declared evaluation must show that the
>    house sustains adequacy across the horizon within the resource budget,
>    reliably enough to be useful, with a human-agent house given the same
>    requests and resources as the baseline. A single successful sequence may
>    result from chance and establishes only possibility, not practical
>    operability.

**Before (hunk 3):**

> - **Evaluation:** success thresholds for sustained adequacy,
>   repetitions or another justified estimation method, and the interventions
>   used to test program-theory application.

**After (hunk 3):**

> - **Evaluation:** the human-agent baseline and success thresholds for
>   sustained adequacy, repetitions or another justified estimation method, and
>   the interventions used to test program-theory application.

