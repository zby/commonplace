---
description: Step-by-step decomposition of the ingest-a-source scenario — skill-orchestrated, most steps mediated by /ingest which chains snapshot, connect, classify, and analyse
type: scenario
frequency: occasional
---

# Ingest a source

User provides a URL or document to capture and analyse. The agent uses the /ingest skill which orchestrates a multi-phase pipeline: snapshot the source, connect it to existing knowledge, classify its relevance, and produce a structured analysis.

## Steps

### 1. Route to /ingest skill
- **Context needed:** Skill descriptions — which skill handles source ingestion
- **Source:** `CLAUDE.md`
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** CLAUDE.md is always loaded. The skills table maps "External source snapshot" to `/snapshot-web` and "Source analysis" to `/ingest`.

### 2. Load /ingest skill
- **Context needed:** Full skill procedure for orchestrating ingestion
- **Source:** `skills/ingest/SKILL.md`
- **Hops:** 1
- **Fixed/Variable:** fixed
- **Notes:** The skill body contains the complete orchestration procedure: snapshot → connect → classify → analyse.

### 3. Snapshot the source
- **Context needed:** /snapshot-web skill procedure + URL
- **Source:** `skills/snapshot-web/SKILL.md` + external URL
- **Hops:** 1 (skill) + 1 (URL fetch)
- **Fixed/Variable:** mixed — skill is fixed, URL is variable
- **Notes:** /ingest delegates to /snapshot-web for capture. The URL fetch is external (not a file read), but it's a hop in terms of agent tool calls.

### 4. Read source type definition
- **Context needed:** Structure for source-review documents
- **Source:** `kb/sources/types/source-review.md`
- **Hops:** 1
- **Fixed/Variable:** fixed
- **Notes:** Small file (~500 bytes). Defines the template for source reviews: Key Points, Relevance, Open Questions.

### 5. Find related notes
- **Context needed:** Existing KB content related to the source's topic
- **Source:** variable — search results from `kb/notes/`
- **Hops:** 1 (search) + 2-3 (read results)
- **Fixed/Variable:** variable
- **Notes:** Same as write-a-note step 2. The agent searches for notes that the source extends, contradicts, or grounds.

### 6. Write structured extraction
- **Context needed:** Snapshotted content + source-review template + related notes context
- **Source:** — (agent produces output)
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** No additional reads. The agent writes the `.ingest.md` file using everything loaded in steps 1-5.

### 7. Connect to existing knowledge
- **Context needed:** /connect skill body, area indexes
- **Source:** `skills/connect/SKILL.md` + variable (area indexes)
- **Hops:** 1 (skill) + 1-3 (indexes and search)
- **Fixed/Variable:** mixed — skill is fixed, index reads are variable
- **Notes:** Same as write-a-note step 7. The ingest skill invokes /connect to weave the new source review into the knowledge graph.

## Escalation path (installed projects only)

### E1. Recognize unusual source format
- **Context needed:** Awareness that the skill procedure may not cover all source formats
- **Source:** `CLAUDE.md` (fragment in installed project)
- **Hops:** 0
- **Fixed/Variable:** fixed
- **Notes:** Current skills don't explicitly signal when escalation is needed. The agent must recognise that the standard extraction template doesn't fit.

### E2. Search methodology for source handling guidance
- **Context needed:** Full reasoning behind source classification and extraction
- **Source:** `commonplace/kb/notes/` (search results)
- **Hops:** 1 (search) + 1-2 (read results)
- **Fixed/Variable:** variable
- **Notes:** The agent searches commonplace for notes about document classification, source types, or extraction methodology.

## Variants

**Commonplace repo:** Escalation is seamless — methodology notes are in the same `kb/notes/` the agent already searches. The /ingest skill is the template version (in `skills/`), not a rendered version.

**Installed project:** The /ingest skill is rendered into `.claude/skills/` with project-specific paths. Escalation adds 2-3 hops but is rare — most sources fit the standard extraction template.

**Source type variation:** Academic papers, blog posts, GitHub issues, and X/Twitter posts each have different capture methods (handled by /snapshot-web) but the analysis pipeline is the same. The variable cost is in step 3 (capture method) not in steps 4-7.
