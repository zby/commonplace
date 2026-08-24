---
description: "Tertiary vocabulary evidence that 'monkey patch' names runtime class or module modification as a workaround and carries warnings about incompatibility, conflicts, hidden behavior, and patch warfare"
source: https://en.wikipedia.org/wiki/Monkey_patch
captured: "2026-08-19"
capture: web-fetch
genre: conceptual-essay
snapshot_sha256: 1474a84a716fd4bb84d49465755b24d5c15649db5e66098550cbdc4a7414ac45
ingested: "2026-08-19"
type: kb/sources/types/ingest-report.md
domains: [monkey-patching, runtime-modification, domain-pricing]
---

# Ingest: Monkey patch

## Classification

A collaboratively edited encyclopedia entry that defines a programming term, reports its proposed etymology and language-specific usage, and organizes cited operational warnings rather than presenting original research or a controlled comparison.
Author: Wikipedia contributors synthesize community and secondary sources. This is useful evidence that the vocabulary and warnings are publicly established, but it is tertiary and carries less authority about any one language community's norms than that community's own documentation or a usage study.

## Summary

The article defines monkey patching as modifying a dynamic language's runtime code rather than its source, including adding or replacing methods, classes, attributes, and functions in memory. In Ruby, Python, and some other languages, it narrows the term to runtime modification of a class or module to work around an undesired bug or feature in third-party code. The proposed etymology traces *monkey patch* to *guerrilla patch*: a sneaky runtime change that may be incompatible with other patches, later renamed to sound less forceful. Its pitfalls make the warning content concrete: upgrades may break a patch; multiple patches of one method overwrite one another; runtime behavior can diverge from the source developers inspect; and malicious patches can attack programs or other patches, producing an escalating conflict that calls for platform intervention. The article also limits the inference: monkey patching has sometimes been an official extension mechanism, and comparable runtime class changes may be called *hot fixes* in other communities.

## Claims

No claims have been grounded yet.

## Connections Found

This entry is vocabulary evidence for the pejorative-or-warning-name signature in [Domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md): the name's reported ancestry already associates the practice with stealth and incompatibility, while the pitfalls attach maintenance, coordination, and security costs to it. It also supports the narrower statement in [Instantiation alone cannot model agent learning across sessions](../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) that runtime class mutation can carry the warning name *monkey-patching*. The [Metaobject Protocols ingest](./metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md) and [Fast properties in V8 ingest](./fast-properties-in-v8.ingest.md) attest different signatures in the same pricing bundle: a marked meta-level interface and a runtime optimization charge, respectively. This article attests naming and community warning, not either mechanism.

## Extractable Value

1. **The name carries an exceptional-path story.** The article hedges the derivation with “seems,” but its account starts from *guerrilla patch*: code changed sneakily at runtime and possibly incompatibly with other patches. The later *monkey* substitution softens the force without removing the association with an irregular intervention. [quick-win]
2. **The term can target definition-side mutation specifically.** For Ruby, Python, and other languages, the entry reserves *monkey patch* for runtime modification of a class or module undertaken to patch third-party behavior. That is closer to changing shared definition machinery than to ordinary instance-state mutation. [quick-win]
3. **An ordinary-looking operation can cross the runtime/source boundary.** The Python example uses a normal assignment to replace `math.pi` in memory, yet the article classifies the act by its effect on runtime code and notes that restarting restores the source-defined value. Surface syntax alone therefore does not reveal whether an operation changes definition-side runtime behavior. [just-a-reference]
4. **Upgrade and composition costs make the warning operational.** A new upstream release may invalidate the patch, while two patches of the same method compete so that only the last survives unless authors coordinate around a special pattern. The costs are not merely aesthetic disapproval: they arise from coupling to another component's unstated runtime structure and from ungoverned composition at a shared mutation point. [deep-dive]
5. **The source/runtime discrepancy imposes an epistemic cost.** The `Confusion` warning says the code developers read can disagree with actual behavior. A monkey patch can therefore hide the operative definition from the normal source-of-truth surface, complicating debugging and responsibility assignment. [deep-dive]
6. **The `Chaos` example supplies moral-hazard-like framing without using that term.** The article describes malicious patch code, defensive counter-patches, sabotage, and eventual Mozilla policy intervention. It presents an actor benefiting by externalizing debugging and coordination costs onto users and other maintainers, but “moral hazard” is our characterization of that structure, not Wikipedia's phrase. [just-a-reference]
7. **The warning name is domain-relative rather than universal.** The article says monkey patching has sometimes been an official extension method and that Zope and Plone call security-oriented dynamic class changes *hot fixes*. This bounds the pricing claim: a name marks the path only in communities and contexts that actually use it with warning force. [deep-dive]

## Limitations (our opinion)

Wikipedia is a mutable tertiary synthesis. The article shows that the term, etymological story, and warning categories are established enough to document, but it does not measure practitioner sentiment, usage frequency, or the prevalence and effect size of monkey patches. Its etymology is explicitly hedged and rests chiefly on a cited Plone glossary. The source therefore supports a vocabulary attestation, not the stronger claim that all practicing communities uniformly regard every runtime class change as pejorative or exceptional.

The article's normative force is mixed. It labels a section `Pitfalls` and derives the term from a sneaky, possibly incompatible intervention, but it does not simply condemn the technique: it records official extension uses, conditional patches, special coordination patterns, and alternate names such as *hot fixes*. The Python example also mutates a module attribute rather than demonstrating a class or method patch with production consequences. It shows how ordinary assignment can change runtime behavior, not that ordinary syntax always masks class-definition mutation.

Finally, the source never uses *moral hazard*. Its `Chaos` case supports an interpretation in which a patch author can externalize risks and provoke patch warfare, but that economic framing is ours and should not be quoted as community terminology. As [Domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) requires, even a well-supported warning name supplies only routing evidence. It does not establish that reflective mutation is rare, bounded, or negligible for the declared use.

## Recommended Next Action

In a separate note-edit pass, add `evidenced-by` citations from the two connected notes to this snapshot, using it narrowly for the documented term, proposed *guerrilla patch* etymology, runtime class/module scope, and listed pitfalls—not for universal community condemnation, literal “moral hazard” wording, or idealization adequacy.
