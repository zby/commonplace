# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/articles/an-automated-software-house-as-an-alternative-test.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/articles/an-automated-software-house-as-an-alternative-test.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Trim this to about 1,900 words, and recast the comparison with the knowledge-base arrangement as a compact side-by-side table readers can scan.

## Retained intent

Source: retained commission for this document. Subject: `kb/articles/an-automated-software-house-as-an-alternative-test.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

## Mission

**Intent.** Give outside readers one entry that states the research program as it now stands, the theory-builder conjecture with its three hypotheses and Commonplace as the first arrangement, and keep the software-house work as a shorter, looser companion that a reader can compare against it. Preserve the Naur argument, which the operator judges the best-made part of the current series. Lose nothing a durable artifact cites; drafts may otherwise be rewritten freely under the articles contract.

**End state.**

- A new companion article exists in draft, about two thousand words: the software-house conjecture as an alternative approach to the same underlying question. It keeps the claim and boundary with their own model cutoff, the Naur section close to its current length, the four witness conditions unchanged, the training regime in one section, and a comparison section whose hinge is Naur's program theory: a theory of the product against a theory that is the product, and what follows for falsifier strength and claim form. It makes no claim to be the main path, the paradigm, or a special case.
- The two supplements keep their status: transition closure as a supplement to the companion.
- the head and companion each carry `source_notes` naming the notes they distil.

**Constraints, non-negotiable.**

- Articles are distilled from notes. Lineage runs notes to article; no reverse edges, and no article links into `kb/work/`.
- Commonplace is a theory builder with external validation from consuming projects. It is never described as a software house. The software house is one arrangement of the evidence interface, not the paradigm or the main path; the side conjecture note keeps its conditional claim and is the only formal link between the two approaches.
- Every draft opens with the authored draft banner.
- Article prose avoids KB-internal vocabulary or defines it on first use for a reader with no KB context.

**Left to the executor.** The titles, which the operator may overrule; how much of the training article's experiments survives, as a section of the companion, a pointer to the explanatory-theories workshop's designs, or a cut.

## Inputs

- The Naur section is the conjecture article's "Why the claim is not trivial", with its two Naur notes in `source_notes`.

## Suggested route

- the comparison section is shared and must say the same thing from both sides.
