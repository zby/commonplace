---
type: types/type-spec.md
name: write-brief
description: A document's preface for writers, kept in a sibling file, stating what the document must do for its reader, keep, and exclude; loaded by writers as retained intent
schema: ./write-brief.schema.yaml
---

# Write brief

## Authoring Instructions

Use `write-brief` to record the commission of one document, so that later writers can keep what it was meant to do. A brief is optional. Write one when the commission has boundaries a later writer could not infer from the document itself: passages another artifact relies on, deliberate exclusions, a claim that must not be expanded, decisions reserved for the user. A commission that is only intent, meaning a claim and its reader update, is usually carried by the document's title and opening. Do not add a brief for it.

A brief is a sidecar. It sits next to its target, named `<target-stem>.brief.md`. The target declares it with `brief: <target-stem>.brief.md`. The validator checks that pairing in both directions. A brief never has a brief of its own.

**Force.** A brief binds later writers as intent until a user amends it. Current user direction always prevails. When a request conflicts with the brief, follow the request and state which brief item it amends, then update the brief in the same write, or ask the user when the conflict is not resolvable from the request. Editing a brief affects only the next write of its target. It has no review or freshness consequences.

**Content.** A brief is directive text. Its form follows the directive-text rule in `cp-skill-write`: intent first, then the boundaries every route must respect, with the means left to the writer. Keep it to what the document must do, keep and exclude. Do not copy the document's claims, evidence, outline or prose into the brief. A brief that restates the document drifts from it and adds nothing a writer cannot read in the target.

**Part of its document.** A brief is an integral part of the document it commissions, like a preface written for writers instead of readers. It lives in a sibling file for two reasons only:

- it stays outside the text a write edits, so an edit that drifts cannot rewrite the commission along the way;
- it stays out of the reader's view, so it does not compete with the document's description and body.

In every other respect it goes with the document. Links point to the document, never to the brief. A search that finds the brief has found the document. The brief carries no tags of its own; the document's tags cover it. It moves and retires with the document.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `types/write-brief.md` |
| `description` | Yes | One sentence naming the target and its commission |

`brief:` and `tags:` are forbidden.

## Template

```markdown
---
type: types/write-brief.md
description: "Commission for <target>: <what it must do for its reader, in one sentence>"
---

# Brief: <short target name>

## Intent

<Governing claim or purpose, and what the reader should understand, infer, or do because the document exists.>

## Must keep

- <Passage, distinction, or qualification — and why, e.g. the artifact that relies on it.>

## Must exclude

- <Content the document must not contain or reintroduce — and why.>

## Reserved decisions

- <Choices a later writer must not make without the user.>
```

Omit a section that has nothing in it. A brief that ends up with only `## Intent` should not exist.

---

Relevant Notes:

- [Warranted reader update is the objective of substantive writing](../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — rests-on: the intent section states the reader update the document is organized around
- [Full write briefs cut edit drift; one-line briefs did not](../notes/evidence/full-write-briefs-cut-edit-drift-one-line-briefs-did-not.md) — rests-on: why the must-keep and must-exclude sections carry the brief's value, and why a one-line brief is not enough
