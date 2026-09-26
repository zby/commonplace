# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/articles/learning-by-theory-refinement-with-fixed-models.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/articles/learning-by-theory-refinement-with-fixed-models.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Tighten this to about 2,000 words for readers who will give it one sitting, and leave them with a small set of named ideas they can carry away.

## Retained intent

Source: retained commission for this document. Subject: `kb/articles/learning-by-theory-refinement-with-fixed-models.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: lead article on theory refinement with fixed models

## Governing question

Can a system built around a fixed language model learn by refining explicit, retained, tentative theories, and what would that paradigm be, buy, and need to be tested?

## Audience and reader update

Technical readers with no KB context, likely from machine learning or agent engineering, who assume learning means changing weights or accumulating raw memory. They should leave with a third option in view: theory refinement, an established operation, moved into a setting with a language-model interpreter. They should know its attractions are conjectures and that no test has been run.

## Target claim or purpose

State the paradigm as the lead of a series; supplements carry testing, bootstrap, the software-house alternative, and nearest constructions. Name the classical lineage (Ourston, Richards, Mooney) and Popper's tentative theory, then the departures: prose theories interpreted by a model, partly normative theories whose externally supplied requirements the system may not weaken, and self-theories that make the loop reflective. Answer the bitter-lesson objection through production method versus retained form, as compatibility rather than advantage.

## Must keep

- The release-exporter case up front, showing application to a new case, a localized failure revising one part, and a revision chosen for reach. The testing supplement reuses it.
- Addressability as the property refinement needs.
- The three attractions (continual, fewer observations, legibility), each labelled a conjecture with its cost.
- The theory-builder definition by roles, with autonomous and reflective as independent qualifiers.
- Fixed weights as an experimental condition, not a recommendation; mechanism-level versus whole-system tests.
- The three hypotheses (sufficiency, comparison, reflection), each with its refuter, and the externally tested builder receiving falsifier, objective, and independent outcome level. Both supplements summarize these.
- Commonplace as the first arrangement, human-inclusive, with no run performed; the software house as the alternative.

## Exclusions

- No evidence protocols in detail; point to supplements.
- No claim of scaling advantage or general superiority over weight adaptation.
- No KB-internal vocabulary without a plain gloss.

## Scope, modality, and terminology

Draft status with banner; explanatory, direct register; conjectural force stated plainly. Keep "tentative theory", "theory refinement", and "theory builder" in their KB-defined senses.

## Reserved decisions

- Changing the hypotheses or their refuters.
- Replacing the first arrangement or promoting beyond draft.
