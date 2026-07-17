---
description: "Unqualified technical senses lack a reliable, enforceable prose namespace; schema positions, rare compounds, and linked clause frames make each technical use checkable during writing"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# Collisions among load-bearing technical senses should be prevented or visibly scoped at write time

The difficulty of using technical terms in a knowledge base comes from prose offering no reliable, mechanically enforced namespace for an unqualified technical sense. In the risk model proposed here, a technical sense is **load-bearing** when misresolving it changes what an agent does, which maintenance regime applies, what authority a claim carries, or whether a fallback is licensed. Symbolic systems keep identifiers apart with scope: two `map`s in different namespaces need not collide because formal position participates in resolving meaning. Prose can delimit readings through grammar and context, but those cues are conventional and fallible. In that model, a lexical technical sense without a visible clause frame or schema position therefore binds *globally and weakly*:

- **Globally** — No reliable marker delimits where the binding applies. Absent a clause frame or schema slot, every co-loaded occurrence of the word is a potential use site of the technical sense.
- **Weakly** — No validator enforces the binding. Resolving a sense from context is fallible. A reader or an LLM pass can choose the wrong sense, and nothing necessarily detects the error.

This is the corpus-scale form of a session-scale mechanism. [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — flat concatenation, everything global — already names collision as a pathology: "table" as HTML element in one turn, database table in another. At corpus scale, the colliding senses instead live in durable notes written months apart. A collision can recur whenever two such notes are co-loaded.

## The failure is at composition, and it is silent

An agent may read a note where a term carries one technical sense *together with* a note where it carries another, yet fail to spot the clash. Context assembly is **concatenation, not import**. A symbolic system can resolve name collisions at link time through qualified names, renaming, or a duplicate-symbol error. Concatenated prose offers no built-in rename step or linker error. The reader can blend the senses, producing a conclusion that appears to inherit authority from both notes while following from neither.

Detection is not impossible. An agent sometimes infers that two notes use a term differently when the senses are far enough apart and attention lands on the discrepancy. That inference shares the vulnerabilities of the resolution it would police: sensitivity to distance, phrasing, and load. It may not run, and there is no built-in error signal when it does not. Moreover, the reader doing the detecting is already being steered by the possible blend. This is the shape of [prose has no reliable dereference](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md): dereferencing means reliably resolving a reference to the fact or target it denotes. In prose, that formal operation is replaced by an inference that may work but is not a dependable control.

[Distillation](./definitions/distillation.md)—targeted transformation of recorded material into a use-shaped artifact for a particular downstream consumer—illustrates the collision pattern when one bare word names two operations: entailment-preserving reshaping (methodology → skill) and evidence-to-rule generalization (traces → preference rule). The first produces an artifact that can be checked against its retained source. The second produces a rule that must earn authority through testing. Because the word alone does not mark this maintenance boundary, co-loaded notes can blur which regime applies.

## Write-time collision control is the conservative default

Under this proposed risk model, three candidate remedies offer different levels of assurance:

- **Reader vigilance** — A reader can notice the clash. This remains a useful backup, but a silent and fallible inference is too weak to be the only maintenance control.
- **Symbolic disambiguation** — Writers can declare per-note senses or use qualified terms, and readers can resolve those declarations before composing. This can work, but it adds resolution work to reads and declaration work to writes. A missing declaration leaves the original ambiguity.
- **Write-time prevention or visible scope** — Writers can reserve each unqualified load-bearing term for one sense across co-loadable artifacts. When reuse is necessary, they can place the technical use in a schema slot or a linked clause frame. These controls reduce dependence on read-time inference.

For artifacts designed to be co-loaded, session-level isolation through code-constructed sub-agent frames does not always transfer. If a task needs both artifacts, sandboxing them apart defeats the composition the task requires. Body-composability therefore needs either a collision-free vocabulary or visible, checkable scope for the technical use. A vocabulary policy should treat collision handling as work performed during writing. Collection-local vocabulary is reliably safe only when a colliding sense cannot co-load, which is difficult to guarantee in a cross-linked KB. A distinctive coinage or explicit scope is easier to check.

## Schema position provides mechanically enforced scope

Schema-defined positions offer the strongest scope available in this KB. A link-label token, a `tags:` value, a type-spec field, or a frontmatter key can be unambiguous because it occurs in a validator-defined slot. **Position can disambiguate even when spelling alone cannot.** A schema assigns meanings to positions, while validators and gates keep occurrences in those positions. Moving a binding from prose into such a slot is [codification](./definitions/codification.md) applied to vocabulary itself.

This ranks prose-level naming devices by binding strength:

| Device | Binding | Failure mode |
|---|---|---|
| Definition note + vocabulary entry | Corpus-wide prose convention, not mechanically scoped | Drift or conflicting use |
| "In this note, X means…" | Local declaration, not preserved when excerpted | A citation can lose the qualifier |
| Clausal binding + required link (`actionable`) | Grammar-scoped, link-anchored convention | Mis-predication or a missing link |
| Rare compound token (`trace-learning`) | Distinctive exact string, corpus-auditable | Accidental reuse or jargon opacity |
| Link label / field / tag in a defined slot | Positional, validator-enforced | Schema ambiguity or content misuse |

By itself, a definition note is the weakest device in this comparison. It states a binding, but nothing mechanically enforces or delimits it. A definition that assigns `distillation` to both entailment-shaped reshaping and ampliative generalization would document that collision without enforcing or delimiting either sense.

## Rare multi-word coinages make collision checks cheaper

One practical default for new internal technical terms is to use two or more words. A coinage does not create formal scope. Its advantage is that a rare exact string has fewer unrelated uses to inspect and fewer established associations to overcome. Three mechanisms support the rule:

1. **Few incidental occurrences.** A rare exact string produces fewer unrelated matches during a vocabulary check. Redefining a common word also brings its ordinary associations into every use. An unfamiliar compound begins with fewer established associations for the KB to overcome.
2. **Mutual constraint.** Each word can narrow the other's reading. A descriptive compound may therefore offer a reader a partial gloss even before the definition is loaded. This can reduce misresolution as well as collision.
3. **Exact-string rarity makes the invariant searchable.** Checking whether a common word already carries a technical sense requires semantic classification of many occurrences. Checking `distillation`, for example, would require a semantic audit across its uses. For a rare compound, an exact-string search with `rg`, the ripgrep text-search command, can list the current uses with far less noise. This turns much of the check into a cheap lexical screen, with semantic review reserved for the remaining matches.

`Trace-extracted`, `trace-learning`, and **discovery lifecycle** illustrate the rule. Each technical sense rides on the full compound rather than on the common bare words `extracted`, `learning`, or `discovery`, making the technical token directly searchable.

Existing associations may help or hurt. In this risk model, [context engineering](./definitions/context-engineering.md)—the discipline of routing, loading, scoping, and maintaining knowledge under bounded context—is a lower-risk borrowing when the local sense aligns with established use. `Distillation` is a higher-risk name for entailment-preserving textual reshaping because its machine-learning sense concerns training a student model from a teacher's outputs. That association does not distinguish textual reshaping from evidence-to-rule generalization.

The cost is opacity to outsiders, which is why coined terms are banned from outward-facing copy. Inside the KB, the trade is often worthwhile when a compound is descriptive enough to suggest its role. This supplies the cost side of [the minimum viable vocabulary is the naming set that most reduces](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md). Prose names without reliable scope can affect any co-loaded note, so each term has a corpus-wide maintenance cost. Keeping terms in their defined slots applies [constraining](./definitions/constraining.md)—narrowing the space of valid interpretations an artifact admits—to naming.

## The invariant targets load-bearing technical senses

The rule is not "eliminate polysemy." Polysemy is normal in natural language, and readers resolve it constantly. A KB that tried to eliminate all of it would fight its own medium. The target is **load-bearing polysemy**. Misresolving such a sense changes what an agent does, which maintenance regime applies, what authority a claim carries, or whether a fallback is licensed. The proposed invariant is:

> A load-bearing sense should be carried by a validator-defined schema position, a rare compound, or a clause-bound predicate whose technical use links to its definition. No unqualified term should carry two load-bearing senses across co-loadable artifacts. Writers should prevent or visibly scope collisions rather than delegate resolution to readers.

## Clausal binding is a weaker scoping device, admissible with a required link

A predicate can receive a limited grammatical scope: the technical sense is licensed only where the word predicates an explicit subject in the same clause. `actionable` illustrates this in [actionable methodology](./definitions/actionable-methodology.md): "a methodology is **actionable** for an operator when…" The same word can describe a finding, edit, step, or piece of guidance in ordinary English. Under the linked definition's convention, those uses do not invoke the technical relation unless they enter the methodology-predicate frame and carry the definition link.

Grammar alone is weaker than a distinctive exact string. A clause-bound predicate depends on writer discipline. Writers must reserve the designated subject-predicate relation for the technical sense. They must avoid using the ordinary sense in that same frame. Every technical use must also carry the required link. No validator currently enforces these choices. An exact-string search cannot confirm them because each candidate clause needs semantic reading.

That is why this note admits clausal binding only with a required definition link. The link does not prevent mis-predication. It makes the intended technical use visible and spot-checkable. Under this convention, an unlinked "actionable" has its ordinary reading; only the linked methodology-predicate frame invokes the technical relation. Grammar supplies limited scope, while the required link supplies the check. This is a proposed writing rule, not a claim that a validator already enforces it.

## Boundary and caveats

Three further limits apply. First, minimality still matters. Compounds are cheaper to keep apart, not cheaper to *learn*, and each is still a global name the reader carries. Second, an existing community association helps only when the KB sense agrees with it. Borrowing a term against that association re-creates the capture problem on a smaller scale. Third, clausal binding's required link is currently a writing convention rather than a validator-enforced gate. Nothing yet checks that every technical predication carries the link. Until such a check exists, this device provides write-time discipline rather than mechanical write-time enforcement.

## Open Questions

- Should the proposed one-term-one-sense invariant get mechanical write-time enforcement through a sense-collision check or naming-review gate?
- Should linked clausal binding get separate enforcement that checks whether a technical predication carries its definition link?
- Do definition notes need a health warning as a type? They can bind *concepts to explanations* safely (what is a term?) but bind *words to senses* only weakly.

---

Relevant Notes:

- [Prose has no reliable dereference, so a declared fact must be reinforced where it applies](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — contrasts: sibling "prose lacks a formal-language operation" claim (no resolution vs. no reliable namespace)
