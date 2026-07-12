---
description: Ingest a directory of related files (e.g. a cloned code repository) as a single source unit, producing one coherent `.ingest.md` that cites evidence across files.
type: kb/types/instruction.md
---

# Ingest a directory

**Target: $ARGUMENTS** — path to a directory containing the source material (typically under `tmp/` or `kb/work/<workshop>/`, both gitignored). Do not place cloned repos under `kb/sources/` — that directory is tracked and the `.ingest.md` is the only artifact per source that belongs there.

If no target, ask the user for a directory path.

**Slug.** The slug is the basename of the input directory path — e.g. `tmp/position-bias/` → slug `position-bias`. The ingest report is always written to `kb/sources/<slug>.ingest.md`, regardless of where the source directory lives.

## When to use

- The source is a tree of related files, not a single document — most commonly a cloned code repository, but also a paper plus supplementary material, or a grouped set of related snapshots.
- Cross-file signal matters: the README claims X and a test file measures X; the README alone would not carry the same evidentiary weight.

For single-file sources, use `/cp-skill-ingest` instead.

## Prerequisites

- The directory exists at the given input path and contains the source material. Cloning the repo or downloading the files is out of scope — do it beforehand, into a gitignored location (e.g. `tmp/<slug>/`).
- `kb/sources/COLLECTION.md` exists (required by the connect skill invoked in Step 5, which runs against the ingest report that lands in `kb/sources/`).

## Step 1: Explore the directory

Run `ls` and inspect the tree shape. Classify files into categories:

- **Thesis / intent** — README, top-level docs, project description
- **Implementation** — main code files, entry points, core modules
- **Validation** — tests, evaluations, benchmarks, example runs
- **Artifacts** — prompts, datasets, configs, experimental parameters
- **Output** — results files, logs, figures (if committed)

Ignore: vendored dependencies (`node_modules/`, `.venv/`), lockfiles, compiled artifacts, `.git/`, generated docs.

## Step 2: Select important files

Pick a bounded set (typically 5–15 files) to read in full. Bias toward load-bearing files, not completeness.

Explicitly include-or-skip each of these categories:

- README / top-level docs — usually include
- 1-3 core implementation files that carry the central claim — include
- Tests or evaluations for the central claim — include if the source's trustworthiness rests on "the code runs"
- Prompts, datasets, or configs that define what the system actually does — include if the source is an LLM artifact
- Individual demos or examples — usually skip unless the demo IS the claim
- Aggregate results / outputs (CSVs, result tables, figures) — **include when the repo is a data publication** (findings are the contribution; the code is scaffolding). Skip when the repo is a software tool (outputs are throwaway artifacts of running it).
- Vendored, generated, or build-artifact files — skip

Record your selection as a one-line justification per file; this becomes the File Manifest in Step 4.

## Step 3: Read the selected files

Read each selected file in full. Form a composite understanding:

- What is the source's central claim or contribution?
- What evidence does the tree carry for that claim (code, tests, data)?
- What claims in the README are not supported by code or tests in the tree?
- What is the source's scope — what does it NOT claim or cover?

## Step 4: Write a draft ingest report

Write to `kb/sources/<slug>.ingest.md`, where `<slug>` is the basename of the input directory (e.g. input `tmp/position-bias/` → output `kb/sources/position-bias.ingest.md`). Fill **only** Classification, Summary, and File Manifest. Leave the four connect-informed sections (Connections Found, Extractable Value, Limitations, Recommended Next Action) as the literal string `TO BE FILLED`.

