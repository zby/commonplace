# Proposal: the open-ended automated theory builder

> **Status:** Agent proposal, 2026-09-09, awaiting operator adoption. It
> reorders claims the KB already holds; the only new content is the
> definition's structure, the role table, and the discriminating test.

## 1. What the reorder is for

The program currently reads: assume an automated software house, then explain
how it learns through theory. The reordered program reads: postulate an
automated theory builder that must handle theories it did not anticipate, then
ask what that forces. The software house stops being a premise and becomes a
conditional consequence.

Three things are gained.

- **An honest novelty claim.** Automatic theory refinement, the operation
  `(T, E) -> T'`, was implemented in the early 1990s. EITHER and FORTE took an
  imperfect Horn-clause theory and labelled cases and produced a repaired
  theory with no human in the refinement step
  ([theory refinement](../../notes/definitions/theory-refinement.md)). What
  those systems fixed in advance was everything around that step: the
  representation, the consequence procedure, the repair operators, the
  evaluator. The proposed advance is acquiring those.
- **A smaller postulate.** A theory builder is a narrower and more testable
  object than a software house. Its outputs are theories, its evidence is
  cases and consequences, and its failure modes are already catalogued in the
  refinement literature.
- **A derivation instead of an assumption.** Whether the builder must contain
  a software house becomes a question with a refuter, stated in section 5.

## 2. The adjective

The ChatGPT summary uses *universal*. Three reasons not to.

1. The KB already holds that [an unqualified *universal* is not a stable
   technical concept](../../notes/universal-software-factory-needs-a-declared-universality-axis.md):
   the word has named portability, factory-valued output, constructional
   expressivity, and acquisition reach, and evidence for one does not
   establish the others. Any use here must declare its axis.
2. Every builder keeps a fixed substrate: the model weights, the host
   language, the operating system, the physics of the machine. *Universal*
   read literally is refuted by that, and read loosely it cannot be refuted
   at all.
3. *Universal* carries the Turing-completeness connotation. The property we
   want is not that the builder can in principle express every refinement
   procedure. It is that it does not need a person to supply the procedure
   when a new kind of theory arrives.

*Open-domain*, the existing note's word, is closer but names the wrong thing.
Domain is subject matter. The demand that matters is a **theory family**: a
kind of theory for which the builder's retained machinery cannot derive
consequences, localize faults, or edit parts. A new domain may or may not
bring a new family, and a new family can arrive inside an old domain.

