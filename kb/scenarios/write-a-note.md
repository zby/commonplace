---
description: Step-by-step decomposition of the write-a-note scenario with file references for cost measurement — the most step-rich common scenario, 7 steps plus escalation
type: scenario
frequency: common
---

# Write a note

User asks the agent to capture an insight, design observation, or analysis as a KB note. The agent must route to the correct location, find related notes, understand the type structure and writing conventions, write the note, and connect it to existing knowledge.

## Steps

### 1. Route to correct location
- **Context needed:** Routing table — what goes where
- **Source:** `CLAUDE.md`
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** CLAUDE.md is always loaded. The routing table tells the agent `kb/notes/` for design notes, `kb/notes/adr/` for decisions, etc.

### 2. Find related notes
- **Context needed:** Search patterns, good descriptions on existing notes
- **Source:** variable — search results from `kb/notes/`
- **Hops:** 1 (search) + 2-4 (read results)
- **Fixed/Variable:** variable
- **Notes:** The search itself is one hop. Reading results depends on how many relevant notes exist. Estimate 3 results at ~2000 bytes each for typical topics.

### 3. Read related notes
- **Context needed:** Full content of related notes for understanding context
- **Source:** variable — specific notes from search results
- **Hops:** 0 (already read in step 2)
- **Fixed/Variable:** variable
- **Notes:** Counted in step 2. Listed separately because it's a distinct cognitive step — the agent shifts from searching to understanding.

### 4. Know the structure
- **Context needed:** Type template for the target note type
- **Source:** `kb/WRITING.md`
- **Hops:** 1
- **Fixed/Variable:** fixed
- **Notes:** WRITING.md inlines the two global types (note, structured-claim). Directory-local types (adr, index, related-system) require an additional hop to `kb/notes/types/`. For the common case (note or structured-claim), one hop suffices.

### 5. Know how to write well
- **Context needed:** Writing conventions — title-as-claim, description quality, composability
- **Source:** `kb/WRITING.md`
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** Same file as step 4 — already loaded. WRITING.md serves double duty: type templates and writing conventions.

### 6. Write the file
- **Context needed:** All of the above in context
- **Source:** — (agent produces output)
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** No additional reads. The agent writes using everything loaded in steps 1-5.

### 7. Connect to existing knowledge
- **Context needed:** /connect skill body, area indexes
- **Source:** `skills/connect/SKILL.md` + variable (area indexes)
- **Hops:** 1 (skill) + 1-3 (indexes and search)
- **Fixed/Variable:** mixed — skill is fixed, index reads are variable
- **Notes:** The connect step is a separate skill invocation. The skill body is substantial (~15KB). Index reads depend on how many areas the note touches.

## Escalation path (installed projects only)

### E1. Recognize the gap
- **Context needed:** Awareness that full methodology reasoning exists
- **Source:** `CLAUDE.md` (fragment in installed project)
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** The CLAUDE.md fragment includes an escalation hint: "for why things work this way, search `commonplace/kb/`". Always loaded.

### E2. Search methodology
- **Context needed:** Full reasoning behind a convention
- **Source:** `commonplace/kb/notes/` (search results)
- **Hops:** 1 (search) + 1-2 (read results)
- **Fixed/Variable:** variable
- **Notes:** The agent searches the commonplace repo's notes for the reasoning behind whatever convention it's struggling with.

### E3. Read source reasoning
- **Context needed:** The specific methodology note
- **Source:** variable — e.g. `commonplace/kb/notes/title-as-claim-enables-traversal-as-reasoning.md`
- **Hops:** 0 (already read in E2)
- **Fixed/Variable:** variable
- **Notes:** Counted in E2. The agent now has the full reasoning and can apply judgment.

### E4. Return to common path
- **Context needed:** Continue with the write
- **Source:** — (back in `kb/`)
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** No additional reads. The agent returns to step 6 or 7 with deeper understanding.

## Variants

**Commonplace repo:** Escalation steps E1-E4 don't exist. The methodology notes ARE the content the agent searches in step 2. When writing a note about, say, title conventions, the agent naturally encounters the full reasoning because it lives in the same `kb/notes/` directory.

**Installed project (common path):** Steps 1-7 are identical — the copied operational artifacts (WRITING.md, types/) ensure the paths are the same. The agent doesn't know or care whether it's in commonplace or an installed project.

**Installed project (escalation):** Adds 2-3 hops to a different tree. Estimated to occur ~10% of the time — most writes don't hit edge cases requiring full methodology reasoning.

**Directory-local types:** When the target type is adr, index, or related-system, step 4 requires an additional hop to `kb/notes/types/{type}.md`. This adds 1 hop for ~20% of writes.