**Do not pre-draft the four placeholder sections even though Step 3 gave you the material to write them.** The point of deferring them is that the connect pass in Step 5 reshapes what counts as "new" (Extractable Value should exclude anything the KB already captures) and surfaces tensions (Limitations often cites KB notes the agent hasn't considered). Pre-drafting forces a rewrite and loses the filter connect provides.

Draft frontmatter:

```yaml
---
description: {one-line retrieval filter — what makes this source distinctive}
source_snapshot: {input-directory-path, e.g. tmp/<slug>/}
ingested: "{current UTC date}"
type: kb/sources/types/ingest-report.md
domains: [{tag1}, {tag2}, {tag3}]
---
```

Note: `source_snapshot` points to the working copy, which is typically gitignored and ephemeral. The Pin line below (commit hash) is the canonical identifier for reproducibility.

Genre normally lives on the source snapshot (`genre` in snapshot frontmatter, vocabulary in `kb/sources/types/snapshot.md`), but a directory ingest has no snapshot artifact — the genre (normally `code-repository`) appears only in the Classification section's prose line. If the directory is not a code repo (e.g. paper + supplements), pick the closest genre from the snapshot type spec's vocabulary; an off-list value is a deliberate extension, not an error.

Draft body:

```markdown
# Ingest: {repo or project name}

Source: {input-directory-path} (ephemeral; see Pin)
Captured: {date from README/git if known}
From: {upstream URL if known, e.g. GitHub repo URL}
Pin: {commit hash if known, else "unpinned — captured HEAD at <date>"}

## Classification
Genre: code-repository — {brief justification, e.g. "working eval harness with ~N tests"}
Domains: {tag1}, {tag2}, {tag3}
Author: {credibility signal, or "unknown"}

## Summary
{one paragraph — central claim and how the tree supports it}

## File Manifest
Files read in full:
- `path/to/file1.md` — {one-line justification}
- `path/to/file2.py` — {one-line justification}
- ...

## Connections Found
TO BE FILLED

## Extractable Value
TO BE FILLED

## Limitations (our opinion)
TO BE FILLED

## Recommended Next Action
TO BE FILLED
```

## Step 5: Run connect on the draft

Invoke `/cp-skill-connect kb/sources/<slug>.ingest.md`.

Connect reads the draft (Classification + Summary + File Manifest carry enough signal for prospecting) and writes its report to `kb/reports/connect/sources/<slug>.ingest.connect.md`.

Wait for the skill to complete before proceeding.

## Step 6: Revise the ingest report using connect output

Read the connect report. Replace the four `TO BE FILLED` sections.

The connect report is generated, gitignored working context. Do not cite it, link
to it, or name its path in the durable ingest report; summarize its findings and
link only durable KB artifacts, source snapshots, or source files identified in
the File Manifest.

**Relative-link depth.** Links you author here are written from `kb/sources/<slug>.ingest.md`. Use `../notes/…`, `../reference/…`, `../agent-memory-systems/…`, `./<other-source>.md` for sibling sources. Candidate artifact links copied from the connect report may be at the wrong depth, so rewrite paths relative to the ingest report.

**Connections Found** — summarise which notes the source connects to, relationship types, and the key insight about how this source fits (or doesn't) into the KB graph.

**Extractable Value** — 3–7 items, each with an effort tag (`[quick-win]`, `[experiment]`, `[deep-dive]`, `[just-a-reference]`). Focus on what is NEW relative to the connections found. For a code repository specifically, look for:

- Empirical findings the code produces (cite the test or eval file)
- Methods or experimental designs adaptable to our work
- Prompts, benchmarks, or datasets worth reusing
- Claims in the README that the code does NOT support (trustworthiness gap)

Assess reach — does the finding transfer beyond this specific benchmark, model set, or domain? Flag low-reach items.

**Limitations (our opinion)** — code-repository checks:

- Did the agent verify the code runs, or only read it? State which.
- Missing baselines, restricted model sets, cherry-picked benchmarks
- README claims not backed by code or tests in the tree
- Single-author / single-team context — would the result transfer?
- Unpinned repo state — the analysis rots as the repo evolves; the Pin line above should record the commit or capture date

**Recommended Next Action** — one specific action (new note with title, update to existing note, brainstorm topic, file as reference).

## Verify

- `kb/sources/<slug>.ingest.md` exists and has no `TO BE FILLED` markers.
- File Manifest entries match the files actually read in Step 3.
- Every relative link in Connections Found resolves.
- Frontmatter passes schema validation (with the enum extension applied).

Tell the user where the report was saved and the recommended next action.

## Do NOT

- Do not extract atomic claims from individual files — this is ingestion, not decomposition.
- Do not write files under `kb/notes/`, `kb/reference/`, or `kb/instructions/`. The deliverable is the `.ingest.md` only.
- Do not modify files inside the source directory.
- Do not skip Step 5 — connect results are load-bearing for Connections Found and Extractable Value.
- Do not run `/cp-skill-connect` on each selected file individually; one pass on the draft ingest-report is the design.
