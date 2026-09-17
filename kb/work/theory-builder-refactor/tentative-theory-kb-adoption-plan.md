# Plan: adopt tentative theory across the KB

> **Status:** Deferred migration plan, 2026-09-17. The operator requested the
> workshop terminology change now and a plan for the rest of the KB after
> adoption of the workshop conclusions. The workshop change is complete;
> this plan does not authorize starting the wider migration early.

## Adoption trigger and intended result

Start when the operator adopts the workshop conclusions and the
[README's dispositions](./README.md#what-closes-the-workshop) record the
accepted vocabulary, definition destinations, and treatment of retention
policy. If those conclusions change the meaning or scope of the term,
revise this plan against that decision before editing the library.

The intended result is one consistent use of **tentative theory** for the
theory-refinement object held open to criticism and revision. Its structure
stays in theory refinement. Retention thresholds, permission to consume,
objective preservation, and warrant for revision sequences belong to the
adopted policies or explicit research limitations. They are not imported
into the vocabulary through a rename.

## 1. Establish the durable vocabulary destination

Read the destination collection and type contracts. Prefer a short borrowed
term section in [Theory refinement](../../notes/definitions/theory-refinement.md)
over a second definition of the same structural object. The adoption
decision may instead choose a separate entry if navigation requires one;
settle that destination before changing inbound references. If the term is
registered in the root vocabulary, link that entry to the same destination.

Carry over the bounded grounding from the
[workshop entry](../../notes/definitions/theory-refinement.md#tentative-theory): Popper's
[1966 schema](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)
and the retained passages in
[*Conjectures and Refutations*](../../sources/popper-conjectures-and-refutations.ingest.md#quotes).
Make clear that tentativeness is not a waiting period before establishment
as true. Preserve the qualified fault-localization account: a failed test
may implicate several premises, but identifying the fault is not always
impossible. The library already has that qualification; do not duplicate it.

Narrow the stipulation in [Theory refinement](../../notes/definitions/theory-refinement.md)
that the three loop properties are "the definition of a theory". The
properties are what refinement requires of a theory's representation; a
theory that supplies them is **addressable**, a term the definition already
uses and grades. *Theory* keeps its ordinary sense, and the tentative-theory
entry then reads: an addressable theory held tentatively. This removes an
ontological claim the program does not need and keeps the addressability
precondition, which it does. Adopted by the operator on 2026-09-17 from an
external review; execute it in the same commit as the vocabulary destination.

Every policy obligation in the [policy draft](../../notes/a-claim-without-external-assessment-carries-three-obligations.md)
must receive a disposition: promote the accepted rule to the appropriate
library artifact, delimit the research claim, or explain why the obligation
does not apply to the assessed use. Do not preserve rejected clauses merely
to make a global substitution possible.

## 2. Refresh and classify the candidate inventory

Before editing, recheck the live checkout and other active work. Search
prose, frontmatter, headings, filenames, and link labels; include plural,
hyphenated, and line-wrapped forms. A broad starting scan is:

```bash
rg -n -i 'fallib|tentative.theor' kb --glob '*.md'
rg --files kb | rg -i 'fallib|tentative'
```

Classify each occurrence as current KB terminology, source terminology,
verbatim evidence, immutable task provenance, historical record, or ordinary
use of the adjective. A possibility of error in an evaluator, interpreter,
or process remains *fallible*; it is not a tentative theory. Do not replace
that adjective indiscriminately.

The 2026-09-17 scan found sixteen candidate files outside this workshop.
This is a starting inventory, not a closed list for the later execution.

| Candidate | Planned treatment |
|---|---|
| [Theory refinement](../../notes/definitions/theory-refinement.md) | Update the current KB terminology in description and prose; add or link the adopted borrowed-term entry. Preserve classical authors' own terminology and the task's structural requirements. |
| [Three lineages](../../notes/reflective-theory-refinement-has-three-separate-lineages.md) | Update the KB's learning-mechanism description without attributing Popper's terminology to EITHER, FORTE, or reflection authors. |
| [Program theory and delayed feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md) | Update the theory-use wording and relation descriptions; preserve the argument about search and backtracking. |
| [Addressable theory](../../notes/addressable-theory-can-coordinate-heterogeneous-factory-development.md) | Update the theory-status wording in the body and related-note descriptions. |
| [Theory and capacity building](../../notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md) | Update the related-note description that uses the old terminology. |
| [Cost-sensitive formalisms](../../notes/cost-sensitive-formalisms-for-fallible-theory-search.md) | Update title and description and rename the file to match the adopted title. Handle relocation separately as described below. |
| [The software house as the unit of training](../../articles/the-software-house-as-the-unit-of-training.md) | Update the theory-refinement passage as part of the article's adopted disposition; coordinate with its readability workshop. |
| [Active workshops](../README.md) | Update this workshop's description while it remains active; remove its entry when the workshop closes. |

Eight source reports also contain candidate wording in their **Commonplace
analysis**: [EITHER](../../sources/theory-refinement-analytical-empirical-methods.ingest.md),
[FORTE](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md),
[explanation-based generalization](../../sources/explanation-based-generalization-unifying-view.ingest.md),
[AM and EURISKO](../../sources/why-am-and-eurisko-appear-to-work.ingest.md),
[AutoRA](../../sources/autora-automated-research-assistant.ingest.md),
[ADAS](../../sources/automated-design-of-agentic-systems.ingest.md),
[ATMS](../../sources/an-assumption-based-tms.ingest.md), and
[Popper](../../sources/popper-conjectures-and-refutations.ingest.md).
Update their own comparisons with the KB's theory-refinement concept where
appropriate. Preserve source-side descriptions if changing them would
misstate what the source says; make the KB mapping explicit instead.

## 3. Preserve evidence and history

Never edit captured source snapshots, quoted extracts, bibliographic titles,
or capture metadata to normalize terminology. In particular, the EITHER and
explanation-based-generalization reports contain verbatim `occasion` fields:
these record the question asked at ingestion and must keep its wording.
The grounding append already made in the Popper report does not authorize
rewriting any incumbent quote.

Preserve immutable review results, historical task requests, and event
records. Regenerate replaceable navigation from the migrated artifacts
instead of hand-editing derived entries. Record any surviving legacy term
with its reason in the migration commit; zero raw search matches is not the
completion criterion when evidence or provenance must remain verbatim.

## 4. Execute in reviewable groups

Promote the vocabulary and accepted policy destinations first. Then update
the current notes and adopted article reframes, followed by source-analysis
wording and navigation. Read each affected collection contract before
writing there. Durable library links must point to library destinations,
never to this workshop.

For the cost-sensitive-formalisms filename, use the documented
[`commonplace-relocate-note` command](../../reference/commands.md#commonplace-relocate-note)
to rewrite inbound links. Keep the relocation commit pure, then edit title,
description, and prose in a separate commit. Follow the repository's
published-redirect and freshness-baseline handling for a library move; this
does not create a redirect obligation for the temporary workshop entry.

Coordinate shared files with their active writers. Stage explicit reviewed
paths and keep unrelated changes out. Commit messages state what was
migrated, the number of artifacts, preserved source/provenance exceptions,
and any deferred substantive changes, with the workshop and model trailers.

## 5. Verify and close

Run `commonplace-validate` on every changed artifact and any navigation
changed by relocation or regeneration; validate redirects if the published
map changed. Run the applicable semantic reviews for promoted claims,
including grounding alignment against the retained Popper excerpts. These
are Markdown changes, so pytest is not required.

Repeat the broad scan and inspect every remaining occurrence. Verify that
current KB uses resolve to the adopted vocabulary, policy links resolve to
adopted policy artifacts, source wording and provenance remain intact, and
no library link points into this workshop. Check the final diff against the
adoption decision rather than treating a successful replacement count as
evidence of semantic consistency.

Close only after the candidate inventory and newly discovered occurrences
have explicit dispositions, required validation passes, and the migration
commits record the outcome. Then follow the workshop closure procedure:
retain the durable outputs, delete the workshop, and remove its active-list
entry.
