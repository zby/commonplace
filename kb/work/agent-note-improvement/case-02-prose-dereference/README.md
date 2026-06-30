# Case 02: prose has no dereference

Target note: `kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md`

## Frozen material

- [baseline-working-tree](./baseline-working-tree.md) — copied from the current working tree on 2026-06-16. The source note already had uncommitted modifications before this experiment.

## Experiment log

### 2026-06-16: split and rehome critique, then apply locally

Instruction under test: [case 01 split/rehome instruction](../case-01-llm-generation-relaxes-goals/instruction-split-rehome-critique.md).

Critique report: [split-rehome-critique-report](./split-rehome-critique-report.md).

Revised local copy: [revised-split-rehome](./revised-split-rehome.md).

Result: no meaningful split. The critique found that the note is already mostly one argument. The applied revision keeps the core dereference/denormalize/check chain, narrows the code single-source claim to mechanical dereference, compresses the conditional-cost discussion, and tightens the empirical testing section.

Takeaway: the split/rehome instruction does not force splitting when the note does not need it. It still helps by identifying that the right edit is local tightening rather than branch removal.

### 2026-06-16: original critique-note

Instruction under test: `kb/instructions/critique-note.md`.

Report: [critique-note-report](./critique-note-report.md).

Result: useful challenge, mostly additive.

What it found:

- It attacked the note's code/prose contrast by arguing that salience, governing frames, and type contracts may propagate facts without literal repetition.
- It distinguished propagation failure from specification failure: if `status: seedling` has underspecified consequences, repetition may duplicate ambiguity.
- It challenged the check claim by noting that validators can check literal copies more easily than derived semantic consequences.

Takeaway: this critique surfaces real precision gaps, especially fact-vs-consequence and literal-vs-semantic checking. As in case 01, its natural repair path tends toward adding distinctions rather than producing a concise edited note.

### 2026-06-16: prune weak expansions

Instruction under test: [case 01 prune instruction](../case-01-llm-generation-relaxes-goals/instruction-prune-weak-expansions.md).

Report: [prune-weak-expansions-report](./prune-weak-expansions-report.md).

Result: strong fit.

What it found:

- It identified the same retained claim as the split/rehome critique: prose lacks reliable propagation, so reinforce locally and check centrally.
- It recommended compression rather than splitting.
- It flagged the same high-value edits: narrow code to mechanical dereference, clarify fact versus consequence, compress conditional branching, and tighten the testing section.

Takeaway: for this note, prune weak expansions is better than split/rehome because the note has no real branch inventory. It produces an edit direction very close to the local revised copy.

## Comparison

| Method | Main result | Fit for this note |
|---|---|---|
| `critique-note` | Finds conceptual objections and missing distinctions. | Useful for pressure-testing, but tends to add apparatus. |
| split/rehome | Correctly says not to split and recommends tightening. | Good negative signal: no branch should be rehomed. |
| prune weak expansions | Recommends compression and precision, not branch removal. | Best fit for applying edits to this note. |

## Applied Draft Comparison

### 2026-06-16: critique-note application

Applied draft: [revised-from-critique-note](./revised-from-critique-note.md).

Result: strongest conceptual refinement, weakest compression.

Strengths:

- Narrows the claim to the actual risk case: distant, non-obvious, consequence-heavy applications.
- Introduces "nearest reliable control point" instead of treating point-of-use repetition as the only repair.
- Separates literal restatement from consequence restatement, with different checking requirements.
- Adds useful costs missing from the baseline: local overfitting and consequence drift.
- Improves the ablation by comparing frontmatter-only, artifact-level banner, and local point-of-use reinforcement.

Costs:

- Grows from 44 lines to 57 lines.
- Adds enough apparatus that the note becomes less sharp as a single operational rule.
- The title still says "point of use," while the body generalizes to "nearest reliable control point"; either the title or body would need harmonizing before promotion.

### 2026-06-16: prune weak expansions application

Applied draft: [revised-from-prune-weak-expansions](./revised-from-prune-weak-expansions.md).

Result: best edited-note shape.

Strengths:

- Keeps the same 44-line length as the baseline while making the code/prose contrast more precise.
- Narrows "single-source" to mechanical dereference without adding a new theory branch.
- Adds the nearest reliable control point phrase while preserving the note's original flow.
- Tightens conditional branching and testing without changing the note's argumentative footprint.

Costs:

- Mentions literal fact versus interpreted consequence, but does not carry the distinction into the checking rule strongly enough.
- Keeps the simpler two-arm ablation and misses the useful artifact-level-banner middle case from the critique-note draft.
- Leaves the validator/check paragraph a little too literal for consequence restatements.

### Interim judgment

For this note, the best next draft would start from [revised-from-prune-weak-expansions](./revised-from-prune-weak-expansions.md) and borrow two ideas from [revised-from-critique-note](./revised-from-critique-note.md):

- the literal-restatement versus consequence-restatement distinction;
- the three-way test: frontmatter-only, artifact-level banner, local point-of-use reinforcement.

