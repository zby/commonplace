---
description: Use this note to classify retained KB artifacts without conflating communicative profile, content kind, production lineage, or path-relative behavioral authority.
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [artifact-analysis, document-system, foundations]
---

# Artifact classification separates profile, content kind, lineage, and authority

A retained artifact in an agent-operated knowledge base should be analyzed through four non-substitutable questions: its communicative profile, the content kind of each material proposition or operative region, that region's production relation, and the behavioral authority of each consumption path. Profile attaches primarily to the artifact under its collection contract. Content kind and production relation may vary within the artifact. Behavioral authority attaches to a path that consumes an operative part. Because the answers attach to different units, none can substitute for the others.

## Four questions

**Communicative profile.** A [profile](./definitions/text-contract.md) is an open, named bundle of text-contract features that organizes an artifact's intended contribution and review priority. Commonplace ships theoretical, descriptive, and prescriptive as defaults, not as exhaustive information kinds or intrinsic file classes. A profile tells an author and reviewer what contribution and quality to seek; it does not determine what every region contains, how that content arose, or what force a consumer gives it.

**Content kind.** A belief is a truth-apt proposition: its truth does not depend on whether the system adopts or retains it. A residual choice is an operative selection among options that the applicable beliefs, requirements, and constraints leave live. Residual does not mean arbitrary; the live options may have different consequences and trade-offs even when the inputs select none uniquely. Ask this question at the level of a material proposition or operative region, since [epistemic status can vary within one document](./mixed-epistemic-status-must-be-preserved-below-the-document-level.md). Belief and residual choice need not exhaust every kind of supporting region.

**Production relation.** Content is [derived](./commitment-not-derivation-creates-new-ground-truth.md) when its source plus the declared consumer goal determines its substantive content. Commitment records an addition those inputs do not determine, such as a generalization, a selected interpretation, or a selection among live options. Lossiness and producer determinism do not decide this relation; the source-plus-goal test does. A change to determining inputs calls for refresh or re-derivation; changing a committed addition requires a later commitment or supersession. Mechanical and judgment-based checks can both verify derivation. [Inheritance as starting warrant](./derivation-and-inheritance-give-starting-warrant-earns-scope.md) answers a different question, not a third production relation.

The content-kind and production questions interact without collapsing. Selecting one of several still-live options adds what the inputs did not determine, so every residual choice entails commitment. The converse fails: an ampliative conjecture, explanation, or generalization can add content and remain a truth-apt belief. Commitment makes the committed region authoritative for what the system retained there; it does not make the belief true or expand its confidence or evidential scope.

**Behavioral authority.** [Behavioral authority](./definitions/behavioral-authority.md) is the consumer, channel, and force through which an operative part shapes behavior. The same belief may advise when retrieved as context and bind when supplied through an instruction path without ceasing to be a belief. Source-of-truth authority for what was retained belongs to lineage; behavioral force belongs to each consumption path. Neither changes the other answers.

## Whole-artifact labels cannot answer all four questions

| Question | Where it attaches | What it distinguishes | Review or maintenance consequence |
|---|---|---|---|
| Communicative profile | Artifact under a collection contract | Intended contribution and review priority | Apply the profile's quality goal |
| Content kind | Material proposition or operative region | Truth-apt belief from residual selection | Test warrant, modality, and scope, or inspect live alternatives and trade-offs |
| Production relation | Material proposition or operative region | Content determined by source and goal from an added commitment | Refresh or re-derive, or supersede by a later commitment |
| Behavioral authority | Consumption path | Consumer, channel, and force | Inspect the actual paths on which stale or wrong content has consequences |

These attachment levels explain why a filename, directory, frontmatter type, sentence mood, canonical status, importance, or declared intent may route an investigation but cannot settle all four questions.

A proposal makes the failure of whole-artifact classification clear. One proposal may contain beliefs, requirements, alternatives, rationale, and candidate selections. Before adoption, a candidate selection is not the system's operative residual choice. Adoption commits the system to the selection, while a report that adoption occurred is a truth-apt historical belief. Commonplace's [proposal placement](../reference/adr/028-design-proposals-live-in-reference-proposals.md) and [proposal-to-decision map](../reference/design-rationale-management.md) are contingent process policies, not another information kind or classification axis.

## Review and maintenance follow the question

The distinctions imply the following layered review; no comparative evidence here establishes that using it improves outcomes. Review first asks whether the artifact meets the contribution-quality goal set by its profile. For a belief, it asks about truth conditions, warrant, modality, counterevidence, and evidence-earned scope. For a residual choice, it asks which requirements and constraints apply, which alternatives remain live, and what consequences or trade-offs follow. Production relation determines whether maintenance should re-derive content or supersede a commitment. Behavioral authority determines which actual consequence-bearing paths need inspection.

Profile alone does not impose a theory-to-prescription-to-implementation-to-description maintenance flow. Change propagates only across an established dependency or lineage relation, and its consequence depends on the force of the affected consumption path.

## Scope

This classification does not claim that belief and residual choice exhaust every supporting region, or that every nominal combination of answers exists. It establishes the interaction needed here: residual choice entails commitment, while a committed addition may remain a belief.