The proposal uses **open-ended**, copying the sense the
[conjecture article](../../articles/automated-software-houses-with-fixed-llms.md#claim)
already defines: the system handles whatever reasonable requests and
consequences arise as work continues, without their being listed in advance,
including requests that change what it is responsible for. Applied to a theory
builder, this includes theory families for which the builder holds no
refinement machinery when the demand arrives.

The declared universality axis, in the terms of the four-axis note, is
**refinement-machinery acquisition reach**: from permitted evidence, can the
builder determine, construct, and retain the family-specific machinery needed
across a declared demand class. This is the theory-side analogue of the
note's fourth axis, production-knowledge acquisition reach.

## 3. Draft definition

The structure copies the [software house](../../notes/definitions/software-house.md)
definition clause by clause, because the parts that make that definition work
are not specific to software: the functional boundary, the role test, the
separation of persistence from learning, and the automation clause.

**Theory builder.** A theory builder is the complete persistent system
responsible for developing and revising theories for its users. It operates in
response to their questions, cases, evidence, requirements, and the
consequences that arise when its theories are applied. It is not necessarily a
program, a model, or a particular method.

**Boundary.** The theory builder includes the theories whose revision it
remains responsible for, any production knowledge and machinery it uses, and
every person or computational component that fills an internal production
role. The machinery includes representations and their consequence
procedures, repair operators, evaluators and evidence procedures, indexes,
validators, and the records from which any of these can be reconstructed.

Users remain outside the builder when they supply questions, cases, evidence,
preferences, acceptance judgments, or later demands. A person is inside the
builder only when the system depends on them for an internal production role:
interpreting what a theory implies, choosing which part to blame or revise,
writing an evaluator, or repairing the machinery. The same person can occupy
both positions in different interactions. The boundary follows the role, not
the person.

**Persistence.** Persistence means continuity of responsibility for the
theories across demands and consequences. It establishes neither retention nor
learning. A builder whose fixed machinery suffices for every admitted demand
still meets this definition.

**Theory.** A theory here is what the refinement loop requires: an addressable
unit whose consequences a case can contradict, whose parts are available as
candidate repair locations, and whose parts can be edited separately
([theory refinement](../../notes/definitions/theory-refinement.md#what-the-loop-requires-of-a-theory)).
Form is free: natural language, program, causal model, or a mixture. The
theory may describe an external target or the builder's own organization.

**Automated.** An automated theory builder performs every internal production
role computationally. User participation is compatible with automation;
dependence on a human for an internal production role is not.

**Open-ended.** An open-ended theory builder handles whatever reasonable
theories, questions, cases, and consequences arise as work continues, without
their being listed in advance, including demands that change what it is
responsible for and theory families for which it holds no refinement
machinery when the demand arrives. *Reasonable* is left informal, as in the
conjecture article. The working standard is comparative: given the same
demands and resources, the builder does at least as well as a **human-agent
builder**, one with people in its internal production roles.

**Evaluation.** An evaluation examines particular demands over a particular
period. Those limits bound what its evidence establishes; they do not define
the builder's future responsibilities.

### Exclusions

- A model, a prompt, a retrieval index, an agent harness, or a refinement
  algorithm is not the theory builder merely because the builder uses it.
- A user is not inside the builder because their evidence changed a theory.
- A builder is not automated while a person still interprets, localizes,
  evaluates, or repairs for it.
- A stored theory nothing consumes does not count as a theory the builder is
  responsible for, since
  [a representation matters only through its consumption path](../../notes/an-action-model-matters-only-through-its-consumption-path.md).
- Persistence is not evidence that the builder retained experience or learned.

### What the definition does not say

It does not say the builder learns, improves, is reflective, or is a software
house. Each of those is a separate condition with its own evidence. The
derived claim in section 5 connects the last one.

## 4. The role table that replaces the ladder

The ChatGPT ladder has four rungs. Its first three vary one thing, how many
production roles sit inside the computational boundary, and its fourth varies
a different thing, whether the builder's theories act and the consequences
return. These are independent axes, so the ladder should be a table.

**Axis A, role allocation.** The classical systems left five things outside
the automated step. Each is a production role; a level is defined by which
roles move inside.

| Role | EITHER / FORTE | Commonplace today | Automated open-ended builder |
|---|---|---|---|
| Representation and consequence procedure | supplied (Horn clauses, proof) | mixed: schemas and validators inside, prose interpretation by model, new schemas by operator with agents | inside, including construction for new families |
| Repair operators | supplied (retract, generalize, specialize, add) | mixed: full-pass repairs by agents, new repair kinds by operator | inside |
| Evaluator and evidence procedure | supplied (training-set accuracy) | mixed: gates and critique inside, new criteria by operator with agents | inside |
| Initial theory | supplied by an expert | operator and agents | either; a user may still supply one |
| Cases and evidence | supplied | operator, sources, operating consequences | users and consequences; may remain outside |

The bottom two rows are legitimately user-side under the boundary rule in
section 3. The top three are the internal production roles. Classical theory
refinement automated the step between them and left all three supplied. The
reorder's postulate is that all three move inside, including their
construction for families not anticipated when the builder was built.

A consequence the ChatGPT summary misses: **natural-language form does not
by itself move any row inside.** A model can write a natural-language theory
that has none of the three theory properties. Interpretation gives it
consequences only as an interpreter's judgment, not as a computed fact
([codification](../../notes/definitions/codification.md) is the crossing that
changes that). So the builder's first job on an unanticipated family is
constructing addressability for it: a schema that localizes parts, a
consequence procedure that makes contradictions checkable, an evaluator that
scores repairs. That construction is the top three rows, and it is what
section 5 turns into software production.

**Axis B, loop closure.** Whether the builder's current theory shapes what it
does, whether the consequences return as evidence, and whether the revised
theory shapes later action. This is theory refinement run as a closed loop,
and the KB already has the vocabulary for it: the
[discovery lifecycle](../../notes/definitions/discovery-lifecycle.md) names the
phases, and reflective theory refinement names the case where the theory is
about the builder's own organization. The ChatGPT summary's fourth rung adds
no fourth concept; it is this axis, and this workshop uses the existing terms
for it. Evidence on this axis is governed by the existing standards: separate
links on the
[evidence ladder](../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md#evidence-forms-a-ladder),
and [witnesses that identify the joins of one causal path](../../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md).

The two axes are independent in both directions. FORTE inside a control loop
would be closed on axis B with every production role supplied on axis A.
Commonplace's full improvement pass is far along axis A for the families it
already knows and closed on axis B only where a decision cites retained theory.

## 5. The derived claim

**Claim.** If open-endedness repeatedly brings theory families whose
refinement needs machinery the builder does not hold, then an automated
open-ended theory builder must construct and maintain that machinery itself.
Constructing and maintaining representations, consequence procedures,
evaluators, indexes, and validators, under continuing responsibility to users
for the theories they serve, meets the software-house definition. The builder
then contains a software house whose users are the builder's users and whose
software is the builder's production machinery.

**What it depends on.** Two premises. First, that new families arrive often
enough that a fixed machinery set built in advance does not cover them; this is
[broad demands create pressure to construct machinery](../../notes/broad-software-demands-create-pressure-for-agentic-factory-development.md),
restated for theories. Second, that the machinery a new family needs is
software in the ordinary sense, not a new prompt. The second premise holds
where consequences must be computed rather than interpreted, which is where
[the scheduler-model separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
already places exact state and checks.

**Refuter.** A fixed harness general enough that new families never require
machinery changes. The existing
[open-domain note](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
states this refuter and should remain the claim's home; the reorder promotes
it from a side link to the load-bearing step and swaps *domain* for *family*
in the antecedent.

**What the reorder does to the conjecture.** The
[automated software house conjecture](../../articles/automated-software-houses-with-fixed-llms.md)
keeps its claim, boundary, fixed-model premise, and four witness conditions.
Its motivation changes: the house is now the thing an open-ended automated
theory builder is forced to contain, and a witness house is evidence that the
forced component is buildable. The
[training article](../../articles/the-software-house-as-the-unit-of-training.md)
needs the least change; its mechanism already is theory refinement of the
house's own production theory, which is the reflective case of section 3.
The bootstrapping article's seed becomes a seed theory builder rather than a
seed house.

## 6. Discriminating test before building

The derived claim's empirical content is the first premise: new families
repeatedly expose machinery the builder did not hold. Commonplace's own history
is a cheap corpus for one witness, and the test should run before any article
is reframed.

Procedure: walk the commits that changed `kb/types/`, any `COLLECTION.md`,
the validators under `src/commonplace/`, or a skill under
`kb/instructions/`. For each, record whether the change was forced by a new
kind of retained theory (a new claim mode, a new evidence relation, a new
source genre, a new link semantics) or by ordinary maintenance. Then record
whether an agent could have made the change unaided, from the evidence in the
repository, or whether it needed an operator decision. The ADR set is a second
index into the same events.

Two readings decide the next step. Many family-forced machinery changes with
operator decisions inside them: the first premise holds for this witness, and
the reorder proceeds with the operator role named as what automation must
absorb. Few such changes, or changes an agent made unaided: the premise is
weak here, the fixed-harness refuter gains ground, and the reorder should be
scaled to a note rather than an article rewrite.

A second, smaller check positions the novelty claim. Agentic variation
operators, library-learning program synthesizers, and predicate invention in
inductive logic programming each construct some of their own machinery. The
claim survives if each is shown to construct inside a fixed family
(a fixed scoring function, a fixed grammar, a fixed logic) rather than
acquiring a family. The
[AVO ingest](../../sources/avo-agentic-variation-operators-autonomous-evolutionary-search.ingest.md)
already records that AVO's operator sits inside fixed scoring; the other two
are not ingested.

## 7. Choices left to the operator

- **The term.** *Open-ended* is proposed. Alternatives are *open-family*,
  which is precise and ugly, and keeping *open-domain* with a definition that
  stretches domain to cover family.
- **Where the definition lives.** A new `kb/notes/definitions/theory-builder.md`,
  or an extension of the software-house definition with a sibling section.
  The proposal assumes a new definition because the software-house note is
  cited by artifacts that do not need the builder.
- **Whether *users* stays.** The software house serves external users. For
  Commonplace the users of its theories are its operators and readers, and in
  the reflective case the builder itself. The draft says *its users* and lets
  the boundary rule decide who that is per interaction. If the operator wants
  *external* kept, the reflective case needs a sentence.
- **How far the articles move.** Rewriting the conjecture article's head, or
  adding a short companion article that states the reorder and links the
  three. The discriminating test in section 6 should decide this, not
  preference.

---

Relevant Notes:

- [Software house](../../notes/definitions/software-house.md) — copied-from: boundary rule, persistence clause, automation clause, evaluation clause
- [Theory refinement](../../notes/definitions/theory-refinement.md) — rests-on: the three theory properties and the classical role split
- [An open-domain theory builder becomes a software house when new domains require production-machinery changes](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md) — supersedes-candidate: the derived claim's existing home
- [Universal software factory needs a declared universality axis](../../notes/universal-software-factory-needs-a-declared-universality-axis.md) — rests-on: why the adjective must declare an axis
- [A fixed-model house must retain missing procedures for theory use](../../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md) — see-also: the same machinery gap seen from the house side
- [Open-ended theory learning and factory learning close the same reflective loop](../../notes/open-ended-theory-learning-and-factory-learning-close-the-same.md) — see-also: the convergence argument the reorder makes directional
- [The automated software house conjecture](../../articles/automated-software-houses-with-fixed-llms.md) — depends-on: the sense of *open-ended* and the witness conditions kept unchanged
