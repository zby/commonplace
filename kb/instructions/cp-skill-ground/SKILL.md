---
name: cp-skill-ground
description: Ground one source-side claim by retaining the minimum verbatim quotes in its ingest, or declare that the pinned snapshot is required. Use when a note needs source support or when asked to retain quotes; never call cp-skill-ingest for that.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "Target: <ingest path or canonical source URL>; Claim needed: <source-side proposition or question>"
---

# Ground a source-dependent claim

`$ARGUMENTS` supplies both inputs. Stop and ask if either is missing.

**Target:** exact repo-relative ingest path or canonical source URL.

**Claim needed:** source-side proposition or question. Do not include target
prose or a target-specific transfer argument.

This skill may reuse or append verbatim quotes and is the only procedure
that writes an ingest's Quotes section. It never edits the target artifact,
never changes any other part of an ingest, and never interprets a paraphrase
stored in an ingest as source support.

## Procedure

1. Read the source collection and ingest type contracts.
2. Resolve one ingest. For a URL with no ingest, invoke `cp-skill-ingest` on the
   exact URL and use its validated result. Stop on ambiguity.
3. Read the complete `## Quotes` section. Judge the requested source-side
   proposition directly against its retained `Source extract (verbatim)`
   values. Ignore the ingest's Summary, Connections Found, Extractable Value,
   and Limitations as support.
   - If the retained quotes are sufficient, return the ingest path and
     `quotes sufficient` without mutation.
   - If they are insufficient, continue. Do not infer the answer from an ingest
     paraphrase or analysis.
4. Derive `kb/sources/.snapshots/<slug>.md` from
   `kb/sources/<slug>.ingest.md`. Require that exact file to exist, require its
   exact-byte SHA-256 to equal the ingest's `snapshot_sha256`, and require its
   frontmatter `source` to equal the ingest's canonical `source`. Do not search
   for a differently named checksum match. If any check fails, stop with the
   literal re-ingest route:
   - source checkout: `Read and execute kb/instructions/re-ingest.md with Target: <ingest-path>.`
   - installed project: `Read and execute kb/commonplace/instructions/re-ingest.md with Target: <ingest-path>.`
5. Read enough of the primary snapshot to determine the source-side
   proposition and its bounds. Stop if the source does not establish it or the
   request depends on a secondary resource.
6. Choose the smallest sound retained form:
   - If one or a few bounded excerpts let a later reviewer judge the
     proposition without missing material context, construct one or more
     adjacent quote items in this exact shape:

     ```markdown
     - **Source extract (verbatim):** <exact supporting content>
       - **Source location:** <human-resolvable locator for that extract>
     ```

     Repeat the complete pair when support is non-contiguous. Line wrapping is
     not non-contiguity: verbatim matching normalizes whitespace. Copy the
     snapshot's text exactly and retain only the minimum passages needed for a
     sound check.
   - If sound checking depends on broad or distributed context that should not
     be retained as a bounded set of quotes, do not append a substitute
     paraphrase or an oversized extract. Return `snapshot required` and tell
     the writer to include the exact marker `(snapshot required)` in the ingest
     link text. The source claim must pass `semantic/grounding-alignment` while
     the verified snapshot is present.
7. For the bounded-quotes route, append the items yourself:
   - Retain the ingest's complete incumbent bytes. Construct a candidate by
     splicing only within the `## Quotes` section, using the incumbent file's
     newline convention: when the section body is exactly
     `No source quotes have been retained yet.`, replace only that sentence;
     otherwise insert the new items after all incumbent items and before the
     next level-two heading, adding only the separator newlines valid adjacent
     items need. Preserve every incumbent item and every byte outside the
     section. Do not merge, deduplicate, reorder, or reword anything.
   - Recheck the paired paths, source identity, and checksum against the
     current bytes, write the candidate once, then run
     `commonplace-validate kb/sources/<slug>.ingest.md`. The validator resolves
     each `Source extract (verbatim)` against the name-paired snapshot and
     fails on one that does not occur; that check, not your own reading, is
     the verification — an agent checking text it just transcribed confirms
     its own copy. Earlier grounding runs produced false extracts by silently
     repairing capture artifacts (line-break hyphenation, an inline footnote
     marker, a LaTeX arrow); quote the snapshot's bytes as they are.
   - Re-read the result and require the intended splice plus exact
     preservation of all other bytes. If any post-write check or validation
     fails, restore the retained incumbent bytes exactly, verify that
     restoration, and report failure rather than leaving an invalid or partial
     append. A `source quote` failure is about the item, not the splice: fix
     the extract against the snapshot, never rewrite the file around it.
     A `populated Quotes section conflicts` failure identifies stale prose
     outside Quotes. Restore the incumbent and report that non-quote prose must
     be repaired before grounding is retried; this skill must not repair it.
8. Return the ingest path and exactly one route: `quotes sufficient`, `quotes
   added`, or `snapshot required`. For `quotes added`, also return the appended
   quote texts. If validation warned that a populated Quotes section coexists
   with `(snapshot required)`, repeat that warning so the caller verifies that
   the marker still belongs to a claim needing broader snapshot context. For
   `snapshot required`, repeat the exact link-text marker and the requirement
   to run `semantic/grounding-alignment` before the source claim lands.

Semantic uniqueness is not required. Similar, overlapping, or disputed exact
passages are never merged, rewritten, or deleted by this procedure.
