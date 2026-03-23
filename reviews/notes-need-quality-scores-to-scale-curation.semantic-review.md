=== SEMANTIC REVIEW: notes-need-quality-scores-to-scale-curation.md ===

Claims identified: 14

## Step 1: Claims extracted

1. "At current scale (~100 notes) this works — the candidate list is short enough for an agent to scan." (opening paragraph — scope claim about current viability)
2. "The fix is a quality score per note that lets /connect filter and rank candidates before the agent evaluates them." (opening paragraph — causal claim: scores fix the scaling problem)
3. "Status is the strongest signal." (Scoring dimensions — strength claim)
4. The four-level status table: current > speculative > seedling > outdated (Scoring dimensions — enumeration)
5. "A `structured-claim` with Evidence/Reasoning sections is a more valuable link target than a `text` with no frontmatter" (Scoring dimensions — comparative claim about type)
6. "Inbound link count is a social proof signal." (Scoring dimensions — definitional claim)
7. "it must be weighted by link strength — ten footer 'related' links count less than three inline 'since [X]' premise links" (Scoring dimensions — dependency on link-strength note)
8. "Recency matters differently per content type." (Scoring dimensions — scope claim)
9. The recency decay table: four content types with decay rates (Scoring dimensions — enumeration)
10. "note scores are the composite of those signals — a single number that summarises 'how valuable is this note as a link target?'" (Where scores get used — definitional claim relating to quality-signals note)
11. Three usage sites: connect candidate filtering, retrieval ranking, quality signals (Where scores get used — enumeration)
12. Three implementation levels: cheapest/medium/full (Implementation spectrum — enumeration)
13. "Probably enough for 200-500 notes" for the cheapest approach (Implementation spectrum — scope estimate)
14. Three open questions: visibility, bootstrapping, rich-get-richer (Open questions — enumeration)

## Step 2: Completeness and boundary cases

**Framework under test: the four scoring dimensions (status, type, inbound links, recency)**

The note claims these four dimensions are what a quality score should capture. The implicit space is "all properties of a note that predict its value as a link target."

Boundary cases:

- **A `current` note that is factually wrong or poorly argued.** Status reflects editorial review, not argument quality. A note can be reviewed, endorsed, and stable but still make a weak claim. The scoring framework would rank it highly. This is a dimension the framework does not cover: content quality independent of status.
- **A note with high inbound links that is a vague generality.** The note itself acknowledges the rich-get-richer problem in Open questions, but frames it as a bootstrapping issue for new notes. The opposite problem also exists: a vague note attracts many links precisely because it is vague enough to relate to anything. Inbound link count rewards vagueness. The quality-signals note explicitly flags this ("A note can be well-connected because it's vague enough to 'relate to' everything"), but this note does not incorporate that caveat into its scoring model.
- **A note that is the sole authority on a niche topic.** It may have zero inbound links (no other note covers adjacent ground), low recency (written once and not revisited), and be a seedling. Yet it could be the most valuable link target for a specific new note about that niche. All four dimensions would rank it low. The scoring framework has no "topical uniqueness" or "semantic relevance to the query" dimension.
- **A `structured-claim` that is empty or boilerplate.** The note asserts type reflects structural maturity, using structured-claim as the high end. But the type field is self-declared metadata; a note can declare itself a structured-claim and have trivial Evidence/Reasoning sections. Type as a scoring dimension assumes type is truthful, which depends on the verification infrastructure the document-classification note describes — a dependency the note acknowledges but doesn't treat as a caveat on the score's reliability.

**Framework under test: the recency decay table (four content types with decay rates)**

- **Index notes.** The table lists source snapshots, design notes, task artifacts, and ADRs, but not index notes. Indexes can become stale (the stale-indexes note is built around this). Where do they fall? They are not timeless like ADRs, and they are not fast-decaying like tasks. This is a gap between enumerated items.
- **Instruction notes.** `kb/instructions/` artifacts are procedures. They decay when the tools or conventions they describe change, but not on a calendar schedule. They don't map cleanly to any row in the table.

WARN:
- [Completeness] The four scoring dimensions omit content quality — a `current` note with a weak argument scores the same as a `current` note with a strong one. The quality-signals note explicitly catalogues content-proxy signals (description uniqueness, title-as-claim ratio) that could feed into content quality, but this note does not incorporate them, despite citing quality-signals as the source of the composite. The note says "note scores are the composite of those signals" but then defines a composite that uses only four of the many signals quality-signals catalogues.

INFO:
- [Completeness] The recency decay table covers four content types but omits index notes and instruction notes, both of which exist in the KB and have distinct decay characteristics. The table's implicit scope claim ("different content types age at different rates") is correct, but the enumeration is incomplete.

INFO:
- [Completeness] Inbound link count as a scoring dimension is vulnerable to the vagueness problem the quality-signals note identifies. The note's own open questions section touches the "rich-get-richer" dynamic but frames it as a problem for new notes, not for vague notes that attract links precisely because they are non-specific.

INFO:
- [Completeness] Topical relevance to the specific query is absent from the scoring dimensions. The dimensions are all note-intrinsic properties, but "value as a link target" is partly relational — it depends on what the connecting note is about. A note can score high on all four dimensions and still be irrelevant to a particular /connect invocation.

