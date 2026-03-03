# Quality Gates

## Gate 1: Articulation Test

For every connection in the report, can you complete:
> [A](kb/notes/a.md) connects to [B](kb/notes/b.md) because [specific reason]

If any connection fails this test, remove it from the report.

## Gate 2: Candidate Verification

Verify every candidate note path actually exists:

```bash
ls "path/to/candidate.md" 2>/dev/null
```

Never include connections to non-existent files in the report.

## Gate 3: No Forced Connections

If nothing genuine was found, say so. An honest "no connections found" report is better than weak connections that waste the reader's time.

---

# Edge Cases

## No Connections Found

Sometimes a note genuinely does not connect yet. Report this honestly.

Note in the report:
- Which indexes were checked
- Which searches returned nothing relevant
- Whether the note might belong to an area index even without direct note-to-note connections

## Too Many Connections (Split Detection)

If a note connects to 5+ notes across different domains, it might be too broad.

**Split detection criteria:**

1. **Domain spread:** Connections span 3+ distinct topic areas
2. **Multiple claims:** The note makes more than one assertion that could stand alone
3. **Linking drag:** You would want to link to part of the note but not all of it

Flag in the report with proposed split — do not act on it.

**When NOT to flag:**
- Note is genuinely about one thing that touches many areas
- Connections are all variations of the same relationship
- Splitting would create notes too thin to stand alone

## Conflicting Notes

When the target note contradicts an existing note:

1. Flag the tension in the report
2. Note which index Tensions section it belongs in
3. Do not resolve — flag for judgment

## Orphan Discovery

If you encounter notes with no connections during search:

1. Flag them in the report
2. Do not attempt to connect them — that's a separate `/connect` run
