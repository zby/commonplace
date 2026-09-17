# Workshop: migrate the article series to the theory-builder head

Posed by the operator on 2026-09-17, after the theory-builder definitions
were promoted and the software house was demoted from the main path. The
series currently has three main drafts and two supplements, all headed by
the automated software house. The program's head is now the learning
paradigm carried by a theory builder. Every other article is a supplement
to that one lead.

Revised by the operator later the same day, before any drafting: the lead
leads with the learning paradigm, not with the builder machinery; the
software house is a supplement rather than a companion; and the bootstrap
is a supplement too, so the series is one lead plus supplements with no
second tier. The end state below is the revised one.

## Mission

**Intent.** Give outside readers one entry whose main idea is the learning
paradigm: theory refinement with fixed weights, where what is learned is
retained as revisable tentative theories outside the model, refined from
consequences, and used at the next request. Everything else in the lead is
support for that idea: the theory builder as the system that carries it,
the three hypotheses as what tests it, Commonplace as the first
arrangement. Every other article is a supplement that develops one part of the
lead: the evidence setup, which needs much more testing and so stays out
of the lead; the software house as an alternative arrangement; the
bootstrap as Commonplace's route to autonomy; the two existing supplements
as before. Preserve the Naur argument, which the operator
judges the best-made part of the current series. Lose nothing a durable
artifact cites; drafts may otherwise be rewritten freely under the articles
contract.

**End state.**

- A new lead article exists in draft, short, in this order of emphasis.
  First, the paradigm: theory refinement as the training regime, with the
  three things the current training article marks as new (a partly
  normative theory, preference for explanatory reach among fitting
  revisions, and revisable refinement machinery), the Bitter Lesson
  compatibility argument, and the continual, sample-efficient, and legible
  attractions, each still a conjecture. Then the support, in outline only:
  the theory builder as the system that carries the paradigm; the three
  hypotheses named in a sentence each with what kind of evidence would
  test them; Commonplace producing a KB for consuming projects as the first
  arrangement, in a paragraph; the software house as an alternative
  arrangement, in a sentence; and the open questions. Each support topic
  points to the supplement that develops it. It states that no run exists
  and that the experimental setup is provisional. It defines no term the
  library does not already define.
- A new evidence supplement exists in draft, holding the details the lead
  leaves out: the sufficiency, comparative, and reflection hypotheses in
  full with what refutes each; the theory builder's boundary and lineage
  and the boundary cases; the evidence interface and the externally tested
  main path; reflection and extension as what the program measures; the
  protocol's shape for the first arrangement; and whatever survives of the
  training article's experiments. It opens by saying that the setup is a
  first design that needs much more testing before a run, and it makes no
  claim that the setup is settled. Whether this is one supplement or two
  is left to the executor.
- A new software-house supplement exists in draft, comparable in length to
  the other supplements, about two thousand words. It keeps the claim and
  boundary with their own model cutoff, the Naur section close to its
  current length, the four witness conditions (condition 1 amended as the
  findings below require), and a comparison section whose hinge is Naur's
  program theory: a theory of the product against a theory that is the
  product, and what follows for falsifier strength and claim form. The
  paradigm exposition moves to the lead and is not repeated here. It makes
  no claim to be the main path, the paradigm, or a special case.
- The current conjecture and training articles carry `status: superseded`
  at their existing paths, with a banner naming the successor, so cited
  URLs stay live. The training article's successor is the lead; the
  conjecture article's successor is the software-house supplement.
- The bootstrapping article becomes a supplement. It is relocated under a
  title that names the theory builder, with a published redirect from the
  old address, and its target is an autonomous externally tested theory
  builder rather than a witness house. Its transfer analysis, readiness
  conditions, and worked trial stay.
- The two existing supplements keep their status: nearest constructions as
  is; transition closure as before. The README lists every supplement
  under the lead and says which part of it each one develops.
- `kb/articles/README.md` lists the series in its new order with reading
  guidance, and the lead and the software-house supplement each carry
  `source_notes` naming the notes they distil.

**Constraints, non-negotiable.**

- Articles are distilled from notes. Lineage runs notes to article; no
  reverse edges, and no article links into `kb/work/`.
- Commonplace is a theory builder with external validation from consuming
  projects. It is never described as a software house. The software house
  is one arrangement of the evidence interface, not the paradigm or the
  main path; the side conjecture note keeps its conditional claim and is
  the only formal link between the two approaches.
- Every draft opens with the authored draft banner. Supersession is a
  status change plus a successor banner, never a deletion or a silent
  rewrite of a cited draft.
- The bootstrapping relocation is a pure commit made with the relocate
  command, content edits before or after it in their own commits.
- Reframes stay out of the operator-led-article-clarification workshop's
  readability commits; that workshop records a method, not this content.
- One article per commit, the commit body stating what the change is meant
  to make true. Article prose avoids KB-internal vocabulary or defines it
  on first use for a reader with no KB context.

**Left to the executor.** The titles, which the operator may overrule; the
order of the commits beyond the dependencies below; how much of the
training article's experiments survives in the evidence supplement, as a
section, a pointer to the explanatory-theories workshop's designs, or a
cut; whether the evidence supplement's boundary cases are a paragraph each
or a table; whether the evidence material is one supplement or two; and
the reading guidance in the collection README.

