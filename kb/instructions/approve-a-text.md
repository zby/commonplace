---
description: "Use when commonplace-revise published a text, or a revise or rewrite report has `held`: report the publication, or show the exact held candidate and diff, and on the operator's word publish it or their revision with commonplace-revise publish RUN"
type: types/instruction.md
---

# Approve a text

Goal: the operator knows each text a revise run published, and a held candidate replaces the note only when the operator has seen that exact text, or their revision of it, and said to publish it.

Consumption: an agent in a session with the operator, reached from a run report's `publications` or `held`, or from a `held-candidate` item of a continuation record through [continue a revise pass](./continue-a-revise-pass.md). Nothing here is inherited from the worker instruction; the rules below are the whole procedure. For a list of proposals, follow [decide items](./decide-items.md) instead.

## After a revise run publishes

`commonplace-revise` writes its candidate to the note without a stop when no decision is needed: changes applied without a decision, and items the operator already decided. It does so before a per-item pass is asked for proposals and when the run ends. The report then has `published: true`, and its `publications` list gives, for each publication, the published text `text`, its `diff` from the text before it, and the plan `entries` it covers. The run does not ask for approval of these texts.

After each run whose report has `published: true`:

1. Tell the operator what was published: the plan entries the new publication covers, the path of the note, and the path of the publication's `diff`.
2. Tell the operator that the change is not committed. It is in the working tree, and `git diff` on the note shows it.
3. Tell the operator that they reverse it with git, for example `git checkout -- NOTE` or `git restore NOTE`. The run does not reverse it.
4. If the report has a `continuation`, continue with [continue a revise pass](./continue-a-revise-pass.md).

Do not approve, commit or reverse a publication on your own judgment.

## A held candidate

A revise run holds its candidate when the candidate adds a validation warning the note does not have, and ends. Every rewrite run whose accepted candidate changes the note holds it. The note is not written.

Inputs:

- the run's JSON report: `held` gives the candidate `artifact/final.md`, its `diff` `artifact/final.diff`, the `new-warnings`, the `command` that publishes the candidate and the `revised-command` that publishes a revision; a rewrite's `held.what` also says how many `warn` findings the accepted review left and where it is;
- `new-warnings`: validation warnings that the candidate has and the note did not have;
- `artifact/final.md` and `artifact/final.diff`.

Authority: the decision is the operator's. The agent shows, records and runs commands. It never publishes, rejects or defers on its own judgment, never revises the text on its own judgment, and never edits a file under the run's `artifact/`: the candidate is a workflow output, not an input.

### Procedure

1. If `new-warnings` lists warnings, tell the operator each one, and that a revise run held the candidate because of them. A warning does not block publication; the operator decides with it in view. If `held.what` says the accepted review left findings of level warn, tell the operator how many there are and where the review is.
2. Give the operator the full paths of the note, `final.md` and `final.diff`, so they can open each. Show the operator `final.diff`, and `final.md` when they ask for the whole text. Ask: publish this exact text, publish it with changes, or do not publish it. For publication with changes, follow [accept with a revision](#accept-with-a-revision).
3. On the operator's stated word to publish this exact candidate, run `commonplace-revise publish RUN`, the `command` in `held`. Naming the run is the approval; no other step precedes it.
4. If the command refuses, read the refusal to the operator. It writes nothing when the note no longer holds the text the candidate was held over, when `final.md`, `final.diff` or a rewrite's accepted review changed after the run, when the write brief changed, or when the candidate was already published. A new run works on the current text.
5. When the operator does not want it published, nothing is written and nothing needs to run: the note keeps its text, and `commonplace-revise decisions` lists the candidate as a pending publication until the note changes. To change the candidate other than by a stated revision, start a new run: a replacement plan with `--plan` for revise, or a changed commission for rewrite. Do not edit `final.md`.

### Accept with a revision

Use this when the operator accepts the candidate with changes.

1. Copy `final.md` to a file outside the run's `artifact/` directory.
2. In the copy, apply exactly the changes the operator stated, or the wording the operator approved. Change nothing else.
3. Show the operator the diff from `final.md` to the copy, and ask them to approve that exact revised text. Do not continue before the operator has seen it.
4. On the operator's stated word for that text, run `commonplace-revise publish RUN --revised FILE`, the `revised-command` in `held`. It launches nothing. It is refused on the checks of step 4 above, and when the revised text fails the candidate checks (frontmatter, H1, validation). Read a refusal to the operator. When it publishes, the run keeps the text as `artifact/revised.md`, with `artifact/revised-from-final.diff` from the candidate and `artifact/revised.diff` from the note, and its report lists any `new-warnings` of the published text; tell the operator each one.

Verification: after `publish`, its report names the publication under `published`, and the note holds `final.md` or the revised text. For a rewrite whose published text is the judged candidate, the report's `current-result` names the stored review; after a revision, `not-current` says why the review was not stored. Code writes the note only when every check of step 4 passes. Any other case writes nothing.

Stop and leave the candidate unpublished when the operator declines to decide.
