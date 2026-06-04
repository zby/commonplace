# Plan: refresh the comparative review with matrix data (and absorb the chooser doc)
What I found in `systems.csv` + `analyze_matrix.py`, and what I propose doing to `agentic-memory-systems-comparative-review.md`. Comment inline; I'll act on your marks.
## What the data actually is
- **129 code-based reviews + 5 lightweight = 134 rows.** The CSV is fresh (rebuild produces no diff). But the comparative review still opens with **"Eleven systems."** It is a snapshot from an early era and is badly out of date on scope.
  
- **Only 5 of 29 columns are populated** (`analyze_matrix.py`): `storage_substrate`, `representational_form`, `trace_derived`, `read_back_direction`, `push_engineered`. The review's other five dimensions — **agency, link, temporal, curation, extraction** — are **not** in the matrix. They exist only as prose over the original 11 systems.
  
- So: we **cannot** regrow the six-dimension tables to 129 rows from data. What we _can_ do is ground a smaller set of axes quantitatively across the whole population.
  
## The interesting observations (all over 129 code-based systems)
1. **Files-first is still the plurality but no longer a consensus.** `files` 45% (58), files-family (files/repo/in-memory) **60%**, database-family (sqlite/rdbms/vector/graph/kv) **33%**, other (weights/registry/service-object) 6%. The review's claim that "the filesystem-first consensus breaks" is _directionally right but overstated_ — files still win the plurality. **SQLite (19) is the single most common DB substrate** — more than vector (10) + graph (5) combined. The database camp is mostly boring embedded SQL, not exotic vector/graph stores.
  
2. **Representational form barely discriminates: 81% are** `mixed`**.** Pure prose 8%, pure symbolic 9%, pure parametric 2%. Almost everything blends prose + metadata + embeddings + prompts + code. This axis is near-constant at scale -> footnote, not a table column.
  
3. **Headline finding -- trace-derived learning co-occurs with proactive activation.** Trace-derived systems (89) are push-or-both **80%** of the time; non-trace systems (40) are **pull-only 68%**. Systems that learn from their own traces also tend to push memory back into the next action without the agent asking. The learning loop and the activation loop arrive together. This is in neither doc today.
  
4. `pull` **implies never engineered-push (0 of 45).** Clean definitional confirmation: pull-only systems carry no relevance-gated push path. Half the field (53%) does engineer a push.
  
5. **Databases couple lookup with auto-injection more than files do.** db-family is `both` 63% vs files-family split evenly (`pull` 41% / `both` 44%). Choosing a database tends to buy you an automatic injection path, not just a query surface.
  
## Consolidate: delete the chooser doc, spare its best parts
You want `choosing-an-agent-memory-framework.md` deleted. I agree it's weak: it states trends _without numbers_ ("files remain the largest group", "mixed dominate", "trace-derived are the majority"), and it's missing the trace×activation correlation and the SQLite / db-coupling findings -- so the data we just extracted makes it redundant anyway.

That fits your original ask: make the comparative review useful for **both choosing and designing**. So fold the worthwhile chooser material into the comparative review and delete the standalone doc.

**Worth sparing from the chooser (move into the comparative review):**

- The activation-first reframe: the first chooser question is **how remembered material reaches the next action**, not "files or database?". A genuinely good lead.
  
- The activation taxonomy: **pull / coarse push / identifier-targeted push / inferred push**. Sharper than the review's current prose, and now data-backed.
  
- The "match system shape to use case" guidance (condensed) -- the practical chooser payload.
  

**Drop:** the un-numbered trend bullets (we have the real numbers now), and the "Open Questions" list (fold the still-live ones into the review's open questions).

**Deletion mechanics:** inbound links are only `README.md` (intro + cross-cutting list) and `dir-index.md` (auto-generated -- refresh with `commonplace-refresh-indexes`). Update README to point those references at the comparative review; rebuild the index.
## Proposed shape of the updated comparative review
1. **Fix the scope framing.** Open by stating the collection now holds 129 code-based reviews; position the named-systems deep dive as the _qualitative core_, set against a 129-system _quantitative backdrop_. Stop implying the whole landscape is 11 systems.
  
2. **New early section "What 129 reviews show"** -- the five quantitative findings above (distributions + the trace×activation cross-tab). The data-driven payload.
  
3. **New section "Choosing: start with activation"** -- the spared chooser lens: the activation-first question and the pull/coarse/identifier/inferred taxonomy, with the condensed use-case matching. Makes the doc useful to choosers, not just designers.
  
4. **Update Convergences/Divergences with numbers:** quantify "filesystem-first consensus breaks"; fold in the trace×activation correlation; note form collapses to `mixed`.
  
5. **Keep the six-dimension tables** as the qualitative deep dive on the original named systems, but label them a _bounded close-read_, not a census -- and flag that agency/link/temporal/curation/extraction aren't matrix-extractable yet.
  
6. Update the frontmatter `description` to match the new scope.
  
## What I deliberately won't do
- Won't hand-build 129-row tables for un-extracted dimensions (no data; would be fabrication).
  
- Won't touch the matrix schema or build script in this pass (the "should X become a column?" questions stay as open questions).
  
## Open questions for you
- Keep the 11-system deep-dive tables, or trim them hard now that they're a small sample of 129?
  
- Do the chooser absorb + the data refresh in one commit, or split into two?