## Inputs

- The library definitions: [theory builder](../../notes/definitions/theory-builder.md),
  [externally tested theory builder](../../notes/definitions/externally-tested-theory-builder.md),
  [reflective](../../notes/definitions/reflective-theory-builder.md) and
  [autonomous](../../notes/definitions/autonomous-theory-builder.md) theory
  builder, the [fence note](../../notes/a-claim-without-external-assessment-carries-three-obligations.md),
  [theory refinement](../../notes/definitions/theory-refinement.md) with its
  tentative-theory section, and [software house](../../notes/definitions/software-house.md).
- The three hypotheses, as stated in the
  [first-downstream-run workshop](../first-downstream-run/README.md#adopted-hypotheses),
  and the [evidence protocol](../first-downstream-run/commonplace-evidence-protocol.md)
  for the first arrangement's shape. The lead article describes the
  arrangement without linking the workshop.
- The current drafts, after the Codex adoption session's reframes of
  2026-09-17 (commit `1061ace8` and its follow-up): the
  [conjecture article](../../articles/automated-software-houses-with-fixed-llms.md),
  the [training article](../../articles/the-software-house-as-the-unit-of-training.md),
  the [bootstrapping article](../../articles/bootstrapping-the-first-automated-software-house.md),
  and the two supplements. The Naur section is the conjecture article's
  "Why the claim is not trivial", with its two Naur notes in
  `source_notes`.
- The boundary cases, in the
  [retained assessment](../../reports/retained/theory-builder-boundary-cases-20260917.md)
  and in the definitions' own words.
- The articles [collection contract](../../articles/COLLECTION.md), the
  [publish instruction](../../instructions/publish-an-article.md) for
  status semantics, and the relocate command in
  [commands](../../reference/commands.md) for the bootstrapping retitle.

## Review findings to carry into the successors

Astra reviewed the conjecture article after the adoption session's reframe
(2026-09-17). The findings are accepted and bind the software-house supplement and, where
marked, the lead; the superseded draft is not patched.

- **Gödel-machine contrast.** The draft says a request can influence a
  rewrite only if the formalization already assigns it a utility. That is
  not what the paper supports: the objective can concern future reward and
  new inputs enter through the formalized operations, as the library's
  [Gödel-machine note](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
  already says. The supported distinction is proof under the formalization
  against empirical acceptance and recovery. If the supplement keeps a
  contrast paragraph, it states that distinction and nothing about advance
  valuation of requests.
- **"Establishes the conjecture" exceeds the evidence.** The conjecture
  covers whatever reasonable requests arise; the four conditions assess a
  declared workload over a finite horizon. In the supplement, a witness run
  supplies evidence for the conjecture under its reported conditions, or
  establishes a version bounded to them. The lead says the same of a
  downstream run: a finite evaluation supports a bounded claim.
- **Witness condition 1 leaves explanatory use underdetermined.** A
  predicted behavioural change after altering a commitment shows causal
  influence; instruction-following also produces one. The condition itself
  must require distinguishing explanatory use from instruction-following,
  by predicted changes on cases not stated verbatim, variation of the
  consumption path, and accounting for equivalent reconstruction, rather
  than leaving those controls to a separate experiment. This amends the
  end state's "four witness conditions unchanged": condition 1 changes in
  this one respect, and the change is recorded in the supplement. The evidence supplement
  carries the same requirement in its account of reflection evidence, where
  the reflective definition already places it.
- **Editorial.** The reframe's research-program paragraph sits before the
  claim is explained. In the supplement the relation to the theory-builder
  program is the last section, so the article stands on its own first.

## Suggested route

Dependencies only; the executor may reorder within them.

1. Wait for the Codex adoption session's final article commit; it holds the
   conjecture and training articles and has asked for no overlapping writes.
   Done: commit `43135cf5` landed and that workshop closed in `fc30a44e`.
2. Draft the lead, the evidence supplement, and the software-house
   supplement together, since the lead's outline and each supplement's
   detail must say the same thing from both sides. Operator review of all
   three before any is listed.
3. Supersede the conjecture and training articles, one commit each, after
   their successors exist to be named.
4. Relocate and reframe the bootstrapping article: pure relocation commit,
   then the content commit.
5. Rewrite the collection README's "In draft" section for the new series.
6. Record the outcome in this README and close: the series is one lead
   plus supplements, with no second tier.

## Coordination

- The Codex adoption session, until its commit lands; its
  [coordination note](../../messages/) in the mailbox names the files it
  holds.
- [first-downstream-run](../first-downstream-run/README.md) owns the
  hypotheses' wording and the protocol; the lead article quotes the
  hypotheses and does not restate the protocol.
- [operator-led-article-clarification](../operator-led-article-clarification/README.md)
  records the readability method; its commits and these stay separate.

## What closes the workshop

The end state above holds, the operator has reviewed the lead, the evidence
supplement, and the software-house supplement, validation passes on every changed article and on the
collection README, and the redirect map validates after the relocation.

Write scope while open: `kb/articles/` and this directory, plus the
redirect map through the relocate command.
