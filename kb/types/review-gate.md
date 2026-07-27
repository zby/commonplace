---
type: kb/types/type-spec.md
name: review-gate
description: A single quality check the Commonplace review system applies to KB artifacts
schema: kb/types/review-gate.schema.yaml
---

# Review gate

## Authoring Instructions

A review gate is a closed-ended, verdict-kind quality assay. Each gate is one markdown criterion telling a reviewer what failure to seek and how to choose the final decision: PASS, WARN, FAIL, or ERROR. INFO may label a finding in the prose but is not a final decision. Report-kind assays are instructions, not `review-gate` artifacts. The catalog discovers gates at `kb/instructions/review-gates/{lens}/{name}.md`.

## Frontmatter

- `gate_id: {lens}/{name}` — matches the file path under `kb/instructions/review-gates/`.
- `name: {Human-Readable Name}` — used in rendered reviews.
- `lens: {bundle}` — the bundle this gate belongs to (`accessibility`, `semantic`, `structural`, `complexity`, `prose`, `frontmatter`, `sentence`).
- `watches: [body | frontmatter | ...]` — which parts of the target the gate inspects.
- `staleness: changed | always | ...` — when an accepted review becomes stale.
- `description` — the trigger condition: what kind of authoring problem this gate catches.
- `type: kb/types/review-gate.md`.
- Optional `requires_trait` or `requires_type` — narrow the gate to a subset of artifacts that carry the given trait or type.

## Body

- `## Failure mode` — the failure the reviewer is looking for, stated as the concrete pattern that should not appear.
- `## Test` — the procedure for choosing PASS, WARN, FAIL, or ERROR. It may route INFO findings without changing a clean final decision. Name exceptions explicitly so the reviewer does not double-flag adjacent gates.
- Optional `## Example (pass)` and `## Example (fail)` blocks make the test concrete. Most existing gates carry at least one of each — copy their shape rather than reinventing it.
- **The test must be self-contained.** Review freshness hashes only note text and criterion text, so a test that leans on contract text living elsewhere (a type spec, a collection convention) carries a dependency that never invalidates acceptances. If the test needs contract language, quote it in the gate body — that converts the dependency into hashed criterion text, and editing the gate to track a moved contract fires `criterion-changed` through the normal path. Conformance to a type's contract as a whole is not a catalog gate's job: that is the type-conformance pair, whose criterion side is the type spec itself (ADR 038). A gate scoped by `requires_type` owns a sharper, named failure mode and should state its boundary with the conformance pair.

## Force and warrant

A gate is automated problem-noticing, not reject-capable evaluation. Its verdict generates disposition work — fix, reject, or defer, decided downstream — and commit or merge is what retains a change; FAIL is an escalation signal, not an operative blocker. Author the test as a detector for the named failure mode, not as an acceptance authority.

- **Warrant boundary.** The model-judged test is warranted only for the failure mode the gate names, and that warrant is currently uncalibrated. Do not raise a gate's enforcement force (making its verdicts blocking, or auto-acting on them without disposition) before it meets the acceptance criteria in the [calibration proposal](../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md).
- **Judgment outside the freshness hash.** Review freshness hashes note text and criterion text only. Editing a gate's criterion text fires `criterion-changed` through the normal path — but a change that shifts judgment without touching either hashed side (prompt rendering, process scaffolding, judging configuration) leaves accepted baselines silently standing. Such a change owes a deliberate re-review of the affected corpus until freshness can represent that dependency.

## Template

```markdown
---
gate_id: {lens}/{name}
name: {Human-Readable Name}
description: '{What kind of authoring problem this gate catches.}'
type: kb/types/review-gate.md
lens: {lens}
watches: [body]
staleness: changed
---

## Failure mode

{Concrete pattern that should not appear.}

## Test

{Procedure for choosing PASS, WARN, FAIL, or ERROR. INFO may appear only as a finding label. Name exceptions explicitly.}

## Example (fail)

{Minimal failing example.}

## Example (pass)

{Minimal passing example.}
```
