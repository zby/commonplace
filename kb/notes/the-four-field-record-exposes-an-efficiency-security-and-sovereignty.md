---
description: The four artifact-analysis fields exist to surface three architectural review concerns over retained behavior — efficiency, security, and sovereignty — with sovereignty (owner control to inspect, regenerate, delete, roll back) as the new axis
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [learning-theory, artifact-analysis]
status: current
---

# The four-field record exposes an efficiency, security, and sovereignty risk triad

The four fields of [artifact analysis](./axes-of-artifact-analysis.md) — [storage substrate](./definitions/storage-substrate.md), [representational form](./definitions/representational-form.md), [lineage](./definitions/lineage.md), and [behavioral authority](./definitions/behavioral-authority.md) — read like descriptive bookkeeping: where retained behavior lives, how it is encoded, what it derives from, and with what force it acts. But the reason to keep all four visible is not completeness for its own sake. The record exists to surface three recurring architectural review concerns over retained behavior-shaping artifacts: **efficiency**, **security**, and **sovereignty**. Each concern is a question you can only ask once two of the fields are recorded; collapse the fields back into a storage label and the question disappears.

## The triad, field by field

**Efficiency risk** is a representational-form plus behavioral-authority question. It appears when a retained lesson stays in a recurring prompt or retrieval path — paid in tokens, latency, and context bloat on every consumption — even though it could be compressed into a cheaper symbolic check, schema, test, or workflow that runs once and stops competing for context. You cannot see this risk from substrate alone: the same prose reflection in a file and a validator in the same repo have identical substrate but opposite efficiency profiles. You see it only when the form (prose, interpreted each time) is read against the authority path (loaded into every prompt). The cure is the [codification](./definitions/codification.md) move — change the form, not the location — and it only pays when authority is recurring and high-frequency. This is the most general framing of why [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md): recurring prose authority is the default leak.

**Security risk** is a behavioral-authority plus lineage question. It appears when an untrusted or poisoned artifact enters a high-authority channel, or when a stale derived view survives a source change and keeps governing behavior. Prose carries a specific vulnerability here: it blurs the line between data and instruction, so retrieved content can act as instruction the architect never authorized — the indirect-prompt-injection failure Greshake et al. (2023) identify in LLM-integrated applications. The authority field names which channels are high-force (instruction, enforcement, routing); the lineage field names which derived artifacts can drift from a fixed source. The security question is the conjunction: *does anything untrusted, or anything stale, reach a high-authority channel?* Neither field answers it alone.

**Sovereignty risk** is a storage-substrate plus representational-form question. It appears when behavior depends on artifacts the system owner cannot inspect, regenerate, delete, or roll back — vendor checkpoints, hosted retrieval indexes, externally-managed model state. Define sovereignty as exactly that owner capability: the ability to **inspect, regenerate, delete, and roll back** retained behavior. Those are the same four verbs lineage and storage-substrate already track — but read as an ownership and control concern rather than a maintenance concern. Lineage asks "can the *system* regenerate this when its source changes?"; sovereignty asks "can the *owner* regenerate it at all, or does that capability live with a vendor?" The verbs are shared; the question shifts from internal upkeep to external dependence.

## Sovereignty is the load-bearing new content

Efficiency and security already appear scattered across the artifact-analysis cluster — efficiency in the form/authority cost arguments, security in the prompt-injection and stale-derived-view discussions. Sovereignty does not. It is the genuinely new axis the triad adds, and it is worth stating because it explains a failure the other two miss: a system can be efficient (cheap symbolic checks) and secure (no untrusted input, no stale views) and still be unable to inspect, regenerate, delete, or roll back the artifacts its behavior depends on, because those artifacts are hosted and owned elsewhere. The digital-sovereignty literature treats this as control over the artifacts a system depends on (Couture and Toupin, 2019; Dale, 2025); the four-field record localizes it to substrate and form.

The inspection-method story interacts sharply with sovereignty. Form sets the default inspection method — read prose, test or statically check symbolic artifacts, behaviorally probe distributed-parametric ones (and [opacity is a scale threshold, not a class property](./opacity-is-a-scale-threshold.md), so even prose can pass that threshold). Distributed-parametric form is the hardest to inspect; an externally-hosted substrate is the hardest to own. Their conjunction — distributed-parametric state on a vendor substrate, such as a closed hosted checkpoint or a managed embedding index — is the worst case on both axes at once: you can neither read what it encodes nor regenerate or delete the thing encoding it. This is why [inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) is also a sovereignty argument: choosing a readable, owner-regenerable form buys back both inspection and control.

## Why this matters

The triad turns the four-field record from a classification scheme into a review checklist. For any retained artifact, the architect asks three questions whose terms the fields supply: is its form-and-authority pair leaking recurring cost (efficiency); does anything untrusted or stale reach a high-authority channel (security); can the owner inspect, regenerate, delete, and roll back it (sovereignty). The fields were always the answer to "how does this artifact act?" The triad names the three things you were trying to find out when you asked.

This synthesis is refined beyond what the notes held: the KB's own ASIS&S 2026 position paper sharpened the triad framing — especially the sovereignty axis — and that refinement flows back here into the notes, rather than the notes deriving from the paper.

## Open Questions

- Sovereignty and lineage share the same four verbs (inspect, regenerate, delete, roll back) read under different ownership assumptions. Is sovereignty a distinct field, or a lens on the substrate/lineage pair worth promoting to a definition only if it earns repeated use?
- The triad is presented as covering the recurring concerns, but the position paper calls the field set non-exhaustive. Are there review concerns (auditability, fairness, cost attribution) that need a fourth member rather than folding into these three?

---

Relevant Notes:

- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — extends: the four fields exist to surface the efficiency/security/sovereignty triad, not just to describe artifacts
- [storage substrate](./definitions/storage-substrate.md) — defined-in: sovereignty's externally-hosted worst case is a substrate property
- [representational form](./definitions/representational-form.md) — defined-in: form fixes both the efficiency cost and the inspection method that sovereignty depends on
- [lineage](./definitions/lineage.md) — defined-in: security's stale-derived-view mode and sovereignty's regenerate/roll-back verbs are lineage concerns read differently
- [behavioral authority](./definitions/behavioral-authority.md) — defined-in: efficiency and security both turn on which channel carries high force
- [codification](./definitions/codification.md) — mechanism: the efficiency cure is a prose-to-symbolic form change, not a relocation
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: recurring prose authority is the default efficiency leak the triad names
- [Opacity is a scale threshold, not a class property](./opacity-is-a-scale-threshold.md) — mechanism: distributed-parametric form is hardest to inspect, compounding sovereignty when hosted
- [inspectable artifact, not supervision, defeats the blackbox problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — extends: choosing a readable owner-regenerable form is also a sovereignty move