This supports the broader workshop pattern: `critique-note` is good at discovering missing distinctions, while `prune weak expansions` is better at producing a usable edited note.

### 2026-06-16: semantic bundle and application

Semantic review run: `2304`.

Review output: [semantic-review-run-2304](./semantic-review-run-2304.md).

Applied draft: [revised-from-semantic-review-2304](./revised-from-semantic-review-2304.md).

Gate results:

| Gate | Result | Scope/redundancy signal |
|---|---|---|
| `semantic/completeness-boundary-cases` | PASS | Treats the scope gradient as useful boundary handling. |
| `semantic/explanatory-reach` | PASS | Treats the current explanation and testing section as sufficient. |
| `semantic/grounding-alignment` | PASS + INFO | Only actionable issue: footer relation to the checked-copy note is synthetic rather than direct evidence. |
| `semantic/internal-consistency` | PASS | Says the scope section is consistent with title and body. |
| `semantic/load-bearing-qualifiers` | PASS | Explicitly says the scope material is not redundant and prevents overextension. |

Applied result: the semantic-review application changed only the footer relation for `a derived copy of recomputable truth must be checked or absent`, from `exemplifies` to `extends`, and left the `Scope` section unchanged.

Gate-gap conclusion: the current semantic bundle does **not** catch the human-obvious redundancy that the `Scope` section repeats an already obvious boundary. Worse, `semantic/load-bearing-qualifiers` positively defends the section because it checks whether qualifiers are necessary for truth, not whether an explicit scope paragraph adds marginal value beyond what the argument already made.

Candidate new gate shape:

- Failure mode: a boundary, caveat, or scope paragraph is true and consistent but adds no marginal constraint because the body already establishes it.
- Test: delete the paragraph mentally; if the note's claim, falsifiability, and likely misreadings are unchanged, warn for obvious boundary redundancy.
- Suggested action: delete, fold one phrase into the relevant paragraph, or keep only when it blocks a likely misread that the body does not already block.

### 2026-06-16: draft marginal-value redundancy gate

Draft gate: [marginal-value-redundancy](../compression/marginal-value-redundancy.md).

Trial report: [marginal-value-redundancy-report](./marginal-value-redundancy-report.md).

Result: partial success.

What improved over the semantic bundle:

- The gate is universal rather than scope-specific: it checks any section, paragraph, list item, example, table row, or Relevant Notes entry for marginal value.
- It catches the `Scope` section as a likely marginal-value problem.
- It applies the intended deletion test: standalone `Scope` repeats the formal-system/prose contrast and distance/non-obviousness condition already established earlier.
- It recommends the right edit shape: fold the useful representational-form gradient into the main mechanism instead of keeping a standalone recap.

Remaining issue:

- The result was `INFO`, not `WARN`, because the reviewer found one useful boundary inside the section. This may be the right behavior if the gate distinguishes delete from fold, but it also shows the threshold needs precision: a standalone unit can deserve a WARN even when one phrase inside it should be salvaged.

Next gate revision hypothesis:

- WARN when a unit should not remain as a unit, even if a small part should be folded elsewhere.
- INFO when the reviewer is unsure whether the unit serves reader orientation or deliberate reinforcement.
- PASS only when the unit's current placement and size are justified, not merely when it contains one useful distinction.

### 2026-06-16: strengthened marginal-value redundancy gate

Updated draft gate: [marginal-value-redundancy](../compression/marginal-value-redundancy.md).

Second trial report: [marginal-value-redundancy-report-v2](./marginal-value-redundancy-report-v2.md).

Result: success on this case.

Gate change:

- Added an explicit compression bias: agent-written notes tend to accumulate defensible detail, caveats, and recap paragraphs.
- Changed the threshold so a unit gets WARN when it should not remain as a unit, even if one phrase inside it should be folded elsewhere.
- Restricted INFO to genuine uncertainty, not "contains one useful phrase."
- Required PASS to mean the unit earns its current placement and size.

Trial result:

- Overall result changed from INFO to WARN.
- `Scope` changed from INFO to WARN.
- Suggested revision became: delete `## Scope` as a standalone section and fold the representational-form gradient into the earlier mechanism paragraph.

Takeaway: for agent note improvement, redundancy gates should lean toward compression. Truth and consistency are too weak; the question is whether the unit earns its current context cost.

### 2026-06-16: output discipline check

Gate change: [marginal-value-redundancy](../compression/marginal-value-redundancy.md) now says to report WARN/INFO findings for chunks that need attention and avoid PASS-per-chunk output.

Third trial report: [marginal-value-redundancy-report-v3](./marginal-value-redundancy-report-v3.md).

Result: success.

- Overall result: WARN.
- Scope status: WARN.
- Report shape: one actionable WARN finding, no PASS-per-chunk output.
- Report length dropped from 18 lines in v2 to 13 lines in v3.

Takeaway: for open-ended compression gates, one overall PASS summary is enough when the artifact passes; when it warns, the report should focus on actionable compression targets.
