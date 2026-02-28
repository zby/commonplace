---
name: connect
description: Find connections between notes and update indexes. Requires semantic judgment to identify genuine relationships. Use after /extract creates notes, when exploring connections, or when a topic needs synthesis. Triggers on "/connect", "/connect [note]", "find connections", "update indexes", "connect these notes".
user-invocable: true
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, Skill, mcp__qmd__search, mcp__qmd__vsearch, mcp__qmd__query, mcp__qmd__status
context: fork
model: opus
---

## Link Format

All links between notes use **standard markdown links**, not wiki-links. This ensures links render correctly on GitHub and other markdown viewers.

**Same-directory links:**
```markdown
[note-title](./note-title.md)
```

**Cross-directory links** (use relative paths from the source file's directory):
```markdown
[note-title](./research/note-title.md)       # linking into a subdirectory
[note-title](../note-title.md)                # linking up from a subdirectory
```

**Links with display text:**
```markdown
[display text](./note-title.md)
```

**Path resolution rules:**
- Always use relative paths from the source file's directory
- When linking to a file in a subdirectory, verify the path with `ls` before creating the link
- Filenames use hyphens, not spaces (e.g., `my-note-title.md`)

**Active depth: standard**

| Depth | Connection Behavior |
|-------|-------------------|
| deep | Full dual discovery (index + semantic search). Evaluate every candidate. Multiple passes. Synthesis opportunity detection. Bidirectional link evaluation for all connections. |
| standard | Dual discovery with top 5-10 candidates. Standard evaluation. Bidirectional check for strong connections only. |
| quick | Single pass — either index or semantic search. Accept obvious connections only. Skip synthesis detection. |

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse immediately:
- If target contains a note name or path: find connections for that note
- If target is empty: check for recently created notes or ask which note
- If target is "recent" or "new": find connections for all notes created today

**Execute these steps:**

1. Read the target note fully — understand its claim and context
2. **Check note type.** If the target has no frontmatter (a `text` file), run `/convert` on it first to add frontmatter with `status: seedling`. Do not connect a text file without converting it — frontmatter is required for areas, indexes, and quality gates.
3. **Throughout discovery:** Capture which indexes you read, which queries you ran (with scores), which candidates you evaluated. This becomes the Discovery Trace — proving methodology was followed, not reconstructed.
4. Run Phase 0 (sync search index)
5. Use dual discovery in parallel:
   - Browse relevant index(s) for related notes
   - Run semantic search for conceptually related notes
6. Evaluate each candidate: does a genuine connection exist? Can you articulate WHY?
7. Add inline markdown links where connections pass the articulation test
8. Update relevant index(s) with this note
9. Report what was connected and why

**START NOW.** Reference below explains methodology — use to guide, not as output.

---

# Connect

Find connections, weave the knowledge graph, update indexes.

## Philosophy

**The network IS the knowledge.**

Individual notes are less valuable than their relationships. A note with fifteen incoming links is an intersection of fifteen lines of thought. Connections create compound value as the vault grows.

This is not keyword matching. This is semantic judgment — understanding what notes MEAN to determine how they relate. A note about "friction in systems" might deeply connect to "verification approaches" even though they share no words. You are building a traversable knowledge graph, not tagging documents.

**Quality over speed. Explicit over vague.**

Every connection must pass the articulation test: can you say WHY these notes connect? "Related" is not a relationship. "Extends X by adding Y" or "contradicts X because Z" is a relationship.

Bad connections pollute the graph. They create noise that makes real connections harder to find. When uncertain, do not connect.

## Invocation Patterns

### /connect (no argument)

Check for recent additions:
1. Look for notes modified in the last session
2. If none obvious, ask user what notes to connect

### /connect [note]

Focus on connecting a specific note:
1. Read the target note
2. Discover related content
3. Add connections and update indexes

### /connect [topic area]

Synthesize an area:
1. Read the relevant index
2. Identify notes that should connect
3. Weave connections, update synthesis

## Search Scope

Discovery scans three collections under `kb/`:

| Directory | Contains |
|-----------|----------|
| `kb/notes/` | Main KB — claims, design notes, research |
| `kb/claw-design/` | Knowledge system methodology and architecture |
| `kb/sources/` | Snapshotted external sources |

Use all three directories when searching for candidates (keyword grep, description scan, link following). Index updates (Phase 5), directory index regeneration (Phase 7), and areas-topics sync (Gate 6) only apply to notes in `kb/notes/`.

## Workflow

### Phase 0: Sync Search Index

Before using semantic search, ensure the index reflects current files. `qmd update` re-scans all configured collection directories; `qmd embed` updates vectors for any changed files. Both are idempotent and fast.

```bash
qmd update && qmd embed
```

### Phase 1: Understand What You Are Connecting

Before searching for connections, deeply understand the source material.

For each note you are connecting:
1. Read the full note, not just title and description
2. Identify the core claim and supporting reasoning
3. Note key concepts, mechanisms, implications
4. Ask: what questions does this answer? What questions does it raise?

**What you are looking for:**
- The central argument (what is being claimed?)
- The mechanism (why/how does this work?)
- The implications (what follows from this?)
- The scope (when does this apply? When not?)
- The tensions (what might contradict this?)

### Phase 2: Discovery (Find Candidates)

Use dual discovery: index exploration AND semantic search in parallel. These are complementary, not sequential.

**Capture discovery trace as you go.** Note which indexes you read, which queries you ran (with scores), which searches you tried. This becomes the Discovery Trace section in output — proving methodology was followed, not reconstructed after the fact.

**Primary discovery (run in parallel):**

**Path 1: index Exploration** — curated navigation

If you know the topic (check the note's Topics footer), start with the index:

- Read the relevant index(s)
- Follow curated links in Core Ideas — these are human/agent-curated connections
- Note what is already connected to similar concepts
- Check Tensions and Gaps for context
- What do agent notes reveal about navigation?

indexes tell you what thinking exists and how it is organized. Someone already decided what matters for this topic.

**Path 2: Semantic Search** — find what indexes might miss

**Three-tier fallback for semantic search:**

**Tier 1 — MCP tools (preferred):** Use `mcp__qmd__query` (hybrid search with expansion + reranking):
- query: "[note's core concepts and mechanisms]"
- limit: 15

**Tier 2 — bash qmd:** If MCP tools fail or are unavailable:
```bash
qmd query "[note's core concepts]" --collection notes --limit 15 2>/dev/null
```

**Tier 3 — grep only:** If both MCP and bash fail, log "qmd unavailable, grep-only discovery" and rely on index + keyword search only. This degrades quality but does not block work.

Evaluate results by relevance — read any result where title or snippet suggests genuine connection. Semantic search finds notes that share MEANING even when vocabulary differs. A note about "iteration cycles" might connect to "learning from friction" despite sharing no words.

**Why both paths:**

index = what is already curated as relevant
semantic search = neighbors that have not been curated yet

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

### Phase 3: Evaluate Connections

For each candidate connection, apply the articulation test.

**The Articulation Test:**

Complete this sentence:
> [note A](./note-a.md) connects to [note B](./note-b.md) because [specific reason]

If you cannot fill in [specific reason] with something substantive, the connection fails.

**Valid Relationship Types:**

| Relationship | Signal | Example |
|-------------|--------|---------|
| extends | adds dimension | "extends [X](./x.md) by adding temporal aspect" |
| grounds | provides foundation | "this works because [Y](./y.md) establishes..." |
| contradicts | creates tension | "conflicts with [Z](./z.md) because..." |
| exemplifies | concrete instance | "demonstrates [W](./w.md) in practice" |
| synthesizes | combines insights | "emerges from combining [A](./a.md) and [B](./b.md)" |
| enables | unlocks possibility | "makes [C](./c.md) actionable by providing..." |

**Reject if:**
- The connection is "related" without specifics
- You found it through keyword matching alone with no semantic depth
- Linking would confuse more than clarify
- The relationship is too obvious to be useful

**Agent Traversal Check:**

Ask: **"If an agent follows this link, what do they gain?"**

| Agent Benefit | Keep Link |
|---------------|-----------|
| Provides reasoning foundation (why something works) | YES |
| Offers implementation pattern (how to do it) | YES |
| Surfaces tension to consider (trade-off awareness) | YES |
| Gives concrete example (grounds abstraction) | YES |
| Just "related topic" with no decision value | NO |

The vault is built for agent traversal. Every connection should help an agent DECIDE or UNDERSTAND something. Connections that exist only because they feel "interesting" without operational value are noise.

**Synthesis Opportunity Detection:**

While evaluating connections, watch for synthesis opportunities — two or more notes that together imply a higher-order claim not yet captured.

Signs of a synthesis opportunity:
- Two notes make complementary arguments that combine into something neither says alone
- A pattern appears across three or more notes that has not been named
- A tension between two notes suggests a resolution claim

When you detect a synthesis opportunity:
1. Note it in the output report
2. Do NOT create the synthesis note during connect — flag it for future work
3. Describe what the synthesis would argue and which notes contribute

### Phase 4: Add Inline Connections

Connections live in the prose, not just footers.

**Inline Links as Prose:**

The markdown link IS the argument. The title works as prose when linked.

Good patterns:
```markdown
Since [other note](./other-note.md), the question becomes how to structure that memory for retrieval.

The insight that [throughput matters more than accumulation](./throughput-matters-more-than-accumulation.md) suggests curation, not creation, is the real work.

This works because [good systems learn from friction](./good-systems-learn-from-friction.md) — each iteration improves the next.
```

Bad patterns:
```markdown
This relates to [other note](./other-note.md).

See also [throughput matters more than accumulation](./throughput-matters-more-than-accumulation.md).

As discussed in [good systems learn from friction](./good-systems-learn-from-friction.md), systems improve.
```

If you catch yourself writing "this relates to" or "see also", STOP. Restructure so the claim does the work.

**Where to add links:**

1. Inline in the body where the connection naturally fits the argument
2. In the Relevant Notes footer section with context phrase
3. BOTH when the connection is strong enough

**Relevant Notes Format:**

```markdown
Relevant Notes:
- [note title](./note-title.md) — extends this by adding the temporal dimension
- [another note](./another-note.md) — provides the mechanism this claim depends on
```

Context phrases use standard relationship vocabulary: extends, grounds, contradicts, exemplifies, synthesizes, enables.

**Bidirectional Consideration:**

When adding a link from A to B, ask: should B also link to A?

Not always. Relationships are not always symmetric:
- "extends" often is not bidirectional
- "exemplifies" usually goes one direction
- "contradicts" is often bidirectional
- "synthesizes" might reference both sources

Add the reverse link only if following that path would be useful for agent traversal.

**Reweave Task Filtering (when adding bidirectional links):**

When you edit an older note to add a reverse link, you MAY flag it for full reconsideration. But SKIP flagging if ANY of these apply:

| Skip Condition | Rationale |
|----------------|-----------|
| Note has >5 incoming links | Already a hub — one more link does not warrant full reconsideration |
| Note has `type: tension` in YAML | Structural framework, not content that evolves |
| Note was processed in current batch | Do not re-process what was just processed |
| Note is an index | indexes are navigation, not claims to reconsider |

**Check incoming links:**
```bash
grep -r '\[.*\](.*note-name\.md)' kb/notes/ kb/claw-design/ kb/sources/ --include="*.md" | wc -l
```

If >= 5, skip flagging.

### Phase 5: Update indexes

indexes are synthesis hubs, not just indexes.

**Step 1: Check all indexes for membership.**

Read `kb/indexes.md` — the index of indexes. For each index listed, ask: "does this note belong here?" This prevents silent omissions where a note is relevant to an index but never gets added.

If the note should belong to an index it doesn't yet claim, add the index name to the note's `areas:` frontmatter field, then run `uv run kb/scripts/sync_topic_links.py` on the note to update its Topics footer.

**Step 2: Update the indexes this note belongs to.**

For each relevant index:

- Add the note to the appropriate section with a context phrase
- Update Tensions if a new tension was discovered
- Remove Gaps that are now filled
- Add new Gaps discovered during connection-finding

**index Size Check:**

After updating Core Ideas, count the links:

```bash
grep -c '^\- \[' "kb/notes/[index-name].md"
```

If approaching the split threshold (configurable, default ~40): note in output "index approaching split threshold (N links)"
If exceeding: warn "index exceeds recommended size — consider splitting"

Splitting is a human decision (architectural judgment required), but /connect should surface the signal.

**index Structure:**

```markdown
# [Topic Name]

[Opening synthesis: Claims about the topic. Not "this index collects notes" but "the core insight is Y because Z." This IS thinking, not meta-description.]

## Core Ideas

- [claim note](./claim-note.md) — what it contributes to understanding
- [another claim](./another-claim.md) — how it fits or challenges existing ideas

## Tensions

- [claim A](./claim-a.md) and [claim B](./claim-b.md) conflict because... [genuine unresolved tension]

## Gaps

- nothing about X aspect yet
- need concrete examples of Y
- missing: comparison with Z approach

---

Agent Notes:
- YYYY-MM-DD: [what was explored]. [the insight or dead end].
```

**Updating Core Ideas:**

Add new notes with context phrase explaining contribution:
```markdown
- [new note](./new-note.md) — extends the quality argument by showing how friction teaches you what to check
```

Order matters. Place notes where they fit the logical flow, not alphabetically.

**Updating Tensions:**

If the new note creates or resolves tension:
```markdown
## Tensions

- [composability](./composability.md) demands small notes, but [context limits](./context-limits.md) means traversal has overhead. [new note](./new-note.md) suggests the tradeoff depends on expected traversal depth.
```

Document genuine conflicts. Tensions are valuable, not bugs.

**Updating Gaps:**

Remove gaps that are now filled. Add new gaps discovered during reflection.

### Phase 6: Add Agent Notes

Agent notes are breadcrumbs for future navigation.

**Add agent notes when:**
- Non-obvious navigation path discovered
- Dead end worth documenting
- Productive note combination found
- Insight about topic cluster emerged

**Format:**
```markdown
Agent Notes:
- YYYY-MM-DD: [what was explored]. [the insight or finding].
```

**Good agent notes:**
```markdown
- 2026-02-15: tried connecting via "learning" — too generic. better path: friction -> verification -> quality. the mechanism chain is tighter.
- 2026-02-15: [claim A](./claim-a.md) and [claim B](./claim-b.md) form a tight pair. A sets the standard, B teaches the method.
```

**Bad agent notes:**
```markdown
- 2026-02-15: read the index and added some links.
- 2026-02-15: connected [note A](./note-a.md) to [note B](./note-b.md).
```

The test: would this help a future agent navigate more effectively?

### Phase 7: Regenerate Directory Index

After all connections and area index updates are done, regenerate the directory index for the collection the target note belongs to. Determine the collection directory from the target note's path (e.g. `kb/notes/foo.md` → `kb/notes`):

```bash
uv run kb/scripts/generate_notes_index.py <collection-directory>
```

Directory indexes are auto-generated flat listings (title, description, type) — distinct from the curated area indexes updated in Phase 5. This ensures new notes appear in the directory immediately.

## Quality Gates

### Gate 1: Articulation Test

For every connection added, can you complete:
> [A](./a.md) connects to [B](./b.md) because [specific reason]

If any connection fails this test, remove it.

### Gate 2: Prose Test

For every inline link, read the sentence aloud. Does it flow naturally? Would you say this to a friend explaining the idea?

Bad: "this is related to [note](./note.md)"
Good: "since [note](./note.md), the implication is..."

### Gate 3: Bidirectional Check

For every A -> B link, explicitly decide: should B -> A exist?
Document your reasoning if the relationship is asymmetric.

### Gate 4: index Coherence

After updating an index, read the opening synthesis. Does it still hold? Do new notes extend or challenge it?

If the synthesis is now wrong or incomplete, update it.

### Gate 5: Link Verification

Verify every markdown link target exists. Never create links to non-existent files. Targets may live in any of the three collections:

```bash
# Check that a link target exists
ls kb/notes/"target-name.md" kb/claw-design/"target-name.md" kb/sources/"target-name.md" 2>/dev/null
```

### Gate 6: Areas-Topics Consistency

Run the sync script on notes you've modified to ensure `Topics:` footer matches `areas:` frontmatter:

```bash
uv run kb/scripts/sync_topic_links.py kb/notes/target-note.md
```

This is deterministic — `areas:` is the single source of truth. The script generates/replaces the `Topics:` footer section. Notes with no `areas:` field get no Topics section. Accepts files or directories.

## Handling Edge Cases

### No Connections Found

Sometimes a note genuinely does not connect yet. That is fine.

1. Ensure it is linked to at least one area index via Topics footer
2. Note in index Gaps that this area needs development
3. Do not force connections that are not there

### Too Many Connections (Split Detection)

If a note connects to 5+ notes across different domains, it might be too broad.

**Split detection criteria:**

1. **Domain spread:** Connections span 3+ distinct indexes/topic areas
2. **Multiple claims:** The note makes more than one assertion that could stand alone
3. **Linking drag:** You would want to link to part of the note but not all of it

**How to evaluate:**

Ask: "If I link to this note from context X, does irrelevant content Y come along?"

If yes, the note bundles multiple ideas that should be separate.

**Split detection output:**

```markdown
### Split Candidate: [broad note](./broad-note.md)

**Indicators:**
- Connects to 7 notes across 3 domains
- Makes distinct claims about: (1) capture workflows, (2) synthesis patterns, (3) tool selection
- Linking from [note A](./note-a.md) would drag in unrelated content about tool selection

**Proposed split:**
- [capture workflows matter less than synthesis](./capture-workflows-matter-less-than-synthesis.md) — the first claim
- [tool selection follows from workflow needs](./tool-selection-follows-from-workflow-needs.md) — the third claim
- Keep original note focused on synthesis patterns

**Action:** Flag for human decision, do not auto-split
```

**When NOT to split:**
- note is genuinely about one thing that touches many areas
- Connections are all variations of the same relationship
- Splitting would create notes too thin to stand alone

### Conflicting Notes

When new content contradicts existing notes:

1. Document the tension in both notes
2. Add to index Tensions section
3. Do not auto-resolve — flag for judgment

### Orphan Discovery

If you find notes with no connections:

1. Flag them in your output
2. Attempt to connect them
3. If genuinely orphaned, note in relevant index Gaps

## Output Format

After connecting, report:

```markdown
## Connection Complete

### Discovery Trace

**Why this matters:** Shows methodology was followed. Blind delegation hides whether dual discovery happened. Trace enables verification.

**index exploration:**
- Read [index-name](./index-name.md) — found candidates: [note A](./note-a.md), [note B](./note-b.md), [note C](./note-c.md)
- Followed link from [note A](./note-a.md) to [note D](./note-d.md)

**Semantic search:** (via MCP | bash fallback | grep-only)
- query "[core concept from note]" — top hits:
  - [note E](./note-e.md) (0.74) — evaluated: strong match, mechanism overlap
  - [note F](./note-f.md) (0.61) — evaluated: weak, only surface vocabulary
  - [note G](./note-g.md) (0.58) — evaluated: skip, different domain

**Keyword search:**
- grep "specific term" — found [note H](./note-h.md) (already in index candidates)

### Connections Added

**[source note](./source-note.md)**
- -> [target](./target.md) — [relationship type]: [why]
- <- [incoming](./incoming.md) — [relationship type]: [why]
- inline: added link to [note](./note.md) in paragraph about X

### index Updates

**[index-name](./index-name.md)**
- Added [note](./note.md) to Core Ideas — [contribution]
- Updated Tensions: [A](./a.md) vs [B](./b.md) now includes [C](./c.md)
- Removed from Gaps: [what was filled]
- Agent note: [what was learned]

### Synthesis Opportunities

[notes that could be combined into higher-order insights, with proposed claim]

### Flagged for Attention

- [orphan note](./orphan-note.md) — could not find connections
- [broad note](./broad-note.md) — might benefit from splitting
- Tension between [X](./x.md) and [Y](./y.md) needs resolution
```

## What Success Looks Like

Successful connection finding:
- Every connection passes the articulation test
- Inline links read as natural prose
- indexes gain synthesis, not just entries
- Agent notes reveal non-obvious paths
- The knowledge graph becomes more traversable
- Future agents will navigate more effectively

The test: if someone follows the links you added, do they find genuinely useful context? Does the path illuminate understanding?

## Critical Constraints

**Never:**
- Create links to non-existent files
- Add "related" connections without specific reasoning
- Force connections that are not there
- Auto-generate without semantic judgment
- Skip the articulation test

**Always:**
- Verify link targets exist
- Explain WHY connections exist
- Consider bidirectionality
- Update relevant indexes
- Add agent notes when navigation insights emerge
- Capture discovery trace as you work

## The Network Grows Through Judgment

This skill is about building a knowledge graph that compounds in value. Every connection you add is a traversal path that future thinking can follow. Every connection you do not add keeps the graph clean.

Quality beats quantity. One genuine connection is worth more than ten vague ones.

The graph is not just storage. It is an external thinking structure. Build it with care.

