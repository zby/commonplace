## Fix Report: areas-exist-because-useful-operations-require-reading-notes-together

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | clause-packing (finding 1) | clause-unpack | Split parenthetical qualifiers into separate clauses on line 40 | fixed |
| 2 | clause-packing (finding 2) | clause-unpack | Split four-concept sentence into two sentences on line 50 | fixed |
| 3 | clause-packing (finding 3) | — | Borderline; review rates as moderate packing, readable | deferred |
| 4 | clause-packing (finding 4) | — | Borderline; review rates as readable but dense | deferred |
| 5 | misleading-link-text (broken link) | stale-paths | Updated broken link target `deep-search-is-...` to `brainstorming-how-to-enrich-web-search.md` | fixed |
| 6 | misleading-link-text (~40 threshold) | stale-paths | Retargeted two WRITING.md links to `adr/004-replace-areas-with-tags.md` which documents the threshold | fixed |

### Warning-to-fix mapping

- **#1 (clause-packing finding 1):** "The sentence 'Running either operation...' packs three ideas: (a) running on the full KB is infeasible due to context limits, (b) it's also inefficient, (c) the reason is most notes don't contribute. The parenthetical qualifiers add clause density."
- **#2 (clause-packing finding 2):** "The first sentence has four concepts: (a) the threshold isn't arbitrary, (b) it's the point where the area exceeds working context, (c) context must also hold instructions, (d) context must also hold reasoning space."
- **#5 (broken link):** "The target file does not exist. This is a broken link." The original target `deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md` was never created. The closest existing note covering /connect with corpus expansion is `brainstorming-how-to-enrich-web-search.md`.
- **#6 (~40 threshold links):** "WRITING.md does not contain the number '40' anywhere, nor does it discuss a split threshold in terms of note count." The ~40 threshold was part of the areas system documented before ADR 004 migrated areas to tags. ADR 004 explicitly mentions the threshold twice.

### Deferred items

- **#3 (clause-packing finding 3):** The review rates this as "moderate packing" — three concepts plus a parenthetical. The sentence is readable and the recommendation identifies findings 1 and 2 as the strongest candidates, with 3 and 4 as borderline.
- **#4 (clause-packing finding 4):** The review rates this as "readable but dense" — a double comparison with three ideas. Same reasoning as #3; the recommendation treats this as borderline.

### New patterns

- **clause-unpack**: A sentence packs multiple ideas into parenthetical qualifiers or chained subordinate clauses. Fix by splitting into separate sentences or replacing parentheticals with independent clauses joined by em dashes or conjunctions. The goal is one main idea per clause, not one idea per sentence.
