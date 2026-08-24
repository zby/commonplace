---
description: Ground one requested primary-source claim and append it through the ingest-owned mutation path
type: kb/types/instruction.md
---

# Ground a source-dependent claim

**Target:** exact repo-relative ingest path or canonical source URL.

**Claim needed:** source-side proposition or question. Do not include target
prose or a target-specific transfer argument.

This instruction may reuse or add an entry. It never edits the target or an
existing Claims entry.

## Procedure

1. Read the source collection and ingest type contracts.
2. Resolve one ingest. For a URL with no ingest, invoke `cp-skill-ingest` on the
   exact URL and use its validated result. Stop on ambiguity.
3. Read the complete Claims section. If an entry answers `Claim needed`, return
   its exact `Claim (paraphrase)` wording without mutation.
4. Derive `kb/sources/.snapshots/<slug>.md` from
   `kb/sources/<slug>.ingest.md` and require its SHA-256 to equal the ingest's
   `snapshot_sha256`. Do not search for a differently named checksum match. If
   the named file is absent or mismatched, stop with the literal re-ingest route:
   - source checkout: `Read and execute kb/instructions/re-ingest.md with Target: <ingest-path>.`
   - installed project: `Read and execute kb/commonplace/instructions/re-ingest.md with Target: <ingest-path>.`
5. Require the snapshot frontmatter's canonical `source` to equal the ingest's
   `source`. Read enough of this primary snapshot to determine the claim and
   its bounds. Stop if the request depends on a secondary resource or the
   source does not establish it.
6. Construct one entry:

   ```markdown
   - **Claim (paraphrase):** <bounded source-side proposition>
     - **Source extract (verbatim):** <exact supporting content>
     - **Source location:** <human-resolvable locator for that extract>
     - **Scope:** <population, conditions, and exclusions>
     - **Confidence:** <scoped prose>
     - **Limitation:** <boundary needed to prevent overstatement>
   ```

   Repeat the adjacent extract/location pair when support is non-contiguous.
   Line wrapping is not non-contiguity: verbatim matching normalizes
   whitespace, so one extract may span wrapped lines. Quote the whole
   contiguous span rather than one fragment per line — a `pdftotext` snapshot
   wraps mid-sentence, and fragmenting on those breaks makes the entry unreadable
   for the `source` review lens without making it any more verifiable.
   Verify every extract against the snapshot. `commonplace-validate` performs
   this check when the ingest skill appends your entry, so a wrong extract
   fails there rather than landing; quote the snapshot's bytes as they are
   instead of repairing capture artifacts as you copy.
7. Invoke `cp-skill-ingest` with:

   ```yaml
   claim_append_request:
     ingest_path: <exact ingest path>
     snapshot_path: <name-paired, checksum-matching snapshot path>
     entry: |-
       <complete entry>
   ```

   The ingest skill rechecks identity and checksum, verifies extracts, replaces
   the canonical empty sentence on a first append, and mechanically appends the
   entry without changing incumbent entries or other sections. It then
   validates. Do not write the ingest directly or repair a failed append
   outside that skill.
8. Return the ingest path, `reused` or `added`, and the exact normalized claim
   wording a writer should prefer.

Semantic uniqueness is not required. A similar, broader, narrower, or disputed
entry is never merged, rewritten, or deleted by this procedure.
