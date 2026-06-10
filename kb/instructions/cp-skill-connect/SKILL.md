---
name: cp-skill-connect
description: Discover connections for a single artifact. Writes a connect-report under kb/reports/connect/<collection>/ without mutating library artifacts or indexes. Use with an artifact path or artifact name.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
---

# Connect — Discovery Only

Find candidate connections for a single artifact and write them to a **discovery report** at `kb/reports/connect/<collection>/<artifact-name>.connect.md`. The report is the only direct write this skill performs. Do not edit the source artifact, other artifacts, indexes, collection files, or logs.

Connect reports are gitignored; they are immediate downstream context and can be regenerated from the source artifact plus current KB state.

The skill owns execution. The type owns the report contract.
Use this skill for routing, setup, tool use, delegated skill calls, and file writes.
Use the loaded type spec for section meanings, quality standards, and the template.
If the skill and type both mention the same report-content rule, prefer the type.

## Input

Target: `$ARGUMENTS` — one artifact path or artifact name. If none provided, ask which artifact to connect. Determine the source **collection** from the artifact's path (`kb/notes/` -> notes, `kb/reference/` -> reference, etc.).

## Setup

1. Determine the source collection from the target artifact's path (`kb/notes/...` -> `notes`, `kb/reports/foo.md` -> `reports`, etc.). **Hard fail immediately if `kb/<source-collection>/COLLECTION.md` does not exist** — do not attempt discovery, do not fall back to defaults, do not soldier on. Report the missing file path to the user and stop. The COLLECTION.md is the only linking-rules surface; without it the skill has no authorised destinations or labels and any output would be invented.
2. Read `kb/reports/types/connect-report.md` before candidate discovery. It defines the report sections, quality standards, and template you will use while judging candidates.
3. Read the target artifact fully. Identify its claim, mechanism, implications, scope, and tensions. If the target has no frontmatter (`text` file), continue discovery from its title/body and mark the report as provisional.
4. Read `kb/<source-collection>/COLLECTION.md` and find its **outbound-linking section** (heading varies — look for the one that names destinations and labels). Read it as authoritative guidance — extract three things, regardless of whether the section is structured as per-destination blocks, a single labels table with a destinations column, prose, or any mix:
   - **Which destination collections to prospect from this source** (and which are excluded).
   - **Which labels are authorised for which source->destination pairs**, with the reader-need each label serves.
   - **Any direction or composition hints** — inverse-edge expectations, rare/common edges, frontloading posture, sub-agent invocation preferences. The skill below leans on these for reverse-edge candidates and for tightening prospecting on rare edges.

   This is the only linking-rules surface. There is no compiled topology and no separate vocabulary doc to consult.
5. Treat the installed KB goals from always-loaded `AGENTS.md` as an outer scope check, not as a replacement for collection label authorisation. `kb/reference/control-plane-goals.md` documents this always-loaded goal-frame invariant, including forked skill contexts, so connect does not add a separate goal-loading step.
6. Use repo-local discovery only: curated indexes, scoped `rg`, and link following. Do not call external semantic-search tools or MCP search services; connect must work in Codex without external search state. Complete generated listings (`dir-index.md`, tag tails) are build-time site artifacts and do not exist in the repo (ADR 025).

## Discovery — per destination

Connect is the skill that pays the cost of active search. The write skill is bounded to a targeted duplicate check + already-loaded context + user-named targets; connect runs the full prospecting procedure on every destination the source's `COLLECTION.md` permits.

Active depth: **standard** (quick: index-only single pass; deep: full discovery, multiple passes, synthesis detection).

Capture discovery trace throughout — indexes read, actual query strings, candidate evaluations, and links followed. A trace with only keywords is insufficient.

For **each** destination collection authorised by the source's outbound section:

### 1. Decide breadth from the source COLLECTION.md's guidance

Use the outbound section's triggers, latitude cues, and direction hints to set prospecting breadth. If the source has no plausible match for a destination's trigger, note that in the trace and skip that destination.

### 2. Prospect using repo-local tools

In order of cost:

- **Curated heads.** Read the destination's `README.md` and, when the source carries `tags:`, the matching `<tag>-README.md` pages — their editorial groupings and context phrases capture routing signal a flat listing misses. If a tag-README declares `complete: true`, it links every note carrying that tag — **skip the by-tag rg for that tag** and record the skip in the discovery trace.
- **Scoped `rg` description listing.** Enumerate candidates at path + description resolution without loading a complete index:

  ```bash
  # whole destination
  rg '^description:' kb/<destination>/ --glob '*.md'
  # by tag
  rg -l '^tags:.*\bTAG\b' kb/<destination>/ --glob '*.md' \
    | xargs -r rg -N --no-heading '^description:\s*' -r ''
  ```

  The `xargs -r` guard matters: a tag matching zero files would otherwise make `rg` search the whole repo.
