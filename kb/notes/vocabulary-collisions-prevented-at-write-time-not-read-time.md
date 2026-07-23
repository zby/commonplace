---
description: "Unqualified technical senses have no reliable namespace in prose; schema slots, rare compounds, and linked clause frames scope them at write time; audits and remediation recover when prevention fails"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [computational-model]
---

# Load-bearing vocabulary collisions should be prevented or visibly scoped at write time

Technical terms are hard to use in a knowledge base because prose offers no reliable, mechanically enforced namespace for an unqualified technical sense. In the risk model proposed here, a technical sense is **load-bearing** when misresolving it changes what an agent does, which maintenance regime applies, what authority a claim carries, or whether a fallback is licensed. Symbolic systems use scope to keep identifiers apart: two `map`s in different namespaces need not collide, because formal position participates in resolving meaning. Prose has no equivalent: readings are delimited only by grammar and context — conventional, fallible cues. A lexical technical sense without a visible clause frame or schema position therefore binds *globally and weakly*:

- **Globally** — no marker delimits where the binding applies; every co-loaded occurrence of the word is a potential use site of the technical sense.
- **Weakly** — no validator enforces the binding; a reader or an LLM pass can resolve the wrong sense, and nothing necessarily detects the error.

This is the corpus-scale form of a session-scale mechanism: [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) already names collision as a session-scale pathology. At corpus scale the colliding senses live in durable notes written months apart, and the collision can recur whenever the notes are co-loaded.

## The failure is at composition, and it is silent

Context assembly is **concatenation, not import**. A symbolic system resolves name collisions at link time — qualified names, renaming, or a duplicate-symbol error. Concatenated prose has no rename step and no linker error. An agent can read two notes that use one term in different technical senses, blend them, and produce a conclusion that appears to inherit authority from both notes while following from neither. A reader sometimes notices the clash, but that noticing is itself an inference — vulnerable to distance, phrasing, and load — and it emits no error signal when it fails to fire. This is the shape of [prose has no reliable dereference](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md): a formal operation replaced by an inference that may work but cannot be relied on as a control.

The deficit is not inherent to prose as a medium. Books are prose, and books do not suffer this collision problem in practice. What protects a book's vocabulary is not formal scope but a boundary object. Opening a book is a manual act of entering an attentional frame that stays active for the whole reading session; a chemistry textbook's *reduction* never collides with a rhetoric textbook's *reduction* because no reader is inside both books at once. A knowledge base removes that boundary object: retrieval pulls notes across former book-equivalent boundaries with no signal that a crossing happened. The risk, then, is not that prose lacks formal scope — ordinary reading has survived without it for as long as books have existed. It is that KB composition strips away the informal single-source boundary that let prose get away with lacking it, and puts nothing in its place.

`Distillation` — the retired term that named both entailment-preserving reshaping (methodology → skill) and evidence-to-rule generalization (traces → preference rule) — illustrates the stakes. The two operations carry different maintenance regimes: one is checkable against its retained source, the other must earn authority through testing. The bare word marks no boundary between them, so co-loaded notes could blur which regime applies.

## Write-time prevention is the conservative default

Three candidate remedies offer different levels of assurance. Reader vigilance — noticing the clash at read time — is a useful backup but too silent and fallible to be the only control. Symbolic disambiguation — per-note sense declarations ("in this note, X means…") that readers resolve before composing — can work, but it adds work to every read and write, and a missing declaration silently restores the original ambiguity. Write-time prevention or visible scope — reserving each unqualified load-bearing term for one sense across co-loadable artifacts, and placing necessary reuse in a schema slot or linked clause frame — removes the dependence on read-time inference altogether.

Retrieval-time disambiguation looks like a fourth remedy: treat the collision as word-sense disambiguation and let the composer assemble context in which each occurrence resolves correctly. But it decomposes into the first two. Where the retriever resolves senses from declared markers, it is symbolic disambiguation executed mechanically — stronger than leaving declarations to readers, but the declarations must still exist and travel with every excerpt, so writing them is write-time scoping by another name. Where it resolves senses semantically, it is reader vigilance moved into the pipeline: the same silent inference, weakest exactly here. Classic word-sense disambiguation leans on sense inventories a model's priors already know, but a KB's load-bearing senses are local coinages defined in single notes — an excerpt that drops the qualifier leaves only the bare word, and the prior pulls toward the common reading. The assurance a retrieval solution adds is precisely its symbolic, write-time ingredient; the semantic remainder inherits the failure profile of the reader it replaced.

