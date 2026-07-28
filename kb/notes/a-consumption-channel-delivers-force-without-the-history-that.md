---
description: "Injected instructions and honestly distilled but false rules fail as one boundary: force is conferred by position in a consumption path, so authority no gate granted acts exactly like authority a gate did"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [failure-modes, artifact-analysis, self-improving-systems]
---

# A consumption channel delivers force without the history that earned it

[Behavioral authority](./definitions/behavioral-authority.md) attaches to a consumption path — a consumer, a channel, and a force — not to the bytes of an artifact. That is usually stated as a precision gain: it stops you calling a Markdown file low-authority just because it is prose. It also has a consequence that cuts the other way. If force comes from the path, then whatever sits in the path gets the force, and the path does not ask how the content got there. An artifact can become operative carrying authority its consumer assigns but that nothing about the artifact earned.

This is a distinct failure boundary, and it is the one that makes a writable self-representation an attack surface rather than a maintenance chore. Where [retrieval is the wire a self-representation acts along](./retrieval-failure-is-reflection-failure.md), the failure there is that the search finds nothing and a represented constraint stays inert. Here the wire works perfectly. It finds an artifact, delivers it into a high-force position, and the consumer does what it says — and the trust that made it act is trust the artifact never acquired.

## Two ways in, one boundary

The adversarial case is familiar. Content reaches a channel that treats it as instruction: a poisoned rule file, a memory written from a compromised tool result, text in retrieved material that reads as a directive. Natural language supplies the opening, since it has no artifact-internal separation of data from instruction — the indirect-prompt-injection failure Greshake et al. (2023) identify in LLM-integrated applications, where an application "blurs the line between data and instructions."

The innocent case has no attacker at all:

- A model distils a rule from an episode that did not happen the way the trace suggests, and the rule is written into a standing instruction file.
- A commitment that was right when made keeps binding later work after its grounds changed. Nothing downstream re-derives it, because [what a commitment adds was never recoverable from its source](./commitment-not-derivation-creates-new-ground-truth.md) — only a later commitment displaces it, and none has been made.
- An automatic extractor writes a candidate observation, and a reader later grants it the weight of a checked rule. [Memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md); an unverified diagnosis is a guess with a confident tone.

These look like different problems — one is security, the others are quality — and they are usually staffed by different concerns. On this boundary they are the same event. In each, an artifact occupies an operative position, and the position confers force regardless of whether the content passed anything. The channel has no field for "how this got here," so it cannot behave differently toward the two.

That is worth stating plainly because it predicts an incomplete defence in both directions. Controlling who may write, without any check on what gets written, admits every honest error an authorized writer makes. Reviewing content well, without controlling the entrance, leaves a path into the channel that review never sees. Neither half is optional if the boundary is the thing you are closing.

## Not a wrong verdict, either

The boundary is also distinct from a gate that ran and erred. [False-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) describes an evaluator passing something it should have rejected; the correction path is a stronger oracle, and [warranted autonomy is bounded by what an oracle can assess](./warranted-autonomy-is-bounded-by-oracle-domain.md). Both arguments assume the candidate went through the gate.

The failure here is that gate membership is not a property the channel reads. An artifact that never faced an evaluator and one that passed a strong evaluator arrive at the consumer indistinguishable. Strengthening the oracle does nothing about a write path that does not route through it — which is why the two are separate design problems even though both end in a bad artifact acting.

## The countermeasures are all the same move

Provenance, write authority, review, and rollback are usually listed as repository hygiene. Read against this boundary they are one operation applied at four points: putting the artifact's history back into the channel that would otherwise deliver force without it.

- **Provenance** makes the history readable at consumption time, so a consumer can weigh it. It is the only one of the four that acts on the consuming call itself.
- **Write authority** narrows which paths can place content in an operative position — the entrance-side fix, and the one that decides whether the other three ever get a chance.
- **Review** is what actually earns the force; without it provenance records only that something arrived.
- **Rollback** withdraws force already conferred. It is the only remedy available once the artifact has been operative, and it is a [sovereignty capability](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) — it requires that the owner can still regenerate or restore the artifact, which an externally-held one may not permit.

