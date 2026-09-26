# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Narrow the concession. Keep that methodology, heuristics, and conventions may migrate into weights, but stop saying that no current vocabulary or decomposition is promised permanence: the core vocabulary is now settled enough to commit to.

## Retained intent

Source: retained commission for this document. Subject: `kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: bitter-lesson defense portfolio by role

## Governing question

The KB has accumulated many notes that respond, in one way or another, to the objection that the bitter lesson makes retained theories, instructions, tests, schemas, and programs obsolete. Which of those responses is actually needed to reject the narrow, form-only version of that objection, and what role does each of the others play?

## Audience and reader update

The primary consumers are downstream writers — above all the introductory article arguing that the bitter lesson does not require everything to live in weights — plus agents and maintainers who cite bitter-lesson notes as premises. They currently see a loose cluster of defenses and are at risk of citing more than a conclusion needs, or of presenting a forecast or a methodology note as if it rebutted the lesson. After reading, they should know that one member (the production-method versus representational-form distinction) carries the categorical rebuttal, what that rebuttal leaves unestablished, and which other member to cite for which purpose.

## Target claim or purpose

Only the distinction between production method and representational form is load-bearing for rejecting the inference that localized retained artifacts are inherently incompatible with the bitter lesson. That rebuttal is conditional: a loop that searches over localized artifacts and retains selected ones would make them products of learning, not fixed human knowledge. It does not show that any current loop satisfies the condition. Every other member bounds the conclusion, states the empirical burden, supplies methodology or instrumentation, answers a different objection (absorption, cheap formalization, hand-authorship), sets scope, or forecasts conditionally. The note's job is classification by role so that each downstream claim earns its own support.

## Must keep

- A short statement of Sutton's lesson and of the form-only objection it is being stretched into, so the narrow target is clear.
- The narrow rebuttal and its conditional structure, with what a stronger empirical case would need: scalable cross-artifact credit assignment, manageable evaluator cost, evidence that ontology, decomposition, routing, and acceptance are not just human design moved up a level, and bounded human-judgment burden.
- The recursive extension that loop machinery persists by warrant, not position — flagged as an extension, not a premise.
- The two qualifications that travel with the rebuttal: the concession (no artifact is promised permanence; structure may migrate into weights or be relaxed) and the empirical burden (compare useful work per unit of human judgment against stronger models and simpler memory as scale varies; point to the ablation-baselines proposal as the design space for such tests).
- A role table covering the current members, each with what it contributes and what it does not establish. It must include the unearned-reach diagnostic (and its disclaimer of an inverse guarantee), hardening methodology, instrumentation through self-use, the absorption answer from commitments and authoritative records, the two conditional forecasts, goal-holding failure economics, the per-portion compatibility scope rule, production freedom with its per-artifact-class check, and the substitute-versus-complement criterion marked as candidate with no carrier note.
- The pre-formal-stage row: the cheap-formalization objection is answered as an objection to permanent form, not to a prototype stage. Another note relies on this classification.
- The shared scoping move among per-portion compatibility, production freedom, and the consumer regime: each narrows a claim's scope while leaving the lesson's mechanism at full strength, tied to the rule that mechanism bounds transfer.
- The checkable form of production freedom: ask per artifact class what would have to be undone or added for a search loop to author it.
- A definition of "load-bearing" as "rejecting it reopens the narrow objection", explicitly not a ranking of truth or daily value.

## Exclusions

- No new argument for any member; each member's case lives in its own note.
- No claim that artifact loops currently scale or that the current allocation is efficient.
- No treatment of training frontier models; that regime is out of scope, not denied.
- No forecast presented as something an introduction requires the reader to accept.

## Scope, modality, and terminology

A `synthesis`-trait note, cited as a unit. The central claim is a classification about the argument structure: universal in the sense that one member whose removal did not reopen the objection, or a second member whose removal did, would refute it. State the regime explicitly: improving a system around a frontier model the operator does not train, with limited auxiliary models allowed; say why budget and deployment reality put nearly all systems there, and that cheaper training could move the boundary. Use "representational form" and "production method" in their KB-defined senses; use "load-bearing" only in the defined sense. The portfolio is the current inventory, not a closed set: new defenses enter by being classified here before outward text relies on them.

## Reserved decisions

- Promoting any other member to load-bearing status, or demoting the method/form distinction.
- Promoting the substitute-versus-complement criterion to a carried claim before a carrier note exists.
- Widening the regime to include frontier-model training.
- Dropping members from the table because they seem minor; removal changes what downstream text may cite.
