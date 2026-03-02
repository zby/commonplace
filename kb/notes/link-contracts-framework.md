---
description: Reference framework for systematic, testable linking — link contracts, intent taxonomy, automated checks, agent implications
type: note
traits: [has-external-sources]
areas: [links]
status: current
---

# Link contracts framework — source material

Framework for systematic, testable linking in knowledge bases. Received 2026-02-21.
Saved as reference for when we start building concrete link practices.

See [agents-navigate-by-deciding-what-to-read-next](./agents-navigate-by-deciding-what-to-read-next.md) and
[two-kinds-of-navigation](./two-kinds-of-navigation.md) for the distilled observations.

---

## Every link needs to earn a "click decision"

When a reader encounters a link, they're silently asking:

1. **What is it?** (definition, how-to, API docs, evidence, discussion, example…)
2. **Why should I click now?** (what problem it helps with)
3. **What will it cost?** (time, depth, complexity)
4. **How trustworthy/current is it?** (official doc vs random blog; last updated)
5. **What happens if I don't click?** (optional background or required to proceed?)

Goal: make those answers cheap. That's the "link contract."

## Link contract: minimal information

### Inline link (minimum bar)

* Descriptive anchor text (not "here" / "this")
* Local context explaining why it matters

### Annotated link (high-performing pattern)

Short "decision hint" next to the link: what it is + why + cost.

* "See **SLO policy** (canonical definition, 4–6 min)."
* "Background: **CAP theorem** (conceptual, 8 min)."
* "Evidence: **Postmortem 2024-09-12** (why we changed the retry logic)."

## Link intent taxonomy

* **Definition**: explains a term used here
* **How-to / Procedure**: steps to do something
* **Reference**: authoritative source of truth
* **Example**: concrete instance / sample
* **Rationale / Decision**: why we do it this way
* **Evidence**: data, incident report, research paper
* **Tool**: dashboard, repo, script, UI
* **Related**: nearby topic, optional expansion
* **Index / Hub**: navigation page

Once links have intent, you can enforce rules:

* Every new term must link to a Definition once
* Every instruction must link to a How-to or include steps
* Every strong claim should link to Evidence or be labeled as assumption

## Making link decisions obvious

* Put optional links where they don't interrupt flow (parenthetical, footnote, end-of-section)
* Use "when to click" language: "If you're implementing this, see…"
* Avoid ambiguous anchors — name the destination
* Group links by intent when there are many

## Index page quality bar

* Purpose, scope, how to use it
* Each link has a one-line description
* Optional: tags (audience, difficulty, time, type)

## LLM/agent implications

Agents do constrained exploration. If links carry intent and cost:

* Prefer Reference/Evidence when verifying claims
* Prefer How-to when executing tasks
* Prefer Rationale when asked "why"
* Skip Background when time/context is tight
* Use Index/Hub as starting points

## Automated tests for linking

### Deterministic

* Broken links / redirects
* Banned anchors ("here", "this", "link")
* Link density thresholds
* External link labeling

### LLM rubric

* Does every link have clear purpose in surrounding text?
* Could a reader predict what they'll get from clicking?
* Are required dependencies hidden behind unlabeled links?

### Corpus compatibility

* New term → links to canonical definition
* Strong claim → links to evidence or marked as assumption
* Index entries → one-line descriptions exist
* Orphan detection

## Five rules that work

1. Never use "here/this" as anchor text
2. Every link gets a "why/when" hint
3. Group links by intent
4. Index pages must describe each link in one line
5. If something is required to proceed, summarize it — don't outsource to a link

Topics:
- [links](./links.md)
