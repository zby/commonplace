# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Make this note readable for someone who has not read the rest of the KB, and strengthen its case by explaining why current LLM reviewers do or do not catch the kinds of errors that composing a text by hand exposes.

## Retained intent

Source: retained commission for this document. Subject: `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: rewrite of the adversarial-loop writing note

## Governing question

The library note "An adversarial human-agent loop can reconstruct the writing-is-thinking filter" claims more than its evidence supports. When writing is distributed across generator, critic, and acceptor, what can a recorded composition loop actually establish, and what would each stronger claim need as evidence?

## Audience and reader update

Agents and maintainers who design or run critique, review, and composition gates, and anyone citing the note as a premise. They should stop reading "the loop reconstructs the filter" as established. They should instead see a tiered evidence ladder: a local artifact correction can be shown from one preserved trace; critic reliability, whole-loop comparison with solo composition, stage attribution, human understanding, and later-system use each need different evidence.

## Target claim or purpose

A preserved challenge, confirmed as a load-bearing fault by independent adjudication and resolved by the final response, establishes a local artifact outcome. It does not validate the method as reliable, causal, or equivalent to solo composition. Offer one candidate record contract (commit-and-expose, challenge-and-locate, respond-and-decide, with defined dispositions), motivated by the writing-practice essays, and state that it is neither canonical nor validated.

## Must keep

- Distinct checker and acceptor roles, and the rule that approval or actor identity (human or agent) is no substitute for evidence; approval grants admission authority only. Two instructions rest on the note's separation of verdict from critique and on decorrelated, fresh checking.
- The requirement that combined checks measure error correlation, and that critic reliability be tested on true conclusions reached by invalid routes, linking the production-versus-evaluation note.
- Naive prose delegation as the contrast case, and the passive-assent / anchoring objection from the practitioner account, treated as a serious objection rather than dismissed.
- The separation of artifact, human-understanding, later-system, and acceptance outcomes.
- Open questions on critic discrimination, commit-and-expose completeness, anchoring order, and a solo baseline.

## Exclusions

- No claim that the loop reconstructs the writing-is-thinking filter or matches solo writing.
- Human writing practices are motivating comparators, not evidence that a distributed loop preserves their effects.
- Rendering, transcription, and stylistic editing are out of scope.

## Scope, modality, and terminology

Conditional, deliberately narrowed claim; state the conditions in the opening. Define "independent adjudication" as a separate role applying a stated criterion, not merely a different actor. Keep the operation names and outcome names fixed once introduced.

## Reserved decisions

- Promoting the candidate over the library note, and the retitle that follows.
- Whether the human judge stays load-bearing; the candidate leaves role allocation to separate warrant, which changes what dependent instructions rest on.
- Updating the rests-on links in the composition-friction and critique instructions.
