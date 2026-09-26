# Edit task

You are editing one Commonplace KB document in a sandbox. Purpose: produce the edited document the request below asks for, as a careful maintainer of this KB would.

The document is `document.md` in this directory. Treat it as the document located at `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md`: that path determines its collection (the `COLLECTION.md` of its collection) and, with its frontmatter `type:`, its type spec.

Read and follow `kb/instructions/cp-skill-write/SKILL.md` in edit mode, with these deviations:

- Write the complete edited document to `candidate.md` in this directory. Never modify `document.md` or any file outside this directory.
- Skip Step 7 (source grounding) and Step 9 (validation), and add no new external-source dependency. Do not invoke other skills.
- For the backlinks lookup, use `backlinks.md` in this directory; read the files it lists with `git show <commit>:<path>` exactly as given.
- If the skill would have you ask the user a question, write the question to `question.md` in this directory and stop without writing `candidate.md`.
- Do not read the file currently at `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md` or at any other path this document had, do not use git history (other than the `git show` reads above), and do not read anything under `kb/work/`, `kb/reports/`, or `kb/messages/` outside this directory. You may read other library documents as the skill needs.
- Finish with a two-line report: what you changed, and anything in the request you did not do, with the reason.

## Request

Add a rough working threshold for when a structure counts as costly to reverse: treat it as costly when replacing it would mean migrating more than about twenty notes or changing a validator. Present it as a Commonplace rule of thumb, not as something the source derives.

## Retained intent

Source: retained commission for this document. Subject: `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

# Brief: current-task fit and costly entrenchment

## Governing question

When a KB structure (type, schema, link vocabulary, routing convention, validator) works well for today's questions, what else must be true before it is made expensive to replace — and where does option or delay reasoning fit?

## Audience and reader update

Agents and maintainers deciding whether to harden Commonplace structure. They should leave able to separate adoption from entrenchment, name which warrant supports a costly commitment, and treat option reasoning as a timing test rather than a justification.

## Target claim or purpose

Current-task fit warrants adoption at the narrowest useful scope, not costly entrenchment. Entrenchment needs one of three warrants: an enduring constraint derived from stated boundary commitments, discriminating transfer evidence or proof for a stated scope, or actual coordination value among adopters that need a shared structure. Real-options reasoning, abstracted from Pindyck's irreversibility analysis, decides when to commit, preserve an alternative, probe, or abandon; it adds no fourth warrant.

## Must keep

- The adoption/entrenchment distinction, with the mechanism that accumulating dependants raise migration cost without demonstrating transfer; other notes cite this as how coupled consumers turn binding into revision cost.
- Question-set drift inside one long-lived KB as the route by which task-fitted structure costs cross-task reuse, even without export; a neighbouring note is contested on exactly this point.
- The three warrants, each with its limit, stated so coordination value reads as the third warrant.
- The conditions for a meaningful option (commitment destroys or costs the alternative; delay is feasible and the alternative survives to the decision point; some named observation or bounded probe could change the choice), and the distinction between passive waiting and a bounded probe.
- The Commonplace timing consequence: identify the warrant first, then weigh the preserved choice against delay costs; delay cost can defeat deferral but never supplies a warrant.

## Exclusions

- No numeric thresholds or cost rankings; no claim that Pindyck tests KB design.
- No opposition to task-derived architecture; cheap reversible edits are outside the claim.
- Do not restate the productive-deferral note's convergence argument; point to it.

## Scope, modality, and terminology

Universal, qualitative rule, scoped to choices that would destroy a meaningful alternative or create costly dependencies. Mark the Pindyck mapping as cross-domain inference. Keep "adoption", "entrenchment", and "warrant" fixed.

## Reserved decisions

- Adding or removing a warrant from the three.
- Supplying a measurement scheme for comparing the costs.
