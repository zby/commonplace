# Speech Acts

## Candidate borrowing

Speech-act theory distinguishes utterances by what they do, not only by what they say: asserting, requesting, committing, directing, declaring, warning. For commonplace, this maps to document types. A type should encode the action an artifact performs in the KB, not its subject matter.

## Why it fits

The KB already says document types should be verifiable structural properties, not topics. Speech acts may sharpen the reason: documents are not passive containers. They change the state of the work.

Examples:

| Artifact | KB action |
|---|---|
| note | asserts or frames a reusable claim |
| structured-claim | argues a claim with evidence and reasoning |
| instruction | directs future agent behavior |
| ADR | commits the system to a decision |
| review | challenges an artifact and records findings |
| index | routes navigation |
| task | requests or tracks action |

This is close to "types mark affordances," but speech acts may give a better vocabulary for why the affordance exists.

## Possible operational form

Use speech-act questions when defining or reviewing types:

1. What action does this artifact perform in the KB?
2. Who is the consumer of that action: agent, maintainer, script, future reviewer?
3. What state transition should the artifact license?
4. What structural evidence lets the consumer trust that the action was performed?

For example, an ADR should not just be "about architecture"; it should record an accepted decision and license future agents to treat that decision as binding until superseded.

## Existing connections

- [Document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — speech acts may explain why subject-matter types are weak: they do not say what the artifact does
- [Instructions are typed callables](../../notes/instructions-are-typed-callables.md) — strongest local analogue: artifacts have callable operations and affordances
- [Types give agents structural hints before opening documents](../../notes/types-give-agents-structural-hints-before-opening-documents.md) — speech-act type semantics should improve those hints
- [Type system rationalization](../type-system-rationalization/README.md) — existing workshop that settled the current base-type + trait model

## Failure mode

The risk is creating a second type taxonomy that competes with the implemented one. The useful move is not to rename every type as a philosophical act. It is to add a design question for future type definitions: "what does this artifact do?"

## What would make this worth promoting?

Promote this if it helps resolve ambiguous type proposals or improves type instructions. A small addition to type-template guidance may be enough; it does not need to become a standalone theory note unless it changes multiple type decisions.
