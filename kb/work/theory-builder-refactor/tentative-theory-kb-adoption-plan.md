# Plan: adopt tentative theory across the KB

> **Status:** Migration plan, ready to execute as of 2026-09-17. The
> trigger has fired: the operator adopted the workshop conclusions the same
> day, recorded in the README's [Adoption section](./README.md#adoption)
> (commit `28a2ea8d`), and step 1 below was executed with the promotion
> commit `1b995707`. Execution starts at step 2. The operator is handing
> this to a Codex session.

## Mission

**Intent.** Make the library speak with one voice about the status of a
retained theory: *tentative theory*, Popper's term, applied to an
addressable theory, with the definition at
[theory refinement](../../notes/definitions/theory-refinement.md#tentative-theory)
as the single link target. The rename serves readers who navigate by the
term; it must not change any claim.

**End state.** Every current KB use of the old term resolves to the adopted
vocabulary or is recorded as a deliberate survivor with its reason; every
link that once pointed at the old workshop entry or the deleted
`fallible-theory.md` points at the section above; the cost-sensitive
formalisms note is relocated under its new title; validation passes on every
changed artifact; and the migration commits state what moved, how many, and
what was kept or deferred.

**Constraints, non-negotiable.** Source snapshots, verbatim quotes, occasion
fields, bibliographic titles, and capture metadata are never edited.
Immutable review results and event records keep their wording. *Fallible*
stays wherever it is the ordinary adjective for an evaluator, interpreter,
or process. A relocation commit is pure. No library link points into
`kb/work/`. Coordinate shared files with their active writers.

**Left to the executor.** The order of the groups, the grouping itself, how
occurrences are classified beyond the rule above, and whether an article's
wording waits for its adopted reframe. The numbered sections below are the
author's inventory and suggested route, not a required sequence; where they
conflict with the live checkout, the checkout wins and the deviation is
recorded in the commit.

## Adoption trigger and intended result

The trigger was the operator's adoption of the workshop conclusions,
recorded in the README's [Adoption section](./README.md#adoption). The
conclusions did not change the meaning or scope of the term: tentative
theory is Popper's status, borrowed as is, applied to an addressable theory.

The intended result is one consistent use of **tentative theory** for the
theory-refinement object held open to criticism and revision. Its structure
stays in theory refinement. Retention thresholds, permission to consume,
objective preservation, and warrant for revision sequences belong to the
adopted policies or explicit research limitations. They are not imported
into the vocabulary through a rename.

## 1. Establish the durable vocabulary destination (done)

Executed in commit `1b995707`. The destination is the
[Tentative theory section](../../notes/definitions/theory-refinement.md#tentative-theory)
of the theory-refinement definition, grounded in Popper's
[1966 schema](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)
and the retained passages in
[*Conjectures and Refutations*](../../sources/popper-conjectures-and-refutations.ingest.md#quotes).
The root vocabulary in `AGENTS.md` has a **Tentative theory** entry
pointing there. The same commit narrowed the definition's stipulation that
the three loop properties define *theory* to **addressable theory** and
recorded both terms under its Word forms.

The former retention-policy obligations now live as the first obligation
and the open questions of
[a claim without external assessment carries three obligations](../../notes/a-claim-without-external-assessment-carries-three-obligations.md);
none was promoted as a rule. The migration does not revisit them.

Two rules from this step still bind the rest: the library carries the
fault-localization qualification once, in the theory-refinement definition,
so do not duplicate it into migrated files; and an inbound reference to the
old workshop entry or to the deleted `fallible-theory.md` resolves to the
section above, never to `kb/work/`.

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
A re-scan at hand-off, after the promotion commits, matches 66 files on
`fallib` outside the snapshot store. Most are not candidates: retained
reports under `kb/reports/retained/` and review state under
`kb/reports/state/` are frozen records; source ingests carry source-side
wording, verbatim quotes, and occasion fields; workshop packets, staging
copies, and evidence snapshots under `kb/work/` are records of past runs;
and this workshop's own README, warrant-bounded proposal, and this plan
mention the old term as history. Classify before editing, and expect the
live candidate set to be near the table below plus the notes the scan
adds: the consumption-channel, retrieval-miss, codify-versus-LLM,
proposal-selection-loop, closure, open-ended-construction, project-theory,
residue-classes, vocabulary-collisions, and why-notes-have-types notes,
each of which may use *fallible* as the ordinary adjective and needs the
classification rule above, not a substitution.

| Candidate | Planned treatment |
|---|---|
| [Theory refinement](../../notes/definitions/theory-refinement.md) | Update the current KB terminology in description and prose; add or link the adopted borrowed-term entry. Preserve classical authors' own terminology and the task's structural requirements. |
| [Three lineages](../../notes/reflective-theory-refinement-has-three-separate-lineages.md) | Update the KB's learning-mechanism description without attributing Popper's terminology to EITHER, FORTE, or reflection authors. |
| [Program theory and delayed feedback](../../notes/program-theory-sustains-search-under-delayed-feedback.md) | Update the theory-use wording and relation descriptions; preserve the argument about search and backtracking. |
| [Addressable theory](../../notes/addressable-theory-can-coordinate-heterogeneous-factory-development.md) | Update the theory-status wording in the body and related-note descriptions. |
| [Theory and capacity building](../../notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md) | Update the related-note description that uses the old terminology. |
| [Cost-sensitive formalisms](../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) | Update title and description and rename the file to match the adopted title. Handle relocation separately as described below. |
| [The software house as the unit of training](../../articles/the-software-house-as-the-unit-of-training.md) | Update the theory-refinement passage as part of the article's adopted disposition; coordinate with its readability workshop. |
| [Active workshops](../README.md) | Done at hand-off: the entry no longer uses the old term. Remove the entry when the workshop closes. |

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
