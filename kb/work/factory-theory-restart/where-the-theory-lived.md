# Where the theory lived in the historical factories

The software-factory literature never cites Naur. It engaged his problem
anyway, and its outcome is the derivation's first data point.

## The constructors kept people

The historical factories — Greenfield and Short's, Cook and Kent's Tool
Factory, MDSoFa — were not fully automated, and the incomplete automation was
not an engineering shortfall. The people in the loop were the component that
held the theory: they supplied the family definitions and mappings, and, when
feedback arrived, they interpreted it and redesigned the assets. Our ingest of
Greenfield 2007 records this directly: feedback-supported revision remained
"an open human process."

## Greenfield's program was a bet against Naur

The software-factory pitch was to codify expert knowledge into machinery —
DSLs, metamodels, mappings, patterns — so the expertise of the few could be
used by the many. That is codification applied to the theory itself, and it is
implicitly a bet against Naur's claim that the theory of a program cannot be
fully formulated. The pitch even half-concedes the premise: "capture the
expertise of the few" admits the theory lives in the few; Naur adds that the
capture is lossy and the residue is exactly what modification needs.

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
to pay; broad enough to pay admits novelty, and novelty needs the theory. The
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

Four ways of supplying the theory function a factory needs:

1. **Keep people.** What every historical factory did. Works; but the factory
   scales only as far as its theory-holders, and the theory leaves when they
   do — Naur's account of program death.
2. **Codify it away.** Greenfield's ambition. Captures the formalizable part
   and hits Naur's limit at the remainder — and this strategy was run at
   industrial scale for a decade, so the limit is not hypothetical: it is
   where the effort stopped.
3. **Hold it in natural language, interpreted by a model.** Keep the theory
   informal, as Naur requires, and change the bearer. Neither human-held nor
   codified. This is why LLMs reopen a question the 2000s closed.
4. **Train it into model weights.** Also newly available, and the standing
   rival to the third: project-specific training carries the theory
   implicitly, at the cost of addressability and cheap revision. The Bitter
   Lesson is its argument.

The derivation says a factory needs the theory. The first two carriers are
historical and stopped where the history above stops; the last two are the
live alternatives. The program's bet is the third, run with weights fixed —
which is what makes the third and fourth separable in an experiment.

## The import is selective, both times

From the factory literature the program takes the definition — a configured
production environment holding reusable production knowledge for a declared
family — and not the methodology. That is consistent, not cherry-picking: the
definition is form-neutral, saying the production knowledge must exist and be
reusable, not how it is carried. Greenfield's methodology is what fixed the
form, to codified symbolic assets, and the failure reading above indicts the
fixed form, not the target.

The same selective import already happened with Naur: the program takes the
theory function — mapping, organization-account, demand-relating — and not
his conclusion that only people can hold it. Both originals bind the
knowledge to one carrier: Naur to human heads, Greenfield to codified
artifacts. The program's move, both times, is to keep the function and unbind
the carrier. That is why the bearer question is the empirical center, and why
the carrier list is the representational-form axis applied to the theory
function.