Session-level isolation does not substitute for this, and neither does a retriever that simply keeps colliding notes apart — that only relocates the same move earlier in the pipeline: if a task needs both artifacts, separating them defeats the composition the task requires. The both-notes-needed case rules out *separation*, not co-loading: annotating both notes with sense-distinguishing markers — provenance metadata, sense qualifiers — does make the co-load safe. But that is not a rival remedy; it is visible scope executed as metadata. The markers must be authored before any task needs them and must travel with every excerpt, so the strategy lands exactly where this note already places the burden: at write time. Body-composability needs either a collision-free vocabulary or visible, checkable scope for the technical use, and collection-local vocabulary is reliably safe only when a colliding sense cannot co-load — which a cross-linked KB makes hard to guarantee.

## Devices rank by binding strength

Schema-defined positions offer the strongest scope available: a link-label token, a `tags:` value, a type-spec field, or a frontmatter key can be unambiguous because it occurs in a validator-defined slot. **Position can disambiguate even when spelling alone cannot.** Moving a binding from prose into such a slot is [codification](./definitions/codification.md) applied to vocabulary itself. The prose-level devices rank below it by binding strength:

| Device | Binding | Failure mode |
|---|---|---|
| Definition note + vocabulary entry | Corpus-wide prose convention, not mechanically scoped | Drift or conflicting use |
| "In this note, X means…" | Local declaration, not preserved when excerpted | A citation can lose the qualifier |
| Clausal binding + required link (`actionable`) | Grammar-scoped, link-anchored convention | Mis-predication or a missing link |
| Rare compound token (`trace-learning`) | Distinctive exact string, corpus-auditable | Accidental reuse or jargon opacity |
| Link label / field / tag in a defined slot | Positional, validator-enforced | Schema ambiguity or content misuse |

The two strongest rows compose. A rare hyphenated compound occupying a validator-defined slot is both cheap to audit corpus-wide and mechanically checkable in position — `derived-from` and its siblings, used as link-label relation names, are this composition, with the spaced phrase (`derived from`) left free for ordinary prose. Neither ingredient alone suffices: a bare rare compound still depends on writers keeping it out of unscoped prose, and a slot alone does not stop a common word placed there from dragging in its ordinary associations. At the other end, a definition note by itself is the weakest device — it states a binding but neither enforces nor delimits it.

### Rare compounds make the collision check lexical

The practical default for new internal technical terms is a compound of two or more words. A coinage creates no formal scope; its value is that it changes the *kind* of check collision control requires. Auditing whether a common word already carries a technical sense demands semantic classification of many occurrences; for a rare exact string, `rg` lists the few uses directly, turning most of the audit into a cheap lexical screen with semantic reading reserved for the residue. The component words also constrain each other's reading, offering a partial gloss before the definition loads, and an unfamiliar compound imports fewer established associations than a redefined common word. Fewer is not none: no string is semantically neutral ground — even pseudowords, orthographically legal non-words, elicit form-based meanings that humans and language models converge on ([de Varda et al., 2024](https://aclanthology.org/2024.cl-4.4/)). A coinage does not open a blank namespace entry to be trivially overwritten; it trades a strong established prior for a weak form-driven one. The pre-definition gloss is therefore unavoidable, which is why the component words must be chosen to point it toward the technical sense — they will point somewhere regardless. `Trace-learning` and **discovery lifecycle** carry their technical senses on the searchable compound rather than the common bare words `learning` and `discovery`.

Borrowed terms follow the same risk logic: [context engineering](./definitions/context-engineering.md) is a low-risk borrowing because the local sense aligns with established use, while `distillation` was high-risk because its machine-learning association fails to mark the boundary the KB needed. The cost of coinage is opacity to outsiders — coined terms are banned from outward-facing copy — and each coinage is still a global name every reader carries: the cost side of [the minimum viable vocabulary is the naming set that most reduces](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md).

### Clausal binding is admissible with a required link

