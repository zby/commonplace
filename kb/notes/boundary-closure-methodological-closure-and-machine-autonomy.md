---
description: "Closure and autonomy are readings relative to a chosen system boundary, so boundary closure, methodological closure, and machine autonomy vary independently of each other and of reflectivity"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, self-improving-systems]
---

# Boundary closure, methodological closure, and machine autonomy vary independently

Once a [self-improving system](./definitions/self-improving-system.md)'s boundary is treated as the analyst's choice rather than a given, two properties that read as intrinsic to a loop turn out to be readings taken *relative to* that boundary. Whether the loop is **closed** — completes using only internal resources — depends on where the line is drawn: the same dependency counts as internal or external according to which actors the boundary encloses. Whether a selected component is **autonomous** — proceeds without intervention from the others — depends on the same line seen from the opposite side. Closure looks at the boundary from outside and asks whether any dependency crosses it; autonomy stands inside and asks whether a chosen actor runs without the others. They are the same loop described from two angles, and neither is a fact about the loop until a boundary is fixed.

Three concepts have to be kept apart:

- **System boundary** — which actors and resources count as internal. A free choice, and one that must be declared before either reading below means anything, [as the autonomy grading already requires](./definitions/self-improving-system.md).
- **Closure relative to that boundary** — whether the loop completes using only internal resources; equivalently, whether any required dependency crosses the boundary.
- **Autonomy of a selected actor** — how far that actor proceeds without intervention from the others, humans especially.

## Moving the boundary, not the loop

Suppose a process contains an agent and a human reviewer. Draw the boundary around both, and the loop is closed — every required decision is resolved internally — yet calling it *autonomous* in the machine sense misleads, because a human sits inside the system. Draw the boundary around the computational components only, and the same loop is open — it now depends on an external human decision — while the computational subsystem may still act autonomously between interventions. Nothing about the loop changed; only the boundary did, and both readings flipped, [because moving the line moves the reading](./admitting-a-human-into-the-boundary-trades-reflectivity-for-autonomy.md).

This is what makes the earlier gloss of closure as *procedural completeness* too absolute. The basic sense of closure is topological: does a required dependency cross the chosen boundary? Whether the system's retained method actually settles the decisions that arise is a further, separable question that can hold or fail wherever the boundary sits.

## An actor can be autonomous without settling its decisions

The case that forces the split: an agent receives an underspecified task and improvises until it produces something. No external intervention occurs — so it is autonomous, and drawing the boundary around the agent alone, the loop is boundary-closed. But the decisions were not settled by any retained methodology; they were made up on the spot. This is autonomous execution of an open-ended process — closed and autonomous, yet nothing was *governed*. So three properties come apart, and each answers a different question:

- **boundary closure** — all required functions lie inside the selected system: no required dependency crosses the boundary;
- **methodological closure** — the system's retained methodology settles the consequential decisions that arise, its [closure under its own recommendations](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md);
- **machine autonomy** — the computational components perform the process without human intervention.

## They vary independently

No one of the three is a function of the other two:

| Case | Boundary closure | Methodological closure | Machine autonomy |
|---|---|---|---|
| Agent improvises alone | Yes | Low | High |
| Agent follows a complete method but needs human approval | No, at the machine boundary | High | Partial |
| Agent + human treated as one system | Yes | Potentially high | Not fully machine |
| Fully specified, automated pipeline | Yes | High | High |

The improvising agent is boundary-closed and machine-autonomous yet methodologically open; the approval-gated agent is methodologically closed yet not boundary-closed at the machine boundary. Because the columns move independently, a placement has to report all three — collapsing them loses exactly the discriminating information.

Independence is also why closure sits awkwardly as one of the [gradings of reflectivity](./three-independent-gradings-place-a-self-improving-system.md), which files it alongside retention form and coverage. Retention form and coverage are read off the reflective relationship — how retention is held, which forms are represented. Boundary closure is not: it is an architectural property of where the analyst draws the line, and machine autonomy is an operational property of a selected actor. Methodological closure is a third kind of thing again — a property of the retained methodology-as-input, [not of any one system or agent](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md). None of the three is derivable from reflective structure, which is what the reflectivity gradings measure. The placement scheme's own open question — whether its axes are exhaustive and minimal — is answered here in the direction of *fewer* reflectivity gradings and *more* separately-named system properties.

## The trajectory is internalization by the computational subsystem

