# What should the first article be about?

Working question: what is the one thing a reader should carry away and repeat to someone else? The [editorial contract](../../articles/COLLECTION.md) names spreadability (Jenkins/Ford/Green) as an obligation: give readers material worth carrying into their own communities. This brainstorm diagnoses why the current draft doesn't meet that bar, examines "reflective self-improvement" as the anchor phrase, and lays out candidate cores with a recommendation.

## Diagnosis: why the current draft doesn't spread

[The current draft](../../articles/what-makes-a-system-self-improving.md) is a **vocabulary tour**: five sections, each faithfully compressing one region of the [self-improving-systems cluster](../../notes/self-improving-systems-README.md) — membership test, update architectures, reflection-as-separate-property, addressability, profile-not-ladder. Each section is good. The whole has three structural problems as outward content:

1. **No single takeaway.** A reader who finishes it holds a taxonomy, not a claim. Spreadable technical writing gives the reader one sentence they can retell — "you should read this, it argues X." The draft's X is "here is a precise vocabulary," which is a reference-shelf pitch, not a lunch-table pitch. Taxonomies get bookmarked; claims get repeated.
2. **Inward-facing motivation.** The framing device is "Commonplace needed the term to be precise, because it wants to apply the term to itself." That centers *our* problem. The reader's problem — "my agent appends lessons to a memory file and I can't tell whether that's learning or theater" — appears only implicitly. Spreadable pieces open inside the reader's situation, not the author's.
3. **Even coverage where an article needs a spike.** Distilling a whole cluster produces uniform depth: every section gets ~150 words regardless of how surprising it is. But the cluster's genuinely contrarian content — reflection does *not* buy compounding; a loop without a reject-capable evaluator is a *different architecture*, not a weaker one — is buried mid-list at the same volume as definitional housekeeping.

None of this means the draft is wasted: it is a competent map, and most of its paragraphs can be salvaged as sections or follow-ups. The problem is the *shape*, not the sentences.

## The anchor phrase: "reflective self-improvement"

The operator's instinct: "reflective self-improvement" can be a catchable phrase. Assessment: **yes, with one condition — it must name a category the reader is already living in, not a term we define.**

What it has going for it:

