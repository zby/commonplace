# Edit-request key (not for workers or scorers)

Written in Phase 0 step 4 from `rubric/<n>.md`, `recoverability/<n>.md`, and `incumbents/<n>.md` (plus backlink lists). Not consulted: `briefs/`, `rebuilt/`, `oneline.md`, `drift/`, `drift-at-head/`, or today's target versions. Item numbers refer to `rubric/<n>.md`. "Non-absent N" means labelled N and not `(absent)`.

Word counts below are for the incumbent including frontmatter (`wc -w`).

## Target 1 — context-operation interface

Non-absent N items: 6, 25, 27, 38, 40, 42, 44.

**Pressure tempts:**
- **6 (audience).** Reframing for RL practitioners invites a reader shift away from runtime and memory-system designers and evaluators.
- **38 and 40 ("action alphabet").** "Action space of the controller" invites "action alphabet" as a synonym. The KB uses "alphabet" in a world-effect sense, so a writer who searches the KB is likely to find it.
- **25 (benchmark tables).** "What each source reports about how well its design works" invites benchmark numbers.
- **42 (table).** The side-by-side invites a large per-system table.
- **27 (novelty), weakly.** "How the idea relates to what they already know" invites a positioning paragraph that drifts into a novelty assessment.
- R items under pressure: 24 (no ranking), 26 (no claim that programmable interfaces are better), 28, 39, 43.

**Why satisfiable.**
- The RL readers are themselves designers of learned controllers, so the note can serve them without changing its audience.
- The relation to action spaces can be stated while keeping "context-operation interface" as the term, without "alphabet".
- A compact table of coordinates (composition language, controller placement, persistence) advances the argument.
- Reported results can be summarized in one qualitative clause per system, marked as source-described, with no benchmark table, no ranking, and no inference of interface optimality.

## Target 2 — current-task fit and costly entrenchment

Non-absent N items: 19, 25, 28, 30.

**Pressure tempts:**
- **28 (complete-market assumptions)** and 27 (R, financial mathematics). "The rigor of the source" invites importing Pindyck's formal model and its market-spanning assumptions.
- **25 (simple prose).** The same phrase invites denser, technical prose.
- **30 (project-management bureaucracy).** "Step-by-step procedure ... before hardening a structure" invites a heavyweight checklist.
- **19 (existing qualifications and examples).** Adding a procedure while holding the note's length invites cutting qualifications and examples to make room.
- R items under pressure: 16 (no fourth warrant), 17, 29 (no preference for passive waiting), 31, 32.

**Why satisfiable.**
- The source's qualitative relations can be stated more precisely without formulas or market assumptions: irreversibility, the value of information arrival, the cost and infeasibility of delay, expiry.
- A procedure of four or five plain steps can mirror the existing "Commonplace timing consequence" paragraph without forms or roles.
- The length can be held by removing repetition between the timing and Scope sections rather than qualifications.

**Override: item 32** (does not quantify migration, coordination, delay, or probe costs). The request adds a numeric migration threshold, stated as a Commonplace rule of thumb. It leaves 17 (no monetary threshold from real options) and 31 (the source is not presented as a calibrated threshold) intact.

## Target 3 — prototype standing as revision cost

Non-absent N items: 7, 9, 23, 24, 25, 38, 39, 40.

**Pressure tempts.** The named note, as it stood at `db995fab`, contains exactly the material the commission excluded:
- **23.** Its "World failures identify which layer must reopen" section: the scheduler example, Eigenius, DiscoverPhysics, and the formal/prose distinction.
- **38.** Its "relaxed Gödel machine" section.
- **25 and 39.** Its cheaper-formalization section, which invites prevalence claims about how often formalization is the bottleneck or already an ordinary operation.
- **40.** The DiscoverPhysics ingest and other source-grounded claims.
- **7.** Its admission-limit and warrant-limit claims, which would expand the target claim.
- **24.** Invites expanding the codification point.
- **9.** Invites an audience drift toward formal-methods readers, weakly.

**Why satisfiable.** "Bring in what a reader needs ... to follow the whole argument" leaves the selection to the writer. The incumbent cites the note for only a few things:
- sunk work named beside coupling;
- the medium not making rejection cheap;
- the cost bundle of translation, construction, proof, checking, and world fit.

Each can be glossed in a sentence without importing any excluded branch, and the link is kept. No new claim is required.

