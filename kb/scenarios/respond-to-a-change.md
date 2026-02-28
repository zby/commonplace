---
description: Step-by-step decomposition of the respond-to-a-change scenario — chains reading (assemble evidence) with writing (compose response), the most complex occasional scenario with escalation possible during either phase
type: scenario
frequency: occasional
---

# Respond to a change

User notices an upstream change (PR, RFC, API update) or has a design idea, and asks the agent to analyse it against existing knowledge and write a grounded response. This chains the answer-a-question scenario (assemble evidence) with the write-a-note scenario (compose response), making it the most complex scenario.

## Steps

### 1. Understand the change
- **Context needed:** The change itself — PR description, RFC text, or user explanation
- **Source:** variable — external URL or user message
- **Hops:** 0-1 (0 if user explains, 1 if URL fetch needed)
- **Fixed/Variable:** variable
- **Notes:** The change may be provided inline or as a URL requiring a fetch.

### 2. Route to correct search scope
- **Context needed:** Routing table, search patterns
- **Source:** `CLAUDE.md`
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** Always loaded. The agent needs to know which areas of the KB are relevant to this change.

### 3. Search for related evidence
- **Context needed:** KB notes that inform the response — prior decisions, design rationale, relevant analysis
- **Source:** variable — search results from `kb/notes/`, `kb/sources/`
- **Hops:** 1 (search)
- **Fixed/Variable:** variable
- **Notes:** One search hop. The agent looks for notes that constrain, inform, or provide evidence for the response.

### 4. Read evidence notes
- **Context needed:** Full content of relevant notes
- **Source:** variable — specific notes from search results
- **Hops:** 3-5 (read results)
- **Fixed/Variable:** variable
- **Notes:** More reads than answer-a-question because the agent needs not just understanding but quotable evidence. Prior ADRs, structured claims, and source reviews are especially valuable.

### 5. Follow links for deeper grounding
- **Context needed:** Notes linked from evidence that strengthen the argument
- **Source:** variable — notes referenced by links in step 4
- **Hops:** 1-3 (follow links)
- **Fixed/Variable:** variable
- **Notes:** The agent follows links to find the full reasoning chain. A structured claim's evidence section may reference other notes that provide the actual data.

### 6. Read writing conventions
- **Context needed:** How to write the response document — type template, quality conventions
- **Source:** `kb/WRITING.md`
- **Hops:** 1
- **Fixed/Variable:** fixed
- **Notes:** Needed if the response is a KB note (analysis, ADR). May be skipped if the response is a PR comment or external message — but even then, the grounding conventions apply.

### 7. Write the response
- **Context needed:** All evidence and conventions in context
- **Source:** — (agent produces output)
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** No additional reads. The agent composes the response grounded in the evidence assembled in steps 3-5.

### 8. Connect the response (if KB note)
- **Context needed:** /connect skill body, area indexes
- **Source:** `skills/connect/SKILL.md` + variable (area indexes)
- **Hops:** 1 (skill) + 1-3 (indexes and search)
- **Fixed/Variable:** mixed — skill is fixed, index reads are variable
- **Notes:** Only applies when the response is a KB note (analysis document, ADR). Skipped for external outputs (PR comments, messages).

## Escalation path (installed projects only)

### E1. Evidence assembly escalation
- **Context needed:** When KB evidence is thin, full methodology reasoning may provide additional grounding
- **Source:** `commonplace/kb/notes/` (search results)
- **Hops:** 1 (search) + 1-2 (read results)
- **Fixed/Variable:** variable
- **Notes:** Triggers when the agent can't find enough evidence in `kb/` to ground the response. The methodology notes may contain design reasoning that applies.

### E2. Response structure escalation
- **Context needed:** When the response doesn't fit standard types
- **Source:** `commonplace/kb/notes/` (search results)
- **Hops:** 1 (search) + 1 (read)
- **Fixed/Variable:** variable
- **Notes:** Triggers when the response is a complex document type (e.g. a multi-claim analysis that doesn't fit the standard note or ADR template).

## Variants

**Commonplace repo:** No escalation needed — the methodology IS the content. Responding to a change about, say, how types should work naturally involves reading the methodology notes about types.

**Installed project:** Escalation can trigger during either the evidence assembly phase (steps 3-5) or the response composition phase (steps 6-7). Two distinct escalation points make this the most expensive scenario when escalation occurs.

**Output type variation:** The response may be a KB note (full write-a-note connection step), a PR comment (no connection needed, but grounding conventions still apply), or an external message (minimal formatting). Steps 6 and 8 vary accordingly.