## Step 3: Grounding alignment

**Claim: "note scores are the composite of those signals — a single number that summarises 'how valuable is this note as a link target?'"** (cites quality-signals note)

The quality-signals note catalogues three categories of signals: graph-topology, content-proxy, and LLM-hybrid. It proposes combining "many weak signals" into a composite oracle. This note claims to be "the composite of those signals" but defines a composite from only four dimensions (status, type, inbound links, recency). The quality-signals note includes signals like description uniqueness, title-as-claim ratio, PageRank, cluster coefficient, and several others that are not represented in this note's four dimensions. The relationship is more accurately "note scores are a simplified subset of the signals that note catalogues" rather than "the composite of those signals."

**Claim: link strength weighting via the link-strength note.** (cites link-strength-is-encoded-in-position-and-prose)

The link-strength note does say exactly what this note claims: "Three inline premise links from well-regarded notes say more about a note's value than twenty footer 'related' links." The attribution is accurate. The link-strength note also says strength could be inferred from position and prose, confirming the feasibility of weighting inbound links by strength. Clean grounding.

**Claim: "note scoring is what makes automated curation tractable at scale"** (cites automating-kb-learning-is-an-open-problem)

The automating-kb-learning note discusses quality gates as an open problem and links back to this note, saying: "note scoring addresses part of the quality gates problem." The word "part" is important — the source hedges where this note's link context phrase ("is what makes automated curation tractable") does not. The source treats note scoring as one component of a larger unsolved problem; this note's framing suggests scoring is the key enabler. The gap is modest but present.

**Claim: type as a scoring dimension "depends on the type system being meaningful"** (cites document-classification)

The document-classification note defines the type system and its migration path. It does not directly discuss whether the type system is "meaningful" for scoring purposes. The document-types-should-be-verifiable note (which document-classification links to) is closer to the intended grounding — verifiability is what makes type trustworthy as a scoring input. The citation is reasonable but slightly indirect.

WARN:
- [Grounding — scope mismatch] The note claims "note scores are the composite of those signals" about the quality-signals note, but the quality-signals note catalogues dozens of signals across three categories, while this note defines a composite from only four dimensions (status, type, inbound links, recency). The quality-signals note's composite is much broader than what this note implements. Readers could mistake the link as grounding for the full composite when this note covers a subset.

INFO:
- [Grounding — hedging mismatch] The automating-kb-learning note says note scoring "addresses part of the quality gates problem," but this note's link context phrase says scoring "is what makes automated curation tractable at scale" — dropping the "part of" qualifier. The source is more cautious than the citation implies.

PASS:
- [Grounding] The link-strength attribution is accurate. The link-strength note explicitly describes the weighting mechanism this note references, including the "ten footer links vs three premise links" distinction.
- [Grounding] The document-classification citation is reasonable. While the direct grounding for "meaningful type system" lives in document-types-should-be-verifiable rather than document-classification itself, document-classification links to that note and the chain is short.

## Step 4: Internal consistency

**Status as "the strongest signal" vs. the composite model.**

The note declares status is the strongest signal, but the open questions section asks "Does filtering by score create a rich-get-richer problem?" — which is primarily about inbound link count, not status. If status truly dominates, the rich-get-richer problem is less severe (new notes can earn `current` status through review, regardless of inbound links). The two claims are not contradictory but create a tension: either status dominates (and inbound-link bias matters less) or inbound links are influential enough to create the rich-get-richer problem (and status is not as dominant as claimed). The note does not resolve this tension.

**"Only the top N candidates get full attention" vs. the open question about new notes.**

The opening claim says /connect should filter to top N by score, but the open questions section asks about bootstrapping: "A fresh note with no inbound links scores low, but it might be exactly the right link target." These are in tension — the proposed solution (filter by score) would systematically exclude the cases the open question identifies as problematic. The note is aware of this tension (it's an open question, not an oversight), but the body presents filtering-by-score as "the fix" without qualifying it with the bootstrapping caveat.

**Recency "None" for design notes vs. status as a signal.**

The recency table says design notes have no recency decay — "Timeless if still current." But "if still current" is doing significant work: a design note that is no longer current (status: outdated) does decay, just through the status dimension rather than recency. This is not a contradiction but a dependency between dimensions that the note does not make explicit. A reader might infer that old design notes never lose relevance, when the note means they don't lose relevance *from age alone* — status handles the other case.

INFO:
- [Consistency — unresolved tension] The note presents score-based filtering as "the fix" in the opening, then raises bootstrapping as an open question that would undermine the fix for new notes. The body could qualify the claim: "the fix for established notes" or "the fix, with a bootstrapping exception."

INFO:
- [Consistency — implicit dependency] Recency decay "None" for design notes implicitly depends on the status dimension catching staleness. The sentence "Timeless if still current" embeds this dependency but a reader scanning the table alone would miss it.

PASS:
- [Consistency] No pairwise contradictions found between sections. The status table, type discussion, and inbound link count are mutually compatible.
- [Consistency] No definition drift detected. "Quality score," "scoring dimensions," and "composite" are used consistently throughout.
- [Consistency] The description ("As the KB grows, /connect will retrieve too many candidates...") faithfully represents the body's argument. No elided tensions.

Overall: 2 warnings, 5 info
===
