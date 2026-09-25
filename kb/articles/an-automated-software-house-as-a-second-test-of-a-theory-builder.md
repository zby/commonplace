---
description: "Rewrite plan for the software-house supplement: intent, end state, constraints, inputs, and open choices for a compact article on the automated software house as a second, harder test of a theory builder"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/software-house.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md
  - kb/notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md
---

# An Automated Software House as a Second Test of a Theory Builder

> **Rewrite plan, not the article.** The previous draft of this supplement is
> superseded and stays in git history at commit `6d39a12f`. This page holds
> the plan for its replacement, in the compact form of
> [Building a Theory Builder from Today's LLMs](./building-a-theory-builder-from-todays-llms.md).
> Comments on the plan are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

## Purpose

The lead article's first arrangement is a knowledge base, whose failures
are slow and partly judged by people. This supplement exists to state the
second arrangement, an automated software house, and to say why it is worth
keeping beside the first: **software gives the program a stronger falsifier
than a knowledge base does, at the price of a harder claim.** A researcher
who has read the lead should finish this article knowing what the
software-house conjecture asserts, why an automated house is a theory
builder and not just a coding agent, what a witness would have to show, and
why the arrangement is a companion rather than the main path.

## End state

A draft of about 1,000 to 1,400 words at this path, conjecture first, that a
technical reader with no KB context can restate as four claims:

1. **The conjecture, as stated.** At least one automated software house
   capable of open-ended coherent software change can operate practically
   using only models available by 2026-09-02 and held fixed. Quoted as
   stated, with its working standard: at least as well as a house with
   people in its internal production roles, on the same requests and
   resources.
2. **Why it is a test of a theory builder.** The retained theory is
   Naur's program theory, the account of what the program is for and how
   it is built, held by whoever maintains it. Naur did not show that only
   people can hold it; he equated machine execution with formulated
   criteria, and his compiler case is one historically bounded system.
   A house that revises its program theory under the consequences of its
   own changes, and uses the revision on later requests, runs the lead's
   cycle with software failures as the error-elimination step.
3. **Why the falsifier is stronger.** Failing tests, broken builds, and
   rejected releases are external, fast, and not judged by the house's own
   evaluators. These are the three items of full external assessment (an
   external falsifier, an external objective, and an outcome level
   independent of the builder's evaluators), supplied without the
   consuming-project arrangement the knowledge base needs. The price:
   open-ended coherent change is a harder claim than knowledge delivery, and
   no finite run establishes it.
4. **What a witness must show.** The four witness conditions, holding and
   application, coherent revision, automated continuation, and practical
   reliability, each with what would fail it. A witness run supports a
   version of the conjecture bounded to its workload, horizon, and budget.
   No existing construction meets the four together; the article says so
   and links the survey rather than reproducing it.

The draft says the arrangement is a companion to the knowledge-base test,
not its replacement. It carries the draft banner, links each claim to the
note that develops it, links external texts as themselves, lists its source
notes, and passes `commonplace-validate`. The articles README entry is
rewritten to match.

## Constraints

- **Conjecture first.** The conjecture's wording and its 2026-09-02 cutoff
  are commitments. Quote them; commentary goes around the quotation.
- **Naur is cited as himself.** Link the paper, not the ingest. State what
  he claimed and what he did not, and no more than the two Naur notes
  support.
- **The survey is not repeated.** The nearest-constructions supplement
  holds the eighteen-row comparison. This article states its conclusion in
  one sentence and links it.
- **Companion, not main path.** Say once why the knowledge base remains
  the first arrangement, and do not relitigate it.
- **Ordinary words.** "Program theory" is Naur's term and is defined where
  first used. "Witness house" and "witness run" are defined in one sentence
  each or replaced with plain phrases.
- **Length.** Under 1,400 words. The formal contrast with the Gödel machine
  and the component-by-component account of how the house could hold a
  program theory do not fit; what is worth keeping goes to a note first.

## Inputs

- The superseded draft at `6d39a12f`: its claim section is reused near
  verbatim; the boundary, witness conditions, and comparison sections are
  material, not structure.
- The two earlier superseded drafts, *The Automated Software House
  Conjecture* and *The Automated Software House as the Unit of Training*,
  stay at their addresses with their banners and are not touched.
- The nearest-constructions supplement, for the one-sentence survey
  conclusion.
- The software-house and theory-builder definitions for claims 1 and 2;
  the note on what a claim without external assessment must supply, and the
  testing supplement's evidence-interface section, for claim 3; the two
  Naur notes and the program-theory note for claim 2; the missing-procedures
  note for why a fixed-model house must retain procedures outside its
  weights.

## Choices left to the writer

- Whether the four witness conditions are a list or four short paragraphs.
- Whether one concrete software change is used to show the cycle, or the
  claims stand without an example.
- Section titles and order after the opening conjecture.

## Verification and stop

Validate with `commonplace-validate`. Then read the draft cold and check
that the four claims can be restated and that nothing in it asserts more
about Naur than the two notes support. If a claim needs support no note
supplies, write the note first.
