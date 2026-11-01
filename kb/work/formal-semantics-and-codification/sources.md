# Evidence ledger

Split from the [tentative theory](./where-meaning-is-settled.md) on 2026-11-01. Part of the [workshop](./README.md). Each source was commissioned to support one named claim; the entry records the claim, the status, what the source actually supports, and its limits. Sources cannot link into `kb/work/`, so the workshop links to them from here.

## Sources

- [Schegloff, Jefferson and Sacks, "The preference for self-correction in the organization of repair in conversation" (1977)](../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md): repair is a structural feature of conversation with its own organization, not a failure mode. Ingested. The paper supports that claim: repair occurs where nothing is hearably wrong, errors often go unrepaired, nothing is in principle excluded from the repairable, and the authors call repair the self-righting mechanism of language use in interaction. It does not separate what an expression conventionally means from what the speaker intended, and it ties repair to continuing the next action. No quotes retained yet. The KB uses "self-repair" for an LLM regenerating code until a check passes; the paper's sense is repair by the speaker, so the collision ledger may need an entry.
- [Purver, Ginzburg and Healey, "On the means for clarification in dialogue" (2001)](../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md): clarification requests are frequent in ordinary dialogue and have classifiable forms and readings. Open stand-in for Ginzburg's *The Interactive Stance* (2012), which is not freely available. Ingested. It supports frequency and classifiability only: requests are about 3 to 4 percent of dialogue sentences in the British National Corpus, with eight forms and four readings, and 96 percent target a sentence at most four back. Only about 15 percent ask what an expression refers to; most ask whether the words were heard or what move the speaker made. So the repair feature above must not be read as showing that meaning in general is settled by asking. Single annotator, no agreement check. No quotes retained yet.
- [Tarski, "The semantic conception of truth and the foundations of semantics" (1944)](../../sources/tarski-semantic-conception-of-truth.ingest.md): exactly specified structure as the precondition for a precise semantics (section 6); the semantically closed language and the decision not to use one (section 8); truth defined in an essentially richer metalanguage (section 10). Ingested, whole paper captured. Universality of colloquial language is not in this paper; it is in the 1933 monograph, which is not ingested. Undefinability of a language's own truth holds for formalized arithmetic too, and the paper says nothing about computation, so neither separates natural from programming languages; the antinomy itself hits only semantically closed languages, which arithmetic is not. No quotes retained yet; the ingest names four passages to ground.
- Tarski, "The concept of truth in formalized languages" (1933, English 1956): the universality of colloquial language and the guess that it is inconsistent. Not ingested. Needed before the structural conjecture above can be attributed to Tarski by quotation.
- Clark and Brennan, "Grounding in communication" (1991): what was meant is established jointly, by grounding, as part of language use. Ingest in progress.
- Lakoff, "Hedges: a study in meaning criteria and the logic of fuzzy concepts" (1973): the fuzzy-logic treatment of natural-language vagueness. No copy accessible without a login; the fuzziness claim above stays suspended.
- Clark and Brennan, "Grounding in communication" (1991): what was meant is established jointly, by grounding, as part of ordinary language use. Snapshot and connection report exist; the ingest report was not delivered as of this revision. The connection pass flagged that "grounding" has a different sense in this KB, source support for claims, and that the term needs qualifying at first use.

## Quotes to ground

No ingest has retained quotes yet. The ingests name the passages:

- Schegloff, Jefferson and Sacks: the "nothing is, in principle, excludable" sentence (sections 2.12 to 2.13), the three-turn opportunity space paragraph (section 4.3), the "self-righting mechanism" sentence (section 7).
- Purver, Ginzburg and Healey: the frequency figures, the reading definitions, the ambiguity-resolution passage.
- Tarski: the section 6 "exactly specified" sentence, the section 8 assumptions with the decision not to use semantically closed languages, the section 8 "no exact meaning" sentence, the section 10 sufficiency sentence.

## Not yet ingested

- Tarski 1933, for universality. Needed by the [Tarski thread](./tarski-thread.md).
- Lakoff 1973, for the fuzziness feature. No accessible copy.
- Ginzburg 2012, *The Interactive Stance*. Not freely available; the 2001 paper stands in.
