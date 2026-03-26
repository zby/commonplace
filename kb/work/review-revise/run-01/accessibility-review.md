=== ACCESSIBILITY REVIEW: baseline.md ===

Checks applied: 4

WARN:
- [Undefined terms] "An execution boundary usually creates two different questions" — "execution boundary" is the note's central concept but receives no inline definition or gloss. A reader unfamiliar with the KB cannot tell whether this means an API call boundary, a process boundary, a turn boundary, or something else.
  Recommendation: Add an inline gloss on first use, e.g., "An execution boundary — any point where one LLM call ends and another begins — usually creates two different questions."

- [Undefined terms] "storage in `K` is cheap; bounded context is expensive" — `K` appears without any definition. The sentence is load-bearing (it motivates the entire note) but is opaque without prior knowledge of the bounded-context orchestration model's notation.
  Recommendation: Gloss on first use: "the scheduler's accumulated external state `K`" or similar.

- [Undefined terms] "the next bounded call" — "bounded call" is used seven times in the note but is never defined or paraphrased. The reader can guess it means a single LLM invocation with a finite context, but the note treats it as a precise term without establishing what makes a call "bounded."
  Recommendation: Define on first use, e.g., "the next bounded call — a single LLM invocation with a deliberately assembled context."

- [Undefined terms] "letting `select(K)` choose what the next call should see" — `select(K)` is functional notation from the KB's orchestration model. It appears six times in the note but is never defined here. A reader who has not read the orchestration model note cannot parse this.
  Recommendation: Gloss on first use: "`select(K)` — the function that chooses which stored artifacts to load into the next call's prompt."

- [Undefined terms] "external symbolic state" — used four times (lines covering storage vs loading), never defined. "Symbolic" is doing unexplained work — it distinguishes this state from something (weights? embeddings?) but the reader cannot tell what.
  Recommendation: Gloss on first use, e.g., "external symbolic state — explicitly stored artifacts like structured data, compressed summaries, and traces, as opposed to in-context or latent state."

- [Undefined terms] "The scheduler can afford to keep many artifact kinds in external symbolic state" — "scheduler" appears without context. The reader does not know whether this is a software component, a human role, or an abstract function in the KB's model.
  Recommendation: Identify on first use: "The scheduler — the orchestration layer that dispatches bounded calls — can afford to keep..."

- [Notation opacity] `K` is used at four points across the note (paragraphs 2, 8, 10, and the Relevant Notes section) and is never defined in this note. The sentence "storage in `K` is cheap" requires the reader to have read the bounded-context orchestration model note to decode.
  Recommendation: Same as the `K` undefined-term finding — add an inline gloss on first use.

- [Notation opacity] `select(K)` appears six times and is never defined. By the section "The right split: storage vs next-context loading," the reader encounters "loading happens through `select(K)`" as if it were already established notation, but it was never established in this note.
  Recommendation: Define on first use and consider using plain language ("the selection function") in some later occurrences to reduce notation density.

- [Notation opacity] `P` in "assembles a prompt `P`" — borderline. The gloss "a prompt" is present, but `P` is never used again, making the notation pointless rather than opaque.
  Recommendation: Drop `P` — it adds notation weight without payoff since it is never referenced again.

- [Unidentified references] "Slate is the main tension case" — Slate is not identified. The reader does not learn what Slate is (an agent framework? a product? by whom?) until they encounter "workers return episodes" several sentences later, and even then the identification is incomplete.
  Recommendation: Identify on first mention: "Slate — an agent system described by its creators as moving beyond ReAct — is the main tension case."

- [Unidentified references] "Spacebot branches return only a scrubbed conclusion" — Spacebot is introduced with a link but no identification. The reader does not know what kind of system it is.
  Recommendation: Add a brief identifier: "Spacebot, an LLM-based research agent, ..."

- [Jargon persistence] "bounded call" / "bounded context" — appears at least ten times after its first (undefined) use. By the practical-principle section ("keep the raw trace as an auxiliary substrate... unless a specific bounded call truly needs it"), the term has become load-bearing shorthand that was never grounded.
  Recommendation: Define on first use (see above) and consider replacing some later occurrences with plain language like "a single LLM invocation" to reduce the reader's recall burden.

- [Jargon persistence] `select(K)` — appears six times across the note. After the first use in paragraph 2, it reappears in "The right split" section and the "Execution-boundary compression" section without re-grounding. By the later uses, the reader who did not fully absorb the notation on first encounter is lost.
  Recommendation: After defining it once, use "the selection function" or "the loading decision" in at least some later uses.

- [Jargon persistence] "external symbolic state" — appears four times. The phrase is used as established vocabulary from the second paragraph onward, but it was never grounded.
  Recommendation: Define on first use (see above); later uses will then be adequately grounded.

INFO:
- [Undefined terms] "clean model" in "In the clean model, loading happens through `select(K)`" — "clean" is doing classificatory work (distinguishing this model from a messy/default one) but the term is not established. The reader can infer the contrast from surrounding prose, so this is mildly rather than severely opaque.

- [Undefined terms] "framework-owned tool loops" — "framework-owned" implies a contrast with some other ownership model. The note partially explains this in the bullet list ("framework-managed tool loops make intermediate progression happen inside a hidden runtime"), which is enough to infer the meaning, but the phrase on its own is somewhat jargon-heavy.

- [Notation opacity] `P` is introduced but never reused — harmless but unnecessary notation.

CLEAN:
- [Unidentified references] Standard technical terms (LLM, SDK, API, context window, prompt, token) are used appropriately and do not need identification.
- [Jargon persistence] "transcript inheritance," "trace-preserving handoff," and "artifact-first loading" are introduced with enough surrounding context that they remain comprehensible on later use. These are explanatory phrases rather than opaque jargon.

Overall: 9 warnings, 3 info
===