The dynamic payoff is sharper than "the loop becomes closed." A broad boundary drawn around a system, its agents, and its human operator may *already* yield a boundary-closed improvement loop; closure at that width is not the interesting event. The interesting event is that the boundary width required for closure is shrinking. Functions that once had to enclose the human operator to reach closure are converted into machine-operable representations, procedures, and checks — [hardening from prose into symbolic form as they cross inward](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — so the computational subsystem alone completes pathways that previously crossed the human–machine boundary.

That is the precise version of "closing the loop": not that the broad socio-technical system becomes closed, but that the loop is progressively **internalized by the computational subsystem**. Each converted function relocates one required dependency from outside the machine boundary to inside it — the boundary-topological reading of [converting improvised decisions into governed machinery](./an-improvement-loop-closes-by-converting-improvised-decisions.md) and of [the human role shifting to the frontier](./a-closing-loop-relocates-human-effort-to-the-frontier.md). Methodological closure and machine autonomy are what advance as this happens: a function that crosses inward is one the retained method now settles and one the machine now performs. Boundary closure at the machine boundary is the accumulating result.

## Where this places the vocabulary

Read as a scheme, the properties layer rather than compete:

- membership in the category needs only operative, evidence-responsive retention;
- reflectivity is graded — coverage and addressability;
- boundary closure is a boundary-relative architectural property, methodological closure a property of the retained methodology, machine autonomy an actor-relative operational property; the three are not reflectivity gradings and vary independently of it and of each other;
- the central trajectory a maturing system traces is the migration of improvement functions across the human–machine boundary into the computational subsystem.

## Scope

- The independence is analytic, not a denial of correlation. A fully automated, fully specified pipeline scores high on all three; the extremes cluster. The claim is that a reading on one does not entail a reading on the others, which is what forces reporting all three.
- The machine-autonomy column is *bare* autonomy — running without a human — not *warranted* autonomy. The improvising agent scores high on it precisely because nothing checks it, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md): boundary closure and bare machine autonomy can both hold while the result is untrustworthy.
- Stated generally, the trajectory is a conjecture about human-operated agentic improvement systems, [Commonplace among them](../reference/commonplace-as-a-reflective-system.md); the closing-loop notes carry its evidence and [the measurement caveats](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md). This note supplies the boundary-topological vocabulary those notes' "displacement" and "relocation" language was reaching for.

## Open Questions

- Whether methodological closure belongs on the same list as boundary closure and machine autonomy at all, or is better held apart as a property of the retained method that merely interacts with the other two — the boundary and the actor.
- Whether [the three-gradings placement scheme](./three-independent-gradings-place-a-self-improving-system.md) should be refactored to move closure out of the reflectivity gradings and adopt this split, or whether the two framings are complementary reports at different grain and should both stand.
- Whether internalization is net-monotone: converting a function inward lets the subsystem attempt harder pathways that re-cross the boundary, so the width required for closure could rebound — the boundary-side form of the frontier-recession question the closing-loop note leaves open.

---

Relevant Notes:

- [Three independent gradings place a self-improving system](./three-independent-gradings-place-a-self-improving-system.md) — contrasts: files closure as one of three reflectivity gradings; this note separates boundary closure from methodological closure and argues closure is boundary-architectural, not a reflectivity grade
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — grounds: supplies methodological closure — "closure under its own recommendations," a property of the methodology-as-input rather than of the boundary
- [An improvement loop closes by converting improvised decisions into governed machinery](./an-improvement-loop-closes-by-converting-improvised-decisions.md) — extends: the internalization trajectory is the boundary-topological reading of conversion and the displacement ladder
- [A closing improvement loop relocates human effort to the frontier instead of reducing it](./a-closing-loop-relocates-human-effort-to-the-frontier.md) — extends: the human-side of internalization — effort crosses outward as functions cross inward
- [Admitting a human into the boundary trades reflectivity for autonomy](./admitting-a-human-into-the-boundary-trades-reflectivity-for-autonomy.md) — grounds: the boundary-relativity these readings rest on — moving the declared line moves the reading
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: autonomy assessed pathway-by-pathway against a declared boundary, the base grading this note builds on
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: whether a system *becoming* more autonomous over time is measurable at all — the caveat on this note's internalization trajectory and its net-monotone open question
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — extends: the machine-autonomy column is bare autonomy; warrant is the further question, and the improvising agent is the unwarranted case
- [Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — mechanism: the form-level account of internalization — a required dependency relocates inward by hardening from prose into symbolic representation
