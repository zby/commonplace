# Software house research program restart

## Goal

Rebuild the research program, not merely revise its current article. Split it
into atomic parts that can be assessed, rejected, and reused independently:
definitions fix the object; derivations expose only their premises and
conclusions; conjectures state contingent bets and their live competitors;
historical accounts supply evidence or explicit retrodictions; and tests later
specify the observations that discriminate among them.

An atomic part does one inferential job, states its status, and makes its
dependencies visible. If it fails, only the parts that depend on it should
fall. Assemble the eventual research program and publication from these parts
after the theoretical structure settles.

## Starting point

Workshop opened 2026-09-02 by the operator. The current program article
(`kb/articles/a-research-program-for-learning-software-factories.md`) has
accumulated machinery — two-layer definitions, boundary declarations, the
measurement instrument, attribution cases, and experiment contrasts — to the
point where the core argument is getting lost in it. Treat that article as
source material rather than inherited structure. Rebuild from scratch, theory
first: state the simplest derivation, grow only what it forces, and keep the
testing machinery out until the theory stands on its own.

## Settled direction

From the article sessions of 2026-09-01/02, recorded so later work need not
re-derive it:

- The theory-need claim is to be *derived*, not posed as a hypothesis; the
  empirical question moves to the bearer: can the theory be held outside model
  weights?
- The theory layer does not need the learner-boundary machinery. Boundaries,
  attribution (the cheap-operator case), the relation-relative comparison, and
  the oracle problem belong to testing, not to the theory.
- The program's term for the full system is **software house**: the persistent
  producer that develops and evolves software in response to its users and
  operating environment. The term is generalized from a human organization
  to a system whose internal roles may be filled by people, computational
  machinery, or both. Automation, changes to production machinery, and
  learning are later claims, not parts of the base definition.
- Greenfield's **software factory** remains family-specific production
  machinery that a software house may use. The research program imports none
  of its product-family, schema, template, or developer-role ontology;
  Greenfield belongs in the historical comparison, not the core derivation.
- Likely eventual shape: a theory note (or notes), then possibly a split of
  the article into a theory-formulation part and a testing part. Not committed
  yet; the derivation comes first.

## Current parts

- [Software house](../../notes/definitions/software-house.md) — the canonical
  system definition, its user boundary, implementation-neutral role
  allocation, automation qualifier, and contrast with Greenfield's software
  factory.
- [naur-derivation.md](./naur-derivation.md) — the simple derivation: a
  software house needs a theory in Naur's meaning.
- [where-the-theory-lived.md](./where-the-theory-lived.md) — the historical
  comparison: Greenfield's constructors designed people in as theory-holders,
  his containment bet met Naur's residue at breadth, and four combinable
  theory-holding architectures frame the program's bet without supplying its
  ontology.
- [why-now.md](./why-now.md) — why software houses can be automated now: LLMs
  move the codification burden from theory content to theory delivery, stated
  as a prediction with three discriminable readings of the current wave, the
  conjecture that full theory-holding machinery is not yet there, and the
  bridge to learning via cheap explicit revision of retained notes.
- [learning-derivation.md](./learning-derivation.md) — the second derivation:
  Naur's guided-participation account explains acquisition, while theory
  revision follows only when production experience exposes that the held
  theory is no longer adequate; the standing-requirement reading is the
  named invalidation-frequency conjecture.
- [holding-conjecture.md](./holding-conjecture.md) — the constructive bet:
  theory holding internalized as natural-language notes caching prior theory
  building, an LLM interpreter, and a harness that activates the right theory;
  plus the competing conjecture that the LLM and harness can instead
  reconstruct it from the primary record on demand.
- [theory-builder.md](./theory-builder.md) — the reverse direction: a
  general theory builder of natural-language theories needs software to
  manipulate them, no closed harness fits a general builder (this document's
  conjecture), so it must keep changing software and falls under the
  derivations; the closing circle is the arc's consistency check, and the
  conclusion is that the program's object is one system that is both software
  house and theory builder.
- [bootstrap-conjecture.md](./bootstrap-conjecture.md) — the second
  conjecture: the theoretical system can be reached by bootstrapping — a
  human-operated system internalizes its own holding through its own
  operation, with declining human theory-interventions as the progress
  measure, while supplied transfer and on-demand reconstruction remain
  competing paths.

## Closure

The workshop closes when the derivations, conjectures, and whatever they force
are promoted to library artifacts — notes and possibly restructured articles —
or deliberately discarded, and the existing article's fate is decided and
executed: rewritten around them, split, or superseded.