- **It names the thing agent builders are actually doing.** Memory files, skill libraries, CLAUDE.md files, learned instructions, agent-curated KBs — all of these route self-improvement through readable artifacts. The field has hype-words for this ("self-evolving agents," "compounding memory") but no *architectural* name that distinguishes it from the other kind of self-improvement (weights). Naming an existing unnamed practice is the highest-percentage spread move there is — cf. "context engineering."
- **It comes with a built-in contrarian correction.** The KB's sharpest claim is [reflection buys addressability, not compounding](../../notes/reflection-buys-addressability.md): parametric learning compounds fine without any self-representation; what routing improvement through readable artifacts buys is that retained lessons become *inspectable, criticizable, selectively revisable, rollback-able, auditable*. This cuts directly against the dominant sales pitch ("memory makes your agent compound") and is defensible to a hostile technical reader. A correction to hype travels further than a definition.
- **It comes with a built-in warning.** [Retrieval failure is reflection failure](../../notes/retrieval-failure-is-reflection-failure.md): the reflective path's compounding is best-effort — a lesson that never surfaces contributes nothing. Weights can't fail to find their retained change; artifacts can. This gives the article a practical edge (engineer your retrieval path like you'd engineer your update rule) rather than pure taxonomy.
- **It scales to a series.** "Reflective self-improvement" is an umbrella. Article 1 plants the flag; later articles each take one slogan at full depth (the evaluator question, the retrieval question, the worked trace, the profile). Choosing an umbrella phrase for article 1 is a strategic decision, not just an editorial one.

Risks and mitigations:

- **"Reflective" reads as "the model thinks about its outputs"** — Reflexion-style self-critique loops are the established association in the agents literature. The article must disambiguate early: reflective in the *computational reflection* sense (a causally connected self-representation the system reads and edits), not "the LLM reflects on its mistakes." This collision is real but survivable — one early paragraph, and the collision itself is content ("the word you know from Reflexion means something older and stronger").
- **Two-kinds framings invite border disputes.** Fine-tuning-on-own-trajectories vs. artifact memory is clean, but hybrids exist. The note cluster already handles this honestly (boundary cases, open questions); the article should gesture at it and link out rather than litigate.
- **The phrase is abstract.** Mitigate with a concrete opening: an agent writing a lesson into a file, and the question "what did that buy you that fine-tuning wouldn't?"

## Candidate cores

Each candidate is stated as the one-liner a reader would repeat.

**A. The flag-plant (recommended): "There are two architectures of self-improvement — opaque and reflective — and they have opposite failure profiles."**
Weights compound automatically but can't be read; artifacts can be read but compound only if retrieved. Your agent's memory file is not a budget version of fine-tuning — it's a different architecture whose payoff is addressability (audit, selective revision, rollback, transfer) and whose tax is retrieval. Draws on: [reflection-buys-addressability](../../notes/reflection-buys-addressability.md), [retrieval-failure-is-reflection-failure](../../notes/retrieval-failure-is-reflection-failure.md), [reflective-system](../../notes/definitions/reflective-system.md). This is the piece the phrase "reflective self-improvement" titles.

**B. The evaluator question: "A self-evolving loop without a reject-capable evaluator isn't a weaker version of the architecture — it's a different architecture."**
Where exactly is your evaluator, what can it reject, and what evidence does it consume? A false positive that passes evaluation becomes part of your agent's operative organization. Draws on: [a-proposal-selection-loop-requires-search-evaluation-and-retention](../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). Sharp, practical, quotable — but narrower, and it doesn't need the anchor phrase. Strong candidate for **article 2**.

**C. The retrieval slogan: "Retrieval failure is reflection failure."**
Your memory system is only as self-improving as its retrieval path; treat retrieval engineering as improvement-pathway engineering. Spreads well in the agent-memory community, but presupposes the reflective framing — it lands harder *after* A has planted the flag. Natural **article 3** (or a section of A, which is where it currently sits in miniature).

**D. The worked trace: "We run a KB whose content is its own methodology; here is a commit-level trace of it improving itself."**
Show-don't-tell, verifiable, unusual — nobody else publishes their self-improvement loop with a public audit trail. But as a *first* article it reads as project marketing before the reader has a frame to evaluate it with. Best as the closing proof-of-life section in A (two paragraphs + link to [commonplace-as-a-reflective-system](../../reference/commonplace-as-a-reflective-system.md)) and later a full article.

**E. Tighten the existing tour.** Keep the five-section structure, improve the prose. Rejected: the problems are structural (no spike, no single claim), not stylistic.

## Recommendation

**Core A, titled with the phrase.** Working titles, in preference order:

1. *Reflective self-improvement* — bare flag-plant; strongest if the term is meant to be the citable handle.
2. *Reflective self-improvement: the kind you can audit* — adds the payoff to the title.
3. *Two ways an agent can improve itself* — most accessible, but spends the title on the setup instead of the name.

Sketch of the shape (≈40% the length of the current draft's ambitions, one spike):

1. **Open in the reader's system.** An agent appends a lesson to its memory file. Is that self-improvement? Is it *better* than fine-tuning, or worse, or something else? (No Commonplace, no "we needed precision.")
2. **Name the split.** Two architectures: retention in opaque weights vs. retention routed through a readable self-representation. Define "reflective self-improvement" in two sentences; disambiguate from Reflexion-style self-critique in one.
3. **The correction (the spike).** What reflection does *not* buy: compounding — parametric learners compound by construction. What it buys: addressability — the retained change becomes an object the system (and you) can read, criticize, revise selectively, roll back, check against other changes, and audit. State the trade symmetrically: automatic-but-opaque vs. criticizable-but-best-effort.
4. **The tax.** Retrieval is the wire. One paragraph of "retrieval failure is reflection failure," pitched as an engineering obligation.
5. **One paragraph of the evaluator question** (B) as the second practical takeaway — where can your loop say no?
6. **Proof of life.** Two paragraphs of the Commonplace worked trace (D), explicitly as "we eat this cooking, and the trace is public."
7. **Where to go next.** The onward path the contract requires: cluster head, membership definition with its ten boundary cases, the full addressability argument, the self-classification.

What this drops from the current draft (and where it goes): the full membership test with its three clauses → onward link + article on its own if ever needed; profile-not-a-ladder → onward link, possibly a later article; the Smalltalk/Homeostat dissociation → one sentence each inside section 2, links carry the rest.

Credibility guardrail worth keeping from the KB's own restraint: do **not** claim reflective pathways improve faster or more safely — the KB records that as an open empirical question, and saying so out loud is itself differentiating in a hype-saturated feed.

## Open decisions for the operator

1. **Confirm core A** (or redirect to B/D as the opener).
2. **Title**: bare phrase vs. phrase-plus-payoff (options above).
3. **Fate of the current draft**: rewrite in place (it is `status: draft`, so the freeze rule doesn't bind yet — replacing the body is legitimate), or keep it as an internal map and start the article file fresh.
4. **Series intent**: if B and C are earmarked as articles 2–3, article 1 can be shorter and point forward; if article 1 must stand alone indefinitely, sections 4–5 grow slightly.
