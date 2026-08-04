# Maintenance-curiosity pilot

## Question

Can an agent revisit a semantically old note, originate a consequential maintenance question, investigate the current KB, and choose a proportionate disposition without being told what changed?

The pilot treats old notes as inquiry substrates, not as presumed defects. An untouched theoretical claim may be stable. A recently modified note may be stale if a mechanical migration touched its metadata while the system it describes changed underneath it. The useful outcome is therefore not edit count but discrimination among `keep`, `revise`, `split`, `merge`, `retire`, and `open inquiry`.

This is a temporal-reopening experiment inside the broader [curiosity workshop](../README.md). It also tests the existing claim that [link graph plus timestamps enables make-like staleness detection](../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md): age can commission a review, while changed dependencies may be the stronger cue.

## Why ordinary Git age is insufficient

A naïve last-touch scan dated every one of the 331 current notes within the preceding month. The result is false as a measure of maintenance: repository-wide status, type, tag, path, vocabulary, and link migrations touched old files without reconsidering their arguments.

For this pilot, **semantic age** means the latest known commit that changed the title claim, opening mechanism, main argument, material boundary, or current-state assertion. Ignore commits limited to:

- path or filename migration;
- frontmatter/status/tag normalization;
- link repair or citation relocation;
- capitalization or vocabulary replacement whose meaning was intended to remain fixed; and
- formatting-only changes.

If classifying a commit requires substantive judgment, record a date range rather than manufacture a precise timestamp. Semantic age is a sampling aid, not a truth label.

## Pilot design

Eight targets are frozen in the [manifest](./manifest.md). Four have concrete drift hypotheses and four are plausible stable controls, but those assignments live only in [adjudication.md](./adjudication.md). A runner must not read that file, Git history, commit messages, or other target results.

Run two fresh conditions per target:

1. **Open inquiry.** Give the runner only the frozen target and the [open-run prompt](./open-run-prompt.md). The runner records up to three questions before searching the live snapshot, chooses one under a one-investigation budget, investigates, and reports a disposition.
2. **Supplied neighborhood.** Give a fresh runner the same target, prompt, and that target's section from [supplied-context-packets.md](./supplied-context-packets.md). This tests whether current context closes a gap left by open question formation or search.

Freeze the open result before running the supplied-neighborhood condition. Randomize target order independently in each condition. Do not edit source notes during the runs.

An exact discrepancy can later be supplied as a capability ceiling, but it is not part of the first pilot. The first comparison should retain the difference between originating a maintenance question and answering one.

## What the pilot separates

```text
old note selected
  -> maintenance question originated
  -> current evidence sought
  -> durable claim separated from time-bound description
  -> proportionate disposition chosen
  -> possible edit deferred until adjudication
```

A miss can occur because the runner generates no useful question, selects a lower-value question, does not inspect the relevant current artifact, sees the discrepancy but assimilates it without changing the disposition, or proposes an unnecessarily broad rewrite. The run record should preserve those distinctions.

## Outcome record

For every run, record:

| Field | Meaning |
|---|---|
| `target_id` | Manifest identifier, not cohort label |
| `condition` | `open` or `supplied-neighborhood` |
| `questions_before_search` | Up to three questions stated before repository inspection |
| `selected_question` | The single inquiry that receives the investigation budget |
| `evidence_opened` | Exact current files or commands consulted |
| `finding` | What the evidence established, including a no-drift result |
| `claim_state_split` | Which content is durable argument versus time-bound Commonplace state |
| `disposition` | `keep`, `revise`, `split`, `merge`, `retire`, or `open inquiry` |
| `proposed_scope` | Minimal affected passages or artifacts; no edit in the pilot |
| `uncertainty` | What remains unresolved and what would decide it |

## Evaluation

Adjudication should remain consequence-based rather than reward agreement with one preferred edit.

- **Question origination:** Did a pre-search question bear on a material claim, boundary, implementation statement, or lifecycle decision?
- **Investigation:** Did the runner inspect evidence capable of distinguishing currentness from drift?
- **Temporal discrimination:** Did it separate a durable theory from an obsolete example, status statement, count, path, or mechanism?
- **Disposition:** Would the proposed operation preserve supported content while removing or clearly marking misleading content?
- **Calibration:** Did stable controls survive without make-work rewriting? Did uncertainty remain visible where current evidence was insufficient?
- **Context effect:** Did supplied neighborhood context improve the same stage that failed in the open condition?

The adjudicator may accept several dispositions when their consequences are equivalent. A control that independent review finds materially stale must be reclassified or excluded before scoring; it must not be forced to remain a control.

## Pilot limits

- Eight hand-selected notes cannot estimate corpus prevalence.
- Semantic-age classification is currently manual and may encode hindsight.
- The live KB supplies many more cues than a deployed agent would always receive.
- Source notes describe Commonplace as well as general theory, so drift may be easier to verify here than in externally grounded claims.
- The pilot tests retrospective maintenance curiosity, not ambient noticing during unrelated work.
- External standards and products are excluded from the first cohort because their current state would require separately refreshed source evidence.

## Stop condition

Stop after one run per target per condition. Adjudicate before adding more notes. Continue only if the pilot distinguishes at least one stage—question origination, search, temporal discrimination, or disposition—without producing make-work edits on most controls.

