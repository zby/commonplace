# Protocol

## Hypotheses

**H1: Drift reduction.** A sparse anchored claim ledger reduces accidental claim changes over repeated editing passes.

**H2: Convergence.** Typed edits produce a clearer stopping condition than ordinary prompts because "improvement" is evaluated against an explicit rubric and claim-preservation check.

**H3: Lazy extraction beats eager ontology.** Starting with claims only will reveal which extra structures are actually needed. Adding assumptions, evidence, caveats, or examples before observing failures will create false invariants and unnecessary overhead.

## Materials

Each trial needs:

- A source text of 300-1500 words.
- An ordinary-edit baseline prompt.
- A stateful-edit prompt using [state-template](./state-template.md).
- Three to five repeated edit passes for each condition.
- A human or agent scorer that compares each pass to the initial claim ledger.

Prefer source texts with real argumentative content, not generic marketing copy. Good first candidates are workshop drafts, speculative notes, or source-review paragraphs where nuance matters.

## Conditions

### Baseline

Run repeated ordinary editing prompts:

```text
Revise this text to make it clearer and more concise while preserving the author's meaning and voice.
```

Then feed the revised text into the same prompt again for the next pass.

### Stateful

Use the [v0 two-loop algorithm](./v0-two-loop-algorithm.md):

1. Build the initial status file from the source text using [state-template](./state-template.md).
2. Approve the status file as the editing contract.
3. External loop selects exactly one tuple part: `text`, `claim_ledger`, `presentation_spec`, `rubric`, or `gap_policy`.
4. Internal loop proposes one complete candidate state for that selected part.
5. Verify the candidate against the frozen tuple parts.
6. Accept, reject, or send warning-level cases to human review.

Default typed request:

```text
Select one active tuple part and propose one complete candidate state for that part only. Preserve all unselected tuple parts. Verify the candidate against claim preservation tests, presentation_spec, rubric, and gap_policy. Return the candidate file and verification report.
```

## Minimal claim extraction

Extract only claims that a later edit could plausibly distort. Do not extract every sentence. Do not infer hidden premises unless the text itself makes them operationally important.

Each claim gets:

- `id`
- `status`: asserted, implied, candidate, disputed, or retired
- `span`: exact quoted anchor from the source text
- `claim`: normalized paraphrase
- `preservation_test`: what would count as accidental change

Status meanings:

- **asserted** — the text commits to this.
- **implied** — the text relies on this, but less directly.
- **candidate** — plausible but not yet stable; do not freeze it.
- **disputed** — intentionally contested or unresolved.
- **retired** — removed through explicit claim edit.

## Scoring

Score each pass on separate axes:

| Axis | Question | Scale |
|---|---|---|
| Claim preservation | Did asserted/implied claims survive unchanged? | pass / minor drift / major drift |
| Claim auditability | Are any claim changes explicit and inspectable? | pass / unclear / fail |
| Local quality | Is the text clearer, tighter, or better organized? | worse / neutral / better |
| Voice preservation | Does the text still sound like the intended author/style? | worse / neutral / better |
| Generic smoothing | Did the edit replace specific content with generic polish? | none / mild / severe |
| Ontology pressure | Did the model invent structure or false invariants? | none / mild / severe |

## Failure classes

Log failures in [failure-log](./failure-log.md) using these initial classes:

- **semantic drift** — a claim changes without a claim edit.
- **specificity loss** — concrete wording becomes generic.
- **voice damage** — style becomes flatter, more corporate, or less authorial.
- **false invariant** — extracted structure freezes an interpretation the text did not commit to.
- **over-extraction** — the model creates too many ledger entries for practical use.
- **rubric capture** — the edit optimizes for a rubric item while making the piece worse.
- **anchor mismatch** — the claim is not tied to the right text span.
- **revision blockage** — the ledger prevents a genuinely good structural rewrite.

## Generalization rule

Do not add a new state field because it seems theoretically complete. Add one only when:

1. A trial produces a repeated failure.
2. The failure would likely have been prevented by a specific field.
3. The field can be extracted conservatively.
4. The field has a clear acceptance or rejection test.

Candidate additions should be trial-scoped first. Promote them into the template only after repeated use.

## First trial plan

1. Select one short KB-adjacent draft with 5-10 meaningful claims.
2. Run three baseline passes and three stateful passes.
3. Score all six outputs against the initial claim ledger.
4. Record every failure, including overhead and annoyance.
5. Decide whether the next trial needs evidence, caveats, examples, or presentation-state changes.
