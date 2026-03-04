# Phase 2: Discovery Methodology

**Capture discovery trace as you go.** Record actual query strings, scores, and which candidates you evaluated or rejected. This becomes the Discovery Trace section in output — proving methodology was followed, not reconstructed after the fact. A trace that only lists keywords without query strings or scores is insufficient.

## Step 1: Read the Directory Index (required first step)

Read `kb/notes/index.md` before any other discovery. It lists every note with its description — a complete, cheap candidate scan that catches cross-domain connections that vocabulary-based search misses.

Scan every entry. For each, ask: does this note's description suggest a genuine connection to the source? Flag candidates with a reason. Don't filter by vocabulary overlap — a note about "legal drafting" connects to a paper about "behavioral contracts" even though they share no domain terminology, because both address specification and enforcement.

This step is the primary discovery mechanism. It costs one file read and surfaces connections that semantic search would miss due to vocabulary mismatch.

## Step 2: Topic Index Exploration (if relevant)

If the source connects to a known area (check candidates from Step 1), read the relevant topic index(es). Topic indexes add curated structure that index.md lacks — groupings, tensions, gaps — which can reveal connections the flat listing misses.

## Step 3: Semantic Search

**Two-tier fallback:**

**Tier 1 — qmd (primary):** Run `qmd` with the `commonplace` index:
```bash
qmd --index commonplace query "[note's core concepts]" --collection notes -n 15
```
Also search sources:
```bash
qmd --index commonplace query "[note's core concepts]" --collection sources -n 10
```

Record the actual query string and top results with scores in the discovery trace.

**Tier 2 — grep only:** If qmd fails (command not found or errors), log "qmd unavailable" and rely on index + keyword search only. This degrades quality but does not block work.

Semantic search finds notes that share MEANING even when vocabulary differs. A note about "iteration cycles" might connect to "learning from friction" despite sharing no words. But it is biased toward the source document's vocabulary — that's why Step 1 (directory index scan) comes first.

## Step 4: Keyword Search

For specific terms and exact matches — search notes and sources:
```bash
grep -r "term" kb/notes/ kb/sources/ --include="*.md"
```

Use grep when:
- You know the exact words that should appear
- Searching for specific terminology or phrases
- Finding all uses of a named concept

## Step 5: Link Following

From promising candidates, follow their existing links:
- What do THEY connect to?
- Are there clusters of related notes?
- Do chains emerge that your source note should join?

This is graph traversal. You are exploring the neighborhood.
