# Minimal Writing State Template

Use this template for early trials. Keep it sparse. The point is to expose accidental semantic drift, not to fully model the text.

```yaml
state_id:
source:
created:
text_version: v0

presentation_spec:
  voice:
  register:
  avoid:
  preserve:

rubric:
  primary_goal:
  secondary_goals:
  non_goals:
  stop_condition:

gap_policy:
  close_in_text:
  extract_candidate:
  mark_format:

claim_ledger:
  - id: C1
    status: asserted
    span: ""
    claim: ""
    preservation_test: ""
```

## Field guidance

`presentation_spec.voice` names the intended sound. Use concrete contrast pairs when possible: "plain but not flattened", "technical but not academicized", "opinionated but not promotional".

`presentation_spec.avoid` names presentation damage to watch for: generic smoothing, hiding derivation, hedging every claim, corporate polish, inflated transitions, stock "not just X" rhetoric.

`presentation_spec.preserve` names rhetorical or framing commitments that should remain visible even when the exact wording changes. This is broader than voice but weaker than the claim ledger: it protects how the argument is presented, not what the text is allowed to claim.

`rubric.primary_goal` should be one sentence. If the goal is vague, the edit will optimize toward generic polish.

`rubric.non_goals` prevents local improvement from becoming drift. Examples: "do not make this more balanced", "do not soften the critique", "do not add examples unless requested".

`rubric.stop_condition` states when further editing should stop. Example: "Stop after the text is easier to scan and no claim-preservation warnings remain; do not keep polishing."

`claim_ledger.span` should quote the smallest source span that anchors the claim.

`claim_ledger.preservation_test` should name the specific forbidden movement. Examples:

- "Fails if the edit implies structure is sufficient by itself rather than a control surface."
- "Fails if lazy extraction becomes a claim that evidence/caveats are unnecessary."
- "Fails if 'locally improving but not convergent' becomes 'LLM edits are bad'."

## Typed edit record

Append one of these records after each accepted edit.

```yaml
edit_history:
  - id: E1
    type: text
    request: ""
    accepted: true
    claim_changes: []
    rubric_changes: []
    presentation_changes: []
    notes: ""
```

For claim edits:

```yaml
edit_history:
  - id: E2
    type: claim
    request: ""
    accepted: true
    claim_changes:
      - claim_id: C3
        operation: weaken
        before: ""
        after: ""
        reason: ""
```

Valid claim operations for trials:

- `add`
- `remove`
- `weaken`
- `strengthen`
- `merge`
- `split`
- `reanchor`
- `retire`

## Initial state for the workshop claim

This is a seed example based on the workshop framing, not a universal schema.

```yaml
presentation_spec:
  voice: "direct, methodological, careful about overclaiming"
  register: "workshop-theoretical"
  avoid:
    - "generic AI-product framing"
    - "complete ontology language"
    - "unqualified claims that structure solves writing"
  preserve:
    - "bitter-lesson caution"
    - "lazy extraction discipline"
    - "claims may change, but only explicitly"

rubric:
  primary_goal: "Make the argument testable as an editing protocol."
  secondary_goals:
    - "Keep claims auditable."
    - "Separate control surfaces from scalable learning mechanisms."
    - "Prefer observed failures over speculative ontology expansion."
  non_goals:
    - "Do not design a full writing ontology."
    - "Do not claim claim ledgers are the true engine of intelligence."
  stop_condition: "Stop when the protocol can run a small trial and the claim ledger catches accidental drift."

gap_policy:
  close_in_text: "Use when the gap is a missing local inference, transition, or qualification that the draft can state without creating a new reusable theory."
  extract_candidate: "Use when the gap is a reusable theoretical claim, missing definition, missing mechanism, or unresolved tension that should probably become its own note."
  mark_format: "Use inline TODO-style markers during experiments: [GAP close-in-text: ...] or [GAP extract-candidate: ...]."

claim_ledger:
  - id: C1
    status: asserted
    span: "many editing operations are locally improving but not convergent"
    claim: "Some LLM-assisted editing prompts improve local prose while failing to converge under repetition."
    preservation_test: "Fails if revised into a blanket claim that LLM editing is ineffective."
  - id: C2
    status: asserted
    span: "claims should not change accidentally"
    claim: "Claim changes should require an explicit claim-revision step."
    preservation_test: "Fails if text edits are allowed to alter claims implicitly."
  - id: C3
    status: asserted
    span: "lazy extraction"
    claim: "The state should start with minimal anchored claims and add structure only in response to observed editing failures."
    preservation_test: "Fails if the protocol requires eager extraction of evidence, assumptions, caveats, examples, or discourse roles."
  - id: C4
    status: asserted
    span: "human-facing control surfaces, not as the true engine of intelligence"
    claim: "Explicit structure is for auditability and control, while scalable improvement should come from search, comparison, feedback, evaluators, and edit history."
    preservation_test: "Fails if structure is presented as a complete handcrafted model of writing intelligence."
```
