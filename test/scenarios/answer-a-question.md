---
description: Step-by-step decomposition of the answer-a-question scenario — read-only, mostly variable costs, rarely needs escalation because no structural decisions are involved
type: scenario
frequency: common
---

# Answer a question

User asks something the KB should know. The agent must search for relevant notes, read them, follow links to deepen understanding, and synthesise an answer. This is a read-only scenario — no files are created or modified.

## Steps

### 1. Understand the question
- **Context needed:** Routing table to know where to search, search patterns
- **Source:** `CLAUDE.md`
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** CLAUDE.md is always loaded. The agent uses routing and search patterns to determine where to look.

### 2. Search for relevant notes
- **Context needed:** KB content matching the question
- **Source:** variable — search results from `kb/notes/`, `kb/sources/`
- **Hops:** 1 (search)
- **Fixed/Variable:** variable
- **Notes:** One search hop. Results depend entirely on the question and KB content. Estimate 3-5 results.

### 3. Read matching notes
- **Context needed:** Full content of relevant notes
- **Source:** variable — specific notes from search results
- **Hops:** 3-5 (read results)
- **Fixed/Variable:** variable
- **Notes:** Each result is a read. The agent scans descriptions to decide which to load fully. Good descriptions (the retrieval filter convention) reduce unnecessary reads.

### 4. Follow links for deeper context
- **Context needed:** Notes linked from the initial results
- **Source:** variable — notes referenced by links in step 3
- **Hops:** 1-3 (follow links)
- **Fixed/Variable:** variable
- **Notes:** The agent follows inline and footer links from loaded notes to build a more complete picture. Not all links are followed — the agent uses link semantics (extends, grounds, contradicts) to decide which are relevant.

### 5. Synthesise answer
- **Context needed:** All loaded notes in context
- **Source:** — (agent produces output)
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** No additional reads. The agent composes an answer from everything loaded.

## Escalation path (installed projects only)

### E1. Question is about methodology, not content
- **Context needed:** Understanding of how the KB system works
- **Source:** `commonplace/kb/notes/` (search results)
- **Hops:** 1 (search) + 1-2 (read results)
- **Fixed/Variable:** variable
- **Notes:** When the user asks "what types of notes can I create?" or "how does the connect skill work?", the answer lives in commonplace methodology, not in the project's KB. The CLAUDE.md fragment must distinguish: "for your content, search `kb/`; for how the system works, search `commonplace/kb/`."

## Variants

**Commonplace repo:** No distinction between content and methodology questions — everything is in `kb/notes/`. A question about "how do types work?" and "what are the design principles?" search the same directory.

**Installed project:** The agent must distinguish content questions (search `kb/`) from methodology questions (search `commonplace/kb/`). The CLAUDE.md fragment handles this routing.

**Depth variation:** Simple factual questions ("what did we decide about X?") may need only steps 1-3 (2-4 hops total). Complex synthesis questions ("what's the relationship between X and Y?") exercise the full chain including step 4 (5-9 hops total).
