# V0 Two-Loop Algorithm

Use this for the first experiments. Do not build a general tuple-evolution system yet. The status file is a sparse control surface, and changes happen through two loops:

```text
external loop: choose which tuple part is active
internal loop: propose, verify, and accept/reject one complete candidate state for that part
```

The tuple for v0 is:

```text
S = (text, claim_ledger, presentation_spec, rubric, gap_policy)
```

`notes` may exist in `status.yaml`, but they are commentary unless the external loop selects them for cleanup.

## Inputs

```text
source.md
status.yaml
```

`status.yaml` contains:

- `presentation_spec`
- `rubric`
- `gap_policy`
- `claim_ledger`
- `notes`

## Status Approval

Before editing, approve the generated `status.yaml` as the working contract.

For each claim, check:

- Does the `span` actually appear in the source?
- Does the normalized `claim` match the span?
- Is the `preservation_test` operational?

Important distinction: `status: asserted` means "extracted from the current draft." It does not mean "approved invariant" until the status file is approved for the editing run.

Once approved, normal editing must not silently change unselected tuple parts.

## External Loop: Select A Tuple Part

At each step, select exactly one active part:

- `text`
- `claim_ledger`
- `presentation_spec`
- `rubric`
- `gap_policy`

The controller should save this decision as a direction file before invoking the editor.

Direction format:

```yaml
direction_id: D003
candidate_id: CAND003
active_part: text
target: "opening paragraphs"
intent: "Move the contextual-competence citation into the opening derivation."
rationale: "The concept does work before its theory source is named."
constraints:
  - "Do not collapse KB and memory into synonyms."
expected_improvement:
  rubric:
    primary_goal: improved
risk:
  touched_claims: [C1, C2, C3]
  failure_modes: []
```

Selection rule:

- Choose `text` when the source can be improved under the current contract.
- Choose `claim_ledger` when a claim is missing, overbroad, badly anchored, duplicated, or no longer matches the source.
- Choose `presentation_spec` when repeated edits damage voice, framing, or rhetorical constraints that are not semantic claims.
- Choose `rubric` when the improvement target is wrong or too vague.
- Choose `gap_policy` when gap markers are ambiguous or the close-in-text vs extract-candidate distinction is failing.

Only the selected part may change inside the internal loop. All other parts are frozen.

Status-part changes can reveal that the current text is no longer valid under the revised contract. Do not solve that by changing status and text in one candidate. Use a coupled cycle: first accept the status candidate, then immediately run a text-alignment candidate against the new status.

## Internal Loop: Propose A Candidate State

The editor proposes one complete candidate state for the selected part. This is deliberately heavier than a diff, because full states are easier for humans to inspect.

Use [editor-prompt](./editor-prompt.md) for this role.

Candidate format:

```yaml
candidate_id: CAND001
direction_id: D001
active_part: text
base_text: memory-derivation.md
base_status: status.yaml
direction_file: directions/D001.yaml
candidate_file: candidates/CAND001.memory-derivation.md
reason: "what rubric goal this improves"

touched_claims:
  - C2
  - C5

gap_action:
  type: none
  marker: null

self_check:
  changes_unselected_parts: false
  adds_new_requirement: false
  changes_claims: false
  changes_architecture_framing: false
  hides_theory_derivation: false
```

For non-text candidates, `active_part` changes and `candidate_file` points to a complete candidate `status.yaml`.

## Coupled Status-Then-Text Cycle

When `active_part` is `claim_ledger`, `presentation_spec`, `rubric`, or `gap_policy`, verification must also answer:

```yaml
requires_followup_text_candidate: true | false
followup_reason: ""
```

Use `requires_followup_text_candidate: true` when accepting the status candidate would make the current source invalid, under-specified, or misleading relative to the revised status file.

Common cases:

- A claim is narrowed, but the text still states the broader version.
- A claim is split, but the text still entangles the two claims.
- A preservation test is sharpened, revealing an ambiguous paragraph.
- A presentation constraint is added, and the text currently violates it.
- A rubric goal is changed, and the current text lacks the required derivation.
- `gap_policy` changes, and the current text has unsupported bridges that now need markers.

