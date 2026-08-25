---
name: cp-skill-ground
description: Ground one source-side claim by retaining the minimum verbatim quotes in its ingest, or declare that the pinned snapshot is required. Use when a note needs source support or when asked to retain quotes; never call cp-skill-ingest for that.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "Target: <ingest path or canonical source URL>; Claim needed: <source-side proposition or question>"
---

# Ground a source-dependent claim

`$ARGUMENTS` supplies both inputs. Stop and ask if either is missing.

**Target:** exact repo-relative ingest path or canonical source URL.

**Claim needed:** source-side proposition or question. Do not include target
prose or a target-specific transfer argument.

This skill may reuse or append verbatim quotes. It never edits the
target artifact or interprets a paraphrase stored in an ingest as source
support.

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
7. For the bounded-quotes route, invoke `cp-skill-ingest` with:

   ```yaml
   quote_append_request:
     ingest_path: <exact ingest path>
     snapshot_path: <name-paired, checksum-matching snapshot path>
     quotes: |-
       <one or more complete quote items>
   ```

   The ingest skill rechecks identity and checksum, verifies every verbatim
   quote, replaces the canonical empty sentence on a first append, and
   mechanically appends without changing incumbent quotes or other sections.
   It then validates. Do not write the ingest directly or repair a failed
   append outside that skill.
8. Return the ingest path and exactly one route: `quotes sufficient`, `quotes
   added`, or `snapshot required`. For `quotes added`, also return the appended
   quote texts. For `snapshot required`, repeat the exact link-text marker and
   the requirement to run `semantic/grounding-alignment` before the source
   claim lands.

Semantic uniqueness is not required. Similar, overlapping, or disputed exact
passages are never merged, rewritten, or deleted by this procedure.
