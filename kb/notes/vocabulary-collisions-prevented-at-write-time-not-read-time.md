---
description: "Prose has no scope, so co-loaded notes merge colliding senses of a term silently; the reliable fix is corpus-wide sense uniqueness enforced at write time, favouring multi-word coinages."
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# Vocabulary collisions are prevented at write time, not resolved at read time

The difficulty of using technical terms in a knowledge base comes from prose having no scoping mechanism. Symbolic systems keep identifiers apart with scope: two `map`s in different namespaces never collide, because meaning is resolved by position in a formal structure, not by spelling. Prose has no such device. A technical sense declared anywhere binds *globally and weakly*:

- **Globally** — nothing delimits where the binding applies. Every future occurrence of the word, in any note, by any writer, is a potential use site of the technical sense.
- **Weakly** — nothing enforces the binding. Sense resolution happens by context, which is probabilistic; a reader or an LLM pass can resolve wrong, and nothing detects it.

This is the corpus-scale form of a session-scale mechanism. [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — flat concatenation, everything global — already names collision as a pathology: "table" as HTML element in one turn, database table in another. At corpus scale the colliding senses live not in one session's turns but in durable notes written months apart, and the collision reactivates every time two are co-loaded.

## The failure is at composition, and it is silent

An agent reads a note where a term carries one technical sense *together with* a note where it carries a different one, and has no reliable way to spot the clash. Context assembly is **concatenation, not import**. A symbolic system resolves name collisions at link time — qualified names, renaming, or a duplicate-symbol error. Concatenated prose has no rename step and no linker error: the two senses merge by default, and conclusions drawn from the blend inherit authority from both notes while following from neither.

Detection is not impossible — the agent sometimes infers that two notes use the term differently, when the senses are far enough apart and attention lands on the discrepancy. But that inference has the same failure profile as the resolution it would police — sensitive to distance, phrasing, and load, with no guarantee it runs and no error signal when it doesn't — and the reader that must do the detecting is the same reader being steered by the blend. This is the shape of [prose has no reliable dereference](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md): the formal operation is replaced by an inference that often works and can never be relied on.

The concrete case is this KB's own "distillation." By mid-2026 it meant entailment-preserving reshaping (methodology → skill) in some notes and evidence-to-rule generalization (traces → preference rule) in others — senses with opposite maintenance semantics: a reshaped artifact is recomputable from its retained source, while an extracted rule must earn authority through testing. The two senses co-loaded routinely, were flagged by no in-context reading, and were caught only by a deliberate whole-corpus audit of 464 occurrences.

## Prevention, not scoping, is the remedy

Three candidate remedies exist, and they are not symmetric:

- **Reader vigilance** — rely on the agent noticing the clash. It sometimes does; but a probabilistic, silently-failing inference is not a mechanism, and a maintenance regime cannot rest on it. This is the do-nothing option wearing a safety argument.
- **Symbolic disambiguation** — per-note sense declarations, namespaced terms, readers instructed to resolve senses before composing. Buildable, and very complex: it taxes every read with resolution work and every write with declarations, and its own failure mode — one missing declaration — reproduces the original problem.
- **Prevention** — never let two technical senses of one term exist: **one term, one sense, corpus-wide.** Enforced at write time, it needs no read-time luck at all — best-effort inference can stay a bonus safety net rather than a load-bearing check.

At corpus scale, prevention also wins by elimination: the session-scale architectural remedy — code-constructed sub-agent frames — does not transfer, because notes exist to be co-loaded, and you cannot sandbox apart two artifacts the task needs together. Sense uniqueness is therefore a precondition for body-composability: composition is only sound over a collision-free vocabulary. A vocabulary policy must read "collision handling" as collision *prevention* — a uniqueness invariant across every source that can co-load. Collection-local vocabulary is safe only for terms that cannot co-load with a colliding sense (hard to guarantee — cross-collection linking exists precisely to co-load) or are coined so collision is impossible.

## Scope in a KB is position in a schema

The precise sense in which only the symbolic layer can keep senses apart: a link-label token, a `tags:` value, a type-spec field, a frontmatter key are unambiguous not because of their spelling but because they occur only in validator-defined slots. **Position disambiguates; spelling never has to.** The symbolic layer has scope because a schema assigns meanings to positions, and enforcement — validators, gates — keeps occurrences in their positions. Moving a binding from prose into such a slot is [codification](./definitions/codification.md) applied to vocabulary itself, and the enforced positions are what give that layer its scope at all.

This ranks prose-level naming devices by binding strength:

| Device | Binding | Failure mode |
|---|---|---|
| definition note + vocabulary entry | global, unenforced prose convention | drift |
| "in this note, X means…" | locally declared, decays at the note boundary | citations strip the qualifier |
| coined compound token (`trace-learning`) | no scope needed — no collision possible | jargon opacity |
| link label / field / tag in defined slot | positional, validator-enforced | none at the term level (misuse is a content error, catchable by gates) |

A definition note is the weakest device: it states a binding but nothing enforces or delimits it — the KB's `distillation` definition existed throughout the drift it failed to prevent, and its own instance list ended up spanning the colliding senses.

## Multi-word coinages are the enforcement-friendly naming rule

The practical default for technical terms is to use two or more words. A coined compound is collision-free not because it is scoped but because nothing else occupies it — for an LLM reader, **the tokenizer's prior is the actual namespace**. Three mechanisms make the rule work:

1. **Low prior — few innocent occurrences.** Collision chance tracks how often the exact string arises innocently in ordinary prose: a captured common word arises constantly, a coinage essentially never. And where a technical redefinition of a common word fights the model's distributional prior at every occurrence, a coinage arrives with an empty prior the KB fills entirely — a high-entropy identifier, the same reason long symbol names survive a flat namespace.
2. **Mutual constraint — partial self-definition.** Each word narrows the other's reading, so the compound half-carries its meaning even to a reader who never saw the definition. This attacks misresolution, not just collision.
3. **Exact-string rarity — the uniqueness invariant becomes greppable.** Checking "does this term already carry a technical sense?" for a captured common word means sense-classifying every occurrence — auditing "distillation" for rename took a multi-agent semantic classification of all 464 hits. For a rare compound, one `rg` over the exact string finds all uses and nothing else: write-time prevention drops from semantic audit to lexical search, converting the enforcement problem into one the symbolic layer can actually run.

The rule in use: when this KB freed "derived" for ordinary English, the infrastructure vocabulary moved to coined compounds — `trace-extracted` for artifact lineage, `trace-learning` for the learning loop — and when the same migration needed a technical home for staged ampliative acceptance it adopted the compound **discovery lifecycle** rather than loading the bare word "discovery." The borrowed-prior contrast runs both ways: "context engineering" holds as a KB term because the KB's sense agrees with the community's, while "distillation" was borrowed *against* its prior — ML knowledge distillation is statistical fitting, not entailment-preserving reshaping, so the imported intuition sat on the wrong side of the very boundary the KB sense needed to hold.

The cost is opacity to outsiders, which is why coined terms are banned from outward-facing copy. Inside the KB the trade is usually right: a compound that is *descriptive* almost self-defines and buys collision-freedom nearly for free. This supplies the cost side of the case that [the minimum viable vocabulary is the naming set that most reduces](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md): prose names are unscoped globals, so each one taxes the whole corpus, not just the notes that use it — and enforcement, keeping terms in their slots, is [methodology enforcement as constraining](./methodology-enforcement-is-constraining.md) applied to naming.

## Boundary and caveats

The rule is not "eliminate polysemy." Polysemy is normal in natural language and readers resolve it constantly; a KB that tried to eliminate it would fight its own medium. The problem is specifically **load-bearing polysemy**: senses whose misresolution changes what an agent does — which maintenance regime applies, what authority a claim carries, whether a fallback is licensed. The invariant is:

> A load-bearing sense must be carried by a scoped surface (label, field, tag) or an empty-prior token (coined compound) — never by capturing a common word. And no term may carry two load-bearing senses anywhere in the corpus: collisions are prevented at write time, not resolved at read time.

Two further limits. Minimality still applies — compounds are cheap to keep apart, not cheap to *learn*; each is still a global the reader carries. And a compound with an existing community prior is safe only when the KB sense agrees with that prior; borrowing against the prior re-creates capture in miniature.

## Open Questions

- Should the one-term-one-sense invariant get write-time enforcement — extending a write skill's cheap duplicate check to a sense-collision check, or a naming-review gate? Prevention is only as good as the check that runs at write time.
- Do definition notes need a health warning as a type? They can bind *concepts to explanations* safely (what is a term?) but bind *words to senses* only weakly; the definitions that have held are mostly coined-or-rare words, which may be why.
- The philosophy-borrowing angle — formal languages were invented precisely because natural language lacks scope discipline (Frege's *Begriffsschrift*) — is probably cite-in-passing only.

---

Relevant Notes:

- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — grounds: the session-scale statement of the mechanism, whose name-collision pathology is this note's failure mode and whose sub-agent remedy is the one that does not transfer to co-loaded library artifacts
- [prose has no reliable dereference, so a declared fact must be reinforced where it applies](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — contrasts: sibling "prose lacks a formal-language operation" claim (no resolution vs no boundaries)
- [minimum viable vocabulary is the naming set that most reduces](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — extends: supplies the cost mechanism (names as unscoped globals) to its payoff argument
- [codification](./definitions/codification.md) — mechanism: moving a binding from prose to schema is the codification crossing applied to vocabulary itself
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — grounds: enforced positions are what give the symbolic layer its scope
