---
name: cp-skill-revise
description: "Edit, improve, triage findings on, or rewrite a KB note with commonplace-revise: focused fixes, triage, quick or full passes, rewrites, stops, and publication. May write the note. Use cp-skill-review for read-only review."
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
argument-hint: "[<note> [--full|--quick|--pass NAME|--finding RESULT|--plan FILE]] | [triage|rewrite|try|apply|publish|answers|decisions ...]"
---

# cp-skill-revise

Goal: improve, triage, or rewrite a note through `commonplace-revise` while keeping operator decisions, publication boundaries, and continuation stops explicit.

## What it can and cannot do

**Can do:**
- Run simplification passes and finding fixes on one note whose claims stand (`--full`, `--quick`, `--pass`, `--finding`, `--plan`), triage fresh stored warnings/failures (`triage`), apply decided answers (`apply`), publish held candidates (`publish`), trial one edit operation without writing (`try`), list operator and automatic decisions (`decisions`), and rebuild unsettled claims from grounded sources (`rewrite`).
- Carry over identical operator decisions across runs on the same note path (exact `quote` + `change` for proposals; exact criterion + `scope` + `quotes` + `reason` + `level` for triage findings) and feed rejected/deferred findings to later assessors and reviews.
- Protect concurrent edits with a per-note publication lock and start-text/write-brief hash checks. Exact flags live in `commonplace-revise --help` and `commonplace-revise ACTION --help`.

**Cannot do (limitations):**
- **Simplification passes cannot change claims generally, retitle a note, or split it.** Passes keep title, H1, type, brief declaration, and link targets (`narrow-overclaims` needs operator-supplied evidence via `--must-keep`; `split-out-a-treatment` is interactive in a session). Even `rewrite` cannot change the title or filename — retitle separately with `commonplace-relocate-note`.
- **Direct edits publish without asking; `rewrite` and new-warning candidates always hold.** Note-first runs and `apply` write directly to the working tree without whole-text approval (uncommitted; `git diff` shows them, git reverses them). `publish` writes a held candidate only after operator approval of that exact text (or a `--revised` copy). `triage`, `answers`, `decisions`, `rewrite`, and `try` never write the note.
- **Never commits, reverts, or edits a write brief.** No command creates or updates `<stem>.brief.md` without the operator's word.
- **Does not verify that an edit fixed its finding.** No procedure re-reviews the edited note; inspect the actual diff and run `cp-skill-review` when updated verdicts are needed.
- **Never repeats or resumes a run.** Every invocation opens a new run and stops at its first stop (`plan-stop`, `triage`, per-item proposal, `held` candidate, or failed entry), leaving `continuation.json` for a session agent to handle.
- **Refuses stale inputs and in-place edits to held candidates.** `apply` and `publish` refuse if the note, write brief, or watched parts changed since the asking/holding run. Never edit `artifact/final.md` directly (copy it outside `artifact/` and pass `--revised`). On per-item apply/`try`, code checks that unapproved proposal passages stayed unchanged, not that untouched text elsewhere in the note did.
- **Single-note only; does not fetch sources or compute decision stats.** Every editing command targets one note; `decisions` is a read-only listing with no statistics. For `rewrite`, ground sources (`cp-skill-ground`) and write the commission before launching; gitignored/`.snapshots/` sources are referenced by hash rather than copied, and changing one mid-run stops the run.
- **Separate routes:** use `cp-skill-review` for read-only review status and sweeps; use `cp-skill-revise-autoreason` only when explicitly testing the experimental AutoReason blind tournament.

## Pick the procedure

| Intent | Command | Reviews launched | May write note |
|---|---|---|---|
| Fix one finding or run one pass/plan | `commonplace-revise NOTE --finding RESULT` / `--pass NAME` / `--plan FILE` | none | yes |
| Decide fresh stored `warn`/`fail` findings first | `commonplace-revise triage NOTE` | none | no |
| Assessor picks passes from fresh stored findings | `commonplace-revise NOTE --quick` | none | yes |
| Review, assess, and apply simplification passes | `commonplace-revise NOTE --full` (current bare default; name `--full` when required) | all depth-declaring criteria + `type`, `collection`, `compression-synthesis`, `role` | yes |
| Rebuild unsettled claims or synthesis from sources | `commonplace-revise rewrite NOTE --commission FILE` | rewrite candidate review | no (always holds candidate) |
| Trial one edit operation without writing the note | `commonplace-revise try OPERATION NOTE` | none | no |
| List operator and automatic decisions | `commonplace-revise decisions [--note NOTE] [--class NAME]` | none | no |

## Procedure

Resolve relative links below from this skill's real location in the library.

1. **Confirm the procedure before launching.** Tell the operator which procedure will run, whether it launches paid reviews, and whether it may write the note.
   - Pass `--purpose` and `--must-keep` when the operator states them (not with `--plan FILE`, which carries its own). `--must-keep` holds only additions beyond the note's sibling write brief (`brief:` in frontmatter), which every assessor and pass already reads.
   - Use `commonplace-revise` passes when the note's claims stand. Use `commonplace-revise rewrite` when claims or synthesis must be rebuilt from grounded sources; follow [cp-skill-write-multistage](../cp-skill-write-multistage/SKILL.md) to ground sources and write the commission.
2. **Inspect the report and diff after running.** Check `outcome`, `published`, `held`, `continuation`, and `guard`. Exit 0 means `completed` or `needs-continuation`, 1 means failure or concurrent-edit conflict, and 2 means a command error. Always inspect `guard.changed` (other sessions' edits show up too; nothing is reverted) and review the actual diff rather than relying on a worker's summary.
3. **Handle publication, held candidates, and continuation.**
   - **`published: true`**: follow [approve-a-text.md](../approve-a-text.md#after-a-revise-run-publishes) — report covered plan entries, note path, diff path, and that the edit is uncommitted and reversible with git.
   - **`held` is set** (revise candidate added a validation warning, or any accepted rewrite candidate): follow [approve-a-text.md](../approve-a-text.md#a-held-candidate) — show `final.diff` and any `new-warnings` or review warnings; never edit `artifact/final.md`.
   - **`continuation` is set** (`outcome: needs-continuation` or `failed`): follow [continue-a-revise-pass.md](../continue-a-revise-pass.md). For pending answers (`proposals`, `findings`, `plan-stop`), follow [decide-items.md](../decide-items.md).

## Approval commands

Naming a file or run to these commands **is** the operator's approval. Run them **only on the operator's stated word for that exact file or run**:

| Stop output | Command |
|---|---|
| Decided proposals of a per-item pass (`plain-wording`, `abstractions`) | `commonplace-revise apply FILE` |
| Decided finding answers from `triage` or `answers create --run` | `commonplace-revise apply FILE [FILE ...]` |
| Held candidate (exact text, or operator's revision outside `artifact/`) | `commonplace-revise publish RUN` / `commonplace-revise publish RUN --revised FILE` |
| Answers nothing consumes (none approved, plan stop, overtaken run) | `commonplace-revise answers record FILE` |

## Write brief and overtaken runs

- If a `role` report lists relied-on terms or claims absent from the note's write brief, tell the operator and offer to add them (never edit a brief without the operator's word).
- When a structural change (such as a split) overtakes a run's findings, record discussed decisions with `commonplace-revise answers create --run RUN` and `answers record FILE` ([decide-items.md](../decide-items.md#findings-answered-by-a-structural-change)).
