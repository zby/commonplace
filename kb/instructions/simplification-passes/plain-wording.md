---
description: "Use when an artifact's wording should be simplified: decorative figures made literal, unusual words made common, and redundant exclusions cut, without stripping the metaphors that carry the argument or the terms the KB registers"
type: types/instruction.md
effort: simple
---

# Plain wording

Replace wording that costs the reader effort without carrying meaning: figures
that display the writer, unusual words where a common word says the same
thing, and exclusions that deny what the sentence has already ruled out.

Effort: simple. Listing and marking against a recorded threshold; the operator strikes.

1. List every candidate with a proposed replacement. Do not apply any. Four
   kinds of candidate:
   - A figurative phrase, with a literal statement.
   - An unusual word, with the common word that says the same thing. Unusual
     means a general technical reader would pause on it or look it up: rare
     or learned words (ameliorate, adumbrate, orthogonal used for
     "independent"), Latin tags (inter alia, mutatis mutandis), and long
     words with a short everyday equivalent (utilize, endeavour, commence).
   - A redundant exclusion, with the sentence without it. An exclusion is
     redundant when the positive clause already rules out what it denies: "a
     candidate, not a settled finding", "outside the term without being
     denied". Look at "not", "without", "only", and "rather than".
   - A negation-first or contrast construction, with a positive statement:
     "X is not Y. It is Z", "not X but Y", "X, not Y", "does not A; it B",
     or a sentence that denies something and never states what is the case.
2. For each figure, ask whether the mapping does work the literal phrase would
   need more words to do. A tradeoff as buying and paying, a successor chain
   as descent, an internal role as being inside: these stay. A dramatic or
   legal verb applied to an argument (indict, touch, rescue), a contest verb
   (lose, win), or an adverb of manner that adds no content (quietly,
   silently): these go.
3. For each unusual word, ask whether the common word keeps the claim and its
   qualifications. Replace when it does. Keep when the common word drops a
   distinction the sentence relies on and no short plain phrase recovers it,
   and say which distinction. Replace every occurrence of a word with the
   same common word; one occurrence swapped and another kept reads as two
   referents.
4. For each exclusion or contrast, state the positive claim. Keep an
   explicit negation only when readers would otherwise draw the excluded
   inference and the positive form cannot block it: the ordinary sense of a
   technical word ("conjectural" does not mean speculative), a position the
   KB used to hold, a status readers tend to inflate (not a success term), or
   a finding that is itself negative ("no run has been performed"). A
   contrast being the sentence's point is not enough to keep its negative
   form when a positive sentence carries the same point. Threshold set by
   the operator on 2026-09-25, after LLM-drafted articles overused contrast
   and negation.
5. Return the list marked keep or replace, with the reason in a few words.
   The operator strikes items. Apply only what survives.
6. When the literal phrase needs a referent the figure did not name (who is
   charged, what is at fault), do not choose one. Report the phrase as a
   question with the candidate referents.

Report: the applied replacements, one line each. The operator's strikes are
recorded as the threshold for the next run.

Preserve: technical terms that look figurative or unusual but are the field's
or the KB's registered words (seed, holding a theory, gradient descent,
legible, ampliative); a term the artifact itself defines; and quoted text,
which is never reworded. Whether a registered abstraction should give way
to the ordinary word is the [abstractions](./abstractions.md) pass's
question.