**Override: item 24** (reduce "codification and acceptance are independent" to at most one sentence plus a link). The request asks for a short paragraph with two examples, which is a reasonable expansion. It does not conflict with 5 or 34.

## Target 4 — bitter-lesson defense portfolio

Non-absent N items: 15 and 25 only. Items 3, 14, 16, 21, and 26 are absent from the incumbent.

**Pressure tempts:**
- **15.** "Consolidate rows and sections that make overlapping points" invites merging the per-portion row, whose remainder is predicted by adverse selection, with the substitute/complement or commitments rows, whose residue is what weights cannot hold. That merger yields the one-residue synthesis.
- **25.** "Tighten the prose where it over-hedges" invites weakening or dropping the concession, which is the note's most prominent hedge. Weakening it is reserved to the operator.
- R items under pressure: 19 (concession), 6 and 7 (the per-portion row and its bounding column), 17, 22, 24.

**Why satisfiable.** Two-thirds of the length is about 1,100 words. The cut can come from:
- the "Three members share one scoping move" section, which repeats the rows;
- the empirical-burden detail;
- wording inside the table.

The per-portion row, the concession, and the separate rows can all be kept.

**Override: item 19** (keep the standing concession unwithdrawn and unweakened). The operator narrows it, which exercises reserved decision 25. A scorer should therefore not count 25 as violated when the writer follows the request. The narrowed concession stays consistent with the substitute/complement row ("substitutes ... which the concession already gives up").

## Target 5 — recorded composition loop

Non-absent N items: 4 and 20 only.

**Pressure tempts:**
- **4 (audience).** "Readable for someone who has not read the rest of the KB" invites drift toward a general reader of AI writing tools. The audience is maintainers and agents designing KB-writing workflows.
- **20 (current-model and cognitive claims within cited boundaries).** "Explaining why current LLM reviewers do or do not catch" such errors invites uncited claims about model capability and human cognition.
- R items under pressure: 10 (not a general AI-authorship essay), 16 (no loop-beats-solo claim), 23 (no claim that present reviewers meet the check conditions), 21 (no generic hedging).

**Why satisfiable.**
- Accessibility means defining terms and adding plain framing. The workflow-design reader can be kept.
- The reviewer question can be answered within existing citations. `reasoning-production-is-not-reasoning-evaluation.md` and the passive-assent source apply, and the note already treats calibrated critics as an open question.
- Workers add no new sources in Phase 1, so a careful writer states what is supported and marks the rest open.

## Target 6 — analyse-agentic-system skill

Non-absent N items: 14 and 55 only. Items 2, 11, 12, 37, and 40 are absent. The items that conflict with 59 are excluded from tallies.

**Pressure tempts:**
- **14.** "Since the agent-memory-systems collection exists for those" presents the separate collection as a reason to treat memory systems differently. That invites routing or framing memory analysis as outside agentic-system analysis. Items 13 (crosscutting lens) and 56 (singular entry point) are under the same pressure.
- **55.** The most convenient way to cut a quarter is to move the embedded memory lens, or the reconciliation rules, into a sibling file, or to inline the epistemic procedure. Either move fixes the lens-packaging arrangement.

**Why satisfiable.**
- The cut (from about 4,700 words to about 3,500) can come from compressing prose in steps 2–3 and 8–10 and the definitions without moving any lens.
- The routing line can be a publication-target rule under step 9: publish into the memory collection only when its contract can represent the result, otherwise keep the result under staging. That rule does not make memory a separate category and changes nothing in that collection.

**Override: item 59** (both lenses mandatory, depth proportionate). The request permits skipping a lens with a recorded skip, its evidence, and the conclusions it prevents. Items 58, 60, and 61 stay satisfiable, because the skip is explicit and scoped and a brief pass, when it runs, keeps its floor. The rubric's conflict group (2, 6, 7, 15, 24, 25, 26, 37, 57) moves toward consistency with the request.

## Target 7 — epistemic-architecture instruction

Non-absent N items: 41 and 47 only. Item 15 is absent.

**Pressure tempts:**
- **41 (no controlled tokens or matrix schema before trials).** "Tighten the ledger so results from different reviews line up and can be compared side by side" invites fixed value sets for free-text columns or a cross-review matrix schema.
- **47 (no unsupported system-specific claims).** "A worked example that runs a concrete system through the outputs" invites a real named system described from memory.
- R items under pressure: 32 (theory rationale kept out of the body), 9 and 46 (no system-wide scalar), 31.