Where all four hold for a channel, the boundary is closed for that channel by construction rather than by vigilance: a [system-definition artifact](./definitions/system-definition-artifact.md) can only get into an instruction, enforcement, or routing position by a path that recorded and checked it. Where they do not, prose that anyone can write is prose that anyone can make binding. That is why this sits inside the [reflective architecture](./definitions/reflective-system.md) rather than beside it — when the operative artifacts *are* the self-representation, editing one is modifying the system, and the write path is part of the causal connection.

Closing the boundary is not free, and the costs land on scarce resources: provenance fields spend context on every consumption, entrance control spends throughput, and review spends the evaluation capacity that was already the binding constraint. The claim is that the boundary exists and what closes it, not that every channel should pay full price.

## The cure states a claim of its own

Re-coupling history to the channel produces an artifact that asserts *this was earned* — a provenance field, a verified flag, an approved status. That assertion is itself content in a trusted position, and it inherits the problem it was introduced to fix: a stale or unbacked mark tells a consumer to skip the check that would have caught it. So it falls under the rule that [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — enforce the mark or omit it, because a trusted mark with nothing behind it is worse than none.

This KB's own `user-verified` field is the case worth holding in mind, and it is handled the hard way: the attestation is a human commitment nothing recomputes, so a substantive edit must strip it and only an explicit act can re-grant it. The discipline is not a check that the flag is true; it is a rule that mechanically destroys the flag whenever it might have stopped being true.

## Scope

- The claim is about channels that do not carry history, not about channels in general. A signed artifact, a trust-tiered loader, or a store whose only write path runs through validation puts history back in the channel — that is the fix, not a counterexample, and it holds only for the channel so equipped.
- Force being channel-conferred does not mean all channels are equally dangerous. It means danger is read off the channel rather than the artifact: an advisory note pinned into every prompt can be a higher-force position than a formal policy nothing loads.
- Nothing here says the two cases are equally likely or equally severe, only that a defence addressing one leaves the other open. Which dominates is a property of the deployment.

## Open Questions

- Is there anything that detects unearned authority from the consuming side alone — a signal in how an artifact is written or how it interacts with neighbours — or is entrance-side control the only place the boundary can be closed?
- Provenance is the countermeasure that costs context on every consumption. Is there a cheap encoding that survives context pressure, or does entrance control always dominate on cost?
- Rollback assumes you can identify what a wrongly-authorized artifact influenced while it was operative. In a retrieval-mediated system with no record of which artifacts entered which calls, what does withdrawing force actually recover?

---

Relevant Notes:

- [Behavioral authority](./definitions/behavioral-authority.md) — defined-in: supplies the consumer/channel/force decomposition whose path-relativity this note reads as a failure surface
- [System-definition artifact](./definitions/system-definition-artifact.md) — defined-in: the high-force family whose binding force is what gets misassigned
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — contrasts: the sibling failure where the wire finds nothing, against this one where the wire works and delivers unearned trust
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — contrasts: a gate that ran and erred, against content that reached the channel without facing a gate
- [Trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — grounds: the earning ladder whose rung the channel does not read
- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: why a stale commitment keeps binding force and only supersession displaces it
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the oracle-side bound this note holds fixed while attacking the write paths that bypass it
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: why the provenance mark introduced as the cure must itself be enforced or omitted
- [The four-field record exposes an efficiency, security, and sovereignty risk triad](./the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) — grounds: states the security question as the authority-plus-lineage conjunction this note develops into a boundary, and supplies rollback as a sovereignty capability
- [Reflective system](./definitions/reflective-system.md) — grounds: the causal connection that makes a write to an operative artifact a modification of the system
