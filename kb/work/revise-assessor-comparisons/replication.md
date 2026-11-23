# Cross-model replay of the assessor pilot

Requested by the operator, 2026-11-23. Count the four completed GPT-6.2 Astra cells as the first arm. Repeat both conditions on both frozen cases with GPT-6.2 Sol, then Claude Opus 5.5. Each cell gets a fresh project worker, the same packet construction as the pilot, and independently shuffled X/Y labels within case and family. No access to other outputs. No live edit passes. Score the cases by the first trial’s criteria. Use fresh Astra readers blind to condition for consistency with the pilot. Compare within each family first, not raw verbosity across families. A single response per cell measures neither repeatability nor downstream reader success.

## Launch record

Sol (`openai/gpt-6.2-sol`), mixed X/Y then stop X/Y: `20f6403b-b958-4be8-af6e-93006267578c`, `5eb15e1e-66e1-4997-a10f-8dbc4565c368`, `536d005a-d5d6-4580-99e9-04709729c4d4`, `ece90810-878d-451f-b7e9-064a6ef857cc`. Work areas under `kb/reports/state/revise-assessor-comparisons/replication-{sol,opus}/`.

Opus (`anthropic/claude-opus-5-5`), same slot order: `b25c74ed-2730-4a46-a970-b8667f9f49e0`, `8f302592-35b4-49a5-a327-11048fa6218a`, `3f1ca897-f412-4806-bf42-32502c445d8d`, `80da664a-63ff-4b05-b717-9bd340958963`. Four failed launches, no outputs. Anthropic OAuth reported `invalid_grant: Refresh token expired`. No substitution.

Opus rerun, same day: Pi's Anthropic credentials were still invalid, so the four prepared packets ran as fresh headless Claude Code sessions (`claude -p --model claude-opus-5-5`, tools limited to read, write and `ls`, no delegation) with the same worker instructions and task wording as the Sol launch. Harness therefore differs from the Astra and Sol arms. Same slot order: `ec5cc07e-3309-4807-99f2-07dcee8d1fc2`, `47ed3326-5430-409e-bbf8-8379decdc0e2`, `babe1beb-44fa-4a9d-8778-4dd1f3e9cbea`, `fc0cb91d-496b-473d-81ea-9416999ceed1`. The blind reader was a fresh Pi Astra session with the Sol reader's prompt.

## Results

All four Sol plans passed the controller’s `read_plan` checks. Sol’s mixed-case X was amended; its stop-case Y was amended. The [blinded comparison](./blind-sol.txt) evaluated the texts retained in `answers-sol/`. No revision passes were run.

- **Mixed edits:** Sol baseline kept the library case in place; amended Sol moved it next to the facts-versus-values distinction. The blind reader preferred the move for placement, but noted an unnecessary deferral of the independent first-mention gloss for Commonplace. Both planned the referent repairs. Baseline → amended: four → five plan entries; 1,636 → 1,859 assessment words. [Astra](./README.md) kept the case in place under both instructions; its blind reader favored the amended explanation of why *not* to move it. These are different editorial predictions, not measured reader outcomes.
- **Mandatory stop:** both Sol conditions, like both Astra conditions, returned a stop and no executable passes. The amended Sol assessment laid out the operator’s choices more explicitly. Baseline → amended: 1,668 → 1,805 words.

All four Opus plans passed `read_plan`. Opus's mixed-case Y was amended; its stop-case X was amended. The [blinded comparison](./blind-opus.txt) evaluated the texts retained in `answers-opus/`. No revision passes were run.

- **Mixed edits (Opus):** both conditions moved the library case to the "Who gains" question, cut the extra month of counts and scheduled both referent repairs. The amended run explained the move against trimming in place, but the placement plan was the same. Baseline scheduled `narrow-overclaims` on two sentences; amended diagnosed the same two and left them to the operator. Amended scheduled the Commonplace identification that baseline dropped. The blind reader preferred baseline for leaving fewer independent repairs pending. Baseline → amended: five → four plan entries; 1,761 → 2,429 assessment words.
- **Mandatory stop (Opus):** both stopped with no passes and routed the two readings of "requires" to a commissioned rewrite. Blind reader: tie. Baseline → amended: 1,609 → 2,078 words.

## Across the three families

| Family | Library case, baseline → amended | Blind reader on the mixed plan | Stop case |
|---|---|---|---|
| Astra | kept → kept | amended explanation preferred; plan not clearly | both stop |
| Sol | kept → moved | amended preferred for placement; one unnecessary deferral | both stop |
| Opus | moved → moved | baseline preferred; amended deferred two bounded repairs | both stop |

The amendment never broke the mandatory stop (6 of 6 cells stop). It lengthened every assessment (8–38% more words). Its effect on the mixed plan has no consistent direction: the placement choice varies more by family than by condition, and in two of three families the amended run deferred an independent repair that a bounded pass could have made — the over-deferral the amendment's last sentence was meant to prevent. One response per cell cannot separate this from run variation. The three arms do not support changing the live instruction.

The mixed Sol pair supplies a concrete next test: compare the two placements on a reader task, controlling the unrelated changes.