- **`rg` body search.** Run focused queries for terms and adjacent concepts the source's claim foregrounds and the destination's outbound guidance suggests. Multiple queries; capture the actual query strings.

  ```bash
  rg -n "term" kb/<destination>/ --glob "*.md"
  ```

- **Link following.** From promising candidates, follow their existing links one hop, then re-filter. Look for clusters and chains the source should join.

### 3. Articulation test

Every candidate must complete: `[source] connects to [target] because [specific reason].` Keep the candidate only if an agent, or another intended KB consumer named by the collection contract, gains something concrete by following the link. The KB goal frame filters whether a plausible candidate is worth surfacing at all; candidate acceptance still depends on the articulation test and authorised labels.

### 4. Label the candidate from the destination's authorised set

Each authorised label carries a reader-need; pick the one whose reader-need matches the candidate connection's purpose, and record both label and a one-line context phrase in the report. The labels the source's outbound section authorises **for this specific destination** are the only options — do not propose labels outside that set. (Labels often appear in a single table with a destinations column; filter to rows whose destinations include the current target collection.)

If a candidate passes the articulation test but **no authorised label fits**, it is either off-scope or a signal that the collection author should extend the authorisation. Move it to **Off-authorisation Candidates** in the report. Do not invent a label or downgrade to `see-also` to make it fit.

The label and context phrase are recorded *in the report* — connect does not write them anywhere else.

### Honour collection-specific posture

Some `COLLECTION.md` files declare global postures that constrain prospecting beyond the per-label rules. Examples to respect when present:

- **Frontloading** — outbound is exceptional. Do not propose broad `see-also` sprays from frontloaded collections; terms an executing consumer needs should be present in the artifact, not only linked.
- **Excluded destinations** — a collection may explicitly say "do not link into X" (commonly `kb/work/`). Don't surface candidates from excluded destinations even if they pass the articulation test.

Read these from the outbound section before prospecting, not after.

## Reverse-edge candidates

Not every useful link is authored from the source side. When the useful direction is inbound, prospect for artifacts elsewhere that should link to this target under their own `COLLECTION.md` rules. Surface those as Reverse-edge Candidates; do not edit the other artifacts.

The source COLLECTION.md often flags this directly — language like "the usual direction is inverse" or "primary edge is authored from another collection" tells you to look for reverse edges from the named direction. When such a hint is present, treat reverse-edge prospecting as a first-class pass for that destination, not an afterthought.

The skill does **not** edit those source artifacts or write draft links from them. It names the candidate reverse edges so the author of the source artifact (or a future connect run on the source) can decide whether to author the link.

## Authored surfaces

Snapshots in `kb/sources/` are immutable; their authored connection surface is normally the matching `.ingest.md`. For other non-authored artifacts, use the authored companion named by the collection contract, if one exists. If none exists, keep the suggestion in the connect report.

## Output

Save the report to `kb/reports/connect/<source-collection>/<artifact-name>.connect.md`. Use the loaded `kb/reports/types/connect-report.md` template and file-relative markdown links in the body. Tell the user: `Report saved: <full path>`.

Every section describes **candidate** signal for a future writer to act on. The connect skill does not author any of these edges into any artifact — the report is the entire connection deliverable.

- Verify every candidate path exists before including it.
- Write `None` for empty sections.
- Put traversal issues and durable follow-up signals in the report's `Maintenance Observations` section, not in a side file.

## Constraints

**Never** edit the target artifact, other artifacts, indexes, collection files, logs, or any library artifact — the report is the *only* connection output the skill produces. Every section is a candidate signal for future authoring, not committed state.

**Never** add "related" connections without specific reasoning. **Never** force connections — if no genuine connections exist, say so honestly. **Never** propose a label outside the destination's authorised set; route those to Off-authorisation Candidates.

**Always** capture discovery trace per destination. **Always** verify candidate paths exist before including them. **Always** read the source `COLLECTION.md`'s outbound-linking section before prospecting — it is the only authoritative linking-rules surface, regardless of how that section is internally structured.

## Maintenance observations

Use `Maintenance Observations` for report-local traversal observations that are not connection candidates. This is a best-effort signal inside a gitignored, regenerable report. A later explicit maintenance or triage step may promote entries from this section into durable local artifacts; connect does not do that promotion.
