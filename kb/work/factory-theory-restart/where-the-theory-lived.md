# Where the theory lived in the historical factories

The software-factory literature never cites Naur. It engaged his problem
anyway, and its outcome is the derivation's first data point.

## The constructors kept people — by design

Full automation was not the ambition. Greenfield's definition builds people
in, as two named roles: solution developers use the machinery to build family
members; factory developers harvest domain practice, build and revise the
reusable machinery, and respond to variation the existing asset base did not
anticipate. Automation is scoped inside this: model-driven development
automates lifecycle tasks from model metadata but "is not the whole factory."

Look at where the second role sits. Responding to unanticipated variation by
revising the reusable machinery is the theory function — Naur's third
capacity, institutionalized as a job. Greenfield did not overlook the
theory-holder; he designed the position. Our ingest records the consequence:
feedback-supported revision remained "an open human process."

## Greenfield's bet was containment, not elimination

The software-factory pitch was to codify expert knowledge into machinery —
DSLs, metamodels, mappings, patterns — so the expertise of the few could be
used by the many. Given the role split, the bet was not that the theory could
be fully formulated and its holders eliminated; it was containment: codify
the anticipated variation so solution developers need little theory, and
keep a few factory developers for the unanticipated remainder. Naur's
objection then lands on the containment, not on a strawman of full
codification: the capture is lossy, the residue is exactly what modification
needs — so the question becomes how often the residue is needed. At breadth,
the answer is constantly.

## How a factory differs from an IDE with libraries

If people hold the theory either way, what separates a factory from ordinary
tooling — an IDE, libraries, a framework? Not the presence of humans. Two
things.

The retained knowledge is family-scoped. An IDE and general-purpose libraries
retain knowledge about programming in general; a factory's schemas, DSLs,
templates, and guidance retain knowledge about producing members of one
declared family. The declaration is what makes the reuse claim testable: the
machinery is supposed to transfer across family members, not across all
software. Without it, every shop with an IDE is a factory and the term says
nothing.

And the difference is a position on an axis, not a kind. The axis is how much
of each member's production is determined by retained machinery rather than
fresh human decision. An IDE sits near zero. Libraries move up it; a
framework further — it already decides architecture. A factory is the high
end: generate, assemble, configure, with people supplying the residue.

Read this way, the containment bet is a position on the same axis, and the
program is its limit point: the one kind of knowledge Greenfield's
containment left in people — the theory — is the kind the program tries to
move into retained machinery. A software factory system that holds its own theory in readable
artifacts is not a different project from the software-factory vision; it is
that vision completed. It also follows that the derivation covers the IDE
shop: there the theory is simply all of it, carried entirely by people.

## The vision failed, and our reading of why

The vision did not materialize at scale; the initiative faded within a decade.
[GROUNDING TODO: our only source is the 2007 essay. Before this claim leaves
kb/work it needs sources on the initiative's fate — later retrospectives, the
end of the Microsoft factories effort, the MDD-adoption literature — and on
where the product-line successes sat on the family-breadth axis.]

The standard post-mortems: codification cost more than it saved; the modeled
assets went brittle under change; the expert bottleneck never went away; agile
won the decade. The move this workshop makes: these are not independent
rivals to a theory-holding explanation — they are what Naur predicts
codifying the theory would produce. Codification is expensive because the
theory resists formulation. The assets go brittle because the theory keeps
changing and the codified layer lags it. The bottleneck persists because the
un-codified remainder is load-bearing and only theory-holders carry it.

Family breadth gives the mechanism its squeeze — with one care, because
breadth has two senses. Amortization needs member count: enough family
members to pay for building the factory. The theory-need comes from novelty:
demands nobody pre-analyzed. The two come apart in principle — a family can
be huge and fully enumerated — so the squeeze's load-bearing premise is that
in most software markets they do not come apart in practice: the demand that
supplies paying member count also drifts, so the members differ in
unanticipated ways. Under that premise: narrow enough to codify is too narrow
to pay; broad enough to pay admits novelty, and novelty needs the theory — and in
Greenfield's own role split, novel demands route through the few factory
developers, so the contained theory-holders become the bottleneck. The
prediction to ground: the codification successes — generators, tightly
managed product lines — should cluster where member count is high but novelty
is controlled, and the vision's economics required the markets where it is
not.

Stated with its status: this is the program's explanatory conjecture — a
retrodiction unifying the known failure modes under one mechanism — not an
established causal result. What would refute it: factories that scaled
without theory-holders, or that failed where theory was held and the
codification was adequate.

## The carriers

Four ways of supplying the theory function a software factory system needs:

1. **Keep people.** What every historical factory did. Works; but the factory
   scales only as far as its theory-holders, and the theory leaves when they
   do — Naur's account of program death.
2. **Codify what can be anticipated.** Greenfield's actual strategy was a
   blend of this with the first — containment, people kept for the remainder.
   It captures the formalizable part and meets Naur's limit at breadth — and
   it ran at industrial scale for a decade, so the limit is not hypothetical:
   it is where the effort stopped.
3. **Hold it in natural language, interpreted by a model.** Keep the theory
   informal, as Naur requires, and change the bearer. Neither human-held nor
   codified. This is why LLMs reopen a question the 2000s closed.
4. **Train it into model weights.** Also newly available, and the standing
   rival to the third: project-specific training carries the theory
   implicitly, at the cost of addressability and cheap revision. The Bitter
   Lesson is its argument.

The derivation says a software factory system needs the theory. The historical factories ran
a blend of the first two carriers and stopped where the history above stops; the last two are the
live alternatives. The program's bet is the third, run with weights fixed —
which is what makes the third and fourth separable in an experiment.

## The import is selective — and it modifies the definition

From the factory literature the program takes the definition's structure: a
configured production environment holding reusable production knowledge for a
declared family, with two development processes — building family members,
and building the machinery that builds them. It does not take the
methodology, and — this must be said plainly — it does not take the
definition unchanged. Greenfield's definition fixes the role-fillers:
solution developers and factory developers are people, constitutively. The
program's definition parameterizes them: the roles stay, and who or what
fills each — a person, a codified asset, a model reading retained artifacts,
weights — becomes the open variable. Greenfield's factories are then one
instantiation of the generalized definition, the all-human-plus-codified
one, not the definition itself.

The generalized definition carries its own term — **software factory system**, defined
in the derivation document — rather than reusing "software factory" with a
shifted meaning. The general expectation today may already match the
generalized sense, but Greenfield defined the words otherwise, and importing
a term while quietly changing its meaning is how equivocation gets built.
In these documents "software factory" keeps Greenfield's meaning; the
program's claims are about software factory systems.

The generalization is the same move the program makes on Naur: take the
theory function — mapping, organization-account, demand-relating — and not
his conclusion that only people can perform it. Both originals bind a
function to one filler: Naur binds theory to human heads, Greenfield binds
the factory roles to human occupants and the retained knowledge to codified
assets. The program's move, each time, is to keep the function and unbind
the filler. That is why the bearer question is the empirical center, and why
the carrier list is the representational-form axis applied to the theory
function.
