# Where the theory lived in the historical factories

The software-factory literature never cites Naur. It engaged his problem
anyway, and its outcome is the derivation's first data point.

## The constructors kept people — by design

Full automation was not the ambition. Greenfield's software factory is the
machinery: a specialized development environment, its installable template,
its schema, its reusable assets. Around it, his account places people in two
named roles: solution developers use the machinery to build family members;
factory developers harvest domain practice, build and revise the reusable
machinery, and respond to variation the existing asset base did not
anticipate. The factory is the software part of a bigger production system
that includes the people — a system his account describes at length and
never names. Automation is scoped inside the machinery: model-driven
development automates lifecycle tasks from model metadata but "is not the
whole factory."

Look at where the second role sits. Responding to unanticipated variation by
revising the reusable machinery is the theory function — Naur's third
capacity, institutionalized as a job. Greenfield did not overlook the
theory-holder; he designed the position — outside the factory, inside the
system. Our ingest records the consequence:
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

The declared family itself belongs to the bet: scoping, as the derivation
notes, is codification applied to the demand space, buying automation only
over the pre-analyzed region. The family is part of Greenfield's method, not
of the system's ontology — which is why the program's definition leaves
product scope as a parameter.

Together these moves expose the tradeoff: Greenfield gets generality only by
widening the effective system boundary to include human developers, and
automation only by narrowing the automated task to a pre-engineered product
family. His architecture does not provide both within one computational
boundary.

## How a software factory differs from an IDE with libraries

If people hold the theory either way, what separates a software factory from
ordinary tooling? Take a concrete shelf: IntelliJ, the React library, the
Rails framework, and — from the first wave — Microsoft's Web Service
Software Factory, a guidance package that configured Visual Studio to
generate and assemble service applications of one declared kind.

The swap test separates them. Move each to an unrelated shop. The IDE keeps
its full value: it knows editing, debugging, refactoring — programming in
general. The library keeps its value: a solution fragment any product can
embed. The framework keeps most of its value: it decides an architecture,
but for any web application whatsoever. The factory loses almost everything:
its schema, generators, and guidance encode how to produce members of one
declared family, and outside that family they are dead weight. Family-scoped
retained knowledge is the first difference, and it is what makes the reuse
claim testable: the machinery is supposed to transfer across family members,
not across all software. Without the declared family, every shop with an IDE
is a factory and the term says nothing.

The residue test gives the second difference. Ask how much of a new product
the humans still write. With an IDE, nearly everything — the tool assists
keystrokes and navigation. With libraries, less: fragments come ready, and
the humans decide where they go and write what connects them. With a
framework, less again: the skeleton is decided, and the humans fill declared
slots. With a factory, a new family member is mostly generated, assembled,
and configured, and the humans supply the residue. So the difference is a
position on an axis — how much of each member's production is determined by
retained machinery rather than fresh human decision — not a different kind
of thing. The blurriness with frameworks is real and harmless.

Nor are they rivals: the layers stack. The first wave's factories literally
configured the IDE — guidance packages inside Visual Studio — and generated
code against libraries. A factory is what sits on top of an IDE and
libraries when someone commits to a family.

Read this way, the containment bet is a position on the residue axis, and
the comparison with this program becomes precise: the one kind of knowledge
Greenfield's containment left in people — the theory — is the kind an
automated software house would have to move into machinery. The program is
not an extension of Greenfield's ontology or methodology. His factory is one
historical arrangement of production machinery inside a human-operated
software house. An IDE-based house is another; there the theory is carried
entirely by people.

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

## Four theory-holding architectures

Four idealized architectures for supplying the theory function a software
house needs. They are not values on one axis: they combine who
performs the function, where project-specific state is represented, and how
that state is updated. Running systems can combine them.

1. **Human-held theory.** What every historical factory used. Works; but the
   system scales only as far as its theory-holders, and the theory leaves when
   they do — Naur's account of program death.
2. **Codified containment.** Greenfield's actual strategy combined codified
   anticipated variation with human judgment kept for the remainder. It
   captures the formalizable part and meets Naur's limit at breadth — and it
   ran at industrial scale for a decade, so the limit is not hypothetical: it
   is where the effort stopped.
3. **Project-specific notes interpreted by a fixed-weight model.** Retain
   selected theory-building results in natural language while general model
   weights supply the interpreter. This is neither human-held nor a claim to
   have expressed the theory as codified criteria.
4. **Project-specific theory in model weights.** Training changes the weights
   that supply the theory function. This is the standing machine-intensive
   rival to the third, at the cost of addressability and cheap revision. The
   Bitter Lesson is its argument.

The derivation says a software house needs the theory. The historical
factories ran a blend of the first two architectures and stopped where the
history above stops; the last two are the live machine-intensive alternatives.
Both use model weights. They differ in where project-specific, revisable state
is retained: external notes under fixed weights, or the weights themselves.
That is what makes the third and fourth separable in an experiment.

## The historical factory sits inside a software house

The research program defines [software house](../../notes/definitions/software-house.md)
independently as the complete persistent producer. It imports no product
family, schema, template, or developer-role ontology from the factory
literature. In the comparison developed here, Greenfield's configured
environment is a software factory: family-specific machinery used by a human
software house. His factory developers and solution developers are role
fillers in that historical house, not roles the program requires every
software house to have.

The move on the role-fillers is the same move the program makes on Naur:
take the theory function — mapping, organization-account, demand-relating —
and not his conclusion that only people can perform it. Naur binds theory to
human heads; Greenfield's operating model fills the system's roles with
human occupants and its retained knowledge with codified assets. The
comparison keeps the function and varies the filler. That is why the bearer
question is the empirical center. Representational form classifies the state
used within each architecture; it does not classify the whole architecture or
determine who performs the theory function.