A predicate can receive limited grammatical scope: the technical sense is licensed only where the word predicates an explicit subject in the same clause, as with `actionable` in [actionable methodology](./definitions/actionable-methodology.md) — "a methodology is **actionable** for an operator when…". Grammar alone is weaker than a distinctive string: the frame depends entirely on writer discipline, no validator enforces it, and an exact-string search cannot confirm it because every candidate clause needs semantic reading. That is why clausal binding is admissible only with a required definition link. The link does not prevent mis-predication, but it makes each intended technical use visible and spot-checkable — under the convention, an unlinked `actionable` simply has its ordinary reading. A corpus audit on 2026-07-18 found all 36 bare uses of `actionable` across the library to be ordinary ones: exactly the many-innocent-occurrences profile that makes capturing a bare common word dangerous, and evidence the frame convention has held so far.

## The invariant targets load-bearing technical senses

The rule is not "eliminate polysemy" — polysemy is normal in natural language, and a KB that fought all of it would fight its own medium. The target is load-bearing polysemy, and the proposed invariant is:

> A load-bearing sense should be carried by a validator-defined schema position, a rare compound, or a clause-bound predicate whose technical use links to its definition. No unqualified term should carry two load-bearing senses across co-loadable artifacts. Writers should prevent or visibly scope collisions rather than delegate resolution to readers.

Today the invariant is held by writer discipline and manual audits. The candidate mechanical controls — a reserved-term registry, a coinage collision screen in the write path, a naming-review gate, slot-escape linting, and a clausal-binding link check — are collected as a design object in [write-time vocabulary collision controls](../reference/proposals/write-time-vocabulary-collision-controls.md).

## Prevention fails sometimes, so the invariant owes a recovery path

Write-time prevention is a control, not a guarantee. Writers scope terms under incomplete information: the colliding sense may not exist yet when a term is chosen, or the fact that would disambiguate may be missing at authoring time. Some misresolutions will therefore ship despite the invariant, and since [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md), the invariant owes two contingencies beyond prevention:

- **Detection** — a way to attribute a downstream problem to sense misresolution. This is the hard half: by this note's own argument the failure is silent, so detection cannot wait for an error signal. The proven instrument is the corpus audit — sweep a suspect term's occurrences and classify each against its declared sense. A cheaper per-artifact probe — re-deriving a suspect conclusion with each technical term's intended sense spelled out, to see whether the derivation survives — is plausible but untested.
- **Remediation** — once a misresolving term is identified, determine what disambiguating information is missing and put it in place: promote the sense to a stronger device in the ranking, split the senses across distinct terms, or retire the word entirely and rescope its former traffic.

The `distillation` retirement ([ADR 053](../reference/adr/053-retire-distillation-without-a-successor-term.md)) is a worked instance of the full loop: a 464-occurrence audit detected two load-bearing senses with opposite maintenance regimes sharing one word, and remediation retired the term, moved the boundary into lineage link labels, and routed the ampliative traffic to a coined compound — while the definition note that was supposed to hold the binding had existed, impotently, throughout the drift.

## Open Questions

- Do definition notes need a health warning as a type? They can bind *concepts to explanations* safely (what is a term?) but bind *words to senses* only weakly.
- Which of the proposed enforcement mechanisms earns adoption first — and does the deterministic subset (registry uniqueness, slot-escape linting) deliver enough of the invariant to defer the semantic gates?
- Detection of shipped misresolutions currently rides expensive corpus audits triggered by suspicion. Is there a cheaper standing signal — a review criterion, a co-load-time check — that flags sense misresolution before a full audit is warranted?

---

Relevant Notes:

- [Prose has no reliable dereference, so a declared fact must be reinforced where it applies](./prose-has-no-dereference-reinforce-facts-at-point-of-use.md) — contrasts: sibling "prose lacks a formal-language operation" claim (no resolution vs. no reliable namespace)
- [Enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — grounds: the general claim behind the recovery section — detection and blocking without a structured post-failure path leave correction ad hoc
- [Meaning Beyond Lexicality: Capturing Pseudoword Definitions with Language Models (de Varda et al., 2024)](https://aclanthology.org/2024.cl-4.4/) — evidence: even pseudowords elicit convergent form-based meanings from humans and language models, so no coinage lands on semantically neutral ground