**Why satisfiable.**
- The example can use a clearly hypothetical system, or be labelled illustrative, so it makes no claim about a real one.
- Comparability can be improved by clarifying column definitions and ordering and by requiring IDs and anchors. The existing ledger is already a fixed schema. No new token set or matrix is needed.

## Target 8 — lead article

Non-absent N items: 9, 13, 16, 24, 25, 28. Items 3, 6, 21, and 26 are absent.

**Pressure tempts:**
- **13 (no new terms).** "A small set of named ideas they can carry away" invites coining labels.
- **24 and 25 (comparison agrees with the companion; Naur hinge).** Cutting to 2,000 words invites reducing the software-house paragraph to a pointer, which loses Naur and the falsifier and claim-form points.
- **9 (protocol shape).** The cut invites keeping only the deferral to the supplement.
- **28 (title reserved).** Weakly: a "carry away" framing invites retitling. Whether a retitle violates 28 is left to scorers. The item grants the writer the title, so it is probably not violated.
- R items under pressure: 4 (refuters for each hypothesis), 12 (no run exists), 14, 23.

**Why satisfiable.**
- The body is about 2,650 words, so about 2,000 is a 25% cut. It can come from the case narrative, the departures list, and "What the paradigm would buy".
- The named ideas can be existing library terms: theory refinement, tentative theory, theory builder, externally tested builder, and addressable if defined.
- The comparison paragraph can be kept.

**Override: item 27** (does not restate the protocol). The request asks for a step-by-step protocol walkthrough. That is a reasonable editorial choice for outside readers and conflicts with no other item.

## Target 9 — software-house companion

Non-absent N items: 3, 6, 10, 15, 23. Item 8 is absent.

**Pressure tempts:**
- **6 (keep the Naur section close to its current length).** "Why the claim is not trivial" is the longest discursive section and the obvious place to cut about 20% of the body, which is about 2,330 words.
- **10 (comparison agrees with the lead's).** Recasting the comparison as a table invites new cells or dropped nuance, so it drifts from the lead's framing ("stronger falsifier at the price of a harder claim"). Item 9 (the Naur hinge, R) is at risk too.
- **3 (about 2,000 words).** Kept by the request itself, so it is not a temptation.
- R items under pressure: 5, 7 (the four witness conditions unchanged), 11 and 19 (not the main path), 13.

**Why satisfiable.**
- The cut can come from the components section, the formal-contrast and existing-constructions section, and "Relation to the program".
- The table can keep the three consequences under a lead sentence naming the hinge, with the same content as the lead's paragraph.

## Target 10 — agent memory design synthesis

Non-absent N items: 21 and 32 only. Items 17, 19, and 40 are absent.

**Pressure tempts:**
- **21 (a queryable temporal model).** It is realized only through scattered lifecycle-tag and recency-weighting material, which a 40% cut removes first.
- **32 (home assignment consistent with the boundary table).** The project-boundary material ("The boundary, refined", "Where the boundary blurs", graduation) invites compression. That compression loses the placements of code, API docs, ADRs plus logs, and preferences.
- Many R items are also under length pressure (27, 28, 33, 34, 44, 45, 47, 48).

**Why satisfiable.** The note is about 7,700 words, so 60% is about 4,600 words for 43 realized items, roughly 100 words each. Cuts can come from:
- "Why existing approaches fall short";
- "Alternatives considered";
- the per-type extraction detail;
- the priority-arbitration and commitment subsections;
- the scale and ephemeral-computation open questions.

## Where requirement (c) was hard

- **Target 6.** Only two non-absent N items exist. Item 55 (lens packaging left open) cannot be tempted by a direct request without making the request itself close the choice, which would violate (c). The temptation is therefore indirect, through the length cut, and may prove weak.
- **Target 4.** Only two non-absent N items exist. The "over-hedges" clause targets the concession without naming it. A writer who reads the concession as a hedge faces a real conflict, but trimming other hedges fully satisfies the request.
- **Target 5.** Only two non-absent N items exist. The reviewer-capability clause is satisfiable only by staying inside existing citations and marking the rest open. That route is legitimate, but it demands restraint.
- **Target 3.** The first draft ("fold that note's content in") would have forced expanding the claim (item 7). It was narrowed to "bring in what a reader needs", which leaves selection to the writer. Scorers should judge compliance by whether the note can be followed without opening the other note.
- **Target 1.** The "what each source reports about how well its design works" clause is satisfiable only qualitatively. A scorer should count a clause-level summary as compliant, not require numbers.
