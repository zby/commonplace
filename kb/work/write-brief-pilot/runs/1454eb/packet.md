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

Draw more directly on Pindyck's analysis so the timing logic is stated with the rigor of the source rather than informally, and add a short step-by-step procedure maintainers can follow before hardening a structure. Keep the note at about its current length.

## Retained intent

Source: retained commission for this document. Subject: `kb/notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md`. Scope: this document. Force: authoritative for intent; the request above is current user direction and prevails where the two conflict.

Refine the claim that current-task fit warrants only reversible adoption: real options add a conditional test for when replaceability, waiting, or a probe pays, never a fourth entrenchment warrant or a case for passive delay.
