---
description: "The Deutsch-derived quality property is carried corpus-wide by the rare compound explanatory-reach; bare reach returns to ordinary English, with two note retitles and one brainstorming rename"
type: ../types/adr.md
tags: []
status: accepted
---

# 055-Explanatory-reach replaces bare reach as the technical term

**Status:** accepted
**Date:** 2026-07-23

## Context

`Reach` — the Deutsch-derived property that an explanation keeps working beyond the cases that produced it — was one of the KB's most load-bearing technical senses: the declared quality goal of `kb/notes/` (COLLECTION.md, collection tables, tag READMEs), the axis of the learning-theory decomposition (facts low, theories high), and the property the review gate `semantic/explanatory-reach` and the reach-assessment cluster judge. Yet it rode on a bare common English word. A corpus sweep found roughly 950 occurrences of the word across the KB, the overwhelming majority ordinary English (verbs, "out of reach", "reach the consumer") interleaved with the technical sense in the same collections — exactly the many-innocent-occurrences profile [the write-time collision rule](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) marks as dangerous for a captured common word, and the audit shape that made the `distillation` retirement ([ADR 053](./053-retire-distillation-without-a-successor-term.md)) expensive.

The remediation was already half-registered: the [reach-assessment definition](../../notes/definitions/reach-assessment.md) had reserved the rare compounds **reach-assessment** (the capability) and **explanatory-reach** (the judged property), declared bare *reach* free of technical sense in its cluster, and renamed the neighbouring limits to **oracle domain** and **search range**. But the declaration did not yet hold corpus-wide: note titles, the brainstorming note, and the `kb/notes/` quality-goal declaration still carried the sense on the bare or spaced word.

## Decision

Promote **explanatory-reach** — hyphenated, one greppable token — to the sole carrier of the technical sense, corpus-wide. Bare "reach" returns to ordinary English everywhere.

- **One spelling.** The hyphenated compound is used in titles, descriptions, headings, tables, and prose alike; the spaced form "explanatory reach" is not a permitted variant, so a single exact-string search audits the vocabulary. Graded uses keep the compound intact: attributive modifiers hyphenate through ("high-explanatory-reach changes"), and predicate or noun uses grade it with a spaced adverbial ("high explanatory-reach", "low explanatory-reach") — the former "high-reach"/"low-reach" shorthands are retired with the bare word.
- **Registered surfaces carry the compound.** The `AGENTS.md` vocabulary, `kb/notes/COLLECTION.md`'s quality goal, the collection tables, and the `semantic/explanatory-reach` gate's display name use it.
- **Titles follow the vocabulary.** A note title that carries the technical sense uses the compound.
- **Deutsch's own term survives as a mention.** Attribution sites ("Deutsch's 'reach'", "his term is bare 'reach'") keep the bare word in quotes as the borrowed source term, immediately paired with the registered compound.
- **Untouched:** ordinary-English uses (verbs, idioms, "reach the consumer"-style delivery phrasing), captured sources (`kb/sources/`), workshop drafts (`kb/work/`), the improvement log, generated reports, and prior ADR text — historical records keep their wording.

## Consequences

- **Easier:** the technical sense is now positionally and lexically auditable — `rg "explanatory-reach"` enumerates every technical use, and any future bare "reach" can be read as ordinary English without a which-sense resolution. The compound also self-glosses partially before its definition loads, and matches the sibling registrations (`reach-assessment`, `oracle domain`, `search range`) so the cluster's vocabulary is uniform.
- **Harder:** prose gets heavier — "high-explanatory-reach changes" is clumsier than "high-reach changes", and the compound repeats visibly in notes that discuss the property densely. That verbosity is the price of removing read-time sense resolution, the same trade ADR 053 accepted.
- **Risk:** writers may reintroduce the spaced variant or bare technical uses. The guard is the same as ADR 053's: the invariant that load-bearing senses ride on schema positions or rare compounds, plus the cheap lexical audit this decision makes possible.
