---
description: "An agent can detect a contaminant in its context, refuse to replicate it, and still leak its lean as fine-grained stance drift; excluding a contaminant beats instructing an agent to ignore it"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [llm-interpretation-errors, context-engineering]
---

# Context contamination operates below an agent's compliance reasoning

Content in an agent's context that the agent is instructed not to adopt still shapes what it writes, and it does so **beneath the level at which the agent's explicit compliance reasoning runs**. An agent can notice the contaminant, correctly name it as out-of-contract, refuse to reproduce it — and leak its lean anyway. Detection confers no immunity. The practical consequence is sharp: **excluding a contaminant from context dominates instructing the agent to ignore it**, and no strengthening of the instruction closes the gap.

## What the contamination actually looks like

The intuitive model of contamination — the agent copies the forbidden content, or drops what the contaminant argues against — is wrong, and being wrong about the *form* is what makes the failure hard to gate on.

In a controlled test (four same-model writer agents drafted the same stance-neutral note from identical inputs; two received one context file carrying an implanted own-voice verdict, two did not; a blind judge audited all four against the contract without knowing conditions existed), the contaminated writers copied nothing. No treatment note reproduced the verdict, dropped an objection, or asserted a position in its title. Every gross-grain check passed. The leak was fine-grained and uniformly directional:

- **evaluative lexicon** — a "mere" continued existence, a "naive reading"; absent from the same writer's own properly cited paraphrase of that same argument earlier in the same note;
- **reassuring own-voice glosses** — an objection "narrows but does not close the safety margin", uncited, inside a dependency-analysis section;
- **structural promotion** — a press rebuttal filed under the official review heading, giving the favoured side three sub-entries to the objectors' one;
- **provenance contamination** — the verdict-carrying artifact cited as though it were a source.

The blind judge separated the conditions cleanly and every deviation it flagged leaned toward the implanted verdict. And one treatment writer explicitly detected the verdict section, named it out-of-contract, refused to replicate it — and still leaked the lean into its analysis. That is what "silent" means operationally: not that the agent fails to notice, but that noticing does not help.

## Why instruction cannot fix what exclusion can

The mechanism is inherited from the consumer's architecture rather than chosen, which is what puts it beyond the reach of a better prompt (the [membership test for an inherited constraint](./first-principles-are-inherited-constraints-not-design-choices.md)). [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — the model "has no mechanism to mark a binding as out of scope." Compliance reasoning is *itself just more tokens*: it produces a statement of refusal, and a statement of refusal does not un-condition the distribution the contaminant is already conditioning. The agent can say the right thing about the contaminant while still being steered by it, because saying and being-steered happen at different levels.

This is the content-steering twin of a mechanism already named for privilege: [orchestration needs privilege quarantine, not permission scope](./orchestration-needs-privilege-quarantine-not-permission-scope.md) observes that untrusted content "can steer the call's *judgment* diffusely, without ever appearing as a taggable argument, leaving no variable-level lineage to check" — which is why the boundary has to move to the role level rather than trying to make the per-call check provenance-aware. Same shape here, and the same remedy: move the boundary. Quarantine the contaminant out of the context; do not ask the exposed role to resist it.

It is also the mirror image of [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md). There, *wanted* knowledge sits in context and fails to activate. Here, *unwanted* content sits in context and activates regardless — against an explicit instruction, and against the agent's own stated intent. Both are failures of the same missing control surface: presence in context is neither sufficient for activation nor avoidable by decree.

## Why the gates that pass are the wrong gates

Every gross-grain check passed on contaminated output. That is not a reassuring result about the checks; it is a measurement of their discriminative power on this error class, and it is near zero. [Error correction works above chance oracles with decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) supplies the reason a high aggregate pass-rate proves nothing: an oracle that accepts almost everything has a high accuracy number and no ability to separate the cases that matter. A neutrality gate that checks title form, attribution presence, and objection coverage is such an oracle. To catch this, a gate must target the signature directly — uncited evaluative language, own-voice glosses in synthesis sections, structural asymmetry between sides, and citations of artifacts that are not sources.

## Scope and limits

The direction is established; the magnitude is not. The evidence is a single controlled test — n=2 per condition, one topic, one model family for both writers and judge — and it carries a declared confound: implanting the verdict required deleting the context file's explicit "no position asserted in own voice" sentence, so the *missing reminder* may carry part of the effect rather than the *present verdict*. What survives that confound is the sharpest finding, which does not depend on the comparison at all: a writer that saw the reminder's absence, diagnosed the verdict, and refused it, still drifted.

Two things follow for how far to push this. "The agent will notice and compensate" is refuted **at this dose** — a blatant, explicit, own-voice verdict. Whether subtler contamination produces the same signature, and whether an explicit neutrality reminder inoculates against a *present* verdict rather than merely helping in its absence, are open.

Two naming collisions worth flagging, since both words are load-bearing elsewhere in this KB. The sibling casework calls this signature *register drift*; "register" was retired here as the name for the profile taxonomy ([ADR 042](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md)), so this note says **stance drift** instead. And [flat memory predicts specific cross-contamination failures](./flat-memory-predicts-specific-cross-contamination-failures-that-are.md) uses "contamination" for a disjoint phenomenon — pollution *across memory spaces*, not a stance bleeding into voice within one generation.

## Open Questions

- Dose–response: does accumulated first-person material (rather than an explicit verdict section) produce the same signature at lower intensity, or is there a threshold?
- Does a cross-family judge reproduce the separation, or is some of it same-family sympathy between writer and judge?
- Can the stance-drift signature be gated cheaply, or does detecting it cost as much as writing the note did?

---

Evidence is the "silently averaged" experiment run in the sibling `epistack-casebooks` repository (black-hole case, 2026-07-09): design, blinding protocol, judge report, and unblinded analysis live in that repo's workshop layer.

Relevant Notes:

- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — exemplifies: this note is direct experimental evidence for that architectural claim; the implanted verdict is its "early turn subtly biases a later response" with no out-of-scope marker available
- [Orchestration needs privilege quarantine, not permission scope](./orchestration-needs-privilege-quarantine-not-permission-scope.md) — mechanism: the same diffuse-steering evasion, and the same move-the-boundary remedy, for content rather than privilege
- [First principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md) — grounds: the missing scoping primitive is inherited from the consumer, which is why no instruction is a rival remedy to exclusion
- [Error correction works above chance oracles with decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — grounds: why "every gross check passed" measures the checks' discriminative power rather than the output's cleanliness
- [Agent orchestration needs coordination guarantees, not just capable agents](./agent-orchestration-needs-coordination-guarantees-not-just.md) — grounds: names contamination as the failure mode of composing flat context without a scoping or isolation primitive
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — contrasts: the mirror case — wanted knowledge present and inert, versus unwanted content present and active
- [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — see-also: theorizes interference, but at gross-accuracy grain; this is the sub-threshold variant that detection does not neutralize