The follow-up is not optional cleanup. It is the second half of the same controlled edit cycle:

```text
status candidate -> verify -> accept status -> text-alignment candidate -> verify -> accept/reject text
```

The status candidate and text candidate still have separate candidate IDs, files, verification reports, and acceptance decisions. If the text-alignment candidate fails, keep the accepted status only if the controller is willing to leave the experiment in a known "status ahead of text" state; otherwise revert or amend the status through another explicit candidate.

## Verification

The verifier compares:

```text
old source
old status
candidate source/status
selected active part
```

For v0, check all claims every time. There are few enough that selective verification is unnecessary.

Use [verifier-prompt](./verifier-prompt.md) for this role.

Verification format:

```yaml
verification:
  candidate_id: CAND001
  direction_id: D001
  active_part: text
  direction_file: directions/D001.yaml
  candidate_file: candidates/CAND001.memory-derivation.md

  frozen_parts_unchanged: true

  claim_checks:
    C1: pass
    C2: pass
    C3: pass
    C4: pass
    C5: warn

  presentation_spec:
    preserve_items: pass
    avoid_items: pass

  rubric:
    primary_goal: improved
    secondary_goals:
      contextual_competence_derivation: improved
      retrieval_insufficient: worsened

  gap_policy: pass

  requires_followup_text_candidate: false
  followup_reason: ""

  decision: needs_human_review
  reason: "Candidate improves local derivation but weakens C5 by making retrieval sound like the main interface."
```

## Acceptance Rule

A candidate is accepted only if:

1. No unselected tuple part changes.
2. No claim preservation test fails.
3. No rubric `non_goal` is violated.
4. The candidate improves at least one relevant goal for the active part.
5. It does not worsen a higher-priority goal.
6. Text candidates do not add new requirements unless the active part is `claim_ledger` or a human approves a claim change.
7. Any gap marker follows `gap_policy`.
8. Status candidates that require text alignment declare `requires_followup_text_candidate: true`.

Examples:

- Clearer but changes a claim: reject.
- Shorter but hides theory derivation: reject.
- More polished but violates `presentation_spec`: reject.
- Adds a new requirement during a text edit: reject.
- Marks a real unsupported bridge according to `gap_policy`: accept or human review.

## Update

If accepted:

```text
copy the accepted candidate over the current source.md or status.yaml
append record to edit_log.yaml
append state pointer to history/manifest.yaml
```

Full-state history is mandatory, but it should not duplicate files unnecessarily. Preserve the initial state as `S000` only when the `candidates/` directory is empty. After candidates exist, an accepted state may point to the accepted full candidate file plus the unchanged companion file instead of copying both into `history/`.

State records must make the full state reconstructable:

```text
history/S000.<source-name>.md
history/S000.status.yaml
candidates/CAND001.<source-name>.md
status.yaml
```

The current root files are head pointers and working copies. The history is the manifest plus the initial snapshot and accepted candidate files.

If rejected:

```text
do not change source.md or status.yaml
keep the rejected candidate for inspection
append failure to failure_log.md or rejection-log.yaml
```

The failure log is how v1 earns new structure. Do not add ontology in advance.

## Stop Condition

Use the local `rubric.stop_condition`, plus:

- no claim checks warn or fail,
- primary goal is satisfied,
- remaining candidates are mostly tone polish,
- or three consecutive candidates are rejected.

The last rule prevents open-ended polishing loops.

## Minimal Loop

```text
1. Generate status.yaml from source.md.
2. Human/controller approves status.yaml.
3. External loop selects one active tuple part.
4. Controller writes a direction file for the selected part.
5. Internal loop proposes one complete candidate state for that part.
6. Verify candidate against source.md, status.yaml, frozen tuple parts, and the direction file.
7. Accept, reject, or request human review.
8. If an accepted status candidate requires text alignment, immediately run a `text` candidate against the new status.
9. Log the decision.
10. Repeat until stop condition.
```

The key simplification is not that only text can change. The simplification is that only one tuple part changes at a time, and the choice of part is explicit.
