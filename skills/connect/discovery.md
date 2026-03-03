# Phase 2: Discovery Methodology

Use dual discovery: index exploration AND semantic search in parallel. These are complementary, not sequential.

**Capture discovery trace as you go.** Note which indexes you read, which queries you ran (with scores), which searches you tried. This becomes the Discovery Trace section in output — proving methodology was followed, not reconstructed after the fact.

**Primary discovery (run in parallel):**

**Path 1: Index Exploration** — curated navigation

If you know the topic (check the note's Topics footer), start with the index:

- Read the relevant index(s)
- Follow curated links in Core Ideas — these are human/agent-curated connections
- Note what is already connected to similar concepts
- Check Tensions and Gaps for context
- What do agent notes reveal about navigation?

Indexes tell you what thinking exists and how it is organized. Someone already decided what matters for this topic.

**Path 2: Semantic Search** — find what indexes might miss

**Two-tier fallback for semantic search:**

**Tier 1 — bash qmd (primary):** Run `qmd` with the `commonplace` index:
```bash
qmd --index commonplace query "[note's core concepts]" --collection notes -n 15
```
Also search sources:
```bash
qmd --index commonplace query "[note's core concepts]" --collection sources -n 10
```

**Tier 2 — grep only:** If qmd fails (command not found or errors), log "qmd unavailable" and rely on index + keyword search only. This degrades quality but does not block work.

Evaluate results by relevance — read any result where title or snippet suggests genuine connection. Semantic search finds notes that share MEANING even when vocabulary differs. A note about "iteration cycles" might connect to "learning from friction" despite sharing no words.

**Why both paths:**

Index = what is already curated as relevant
Semantic search = neighbors that have not been curated yet

Using only search misses curated structure. Using only index misses semantic neighbors outside the topic. Both together catch what either alone would miss.

**Secondary discovery (after primary):**

**Step 3: Keyword Search**

For specific terms and exact matches — search all collections:
```bash
grep -r "term" kb/notes/ kb/claw-design/ kb/sources/ --include="*.md"
```

Use grep when:
- You know the exact words that should appear
- Searching for specific terminology or phrases
- Finding all uses of a named concept
- The vocabulary is stable and predictable

**Choosing between semantic and keyword:**

| Situation | Better Tool | Why |
|-----------|-------------|-----|
| Exploring unfamiliar territory | semantic | vocabulary might not match meaning |
| Finding synonyms or related framings | semantic | same concept, different words |
| Known terminology | keyword | exact match, no ambiguity |
| Verifying coverage | keyword | ensures nothing missed |
| Cross-domain connections | semantic | concepts bridge domains, words do not |
| Specific phrase lookup | keyword | faster, more precise |

**Step 4: Description Scan**

Use ripgrep to scan note descriptions for edge cases:
- Does this extend the source note?
- Does this contradict or create tension?
- Does this provide evidence or examples?

Flag candidates with a reason (not just "related").

**Step 5: Link Following**

From promising candidates, follow their existing links:
- What do THEY connect to?
- Are there clusters of related notes?
- Do chains emerge that your source note should join?

This is graph traversal. You are exploring the neighborhood.
