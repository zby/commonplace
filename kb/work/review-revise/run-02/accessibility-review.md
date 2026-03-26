=== ACCESSIBILITY REVIEW: baseline.md ===

Checks applied: 4

WARN:
- [Undefined terms] "An execution boundary usually creates two different questions" — "execution boundary" is never defined or glossed. A technically competent reader outside this KB cannot tell whether this means a function boundary, a process boundary, an API call, or something else entirely. The term carries the entire opening paragraph and the note's structure depends on it.
  Recommendation: Add an inline gloss on first use, e.g., "An execution boundary — any point where one LLM call ends and another begins — usually creates two different questions."

- [Undefined terms] "bounded call" / "bounded context" first appears in "the next bounded call" and "bounded context is expensive" (paragraph 2) with no definition. The concept is central to the note — it appears in nearly every section — but the reader is never told what makes a call "bounded."
  Recommendation: Gloss on first use, e.g., "the next bounded call (a single LLM invocation with a finite context window assembled for one task)."

- [Notation opacity] "storage in `K` is cheap" — `K` is a bare variable with no inline definition. The link to the bounded-context orchestration model is not a substitute; the sentence is opaque without clicking through.
  Recommendation: Gloss inline, e.g., "storage in the scheduler's accumulated symbolic state (`K`) is cheap."

- [Notation opacity] "letting `select(K)` choose what the next call should see" — `select(K)` is formal notation from another note, never defined here. It recurs at five points throughout the note and is load-bearing for the argument.
  Recommendation: Define once on first use, e.g., "`select(K)` — the function that projects a subset of stored state into the next call's prompt." Later uses can stay as `select(K)` since the definition will be nearby enough in the opening.

- [Unidentified references] "Slate is the main tension case" — the reader has no idea what Slate is. It is partially identified later ("workers return episodes") but the first sentence provides no identification at all.
  Recommendation: Identify on first mention, e.g., "Slate (an agent orchestration system described by Yohei Nakajima) is the main tension case."

- [Unidentified references] "Spacebot branches return only a scrubbed conclusion" — Spacebot is named without any identification. A reader cannot tell whether this is a product, a research project, or a conceptual example.
  Recommendation: Add a brief identifier, e.g., "Spacebot (a branching agent architecture) branches return only a scrubbed conclusion."

- [Jargon persistence] `select(K)` and `K` appear at five and four points respectively across the note (paragraphs 2, 7, 9, 12, and the links section). Because neither is defined in this note, every recurrence compounds the opacity rather than reinforcing a grounded concept. By the "right split" section (paragraph 9), a reader who was confused at first encounter is no better off.
  Recommendation: Defining both terms on first use (per the notation-opacity recommendations above) would largely resolve this. No further action needed for later occurrences if the opening definitions are clear.

INFO:
- [Undefined terms] "external symbolic state" (paragraph 2) — the word "symbolic" does specific work here (distinguishing from weights, latent state, etc.) but is not glossed. A reader can roughly infer "stored data outside the model," but the intended contrast is not explicit.

- [Undefined terms] "The scheduler can afford to keep many artifact kinds in external symbolic state" — "scheduler" appears here for the first time without identification. From context a reader can infer it is whatever orchestrates the calls, but the term is unexplained.

- [Jargon persistence] "execution boundary" recurs at four points (opening, "execution-boundary compression" heading, the compression paragraph, and the links section). The term is never defined, but later uses add enough local context ("compression at the execution boundary," "the execution boundary is the natural place to compress") that later occurrences are less opaque than the opening.

CLEAN:
- [Unidentified references] Standard technical terms (LLM, SDK, API, context window, prompt, token, chain-of-thought) are used appropriately and do not need glossing for the target audience.

- [Jargon persistence] "Transcript inheritance," "trace-preserving handoff," and "artifact-first loading" are KB-coined phrases but each is defined or paraphrased inline when introduced and used consistently afterward. These do not block comprehension.

Overall: 7 warnings, 3 info
===
