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

Add a short section that walks through the first arrangement's protocol step by step, so readers who never open the evidence supplement still see how a run would actually go.

## Retained intent

Source: retained commission for this document. Subject: `kb/articles/learning-by-theory-refinement-with-fixed-models.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

## Mission

**Intent.** Give outside readers one entry that states the research program as it now stands, the theory-builder conjecture with its three hypotheses and Commonplace as the first arrangement, and keep the software-house work as a shorter, looser companion that a reader can compare against it. Lose nothing a durable artifact cites; drafts may otherwise be rewritten freely under the articles contract.

**End state.**

- A new head article exists in draft: the theory-builder conjecture, its sufficiency, comparative, and reflection hypotheses with what refutes each, the theory builder with boundary and lineage, the evidence interface and the externally tested main path, reflection and extension as what the program measures, Commonplace producing a KB for consuming projects as the first arrangement with the protocol's shape, the relation to the software-house approach, and the open questions. It states that no run exists. It defines no term the library does not already define.
- the head and companion each carry `source_notes` naming the notes they distil.

**Constraints, non-negotiable.**

- Articles are distilled from notes. Lineage runs notes to article; no reverse edges, and no article links into `kb/work/`.
- Commonplace is a theory builder with external validation from consuming projects. It is never described as a software house. The software house is one arrangement of the evidence interface, not the paradigm or the main path; the side conjecture note keeps its conditional claim and is the only formal link between the two approaches.
- Every draft opens with the authored draft banner.
- Article prose avoids KB-internal vocabulary or defines it on first use for a reader with no KB context.

**Left to the executor.** The titles, which the operator may overrule; whether the head article's boundary cases are a paragraph each or a table.

## Inputs

- The head article describes the arrangement without linking the workshop.

## Suggested route

- the comparison section is shared and must say the same thing from both sides.
- The comparison section's hinge is Naur's program theory: a theory of the product against a theory that is the product, and what follows for falsifier strength and claim form.

## Coordination

- first-downstream-run owns the hypotheses' wording and the protocol; the head article quotes the hypotheses and does not restate the protocol.
