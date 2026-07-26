# Resolve the metacircular-interpreter note against Smith's own distinction

## Idea

`kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md` runs entirely on Brian Cantwell Smith's term *metacircular interpreter*, cites Smith nowhere, and appears to use the term for the thing Smith introduced it to rule out. Decide which of the three cases holds and act on it:

1. The note means something weaker than Smith's term and should say so explicitly, keeping its argument intact.
2. The note is making a claim Smith would contest, in which case the tension belongs in the note with a `contradicts` or `contrasts` edge to `kb/sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md`.
3. The note's usage is straightforwardly compatible and only the citation is missing.

The tension: Smith's point in distinguishing a metacircular processor from a reflective processor is that the former models a language within itself *without causally accessing the state of the system it models* — metacircularity is precisely **not** reflection (ingest, printed pp. 31–33, 35 n. 6). The note takes metacircularity as the right analogy for a self-hosting methodology whose artifacts govern edits to themselves, which is a system that does have the causal path. On Smith's vocabulary that is closer to a reflective processor than to a metacircular one, and the note's own contrast is with compilers rather than with reflective processors.

## Why

The note is not marginal — it sits in the computational-model cluster and its framing (agents re-interpret prose rules each session; stable paths codify into validators) is used elsewhere. If the central term is borrowed against its source's meaning, the note inherits an authority it does not have, and any reader who follows the term back to Smith finds the opposite claim.

It is also a data point about the KB's citation surface. A 2026-07-26 audit found only two notes citing the reflection corpus by path; this is a third import site that the citation graph cannot see, which means path-link greps understate how much external vocabulary the KB is actually running on. Worth noting wherever the KB reasons about its own link coverage.

## Rough Scope

- Read `kb/sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md` against the note, specifically the metacircular-processor versus reflective-processor sections and the reify/absorb vocabulary.
- Pick among the three cases above; the choice is a semantic judgment, not a lookup.
- Edit the note accordingly and add the source edge.
- Check whether `kb/notes/definitions/reflective-system.md` should gain a cross-reference, since it already carries the same distinction in its Exclusions and the two notes would then agree explicitly.

## Why Not Now

The note's operational content — prose re-interpreted per session, stable paths codified — does not depend on the resolution, so nothing downstream is currently wrong in a way that misleads action. The fix needs a careful reading rather than a mechanical edit.

## Trigger to Activate

The note is edited or reviewed for any reason; the reflection corpus is revisited (see the companion backlog task on unconsumed findings); or a new note wants to cite the metacircular framing, at which point the term's meaning has to be settled before it propagates.
