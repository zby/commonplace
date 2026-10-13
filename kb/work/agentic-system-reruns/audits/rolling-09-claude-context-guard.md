# Claude Context Guard preserved-publication audit

## Disposition

**Integrate with recorded limits — publication clearance only.** No consequential
publication defect or missing public qualification was established within this
bounded audit. The necessary source and coverage limits are already in the
published overview description, synthesis and supporting reports. This report
neither lifts the coordinator-failure hold nor authorizes integration. The outer
coordinator owns that separate reconciliation and integration decision.

The operator explicitly commissioned this fresh audit after the prior hold.
No coordinator was restarted; no run was advanced, retried or integrated. Only
this report was written. No qualification confined to this audit is being used
to repair the publication.

## Identity and inspection scope

- Target: Claude Context Guard, `https://github.com/atreiou/claude-context-guard`.
- Run: `AAS-2026-10-13-claude-context-guard-357cd90664df-01`.
- Frozen method: `25896d8f7968214784f7fd692ec6f622bcb9636b`.
- Frozen source: `efcd0a1815887483a862b32bfb3fbfd6aac79aa6`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/claude-context-guard-357cd90664df`.
- Command environment: that worktree's `.venv/bin`; run-related commands
  executed from that worktree.
- Publication: worktree `kb/agentic-system-analyses/retained/claude-context-guard/`,
  with `overview.md` as public entry.
- Auditor: fresh independent Pi session `01a13707-09dc-76cc-b9ff-588b723ea179`,
  `openai/gpt-6.1-sol`, medium reasoning, verified through `PI_*` environment.
  No delegation.

Chose a bounded mechanism-and-publication audit: read the public entry,
synthesis, boundary, memory and workflow accounts, reconciliation and report/
profile verification; inspect the profile's coverage assessments and rationale;
compare historical mechanism claims; investigate consequential changes in frozen
startup, installation, lessons, itemisation and hook sources. Checked publication
bytes and selected stored attempts. This is not a complete independent review
of every runtime/epistemic declaration or profile unit.

Historical input: origin `kb/agent-memory-systems/reviews/claude-context-guard.md`,
reviewed at `7e09e5b53099ef7b11fd400db39656e766d2e6fa` on 2026-06-04. It supplied
coverage leads, not accepted findings. No old findings were fed back into the
source-first run. The newer source boundary, not historical wording, decides
whether an apparent regression matters.

For evidence below, **P** denotes the publication directory, **R** the worktree
run directory under `kb/agentic-system-analyses/state/` with the run ID above,
and **S** the frozen `related-systems/atreiou--claude-context-guard/` checkout.

## Consequential findings

1. **The core continuity account is retained, with a justified startup change.**
   The historical account's fixed current-file plus last-three-plans recovery
   should not be carried forward as certain behavior. S `.claude/commands/start.md`
   now forbids startup plan reads and moves plan/registry sweeps to `/audit`;
   S `templates/CLAUDE.md` lines 14–15 still demand three plans and the latest
   audit. P `memory.md`, `MEM-OBJ-plans` and integration issue 3, and P
   `synthesis.md`, “Selecting what a later session reads,” retain that conflict
   without inventing precedence. Resume state, task provenance, human feature QA,
   comments, decisions, archives and on-demand sidecar navigation remain covered.
   Five sessions is correctly described as an age window, not a fixed token
   budget or complete discovery guarantee.

2. **Backup and enforcement qualifications are public and source-supported.**
   S `install.sh` sections 4.3/4.5 skip existing settings rather than merge hooks.
   S `.claude/settings.json` uses `CLAUDE_PROJECT_DIR`, while startup can select a
   different `CCG_ROOT`. S `.claude/hooks/pre-compact-save.sh` copies only five
   existing files, increments its counter without checking `cp`, and exits zero;
   it omits resume state, learned behaviour, instructions, plans and archives.
   The commit hook is also an unconditional-pass reminder. P synthesis explicitly
   withholds complete progress capture, active-hook installation, automatic
   restoration and enforced compliance. These are substantive improvements over
   a simple “safety rails” summary, not coverage losses.

3. **Lesson harvesting adds an important route without overstating improvement.**
   S `.claude/commands/lessons.md` specifies this-session scripts only, existing
   lesson/helper checks, interpreted consecutive diffs, human approval before
   installation/deletion, helper export and broken/good self-tests. P synthesis
   carries those conditions and separates candidate criticism, admission,
   future consumption and demonstrated benefit. It does not infer actual helper
   use or improved capacity from exported code or two test cases. No populated
   consumer chain is supplied. This new route need not preserve the historical
   review's broader trace-source labels as proven origin classifications.

4. **Itemisation reliability is bounded rather than silently promoted.**
   S `.claude/commands/itemise.md` contains “500+,” “over 500” and “under 500”
   wording; foreground verification follows worker insertions. Sidecar generation
   precedes filtered integrity comparison, while failure restoration names only
   source. Preserving descriptions by number does not ensure correspondence
   after renumbering. P workflow and synthesis retain exactly-500 ambiguity,
   unavailable host Agent grants/isolation, unspecified retry bounds and unpaired
   rollback. The multiline-string warning is consistent with the source's
   language-insensitive line filter, not evidence of an observed corruption.
   No target execution or corruption experiment was performed in this audit.

5. **Public limits remain visible, including security and incomplete comparison.**
   P overview's description denies demonstrated loss-free recovery/improvement;
   it links the synthesis rather than claiming semantic certification from checks.
   P synthesis's limitations table covers source-policy conflicts, secret-manager
   advice versus credential-recording requests, absent consumer/host execution,
   excluded images/research and partial classification. Independently located the
   security conflict in S `templates/CLAUDE.md` line 26, `save.md` line 35 and
   `end.md` line 37. All ten profile inventory assessments remain `partial`, also
   stated in P profile rationale and synthesis. Verifiers' “Limits: none” means
   no additional verification limit; it does not erase those published limits.

Two nonmaterial details do not require a hold. P reconciliation's “No correction
answers ... supplied” wording is qualified by P report verification's explicit
runtime correction-answer disposition; the repaired threshold remains ambiguous,
not falsely inclusive. The historical README clone-URL lead persists in S
`README.md` lines 36–37 (`atreiou/context-guard`), but does not change this supplied,
verified source identity or the installed mechanism account. Alias/rename validity
was not investigated over the network.

## Publication and operational evidence

- Worktree HEAD equals the frozen method; source HEAD equals the frozen source
  and source `git status --short` is empty.
- Independently hashed every publication file: the exact 13-file set, including
  `ARTIFACT.yaml` and all 12 members, matches R `effects/publish.json`'s `new`
  map, 13/13. All 12 Markdown members also match R `artifact/` byte-for-byte.
  The retained manifest adds member hashes and worker metadata to the artifact's
  one-line seed manifest; R `state/attempts/000048-publish.json` pins its exact
  retained hash `044f9f2009026f0ad0dc36c3f5108d1daef58254a2819953357d712f3c4f4f33`.
  That manifest difference is assembly output, not an unexplained content drift.
- The supplied origin inspection records completed publication, no current open/
  failed attempts or refusals, and empty worker-problems. Historical failure is
  nevertheless present: R `state/attempts/000040-profile-verification.json`
  records `OpenAI Responses stream ended before a terminal response event`;
  `000041-profile-verification.json` records a completed replacement with the
  final verification hash. Terminal empty failed-attempts is not “no failures.”
- Coordinator handle `f5e9e802-2b88-4f9d-8691-b27e0ef7125f` separately returned the
  same terminal stream error without a final report, as retained in origin
  `kb/work/agentic-system-reruns/rolling-09.md`. This audit establishes publication
  byte integrity, not the missing coordinator response or last-advance result.
- No worker tool-call/result traces were located in the run tree or checked
  worktree-local harness locations; R `state/handouts/` has no files. Stored
  attempts, versions, judgments and self-reported validation are not equivalent
  to those traces. Individual `validate-output` execution, exact retry delay,
  complete source-read execution and every worker obligation are not certified.
  Neither publication completion nor empty worker-problems supplies that proof.

## Remaining limits and follow-up

No publication blocker was established within the selected scope. This was not
an exhaustive source reread, full semantic profile audit, host installation test,
network identity check, consumer execution study or worker-compliance audit.
It does not certify unavailable evidence as a pass.

The coordinator-failure reconciliation remains a separate procedural limit.
Before any integration, the outer coordinator must choose a supported disposition
for that failure and perform the standard independently verified integration
checks under separate authority. Recovering unavailable final-advance text is
neither necessary for this byte audit nor something this report fabricates.
If exact worker validation/retry compliance is required for that decision, locate
and pair original worker tool calls/results; absent traces cannot decide it.
Testing actual recovery, source/sidecar fidelity or learning benefit would be
substantial reanalysis requiring a separately commissioned consumer study.

## Validation

Prepared-worktree `.venv/bin/commonplace-validate` against this exact absolute
origin report path returned **VALIDATION SUCCESS**: one text file analysed,
zero failures and zero warnings. Validation concerns this frontmatter-free
workshop report, not semantic certification of the publication or worker compliance.
