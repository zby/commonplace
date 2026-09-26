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

# Brief: costly entrenchment and option value

## Governing question

How should the existing claim that current-task fit alone does not warrant
costly structural entrenchment be refined by real-options theory without
turning replaceability or delay into unconditional virtues?

## Audience and intended use

Commonplace maintainers deciding whether to harden a task-fitted type, schema,
link vocabulary, routing convention, validator, or other structural choice.
The reader should retain the existing adopt-versus-entrench distinction and
three entrenchment warrants, while gaining a qualitative test for when
replaceability, waiting, or a bounded information-producing probe has value.

## Target

- Collection: `kb/notes/`
- Type: `kb/types/note.md`
- Central claim remains: current-task fit alone warrants at most reversible
  adoption; costly entrenchment needs an enduring constraint, discriminating
  transfer evidence or proof for a stated scope, or coordination value that
  justifies the commitment.

## Required refinements

- Preserve adoption versus entrenchment: the branch applies only when current
  action would destroy a meaningful alternative or create dependencies costly
  to reverse. A cheap reversible edit does not need option analysis.
- Make the value of replaceability conditional. Later observation or a bounded
  probe must be capable of changing the structural choice, and the alternative
  must remain available at the later decision point.
- Count delay costs: foregone routing or validation benefit, fragmentation,
  missed coordination value, migration accumulated while waiting, and expiry
  or loss of the alternative can warrant committing now.
- Distinguish passive waiting from active evidence production. A bounded probe
  can be justified when it yields information that can change the later
  entrenchment decision without committing the full structure.
- Keep the existing three entrenchment warrants. Real-options theory refines
  the timing and replaceability decision; it is not a fourth warrant and does
  not prove a monetary threshold.
- Treat the Pindyck formulation as source methodology, the costly-to-reverse
  choice and information-arrival relation as the shared mechanism, and the KB
  decision rule as a Commonplace consequence.
- Preserve existing qualifications, examples, source-boundary claims, useful
  outbound links, and the central meaning relied on by backlinks unless the
  audit establishes a conflict.

## Collection and type constraints

Follow `kb/notes/COLLECTION.md` and `kb/types/note.md`. Preserve one atomic
title claim, simple prose, explicit source/shared-mechanism/Commonplace
separation, and a dedicated Scope section. Do not import financial mathematics,
complete-market assumptions, passive-waiting preference, or project-management
bureaucracy.

## Known uncertainties and user decisions

- The source supplies a qualitative decision structure, not a calibrated KB
  threshold or target-side effectiveness evidence.
- The record does not quantify migration, coordination, delay, or probe costs.
- No user-reserved decision remains.
