---
description: "Discovery report for possible KB connections from one source artifact"
type: connect-report
source: "{repo-root source path}"
source_has_frontmatter: {true|false}
date: "{YYYY-MM-DD}"
depth: standard
---

# Connection Report: {source title}

**Source:** [{source title}]({relative source link})

## Discovery Trace

**Index scan:**
- Read [notes index](../../notes/dir-index.md) -- flagged candidates: {candidates with reasons}

**Topic indexes:**
- {topic index reads and candidates, or "None"}

**Semantic search:** {via qmd | grep-only fallback}
- query "{actual query}" -- top hits:
  - [candidate](../../notes/candidate.md) ({score}) -- {evaluation}

**Keyword search:**
- rg "{actual query}" -- {results and evaluation}

**Link following:**
- {candidate neighborhoods traversed and what they revealed}

## Connections Found

- [target](../../notes/target.md) -- **extends**: {specific reason why this connection exists}

## Bidirectional Candidates

- [target](../../notes/target.md) <-> source -- **contradicts**: {reason the return path is also useful}

## Raw Text Candidates

- [text-file](../../notes/text-file.md) -- potential **extends**: {reason this text is relevant}

## Rejected Candidates

- [rejected](../../notes/rejected.md) -- {reason rejected}

## Index Membership

- [index-name](../../notes/index-name.md) -- {what the source would contribute to this area}

## Synthesis Opportunities

{Two or more notes that together imply a higher-order claim not yet captured, or "None"}

## Flags

- {split candidates, tensions, no-connections finding, or "None"}
