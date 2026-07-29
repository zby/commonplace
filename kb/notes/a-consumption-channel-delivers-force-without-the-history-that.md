---
description: "A consumption path can promote content into a higher-force role without checking whether an authorization covers that content, version, and use"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [failure-modes, artifact-analysis, self-improving-systems]
---

# A consumption channel delivers force without the history that earned it

[Behavioral authority](./definitions/behavioral-authority.md) attaches to a consumption path — a consumer, a channel, and a force — not to the bytes of an artifact. That precision has a converse consequence: whatever reaches the path receives its force unless the path checks whether the promotion is authorized. Here, *earned* means that an explicit authorization covers the content, its version, the role it will occupy, and the use being made of it. It does not mean that the content is guaranteed true.

This boundary makes a writable self-representation an attack surface rather than a maintenance chore. If [retrieval is the wire a self-representation acts along](./retrieval-failure-is-reflection-failure.md), one failure occurs when search finds nothing and a represented constraint stays inert. Here, the wire works: it delivers content into a high-force position without a matching authorization transition.

## Two ways in, one boundary

The adversarial case is familiar. Content reaches a channel that treats it as instruction: a poisoned rule file, a memory written from a compromised tool result, or text in retrieved material that reads as a directive. In an [LLM context, instruction and data share one token medium](./llm-context-is-a-homoiconic-medium.md); typed envelopes help only when the consumer preserves their distinction. This is the indirect-prompt-injection failure [Greshake et al. identify in LLM-integrated applications](../sources/where-it-lives-retained-adaptation-2026-06-23.md), where an application “blurs the line between data and instructions.”

The innocent case has no attacker at all:

- A model distils a false rule from a misleading trace and writes it into a standing instruction file.
- A commitment keeps binding after its grounds change because [only a later commitment displaces it](./commitment-not-derivation-creates-new-ground-truth.md).
- An extractor writes a candidate observation that a later reader treats as checked, although [memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md).

The runtime attack and the persistent false rule are different mechanisms with a shared boundary. The runtime case crosses from untrusted data into an instruction-bearing role during interpretation; the persistent case crosses through admission or lifecycle governance. In both cases, content occupies an operative position without an authorization that covers the transition. The cases therefore share a diagnostic question, not a complete control plan.

This distinction predicts incomplete defences. For persistent artifacts, controlling who may write without checking what was written admits authorized errors, while reviewing content without enforcing the reviewed entrance leaves a bypass. Ephemeral inputs additionally require consumption-side controls such as trust-tiered loading, instruction/data isolation, constrained capabilities, or a [privilege quarantine](./orchestration-needs-privilege-quarantine-not-permission-scope.md).

## Nor is it a wrong verdict

The boundary is also distinct from an evaluation gate that ran and erred. [False-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) describes an evaluator passing something it should have rejected. Its correction path is a stronger oracle — the mechanism that assesses the candidate — and [warranted autonomy is bounded by what that oracle can assess](./warranted-autonomy-is-bounded-by-oracle-domain.md). Those arguments assume the candidate went through the gate.

The failure here is that the channel does not necessarily check gate membership. Strengthening the oracle does nothing about a path that bypasses it. Conversely, a false positive may carry valid procedural authorization without carrying substantive truth. Authorization binding and oracle quality are therefore separate design problems, even though both can end in bad content acting.

## Control must bind authorization to force

Controls can act at several distinct points along the boundary. They work together only when the system binds their state to the exact content consumed:

- **Runtime separation** prevents untrusted content from silently becoming instruction or gaining privileged capabilities during a call.
- **Write authority** restricts which paths may place persistent content in an operative position.
- **Review** grants procedural authorization for a particular content version and scope; it does not establish infallibility.
- **Consumption enforcement and provenance** make the channel verify that the authorization matches the version and use before conferring force. Provenance is evidence for that decision, not the decision itself.
- **Rollback** withdraws future force after detection. It is recovery rather than prevention, and it remains a [sovereignty capability](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) because the owner must be able to restore or regenerate the artifact.

A channel closes the boundary only when every route to an operative position is subject to a mechanical rule that checks the relevant authorization state. A signed artifact, a trust-tiered loader, or a store whose sole write path binds approval to a content digest can supply that rule. Merely recording provenance or performing review somewhere upstream cannot.

This boundary belongs inside a [reflective architecture](./definitions/reflective-system.md): when operative artifacts are the self-representation, editing one modifies the system, so admission and consumption paths are part of the causal connection. Closing these paths is not free. Provenance can spend context, entrance controls spend throughput, and review spends evaluation capacity. Which controls are justified depends on the channel's force and deployment risk.

## The cure states a claim of its own

Authorization metadata inherits the same problem. A verified flag or approved status is itself content in a trusted position, so a stale or unbacked mark can suppress the check that would have caught it. A [derived copy of recomputable truth must therefore be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md), while a non-recomputable attestation must be invalidated whenever its scope may no longer hold. This KB applies the latter rule to `user-verified`: a substantive edit strips the human attestation, and only another explicit act restores it.

---

Relevant Notes:

- [System-definition artifact](./definitions/system-definition-artifact.md) — defined-in: the high-force family whose binding force is what gets misassigned
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — mechanism: explains why instruction and data can share a representation before the consumer assigns their roles
- [Agent orchestration needs a privilege quarantine, not just a permission scope](./orchestration-needs-privilege-quarantine-not-permission-scope.md) — extends: develops runtime separation for attacker-reachable content into a role architecture
- [The four-field record exposes an efficiency, security, and sovereignty risk triad](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) — grounds: states the security question as the authority-plus-lineage conjunction this note develops into a boundary, and supplies rollback as a sovereignty capability
